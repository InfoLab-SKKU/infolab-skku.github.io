"""
fetch_pdf_browser.py
====================
Tier 2 of the subscription PDF collector: drives a real Chrome (Selenium) to
download the publications that block plain HTTP clients with a JS/Cloudflare
challenge — chiefly IEEE Xplore (10.1109) and Elsevier ScienceDirect (10.1016).
Run on the campus network so the browser inherits the institution's access.

How it works:
  * Chrome is configured to DOWNLOAD PDFs (not open the built-in viewer) into a
    temporary watch folder.
  * For each remaining DOI: open https://doi.org/<doi>, let the publisher page
    (and any challenge) settle, then read the page's own
    <meta name="citation_pdf_url"> — both IEEE and ScienceDirect expose it.
    Navigating Chrome to that URL triggers an authenticated download.
  * The downloaded file is moved to pdf/<doi-stem>.pdf and a `pdf` button is
    merged into _data/sources.yaml (existing entries untouched).

If your institution uses SSO/EZproxy rather than pure IP access, pass
--profile "C:\\Users\\<you>\\AppData\\Local\\Google\\Chrome\\User Data" so the
browser reuses your logged-in cookies (close all Chrome windows first — Chrome
locks the live profile).

After running, re-run `python _cite/cite.py` (or push and let CI rebuild).

Usage:
    python _cite/fetch_pdf_browser.py --limit 3        # test a few first
    python _cite/fetch_pdf_browser.py                  # all IEEE/Elsevier
    python _cite/fetch_pdf_browser.py --headful        # watch the browser
"""

# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml", "selenium"]
# ///

import re
import sys
import time
import shutil
import pathlib
import argparse
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()))
from fetch_pdf import (CITATIONS_YAML, SOURCES_YAML, PDF_DIR, load_yaml,
                       save_yaml, pdf_stem, has_pdf_button)
from fetch_pdf_subscription import remaining_dois, wire_up

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Publishers this Tier-2 pass targets.
TARGET_PREFIXES = ("10.1109", "10.1016")
PAGE_SETTLE = 8      # seconds to let the publisher page / challenge resolve
DOWNLOAD_WAIT = 50   # max seconds to wait for a PDF to land


def clone_session(user_data_dir: str) -> str:
    """
    Copy just the cookie/session files from a live Chrome 'User Data' dir into a
    fresh throwaway profile, so Selenium reuses the authenticated session
    (Cloudflare cf_clearance, SSO/EZproxy, publisher login) WITHOUT needing the
    real Chrome to be closed. Returns the path to the temp User Data dir.
    """
    src = pathlib.Path(user_data_dir)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="chrome_clone_"))
    (tmp / "Default" / "Network").mkdir(parents=True, exist_ok=True)
    # Local State holds the DPAPI-wrapped key that decrypts the cookies.
    for f in ["Local State"]:
        if (src / f).exists():
            shutil.copy2(src / f, tmp / f)
    # Cookies live in Default/Network (SQLite + WAL); copy whatever is present.
    for f in ["Cookies", "Cookies-journal", "Cookies-wal"]:
        p = src / "Default" / "Network" / f
        if p.exists():
            try:
                shutil.copy2(p, tmp / "Default" / "Network" / f)
            except Exception:
                pass
    # NOTE: deliberately do NOT copy Preferences / Secure Preferences — Chrome's
    # tamper check rejects a copied Secure Preferences ("failed to write prefs
    # file"). Cookies + Local State are enough to reuse the logged-in session.
    return str(tmp)


def make_driver(download_dir: str, headful: bool, user_data: str | None,
                attach: str | None = None):
    opts = Options()
    if attach:
        # Attach to a Chrome the user already launched with
        # --remote-debugging-port. This drives the REAL browser (real session +
        # TLS fingerprint), so Cloudflare passes and subscription access applies.
        opts.add_experimental_option("debuggerAddress", attach)
        driver = webdriver.Chrome(options=opts)
        driver.set_page_load_timeout(60)
        # Route downloads to our watch folder via CDP.
        try:
            driver.execute_cdp_cmd("Page.setDownloadBehavior",
                                   {"behavior": "allow", "downloadPath": download_dir})
        except Exception:
            pass
        return driver
    if not headful:
        opts.add_argument("--headless=new")
    if user_data:
        opts.add_argument(f"--user-data-dir={user_data}")
        opts.add_argument("--profile-directory=Default")
    opts.add_argument("--window-size=1280,1024")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("prefs", {
        "plugins.always_open_pdf_externally": True,   # download, don't view
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "profile.default_content_setting_values.automatic_downloads": 1,
    })
    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(60)
    return driver


def citation_pdf_url(driver) -> str | None:
    try:
        el = driver.find_element(By.CSS_SELECTOR,
                                 'meta[name="citation_pdf_url"]')
        url = (el.get_attribute("content") or "").strip()
        return url or None
    except Exception:
        return None


