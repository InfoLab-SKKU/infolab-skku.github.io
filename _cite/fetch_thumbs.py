"""
fetch_thumbs.py
===============
Auto-fetch Open Graph thumbnail images for publications that have an empty
`image:` field in _data/sources.yaml (the file the cite.py pipeline reads).

Strategy (applied in order until one succeeds):
  1. Open Graph  — follow the DOI URL, scrape the publisher page og:image
  2. Crossref    — check for a thumbnail link in Crossref metadata
  3. Unpaywall   — find the open-access version (arXiv, PMC, etc.) and scrape its og:image

After running this script, re-run `python _cite/cite.py` so the new image
paths propagate to `_data/citations.yaml` and appear on the site.

Usage (requires uv — already installed with this project):
    uv run --with requests --with beautifulsoup4 --with pyyaml _cite/fetch_thumbs.py

Or with a plain Python 3.9+ that has the packages installed:
    python _cite/fetch_thumbs.py
"""

# /// script
# requires-python = ">=3.9"
# dependencies = ["requests", "beautifulsoup4", "pyyaml"]
# ///

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
    sys.exit("ERROR: beautifulsoup4 not installed.  Run: pip install beautifulsoup4")

# ── Paths (relative to project root) ────────────────────────────────────────
SCRIPT_DIR   = pathlib.Path(__file__).parent.resolve()
ROOT         = SCRIPT_DIR.parent          # one level up from _cite/
# cite.py reads _data/sources.yaml → generates _data/citations.yaml.
# We update sources.yaml so new image paths reach the pipeline.
SOURCES_YAML = ROOT / "_data" / "sources.yaml"
THUMB_DIR    = ROOT / "images" / "thumbnails"

