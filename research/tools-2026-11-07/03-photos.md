# Lane 03: Product photo apps for Holliewood and Vine (shoot, cut out, retouch, upscale, resize, batch)

Date 2026-11-07. Author: research subagent. Question: Which apps and programs make shooting, cutting out, retouching, upscaling, resizing and batch-processing product photos easier for one-of-one vintage pieces, on Windows and iPhone, and what do they cost? Legend: V = vendor page read today (2026-11-07); U = unverified (snippet, memory, or the page would not load).

Method note. WebFetch and crawl4ai were unavailable. Pages were read with the session's headless-Chromium fetch script (curl fallback). The shared WebSearch budget was exhausted before this lane's first search, so every URL below is a vendor URL typed from knowledge, an App Store URL returned by Apple's own iTunes lookup API, or a link found inside a page already read. 100 fetches, 89 loaded, 11 failed (listed in section 4). Photoroom's dollar prices were not rendered in the page text; they were taken from the same page's embedded structured data (JSON-LD offers) and noscript spans, fetched today.

## 0. Bottom line

- The free stack already covers 90 percent of the job on Ricky's two devices. Windows 11 Photos removes or replaces a background locally and has Generative Erase (V). Snapseed on iPhone is free with no ads, subscriptions or watermarks and has one-tap subject masking, healing and batch edits (V). Apple Photos lifts a subject with touch-and-hold (V). Upscayl upscales for free on Windows (V, AGPL-3.0). PowerToys Image Resizer batch-resizes from a right-click (V). Affinity is now free for individuals on Windows (V). Squoosh compresses in the browser, locally (V).
- rembg gotcha: the README now says bria-rmbg is "The default" model (V). Ricky's earlier decision was never BRIA (non-commercial licence). Every rembg call must pass `-m birefnet-general` or the licence decision is silently broken.
- Etsy gotcha: "transparent .png files are not supported. If a file contains transparency, the transparent parts of the image will appear black on Etsy." (V). Every cutout must be flattened onto a solid or photo background before upload. Etsy also requires "at least one unedited photo of the actual item against a real background" and allows AI edits elsewhere, with a best practice to note AI edits in the description (V). Etsy recommends 2000px or more on both sides and warns files over 1MB may not finish uploading (V).
- eBay: minimum 500 x 500, recommends about 1600 x 1600, up to 24 pictures, 12MB each, white background not required ("for shiny or reflective items like a piece of jewelry, a darker background may work better"). eBay's own listing tool offers White or AI-Generated backgrounds, so AI backgrounds are allowed on eBay by eBay's own tool (V). Shopify: 2048 x 2048 displays best for square, up to 5000 x 5000 or 25MP, under 20MB; the admin file editor can "Replace the background of an image with a color" (V).
- Phone cutout apps: Pixelcut Pro is $10 per month monthly or $8 per month billed yearly with "Commercial license" and "1,000 Batch Exports Monthly" (V). Photoroom Pro is $12.99 per month monthly or $89.99 per year ($7.50 per month billed yearly), 8,000 AI credits and 1,000 exports a month (V, from page source). Both have free tiers; both are iOS, Android and web. Trial both free; pay for one only after listings pass about 20 a month.
- Pay-per-image cutout services are cheap for occasional hero shots: Erase.bg $6.00 once for 10 credits (V), Slazzer 10 credits for $6.0 (V), Removal.ai 25 credits for $8.99 lifetime (V), Path hand-drawn clipping path from $0.39 per image (V). Not needed if rembg and Windows Photos work.
- remove.bg's standalone site closes "from 1 December 2026 at 9:00am CET"; it is "moving to Canva" (V). Canva's pricing page lists "remove background" under Pro (US$144/year), while Canva's feature page says "Remove your photo's background for free"; the free allowance is unclear and should be tested with a free account (V, contradiction noted).
- Skip for now: Topaz Photo ($199/yr), Gigapixel ($149/yr), Magnific ($20/month), Pixelz ($95 per mo plus $0.95 per image), Claid, Flair, Pebblely, Mokker, VanceAI, Luminar. They solve bulk or AI-scene problems Hollie does not have, and Etsy still needs the real photo. Adobe's own plan pages returned 403 four times today, so the Photography plan price is unverified (U); Photoshop on iPhone shows "Photoshop Mobile & Web Monthly $7.99" on the App Store (V).

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Windows 11 Photos app | Background blur, remove or replace with a color; Generative Erase retouch; crop, rotate, filters | Built in to Windows; no price shown | Whole feature; "the separation process is done locally on your device" | Windows 11 | High. Free, already installed, local, no account | V | https://support.microsoft.com/en-us/windows/apps/photos/edit-photos-and-videos-in-windows |
| Snapseed (Google) | Phone editor: Smart Masking, Healing, Selective, Batch Editing, RAW, film looks | "Free"; "no subscriptions, purchases, ads, or watermarks" | Everything | iOS 17+ (also Android, U) | High. Best free iPhone retoucher for lamps, glass, frames | V | https://apps.apple.com/us/app/snapseed-photo-editor-camera/id439438619 |
| Apple Photos: lift subject | Touch and hold a subject, then "Copy Subject", "Add Sticker" or "Share" | Built in to iOS | Everything | iPhone, iOS 16 to 27 guides | Medium. Fast cutouts for social and stickers; edge quality not listing grade on glass | V | https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iphfe4809658/27/ios/27 |
| Google Photos (iOS app) | Magic Eraser, Unblur, Portrait Light; 15 GB storage | "Free · In-App Purchases" | Editing tools listed; Magic Editor limits not verified | iOS 18+, Android, web | Medium. Good eraser for stray cords and tags | V (listing); Magic Editor limits U | https://apps.apple.com/us/app/google-photos-backup-edit/id962194608 |
| rembg (BiRefNet) | Local cutout engine, CLI, Python, HTTP server, Docker | Free, "MIT license" | Everything | Windows (Python), Linux, Docker | High, already chosen. Must pass `-m birefnet-general`; "bria-rmbg ... The default" | V | https://github.com/danielgatis/rembg |
| Upscayl | Local AI upscaler (Real-ESRGAN), batch folder | "Free and Open Source"; GitHub: "AGPL-3.0 license" | Desktop app, all of it | Windows, Mac, Linux | High. Rescue small or old photos to 2000px for Etsy | V | https://upscayl.org/ and https://github.com/upscayl/upscayl |
| Upscayl Cloud | Hosted upscaling with credits | "$24.99" shown on the credit selector; plan mapping unclear | "Free Trial $0 10 credits included" | Web | Low. Desktop version is free | V | https://upscayl.org/pricing |
| PowerToys Image Resizer | Right-click bulk resize in Explorer; CLI; presets | Free Microsoft utility | Everything | Windows 10/11 | High. Make 2000px Etsy and 1600px eBay sets in one click | V | https://learn.microsoft.com/en-us/windows/powertoys/image-resizer |
| Affinity (by Canva) | Full photo editor, vector and layout in one app | "Affinity is free for individuals (seriously)" | Everything except Canva AI features ("Access to Affinity with AI" is a Canva Pro line) | Windows, Mac, iPad | High. Serious retouching, free | V | https://www.affinity.studio/ and https://www.canva.com/pricing/ |
| GIMP 3.2.8 | Open-source photo editor | Free, "GNU General Public License" | Everything | Windows 10 1903+, Microsoft Store, Mac, Linux | Medium. Capable, steeper learning curve than Affinity | V | https://www.gimp.org/downloads/ and https://www.gimp.org/about/ |
| Paint.NET | Light Windows editor, layers, plugins | "Classic ... free-of-charge"; "Store ... is paid" | Classic release | Windows 10 21H2+ or 11 | Medium. Quick crops and levels; commercial use allowed | V | https://paint.net/license.html |
| Photopea | Photoshop-like editor in the browser, PSD support | Premium price not found on pages read | Free with ads (U for details) | Web | Medium. No install; good on any PC | U (price) | https://www.photopea.com/learn/ |
| Squoosh | Browser image compressor and resizer, runs locally | Free | Everything | Web (any browser) | High. Fix Etsy's 1MB upload warning without quality loss | V | https://squoosh.app/ |
| ImageMagick 7.1.2 | Command-line resize, convert, composite, batch | "Freely download and use software for personal, internal, or commercial purposes" | Everything | Windows, Linux, Mac | Medium. Scripts for the dashboard pipeline; not a daily tool | V | https://imagemagick.org/license/ |
| XnConvert 1.118 | Batch converter, 80+ actions, 500 formats | "FREEWARE ... for private or educational use"; company licence "1 15.00 €" | Private use only | Windows, Mac, Linux | Medium. Buy the 15 € licence if used for the shop | V | https://www.xnview.com/en/xnconvert/ |
| IrfanView 4.76 | Fast viewer with batch convert and rename | "Freeware for non-commercial use"; commercial licence price not on pages read | Non-commercial only | Windows | Low. Licence does not fit a shop without paying; PowerToys covers resizing | V | https://www.irfanview.com/ |
| darktable | Open-source raw developer | "released under the GPL 3.0" | Everything | Windows, Mac, Linux | Low. Only if Ricky shoots raw | V | https://www.darktable.org/ |
| Krita 5.3.4.1 | Open-source painting and image app | "free and open source ... GNU GPL v3" | Everything | Windows 8.1+, Mac, Linux | Low. Painting tool, not product retouching | V | https://krita.org/en/download/ |
| Pixelcut | Phone and web cutouts, AI backgrounds, Magic Eraser, upscaler, batch up to 100 | "Pro $10 $8 per month, billed yearly"; "Business $30 $24" | "Free $0 ... Limited Background Removal, Limited Upscale, Free export without watermark" | iOS 15+, Android, web | High. Cheapest paid phone cutout with "Commercial license" and "1,000 Batch Exports Monthly" | V | https://www.pixelcut.ai/pricing and https://apps.apple.com/us/app/pixelcut-ai-photo-video/id1534785237 |
| Photoroom | Reseller-standard cutouts, AI backgrounds, shadows, batch, video ads | "Pro (monthly) 12.99 USD"; "Pro (yearly) 89.99 USD" ($7.50 "Per month, billed yearly"); Max 34.99 monthly / 250.00 yearly; Ultra 99.00 / 990.00 | Free version exists (reviews mention it); limits not published on pricing page; batch is a Pro feature | iOS 18+, Android, web | High. Pro is 8,000 AI credits and 1,000 exports a month; dearer than Pixelcut | V (prices from page source) | https://www.photoroom.com/pricing and https://apps.apple.com/us/app/photoroom-ai-photo-video/id1455009060 |
| Canva | Design suite with Background Remover, Magic Resize; now hosts remove.bg | "Free US$0 /year"; "Pro US$144 /year for one person" | Free plan: "Limited access to Standard and Premium AI"; remove background listed under Pro | Web, Windows, iOS, Android | Medium. Already chosen for covers; test whether free bg removal is enough | V | https://www.canva.com/pricing/ and https://www.canva.com/features/background-remover/ |
| remove.bg | One-click background removal, bulk, API, plugins | No plan prices shown; "1 trial credit to spend on AI edits" | 1 trial credit | Web | Low. "will no longer be available from 1 December 2026 at 9:00am CET"; API moved to Leonardo.ai | V | https://www.remove.bg/pricing |
| Erase.bg (Pixelbin) | Pay-as-you-go HD cutouts | "10 Credits $0.60 /credit $6.00 billed once"; 100 credits $12.00; 1000 credits $50.00; "valid for 1 year and are non-refundable" | "3 free credits 3 free downloads" | Web | Medium. Cheap backup when rembg misses on glass | V | https://www.erase.bg/pricing |
| Slazzer | Cutouts with desktop apps, Photoshop extension, API, bulk | Subscription "100 credits / month $ 11.0"; pay-as-you-go "10 credits $ 6.0" | "2 Free credits"; "Unlimited free previews" | Web, Windows, Mac, Linux apps | Medium. Desktop app is a plus; credits roll over while subscribed | V | https://www.slazzer.com/pricing |
| Removal.ai | Cutouts, lifetime credit packs, desktop app | Lifetime "25 credits $0.35 / image $8.99"; Monthly "100 credits $0.05 / image $5.99" | "Unlimited free previews"; full resolution needs credits | Web, desktop app | Medium. $8.99 once covers 25 hero shots | V | https://removal.ai/pricing/ |
| PhotoScissors | Online and desktop cutout, unlimited offline on desktop | "Desktop Version for only $99.99 $29.99" (one-year licence); online "10 Credits $4.99" | "Free download of images in standard definition (SD)" | Windows, Mac, iOS, web | Medium. Local and unlimited for a year at $29.99; online max 10Mb / 4.2Mpx | V | https://photoscissors.com/pricing |
| Cutout.pro | Cutouts, retouch, upscaler, e-commerce staging | Web pricing page not found (404 on four URL variants) | App Store: "Free" with In-App Purchases | Web, iOS 15+ | Low. Could not verify prices | U | https://apps.apple.com/us/app/cutout-pro/id6761744890 |
| Clipdrop (Jasper) | Background removal, upscaler x2/x16, Cleanup, Relight, Uncrop | "Pro 15 US$ per month" | "Free 0 US$": Background Removal 20/24h, Upscaler x2 20/24h, Cleanup 20/24h | Web | Medium. Free daily quota is enough for a small shop; low-res on free | V | https://clipdrop.co/pricing |
| Adobe Photoshop (mobile and web) | Tap Select background removal, Generative Fill, Remove Tool | "Photoshop Mobile & Web Monthly $7.99" | Free download with premium features gated | iOS 18+, web | Medium. Cheapest real Photoshop; desktop Photography plan price unverified (adobe.com 403) | V (App Store); desktop U | https://apps.apple.com/us/app/adobe-photoshop-photo-editor/id1457771281 |
| Adobe Lightroom mobile | Exposure, color, AI edits | "Free · In-App Purchases"; prices not listed | Free app | iOS 18+, Android, web | Medium. Good light and color fixes; premium price U | V (free status) | https://apps.apple.com/us/app/lightroom-photo-editor-video/id878783582 |
| Adobe Express | Templates, "Use AI to add or remove objects", background removal | "Free · In-App Purchases"; Premium price not listed | Free plan | iOS 18+, web | Medium. Canva already chosen | V (free status) | https://apps.apple.com/us/app/adobe-express-create-anything/id1051937863 |
| Photoshop Express | Phone retouch, collage, "Premium (Yearly)" | Price not listed on App Store page | Free app | iOS 18.6+ | Low. Snapseed covers it free | V (free status) | https://apps.apple.com/us/app/photoshop-express-photo-editor/id331975235 |
| Topaz Photo | Denoise, sharpen, upscale, lighting | "$199/yr" annual; product page shows "$39/mo" (billing tab not confirmed) | Trial only | Windows, Mac | Low. Pricier; "Personal and commercial use for orgs under $1M USD annual revenue" | V | https://www.topazlabs.com/pricing and https://www.topazlabs.com/topaz-photo |
| Topaz Gigapixel | Upscale up to 6x | "$149/yr" annual; product page "$29/mo" | Trial only | Windows, Mac | Low. Upscayl is free | V | https://www.topazlabs.com/pricing and https://www.topazlabs.com/topaz-gigapixel |
| Magnific (formerly Freepik) | Upscaler plus image and video models, stock | "Premium $20 $14.50 /month billed annually"; "240K credits/year" | None shown | Web | Low. Pricier, creative suite not a product tool | V | https://www.magnific.com/pricing |
| Let's Enhance | Upscaler and enhancer | "100 credits $9/month Billed annually. $12/month if billed monthly" | "10 Free credits"; "Watermark (removed for paid users)" | Web | Low. Watermark on free; Upscayl is free | V | https://letsenhance.io/pricing |
| VanceAI | Upscale, enhance, desktop apps | Starter "$180 billed annually"; Windows desktop "1 month $39.90" | "Try free with 10 credits" | Web, Windows | Low. Pricier | V | https://vanceai.com/pricing/ |
| Fotor | Online editor, AI tools, background remover | "US$5.83/ Month US$69.99/year" (Pro, yearly); "US$47.99 billed yearly" (basic) | Free tier (details not read) | Web, Windows, iOS | Low. Generic | V | https://www.fotor.com/pricing/ |
| Pixlr | Online editor with Background Remover | "Plus $2.49 per month"; "Premium $9.99 per month" | Free with ads (Plus is "Ad-Free") | Web, iOS, Android | Low. Cheap but Photopea and Affinity are free | V | https://pixlr.com/pricing/ |
| BeFunky | Online editor; Pro adds "Batch AI tools ... Remove backgrounds from large image batches" | "Plus $6.99 $83.88 billed annually"; "Pro $12.49 $149.88 billed annually" | "BeFunky Free $0" | Web | Low. Batch bg removal is on the $12.49 tier | V | https://www.befunky.com/pricing/ |
| Picsart | Phone and web editor, AI tools | "Pro $15 $10.5/mo Billed yearly" | Free app | iOS 15+, Android, web, Windows | Low. Consumer focus | V | https://picsart.com/pricing/ |
| Pebblely | AI product backgrounds, bulk generate | "Lite US$9 per month 30 images"; "Basic US$19 per month 200 images"; "Pro US$39" | Trial answer not rendered | Web | Low. AI scenes; Etsy still needs the real photo | V | https://pebblely.com/pricing/ |
| Flair.ai | AI product photography scenes, custom models | "Pro $8 Per month"; "Pro+ $26"; "Scale $38" (annual-discount toggle state unknown) | "Free $0 Forever ... 5 generated images" | Web | Low. Same reason as Pebblely | V | https://flair.ai/pricing |
| Claid.ai | AI product photo suite and API | Essentials and Pro prices not rendered; Pro "2,000 credits"; background removal "1 credit" | "Free 50 credits to use on any operation" | Web, API | Low. Business and API oriented | V (free tier); price U | https://claid.ai/pricing |
| Mokker AI (now soona AI Studio) | AI background replacement | "Starter $13 / month 500 Photos / month" | "Free 20 photos once" | Web | Low. Brand is migrating to soona.co | V | https://mokker.ai/pricing |
| Pixelz | Outsourced retouching, next-morning delivery | "Monthly subscription $95" plus "$0.95 per image" | None | Web upload | Low. Built for "more than 150 images per month" | V | https://www.pixelz.com/pricing/ |
| Path | Outsourced hand-drawn clipping paths and retouching | "Clipping path FROM $0.39 PER IMAGE"; "Background removal FROM $0.89"; "Shadow FROM $0.25" | "Get 2 free edits" | Web upload | Medium. Pay per hero shot for crystal and chandeliers if AI edges fail | V | https://pathedits.com/pages/pricing |
| Luminar (Skylum) | AI photo editor | "One-time purchase - no subscriptions"; "One flat annual license."; dollar price not in page text | Trial | Windows, Mac | Low. Pricier; price U | U (price) | https://skylum.com/luminar |
| Sirv | Image hosting with 360 spin viewer and zoom | "Business $59 $55 /month Billed annually at $649" | "Free $0 /month 0.5 GB storage ... 360 spin ... Sirv branding on spins/zooms" | Web | Low. Only if 360 spins go on the Shopify site | V | https://sirv.com/pricing/ |
| WebRotate 360 | 360 spin publishing software (SpotEditor), plugins | "PRO $344 $459 ONE-TIME FEE" | "Basic ... FREE ... can be used for commercial purposes" | Windows software plus web viewer | Low. Free tier exists if 360 is ever wanted | V | https://www.webrotate360.com/pricing |
| Foldio360 app (Orangemonkie) | Controls Foldio360 turntable or dome; phone 360 capture, 24/36/48 frames | App free; "one-time $2.99 in-app purchase" for Pro | Base app | iOS, Android | Low. Needs the Foldio360 hardware (price not fetched) | V (app) | https://orangemonkie.com/pages/foldio360-app |
| Arqspin | 360 spin from a phone | Pricing not shown; "TRY IT FOR FREE" | Unknown | iOS, web | Low. U | U | https://arqspin.com/pricing |
| Shopify admin AI image tools and Tinker | "File editor: Replace the background of an image with a color"; "Tinker is a free mobile app with more than 100 AI tools" | "available at no additional cost, but availability can vary by plan" | Included | Shopify admin; Tinker mobile app | Medium. Free once the Shopify store exists | V | https://help.shopify.com/en/manual/ai-powered-tools |
| eBay background enhancement tool | In the listing flow: "White" or "AI-Generated backgrounds, Studio, Surface, and Outside" | Free in eBay listing | Included | eBay web and app | High for eBay listings; zero extra tools | V | https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148 |

