# Vintage

**Mustache moonwalk (2026-11-08):** "ready for moonwalk" means the mustached mannequin video/GIF task. The recovered iPhone handoff, references and November 7 continuous-motion drafts are in `assets/moonwalk/`. Mustache visibility and loop continuity still need fixing; free ZeroGPU remained blocked on November 8. A detached local GPU worker was started at 01:27 Eastern to download the model and render a new candidate; check `.venv/moonwalk-local/job/status.json` and its logs for live progress. A generated candidate is not visually approved. `docs/mustache-moonwalk.md` has the full status, credits, local worker and free-cloud retry. Read those instead of asking Ricky to explain the project again.

**Status (2026-10-26):** Vintage is Ricky's vintage resale shop, **Holliewood and Vine**. A physical room already exists
(burgundy walls, racks, lamps, art, a pink "do it for the plot" neon); the job is to put it online on
Etsy and Shopify, probably with its own site later. First pass done 2026-10-26: Drive folder of 10
photos + a 24 s walkthrough video pulled, inventory catalogued in `research/inventory/`, comps priced
by Sonnet subagents into `research/pricing/`, sample storefront built as an artifact. Photos and
video frames live in `assets/` (previews only; originals stay in Ricky's Drive). Next: Ricky re-shoots
the "needs photo" items. Shop name (Ricky, corrected 2026-10-27): **Holliewood and Vine** or
**Holliewood & Vine**. The spelling is **Hollie**, with **ie**.

**Space (2026-10-30, Ricky):** smaller now. Which catalogued pieces are on hand, and whether the space is a home, are unconfirmed. On-camera direction is three files: `docs/video-direction.md` (Full Picture, the long version: shows, how Hollie talks, every product and tool with prices, the schedule and calendar, accounts, rules, the shop side from Round D, the decisions, and the research and why), `docs/video-shoot-in-depth.md` (gear, settings, shot lists, editing) and `docs/video-shoot-quick.md` (the shoot-day card).

**Dashboard (2026-10-26):** ops dashboard researched (ten Sonnet reports in `research/dashboard/`) and
designed: `docs/dashboard-design.md` (what and why) and `docs/dashboard-handoff.md` (build order, smoke
tests, schema deltas). Same day, Ricky's call: listing from the phone is in Phase 1 (photos plus one
line in, Claude Haiku drafts, Etsy draft listing, Ricky taps Publish, Crosslist imports from Etsy and
fans out to eBay and Shopify; handoff T6b, smoke tests 13 and 14, an Anthropic key in section 0).
Nothing built. Step 0 is blocked on Ricky creating the eBay, Etsy, Shopify, Supabase Pro and Anthropic
accounts and keys (handoff section 0). The next build session starts at the handoff.

