// Projects page group filter
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll(".proj-filter-btn");
    var cards = document.querySelectorAll(".proj-card");

    if (!buttons.length || !cards.length) return;

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        buttons.forEach(function (b) {
          b.classList.remove("active");
          b.setAttribute("aria-pressed", "false");
        });
        btn.classList.add("active");
        btn.setAttribute("aria-pressed", "true");

        var filter = btn.getAttribute("data-filter");

        cards.forEach(function (card) {
          if (filter === "all" || card.getAttribute("data-group") === filter) {
            card.removeAttribute("data-hidden");
          } else {
            card.setAttribute("data-hidden", "true");
          }
        });
      });
    });
  });
})();
