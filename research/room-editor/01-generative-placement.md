# Room editor: is FLUX.2 Klein the right tool for "put THIS product HERE"?
Researched 2026-10-27. Raw pages in `research/room-editor/raw/` (names cited as `raw/x.md`). VERIFIED = read on a live page this session (URL given). UNVERIFIED = not read, or read only as a vendor claim. No model was run, so "does it behave" claims are UNVERIFIED unless a page says so.

## 1. What FLUX.2 Klein 4B actually promises
Source: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B , https://docs.bfl.ai/guides/prompting_unified_reference , https://docs.bfl.ai/guides/prompting_guide_flux2 , https://huggingface.co/docs/diffusers/main/en/api/pipelines/flux2
- VERIFIED licence: 4B is Apache-2.0 ("open weights available for commercial use"); 9B is "FLUX Non-Commercial License" (card text, plus HF API `flux-non-commercial-license`). 9B is out.
- VERIFIED: Klein takes at most 4 reference images (BFL unified reference table). Room + 3 products and you are full. Several items by reference does not scale.
- VERIFIED BFL Klein guidance: "What you write is exactly what the model receives" (no upsampler), "write in prose, not keyword lists", "describe the light source, direction, and softness". FLUX.2 guide: "no negative prompts. Describe what you want." Card limitations: "may fail to generate output that matches the prompts", "heavily influenced by the prompting style".
- VERIFIED: no coordinate or bounding-box feature is documented for FLUX.2. Boxes (0-1000 grid) exist only for FLUX 3 Image (https://docs.bfl.ai/guides/prompting_editing_multi_reference), and even there "Placement is a strong hint, not a hard constraint". So the normalized x/y we send Klein as text is undocumented. Whether it follows them is UNVERIFIED.
- VERIFIED: `Flux2KleinPipeline.__call__` takes `image`, `prompt`, `latents`, `sigmas`, `max_sequence_length=512`; there is NO `mask_image` and NO `strength` (`raw/diffusers-flux2.md` line 173). So there is no built-in inpainting; I infer from the signature that every call redraws the whole frame.
- BFL lists "Interior design: place furniture and decor in rooms" as a multi-reference use, and says to "describe how each input should be used". It never promises exact position or scale.

Why the urn lamp landed mid-table (reading of our code, not a vendor claim): `decorate` mode in `site/room-worker.mjs prompt()` sends no position or size and `room-renderer/app.py` adds no crop, so the 4B model picked the spot and the scale. Our prompt is also negation-heavy ("Do not...") against BFL's advice, and roughly 2k characters (my estimate); the app appends the image-3 sentence last and `max_sequence_length` is 512, so check whether the tail is truncated (token count UNVERIFIED).

## 2. Is "composite first, harmonize second" a recognised technique?
Source: https://ar5iv.labs.arxiv.org/html/1911.13239 , https://huggingface.co/dx8152/Qwen-Image-Edit-2509-Fusion , https://sofabrain.com/learn/how-does-ai-virtual-staging-work/ , https://arxiv.org/html/2403.18818 , https://runway.com/resources/ai-virtual-staging
Yes, it is the standard decomposition:
- Image harmonization is defined as the second step after pasting a foreground (DoveNet / iHarmony4, CVPR 2020).
- The Qwen "Fusion" LoRA is a packaged version. Its trigger string (Chinese on the card) reads roughly: "fuse the image; correct the product's perspective angle and lighting, and blend the product into the background" (VERIFIED card text; the translation is mine). Note it is allowed to change perspective, so it does not hold geometry either.
- SofaBrain describes staging as separate steps: mask what may change, generate, then "blending and lighting" to match light direction, shadows, colour and grain.
- ObjectDrop (Google) says diffusion edits "often violate physical laws... occlusions, shadows, and reflections" and trains specifically for them. Runway's staging checklist: "Contact shadows appear beneath furniture", "Shadow direction matches the room's light".
- Commercial staging (Q4): Luw.ai (vendor page) says most AI staging leaves "the layout... the model's decision, furniture cannot be nudged" and sells 3D drag placement instead. Runway lists ApplyDesign for "DIY placement". Decor8 describes upload, pick a style, AI transforms (no user placement). Virtual Staging AI and roOomy pages said nothing about placement; I will not cite them.

## 3. Candidates
| Model | Licence (read where) | Size | ZeroGPU-feasible (free 5 min/day) | Holds position? | Identity-preserving? | Verdict |
|---|---|---|---|---|---|---|
| FLUX.2 klein 4B (now) | Apache-2.0, VERIFIED card + HF API | 3.9B, ~13 GB VRAM | Yes, our Space runs it; `duration=15` cap | No as used (model chooses; text coords undocumented). Yes only if we paste back | Reference-guided, not pixel-exact; whole frame redrawn | KEEP, change usage (s.5) |
| FLUX.2 klein 9B | FLUX Non-Commercial, VERIFIED | 9.1B | n/a | same | same | REJECT (licence) |
| FLUX.1 Kontext dev | `flux-1-dev-non-commercial-license`, VERIFIED HF API | 11.9B | n/a | n/a | n/a | REJECT (licence) |
| FLUX 3 Image Klein (released 2026-10-13) | FLUX Kommunity v1.0: outputs commercial only for a "Qualifying User" (<US$5M gross revenue incl. affiliates) AND content filters or review AND AI disclosure where law requires (s.2.a, 2.e). Text read from the **-base** repo; the distilled repo LICENSE is gated. Base verified, distilled needs review | 5.6B + Qwen3-VL-4B encoder; mandatory 9B upsampler (18.8 GB) | No on `large` (48 GB): 31 GB base + ~28 GB upsampler. Official Space calls the upsampler on a separate `PUP_URL` endpoint, and offers `xlarge` (2x quota). Space authors budget ~23 s for a 1 MP text-to-image on `large` (their code estimate) | Only documented positional control: boxes, but "strong hint, not hard constraint"; "edits can change content outside the requested region" | "reference images anchor content, they do not lock structure" | WATCH, not now |
| Qwen-Image-Edit-2511 (+ Fusion LoRA, 2509-based) | Apache-2.0 base, VERIFIED card + API; LoRA tagged Apache-2.0 | 20.4B | Poor: both community Spaces I read use `size="xlarge"` (2x quota) and swap in a Rapid-AIO transformer, so their speed says little about the base | No (fusion LoRA may re-angle the product) | "Better consistency", vendor claim only | FALLBACK to test if Klein harmonize fails |
| IC-Light (SD1.5 relight) | Code Apache-2.0 (GitHub); weights `creativeml-openrail-m` (HF page). Terms unread: commercial use UNVERIFIED | SD1.5-class | Official Space is on ZeroGPU | Takes a foreground image and relights it; makes no room shadow | Recolours the foreground | NOT A FIT alone |
| Insert Anything | MIT LoRA on FLUX.1-Fill-dev, which is non-commercial (VERIFIED HF API) | base size not checked | Official Space showed RUNTIME_ERROR | mask-prompt | reference-based | REJECT (base licence) |
| AnyDoor / Paint-by-Example | AnyDoor code MIT, weights licence UNVERIFIED; PbE `creativeml-openrail-m` | SD-class | UNVERIFIED | no | ObjectDrop Fig. 6/7: both lose identity and shadow quality vs ObjectDrop | REJECT (old) |
| ObjectDrop / ObjectMate (Google) | project page links only paper/arXiv; no weights seen | n/a | n/a | n/a | n/a | NOT AVAILABLE |
| GPSDiffusion / DESOBA shadow generation | code MIT; checkpoints on Baidu/Dropbox | n/a | no Space found | n/a | n/a | research only |
| Local canvas paste + shadow + colour match | none | 0 GPU | Free, instant | Exact | Exact | KEEP as step 1 and the offline fallback |

Sources: https://huggingface.co/black-forest-labs/flux-3-image-klein , https://huggingface.co/black-forest-labs/flux-3-image-klein-base/blob/main/LICENSE.md , https://github.com/black-forest-labs/flux-3-image-klein (the Space's `app.py` is saved at `raw/spaceapp-bfl-flux3-klein.py`), https://huggingface.co/Qwen/Qwen-Image-Edit-2511 , https://huggingface.co/lllyasviel/ic-light , https://huggingface.co/WensongSong/Insert-Anything , https://objectdrop.github.io/ , https://github.com/bcmi/GPSDiffusion-Object-Shadow-Generation . ZeroGPU limits: https://huggingface.co/docs/hub/spaces-zerogpu .
- Discrepancy, FLUX 3 Klein licence: HF card says "commercial output generation by Qualifying Users" (verified); whether a hosted shopper-facing preview counts as "your" commercial use of Outputs is UNVERIFIED. A VentureBeat piece restates the $5M rule (secondary source).
- No community Klein-4B LoRA for harmonize or relight turned up in HF search (only `aydin99/flux2-klein4b-seam-blend-v1`, 0 downloads, no licence tag; outpaint and object-remove LoRAs from fal).

## 4. The quota is the real ceiling
Source: https://huggingface.co/docs/hub/spaces-zerogpu ; `site/room-worker.mjs` lines 4-6.
- VERIFIED: free account = 5 min GPU/day; `large` = half RTX Pro 6000 (48 GB) at 1x; `xlarge` = full GPU (96 GB) at 2x. (My memory of "H200" is out of date.)
- Our worker allows `DAILY_LIMIT = 3` per visitor and `STORE_LIMIT = 30` per day. 30 x the 15 s cap = 450 s, over the 300 s quota, if calls run to the cap (actual seconds UNVERIFIED; `app.py` already returns `seconds`, log it). At 15 s that is 20 previews/day.
- UNVERIFIED and decisive: the ZeroGPU page does not say whose quota a server call with `HF_TOKEN` draws from. Test it before trusting any per-day number.
- Consequence: cost per preview must not grow with item count. Composite-first gives one call for N items. Anything on `xlarge` halves the previews.

## 5. Non-AI baseline, and how far it gets
Source: https://ar5iv.labs.arxiv.org/html/1911.13239 (DoveNet user study, 9,999 real composites; scores are Bradley-Terry).
- Classical colour-statistics harmonization did not beat the raw paste: input composite 0.624, Lalonde & Efros 0.260, Xue 0.567, Zhu 0.337; deep DIH 0.948 (DoveNet is the top method in the paper). Table 1 agrees: Lalonde & Efros PSNR 30.16 vs composite 31.63 (lower is worse), MSE 150.5 vs 172.5.
- Caveat: iHarmony4 composites are colour-perturbed real foregrounds, and no shadows were judged. Treat it as "naive global colour matching can look worse than doing nothing", not a measurement of our case.
- I found no published guidance on canvas drop-shadow quality. A cheap canvas contact shadow (blurred dark ellipse, multiply) is still worth doing as a hint to the model and as the no-quota fallback; its realism is UNVERIFIED.

## 6. Recommendation: keep FLUX.2 Klein 4B, change how we use it
Do not switch. Do not ask Klein to choose or find a position. Use it only to add light and shadow, and discard everything else it draws.
1. Browser: the shopper drags and scales each cut-out on the room photo (position and scale are then exact numbers, which also covers "several items" and "drag-and-drop"). Cut-out mattes: see `research/cutouts/` (not re-read here). Licence tags I checked: BiRefNet MIT, RMBG-2.0 `bria-rmbg-2.0` (not Apache).
2. Browser: render composite C = room + all items + a canvas contact shadow under each. Build mask M = dilated cut-out matte plus shadow zone, feathered ~10 px.
3. One Klein call, `image=[C]` (optionally add one catalog ref, max 4). No coordinates. Positive prose only, e.g. (my draft, untested, ~110 words):
   "Image 1 is a photograph of a room. A {title} has been pasted in at its final position and size, so it looks flat, with no shadow and the wrong light. Edit image 1 so the {title} looks photographed in this room: it rests on the {surface} with a soft dark contact shadow directly beneath it and a longer, softer shadow falling away from the {light side}; its brightness, colour temperature and grain match the room's {warm|cool}, {soft|hard} light. The {title} keeps exactly the position, size, shape, pattern and colours it has in image 1. Every other part of the room stays exactly as in image 1. Style: unretouched interior photograph. Mood: natural."
   {light side} and {warm|cool} come from the canvas (luminance centroid, mean R/B of the room). Supported by BFL Klein prose and light-source guidance; effect on Klein is UNVERIFIED.
4. Paste-back (the step that makes this safe): final = original room outside M, Klein output inside the feathered band M, and the original cut-out pixels, tone-matched (Lab mean/std) to Klein's rendering of the object, inside the matte. Needed because Klein has no mask input and BFL says even FLUX 3 "edits can change content outside the requested region".
5. Untested variant to save quota: run Klein on a crop around the items plus margin (smaller token count), then paste back.
6. "Decorate for me": position and scale come from outside the diffusion model: a rule per `product.surface`, or a grounding model proposes a box that the shopper sees as a draggable ghost, then step 1 onward. Qwen3-VL-4B is Apache-2.0 (VERIFIED) and claims "stronger 2D grounding" (vendor claim, UNVERIFIED; also spends quota).
7. Gate before building: 5 rooms x 2 products, log `seconds`, rate shadow and light by eye. If Klein output is not clearly better than the canvas composite alone, test Qwen-Image-Edit-2511 + Fusion LoRA (2x quota) before FLUX 3 Image Klein (licence, upsampler and filter work).

## What I could not verify
- Whether Klein 4B follows text coordinates or holds a pasted object at 4 steps (no model run; BFL pages silent for FLUX.2).
- Whose ZeroGPU quota a Worker call using `HF_TOKEN` consumes, and real seconds per call.
- Token length of the current prompt against `max_sequence_length=512`.
- FLUX 3 Klein distilled-repo LICENSE (gated); whether hosting for shoppers is "your" commercial use; what filter satisfies s.2.e.
- OpenRAIL-M terms for IC-Light weights; AnyDoor weights licence; ObjectDrop/ObjectMate weights existence beyond its project page.
- Real quality of the Fusion LoRA (only the author's card; no 2511 version found).
- Any placement detail for Virtual Staging AI and roOomy; Luw.ai and Decor8 text is vendor marketing.
- Quality of a canvas-only contact shadow (no published source found).
