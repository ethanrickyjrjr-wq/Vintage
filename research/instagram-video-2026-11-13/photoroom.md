2026-11-13 | lane: photoroom | all quotes from crawl4ai fetches today, raw files in `raw/photoroom-*.md`

## Headline
Photoroom now makes video, but the plan Hollie pays for (Pro) does not include it. Video is on Max and Ultra. API video is Enterprise-only.

## Findings

**1. Video exists, gated to Max/Ultra.**
- Pricing page: Pro row "Not included: Video for ads and product pages"; Max "Video for ads and product pages"; Ultra "More video ads for heavy use" and "4K images + HD video". Credit table: "Video for ads and product pages - Pro: Not included, Max: Up to 50 generations, Ultra: Up to 150 generations". (https://www.photoroom.com/pricing, raw/photoroom-pricing.md)
- "You can also animate your product photos into product videos for your product pages and listings. Both are included in Max and Ultra and use your plan's credits." Same page.
- Video generator page: "Available on web, iOS, and Android on Max and Ultra plans." Two tools: Video Ad Maker (AI plans the video) and Product Animator ("300+ video templates, add up to four product photos, and generate. Add a short prompt if you want to change the camera angle or the setting"). (https://www.photoroom.com/tools/video-generator)
- Reels size: "Photoroom exports video ads in 9:16 vertical format for ... Facebook and Instagram ads, Reels and Stories, and in 16:9 for YouTube". Video Ad Maker takes up to 6 photos; clips "from a quick 5-second clip to a full 10-second showcase". (https://www.photoroom.com/tools/video-generator/ad-maker)
- Template categories listed include Dresses, Tops, Bottoms, Outerwear, Accessories, Footwear, Bags, Furniture, UGC, Motion. Ad Maker adds AI actors, music, AI voiceover (not wanted for a vintage shop's own voice; skip).
- Faithfulness claim (vendor marketing, unverified in practice): "Videos are generated from your own product photos, so colors, materials, and logos match the real item." Generative video can still drift on fabric, labels, flaws; check frame by frame.
- Dollar prices for Pro/Max/Ultra did NOT render in the crawl (no `$` on the pricing page). Prior project note says same. Plan prices: could not verify.

**2. Stills.** Pro includes "Unlimited core tools", "AI Backgrounds", "AI Fashion Models"; core tools incl. Background Remover, Retouch, AI Shadows (Presets), AI Fill, AI Expand/Resize, Image Enhancer. 1,000 exports/month, 8,000 AI credits. "Not included: Adjustable AI Shadows", "4K images". AI Fashion Models 1K: Pro up to 1,600 generations; 2K not on Pro. (pricing page)
- Batch: "apply the same edits and AI tools across images at once"; includes "Ghost Mannequin, Virtual Model, Recolor, Flat Lay, Beautify, Product Staging, and Edit with AI". (https://www.photoroom.com/batch)
- Virtual model: input "a shot of someone wearing your products or simple flat lays", output "portrait, landscape, or square". (https://www.photoroom.com/tools/virtual-model)

**3. Misrepresentation risk (my judgement, flagged).** Staging, AI backgrounds, virtual models and ghost mannequin regenerate pixels. For a used item, a regenerated garment or a lifestyle scene can hide wear or change color. Project decision already stands in `docs/ebay-photo-studio.md`: no generative method on a listing photo without comparing against the real garment. For Instagram, AI scenes are lower risk than on eBay but still should not alter the item. Safe: real cut-out on a brand-color or room-photo background, real shadow.

**4. Reel-size templates / Brand Library.** The pages `/tools/video-maker` and `/tools/instagram-story-maker` returned "The page you are looking for cannot be found." No Instagram story/post template page found. Whether Brand Library applies to video templates: could not verify. The Video Ad Maker page makes no Brand Library claim. Pricing lists Brand Library on Pro+ (from prior docs).

**5. API.**
- Plans: Basic = Remove Background API; Plus = Image Editing API (AI Backgrounds, AI Shadows, AI Expand, Ghost Mannequin, Virtual Try-On, Product Staging); Enterprise = "Access all APIs ... Image to Video". (https://www.photoroom.com/api/pricing)
- Video API: "Available on Enterprise plans" (video generator page); Image to Video API "Output fits Instagram, TikTok, YouTube Shorts" (https://www.photoroom.com/api/image-to-video-api). Docs list "Video API (Enterprise Plan)" (https://docs.photoroom.com/). So no scripted video on a normal plan.
- Prices: "Basic price per image of $0.02"; "Plus price per image of $0.10"; examples "$20 Basic API plan (1000 images)", "$40 ... (2000 images)". Free: "1,000 sandbox calls a month on the Image Editing API" (watermarked) and "10 free production calls on the Remove Background API". 1 Plus call = 5 Basic images. (api/pricing)
- "Pro, Max and Ultra don't include any API allowance, and the API has its own plans"; "you can subscribe to a self-serve app plan and a self-serve API plan in parallel." (pricing page)
- Endpoints seen: `POST https://image-api.photoroom.com/v2/edit` with `background.color`, `shadow.mode=ai.preset-soft`, `padding`, `lighting.mode`, `export.format` (webp); also `v1/segment`. Limits: Image Editing max 30MB, 5,000 px; Remove BG 50MB, 6,000 px. (https://www.photoroom.com/api)
- Padding/positioning and background control exist, so a script could make a 9:16 still (e.g. canvas size, white or brand-color background) per photo, but I did not see a documented 1080x1920 canvas parameter: unverified. Rate limits: docs page returned 113 bytes (wall); could not verify.
- Photoroom MCP: "Add Photoroom as a custom connector, then ask Claude to remove backgrounds, stage products, put clothes on a model and more. Works in Claude, Cowork and Claude Code." (https://www.photoroom.com/api/claude). Which API plan it bills against: could not verify.

**6. Terms.** Terms (https://www.photoroom.com/legal/terms): "We grant Free Accounts ... license ... for your own personal, non commercial purposes"; paid subscription "for the Customer's own internal business purposes"; "Customer will own all Customer Content ... Photoroom does not claim any ownership rights in Customer Content." I found no clause in the crawled text about ownership or commercial use of AI-generated outputs specifically; the generated-output clause could not be verified (no matching text; may be in a separate AI/usage policy).

## Could not verify
Dollar price of Pro/Max/Ultra; credits cost per video; video clip length on Product Animator; Brand Library on video; any 1080x1920 canvas size in editor/API; API rate limits; AI-output commercial-use clause; Enterprise video price.

## Recommendation
- Photoroom on Pro does: cut-outs, white/brand backgrounds, shadows, resize/expand, batch, API stills. Keep this role. Make 9:16 stills (1080x1920, item centered, brand-color or room backdrop) for Reel frames; do this with Photoroom editor/batch (Pro) or `v2/edit` on the Plus API ($0.10/image, plus its own subscription; $0.02 for plain cut-outs).
- Photoroom Pro cannot animate. For motion you need Max (price not verified on the page; check at checkout) for Product Animator/Video Ad Maker, up to 50 generations/month at Max; generative camera motion on a garment may alter it, so test on one item first. Otherwise use another tool (CapCut/Reels editor, lane peers) for Ken Burns zooms, slideshow and text over the 9:16 stills, which keeps the real photo intact.
- Scripted auto-video from Photoroom: Enterprise only, not realistic.
- Do not use Virtual Model or Staging as the primary shot of a used piece.
