# Lane 19-bench: rembg models measured on Ricky's photos

Status: date 2026-11-07. Fetched nothing; no web needed. Every number and judgement below is MEASURED_HERE: three rembg models run on CPU in this sandbox (4 cores, 15 GB, no GPU), one process at a time, through scratch copies of tools/cutout/cutout.py with only the MODEL constant changed (scratch copies and outputs under the session scratchpad, `bench/`). The repo script was not edited. Contact sheets (original, general, lite, isnet, each cut shown on white) are in test-results/bench-<photo>.jpg and I looked at every one with the Read tool.

Caveats. (1) Seconds are per photo after the model was loaded (the script starts its timer after new_session), on this 4-core sandbox, not on Ricky's i7-14700KF, so absolute times will differ; the ratios are the useful part. (2) The dress and print photos are 1512x2016 and 1932x2576, the room photos 1050x1400 (previews in assets/photos, not the Drive originals). (3) The first batch pass lost the report line for IMG_6617 with birefnet-general (no output, cause unknown, probably my grep filter or a crash); a single rerun gave the line below. (4) The cutout script auto-applies rect repair to any filename containing "print", so my first "shisa-print" runs were all rect runs. I made a true no-rect run on a copy named shisa-p.jpg. The sheet shows no-rect on the top row and rect on the bottom.

## Results table

Pixels kept is the script's share of solid item pixels identical to the photo. Solid is the share of kept item that is fully opaque (low means see-through or washed out).

| photo | model | seconds | pixels kept | solid | verdict |
|---|---|---|---|---|---|
| dress front | general | 18.2 | 99.9% | 98% | Clean. Hanger hook kept, tag and Neiman Marcus label readable, no halo. |
| dress front | lite | 11.5 | 99.9% | 98% | Practically identical to general. |
| dress front | isnet | 3.3 | 99.9% | 92% | Dress ok but car door handle and window outline survive as faint grey ghost lines left of and below the skirt, and the whole hanger wire is kept. Needs cleanup. |
| dress back | general | 18.4 | 99.9% | 98% | Clean; hook kept, thin wire stub above it. |
| dress back | lite | 11.4 | 99.9% | 98% | Clean; hook cut off flat, slightly tighter crop. |
| dress back | isnet | 3.2 | 99.9% | 92% | Dress ok, faint smudges at sleeve edges and shoulder. |
| label close-up | general | 17.3 | 99.8% | 97% | Cut, but legible: woven text sharp. It keeps the tag string. |
| label close-up | lite | 10.4 | 99.8% | 97% | Same as general. |
| label close-up | isnet | 2.9 | 97.7% | 6% | Failed. Label washed out to near white, "100% SILK" gone. Unusable. |
| framed print, no rect | general | 22.2 | 100.0% | 92% | Whole frame found, but top edge dips and a white smear eats the glare patch on the mat at right. |
| framed print, no rect | lite | 13.5 | 100.0% | 92% | Worse: top and left frame bar partly missing, mat top-left whited out, right frame bar detached. |
| framed print, no rect | isnet | 2.8 | 94.2% | 65% | Failed: frame and mat gone, only the red print art kept. |
| framed print, --rect | general | 22.8 | 100.0% | 93% | Best of all nine print cuts: full frame, mat and print intact, rect repair filled 3.1% of the hull. Tiny nicks in the top edge and one small white speck on the mat at right. |
| framed print, --rect | lite | 16.1 | 100.0% | 96% | Frame complete, but rect repair had to fill 26.0% of the hull and left a ragged white scar on the mat top-left. |
| framed print, --rect | isnet | 3.4 | 96.3% | 79% | Frame still missing; hull around the art only. Failed. |
| room 6607 (mannequins) | general | 16.6 | 100.0% | 97% | Good: both mannequins, chain, jacket, shorts, hanger. Some wall left in gaps is removed cleanly. |
| room 6607 | lite | 10.4 | 99.9% | 96% | Close to general, keeps a bit more stray fringe at left. |
| room 6607 | isnet | 2.0 | 99.3% | 9% | Jacket and leggings washed out and see-through. Failed. |
| room 6610 (shelf, rack) | general | 17.5 | 99.8% | 96% | Keeps the brass shelf, glasses, jewellery, rack and the ceiling chain; whites out the neon sign and part of the chair. |
| room 6610 | lite | 10.2 | 99.7% | 83% | Shelf contents partly erased (upper shelf, bottom shelf), floating chunks, neon kept but rest damaged. |
| room 6610 | isnet | 3.1 | 98.5% | 39% | Shelf contents ghosted. Failed. |
| room 6612 (belts on chair) | general | 16.8 | 99.9% | 97% | Good item cut, but the whole black chair back is kept (it is the same black leather, hard to separate). |
| room 6612 | lite | 10.1 | 99.9% | 95% | Chair seat kept as a blob, ragged denim edge. Worse than general. |
| room 6612 | isnet | 4.3 | 99.5% | 37% | Chair half-erased, item ghosted. Failed. |
| room 6617 (selfie in mirror) | general | 16.1 | 99.8% | 95% | Clean cut of the person only. (Script note "item small in frame" is just the padding.) |
| room 6617 | lite | 12.2 | 99.9% | 98% | Keeps the person and the big pink coat next to her, plus a stray fragment. Different subject choice. |
| room 6617 | isnet | 3.5 | 99.8% | 38% | Head and torso mostly erased. Failed. |
| room 6619 (magazines on rug) | general | 24.5 | 99.8% | 99% | Good: all magazines, rug gone. Edges clean; a bit of a purple magazine lost near the top. |
| room 6619 | lite | 9.7 | 99.8% | 97% | Also good; keeps about the same magazines, slightly rougher edge at left and bottom. |
| room 6619 | isnet | 1.9 | 0.0% | 0% | Failed: nearly nothing kept. |

