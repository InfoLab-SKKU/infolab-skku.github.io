{
  // anti-spam email protection: addresses are split into data attributes
  // (never appearing whole in the HTML source) and assembled here at runtime
  const init = () => {
    document.querySelectorAll(".email-protected").forEach((el) => {
      const user = el.dataset.eu;
      const domain = el.dataset.ed;
      if (!user || !domain) return;
      const address = user + "@" + domain;
      el.setAttribute("href", "mailto:" + address);
      if (el.dataset.show === "true") el.textContent = address;
    });
  };

  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", init);
  else init();
}
