# Handoff for Codex: close and back return you to where you were

**Status 2026-10-28, later the same day:** Ricky said "do it", so Claude built all six items below and pushed
them (`82b313f`). Codex published Sites version 21 but could not reach the browser console, so Claude ran
`site/tests/navigation-check.js` against the live homepage from Chrome DevTools: five PASS. Live showroom round
trips by hand: Back from the showroom and the showroom's "← Back" both restored scroll 14901 with the 3D teaser
in view. A curl of the live `catalog.js` right after publishing returned a stale Cloudflare edge copy
(`CF-Cache-Status: HIT`, old code) for a few minutes while the browser got the new file; a later curl was fresh.
If a check ever fails right after a publish, wait a few minutes and reload before blaming the code.

**Second fix, same day:** a product image dragged from the page replaced the room photo and Undo was empty (Ricky's
screenshot, 16:39). Built as item 2 of `codex-handoff-sample-room-and-star.md`, with check 10 added to the console
script. **Codex: publish only, then this file gets the new version number.**

The item sections stay as the record of what changed and why; their line numbers are from before the change.

Written 2026-10-28 by Claude for Codex. Ricky publishes through the Codex app; Claude cannot publish.
Ricky, 2026-10-28: "showroom and other things need to go back to where they were when you close something.
We don't want it going all the way back to the home screen or a different section. Buttons need to make sense.
Deleting something from your room shouldn't start all over or go to a different section."

Every item below was reproduced in Chrome against the repo at `9c28128`, which is byte-identical to the
live `catalog.js`, `storefront.js` and `showroom.js` (checked with curl 2026-10-28). Line numbers are at `9c28128`.

**Before you start:** `git status`, pathspec `git add` only, never `git add -A`. Another session commits to this
tree. Pushing does NOT publish. No new dependency. Do not touch `disco*.js`, `atmosphere.css`, `assets/`.

## 1. Browser Back from the 3D showroom lands at the top of the homepage

Reproduced: scroll to the "A different angle" teaser (scrollY 14901), tap "Explore in 3D", press Back.
Result: homepage at scrollY 0, no hash. The teaser is 14,000 px below.

Cause: `site/storefront.html:8-16`. `history.scrollRestoration = "manual"` plus a `pageshow` handler that
scrolls to the top whenever there is no hash. That handler also fires on a back/forward restore, so the browser's
own scroll restore is thrown away.

Fix (smallest): only force the top on a fresh visit, never on history traversal.
```js
const traversal = performance.getEntriesByType("navigation")[0]?.type === "back_forward";
history.scrollRestoration = traversal ? "auto" : "manual";
if (!traversal && !location.hash) window.addEventListener("pageshow", (event) => {
  if (!event.persisted && !location.hash) window.scrollTo({ top: 0, left: 0, behavior: "instant" });
});
```
`event.persisted` is true for a bfcache restore; leave those alone too. Keep the `#disco` / `#home` cleanup.

## 2. "Back to the collection" in the showroom is not a back

`site/showroom.html:55` (`.collection-return`), `:23` nav, `:30` "Browse our finds", `:61` footer link all go to
`/#collection` or `/`. That is a fresh load that resets filters and scrolls to the collection top (reproduced:
landed at scrollY 793, category "all", teaser at 14989).

Fix: make the one return control a real back when the visitor came from our own homepage, otherwise keep the link.
```js
document.querySelector(".collection-return").addEventListener("click", (event) => {
  if (history.length > 1 && document.referrer.startsWith(location.origin)) { event.preventDefault(); history.back(); }
});
```
Relabel it "← Back" (it is no longer specifically the collection). Leave the header nav and footer as plain links;
those are deliberate jumps. Item 1 makes the back land on the right scroll position. `showroom.js:175` already uses
`replaceState` for piece changes, so one Back leaves the showroom; keep that.

## 3. Closing a detail that was opened from the bag loses the bag

`site/catalog.js:421`: tapping an item title inside the bag closes the bag, then opens the detail. Closing the
detail (`:498-504`) focuses a card in the grid. Reproduced: bag open → tap title → close detail → bag closed,
focus on `.product-image`. The visitor was shopping their bag and is now somewhere in the grid.

Fix: remember that the detail came from the bag and reopen it on close.
- At `:421`, set `detailFromBag = bagDialog.open` (new `let` next to `detailReturnHash`, `:78`) before closing the bag.
- In the close handler, before `focusFind`: `if (dialog === productDialog && detailFromBag) { detailFromBag = false; openBag(bagTrigger); return; }`.
- "Try it in your room" (`room-preview.js:328-334`) closes the detail on purpose and navigates; it must clear
  `detailFromBag` first or the bag will pop over the room. Simplest: the `#your-room` early return at `:503`
  already runs before `focusFind`; put the bag reopen after it.

