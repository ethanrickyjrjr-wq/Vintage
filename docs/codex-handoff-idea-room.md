# Handoff for Codex: the idea room (preview pages for Hollie to decide on)

Written 2026-10-29 by Claude for Codex.

**Status (2026-10-29).**
- Sections 1–7 are built and published as Sites version 34 (`docs/idea-room-release.md`).
- Round D adds eight more pages and amends two. That is a second build: **section 8**. The 13 built pages stay as they are, except the two amendments in 8.4.

Ricky, 2026-10-29:
> "let's set it all up on different pages. we don't have to make it work exactly, just a lay out so she can see and decide. but don't put everything on homepage like it is now. Way too much there already."

"She" is Hollie.

**What to build.** One hub page and 13 idea pages. Each is a layout mock of one idea (or a small group of related ideas) from the research, with sample pieces and sample prices.
- On every page Hollie marks the idea **Keep / Maybe / Cut** and can add a note.
- The hub copies all her picks as text she can send to Ricky.
- Nothing here has to work for real. Forms don't submit and buttons don't buy.

**Where the ideas come from.** The 42-idea list Claude gave Ricky on 2026-10-29. That list draws on:
- `research/site-ideas/a1..a5`
- `research/consignment/b1..b5`
- `research/fabulous-from-online/c1..c6`
- `docs/site-ideas-and-consignment-synthesis.md`

Each page names its sources in one line.

**Before you start:**
- `git status`. Another session may have uncommitted work in `site/` (on 2026-10-29: `build.mjs` and `room-preview.js`, plus `research/type-and-spacing-2026-10-29/`). Leave it alone.
- Use pathspec `git add` only.
- No new dependency.
- Do not touch `storefront.html`, `storefront.js`, `disco*.js`, `atmosphere.css` or `assets/demo/`. **The homepage does not change and does not link to the idea room.**

**Rules for every page:**
- Burgundy page; white only behind product photos.
- The spelling is Hollie. Never write "Hollywood" for the shop.
- No invented customers, reviews, cities or past jobs. Example content is labeled "sample" or "example".
- Do not promise a disco ball with every order.

## 1. Files

All flat in `site/`, so `build.mjs` only needs list entries:

| File | Idea numbers (from the 42) | Title (h1) |
|---|---|---|
| `ideas.html` | hub | The idea room. |
| `idea-gone.html` | 2, 3, 38 | Gone, not forgotten. |
| `idea-hunt.html` | 4, 5, 42 | What are you hunting? |
| `idea-drop.html` | 1, 10, 11, 35 | Thursday, 7pm. The room restocks. |
| `idea-vibes.html` | 7, 12 | Shop by feeling. |
| `idea-looks.html` | 8, 9 | Looks from the real room. |
| `idea-item.html` | 13–19, 41, 42 | A better item page. |
| `idea-send-room.html` | 39 | Send this room to Hollie. |
| `idea-hire-extras.html` | 20–29 | More ways to hire Hollie. |
| `idea-live-sale.html` | 6 | Live from the room, once a month. |
| `idea-sell.html` | 37, 38 | Sell to Hollie. |
| `idea-flash.html` | 30–34, 36 | A little more flash. |
| `idea-box.html` | 40 | The card in the box. |
| `idea-homepage.html` | Ricky's note | A lighter homepage. |
| `ideas.css`, `ideas.js` | shared | |

Add all 16 to the `for (const file of [...])` list in `site/build.mjs`.

Images:
- Use only images that already ship:
  - `assets/thumbnails/samples-<file>--480.webp` / `--960.webp` (product cutouts; `<file>` is the `file` field in `demo-products.js`)
  - `assets/thumbnails/photos-IMG_66xx--480.webp` / `--960.webp` (original room photos)
  - `assets/editorial/*` (the entrance art, including the disco ball)
- Never reference `assets/photos/IMG_*--1920.webp` or `--3840.webp`. `build.mjs` keeps only the large photos named in `storefront.html`.
- Screenshots you capture go in a new `assets/ideas/` folder (it ships as-is). Keep them as WebP under 200 KB.

For every sample piece, take the **title and price from `demo-products.js`** by its `file` name. Do not make up names or prices.

## 2. The shared page shell

Copy this for every `idea-*.html`; `ideas.html` uses the same head.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex, nofollow" />
  <meta name="theme-color" content="#451c2b" />
  <title>Idea: Gone, not forgotten | Holliewood and Vine</title>
  <link rel="icon" href="favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="assets/fonts/fonts.css" />
  <link rel="stylesheet" href="storefront.css" />
  <link rel="stylesheet" href="atmosphere.css" />
  <link rel="stylesheet" href="ideas.css" />
  <script src="ideas.js" defer></script>