Drive folder (Ricky's second Google account, `u/1`): https://drive.google.com/drive/u/1/folders/1doMLpzt09qxtbSOjWFkBOCYSQQnb3HYD
The Claude Drive connector is on the other account and cannot see it; fetch through the signed-in
Chrome tab (Drive folder menu > Download gives one zip) or ask Ricky to share to the connector account.

**Storefront direction (2026-10-26):** The original room is a reference for the designer's taste and
composition, not a claim of an operating physical store. The site should feel like entering that
world: dimensional lettering, objects in the foreground, varied framed displays and deliberate
overlaps. Disco balls are signature gifts/handouts for buyers (confirmed by Ricky); do not infer an
every-order guarantee. Implemented direction and asset provenance: `docs/storefront-art-direction.md`.

**Photo direction (2026-10-28):** Ricky wants the full sample storefront on the homepage, using all
52 selected transparent product photographs on white framed panels, with item names, illustrative
prices and shopping controls. `site/demo-products.js` now supplies the public catalog and all room
layers. The build includes those selected photos and their 480/960px derivatives. The burgundy
entrance, mouse movement, disco and original neon-lit room remain. The owner’s mirror selfie appears
in the owner section. Rough item photos and stills are omitted. Fashion is excluded from room previews.
The browser-local bag demonstrates shopping;
checkout remains unavailable. See `docs/sample-storefront.md` and the historical `docs/demo-photo-pack.md`.

**Fixed visual constraint (Ricky, 2026-10-28):** White applies to product-photo framing only, never
the page-wide background. Keep the burgundy atmosphere throughout. The original entrance cutouts
(brass-and-cream urn lamp, sea-glass chandelier, cubist painting and disco ball) stay exactly those
objects; do not substitute sample catalog photographs at the top of the homepage. Their details
refer to the original objects, independently of sample listings that reuse the inventory IDs.

**Fabulous From Online (2026-10-28):** a section, now on its own page (`site/hire.html`, since 2026-10-29), where people hire Hollie to find a piece or style a corner, a room or a whole home. Six Sonnet reports are in `research/fabulous-from-online/`. Decisions are in `docs/fabulous-from-online-design.md`, and the build spec is in `docs/codex-handoff-fabulous-from-online.md`. The headline is "You bring the plot. Hollie dresses the set."
- Homes only, no rentals in v1, and payment online before any visit.
- Rush uses collection pieces only (Florida ch. 538 holds).
- Built and published in demo state ("Booking opens soon") as Sites version 27 on 2026-10-28; implementation commit `5675a95`. Ricky approved the written prices, free Screen Test and Hire Hollie nav label. Booking activates when Ricky gives the inbox address (block 0 of the handoff); no Cal.com link is configured. Verification and release details are at the top of the handoff.

**Type and spacing (2026-10-29):** research only; nothing in `site/` has changed. Four Sonnet lanes are in `research/type-and-spacing-2026-10-29/`. The synthesis, decisions and build order are in `docs/type-and-spacing.md`. Bodoni Moda and DM Sans stay; Space Mono vs Courier Prime is Hollie's pick. Floors: no text under 12px, body 16px, no Bodoni under 20px. Phase 1 waits on Ricky's word, and Codex publishes. The desk rules page is `Chief Of Staff/wiki/web-type-and-spacing.md`.

**Lighter homepage (2026-10-29):** Ricky approved the idea room's lighter-homepage layout.
- The homepage runs: entrance, collection, three doors, owner, honest details.
- The doors section carries the story (`#story`) and the disco line. Its doors are Try it in your room, Hire Hollie and the 3D showroom.
- The room editor lives on `site/room.html`, with its directions directly under the photo.
- Hire Hollie lives on `site/hire.html`.
- Departments and the browse bar are gone; the collection's own filters remain.
- Old `/#your-room` and `/#hire-*` links redirect. "Try it in your room" on a find opens `room.html?try=<id>`.
- Checks are in `site/tests/pages.test.mjs`.

**Round D research (2026-10-29):** research only; nothing in `site/` changed.
- Seven Sonnet lanes are in `research/round-d/`: social, shipping, email/SMS, reviews, search, local Southwest Florida, pricing.
- The decision layer is `docs/round-d-synthesis.md`: re-checked quotes, three corrections to the agents, decisions for Ricky and ranked ideas.
- Eight new idea pages plus two amendments are specced in `docs/codex-handoff-idea-room.md` section 8, for a second Codex build.
- Gating fact: items are `#item-<id>` hash routes today, so search and sold-page ideas need one real URL per piece.

**eBay photo studio (2026-11-07):** Ricky asked how to make eBay-grade photos of clothes on vintage forms with the background whited out, as automatically as possible, ready for when he is back at the PC. Two Sonnet sweeps (21 lanes plus 30 claim checks) are in `research/ebay-photo-studio-2026-11-07/`; decisions are in `docs/ebay-photo-studio.md`, the PC setup card in `docs/ebay-photo-studio-handoff.md`. Decided: real garment on a visible form on pure white from our own cut-out, close-ups kept as shot, no ghost mannequin or AI try-on by default. `tools/cutout/cutout.py` grew a 1600 px eBay export, keep-as-shot close-ups by file name, a rectangle repair for frames (tested on Ricky's framed print), a soft shadow option, watch mode and a manifest. The cloud session's network blocked eBay, Reddit, YouTube, Hugging Face web and vendor sites; `fetch-later.md` lists 153 URLs to crawl from the PC. `tools/crawl-cloud.sh` is the cloud stand-in for crawl.sh. PC side done 2026-11-07: the GPU venv `.venv/cutout` (onnxruntime-gpu 1.31.1, CUDA 13 DLLs from pip) runs 7 to 8 s a photo on the 4060 Ti and the CPU venv `.venv/cutout-cpu` 21 to 35 s; 139 of the 157 blocked pages were crawled into `research/ebay-photo-studio-2026-11-07/raw/fetched-on-pc/`, six Sonnet lanes re-verified the claims against them (`verify-on-pc/`) and the decision doc and handoff carry the verdicts and prices. Still unread: the five Etsy policy pages and Reddit, which need the signed-in Chrome tab.

**Photoroom Brand Library (2026-11-08):** set up and saved in the "Holliewood & Vine" Space (Pro) the same day via the Chrome extension; proof in `assets/brand/photoroom-brand-library-2026-11-08.jpg`. `docs/photoroom-brand-library.md` has the kit (three logos in `assets/brand/`, seven hexes, three fonts with TTFs in `assets/brand/fonts/`, brand info) and the step card, all checked against Photoroom's help pages the same day. Brand Library is a Pro-and-up feature.

Global rules (`~/.claude/CLAUDE.md`) apply: Vendor First, Plan Mode First, shell syntax matches the
tool, Claude pushes. Standalone workspace: nothing here touches brain-platform / SWFL Data Gulf.

## crawl4ai (the page fetcher, verified working from this folder 2026-10-26)

One machine-wide install, never reinstalled per project:

- Interpreter: `C:\Users\ethan\crawl4ai-venv\Scripts\python.exe`
- Git Bash shim: `C:\Users\ethan\.local\bin\crawl4ai` · PowerShell shim: `crawl4ai.cmd` beside it
- WSL shim: `~/.local/bin/crawl4ai` (execs the Windows venv; there is NO WSL-native venv)
- Fedora box: podman container `crawl4ai`, REST on `127.0.0.1:11235` (health 200 on 2026-10-26)

Call it:

```bash
tools/crawl.sh "<url>"                 # writes research/<host>-<utc>.md, warns under 1 KB
env -u MSYS_NO_PATHCONV crawl4ai "<url>" -o md -bc < /dev/null > out.md   # the raw form
```

Rules that cost real time before: always `< /dev/null` (it eats stdin in loops); always `env -u
MSYS_NO_PATHCONV` in the Bash tool (else exit 2, zero bytes, looks like a wall); always `-bc` plus a
unique output file when calls run concurrently (cross-call content bleed); under 1 KB is a bot wall,
not a page. Walls and workarounds: `dev/Chief Of Staff/wiki/crawl4ai.md`. Patchright is the
fallback for Cloudflare walls (`wiki/patchright.md`).

## Web search

SearXNG on the Fedora box, free, JSON, no key. `tools/search.sh "query" [general|science|news]`
prints `url | title | engine`. Then crawl the URL. Engines answering as of 2026-10-06: google cse,
bing, yahoo (science: scholar, semantic scholar, arxiv, europepmc). DuckDuckGo and Brave are dead
from that box. Details: `wiki/searxng.md`.

## Fedora box

`ssh fedora` (10.0.0.169, user `stanicky`, key `~/.ssh/fedora_stanicky`, in `~/.ssh/config`).
Always-on second runner on a second residential IP. CPU only (i7-8565U, 15 GB, no GPU), no sudo,
rootless podman, Python 3.14, Claude Code installed. Running there 2026-10-26: `crawl4ai`,
`searxng`, `ollama-agents` (qwen3.5:4b, ~7 tok/s), `beszel-hub`/`beszel-agent`.
Loopback-only services, so tunnel when a local client needs one:
`ssh -L 8888:127.0.0.1:8888 fedora`. Never edit a script a runner is executing; clone per session.
Inventory and gotchas: `wiki/machine-stack.md`, `wiki/shell-and-wsl-gotchas.md`.

## Keys

`.env.local` is a byte copy of the desk key store (`dev/Chief Of Staff/.env`) taken 2026-10-26,
gitignored. `.env.example` has the names only. Load with `set -a; . ./.env.local; set +a` in bash.
A new key goes into the desk `.env` first, then here. Never into brain-platform.

## Layout

- `research/` — fetched pages and notes, dated, with the source URL at the top. Raw layer, never rewritten.
- `tools/` — `crawl.sh`, `search.sh`. Add a script only when a third session would otherwise retype it.
- `docs/` — design and handoff documents (synthesis, decisions). Rewritten as decisions change. Index of every doc and research folder: `docs/README.md`.
- Anything worth keeping past this folder (a decision, a verified vendor fact, a lesson) goes to the
  desk wiki with `/compile <path>`; the wiki lives in `dev/Chief Of Staff/wiki/`.

## Git

Remote `origin` = github.com/ethanrickyjrjr-wq/Vintage (seen 2026-10-26). Every time a task lands:
`git pull --rebase`, secrets grep, commit, push. Structure changes (rename, delete, visibility) still need Ricky's word.
