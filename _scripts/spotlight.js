/*
  Research-spotlight carousel for the homepage bento (.b-spotlight).
  Shows one publication slide at a time with a crossfade, plus dot + arrow
  controls, touch-swipe, and gentle autoplay.

  Accessibility & performance guardrails (mirroring neural-hero.js):
   - prefers-reduced-motion -> no autoplay (first slide shown; manual nav ok).
   - autoplay pauses on hover/focus, when the tab is hidden, and when the
     carousel scrolls offscreen (IntersectionObserver).
*/
(() => {
  "use strict";

  const root = document.querySelector(".b-spotlight");
  if (!root) return;

  const slides = Array.from(root.querySelectorAll(".b-spot-slide"));
  const dots = Array.from(root.querySelectorAll(".b-spot-dot"));
  const arrows = Array.from(root.querySelectorAll(".b-spot-arrow[data-dir]"));
  if (slides.length <= 1) return;

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const DELAY = 5000;

  let current = slides.findIndex((s) => s.classList.contains("is-active"));
  if (current < 0) current = 0;
  let timer = null;
  let visible = true;

  const show = (i) => {
    current = (i + slides.length) % slides.length;
    slides.forEach((s, n) => {
      const on = n === current;
      s.classList.toggle("is-active", on);
      s.setAttribute("aria-hidden", on ? "false" : "true");
    });
    dots.forEach((d, n) => d.classList.toggle("is-active", n === current));
  };

  const stop = () => {
    if (timer) clearInterval(timer);
    timer = null;
  };
  const play = () => {
    if (reduce || timer || !visible) return;
    timer = setInterval(() => show(current + 1), DELAY);
  };
  const restart = () => {
    stop();
    play();
  };

  arrows.forEach((btn) => {
    btn.addEventListener("click", () => {
      const dir = parseInt(btn.getAttribute("data-dir"), 10) || 1;
      show(current + dir);
      restart();
    });
  });

  dots.forEach((dot, n) => {
    dot.addEventListener("click", () => {
      show(n);
      restart();
    });
  });

  root.addEventListener("mouseenter", stop);
  root.addEventListener("mouseleave", play);
  root.addEventListener("focusin", stop);
  root.addEventListener("focusout", play);

  let x0 = null;
  root.addEventListener(
    "touchstart",
    (e) => {
      x0 = e.touches[0].clientX;
    },
    { passive: true }
  );
  root.addEventListener("touchend", (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) {
      show(current + (dx < 0 ? 1 : -1));
      restart();
    }
    x0 = null;
  });

  document.addEventListener("visibilitychange", () => {
    if (document.hidden) stop();
    else play();
  });

  show(current);
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(
      (entries) => {
        for (const en of entries) {
          visible = en.isIntersecting;
          if (visible) play();
          else stop();
        }
      },
      { threshold: 0.2 }
    ).observe(root);
  } else {
    play();
  }
})();
