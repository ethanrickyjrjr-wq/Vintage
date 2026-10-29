# Handoff for Codex: the Fabulous From Online section (hire Hollie)

**Occasion styling updated 2026-10-29: Sites version 29.** All 15 occasions now
have distinct opaque poster colors, contrasting type, and selected invitation,
camera and record details. Terra researched the visual references; Sol checked
the palette; both reviewed the desktop rendering. Design rationale and sources
are recorded in `fabulous-from-online-design.md`. All 33 tests, the build, both
themes and desktop/390/320px checks passed; Lighthouse accessibility is 100.
GitHub: `1281f65`. Sites source: `720b090cf33ec3ff97714ade7c351cdc4d68fe9b`.
Deployment `appgdep_6ae2d58b6f248191ad0fd1df4993802d` succeeded. Booking remains
in demo state. The subtle-tint intermediate release (version 28) is superseded.

**Published 2026-10-28: Sites version 27, demo state.** Inbox is blank, there is no
Cal.com link, Screen Test is free, prices are as written, and the nav says Hire Hollie.
The CTA is “Booking opens soon”; all 15 occasions lead to it. GitHub implementation:
`5675a95`. Sites source: `b97b83a863d66833c026c81f83fa4df4b7742273`. Deployment
`appgdep_6ae2c11e9b848191b90cf90681d59013` succeeded at
https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site/#hire-hollie .

Verified: all 33 `npm test` checks and the production build passed. Browser checks
covered 1440, 900, 390 and 320 CSS px, all three nav links, mobile-menu closure,
keyboard disclosures and focus rings, both burgundy palettes, saved finds, bag,
room editor and disco. Lighthouse accessibility: 100. All six navigation-script
checks passed after replacing its two fixed dialog-close delays with bounded
waits for the actual history/bag state. Email subject/body encoding was tested for
the generic brief and every occasion with a fixture inbox; opening a real mail
client and Cal.com booking are deferred until contact details are supplied.
Local reports and screenshots are in ignored `artifacts/fabulous-from-online/`.
The release preserves the sample-room repair already published in version 25.

Written 2026-10-28 by Claude for Codex. **You can build this and land it on master now.**
- With no inbox in block 0, it lands in **demo state**. The call to action reads "Booking opens soon", like the bag's checkout, and the email script does nothing. Any publish of unrelated work stays safe.
- It goes live when Ricky supplies the inbox.
- Step 5's test passes in both states and fails only on a half-filled section.
- Ricky publishes through the Codex app; pushing does not deploy.

- **Why:** `docs/fabulous-from-online-design.md` (every price and rule has its source there).
- **Evidence:** `research/fabulous-from-online/c1..c6-*.md`.

Ricky, 2026-10-28: "a section where users hire Hollie to find items, decorate entire rooms or sections or entire studios/houses. They can meet virtually, show the space, send photos or describe what they want through email."

**Before you start:**
- Run `git status`. Use pathspec `git add` only, never `git add -A`; another session commits to this tree.
- No new dependency. No new page or CSS file, and no `build.mjs` change: everything lands in files the build already ships (`storefront.html`, `storefront.js`, `homepage.css`).
- Do not touch `disco*.js`, `atmosphere.css` or `assets/`.
- White is for product-photo frames only. The section sits on the existing burgundy page.
- The spelling is **Hollie**, with ie. Never write "Hollywood" for the shop.
- Refer to Hollie by name. No pronouns: none are known.

## 0. Ricky fills (blank rows take the default; a blank inbox means demo state)

