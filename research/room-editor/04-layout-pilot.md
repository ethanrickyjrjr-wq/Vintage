# Deterministic layout check — 2026-10-27

Ran `site/room-layout.js` against all ten sets of actual browser masks from the
[segmentation benchmark](03-browser-benchmark.md), with the four available
styling products. Asset aspect ratios use alpha-content bounds, matching the
editor, rather than an assumed product shape. Exact numeric results and
source links are in [04-layout-pilot.json](04-layout-pilot.json).

Eight rooms received at least one suggested placement; two received none.
Thirteen of forty possible product/room combinations were placed: twelve
artworks and one chandelier. Twenty-seven stayed out. No lamp was put on a
coffee/unknown table. The already furnished test rooms supplied no clear,
unoccupied confirmed lamp support under the current conservative rules.
Missing cutouts are excluded before allocation; no unplaced item is parked on
the floor. Candidate locations are hypotheses, not a count of usable room slots.

Visual review of composites retained local artifacts at
`artifacts/room-editor/layout-contact.jpg`. Suggestions can still hang too
high or overlap existing wall artwork that DETR classified as wall. The model
cannot identify every existing picture or establish real dimensions. This
supports releasing editable starting layouts marked Beta, with explicit
no-fit reporting, rather than claiming professional staging accuracy.

The seven layout tests cover empty/sparse scenes, label mapping, unknown-table
lamp exclusion, one-position side-table capacity, a two-artwork limit even
with twelve picks, deterministic output, foreground protection and bounds on
portrait/landscape photos. The legacy twelve service tests are retained but
do not validate this release's browser placement. AI polish was not run.
