# Verify on the PC: lanes 14 (hosted services) and 15 (competitors)

Date 2026-11-07. Sonnet subagent report, saved as returned. Brief: check each snippet-level claim in `14-disc-hosted.md` and `15-disc-competitors.md` against the pages crawled into `raw/fetched-on-pc/` on the PC, quoting every price as the vendor writes it; read-only, no network.

---

Lanes 14-disc-hosted and 15-disc-competitors are checked against the fetched pages. I read all 11 lane-14 pages and 7 of 9 lane-15 pages. Two lane-15 pages are walled (Emerald is a Cloudflare challenge, Etsy Seller Handbook is 4 bytes). I also opened 7 files indexed under other lanes where a lane cited the same URL; they are marked "(other lane)". No index row exists for Photoroom help 12523455 and 12353253, Pebblely, Clipdrop, Cutout.pro, Slazzer, Erase.bg, Fotor, the Apple, Windows and HowToGeek phone pages, ebay.ca, Top Down Trading, Zipsale, TikTok or Business Insider, so those are NOT FETCHED. Nothing was written or fetched.

## Lane 14

| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| Photoroom bg-removal API "$0.02 per image"; accepts PNG, JPEG, WEBP, HEIC | photoroom.com/api/remove-background (other lane) | CONFIRMED | "$0.02 per image on the Basic API plan." / "Input: PNG, JPEG, WEBP or HEIC, up to 50 MB and 6,000 px on the widest side." (www.photoroom.com_api_remove_background.md) |
| Plus editing is $0.10/image on a $100/month plan | photoroom.com/api/pricing | CORRECTED | $0.10 is on the page; $100/month is not. "charged the Plus price per image of $0.10". Only plan prices shown: "a $20 Basic API plan (1000 images)" and "$40 Basic API plan (2000 images)" (www.photoroom.com_api_pricing.md) |
| "1,000-image minimum" is unreliable and contradicts pay-as-you-go | same | CORRECTED | The plans are prepaid monthly buckets, not pay-as-you-go. "You can purchase a fixed amount (for example, 1000, 2000, etc.)"; "you can subscribe only to monthly plans"; "Unused images will not roll over". The smallest bucket is not stated (the slider did not render). |
| Default rate limit 60 images/min | remove-background page (other lane) | CONFIRMED | "60 images per minute by default." |
| Free account is non-commercial | photoroom.com/legal/terms-and-conditions | CONFIRMED | "We grant Free Accounts a non-exclusive, non-transferable license ... for your own personal, non commercial purposes." Terms effective July 29, 2026 (www.photoroom.com_legal_terms_and_conditions.md) |
| Help text "You cannot use a free account for commercial purposes." | help.photoroom.com/.../12523455 | NOT FETCHED | No index row. |
| Ghost Mannequin API default 1K; 2K and 4K Enterprise only | docs.photoroom.com/.../ghost-mannequin (other lane) | CONFIRMED | "By default, Ghost Mannequin will produce outputs at a resolution of 1K (`1024x1024`). Output resolutions of 2K and 4K are available for Enterprise plans" |
| Ghost Mannequin batch limits (help 14182832) | help.photoroom.com/.../14182832 | NOT ON PAGE | The URL served a different article, "Use AI tools to generate images in Batch (Web App)" (canonical 16001503). It contains no limits and no ghost-mannequin steps. |
| Web-app batch caps, free export caps, AI Fashion Models on every paid plan | none | NOT FETCHED | photoroom.com/pricing has no row. |
| Depop built Photoroom into its listing flow; "free for Depop sellers"; April 24, 2026 | photoroom.com/customer-stories/depop | CONFIRMED | "April 24, 2026"; "Photoroom is free for Depop sellers." |
| Pixelcut API "5 Credits per image = $0.05 per image" | pixelcut.ai/api/background-remover | CONFIRMED | Same text. Input "Handles PNG, JPEG inputs", so HEIC is not listed. |
| Pixelcut Pro about $10/month, commercial licence, "now called Pixa" | same, plus pixelcut.ai (other lane) | NOT ON PAGE | No consumer prices, licence text or "Pixa" on either file. Footer reads "© 2026 Pixelcut". API Terms link goes to Notion (not fetched). |
| remove.bg site closes 1 Dec 2026 | remove.bg/faq | CONFIRMED | "The standalone website will no longer be available from 1 December 2026 at 9:00am CET." Pricing page (other lane): "Go to Leonardo.ai for API Pricing". |
| CARRIED remove.bg "$3 for 3 credits", "$9/month for 40 credits", "Credits expire December 1, 2026" | remove.bg/pricing (other lane) | NOT ON PAGE | The current page has no dollar figures, and the FAQ answers did not render. Treat the carried figures as stale. |
| Canva remover needs paid plan; price, bulk and commercial terms unknown | canva.com/help/background-remover | CORRECTED | "Background remover is included with paid plans." Bulk exists: "Up to 50 images at a time". Also "photos under 9MB" and "downscaled to 10MP". Plan names, price and commercial terms are not on the page. |
| Adobe Express: transparent PNG via Background, No fill; may drop fine detail | helpx.adobe.com/express/.../remove-background | CONFIRMED | "select Background in the left panel and select No fill ... choose Transparent PNG"; "It may also remove fine details or low-contrast areas." Page says "Last updated on Apr 28, 2026". |
| Adobe: 50 MB/HEIC list, Firefly move, batch, free limits, commercial | same | NOT ON PAGE | None of these appear. |
| Claid bg removal costs 2 API credits; resize/crop free in same request | claid.ai/api-pricing | CONFIRMED | "Background removal and blur ... 2"; resize and crop "Free when combined with other operations". |
| Claid trial 50+50 credits; Essential $15 or $9, Pro $35; dollars per credit | same | NOT ON PAGE | The price cell reads "— credits one-time purchase". The web plans are on claid.ai/pricing (not fetched). |
| Pixian: "0.25 MPx image is 0.05 credits and a 25 MPx image is 1 credit" | pixian.ai/pricing | CONFIRMED | Same sentence. |
| Pixian third-party $0.0024 (2 MP) to $0.0166 (25 MP); older $0.02 | same | CORRECTED | At the 10,000-credit pack ($166.00): 2 MPx $0.0019, 25 MPx $0.0166. At the 250-credit pack ($5.00): 2 MPx $0.0023, 25 MPx $0.0200. $0.0024 is not on the page. |
| Pixian HEIC and commercial terms | same | NOT ON PAGE | Neither appears. Terms page not fetched. |
| eBay app removes background, makes it white, auto-cleans at near-100% separability | innovation.ebayinc.com (computer-vision story) | CONFIRMED, but 2020 | Dated "Feb 26, 2020". "the background removal tool to make a first pass at adding the white background". The algorithm runs on the phone and assumes "Pixels along the image border are predominantly background". 2026 behaviour is not on the page. |
| Pebblely, Clipdrop, Cutout.pro, Slazzer, Erase.bg, Fotor | n/a | NOT FETCHED | No rows. |
| iPhone lift-subject, Windows, HowToGeek, eBay tool-loss reports | n/a | NOT FETCHED | Apple pages and the Value Added Resource article are indexed under lane 17 and not opened here. |

