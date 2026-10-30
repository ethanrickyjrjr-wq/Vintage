# Room previews

## Separate room page and phone directions (2026-10-29)

Live publicly as **Sites version 36** at
https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site/room.html .
The release includes the lighter homepage and separate Room/Hire Hollie pages
(`e0ba6f2`), collapsed phone directions (`db03e13`), and the concurrent removal
of the completed homepage idea preview. Sites source is
`9dbc12c89d0d4a3131e3dbe54f2ac136bbdf4bd2`; deployment
`appgdep_6ae36012168c819182470deaf2102f16` succeeded with environment revision 2.
The matching concurrent publication was reused rather than deployed twice.

All 42 tests and the production build passed for that Sites source. Live Chrome
at 390px confirmed the directions start closed, expand and collapse, and keep
the picks close to the photo. The sample-room chandelier can be added and
placed with its resize handle; no console errors appeared. The menu opens,
there is no horizontal overflow, and the homepage's three doors stack in one
column. At 1440px the directions start open. These are browser viewport checks;
finger dragging still needs a real-phone check. The existing roughly 116px
sticky phone header remains unchanged.

## Sample-room placement repair — 2026-10-28

The Gold Egyptian bust lamp (A13) reproduced a zero-placement result in our own
sample photograph: the detector did not provide a usable confirmed support.
The earlier ten-room pilot had placed no lamps, so its passing checks did not
establish that this basic sample-room flow worked.

`site/room-sample.js` now supplies reviewed placement bounds for the fixed
1536 × 1024 sample photograph. The lamp goes on the empty left end of the
credenza, clear of the existing vase; coffee-table objects, wall pieces,
ceiling lighting and a foreground floor position have separate bounds.
The sample skips the model download/inference entirely. Uploaded photographs
still use the local model and cannot inherit the sample's placement map.
Both paths use the same size, capacity, overlap and editability checks.

A zero-placement result now preserves existing layers and reports the specific
reason for a single rejected find. Successful suggestions remain undoable.
The automated regressions pin the sample image hash, check the reported lamp
using its actual cutout proportions, cover all four table lamps individually,
enforce support capacity and verify a bounded, separated mixed arrangement.

Verified with all 26 automated tests and a production build. Chrome checks
covered the exact A13 sample-room flow, Favorites, Remove/Undo, switching to an
uploaded photo, preservation of a manually placed lamp after real inference
returned no position, and switching back to the sample. The published flow
also reports **1 find placed**, visibly on the cabinet.

Published as Sites **version 25**, deployment
`appgdep_6ae2be6123e08191bc600ac81427de43` (succeeded), at
https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site . GitHub repair:
`2fa1abd`; Sites source: `f6b54aac61b357936305fc774343249d677dc190`.
Local screenshot: `artifacts/qa/room-lamp-fixed-live.png`.

## Room disco publication — 2026-10-28