</head>
<body>
  <div class="rug-band" aria-hidden="true"></div>
  <header class="idea-header page-width">
    <a class="wordmark" href="ideas.html" aria-label="Back to the idea room">Holliewood <span>&amp; Vine</span></a>
    <a class="text-link" href="ideas.html">← All ideas</a>
  </header>
  <p class="idea-banner">Idea preview for Hollie. Nothing here is live: sample pieces, sample prices, and buttons that don’t do anything yet.</p>
  <main class="idea-page page-width">
    <div class="idea-top">
      <p class="eyebrow">Getting people back · ideas 2, 3, 38</p>
      <h1>Gone, not forgotten.</h1>
      <p class="idea-why"><strong>Why:</strong> one sentence. <span>From: research/site-ideas/a4, a2.</span></p>
      <fieldset class="idea-decide" data-idea="gone" data-title="Gone, not forgotten">
        <legend>Hollie’s call</legend>
        <label><input type="radio" name="call-gone" value="Keep" /> Keep</label>
        <label><input type="radio" name="call-gone" value="Maybe" /> Maybe</label>
        <label><input type="radio" name="call-gone" value="Cut" /> Cut</label>
        <label class="idea-note">Note <textarea rows="2" placeholder="Change anything?"></textarea></label>
      </fieldset>
    </div>
    <section class="idea-mock" aria-label="Layout preview">
      <!-- the mock for this idea -->
    </section>
  </main>
</body>
</html>
```

The `data-idea` value is the file name without `idea-` and `.html`: `gone`, `hunt`, `drop`, `vibes`, `looks`, `item`, `send-room`, `hire-extras`, `live-sale`, `sell`, `flash`, `box`, `homepage`.

## 3. `ideas.js` (all of it)

```js
// Idea room: Hollie marks each idea Keep, Maybe or Cut. Picks stay in this browser; the hub copies them as text for Ricky.
(() => {
  const key = "hnv-idea-picks";
  let picks = {};
  try { picks = JSON.parse(localStorage.getItem(key)) || {}; } catch {}
  const save = () => { try { localStorage.setItem(key, JSON.stringify(picks)); } catch {} };
  for (const box of document.querySelectorAll("[data-idea]")) {
    const id = box.dataset.idea;
    const saved = picks[id] || {};
    for (const radio of box.querySelectorAll('input[type="radio"]')) {
      radio.checked = radio.value === saved.call;
      radio.addEventListener("change", () => { picks[id] = { ...picks[id], call: radio.value }; save(); });
    }
    const note = box.querySelector("textarea");
    if (note) {
      note.value = saved.note || "";
      note.addEventListener("input", () => { picks[id] = { ...picks[id], note: note.value }; save(); });
    }
  }
  const copy = document.querySelector("#copy-picks");
  copy?.addEventListener("click", async () => {
    const lines = [...document.querySelectorAll("[data-idea]")].map((box) => {
      const pick = picks[box.dataset.idea] || {};
      return `${box.dataset.title}: ${pick.call || "not decided"}${pick.note ? ` (${pick.note})` : ""}`;
    });
    try {
      await navigator.clipboard.writeText(lines.join("\n"));
      copy.textContent = "Copied. Paste it to Ricky.";
    } catch {
      copy.textContent = "Copy didn’t work here. Take a screenshot instead.";
    }
  });
})();
```

## 4. `ideas.css` (aim for about 120 lines)

- **Tokens and buttons.** Reuse the `storefront.css` tokens (`--burgundy`, `--paper-deep`, `--line`, `--pink`, `--rust`, `--display`, `--body`, `--mono`) and its `.button`, `.eyebrow`, `.text-link` and `.page-width`.
- **Banner.** `.idea-banner` is a sticky pink strip (`var(--pink)` background, burgundy text, 13px, centered, `top: 0`).
- **Decision box.** `.idea-decide` is a bordered panel. The radios are 44px-tall pill labels, and the checked pill gets the rust border. On phones it stays near the top: it is not sticky, it sits under the h1.
- **Mock frame.** `.idea-mock` is a dashed `var(--line)` outer frame with 24px padding. It reads as a mock-up, not a live page.
- **Cards.** `.idea-card` is a product card: white panel behind a `contain` image, title in `var(--display)`, price tabular. Reuse the visual pattern of `.product-visual` from `sample-shop.css` without importing that file.
- **Grids.** `repeat(auto-fill, minmax(220px, 1fr))`, collapsing to two columns at 390px.
- **Motion.** Any animation (ticker, glint, neon) sits inside `@media (prefers-reduced-motion: no-preference)`.
- **Layout.** No horizontal scroll at 320px.

## 5. The pages

Copy below is a starting point in the shop's voice; tighten it if needed. Each mock uses real sample photos.

### `ideas.html` (the hub)

**Top of the page:**
- h1 "The idea room."
- Lede: "Ideas from three rounds of research, laid out so you can see them. Open one, look around, then mark it Keep, Maybe or Cut. Your picks stay on this device. When you’re done, tap Copy my picks and send them to Ricky."
- Button `#copy-picks`: "Copy my picks".

