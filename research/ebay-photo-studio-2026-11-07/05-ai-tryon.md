# Lane 05: AI virtual try-on and on-model generation

Status 2026-11-07. Fetched and saved: GitHub repo pages and raw READMEs for CatVTON, IDM-VTON, OOTDiffusion, Leffa, FitDiT, and Awesome-Try-On-Models (all VERIFIED_FETCHED, in raw/05-ai-tryon/gh-*.md). Hugging Face cards, file listings and the Kolors Space app.py were read through the HF MCP tools (MCP_DATA, saved as raw/05-ai-tryon/hf-model-cards-2026-11-07.md). Blocked (CONNECT 403, tested): www.ebay.com, www.etsy.com, huggingface.co web, community.ebay.com, nightjar.so, masonry.so, growtsy.com, valueaddedresource.net, reddit. Every eBay and Etsy policy statement below is therefore SEARCH_SNIPPET or UNVERIFIED. No GPU here, nothing was run. Quality claims come from the authors' own cards and have not been tested on vintage pieces.

## Bottom line

AI try-on does not fit the eBay main photo for used vintage. It also works against Ricky's own aim of showing the real garment. The classic try-on models (IDM-VTON, CatVTON, OOTDiffusion, FitDiT) are non-commercial licences and were trained on modern studio photos of people, not mannequins or vintage cuts. The only commercially clean options are the 2026 Apache-licensed edit-model LoRAs, and those are the most likely to invent detail. Use try-on, if at all, for styling-idea images, social posts and the site, always labelled. Real mannequin photos (lanes 01 to 04) stay the eBay photos.

## Findings per model

1. Kwai-Kolors/Kolors-Virtual-Try-On. MCP_DATA. Space with 10217 likes, updated 1 Apr 2026, README says licence apache-2.0. The Space repo holds only app.py, README, requirements and assets. app.py sends base64 images to `"http://" + os.environ['tryon_url']` with secret token and cookie, so it is a thin client to a private Kuaishou server. It cannot run on the 4060 Ti and there are no weights to download. The underlying Kolors base model card says "Kolors are fully open-sourced for academic research. For commercial use, please fill out this questionnaire". Verdict: free web toy only, no commercial footing, ignore for the pipeline.

2. IDM-VTON (yisol). VERIFIED_FETCHED and MCP_DATA. Licence quote: "The codes and checkpoints in this repository are under the CC BY-NC-SA 4.0 license." Inputs: person photo plus garment photo (flat or worn), auto mask. SDXL inpainting base, 1.6M downloads. Authors claim "Authentic Virtual Try-on in the Wild" and use a garment-detail encoder, so it keeps prints better than older methods, but VRAM is not stated in the README (UNVERIFIED; SDXL-based, community reports of high VRAM from memory). Windows: README gives a conda env, no Windows statement. Non-commercial, so selling listings with it is not clearly allowed.

3. CatVTON (Zheng-Chong). VERIFIED_FETCHED. Licence: "All the materials, including code, checkpoints, and demo, are made available under the Creative Commons BY-NC-SA 4.0 license." VRAM quote: "Simplified Inference (< 8G VRAM for 1024X768 resolution)", fits the 16 GB card. Windows: "Problems under Windows OS, please refer to issue#8", ComfyUI workflow in Releases, plus a mask-free variant. Best fit technically, worst fit legally for a shop.

4. OOTDiffusion (levihsu). VERIFIED_FETCHED. Licence cc-by-nc-sa-4.0 (card). Trained on VITON-HD half-body and Dress Code full-body. Quote: "We've only tested our code and models on Linux (Ubuntu 22.04)". VRAM not stated. Oldest of the set (Apr 2024); skip.

5. Leffa (franciszzj). VERIFIED_FETCHED and MCP_DATA. Licence MIT on card and GitHub sidebar, the only classic model with a permissive licence. CVPR 2025. Quote: "prior methods often distort fine-grained textural details from the reference image ... Leffa ... significantly reducing fine-grained detail distortion". Pose transfer plus try-on, ComfyUI node by StartHua, "generating an image in 6 seconds (on A100)". VRAM not stated. Caveats (UNVERIFIED, check later): its demo masks use SCHP and DensePose and it was trained on VITON-HD and DressCode, whose data terms are often non-commercial; MIT on the weights may not cover that. Best candidate if any classic model is tried.

6. FitDiT (BoyuanJiang). VERIFIED_FETCHED. Gated, with the quote "You agree that this model will only be used for non-commercial purposes." and "This model can only be used for non-commercial use. For commercial use, please visit Tencent Cloud". Built for "Authentic Garment Details" with a two-step mask then try-on flow, bf16 / fp16 / offload options (SD3-based, so heavy; fp16 with offload is the 16 GB route, number not stated). Strongest claim on keeping prints and texture, but a hard no-commercial rule.

