# Lane 04: ghost mannequin

Status (2026-11-07): Fetched and saved: GitHub topic page, two GitHub repo pages, ghost_auto.py source, plus HF model README and Space READMEs (MCP_DATA) under raw/04-ghost-mannequin/. BLOCKED by the proxy (403 CONNECT, saved as stub files): every vendor and tutorial host tried (photoroom docs and help, wearview, fashn, retouch4me, pixc, kaptured, rewarx, catalogcut, picjam, photta, shotova, snappyit, fixanyphoto, colorexpertsbd, retouchinglabs, retouchingzone, imageexpertindia, clippingpathzone, mannequinmadness, community.ebay.com, all-about-photo, pixelretouching), plus ebay and reddit. Because of this, all shooting, Photoshop, GIMP, Affinity, timing, price and "what sellers do" claims are SEARCH_SNIPPET at best. Nothing here is from memory except where marked UNVERIFIED. No Reddit thread surfaced in two searches.

## What it is (SEARCH_SNIPPET)
A ghost mannequin shot is a garment photographed on a form, then the form is removed in editing so the clothing looks worn by nothing. Search summary: "A ghost mannequin is shot on a form, then the form is removed in editing, which leaves a garment that looks worn." Source: https://snappyit.ai/ghost-mannequin (snippet only).

## Shooting method (SEARCH_SNIPPET, vendor blogs; sources listed in 'urls to fetch')
- Two exposures per garment: front on the form, then either the form turned and the garment dressed inside out/back, or the garment laid flat on white foam board to shoot the inside back collar and brand label. Lighting and white balance must match between frames so the composite blends.
- The inside-neck/inside-collar shot is the "fill" that appears behind the neck opening once the form is gone. Sleeves and hems: same pattern (extra frames of interior areas for complex pieces) per one guide.
- A "ghost mannequin torso form" with removable neck and arm pieces makes this easier; "A plain dress form has no removable parts, so producing a ghost effect from a dress form takes more masking work." (snippet, vendor). Pinning/clamping specifics were not obtainable. UNVERIFIED general practice: pin excess fabric at the back so the front looks fitted, keep camera, tripod and light locked between frames.

## Manual editing (SEARCH_SNIPPET)
Photoshop: cut out the front (Pen tool or Select Subject, refine edge at collar, shoulders, armholes), place the inside-collar layer behind, scale and warp it to the neckline, add a shadow layer at roughly 35 to 40 percent opacity, check joins at 100 percent. GIMP: Free Select or Foreground Select to outline, layer mask (black hides, white reveals), feathered mask edge. Affinity Photo: no dedicated tutorial found; steps should transfer (masks, Move/Transform), menu names unconfirmed. Time per garment (vendor claims): about 15 to 20 minutes for a simple neck join by a skilled editor, 45 to 60 for coats, blazers, dresses; beginners 2 to 3 times that; "a brand without a trained Photoshop editor often lands at 40-60 minutes per image." Outsourced: $0.39 to $0.89 basic neck joint, $1 to $3 with shadows, $5 to $15 complex; AI from $0.19 per image (WearView, vendor claim).