| # | What | Where it goes | Default if Ricky says "go with yours" |
|---|---|---|---|
| 1 | Inbox address for Email Hollie | the `inbox` constant in step 3 | `""`: demo state. Use the demo `.hire-cta` from step 2. |
| 2 | Cal.com Screen Test link | `__BOOKING_URL__` in step 2 | Delete the Book a Screen Test button. Change the Screen Test card's last line to "Ask for one in your email." |
| 2b | Screen Test price | Screen Test card | Free. If Ricky sets a price, turn on Stripe payments for that Cal.com event; Cal.com Free lists "Accept Stripe & PayPal payments". Change "a free video call" to "a $X video call, credited toward your billing". |
| 2c | Nav label | step 1 | "Hire Hollie". Ricky's own name for the section is "Fabulous From Online"; ask which goes in the nav. |
| 3 | Starting prices: $95 / $295 / $750 / by the room; Cameo $150 an hour, two-hour minimum, $1,200 a day; Rushes +25% / +50%, $75 minimum | step 2 markup | keep as written |
| 4 | Where Hollie is based and how far The Cameo travels | The Cameo paragraph | "Lee and Collier counties included; farther out, travel time is billed." |
| 5 | Nothing found: store credit or refund | fine print, bullet 4 | 90-day store credit |
| 6 | Is the owner in the owner section Hollie? | placement | no: the section goes after `#your-room` |

## 1. Navigation (three one-line edits in `site/storefront.html`)

