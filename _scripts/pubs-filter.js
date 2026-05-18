// Publications page — filter, sort, view toggle, year separators,
// author highlighting, BibTeX copy, count badges, showing counter
(function () {
  "use strict";

  /* ── Configuration ─────────────────────────────────── */
  var PI_NAMES = ["Tamer Abuhmed", "Tamer AbuHmed", "T. Abuhmed", "T. AbuHmed"];

  var KEYWORDS = {
    security: ["adversarial","attack","malware","binary","security","robust",
               "interpretable","federated","authentication","biometric",
               "authorship","poisoning","backdoor","evasion"],
    biomedical: ["alzheimer","medical","clinical","biomedical","diagnosis","eeg",
                 "mri","brain","multimodal","healthcare","mortality","icu",
                 "patient","skin","disease","drug"],
    explainable: ["explainable","interpretab","transparent","xai","explain",
                  "trustworthy","ensemble","decision support"]
  };

  /* Conference/journal detection (mirrors Liquid logic in citation.html) */
  var CONF_PATTERN = /conference|symposium|workshop|proceedings|congress/i;

  function getPubType(card) {
    return card.dataset.pubtype || (CONF_PATTERN.test(card.dataset.publisher || '') ? 'conference' : 'journal');
  }

  /* ── State ──────────────────────────────────────────── */
  var currentFilter = "all";
  var currentSort   = "newest";
  var currentView   = "compact";

  /* ── DOM Refs (populated on DOMContentLoaded) ───────── */
  var wrapper, filterBtns, sortSelect, viewBtns, showingEl, filterLabelEl;

  /* ── Helpers ────────────────────────────────────────── */
  function getCards() {
    return Array.from(wrapper ? wrapper.querySelectorAll(".citation-container") : []);
  }

  function matchesFilter(card, filter) {
    if (filter === "all") return true;
    if (filter === "journal" || filter === "conference") {
      return getPubType(card) === filter;
    }
    var title     = (card.dataset.title     || "").toLowerCase();
    var publisher = (card.dataset.publisher || "").toLowerCase();
    var authors   = (card.dataset.authors   || "").toLowerCase();
    var text = title + " " + publisher + " " + authors;
    return (KEYWORDS[filter] || []).some(function (kw) { return text.indexOf(kw) !== -1; });
  }

  function getYear(card) {
    return parseInt(card.dataset.year || "0", 10);
  }

  /* ── 4. Author highlighting ─────────────────────────── */
  function highlightAuthors() {
    document.querySelectorAll(".citation-authors").forEach(function (el) {
      var html = el.innerHTML;
      PI_NAMES.forEach(function (name) {
        var escaped = name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
        html = html.replace(new RegExp(escaped, "g"),
          '<span class="citation-author-highlight">' + name + "</span>");
      });
      el.innerHTML = html;
    });
  }

  /* ── 9. Count badges ────────────────────────────────── */
  function updateCountBadges() {
    var cards = getCards();
    var counts = { all: 0, security: 0, biomedical: 0, explainable: 0, journal: 0, conference: 0 };
    cards.forEach(function (card) {
      counts.all++;
      Object.keys(KEYWORDS).forEach(function (f) {
        if (matchesFilter(card, f)) counts[f]++;
      });
      var pt = getPubType(card);
      if (pt === 'journal') counts.journal++;
      if (pt === 'conference') counts.conference++;
    });
    Object.keys(counts).forEach(function (f) {
      var el = document.getElementById("count-" + f);
      if (el) el.textContent = counts[f];
    });
  }

  /* ── 1. Update showing count & filter label ─────────── */
  function updateShowing() {
    var visible = getCards().filter(function (c) {
      return c.getAttribute("data-hidden") !== "true";
    }).length;
    if (showingEl) showingEl.textContent = visible;
    if (filterLabelEl) {
      var labels = { all: "All Topics", security: "Security & Adversarial ML",
                     biomedical: "Biomedical AI", explainable: "Explainable AI",
                     journal: "Journal Articles", conference: "Conference Papers" };
      filterLabelEl.textContent = labels[currentFilter] || "All Topics";
    }
  }

  /* ── 2. Year separators ─────────────────────────────── */
  function removeYearSeps() {
    wrapper && wrapper.querySelectorAll(".pubs-year-sep").forEach(function (el) {
      el.remove();
    });
  }

  function insertYearSeps() {
    if (!wrapper) return;
    removeYearSeps();
    var lastYear = null;
    var visibleCards = getCards().filter(function (c) {
      return c.getAttribute("data-hidden") !== "true";
    });
    visibleCards.forEach(function (card) {
      var year = getYear(card);
      if (year !== lastYear) {
        lastYear = year;
        var sep = document.createElement("div");
        sep.className = "pubs-year-sep";
        sep.textContent = year || "Unknown";
        wrapper.insertBefore(sep, card);
      }
    });
  }

  /* ── 5. BibTeX copy ─────────────────────────────────── */
  function buildBibtex(card) {
    var title   = card.dataset.title   || "";
    var authors = (card.dataset.authors || "").replace(/;/g, " and");
    var year    = card.dataset.year    || "";
    var pub     = card.dataset.publisher || "";
    var doi     = card.dataset.doi     || "";
    var key     = (authors.split(" ")[0] || "Unknown") + year;
    var isConf  = getPubType(card) === "conference";
    if (isConf) {
      return "@inproceedings{" + key + ",\n" +
             "  title     = {" + title + "},\n" +
             "  author    = {" + authors + "},\n" +
             "  year      = {" + year + "},\n" +
             "  booktitle = {" + pub + "},\n" +
             (doi ? "  doi       = {" + doi + "},\n" : "") +
             "}";
    }
    return "@article{" + key + ",\n" +
           "  title     = {" + title + "},\n" +
           "  author    = {" + authors + "},\n" +
           "  year      = {" + year + "},\n" +
           "  journal   = {" + pub + "},\n" +
           (doi ? "  doi       = {" + doi + "},\n" : "") +
           "}";
  }

  function attachCopyButtons() {
    document.querySelectorAll(".cite-copy-btn").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        var card = btn.closest(".citation-container");
        if (!card) return;
        var bibtex = buildBibtex(card);
        var copy = function(text) {
          if (navigator.clipboard) {
            navigator.clipboard.writeText(text).catch(function(){fallbackCopy(text);});
          } else {
            fallbackCopy(text);
          }
          btn.classList.add("copied");
          btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
          setTimeout(function () {
            btn.classList.remove("copied");
            btn.innerHTML = '<i class="fa-solid fa-quote-left"></i> Cite';
          }, 2000);
        };
        var fallbackCopy = function(text) {
          var ta = document.createElement("textarea");
          ta.value = text;
          ta.style.position = "fixed"; ta.style.opacity = "0";
          document.body.appendChild(ta);
          ta.select();
          document.execCommand("copy");
          document.body.removeChild(ta);
        };
        copy(bibtex);
      });
    });
  }

  /* ── 6. Sort ────────────────────────────────────────── */
  function sortCards() {
    if (!wrapper) return;
    var cards = getCards();
    cards.sort(function (a, b) {
      var ya = getYear(a), yb = getYear(b);
      return currentSort === "newest" ? yb - ya : ya - yb;
    });
    cards.forEach(function (c) { wrapper.appendChild(c); });
  }

  /* ── Core: filter + sort + separators ───────────────── */
  function applyAll() {
    getCards().forEach(function (card) {
      var show = matchesFilter(card, currentFilter);
      if (show) { card.removeAttribute("data-hidden"); }
      else      { card.setAttribute("data-hidden", "true"); }
    });
    sortCards();
    insertYearSeps();
    updateShowing();
  }

  /* ── 7. View toggle ─────────────────────────────────── */
  function applyView() {
    if (!wrapper) return;
    wrapper.classList.toggle("compact-view", currentView === "compact");
  }

  /* ── Event bindings ─────────────────────────────────── */
  function bindEvents() {
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) {
          b.classList.remove("active");
          b.setAttribute("aria-pressed", "false");
        });
        btn.classList.add("active");
        btn.setAttribute("aria-pressed", "true");
        currentFilter = btn.getAttribute("data-filter") || "all";
        applyAll();
      });
    });

    if (sortSelect) {
      sortSelect.addEventListener("change", function () {
        currentSort = sortSelect.value;
        applyAll();
      });
    }

    viewBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        viewBtns.forEach(function (b) {
          b.classList.remove("active");
          b.setAttribute("aria-pressed", "false");
        });
        btn.classList.add("active");
        btn.setAttribute("aria-pressed", "true");
        currentView = btn.getAttribute("data-view") || "rich";
        applyView();
      });
    });
  }

  /* ── Init ───────────────────────────────────────────── */
  document.addEventListener("DOMContentLoaded", function () {
    // Capture DOM refs now that DOM is ready
    wrapper       = document.getElementById("pubs-list-wrapper");
    filterBtns    = document.querySelectorAll(".pubs-filter-btn");
    sortSelect    = document.getElementById("pubs-sort");
    viewBtns      = document.querySelectorAll(".pubs-view-btn");
    showingEl     = document.getElementById("pubs-showing-count");
    filterLabelEl = document.getElementById("pubs-filter-label");

    if (!wrapper) return;
    highlightAuthors();
    attachCopyButtons();
    updateCountBadges();
    applyAll();
    applyView();
    bindEvents();
  });
})();
