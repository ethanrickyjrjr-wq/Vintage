# Vintage docs: index

Map of `docs/` and `research/`, written 2026-10-30. Pointers only: every doc keeps its own status line, so read that before trusting a line here. Project status and the fixed constraints are in [`../CLAUDE.md`](../CLAUDE.md); the Codex push rule is in [`../AGENTS.md`](../AGENTS.md).

The desk wiki has a page on this project (`dev/Chief Of Staff/wiki/vintage.md`), filled by `/compile`. It lags this folder. When the two differ, the docs here win.

## Where a new thing goes

- A decision, design or handoff: `docs/`, rewritten as decisions change.
- Evidence (fetched pages, subagent reports): `research/`, dated, source URL at the top, never rewritten.
- A fact or lesson that outlives this folder: the desk wiki, with `/compile <path>`.

## The site as built

- [storefront-art-direction.md](storefront-art-direction.md): the visual direction for the homepage and where the art came from.
- [sample-storefront.md](sample-storefront.md): the 52-photo sample catalog on the homepage; checkout stays unavailable.
- [demo-photo-pack.md](demo-photo-pack.md): historical. The earlier private-only photo pack, superseded by the sample storefront.
- [demo-showroom.md](demo-showroom.md): the 3D showroom and cutout lab; the public release is `site/showroom.html`.
- [room-preview.md](room-preview.md): the room editor (`site/room.html`) and its phone directions.
- [cutout-catalog-handoff.md](cutout-catalog-handoff.md): cut-out product tiles for the catalog.
- [room-cutout-review.md](room-cutout-review.md): which proposed room items cannot yet become honest layers.
- [occasion-pages.md](occasion-pages.md): the 15 "What's the occasion?" pages.
- [type-and-spacing.md](type-and-spacing.md): the type research and decisions. [type-and-spacing-handoff.md](type-and-spacing-handoff.md) is what was implemented.
- [account-layout.md](account-layout.md): where My Finds, My Rooms, Account and Bag sit, with Coming soon screens. [account-preview.md](account-preview.md) is superseded by it.
- [codex-handoff-navigation.md](codex-handoff-navigation.md): close and back return you to where you were (built).
- [codex-handoff-sample-room-and-star.md](codex-handoff-sample-room-and-star.md): the 2026-10-27 handoff for a way back to the sample room, plus the green-star report.
- [idea-room-release.md](idea-room-release.md): release log for the idea room.

## eBay photo studio (clothes on forms, white backgrounds)