Marketplace image specs (V):

| Marketplace | Size | File | Background and AI rules | Source |
|---|---|---|---|---|
| Etsy | "width and height of at least 2000 pixels or more"; first photo "at least 635 pixels"; first photo landscape or square | "Images larger than 1MB in file size may not finish uploading"; "transparent .png files are not supported ... will appear black" | "at least one unedited photo of the actual item against a real background"; other photos may use AI to "change backgrounds"; "note whether images were edited in your listing description" | https://help.etsy.com/hc/en-us/articles/115015663347 |
| eBay | "minimum resolution of 500 x 500 pixels but we recommend images that are about 1600 x 1600"; up to 24 pictures | "maximum 12MB each"; JPEG, PNG, GIF, TIFF, BMP, WEBP, HEIC, AVIF | White not required; eBay's own tool offers AI-generated backgrounds; images must be "truthful, accurate" and your own | https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148 and https://www.ebay.com/help/policies/listing-policies/images-text-policy?id=4240 |
| Shopify | "2048 x 2048 px usually displays best"; "any size up to 5000 x 5000 px, or 25 megapixels" | "smaller than 20 MB"; "best file type ... is PNG, followed by JPEG" | No restriction found; admin AI can recolor backgrounds | https://help.shopify.com/en/manual/products/product-media/product-media-types |

