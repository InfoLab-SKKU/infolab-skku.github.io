/*
  Manages light/dark mode toggle.
  Initial data-dark attribute is set inline in _includes/head.html
  to prevent FOUC; this file only handles the toggle button.
*/

{
  const onLoad = () => {
    const toggle = document.querySelector(".dark-toggle");
    if (toggle) {
      toggle.checked = document.documentElement.dataset.dark === "true";
    }
  };

  window.addEventListener("load", onLoad);

  window.onDarkToggleChange = (event) => {
    const value = event.target.checked;
    document.documentElement.dataset.dark = value;
    window.localStorage.setItem("dark-mode", value);
  };
}
