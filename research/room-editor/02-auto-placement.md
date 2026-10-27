# 02 - Deterministic auto-placement for "Decorate for me" (no generative model chooses)
Researched 2026-10-27. Raw pages and API dumps: `research/room-editor/raw/`. Tags: **V** = verified in-session (URL given), **U** = unverified.

## Bottom line
- Segment the photo **in the shopper's browser** (Web Worker, transformers.js), turn masks into slots with plain geometry, assign items with a greedy rule table. Nothing generative decides.
- **Licence trap:** the obvious ADE20K model, SegFormer (incl. `Xenova/segformer-b0-finetuned-ade-512-512`), is research/evaluation-only. It cannot sit behind a shop. The only permissive, browser-ready model I found with wall / floor / ceiling / couch / table classes is `Xenova/detr-resnet-50-panoptic` (44.5 MB q8).
- Depth Anything, Florence-2, OWLv2, Grounding DINO, Qwen-VL: not needed for v1 (section 3, 4).

## 1. Segmentation models and licences
Source: https://github.com/NVlabs/SegFormer/blob/master/LICENSE , https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512 , https://github.com/facebookresearch/MaskFormer/blob/main/LICENSE , https://github.com/facebookresearch/Mask2Former/blob/main/LICENSE , https://github.com/SHI-Labs/OneFormer/blob/main/LICENSE , https://github.com/facebookresearch/detr/blob/main/LICENSE
- **SegFormer b0..b5 (ADE20K)** V: HF tag `other`, points to "NVIDIA Source Code License for SegFormer": section 3.3 "may be used or intended for use non-commercially ... for research or evaluation purposes only". The Xenova / onnx-community ONNX copies show blank tags but are the same weights; treat as the same licence (legal reading U).
- **MaskFormer** V: repo is CC BY-NC 4.0. `facebook/maskformer-swin-tiny-ade` tag `other`; `onnx-community/maskformer-swin-tiny-ade` (48 MB int8) tag blank. Treat as non-commercial.
- **Mask2Former** V: repo MIT. HF checkpoint `facebook/mask2former-swin-tiny-ade-semantic` says "License: other" with no text: **repo MIT verified, checkpoint tag needs review.** Not in the transformers.js supported-model list (grep of docs index), so server-only.
- **OneFormer ADE20K swin-tiny** V: repo MIT, HF tag `mit`, 203 MB `pytorch_model.bin`, not in transformers.js list. **UperNet-ConvNeXt-tiny** V: `openmmlab/upernet-convnext-tiny` MIT, 60.3M params, 241 MB. Best licence-clean ADE20K options, server-side only.
- **DETR R50 panoptic (COCO)** V: Apache-2.0 (HF API tag for `facebook/detr-resnet-50-panoptic`, repo "Apache License 2.0"). Xenova ONNX copy has no licence tag; upstream is Apache.
- **ADE20K label set** V (nvidia config.json, 150 classes): wall 0, floor 3, ceiling 5, table 15, coffee table 64, chest of drawers 44, cabinet 10, buffet 99 (= sideboard), desk 33, counter 45, bookcase 62, shelf 24, sofa 23, chair 19, armchair 30, rug 28, painting 22, lamp 36, plant 17, mirror 27, vase 135, tray 137, fireplace 49, ottoman 97, chandelier 85, sconce 134. No "console table". Same 150 set for OneFormer is assumed (U).
- **Dataset terms** V (https://ade20k.csail.mit.edu/terms/ , https://cocodataset.org/dataset/termsofuse.htm): ADE20K images = non-commercial research/education only, annotations BSD-3. COCO annotations = CC BY 4.0, images = Flickr terms. Whether weights inherit dataset terms is a legal call (U); COCO is the cleaner chain.
- Indoor accuracy of any of these: no benchmark fetched (U). Needs a 10-photo test on real shopper-style rooms.

## 2. In the browser (transformers.js)
Source: https://huggingface.co/docs/transformers.js/index , .../installation , .../guides/webgpu , .../api/pipelines , https://registry.npmjs.org/@huggingface/transformers , https://huggingface.co/api/models/Xenova/detr-resnet-50-panoptic/tree/main
- Library V: Apache-2.0, npm `latest` = 4.3.2 (published 2026-10-27), 4.3.1 on 2026-10-06. Docs install page shows `import { pipeline } from 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.3.2'`. The WebGPU guide banner still calls v3.8.1 the latest stable: **npm verified, docs banner needs review.** Pin 4.3.1 (3 weeks old), not 4.3.2 (published today).
- Runs on WASM CPU by default; `device: 'webgpu'` opt-in; docs put WebGPU support at ~85% (Mar 2026). "No need for a server" (docs index). Model files download from the Hub once; the photo is never uploaded.
- The `image-segmentation` docs example is literally `pipeline('image-segmentation','Xenova/detr-resnet-50-panoptic')` returning `[{label, score, mask: RawImage}]`. Options include `threshold`, `mask_threshold`, `subtask`.
- ONNX sizes V (HF tree API): DETR panoptic fp32 172.3 / fp16 86.6 / **q8 44.5 MB**. SegFormer b0 q8 4.4, b2 q8 28.9 (licence-blocked). Depth-Anything-V2-small q8 27.3.
- Latency U (not run). Stock preprocessor resizes to **shortest edge 800** (V, preprocessor_config.json), the main cost on WASM; test overriding it, show a progress bar, load once per session.
- **Label gotcha V:** `Xenova/detr-resnet-50-panoptic` config names ids 184+ as `LABEL_n`, but the merged stuff classes are exactly those. Per https://raw.githubusercontent.com/cocodataset/panopticapi/master/panoptic_coco_categories.json : 186 ceiling-merged, 188 cabinet-merged, 189 table-merged, 190 floor-other-merged, 199 wall-other-merged, 200 rug-merged; also 118 floor-wood, 63 couch, 62 chair, 64 potted plant, 67 dining table, 156 shelf, 107 counter, 181 window-other, 112 door-stuff, 133 mirror-stuff, 72 tv, 92 banner, 109 curtain. Ship a hand-written id map; match unmerged names too (173 wall-other) in case.

## 3. Comparison
| Approach | Model | Licence | Runs | Download / latency | Gives us | Verdict |
|---|---|---|---|---|---|---|
| ADE20K semantic | SegFormer b0..b5 | NVIDIA, non-commercial V | browser | 4.4-29 MB q8 / U | 150 classes, masks | **No (licence)** |
| ADE20K semantic | MaskFormer swin-tiny | CC BY-NC V | browser | 48 MB / U | masks | No (licence) |
| ADE20K semantic | Mask2Former swin-tiny | repo MIT V, ckpt "other" | server | n/a | masks | Needs review; no web build |
| ADE20K semantic | OneFormer swin-tiny / UperNet-CNX-t | MIT V | ZeroGPU / CPU Space | 203 / 241 MB; ZeroGPU Gradio-only, free acct 5 min/day, anon 2 min/day V | best class set (coffee table, buffet) | Fallback tier; photo leaves device |
| COCO panoptic | DETR R50 panoptic | Apache-2.0 V | browser | 44.5 MB q8 / U | wall, floor, ceiling, couch, chair, plant, table, cabinet, shelf, rug, mirror, tv, window, door masks | **Recommended v1** |
| Phrase grounding | Florence-2 base-ft (`onnx-community`) | MIT V, 0.23B | browser | ~275 MB (sum of q8 vision+encoder+decoder+embed) / slow autoregressive U | boxes for phrases, no masks | Later, optional |
| Open-vocab detect | Grounding DINO tiny ONNX | Apache-2.0 V, 172M | browser | 203.8 MB q8 | boxes | No (heavy, boxes only) |
| Open-vocab detect | OWLv2 base-ensemble | Apache-2.0 V, 155M | browser | 155 MB q8 | boxes | No (heavy, boxes only) |
| VLM grounding | Qwen2.5-VL-3B | Qwen Research V (LICENSE: "Non-Commercial" = "research or evaluation purposes only"; commercial use must request a licence) | server | n/a | JSON boxes | **No (licence)** |
| VLM grounding | Qwen2.5-VL-7B / Qwen3-VL-2B,4B | Apache-2.0 V | ZeroGPU only | 8.3B / 2.1B / 4.4B | boxes, non-deterministic | No (it is "ask a model to choose" again) |
| Text-prompt seg | SAM 3 | gated, licence "other" V, 860M | server | n/a | masks for phrases | No (gated) |
| Depth | Depth-Anything-V2-small | Apache-2.0 V (Base/Large CC-BY-NC V) | browser | 27.3 MB q8 | **relative** depth | Skip v1 (section 4) |
Sources: https://huggingface.co/microsoft/Florence-2-base , https://huggingface.co/onnx-community/Florence-2-base-ft , https://huggingface.co/google/owlv2-base-patch16-ensemble , https://huggingface.co/IDEA-Research/grounding-dino-tiny , https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct (+ /raw/main/LICENSE), https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct , https://huggingface.co/docs/hub/spaces-zerogpu , https://huggingface.co/api/models/facebook/sam3
Florence-2 supports `<CAPTION_TO_PHRASE_GROUNDING>`, `<OD>`, `<REGION_PROPOSAL>` (V, model card); whether it localises "sideboard" reliably is U. Open-vocab boxes cannot give floor/wall/ceiling extents anyway, so segmentation stays the base layer.

## 4. Scale and perspective: is depth worth it?
Source: https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf , https://github.com/DepthAnything/Depth-Anything-V2 , .../tree/main/metric_depth , https://www.houzz.com/magazine/key-measurements-for-your-living-room-stsetivw-vs~25889785
- DA-V2 small is tagged **relative depth** V, Apache-2.0 V (README: Small Apache-2.0, Base/Large/Giant CC-BY-NC-4.0). Relative depth gives no inches. The metric-indoor small (`Depth-Anything-V2-Metric-Indoor-Small-hf`, tagged "absolute depth", Hypersim, max 20 m) has **no licence on its card (U)**; the README licence line covers the relative models.
- Not worth it for v1: every stager rule below is a ratio to the furniture the item sits on or hangs over, so no metres are needed. Anchor px-per-inch on the **sofa mask: width_px / 84 in** (Houzz average sofa 84 x 38 in, range 72-96 V). Wall art and side/coffee-table items share roughly that depth plane. Fallback anchor: wall height floor-to-ceiling = 96 in (The Spruce's chandelier rule assumes an 8-ft ceiling V; not universal U). For floor items far from the sofa, scale by floor-mask y between the sofa row and the bottom edge (heuristic, U).
- Upgrade path only if real item sizes arrive and tests show wrong scale: add DA-V2-small and read depth at the slot; check the metric licence first.

## 5. Stager rules (numbers and sources)
| Rule | Number | Source (all V) |
|---|---|---|
| Art centre height | 57 in from floor (60 if tall ceilings / tall household); hang lower where people sit | https://www.thespruce.com/tips-for-perfectly-placed-art-1976086 ; https://www.architecturaldigest.com/story/how-to-hang-picture |
| Art above sofa / console / sideboard | frame bottom 6-8 in above sideboard/console, a little more above a sofa (AD); 6-12 in above sofa back or tabletop, centred (Spruce); "one hand width" (BHG) | AD and Spruce above ; https://www.bhg.com/decorating/home-accessories/wall-art/how-to-arrange-art/ |
| Art width vs furniture | at least 2/3 of the sofa or sideboard width (9 ft sofa -> 6 ft art) | BHG above ; Spruce 57-inch article FAQ ("2/3 rule") |
| Table lamp | ~30 in tall, top of lamp 58-64 in from floor, width no more than half the table width | https://www.alicelaneinteriordesign.com/blog/rules-of-scale-table-lamps |
| Where lamps live | sofa/console tables 14-20 in deep x 60-72 in long "great for placing lamps upon"; end tables 20-30 in square | https://www.houzz.com/magazine/key-measurements-for-your-living-room-stsetivw-vs~25889785 |
| Coffee table decor | rule of thirds, 3 objects (5 on big tables, odd numbers), vary heights | https://www.thespruce.com/ways-to-style-a-coffee-table-11725514 |
| Coffee table formula | one tray + a book stack + one organic element + 1-2 decor; the only lamp mentioned is a *mini cordless lamp* | https://www.housebeautiful.com/room-decorating/a71352748/coffee-table-designer-styling-advice/ |
| Tray size / position | no bigger than ~half the tabletop, pushed to one side, keep a clear area for drinks | https://www.apartmenttherapy.com/practical-coffee-table-design-ideas-267151 |
| Console / sideboard top | one central piece, or three objects at one end in varying heights, pyramid (1 tall + 2 low); keep styling to one side for asymmetry; tall plant beside it; art leaned or hung a few inches above | https://www.thespruce.com/how-to-style-a-console-table-with-functional-decor-11731584 ; https://www.thespruce.com/sideboard-decor-ideas-7096349 |
| Chandelier | diameter 1/2 to 2/3 of table width (or table minus 12 in); bottom 30-36 in above table at 8-ft ceiling, +3 in per extra foot | https://www.thespruce.com/how-to-hang-a-dining-room-chandelier-1976284 |
| Walkways / seating | circulation paths 30-36 in clear; coffee table 12-20 in from seating; accent chair 36-40 w x 40-44 d in | Houzz article above |
| Floor plants | tall plant in the dead corner beside the sofa or a window; group in odd numbers | https://www.thespruce.com/how-to-arrange-plants-in-a-living-room-11833913 |
| Balance | in a group keep heavy pieces low and left (eye starts left) | BHG above |
Not found in credible sources (judgement, mark in code): dress-form placement, pair-of-hurricane-lamps spacing, "never a lamp in the middle of a coffee table" (derived: Alice Lane's 58-64 in lamp top cannot work on a ~16 in table; House Beautiful only allows a mini lamp).

## 6. Recommended pipeline
1. **Load** (Web Worker, module): transformers.js 4.3.1 from jsDelivr, `pipeline('image-segmentation','Xenova/detr-resnet-50-panoptic',{dtype:'q8', device: navigator.gpu ? 'webgpu' : 'wasm'})`. Lazy-load on first click, cache, show progress. Photo stays on device.
2. **Segment** the (EXIF-corrected) photo. Remap `LABEL_n` ids. Group: WALL (199,173,wall-*), FLOOR (190,118,floor-*) + RUG (200), CEIL 186, SOFA 63, CHAIR 62/15, TABLE 189+67, CAB 188/156/107, PLANT 64, NOGO = window 181, door 112, mirror 133/66, tv 72, banner 92, curtain 109, clock 85, bed 65.
3. **Reduce** each mask to a 160-px-wide grid; per group keep connected blobs with bbox, area, top-edge y per column. Compute px/in from the sofa (84 in); fallback wall height (96 in); fallback "no scale": use fractions below. Wall free-space = WALL minus NOGO minus furniture bboxes.
4. **Classify tables geometrically** (COCO has no coffee/side/console class): TABLE/CAB blob overlapping the sofa's x-range and below its centre = **coffee**; small blob (< 0.5 sofa width) beside the sofa/chair at arm height = **side**; wide TABLE/CAB blob with WALL pixels directly above its top edge = **console/sideboard**; else TABLE alone = **other table** (treat as console).
5. **Build slots** (normalised 0-1 boxes): see table below.
6. **Assign greedily, deterministic**: order items chandelier, wall art (largest first), lamps, floor pieces, small decor. For each item score every legal slot = rule fit (preferred 1.0, acceptable 0.5, forbidden = skip) - overlap with placed boxes / NOGO (reject > 10% IoU) + balance term (put the next heavy item on the lighter side of the sofa centre-line) ; ties by x then y. Fill capacity (3 per console/coffee, 1 lamp per side table, shrink-to-fit never below 70%). No match -> park the item in the bottom-centre floor and flag "drag me". Same photo + same cart = same layout; a "Shuffle" button can rotate to the 2nd-best layout.
7. **Output** per item `{id, cx, cy, w}` as photo fractions + z-order; the existing drag UI just edits those numbers. Add a `kind` field to `room-products.js` because `surface:"table"` hides lamp vs decor (inventory: A1/A13/A17 lamps, A14/A8/A10 decor, A16/A9 low media, A19 throw/rug).

**Slots and defaults** (width = share of the support's width unless real size known: `w_px = item_in x px_per_in`):
| Item kind (ids) | Slot (preferred, then acceptable) | Default size | Position rule |
|---|---|---|---|
| Wall art (A3, A4, A5) | WALL above sofa > above console > free wall at 57 in centre | grouped art = 2/3 of furniture width, single piece >= 1/2 | bottom 8 in above sofa top (6 for console), centred; skip NOGO; heavy left |
| Chandelier (A2) | CEIL centre over coffee/dining table > CEIL centroid | 1/2 to 2/3 of dining table width, else <= 1/5 photo width | hangs from ceiling mask; bottom >= 30 in above any table |
| Table lamp (A1, A13) | side table > console end > (none on coffee table) | <= 1/2 of support width; ~30 in tall | centred on side table; at 1/6 or 5/6 of console |
| Pair of lamps (A17) | both ends of console > two side tables | each <= 1/4 console width | mirrored about console centre |
| Small decor (A14, A8, A10) | console (thirds, pyramid) > coffee table (tray rule) | each <= 1/4 support width; coffee set <= 1/3 of top | off-centre, odd count, vary height |
| Low media (A16, A9) | console / sideboard > other table | <= 1/3 support width | one end, opposite the lamp |
| Armchair / sculptural chair (A15, A20) | FLOOR beside the sofa end or in the open corner | 36-40 in wide = 0.45 x sofa width | keep >= 30 in clear to sofa front and walls; angle ignored |
| Dress form (A22) | FLOOR corner next to window/door, away from walkway | ~0.2 x sofa width wide, ~1.3 x sofa height tall (judgement U) | against wall line, not in front of NOGO |
| Throw / rug (A19) | SOFA mask draped over arm > RUG/FLOOR centre under coffee table | 0.4 x sofa width | pinned to sofa mask top-left |
Missing slot types fall back in order: console -> other table -> floor; no sofa -> use the largest TABLE/CAB blob as the anchor.

## 7. What I could not verify
- Real latency and memory of DETR-R50-panoptic q8 on WASM and WebGPU (not run; instructed not to); whether transformers.js lets you override the 800 px resize.
- Indoor-room segmentation quality of any model; that the model emits ids 186/190/199 (merged) rather than 173/118-style unmerged ids (derived from the training category file, not observed).
- Legal effect of ADE20K / COCO dataset terms on trained weights; Mask2Former HF checkpoint licence ("other"); metric-indoor Depth Anything licence; SAM 3 terms.
- Whether Gradio/ZeroGPU temporary upload caching would breach "photos never stored" (if the server tier is ever used). ZeroGPU quota counts per visitor account (V: free 5 min/day, anon 2 min/day); how it behaves for anonymous shop traffic is U.
- Florence-2 grounding quality on "sideboard / side table"; OneFormer / UperNet speed on a free CPU Space.
- Credible sources for dress-form and vintage-lamp-pair placement (none found).