## Open-source and Hugging Face (VERIFIED_FETCHED / MCP_DATA)
1. ccsaltik-photography/GhostMannequinEngine (VERIFIED_FETCHED, https://github.com/ccsaltik-photography/GhostMannequinEngine, raw/gh-GhostMannequinEngine.md). Quote: "It seamlessly fuses an on-hanger product image with an unbuttoned/flat lay back-collar image, completely automatically." Uses SAM 3.1 masking and a thin plate spline warp, with a QC bot. Needs PyTorch, OpenCV, SciPy and "SAM 3.1 weights in weights/sam3.1/". Usage: python ghost_auto.py --hanger X --flat Y --out output/. Caveats: 0 stars, 2 commits, no license visible on the page, code comments are Turkish, written for hanger shots (not forms) and 6720x4480 masters, SAM 3.1 weights are separate and probably gated. This is the only real neck-joint automation found, and it is exactly the two-shot method, automated. Treat as a prototype to test on one garment, not a product.
2. awekakwe/json-ghost-mannequin-pipeline (VERIFIED_FETCHED, https://github.com/awekakwe/json-ghost-mannequin-pipeline). Topic page: "automated 6-step pipeline ... using SDXL, ControlNet, and Gemini Vision" (the peterpeeterspeter original, 2 stars). The awekakwe copy has a README that is generic download-bait ("Download Now", a zip link to a .zip path inside src/) and an MIT license. WARNING: do not download or run its zip. The original peterpeeterspeter/json-ghost-mannequin-pipeline is the one to read, and needs a Gemini API key (UNVERIFIED).
3. GitHub topic ghost-mannequin (VERIFIED_FETCHED): only 3 public repos; the third is a Photta marketing checklist repo. The ecosystem is thin.
4. HF model nhathoangfoto/FLUX.2-klein-ghost-mannequin (MCP_DATA, raw/hf-flux2-klein-ghost-mannequin.md). apache-2.0 LoRA, trigger "3Dghostmannequin", "Trained on 50 diverse, meticulously curated pairs", 20.4K downloads. Base black-forest-labs/FLUX.2-klein-base-9B is gated, license "other", 9B parameters. Likely fits 16 GB with quantization (UNVERIFIED). It regenerates the garment with a diffusion model, so it can invent collars, prints and seams. For used goods that is a risk (see honesty section). No image-in/out guarantee from the README beyond "transforms flat or mannequin-worn clothing".
5. HF Spaces (MCP_DATA): amrhisham123/clawset-ghost-mannequin ("rembg + clothing segmentation + Stable Diffusion inpainting", 0 likes, no license) and meowmeows1/wardrobe-ghost-mannequin (MIT, README is only a title). Both are 0-like experiments. No HF results for "invisible mannequin" or "mannequin removal".

## Commercial AI (SEARCH_SNIPPET unless noted; vendor sites blocked)
- Photoroom: official docs (snippet): API parameter "ghostMannequin.mode" set to "ai.auto", default 1K output (1024x1024), accepts flat, hanging, mannequin or model input; Android app offers square or 3:2 output. Most credible single-photo tool. Pricing conflicting in snippets (about $29/mo in one blog).
- Pixelcut: ghost mannequin claimed by comparison blogs; Pro about $8 to $10/mo (conflicting).
- WearView: $29/mo or $49 for 200 credits, service from $0.19 per image (vendor).
- Rewarx: claims $29/month flat (own blog, treat as marketing). Photta from $14/mo, Pixelz $0.95/image plus $0.50 invisible mannequin, Picjam $99/mo, Musely free with low quality.
- Claid and Pebblely: described as not dedicated ghost mannequin tools. Flair: manual brush needed. Kive, Dresma: nothing found.
- Cross-source caution (snippet): AI tools "may redraw collars, prints, buttons or seams"; weakest on drape and fine interior detail.

## Do vintage sellers ghost? Honest answer
Evidence is thin and mostly vendor-written. SEARCH_SNIPPET from eBay community threads: one seller found flat lays outsold mannequin shots (small sample); another saw sales rise after switching from flat lay to a dress form. No source showed pre-owned or vintage sellers routinely using ghost mannequin. eBay guidance in snippets: used items require your own photos "that accurately represent the specific item being sold, including any flaws or wear", up to 24 photos, 1600 px recommended; nothing eBay-specific about forms. My reasoned conclusion (labelled inference, not evidence): ghost mannequin is a new-goods catalog technique where every unit is identical and flaws do not exist. For one-of-a-kind used garments, a visible form shows true fit, drape, shoulder structure and the vintage cut, a heavily composited image can hide or invent detail, and buyers of vintage trust honest photos. Compositing a neck from a second photo is also a place to accidentally misrepresent a garment.

## Recommendations for Ricky
1. Default for Holliewood and Vine: keep the form visible, clean white or soft neutral backdrop, even light, with the hero shot on the nice vintage form (the visible form is on-brand with the room). Cut the background out, leave the form in.
2. Add flat, honest shots: label, inside neck, each flaw, closure, close-up of fabric. These do the trust work.
3. Ghost only for clean, structured, simple garments (blazers, coats, tailored jackets, shirts) where the form shows awkwardly or there are no flaws, and always include one visible-form or flat shot alongside. Never ghost fragile, stretched, stained or heavily damaged pieces, and never use a generative method (FLUX LoRA, inpainting Spaces) on a vintage listing unless you compare to the real garment.
4. If you want to try ghosting: use the two-shot method with a removable-neck torso form (shoot front, then neck and inside-back with identical light, tripod locked), composite in Photoshop or GIMP in about 20 to 45 minutes, or test GhostMannequinEngine on one garment on the 4060 Ti. Test Photoroom's single-photo ghost on the same garment as a comparison.
5. Do not install or run the awekakwe zip.

## Open questions
- Does Ricky own a removable-neck form, or only the solid vintage forms? (decides whether ghosting is practical)
- Does the Photoroom ghost output hold up on vintage prints and lace? Needs a one-garment test.
- GhostMannequinEngine: license, SAM 3.1 weights access, whether it works on form shots rather than hanger shots.
- eBay's current Seller Center language on edited and AI-altered photos.
- Reddit r/Flipping, r/EbaySellers, r/vintage opinions, none retrieved.

## URLs to fetch once the network opens
- https://fashn.ai/blog/ghost-mannequin-photography-complete-guide (shoot and Photoshop detail, cost)
- https://retouch4.me/blog/how-to-create-the-ghost-mannequin-effect-for-ecommerce-product-photography (step-by-step)
- https://pixc.com/blog/how-to-create-a-ghost-mannequin-effect-photoshop/ (Photoshop steps)
- https://retouchinglabs.com/ghost-mannequin-tutorial/ (tutorial)
- https://www.retouchingzone.com/edit-ghost-mannequin-photography-in-gimp/ (GIMP steps)
- https://docs.photoroom.com/image-editing-api-plus-plan/ghost-mannequin (official Photoroom spec and pricing)
- https://www.photoroom.com/tools/ghost-mannequin and https://www.wearview.co/blog/best-ai-ghost-mannequin-tools (tool comparison, pricing)
- https://community.ebay.com/t5/Selling/Using-a-mannequin-to-display-clothing-for-resale-Dated/td-p/32785890 and https://community.ebay.com/t5/Ask-a-Mentor/a-ghost-mannequin-tool/td-p/32239377 (seller opinion)
- https://blog.mannequinmadness.com/2019/05/a-crash-course-in-staging-your-clothing-to-photograph-to-sell-online/ (pinning and staging)
- https://github.com/peterpeeterspeter/json-ghost-mannequin-pipeline (original of the SDXL/ControlNet pipeline)
- https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B (license terms)
- Reddit searches: r/Flipping, r/EbaySellers "ghost mannequin" and "dress form".