## Lane 15

| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| Campervan Vintage quote: good camera and light "makes a huge difference" | photoroom.com/blog/sell-fast-on-depop | CONFIRMED | "Using a good camera and natural light or studio lights to capture your stock with clear photos makes a huge difference," ... "told Business Insider". The Business Insider URL is dated 2020-02. |
| arXiv 1406.3561: flat about 41% and mannequin about 34% "of clicked items"; "mostly new apparel" | ar5iv.labs.arxiv.org/html/1406.3561 | CORRECTED | Those are the displayed shares. Clicked shares are Flat 39.21%, Mannequin 33.26%, Person 27.53%. Sample is "black dress" queries only, from 2012. |
| Person beats mannequin beats flat | same | CORRECTED | True for person. Mannequin versus flat: "such difference is hardly observable from the real online market data". Conversion of clicked items: Flat 41.88%, Mannequin 42.45%, Person 47.94%. |
| Journal of Research in Interactive Marketing study (169 and 156 participants) | emerald.com | WALLED | Cloudflare "Performing security verification". |
| Blondes in Heaven: use form or model; flat lay hides drape; pair with measurements; no heavy retouching | blondesinheaven.com (lane 09 file) | NOT FETCHED in lane 15, but the text matches | "Flat-lay photography can hide drape problems, fit issues, or shoulder distortion." / "heavy retouching erases the texture and patina" |
| ProductScene: flat-only shops "consistently see lower conversion rates"; assertion with no data | productscene.com | CONFIRMED | Exact sentence on the page, with no data or citation. It also says Etsy buyers "aren't there for clinical white backgrounds". |
| eBay blogs: mannequin for structured garments; $30-$80 mannequin | underpriced.app | CORRECTED | Mannequin: "Invest in a good mannequin ($50-150)", best for "fitted items, professional clothing". "dresses, blazers, structured items" belongs to the Hanging method. Flat lay is best for "t-shirts, pants, shorts, accessories". |
| "At least two hanging and two flat photos"; $30-$80; "extra time does not pay" | topdowntrading.co.uk | NOT FETCHED | No row. |
| Anecdotes: eBay flat lay outsold mannequin; Depop TikTok | community.ebay.com thread (lane 04 file); TikTok | eBay thread confirmed; TikTok NOT FETCHED | "the flat lay items are outselling the ones displayed on a mannequin". |
| Depop: original photos, condition check, yardstick | photoroom blog; zipsale | PARTLY | The Photoroom blog confirms natural light. Zipsale NOT FETCHED. The other sub-claims were not checked. |
| Etsy: "Up to 20 photos and 1 video 5-15 s"; 2000 px | help.etsy.com/.../115015628707 | CORRECTED | "up to 20 photos and 2 videos that are 5-15 seconds"; "at least 2000 pixels wide". |
| Etsy Seller Handbook 1347574487014 | etsy.com | WALLED | 4 bytes. |
| eBay up to 24 photos, 500 px min, 1600 recommended, white not required | ebay.ca (not fetched); ebay.com help (lane 08 file) | ebay.ca NOT FETCHED; ebay.com confirms | "You can add up to 24 pictures." "minimum resolution of 500 x 500 pixels ... about 1600 x 1600." "White backgrounds are generally best." |
| Vintage Seeker: "a working vintage seller's process" | thevintageseeker.ca | NOT ON PAGE | It is about Etsy draft-listing templates (candleholder example). Photography is in a part two that was not fetched. |