Add `<a href="#hire-hollie">Hire Hollie</a>` immediately after the "Try it in your room" link in each of:
- `nav.desktop-nav` (about line 80)
- `nav#mobile-nav` (about line 108; keep that nav's no-whitespace `</a\n><a` style)
- `nav.footer-nav` (about line 469)

## 2. The section (`site/storefront.html`)

Insert directly after the closing `</section>` of `section#your-room` and before `section#disco`.

Copy is final unless Ricky edits it. The section reuses existing classes (`page-width`, `eyebrow`, `button`, `button-cream`, `button-outline`); new classes are prefixed `hire-`.

```html
<section class="hire page-width" id="hire-hollie" aria-labelledby="hire-title">
  <div class="hire-intro">
    <div>
      <p class="eyebrow">Holliewood &amp; Vine Fabulous From Online</p>
      <h2 id="hire-title">You bring the plot.<br /><em>Hollie dresses the set.</em></h2>
      <p>Rather not do it yourself? Hire Hollie to find the piece, style a corner, dress a room or take on the whole house. Show Hollie the space on a video call, send a few photos, or describe it in one good email.</p>
    </div>
    <figure class="hire-photo">
      <img src="assets/thumbnails/photos-IMG_6611--960.webp"
        srcset="assets/thumbnails/photos-IMG_6611--480.webp 480w, assets/thumbnails/photos-IMG_6611--960.webp 960w"
        sizes="(max-width: 767px) 80vw, 380px" width="960" height="1280" loading="lazy"
        alt="A feathered hat on a lace head beside cut crystal in the original Holliewood and Vine room" />
      <figcaption>From the original room.</figcaption>
    </figure>
  </div>

  <h3 class="hire-heading">Three ways in.</h3>
  <ol class="hire-ways">
    <li><h4>Screen Test</h4><p class="hire-line">Pan slowly. Hollie has notes.</p><p>Book a free video call and walk Hollie through the space.</p></li>
    <li><h4>Stills</h4><p class="hire-line">Send photos.</p><p>Daylight, lamps off, and please don’t tidy. The checklist is below.</p></li>
    <li><h4>The Logline</h4><p class="hire-line">Describe it in an email. Free.</p><p>A sentence or three. Hollie replies with a plan and a price.</p></li>
  </ol>

  <h3 class="hire-heading">Pick your billing.</h3>
  <ul class="hire-tiers">
    <li><h4>Casting Call</h4><p class="hire-scope">One find</p><p>Tell Hollie the part. Hollie finds the piece to play it.</p><p class="hire-price">from $95 <span>credited toward the piece</span></p></li>
    <li><h4>Close-Up</h4><p class="hire-scope">A corner or section</p><p>A shelf, a bar cart, the spot by the door, a party table. One corner gets all the attention.</p><p class="hire-price">from $295</p></li>
    <li><h4>Leading Role</h4><p class="hire-scope">A room</p><p>Living room, bedroom, spare room, the one after the remodel. Top billing.</p><p class="hire-price">from $750</p></li>
    <li><h4>Full Production</h4><p class="hire-scope">A studio or the whole house</p><p>Every room, one vision, no continuity errors.</p><p class="hire-price">by the room <span>10% off each room after the first</span></p></li>
  </ul>
  <div class="hire-addons">
    <div><h4>The Cameo</h4><p class="hire-line">Hollie, in person.</p><p>$150 an hour with a two-hour minimum, or $1,200 for a styling day. Lee and Collier counties included; farther out, travel time is billed.</p></div>
    <div><h4>Rushes</h4><p class="hire-line">Need it now?</p><p>+25% to start within a week, +50% within 48 hours, $75 minimum. Rush styles with pieces already in the collection.</p></div>
  </div>
  <p class="hire-note">Starting prices. Hollie quotes after the logline. Plus applicable sales tax.</p>

  <h3 class="hire-heading">What’s the occasion?</h3>
  <ul class="hire-occasions">
    <li><a href="#hire-contact" data-hire="Cocktail hour"><strong>Cocktail hour</strong><span>Brass, mirrors, a little chrome. You bring the ice.</span></a></li>
    <li><a href="#hire-contact" data-hire="Dinner party"><strong>Dinner party</strong><span>Dinner at eight. The table arrives at six, in brass and pink glass.</span></a></li>
    <li><a href="#hire-contact" data-hire="The party"><strong>The party</strong><span>Any excuse works. The lighting does the rest.</span></a></li>
    <li><a href="#hire-contact" data-hire="Disco night"><strong>Disco night</strong><span>Oscars, New Year’s, a Tuesday. Red carpet optional. Mirrors mandatory.</span></a></li>
    <li><a href="#hire-contact" data-hire="Bachelorette"><strong>Bachelorette</strong><span>The house gets styled. The guest of honor gets photographed.</span></a></li>
    <li><a href="#hire-contact" data-hire="Proposal"><strong>Proposal</strong><span>Somebody is about to say yes. The room should say it first.</span></a></li>
    <li><a href="#hire-contact" data-hire="Photo set"><strong>Photo set</strong><span>A corner built for the camera, ready before the light changes.</span></a></li>
    <li><a href="#hire-contact" data-hire="After the remodel"><strong>After the remodel</strong><span>The walls are done. The room isn’t.</span></a></li>
    <li><a href="#hire-contact" data-hire="Guest room"><strong>Guest room</strong><span>Guests land Friday. Make it look like you planned this.</span></a></li>
    <li><a href="#hire-contact" data-hire="Spare room"><strong>Spare room</strong><span>A room with potential and a treadmill.</span></a></li>
    <li><a href="#hire-contact" data-hire="Home office"><strong>Home office</strong><span>Your coworkers have seen enough beige.</span></a></li>
    <li><a href="#hire-contact" data-hire="Snowbird season"><strong>Snowbird season</strong><span>You land. The house is already dressed.</span></a></li>
    <li><a href="#hire-contact" data-hire="Reading nook"><strong>Reading nook</strong><span>A chair, a lamp, a reason to stay home.</span></a></li>
    <li><a href="#hire-contact" data-hire="Gift a room"><strong>Gift a room</strong><span>Give a room instead of a candle.</span></a></li>
    <li><a href="#hire-contact" data-hire="Something else"><strong>Something else</strong><span>Whatever it is, do it for the plot.</span></a></li>
  </ul>

  <h3 class="hire-heading">How it works.</h3>
  <ol class="hire-steps">
    <li><strong>The Logline.</strong> Email Hollie. Free.</li>
    <li><strong>The Screen Test.</strong> A video call, booked online, so Hollie sees the real room. Photos work too.</li>
    <li><strong>The board.</strong> Pay your billing online, and in 7 to 10 business days you get a plan and options, each labeled From the collection or Sourced for you. Two rounds of changes included.</li>
    <li><strong>You approve.</strong> In writing, piece by piece. You pay for a sourced piece before Hollie buys it. Collection pieces hold for 48 hours.</li>
    <li><strong>That’s a wrap.</strong> Hollie places it in person, or you get the list and the pieces, shipped.</li>
  </ol>

  <div class="hire-disclosure">
    <h3>Yes, Hollie sells things too.</h3>
    <p>Some of what you’re shown comes from the Holliewood &amp; Vine collection. Some is found elsewhere. Every option is labeled <strong>From the collection</strong> or <strong>Sourced for you</strong>, so you always know whose shelf it came from. Collection pieces are the listed price. Sourced pieces carry a 10% sourcing fee on its own line, and you see the full price before anything is bought. No mystery math.</p>
  </div>

  <details class="hire-details">
    <summary>Photo checklist</summary>
    <ul>
      <li>A wide shot from the doorway.</li>
      <li>One photo of each corner.</li>
      <li>Each wall, straight on, with a little ceiling and floor.</li>
      <li>Daylight, lamps off. No wide-angle lens.</li>
      <li>Don’t tidy. Hollie needs the real room.</li>
      <li>Rough measurements: room length and width, windows, doors.</li>
      <li>What you’re keeping, what’s a maybe, what’s a hard no.</li>
      <li>A budget number.</li>
    </ul>
  </details>
  <details class="hire-details">
    <summary>The fine print</summary>
    <ul>
      <li>Homes only: houses, condos, apartments and studios.</li>
      <li>Book and pay online before any visit. No money changes hands in your home.</li>
      <li>Fees cover Hollie’s time and taste and are paid upfront. The Casting Call fee is credited toward the piece.</li>
      <li>If Hollie comes up empty, the fee becomes store credit for 90 days.</li>
      <li>Rush applies to the service fee, never to item prices, and uses pieces already in the collection.</li>
      <li>In person, Hollie places furniture, hangs art and mirrors, sets lamps and styles. No electrical work, no plumbing, nothing that needs a permit, and no hiring trades for you: your own trades work for you directly.</li>
      <li>Sourced pieces are final once you approve them against condition photos, unless they arrive damaged or different from what you were shown. Collection pieces follow the shop’s usual policy.</li>
      <li>Prices are starting points, plus applicable sales tax.</li>
    </ul>
  </details>

  <div class="hire-cta" id="hire-contact">
    <a class="button button-cream" href="#hire-contact" data-hire="">Email Hollie <span aria-hidden="true">↗</span></a>
    <a class="button button-outline" href="__BOOKING_URL__" target="_blank" rel="noopener">Book a Screen Test <span aria-hidden="true">↗</span></a>
    <p>Or write to <a href="#hire-contact" data-hire="" data-hire-inbox>the shop inbox</a>. Attach your photos to the email that opens; it can’t attach them for you.</p>
  </div>
  <!-- Demo state (block 0 row 1 empty): use this .hire-cta instead of the one above.
  <div class="hire-cta" id="hire-contact">
    <button class="button button-outline" type="button" disabled>Booking opens soon</button>
    <p>Hollie is setting up the booking line. The occasions above show what’s on offer.</p>
  </div>
  -->

  <blockquote class="hire-epigraph">
    <p>“There never was a house so bad that it couldn’t be made over into something worth while.”</p>
    <footer>Elsie de Wolfe, <cite>The House in Good Taste</cite>, 1913</footer>
  </blockquote>
</section>
```

**Wording rule.** Do not add any of these to the section:
- "registered interior designer"
- "architect"
- "licensed", "certified" or "insured"
- "contractor" or "builder"
- "remodeling services" or "renovation services"
- "install lighting" or "hardwire"

They come from Florida ch. 481, 489 and 501; the citations are in the design doc. Step 5's test enforces this list.

## 3. The email links (`site/storefront.js`, append after the last `})();`)

Every `[data-hire]` link opens one brief; occasion links add their occasion to the subject and the first lines.
- `encodeURIComponent` turns the `&` in "Holliewood & Vine" into `%26`. A raw `&` would split the query (RFC 6068).
- Files can't be attached through `mailto:`, hence the line under the buttons.
- The fallback `href="#hire-contact"` keeps links harmless if the script doesn't run.
- In demo state (`inbox` empty) that fallback is the whole behavior: an occasion block scrolls to "Booking opens soon".

```js
// Fabulous From Online: every hire link opens the same email brief; occasion links add their occasion.
(() => {
  const inbox = ""; // Ricky's inbox address. Empty = demo state: links stay on #hire-contact ("Booking opens soon").
  if (!inbox) return;
  const brief = (occasion) => [
    "Hi Hollie,",
    "",
    "What I need (one find / a corner / a room / the whole house):",
    `The occasion: ${occasion}`,
    "Where (city; house, condo, apartment or studio):",
    "Rooms or areas:",
    "Budget:",
    "Needed by (or rush):",
    "How I'd like to work (video call / photos / in person):",
    "Things I love:",
    "Things I'm keeping:",
    "Hard no's:",
    "Inspiration link:",
    "Best times for a call:",
    "Name and phone:",
    "",
    "Photos attached: a wide shot of each space and each corner, in daylight.",
  ].join("\r\n");
  for (const link of document.querySelectorAll("[data-hire]")) {
    const occasion = link.dataset.hire;
    const subject = ["Fabulous From Online", occasion, "Holliewood & Vine"].filter(Boolean).join(" - ");
    link.href = `mailto:${inbox}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(brief(occasion))}`;
  }
  for (const node of document.querySelectorAll("[data-hire-inbox]")) node.textContent = inbox;
})();
```

