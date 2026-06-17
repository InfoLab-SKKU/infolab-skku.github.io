"""
cite process to convert sources and metasources into full citations
"""

import re
import traceback
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from importlib import import_module
from pathlib import Path
from dotenv import load_dotenv
from util import *


# load environment variables
load_dotenv()


# error flag
error = False

# output citations file
output_file = "_data/citations.yaml"


log()

log("Compiling sources")

# compiled list of sources
sources = []

# in-order list of plugins to run
# NOTE: "google-scholar" is intentionally disabled. The scholarly library
# scrapes Google Scholar, which bot-blocks intermittently — so it returned a
# different (often polluted) set of publications on every run. ORCID +
# sources.yaml give complete, deterministic results. Re-add "google-scholar"
# only with a reliable backend (e.g. SerpAPI); the dedup below is hardened to
# tolerate it.
plugins = ["pubmed", "orcid", "sources"]

# loop through plugins
for plugin in plugins:
    # convert into path object
    plugin = Path(f"plugins/{plugin}.py")

    log(f"Running {plugin.stem} plugin")

    # get all data files to process with current plugin
    files = Path.cwd().glob(f"_data/{plugin.stem}*.*")
    files = list(filter(lambda p: p.suffix in [".yaml", ".yml", ".json"], files))

    log(f"Found {len(files)} {plugin.stem}* data file(s)", 1)

    # loop through data files
    for file in files:
        log(f"Processing data file {file.name}", 1)

        # load data from file
        try:
            data = load_data(file)
            # check if file in correct format
            if not list_of_dicts(data):
                raise Exception("File not a list of dicts")
        except Exception as e:
            log(e, 2, "ERROR")
            error = True
            continue

        # loop through data entries
        for index, entry in enumerate(data):
            log(f"Processing entry {index + 1} of {len(data)}, {label(entry)}", 2)

            # run plugin on data entry to expand into multiple sources
            try:
                expanded = import_module(f"plugins.{plugin.stem}").main(entry)
                # check that plugin returned correct format
                if not list_of_dicts(expanded):
                    raise Exception("Plugin didn't return list of dicts")
            # catch any plugin error
            except Exception as e:
                # log detailed pre-formatted/colored trace
                print(traceback.format_exc())
                # log high-level error
                log(e, 3, "ERROR")
                error = True
                continue

            # loop through sources
            for source in expanded:
                if plugin.stem != "sources":
                    log(label(source), 3)

                # include meta info about source
                source["plugin"] = plugin.name
                source["file"] = file.name

                # add source to compiled list
                sources.append(source)

            if plugin.stem != "sources":
                log(f"{len(expanded)} source(s)", 3)


log("Merging sources by id")

# merge sources with matching (non-blank) ids (case-insensitive DOI comparison)
for a in range(0, len(sources)):
    a_id = get_safe(sources, f"{a}.id", "")
    if not a_id:
        continue
    for b in range(a + 1, len(sources)):
        b_id = get_safe(sources, f"{b}.id", "")
        if b_id and b_id.lower() == a_id.lower():
            log(f"Found duplicate {b_id}", 2)
            sources[a].update(sources[b])
            sources[b] = {}
sources = [entry for entry in sources if entry]


log("Deduplicating sources by title")

def _norm_title(entry):
    """
    Aggressively normalised title for comparison. Strips diacritics, unifies
    "&"/"and", lowercases, and removes everything but letters and digits so
    that punctuation, curly apostrophes, math symbols and spacing differences
    (e.g. "Opaque Attack" vs "OpaqueAttack") collapse to the same key.
    """
    t = get_safe(entry, "title", "")
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "", t)


def _id_rank(id_str):
    """Quality ranking of a source id, used to pick the winner among title
    duplicates. Higher is better; any non-empty id beats a blank one."""
    id_str = (id_str or "").lower()
    if id_str.startswith("doi:"):
        return 4
    if id_str.startswith("pmid:"):
        return 3
    if id_str.startswith("arxiv:"):
        return 2
    if id_str:
        return 1
    return 0

seen_titles = {}   # norm_title -> index into sources[]
for i, source in enumerate(sources):
    t = _norm_title(source)
    if not t:
        continue
    if t not in seen_titles:
        seen_titles[t] = i
    else:
        keep = seen_titles[t]
        dupe = i
        # winner = entry with the higher-quality id (doi > pmid > arxiv >
        # other > blank); ties keep the earlier entry
        if _id_rank(get_safe(sources, f"{dupe}.id", "")) > _id_rank(get_safe(sources, f"{keep}.id", "")):
            winner, loser = dupe, keep
        else:
            winner, loser = keep, dupe
        # fill any fields the winner is missing/blank from the loser
        sources[winner].update({k: v for k, v in sources[loser].items() if k not in sources[winner] or not sources[winner][k]})
        sources[loser] = {}
        seen_titles[t] = winner
        log(f"Removed title duplicate: {get_safe(sources[winner], 'title', t)[:60]}", 2)

sources = [entry for entry in sources if entry]


log(f"{len(sources)} total source(s) to cite")


log()

log("Generating citations")

# list of new citations (index preserved for ordering)
citations_map = {}


def _process_source(index, source):
    """Resolve a single source to a citation dict. Returns (index, citation_or_None, is_error)."""
    log(f"Processing source {index + 1} of {len(sources)}, {label(source)}")

    # if explicitly flagged, remove/ignore entry
    if get_safe(source, "remove", False) == True:
        return index, None, False

    # new citation data for source
    citation = {}

    # source id
    _id = get_safe(source, "id", "").strip()

    # Manubot doesn't work without an id
    if _id:
        log("Using Manubot to generate citation", 1)

        try:
            # run Manubot and set citation
            citation = cite_with_manubot(_id)

        # if Manubot cannot cite source
        except Exception as e:
            # if regular source (id entered by user), throw error
            if get_safe(source, "plugin", "") == "sources.py":
                log(e, 3, "ERROR")
                return index, None, True
            # otherwise, if from metasource (id retrieved from some third-party API), just warn
            else:
                log(e, 3, "WARNING")
                # keep source if the metasource already supplied a title;
                # otherwise there's nothing to render, so discard
                if not get_safe(source, "title", ""):
                    return index, None, False
                citation = {}

    # preserve fields from input source, overriding existing fields
    citation.update(source)

    # ensure date in proper format for correct date sorting
    if get_safe(citation, "date", ""):
        citation["date"] = format_date(get_safe(citation, "date", ""))

    return index, citation, False


# run Manubot citations in parallel (I/O-bound subprocesses)
max_workers = 8
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = {
        executor.submit(_process_source, i, src): i
        for i, src in enumerate(sources)
    }
    for future in as_completed(futures):
        idx, citation, is_error = future.result()
        if is_error:
            error = True
        if citation is not None:
            citations_map[idx] = citation

# restore original source order
citations = [citations_map[i] for i in sorted(citations_map)]


log()

log("Saving updated citations")


# save new citations
try:
    save_data(output_file, citations)
except Exception as e:
    log(e, level="ERROR")
    error = True


# exit at end, so user can see all errors in one run
if error:
    log("Error(s) occurred above", level="ERROR")
    exit(1)
else:
    log("All done!", level="SUCCESS")

log("\n")
