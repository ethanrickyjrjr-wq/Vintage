(() => {
  const revealElements = document.querySelectorAll(".reveal");
  if (
    "IntersectionObserver" in window &&
    !matchMedia("(prefers-reduced-motion: reduce)").matches
  ) {
    const observer = new IntersectionObserver(
      (entries) =>
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
            observer.unobserve(entry.target);
          }
        }),
      { threshold: 0.08 },
    );
    revealElements.forEach((element) => {
      element.classList.add("will-reveal");
      observer.observe(element);
    });
  }
  const themeButton = document.querySelector("#theme-toggle");
  let theme = "day";
  try {
    theme =
      localStorage.getItem("hnv-theme") ||
      (matchMedia("(prefers-color-scheme: dark)").matches ? "evening" : "day");
  } catch {}
  function applyTheme() {
    document.documentElement.dataset.theme = theme;
    themeButton.textContent =
      theme === "day" ? "Evening colors ◐" : "Daytime colors ◑";
    themeButton.setAttribute(
      "aria-label",
      theme === "day" ? "Switch to evening colors" : "Switch to daytime colors",
    );
  }
  applyTheme();
  themeButton.addEventListener("click", () => {
    theme = theme === "day" ? "evening" : "day";
    applyTheme();
    try {
      localStorage.setItem("hnv-theme", theme);
    } catch {}
  });
  document.querySelector("#header-saved").addEventListener("click", () => {
    const savedFilter = document.querySelector("#saved-filter");
    if (savedFilter.getAttribute("aria-pressed") !== "true")
      savedFilter.click();
    document
      .querySelector("#collection")
      .scrollIntoView({
        behavior: matchMedia("(prefers-reduced-motion: reduce)").matches
          ? "instant"
          : "smooth",
      });
  });
})();
