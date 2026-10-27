(() => {
  "use strict";
  const form = document.querySelector("#room-form");
  if (!form) return;
  const $ = (id) => document.getElementById(id);
  const canvas = $("room-canvas");
  const context = canvas.getContext("2d");
  const products = HNV_ROOM_PRODUCTS.map((product) => ({
    ...HNV_ITEMS.find((item) => item.id === product.id), ...product,
  })).filter((product) => product.title);
  const state = {
    original: null, current: null, history: [], point: null, box: null,
    drag: null, overlay: null, busy: false, comparing: false, generated: false, aiAvailable: false,
  };
  let imageVersion = 0;
  let uploadVersion = 0;
  let frame = 0;
  const mode = () => form.elements["room-mode"].value;
  const selected = () => products.find((product) => product.id === $("room-product").value);
  function status(message, error = false) {
    $("room-status").textContent = message;
    $("room-status").classList.toggle("is-error", error);
  }
  function loadImage(source) {
    return new Promise((resolve, reject) => {
      const image = new Image();
      image.onload = () => resolve(image);
      image.onerror = () => reject(new Error("That photo could not be opened. Please try a JPG, PNG or WebP."));
      image.src = source;
    });
  }
  function coordinates(event) {
    const bounds = canvas.getBoundingClientRect();
    // object-fit: contain may leave space above/below a wide or tall photograph.
    const scale = Math.min(bounds.width / canvas.width, bounds.height / canvas.height);
    const width = canvas.width * scale;
    const height = canvas.height * scale;
    return {
      x: Math.max(0, Math.min(1, (event.clientX - bounds.left - (bounds.width - width) / 2) / width)),
      y: Math.max(0, Math.min(1, (event.clientY - bounds.top - (bounds.height - height) / 2) / height)),
    };
  }
  function syncControls() {
    const hasPhoto = !!state.current;
    const localPlacement = mode() === "place" && !!state.overlay;
    $("room-generate").disabled = state.busy || (!localPlacement && !state.aiAvailable) || !hasPhoto ||
      (mode() === "place" && !state.point) ||
      (mode() === "replace" && !state.box && !$("room-replace-target").value.trim());
    $("room-generate").innerHTML = `${localPlacement ? "Keep this placement" : mode() === "decorate" ? "Decorate my room" : mode() === "replace" ? "Replace with this find" : "Render this placement"} <span aria-hidden="true">↗</span>`;
    $("room-before").disabled = state.busy || (state.current === state.original && !state.point);
    $("room-before").setAttribute("aria-pressed", String(state.comparing));
    $("room-before").textContent = state.comparing ? "Show preview" : "Show original";
    $("room-undo").disabled = state.busy || (!state.history.length && !state.point && !state.box);
    $("room-reset").disabled = state.busy || !hasPhoto;
    $("room-download").disabled = state.busy || !hasPhoto || (state.current === state.original && !(state.point && state.overlay));
    $("room-change-photo").disabled = state.busy;
    $("room-file").disabled = state.busy;
    form.querySelectorAll("input, select, textarea").forEach((input) => { input.disabled = state.busy; });
    $("room-working").hidden = !state.busy;
    $("room-stage").setAttribute("aria-busy", String(state.busy));
    $("room-size-controls").hidden = mode() !== "place";
    $("room-replace-controls").hidden = mode() !== "replace";
  }
  function draw(includeSelection = true, includeMarker = true) {
    frame = 0;
    const photo = state.comparing ? state.original : state.current;
    if (!photo) return;
    canvas.width = photo.image.naturalWidth;
    canvas.height = photo.image.naturalHeight;
    context.drawImage(photo.image, 0, 0);
    if (!includeSelection || state.comparing) return;
    const unit = canvas.width / 800;
    if (mode() === "place" && state.point) {
      const x = state.point.x * canvas.width;
      const y = state.point.y * canvas.height;
      if (state.overlay) {
        const width = canvas.width * Number($("room-size").value) / 100;
        const height = width * state.overlay.naturalHeight / state.overlay.naturalWidth;
        context.save();
        context.globalAlpha = .9;
        const outline = selected().outline;
        if (outline) {
          context.beginPath();
          outline.forEach(([px, py], index) => context[index ? "lineTo" : "moveTo"](x - width / 2 + px * width, y - height / 2 + py * height));
          context.closePath(); context.clip();
        }
        context.drawImage(state.overlay, x - width / 2, y - height / 2, width, height);
        context.restore();
      }
      if (includeMarker) {
      context.beginPath();
      context.arc(x, y, 12 * unit, 0, Math.PI * 2);
      context.fillStyle = "#451c2b";
      context.fill();
      context.strokeStyle = "#f6efdf";
      context.lineWidth = 2 * unit;
      context.stroke();
      context.fillStyle = "#f6efdf";
      context.font = `${16 * unit}px Arial`;
      context.textAlign = "center";
      context.textBaseline = "middle";
      context.fillText("+", x, y);
      }
    }
    if (mode() === "replace" && state.box) {
      const { x, y, width, height } = state.box;
      context.fillStyle = "#e5a6b455";
      context.fillRect(x * canvas.width, y * canvas.height, width * canvas.width, height * canvas.height);
      context.strokeStyle = "#f6efdf";
      context.lineWidth = 3 * unit;
      context.strokeRect(x * canvas.width, y * canvas.height, width * canvas.width, height * canvas.height);
      context.strokeStyle = "#451c2b";
      context.lineWidth = unit;
      context.setLineDash([6 * unit, 4 * unit]);
      context.strokeRect(x * canvas.width, y * canvas.height, width * canvas.width, height * canvas.height);
      context.setLineDash([]);
    }
  }
  function scheduleDraw() { if (!frame) frame = requestAnimationFrame(() => draw()); }
  function guidance() {
    if (!state.current) return;
    const messages = {
      place: selected().overlay ? "Click a spot, adjust the size, then keep your placement. Local cutouts stay exactly where you put them." : "Click a spot, then render this find from its catalog photo. AI may adjust its position or details.",
      decorate: "Ready when you are. Decorate will choose a spot that suits this find and your room.",
      replace: "Draw a box around what you want to replace, or describe the item. We’ll remove it and try your find there.",
    };
    status(messages[mode()]);
  }
  async function updateProduct() {
    const product = selected();
    $("room-product-image").src = product.img;
    $("room-product-image").alt = product.title;
    $("room-product-title").textContent = product.title;
    const price = HNV_PRICES[product.id];
    $("room-product-price").textContent = price ? `$${price.target.toLocaleString("en-US")} guide price` : "Pricing pending";
    $("room-product-details").href = `#item-${product.id}`;
    state.overlay = null;
    state.comparing = false;
    const version = ++imageVersion;
    draw(); syncControls(); guidance();
    if (product.overlay) {
      try {
        const image = await loadImage(product.overlay);
        if (version === imageVersion) { state.overlay = image; draw(); syncControls(); }
      } catch { /* The placement marker remains available if a cutout fails. */ }
    }
  }
  async function upload(file) {
    if (state.busy || !file) return;
    if (!["image/jpeg", "image/png", "image/webp"].includes(file.type)) {
      status("Please choose a JPG, PNG or WebP room photo. Convert HEIC photos to JPG first.", true); return;
    }
    if (!file.size || file.size > 15 * 1024 * 1024) {
      status("Please choose a photo smaller than 15 MB.", true); return;
    }
    const version = ++uploadVersion;
    const objectUrl = URL.createObjectURL(file);
    try {
      const image = await loadImage(objectUrl);
      if (image.naturalWidth < 200 || image.naturalHeight < 200) throw new Error("Use a room photo at least 200 pixels wide and tall.");
      // Re-encoding strips EXIF/GPS metadata and bounds the service payload.
      const scale = Math.min(1, 1600 / Math.max(image.naturalWidth, image.naturalHeight));
      const normalized = document.createElement("canvas");
      normalized.width = Math.round(image.naturalWidth * scale);
      normalized.height = Math.round(image.naturalHeight * scale);
      const ctx = normalized.getContext("2d");
      ctx.fillStyle = "#fff";
      ctx.fillRect(0, 0, normalized.width, normalized.height);
      ctx.drawImage(image, 0, 0, normalized.width, normalized.height);
      const url = normalized.toDataURL("image/jpeg", .88);
      const photo = { url, image: await loadImage(url), kind: "original" };
      if (version !== uploadVersion) return;
      Object.assign(state, { original: photo, current: photo, history: [], point: null, box: null, comparing: false, generated: false });
      $("room-upload").hidden = true;
      canvas.hidden = false;
      $("room-change-photo").hidden = false;
      $("room-photo-label").textContent = "Your room / placement sketch";
      draw(); syncControls(); guidance();
    } catch (error) { if (version === uploadVersion) status(error.message, true); }
    finally { URL.revokeObjectURL(objectUrl); $("room-file").value = ""; }
  }
  products.forEach((product) => {
    const option = document.createElement("option");
    option.value = product.id; option.textContent = product.title;
    $("room-product").append(option);
  });
  $("room-upload-button").addEventListener("click", () => $("room-file").click());
  $("room-change-photo").addEventListener("click", () => $("room-file").click());
  $("room-file").addEventListener("change", () => upload($("room-file").files[0]));
  $("room-use-example").addEventListener("click", async () => {
    try {
      const response = await fetch("assets/rooms/example-room.webp");
      if (!response.ok) throw new Error("The sample room couldn’t be opened. Please try your own photo.");
      await upload(new File([await response.blob()], "Sample room.webp", { type: "image/webp" }));
      $("room-photo-label").textContent = "Sample room / AI-generated example";
    } catch (error) { status(error.message, true); }
  });
  $("room-demo-video").closest("details").addEventListener("toggle", (event) => {
    const video = $("room-demo-video");
    if (!event.currentTarget.open) video.pause();
    else if (!matchMedia("(prefers-reduced-motion: reduce)").matches) video.play().catch(() => {});
  });
  $("room-stage").addEventListener("dragover", (event) => { event.preventDefault(); if (!state.busy) $("room-stage").classList.add("is-dragging"); });
  $("room-stage").addEventListener("dragleave", () => $("room-stage").classList.remove("is-dragging"));
  $("room-stage").addEventListener("drop", (event) => { event.preventDefault(); $("room-stage").classList.remove("is-dragging"); upload(event.dataTransfer.files[0]); });
  $("room-product").addEventListener("change", updateProduct);
  form.querySelectorAll('[name="room-mode"]').forEach((input) => input.addEventListener("change", () => {
    state.comparing = false; state.drag = null; syncControls(); draw(); guidance();
  }));
  $("room-size").addEventListener("input", () => { $("room-size-value").value = `${$("room-size").value}%`; scheduleDraw(); });
  $("room-replace-target").addEventListener("input", syncControls);
  $("room-clear-selection").addEventListener("click", () => { state.box = null; draw(); syncControls(); });
  canvas.addEventListener("pointerdown", (event) => {
    if (state.busy || !state.current || mode() === "decorate" || event.button !== 0) return;
    state.comparing = false;
    const point = coordinates(event);
    state.drag = point;
    if (mode() === "place") state.point = point;
    else state.box = null;
    canvas.setPointerCapture(event.pointerId);
    canvas.focus({ preventScroll: true });
    draw(); syncControls();
  });
  canvas.addEventListener("pointermove", (event) => {
    if (!state.drag) return;
    const point = coordinates(event);
    if (mode() === "place") state.point = point;
    else state.box = { x: Math.min(state.drag.x, point.x), y: Math.min(state.drag.y, point.y), width: Math.abs(point.x - state.drag.x), height: Math.abs(point.y - state.drag.y) };
    scheduleDraw();
  });
  function finishDrag() {
    if (!state.drag) return;
    state.drag = null;
    if (state.box && (state.box.width < .025 || state.box.height < .025)) {
      state.box = null; status("Draw a box around the whole item, or describe it in the replacement field.", true);
    } else if (mode() === "place") status(state.overlay ? "Spot selected. Adjust the size, then choose Keep this placement." : "Spot selected. Choose Render this placement to create an AI preview.");
    else status("Area marked. Choose Replace with this find to create your preview.");
    draw(); syncControls();
  }
  canvas.addEventListener("pointerup", finishDrag);
  canvas.addEventListener("pointercancel", finishDrag);
  canvas.addEventListener("keydown", (event) => {
    if (state.busy || mode() !== "place" || !["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes(event.key)) return;
    event.preventDefault(); state.comparing = false;
    state.point ??= { x: .5, y: .5 };
    const axis = ["ArrowLeft", "ArrowRight"].includes(event.key) ? "x" : "y";
    const direction = ["ArrowLeft", "ArrowUp"].includes(event.key) ? -1 : 1;
    state.point[axis] = Math.max(0, Math.min(1, state.point[axis] + direction * (event.shiftKey ? .05 : .01)));
    draw(); syncControls(); status("Spot selected. Arrow keys move the find; Shift moves it farther.");
  });
  $("room-before").addEventListener("click", () => { state.comparing = !state.comparing; draw(); syncControls(); });
  $("room-undo").addEventListener("click", () => {
    if (state.point || state.box) {
      state.point = null; state.box = null; state.comparing = false;
      draw(); syncControls(); guidance(); return;
    }
    const previous = state.history.pop();
    if (!previous) return;
    state.current = previous; state.generated = previous.kind === "ai";
    state.comparing = false; state.point = null; state.box = null;
    $("room-photo-label").textContent = state.generated ? "Your room / AI styling preview" : "Your room / placement sketch";
    draw(); syncControls(); guidance();
  });
  $("room-reset").addEventListener("click", () => {
    Object.assign(state, { current: state.original, history: [], point: null, box: null, comparing: false, generated: false });
    $("room-photo-label").textContent = "Your room / placement sketch";
    draw(); syncControls(); guidance();
  });
  $("room-download").addEventListener("click", () => {
    // Export what is currently shown, with an honest label on sketches and renders.
    const sketch = mode() === "place" && state.point && state.overlay && !state.comparing;
    draw(!!sketch, false);
    const output = document.createElement("canvas");
    const footer = Math.max(36, Math.round(canvas.width * .035));
    output.width = canvas.width; output.height = canvas.height + footer;
    const ctx = output.getContext("2d");
    ctx.drawImage(canvas, 0, 0);
    ctx.fillStyle = "#451c2b"; ctx.fillRect(0, canvas.height, output.width, footer);
    ctx.fillStyle = "#f6efdf"; ctx.font = `${Math.max(10, footer * .33)}px Arial`;
    const label = state.comparing ? "Original photo" : sketch || state.current.kind === "sketch" ? "Placement sketch · proportions approximate" : "AI styling preview · proportions approximate";
    ctx.fillText(`Hollywood & Vine / ${label}`, footer * .35, canvas.height + footer * .63, output.width - footer * .7);
    output.toBlob((blob) => {
      if (!blob) return;
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a"); link.href = url; link.download = "hollywood-and-vine-your-room.png"; link.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
    }, "image/png");
    draw();
  });
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if ($("room-generate").disabled) return;
    if (mode() === "place" && state.overlay && state.point) {
      // Keep exact browser placement without sending the room to any service.
      $("room-generate").disabled = true;
      state.comparing = false;
      draw(true, false);
      const url = canvas.toDataURL("image/jpeg", .94);
      const photo = { url, image: await loadImage(url), kind: "sketch" };
      state.history.push(state.current);
      if (state.history.length > 5) state.history.shift();
      Object.assign(state, { current: photo, generated: false, point: null, box: null });
      $("room-photo-label").textContent = "Your room / placement sketch";
      draw(); syncControls();
      status("Placement kept. Add another find, compare with your original, or download your room. No photo was sent to the AI service.");
      return;
    }
    state.busy = true; state.comparing = false;
    $("room-working-label").textContent = mode() === "replace" ? "Making room for your find…" : "Finding its place…";
    draw(); syncControls(); status("Creating your AI preview. Keep this page open.");
    try {
      const response = await fetch("/api/room-preview", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ image: state.current.url, productId: selected().id, mode: mode(), point: state.point, box: state.box, size: Number($("room-size").value) / 100, target: $("room-replace-target").value.trim(), notes: $("room-notes").value.trim() }),
        signal: AbortSignal.timeout(120000),
      });
      if (!(response.headers.get("content-type") || "").includes("application/json")) throw new Error("AI room previews are not connected on this preview server yet. Your placement sketch is still available.");
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "Your preview could not be created. Please try again.");
      if (!/^data:image\/(png|jpeg|webp);base64,/.test(result.image || "")) throw new Error("The image service did not return a preview. Please try again.");
      const photo = { url: result.image, image: await loadImage(result.image), kind: "ai" };
      state.history.push(state.current);
      if (state.history.length > 5) state.history.shift();
      Object.assign(state, { current: photo, generated: true, point: null, box: null });
      $("room-photo-label").textContent = "Your room / AI styling preview";
      status("Here’s your room with a little more character. Compare with the original, try another find, or download your preview.");
    } catch (error) {
      status(["TimeoutError", "AbortError"].includes(error.name) ? "The image service took too long. Your photo and placement are still here; please try again." : error.message, true);
    } finally { state.busy = false; draw(); syncControls(); }
  });
  document.addEventListener("click", (event) => {
    const button = event.target.closest("[data-try-room]");
    if (!button || state.busy) return;
    event.preventDefault();
    $("room-product").value = button.dataset.tryRoom;
    document.querySelector("#product-dialog")?.close();
    updateProduct();
    history.pushState(null, "", "#your-room");
    $("your-room").scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" });
    (state.current ? $("room-product") : $("room-upload-button")).focus({ preventScroll: true });
  });
  updateProduct(); syncControls();
  fetch("/api/room-preview", { headers: { accept: "application/json" } }).then(async (response) => {
    if (!(response.headers.get("content-type") || "").includes("application/json")) return;
    const service = await response.json();
    state.aiAvailable = !!service.available;
    $("room-service").textContent = service.available ? `Up to ${service.dailyLimit} AI previews per day on this connection.` : "AI previews are not available yet. Try a placement sketch with the urn lamp, chandelier, or either original artwork.";
    syncControls();
  }).catch(() => { $("room-service").textContent = "The AI service is unavailable right now. Local placement sketches are still available."; });
})();