- [ebay-setup.md](ebay-setup.md): the approved two-business-day dispatch and 30-day return baseline, free-profile setup now and Store upgrade later, reusable footer, listing templates, customer replies and brand assets in `assets/ebay-shop-kit/`. Prepared November 8; account implementation remains pending browser access.
- [ebay-photo-studio.md](ebay-photo-studio.md): the decisions (visible form on white, honest close-ups, no ghost mannequin or AI try-on by default), the rules, the tools, the shoot, what the tests showed, what is still unverified.
- [ebay-listings-2026-11-08.md](ebay-listings-2026-11-08.md): the 2026-11-08 batch of seven garments (Liz Claiborne, Future Collective, Ronny Kobo, Brooks Brothers, The Limited, Starlo, We The Free): how each image was cut, the title, item specifics and description per piece, the measurement sheet to fill in, and ballpark prices to replace with comps. Images in `assets/ebay-2026-11-08/ebay/`.
- [photoroom-brand-library.md](photoroom-brand-library.md): the Photoroom Brand Library kit for Holliewood & Vine (logos in `assets/brand/`, palette, fonts, brand info), what Photoroom accepts, and the ten-minute upload card.
- [../research/instagram-and-marketplaces-2026-11-08.md](../research/instagram-and-marketplaces-2026-11-08.md): what the public `@holliewoodandvine` Instagram, the `holliewoodandvinellc` eBay store and the Depop page showed on 2026-11-08, and what it changes for the Photoroom kit, the social manual, the site and the eBay and Shopify plans.
- [ebay-photo-studio-handoff.md](ebay-photo-studio-handoff.md): the card for the Windows PC: install, GPU check, first run, daily flow, shopping list, fetching the blocked pages.
- [facebook-marketplace.md](facebook-marketplace.md): current preparation on Hollie's established account, the existing 186-follower shop Page, the saved item 01 draft and its missing facts. Personal profile and live Page stay unchanged; local Southwest Florida Page copy and artwork review are in [the Facebook review pack](../assets/facebook-shop-kit/preview.html). Earlier second-account work and dated Meta sources remain as history.
- [instagram-video-2026-11.md](instagram-video-2026-11.md): promoting new listings with Instagram video. Covers ranked formats, which tools to use or skip (Claude + ffmpeg, Photoroom, ChatGPT, Hugging Face, paid generators), rules for our videos and the Fable 5.2 build order. Built from seven Sonnet lanes in `research/instagram-video-2026-11-13/`, with a working 11 s reel proof in `poc/`.
- [following-2026-11.md](following-2026-11.md): how to build a following before the Marketplace and eBay launch. Covers what Ricky must decide first, Facebook Pages to like and groups to join in order (four checked signed-in on 2026-11-09), Meta's and eBay's red lines, the free-account eBay levers and two shop-kit fixes. Built from seven Sonnet lanes in `research/following-2026-11-09/`.
- [launch-todo.md](launch-todo.md): the ordered to-do for the Facebook and eBay launch, a snapshot of the first export. The live copy with statuses is in the allstatecoop@gmail.com Drive at `My Drive/Holliewood Launch`, written by `tools/launch-drive-export.py` together with the plan and research as docx.
- [ebay-drive-items.md](ebay-drive-items.md): the rule of one Drive folder per eBay item (photos plus `listing.txt`), the script that builds and checks it, and the 2026-11-08 check.
- [ebay-weights-2026-11-12.md](ebay-weights-2026-11-12.md): paste-ready fill-ins for the 20 clothing drafts: measurement lines from the 11/12 tape photos, the smoke-free line (Ricky confirmed every piece is from a non-smoking home), and packed weight and box size estimated at the high end. Nothing has been weighed or entered into eBay.
- `tools/cutout/cutout.py` is the script both describe; `tools/crawl-cloud.sh` is the cloud-session page fetcher the research lanes used.

## Hire Hollie (Fabulous From Online)

- [fabulous-from-online-design.md](fabulous-from-online-design.md): decisions, prices and occasion styling.
- [codex-handoff-fabulous-from-online.md](codex-handoff-fabulous-from-online.md): the build spec and its verification.

## Ideas and research syntheses

- [codex-handoff-idea-room.md](codex-handoff-idea-room.md): preview pages for Hollie to decide on. Section 8 specs the Round D pages for a second build.
- [round-d-synthesis.md](round-d-synthesis.md): being found, keeping people, shipping safely. [research-brief-round-d.md](research-brief-round-d.md) is the brief behind it.
- [site-ideas-and-consignment-synthesis.md](site-ideas-and-consignment-synthesis.md): ten reports on site ideas and consignment, including Florida ch. 538.

## Social and video

