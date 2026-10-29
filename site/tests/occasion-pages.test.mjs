import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import test from "node:test";
import vm from "node:vm";
import { occasions, renderOccasionPage } from "../occasion-pages.mjs";

const read = file => readFileSync(new URL(`../${file}`, import.meta.url), "utf8");
const hirePage = read("hire.html");
const links = [...hirePage.matchAll(/href="([^"]+)" data-hire="([^"]+)" data-occasion-page/g)];

test("every occasion button opens its own matching page", () => {
  assert.equal(links.length, 15);
  assert.equal(new Set(links.map(link => link[1])).size, 15);
  assert.match(hirePage, /id="hire-occasions"/);
  for (const occasion of occasions) {
    assert.ok(links.some(link => link[1] === `/occasions/${occasion.slug}.html` && link[2] === occasion.name), occasion.name);
  }
});

test("each scene has its own picture, copy and complete shared page", () => {
  assert.equal(new Set(occasions.map(item => item.headline)).size, 15);
  assert.equal(new Set(occasions.map(item => item.description)).size, 15);
  for (const occasion of occasions) {
    const page = renderOccasionPage(occasion);
    assert.ok(page.includes(`<h1 id="scene-title">${occasion.name}</h1>`));
    assert.ok(page.includes(`content="https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site/occasions/${occasion.slug}.html"`));
    for (const suffix of [".webp", "--768.webp"]) {
      assert.ok(existsSync(new URL(`../assets/occasions/${occasion.slug}${suffix}`, import.meta.url)), `missing ${occasion.slug}${suffix}`);
    }
    assert.match(page, /alt="[^"]+" fetchpriority="high"/);
    assert.match(page, /AI-created styling inspiration/);
    assert.match(page, /Moodboard coming soon/);
    assert.match(page, /Styling details coming soon/);
    assert.match(page, /Packages &amp; booking coming soon/);
    assert.match(page, /disabled>Booking opens soon/);
    assert.equal([...page.matchAll(/aria-current="page"/g)].length, 1);
    assert.equal([...page.matchAll(/<li><a href="\/occasions\//g)].length, 15);
    for (const [, id] of page.matchAll(/href="#([^"]+)"/g)) assert.ok(page.includes(`id="${id}"`), `missing #${id}`);
  }
});

test("activating the booking inbox never replaces occasion navigation with email", () => {
  const script = read("storefront.js");
  const hireScript = script.slice(script.indexOf("// Fabulous From Online:"));
  const pageLinks = links.map(link => ({ dataset: { hire: link[2], occasionPage: "" }, href: link[1] }));
  const emailLink = { dataset: { hire: "Bachelorette" }, href: "#hire-contact" };
  vm.runInNewContext(hireScript.replace('const inbox = ""', 'const inbox = "hollie@example.com"'), {
    document: { querySelectorAll(selector) { return selector === "[data-hire]" ? [...pageLinks, emailLink] : []; } },
  });
  assert.deepEqual(pageLinks.map(link => link.href), links.map(link => link[1]));
  const email = new URL(emailLink.href);
  assert.equal(email.protocol, "mailto:");
  assert.ok(email.searchParams.get("body").includes("The occasion: Bachelorette"));
});