## What I see, model by model

birefnet-general (default). Never failed. On both dress shots the cut is complete with the hanger hook kept and a fine wire stub, no halo against white, collar, cuffs, pink button and tag intact. The Neiman Marcus label stays legible in the cut. On the framed print without rect it found the whole frame but left a dip and a glare smear; with --rect the frame, mat and art are complete. Cost: about 16 to 25 s each here.

birefnet-general-lite. About 35 to 40 percent faster (10 to 13 s against 16 to 25 s). On clean subjects on a plain-ish background (dress front, dress back, label, mannequins, magazines) it is visually the same as general. It breaks on thin, low-contrast structures: on the print it lost parts of the black frame (rect repair then filled a quarter of the hull) and on the glass shelf the upper and lower shelves were partly erased. Pick it only as a speed fallback on garments.

isnet-general-use. Fast (2 to 4 s) but not usable here. It kept the whole hanger wire and ghost lines of the background on the dress, washed the label to near white, dropped the print's frame and mat, and left the rest mostly see-through (solid 6 to 39 percent on five of the nine photos; 0 percent on the magazines). Its "pixels kept" figure drops under 99% on four photos, which the script flags. Not recommended for any of Ricky's photo types.

## Where models failed

- Label (nm-dress-label.jpg): isnet erased the text. General and lite keep it legible, but the label then floats on white with a stray string line.
- Framed print: only general with --rect gave a full frame. The black frame against a dark teal pegboard is the hard case. Lite loses frame bars; isnet loses the frame entirely.
- Glass and shelf scenes (6610): the room-photo cuts show lite and isnet erasing shelf contents. This is a room-photo stress test, not a listing use.
- Same-colour neighbours (6612): the black leather chair is kept with the belts by general.

## Answering Ricky's question about picture frames

The program is not the problem. BiRefNet general with --rect already returns a complete frame on the one framed print tested (rect repair added only 3.1 percent from the photo's own pixels). What remains imperfect on that cut: tiny nicks in the top edge of the frame and one small white speck inside the mat near the right edge, where glare on the glass was treated as background. That is a rect-repair limit (it fills the convex hull, so interior holes inside the mat are not repaired), and a perspective photo makes the hull wider than the frame. One print is a small sample; I did not test other frames, mirrors or sizes.

## Recommendations

- Default model for garments: birefnet-general. It matches lite on the dress shots and is better on thin and low-contrast parts; the extra 6 to 8 s per image is cheap against the cost of re-shooting.
- Objects with straight edges (framed art, mirrors, boxes, books): birefnet-general with --rect, never lite and never isnet. Shoot against a background that contrasts with the frame (not a dark wall behind a black frame) and avoid glare on the glass, or use a cross-polarized setup, because the whited-out glare speck is the remaining flaw.
- CPU-only machine: this sandbox ran general at 16 to 25 s and lite at 10 to 16 s per photo. Lite is the only speed option worth keeping, and only for clean garment shots on plain backgrounds. Do not use isnet-general-use. Ricky's PC has a 4060 Ti; I could not test the GPU here, so no GPU number is claimed.
- Labels and close-ups: do not cut. The label shot cuts legibly with general but leaves a stray string and floating shape; the original photo is the more honest listing image. The same goes for detail, texture and flaw shots: list the original (eBay allows non-white backgrounds for secondary photos; I did not verify the eBay rule in this lane).
- Glass, shelf contents, anything transparent: list the original.

## Open questions

- Does Ricky's GPU change the model speed gap enough to make lite pointless? Not testable here.
- Is a mean 16 to 25 s per image acceptable for batch runs on his machine, and how many photos per week are expected?
- A second frame test (white frame on white wall, glass with strong reflection) is needed before calling the frame problem solved.
- The missing report line for IMG_6617 general in the first pass is unexplained; rerun worked.