# ── Config ──────────────────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
CROSSREF_HEADERS = {
    "User-Agent": "InfoLabThumbBot/1.0 (mailto:infolab@skku.edu)",
    "Accept": "application/json",
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
        yaml.dump(data, f, default_flow_style=False, sort_keys=False,
                  allow_unicode=True)


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


# Generic/branding images to skip (not paper-specific)
_GENERIC_IMAGE_PATTERNS = (
    "logo", "icon", "favicon", "placeholder",
    "card-share", "share.jpg", "share.png",
    "og-default", "default-og", "site-image",
    "pmc-card", "pubmed-logo", "nih-logo",
    "opengraph/img",    # DOAJ generic OG image
    "assets/img/og",    # site-level OG assets
    "/og-image.",       # generic og-image filenames
    "default-image",
)

def try_open_graph(doi: str) -> str | None:
    """
    Follow the DOI redirect to the publisher page and scrape og:image/twitter:image.
    Returns an absolute image URL or None.
    """
    doi_url = f"https://doi.org/{doi}"
    try:
        resp = requests.get(doi_url, headers=HEADERS, timeout=TIMEOUT,
                            allow_redirects=True)
        if resp.status_code != 200:
            return None
        soup = BeautifulSoup(resp.text, "html.parser")
        # Try standard OG and Twitter card image tags
        for prop in ("og:image", "og:image:url", "twitter:image", "twitter:image:src"):
            tag = (soup.find("meta", property=prop)
                   or soup.find("meta", attrs={"name": prop}))
            if tag and tag.get("content", "").strip():
                img_url = tag["content"].strip()
                if not img_url.startswith("http"):
                    img_url = urljoin(resp.url, img_url)
                # Skip generic logo/icon images from major publishers
                low = img_url.lower()
                if any(s in low for s in _GENERIC_IMAGE_PATTERNS):
                    continue
                return img_url
        return None
    except Exception:
        return None


# ── Strategy 2: Crossref ────────────────────────────────────────────────────

def try_crossref(doi: str) -> str | None:
    """
    Fetch Crossref metadata and look for a link with content-type image/*.
    Also checks the 'cover-image' field some publishers provide.
    """
    url = f"https://api.crossref.org/works/{doi}"
    try:
        resp = requests.get(url, headers=CROSSREF_HEADERS, timeout=TIMEOUT)
        if resp.status_code != 200:
            return None
        data = resp.json().get("message", {})
        # Check cover image field
        covers = data.get("cover-image") or data.get("cover")
        if covers:
            first = covers[0] if isinstance(covers, list) else covers
            url_ = first.get("URL") if isinstance(first, dict) else first
            if url_ and url_.startswith("http"):
                return url_
        # Check link entries for image content types
        for link in data.get("link", []):
            ct = link.get("content-type", "")
            if "image" in ct:
                return link.get("URL")
        return None
    except Exception:
        return None


# ── Strategy 3: Unpaywall → preprint OG image ───────────────────────────────

def try_unpaywall(doi: str) -> str | None:
    """
    Use Unpaywall to find the open-access landing page (often arXiv, PMC, or an
    institutional repo), then scrape OG images from that page.
    These preprint pages tend to allow scraping unlike publisher sites.
    """
    url = f"https://api.unpaywall.org/v2/{doi}?email=infolab@skku.edu"
    try:
        resp = requests.get(url, headers=CROSSREF_HEADERS, timeout=TIMEOUT)
        if resp.status_code != 200:
            return None
        data = resp.json()
        # Collect candidate OA URLs (best first)
        oa_urls = []
        best = data.get("best_oa_location") or {}
        if best.get("url_for_landing_page"):
            oa_urls.append(best["url_for_landing_page"])
        for loc in data.get("oa_locations", []):
            u = loc.get("url_for_landing_page") or loc.get("url")
            if u and u not in oa_urls:
                oa_urls.append(u)
        # Try each OA page for an OG image
        for oa_url in oa_urls[:3]:
            try:
                r2 = requests.get(oa_url, headers=HEADERS, timeout=TIMEOUT,
                                  allow_redirects=True)
                if r2.status_code != 200:
                    continue
                soup = BeautifulSoup(r2.text, "html.parser")
                for prop in ("og:image", "twitter:image"):
                    tag = (soup.find("meta", property=prop)
                           or soup.find("meta", attrs={"name": prop}))
                    if tag and tag.get("content", "").strip():
                        img_url = tag["content"].strip()
                        if not img_url.startswith("http"):
                            img_url = urljoin(r2.url, img_url)
                        low = img_url.lower()
                        if any(s in low for s in _GENERIC_IMAGE_PATTERNS):
                            continue
                        return img_url
            except Exception:
                continue
        return None
    except Exception:
        return None

def fetch_thumbnails(limit: int = 0, dry_run: bool = False):
    """
    limit: if > 0, only process the first N papers (useful for testing)
    dry_run: if True, find image URLs but don't download or save anything
    """
    THUMB_DIR.mkdir(parents=True, exist_ok=True)

    if not SOURCES_YAML.exists():
        sys.exit(f"ERROR: {SOURCES_YAML} not found. Run from the project root.")

    sources = load_yaml(SOURCES_YAML)

    # Find entries that need images
    to_fetch = [
        (i, entry) for i, entry in enumerate(sources)
        if entry.get("id", "").startswith("doi:")
        and not entry.get("image", "").strip()
    ]

    if not to_fetch:
        print("All papers already have thumbnail images. Nothing to do.")
        return

    if limit > 0:
        to_fetch = to_fetch[:limit]
        print(f"[--limit {limit}] Testing first {len(to_fetch)} papers only.")

    print(f"Fetching thumbnails for {len(to_fetch)} papers "
          f"(out of {len(sources)} total in sources.yaml)...")
    if dry_run:
        print("[dry-run] Will not download or save anything.\n")
    updated = 0

    for i, entry in to_fetch:
        doi_id = entry["id"]
        doi    = doi_id.replace("doi:", "").strip()
        stem   = safe_filename(doi)
        print(f"  [{doi}]", end="", flush=True)

        img_url = None

        # Strategy 1: OG image from publisher page
        img_url = try_open_graph(doi)
        if img_url:
            print(f"  OG -> {img_url[:70]}", end="", flush=True)
        time.sleep(REQUEST_DELAY)

        # Strategy 2: Crossref cover/image links
        if not img_url:
            img_url = try_crossref(doi)
            if img_url:
                print(f"  Crossref -> {img_url[:70]}", end="", flush=True)
            time.sleep(REQUEST_DELAY)

        # Strategy 3: Unpaywall OA landing page OG image
        if not img_url:
            img_url = try_unpaywall(doi)
            if img_url:
                print(f"  Unpaywall -> {img_url[:70]}", end="", flush=True)
            time.sleep(REQUEST_DELAY)

        if not img_url:
            print("  -> no image found")
            continue

        if dry_run:
            print(f"  -> [dry-run] would save from {img_url[:60]}")
            updated += 1
            continue

        # Derive file extension
        parsed_path = urlparse(img_url).path
        ext = pathlib.Path(parsed_path).suffix.lower().split("?")[0]
        if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
            ext = ".jpg"

        dest     = THUMB_DIR / f"{stem}{ext}"
        rel_path = f"images/thumbnails/{stem}{ext}"

        if dest.exists():
            print(f"  -> already exists: {rel_path}")
            sources[i]["image"] = rel_path
            updated += 1
            continue

        ok = download_image(img_url, dest)
        if ok:
            sources[i]["image"] = rel_path
            updated += 1
            print(f"  -> saved: {rel_path}")
        else:
            print("  -> download failed")

    if updated and not dry_run:
        save_yaml(SOURCES_YAML, sources)
        print(f"\nDone. Updated {updated} image path(s) in {SOURCES_YAML}.")
        print("Next steps:")
        print("  1. cd _cite && uv run cite.py   (regenerate citations.yaml)")
        print("  2. bundle exec jekyll build     (rebuild the site)")
    elif updated and dry_run:
        print(f"\n[dry-run] Would have updated {updated} image path(s).")
    else:
        print("\nNo new thumbnails could be downloaded.")
        print("Note: Most publisher sites block automated scrapers (403/bot detection).")
        print("The SVG word-cloud fallback (pub-thumbs.js) covers all papers automatically.")
        print("For manual thumbnails, screenshot paper pages and save to images/thumbnails/,")
        print("then add the path to the 'image:' field in _data/sources.yaml.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Auto-fetch paper thumbnail images")
    parser.add_argument("--limit", type=int, default=0,
                        help="Process only the first N papers (0 = all)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Find images but don't download or save")
    args = parser.parse_args()
    fetch_thumbnails(limit=args.limit, dry_run=args.dry_run)