The encoded href is about 780 characters, under the roughly 2,000 that c4 treats as the practical ceiling. That ceiling is inferred; RFC 6068 sets none.

Claude dry-ran steps 1, 2, 3 and 5 on copies of the real files in a scratch folder on 2026-10-28, in three states:
- **Demo** (empty inbox, demo CTA): 5 of 5 pass.
- **Live** (dummy inbox and Cal.com link): 5 of 5 pass.
- **Half-filled** (live CTA, empty inbox): fails with "with no inbox the section must ship the demo CTA".

A stub DOM decoded Dinner party to the subject "Fabulous From Online - Dinner party - Holliewood & Vine", with the body line "The occasion: Dinner party"; the link is 798 characters.

The CSS and the browser checks are untested; they are yours.

## 4. Styles (`site/homepage.css`, append; aim for about 40 lines)

- **Headings.** Copy `.showroom-invitation h2` for `.hire-intro h2`. Make `em` `var(--rust)`, as `sample-shop.css` does for other section headlines. `.hire-heading` uses `var(--display)`, about 28–34px.
- **Intro.** `.hire-intro` is a two-column grid like `.showroom-invitation` (1.1fr / .8fr). The photo frame copies `.showroom-invitation img`: 8px `#e6dac8` border, `aspect-ratio: 3/4`. Stack to one column under 768px.
- **Grids.** `.hire-ways` (3 columns), `.hire-tiers` (4 → 2 at ≤1000px → 1 at ≤560px) and `.hire-addons` (2 → 1) are grids of panels.
  - Panels: `border: 1px solid var(--line)`, `background: var(--paper-deep)`, padding about 24px, no white.
  - Reset list styles on these `ol`/`ul`.
