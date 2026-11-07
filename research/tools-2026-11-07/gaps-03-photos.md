# Gaps review: lane 03, product photo apps (shoot, cut out, retouch, upscale, resize, batch)

Date: 2026-11-07. Author: research subagent (completeness critic for lane 03).
Question: Which photo tools for one-of-one vintage pieces on Windows and iPhone are missing from the lane 03 list (launched or renamed in 2025 and 2026, present on Shopify App Store, Chrome Web Store, App Store or GitHub category pages, or free and open source), and which listed tools are defunct, acquired or renamed?
Legend: V = vendor, app-store, GitHub or Shopify App Store page read today (2026-11-07); U = unverified (page would not load, price not in the text layer, or no vendor page reached).

Method note. WebSearch's shared budget for this turn was already used up when this agent started, so no search engine was queried. Every page below was fetched directly through the session's headless Chromium fetcher (curl fallback) at a vendor, app-store, help-center, GitHub, Hugging Face, Chrome Web Store or Shopify App Store URL. Leads came from category pages fetched today: the GitHub topic `background-removal` (1,024 repositories, sorted by stars), the Shopify App Store search "background remover" (787 apps), the Chrome Web Store search "background remover", and Apple's iTunes lookup API (a vendor API, not a search engine). Product Hunt returned 403. Reddit was not read. About 80 URLs were fetched; 70 loaded. Tools already on the lane list were not re-verified, except where a page fetched for another reason corrected a lane "U" (Cutout.pro) or showed a rename.

## 0. Bottom line

- The lane missed two free Microsoft tools already in Ricky's reach. Windows 11 Paint has one-click AI "Background Removal" and layers, built in and free (V). Microsoft Designer is free with a Microsoft account on iPhone and web, with "Remove background" and "Generative erase" (V, App Store listing). Together with Windows Photos and Snapseed these make the zero-cost stack deeper, not wider.
- Apple Photos has more than "lift subject": the Clean Up tool removes cords, tags and reflections with a tap, brush or circle, free, but only on "iPhone 15 Pro, iPhone 15 Pro Max, or iPhone 16 model or later" and "Usage limits may apply" (V). Check Ricky's model before counting on it.
- The cheapest commercial product-photo app read today is PicWish: Pro is "$4.99 /mo Billed Annually" ($59.99 a year), with a white-background tool, product retouching and bulk listing images, on iOS, Android, web and Windows (V). That undercuts Pixelcut Pro ($8 a month yearly) and Photoroom Pro ($7.50 a month yearly) on the lane list. Monthly-billing price did not render.
- Pay-per-use cutouts are cheaper than the lane's options: Pixian.AI sells 250 credits for $5.00 with megapixel pricing, where a 2 MP image costs 0.117 credits, and credits "do not expire" if a purchase was made in two years (V). Free use is capped at 0.25 megapixels, too small for Etsy.
- Open source has moved on since rembg: withoutBG ships an "Apache-2.0" open-weights model that runs locally with Docker or pip and a web demo with "5 free images a day, no signup" (V). Removerized runs BiRefNet-class background removal and an upscaler entirely in the browser, offline-capable, GPL-3.0 (V). BG-Remover is a free MIT Windows installer with the model embedded, so no Python (V). BiRefNet itself released higher-resolution weights in 2025 (BiRefNet_HR at 2048x2048, BiRefNet_dynamic) under MIT (V); rembg's `birefnet-general` is the older general model.
- Free batch utilities the lane lacks: Caesium Image Compressor (GPL-3.0, Windows desktop batch compression with preview, V), chaiNNer (GPL-3.0 node-based upscaling and batch chains, V), Bulk Resize Photos ("100% free", browser, "No sign-up", V) and two Chrome extensions that remove backgrounds offline in batches (V).
- Paid Windows editors that bundle AI cutout, retouch and upscale exist but none beats the free stack: Movavi Photo Editor "Lifetime $49.95" (V), Luminar "Desktop Only" "$99.00" one-time with AI tools limited to 365 days (V), HitPaw FotorPea perpetual "$130.39" (V), Aiarty lifetime "$109.00" (V), CyberLink PhotoDirector 365 "$5.83/mo" on sale (V), ON1 Photo RAW 2027 "$99.99" (V). All marked pricier.
- Renamed or moved: Luminar Neo is now plain "Luminar" (skylum.com/luminar-neo redirects; no "Neo" on the product or pricing page). HitPaw Photo Enhancer is "HitPaw FotorPea". Mokker AI confirms "Mokker AI is now soona's AI Studio". Photomator and Pixelmator are now sold by "Apple Inc." Cutout.pro is not price-less: its pricing lives at /image-pricing (80 credits a month for $5.00; pay as you go $0.130 a credit), which fixes the lane's U. V.

## 1. Comparison table: tools missing from the lane list

