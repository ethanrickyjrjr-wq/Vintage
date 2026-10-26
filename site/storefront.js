(() => {
  // Small foreground/background offsets make the assembled display feel spatial.
  // No scroll handler, continuous loop, or motion on touch/reduced-motion devices.
  const stage = document.querySelector(".salon-stage");
  const allowDepth = matchMedia("(prefers-reduced-motion: no-preference) and (hover: hover) and (pointer: fine)");
  let depthFrame = 0;
  let depthX = 0;
  let depthY = 0;
  function resetDepth() {
    cancelAnimationFrame(depthFrame);
    depthFrame = 0;
    stage?.style.removeProperty("--look-x");
    stage?.style.removeProperty("--look-y");
  }
  stage?.addEventListener("pointermove", (event) => {
    if (!allowDepth.matches) return;
    const bounds = stage.getBoundingClientRect();
    depthX = ((event.clientX - bounds.left) / bounds.width - .5) * 12;
    depthY = ((event.clientY - bounds.top) / bounds.height - .5) * 8;
    if (depthFrame) return;
    depthFrame = requestAnimationFrame(() => {
      stage.style.setProperty("--look-x", `${depthX.toFixed(2)}px`);
      stage.style.setProperty("--look-y", `${depthY.toFixed(2)}px`);
      depthFrame = 0;
    });
  });
  stage?.addEventListener("pointerleave", resetDepth);
  allowDepth.addEventListener("change", resetDepth);
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
