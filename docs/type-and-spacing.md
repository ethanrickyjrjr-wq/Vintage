# Type and spacing: what to fix, what to adopt

**Status (2026-10-29):** research done, nothing built. Ricky asked for a check that the site uses the
right fonts and spacing, with vintage styles worked in. Four Sonnet lanes reported; this document
reconciles them. **No `site/` change is made until Ricky approves**: the decisions are in section 6.
The live site deploys through Ricky via Codex, so a git push does not change it.

Evidence (read these for sources; every number below is traced there):

| Lane | Report | What it covers |
|---|---|---|
| A | `research/type-and-spacing-2026-10-29/a-vintage-type/REPORT.md` | Font choice, vintage type traditions, new shop references, bytes |
| B | `research/type-and-spacing-2026-10-29/b-vintage-vocabulary/REPORT.md` | Vintage motifs as native CSS, ranked |
| C | `research/type-and-spacing-2026-10-29/c-web-type-spacing/REPORT.md` | Fluid type scale, floors, Didone optical sizing, fallbacks |
| D | `research/type-and-spacing-2026-10-29/d-css-audit/REPORT.md` | Read-only audit of every size and spacing value in `site/*.css` |

## 1. What existing research said

- **The desk (Chief of Staff) has no typography or spacing page.** `wiki/vintage.md` predates the shop. The nearest desk material is the HQ dashboard's card geometry, which doesn't apply to a storefront.
- **The reusable rules came from three places.** We kept their rules, not their numbers:
  - `brain-platform/docs/standards/email-build-playbook.md` §1.3, §1.4 and §1.16. These give role tokens that bundle size, leading and weight; one spacing scale; a 45–75 character measure; and the rule that internal space is no larger than external space.
  - `research/dashboard/07-ui-ux-frontend.md` §4.2–4.3. This sets a 12px floor, 16px body text and inputs, and a 4px grid.
  - Global design skills: serif is allowed when the brand is genuinely vintage. That's the case here, so Bodoni is justified.

## 2. Verdict on the fonts

| Face | Verdict | Why |
|---|---|---|
| **Bodoni Moda** (display, wordmark) | **Keep.** Widen `fonts.css` to `font-weight: 400 900`. | The shipped files already contain weights 400–900 and optical sizes 6–96, verified with fontTools. Widening costs 0 bytes (A). Today nothing asks for more than 500 and nothing renders faux-bold (A, D). |
| **DM Sans** (body) | **Keep.** | Jost is the period-correct runner-up, but body text would need about 16.4px to match (A). The shipped DM Sans has **no tabular figures**, so the existing `tabular-nums` on prices does nothing. Verified: GSUB features are calt, ccmp, dnom, frac, liga, locl and numr; digit widths run 342–656. |
| **Space Mono** (labels) | **The weak link.** It runs at 8–11px, but its own README calls it a display face. | Candidate swap: **Courier Prime**, a screenplay typewriter face that matches the film copy in Hire Hollie (Screen Test, Logline, Casting Call). It adds +2.1 KB and needs `size-adjust: 120%` because its caps are 17% shorter. A live injection test showed no overflow at 1440, 390 or 320px; one eyebrow wraps at 320 (A). This is decision 1. |
| Accent script | **None by default.** | Optionally, one new neon line "do it for the plot" (48px or larger) above the Hire contact, in Sacramento, at +6.2 KB. No script matches the real sign's hand. Bodoni italic plus a glow is the zero-byte fallback (A). This is decision 5. |

**Correction to my first read-out:** I flagged about 11 headings as possibly faux-bold. Lanes A and D measured computed styles in Chromium and found **none**: those headings set weight 400 through the `font:` shorthand. What D did find is **two faux-italics in DM Sans**, which has no italic face: `p.owner-aside` and the `<cite>` in the Hire epigraph.

## 3. What is wrong today (lane D, measured)

- **The 6–9px labels are the core problem.** 115 font-size declarations are under 12px, and 77 of them are live. At 390px, **25% of visible characters render under 12px** (18% at 1440).
  - The worst cases: a 7px owner kicker on phones; an 8–9px category chip and category line in the product dialog, which buyers read before "Add to bag"; and a 9px uppercase chip on all 52 phone cards.