Pipes inside vendor quotes are replaced with semicolons so the table renders.

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Microsoft Paint (Windows 11) | Built-in editor with AI Background Removal, Layers, Image Creator, crop, rotate, resize | Free. "Included in the latest version of Windows 11, Paint is your new creative partner." | Everything | Windows 11 | High. Already on the PC, no account. "This powerful editing tool uses AI to help you isolate a subject and remove the background with just one click." A second opinion next to Windows Photos when an edge fails | V | https://www.microsoft.com/en-us/windows/paint |
| Microsoft Designer | Free AI design app: "Remove background", "Generative erase", "Blur background", templates, image generation | "Microsoft Designer is available for free with a Microsoft account." App Store: "Free · In‑App Purchases" | Free with a Microsoft account; in-app purchases exist, limits not stated | iOS 17+, web (designer.microsoft.com, bot wall today), Windows | Medium-high. Free phone cutout plus an eraser for cords and tags; AI-generated backgrounds must be disclosed on Etsy | V (App Store listing) | https://apps.apple.com/us/app/microsoft-designer/id6448308247 |
| Apple Photos Clean Up (Apple Intelligence) | Remove distracting objects; also Extend and Reframe | Built in to iOS | Everything; "Usage limits may apply" | iPhone: "iPhone 15 Pro, iPhone 15 Pro Max, or iPhone 16 model or later", iOS 27 | Medium. Free Magic Eraser equivalent for cords, stickers and reflections, if Ricky's iPhone qualifies. "Tap, brush, or circle what you want to remove." | V | https://support.apple.com/guide/iphone/clean-up-extend-and-reframe-photos-xy0grrlxue5w/27/ios/27 |
| PicWish | Background remover, White Background, Product Retouching, Enhance Photo, Remove Object, Bulk Listing Images, API | "Pro $4.99 /mo Billed Annually" ("billed $59.99/yr"); "Max $21.99 /mo" ("billed $263.99/yr"); monthly-billing price not rendered | "Free ... Limited" core downloads; credit features 2 to 15 images once (table) | Web, iOS, Android, Windows ("online or Windows version of PicWish") | High. Cheapest commercial product-photo app read today; Pro lists "100 HD downloads/day" and "450 credits/mo" | V | https://picwish.com/pricing |
| Pixian.AI | Web and API background remover, no signup for free use, megapixel-based pay-as-you-go | "250 $5.00"; "500 $9.50"; "1,000 $18.60" credits; "1 Image = 0.05 to 1 Credits"; "No monthly fees or minimums" | "Free ... Limited use ... 0.25 megapixels resolution ... Low priority processing ... Website only" | Web, API | Medium-high. A 2 MP image is "0.117" credits, so $5 covers about 2,000 full-size cutouts; "Credits do not expire, but you must have made a purchase in the last two years" | V | https://pixian.ai/pricing |
| withoutBG | Open-weights background removal model (Docker or pip), web demo with Smart Brush, Pro Model API, macOS app | API packs: "100 credits 100 €10 €0.10 30 days"; "Every pack is also available as a monthly subscription at the same price." | Open model: "Apache-2.0", "Unlimited processing"; web "5 free images a day, no signup"; API "50 free credits" | Windows via Python or Docker, web, macOS app, API | High for the dashboard. Second local engine beside rembg with a commercial-safe licence; the Pro API is a paid fallback for crystal and glass edges | V | https://withoutbg.com/ and https://withoutbg.com/pro-model-api/pricing |
| Removerized | Open-source in-browser background remover and upscaler, model selector, batch, works offline | Free; "GPL-3.0 license" | Everything | Web (any browser on Windows or iPhone), installable PWA | Medium-high. "All processing happens locally in your browser. No image ever leaves your device." No install, no account | V | https://removerized.yoss.pro/ and https://github.com/yossdotpro/removerized |
| BG-Remover (developersharif/bgremover-app) | Offline Windows desktop background remover with the model embedded in the installer | Free; "MIT license". "BG-Remover (setup) with embeded model 4.0 windows Download (317MB)" | Everything | Windows, Linux | Medium. rembg without Python for Ricky's PC; the page does not name the model, so edge quality is untested | V | https://github.com/developersharif/bgremover-app |
| Bulk image background remover (Chrome extension) | Offline batch background removal inside Chrome | Free (no price on page) | Everything; "2,000 users", "5 ratings" | Chrome extension (Windows) | Medium. "supports batch processing and operates offline"; page warns processing time "can be substantial" | V | https://chromewebstore.google.com/detail/bulk-image-background-rem/gagmnmenidmghmppkbadhgmhnjeaglan |
| AlphaDrop (Chrome extension) | Local AI background remover with manual eraser | Free: "AlphaDrop is free." | Everything; "334 users", "3 ratings" | Chrome extension (Windows) | Medium-low. "Works offline after initial setup"; tiny user base | V | https://chromewebstore.google.com/detail/alphadrop-ai-background-r/hbmfofpedlbllenmpnebikhadgkplobj |
| chaiNNer | Node-based image processing GUI: AI upscaling, batch chains, resize, format | Free; "GPL-3.0 license" | Everything | Windows, Mac, Linux | Medium. One saved chain can upscale, resize to 2000px and flatten onto white; steeper than Upscayl | V | https://github.com/chaiNNer-org/chaiNNer |
| Caesium Image Compressor | Desktop batch compressor and resizer with real-time preview, JPG, PNG, WebP, CLI | Free; "GPL-3.0 license" | Everything | "Windows 10 (build 1809) or later", macOS 12+, Linux | Medium-high. Desktop Squoosh for whole folders under Etsy's 1 MB upload warning | V | https://saerasoft.com/caesium/ and https://github.com/Lymphatus/caesium-image-compressor |
| Bulk Resize Photos | Browser resizer, crop, compress, flip, watermark; local processing | "100% free" | "Unlimited usage"; "No sign-up" | Web; Chrome, Edge and Firefox extensions | Medium. Phone-side resizer in Safari when PowerToys is out of reach | V | https://bulkresizephotos.com/ |
| Movavi Photo Editor | Windows editor: AI background removal and swap, object removal, retouching, colorization | "Lifetime $49.95"; 1-year tab price not rendered | Trial download ("Download for Free"); paid tier lists "No watermark", "No-limits photo export" | Windows, Mac | Medium-low. One-time price under $50 for a GUI cutout plus retouch; Affinity does it free | V | https://www.movavi.com/photo-editor/buynow.html |
| Luminar (Skylum) | AI photo editor, batch, Upscale, HDR, plugin for Lightroom and Photoshop | "Desktop Only ... One-time payment, use app forever ... $99.00" (struck "$417.00", "-77% OFF"); "All Platforms ... $139.00"; "Max ... $159.00"; "*365 days access to AI tools. Subject to fair use policy." | None; "30 days money back guarantee" | Windows, Mac, mobile; web "coming Fall 2026" | Low. Pricier, and the AI tools are time-limited despite the one-time price | V | https://skylum.com/luminar/pricing |
| HitPaw FotorPea (formerly HitPaw Photo Enhancer) | Windows AI upscaler to 8K, background remover, batch, Nano Banana Pro inside | "1 Year License ... $90.39 $112.99"; "1 Month License ... $22.39 $27.99"; "Perpetual License One-Time Price $130.39 $162.99" | "Try 7 days for free, then auto-renew at US$43.19/month" | "Windows 11/10 (64-bit)", Mac | Low. Pricier; Upscayl is free | V | https://www.hitpaw.com/purchase/buy-hitpaw-fotorpea.html |
| Aiarty Image Enhancer | Offline AI upscaler and denoiser, batch, AI eraser | "Standard License Price: $85.00 $59.00" (1 PC, 1 year of updates); "Lifetime License ... $155.00 $109.00" (3 PCs) | "Free Trial" | Windows, Mac | Low. Pricier; Upscayl is free | V | https://www.aiarty.com/ai-image-enhancer/buy.htm |
| CyberLink PhotoDirector 365 | Windows editor: Background Removal, AI backgrounds, AI Image Upscaler, Batch Editor | "PhotoDirector 365 Windows ... $6.67 $5.83/mo" ("15% OFF·Ends November 8th"); billing period not labelled in text | Trial ("Free Download") | Windows; separate Mac version | Low-medium. Cheap subscription, but Paint, Photos and Affinity cover it free | V | https://www.cyberlink.com/products/index_en_US.html |
| ON1 Photo RAW 2027 | Raw editor with Super Select AI masks, layers, retouch, noise reduction | "Photo RAW 2027 ONE-TIME PURCHASE ... $99.99"; "Photo RAW MAX 2027 ... $169.99$149.99"; subscription "$89.99$79.99/year" | "Free Trial" | Mac, Windows | Low. Pricier; raw workflow is overkill for phone photos | V | https://www.on1.com/products/photo-raw/ |
| Adobe Photoshop Elements | One-time Photoshop lite: subject extraction, background swap | Adobe pages returned 403. Mac App Store: "Free · In‑App Purchases"; a reviewer, not Adobe: "The $99 was a reduction in price because it covers 3 years." | None | Windows (U), Mac (V) | Low-medium. Price unverifiable today; a 3-year licence model, not perpetual | U | https://apps.apple.com/us/app/adobe-photoshop-elements-2025/id6714463383?mt=12 |
| Photomator (Apple) | iPhone and Mac editor: AI subject, sky and background selection, Repair, Denoise, Super Resolution, batch | "Free · In‑App Purchases"; "One license for Mac, iPad, iPhone, and Apple Vision Pro."; amounts not in text | Free download; paid licence | iOS 17+, iPad, Mac, Vision Pro | Medium-low. Lightroom-grade phone retouching now owned by Apple; price unknown today | V (listing), U (price) | https://apps.apple.com/us/app/photomator-photo-editor/id1444636541 and https://www.pixelmator.com/photomator/ |
| Remini | iPhone photo enhancer and upscaler | "Free · In‑App Purchases"; "Subscription length: weekly, monthly, yearly"; amounts not in text | Free with ads (reviewers) | iOS 15+, Android, web | Low. Face-first restoration; reviewers report heavy ads and distorted thin details; Upscayl is free | V (listing), U (price) | https://apps.apple.com/us/app/remini-ai-photo-enhancer/id1470373330 |
| Halide Mark III | Pro camera app: Process Zero (no computational processing), RAW, manual controls, Looks | "Halide is a paid app. Try it free for 7 days with an annual membership, or buy it outright with a one-time purchase"; amounts not in text | 7-day trial | iOS 18+, iPad | Low-medium. Only if the stock camera over-sharpens brass and glass; "Editors' Choice" | V (listing), U (price) | https://apps.apple.com/us/app/halide-mark-iii-pro-camera/id885697368 |
| Google Gemini app (Nano Banana 2) | AI image generation and editing: "Generate and edit photos with Nano Banana 2" | App "Free · In‑App Purchases"; "Google AI Plus $4.99/mo"; "Google AI Pro $19.99/mo" | Free tier in the app | iOS 18.2+, Android, web | Low. AI backgrounds; Etsy still needs one unedited photo and a disclosure | V | https://apps.apple.com/us/app/google-gemini/id6477489729 and https://one.google.com/about/google-ai-plans/ |
| Icons8 Background Remover and Smart Upscaler | Web batch background removal (up to 500 images) and upscaler | Remover: "$0.20 per image" prepaid; "Up to 100 images per month ... $9 $13" (Monthly / Yearly -20% toggle); "Unlimited ... $99 $120". Upscaler: "prepaid package starting at $10 for 50 images"; "100 images/month for $9" | "Try it with 3 demo removes." | Web; Mac app (GoProd) | Medium-low. $0.20 a hero shot is cheap; images are stored on their servers for history | V | https://icons8.com/bgremover/pricing and https://icons8.com/upscaler |
| Pippit (CapCut) | AI product photo and video studio with agents | "STARTER USD101 USD168 /Yearly"; "PLUS USD246 USD410 /Yearly"; "PRO USD2,196 USD3,660 /Yearly" | "FREE ... Get free daily credits"; "Remove watermark" is listed under paid tiers | Web | Low. AI scenes, same verdict as Pebblely and Flair | V | https://www.pippit.ai/pricing |
| PhotoScape X | Free all-in-one editor: "Cut Out: Remove the background from an image. (Magic Eraser, Lasso tool, Brush tool)", Batch, batch rename and resize | "Free · In‑App Purchases" (Pro) | Free version | Mac (V); Windows site x.photoscape.org unreachable today (U) | Medium-low. Free batch resize plus cutout in one app; Windows build unverified | V (Mac listing), U (Windows) | https://apps.apple.com/us/app/photoscape-x-photo-editor/id929507092?mt=12 |
| FastStone Photo Resizer | Windows batch convert, rename, resize, crop, watermark | "Free for personal and educational use"; "License required for commercial use"; Resizer's commercial price not in text (Image Viewer "$34.95 one-time") | Personal use only | Windows | Low. Same licence catch as XnConvert and IrfanView | V (licence), U (price) | https://www.faststone.org/FSResizerDetail.htm and https://www.faststone.org/order.htm |
| darktable | Open-source raw developer and library | "darktable is released under the GPL 3.0" | Everything | Windows, Mac, Linux | Low. Raw workflow for phone HEIC is overkill | V | https://www.darktable.org/ |
| Alpha Background Remover (Shopify app) | Local, in-browser background remover inside Shopify admin, syncs to product media | "Free" | Everything | Shopify app | Medium, later. "processing runs entirely in the browser"; "Launched July 15, 2026"; "No reviews yet" | V | https://apps.shopify.com/alpha-background-remover |
| Pxl ‑ Photo Background Remover (Shopify app) | One-click product background removal in Shopify | "Free to install. Additional charges may apply."; "5 free credits ; $5 for 10 credits ; $10 for 30 credits ; $25 for 100 credits ; $50 for 250 credits" | 5 free credits | Shopify app | Medium-low, later. Rated 5.0 from 35 reviews; one review notes trouble with "black components against dark shadows" | V | https://apps.shopify.com/background-image-remover |
| VF Image Resizer+ (Shopify app) | Bulk resize, crop, compress, background removal, format conversion, AI alt text | "Basic plan $12.99 / month"; "Professional plan $26.99 / month" | "Free plan ... 100 welcome credits" | Shopify app | Medium, later. Free plan covers a small catalog; 467 reviews | V | https://apps.shopify.com/image-batch-editor |
| Photoroom AI Listing Assistant (Shopify app) | Photoroom's bulk catalog editor inside Shopify | "Photoroom Pro $12.99 / month or $89.99/year"; "Photoroom Max $34.99 / month or $250/year"; "Photoroom Ultra $99 / month or $990/year" | "Free plan available" | Shopify app | Low, later. Same prices as Photoroom on the lane list | V | https://apps.shopify.com/photoroom-production |