**The cards.** Under six group headings, one card per idea page. Each card has:
- the h1 as a link
- one line of pitch
- a "Claude’s pick" badge on gone, send-room, drop, vibes, item and hire-extras (these were the top picks)
- the same `.idea-decide` fieldset as on that idea's page, with the same `data-idea` and `data-title`, so picks stay in sync

**Groups:**
- Getting people back: gone, hunt, drop, live-sale
- Shop by feeling: vibes, looks
- Trust: item, box
- Hire Hollie: hire-extras, send-room
- Getting inventory: sell
- Flash and the homepage: flash, homepage

### `idea-gone.html`: sold pieces stay up

**Why:** one-of-ones never restock. A sold archive proves things sell, shows what pieces are worth, and turns every sold piece into a request. (a2 Joy of Cocktails; a4 drop → sold archive → "find me one" loop.)

**Mock:**
- A filter row: All · Lighting · Glass · Furniture · Fashion.
- Eight cards from the sample collection, for example: gold-bust-lamp, pink-coupes, lamp-ruby-glass-brass, red-swan-sofa-chrome-base, rotary-phone-red, mirror-gold-oval-rococo, faceted-pink-coupe, zebra-print-star-pump.
- Each card has:
  - a diagonal **GONE** ribbon over a slightly faded photo
  - "Sold for $X (sample)" using its demo price
  - one item-voice line with no buyer claims, e.g. "Brass, bust, attitude. Gone." or "Pink glass never stays long."
  - a button **Find me one of these**
- The first card's button is shown expanded as a small panel: "Hollie will hunt for one like it. Casting Call from $95, credited toward the piece."
- A band at the bottom: "Clearing out a whole house of this? Tell Hollie." (idea 38, which links to the sell idea).

### `idea-hunt.html`: wish list and first dibs

**Why:** shoppers count on vintage shops to keep an eye out. A free wish list feeds Hollie's buying and the paid Casting Call. (c2: Potomac's and R&R's free wish lists; a buyer on a sourcing forum: "specific items I've been trying to find for years".)

**Mock:**
- **The form.** It doesn't submit. Above it: "The thing you’ve been trying to find for years." Fields:
  - What are you hunting
  - Category
  - Budget
  - Measurements or size
  - Email
  - "Tell me when" checkboxes: the next drop / a match for my list

  Button "Put me on the list". Small print: "Free. No guarantee. Hollie keeps an eye out."