Hardware, one line each, not priced today (U): a 24 to 32 inch folding lightbox with two LED strips for glassware and figurines; a phone tripod or clamp mount for repeatable framing; a motorized turntable only if 360 spins are ever wanted (the Foldio360 app above drives Orangemonkie's).

## 2. Notes per tool

Windows 11 Photos (V). The help page: "AI is used to separate the background, but the separation process is done locally on your device." Options are Blur, Remove, or Replace with a palette or RGB color. Generative Erase has Auto apply and Add mask / Remove mask brushes. Super Resolution and Restyle are separate Copilot+ PC features; the background tool is not listed as Copilot+ only. No price, no account.

Snapseed (V). App Store text: "Get 30+ pro tools and filters - no subscriptions, purchases, ads, or watermarks." "Smart Masking: Instantly and intelligently isolate subjects or backgrounds with a single tap." "Batch Editing: Quickly apply your favorite looks and edits to multiple photos." Healing tool removes small distractions. "Requires iOS 17.0 or later." Developer Google.

Apple Photos lift subject (V). "Touch and hold the subject. When an outline appears around the subject" then "Tap Copy or Copy Subject", "Tap Add Sticker" or "Tap Share". No background replacement inside Photos; paste the subject into another app. Good for social cutouts, not for 2000px listing photos with glass edges.

Google Photos (V for the App Store listing). "Remove unwanted distractions with Magic Eraser. Improve out-of-focus blurry photos with Unblur." "Free · In-App Purchases", iOS 18+. Three Google help URLs for Magic Editor returned "Sorry, this page can't be found", so Magic Editor's free quota and Google One gating are U.

rembg (V). "Rembg is a tool to remove image backgrounds. It can be used as a CLI, Python library, HTTP server, or Docker container." Install: `pip install "rembg[cpu,cli]"`. The models list says "bria-rmbg ... The default." and a commit "feat: make bria-rmbg the default model (#845)". The BiRefNet models are listed: birefnet-general, birefnet-general-lite, birefnet-massive and others. Rule for Ricky's pipeline: always `rembg i -m birefnet-general in.jpg out.png`, never the bare default. Licence of rembg itself: MIT.

Upscayl (V). "Upscayl Desktop continues to be the best image upscaler for Linux, MacOS and Windows." "Free and Open Source ... Download once, forever yours." GitHub: "AGPL-3.0 license"; "It uses Real-ESRGAN and Vulkan". AGPL affects redistribution of modified software, not use of the app on Ricky's PC. Upscayl Cloud is a separate paid service with "Free Trial $0 10 credits included".

PowerToys Image Resizer (V). "a Windows shell extension for bulk image-resizing ... right-click on one or more selected image files in File Explorer". Presets are editable; there is a CLI: `PowerToys.ImageResizer.CLI.exe --width 800 --height 600 .\image.png`. Set two presets: 2000 longest side for Etsy, 1600 for eBay.

Affinity (V). "Affinity is free for individuals (seriously). Just choose your preferred platform below to get started." Windows download offered. Canva pricing lists "Access to Affinity" under Free and "Access to Affinity with AI" under Pro, so AI selections inside Affinity may need Canva Pro; the manual tools are free.

GIMP (V). 3.2.8 released 2026-11-02; Windows 10 1903 or newer; Microsoft Store build for Windows 11. GPL. Fine but Affinity is friendlier.

Paint.NET (V). "Classic ... provided free-of-charge." "Store ... is paid." Licence FAQ: "Yes, you may use it for business, commercial, school, and government use." Needs Windows 10 21H2 or newer, 64-bit CPU with AVX2.

Photopea (U for price). The Learn page confirms a free web editor with layers, masks, refine edge, actions and scripts. Premium pricing is shown inside the app and was not on any page read today.

Squoosh (V). "Images never leave your device since Squoosh does all the work locally." Use it to get a 2000px JPEG under Etsy's 1MB upload warning.

ImageMagick (V). Licence summary: "Freely download and use software for personal, internal, or commercial purposes." Useful inside the dashboard for flattening transparent PNGs onto white before Etsy upload.

XnConvert (V). "XnConvert is provided as FREEWARE (NO Adware, NO Spyware) for private or educational use." "If you intend to use XnView in a company, you must purchase a license." One licence "15.00 €". A sole-proprietor shop is company use; budget 15 € one time if XnConvert is used.

IrfanView (V). "Freeware for non-commercial use." The FAQ explains how to insert a licence but the commercial price was not on the pages read. Use PowerToys instead.

Pixelcut (V). Free: "Limited Background Removal, Limited Upscale, Free export without watermark." Pro: "$10 $8 per month, billed yearly", "600 AI Credits Monthly", "Unlimited Background Removal", "Unlimited Upscale", "1,000 Batch Exports Monthly", "Commercial license". Business "$30 $24". App Store: "Batch Editor - Edit up to 100 photos at once", "Requires iOS 15.0 or later". FAQ confirms iOS and Android. One App Store review complains a 3-day trial was needed to use a feature not in the free version; cancel in Settings before day 3 if only testing.

Photoroom (V, prices from page source). Pricing text shows Pro "8,000 AI credits • 1,000 exports" per month, Max "25,000 AI credits • 3,000 exports", Ultra "75,000 AI credits • 10,000 exports". The page's JSON-LD: "Pro (monthly) ... 12.99 USD", "Pro (yearly) ... 89.99 USD", "Max (monthly) 34.99", "Max (yearly) 250.00", "Ultra (monthly) 99.00", "Ultra (yearly) 990.00"; noscript spans "$7.50", "$20.99", "$82.50" "Per month, billed yearly". Google Play: Pro unlocks "batch editing, product videos, Video Ad Maker, premium templates, faster processing and higher usage limits", so batch is paid. App Store "Requires iOS 18.0 or later". Reviews: one reseller praises it; one says it "removed the background but left the doll stand showing" and AI backgrounds vary. Photoroom's reply to a reviewer: "We are sorry we don't offer a one-time subscription."

Canva (V). Free "US$0 /year"; Pro "US$144 /year for one person" with "AI tools (resize, translate, remove background, and more)". The free plan line is "Limited access to Standard and Premium AI". The feature page says "Remove your photo's background for free with Canva's background remover" and the FAQ answer did not render. remove.bg's page says "Free to try in HD and part of Canva's Visual Suite." Treat free background removal in Canva as limited until tested.

remove.bg (V). Banner: "remove.bg's background removal is moving to Canva. The standalone website will no longer be available from 1 December 2026 at 9:00am CET." Plans are not priced on the page; it points to "Try Canva for Free" and "Go to Leonardo.ai for API Pricing". Do not build on it.

Erase.bg (V). "Each background removal uses 1 credit." "10 Credits $0.60 /credit $6.00 billed once"; "100 Credits $0.12 /credit $12.00 billed once"; "1000 Credits $0.05 /credit $50.00 billed once"; "Credits are valid for 1 year and are non-refundable." Sign-up required; "3 free credits". Run by Pixelbin.

Slazzer (V). "2 Free credits", "Unlimited free previews on slazzer.com", "API access & Apps for windows / Mac / Linux", "Photoshop Extension". Subscription "100 credits / month $ 11.0"; pay-as-you-go "10 credits $ 6.0", "50 credits $ 18.0". "Unused credits roll over as long as you're subscribed." Pay-as-you-go credits "available for use anytime within two years".

Removal.ai (V). Lifetime packs "Pay Only Once. Credits available for use within 3 years": "3 credits $1.89", "25 credits $8.99", "150 credits $45.99". Monthly "100 credits $5.99". "Unlimited free previews on Removal.AI"; full resolution needs a credit. Desktop app link on the page.

PhotoScissors (V). Online: "Free download of images in standard definition (SD)"; "Maximum image size: 10Mb", "Maximum image resolution: 4.2Mpx"; credits "10 Credits $4.99", "50 Credits $9.99", "200 Credits $19.99". Desktop: "BUY PhotoScissors Desktop Version for only $99.99 $29.99 ... UNLIMITED offline image processing"; "License period is one year from the date of purchase." No refunds.

Cutout.pro (U). Four pricing URL variants returned "This page could not be found". The iOS app is "Free" with In-App Purchases, iOS 15+. Not enough to recommend.

Clipdrop (V). Free: "Background Removal 20/24h", "Image Upscaler x2 20/24h", "Cleanup 20/24h", "Text Remover 50/24h". Pro "15 US$ per month": "High Resolution Background Removal 1000/24h", "High Resolution Image Upscaler x16". Footer links to "Jasper Free Trial" (owner). Free outputs are not high resolution.

Adobe (mixed). adobe.com and helpx.adobe.com returned HTTP 403 on all seven attempts, so the Photography plan price is U. App Store pages read: Photoshop "Photoshop Mobile & Web Monthly $7.99", with "Select the backgrounds with the Tap Select tool" and "create AI-generated backgrounds with Generative Fill"; Lightroom "Free · In-App Purchases" iOS 18+; Adobe Express "Free · In-App Purchases" with "Use AI to add or remove objects"; Photoshop Express "Free" with "Premium (Yearly)" unpriced. All are governed by Adobe's General Terms.

Topaz (V). Pricing page: "Topaz Photo Mac and PC $199/yr", "Topaz Gigapixel Mac and PC $149/yr", "Topaz Studio $399/yr Billed annually". Product pages show "$39/mo" (Photo) and "$29/mo" (Gigapixel) under an Annual / Annual, Billed Monthly / Monthly selector whose active tab was not confirmed. Footnote: "Personal and commercial use for orgs under $1M USD annual revenue." Pricier; one-time licences are not offered on the pages read.

Magnific (V). Title "Pricing plans | Magnific (formerly Freepik)". "Premium $20 $14.50 /month billed annually", "240K credits/year", "Commercial AI license". Pricier for this use.

Let's Enhance (V). "10 Free credits get upon signing up", "Watermark (removed for paid users)", "Upscale up to 8 megapixels" on free. "100 credits $9/month Billed annually. $12/month if billed monthly."

VanceAI (V). Starter "200 credits +60 free /mo $180 billed annually"; "Try free with 10 credits"; Windows desktop "1 month $39.90". Pricier.

Fotor, Pixlr, BeFunky, Picsart (V). Generic online editors with background removers. Fotor Pro "US$5.83/ Month US$69.99/year". Pixlr "Plus $2.49 per month" (ad-free, 80 credits), "Premium $9.99 per month". BeFunky "Plus $6.99 $83.88 billed annually", "Pro $12.49 $149.88 billed annually" and only Pro has "Batch AI tools ... Remove backgrounds from large image batches". Picsart "Pro $15 $10.5/mo Billed yearly". None beats the free stack for a one-person shop.

Pebblely, Flair.ai, Claid.ai, Mokker (V). AI scene generators. Pebblely "Lite US$9 per month ... 30 images every month", Basic US$19 with "Bulk generate", Pro US$39 (500 images). Flair "Free $0 Forever ... 5 generated images", "Pro $8 Per month", "Pro+ $26", "Scale $38" with "Company Commercial License" on Pro+. Claid free "50 credits", Pro "2,000 credits", background removal "1 credit"; Essentials and Pro dollar prices did not render. Mokker "Mokker AI is now soona's AI Studio", "Starter $13 / month 500 Photos / month", free "20 photos once". Etsy requires a real unedited photo regardless and asks sellers to disclose AI edits; these tools fit Shopify or social, not the Etsy first photo.

Pixelz and Path (V). Pixelz "Monthly subscription $95" plus "$0.95 per image", aimed at "teams processing more than 150 images per month". Path "Clipping path FROM $0.39 PER IMAGE", "Background removal FROM $0.89 PER IMAGE", "Shadow FROM $0.25", "Turnaround from 6 hours", "Get 2 free edits". Path is the one outsourcing option that fits one-of-one items: pay 39 to 89 cents only for a crystal decanter or chandelier the AI cannot cut cleanly.

360 spin (V where noted). Sirv Free "$0 /month 0.5 GB storage" includes "360 spin" with "Sirv branding on spins/zooms"; Business "$59 $55 /month Billed annually at $649". WebRotate 360 Basic "FREE ... can be used for commercial purposes", PRO "$344 $459 ONE-TIME FEE", with "Noxon 360 Turntable Integration". Foldio360 app: free, "one-time $2.99 in-app purchase" for Pro; "Mode 2 - Phone 360: ... number of frames (24, 36, or 48)". Arqspin pricing not shown (U). Etsy and eBay have no 360 slot; this is a Shopify-only idea and not a 2026 priority.

Shopify (V). "File editor: Replace the background of an image with a color." "Many of these features are available at no additional cost, but availability can vary by plan, device, and language." "Tinker is a free mobile app with more than 100 AI tools for creating images, videos, and brand assets for your store, such as product photography." Image specs in the table.

eBay (V). Listing tool: "Select the Background icon to automatically replace the background with a solid white color" on web; in the app "Choose White ... Or, choose from the AI-Generated backgrounds, Studio, Surface, and Outside". Policy: "You should take your own images and videos and write your own descriptions." "No, you can't use images or videos from a manufacturer's website." Accepted formats and limits in the table.

Etsy (V). Full quotes in the table and bottom line. Extra: "You can't use editing to hide flaws, conceal damage, or edit an item's appearance to make it look different from what the buyer will receive." "Your first listing image does not need to be the unedited photo." Etsy's legal "Creativity Standards" page returned 403; the help article above carries the operative rules.

## 3. Recommendation for Hollie

Install or sign up today, all free:

1. Windows 11 Photos app (already on the PC). Use Background > Remove or Replace, and Generative Erase for price tags and cords. Zero cost, local.
2. Snapseed on the iPhone. Shoot, then Smart Masking to lift the subject's exposure, Healing for dust and tags, Batch Editing for a consistent look across a listing's photos.
3. PowerToys (Microsoft). Add two Image Resizer presets: 2000px for Etsy, 1600px for eBay. Right-click a folder of photos, done.
4. Upscayl desktop. Rescue any photo under 2000px before Etsy upload.
5. Affinity (free for individuals, Canva account). For real retouching: levels, dust, reflections in glass, straightening frames.
6. Squoosh in the browser. Get each Etsy photo under 1MB.
7. rembg with `-m birefnet-general` on the PC (already decided). Flatten the PNG onto white or a room background before Etsy, because Etsy renders transparency black. ImageMagick does the flatten in one command.
8. Apple Photos lift subject and Google Photos Magic Eraser for quick social cutouts and erasures on the phone.

Pay only once it earns it:

- First paid app: Pixelcut Pro at "$8 per month, billed yearly" ($10 monthly) or Photoroom Pro at "$89.99" a year ($12.99 monthly). Trial both on the free tiers for two weeks of listings. Buy one only when Ricky is listing 20 or more pieces a month and wants batch backgrounds and AI shadows on the phone. Pixelcut is cheaper and states "Commercial license"; Photoroom has the bigger reseller following and 1,000 exports a month.
- Per-image fallback for hard glass and crystal: Path clipping path from $0.39 per image (2 free edits), or Erase.bg $6.00 once for 10 HD credits. Both under budget, pay only when AI edges fail.
- XnConvert company licence 15.00 € one time, only if PowerToys and ImageMagick are not enough for batch work.

Skip and why:

- remove.bg: standalone closes 1 December 2026.
- IrfanView for the shop: non-commercial freeware, price not published.
- Topaz, Gigapixel, Magnific, Let's Enhance, VanceAI: $9 to $199 a year or more for upscaling Upscayl does free.
- Pebblely, Flair, Claid, Mokker, BeFunky Pro, Pixelz: bulk or AI-scene tools for catalogs; Etsy still needs the real photo and asks for disclosure of AI edits; a one-of-one shop does not have the volume.
- Cutout.pro, Arqspin, Luminar, Photopea Premium, Adobe desktop plans: prices could not be verified today.
- 360 spin hardware and software: Shopify-only, not a 2026 need. If wanted later, WebRotate 360 Basic and Sirv Free both cost nothing to try.

## 4. Gaps and pages that would not load

- WebSearch budget was exhausted before this lane started, so no roundups or app-store category pages were swept; all pages are direct vendor URLs. Tools not covered: dedicated iPhone camera apps (Halide, ProCamera), Vendoo or Crosslist's built-in background removers (other lane), Remini.
- Adobe: www.adobe.com/products/photoshop/plans.html, www.adobe.com/express/pricing, www.adobe.com/products/photoshop-lightroom/plans.html, www.adobe.com/creativecloud/photography/compare-plans.html, www.adobe.com/products/photoshop-lightroom.html, helpx.adobe.com/creative-cloud/help/plans.html, helpx.adobe.com/lightroom-cc/kb/lightroom-plans.html all returned HTTP 403 (bot wall). Photography plan price is U.
- Etsy: www.etsy.com/legal/creativity-standards returned HTTP 403. The help-center article loaded and carries the image rules.
- Google Photos help: support.google.com/photos/answer/13582552, /12496398 and /13702007 all returned "Sorry, this page can't be found" (wrong article IDs; could not search for the right ones). Magic Editor quotas are U.
- Cutout.pro: www.cutout.pro/pricing and three variants returned "This page could not be found".
- Photoroom: prices are not in the rendered text of the pricing page; taken from the page's structured data. help.photoroom.com rendered only a shell. Free-tier limits not published.
- Photopea Premium price, Claid Essentials and Pro prices, Luminar price, Arqspin price, Pebblely free trial, Canva free background-remover allowance, Fotor free tier, Topaz product-page billing tab: not rendered or not on page.
- Wrong App Store IDs tried first: id1444555011 (404), id6504263592 (404), id1113153706 (Microsoft Teams). Corrected via Apple's iTunes lookup API.
- Microsoft Store page for Photoshop (apps.microsoft.com) rendered only CSS.
- Hardware prices (lightbox, phone mount, turntable) were not fetched.

## 5. Sources (every URL fetched today, one per line; status in brackets where not a normal load)

https://www.photoroom.com/pricing
https://www.photoroom.com/pricing?plan=pro
https://www.photoroom.com/batch
https://www.photoroom.com/enterprise (redirect from /business)
https://help.photoroom.com/en/articles/8395421-how-much-does-photoroom-cost [shell only]
https://play.google.com/store/apps/details?id=com.photoroom.app&hl=en_US
https://apps.apple.com/us/app/photoroom-ai-photo-video/id1455009060
https://apps.apple.com/us/app/id1444555011 [404]
https://apps.apple.com/us/app/photoroom-ai-photo-editor/id1444555011 [404]
https://apps.shopify.com/photoroom [page does not exist]
https://www.pixelcut.ai/pricing
https://apps.apple.com/us/app/pixelcut-ai-photo-video/id1534785237
https://www.canva.com/pricing/
https://www.canva.com/features/background-remover/
https://www.affinity.studio/
https://www.remove.bg/pricing
https://www.erase.bg/pricing
https://www.slazzer.com/pricing
https://removal.ai/pricing/
https://www.cutout.pro/pricing [not found]
https://www.cutout.pro/pricing-plans [not found]
https://www.cutout.pro/pricing/ [not found]
https://www.cutout.pro/en/pricing [not found]
https://www.cutout.pro/user/pricing [not found]
https://apps.apple.com/us/app/cutout-pro/id6761744890
https://photoscissors.com/
https://photoscissors.com/pricing
https://clipdrop.co/pricing
https://claid.ai/pricing
https://pebblely.com/pricing/
https://flair.ai/pricing
https://mokker.ai/pricing
https://www.pixelz.com/pricing/
https://pathedits.com/pages/pricing
https://www.topazlabs.com/topaz-photo
https://www.topazlabs.com/topaz-gigapixel
https://www.topazlabs.com/pricing
https://www.magnific.com/pricing (redirect from magnific.ai/pricing)
https://letsenhance.io/pricing
https://vanceai.com/pricing/
https://upscayl.org/
https://upscayl.org/pricing
https://github.com/upscayl/upscayl
https://www.gimp.org/downloads/
https://www.gimp.org/about/
https://www.photopea.com/learn/
https://www.photopea.com/ [raw HTML grep only]
https://paint.net/download.html
https://paint.net/license.html
https://learn.microsoft.com/en-us/windows/powertoys/image-resizer
https://www.xnview.com/en/xnconvert/
https://www.irfanview.com/
https://www.irfanview.com/faq.htm
https://imagemagick.org/license/
https://squoosh.app/
https://www.darktable.org/
https://krita.org/en/download/
https://skylum.com/luminar (redirect from /luminar-neo)
https://www.fotor.com/pricing/
https://pixlr.com/pricing/
https://www.befunky.com/pricing/
https://picsart.com/pricing/
https://apps.apple.com/us/app/snapseed-photo-editor-camera/id439438619
https://apps.apple.com/us/app/google-photos-backup-edit/id962194608
https://apps.apple.com/us/app/lightroom-photo-editor-video/id878783582
https://apps.apple.com/us/app/adobe-express-create-anything/id1051937863
https://apps.apple.com/us/app/photoshop-express-photo-editor/id331975235
https://apps.apple.com/us/app/adobe-photoshop-photo-editor/id1457771281
https://apps.apple.com/us/app/adobe-photoshop/id6504263592 [404]
https://apps.apple.com/us/app/adobe-express-ai-photo-video/id1113153706 [resolved to Microsoft Teams; wrong ID]
https://apps.microsoft.com/detail/xpdlr6g4t5x4k7 [CSS only]
https://itunes.apple.com/search?term=photoroom&country=us&entity=software [Apple lookup API]
https://itunes.apple.com/search?term=pixelcut&country=us&entity=software [Apple lookup API]
https://itunes.apple.com/search?term=google+photos&country=us&entity=software [Apple lookup API]
https://itunes.apple.com/search?term=adobe+photoshop&country=us&entity=software [Apple lookup API]
https://itunes.apple.com/search?term=cutout.pro&country=us&entity=software [Apple lookup API]
https://www.adobe.com/products/photoshop/plans.html [403]
https://www.adobe.com/express/pricing [403]
https://www.adobe.com/products/photoshop-lightroom/plans.html [403]
https://www.adobe.com/creativecloud/photography/compare-plans.html [403]
https://www.adobe.com/products/photoshop-lightroom.html [403]
https://helpx.adobe.com/creative-cloud/help/plans.html [403]
https://helpx.adobe.com/lightroom-cc/kb/lightroom-plans.html [403]
https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iphfe4809658/27/ios/27
https://support.apple.com/guide/iphone/identify-objects-in-your-photos-and-videos-iph21c29a1cf/ios
https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iph5a2b8b4f5/ios [redirected to guide welcome; wrong slug]
https://support.apple.com/guide/iphone/remove-distractions-with-clean-up-iph63bbf3f2b/ios [redirected to guide welcome; wrong slug]
https://support.apple.com/en-us/105087 [wrong article]
https://support.google.com/photos/answer/13582552 [not found]
https://support.google.com/photos/answer/12496398 [not found]
https://support.google.com/photos/answer/13702007 [not found]
https://support.microsoft.com/en-us/windows/apps/photos/edit-photos-and-videos-in-windows
https://help.etsy.com/hc/en-us/articles/115015663347
https://www.etsy.com/legal/creativity-standards [403]
https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148
https://www.ebay.com/help/policies/listing-policies/images-text-policy?id=4240
https://www.ebay.com/help/policies/listing-policies/picture-policy?id=4262 [resolved to member-to-member contact policy; wrong ID]
https://help.shopify.com/en/manual/products/product-media/product-media-types
https://help.shopify.com/en/manual/products/product-media
https://help.shopify.com/en/manual/products/product-media/edit-media
https://help.shopify.com/en/manual/ai-powered-tools (redirect from /shopify-magic)
https://github.com/danielgatis/rembg
https://sirv.com/pricing/
https://www.webrotate360.com/pricing
https://arqspin.com/pricing
https://orangemonkie.com/pages/foldio360-app