## 2. Notes per tool

### Microsoft Paint (Windows 11). V
- microsoft.com/en-us/windows/paint lists "Image Creator", "Background Removal" and "Layers" as the headline tools. Quote: "This powerful editing tool uses AI to help you isolate a subject and remove the background with just one click."
- The Microsoft Store listing (apps.microsoft.com/detail/9pcfs5b6t72h) renders only through JavaScript; the fetcher got the title "Paint - Free download and install on Windows" and nothing else. Image Creator carries footnotes "1 2" on the product page (account and region limits), not read.
- Fit: free, installed, no account. Paint saves the cutout as a layer; export as PNG then flatten onto white or a room background before Etsy, because Etsy renders transparency black (lane finding).

### Microsoft Designer. V (App Store listing)
- "Microsoft Designer is available for free with a Microsoft account. Your Microsoft account provides 5 GB of free cloud storage".
- Tools listed: "Generative erase: Erase distractions to make objects you don't want in your image disappear." "Remove background: Say bye-bye to bad backgrounds. Easily remove unwanted image backgrounds in one step." "Blur background".
- "Free · In‑App Purchases", "Requires iOS 17.0 or later." The in-app purchases are not itemized in the text. Reviews praise the free tier ("I have been using Designer for free for a few months").
- The web app (designer.microsoft.com) returned an empty page and a 292-character stub today (bot wall). create.microsoft.com redirected to a generic Microsoft 365 "Create" page.
- Gotcha: generated or AI-swapped backgrounds count as AI edits under Etsy's listing-photo rules found by the lane; keep one unedited real photo per listing.

