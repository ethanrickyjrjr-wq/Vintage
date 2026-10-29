# Storefront type and vintage details: decisions and handoff

2026-10-29. Implements Ricky's five-item follow-up to `type-and-spacing.md`.

**Published: Sites version 34**, in the combined release with the occasion pages and idea room.
Typography implementation: GitHub `56fde52`, Sites source `4df431bc2f704c48d87b22cb28604a4b0006ce23`.
Combined published source: `9939f99c5363347abfd294bb5cf2b76d07cf6d09`.
Deployment `appgdep_6ae340cd18648191902668d705740849` succeeded.
Live review: https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site/type-review.html .
The review heading and both full-shop links were checked on the published page.

## Decisions made

| Item | Decision and delivered behavior |
| --- | --- |
| Label face | Build both; **Space Mono remains the default pending Hollie's choice**. `type-review.html` compares identical labels and prices. Open `/?labels=space` or `/?labels=courier` for the full shop. The query applies only to that visit; no preference is stored. |
| Phone headline | **52px, expressed as `3.25rem`**, with natural wrapping. The 80px trial broke “influence” across letters at 320px. At 390px, 52px gives one line per phrase; at 320px, “Bad influence.” wraps at the space. The entrance is now in normal flow and grows with its copy, on desktop too. |
| Headline tracking | **-0.03em**. Compared against -0.055em side by side in Chromium at equal sizes. The looser version separates the italic joins and punctuation while retaining the Bodoni silhouette. Both specimens remain in the review page. |
| Vintage details | **Film-credit double rules and mono billing prices in Hire Hollie; receipt double/dashed rules and mono figures in the bag.** Keep the established burgundy room, gilt frames, invitation posters and disco as the main atmosphere. |
| Extra neon script | **Omit it.** The photographed sign already carries the phrase, and the Hire headline already uses the plot/set idea. A second glowing script competes with those elements. No Sacramento download or new sign animation. |

The entrance eyebrow, catalog category labels and Hire scope labels now use the mono face at a 12px rem-based floor. This is a targeted pass, not the full migration of every small label in the audit. Bodoni and DM Sans remain unchanged.

## Hollie's remaining choice

Review `/type-review.html` and both full-shop links on a phone and desktop. Recommend **Courier Prime** for its screenplay connection to Screen Test, Casting Call and Leading Role; retain Space Mono if Hollie prefers the cleaner labels.

Courier Prime is self-hosted with its OFL license in `site/assets/fonts/`. `size-adjust: 120%` matches its shorter caps to Space Mono. Its regular Latin file adds 18,640 bytes to the build, but normal Space Mono visits do not request it. This is an additional review face, not the +2.1 KB replacement cost in the earlier research.

To finalize Courier, change `--mono` in `site/storefront.css` to `"Courier Prime", "Courier New", monospace`, and update the review page's default explanation. To finalize Space Mono, leave the token as it is. After either choice, retain the comparison as an unindexed review page or remove it and its `build.mjs` entry together. If removing Courier entirely, remove its face declaration and the two Courier files together. The preview query affects mono labels and figures on the storefront; it does not carry into the separate 3D showroom page.

## Implementation handed off

**Lot numbers:** defer until a durable catalog identity exists. Add an explicit unique `lot` string to the authoritative product data. Assign it once and preserve it when sort order, title, photo or inventory ID changes. Original entrance objects and sample products that reuse IDs need separate identities. Validate uniqueness and stability before showing the same `No. 0042` on a card, its dialog and its bag line. Do not generate public lots from array order, CSS counters or the current colliding inventory IDs.

**Gallery labels:** add real maker, date/era, materials and dimensions to the catalog first. Render only populated fields, with the existing source credit retained. The sample pack's styling does not establish provenance. Do not invent museum-style metadata to complete the design.

**Other motifs:** leave swing tags, sunbursts, Greek-key rules, grain, foxing, marquee bulbs and ticket notches out of this pass. Reconsider only if the existing room and the two delivered print treatments leave a concrete design gap.

**Broader type audit:** sections 4 and 7 of `type-and-spacing.md` remain a separate task. That includes the other small labels, body-size migration, shared role/spacing tokens, fallback metrics, DM Sans preload, Bodoni weight range, faux italics, prose measures, intermediate Hire grid widths and dead-rule cleanup. Do not infer that those have shipped from this change.

## Verification and limits

- All 33 existing tests and the production build pass. After integrating the other sessions' additions, all 40 tests and the build pass.
- Chromium review at 320, 390, 820, 1100 and 1440 CSS px: no page-level horizontal overflow; hero copy and actions remain inside the growing stage.
- Root text size enlarged to 200% at 320, 390, 820 and 1440px: phone headline becomes 104px, wrapping is allowed, and copy stays inside the stage. This is a text-size fixture, not certification of the entire site's zoom accessibility.
- Equal-size tracking A/B and both real label faces reviewed; Courier Prime loads successfully. Bag still shows illustrative prices and disabled checkout.
- The text-spacing override (1.5 line-height, .12em tracking, .16em word spacing and 2em paragraph margins) leaves the hero contained at 320 and 1440px. It exposes an existing 13px overflow in the owner's price/copy at 320px; that belongs with the broader type audit above.
- Both existing burgundy themes were exercised in Chrome. Safari and Firefox still need a real-device/browser pass; this environment supplied Chrome.

Work was isolated in `C:/Users/ethan/dev/Vintage-storefront-finishing` to preserve the original checkout's staged work and live processes. GitHub changes are pushed to `origin/master`; Sites publication uses its existing project and public audience.
