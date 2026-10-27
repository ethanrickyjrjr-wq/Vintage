# Room previews

## Browser editor — 2026-10-27

The current editor replaces generative placement with independent browser layers. Picks and saved favorites feed separate Decorate actions. Manual drag/drop, resize, flip, bring-forward, delete, keyboard movement, undo, reset, original comparison and labeled PNG export all work without a model service. Every position/size is numeric and remains editable; layers are never flattened into the working room. Photos are normalized locally and kept only in tab memory.

Automatic starting layouts use a lazy module worker (`site/room-segmentation.js`) with pinned Transformers.js 4.3.1 and DETR panoptic q8. The model/runtime are downloaded; the room pixels are transferred only to the local worker. The pipeline and public assets can be cached for reuse. `site/room-layout.js` remaps merged COCO labels, measures connected mask regions, checks blank wall/support space and foreground overlap, and assigns candidates deterministically. Wall art uses furniture-relative proportions and approximate spacing, with at most two artwork placements. Side tables have one available position. Lamps require side-table geometry or a broad cabinet; coffee/unknown tables are excluded. Used candidates, overlapping items and uncertain areas are rejected. Pieces that cannot fit are listed rather than parked on the floor. No inches are inferred from an assumed sofa size.

The model's masks are imperfect, so these are editable suggestions. Missing/ambiguous masks produce fewer placements. Cancellation, timeout, unavailable assets or failed model downloads preserve manual editing and the prior layout. The privacy copy discloses the roughly 45 MB model plus runtime download. Room/layout state clears on reload; favorites remain in browser storage or the catalog's session save set.

Four styling assets remain available: A1 urn lamp and A2 chandelier retain the existing editorial cutouts; A3/A4 now use perspective-correct crops of original photos, with photographed glare/occlusion retained. A5, A22, A8, A9 and A10 could not become honest whole-item layers; see [source review](room-cutout-review.md). The seven still-only room items also remain unavailable.

The storefront no longer calls `/api/room-preview`. Replace is removed, and publication sets the retained legacy service's `ROOM_PREVIEW_ENABLED=false`. Optional Klein light/shadow polish is deferred until its ten-run quality test and authenticated shop-call quota attribution are checked. The historical service notes below describe the previous release, not current editor behavior.

### Verification for this release

`npm test` passes 19 tests: seven new layout safeguards and twelve retained legacy server tests. Layout checks cover COCO remapping, missing surfaces/cutouts, coffee-table lamp exclusion, side-table capacity, deterministic/limited wall arrangements, foreground protection, and portrait/landscape bounds.

The [ten-photo browser benchmark](../research/room-editor/03-browser-benchmark.md) completed on real photos: 16.45 seconds cold including downloads, then 2.69–3.62 seconds per photo (3.26-second median) on this desktop. Captured requests were GET downloads with no photo payloads. These are desktop measurements; phone latency/peak memory and ground-truth mask accuracy have not been measured. The report includes source licences, exact revision, runtime details and observed mask errors.

## Previous service record

The storefront's `#your-room` section offers local placement sketches, automatic decorating, and replacement of an existing item selected by rectangle or description. Four cutouts stay exactly where clicked and can be kept and combined locally for free. Other inventory references can be rendered at a requested location, with the explicit limitation that AI may shift placement and details. Room previews include before/after, undo, reset and download. They are visual styling aids, not dimensional measurements or condition guarantees.

## Free rendering service

- Model: `black-forest-labs/FLUX.2-klein-4B`, Apache-2.0, four inference steps.
- Private Space: `Stanicky/Spark-X2.5-4B`, reusing its existing free ZeroGPU allocation with Ricky's approval on 2026-10-27. The video-generator Space, `Stanicky/clipboard-bench`, is unchanged.
- Original Spark branch: `spark-original-20261027`, revision `6054219a10550a6d0f90cfc26d6181fe3ab87e55`. Restore this revision to return to the old demo. The new app changes the existing Space's title and code; its repository name and private access are preserved.
- Authenticated account was checked as free (`isPro=false`, `canPay=false`). There is no paid API fallback. Free compute quotas and queues apply; this is appropriate for a pilot, not a promise of unlimited capacity.
- Runtime key names: `HF_TOKEN` (secret), `ROOM_RENDERER_URL`, `ROOM_PREVIEW_ENABLED`. The storefront calls its own Worker; the token is never sent to a shopper's browser.
- Request and result images pass as base64 JSON in memory. Neither the storefront Worker nor the renderer app saves photos to storage, galleries, datasets, or logs. D1 stores only date, salted connection hash and successful-use count. Old counters are pruned after 14 days.

## Images and demonstration

`site/assets/rooms/example-room.webp` is a generated, fictitious example room, not a customer photo. It was created with the built-in imagegen tool on 2026-10-27 from this brief: a straight-on, naturally lit living room with an oatmeal sofa, warm ivory walls, walnut tables and credenza, simple dark lamp, neutral framed artwork, white pendant and leather accent chair; generous space for vintage statements; no people or text. The uncompressed source is retained in `artifacts/room-preview/example-room-original.png` (ignored build artifact). Existing lamp/chandelier editorial cutouts and masked original artwork supply local placement sketches; no catalog originals were modified.

The loop uses actual FLUX.2 Klein room-editing outputs, labeled as AI styling previews. It is an illustrative sequence of room changes, not a screen recording or a claim of instantaneous rendering. Source frames and exports live in `artifacts/room-preview/`; the optimized video lives with the example room.

## Verification

All 12 server tests pass, exercising real SQLite quota statements, original-asset selection, placement and replacement instructions, invalid payloads, cross-origin rejection, request size bounds, connection/store limits, failure refunds, and absent-image errors. Live private-Space rendering took 3.18–6.76 seconds of measured handler time; queueing and cold starts can add time. Native-browser QA covers local uploads, sample-room loading, exact placement, multiple kept finds, undo to the original, resizing, keyboard movement, comparison, PNG export and a 375-pixel mobile layout without horizontal overflow. The published Worker successfully returned a real AI preview to the shopper UI; its asset binding, runtime secrets, D1 migration and private renderer authentication were verified together.

Sources: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B ; https://huggingface.co/docs/hub/en/spaces-zerogpu