### Apple Photos Clean Up. V
- "With Apple Intelligence, you can remove distracting objects, extend a photo beyond its original frame, and adjust its perspective."
- Steps: "Tap Tools, then tap Clean Up." "Tap, brush, or circle what you want to remove." "Some items may be highlighted automatically so you can quickly tap to remove them." Processing modes "Auto, Fast, or High Quality".
- Hardware gate: "available on an Apple Intelligence-enabled iPhone 15 Pro, iPhone 15 Pro Max, or iPhone 16 model or later." The parent guide adds that server-side features "are subject to daily usage limits" and "Expanded access to such features will be available for a fee in the future."
- Fit: the lane listed only "lift subject". Clean Up is the free equivalent of Google Photos Magic Eraser for cords, price stickers and lamp reflections, if Ricky's phone qualifies.

### PicWish. V
- Pricing rendered only after a 15-second JavaScript wait: "Pro $4.99 /mo Billed Annually", "billed $59.99/yr"; "Max $21.99 /mo", "billed $263.99/yr". A monthly-billing toggle exists but its prices did not render.
- Limits table: Free "Limited" core downloads; Pro "450 credits/mo" and "100 images/day" free core downloads; Max "2,000 credits/mo" and "15,000 images/month". Core features at no credit cost on paid plans: Remove Background, Enhance Photo, Remove Object, White Background. Credit features: Product Retouching, Product Listing, Bulk Listing Images, Product & Portrait Background, Ghost Mannequin (fashion), Flat Lay.
- Platforms from the FAQ: "unlimited access to all features on both iOS and Android apps"; refunds for "our online or Windows version of PicWish". iOS listing "PicWish: AI Photo Editor" by Wangxu Technology, iOS 13+ (iTunes lookup).
- Fit: a one-of-one shop lists a few pieces a day; the free tier's "Limited" HD downloads may be enough to test. Pro at $4.99 a month billed yearly is the cheapest commercial phone-plus-PC cutout read in this sweep. Commercial licence terms were not read; check before paying.

### Pixian.AI. V
- "Pixian.AI offers both a Web App and an API. While the Web App offers some free usage, the API requires buying a credit pack."
- Free: "0.25 megapixels resolution", "Low priority processing", "Website only". 0.25 MP is 500x500, useless for Etsy's 2000px guidance; the free tier is a quality preview only.
- Paid: 250 credits $5.00, 500 $9.50, 1,000 $18.60, 2,500 $45.00, 5,000 $85.00. Per-image credits scale with megapixels: 1 MP 0.079, 2 MP 0.117, 4 MP 0.194, 12 MP 0.501, 25 MP 1.000. A 12 MP iPhone photo costs about $0.01 at the $5 pack.
- "Credits do not expire, but you must have made a purchase in the last two years to use them." Company statement: "We see AI commoditizing rapidly".
- Fit: the cheapest HD pay-per-use cutout found, with a reputation for fine edges (unverified here). Good backup when local engines miss on cut crystal.

### withoutBG. V
- Home: "The Pro Model API for hair, fur, and complex edges, managed in Frankfurt. Pro Model Self-Host ... Or self-host the free Apache-2.0 open-weight model." "Open Model quick start: run with Docker using docker run -p 80:80 withoutbg/app:latest, or install via Python with pip install withoutbg. Apache-2.0 license."
- Web demo: "5 free images a day, no signup", with Keep and Remove brush strokes to fix a cutout ("A rough stroke is enough; the edges are refined again").
- GitHub SDK: "run open weights on your machine (private, offline, unlimited) or call the Cloud API (sharper edges on hair and fur, no local GPU)". "First local run downloads ~1.5 GB of weights from Hugging Face (once; the BiRefNet branch is fetched the first time an image needs it)." Repo also carries a LICENSE-DINOv3 file; check that third-party licence before shipping weights inside a product (local use is fine).
- API: 100 credits €10 (30 days), 500 €40, 1K €70 (90 days), up to 10K €500; "New accounts get 50 free credits, valid 30 days. No card required." Self-hosted Pro Model is "€3,600 + VAT, one-off flat fee" (enterprise, skip).
- Fit: a second engine for the dashboard pipeline with the same CLI shape as rembg, and a human-correctable web fallback for glass.