- **A first-dibs panel:** "The drop email lands an hour before the room restocks."
- **A perk line:** "List members can hold one piece for 24 hours." (idea 42; c2 Potomac's 48-hour hold)

### `idea-drop.html`: the weekly drop

**Why:** a fixed-time drop gives people a reason to come back when nothing restocks (a4). Shopify can schedule publishing on its Online Store; Etsy shows no scheduler (synthesis, a5).

**Mock, top to bottom:**
- A ticker band: "Next drop Thursday 7pm · six pieces · pink glass, brass and one very good chair". It scrolls only under `prefers-reduced-motion: no-preference`; otherwise it is static.
- A static countdown block: "2 days 4 hours" (sample).
- A theme banner: "THE BAR CART IS OPEN" (idea 10).
- Six cards, each tagged **Freshly Hunted** (idea 11).
- A small first-dibs sign-up box (dead).

### `idea-vibes.html`: shop by feeling

**Why:** a vibe is a set of tags that cuts across categories. It needs no new inventory (a1). Glass collectors search by maker (a2), so glass gets maker tags.

**Mock:**
- **Five big tiles**, each a collage of three sample cutouts on burgundy:
  - Pink Glass: "Rose-tinted, on purpose."
  - Brass & Mirrors: "Everything reflects well on you."
  - Cocktail Hour: "You bring the ice."
  - Disco Fever: "Mirrors mandatory."
  - Burgundy Hours: "After dark, before midnight."
- **The open Pink Glass view** below the tiles: a grid of the pink pieces.
- **Maker chips** on the glass pieces, reading "Maker tag goes here (e.g. Georges Briard)". Do not assign real makers to sample pieces.

### `idea-looks.html`: named looks and dots on the room photo

**Why:** Soho Home and The Kitschy Maximalist sell "the look": a few real pieces framed as one idea. No vintage shop has clickable dots on a real room photo (a2).

**Mock:**
- **Mock A.** Three look cards: The Bar Cart (pink coupes, cut-crystal goblet, faceted pink coupe, rotary phone), Pink Hour, and Brass & Glass. Each has:
  - a wide image: `photos-IMG_6610--960.webp` for one, sample cutouts on burgundy for the others
  - one sentence
  - a rail of 3–6 pieces
- **Mock B.** `photos-IMG_6610--960.webp` with three round dot buttons placed on the pink glass, the silver busts and the neon. Hover or focus shows a small label card (CSS only): title, price, "View piece".

### `idea-item.html`: a better item page (using the gold bust lamp)

**Why:** trust on one-of-ones comes from grades, notes, specs and honest wording. Sources:
- a2 Joy of Cocktails and Show Pony: condition grades and notes
- a2 The Old Above: the lamp spec block, lamps photographed lit
- a2 Show Pony: item numbers and attribution wording
- a1 Shrimpton: the "ask" button

**Mock, two columns:**
- **Left column, photos:** the cutout first, then two empty frames labeled "Real photo, lamp lit" and "On black, for glass" (idea 19).
- **Right column, item details:**
  - item number "HV-A13"
  - title and price from `demo-products.js`
  - a condition chip "Very good", with a legend of four grades: Mint-ish · Very good · Good, with character · Needs a little love
  - a Condition notes block
  - a lamp spec table: Bulb base · Max wattage · Wiring (original, tested / rewired) · Height · Shade included · Ready to plug in. Every value says "sample".
  - an attribution line: "In the style of. A maker’s mark has not been verified."
  - "Shipping this piece: $— insured, packed by Hollie" (sample)
  - buttons: Add to bag · Ask before you buy · Send to a friend · Hold for 24 hours (list members)

### `idea-send-room.html`: Send this room to Hollie

**Why:** people who use the room editor have already uploaded a photo of their own room. One tap from there to the Fabulous From Online email is the shortest path from playing to paying (Claude's idea, 39).

**Mock:** a three-frame storyboard.
1. A real screenshot of the room editor with the sample room and a find placed. Capture it from the local site into `assets/ideas/send-room-1.webp`.
2. The same toolbar with a new button **Send this room to Hollie ✦** next to Discofy. It opens a small sheet: "We’ll save the picture. Attach it to the email that opens." with buttons Save picture · Open email.
3. A mocked email draft:
   - subject "Fabulous From Online - My room - Holliewood & Vine"
   - the first lines of the brief
   - an attachment chip "my-room.png"

A note under the storyboard: "Email links can’t attach files, so the picture is saved first (RFC 6068; c4)."

### `idea-hire-extras.html`: more ways to hire Hollie

**Why:** packages the c1/c3 research found that the live section doesn't have yet.

**Mock:** a card grid. Each card gives the name, one line, and "Price: TBD" unless a sourced number is noted.
- Shop live on the call (c1 Mix & Match): "Hollie pulls pieces from the collection on camera."
- Holiday dressing (c3): "Installed now, gone by January 15. Booking through November."
- Snowbird season opening (c3): "You land. The house is already dressed."
- Gift a Room: draw a mock certificate in burgundy and brass with "This certificate is good for one Close-Up, styled by Hollie."
- Revive (c1 Dwelling Envy): "For rooms that are almost there."
- Recently sourced (c2 Mercer). One card labeled **"Example, not a real job"**: the request, days to find, price against budget.
- Design-client discount (c1 Noeka 10–15%): "10% off collection pieces when Hollie styles your room."
- Your room page (c1 Dwelling Envy, Mix & Match): "The call recording and your board, kept for a year."
- Party takedown (c3 Bach Me, from $150): "Who takes it down? Hollie does."
- Party rentals. Shown greyed out with "Parked: Ricky said no for v1" (c3 Vintage Gathering lounge sets $325–$495).

### `idea-live-sale.html`: monthly live sale

**Why:** live selling is how some vintage shops move pieces (a4). One person can't watch comments, pack and perform every week, so it's monthly at most, and payment goes through the shop's own checkout, not DMs (a4).

**Mock:**
- An event card: "Live sale · first Sunday of the month · 7pm · Instagram Live or Whatnot (TBD)".
- "How to claim": comment "mine", then get an invoice from our checkout.
- A dead "Set a reminder" button.
- Six sample cards under "On the table tonight".

### `idea-sell.html`: Sell to Hollie

A red-bordered note at the top:

> "Parked until a Florida attorney answers. Buying from the public falls under Florida ch. 538: registration, a report to police within 24 hours, and 15–30 day holds (docs/site-ideas-and-consignment-synthesis.md)."

**Mock:**
- **"What Hollie loves":** short era paragraphs for '60s brass, '70s glass and lucite, '80s glam and '90s chrome. (Consignment research: a want list in the shop's own voice.)
- **"What to send":** photos including any maker's mark, measurements, flaws, smells, ZIP code, asking price. (Consignment research.)
- **Steps:** photos → an offer within 48 hours → drop off or ship → paid after inspection.
- **A line for estates:** "A whole house? Tell Hollie." (idea 38)

### `idea-flash.html`: a little more flash

**Why:** the a3 list, ranked by wow per effort. Everything builds on the existing disco code, and motion starts only after "Start the disco" (a3).

**Mock:** six tiles, each with a static image and a two-line description. Only 2 and 3 get tiny live CSS demos, inside the reduced-motion media query.
1. **Drag to spin the mirror ball:** the entrance ball `assets/editorial/disco-ball.webp`, with a ↻ hint. The sample `disco-ball-*` files are not in the collection, so they don't ship.
2. **Light glints on glass:** a CSS gradient sweep across the pink-coupes card on hover.
3. **The neon breathing with the music:** "do it for the plot" in pink text with a slow glow.
4. **A burst of mirror chips on Add to bag:** static frame.
5. **A light sweep when the phone tilts, after Start the disco:** text only.
6. **The 404 page:** a framed mini page reading "404. This piece has left the room." with a link to the collection.

### `idea-box.html`: the card in the box

**Why:** a note card in the package (a1 Kiko). The QR code brings buyers back to the room, the music and "find me another".

**Mock:** a 5×7 card, front and back side by side.
- **Front:** the wordmark and "Do it for the plot."
- **Back:** "Thank you for giving it a new home. Scan to see the room, play the music, or ask Hollie to find you another."
- **The QR code:** a square labeled "QR goes here". No real code.
- **A note under the card:** "The mirror-ball line only goes on cards in boxes that have a mirror ball. It isn’t every order."

### `idea-homepage.html`: a lighter homepage (Ricky: "Way too much there already")

**Why:** the homepage holds ten sections. This page proposes what stays and what moves. **Nothing moves until Hollie and Ricky decide.**

**Mock, two columns:**
- **Now.** The ten current sections in order: entrance, the collection, departments, the 3D showroom invitation, the story, your room, Hire Hollie, the disco note, the owner, and "Good finds. Honest details." Each block's height is proportional to the section's real height at 1440px.
  - Measure each `section` and the `.browse-nav`/departments block with `offsetHeight` in the browser, and print the numbers and the total.
- **Proposed.**
  - Entrance → The collection → **Three doors** (Try it in your room → its own page · Hire Hollie → its own page · 3D showroom) → The owner → Good finds. Honest details. → footer.
  - The room editor and the Hire Hollie section each move to their own page. The story and the disco note fold into the doors or the owner section.
  - Print the estimated new total.
- A one-line caveat: "Moving the room editor or Hire Hollie means changing nav links and the tests that look for them on the homepage."

## 6. Test: `site/tests/idea-room.test.mjs` (new)

```js
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
```

## 7. Acceptance

1. `npm test` in `site/` passes, the existing tests included.
2. `git diff --stat site/storefront.html site/storefront.js` is empty.
3. Local server (`npm run dev`), `/ideas.html`:
   - every card opens its page
   - each page shows the banner, the decision box and the mock
   - no failed image requests in DevTools Network
   - no console errors
4. Mark three ideas on their pages, reload the hub: the three picks show. Copy my picks puts the text on the clipboard.
5. At 1440, 390 and 320 CSS px: no horizontal scroll. Decision pills are at least 44px tall.
6. With reduced motion on, the ticker, glint and neon demos are still.

Commit only the new files and the `build.mjs` list edit, with a message that says what changed. `git pull --rebase`, then push.

**Publishing.** The pages ship with the site, unlinked and noindex. Ricky publishes as usual, then sends Hollie `<site>/ideas.html`. Record the Sites version at the top of this file.

## 8. Round D additions (2026-10-29, a second build)

Sections 1–7 are built and published as Sites version 34 (`docs/idea-room-release.md`). This section is a delta on top of that build: **eight new idea pages, two amended pages and a seventh hub group.** Sections 2–4 (shell, `ideas.js`, `ideas.css`) and the section 1 rules apply unchanged.

The ideas come from `docs/round-d-synthesis.md`, ranked ideas 1–8, 8b and 11–12, with evidence in `research/round-d/d1..d7-*.md`.

**Picks Hollie has already made stay put.** They are keyed by `data-idea`, and no existing `data-idea` changes.

### 8.1 Files

| File | Synthesis idea | Title (h1) | Eyebrow |
|---|---|---|---|
| `idea-own-page.html` | 1 | Every piece gets its own address. | Getting found · round D |
| `idea-travel.html` | 2, 8 | How it travels. | Shipping · round D |
| `idea-letters.html` | 3, 9 | Letters from Hollie. | Keeping people · round D |
| `idea-proof.html` | 4 | Proof before the stars. | Trust · round D |
| `idea-slow-burn.html` | 5, 11, 12 | The slow burn. | Pricing · round D |
| `idea-marks.html` | 6 | Read the marks. | Getting found · round D |
| `idea-local.html` | 7, 10, 13 | Around here, in season. | Local · round D |
| `idea-four-weeks.html` | 8b | Four weeks from the room. | Social · round D |

- Add the eight files to the `build.mjs` list.
- `data-idea` values: `own-page`, `travel`, `letters`, `proof`, `slow-burn`, `marks`, `local`, `four-weeks`.
- Each page's "Why" line names its round D report and the synthesis, for example `From: research/round-d/d5; docs/round-d-synthesis.md.`

### 8.2 The hub (`ideas.html`)

- **Lede:** "Ideas from three rounds of research" becomes "Ideas from four rounds of research".
- **Count line:** "13 ideas to open. Six groups. No wrong answers." becomes "21 ideas to open. Seven groups. No wrong answers."
- **New seventh group:** "07 / 8 possibilities", heading "Found, kept and shipped", after "Flash and the homepage". It has one card per new page, with the same fieldset markup as the other cards.
- **Claude's pick badges:** own-page, travel and letters. The other five get "A possibility".
- **Card pitches:**
  - own-page: "One real page per piece, kept up after it sells. Search, Pinterest and the sold archive all start here."
  - travel: "A plain box, a card that says open it on camera, and shipping prices that cover the double box."
  - letters: "First dibs an hour early, a wish-list match, and the email that says it's gone, here's its cousin."
  - proof: "No stars yet. Show what's true instead: what sold, what Hollie checked, where pieces landed."
  - slow-burn: "No offers. Pieces step down quietly on drop day, and the old price is shown honestly."
  - marks: "Guides built from Hollie's own photos of stamps, labels and bases."
  - local: "One market worth a booth, a delivery note for Lee and Collier, and shipping north in April."
  - four-weeks: "A month of posts shot from the room: hands, neon, the mirror ball. Every post points to a page."

### 8.3 The new pages

Sample pieces, titles and prices come from `demo-products.js`, as in section 1. A computed sample price uses the stated rule and is labeled "sample". Every person, review, quote, count and date is a labeled placeholder; no invented buyers. Never write "Hollywood" next to "Vine", even to explain a search collision; "Hollywood Regency" is fine.

#### `idea-own-page.html`: one page per piece

**Why:** items open as `#item-<id>` inside a dialog today, and Google indexes the page, not the fragment. So the sold archive, search markup and Pinterest pins all need one real URL per piece, kept at HTTP 200 after it sells (d5; synthesis).

**Mock:** two side-by-side frames of the same piece, `gold-bust-lamp`.
- **Frame 1, for sale.** A fake address bar reading `…/pieces/gold-bust-lamp`. Below it: the title and price, a condition line "Used. Rewired. Brass polished by hand. (sample)" and an Add to bag button.
- **Frame 2, sold.** Same address bar, the same photo with the GONE ribbon from `idea-gone`, "Sold for $245 (sample)" and a **Find me one like it** button.
- **Under the frames,** a small "What search engines read" panel in `var(--mono)`: two short JSON-like snippets for the two frames. They show only `"itemCondition": "UsedCondition"` and `"availability": "InStock"` vs `"OutOfStock"`, with the price kept.
- **A note:** "The page stays up when it sells. Only the label changes. Never 'Refurbished': Google means a warranty by that."

#### `idea-travel.html`: how it travels

**Why:** the insurer won't pay a loss claim if the box hints at what's inside. USPS denies damage claims without packing evidence. Etsy's calculated shipping prices the item before it's double-boxed (d2; Shipsurance, USPS DMM 609 and Etsy captures re-checked in the synthesis).

**Mock, three bands:**
1. **The box.** Two drawn boxes side by side, in CSS, no photos: a plain kraft outer box labeled "Outside: plain. Says nothing." and an open inner box labeled "Inside: tissue, the card, sometimes something shiny (never promised)."
2. **The card line.** A 5×7 card reading: "Open it on camera. Keep the box until you're happy. Anything wrong? Tell Hollie within 48 hours."
3. **Shipping classes, as a four-row table.** A small glass · B table lamp or one parcel · C mirror or art box · D oversize, local or quoted. Every price cell reads "$— (from a real label quote)".

**Also on the page:**
- A lamp **parts bag** tag reading "HARP · FINIAL · BULB".
- The listing line "Ships double-boxed, insured to the sale price."

#### `idea-letters.html`: letters from Hollie

**Why:** an email list, sold as first dibs, fits the weekly drop. Kit's free plan covers 10,000 subscribers with unlimited sends but no automations. Buyers are invited by the box-card QR, never added (d3).

**Mock:**
- **Five email cards stacked like letters.** Each has the subject line and three lines, copied from `research/round-d/d3-email-sms.md` section 6 with `{placeholders}` left visible:
  - Welcome
  - Drop alert
  - Wish-list match
  - It's gone, here's its cousin
  - After purchase, find me another
- **The footer line** under the last card: "Holliewood & Vine, {postal address} … Unsubscribe in one click, no hard feelings."
- **A signup box** (dead) beside the cards. Microcopy: "Get the door an hour early. One email a week. Leave any time." Fields: Email, and "What are you hunting?" chips (Lamps · Glass · Mirrors · Chairs · Fashion) that read as tags.
- **A greyed "Texts" card:** "Parked: texts wait for a lawyer to read the consent wording."

#### `idea-proof.html`: proof before the stars

**Why:** one-of-one listings lose their reviews when they sell, and most small vintage shops show no stars at all. The FTC rule allows asking every buyer the same honest question. Google and Shopify ban any reward for a review, and so does this shop (d4).

**Mock, four blocks:**
1. **A "Rehomed" counter.** Large numeral "—", with the line "Counts real sales only. None yet."
2. **"Checked by Hollie" on a lamp card** (`lamp-ruby-glass-brass`): cord · socket · harp, each with an empty checkbox and "(sample)".
3. **"Where it landed."** Three empty white frames labeled "A buyer's photo goes here, with their yes on file". Each credit line reads "First name, city (placeholder)". Under the frames: "Photos from buyers who were invited to send one and told we might feature it. Nobody was paid."
4. **"The ask, word for word."**
   - The card line: "Good, bad or somewhere in the middle, tell people where you found it."
   - A small rules list:
     - same ask to everyone
     - no gifts or discounts for reviews
     - no reviews from family or friends
     - newest first

No stars and no quotes anywhere on the page.

#### `idea-slow-burn.html`: the slow burn

**Why:** buyers anchor offers low. On eBay, first offers average 61% of list. The shop's line is "Absolutely no offers." A quiet markdown ladder on drop day keeps that true. "Was / now" is a legal claim, so the old price is shown with its date (d7; 16 CFR 233.1).

**Mock:**
- **A ladder graphic:** day 30 → 10% off · day 60 → 20% · day 90 → 30%, then "back to Hollie's shelf or a new photo".
- **A "Recently reduced" shelf of three cards.** Each shows "Listed at $X on {date}. Now $Y. (sample)", where Y = the demo price × (1 − step), rounded down to the nearest $5:
  - `gold-bust-lamp` $245 → day 30 → $220
  - `southwestern-armchair` $325 → day 60 → $260
  - `mirror-gold-oval-rococo` $225 → day 90 → $155
- **A 48-hour hold card:** "Held for you until {time}. Then it goes back on the rack."
- **A greyed "Layaway, $300 and up" card:** "Parked: a lawyer reads the terms first."

#### `idea-marks.html`: read the marks

**Why:** searches about identifying or dating a piece are won by guides and collector threads, not marketplaces. A guide built from the shop's own photos beats a generic retailer guide (d5).

**Mock:**
- **One guide page laid out:**
  - h2 "Is that brass lamp a Stiffel? Check the base before you get excited."
  - sections: What it is · Features · Marks and numbers · Value · Questions
  - three empty frames labeled "Hollie's photo: base stamp", "Hollie's photo: paper label" and "Hollie's photo: cord tag"
  - body text that is visibly placeholder: "Facts to be sourced before publishing."
- **A rail of the other four titles** from d5's deliverable, as cards:
  - "Pink glass, interrogated"
  - "Hollywood Regency without the costume"
  - "The bar cart is a stage"
  - "Cut glass or merely pressed?"
- **Rule: state no maker facts on the mock.**

#### `idea-local.html`: around here, in season

**Why:** a booth at a real vintage market, a line for local delivery tax, and shipping north when the season ends (d6; the Lee County 2025 visitor table puts 33.9% of visitor spending in January–March).

**Mock:**
- **An event card:** "Vintage Market Days · Lee Civic Center, Fort Myers · January 29–31, 2027 · booth fee: asking". Under it, a small card: "Scan for a free Screen Test" with a square labeled "QR goes here".
- **"Send it north."** "Bought it here in February? We'll ship it to your other address in April." No price shown.
- **A delivery-tax note:** "Delivered in Lee: 6.5% sales tax. In Collier: 6%."
- **A greyed Google card:** "A Google listing only when Hollie visits homes (the Cameo)."

#### `idea-four-weeks.html`: four weeks from the room

**Why:** niche shops sell on a fixed weekly drop slot stated in the bio, a teaser the day before, and sold pieces marked in place. This shop skips comment or DM claims, because one-of-one stock on three channels can sell twice. Every post points to a page (d1).

**Mock:**
- **A four-column calendar,** one column per week, each with its theme as the column head:
  - Enter the Room
  - Lights On
  - Pink, Cut and Wrapped
  - Dress the Set
- **Five post tiles per column.** Each is a small 4:5 frame, with the post's one line under it and the page it links to in `var(--mono)`. Copy the lines and targets from the table in `research/round-d/d1-social-video.md` ("4-week content skeleton"). Each frame:
  - uses `photos-IMG_66xx--480.webp` or a sample cutout on burgundy
  - is labeled "Reel", "Carousel" or "Still" in the corner
- **A "Here / Gone" legend strip** above the calendar: a white chip "HERE" and a pink chip "GONE", with the line "When it sells, the caption starts with Gone. The post stays up."
- **A phone-sized bio card:** "Holliewood & Vine · one of one, always · drops every {DROP DAY} · link below". Under it, the canned reply "Is this still available?" → "If the page says Here, yes. Here's the link."
- **A greyed "Shops" card:** "TikTok Shop, Instagram Shop, Pinterest Product Pins: parked. No lane for this stock, or the site needs checkout first."
- Week 4's video-call post and the live carry the tag "after booking opens".

### 8.4 Amend two built pages

- **`idea-box.html`.** Add one line to the back of the card: "Good, bad or somewhere in the middle, tell people where you found it." Add a note under the card: "The mirror ball is never tied to a review. Google and Shopify ban gifts for reviews (round D, d4)." Keep everything else.
- **`idea-item.html`.** In the right column, under the shipping line, add:
  - "Ships double-boxed, insured to the sale price."
  - a "Checked by Hollie: cord · socket · harp (sample)" line
  - the condition line "Used. Rewired. Brass polished by hand. (sample)"

  Keep the existing grade legend.

### 8.5 Test change

In `site/tests/idea-room.test.mjs`, change `assert.equal(pages.length, 13);` to `assert.equal(pages.length, 21);`. Everything else in the test already covers the new pages: the build list, noindex, banner, `data-idea`, the hub link, the hub fieldset, shipped images and the spelling rule.

### 8.6 Acceptance

- Section 7 applies to all 21 pages and the hub.
- Also check:
  1. The eight new cards sit in group 07.
  2. Hollie's existing picks still load on the hub after the rebuild.
  3. Copy my picks now produces 21 lines.
  4. `git diff --stat site/storefront.html site/storefront.js` is empty.
- Record the new Sites version in `docs/idea-room-release.md`.
