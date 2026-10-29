import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";

const root = fileURLToPath(new URL("../", import.meta.url));
const read = (file) => readFileSync(path.join(root, file), "utf8");
const home = read("storefront.html");
const page = read("hire.html");
const script = read("storefront.js");
const section = page.match(/<section[^>]*id="hire-hollie"[\s\S]*?<\/section>/)?.[0] ?? "";

test("the hire section carries Ricky's name and every nav reaches it", () => {
  assert.ok(section, "section#hire-hollie is missing");
  assert.match(section, /Holliewood &amp; Vine Fabulous From Online/);
  for (const [name, html] of [["storefront.html", home], ["hire.html", page]]) for (const nav of ["desktop-nav", "mobile-nav", "footer-nav"]) {
    const block = html.match(new RegExp(`<nav[^>]*class="${nav}"[\\s\\S]*?</nav>`))?.[0] ?? "";
    assert.match(block, /href="hire\.html"/, `${name} ${nav} needs a Hire Hollie link`);
  }
});

test("live or demo, never half-filled", () => {
  const inbox = script.match(/const inbox = "([^"]*)"/)?.[1];
  assert.notEqual(inbox, undefined, "the hire script is missing from storefront.js");
  assert.doesNotMatch(section, /__BOOKING_URL__/, "add the Cal.com link or remove the Book a Screen Test button");
  const cta = section.match(/<div class="hire-cta"[\s\S]*?<\/div>/)?.[0] ?? "";
  if (inbox) {
    assert.match(inbox, /^[^@\s"]+@[^@\s"]+\.[a-z]{2,}$/i, "inbox is not an email address");
    assert.match(cta, /data-hire=""/, "live state needs the Email Hollie link");
  } else {
    assert.match(cta, /disabled>Booking opens soon</, "with no inbox the section must ship the demo CTA");
    assert.doesNotMatch(cta, /data-hire/, "demo state must not show a live Email Hollie link");
  }
});

test("the section keeps to the Florida wording guardrails", () => {
  const text = section.replace(/<[^>]+>/g, " ");
  for (const banned of [/registered interior designer/i, /\barchitect/i, /\blicensed\b/i, /\bcertified\b/i, /\binsured\b/i,
    /\bcontractor/i, /\bbuilder/i, /(remodeling|renovation) services/i, /install(ing)? (lighting|fixtures)/i, /hardwir/i]) {
    assert.doesNotMatch(text, banned);
  }
});

test("hire links are anchors and encode the subject and body", () => {
  assert.doesNotMatch(section, /<(?!a\b)[a-z]+\b[^>]*\bdata-hire\b/, "data-hire belongs on <a> only");
  assert.match(script, /subject=\$\{encodeURIComponent\(subject\)\}&body=\$\{encodeURIComponent\(/);
});

test("the shop is never spelled Hollywood", () => {
  for (const source of [page, script]) assert.doesNotMatch(source, /Hollywood\s*(&amp;|&|and)\s*Vine/);
});

const hireScript = script.slice(script.indexOf("// Fabulous From Online:"));

test("an empty inbox leaves demo links alone", () => {
  vm.runInNewContext(hireScript.replace(/const inbox = "[^"]*"/, 'const inbox = ""'), {
    document: { querySelectorAll() { assert.fail("demo must not rewrite links"); } },
  });
});

test("live briefs preserve occasions, ampersands and line breaks", () => {
  const occasions = ["", ...section.matchAll(/data-hire="([^"]+)"/g)].map(value => typeof value === "string" ? value : value[1]);
  const links = occasions.map(occasion => ({ dataset: { hire: occasion }, href: "#hire-contact" }));
  const inboxLabel = {};
  vm.runInNewContext(hireScript.replace(/const inbox = "[^"]*"/, 'const inbox = "hollie@example.com"'), {
    document: { querySelectorAll(selector) { return selector === "[data-hire]" ? links : [inboxLabel]; } },
  });
  assert.equal(inboxLabel.textContent, "hollie@example.com");
  assert.equal(occasions.length, 16);
  for (const link of links) {
    const url = new URL(link.href);
    assert.equal(url.protocol, "mailto:");
    assert.equal(url.pathname, "hollie@example.com");
    assert.match(link.href, /Holliewood%20%26%20Vine/);
    assert.match(link.href, /%0D%0A/);
    assert.ok(link.href.length < 2000);
    assert.equal(url.searchParams.size, 2);
    assert.equal(url.searchParams.get("subject"), ["Fabulous From Online", link.dataset.hire, "Holliewood & Vine"].filter(Boolean).join(" - "));
    assert.ok(url.searchParams.get("body").includes(`\r\nThe occasion: ${link.dataset.hire}\r\n`));
  }
});
