"""
fetch_thumbs.py
===============
Auto-fetch Open Graph thumbnail images for publications that have an empty
`image:` field in _cite/papers.yaml.

Strategy (applied in order until one succeeds):
  1. Open Graph  — follow the DOI URL, scrape the publisher page og:image
  2. Semantic Scholar — query the S2 Graph API for an openAccessPdf cover
  3. Crossref      — check for a thumbnail link in Crossref metadata

Usage (from project root or _cite/ directory):
    python _cite/fetch_thumbs.py

Requirements (install if missing):
    pip install requests beautifulsoup4 pyyaml
"""

import os
import re
import sys
import time
import pathlib
import yaml
import requests
from urllib.parse import urlparse, urljoin

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("ERROR: beautifulsoup4 not installed. Run: pip install beautifulsoup4")

# ── Paths (relative to project root) ────────────────────────────────────────
SCRIPT_DIR   = pathlib.Path(__file__).parent.resolve()
ROOT         = SCRIPT_DIR.parent  # one level up from _cite/
PAPERS_YAML  = SCRIPT_DIR / "papers.yaml"
CITES_YAML   = ROOT / "_data" / "citations.yaml"
THUMB_DIR    = ROOT / "images" / "thumbnails"

# ── Config ──────────────────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; InfoLabThumbBot/1.0; "
        "+https://infolab-skku.github.io)"
    )
}
# Seconds to wait between HTTP requests (be polite to publishers)
REQUEST_DELAY = 1.5
# Max image file size to download (bytes)  — skip huge files
MAX_IMAGE_BYTES = 5 * 1024 * 1024  # 5 MB
# Timeout per HTTP request (seconds)
TIMEOUT = 10


def load_yaml(path: pathlib.Path) -> list:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def save_yaml(path: pathlib.Path, data: list) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def safe_filename(doi: str) -> str:
    """Convert a DOI string to a safe filename stem."""
    return re.sub(r"[^a-zA-Z0-9_\-]", "_", doi)[:120]


def download_image(url: str, dest: pathlib.Path) -> bool:
    """Download an image from url → dest. Returns True on success."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, stream=True)
        if resp.status_code != 200:
            return False
        content_type = resp.headers.get("content-type", "")
        if "image" not in content_type and "octet" not in content_type:
            return False
        size = 0
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(4096):
                size += len(chunk)
                if size > MAX_IMAGE_BYTES:
                    return False
                f.write(chunk)
        return dest.stat().st_size > 1024  # at least 1 KB
    except Exception:
        return False


# ── Strategy 1: Open Graph scraping ─────────────────────────────────────────

def try_open_graph(doi: str) -> str | None:
    """
    Follow the DOI redirect to the publisher page, then scrape the og:image
    meta tag. Returns an absolute image URL or None.
    """
    doi_url = f"https://doi.org/{doi}"
    try:
        resp = requests.get(doi_url, headers=HEADERS, timeout=TIMEOUT,
                            allow_redirects=True)
        if resp.status_code != 200:
            return None
        soup = BeautifulSoup(resp.text, "html.parser")
        # Try og:image first, then twitter:image
        for prop in ("og:image", "twitter:image"):
            tag = soup.find("meta", property=prop) or soup.find("meta", attrs={"name": prop})
            if tag and tag.get("content"):
                img_url = tag["content"].strip()
                # Make absolute if relative
                if not img_url.startswith("http"):
                    img_url = urljoin(resp.url, img_url)
                return img_url
        return None
    except Exception:
        return None


# ── Strategy 2: Semantic Scholar ────────────────────────────────────────────

def try_semantic_scholar(doi: str) -> str | None:
    """
    Query the Semantic Scholar API. S2 doesn't return cover images directly,
    but if there's a direct PDF link we can skip and rely on the OG strategy.
    Returns None (reserved for future S2 cover image support).
    """
    return None  # Placeholder — S2 does not currently expose cover images


# ── Strategy 3: Crossref ────────────────────────────────────────────────────

def try_crossref(doi: str) -> str | None:
    """
    Fetch Crossref metadata and look for a link with content-type image/*.
    """
    url = f"https://api.crossref.org/works/{doi}"
    try:
        resp = requests.get(url, headers={**HEADERS, "Accept": "application/json"},
                            timeout=TIMEOUT)
        if resp.status_code != 200:
            return None
        data = resp.json().get("message", {})
        for link in data.get("link", []):
            ct = link.get("content-type", "")
            if "image" in ct:
                return link.get("URL")
        return None
    except Exception:
        return None


# ── Main ────────────────────────────────────────────────────────────────────

def fetch_thumbnails():
    THUMB_DIR.mkdir(parents=True, exist_ok=True)

    # Load both files
    papers   = load_yaml(PAPERS_YAML)
    cites    = load_yaml(CITES_YAML)

    # Build a set of DOIs that already have images in citations.yaml
    has_image = {
        c["id"]: c.get("image", "")
        for c in cites
        if c.get("image", "").strip()
    }

    # Find papers.yaml entries that still need images
    to_fetch = []
    for entry in papers:
        doi_id = entry.get("id", "")
        if not doi_id.startswith("doi:"):
            continue
        if entry.get("image", "").strip():
            continue                 # already has an image override
        if has_image.get(doi_id, "").strip():
            continue                 # already has image in citations.yaml
        to_fetch.append(entry)

    if not to_fetch:
        print("All papers already have thumbnail images. Nothing to do.")
        return

    print(f"Fetching thumbnails for {len(to_fetch)} papers...")
    updated = 0

    for entry in to_fetch:
        doi_id  = entry["id"]
        doi     = doi_id.replace("doi:", "").strip()
        stem    = safe_filename(doi)
        print(f"  [{doi}]", end="", flush=True)

        img_url = None

        # Strategy 1: OG image from publisher page
        img_url = try_open_graph(doi)
        if img_url:
            print(f" OG→{img_url[:60]}", end="", flush=True)
        time.sleep(REQUEST_DELAY)

        # Strategy 2: Crossref (if OG failed)
        if not img_url:
            img_url = try_crossref(doi)
            if img_url:
                print(f" XRef→{img_url[:60]}", end="", flush=True)
            time.sleep(REQUEST_DELAY)

        if not img_url:
            print(" no image found")
            continue

        # Derive file extension from URL
        parsed_path = urlparse(img_url).path
        ext = pathlib.Path(parsed_path).suffix.lower()
        if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
            ext = ".jpg"

        dest = THUMB_DIR / f"{stem}{ext}"
        rel_path = f"images/thumbnails/{stem}{ext}"

        if dest.exists():
            print(f" already downloaded → {rel_path}")
            entry["image"] = rel_path
            updated += 1
            continue

        ok = download_image(img_url, dest)
        if ok:
            entry["image"] = rel_path
            updated += 1
            print(f" saved → {rel_path}")
        else:
            print(" download failed")

    if updated:
        save_yaml(PAPERS_YAML, papers)
        print(f"\nDone. Updated {updated} image path(s) in {PAPERS_YAML}.")
        print("Re-run `python _cite/cite.py` to regenerate citations.yaml.")
    else:
        print("\nNo new thumbnails could be downloaded.")


if __name__ == "__main__":
    fetch_thumbnails()
