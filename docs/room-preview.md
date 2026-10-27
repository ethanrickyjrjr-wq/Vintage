# Room previews

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