Sites **version 22** is live publicly at https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site .
Implementation commit: `ef4f9b3`; Sites source commit: `085a690c3c18a7f76010dbcd74cf9084f5302132`;
deployment `appgdep_6ae2628c26d88191bbad86c9ba941a30` succeeded. Build and all 23 tests pass.
Live Chrome acceptance line 11 passes on desktop and at 390 px: placement reveals the ball,
clicking starts advancing audio, spinning and photo-clipped lights; Clear stops playback and hides
the ball; Undo restores it silently. The entrance ball retains page-wide lights and toggles off.
At 390 px the ball measures 56 px and the page has no horizontal overflow.
Detailed verification is recorded in [the navigation handoff](codex-handoff-navigation.md#published).

## Browser editor — 2026-10-27

The current editor replaces generative placement with independent browser layers. Picks and saved favorites feed separate Decorate actions. Manual drag/drop, resize, flip, bring-forward, delete, keyboard movement, undo, reset, original comparison and labeled PNG export all work without a model service. Every position/size is numeric and remains editable; layers are never flattened into the working room. Photos are normalized locally and kept only in tab memory.

Automatic starting layouts use a lazy module worker (`site/room-segmentation.js`) with pinned Transformers.js 4.3.1 and DETR panoptic q8. The model/runtime are downloaded; the room pixels are transferred only to the local worker. The pipeline and public assets can be cached for reuse. `site/room-layout.js` remaps merged COCO labels, measures connected mask regions, checks blank wall/support space and foreground overlap, and assigns candidates deterministically. Wall art uses furniture-relative proportions and approximate spacing, with at most two artwork placements. Side tables have one available position. Lamps require side-table geometry or a broad cabinet; coffee/unknown tables are excluded. Used candidates, overlapping items and uncertain areas are rejected. Pieces that cannot fit are listed rather than parked on the floor. No inches are inferred from an assumed sofa size.

The model's masks are imperfect, so these are editable suggestions. Missing/ambiguous masks produce fewer placements. Cancellation, timeout, unavailable assets or failed model downloads preserve manual editing and the prior layout. The privacy copy discloses the roughly 45 MB model plus runtime download. Room/layout state clears on reload; favorites remain in browser storage or the catalog's session save set.

Four styling assets remain available: A1 urn lamp and A2 chandelier retain the existing editorial cutouts; A3/A4 now use perspective-correct crops of original photos, with photographed glare/occlusion retained. A5, A22, A8, A9 and A10 could not become honest whole-item layers; see [source review](room-cutout-review.md). The seven still-only room items also remain unavailable.

The storefront no longer calls `/api/room-preview`. Replace is removed, and publication sets the retained legacy service's `ROOM_PREVIEW_ENABLED=false`. Optional Klein light/shadow polish is deferred until its ten-run quality test and authenticated shop-call quota attribution are checked. The historical service notes below describe the previous release, not current editor behavior.

### Verification for this release

`npm test` passes 19 tests: seven new layout safeguards and twelve retained legacy server tests. Layout checks cover COCO remapping, missing surfaces/cutouts, coffee-table lamp exclusion, side-table capacity, deterministic/limited wall arrangements, foreground protection, and portrait/landscape bounds.

The [ten-photo browser benchmark](../research/room-editor/03-browser-benchmark.md) completed on real photos: 16.45 seconds cold including downloads, then 2.69–3.62 seconds per photo (3.26-second median) on this desktop. Captured requests were GET downloads with no photo payloads. These are desktop measurements; phone latency/peak memory and ground-truth mask accuracy have not been measured. The report includes source licences, exact revision, runtime details and observed mask errors.

Native-browser QA verified a real local room upload, multiple editable layers, canvas dragging and corner resizing, flip, keyboard movement/delete, undo, original comparison, a labeled PNG without handles, separate favorites/picks inputs, model cancellation, unavailable-item explanations, and a 375-pixel viewport without horizontal overflow. A real-room UI run placed both paintings and left the dress form out. The [layout pilot](../research/room-editor/04-layout-pilot.md) records all ten placement results and observed shortcomings.

Published through Sites as **version 15** on 2026-10-27 at https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site . Audience remains public. GitHub implementation commit: `2dc9e20`; Sites source commit: `2540be20ab64b4791b5c94b001bd8d964b9334f6`; deployment: `appgdep_6ae10e8488948191ad18cc992a828028`, succeeded with environment revision 2. The published API reports `available:false`, confirming the old Klein placement endpoint is disabled. A live-origin sample upload and artwork layer also passed. The first v13 live asset load failed, then v14 completed download and inference on the same Chrome surface. Version 15 adds one fresh-worker retry for library/network download failures, retaining cancellation and manual fallback; it does not retry inference errors. No hosting-policy or runtime-cache changes were necessary.

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

## Real-size placement in the sample room (2026-10-29)

Each sample find carries `cm`, an illustrative real-world size of its longest side, in `site/demo-products.js`. These are estimates, like the sample prices. Each reviewed slot in `site/room-sample.js` carries `ppm`, the fraction of the photo width one metre spans at that depth, calibrated on objects already in the photo (throw pillows, vase, credenza, sofa, coffee table).

A find is drawn at `cm × ppm`, capped to its slot and never enlarged. If the slot can hold less than 70% of real size, the find is left out as "Too big for the open space in this room" (the three sofas, because the sample already has one). Uploaded rooms have no scale reference, so they keep fitting finds to the slot. Deriving a scale from a detected sofa is the next step there.

The `.1` width floor on the Egyptian-lamp test still guards the fit-to-slot path. At real size that lamp is about `.088` wide, the same scale as the lamp already in the photo.

Rugs and hides are their own `rug` kind. They lie flat: `flat.rug` foreshortens the layer's stored `ratio`, so drawing, dragging, resizing and hit-testing need no special case. They go in the open foreground band below the coffee table's feet, draw underneath everything else, and may be shown down to 50% of real size (furniture: 70%, otherwise "Too big for the open space in this room"). Uploaded rooms place a rug inside the detected floor.

## Decision: move the room tool to generative redesign (2026-10-30)

Ricky's call: a room tool should redesign the whole room (several chairs, a rug, lamps, cushions) from the photo in seconds, as established apps do. Browser stickers on fixed spots cannot do that, so they become the free fallback, not the product.

Verified from live vendor docs on 2026-10-30 (raw pages in `research/ai.google.dev_gemini_api_docs_*`, `research/vercel.com_docs_ai_gateway_*`):

- Model `gemini-nano-banana-2.1` (also `gemini-3.1-flash-image`, `gemini-3-pro-image`, `gemini-2.5-flash-image`). Up to 10 high-fidelity object reference images per call on Nano Banana 2.1 and 3.1 Flash Image (Pro: 6 objects, 14 total).
- Price per output image, paid tier: about $0.034 at 1K, $0.050 at 2K, plus input tokens. The free tier has **no access** to these image models, and free-tier data is used to improve Google's products; paid-tier data is not. Customer room photos must therefore only go through a paid key.
- Request shape: `POST https://generativelanguage.googleapis.com/v1beta/interactions`, header `x-goog-api-key`, body `{model, input: [{type: "text", text}, {type: "image", mime_type, data(base64)}, ...], response_format: {type: "image", aspect_ratio, image_size}}`. The SDK returns the image as `interaction.output_image.data` (base64). The raw REST response shape is not yet observed.
- Vercel AI Gateway also exposes `google/gemini-3-pro-image`, `google/gemini-3.1-flash-image-preview`, `openai/gpt-image-2`, `bfl/flux-2-pro` through the AI SDK (`generateText`, images in `result.files`); useful for a quality comparison with one key.

Not yet verified: output quality on our products. A test (sample room plus three chairs, a rug, a lamp, two cushions and a mirror as references in one call) is scripted but could not run: the key store's `GEMINI_API_KEY` is free-tier (limit 0 for these models), `GEMINI_API_KEY_2` has depleted prepaid credits (HTTP 402), `AI_GATEWAY_API_KEY` is rejected (HTTP 401), and `HF_TOKEN` is absent. The previous generative pilot (FLUX.2 Klein 4B on a free ZeroGPU Space, one product per call) stays disabled.