### Removerized. V
- Web app: "Remove backgrounds from any image with on-device AI. No uploads, no server, fully offline-capable." "Batch Processing". "Upscaler". "Free & open source".
- GitHub: "runs entirely in the browser using ONNX Runtime Web", "Multiple AI Models", "GPL-3.0 license", PWA with offline fallback.
- Fit: works on the iPhone in Safari and on the PC in Chrome with nothing installed. Speed and quality depend on the device and the model picked; the lane's test protocol (one lamp, one decanter, one framed print) applies.

### BG-Remover (developersharif/bgremover-app). V
- "Free Offline Image Background Remover for Linux,Windows." Downloads: "BG-Remover (setup) with embeded model 4.0 windows Download (317MB)", "3.0 ... (168MB)". "MIT license".
- The README does not name the segmentation model; a 317 MB installer suggests a mid-size model, not BiRefNet-HR. Treat it as a convenience wrapper, not a quality upgrade over rembg.

### Chrome Web Store extensions. V
- "Bulk image background remover" (2,000 users, 5 ratings): "supports batch processing and operates offline, ensuring absolute data security by not uploading any information to servers." Warning on the page: processing time "can be substantial, so please be patient".
- "AlphaDrop - AI Background Remover" (334 users, 3 ratings): "runs completely in your browser. No uploads to external servers, no subscriptions, no limits". "AlphaDrop is free."
- "Background Remover Pro" (43 users): background and watermark removal, "100% local processing", "No usage limits", "Works offline". Removing other people's watermarks is a rights problem; use it on Ricky's own photos only.
- All three have tiny user bases and no stated maintainer. Fine as free experiments, not as the pipeline.

### chaiNNer. V
- "A node-based image processing GUI aimed at making chaining image processing tasks easy and customizable. Born as an AI upscaling application". "cross-platform, meaning you can run it on Windows, MacOS, and Linux." "You don't even need to have Python installed". "GPL-3.0 license". 6.2k stars.
- Fit: build one chain (load folder, upscale 2x, resize longest side 2000, flatten onto white, save JPEG) and run it on every shoot. More setup than Upscayl plus PowerToys, less than ImageMagick scripting.

### Caesium Image Compressor. V
- "Compress your pictures up to 90% without visible quality loss". "Caesium is a free software developed for simplicity and effectiveness." Versions: "v2.8.5", "Windows 10 (build 1809) or later", installer and portable, "macOS (12+)". GitHub: "GPL-3.0 license". Also a command-line tool and an online compressor.
- Fit: Squoosh handles one image at a time in the browser; Caesium does a folder with a preview. Solves Etsy's 1 MB warning for a whole shoot.

### Bulk Resize Photos. V
- "Unlimited Free Image Resizing", "100% free", "Unlimited usage", "No sign-up", and a lock icon labelled private with no uploading. Browser extensions for Chrome, Edge and Firefox. Footer has a "Specified Commercial Transactions" page (Japanese operator disclosure).
- Fit: a resizer that runs on the iPhone in Safari when a listing is being done from the phone; PowerToys already covers the PC.

### Movavi Photo Editor. V
- Buy page: tabs "1 year" and "Lifetime"; "Photo Editor $49.95" under Lifetime; the 1-year price did not render. Paid features listed: "No watermark", "No-limits photo export", "Background replacement", "Object removal", "Portrait retouching". Product page: "AI BACKGROUND REMOVAL", "Download for Free" (trial).
- Fit: the cheapest one-time Windows GUI with AI cutout and object removal, but Affinity (free for individuals, on the lane list) and Paint make it unnecessary.

### Luminar (Skylum). V
- skylum.com/luminar-neo redirects to skylum.com/luminar. Pricing page tiers: "Desktop Only ... $99.00" (struck "$417.00", "-77% OFF"), "All Platforms ... $139.00", "Max ... $159.00", each "One-time payment, use apps forever". Footnote on every tier: "*365 days access to AI tools. Subject to fair use policy." Desktop Only is a "Perpetual license for Luminar for Desktop on 2 devices (macOS&Windows)".
- The product page: "Batch processing", "With Pro Tools, you can sharpen, denoise, upscale, and merge exposures". "Stunning results, now with up to 77% OFF" means the prices read are sale prices.
- Gotcha: the one-time price does not cover the AI tools past a year. Pricier and not needed.

### HitPaw FotorPea. V
- "HitPaw FotorPea(formerly HitPaw Photo Enhancer)". Windows buy page: "1 Year License ... $90.39 $112.99", "1 Month License ... $22.39 $27.99", "Perpetual License One-Time Price $130.39 $162.99", "(Tax Excl.)". Trial: "Try 7 days for free, then auto-renew at US$43.19/month (20% off)." The trial auto-renews at a higher price than the listed plans; cancel before day 7. Features: upscale to 8K, "AI background remover", "Enhance photos in bulk without limits", "Nano Banana Pro available".
- Fit: pricier; Upscayl is free.

### Aiarty Image Enhancer. V
- Product page: "Lifetime License. Risk-Free Refund.", "Processing runs offline on your device". Buy page: "Standard License Price: $85.00 $59.00 ... Licensed to 1 PC. Enjoy free software update for 1 year." "Lifetime License One-time Payment, Lifetime Upgrades Price: $155.00 $109.00 ... Licensed to 3 PCs." Bonus gift "AI Image Matting 1-Year License ... Remove, change and refine image background." The first buy URL guessed (buy-now.htm) was a 404; buy.htm worked.
- Fit: pricier; Upscayl is free.

### CyberLink PhotoDirector 365. V
- The store URL redirected to the products index, which lists "PhotoDirector 365 Windows Photo editing and retouching with generative AI. $6.67 $5.83/mo" with "15% OFF·Ends November 8th". Which figure is monthly versus annual billing is not labelled in the text. Features page: "Background Removal and Effects", "AI Image Upscaler", "Batch Editor".
- Fit: cheap, but the free stack covers it.

### ON1 Photo RAW 2027. V
- "Photo RAW 2027 ONE-TIME PURCHASE ... $99.99 ... Install on 2 computers"; "Photo RAW MAX 2027 ... $169.99$149.99"; subscription "$89.99$79.99/year". "Click on a sky, a subject, or a background and Super Select AI isolates it precisely." Mac and Windows, "30-day money-back guarantee".
- Fit: pricier, photographer-grade raw tool.

