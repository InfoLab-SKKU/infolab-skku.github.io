{
  // featured hero carousel on the homepage
  const init = () => {
    const root = document.getElementById("featured-carousel");
    if (!root) return;

    const track = root.querySelector(".fc-track");
    const slides = Array.from(track.querySelectorAll(".fc-slide"));
    const prevButton = root.querySelector(".fc-prev");
    const nextButton = root.querySelector(".fc-next");
    const dotsWrap = root.querySelector(".fc-dots");
    const playPause = root.querySelector(".fc-playpause");

    if (slides.length < 2) {
      [prevButton, nextButton, playPause, dotsWrap].forEach(
        (el) => el && (el.style.display = "none"),
      );
      return;
    }

    const DELAY = 7000;
    const reduceMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)",
    ).matches;

    let index = 0;
    let timer = null;
    let playing = !reduceMotion;

    // build dot indicators
    const dots = slides.map((slide, i) => {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.className = "fc-dot";
      dot.setAttribute("aria-label", `Go to slide ${i + 1} of ${slides.length}`);
      dot.addEventListener("click", () => {
        goTo(i);
        restart();
      });
      dotsWrap.appendChild(dot);
      return dot;
    });

    const goTo = (i) => {
      index = (i + slides.length) % slides.length;
      track.style.transform = `translateX(-${index * 100}%)`;
      dots.forEach((dot, j) => dot.classList.toggle("active", j === index));
      slides.forEach((slide, j) => {
        slide.classList.toggle("fc-current", j === index);
        // keep links/buttons of off-screen slides out of the tab order
        if (j === index) slide.removeAttribute("inert");
        else slide.setAttribute("inert", "");
      });
    };

    const stop = () => {
      if (timer) clearInterval(timer);
      timer = null;
    };

    const start = () => {
      if (!playing || timer) return;
      timer = setInterval(() => goTo(index + 1), DELAY);
    };

    const restart = () => {
      stop();
      start();
    };

    const setPlaying = (state) => {
      playing = state;
      const icon = playPause.querySelector(".icon");
      if (icon) {
        icon.classList.toggle("fa-pause", playing);
        icon.classList.toggle("fa-play", !playing);
      }
      playPause.setAttribute(
        "aria-label",
        playing ? "Pause slideshow" : "Play slideshow",
      );
      playPause.dataset.state = playing ? "playing" : "paused";
      if (playing) start();
      else stop();
    };

    prevButton.addEventListener("click", () => {
      goTo(index - 1);
      restart();
    });
    nextButton.addEventListener("click", () => {
      goTo(index + 1);
      restart();
    });
    playPause.addEventListener("click", () => setPlaying(!playing));

    // pause while the user is reading or interacting with the carousel
    root.addEventListener("mouseenter", stop);
    root.addEventListener("mouseleave", start);
    root.addEventListener("focusin", stop);
    root.addEventListener("focusout", start);

    // pause when the tab is in the background
    document.addEventListener("visibilitychange", () => {
      if (document.hidden) stop();
      else start();
    });

    // keyboard navigation
    root.addEventListener("keydown", (event) => {
      if (event.key === "ArrowLeft") {
        goTo(index - 1);
        restart();
      } else if (event.key === "ArrowRight") {
        goTo(index + 1);
        restart();
      }
    });

    // touch swipe
    let touchStartX = 0;
    root.addEventListener(
      "touchstart",
      (event) => {
        touchStartX = event.touches[0].clientX;
      },
      { passive: true },
    );
    root.addEventListener(
      "touchend",
      (event) => {
        const delta = event.changedTouches[0].clientX - touchStartX;
        if (Math.abs(delta) < 50) return;
        goTo(delta < 0 ? index + 1 : index - 1);
        restart();
      },
      { passive: true },
    );

    goTo(0);
    if (reduceMotion) setPlaying(false);
    else start();
  };

  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", init);
  else init();
}
