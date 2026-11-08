# Lane 03-photos: product photo apps (shoot, cut out, retouch, upscale, resize, batch)

Question: which apps make shooting, cutting out, retouching, upscaling, resizing and batch-processing one-of-one vintage pieces easier on Windows and iPhone, and what do they cost? Date 2026-11-07. Verify re-read 24 lane pages (both eBay pages hit a captcha wall); gaps added about 30 tools from category pages. V = vendor page read 2026-11-07; U = figure not readable.

## Bottom line

- The free stack covers the job. PC: Windows 11 Photos (Remove or Replace background "locally on your device", Generative Erase), Windows 11 Paint (one-click "Background Removal"; the lane missed it), Affinity ("free for individuals (seriously)"), Upscayl, PowerToys Image Resizer (Ricky adds the 2000px and 1600px presets; none ship), Caesium for folders. Phone: Snapseed ("no subscriptions, purchases, ads, or watermarks"), Apple Photos lift subject, Clean Up only on "iPhone 15 Pro, iPhone 15 Pro Max, or iPhone 16 model or later", Microsoft Designer ("free with a Microsoft account").
- rembg gotcha, confirmed by verify: the README makes bria-rmbg "The default" and says the BRIA licence "requires a paid agreement for commercial use". Every call must pass `-m birefnet-general`. Gaps adds BiRefNet's MIT "BiRefNet_HR" weights (2048x2048) and withoutBG's "Apache-2.0" open model as safe-licence options.
- Etsy rules, lane V: "transparent .png files are not supported ... will appear black", so flatten every cutout; "at least one unedited photo of the actual item against a real background"; 2000 pixels or more; over 1MB "may not finish uploading"; note AI edits in the description. eBay's specs rest on the lane's read alone.
- Paid phone app, if ever: PicWish Pro "$4.99 /mo Billed Annually" ("billed $59.99/yr") undercuts Pixelcut Pro "$8 per month, billed yearly" ($10 struck through; "billed monthly" never appears) and Photoroom "Pro (monthly) 12.99 USD" / "Pro (yearly) 89.99 USD" (figures only in the page's JSON-LD). PicWish's commercial terms were not read.
- Pay-per-image fallback for glass: Pixian.AI "250 $5.00" credits, a 2 MP image is "0.117" credits; Path "Clipping path FROM $0.39 PER IMAGE"; Erase.bg "10 Credits ... $6.00 billed once" (its FAQ says "$5 for 10 credits"; the card is the checkout figure). Removal.ai's "Lifetime" credits expire "within 3 years"; Slazzer's last two years.
- Canva correction: the pricing page has no background-remover line today, so the lane's "listed under Pro" is refuted. The feature page says "Remove your photo's background for free"; the quota is U. remove.bg closes "from 1 December 2026 at 9:00am CET", "moving to Canva".
- Skip paid upscalers and editors: Topaz Photo "$199/yr", Gigapixel "$149/yr", Luminar "$99.00" one-time with "*365 days access to AI tools", HitPaw FotorPea perpetual "$130.39". Upscayl does it free.

## Table

| Tool | Does | Price (vendor wording, billing period) | Free tier | Platform | Verdict for Hollie | V or U | Source file and URL |
|---|---|---|---|---|---|---|---|
| Windows 11 Photos | Background Blur, Remove or Replace with a color; Generative Erase; crop | Built in; no price on the page | Everything; "the separation process is done locally on your device" | Windows 11 | Use now | V | lane, verify: https://support.microsoft.com/en-us/windows/apps/photos/edit-photos-and-videos-in-windows |
| Microsoft Paint (Windows 11) | One-click AI "Background Removal", Layers, crop, resize | Built in; "Included in the latest version of Windows 11" | Everything | Windows 11 | Use now; second opinion when a Photos edge fails | V | gaps: https://www.microsoft.com/en-us/windows/paint |
| Snapseed (Google) | Smart Masking, Healing, Selective, Batch Editing, RAW | "Free"; "no subscriptions, purchases, ads, or watermarks" | Everything | iOS 17+ (Android U) | Use now; the phone retoucher | V | lane, verify: https://apps.apple.com/us/app/snapseed-photo-editor-camera/id439438619 |
| Apple Photos: lift subject; Clean Up | Touch and hold, then Copy Subject, Add Sticker or Share; Clean Up removes objects by "Tap, brush, or circle" | Built in to iOS | Everything; Clean Up "Usage limits may apply" | iPhone; Clean Up needs "iPhone 15 Pro, iPhone 15 Pro Max, or iPhone 16 model or later" | Use now for social cutouts and cord removal; no save-as-PNG step, so not listing grade | V | lane, verify: https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iphfe4809658/27/ios/27 ; gaps: https://support.apple.com/guide/iphone/clean-up-extend-and-reframe-photos-xy0grrlxue5w/27/ios/27 |
| Microsoft Designer | "Remove background", "Generative erase", "Blur background", templates | "Microsoft Designer is available for free with a Microsoft account"; App Store "Free · In-App Purchases" | Free with account; purchase limits not stated | iOS 17+, web, Windows | Use now on the phone; disclose AI backgrounds on Etsy | V (App Store listing) | gaps: https://apps.apple.com/us/app/microsoft-designer/id6448308247 |
| Google Photos (iOS) | Magic Eraser, Unblur, Portrait Light | "Free · In-App Purchases" | Editing tools listed; Magic Editor quotas U | iOS 18+, Android, web | Use now as the phone eraser when Clean Up is unavailable | V listing; quotas U | lane: https://apps.apple.com/us/app/google-photos-backup-edit/id962194608 |
| rembg (BiRefNet) | Local cutout CLI, Python, HTTP server, Docker | Free, "MIT license" | Everything | Windows (Python), Linux, Docker | Use now (decided); always `-m birefnet-general`; "bria-rmbg ... The default" needs "a paid agreement for commercial use" | V | lane, verify: https://github.com/danielgatis/rembg |
| withoutBG | Open-weights cutout model (pip or Docker), web demo with Keep and Remove brushes, Pro API | Open model "Apache-2.0"; API "100 credits 100 €10 €0.10 30 days" | Local "Unlimited processing"; web "5 free images a day, no signup"; API "50 free credits" | Windows via Python or Docker, web, API | Use now as second local engine; API is a glass fallback | V | gaps: https://withoutbg.com/ ; https://withoutbg.com/pro-model-api/pricing |
| Removerized | In-browser cutout plus upscaler, model selector, batch, offline PWA | Free; "GPL-3.0 license" | Everything | Any browser, PC or iPhone | Use now; nothing to install | V | gaps: https://removerized.yoss.pro/ ; https://github.com/yossdotpro/removerized |
| Upscayl (desktop) | Local Real-ESRGAN upscaler, batch folder | "Free and Open Source"; "AGPL-3.0 license" | Everything | Windows, Mac, Linux | Use now to reach 2000px for Etsy | V | lane, verify: https://upscayl.org/ ; https://github.com/upscayl/upscayl |
| PowerToys Image Resizer | Right-click bulk resize in Explorer, presets, CLI | Free via "MIT license" (the Learn page never says free) | Everything | Windows 10/11 | Use now; add the 2000px and 1600px presets yourself ("Add new size") | V | lane, verify: https://learn.microsoft.com/en-us/windows/powertoys/image-resizer ; https://github.com/microsoft/PowerToys |
| Affinity (by Canva) | Full photo editor, vector and layout | "Affinity is free for individuals (seriously)" | Everything except "Access to Affinity with AI" (a Canva Pro line) | Windows, Mac, iPad | Use now for real retouching | V | lane, verify: https://www.affinity.studio/ ; https://www.canva.com/pricing/ |
| Squoosh | Browser compressor and resizer, runs locally | Free via "Apache-2.0 license" (the site does not say free) | Everything | Web | Use now for single files under Etsy's 1MB warning | V | lane, verify: https://squoosh.app/ ; https://github.com/GoogleChromeLabs/squoosh |
| Caesium Image Compressor | Desktop batch compression and resize with preview, CLI | Free; "GPL-3.0 license" | Everything | "Windows 10 (build 1809) or later", macOS 12+, Linux | Use now for whole shoots under 1MB | V | gaps: https://saerasoft.com/caesium/ ; https://github.com/Lymphatus/caesium-image-compressor |
| ImageMagick 7.1.2 | Command-line resize, convert, composite, batch | "Freely download and use software for personal, internal, or commercial purposes" | Everything | Windows, Linux, Mac | Use now inside the dashboard to flatten PNGs onto white | V (lane only) | lane: https://imagemagick.org/license/ |
| chaiNNer | Node-based GUI: AI upscale, resize, flatten, batch chains | Free; "GPL-3.0 license" | Everything | Windows, Mac, Linux | Use later if one saved chain beats Upscayl plus PowerToys | V | gaps: https://github.com/chaiNNer-org/chaiNNer |
| Shopify admin AI tools and Tinker | "File editor: Replace the background of an image with a color"; Tinker is a "free mobile app with more than 100 AI tools" | "available at no additional cost, but availability can vary by plan" | Included | Shopify admin, mobile | Use when the store exists | V | lane, verify: https://help.shopify.com/en/manual/ai-powered-tools |
| eBay background tool and image specs | Listing flow offers "White" or "AI-Generated backgrounds, Studio, Surface, and Outside"; 500 x 500 minimum, about 1600 x 1600, 24 pictures, 12MB | Free in the listing flow | Included | eBay web and app | Use now for eBay listings | U (lane read it; verify hit a captcha wall) | lane: https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148 |
| Pixelcut | Phone and web cutouts, AI backgrounds, Magic Eraser, upscaler, batch up to 100 | "Pro $10 $8 per month, billed yearly"; "Business $30 $24 per month, billed yearly" | "Limited Background Removal, Limited Upscale, Free export without watermark" | iOS 15+, Android, web | Pay when listing 20+ a month; "Commercial license", "1,000 Batch Exports Monthly"; cancel the 3-day trial in iPhone Settings | V | lane, verify: https://www.pixelcut.ai/pricing |
| Photoroom | Reseller cutouts, AI backgrounds, shadows, batch | "Pro (monthly) 12.99 USD"; "Pro (yearly) 89.99 USD" ($7.50 "Per month, billed yearly"); Max 34.99 / 250.00; Ultra 99.00 / 990.00 | Free version; limits not published; batch is Pro | iOS 18+, Android, web, Shopify app | Pay only if Pixelcut and PicWish fail on edges; "8,000 AI credits • 1,000 exports" | V (JSON-LD, not rendered text) | lane, verify: https://www.photoroom.com/pricing |
| PicWish | Background remover, White Background, Product Retouching, Remove Object, Bulk Listing Images | "Pro $4.99 /mo Billed Annually" ("billed $59.99/yr"); "Max $21.99 /mo" ("billed $263.99/yr") | "Free ... Limited" core downloads | Web, iOS, Android, Windows | Pay when it earns it; cheapest commercial app read; read the commercial terms first | V; monthly-billing price U | gaps: https://picwish.com/pricing |
| Pixian.AI | Web and API cutout, megapixel pricing, no signup for free use | "250 $5.00"; "500 $9.50"; "1,000 $18.60" credits; a 2 MP image is "0.117" credits; "No monthly fees or minimums" | "0.25 megapixels resolution ... Website only" | Web, API | Pay when local engines miss on glass; about $0.01 per 12 MP photo | V | gaps: https://pixian.ai/pricing |
| Erase.bg (Pixelbin) | Pay-as-you-go HD cutouts | "10 Credits $0.60 /credit $6.00 billed once"; "100 Credits ... $12.00 billed once"; "valid for 1 year" | "3 free credits 3 free downloads"; sign-up required | Web | Pay when needed; FAQ says "starting at $5 for 10 credits", card says $6.00 | V | lane, verify: https://www.erase.bg/pricing |
| Removal.ai | Cutouts, credit packs, desktop app | "Lifetime ... 25 credits $0.35 $8.99"; "Monthly 100 credits $0.05 $5.99"; lifetime credits "available for use within 3 years" | "Unlimited free previews"; full resolution needs credits | Web, Windows, Mac, Linux apps | Pay when needed; $8.99 once covers 25 hero shots | V | lane, verify: https://removal.ai/pricing/ |
| Slazzer | Cutouts, desktop apps, Photoshop extension, API | "100 credits / month $ 11.0"; pay-as-you-go "10 credits $ 6.0", usable "within two years" | "2 Free credits"; "Unlimited free previews" | Web, Windows, Mac, Linux | Skip unless the desktop app matters; Pixian is cheaper | V | lane, verify: https://www.slazzer.com/pricing |
| Path | Hand-drawn clipping paths and retouching, "Turnaround from 6 hours" | "Clipping path FROM $0.39 PER IMAGE"; "Background removal FROM $0.89"; "Shadow FROM $0.25" | "Get 2 free edits" | Web upload | Pay per hero shot for crystal and chandeliers AI cannot cut | V (lane only) | lane: https://pathedits.com/pages/pricing |
| Clipdrop (Jasper) | Background removal, upscaler, Cleanup, Relight | "Pro 15 US$ per month" | "Free 0 US$": "Background Removal 20/24h", "Image Upscaler x2 20/24h", "Cleanup 20/24h"; standard resolution | Web | Skip for listings (free is low-res); fine for social | V | lane, verify: https://clipdrop.co/pricing |
| Canva | Design suite, Background Remover, Magic Resize; takes in remove.bg from December | "Free ... US$ 0 /year for one person"; "Pro ... US$ 144 /year for one person" (yearly toggle; monthly U) | Free plan "Limited access to Standard and Premium AI"; feature page "Remove your photo's background for free"; quota U | Web, Windows, iOS, Android | Use now (Canva Free decided); test background removal before paying | V price; free allowance U | lane, verify: https://www.canva.com/pricing/ ; https://www.canva.com/features/background-remover/ |
| Cutout.pro | Cutouts, retouch, upscaler | "80 credits/month $5.00"; "170 credits/month $9.90"; "Pay as you go ... USD $0.130 / credit"; "30credits $4.99" | "5 free credits"; "Free previews forever" | Web, iOS 15+ | Skip; Pixian is cheaper per image and the local engines are free | V (gaps fixed the lane's U) | gaps: https://www.cutout.pro/image-pricing |
| Topaz Photo and Gigapixel | Denoise, sharpen, upscale | "Topaz Photo Mac and PC $199/yr"; "Topaz Gigapixel Mac and PC $149/yr"; product pages "$39/mo" and "$29/mo", billing tab unconfirmed | Trial only | Windows, Mac | Skip; Upscayl is free | V (lane only); monthly figures U | lane: https://www.topazlabs.com/pricing |

Dropped: remove.bg (closes 1 December 2026); Mokker (now soona AI Studio); Pixelz ("Monthly subscription $95" plus "$0.95 per image"; built for 150+ images a month); Pebblely, Flair, Claid, Pippit, Gemini Nano Banana, Vmake (AI scenes); IrfanView, FastStone, XnConvert (non-commercial freeware); Krita, darktable, ON1 (painting or raw tools); Fotor, Pixlr, BeFunky, Picsart, Remini (generic consumer editors); Luminar, HitPaw FotorPea, Aiarty, CyberLink, Movavi (paid Windows editors; the free stack replaces them); Adobe Lightroom, Express, Photoshop Express, Elements and Photoshop mobile ("Photoshop Mobile & Web Monthly $7.99"; the rest U); GIMP, Paint.NET, Photopea, PhotoScape X (Affinity covers them free); BG-Remover, Chrome extensions (tiny user bases); Icons8 ("$0.20 per image", stores uploads); Sirv, WebRotate 360, Foldio360, Arqspin (360 spin, not a 2026 need); Shopify apps (none until the store exists; Alpha Background Remover is "Free"); Upscayl Cloud (desktop is free); Halide, Photomator (prices U).

## Picks

Use now (free):
- PC: Windows 11 Photos and Paint; Affinity; Upscayl; PowerToys Image Resizer with 2000px and 1600px presets; Caesium for folders, Squoosh for one-offs.
- Phone: Snapseed; Apple Photos lift subject, and Clean Up if the iPhone qualifies; Microsoft Designer; Google Photos Magic Eraser as fallback.
- Pipeline: rembg with `-m birefnet-general`, withoutBG as second engine, ImageMagick to flatten every PNG before Etsy. Removerized in any browser. Canva Free as decided.
- eBay's background tool, and Shopify's file editor and Tinker, once those accounts exist.

Pay when it earns it:
- PicWish Pro, "$4.99 /mo Billed Annually". Trigger: 20 or more listings a month and bulk listing images wanted from the phone. Read its commercial terms first.
- Pixelcut Pro, "$8 per month, billed yearly". Trigger: same volume, PicWish's terms do not fit; "Commercial license" is on the page.
- Photoroom, "Pro (yearly) 89.99 USD". Trigger: both of the above fail on edges.
- Pixian.AI "250 $5.00" or Path "FROM $0.39 PER IMAGE". Trigger: a crystal or chandelier piece every local engine cuts badly. Erase.bg "$6.00 billed once" and Removal.ai "$8.99" are alternatives; both expire.

Skip:
- remove.bg: closes 1 December 2026.
- Topaz, Gigapixel, Magnific, Let's Enhance, VanceAI, HitPaw, Aiarty: paid upscaling Upscayl does free.
- Luminar: "$99.00" one-time hides "*365 days access to AI tools".
- Pebblely, Flair, Claid, Mokker, Pippit, Gemini: AI scenes; Etsy needs the real photo plus a disclosure.
- Pixelz, BeFunky Pro: bulk catalog tools; no volume.
- Clipdrop, Cutout.pro, Slazzer, Icons8: Pixian is cheaper and the local stack is free.
- IrfanView, XnConvert, FastStone: non-commercial freeware.
- Adobe plans, Photoshop Elements, Photopea Premium, Photomator, Halide, Arqspin: prices U.
- 360 spin (Sirv, WebRotate, Foldio360): Shopify-only, not a 2026 need.

## Contradictions with earlier decisions

- rembg BiRefNet: no contradiction, but the decision breaks silently unless every call passes `-m birefnet-general`. The README now makes bria-rmbg "The default" (commit "#845") and warns the BRIA licence "requires a paid agreement for commercial use" (verify, V). Refinements from gaps: MIT "BiRefNet_HR" weights, and withoutBG "Apache-2.0" as a second engine. rembg's transparent PNG renders black on Etsy, so the phone-listing flow needs a flatten step before the Etsy draft.
- Canva Free: the lane's "remove background listed under Pro" would have argued for Pro at "US$ 144 /year for one person". Verify refuted it; the feature page says "Remove your photo's background for free". Canva Free stands; the free quota is U.
- Claude Haiku drafts: an amendment, not a contradiction. Etsy asks sellers to "note whether images were edited in your listing description" (lane, V), so the Haiku template needs a disclosure line whenever a background was replaced.
- Crosslist Gold, Buffer Free, Instagram Edits, Supabase, Pushover, fixed Etsy shipping classes: nothing in these files touches them.

## Check by hand

- https://www.canva.com/features/background-remover/ : in the free account, open the FAQ "Can I use the background remover for free?" and note resolution and any monthly cap.
- https://www.photoroom.com/pricing : confirm "$12.99" monthly and "$7.50" per month billed yearly for Pro, and whether free-tier limits appear.
- https://www.pixelcut.ai/pricing : flip the toggle to Monthly; confirm Pro reads $10 per month.
- https://picwish.com/pricing : flip to monthly billing and read the price; open the commercial-use terms.
- https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148 : confirm 500 x 500 minimum, about 1600 x 1600, 24 pictures, 12MB each, and the White or AI-Generated background options.
- iPhone Settings > General > About: Clean Up needs 15 Pro, 15 Pro Max or any 16 or later.
- Optional: https://www.adobe.com/creativecloud/photography/compare-plans.html for the Photography plan price (403 to the fetcher).

## Sources

- research/tools-2026-11-07/03-photos.md
- research/tools-2026-11-07/verify-03-photos.md
- research/tools-2026-11-07/gaps-03-photos.md