### Adobe Photoshop Elements. U
- adobe.com/products/photoshop-elements.html and helpx.adobe.com returned HTTP 403 today. The Mac App Store lists "Adobe Photoshop Elements 2025", "Free · In‑App Purchases", "Requires macOS 13.0 or later". Reviews describe a three-year licence: "The $99 was a reduction in price because it covers 3 years." Another says Adobe's site already sells "Adobe Photoshop Elements 2026". Windows price unverifiable today.

### Photomator (Apple). V listing, U price
- App Store: "Free · In‑App Purchases", "Requires iOS 17.0 or later", "iPhone, iPad, Mac". Features: "Quickly make precise subject, sky, and background selections in photos using AI", "remove unwanted objects", "intelligently upscale photos with Super Resolution", batch editing in reviews. pixelmator.com: "One license for Mac, iPad, iPhone, and Apple Vision Pro." Footer: "Copyright © 2025 Apple Inc." Price amounts not in either page's text.

### Remini, Halide Mark III, Google Gemini. V listings
- Remini: "Turn your old, blurry photos into gorgeous, clear HD in just ONE TAP." "Subscription length: weekly, monthly, yearly." Reviews: "quite a few ads", "struggles to pick up on thin materials like string, yarn". Low fit for lamps and glass.
- Halide Mark III: "Zero AI, Natural Photos, RAW". "Try it free for 7 days with an annual membership, or buy it outright with a one-time purchase". "Requires iOS 18.0 or later." halide.cam shows no price. Only worth a trial if the stock camera over-processes reflective pieces.
- Gemini: "Generate and edit photos with Nano Banana 2: Apply camera and lighting controls, create mockups by blending multiple images". Google AI Plus "$4.99/mo", AI Pro "$19.99/mo", Ultra "From $99.99/mo". Etsy still requires a real, unedited photo; AI backgrounds need disclosure (lane finding).

### Icons8 Background Remover and Smart Upscaler. V
- Remover: "You can remove backgrounds from 3 images for free." "Upload up to 500 images at once!" Pricing: "Prepaid package ... $0.20 per image"; "Limited subscription ... Up to 100 images per month ... $9 $13"; "Unlimited subscription ... $99 $120" (the two figures sit under a "Monthly / Yearly (-20%)" toggle; which is which is not labelled in text). "We securely store uploaded images to let you view your history".
- Upscaler: "prepaid package starting at $10 for 50 images", "limited subscription: 100 images/month for $9", "unlimited subscription: $99/month"; "Images can be upscaled up to 7680x7680px". Free use adds a watermark ("How can I remove the watermarks?").

### Pippit (CapCut). V
- pippit.capcut.com/pricing redirects to pippit.ai/pricing. "Free to use, upgrade anytime." "FREE ... Get free daily credits". Paid: "STARTER USD101 USD168 /Yearly", "PLUS USD246 USD410 /Yearly", "PRO USD2,196 USD3,660 /Yearly", each "Auto renews, cancel anytime." Paid tiers list "Remove watermark", so free output is watermarked. Monthly prices sit under a toggle that did not render.
- Fit: AI scene generator, same verdict as Pebblely and Flair on the lane list.

### PhotoScape X. V (Mac), U (Windows)
- Mac App Store: "Free · In‑App Purchases", "All-in-One: Photo Editor, Batch Editor, Photo Viewer, Cut Out, Collage Maker", "Cut Out: Remove the background from an image. (Magic Eraser, Lasso tool, Brush tool)", "Batch: Batch edit multiple photos", "Batch Rename, Batch Resize". A reviewer: "I purchased the Pro version after testing the free one. Basically, for the cost of 1 month of an Adobe subscription, I own this software."
- x.photoscape.org failed on DNS (http) and connection reset (https), so the Windows build and Pro price are unverified today.

### FastStone Photo Resizer. V licence, U price
- "Free for personal and educational use"; order page: "License required for commercial use", "One-time purchase with a lifetime license." The table shows "FastStone Image Viewer ... $34.95 one-time"; the Photo Resizer row was not in the text read. Same shop-use catch as XnConvert and IrfanView on the lane list.

### darktable. V
- "darktable is released under the GPL 3.0". Raw developer with library. Low fit for phone JPEG and HEIC.

