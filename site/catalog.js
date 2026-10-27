(() => {
  "use strict";

  const grid = document.querySelector("#product-grid");
  if (!grid) return;

  const categoryNames = {
    lighting: "Lighting & decor",
    art: "Art & memorabilia",
    print: "Print",
    fashion: "Fashion",
  };
  const statusNames = {
    ready: "Ready",
    reshoot: "Re-shoot",
    still: "Video still",
    auth: "Authenticate",
    mature: "Mature content",
  };
  const statusNotes = {
    ready:
      "Catalogued from a shop photograph. Final condition and availability still need confirmation.",
    reshoot:
      "A clearer photograph is needed before this piece is ready to list.",
    still:
      "Shown in a frame from the shop walkthrough. A dedicated product photograph is still needed.",
    auth: "Signatures have not been authenticated. No certificate of authenticity is currently recorded.",
    mature:
      "An adult magazine from the print collection. Mature-content labelling is needed when listing.",
  };
  const curatedIds = ["A1", "A10", "B1", "A14", "B6", "A3", "B10", "A16"];
  const inventory = HNV_ITEMS.filter((item) => item.id !== "OWNER");
  const curated = [...inventory].sort((a, b) => {
    const aRank = curatedIds.indexOf(a.id);
    const bRank = curatedIds.indexOf(b.id);
    return (aRank === -1 ? 100 : aRank) - (bRank === -1 ? 100 : bRank);
  });
  const storageKey = "hollywood-and-vine-saved";
  let saved = new Set();
  try {
    const stored = JSON.parse(localStorage.getItem(storageKey) || "[]");
    if (Array.isArray(stored))
      saved = new Set(
        stored.filter((id) => inventory.some((item) => item.id === id)),
      );
  } catch {
    /* Browsing still works when storage is unavailable. */
  }

  const state = {
    category: "all",
    search: "",
    sort: "curated",
    savedOnly: false,
    limit: 8,
  };
  const revealed = new Set();
  const search = document.querySelector("#search-input");
  const sort = document.querySelector("#sort-select");
  const productDialog = document.querySelector("#product-dialog");
  const tourDialog = document.querySelector("#walkthrough-dialog");
  let lastTrigger = null;
  let lastTriggerItemId = null;
  let detailId = null;
  let detailReturnHash = "";

  const escape = (value) =>
    String(value).replace(
      /[&<>"']/g,
      (char) =>
        ({
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#39;",
        })[char],
    );
  const money = (value) => "$" + Number(value).toLocaleString("en-US");
  const isHidden = (item) => item.chip === "mature" && !revealed.has(item.id);

  function updateHash(hash, replace = false) {
    if (location.hash === hash) return;
    history[replace ? "replaceState" : "pushState"](
      null,
      "",
      hash || location.pathname + location.search,
    );
  }

  function focusFind(id, preferred) {
    const target = preferred?.isConnected
      ? preferred
      : grid.querySelector(`#item-${id} .product-image`) ||
        grid.querySelector(".product-image") ||
        document.querySelector("#saved-filter") ||
        search;
    target?.focus({ preventScroll: true });
  }

  function scrollToCollection() {
    document.querySelector("#collection")?.scrollIntoView({
      behavior: matchMedia("(prefers-reduced-motion: reduce)").matches
        ? "instant"
        : "smooth",
    });
  }

  function saveButton(item, extraClass = "") {
    const active = saved.has(item.id);
    return `<button class="save-item ${extraClass}" type="button" data-save="${item.id}" aria-pressed="${active}" aria-label="${active ? "Unsave" : "Save"} ${escape(item.title)}"><span aria-hidden="true">${active ? "♥" : "♡"}</span></button>`;
  }

  function photoSources(item, detail = false) {
    const match = item.img.match(/^assets\/photos\/(IMG_\d+)\.webp$/);
    if (!match) return "";
    const base = `assets/photos/${match[1]}`;
    const sizes = detail
      ? "(max-width: 767px) 100vw, 450px"
      : "(max-width: 767px) 50vw, (max-width: 1150px) 25vw, 320px";
    return `srcset="${base}--480.webp 480w, ${base}--960.webp 960w, ${base}.webp 2048w" sizes="${sizes}"`;
  }

  function card(item) {
    const price = HNV_PRICES[item.id];
    return `<article class="product-card" id="item-${item.id}">
      <div class="product-visual">
        <button class="product-image" type="button" data-open-item="${item.id}" aria-label="View ${escape(item.title)}">
          <img src="${escape(item.img)}" ${photoSources(item)} alt="${escape(item.title)}" class="${isHidden(item) ? "mature-hidden" : ""}" loading="lazy" decoding="async" width="640" height="800">
        </button>
        ${saveButton(item)}
        ${isHidden(item) ? `<button type="button" class="reveal-cover" data-reveal="${item.id}" aria-label="View adult magazine cover for ${escape(item.title)}">View cover (18+)</button>` : ""}
      </div>
      <div class="product-info">
        <div class="product-meta"><span class="status ${item.chip}">${statusNames[item.chip]}</span><span class="product-id">${item.id}</span></div>
        <h3 class="product-title"><button type="button" data-open-item="${item.id}">${escape(item.title)}</button></h3>
        <div class="product-bottom"><span class="product-price">${price ? money(price.target) : "Pricing pending"}<small>guide price</small></span><button class="product-arrow" type="button" data-open-item="${item.id}" aria-label="Details for ${escape(item.title)}">↗</button></div>
      </div>
    </article>`;
  }

  function matches() {
    const query = state.search.trim().toLocaleLowerCase();
    let items = curated.filter(
      (item) =>
        (state.category === "all" || item.cat === state.category) &&
        (!state.savedOnly || saved.has(item.id)) &&
        (!query ||
          `${item.title} ${item.sub} ${categoryNames[item.cat]} ${item.id}`
            .toLocaleLowerCase()
            .includes(query)),
    );
    if (state.sort !== "curated") {
      items = [...items].sort(
        (a, b) =>
          (HNV_PRICES[a.id]?.target ?? Infinity) -
          (HNV_PRICES[b.id]?.target ?? Infinity),
      );
      if (state.sort === "price-desc") items.reverse();
    }
    return items;
  }

  function syncSaved() {
    document.querySelector("#header-saved")?.setAttribute("aria-label", `View saved finds (${saved.size})`);
    document.querySelectorAll(".saved-count").forEach((el) => {
      el.textContent = String(saved.size);
    });
    document.querySelectorAll("[data-save]").forEach((button) => {
      const item = inventory.find(
        (candidate) => candidate.id === button.dataset.save,
      );
      if (!item) return;
      const active = saved.has(item.id);
      button.setAttribute("aria-pressed", String(active));
      button.setAttribute(
        "aria-label",
        `${active ? "Unsave" : "Save"} ${item.title}`,
      );
      if (button.classList.contains("detail-save"))
        button.innerHTML = `${active ? "♥ Saved to your finds" : "♡ Save this find"}`;
      else
        button.innerHTML = `<span aria-hidden="true">${active ? "♥" : "♡"}</span>`;
    });
  }

  function render() {
    const items = matches();
    const shown = items.slice(0, state.limit);
    grid.innerHTML = shown.map(card).join("");
    const count = document.querySelector("#result-count");
    if (count)
      count.textContent = `${shown.length} of ${items.length} ${items.length === 1 ? "find" : "finds"}${state.savedOnly ? " saved" : ""}`;
    const empty = document.querySelector("#empty-state");
    if (empty) empty.hidden = items.length > 0;
    const more = document.querySelector("#load-more");
    if (more) more.hidden = shown.length >= items.length;
    document
      .querySelectorAll("#category-filters [data-category]")
      .forEach((button) => {
        const active = button.dataset.category === state.category;
        button.setAttribute("aria-pressed", String(active));
        button.classList.toggle("active", active);
      });
    document
      .querySelector("#saved-filter")
      ?.setAttribute("aria-pressed", String(state.savedOnly));
    syncSaved();
  }

  function reset() {
    Object.assign(state, {
      category: "all",
      search: "",
      sort: "curated",
      savedOnly: false,
      limit: 8,
    });
    if (search) search.value = "";
    if (sort) sort.value = "curated";
    updateHash("#collection");
    render();
  }

  function showDetails(id, trigger, changeHash = true) {
    const item = inventory.find((candidate) => candidate.id === id);
    const detail = document.querySelector("#product-detail");
    if (!item || !detail || !productDialog) return;
    if (!productDialog.open) {
      detailReturnHash = location.hash.startsWith("#item-")
        ? `#${item.cat}`
        : location.hash;
      lastTrigger = trigger || document.activeElement;
      lastTriggerItemId = id;
    }
    detailId = id;
    if (changeHash) updateHash(`#item-${id}`);
    const price = HNV_PRICES[id];
    const extra =
      id === "B15"
        ? "Guide: $40 for the embroidered jacket; $24 for the blouse. These are separate pieces."
        : id === "B18"
          ? "Guide price is per pair. Individual pairs range from $14 to $26."
          : id === "A2"
            ? "The visible shop tag is $60. The $125 guide is a separate research estimate, not a confirmed selling price."
            : id === "A20"
              ? "Designer and maker are unconfirmed. No Vitra or Easy Edges label has been verified."
              : id === "A1"
                ? "The lamp is Stiffel-style. A maker’s stamp has not been verified."
                : id === "A19"
                  ? "Availability as stock rather than room styling still needs confirmation."
                  : "";
    detail.innerHTML = `<div class="detail-layout">
      <div class="detail-image"><img src="${escape(item.img)}" ${photoSources(item, true)} alt="${escape(item.title)}" class="${isHidden(item) ? "mature-hidden" : ""}" width="640" height="800">${isHidden(item) ? `<button type="button" class="reveal-cover" data-reveal="${id}">View cover (18+)</button>` : ""}</div>
      <div class="detail-copy"><p class="detail-category">${categoryNames[item.cat]} / ${item.id}</p><h2 id="detail-title">${escape(item.title)}</h2><span class="status ${item.chip}">${statusNames[item.chip]}</span><p>${escape(item.sub)}</p>
      <p class="detail-price"><strong>${price ? money(price.target) : "Pricing pending"}</strong><small>Guide price</small></p>
      <button class="detail-save" type="button" data-save="${id}" aria-pressed="${saved.has(id)}">${saved.has(id) ? "♥ Saved to your finds" : "♡ Save this find"}</button>
      ${typeof HNV_ROOM_PRODUCTS !== "undefined" && HNV_ROOM_PRODUCTS.some((product) => product.id === id) ? `<button class="detail-save" type="button" data-try-room="${id}">Try it in your room ↗</button>` : ""}
      <div class="detail-notes"><h3>About this find</h3><p>${statusNotes[item.chip]}</p>${extra ? `<p>${extra}</p>` : ""}<p>Prices are provisional research guides from October 26, 2026. This preview does not take orders or payments.</p>
      ${price ? `<details><summary>Price research</summary><p>Comparable range: ${money(price.low)} to ${money(price.high)}.</p><p>${escape(price.conf)}</p></details>` : ""}</div></div></div>`;
    productDialog.setAttribute("aria-labelledby", "detail-title");
    if (!productDialog.open) productDialog.showModal();
  }

  function closeMobileNav() {
    const mobileNav = document.querySelector("#mobile-nav");
    if (mobileNav) mobileNav.hidden = true;
    document
      .querySelector("#menu-toggle")
      ?.setAttribute("aria-expanded", "false");
  }

  function readHash() {
    let hash;
    try {
      hash = decodeURIComponent(location.hash.slice(1));
    } catch {
      return;
    }
    const item = hash.startsWith("item-")
      ? inventory.find(
          (candidate) => candidate.id === hash.slice(5).toUpperCase(),
        )
      : null;
    if (item) {
      state.category = item.cat;
      state.search = "";
      state.savedOnly = false;
      if (search) search.value = "";
      const index = matches().findIndex(
        (candidate) => candidate.id === item.id,
      );
      state.limit = Math.max(8, Math.ceil((index + 1) / 8) * 8);
      render();
      showDetails(
        item.id,
        grid.querySelector(`#item-${item.id} .product-image`),
        false,
      );
      return;
    }
    if (productDialog?.open) productDialog.close();
    if (Object.hasOwn(categoryNames, hash) || hash === "collection" || !hash) {
      state.category = Object.hasOwn(categoryNames, hash) ? hash : "all";
      state.search = "";
      state.savedOnly = false;
      state.limit = 8;
      if (search) search.value = "";
      render();
      if (hash) scrollToCollection();
    }
  }

  document.addEventListener("click", (event) => {
    const button = event.target.closest("button, a");
    if (!button) return;
    if (button.matches("a") && button.closest("#mobile-nav")) closeMobileNav();

    if (button.hasAttribute("data-save")) {
      const id = button.dataset.save;
      if (saved.has(id)) saved.delete(id);
      else saved.add(id);
      try {
        localStorage.setItem(storageKey, JSON.stringify([...saved]));
      } catch {
        /* Session-only saves remain usable. */
      }
      if (state.savedOnly) {
        render();
        if (!productDialog?.open) focusFind(id, button);
      } else syncSaved();
      return;
    }
    if (button.hasAttribute("data-reveal")) {
      const id = button.dataset.reveal;
      revealed.add(id);
      render();
      if (productDialog?.open && detailId === id) {
        showDetails(id, lastTrigger, false);
        document.querySelector("#product-detail .detail-save")?.focus();
      } else
        document
          .querySelector(`#item-${id} .product-image`)
          ?.focus({ preventScroll: true });
      return;
    }
    if (button.hasAttribute("data-open-item")) {
      event.preventDefault();
      showDetails(button.dataset.openItem, button);
      return;
    }
    if (
      button.hasAttribute("data-category") ||
      button.hasAttribute("data-browse-category")
    ) {
      event.preventDefault();
      state.category = button.dataset.category || button.dataset.browseCategory;
      state.savedOnly = false;
      state.limit = 8;
      if (button.hasAttribute("data-browse-category")) {
        state.search = "";
        if (search) search.value = "";
      }
      updateHash(
        state.category === "all" ? "#collection" : `#${state.category}`,
      );
      render();
      if (button.hasAttribute("data-browse-category")) {
        closeMobileNav();
        scrollToCollection();
      }
      return;
    }
    if (button.id === "saved-filter") {
      state.savedOnly = !state.savedOnly;
      state.limit = 8;
      render();
      scrollToCollection();
      return;
    }
    if (button.id === "clear-filters") {
      reset();
      search?.focus();
      return;
    }
    if (button.id === "load-more") {
      const previousCount = grid.children.length;
      state.limit += 8;
      render();
      grid.children[previousCount]
        ?.querySelector("button")
        ?.focus({ preventScroll: true });
      return;
    }
    if (button.id === "menu-toggle") {
      const nav = document.querySelector("#mobile-nav");
      if (nav) {
        nav.hidden = !nav.hidden;
        button.setAttribute("aria-expanded", String(!nav.hidden));
      }
      return;
    }
    if (button.hasAttribute("data-close-dialog")) {
      button.closest("dialog")?.close();
      return;
    }
    if (button.hasAttribute("data-open-walkthrough") && tourDialog) {
      lastTrigger = button.closest("#mobile-nav")
        ? document.querySelector("#menu-toggle")
        : button;
      closeMobileNav();
      lastTriggerItemId = null;
      tourDialog.showModal();
      const video = document.querySelector("#tour-video");
      if (video && !matchMedia("(prefers-reduced-motion: reduce)").matches)
        video.play().catch(() => {});
    }
  });

  search?.addEventListener("input", () => {
    state.search = search.value;
    state.limit = 8;
    render();
  });
  sort?.addEventListener("change", () => {
    state.sort = sort.value;
    state.limit = 8;
    render();
  });
  [productDialog, tourDialog].filter(Boolean).forEach((dialog) => {
    dialog.addEventListener("close", () => {
      if (dialog === tourDialog) document.querySelector("#tour-video")?.pause();
      if (dialog === productDialog && location.hash === `#item-${detailId}`)
        updateHash(detailReturnHash, true);
      if (dialog === productDialog && location.hash === "#your-room") return;
      focusFind(lastTriggerItemId, lastTrigger);
    });
    dialog.addEventListener("click", (event) => {
      if (event.target !== dialog) return;
      const rect = dialog.getBoundingClientRect();
      if (
        event.clientX < rect.left ||
        event.clientX > rect.right ||
        event.clientY < rect.top ||
        event.clientY > rect.bottom
      )
        dialog.close();
    });
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeMobileNav();
  });
  window.addEventListener("hashchange", readHash);
  render();
  if (location.hash) readHash();
})();