- **Panel text.** `.hire-line` uses the display font in `var(--pink)`. `.hire-scope` is small caps or `var(--mono)` at 11–12px in `var(--muted)`. `.hire-price` uses `font-variant-numeric: tabular-nums`, and its `span` is block, small and muted.
- **Occasions.** `.hire-occasions` is a grid of `repeat(auto-fill, minmax(220px, 1fr))`. Each `a` is a bordered block with:
  - `min-height: 44px`, padding about 14px 16px
  - `strong` on its own line, `span` muted at 14px
  - hover and `:focus-visible` border `var(--rust)`
- **The rest.**
  - `.hire-steps` is a numbered list with the display-font numbers.
  - `.hire-disclosure` is one bordered panel.
  - `.hire-details summary` gets a pointer cursor, the display font and at least 44px height.
  - `.hire-cta` is a flex row that wraps, with gap 12px; its `p` is small and muted.
  - `.hire-epigraph` is centered, display italic, max-width 40ch, and its `footer` is small and muted.
- **Rhythm.** Section margin-bottom of about 90px, matching `.showroom-invitation`.
- **Motion and fonts.** No new animation and no new fonts. The existing `.reveal` class is optional.

## 5. Test (`site/tests/fabulous-from-online.test.mjs`, new)

`npm test` runs it with the others. It passes in demo state and in live state. It fails on a half-filled section: a placeholder left in, a live-looking CTA with no inbox, or an inbox that isn't an address.

