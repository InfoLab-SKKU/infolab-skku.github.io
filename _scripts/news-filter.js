(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var items      = document.querySelectorAll(".news-card-item");
    var filterBtns = document.querySelectorAll(".news-filter-btn");
    var yearGroups = document.querySelectorAll(".news-year-group");
    var emptyEl    = document.getElementById("news-empty");

    // Only run on the news page
    if (!items.length || !emptyEl) return;

    var currentFilter = "all";

    /* ── Count badges ──────────────────────────── */
    function updateCounts() {
      var counts = { all: items.length };
      items.forEach(function (item) {
        var type = item.dataset.type;
        counts[type] = (counts[type] || 0) + 1;
      });
      filterBtns.forEach(function (btn) {
        var badge = btn.querySelector(".news-filter-count");
        if (badge) badge.textContent = counts[btn.dataset.filter] || 0;
      });
    }

    /* ── Apply filter ──────────────────────────── */
    function applyFilter(filter) {
      var totalVisible = 0;

      items.forEach(function (item) {
        var show = filter === "all" || item.dataset.type === filter;
        item.style.display = show ? "" : "none";
        if (show) totalVisible++;
      });

      // Show/hide year group sections; update their counts
      yearGroups.forEach(function (group) {
        var groupItems   = group.querySelectorAll(".news-card-item");
        var visibleCount = Array.from(groupItems).filter(function (i) {
          return i.style.display !== "none";
        }).length;

        group.style.display = visibleCount === 0 ? "none" : "";

        var countEl = group.querySelector(".news-year-count");
        if (countEl) {
          var total = groupItems.length;
          countEl.textContent =
            (filter === "all" ? total : visibleCount + " of " + total) +
            " update" + (total === 1 ? "" : "s");
        }
      });

      emptyEl.style.display = totalVisible === 0 ? "block" : "none";
    }

    /* ── Filter button clicks ──────────────────── */
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        currentFilter = btn.dataset.filter;
        applyFilter(currentFilter);
      });
    });

    /* ── Init ──────────────────────────────────── */
    updateCounts();
    applyFilter("all");
  });
})();
