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

## Hire Hollie (Fabulous From Online)

- [fabulous-from-online-design.md](fabulous-from-online-design.md): decisions, prices and occasion styling.
- [codex-handoff-fabulous-from-online.md](codex-handoff-fabulous-from-online.md): the build spec and its verification.

## Ideas and research syntheses

- [codex-handoff-idea-room.md](codex-handoff-idea-room.md): preview pages for Hollie to decide on. Section 8 specs the Round D pages for a second build.
- [round-d-synthesis.md](round-d-synthesis.md): being found, keeping people, shipping safely. [research-brief-round-d.md](research-brief-round-d.md) is the brief behind it.
- [site-ideas-and-consignment-synthesis.md](site-ideas-and-consignment-synthesis.md): ten reports on site ideas and consignment, including Florida ch. 538.

## Social and video

- [social-manual.md](social-manual.md): the social media manual. [social-manual-appendices.md](social-manual-appendices.md) holds the content banks.
- `social-manual-phone.html`: derived copy of the two files above. Edit the markdown, then run `python tools/build-phone-manual.py`.
- [codex-handoff-social-autopilot.md](codex-handoff-social-autopilot.md): the build handoff. Designed, nothing built.
- [video-direction.md](video-direction.md): what Hollie films and how she talks. `video-direction-phone.html` is its phone edition.

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
| loose `*.md` in `research/` | pages fetched by `tools/crawl.sh`, named `<host>-<utc>.md` | none |
