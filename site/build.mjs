import { cpSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const output = path.join(root, "dist");
mkdirSync(output, { recursive: true });
for (const file of [
  "storefront.html",
  "storefront.css",
  "storefront.js",
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
});
console.log("Built Hollywood and Vine in site/dist.");
