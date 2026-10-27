# Handoff for Codex: a way back to the sample room, plus the green-star report

Written 2026-10-27 (about 18:00 local) by Claude for Codex. Ricky publishes through the Codex app; Claude cannot publish to the site.
Two items. Item 2 is code plus a publish. Item 1 is a check, not a change.

**Before you start:** `git status`. On 2026-10-27 the tree had uncommitted edits in `site/demo.css` and `docs/demo-photo-pack.md` that Claude did NOT make
(another Codex session). Do not overwrite or revert them. Pathspec `git add` only, never `git add -A`. Commit and push when each item lands.
Pushing does NOT publish the site. Line numbers below are at `7337062` and may have moved. Shop name is spelled **Holliewood and Vine** (Ricky, 2026-10-27).

## 1. Green star: gone from the deployed site, Ricky still sees one

What it was: the character U+2733 (✳) in the header wordmark and in the corner of the owner section. Phones draw it as a green-square emoji. Removed in `8ce0eb4`.

Checked against the live site (https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site, Sites version 15) at 17:53 local:
- `storefront.html` has 0 `wordmark-star`, 0 `✳`; `storefront.css` has 0 `owner-star` / `wordmark-star`.
- Every live `.html`, `.css`, `.js` file, scanned for code points at or above U+2190, contains only: ↗ ♡ ♥ ☰ ▷ ⌕ ↓ ↑ ♪ ◐ ◑ ✓. No star, no ✳ ❇ ✴ ⭐ ✅.
- No star in CSS escapes (`\2733` and the like) or JS escapes in the source.
- `favicon.svg` is a burgundy "H" with a small plus. Not a star.
- Headers are `Cache-Control: public, max-age=0, must-revalidate`, so a normal visit rechecks. A phone tab left open, or restored from memory, can still show the old page.

X verified, Y needs review: the deployed files have no star (verified). What Ricky's phone is showing is not verified; Claude cannot see it.

Do this, and no more:
1. Ask Ricky to close the tab and reopen the link (or pull to refresh), then tell you whether it is still there.
2. If it is, get a screenshot with the spot circled and find the real element. Do not delete more glyphs on a guess.
3. This publish also carries `7337062` (Holliewood branding). The live page still says "Hollywood".

## 2. Room editor: Ricky dragged a photo in and cannot get back to the sample room

Ricky's screenshot: `C:\Users\ethan\OneDrive\Documents\Pictures\Screenshots 1\Screenshot 2026-10-27 174946.png`. It shows the editor with the Cubist painting photo as
the room, labelled "Your room / placement sketch" (the non-sample label), and the Cubist figure as the selected pick. Ricky said they accidentally dragged the picture
photo over and there is no way back to "the original room we provide".

What the code does (verified by reading, not reproduced in a browser):
- `site/room-preview.js:249-253`: any drop that is not a find id goes to `upload(event.dataTransfer.files[0])`. `dragover` (line 247) accepts anything typed "Files".
- `upload()` replaces the photo, empties `layers` and `history` (line 160) and hides `#room-upload` (line 162).
- `#room-use-example` ("Or try our sample room") lives only inside `#room-upload` (`storefront.html:399`). Once a photo loads, it is hidden for good.
- What is left: "Change photo" opens the file picker; "Start over" (line 304) keeps the photo; Undo restores layers only. Nothing returns to the sample.
- Today's workaround: reload the page. The start screen shows the sample button again. It clears the room, as the page copy says.
- Likely cause of the accidental swap (inferred, confirm first): dragging an `<img>` from the page, such as `#room-product-image` (`storefront.html:413`) or a pick thumbnail, puts an image file in `dataTransfer.files`, so line 252 treats it as an upload.

Build the smallest fix:
- **A. Way back.** Pull the click handler at lines 243-246 into `loadSample()`. Add a "Use sample room" button in `.room-bottom-bar` beside "Change photo" (`storefront.html:405-408`). Show it whenever a photo is loaded and the current photo is not the sample (track `state.sample`). Use a new id, not a duplicate `room-use-example`. Add it to the busy-disable list at line 118. Same label and status text as the existing sample path.
- **B. Stop accidental swaps.** Set `draggable="false"` on `#room-product-image`, the pick thumbnails and the `.room-example img`. In the drop handler, ignore drags that carry `text/uri-list` or `text/html` alongside Files, since real files from the OS carry only Files. Check the actual `types` in Chrome and Safari before you rely on that rule.
- **C. Optional, only if small.** Keep one previous `{photo, layers, unplaced}` so a swap can be undone.

Acceptance (run in a real browser; also at 390 px wide):
1. Sample loaded: label reads "Sample room / AI-generated example", the new button is hidden.
2. Own photo loaded: the button shows; click it, the sample loads, layers reset, label and status update.
3. Drag a pick thumbnail, `#room-product-image` or the sample image onto the stage: nothing happens, the photo stays.
4. Drag a real JPG from Explorer onto the stage: it still loads.
5. Drag a pick row that has an overlay: it still places the find.
6. The button is disabled while the room guide is loading. It is reachable by keyboard and has an accessible name. The bottom bar does not scroll sideways on a phone.

## 3. Publish

Do not touch `site/disco*.js`, `atmosphere.css`, `assets/editorial/`, or the in-flight demo files. No new dependency.
Then: `node build.mjs` in `site/`, push, publish `site/dist` to the existing Sites project (id in `site/.openai/hosting.json`), keep audience public.
Verify with `curl`: the live `storefront.html` contains "Holliewood" and the new button id, and contains no `✳`. Add the version number and commit to the publication note in
`docs/room-preview.md`. If a push fails, report the exact error.
