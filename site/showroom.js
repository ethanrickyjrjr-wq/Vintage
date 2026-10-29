    const MODELS = [
      { title: "Glam velvet sofa", cat: "furniture", src: "assets/demo/models/GlamVelvetSofa.glb", yaw: 0, page: "https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/GlamVelvetSofa", credit: "Glam Velvet Sofa, © 2021 Wayfair, LLC, Eric Chadwick. CC BY 4.0." },
      { title: "Damask lounge chair", cat: "furniture", src: "assets/demo/models/ChairDamaskPurplegold.glb", yaw: 0, page: "https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/ChairDamaskPurplegold", credit: "Chair Damask Purple Gold, © 2021 Wayfair. CC BY 4.0." },
      { title: "Sneaker colorways", cat: "fashion", src: "assets/demo/models/MaterialsVariantsShoe.glb", yaw: 90, page: "https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/MaterialsVariantsShoe", credit: "Materials Variants Shoe, © 2021 Shopify. CC BY 4.0." },
      { title: "8mm film projector", cat: "media", src: "assets/demo/models/filmstrip_projector_8mm/filmstrip_projector_8mm_1k.gltf", yaw: 90, page: "https://polyhaven.com/a/filmstrip_projector_8mm", credit: "Filmstrip Projector 8mm by PeterM, Poly Haven. CC0." },
      { title: "Vintage oil lamp", cat: "lighting", src: "assets/demo/models/vintage_oil_lamp/vintage_oil_lamp_1k.gltf", yaw: 0,
        // The chimney is a BLEND material whose texture has no alpha channel, so it renders as an opaque black rod. Make it smoked glass.
        fix: (viewer) => viewer.model.getMaterialByName("vintage_oil_lamp_glass")?.pbrMetallicRoughness.setBaseColorFactor([1, 1, 1, 0.16]),
        page: "https://polyhaven.com/a/vintage_oil_lamp", credit: "Vintage Oil Lamp by Monsta3D, Poly Haven. CC0." },
      { title: "Mid-century lounge chair", cat: "furniture", src: "assets/demo/models/mid_century_lounge_chair/mid_century_lounge_chair_1k.gltf", yaw: 0, page: "https://polyhaven.com/a/mid_century_lounge_chair", credit: "Mid Century Lounge Chair by Kuutti Siitonen, Poly Haven. CC0." },
      { title: "Brass chandelier", cat: "lighting", src: "assets/demo/models/Chandelier_01/Chandelier_01_1k.gltf", yaw: 0, page: "https://polyhaven.com/a/Chandelier_01", credit: "Chandelier 01 by Kirill Sannikov, Poly Haven. CC0." },
      { title: "80s boombox", cat: "media", src: "assets/demo/models/boombox/boombox_1k.gltf", yaw: 0, page: "https://polyhaven.com/a/boombox", credit: "Boombox by Thomas Paul Mouilleron, Poly Haven. CC0." },
      { title: "Vintage video camera", cat: "media", src: "assets/demo/models/vintage_video_camera/vintage_video_camera_1k.gltf", yaw: 0, page: "https://polyhaven.com/a/vintage_video_camera", credit: "Vintage Video Camera, model and photography by Jenelle van Heerden, textures by James Ray Cock, Poly Haven. CC0." },
      { title: "Marble bust", cat: "art", src: "assets/demo/models/marble_bust_01/marble_bust_01_1k.gltf", yaw: 0, page: "https://polyhaven.com/a/marble_bust_01", credit: "Marble Bust 01 by Rico Cilliers, Poly Haven. CC0." },
      { title: "Porcelain horse", cat: "decor", src: "assets/demo/models/horse_statue_01/horse_statue_01_1k.gltf", yaw: 0, page: "https://polyhaven.com/a/horse_statue_01", credit: "Horse Statue 01 by Rico Cilliers, Poly Haven. CC0." },
    ];

const categoryNames = { furniture: "Furniture", fashion: "Fashion", media: "Music & media", lighting: "Lighting", art: "Art & mirrors", decor: "Glass & objects" };

const $ = (selector) => document.querySelector(selector);
const node = (tag, attrs = {}, text) => {
  const element = Object.assign(document.createElement(tag), attrs);
  if (text != null) element.textContent = text;
  return element;
};
try {
  document.documentElement.dataset.theme = localStorage.getItem("hnv-theme") ||
    (matchMedia("(prefers-color-scheme: dark)").matches ? "evening" : "day");
} catch {}