- **There is no type scale.** The CSS has 80 distinct size expressions and 22 line-heights. Body text is 15px at line-height 1.6.
- **There is no spacing scale.** The CSS has 70 distinct spacing values. The most-used one is **20px**, used 64 times, and it isn't on the 4/8/12/16/24 grid.
- **Tracking set in px breaks when the type resizes.** One example is the "HV" monogram: it was designed at -0.125em but now renders at -0.169em, because a later rule shrank its size while the px tracking stayed.
- **The measure is too wide in places and too narrow in others.**
  - Too wide: the Hire fine print and disclosure run 83–90 characters per line, and the music credit runs up to 189.
  - Too narrow: the Hire grids squeeze down to 18–19 character columns at 820 and 1100px.
- **The cascade has drifted.** `.product-title` alone has 12 size declarations across 4 files. About 63 rules (the `.hero*`, `.tour-button`, `.price-notes` and `.back-top` families) appear to match nothing.

## 4. The system to adopt

These come from lane C's token block, amended by A, B and D. The full CSS is in the lane C report.

**Type roles.** Ten sizes, down from 80. They scale fluidly (Utopia method) from 360 to 1500px, base 16 to 18px, ratio 1.2 to 1.25, sized in rem so browser text settings work.

| Role | Size | Face | Leading | Tracking |
|---|---|---|---|---|
| Hero | 52 → 130px (its own clamp) | Bodoni 500 | 1.1 | -0.02em by the research; today -0.055em (decision 3) |
| H1 | 40 → 55px | Bodoni 500 | 1.1 | -0.015em |
| H2 | 33 → 44px | Bodoni 500 | 1.15 | -0.01em |
| Card title | 23 → 28px | Bodoni 500, `font-optical-sizing: none` | 1.2 | -0.01em |
| Price | 19 → 22.5px | DM Sans 600 | 1.2 | 0 |
| Body | 16 → 18px | DM Sans 400 | 1.5 | 0 |
| Meta (size, condition) | 13.3 → 14.4px | DM Sans 400 | 1.45 | 0 |
| Label | 12px, with an 11px floor for decorative tags only | mono, uppercase | 1.3 | 0.08em (allowed 0.06 to 0.12) |

Rules that come with the roles:
- **No Bodoni under 20px, and none on prices, sizes, conditions or buttons.** Lane C measured the hairline at about 0.2 CSS px at every size, and `opsz: auto` doesn't thicken it. From 20 to 31px, use `font-optical-sizing: none`, which doubles the hairline. No Bodoni italic under 28px.
  - **X verified, Y needs review:** the existing 23px italic disco sign-off fails this rule on C's measurement, but lane A judged it to read well by eye. Check it on a 1x Windows monitor before changing it.
- **Tracking is always in em, never px.** Display text runs -0.01 to -0.02em. Labels use 0.08em instead of today's 0.14.
- **Prices:** DM Sans can't do tabular digits. A single price per card doesn't need them. Column figures (bag lines, totals, the receipt) use the mono face, whose digits are uniform. Bodoni with `tabular-nums` also works, but only at 20px and above.
- **Ordering trap:** the `font` shorthand resets `font-optical-sizing` and `font-variant-numeric`. Set those after `font:`.

**Card order:** maker, era and place as a label → Bodoni title → price (the only 600 weight on the card, in the same corner on every card) → size and condition as meta (C, from NN/g and Baymard).

**Spacing:** 4 / 8 / 12 / 16 / **20** / 24 / 32 / **40** / 48 / 64 / 96. 20 and 40 are added to the grid from earlier research because lane D found 20 to be the site's most-used value. Those two additions remove about 100 of the 177 tokens that would otherwise move by more than 2px. Two fluid tokens sit on top: page gutter 16 → 32px and section gap 48 → 96px. Padding inside labels and tags goes in em, so the WCAG 1.4.12 text-spacing override can't clip them.

**Line-heights:** 1 (icons and badges), 1.15, 1.3, 1.5 and 1.7. These replace the current 22.

