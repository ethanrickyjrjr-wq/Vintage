import assert from "node:assert/strict";
import { readFileSync, readdirSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import test from "node:test";

const root = fileURLToPath(new URL("../", import.meta.url));
const read = (file) => readFileSync(path.join(root, file), "utf8");
const pages = readdirSync(root).filter((name) => /^idea-[a-z-]+\.html$/.test(name));
const hub = read("ideas.html");
const build = read("build.mjs");

test("the idea room has its pages and ships them", () => {
  assert.equal(pages.length, 13);
  for (const file of ["ideas.html", "ideas.css", "ideas.js", ...pages]) assert.match(build, new RegExp(`"${file}"`), `${file} missing from build.mjs`);
});

test("every idea page is a labeled, unindexed preview with a decision box the hub also has", () => {
  for (const file of pages) {
    const page = read(file);
    const id = file.slice(5, -5);
    assert.match(page, /<meta name="robots" content="noindex, nofollow"/, file);
    assert.match(page, /class="idea-banner"/, file);
    assert.match(page, new RegExp(`data-idea="${id}"`), file);
    assert.match(hub, new RegExp(`href="${file}"`), `hub must link ${file}`);
    assert.match(hub, new RegExp(`data-idea="${id}"`), `hub must carry the ${id} decision box`);
  }
});

test("the homepage stays out of it", () => {
  assert.doesNotMatch(read("storefront.html"), /href="ideas?(-[a-z-]+)?\.html"/);
});

test("only shipped images, and the shop is never spelled Hollywood", () => {
  for (const file of ["ideas.html", ...pages]) {
    const page = read(file);
    assert.doesNotMatch(page, /Hollywood\s*(&amp;|&|and)\s*Vine/, file);
    for (const [, src] of page.matchAll(/(?:src|srcset)="([^"\s]+)/g)) {
      assert.doesNotMatch(src, /assets\/photos\/IMG_\d+--(1920|3840)/, `${file}: large photos only ship from storefront.html`);
      assert.ok(existsSync(path.join(root, src)), `${file}: ${src} does not exist`);
    }
  }
});