def wait_for_download(watch: pathlib.Path, before: set, timeout: int):
    """Return the newly-finished file in `watch`, or None on timeout."""
    end = time.time() + timeout
    while time.time() < end:
        files = set(watch.glob("*"))
        new = [f for f in files - before
               if f.suffix.lower() == ".pdf" and not f.name.endswith(".crdownload")]
        # also ignore in-progress .crdownload
        if new and not any(f.name.endswith(".crdownload") for f in files):
            return new[0]
        time.sleep(1)
    return None


def resolve_pdf_url(driver):
    """
    From the currently-loaded publisher page, work out the PDF URL.
      * Any publisher exposing <meta name="citation_pdf_url"> (Elsevier when the
        Cloudflare challenge has passed, most others).
      * IEEE Xplore: derive the arnumber from /document/<id> and read the PDF
        iframe on the stamp page.
    Returns a URL string or None.
    """
    url = citation_pdf_url(driver)
    if url:
        return url
    m = re.search(r"/document/(\d+)", driver.current_url)
    if m:
        arn = m.group(1)
        driver.get(f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={arn}")
        time.sleep(PAGE_SETTLE)
        for ifr in driver.find_elements(By.TAG_NAME, "iframe"):
            src = ifr.get_attribute("src") or ""
            if ".pdf" in src.lower() or "arnumber=" in src:
                return src
        return f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={arn}&ref="
    return None


def run(limit=0, headful=False, user_data=None, attach=None):
    citations = load_yaml(CITATIONS_YAML)
    sources   = load_yaml(SOURCES_YAML)
    by_id = {(e.get("id") or "").strip().lower(): e for e in sources if e.get("id")}

    dois = [d for d in remaining_dois(citations, sources)
            if d.replace("doi:", "").startswith(TARGET_PREFIXES)]
    if limit:
        dois = dois[:limit]
    print(f"Tier 2 (browser): {len(dois)} IEEE/Elsevier DOIs to try.")
    if not dois:
        return

    clone = None
    if user_data and not attach:
        clone = clone_session(user_data)
        print(f"Cloned authenticated session -> {clone}")

    watch = pathlib.Path(tempfile.mkdtemp(prefix="pdf_dl_"))
    driver = make_driver(str(watch), headful, clone, attach=attach)
    got = miss = 0
    try:
        for doi_id in dois:
            doi  = doi_id.replace("doi:", "").strip()
            dest = PDF_DIR / f"{pdf_stem(doi)}.pdf"
            rel  = f"pdf/{pdf_stem(doi)}.pdf"
            print(f"  [{doi}]", end="", flush=True)
            if dest.exists():
                print("  on disk")
                wire_up(sources, by_id, doi_id, rel); got += 1
                continue
            try:
                driver.get(f"https://doi.org/{doi}")
                time.sleep(PAGE_SETTLE)
                pdf_url = resolve_pdf_url(driver)
                if not pdf_url:
                    print("  -> no PDF url (challenge / no access)")
                    miss += 1
                    continue
                before = set(watch.glob("*"))
                driver.get(pdf_url)
                got_file = wait_for_download(watch, before, DOWNLOAD_WAIT)
                if not got_file:
                    print("  -> download did not complete")
                    miss += 1
                    continue
                with open(got_file, "rb") as fh:
                    head = fh.read(5)
                if not head.startswith(b"%PDF"):
                    print("  -> not a PDF (login/challenge?)")
                    got_file.unlink(missing_ok=True)
                    miss += 1
                    continue
                PDF_DIR.mkdir(parents=True, exist_ok=True)
                shutil.move(str(got_file), str(dest))
                wire_up(sources, by_id, doi_id, rel)
                print(f"  -> saved {rel}")
                got += 1
            except Exception as e:
                print(f"  -> error: {str(e)[:60]}")
                miss += 1
            time.sleep(2)
    finally:
        driver.quit()
        shutil.rmtree(watch, ignore_errors=True)
        if clone:
            shutil.rmtree(clone, ignore_errors=True)

    print(f"\nTier 2 summary: {got} obtained, {miss} failed.")
    if got:
        save_yaml(SOURCES_YAML, sources)
        print(f"Updated {SOURCES_YAML}. Next: re-merge into citations.yaml.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--headful", action="store_true",
                    help="Show the browser window (default headless)")
    ap.add_argument("--profile", default=None,
                    help="Path to a live Chrome 'User Data' dir; its session "
                         "cookies are cloned so downloads use your access")
    ap.add_argument("--attach", default=None, metavar="HOST:PORT",
                    help="Attach to a Chrome you launched with "
                         "--remote-debugging-port=9222 (use 127.0.0.1:9222). "
                         "Drives your real browser: passes Cloudflare and uses "
                         "your subscription. Most reliable for IEEE/Elsevier.")
    args = ap.parse_args()
    run(limit=args.limit, headful=args.headful, user_data=args.profile,
        attach=args.attach)
