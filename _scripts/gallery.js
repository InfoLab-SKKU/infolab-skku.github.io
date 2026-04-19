(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var items        = document.querySelectorAll(".gallery-item");
    var filterBtns   = document.querySelectorAll(".gallery-filter-btn");
    var emptyEl      = document.getElementById("gallery-empty");
    var lightbox     = document.getElementById("gallery-lightbox");

    // Only run on the gallery page
    if (!items.length || !lightbox) return;

    var lbImg     = document.getElementById("lb-img");
    var lbCaption = document.getElementById("lb-caption");
    var lbCounter = document.getElementById("lb-counter");
    var lbClose   = document.getElementById("lb-close");
    var lbPrev    = document.getElementById("lb-prev");
    var lbNext    = document.getElementById("lb-next");

    var currentFilter = "all";
    var visibleItems  = [];
    var currentIdx    = 0;

    /* ── Count badges ──────────────────────────────── */
    function updateBadges() {
      var counts = { all: items.length };
      items.forEach(function (item) {
        var cat = item.dataset.category;
        counts[cat] = (counts[cat] || 0) + 1;
      });
      filterBtns.forEach(function (btn) {
        var badge = btn.querySelector(".gallery-filter-count");
        if (badge) badge.textContent = counts[btn.dataset.filter] || 0;
      });
    }

    /* ── Filter ────────────────────────────────────── */
    function applyFilter(filter) {
      var visible = 0;
      items.forEach(function (item) {
        var show = filter === "all" || item.dataset.category === filter;
        item.setAttribute("data-hidden", show ? "false" : "true");
        if (show) visible++;
      });
      if (emptyEl) emptyEl.style.display = visible === 0 ? "block" : "none";
    }

    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        filterBtns.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        currentFilter = btn.dataset.filter;
        applyFilter(currentFilter);
      });
    });

    /* ── Lightbox ──────────────────────────────────── */
    function getVisibleItems() {
      return Array.from(items).filter(function (item) {
        return item.getAttribute("data-hidden") !== "true";
      });
    }

    function showImage(idx) {
      var item = visibleItems[idx];
      if (!item) return;
      lbImg.src = item.dataset.src;
      lbCaption.textContent = item.dataset.caption || "";
      lbCounter.textContent = (idx + 1) + " / " + visibleItems.length;
      currentIdx = idx;
    }

    function openLightbox(idx) {
      visibleItems = getVisibleItems();
      document.body.style.overflow = "hidden";
      lightbox.style.display = "flex";
      showImage(idx);
    }

    function closeLightbox() {
      lightbox.style.display = "none";
      document.body.style.overflow = "";
    }

    // Attach click to each item
    items.forEach(function (item) {
      item.querySelector(".gallery-img-wrap").addEventListener("click", function () {
        visibleItems = getVisibleItems();
        var idx = visibleItems.indexOf(item);
        openLightbox(idx >= 0 ? idx : 0);
      });
    });

    lbClose.addEventListener("click", closeLightbox);

    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) closeLightbox();
    });

    lbPrev.addEventListener("click", function () {
      showImage((currentIdx - 1 + visibleItems.length) % visibleItems.length);
    });

    lbNext.addEventListener("click", function () {
      showImage((currentIdx + 1) % visibleItems.length);
    });

    document.addEventListener("keydown", function (e) {
      if (lightbox.style.display !== "flex") return;
      if (e.key === "Escape")      closeLightbox();
      if (e.key === "ArrowLeft")   showImage((currentIdx - 1 + visibleItems.length) % visibleItems.length);
      if (e.key === "ArrowRight")  showImage((currentIdx + 1) % visibleItems.length);
    });

    /* ── Init ──────────────────────────────────────── */
    updateBadges();
    applyFilter("all");
  });
})();
