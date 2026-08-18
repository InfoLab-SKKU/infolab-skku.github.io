// Image fallback / failure handlers (CSP-friendly replacement for inline onerror)
(function () {
  "use strict";

  function handleError(img) {
    if (img.dataset.fallbackHandled === "true") return;
    img.dataset.fallbackHandled = "true";

    // If image has data-fallback-hide, remove its container.
    if (img.hasAttribute("data-fallback-hide")) {
      var container = img.closest(".proj-card-img");
      if (container) {
        container.style.display = "none";
      } else {
        img.style.display = "none";
      }
      return;
    }

    // Otherwise swap to the configured fallback image.
    var fallback = img.getAttribute("data-fallback");
    if (fallback && img.src !== fallback) {
      img.src = fallback;
    }
  }

  // Catch loads that already failed before this script ran.
  document.querySelectorAll("img[data-fallback], img[data-fallback-hide]").forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) {
      handleError(img);
    }
  });

  // Use a capturing listener so we catch error events on any img that bubbles.
  document.addEventListener(
    "error",
    function (event) {
      var target = event.target;
      if (
        target &&
        target.tagName === "IMG" &&
        (target.hasAttribute("data-fallback") || target.hasAttribute("data-fallback-hide"))
      ) {
        handleError(target);
      }
    },
    true
  );
})();
