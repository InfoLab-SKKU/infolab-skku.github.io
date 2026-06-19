"""
fetch_pdf_subscription.py
=========================
Companion to fetch_pdf.py for the publications that have NO open-access copy
(Unpaywall returns nothing) but ARE reachable through the institution's paid
subscriptions. Run this from a machine on the campus network so the requests
carry the university's IP-based entitlement.

Two tiers:
  Tier 1 (default, requests-based):
    * GET https://doi.org/<doi> to reach the publisher landing page, then read
      the publisher's own <meta name="citation_pdf_url"> tag (most publishers
      expose it) — this is the canonical PDF URL.
    * Fall back to well-known per-publisher direct-PDF URL patterns
      (Springer / Wiley / ACM / Taylor & Francis / PLOS).
  Tier 2 (--browser, Selenium):
    * For publishers that block plain HTTP clients with a JS/Cloudflare
      challenge (IEEE Xplore, Elsevier ScienceDirect), drive a real Chrome that
      passes the challenge under the campus session and auto-downloads the PDF.

Same conventions as fetch_pdf.py: PDFs go to pdf/<doi-stem>.pdf and a `pdf`
button is merged into _data/sources.yaml without disturbing existing entries.
After running, re-run `python _cite/cite.py` (or push and let CI rebuild).

Usage:
    python _cite/fetch_pdf_subscription.py                 # Tier 1
    python _cite/fetch_pdf_subscription.py --browser        # Tier 2 (IEEE/Elsevier)
    python _cite/fetch_pdf_subscription.py --limit 5 --dry-run
"""

# /// script
# requires-python = ">=3.9"
# dependencies = ["requests", "pyyaml", "beautifulsoup4", "selenium"]
# ///

import re
import sys
import time
import pathlib
import argparse
import yaml
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Reuse paths / helpers from the sibling OA fetcher.
sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()))
from fetch_pdf import (ROOT, CITATIONS_YAML, SOURCES_YAML, PDF_DIR, HEADERS,
                       TIMEOUT, MAX_PDF_BYTES, load_yaml, save_yaml, pdf_stem,
                       has_pdf_button)

REQUEST_DELAY = 2.0  # be gentle with publisher sites

# Publishers that reliably block plain HTTP clients — skip in Tier 1, do in Tier 2.
BROWSER_ONLY_PREFIXES = ("10.1109", "10.1016")


def landing_url(doi: str) -> str | None:
    """Follow the DOI to the publisher landing page; return its final URL + html."""
    try:
        r = requests.get(f"https://doi.org/{doi}", headers=HEADERS,
                        timeout=TIMEOUT, allow_redirects=True)
        if r.status_code == 200:
            return r
    except Exception:
        pass
    return None


def meta_pdf_url(resp) -> str | None:
    """Read <meta name="citation_pdf_url"> from a landing-page response."""
    try:
        soup = BeautifulSoup(resp.text, "html.parser")
        tag = soup.find("meta", attrs={"name": "citation_pdf_url"})
        if tag and tag.get("content", "").strip():
            return urljoin(resp.url, tag["content"].strip())
    except Exception:
        pass
    return None


def direct_candidates(doi: str) -> list[str]:
    """Per-publisher direct-PDF URL patterns (used as a fallback)."""
    p = doi.split("/")[0]
    c = []
    if p in ("10.1007", "10.1186", "10.1140"):           # Springer family
        c.append(f"https://link.springer.com/content/pdf/{doi}.pdf")
    if p == "10.1145":                                    # ACM
        c.append(f"https://dl.acm.org/doi/pdf/{doi}")
    if p in ("10.1002", "10.1111", "10.1155"):            # Wiley (Hindawi=Wiley now)
        c.append(f"https://onlinelibrary.wiley.com/doi/pdfdirect/{doi}?download=true")
    if p == "10.1080":                                    # Taylor & Francis
        c.append(f"https://www.tandfonline.com/doi/pdf/{doi}?download=true")
    if p == "10.1371":                                    # PLOS
        c.append(f"https://journals.plos.org/plosone/article/file?id={doi}&type=printable")
    return c


