/*
  Neural-network hero canvas for the homepage bento.
  Dependency-free: drifting nodes + proximity edges with a subtle pointer
  parallax, plus a count-up for the live stats.

  Performance & accessibility guardrails:
   - prefers-reduced-motion -> draws a single static frame, no animation,
     and stats jump straight to their final value.
   - devicePixelRatio capped at 2.
   - node count scales down on small screens.
   - rAF pauses when the hero scrolls offscreen (IntersectionObserver)
     and when the tab is hidden (visibilitychange).
*/
(() => {
  "use strict";

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------------- canvas */
  const canvas = document.querySelector("canvas.neural-hero");
  if (canvas && canvas.getContext) {
    const ctx = canvas.getContext("2d");
    const hero = canvas.closest(".b-hero") || canvas.parentElement;
    const pointer = { x: 0.5, y: 0.5 };

    let w = 0;
    let h = 0;
    let nodes = [];
    let raf = null;
    let running = false;
    let nodeColor = "#38bdf8";
    let edgeColor = "#22d3ee";

    const cssVar = (name, fallback) => {
      const v = getComputedStyle(document.documentElement)
        .getPropertyValue(name)
        .trim();
      return v || fallback;
    };

    const toRgba = (hex, a) => {
      let c = hex.replace("#", "");
      if (c.length === 3) c = c.split("").map((x) => x + x).join("");
      const r = parseInt(c.slice(0, 2), 16);
      const g = parseInt(c.slice(2, 4), 16);
      const b = parseInt(c.slice(4, 6), 16);
      return `rgba(${r},${g},${b},${a})`;
    };

    const nodeCount = () => {
      if (w < 520) return 14;
      if (w < 900) return 26;
      return Math.min(46, Math.round((w * h) / 22000));
    };

    const seed = () => {
      nodes = [];
      const n = nodeCount();
      for (let i = 0; i < n; i++) {
        nodes.push({
          x: Math.random() * w,
          y: Math.random() * h,
          vx: (Math.random() - 0.5) * 0.18,
          vy: (Math.random() - 0.5) * 0.18,
          r: Math.random() * 1.6 + 1,
        });
      }
    };

    const resize = () => {
      const rect = canvas.getBoundingClientRect();
      w = rect.width;
      h = rect.height;
      if (w === 0 || h === 0) return;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      nodeColor = cssVar("--primary", "#38bdf8");
      edgeColor = cssVar("--security", "#22d3ee");
      seed();
    };

    const draw = () => {
      if (w === 0 || h === 0) return;
      ctx.clearRect(0, 0, w, h);
      const maxD = Math.min(w, h) * 0.32;
      const px = (pointer.x - 0.5) * 26;
      const py = (pointer.y - 0.5) * 26;

      for (let i = 0; i < nodes.length; i++) {
        const a = nodes[i];
        for (let j = i + 1; j < nodes.length; j++) {
          const b = nodes[j];
          const dx = a.x - b.x;
          const dy = a.y - b.y;
          const d = Math.hypot(dx, dy);
          if (d < maxD) {
            ctx.strokeStyle = toRgba(edgeColor, (1 - d / maxD) * 0.5);
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(a.x + px * 0.4, a.y + py * 0.4);
            ctx.lineTo(b.x + px * 0.4, b.y + py * 0.4);
            ctx.stroke();
          }
        }
      }

      ctx.fillStyle = toRgba(nodeColor, 0.85);
      for (const nd of nodes) {
        ctx.beginPath();
        ctx.arc(nd.x + px, nd.y + py, nd.r, 0, Math.PI * 2);
        ctx.fill();
      }
    };

    const step = () => {
      for (const nd of nodes) {
        nd.x += nd.vx;
        nd.y += nd.vy;
        if (nd.x < 0 || nd.x > w) nd.vx *= -1;
        if (nd.y < 0 || nd.y > h) nd.vy *= -1;
      }
      draw();
      raf = requestAnimationFrame(step);
    };

    const start = () => {
      if (running || reduce) return;
      running = true;
      raf = requestAnimationFrame(step);
    };
    const stop = () => {
      running = false;
      if (raf) cancelAnimationFrame(raf);
      raf = null;
    };

    hero.addEventListener("pointermove", (e) => {
      const rect = hero.getBoundingClientRect();
      pointer.x = (e.clientX - rect.left) / rect.width;
      pointer.y = (e.clientY - rect.top) / rect.height;
    });

    let resizeTimer;
    window.addEventListener("resize", () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        resize();
        if (reduce) draw();
      }, 150);
    });

    document.addEventListener("visibilitychange", () => {
      if (document.hidden) stop();
      else start();
    });

    resize();
    if (reduce) {
      draw();
    } else if ("IntersectionObserver" in window) {
      new IntersectionObserver(
        (entries) => {
          for (const en of entries) {
            if (en.isIntersecting) start();
            else stop();
          }
        },
        { threshold: 0.05 }
      ).observe(canvas);
    } else {
      start();
    }
  }

  /* ------------------------------------------------------------- count-up */
  const counters = document.querySelectorAll(".b-stat-num [data-count]");
  if (counters.length) {
    const run = (el) => {
      const target = parseInt(el.getAttribute("data-count"), 10) || 0;
      if (reduce || target === 0) {
        el.textContent = target;
        return;
      }
      const dur = 1100;
      const t0 = performance.now();
      const tick = (now) => {
        const p = Math.min((now - t0) / dur, 1);
        const eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
        el.textContent = Math.round(target * eased);
        if (p < 1) requestAnimationFrame(tick);
        else el.textContent = target;
      };
      requestAnimationFrame(tick);
    };

    if ("IntersectionObserver" in window && !reduce) {
      const io = new IntersectionObserver(
        (entries, obs) => {
          for (const en of entries) {
            if (en.isIntersecting) {
              run(en.target);
              obs.unobserve(en.target);
            }
          }
        },
        { threshold: 0.4 }
      );
      counters.forEach((el) => io.observe(el));
    } else {
      counters.forEach(run);
    }
  }
})();