## Prices as the vendor writes them

| Vendor | Plan or product | Exact price text | Billing period | Commercial use on this tier | File |
|---|---|---|---|---|---|
| Photoroom | Remove Background API, Basic | "$0.02 per image on the Basic API plan"; example "a $20 Basic API plan (1000 images)" and "$40 Basic API plan (2000 images)" | Monthly only, prepaid, no rollover | Not stated for the API. Paid licence is "for the Customer's own internal business purposes". | www.photoroom.com_api_pricing.md, www.photoroom.com_api_remove_background.md, www.photoroom.com_legal_terms_and_conditions.md |
| Photoroom | Image Editing API, Plus (includes Ghost Mannequin) | "the Plus price per image of $0.10"; the Plus plan's monthly price is not rendered | Monthly | Same as above. | www.photoroom.com_api_pricing.md |
| Photoroom | Free / trial | "10 free production calls on the Remove Background API"; "1,000 sandbox calls a month" (watermarked) | Calls monthly; sandbox monthly | "for your own personal, non commercial purposes" | www.photoroom.com_api_pricing.md |
| Pixelcut | Background Removal API | "5 Credits per image = $0.05 per image" | Per image; plan period not stated | Not on page. | www.pixelcut.ai_api_background_remover.md |
| Pixian | PAYGO credit packs | "250 / $5.00", "1,000 / $18.60", "10,000 / $166.00"; 12 MPx "$0.0100" per image at the smallest pack | One-time purchase; "Credits do not expire, but you must have made a purchase in the last two years" | Not on page. | pixian.ai_pricing.md |
| Claid | API background removal | "2 Credits (per image)"; dollars per credit not shown | One-time purchase | Not on page. | claid.ai_api_pricing.md |
| Canva | Background Remover | No dollar figure: "included with paid plans" | n/a | Not on page. | www.canva.com_help_background_remover_.md |

