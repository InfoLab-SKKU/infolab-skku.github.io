// Register the service worker once the page has finished loading.
// Skipped on localhost/127.0.0.1 to avoid caching surprises during local development.
(function () {
  if (!("serviceWorker" in navigator)) return;
  if (/^(localhost|127\.0\.0\.1)$/.test(location.hostname)) return;

  window.addEventListener("load", function () {
    navigator.serviceWorker.register("/sw.js").catch(function (err) {
      console.warn("Service worker registration failed:", err);
    });
  });
})();
