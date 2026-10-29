# Idea room release — 2026-10-29

Published as **Sites version 34** at https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site/ideas.html.

- Sites source: `9939f99c5363347abfd294bb5cf2b76d07cf6d09`.
- Saved version: `appgprj_6adfa102ca188191b5cd6634c734894a~appgver_cf5438499c4c819186e9386b925b0adc`.
- Deployment: `appgdep_6ae340cd18648191902668d705740849`, succeeded.
- GitHub implementation: `5749610`; measured-layout follow-up: `4c372b9`.

The hub links thirteen idea pages, each with a preview banner, source line, layout mock and Keep / Maybe / Cut plus note controls. Picks stay in the current browser; the hub copies all thirteen decisions as text. Shopping and service controls are previews only. Every idea page and the hub are noindex/nofollow and remain unlinked from the homepage.

Only the new idea-room files, screenshot, handoff test and sixteen `build.mjs` list entries were added. This new release note records publication without editing the existing handoff. No homepage file was edited by this task. The Sites commit is a direct child of occasion release `c6fa483`, preserving its fifteen pages, pictures and homepage links, plus typography source `4df431b`, the Courier font/license and `type-review.html`.

## Verification

1. `npm test` passed all **40 tests**, including the existing room, catalog, Hire Hollie and concurrent occasion-page tests. `npm run build` passed.
2. `git diff --stat site/storefront.html site/storefront.js` was empty. The Sites addition also has an empty homepage diff against `c6fa483`.
3. Clicked all thirteen hub cards in Chrome. Each opened the expected page with its banner, decision fieldset and mock. No console errors or broken images. All **34 unique image URLs**, including every srcset candidate, exist in the deployment output and returned HTTP 200 locally.
4. Marked gone Keep, vibes Maybe and flash Cut on their respective pages, added notes, then reloaded the hub. All three choices and notes appeared. Copy my picks wrote the expected thirteen-line text to the clipboard.
5. Checked all fourteen pages at **1440, 390 and 320 CSS px**: **42 checks**, no horizontal scroll. Every decision pill was **46px** tall. Fixed the package-card min-content overflow found during this check.
6. Chrome DevTools emulation of `prefers-reduced-motion: reduce` gave `animation-name: none` for ticker, glint and neon. The glint pseudo-element was absent. Cleared the temporary override and verified normal motion returned.

The actual local room editor was used to place the Gold Egyptian bust lamp in the AI-generated example room. Its captured reference, `site/assets/ideas/send-room-1.webp`, is **60,584 bytes**. All sample titles and prices come from `demo-products.js` by file name. No dependencies were added.

## Homepage comparison measurements

Read `offsetHeight` at a 1440px browser viewport after fonts loaded, against the then-published v32 source. Browse navigation is grouped with departments in the ten-section diagram. Heights exclude outside margins, the header and gaps.

| Block | Height, px |
| --- | ---: |
| Entrance | 658 |
| Browse navigation | 69 |
| Collection | 8,796 |
| Departments | 742 |
| 3D showroom invitation | 480 |
| Story | 892 |
| Your room | 2,078 |
| Hire Hollie | 3,547 |
| Disco note | 550 |
| Owner | 449 |
| Good finds. Honest details. | 281 |
| Footer | 384 |

Ten content sections total **18,542px**; with footer, **18,926px**. The proposed version totals **11,048px**, retaining measured entrance, collection, owner, notes and footer, and estimating the three-door block at 480px. The diagram is a proposal only.

Local visual and machine-readable evidence is in ignored `artifacts/idea-room/`, including the editor capture, mobile screenshot, live release screenshot and responsive checks.

After publication, verified the live hub and sold-archive page in Chrome; all eight archive photographs loaded and no console errors were reported. A separate command-line HTTP probe was blocked with HTTP 403 by the hosted service, so full live URL coverage is not claimed; complete image-URL checks above were against the local build.

Hollie delivery: waiting for an email address or messaging contact; neither signed-in Gmail account yielded an identifiable matching contact.
