"""
fetch_pdf.py
============
Auto-fetch open-access PDF files for every publication and wire the local path
into _data/sources.yaml (the file the cite.py pipeline reads), so the /pubs page
can show a "PDF" button — same idea as the feamster/publications repo, which
keeps a local copy of each paper's PDF.

Strategy:
  * Read every DOI from _data/citations.yaml (the full publication list).
  * For each DOI, ask Unpaywall for the best open-access PDF and download it to
    pdf/<doi-stem>.pdf  (e.g. 10.3390/app13063937 -> pdf/app13063937.pdf, the
    same naming scheme already used by the existing PDFs in pdf/).
  * Merge the result into sources.yaml WITHOUT touching existing entries: an
    entry that already has a `pdf` button is left exactly as-is (preserves the
    hand-curated images and manual PDF links); otherwise a `pdf` button is added
    to the existing entry, or a new entry is appended.

Only open-access papers can be downloaded automatically. Paywalled IEEE /
Elsevier / Springer papers with no OA copy are reported as "no OA PDF" and must
be added by hand (drop the file in pdf/ and add a button in sources.yaml).

After running this script, re-run `python _cite/cite.py` so the new PDF paths
propagate to _data/citations.yaml and appear on the site.

Usage (plain Python 3.9+ with the packages installed):
    python _cite/fetch_pdf.py
    python _cite/fetch_pdf.py --limit 5 --dry-run   # test on a few, no writes
"""

# /// script
# requires-python = ">=3.9"
# dependencies = ["requests", "pyyaml"]
# ///

import re
import sys
import time
import pathlib
import argparse
import yaml
import requests

# ── Paths (relative to project root) ────────────────────────────────────────
SCRIPT_DIR    = pathlib.Path(__file__).parent.resolve()
ROOT          = SCRIPT_DIR.parent          # one level up from _cite/
# cite.py reads _data/sources.yaml -> generates _data/citations.yaml.
# citations.yaml is the full publication list; sources.yaml is where the
# per-paper buttons/images live and is the only file we write to here.
CITATIONS_YAML = ROOT / "_data" / "citations.yaml"
SOURCES_YAML   = ROOT / "_data" / "sources.yaml"
PDF_DIR        = ROOT / "pdf"

# ── Config ──────────────────────────────────────────────────────────────────
# Unpaywall requires a contact email in every request.
UNPAYWALL_EMAIL = "infolab@skku.edu"
UNPAYWALL_API   = "https://api.unpaywall.org/v2/{}?email=" + UNPAYWALL_EMAIL

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/pdf,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
# Seconds to wait between papers (be polite to Unpaywall / publishers)
REQUEST_DELAY = 1.0
# Timeout per HTTP request (seconds)
TIMEOUT = 30
# Reject anything larger than this (likely not a paper PDF)
MAX_PDF_BYTES = 80 * 1024 * 1024  # 80 MB


def load_yaml(path: pathlib.Path) -> list:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def save_yaml(path: pathlib.Path, data: list) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False,
                  allow_unicode=True)


def pdf_stem(doi: str) -> str:
    """
    DOI -> local PDF filename stem. Uses the whole DOI suffix (everything after
    the registrant prefix), not just the last path segment, so multi-slash DOIs
    stay unique — e.g. the Research Square preprints 10.21203/rs.3.rs-49216/v1
    and 10.21203/rs.3.rs-8614100/v1 would both collapse to "v1" otherwise.
    For the common single-slash DOI this is identical to the scheme already used
    by the existing files in pdf/  (10.3390/app13063937 -> app13063937,
    10.1016/j.knosys.2020.106688 -> j_knosys_2020_106688).
    """
    suffix = doi.split("/", 1)[1] if "/" in doi else doi
    return re.sub(r"[^A-Za-z0-9-]", "_", suffix)


def has_pdf_button(entry: dict) -> bool:
    for b in entry.get("buttons") or []:
        if isinstance(b, dict) and b.get("type") == "pdf":
            return True
    return False


def unpaywall_pdf_url(doi: str) -> str | None:
    """Return the best open-access PDF URL for a DOI, or None."""
    try:
        resp = requests.get(UNPAYWALL_API.format(doi), headers=HEADERS,
                            timeout=TIMEOUT)
        if resp.status_code != 200:
            return None
        data = resp.json()
        # Prefer best_oa_location, then fall back to any OA location with a PDF.
        locs = []
        best = data.get("best_oa_location")
        if best:
            locs.append(best)
        locs.extend(data.get("oa_locations") or [])
        for loc in locs:
            url = (loc or {}).get("url_for_pdf")
            if url:
                return url
        return None
    except Exception:
        return None