```js
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import test from "node:test";

const root = fileURLToPath(new URL("../", import.meta.url));
const read = (file) => readFileSync(path.join(root, file), "utf8");
const page = read("storefront.html");
const script = read("storefront.js");
const section = page.match(/<section[^>]*id="hire-hollie"[\s\S]*?<\/section>/)?.[0] ?? "";

test("the hire section carries Ricky's name and every nav reaches it", () => {
  assert.ok(section, "section#hire-hollie is missing");
  assert.match(section, /Holliewood &amp; Vine Fabulous From Online/);
  for (const nav of ["desktop-nav", "mobile-nav", "footer-nav"]) {
    const block = page.match(new RegExp(`<nav[^>]*class="${nav}"[\\s\\S]*?</nav>`))?.[0] ?? "";
    assert.match(block, /href="#hire-hollie"/, `${nav} needs a Hire Hollie link`);
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
```

## 6. Acceptance (browser, before Ricky publishes)

Run `npm test` in `site/`. Everything passes, in demo state or live.

Then `npm run dev` (or `python -m http.server <port> --bind 127.0.0.1` from `site/`) and check:

1. At 1440, 390 and 320 CSS px:
   - no horizontal scroll
   - tiers go 4 → 2 → 1, and ways and add-ons stack
   - occasion blocks wrap with readable text
2. Hire Hollie in the header, the mobile menu and the footer each scrolls to the section. The mobile menu closes as its other links do.
3. Email Hollie's `href` (DevTools) starts `mailto:` followed by the inbox, contains `Holliewood%20%26%20Vine`, and the body has line breaks (`%0D%0A`). Click it: the mail client opens with that subject.
4. An occasion block, for example Dinner party, gives the subject "Fabulous From Online - Dinner party - Holliewood & Vine" and the body line "The occasion: Dinner party".
5. Both `<details>` open and close with the keyboard. Focus rings are visible on blocks, buttons and summaries.
6. Evening colors (footer toggle): everything stays legible on burgundy, and there is no white panel anywhere in the section.
7. Lighthouse accessibility stays at 100 (it was 100 at the public launch). The heading order runs h2 → h3 → h4 within the section.
8. Nothing else moved: the disco, the room editor, the bag, saved finds, and `site/tests/navigation-check.js` against the local page.

Commit the three edited files plus the test with a message that says what changed. Then `git pull --rebase` and push.

Demo state is safe to publish. When Ricky fills block 0 row 1:
1. Swap in the live `.hire-cta`.
2. Set `inbox`.
3. Rerun the tests and checks 3–4.
4. Publish as usual.
5. Record the version number at the top of this file.