## 4. Browser Back while a detail is open wipes the search and filters

`showDetails` pushes `#item-ID` (`:286`). Back fires `hashchange` → `readHash` (`:326`) closes the dialog (`:356`)
and then, because the previous hash is `#collection`, a category or empty, resets `search`, `savedOnly` and
`category` and re-renders. Reproduced: search "lamp" (4 finds) → open → Back → dialog closed, search box empty,
"52 finds to explore".

Fix: when `readHash` runs because a detail is being closed, close it and stop.
```js
if (productDialog?.open) { productDialog.close(); return; }
```
at `:356`. The close handler already fixes the hash with `replaceState`. Deep links (`#lighting` on a fresh load)
still work because no dialog is open then.

## 5. Every category tap is a history entry

`updateHash` (`:95`) pushes for category/browse taps (`:436`) and for `reset` (`:270`). Reproduced: three category
taps added entries; Back then walks the filter history and scrolls to the collection each time, instead of leaving
the page. Only the product detail should push (so Back closes it). Change `:436` and `:270` to
`updateHash(..., true)`. Leave `:286` (detail) as a push.

## 6. Room editor: "Start over" sits where "Remove" should be

Reproduced at phone width: "Undo" and "Start over" are in the bar above the photo (`storefront.html:326-329`);
the per-find "Remove" (`:372`) is 1,086 px below the photo, under the layer list. A visitor who wants one find
gone sees "Start over" and clears the whole room. Removing a find or a pick does not navigate or scroll
(verified), so the "starts all over" report is this button.

Fix:
- Move the three layer actions (`#room-flip`, `#room-front`, `#room-delete`) up next to the size slider, directly
  under the photo, and keep the layer list below them. Or add an "×" per row in `#room-layers`
  (`room-preview.js:107-110`), same handler as `#room-delete` for that id.
- Rename `#room-reset` to "Clear the room" and keep it last in the bar; it must not look like a per-item delete.
- After `#room-delete` (`room-preview.js:315`) set the status to "Removed. Undo brings it back." The status currently
  still says "Placed. Drag the find…" after a remove (reproduced).
- Removing the last layer hides `#room-layer-controls` (`:115`), which shifts the page. Keep the controls visible
  but disabled when a photo is loaded and no find is placed, so nothing jumps.

Not broken, verified: bag "Remove" keeps the bag open and focuses "Continue exploring"; tray "×" and layer
"Remove" change no hash and no scroll; Undo restores a removed layer.

## Acceptance (desktop and 390 px; run every line, do not sample)

1. Homepage, scroll to the 3D teaser, open the showroom, Back → teaser in view, filters untouched.
2. Showroom "← Back" → same as 1. Open the showroom from a new tab (no referrer) → "← Back" goes to `/#collection`.
3. Next piece ×3, then Back once → on the homepage, not an earlier piece.
4. Search "lamp", open a find, press Back → dialog closed, search still "lamp", 4 finds.
5. Search "lamp", open a find, tap × → same as 4; hash is `#collection` or the category, never `#item-…`.
6. Bag → tap a title → close detail → bag is open again with the same items.
7. Bag → tap a title → "Try it in your room" → room section, bag closed, detail closed.
8. Tap three categories, press Back once → you leave the page (or return to the showroom you came from).
9. Room: place two finds, tap Remove on one → the other remains, status says removed, Undo brings it back,
   page does not scroll or jump. "Clear the room" asks nothing but is clearly labelled and sits last.
10. Keyboard: Escape closes each dialog and returns focus to what opened it; Tab reaches "← Back".
11. Room: place one find → a small disco ball drops into the photo's top-right corner. Tap it → music plays, the
    ball spins, mirror lights move over the room photo only (none on the controls or page). Clear the room → the
    ball goes and the music stops. Undo → the ball is back, silent. The entrance ball still works on its own.

Paste `site/tests/navigation-check.js` into the browser console on the homepage: it runs 1, 4, 5, 6, 8 and 9
and prints PASS/FAIL per line. It must print no FAIL before you publish.

## Publish

`node build.mjs` in `site/`, `npm test`, commit, push, then publish `site/dist` to the existing Sites project
(id in `site/.openai/hosting.json`), audience public. Then paste the console check into the live site and
report its output verbatim. Add the Sites version number to this file under a "Published" heading.

## Published

Sites version 21 was published publicly on 2026-10-28 from the `82b313f` site build.
The live console check remains unverified: the available browser connection did not expose the developer console.
