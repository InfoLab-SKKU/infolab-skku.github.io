import json
import re
from urllib.request import Request, urlopen
from util import *


def main(entry):
    """
    receives single list entry from orcid data file
    returns list of sources to cite
    """

    # orcid api
    endpoint = "https://pub.orcid.org/v3.0/$ORCID/works"
    headers = {"Accept": "application/json"}

    # get id from entry
    _id = get_safe(entry, "orcid", "")
    if not _id:
        raise Exception('No "orcid" key')

    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(_id):
        url = endpoint.replace("$ORCID", _id)
        request = Request(url=url, headers=headers)
        response = json.loads(urlopen(request).read())
        return get_safe(response, "group", [])

    response = query(_id)

    # list of sources to return
    sources = []

    # go through response structure and pull out ids e.g. doi:1234/56789
    for work in response:
        # get list of ids
        ids = []
        for summary in get_safe(work, "work-summary", []):
            ids = ids + get_safe(summary, "external-ids.external-id", [])
        ids = ids + get_safe(work, "external-ids.external-id", [])

        # prefer doi id type, or fallback to first id
        _id = next(
            (id for id in ids if get_safe(id, "external-id-type", "") == "doi" and get_safe(id, "external-id-relationship", "") == "self"),
            ids[0] if len(ids) > 0 else {},
        )

        # get id and id-type from response
        id_type = get_safe(_id, "external-id-type", "")
        id_value = get_safe(_id, "external-id-value", "")

        # normalise arxiv ids: ORCID stores these inconsistently
        # ("arXiv:2103.13032v1", "https://arxiv.org/abs/2405.01934",
        # "2307.11906"), which Manubot can't resolve unless reduced to a bare
        # arxiv id. Without this they fall back to ORCID metadata (no authors,
        # wrong date).
        if id_type == "arxiv":
            id_value = re.sub(r"(?i)^\s*arxiv:", "", id_value)
            id_value = re.sub(r"(?i)^https?://arxiv\.org/abs/", "", id_value)
            id_value = re.sub(r"(?i)v\d+$", "", id_value).strip()

        # create source; omit id entirely when ORCID has no external id,
        # so cite.py won't try to resolve a bogus ":" via Manubot
        source = {}
        if id_type and id_value:
            source["id"] = f"{id_type}:{id_value}"

        # doi and arxiv ids resolve to full, correct metadata via Manubot, so
        # don't attach ORCID's own fields for them — in particular ORCID's
        # last-modified-date is NOT a publication date and must never override
        # Manubot's. Only entries with no Manubot-resolvable id fall back to
        # ORCID metadata below.
        if id_type not in ("doi", "arxiv"):
            # get summaries
            summaries = get_safe(work, "work-summary", [])

            # sort summary entries by most recent
            summaries = sorted(
                summaries,
                key=lambda summary: (get_safe(summary, "last-modified-date.value", 0))
                or get_safe(summary, "created-date.value", 0)
                or 0,
                reverse=True,
            )

            # get first summary with defined sub-value
            def first(get_func):
                return next(
                    (value for value in map(get_func, summaries) if value), None
                )

            # get title
            title = first(lambda s: get_safe(s, "title.title.value", ""))

            # get publisher
            publisher = first(lambda s: get_safe(s, "journal-title.value", ""))

            # get date from the actual publication-date (year/month/day), NOT
            # last-modified-date (which is when the ORCID record changed)
            def pub_date(s):
                year = get_safe(s, "publication-date.year.value", "")
                if not year:
                    return None
                month = (get_safe(s, "publication-date.month.value", "") or "1").zfill(2)
                day = (get_safe(s, "publication-date.day.value", "") or "1").zfill(2)
                return f"{year}-{month}-{day}"

            date = first(pub_date)

            # get link
            link = first(lambda s: get_safe(s, "url.value", ""))

            # keep available details
            if title:
                source["title"] = title
            if publisher:
                source["publisher"] = publisher
            if date:
                source["date"] = format_date(date)
            if link:
                source["link"] = link

        # copy fields from entry to source
        source.update(entry)

        # add source to list
        sources.append(source)

    return sources