def download_pdf(url: str, dest: pathlib.Path, referer: str | None = None) -> bool:
    """Download url -> dest only if it is a real PDF (verifies %PDF magic)."""
    headers = dict(HEADERS)
    if referer:
        headers["Referer"] = referer
    try:
        resp = requests.get(url, headers=headers, timeout=TIMEOUT, stream=True,
                            allow_redirects=True)
        if resp.status_code != 200:
            return False
        ctype = resp.headers.get("content-type", "").lower()
        it = resp.iter_content(8192)
        first = next(it, b"")
        if not first.startswith(b"%PDF") and "application/pdf" not in ctype:
            return False
        size = len(first)
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as f:
            f.write(first)
            for chunk in it:
                size += len(chunk)
                if size > MAX_PDF_BYTES:
                    dest.unlink(missing_ok=True)
                    return False
                f.write(chunk)
        if dest.stat().st_size < 1024:
            dest.unlink(missing_ok=True)
            return False
        return True
    except Exception:
        return False


def remaining_dois(citations, sources):
    """DOIs in the publication list that still have no PDF button."""
    wired = set()
    for s in sources:
        if has_pdf_button(s):
            wired.add((s.get("id") or "").strip().lower())
    out, seen = [], set()
    for c in citations:
        _id = (c.get("id") or "").strip()
        low = _id.lower()
        if (low.startswith("doi:") and low not in seen and low not in wired
                and not has_pdf_button(c)):
            seen.add(low)
            out.append(_id)
    return out


def wire_up(sources, by_id, doi_id, rel_path):
    button = {"type": "pdf", "link": rel_path}
    entry = by_id.get(doi_id.lower())
    if entry:
        entry.setdefault("buttons", []).append(button)
    else:
        entry = {"id": doi_id, "image": "", "buttons": [button]}
        sources.append(entry)
        by_id[doi_id.lower()] = entry


def tier1(limit=0, dry_run=False):
    citations = load_yaml(CITATIONS_YAML)
    sources   = load_yaml(SOURCES_YAML)
    by_id = {(e.get("id") or "").strip().lower(): e for e in sources if e.get("id")}
    dois = remaining_dois(citations, sources)
    dois = [d for d in dois
            if not d.replace("doi:", "").startswith(BROWSER_ONLY_PREFIXES)]
    if limit:
        dois = dois[:limit]
    print(f"Tier 1: {len(dois)} subscription DOIs to try "
          f"(IEEE/Elsevier deferred to --browser).")
    got = miss = 0
    for doi_id in dois:
        doi  = doi_id.replace("doi:", "").strip()
        dest = PDF_DIR / f"{pdf_stem(doi)}.pdf"
        rel  = f"pdf/{pdf_stem(doi)}.pdf"
        print(f"  [{doi}]", end="", flush=True)
        if dest.exists():
            print("  on disk")
            if not dry_run:
                wire_up(sources, by_id, doi_id, rel)
            got += 1
            continue
        # 1) citation_pdf_url meta on the landing page
        pdf_url, ref = None, None
        resp = landing_url(doi)
        if resp is not None:
            ref = resp.url
            pdf_url = meta_pdf_url(resp)
        # 2) direct per-publisher patterns
        cands = ([pdf_url] if pdf_url else []) + direct_candidates(doi)
        ok = False
        for cand in cands:
            if not cand:
                continue
            if dry_run:
                print(f"  -> [dry-run] candidate {cand[:70]}")
                ok = True
                break
            if download_pdf(cand, dest, referer=ref or f"https://doi.org/{doi}"):
                print(f"  -> saved {rel}  (via {cand[:50]})")
                wire_up(sources, by_id, doi_id, rel)
                ok = True
                break
        if ok:
            got += 1
        else:
            print("  -> no subscription PDF")
            miss += 1
        time.sleep(REQUEST_DELAY)
    print(f"\nTier 1 summary: {got} obtained, {miss} failed.")
    if got and not dry_run:
        save_yaml(SOURCES_YAML, sources)
        print(f"Updated {SOURCES_YAML}. Next: re-merge into citations.yaml.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--browser", action="store_true",
                    help="Tier 2: Selenium for IEEE/Elsevier (not yet wired here)")
    args = ap.parse_args()
    if args.browser:
        sys.exit("Tier 2 (Selenium) runs via fetch_pdf_browser.py — see that script.")
    tier1(limit=args.limit, dry_run=args.dry_run)