const mv = $("#mv"), stage = $("#stage"), status = $("#status");
const select = $("#model-select"), controls = $("#viewer-controls"), galleryButton = $("#make-photos");
const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
const VIEWS = { Front: [0, 80], "Three-quarter": [38, 70], Side: [90, 82], Back: [180, 80], Top: [0, 0] };
let current = MODELS[0], shootToken = 0, loaded = false;
const frames = (count) => new Promise((resolve) => {
  const tick = () => (--count <= 0 ? resolve() : requestAnimationFrame(tick));
  requestAnimationFrame(tick);
});
const orbit = (view) => `${VIEWS[view][0] + (current.yaw || 0)}deg ${VIEWS[view][1]}deg 105%`;
function stopSpin() {
  mv.removeAttribute("auto-rotate");
  spin.setAttribute("aria-pressed", "false");
}
function go(view) {
  stopSpin();
  mv.setAttribute("camera-orbit", orbit(view));
  if (reducedMotion.matches) mv.jumpCameraToGoal();
  viewChips.forEach((chip) => chip.setAttribute("aria-pressed", String(chip.textContent === view)));
}
const viewChips = Object.keys(VIEWS).map((name) => {
  const chip = node("button", { type: "button", className: "chip" }, name);
  chip.setAttribute("aria-pressed", "false");
  chip.addEventListener("click", () => go(name));
  $("#viewChips").append(chip);
  return chip;
});
const backdrops = {
  White: "#fcfaf7",
  Burgundy: "#451c2b",
  Pink: "radial-gradient(circle at 50% 40%, #e5a6b4, #7a3150 75%)",
  Gold: "linear-gradient(160deg, #f6e3a6, #c9a24a)",
  "The original room": "url(assets/photos/IMG_6610--960.webp) center 28% / cover #451c2b",
};
const backdropButtons = Object.entries(backdrops).map(([name, css], index) => {
  const chip = node("button", { type: "button", className: "chip" }, name);
  chip.setAttribute("aria-pressed", String(index === 0));
  chip.addEventListener("click", () => {
    backdropButtons.forEach((button) => button.setAttribute("aria-pressed", String(button === chip)));
    stage.style.background = css;
  });
  $("#backChips").append(chip);
  return chip;
});
const spin = node("button", { type: "button", className: "chip" }, "Auto-spin");
spin.setAttribute("aria-pressed", "false");
spin.addEventListener("click", () => {
  if (mv.hasAttribute("auto-rotate")) stopSpin();
  else {
    mv.setAttribute("auto-rotate", "");
    spin.setAttribute("aria-pressed", "true");
    viewChips.forEach((chip) => chip.setAttribute("aria-pressed", "false"));
  }
});
const shadow = node("button", { type: "button", className: "chip" }, "Shadow");
shadow.setAttribute("aria-pressed", "true");
shadow.addEventListener("click", () => {
  const on = shadow.getAttribute("aria-pressed") !== "true";
  shadow.setAttribute("aria-pressed", String(on));
  mv.setAttribute("shadow-intensity", on ? "1.1" : "0");
});
$("#toggleChips").append(spin, shadow);
reducedMotion.addEventListener("change", () => { if (reducedMotion.matches) stopSpin(); });
document.addEventListener("visibilitychange", () => { if (document.hidden) stopSpin(); });
mv.addEventListener("pointerdown", () => {
  stopSpin();
  viewChips.forEach((chip) => chip.setAttribute("aria-pressed", "false"));
});

