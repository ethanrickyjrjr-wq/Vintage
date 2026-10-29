import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const read = (file) => readFileSync(new URL(`../${file}`, import.meta.url), "utf8");
const home = read("storefront.html");
const room = read("room.html");
const nav = (html, name) => html.match(new RegExp(`<nav[^>]*class="${name}"[\\s\\S]*?</nav>`))?.[0] ?? "";

test("the homepage is lighter: collection, three doors, owner", () => {
  for (const gone of ['id="your-room"', 'id="hire-hollie"', 'class="departments', 'class="browse-nav', 'class="disco-note', 'class="showroom-invitation']) {
    assert.ok(!home.includes(gone), `homepage still has ${gone}`);
  }
  assert.ok(home.indexOf('id="collection"') < home.indexOf('class="doors') && home.indexOf('class="doors') < home.indexOf('id="owner"'));
  for (const href of ["room.html", "hire.html", "showroom.html"]) assert.match(home, new RegExp(`class="door reveal" href="${href}"`));
  for (const name of ["desktop-nav", "mobile-nav", "footer-nav"]) for (const html of [home, room]) assert.match(nav(html, name), /href="room\.html"/, `${name} reaches the room editor`);
  for (const hash of ["#your-room", "#hire-hollie", "#hire-occasions"]) assert.ok(home.includes(`"${hash}":`), `old ${hash} links still arrive`);
  for (const file of ["room.html", "hire.html"]) assert.match(read("build.mjs"), new RegExp(`"${file}"`));
});

test("the room editor has its own page with the directions right under the photo", () => {
  assert.match(room, /id="your-room"/);
  assert.match(room, /<h1 id="room-title">/);
  assert.ok(room.indexOf('class="room-workspace"') < room.indexOf('class="room-directions"'));
  assert.ok(room.indexOf('class="room-directions"') < room.indexOf('id="room-form"'), "directions come before the picks column");
  const order = ["catalog-data.js", "room-products.js", "demo-products.js", "room-preview.js"].map((src) => room.indexOf(`src="${src}`));
  assert.ok(order.every((at, i) => at > 0 && (i === 0 || at > order[i - 1])), "catalog data loads before the editor");
  assert.match(room, /id="theme-toggle"/, "storefront.js needs the footer toggle");
});