**Loading:**
- Add metric-matched fallback faces: DM Sans → Arial, Bodoni → Times New Roman, mono → Courier New. The values are computed in lane C, and it takes about 15 lines with no dependency. Bodoni is 14% wider than Times, so without them the hero reflows when the font swaps in.
- Preload DM Sans. Today only Bodoni is preloaded.

## 5. Vintage elements to adopt

Lane B's ranked picks, all CSS with no new image assets:

1. **Lot numbers ("No. 0042").** A small mono label on cards, in the dialog and in the bag. The number must come from data: a stable `lot` field assigned at build. Don't reuse the inventory IDs, which collide, and don't use CSS counters. `.product-id` already renders but is hidden.
2. **Gallery-label block** using the museum tombstone order (maker, title, date, materials, dimensions). Show **only the fields that are real**. Sample listings have none of those fields yet, so the photo-source link stands in as the credit line. Don't invent dates or dimensions.
3. **Film title card and credits** for Hire Hollie, whose copy is already film language, and for the footer. A double rule, Bodoni names, dotted leaders and mono prices. Set the names at 20px or more, per the Bodoni floor, not lane B's 18px.
4. **Swing price tag**, on the dialog price and a few featured pieces only. On all 52 cards it becomes a tag farm.
5. **Receipt slip for the bag.** It keeps saying the prices are illustrative and checkout is off.

Optional extras:
- A single static gilt sunburst behind the Fabulous headline. Sunbursts are a verified Hollywood Regency motif.
- A Greek-key divider. Treat its link to Hollywood Regency as unverified.

**Avoid:**
- Paper grain and foxing: they read as damage on the item.
- Live neon text: Bodoni's hairlines wash out, and there's a risk under WCAG 2.3.1 (flashing).
- Animated marquee bulbs.
- Matchbooks.
- Ticket notches on the 15 occasion cards.
- №, ★ and ✦: none of the three fonts has these glyphs.

## 6. Decisions for Ricky (and Hollie, who picks the looks)

1. **Labels: Space Mono or Courier Prime?** I recommend building both as a preview and letting Hollie pick. Courier Prime fits the screenplay voice; Space Mono costs nothing to keep.
2. **Hero on phones.**
   - Keep the 52px floor, which fits on one line but grows only 1.42x at 300% zoom.
   - Or raise it to 80px and let it wrap, which reaches 2x at 300% zoom and is WCAG 1.4.4-safe.
3. **Hero tracking.** Today it's -0.055em, about 3.4x what optical-size serifs use. The research suggests -0.02em, or at most -0.03em. It's the signature look, so it needs an eyeball A/B, not a rule.
4. **Which vintage elements ship.** My order is 1 → 3 → 2 → 5 → 4. Lot numbers need the `lot` data field first.
5. **A neon script line, yes or no?** If yes, Sacramento above the Hire contact. If no, zero bytes.

## 7. Build order once approved

**Phase 1: fixes that don't change the look** (about 35 lines; lane D's quick wins):
- Raise the labels, kickers, phone cards and product dialog to 12px.
- Raise body text to 16px.
- Cap prose at about 65 characters and fix the Hire grids at 820 and 1100px.
- Add `text-wrap: balance` to headings and `text-wrap: pretty` to paragraphs.
- Convert the 5 px trackings to em, which restores the monogram.
- Move the 2 faux-italics to Bodoni italic, then add `font-synthesis-weight: none`.
- Widen Bodoni to 400–900.
- Add the fallback faces and preload DM Sans.

**Phase 2: tokens.**
- Add the section 4 roles and spacing as custom properties.
- Migrate selectors one file at a time, in cascade order.
- Delete dead and shadowed rules, about 300 lines. This changes nothing visible but leaves one source per selector.

**Phase 3: vintage elements** from decision 4, plus decisions 1 and 5 as previews.

**Check each phase before it ships:**
- `npm test` in `site/`.
- Screenshots at 360, 390, 820, 1100 and 1440px, with the product, bag and Account dialogs open.
- No horizontal overflow at 320px.
- A 200% zoom check and the WCAG 1.4.12 text-spacing bookmarklet.
- Safari and Firefox at least once. All research rendering was Chromium.

Another session is editing `site/` right now, so look line numbers up by selector, not by the numbers in the lane D report.