// Crop exported geometry to its visible pixels, with room around each silhouette.
async function trim(url) {
  const img = new Image(); img.src = url; await img.decode();
  const canvas = document.createElement("canvas");
  canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
  const ctx = canvas.getContext("2d", { willReadFrequently: true });
  ctx.drawImage(img, 0, 0);
  const { data, width, height } = ctx.getImageData(0, 0, canvas.width, canvas.height);
  let x0 = width, y0 = height, x1 = -1, y1 = -1;
  for (let y = 0; y < height; y++) for (let x = 0; x < width; x++) {
    if (data[(y * width + x) * 4 + 3] <= 16) continue;
    x0 = Math.min(x0, x); y0 = Math.min(y0, y); x1 = Math.max(x1, x); y1 = Math.max(y1, y);
  }
  if (x1 < 0) return url;
  const pad = Math.round(Math.max(x1 - x0, y1 - y0) * .06);
  const sx = Math.max(0, x0 - pad), sy = Math.max(0, y0 - pad);
  const w = Math.min(width, x1 + pad + 1) - sx, h = Math.min(height, y1 + pad + 1) - sy;
  const out = document.createElement("canvas"); out.width = w; out.height = h;
  out.getContext("2d").drawImage(canvas, sx, sy, w, h, 0, 0, w, h);
  return out.toDataURL("image/webp", .9);
}
async function shoot() {
  if (!loaded) return;
  const token = ++shootToken, before = mv.getAttribute("camera-orbit"), shots = [];
  stopSpin();
  stage.classList.add("shooting");
  galleryButton.disabled = true;
  controls.disabled = true;
  try {
    for (const view of Object.keys(VIEWS)) {
      if (token !== shootToken) return;
      mv.setAttribute("camera-orbit", orbit(view)); mv.jumpCameraToGoal();
      await frames(3);
      if (token !== shootToken) return;
      shots.push([view, await trim(mv.toDataURL("image/webp", .9))]);
    }
    if (token !== shootToken) return;
    $("#shots").replaceChildren(...shots.map(([view, url]) => {
      const thumb = node("button", { type: "button", className: "thumb", title: `Show the ${view.toLowerCase()} view` });
      thumb.append(node("img", { src: url, alt: `${current.title}, ${view.toLowerCase()} view` }), node("span", {}, view));
      thumb.addEventListener("click", () => go(view));
      return thumb;
    }));
    status.textContent = "All five views are ready. Choose an angle below.";
    galleryButton.textContent = "Refresh the five views ↓";
  } catch {
    if (token === shootToken) status.textContent = "The gallery could not be prepared. Use the camera buttons or try again.";
  } finally {
    if (token === shootToken) {
      mv.setAttribute("camera-orbit", before); mv.jumpCameraToGoal();
      stage.classList.remove("shooting");
      galleryButton.disabled = !loaded; controls.disabled = !loaded;
    }
  }
}
galleryButton.addEventListener("click", shoot);
function clearGallery() {
  shootToken++;
  stage.classList.remove("shooting");
  $("#shots").replaceChildren();
  galleryButton.textContent = "See all five angles ↓";
  if (loaded) status.textContent = `${current.title}. Drag to rotate, or choose a camera view.`;
}
function showModel(index) {
  clearGallery(); stopSpin(); loaded = false;
  current = MODELS[index]; select.value = String(index);
  for (const element of [select, status, controls, galleryButton, $("#credit"), $("#piece-category"), $(".piece-selection"), $(".viewer-column")]) element.dataset.productCategory = current.cat;
  $("#piece-category").textContent = categoryNames[current.cat];
  status.textContent = `Loading ${current.title.toLowerCase()}…`;
  stage.setAttribute("aria-busy", "true");
  controls.disabled = true; galleryButton.disabled = true;
  $("#variantGroup").hidden = true;
  mv.removeAttribute("variant-name");
  mv.setAttribute("alt", `Interactive 3D sample: ${current.title}`);
  mv.setAttribute("camera-orbit", orbit("Three-quarter"));
  viewChips.forEach((chip) => chip.setAttribute("aria-pressed", String(chip.textContent === "Three-quarter")));
  mv.src = current.src;
  $("#credit").replaceChildren(node("span", {}, current.credit + " "), node("a", { href: current.page, target: "_blank", rel: "noreferrer" }, "Model source ↗"));
  const url = new URL(location.href); url.searchParams.set("piece", String(index + 1));
  history.replaceState(null, "", url);
}
mv.addEventListener("load", () => {
  loaded = true; stage.setAttribute("aria-busy", "false");
  controls.disabled = false; galleryButton.disabled = false;
  status.textContent = `${current.title}. Drag to rotate, or choose a camera view.`;
  const variants = mv.availableVariants || [], host = $("#variantChips");
  host.replaceChildren(); $("#variantGroup").hidden = variants.length < 2;
  const original = node("button", { type: "button", className: "chip" }, "Original");
  original.setAttribute("aria-pressed", "true");
  original.addEventListener("click", () => {
    clearGallery(); mv.removeAttribute("variant-name");
    host.querySelectorAll("button").forEach((button) => button.setAttribute("aria-pressed", String(button === original)));
  });
  host.append(original);
  variants.forEach((name) => {
    const chip = node("button", { type: "button", className: "chip" }, name);
    chip.setAttribute("aria-pressed", "false");
    chip.addEventListener("click", () => {
      clearGallery();
      host.querySelectorAll("button").forEach((button) => button.setAttribute("aria-pressed", String(button === chip)));
      mv.setAttribute("variant-name", name);
    });
    host.append(chip);
  });
  current.fix?.(mv);
});
mv.addEventListener("error", () => {
  clearGallery(); loaded = false;
  stage.setAttribute("aria-busy", "false"); controls.disabled = true; galleryButton.disabled = true;
  status.textContent = "This piece could not load. Choose another piece, or reload to try again.";
});
MODELS.forEach((model, index) => {
  const option = node("option", { value: String(index) }, model.title);
  option.dataset.productCategory = model.cat;
  select.append(option);
  const li = node("li", {}, model.credit + " ");
  li.dataset.productCategory = model.cat;
  li.append(node("a", { href: model.page, target: "_blank", rel: "noreferrer" }, "Source ↗"));
  $("#credits").append(li);
});
select.addEventListener("change", () => showModel(Number(select.value)));
$("#previous-piece").addEventListener("click", () => showModel((Number(select.value) + MODELS.length - 1) % MODELS.length));
$("#next-piece").addEventListener("click", () => showModel((Number(select.value) + 1) % MODELS.length));
// A real back when the visitor came from our own pages; otherwise the link target.
$(".collection-return").addEventListener("click", (event) => {
  if (history.length > 1 && document.referrer.startsWith(location.origin)) { event.preventDefault(); history.back(); }
});
const requestedPiece = Number(new URLSearchParams(location.search).get("piece"));
const initialPiece = Number.isInteger(requestedPiece) && requestedPiece >= 1 && requestedPiece <= MODELS.length ? requestedPiece - 1 : 0;
try {
  await customElements.whenDefined("model-viewer");
  showModel(initialPiece);
} catch { status.textContent = "The 3D viewer is unavailable. Return to the collection to explore our finds."; }