def download_pdf(url: str, dest: pathlib.Path) -> bool:
    """Download url -> dest, only if it is a real PDF. Returns True on success."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, stream=True,
                            allow_redirects=True)
        if resp.status_code != 200:
            return False
        ctype = resp.headers.get("content-type", "").lower()
        # Stream first chunk and verify the PDF magic number, because many
        # publisher "pdf" URLs actually return an HTML interstitial.
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
                    f.close()
                    dest.unlink(missing_ok=True)
                    return False
                f.write(chunk)
        if dest.stat().st_size < 1024:  # < 1 KB = junk
            dest.unlink(missing_ok=True)
            return False
        return True
    except Exception:
        return False


def main(limit: int = 0, dry_run: bool = False):
    if not CITATIONS_YAML.exists():
        sys.exit(f"ERROR: {CITATIONS_YAML} not found. Run from the project root.")
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    citations = load_yaml(CITATIONS_YAML)
    sources   = load_yaml(SOURCES_YAML)

    # Index existing sources by lower-cased DOI id so we can merge in place.
    by_id = {}
    for entry in sources:
        _id = (entry.get("id") or "").strip().lower()
        if _id:
            by_id[_id] = entry

    # Unique DOIs from the full publication list, in order.
    seen = set()
    dois = []
    for c in citations:
        _id = (c.get("id") or "").strip()
        if _id.lower().startswith("doi:") and _id.lower() not in seen:
            seen.add(_id.lower())
            dois.append(_id)

    if limit > 0:
        dois = dois[:limit]
        print(f"[--limit {limit}] Processing first {len(dois)} DOIs only.")

    print(f"Checking {len(dois)} DOIs against {len(sources)} sources.yaml "
          f"entries...")
    if dry_run:
        print("[dry-run] No files or YAML will be written.\n")

    n_have = n_downloaded = n_missing = n_skipped = 0

    for doi_id in dois:
        doi   = doi_id.replace("doi:", "").replace("DOI:", "").strip()
        entry = by_id.get(doi_id.lower())

        # Already wired up -> leave it completely alone.
        if entry and has_pdf_button(entry):
            n_skipped += 1
            continue

        stem     = pdf_stem(doi)
        dest     = PDF_DIR / f"{stem}.pdf"
        rel_path = f"pdf/{stem}.pdf"

        print(f"  [{doi}]", end="", flush=True)

        if dest.exists():
            # PDF is already on disk (downloaded earlier or named by convention):
            # just wire up the button, no network needed.
            print(f"  on disk -> {rel_path}")
            n_have += 1
        else:
            url = unpaywall_pdf_url(doi)
            time.sleep(REQUEST_DELAY)
            if not url:
                print("  -> no OA PDF")
                n_missing += 1
                continue
            if dry_run:
                print(f"  -> [dry-run] would download {url[:60]}")
                n_downloaded += 1
                continue
            if download_pdf(url, dest):
                print(f"  -> saved {rel_path}")
                n_downloaded += 1
            else:
                print(f"  -> download failed ({url[:50]})")
                n_missing += 1
                continue

        if dry_run:
            continue

        button = {"type": "pdf", "link": rel_path}
        if entry:
            # Add the PDF button to the existing entry, preserving image etc.
            entry.setdefault("buttons", []).append(button)
        else:
            new_entry = {"id": doi_id, "image": "", "buttons": [button]}
            sources.append(new_entry)
            by_id[doi_id.lower()] = new_entry

    print(f"\nSummary: {n_skipped} already wired, {n_have} found on disk, "
          f"{n_downloaded} downloaded, {n_missing} with no OA PDF.")

    if dry_run:
        print("[dry-run] Nothing written.")
        return

    if n_have or n_downloaded:
        save_yaml(SOURCES_YAML, sources)
        print(f"Updated {SOURCES_YAML}.")
        print("Next: python _cite/cite.py   (propagate to citations.yaml)")
    else:
        print("No PDFs added; sources.yaml unchanged.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-fetch open-access paper PDFs")
    parser.add_argument("--limit", type=int, default=0,
                        help="Process only the first N DOIs (0 = all)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Find PDFs but don't download or save")
    args = parser.parse_args()
    main(limit=args.limit, dry_run=args.dry_run)
