// Scroll-to-top button
(function () {
  "use strict";

  function init() {
    var btn = document.createElement("button");
    btn.id = "scroll-to-top";
    btn.setAttribute("aria-label", "Scroll to top of page");
    btn.setAttribute("title", "Scroll to top");
    btn.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"></polyline></svg>';
    document.body.appendChild(btn);

    var threshold = 420;

    window.addEventListener(
      "scroll",
      function () {
        if (window.scrollY > threshold) {
          btn.classList.add("visible");
        } else {
          btn.classList.remove("visible");
        }
      },
      { passive: true }
    );

    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

// Reading progress bar
(function () {
  "use strict";

  var bar = document.getElementById("read-progress");
  if (!bar) return;

  window.addEventListener(
    "scroll",
    function () {
      var scrollTop =
        window.scrollY || document.documentElement.scrollTop;
      var docHeight =
        document.documentElement.scrollHeight - window.innerHeight;
      var progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      bar.style.width = Math.min(progress, 100) + "%";
      bar.setAttribute("aria-valuenow", Math.round(progress));
    },
    { passive: true }
  );
})();
