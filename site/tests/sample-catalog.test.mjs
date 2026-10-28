import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import vm from "node:vm";
import test from "node:test";

const root = fileURLToPath(new URL("../", import.meta.url));
const read = file => readFileSync(path.join(root, file), "utf8");
const originals = vm.runInNewContext(`${read("catalog-data.js")}\nHNV_ITEMS`);
const { items, products, prices } = vm.runInNewContext(`${read("catalog-data.js")}\n${read("room-products.js")}\n${read("demo-products.js")}\n({items: HNV_ITEMS, products: HNV_ROOM_PRODUCTS, prices: HNV_PRICES})`);

test("the public sample collection contains every selected photograph and its own price", () => {
  assert.equal(originals.length, 35, "retain the actual inventory source");
  assert.equal(items.length, 52);
  assert.equal(new Set(items.map(item => item.id)).size, 52);
  assert.equal(new Set(items.map(item => item.img)).size, 52);
  assert.equal(new Set(items.map(item => item.cat)).size, 7);
  assert.equal(Object.keys(prices).length, 52);
  for (const item of items) {
    assert.equal(item.chip, "demo");
    assert.match(item.img, /^assets\/demo\/[\w-]+\.webp$/);
    assert.ok(existsSync(path.join(root, item.img)), item.img);
    assert.ok(prices[item.id].sample, `${item.id} must use an illustrative price`);
    assert.ok(Number.isFinite(prices[item.id].target) && prices[item.id].target > 0);
    assert.equal(prices[item.id].low, undefined, "do not inherit original price research");
    assert.match(item.source, /^https:\/\//, `${item.id} keeps its photograph source`);
  }
});

test("every sample keeps the same cutout from collection to room editor", () => {
  assert.equal(products.length, items.length);
  for (const item of items) {
    const product = products.find(product => product.id === item.id);
    assert.ok(product, item.id);
    assert.equal(product.overlay, item.img, item.id);
    for (const width of [480, 960]) {
      assert.ok(existsSync(path.join(root, item.img.replace("assets/demo/", "assets/thumbnails/samples-").replace(".webp", `--${width}.webp`))), `${item.id} has a ${width}px responsive photograph`);
    }
  }
});

test("the homepage initializes the sample collection before catalog and room controls", () => {
  const page = read("storefront.html");
  assert.ok(page.indexOf('src="demo-products.js"') > page.indexOf('src="room-products.js"'));
  assert.ok(page.indexOf('src="demo-products.js"') < page.indexOf('src="catalog.js"'));
  assert.ok(page.indexOf('id="collection"') < page.indexOf('class="departments'));
  assert.ok(!page.includes('id="load-more"'), "all finds are present without another click");
  assert.match(page, /Illustrative prices in USD/);
  assert.match(page, /disabled>Checkout coming soon/);
  assert.match(page, /photos-IMG_6610--960.webp/, "keep the original neon-lit room photograph");
  assert.ok(!page.includes('IMG_6617.webp'), "omit the unfinished selfie");
});