### Shopify apps (for the later store). V
- Alpha Background Remover: "Free", "Using client-side WebAssembly AI technology, processing runs entirely in the browser", "Launched July 15, 2026", "No reviews yet", developer Deepgraphite, Sofia.
- Pxl ‑ Photo Background Remover: "Free to install. Additional charges may apply." Credits: 5 free, "$5 for 10 credits", "$10 for 30 credits", "$25 for 100 credits", "$50 for 250 credits". 5.0 from 35 reviews; launched April 3, 2020.
- VF Image Resizer+: "Free plan ... 100 welcome credits ... Background removal, borders & watermarks"; "Basic plan $12.99 / month ... 2,000 credits / month"; "Professional plan $26.99 / month ... 6,000 credits / month". 467 reviews.
- Photoroom AI Listing Assistant: "Free"; "Photoroom Pro $12.99 / month or $89.99/year and save 42%"; Max "$34.99 / month or $250/year"; Ultra "$99 / month or $990/year". 36 reviews.
- Also seen on the results page, not opened: AIBrush, REMOVEit, Scurix, Pix, "Cutout bulk background remover" (Cutout.pro's app), RoMagic, PeakPulse, Retouched.ai, ImageMagik, LitePix, "AI Background Remove&Generate" (slug `bria`, BRIA's commercial app; BRIA's open RMBG weights stay non-commercial per the earlier decision), Bulk Background Remover.

### Open-source engines, one line each. V
- BiRefNet (ZhengPeng7/BiRefNet): "MIT license"; 2025 releases "BiRefNet_HR ... trained on images in 2048x2048", "BiRefNet_dynamic ... 256x256 to 2304x2304", "BiRefNet_HR-matting". Hugging Face model card confirms "License: mit". rembg's `birefnet-general` predates these; test the HR weights on cut crystal before the dashboard build. The Hugging Face demo Space (ZhengPeng7/BiRefNet_demo) is JavaScript-only and did not render (U).
- nadermx/backgroundremover: "MIT license", CLI for images and video, Windows install instructions with CPU or CUDA torch. 8.2k stars. Older model family; rembg already covers this.
- T8RIN/ImageToolbox: 15.5k stars on the topic page, Android only. Not for Ricky's iPhone; noted for completeness.
- imgly/background-removal-js (7.4k stars) and Bria-AI/RMBG-2.0 (350 stars) appear on the topic page; the first is a developer library, the second is excluded by the non-commercial licence decision.

### Etsy Seller app. V listing
- "Add and edit listing videos and photos straight from your phone." No cutout or background tool is described in the App Store text. Reviews complain of photo-upload bugs. Nothing new for this lane.

## 3. Recommendation for Hollie

Free, today:
1. Open Paint on the PC and run Background Removal on one lamp photo. Compare the edge with Windows Photos and rembg. Costs nothing; it is already installed.
2. Install Microsoft Designer on the iPhone (free with a Microsoft account). Use Remove background and Generative erase for quick social cutouts and cord removal.
3. Check the iPhone model. On a 15 Pro or any 16 or later, use Photos > Tools > Clean Up for stickers, cords and reflections. Otherwise Google Photos Magic Eraser (lane list) stays the phone eraser.
4. Bookmark removerized.yoss.pro on both devices. It is a free, local, batch cutout plus upscaler with nothing to install.
5. Install Caesium on the PC. Compress each shoot's folder under 1 MB per file before Etsy upload.
6. For the dashboard pipeline, add withoutBG's Apache-2.0 open model as the second engine next to rembg BiRefNet, and test BiRefNet_HR weights on cut crystal. Keep BRIA RMBG out.

Pay only once it earns it:
- PicWish Pro, "$4.99 /mo Billed Annually" ($59.99 a year), if Ricky wants one phone-and-PC app with white-background, product retouch and bulk listing images. It is cheaper than Pixelcut Pro ($8 a month yearly) and Photoroom Pro ($7.50 a month yearly) on the lane list. Read its commercial-use terms first; they were not read today.
- Pixian.AI $5.00 for 250 credits as a pay-per-use HD fallback when every local engine fails on glass. About $0.01 per 12 MP photo; credits keep for two years.
- Icons8 prepaid at $0.20 per image is the other cheap fallback, but it stores the uploads.

Skip, and why:
- Luminar, HitPaw FotorPea, Aiarty, ON1, CyberLink PhotoDirector, Movavi: paid Windows editors whose cutout, retouch and upscale jobs Paint, Windows Photos, Affinity (free for individuals) and Upscayl already do. Luminar's one-time price hides a 365-day AI limit.
- Pippit, Gemini Nano Banana: AI scene generators. Etsy requires an unedited real photo and disclosure of AI edits; buyers of vintage want the real object.
- Remini: face-first, ad-heavy, weak on thin details like chandelier chains.
- Photoshop Elements: price unverifiable today and sold as a three-year licence.
- Shopify apps: nothing until the Shopify store exists; then Alpha Background Remover (free, local) or VF Image Resizer+ free plan.

## 4. Defunct, renamed, acquired or corrected, with evidence

- Luminar Neo is now "Luminar". skylum.com/luminar-neo redirects to skylum.com/luminar; the product and pricing pages name "Luminar for Desktop", "Luminar Mobile", "Luminar Web" and "Luminar Prime" and contain zero occurrences of "Neo". The lane said Luminar could not be verified; both pages loaded today. V.
- HitPaw Photo Enhancer is now HitPaw FotorPea: "HitPaw FotorPea(formerly HitPaw Photo Enhancer)". hitpaw.com/photo-enhancer.html redirects to fotorpea-photo-enhancer.html. V.
- Mokker AI is soona's AI Studio, confirming the lane's "migrating brand": "Mokker AI is now soona's AI Studio. Get started with a new account at soona.co. Mokker customers can get account transition help at hey@soona.co." The old pricing ($13, $29, Unlimited "$83.25") still renders below the banner. V.
- Pixelmator and Photomator belong to Apple: pixelmator.com footer "Corporate Address: Apple Inc., One Apple Park Way, Cupertino" and "Copyright © 2025 Apple Inc. All rights reserved."; App Store seller "Apple Inc." V.
- Pippit moved domains: pippit.capcut.com redirects to pippit.ai. V.
- Cutout.pro is alive and priced; the lane marked it U after four 404s. Pricing is at cutout.pro/image-pricing: "Free Account ... Free previews forever ... 5 free credits"; subscription "80 credits/month $5.00", "170 credits/month $9.90", "300 credits/month $16.90", "Roll over up to 5× your monthly credit budget"; "Pay as you go ... USD $0.130 / credit", "30credits $4.99". "1 IMAGE = 1 CREDIT FOR IMAGE BACKGROUND REMOVAL AND IMAGE RETOUCH". The home page now also sells Nano Banana generation. V. Fit stays low-medium: $5 a month for 80 cutouts is fair, but Pixian is cheaper per image and the local engines are free.
- Clipdrop: still live under Jasper ("The Jasper API lets you embed best-in-class AI image models", footer "Jasper Free Trial"). No change. V.
- Pebblely: live, pricing link present. No change. V.
- Halide is now "Halide Mark III" (App Store title); not on the lane list, noted because older roundups say "Mark II". V.
- Google Photos Magic Editor: no evidence either way. The Google Photos blog index loaded but showed six unrelated posts (digital wardrobe, Halloween, Video Remix). U.
- remove.bg, Topaz, Affinity, Magnific and the other listed renames were not re-checked (another agent's job).

## 5. Gaps and pages that would not load

- WebSearch budget exhausted before this agent's first query; no search engine was used. Leads came from category pages only, so tools that appear in 2026 blog roundups but not on GitHub, Shopify, Chrome Web Store or App Store pages may still be missing.
- designer.microsoft.com and designer.microsoft.com/background-remover: empty or 292-character stub (bot wall). Designer facts come from the iOS App Store listing.
- apps.microsoft.com Paint listing: JavaScript-only, title only, even with a 9-second wait. Paint facts come from microsoft.com/en-us/windows/paint.
- support.microsoft.com Paint article (guessed URL): error page. blogs.windows.com Paint post (guessed URL): 404.
- adobe.com/products/photoshop-elements.html and helpx.adobe.com FAQ: HTTP 403. firefly.adobe.com: "Please enable JavaScript". Photoshop Elements Windows price and Firefly plans are U.
- producthunt.com search: HTTP 403.
- x.photoscape.org: DNS failure on http, connection reset on https. PhotoScape X Windows build U.
- huggingface.co/spaces/ZhengPeng7/BiRefNet_demo: JavaScript-only, 434 characters.
- PicWish monthly-billing prices, Pippit monthly prices, Vmake Plus and Pro prices, Movavi 1-year price, Icons8 toggle labels, CyberLink billing-period labels: not in the rendered text layer.
- App Store pages (Remini, Halide, Photomator, Microsoft Designer, PicWish) list "In-App Purchases Yes" without amounts.
- FastStone Photo Resizer commercial price row not in the text read.
- vmake.ai/pricing loaded (free "Get 20 credits daily", outputs "1080p, with watermark" on free, "Commercial Use" on paid) but no dollar amounts rendered; left out of the table.
- Etsy and eBay help pages were not touched (lane covered image specs and AI rules).
- Hardware (lightbox, phone mount, turntable): not researched; software first, per the brief.

## 6. Sources (every URL fetched today, 2026-11-07)

Loaded:
- https://www.microsoft.com/en-us/windows/paint
- https://apps.microsoft.com/detail/9pcfs5b6t72h (title only, JavaScript)
- https://apps.microsoft.com/detail/9pcfs5b6t72h?hl=en-us&gl=US (title only, JavaScript)
- https://apps.apple.com/us/app/microsoft-designer/id6448308247
- https://m365.cloud.microsoft/create (redirect from https://create.microsoft.com/en-us/features/ai-background-remover)
- https://support.apple.com/guide/iphone/edit-photos-and-videos-iphb08064d57/ios
- https://support.apple.com/guide/iphone/clean-up-extend-and-reframe-photos-xy0grrlxue5w/27/ios/27
- https://picwish.com/pricing
- https://pixian.ai/pricing
- https://withoutbg.com/
- https://withoutbg.com/pro-model-api/pricing (redirect from https://withoutbg.com/pricing)
- https://github.com/withoutbg/withoutbg-python
- https://removerized.yoss.pro/ (lands on /removerized)
- https://github.com/yossdotpro/removerized
- https://github.com/developersharif/bgremover-app
- https://github.com/topics/background-removal
- https://github.com/ZhengPeng7/BiRefNet
- https://huggingface.co/ZhengPeng7/BiRefNet
- https://github.com/nadermx/backgroundremover
- https://github.com/Akascape/Rembg-Fuse
- https://github.com/chaiNNer-org/chaiNNer
- https://saerasoft.com/caesium/
- https://github.com/Lymphatus/caesium-image-compressor
- https://bulkresizephotos.com/ (lands on /en)
- https://www.faststone.org/FSResizerDetail.htm
- https://www.faststone.org/order.htm
- https://www.darktable.org/
- https://chromewebstore.google.com/search/background%20remover
- https://chromewebstore.google.com/detail/bulk-image-background-rem/gagmnmenidmghmppkbadhgmhnjeaglan
- https://chromewebstore.google.com/detail/alphadrop-ai-background-r/hbmfofpedlbllenmpnebikhadgkplobj
- https://chromewebstore.google.com/detail/background-remover-pro/mpfgicnhdllnaffdfnedbbbkceaijplc
- https://apps.shopify.com/search?q=background+remover
- https://apps.shopify.com/alpha-background-remover
- https://apps.shopify.com/background-image-remover
- https://apps.shopify.com/image-batch-editor
- https://apps.shopify.com/photoroom-production
- https://www.movavi.com/photo-editor/
- https://www.movavi.com/photo-editor/buynow.html
- https://skylum.com/luminar (redirect from https://skylum.com/luminar-neo)
- https://skylum.com/luminar/pricing
- https://www.hitpaw.com/fotorpea-photo-enhancer.html (redirect from https://www.hitpaw.com/photo-enhancer.html)
- https://www.hitpaw.com/purchase/buy-hitpaw-fotorpea.html
- https://www.aiarty.com/ai-image-enhancer/
- https://www.aiarty.com/ai-image-enhancer/buy.htm
- https://www.cyberlink.com/products/photodirector-photo-editing-software-365/features_en_US.html
- https://www.cyberlink.com/products/index_en_US.html (redirect from https://www.cyberlink.com/store/photodirector-365/buy_en_US.html)
- https://www.on1.com/products/photo-raw/
- https://apps.apple.com/us/app/adobe-photoshop-elements-2025/id6714463383?mt=12
- https://apps.apple.com/us/app/photomator-photo-editor/id1444636541
- https://www.pixelmator.com/photomator/
- https://apps.apple.com/us/app/remini-ai-photo-enhancer/id1470373330
- https://app.remini.ai/ (redirect from https://remini.ai/)
- https://apps.apple.com/us/app/halide-mark-iii-pro-camera/id885697368
- https://halide.cam/
- https://apps.apple.com/us/app/google-gemini/id6477489729
- https://one.google.com/about/google-ai-plans/
- https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1534619962
- https://icons8.com/bgremover
- https://icons8.com/bgremover/pricing
- https://icons8.com/upscaler
- https://www.pippit.ai/pricing (redirect from https://pippit.capcut.com/pricing)
- https://vmake.ai/pricing
- https://apps.apple.com/us/app/photoscape-x-photo-editor/id929507092?mt=12
- https://www.cutout.pro/
- https://www.cutout.pro/image-pricing
- https://pebblely.com/
- https://clipdrop.co/
- https://mokker.ai/
- https://blog.google/products-and-platforms/products/photos/ (redirect from https://blog.google/products/photos/)
- https://itunes.apple.com/search (vendor lookup API; queries: remini, photomator, picwish, pippit, vmake, halide, microsoft designer, blend product photo, background eraser, etsy seller, photo cutout background remover, Pixelmator, Photoshop Elements)

Failed or blocked:
- https://designer.microsoft.com/ (empty page)
- https://designer.microsoft.com/background-remover (292-character stub)
- https://support.microsoft.com/en-us/windows/remove-background-in-paint-c93b4de5-8e2d-4bb3-9f7c-7d6b6d8b7f8c (guessed; error page)
- https://blogs.windows.com/windows-insider/2023/09/07/background-removal-now-available-in-paint-for-windows-insiders/ (guessed; 404)
- https://www.adobe.com/products/photoshop-elements.html (403)
- https://helpx.adobe.com/photoshop-elements/kb/photoshop-elements-faq.html (403)
- https://firefly.adobe.com/ (JavaScript wall)
- https://www.producthunt.com/search?q=background%20remover (403)
- https://huggingface.co/spaces/ZhengPeng7/BiRefNet_demo (JavaScript only)
- http://x.photoscape.org/ (DNS failure) and https://x.photoscape.org/ (connection reset)
- https://www.aiarty.com/ai-image-enhancer/buy-now.htm (404; buy.htm worked)
