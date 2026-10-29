import { arrangeRoom, constrainLayer, layerBox } from "./room-layout.js";
import { sampleRoomScene } from "./room-sample.js";

const form = document.querySelector("#room-form");
if (form) startEditor();

function startEditor() {
  const $ = id => document.getElementById(id);
  const canvas = $("room-canvas"), context = canvas.getContext("2d");
  const inventory = new Map(HNV_ITEMS.map(item => [item.id, item]));
  const products = HNV_ROOM_PRODUCTS.map(product => ({ ...inventory.get(product.id), ...product }));
  const productMap = new Map(products.map(product => [product.id, product]));
  const categoryNames = { lighting: "Lighting", furniture: "Furniture", decor: "Glass & objects", rugs: "Rugs & hides", art: "Art & mirrors", media: "Music & media" };
  const productGroups = Object.entries(categoryNames).map(([cat, title]) => ({ cat, title,
    products: products.filter(product => product.cat === cat).sort((a, b) => a.title.localeCompare(b.title)),
  })).filter(group => group.products.length);
  const textures = new Map();
  const state = { photo: null, sample: false, layers: [], picks: [], selected: null, history: [], unplaced: [], scene: null, busy: false, comparing: false, drag: null };
  const savedKey = "hollywood-and-vine-saved";
  let favorites = [], photoVersion = 0, frame = 0, worker = null, requestId = 0, cancelAnalysis = null, sizeStart = null;
  let loadingTimer = 0;
  const loadingLines = ["Setting the scene…", "Good taste takes a moment…", "Making room for a little drama…", "Bringing a little Holliewood home…", "Finding room for the unexpected…", "A little character is on its way…"];
  function loading(active) {
    clearInterval(loadingTimer);
    if (active) {
      let line = 0;
      $("room-working-title").textContent = loadingLines[line];
      loadingTimer = setInterval(() => {
        if (!document.hidden) $("room-working-title").textContent = loadingLines[++line % loadingLines.length];
      }, 3400);
    }
    document.dispatchEvent(new Event("hnv:room-working"));
  }
  const selectedProduct = () => productMap.get($("room-product").value);
  const selectedLayer = () => state.layers.find(layer => layer.id === state.selected);
  const photoAspect = () => canvas.width / canvas.height;
  function status(message, error = false) { $("room-status").textContent = message; $("room-status").classList.toggle("is-error", error); }
  // While the room is in use the address names the room, so a reload or tab restore lands here, not on the last category or find.
  function claimHash() { if (location.hash !== "#your-room") history.replaceState(null, "", "#your-room"); }
  function snapshot() { return { layers: state.layers.map(layer => ({ ...layer })), selected: state.selected, unplaced: state.unplaced.map(item => ({ ...item })) }; }
  function remember(previous = snapshot()) { state.history.push(previous); if (state.history.length > 30) state.history.shift(); }
  function change(callback) { remember(); callback(); state.comparing = false; refresh(); }
  function loadImage(source) {
    return new Promise((resolve, reject) => {
      const image = new Image(); image.onload = () => resolve(image);
      image.onerror = () => reject(new Error("That image couldn’t be opened. Please try again.")); image.src = source;
    });
  }
  async function texture(product) {
    if (textures.has(product.id)) return textures.get(product.id);
    const image = await loadImage(product.overlay);
    const source = document.createElement("canvas"); source.width = image.naturalWidth; source.height = image.naturalHeight;
    const ctx = source.getContext("2d", { willReadFrequently: true }); ctx.drawImage(image, 0, 0);
    // Ignore transparent cell padding for positioning, contact shadows and size.
    const { data } = ctx.getImageData(0, 0, source.width, source.height);
    let left = source.width, top = source.height, right = -1, bottom = -1;
    for (let y = 0; y < source.height; y++) for (let x = 0; x < source.width; x++) if (data[(y * source.width + x) * 4 + 3] > 12) {
      left = Math.min(left, x); top = Math.min(top, y); right = Math.max(right, x); bottom = Math.max(bottom, y);
    }
    if (right < left) throw new Error("This cutout is empty. Please try another find.");
    const trimmed = document.createElement("canvas"); trimmed.width = right - left + 1; trimmed.height = bottom - top + 1;
    trimmed.getContext("2d").drawImage(source, left, top, trimmed.width, trimmed.height, 0, 0, trimmed.width, trimmed.height);
    textures.set(product.id, trimmed); return trimmed;
  }
  function coordinate(event) {
    const bounds = canvas.getBoundingClientRect();
    const scale = Math.min(bounds.width / canvas.width, bounds.height / canvas.height);
    const width = canvas.width * scale, height = canvas.height * scale;
    return { x: (event.clientX - bounds.left - (bounds.width - width) / 2) / width,
      y: (event.clientY - bounds.top - (bounds.height - height) / 2) / height };
  }
  function draw(selection = true, original = state.comparing) {
    frame = 0; if (!state.photo) return;
    context.clearRect(0, 0, canvas.width, canvas.height); context.drawImage(state.photo, 0, 0);
    if (original) return;
    for (const layer of state.layers) {
      const image = textures.get(layer.id); if (!image) continue;
      const box = layerBox(layer, photoAspect());
      const x = box.x * canvas.width, y = box.y * canvas.height, w = box.w * canvas.width, h = box.h * canvas.height;
      context.save();
      if (["lamp", "floor", "decor", "media", "cushion"].includes(layer.kind)) {
        context.globalCompositeOperation = "multiply"; context.fillStyle = "rgb(35 20 18 / .24)";
        context.shadowColor = "rgb(20 12 10 / .35)"; context.shadowBlur = Math.max(3, w * .035);
        context.beginPath(); context.ellipse(x + w / 2, y + h - Math.max(1, w * .007), w * .37, Math.max(2, w * .025), 0, 0, Math.PI * 2); context.fill();
      }
      context.restore(); context.save();
      context.shadowColor = "rgb(20 12 10 / .2)"; context.shadowBlur = Math.max(2, w * .02); context.shadowOffsetY = w * .012;
      context.translate(x + w / 2, y); context.scale(layer.flip ? -1 : 1, 1); context.drawImage(image, -w / 2, 0, w, h); context.restore();
      if (selection && layer.id === state.selected) {
        const unit = canvas.width / canvas.getBoundingClientRect().width;
        context.save(); context.strokeStyle = "#fff"; context.lineWidth = 3 * unit; context.strokeRect(x, y, w, h);
        context.strokeStyle = "#451c2b"; context.lineWidth = unit; context.strokeRect(x, y, w, h);
        const size = 12 * unit; context.fillStyle = "#451c2b"; context.fillRect(x + w - size / 2, y + h - size / 2, size, size);
        context.strokeStyle = "#fff"; context.strokeRect(x + w - size / 2, y + h - size / 2, size, size); context.restore();
      }
    }
  }
  function scheduleDraw() { if (!frame) frame = requestAnimationFrame(() => draw()); }
  function button(text, label, action, disabled = false) {
    const element = document.createElement("button"); element.type = "button"; element.textContent = text;
    element.setAttribute("aria-label", label); element.disabled = disabled; element.addEventListener("click", action); return element;
  }
  function refresh() {
    const hasPhoto = !!state.photo, layer = selectedLayer();
    $("room-tray").replaceChildren(); $("room-tray-empty").hidden = state.picks.length > 0;
    for (const group of productGroups) {
      const picks = group.products.filter(product => state.picks.includes(product.id));
      if (!picks.length) continue;
      const section = document.createElement("li"), heading = document.createElement("h3"), list = document.createElement("ul");
      section.className = "room-picks-group"; section.dataset.productCategory = group.cat;
      heading.textContent = `${group.title} (${picks.length})`; list.className = "room-tray-items";
      section.append(heading, list); $("room-tray").append(section);
      for (const { id } of picks) {
        const product = productMap.get(id), row = document.createElement("li"), title = document.createElement("span");
        const image = document.createElement("img"); image.src = product.img; image.alt = ""; image.width = 34; image.height = 42; image.draggable = false;
        row.dataset.productCategory = product.cat;
        title.textContent = product.title; row.append(image, title);
        const present = state.layers.some(item => item.id === id);
        row.draggable = !!product.overlay && !present && !state.busy;
        row.addEventListener("dragstart", event => { event.dataTransfer.setData("application/x-hnv-find", id); event.dataTransfer.effectAllowed = "copy"; });
        row.append(button(present ? "In room" : product.overlay ? "Place" : "Photo needed", `Place ${product.title}`, () => place(id), state.busy || !hasPhoto || present || !product.overlay));
        row.append(button("×", `Remove ${product.title} from my picks`, () => { state.picks = state.picks.filter(item => item !== id); refresh(); }, state.busy));
        list.append(row);
      }
    }
    $("room-layers").replaceChildren();
    for (const item of state.layers) {
      const row = document.createElement("li"), control = button(productMap.get(item.id).title, `Select ${productMap.get(item.id).title}`, () => { state.selected = item.id; state.comparing = false; refresh(); }, state.busy);
      control.dataset.productCategory = productMap.get(item.id).cat;
      control.setAttribute("aria-pressed", String(item.id === state.selected)); row.append(control); $("room-layers").append(row);
    }
    $("room-layer-controls").hidden = !hasPhoto;
    $("room-size").disabled = state.busy || !layer;
    if (layer) { $("room-size").value = Math.round(layer.w * 100); $("room-size-value").value = `${Math.round(layer.w * 100)}%`; }
    for (const id of ["room-flip", "room-front", "room-delete"]) $(id).disabled = state.busy || !layer;
    $("room-flip").setAttribute("aria-pressed", String(!!layer?.flip));
    $("room-before").disabled = state.busy || !state.layers.length; $("room-before").setAttribute("aria-pressed", String(state.comparing));
    $("room-before").textContent = state.comparing ? "Show arrangement" : "Show original";
    $("room-undo").disabled = state.busy || !state.history.length;
    $("room-reset").disabled = state.busy || !hasPhoto || !state.layers.length && !state.unplaced.length;
    $("room-download").disabled = state.busy || !state.layers.length;
    $("room-decorate-picks").disabled = state.busy || !hasPhoto || !state.picks.length;
    $("room-decorate-favorites").disabled = state.busy || !hasPhoto || !favorites.length;
    $("room-favorites-count").textContent = favorites.length;
    const picked = state.picks.includes(selectedProduct().id);
    $("room-add").textContent = picked ? "In my picks ✓" : "Add to my picks +"; $("room-add").disabled = state.busy || picked;
    $("room-product").disabled = state.busy; $("room-file").disabled = state.busy;
    for (const control of $("room-product-groups").querySelectorAll("button")) control.disabled = state.busy;
    $("room-sample-photo").hidden = !hasPhoto || state.sample; $("room-sample-photo").disabled = state.busy;
    for (const id of ["room-change-photo", "room-upload-button", "room-use-example"]) $(id).disabled = state.busy;
    $("room-working").hidden = !state.busy; $("room-stage").setAttribute("aria-busy", String(state.busy));
    // Discofy is offered once a find is in the room; the ball itself only drops while that disco runs (disco.js owns it).
    if ((state.busy || !state.layers.length) && $("room-discofy").getAttribute("aria-pressed") === "true") $("room-discofy").click();
    $("room-discofy").hidden = !state.layers.length; $("room-discofy").disabled = state.busy;
    $("room-unplaced").hidden = !state.unplaced.length; $("room-unplaced-list").replaceChildren();
    for (const item of state.unplaced) {
      const row = document.createElement("li"); row.dataset.productCategory = inventory.get(item.id)?.cat || ""; row.textContent = `${inventory.get(item.id)?.title || item.id}: ${item.reason}`; $("room-unplaced-list").append(row);
    }
    draw();
  }
  function updateProduct() {
    const product = selectedProduct(); $("room-product-image").src = product.img; $("room-product-image").alt = product.title;
    $("room-product").dataset.productCategory = product.cat;
    $("room-add").dataset.productCategory = product.cat;
    document.querySelector(".room-selected-product").dataset.productCategory = product.cat;
    for (const control of $("room-product-groups").querySelectorAll("button")) {
      const selected = control.dataset.roomProduct === product.id;
      control.setAttribute("aria-pressed", String(selected));
      if (selected) control.closest("details").open = true;
    }
    $("room-product-title").textContent = product.title;
    const price = HNV_PRICES[product.id];
    $("room-product-price").textContent = product.overlay ? price ? `$${price.target.toLocaleString("en-US")} ${price.sample ? "sample price" : "guide price"}` : "Pricing pending" : "A clear product photo is needed to place this find.";
    $("room-product-details").href = `/#item-${product.id}`; refresh();
  }
  async function place(id, point) {
    const product = productMap.get(id); if (state.busy || !state.photo || !product?.overlay) return;
    if (state.layers.some(layer => layer.id === id)) { state.selected = id; refresh(); return; }
    const version = photoVersion;
    try {
      const image = await texture(product); if (version !== photoVersion || state.busy || state.layers.some(layer => layer.id === id)) return;
      change(() => {
        const layer = constrainLayer({ id, kind: product.kind, x: point?.x ?? .5, y: point?.y ?? .5, w: product.kind === "art" ? .2 : .17, ratio: image.height / image.width, flip: false }, photoAspect());
        state.layers.push(layer); state.selected = id; state.unplaced = state.unplaced.filter(item => item.id !== id);
      });
      claimHash();
      status("Placed. Drag the find or its corner to adjust it. Each find stays editable.");
      if (matchMedia("(max-width: 767px)").matches) canvas.scrollIntoView({ block: "center", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" });
      canvas.focus({ preventScroll: true });
    } catch (error) { status(error.message, true); }
  }
  async function upload(file, sample = false) {
    if (state.busy || !file) return;
    if (!["image/jpeg", "image/png", "image/webp"].includes(file.type)) { status("Choose a JPG, PNG or WebP. Convert HEIC photos to JPG first.", true); return; }
    if (!file.size || file.size > 15 * 1024 * 1024) { status("Choose a room photo smaller than 15 MB.", true); return; }
    const version = ++photoVersion, objectUrl = URL.createObjectURL(file);
    try {
      const image = await loadImage(objectUrl);
      if (image.naturalWidth < 200 || image.naturalHeight < 200) throw new Error("Use a room photo at least 200 pixels wide and tall.");
      const scale = Math.min(1, 1600 / Math.max(image.naturalWidth, image.naturalHeight));
      const normalized = document.createElement("canvas"); normalized.width = Math.round(image.naturalWidth * scale); normalized.height = Math.round(image.naturalHeight * scale);
      normalized.getContext("2d").drawImage(image, 0, 0, normalized.width, normalized.height);
      const photo = await loadImage(normalized.toDataURL("image/jpeg", .92)); if (version !== photoVersion) return;
      Object.assign(state, { photo, sample, layers: [], history: [], selected: null, unplaced: [], scene: null, comparing: false });
      canvas.width = photo.naturalWidth; canvas.height = photo.naturalHeight;
      $("room-upload").hidden = true; canvas.hidden = false; $("room-change-photo").hidden = false;
      $("room-photo-label").textContent = sample ? "Sample room / AI-generated example" : "Your room / placement sketch";
      claimHash(); refresh(); status("Your room is ready. Add finds to your picks, then place them or try a starting arrangement.");
    } catch (error) { if (version === photoVersion) status(error.message, true); }
    finally { URL.revokeObjectURL(objectUrl); $("room-file").value = ""; }
  }
  async function analyze(attempt = 0) {
    if (state.scene) return Promise.resolve(state.scene);
    if (state.sample) return sampleRoomScene();
    worker ??= new Worker(new URL("./room-segmentation.js", import.meta.url), { type: "module" });
    const analysisWorker = worker, id = ++requestId;
    const photo = document.createElement("canvas"), scale = Math.min(1, 1000 / Math.max(canvas.width, canvas.height));
    photo.width = Math.round(canvas.width * scale); photo.height = Math.round(canvas.height * scale);
    const ctx = photo.getContext("2d"); ctx.drawImage(state.photo, 0, 0, photo.width, photo.height);
    const pixels = ctx.getImageData(0, 0, photo.width, photo.height).data.buffer;
    return new Promise((resolve, reject) => {
      const finish = (error, result) => {
        clearTimeout(timeout); cancelAnalysis = null; analysisWorker.onmessage = null; analysisWorker.onerror = null;
        if (error) { analysisWorker.terminate(); if (worker === analysisWorker) worker = null; reject(error); }
        else resolve(result);
      };
      const timeout = setTimeout(() => finish(new Error("The room guide took too long. Your arrangement is still here; try placing your picks by hand.")), 180000);
      cancelAnalysis = () => finish(new Error("Room guide cancelled. Your last arrangement is still here."));
      analysisWorker.onerror = () => finish(new Error("The room guide couldn’t load on this device. You can still place every available cutout by hand."));
      analysisWorker.onmessage = ({ data }) => {
        if (data.requestId !== id) return;
        if (data.type === "progress") {
          $("room-working-label").textContent = data.message;
          if (Number.isFinite(data.progress)) $("room-progress").value = data.progress; else $("room-progress").removeAttribute("value");
        } else if (data.type === "result") finish(null, data);
        else if (data.type === "error") {
          console.warn("Room guide unavailable:", data.phase, data.diagnostic);
          const error = new Error(data.message || "The room guide couldn’t read this photo. Try placing your picks by hand.");
          error.retryable = data.retryable;
          finish(error);
        }
      };
      analysisWorker.postMessage({ requestId: id, width: photo.width, height: photo.height, pixels }, [pixels]);
    }).catch(error => {
      if (error.retryable && attempt === 0 && !state.cancelled) {
        $("room-working-label").textContent = "Download interrupted. Trying once more…";
        $("room-progress").removeAttribute("value");
        return analyze(1);
      }
      throw error;
    });
  }
  async function decorate(ids) {
    if (state.busy || !state.photo || !ids.length) return;
    state.busy = true; state.cancelled = false; $("room-working-label").textContent = state.sample ? "Arranging your finds in the sample room…" : "Loading the room guide on your device…"; $("room-progress").removeAttribute("value"); claimHash(); refresh(); loading(true);
    if (matchMedia("(max-width: 767px)").matches) $("room-stage").scrollIntoView({ block: "center", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" });
    try {
      const usable = [], excluded = [];
      for (const id of ids) {
        const product = productMap.get(id);
        if (!product) { excluded.push({ id, reason: "This find isn’t a room item." }); continue; }
        if (!product.overlay) { excluded.push({ id, reason: "A clear product cutout is needed." }); continue; }
        try { const image = await texture(product); usable.push({ ...product, ratio: image.height / image.width }); }
        catch { excluded.push({ id, reason: "This cutout couldn’t load. Try again or choose another find." }); }
      }
      if (state.cancelled) throw new Error("Room guide cancelled. Your last arrangement is still here.");
      const scene = usable.length ? await analyze() : null;
      if (scene) state.scene = scene;
      const result = scene ? arrangeRoom(usable, scene, photoAspect()) : { layers: [], unplaced: [] };
      remember(); state.unplaced = [...excluded, ...result.unplaced];
      if (result.layers.length) {
        Object.assign(state, { layers: result.layers, selected: result.layers.at(-1).id, comparing: false });
        status(`${result.layers.length} ${result.layers.length === 1 ? "find placed" : "finds placed"}${state.unplaced.length ? `; ${state.unplaced.length} left out` : ""}. Drag any find to make the arrangement yours.`);
      } else {
        const detail = state.unplaced.length === 1 ? state.unplaced[0].reason : "See the pieces left out below for details.";
        status(`We couldn’t suggest a starting position. ${detail}${state.layers.length ? " Your existing arrangement is unchanged." : " You can place available finds by hand."}`);
      }
    } catch (error) { status(error.message, true); }
    finally { state.busy = false; refresh(); loading(false); }
  }
  function readFavorites() {
    try { const stored = JSON.parse(localStorage.getItem(savedKey) || "[]"); favorites = Array.isArray(stored) ? [...new Set(stored.filter(id => inventory.has(id) && id !== "OWNER"))] : []; } catch { /* Keep session saves when storage is blocked. */ }
  }
  for (const group of productGroups) {
    const section = document.createElement("details"), heading = document.createElement("summary"), title = document.createElement("h3"), count = document.createElement("span"), list = document.createElement("div");
    section.className = "room-product-group"; section.name = "room-product-category"; section.dataset.productCategory = group.cat;
    title.textContent = group.title; count.textContent = `${group.products.length} finds`;
    heading.append(title, count); list.className = "room-product-options";
    for (const product of group.products) {
      const control = button("", `Choose ${product.title}`, () => { $("room-product").value = product.id; updateProduct(); });
      control.dataset.roomProduct = product.id; control.dataset.productCategory = product.cat;
      const image = document.createElement("img"), name = document.createElement("span");
      image.src = product.img.replace("assets/demo/", "assets/thumbnails/samples-").replace(".webp", "--480.webp");
      image.alt = ""; image.width = 40; image.height = 48; image.loading = "lazy";
      name.textContent = `${product.title}${product.overlay ? "" : " (photo needed)"}`;
      control.append(image, name); list.append(control);
    }
    section.append(heading, list); $("room-product-groups").append(section);
  }
  $("room-product").value = productGroups[0].products[0].id;
  readFavorites();
  document.addEventListener("hnv:saved-changed", ({ detail }) => { favorites = [...new Set(detail.filter(id => inventory.has(id) && id !== "OWNER"))]; refresh(); });
  window.addEventListener("storage", event => { if (event.key === savedKey || event.key === null) { readFavorites(); refresh(); } });
  form.addEventListener("submit", event => { event.preventDefault(); if (!$("room-add").disabled) { state.picks.push(selectedProduct().id); refresh(); status("Added to your picks. Choose Place to position it yourself, or decorate with your collection."); } });
  $("room-product").addEventListener("change", updateProduct);
  $("room-decorate-picks").addEventListener("click", () => decorate([...state.picks]));
  $("room-decorate-favorites").addEventListener("click", () => decorate([...favorites]));
  $("room-cancel").addEventListener("click", () => { state.cancelled = true; cancelAnalysis?.(); });
  for (const id of ["room-upload-button", "room-change-photo"]) $(id).addEventListener("click", () => $("room-file").click());
  $("room-file").addEventListener("change", () => upload($("room-file").files[0]));
  async function loadSample() {
    try { const response = await fetch("assets/rooms/example-room.webp"); if (!response.ok) throw new Error("The sample room couldn’t load. Try your own photo."); await upload(new File([await response.blob()], "Sample.webp", { type: "image/webp" }), true); }
    catch (error) { status(error.message, true); }
  }
  for (const id of ["room-use-example", "room-sample-photo"]) $(id).addEventListener("click", loadSample);
  // An image dragged from the page itself carries text/uri-list; a file from the device carries only Files.
  const fileDrop = (transfer) => transfer.types.includes("Files") && !transfer.types.includes("text/uri-list");
  $("room-stage").addEventListener("dragover", event => { if (fileDrop(event.dataTransfer) || event.dataTransfer.types.includes("application/x-hnv-find")) { event.preventDefault(); if (!state.busy) $("room-stage").classList.add("is-dragging"); } });
  $("room-stage").addEventListener("dragleave", () => $("room-stage").classList.remove("is-dragging"));
  $("room-stage").addEventListener("drop", event => {
    event.preventDefault(); $("room-stage").classList.remove("is-dragging");
    const id = event.dataTransfer.getData("application/x-hnv-find");
    if (productMap.has(id)) place(id, coordinate(event)); else if (fileDrop(event.dataTransfer)) upload(event.dataTransfer.files[0]);
  });
  canvas.addEventListener("pointerdown", event => {
    if (state.busy || !state.photo || state.comparing || event.button !== 0) return;
    const point = coordinate(event), current = selectedLayer(), currentBox = current && layerBox(current, photoAspect());
    const bounds = canvas.getBoundingClientRect(), scale = Math.min(bounds.width / canvas.width, bounds.height / canvas.height);
    const toleranceX = 20 / (canvas.width * scale), toleranceY = 20 / (canvas.height * scale);
    const resize = currentBox && Math.abs(point.x - currentBox.x - currentBox.w) < toleranceX && Math.abs(point.y - currentBox.y - currentBox.h) < toleranceY;
    const hit = resize ? current : [...state.layers].reverse().find(layer => { const b = layerBox(layer, photoAspect()); return point.x >= b.x && point.x <= b.x + b.w && point.y >= b.y && point.y <= b.y + b.h; });
    state.selected = hit?.id ?? null; refresh();
    if (!hit) return;
    state.drag = { start: point, layer: { ...hit }, previous: snapshot(), resize };
    canvas.setPointerCapture(event.pointerId); canvas.focus({ preventScroll: true });
  });
  canvas.addEventListener("pointermove", event => {
    if (!state.drag) return;
    const point = coordinate(event), drag = state.drag, layer = selectedLayer();
    if (drag.resize) {
      const b = layerBox(drag.layer, photoAspect());
      layer.w = Math.max(.025, point.x - b.x, (point.y - b.y) / (layer.ratio * photoAspect()));
      layer.x = b.x + layer.w / 2; layer.y = b.y + layer.w * layer.ratio * photoAspect() / 2;
    } else { layer.x = drag.layer.x + point.x - drag.start.x; layer.y = drag.layer.y + point.y - drag.start.y; }
    constrainLayer(layer, photoAspect()); $("room-size").value = Math.round(layer.w * 100); $("room-size-value").value = `${Math.round(layer.w * 100)}%`; scheduleDraw();
  });
  function finishDrag(cancel = false) {
    if (!state.drag) return;
    const { previous } = state.drag; state.drag = null;
    if (cancel) Object.assign(state, previous);
    else if (JSON.stringify(previous.layers) !== JSON.stringify(state.layers)) remember(previous);
    refresh();
  }
  canvas.addEventListener("pointerup", () => finishDrag()); canvas.addEventListener("pointercancel", () => finishDrag(true));
  canvas.addEventListener("lostpointercapture", () => finishDrag());
  canvas.addEventListener("keydown", event => {
    if (state.busy || state.comparing) return;
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "z") { event.preventDefault(); $("room-undo").click(); return; }
    const layer = selectedLayer(); if (!layer) return;
    if (["Delete", "Backspace"].includes(event.key)) { event.preventDefault(); $("room-delete").click(); return; }
    if (!["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes(event.key)) return;
    event.preventDefault(); change(() => { const axis = ["ArrowLeft", "ArrowRight"].includes(event.key) ? "x" : "y"; layer[axis] += (["ArrowLeft", "ArrowUp"].includes(event.key) ? -1 : 1) * (event.shiftKey ? .05 : .005); constrainLayer(layer, photoAspect()); });
  });
  $("room-size").addEventListener("input", () => {
    const layer = selectedLayer(); if (!layer || state.busy) return; sizeStart ??= snapshot();
    layer.w = Number($("room-size").value) / 100; constrainLayer(layer, photoAspect()); state.comparing = false;
    $("room-size-value").value = `${Math.round(layer.w * 100)}%`; draw();
  });
  $("room-size").addEventListener("change", () => { if (sizeStart) { remember(sizeStart); sizeStart = null; refresh(); } });
  $("room-flip").addEventListener("click", () => change(() => { selectedLayer().flip = !selectedLayer().flip; }));
  $("room-front").addEventListener("click", () => change(() => { const layer = selectedLayer(); state.layers = [...state.layers.filter(item => item !== layer), layer]; }));
  $("room-delete").addEventListener("click", () => change(() => { state.layers = state.layers.filter(layer => layer.id !== state.selected); state.selected = state.layers.at(-1)?.id ?? null; status("Removed. Undo brings it back."); }));
  $("room-before").addEventListener("click", () => { state.comparing = !state.comparing; refresh(); });
  $("room-undo").addEventListener("click", () => { const previous = state.history.pop(); if (previous) { Object.assign(state, previous, { comparing: false }); refresh(); status("Your last arrangement is back."); } });
  $("room-reset").addEventListener("click", () => change(() => { state.layers = []; state.selected = null; state.unplaced = []; status("The room is clear. Your photo and picks are still here, and Undo brings the layout back."); }));
  $("room-download").addEventListener("click", () => {
    draw(false, false);
    const output = document.createElement("canvas"), footer = Math.max(36, Math.round(canvas.width * .035));
    output.width = canvas.width; output.height = canvas.height + footer;
    const ctx = output.getContext("2d"); ctx.drawImage(canvas, 0, 0); ctx.fillStyle = "#451c2b"; ctx.fillRect(0, canvas.height, output.width, footer);
    ctx.fillStyle = "#f6efdf"; ctx.font = `${Math.max(10, footer * .33)}px Arial`;
    ctx.fillText("Holliewood & Vine / Placement sketch · proportions approximate", footer * .35, canvas.height + footer * .63, output.width - footer * .7);
    output.toBlob(blob => { if (!blob) return; const url = URL.createObjectURL(blob), link = document.createElement("a"); link.href = url; link.download = "holliewood-and-vine-your-room.png"; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000); }, "image/png"); draw();
  });
  document.addEventListener("click", event => {
    const control = event.target.closest("[data-try-room]"); if (!control || state.busy || !productMap.has(control.dataset.tryRoom)) return;
    event.preventDefault(); const id = control.dataset.tryRoom; $("room-product").value = id;
    // Name the room before closing the detail, so the detail does not step back through history behind us.
    if (!state.picks.includes(id)) state.picks.push(id); claimHash(); document.querySelector("#product-dialog")?.close(); updateProduct();
    $("your-room").scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" });
    if (state.photo && productMap.get(id).overlay) place(id); else (state.photo ? $("room-product") : $("room-upload-button")).focus({ preventScroll: true });
  });
  // On phones the directions start folded, so the picks sit right under the photo.
  if (matchMedia("(max-width: 767px)").matches) $("room-directions")?.removeAttribute("open");
  // "Try it in your room" on a homepage find arrives as room.html?try=<id>: the find is waiting in the picks.
  const tryId = new URLSearchParams(location.search).get("try");
  if (productMap.has(tryId)) { $("room-product").value = tryId; state.picks.push(tryId); history.replaceState(null, "", `${location.pathname}#your-room`); }
  updateProduct();
}
