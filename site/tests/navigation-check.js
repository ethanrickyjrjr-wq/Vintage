// Paste into the browser console on the homepage (checks 4–8) or room.html (checks 9–10), local or live. Prints PASS/FAIL per check.
// Covers docs/codex-handoff-navigation.md acceptance lines 1 (same-document part), 4, 5, 6, 8, 9.
// ponytail: console script, no test runner. Move to Playwright only when a second page needs it.
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const $ = (s) => document.querySelector(s);
  const results = [];
  const check = (name, ok, detail) => { results.push(`${ok ? "PASS" : "FAIL"}  ${name}${ok ? "" : "  → " + detail}`); };
  const product = $("#product-dialog"), bag = $("#bag-dialog"), search = $("#search-input");
  const count = () => $("#result-count").textContent;
  const back = () => new Promise((r) => { addEventListener("popstate", () => r(true), { once: true }); setTimeout(() => r(false), 1500); history.back(); });

  if (product) {
  // 4 + 5: a detail must not wipe the search, whether closed by Back or by ×
  search.value = "lamp"; search.dispatchEvent(new Event("input", { bubbles: true })); await sleep(50);
  const lampCount = count();
  $("#product-grid .product-image").click(); await sleep(50);
  await back(); await sleep(250);
  check("4 Back closes detail and keeps search", !product.open && search.value === "lamp" && count() === lampCount,
    `open=${product.open} search="${search.value}" count="${count()}"`);
  await sleep(600); // a person pauses between Back and the next tap; two traversals inside ~300 ms can be dropped by the browser
  search.value = "lamp"; search.dispatchEvent(new Event("input", { bubbles: true })); await sleep(50);
  $("#product-grid .product-image").click(); await sleep(50);
  product.querySelector("[data-close-dialog]").click();
  // Closing the native dialog queues its close event and asynchronous history traversal.
  for (let i = 0; i < 30 && location.hash.startsWith("#item-"); i++) await sleep(50);
  check("5 × closes detail, keeps search, clears #item hash", !product.open && search.value === "lamp" && !location.hash.startsWith("#item-"),
    `open=${product.open} search="${search.value}" hash=${location.hash}`);
  search.value = ""; search.dispatchEvent(new Event("input", { bubbles: true })); await sleep(50);

  // 6: detail opened from the bag returns to the bag
  if (+$(".bag-count").textContent === 0) { $("[data-add-bag]").click(); await sleep(50); }
  $("#header-bag").click(); await sleep(50);
  const bagItems = bag.querySelectorAll(".bag-item").length;
  bag.querySelector(".bag-item-title").click(); await sleep(50);
  product.querySelector("[data-close-dialog]").click();
  for (let i = 0; i < 30 && !bag.open; i++) await sleep(50);
  check("6 closing a detail from the bag reopens the bag", bag.open && bag.querySelectorAll(".bag-item").length === bagItems,
    `bagOpen=${bag.open} items=${bag.querySelectorAll(".bag-item").length}/${bagItems}`);
  if (bag.open) bag.close(); await sleep(100);

  // 8: category taps must not pile up history entries
  const before = history.length;
  for (const c of ["lighting", "furniture", "decor"]) { $(`#category-filters [data-category="${c}"]`).click(); await sleep(20); }
  check("8 three category taps add no history entries", history.length === before, `added ${history.length - before}`);
  $('#category-filters [data-category="all"]').click();

  }
  if (document.getElementById("your-room")) {
  // 9: removing one placed find leaves the other, does not scroll, says so, and Undo restores it
  const id = (s) => document.getElementById(s);
  id("your-room").scrollIntoView({ behavior: "instant" });
  if (id("room-canvas").hidden) { id("room-use-example").click(); for (let i = 0; i < 50 && id("room-canvas").hidden; i++) await sleep(100); }
  const options = [...id("room-product").options];
  for (const option of options.slice(0, 2)) {
    id("room-product").value = option.value; id("room-product").dispatchEvent(new Event("change")); await sleep(20);
    if (!id("room-add").disabled) id("room-add").click(); await sleep(20);
    const place = [...id("room-tray").querySelectorAll("button")].find((b) => b.textContent === "Place" && !b.disabled);
    place?.click(); for (let i = 0; i < 50 && place && !place.disabled; i++) await sleep(100);
  }
  const layers = id("room-layers").children.length;
  const y = scrollY;
  id("room-delete").click(); await sleep(100);
  const afterRemove = id("room-layers").children.length;
  const status = id("room-status").textContent;
  id("room-undo").click(); await sleep(100);
  check("9 Remove takes one find, no scroll, status says removed, Undo restores",
    layers >= 2 && afterRemove === layers - 1 && scrollY === y && /removed/i.test(status) && id("room-layers").children.length === layers,
    `layers=${layers} afterRemove=${afterRemove} scrollDelta=${scrollY - y} status="${status}" afterUndo=${id("room-layers").children.length}`);

  // 10: an image dragged from the page must not replace the room; a file from the device must; the sample room is one tap away
  const stage = id("room-stage"), labelBefore = id("room-photo-label").textContent;
  const png = await new Promise((r) => { const c = document.createElement("canvas"); c.width = c.height = 240; const ctx = c.getContext("2d"); ctx.fillStyle = "#888"; ctx.fillRect(0, 0, 240, 240); c.toBlob(r, "image/png"); });
  const drop = (fromPage) => { const dt = new DataTransfer(); dt.items.add(new File([png], "drag.png", { type: "image/png" })); if (fromPage) dt.setData("text/uri-list", location.href); stage.dispatchEvent(new DragEvent("drop", { dataTransfer: dt, bubbles: true, cancelable: true })); };
  drop(true); await sleep(400);
  const pageDragIgnored = id("room-photo-label").textContent === labelBefore;
  drop(false); for (let i = 0; i < 30 && id("room-photo-label").textContent === labelBefore; i++) await sleep(100);
  const fileDropLoaded = /Your room/.test(id("room-photo-label").textContent);
  const sampleButtonShown = !id("room-sample-photo")?.hidden;
  id("room-sample-photo")?.click(); for (let i = 0; i < 50 && !/Sample room/.test(id("room-photo-label").textContent); i++) await sleep(100);
  check("10 page image drag ignored, device file loads, sample room one tap away",
    pageDragIgnored && fileDropLoaded && sampleButtonShown && /Sample room/.test(id("room-photo-label").textContent),
    `pageDragIgnored=${pageDragIgnored} fileDropLoaded=${fileDropLoaded} sampleButton=${sampleButtonShown} label="${id("room-photo-label").textContent}"`);

  }
  console.log(results.join("\n"));
  return results;
})();