- [mustache-moonwalk.md](mustache-moonwalk.md): the mustached mannequin's backward-moonwalk video and GIF, recovered iPhone handoff, character references, driving clip and generation status.
- [social-manual.md](social-manual.md): the social media manual. [social-manual-appendices.md](social-manual-appendices.md) holds the content banks.
- `social-manual-phone.html`: derived copy of the two files above. Edit the markdown, then run `python tools/build-phone-manual.py`.
- [codex-handoff-social-autopilot.md](codex-handoff-social-autopilot.md): the build handoff. Designed, nothing built.
- Video, three files (each is also a PDF in Ricky's Downloads, built from the markdown):
  - [video-direction.md](video-direction.md): **Full Picture**, the long version. The shows, how it looks, how Hollie talks, scripts, one shoot, every product and tool with prices, the schedule and calendar, accounts, rules, the shop side, decisions, and what was researched and why. Published as a claude.ai page titled Full Picture.
  - [video-shoot-in-depth.md](video-shoot-in-depth.md): **In depth Video making**. Gear, phone settings, light, sound, shot lists, editing, posting.
  - [video-shoot-quick.md](video-shoot-quick.md): **To the Point Videos**. The two-page shoot-day card.
  - `video-direction-phone.html`: the short phone edition, a public claude.ai artifact. It matches the three files above.

## Hermes, Telegram and sourcing

- [hermes-telegram-automation.md](hermes-telegram-automation.md): what the Hermes Agent and its Telegram gateway on the PC can do for the shop (list from the phone, cut-outs back to the phone, estate-sale digest, lot watch, a New Finds channel), the fixes needed first, and what not to build. Ideas only, nothing built. The Hermes docs crawled 2026-11-08 are in `research/hermes/`.
- [sourcing-2026-11.md](sourcing-2026-11.md): where to buy cheap, easy-to-list stock (online bulk, local SWFL venues, what to buy and the buy ceilings), from three Sonnet lanes in `research/sourcing-2026-11-08/`.
- [sourcing-calendar-2026-11.md](sourcing-calendar-2026-11.md): the dated field calendar for November with a link per sale (the Lockerfox mannequin lot included), rendered to Ricky's Drive (`G:\My Drive\Holliewood sourcing\`) with `tools/md-doc.py`, which turns simple markdown into a .docx with live hyperlinks.

## Ops dashboard

- [dashboard-design.md](dashboard-design.md): what and why. Designed, nothing built.
- [dashboard-handoff.md](dashboard-handoff.md): build order, smoke tests, schema deltas.

## Other

- [music-and-lights-notes.md](music-and-lights-notes.md): what shipped for music and disco lights.
- [notebooklm-brief.md](notebooklm-brief.md): a self-contained project brief written 2026-10-27. A snapshot, not kept current.
- `photo-checklist.html`: the shoot checklist (kit, set up, every item, shot list, special cases).

## Research folders

| Folder | What is in it | Synthesis |
|---|---|---|
| `inventory/`, `pricing/` | the catalogue and the priced comps | none; `pricing/SUMMARY.md` |
| `dashboard/` | ten reports plus raw crawls | [dashboard-design.md](dashboard-design.md) |
| `site-ideas/`, `consignment/` | ten reports | [site-ideas-and-consignment-synthesis.md](site-ideas-and-consignment-synthesis.md) |
| `fabulous-from-online/` | six reports | [fabulous-from-online-design.md](fabulous-from-online-design.md) |
| `round-d/` | seven lanes plus raw crawls | [round-d-synthesis.md](round-d-synthesis.md) |
| `social-2026-10-29/` | 19 lanes | [social-manual.md](social-manual.md) |
| `type-and-spacing-2026-10-29/` | four lanes | [type-and-spacing.md](type-and-spacing.md) |
| `video-direction-2026-10-30/` | video transcripts and a README | [video-direction.md](video-direction.md) |
| `cutouts/`, `room-editor/` | cutout tools, grid references, placement benchmarks | [cutout-catalog-handoff.md](cutout-catalog-handoff.md), [room-preview.md](room-preview.md) |
| `music-sources/`, `music-synth/`, `disco-visuals/` | music and light research | [music-and-lights-notes.md](music-and-lights-notes.md) |
| `3d-capture/`, `demo-photo-sourcing/` | 3D capture docs, photo sourcing lists | [demo-showroom.md](demo-showroom.md), [demo-photo-pack.md](demo-photo-pack.md) |
| `account-layout-2026-10-29/` | one note | [account-layout.md](account-layout.md) |
| `vinted-2026-10-30/` | Vinted rules and crosslister support, raw pages plus a README | its README |
| `ebay-clothing-photos-2026-10-30/` | eBay photo and clothing pages fetched 2026-10-30, with a README of the rules | [ebay-photo-studio.md](ebay-photo-studio.md) |
| `ebay-photo-studio-2026-11-07/` | 21 Sonnet lanes on photographing clothes for eBay (models, rembg, ghost mannequin, AI try-on, pipeline, gear, eBay rules, hosted services, phone tools), raw pages, test results on Ricky's photos, a verification table, `fetch-later.md`, `raw/fetched-on-pc/` (the pages crawled from the PC on 2026-11-07) and `verify-on-pc/` (six re-verification reports against them) | [ebay-photo-studio.md](ebay-photo-studio.md) |
| `instagram-video-2026-11-13/` | seven Sonnet lanes (reels mechanics, vintage formats, Photoroom, Hugging Face, ChatGPT and hosted tools, Claude builds, rules and risk), raw crawls and the ffmpeg proof in `poc/` | [instagram-video-2026-11.md](instagram-video-2026-11.md) |
| `following-2026-11-09/` | seven Sonnet lanes (Facebook f1 to f4, eBay e1 to e3), raw crawls and the parent's signed-in check (`raw/parent-chrome-check.md`) | [following-2026-11.md](following-2026-11.md) |
| loose `*.md` in `research/` | pages fetched by `tools/crawl.sh`, named `<host>-<utc>.md` | none |