7. 2026 successors (MCP_DATA). These are edit-model LoRAs, not dedicated try-on nets:
- fal/flux-klein-9b-virtual-tryon-lora, 159 likes, Apache-2.0 LoRA, created 24 Feb 2026. Inputs "Person / Mannequin", top, bottom; says clothing types are T-shirts, hoodies, jackets, jeans, skirts, pants, shorts (no vintage dresses, hats, or coats listed). Its base FLUX.2-klein-9B is gated with licence "other", so commercial rights are unclear.
- xocialize/tryon-FLUX.2-klein-4B-lora, Apache-2.0, base FLUX.2-klein-4B also Apache-2.0 (3.6M downloads). The only fully permissive stack found. Needs a clothing-agnostic (masked) person image. Card admits "all-dark outfits are the weakest case" and trained on only 273 tuples. A 4B model should fit 16 GB (UNVERIFIED).
- FoxBaze/Try_On_Qwen_Edit_Lora_Alpha, Apache-2.0 on Qwen-Image-Edit (20B params, Apache-2.0), alpha, ComfyUI workflow, tops plus bottoms. 20B is too big for 16 GB without heavy quantization (UNVERIFIED).
- ovi054/virtual-tryon-kontext-lora, Apache-2.0 LoRA on FLUX.1-Kontext-dev (gated, licence other).
No successor card makes a fidelity claim about vintage fabrics, prints or wear. Generative editors rebuild the garment, so exact colour and tiny details are at risk.

## Does it preserve the real garment?

Authors of Leffa and FitDiT explicitly say earlier methods "distort fine-grained textural details". That admits the class of problem exists. For a one-off 1960s print or beaded dress, any diffusion output is a re-drawing, not a photograph. None of the cards tests mannequins as the person input, except the fal card listing "Person / Mannequin", which is a prompt convention, not evidence. All-dark and sheer, beaded, sequinned and heavily patterned pieces are the likely failures (UNVERIFIED expectation; test needed).

## Policy (all SEARCH_SNIPPET or UNVERIFIED; eBay and Etsy pages blocked)

- A search summary of seller guides: eBay "does not prohibit AI-generated or AI-edited listing photos as a category" but the seller is responsible and photos must accurately represent the item. SEARCH_SNIPPET.
- Same summary: "Stock photos are barred for used, damaged, or defective goods" and wear and flaws must be shown. SEARCH_SNIPPET.
- An eBay community thread (https://community.ebay.com/forum/selling-57920/topic/anyone-use-ai-generated-model-photos-for-clothing-464874/): commenters said garments looked better than the real photos and warned of not-as-described complaints, advising real photos first and labelling generated ones. SEARCH_SNIPPET.
- Value Added Resource reports eBay testing AI fashion models inserted into listings without seller consent. SEARCH_SNIPPET; shows eBay itself may do this, not that sellers may.
- Etsy: "Sellers must disclose within their listing description if an item is created with the use of AI." Photo-edit disclosure is described as a recommendation; some guides cite an Oct 2026 rule needing at least one unedited photo of the real item (not confirmed). SEARCH_SNIPPET.
- Vintage-specific returns risk: an AI image that flatters fit or colour is the standard path to an "item not as described" return. That is reasoning, UNVERIFIED as eBay policy.

## Recommendations for Ricky

1. Never use AI try-on for the eBay main photo or any listing photo of a used piece. Real mannequin shots, label, flaw and detail photos carry the listing.
2. If Ricky wants it anyway: optional last picture in the gallery, captioned "Styling idea, AI generated, not the actual item", only after at least six real photos. Also add a plain note to Etsy descriptions.
3. Best uses: Instagram/TikTok posts, the storefront site, and Hollie's video, where the commercial-licence risk is lower but still real for non-commercial weights.
4. If testing, use only Apache stacks first (xocialize FLUX.2-klein-4B LoRA) or Leffa after reading its data terms. Do not use CatVTON, IDM-VTON, OOTDiffusion or FitDiT for anything sold; their licences say non-commercial.
5. Skip the Kolors web demo for production.
6. Spend setup effort on the white-background mannequin pipeline instead; that is what eBay buyers and the policy both favour.

## Open questions

- Does eBay's current Picture Policy or Seller AI rules change AI-edited photos for Clothing categories? Needs the official page.
- Does Etsy's Oct 2026 update require an unedited real photo?
- Leffa licence: do VITON-HD/DressCode terms limit commercial use of the weights?
- VRAM and Windows install reality of Leffa and FLUX.2-klein-4B on the 4060 Ti 16 GB; only a hands-on test answers it.
- Do any models handle a headless mannequin or a dress form as the person input without hallucinating a head and arms?

## URLs to fetch once the network opens

- https://www.ebay.com/help/policies/listing-policies/picture-policy?id=4370 (picture rules, stock photos) [blocked]
- https://www.ebay.com/help/policies/ebay-user-agreement (seller responsibility for generative AI content) [blocked]
- https://www.etsy.com/legal/creativity-standards (AI disclosure sentence) [blocked]
- https://www.etsy.com/legal/sellers (listing photo requirements, Oct 2026 change) [blocked]
- https://community.ebay.com/forum/selling-57920/topic/anyone-use-ai-generated-model-photos-for-clothing-464874/ (seller experience) [blocked]
- https://www.valueaddedresource.net/ebay-tests-ai-fashion-models-alters-images/ (eBay AI model test) [blocked]
- https://huggingface.co/black-forest-labs/FLUX.2-klein-9B (licence text) and https://github.com/franciszzj/Leffa/blob/main/LICENSE plus the VITON-HD and DressCode dataset terms
- https://github.com/Zheng-Chong/CatVTON/issues/8 (Windows problems)
- Reddit r/ebay and r/Flipping threads on AI model photos [blocked]
