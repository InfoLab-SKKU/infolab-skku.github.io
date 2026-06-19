"""
merge_buttons.py
================
Propagate the `pdf` (and other) buttons from _data/sources.yaml into the
generated _data/citations.yaml, replicating just the "merge sources by id" step
of cite.py without re-fetching all metadata from Manubot/ORCID/Scholar.

Use it after fetch_pdf.py / fetch_pdf_subscription.py / fetch_pdf_browser.py (or
after manually dropping PDFs into pdf/ and re-running fetch_pdf.py) so the new
PDF buttons show up on /pubs immediately. A full `python _cite/cite.py` (or the
update-citations CI workflow) reproduces the exact same result.

Matches the byte-for-byte serialization style of _cite/util.save_data so the
diff stays minimal (additive button blocks only).

Usage:
    python _cite/merge_buttons.py
"""

import pathlib
import yaml

ROOT = pathlib.Path(__file__).parent.parent.resolve()
CIT = ROOT / "_data" / "citations.yaml"
SRC = ROOT / "_data" / "sources.yaml"


def has_pdf(entry: dict) -> bool:
    return any(isinstance(b, dict) and b.get("type") == "pdf"
               for b in (entry.get("buttons") or []))


def main():
    cits = yaml.safe_load(CIT.read_text(encoding="utf-8")) or []
    srcs = yaml.safe_load(SRC.read_text(encoding="utf-8")) or []
    src_by = {(s.get("id") or "").strip().lower(): s for s in srcs if s.get("id")}

    added = 0
    for c in cits:
        s = src_by.get((c.get("id") or "").strip().lower())
        if not s:
            continue
        s_btns = s.get("buttons") or []
        if has_pdf(s) and not has_pdf(c):
            c["buttons"] = s_btns
            added += 1
        # carry over a curated image if the citation has none
        if not (c.get("image") or "").strip() and (s.get("image") or "").strip():
            c["image"] = s["image"]

    # match _cite/util.save_data exactly (no allow_unicode, no aliases)
    yaml.Dumper.ignore_aliases = lambda *a: True
    body = yaml.dump(cits, default_flow_style=False, sort_keys=False)
    CIT.write_text("# DO NOT EDIT, GENERATED AUTOMATICALLY\n\n" + body,
                   encoding="utf-8")
    print(f"Merged buttons into {added} citation entries -> {CIT}")


if __name__ == "__main__":
    main()
