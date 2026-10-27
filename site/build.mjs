import {
  cpSync,
  existsSync,
  mkdirSync,
  readFileSync,
  readdirSync,
  rmSync,
  unlinkSync,
  writeFileSync,
} from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const root = path.dirname(fileURLToPath(import.meta.url));
const dist = path.join(root, "dist");
if (path.dirname(dist) !== root || path.basename(dist) !== "dist") throw new Error("Build output must stay inside this site.");
// Keep the output directory itself: another Windows preview may hold it open.
if (existsSync(dist)) for (const name of readdirSync(dist)) {
  const entry = path.join(dist, name);
  if (path.dirname(entry) !== dist) throw new Error("Invalid build output path.");
  rmSync(entry, { recursive: true, force: true });
}
const output = path.join(dist, "client");
const page = readFileSync(path.join(root, "storefront.html"), "utf8");
const largePhotos = new Set(
  [...page.matchAll(/assets\/photos\/(IMG_\d+--(?:1920|3840)\.webp)/g)].map(
    (match) => match[1],
  ),
);
const frames = new Set(
  [...page.matchAll(/assets\/frames\/([^"\s]+)/g)].map((match) => match[1]),
);
function shipAsset(file) {
  const name = path.basename(file);
  if (/^IMG_\d+--(?:1920|3840)\.webp$/.test(name)) return largePhotos.has(name);
  if (path.basename(path.dirname(file)) === "frames" && name.endsWith(".webp"))
    return frames.has(name);
  return true;
}
mkdirSync(output, { recursive: true });
for (const file of [
  "storefront.html",
  "storefront.css",
  "atmosphere.css",
  "storefront.js",
  "disco.js",
  "disco-music.js",
  "catalog.js",
  "catalog-data.js",
  "room-products.js",
  "room-preview.css",
  "room-preview.js",
  "room-layout.js",
  "room-segmentation.js",
  "favicon.svg",
]) {
  cpSync(path.join(root, file), path.join(output, file));
}
writeFileSync(
  path.join(output, "index.html"),
  readFileSync(path.join(root, "storefront.html")),
);
cpSync(path.join(root, "assets"), path.join(output, "assets"), {
  recursive: true,
  filter: shipAsset,
});
// Remove obsolete exports from previous builds; retain every source photograph.
for (const folder of ["photos", "frames"]) {
  const directory = path.join(output, "assets", folder);
  for (const name of readdirSync(directory)) {
    const file = path.join(directory, name);
    if (!shipAsset(file)) unlinkSync(file);
  }
}
const catalog = vm.runInNewContext(`${readFileSync(path.join(root, "catalog-data.js"), "utf8")}\n${readFileSync(path.join(root, "room-products.js"), "utf8")}\nHNV_ROOM_PRODUCTS.map(product => ({ ...HNV_ITEMS.find(item => item.id === product.id), ...product }))`);
// Smaller originals remain the reference; never send the editorial cutouts to AI.
for (const product of catalog) {
  product.img = product.img.replace(/(assets\/photos\/IMG_\d+)\.webp$/, "$1--960.webp");
}
mkdirSync(path.join(dist, "server"), { recursive: true });
mkdirSync(path.join(dist, ".openai"), { recursive: true });
writeFileSync(path.join(dist, "server/index.js"), readFileSync(path.join(root, "room-worker.mjs"), "utf8").replace("/* ROOM_CATALOG */ []", JSON.stringify(catalog)));
cpSync(path.join(root, ".openai/hosting.json"), path.join(dist, ".openai/hosting.json"));
writeFileSync(path.join(dist, "server/wrangler.json"), JSON.stringify({
  name: "hollywood-and-vine", main: "index.js", compatibility_date: "2026-05-15",
  assets: { directory: "../client", binding: "ASSETS", run_worker_first: ["/api/*"] },
  d1_databases: [{ binding: "DB", database_name: "room-previews", database_id: "00000000-0000-4000-8000-000000000000" }],
}));
console.log("Built Hollywood and Vine: static assets in dist/client, room API in dist/server.");
