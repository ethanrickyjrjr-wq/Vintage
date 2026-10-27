import {
  cpSync,
  mkdirSync,
  readFileSync,
  readdirSync,
  unlinkSync,
  writeFileSync,
} from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const output = path.join(root, "dist");
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
console.log("Built Hollywood and Vine in site/dist.");