## What changes in docs/ebay-photo-studio.md

**Photoroom claims, section 4 "Paid fallback".** Both are now confirmed on fetched pages.
- "$0.02 per image" is confirmed on photoroom.com/api/remove-background and api/pricing, with PNG, JPEG, WEBP or HEIC input.
- The free-account rule is confirmed in Photoroom's terms (effective July 29, 2026). Those terms define the Services to include the API.

Current sentence: "Photoroom's API at "$0.02 per image" (the page saved 2026-10-27 says so and lists PNG, JPEG, WEBP or HEIC; one of two checkers could not re-find it, so re-check on the PC), on a paid plan because the free account is for personal, non-commercial use."

Recommended: "Photoroom's Remove Background API at "$0.02 per image on the Basic API plan" (re-fetched 2026-11-07; input PNG, JPEG, WEBP or HEIC; 10 free production calls). Plans are prepaid monthly image buckets that do not roll over (the page's example is $20 for 1,000 images), so the true floor may be about $20 a month and is not stated. Use a paid plan, because Photoroom's terms license Free Accounts 'for your own personal, non commercial purposes'."

Current sentence: "Its single-photo ghost mannequin mode exists but regenerates pixels..."
Recommended addition: "It needs the Plus plan at $0.10 per image, outputs 1024x1024 by default, and 2K and 4K are Enterprise-only."

**remove.bg line, section 4 "Do not use".** Current: "remove.bg: 'The standalone website will no longer be available from 1 December 2026' (fetched 2026-10-27)." Recommended: add "at 9:00am CET (re-fetched 2026-11-07); API users are sent to Leonardo.ai".

**Section 8 unverified list.** Current: "Photoroom, Pixelcut and Canva pricing pages".
- Strike Photoroom API and Pixelcut API pricing as verified.
- Canva shows no price (paid plans only).
- Photoroom's consumer app pricing page, Pixelcut's consumer prices and the Photoroom Free-accounts help article are still unverified.

## Surprises the decision doc does not mention

- **Dead link.** The Photoroom help URL for the batch ghost-mannequin article now serves a different article. No batch limits exist in the fetched set.
- **eBay's in-app tool article is from 2020.** It describes a classical algorithm that assumes border pixels are background. Treat it as history, not current behaviour.
- **Mannequin versus flat.** The eBay research paper shows no real-market gap between them; only person-on-model wins. The decision doc does not cite the paper, so no sentence changes.
- **Canva limits.** Bulk removal is capped at 50 images, files must be under 9 MB, and outputs over 10 MP are downscaled to 10 MP.
- **Photoroom Plus plan.** It lists AI Ironing, Flat Lay, Virtual Model and Virtual Try-On. These are all AI pixel regeneration, so the garment-accuracy risk applies. Photoroom's Pro, Max and Ultra app plans "don't include any API allowance".
- **Claid.** AI fashion on-model shots cost 2 credits per image.
- **Scavengerlife thread (2017).** A seller reports small-size clothing "looked stretched out" on a mid-size mannequin. That matters for vintage sizing and Hollie's forms.
