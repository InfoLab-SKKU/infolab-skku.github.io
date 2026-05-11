"""
Plugin to fetch publications from a Google Scholar author profile
using the free `scholarly` library (no API key required).

For each publication, a DOI is looked up via Crossref by title.
If a DOI is found, Manubot generates the full citation automatically.
If not, the raw bibliographic fields from Google Scholar are used directly.

All network results are cached for 24 hours to avoid rate limiting.
"""

import re
import requests
from urllib.parse import quote
from scholarly import scholarly
from util import *


def _extract_doi(url: str) -> str:
    """Extract a bare DOI from a URL, e.g. https://doi.org/10.1234/xyz → 10.1234/xyz"""
    if not url:
        return ""
    m = re.search(r"10\.\d{4,}[\w./;:()\-]+", url)
    return m.group(0).rstrip("./") if m else ""


def _crossref_doi(title: str) -> str:
    """
    Look up a DOI from Crossref by title.
    Returns empty string when no close match is found.
    """
    if not title:
        return ""
    try:
        url = (
            "https://api.crossref.org/works"
            f"?query.title={quote(title)}"
            "&rows=1"
            "&select=DOI,title"
        )
        headers = {"User-Agent": "InfoLab-SKKU cite-script/1.0 (mailto:tamer@skku.edu)"}
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        items = resp.json().get("message", {}).get("items", [])
        if not items:
            return ""
        cr_title = " ".join(get_safe(items[0], "title", [""])).strip().lower()
        our_title = title.strip().lower()
        # Require the first 50 characters to match (handles subtitle differences)
        n = min(50, len(our_title))
        if cr_title[:n] == our_title[:n]:
            return get_safe(items[0], "DOI", "")
    except Exception:
        pass
    return ""


def main(entry):
    """
    Receives a single entry from _data/google-scholar*.yaml with key `gsid`
    (Google Scholar author ID, e.g. pLC4l6YAAAAJ).
    Returns a list of sources to cite.
    """

    gsid = get_safe(entry, "gsid", "")
    if not gsid:
        raise Exception('No "gsid" key in entry')

    # Extra fields to stamp on every source (orcid, list flags, etc.)
    extra = {k: v for k, v in entry.items() if k != "gsid"}

    # ── Fetch & cache the author's full publication list (24-hour TTL) ──────
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(gsid):
        author = scholarly.search_author_id(gsid)
        author = scholarly.fill(author, sections=["publications"])
        return author.get("publications", [])

    publications = query(gsid)

    sources = []

    for pub in publications:
        bib = get_safe(pub, "bib", {})
        title = (get_safe(bib, "title", "") or "").strip()
        if not title:
            continue

        # ── Try to resolve a DOI ────────────────────────────────────────────
        pub_url     = get_safe(pub, "pub_url", "")     or ""
        eprint_url  = get_safe(pub, "eprint_url", "")  or ""
        doi = (
            _extract_doi(pub_url)
            or _extract_doi(eprint_url)
            or _crossref_doi(title)
        )

        if doi:
            # Manubot will resolve this DOI to a full, rich citation
            source = {"id": f"doi:{doi}"}
        else:
            # No DOI found — supply raw bibliographic fields directly.
            # Leaving id="" tells cite.py to skip Manubot and use these fields as-is.
            year = str(get_safe(bib, "pub_year", "") or "")
            author_str = get_safe(bib, "author", "") or ""
            venue = (
                get_safe(bib, "venue", "")
                or get_safe(bib, "journal", "")
                or get_safe(bib, "booktitle", "")
                or ""
            )
            # scholarly uses " and " as the author separator
            authors = [
                a.strip()
                for a in re.split(r"\s+and\s+", author_str)
                if a.strip()
            ]
            source = {
                "id": "",
                "title": title,
                "authors": authors,
                "publisher": venue,
                "date": f"{year}-01-01" if year else "",
                "link": pub_url,
            }

        # ── Stamp orcid, list flags, etc. onto every source ─────────────────
        for key, val in extra.items():
            source.setdefault(key, val)

        sources.append(source)

    return sources
