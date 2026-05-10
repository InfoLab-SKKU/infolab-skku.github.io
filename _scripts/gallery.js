(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var items      = document.querySelectorAll(".gallery-item");
    var catBtns    = document.querySelectorAll("#gallery-cat-bar .gallery-filter-btn");
    var yearBtns   = document.querySelectorAll("#gallery-year-bar .gallery-year-btn");
    var emptyEl    = document.getElementById("gallery-empty");
    var lightbox   = document.getElementById("gallery-lightbox");

    // Support legacy pages without the new id-based bars
    if (!catBtns.length) catBtns = document.querySelectorAll(".gallery-filter-btn");

    if (!items.length || !lightbox) return;

    var lbImg     = document.getElementById("lb-img");
    var lbCaption = document.getElementById("lb-caption");
    var lbCounter = document.getElementById("lb-counter");
    var lbClose   = document.getElementById("lb-close");
    var lbPrev    = document.getElementById("lb-prev");
    var lbNext    = document.getElementById("lb-next");

    var currentCat  = "all";
    var currentYear = "all";
    var visibleItems = [];
    var currentIdx   = 0;

    /* -- Count badges (category only) --------------------------------- */
    function updateCatBadges() {
      var counts = { all: items.length };
      items.forEach(function (item) {
        var cat = item.dataset.category;
        counts[cat] = (counts[cat] || 0) + 1;
      });
      catBtns.forEach(function (btn) {
        var badge = btn.querySelector(".gallery-filter-count");
        if (badge) badge.textContent = counts[btn.dataset.filter] || 0;
      });
    }

    /* -- Apply both filters ------------------------------------------- */
    function applyFilters() {
      var visible = 0;
      items.forEach(function (item) {
        var catOk  = currentCat  === "all" || item.dataset.category === currentCat;
        var yearOk = currentYear === "all" || item.dataset.year === currentYear;
        var show   = catOk && yearOk;
        item.setAttribute("data-hidden", show ? "false" : "true");
        if (show) visible++;
      });
      if (emptyEl) emptyEl.style.display = visible === 0 ? "block" : "none";
    }

    /* -- Category buttons --------------------------------------------- */
    catBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        catBtns.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        currentCat = btn.dataset.filter;
        applyFilters();
      });
    });

    /* -- Year buttons -------------------------------------------------- */
    yearBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        yearBtns.forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        currentYear = btn.dataset.year;
        applyFilters();
      });
    });

    /* -- Lightbox ------------------------------------------------------ */
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
      if (e.key === "Escape")     closeLightbox();
      if (e.key === "ArrowLeft")  showImage((currentIdx - 1 + visibleItems.length) % visibleItems.length);
      if (e.key === "ArrowRight") showImage((currentIdx + 1) % visibleItems.length);
    });

    /* -- Init ---------------------------------------------------------- */
    updateCatBadges();
    applyFilters();
  });
})();