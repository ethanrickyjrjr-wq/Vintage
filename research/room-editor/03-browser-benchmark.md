# Browser segmentation implementation and ten-photo check

Checked live and run on 2026-10-27. This checks the segmentation stage; it does not certify the resulting staging rules, physical dimensions, or mobile performance.

## Verified integration

- Model: `Xenova/detr-resnet-50-panoptic`, revision `ea24b2d4e0bfae31f0a1299ba3fb892a2df064de`. Its q8 ONNX file is **44,483,407 bytes**. This excludes the JavaScript and WASM runtime downloads. [Live model tree](https://huggingface.co/api/models/Xenova/detr-resnet-50-panoptic/tree/main/onnx).
- Licence chain: upstream [`facebook/detr-resnet-50-panoptic`](https://huggingface.co/facebook/detr-resnet-50-panoptic) is tagged Apache-2.0 and the [DETR source licence](https://github.com/facebookresearch/detr/blob/main/LICENSE) is Apache-2.0. The Xenova conversion's card does not add an explicit licence field; it names that upstream model. This is the verified metadata, rather than a new legal opinion about dataset/weight rights.
- Library: `@huggingface/transformers` **4.3.1**, Apache-2.0, pinned rather than today's 4.3.2. [Package metadata](https://registry.npmjs.org/@huggingface/transformers/4.3.1), [official pipeline documentation](https://huggingface.co/docs/transformers.js/api/pipelines#imagesegmentationpipeline).
- Import the bundled `dist/transformers.min.js`. A real browser test found that `dist/transformers.web.js` retains bare `onnxruntime-web/webgpu` imports and cannot be imported directly from a CDN without bundling/import maps.
- `pipeline('image-segmentation', model, {dtype: 'q8', device: 'wasm'})` works in a dedicated module worker. Set `env.backends.onnx.wasm.numThreads = 1` before loading. No cross-origin isolation is required for this configuration.
- **Omit `subtask`.** In 4.3.1's actual pipeline source, an explicit subtask sets the postprocessing function variable to a string; invoking it fails. Automatic resolution binds the panoptic function correctly. [Pinned package source](https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.3.1/src/pipelines/image-segmentation.js).
- Output is an array of `{label, score, mask: RawImage}`. Each binary mask is one channel, with byte values 0 or 255. `target_sizes: [[gridHeight, 160]]` directly produces small masks while preserving photo aspect ratio.
- The preprocessor's mutable `.size` property was verified in source and by actual tensor dimensions. `segmenter.processor.image_processor.size = {shortest_edge: 512, longest_edge: 768}` produced `[1,3,512,768]` on the example room, rather than the stock `[1,3,888,1333]`. [Pinned processor source](https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.3.1/src/image_processors_utils.js).
- Final options: `threshold: .6`, `mask_threshold: .5`, `overlap_mask_area_threshold: .5`, `label_ids_to_fuse: []`. The stock overlap threshold .8 rejected many broad room surfaces in an exploratory run; reducing it improves surface availability but does not make masks reliable measurements.

## Taxonomy and staging limits

The conversion exposes several merged COCO categories as `LABEL_n`. Use the [official panoptic category definitions](https://raw.githubusercontent.com/cocodataset/panopticapi/master/panoptic_coco_categories.json): 186 ceiling, 188 cabinet, 189 table, 190 floor-other, 199 wall-other, 200 rug. Also match the named classes, including `floor-wood`, `wall-wood`, `couch`, `dining table`, `window-other`, `door-stuff`, `mirror-stuff`, `curtain`, and `tv`.

There are **no coffee-table, end-table, or console-table classes** in this model. Any such distinction comes from a separate geometric rule. A support that cannot be classified conservatively should stay empty. Do not put a lamp on a generic table merely because the detector called it a table.

A single uncalibrated image does not supply inches. The earlier report's 84-inch assumed sofa and 96-inch assumed ceiling are staging heuristics, not measurements. The editor should describe suggested proportions and allow dragging, rather than claim it has measured a six- or eight-inch gap.

## Actual browser run

The final worker ran on ten real photographs in an isolated local Chromium **148.0.7778.96**, using single-threaded ONNX Runtime Web WASM, on this Windows desktop. These were photos, including one sepia interior, a dim room, a cluttered room, and an oblique portrait view. They were not generated room fixtures. Photos were fetched from Wikimedia Commons under CC0, CC BY, or CC BY-SA licences and stayed in ignored test artifacts; none ship with the storefront.

All ten inference calls completed. The first call took **16.45 seconds**, including library/runtime/model downloads and first inference. Subsequent calls took **2.69–3.62 seconds**, with a **3.26-second median**. These are desktop observations, not a phone-speed promise.

| Photo | Time (seconds) | Source and licence |
| --- | ---: | --- |
| 1, laptop in a bright living room | 16.45, cold | [Laptop in the living room (Unsplash)](https://commons.wikimedia.org/wiki/File:Laptop_in_the_living_room_(Unsplash).jpg), CC0 |
| 2, small room with a patterned sofa | 3.46 | [Living room (15246771173)](https://commons.wikimedia.org/wiki/File:Living_room_(15246771173).jpg), CC0 |
| 3, bright room with a blue sofa | 3.21 | [Living room (Unsplash)](https://commons.wikimedia.org/wiki/File:Living_room_(Unsplash).jpg), CC0 |
| 4, furnished dining/living interior | 3.26 | [Living room (15235059612)](https://commons.wikimedia.org/wiki/File:Living_room_(15235059612).jpg), CC BY 2.0 |
| 5, sepia sitting room | 3.38 | [Living room Ireland](https://commons.wikimedia.org/wiki/File:Living_room_Ireland.jpg), CC BY 2.0 |
| 6, plants, sofa and coffee table | 3.38 | [Living room.jpg](https://commons.wikimedia.org/wiki/File:Living_room.jpg), CC BY-SA 3.0 |
| 7, portrait view from the kitchen | 3.62 | [Living room seen from the Kitchen](https://commons.wikimedia.org/wiki/File:Living_room_seen_from_the_Kitchen.jpg), CC BY-SA 4.0 |
| 8, dim room with full-height windows | 3.20 | [Simon Rae 2017-05-09 (Unsplash)](https://commons.wikimedia.org/wiki/File:Simon_Rae_2017-05-09_(Unsplash).jpg), CC0 |
| 9, wide sectional and wood ceiling | 2.69 | [Brier Living Room](https://commons.wikimedia.org/wiki/File:Brier_Living_Room.jpg), CC BY-SA 4.0 |
| 10, beach rental living room | 3.20 | [Oceanfront beach rental (26978149970)](https://commons.wikimedia.org/wiki/File:Oceanfront_beach_rental_(26978149970).jpg), CC0 |

The model emitted some wall pixels on 10/10 photos, floor/rug on 8/10, ceiling on 4/10, sofa on 5/10, table on 7/10, and cabinet on 3/10. **Those are label-presence counts, not accuracy scores.** There are no hand-labelled ground-truth masks here. Visual review found partial surfaces, wall pixels on a ceiling/foreground in the oblique room, missing visible furniture, and false `car` detections among the cluttered room's objects. Missing or fragmented masks must produce fewer slots, not an invented fallback arrangement.

Browser network observation recorded 31 requests, all GET, with zero request bodies. External hosts were `cdn.jsdelivr.net`, `huggingface.co`, and `us.aws.cdn.hf.co`; local fixture images came from loopback. No room pixels were uploaded. The library performs an optional missing-tokenizer lookup that returns 404; image segmentation still succeeds. The pipeline remains in worker memory for reuse, with browser caching for downloaded public assets. Peak resident memory and low-memory phone behavior were not measured.

## Evidence and remaining checks

- Committed [`03-browser-benchmark.json`](03-browser-benchmark.json) records source titles, attribution/licences, precise timings, emitted labels, scores, and mask pixel counts without embedding photos or expiring signed CDN URLs.
- Full 160-pixel mask arrays, local fixture photos, browser runner, and screenshots are in ignored `artifacts/room-editor/benchmark/`. `browser-results.json` is the input for the owner's actual `arrangeRoom` placement checks. `browser-masks-contact.jpg` is the visually inspected segmentation contact sheet. These files are local test evidence, not deployment assets.
- A separate native Node CPU run completed all ten in 0.80–1.12 seconds; its labels differed slightly from the browser backend. Browser timings and browser masks above are the relevant release evidence.
- This run verifies model loading, browser inference, small-mask transfer, and request privacy for the worker. The owner must still test staging/slot allocation, no-fit reporting, drag/resize/flip/delete, cancellation, and the final editor's mobile layout. AI lighting/shadow polish and its quota are outside this run.
