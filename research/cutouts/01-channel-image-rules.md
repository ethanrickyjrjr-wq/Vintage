# Channel image rules for cutout / product photos (Etsy, eBay, Shopify, Google Merchant Center)

Fetched 2026-10-27 with crawl4ai (raw pages in `research/cutouts/raw/01-*.md`). VERIFIED = read on the vendor page this session
(URL + quote or close paraphrase). UNVERIFIED = memory, blog, search snippet, or inference. "X verified, Y needs review" is used
where sources disagree.

## Bottom line

1. Never send an alpha PNG/WebP to a channel. Etsy (VERIFIED): transparent PNGs are not supported and transparent pixels render black. Google, eBay and Shopify docs are silent (UNVERIFIED); a third-party blog says Google shows black.
2. Channel files = flattened sRGB JPEG, solid colour (white for Google/eBay), 2048 x 2048 px, <= 1 MB target (Etsy soft limit). 2048 clears every recommended size: Etsy 2000, Shopify 2048, eBay ~1600, Google ~1500.
3. Etsy requires at least one UNEDITED photo of the actual item against a real background in every listing. Cutouts are allowed in the other slots (backgrounds may be changed, flaws may not be hidden). Keep the untouched original in the set.
4. Google main image: no text, border, logo, watermark, placeholder; show the exact item; product 75-90% of frame (recommended). White is not stated as a rule on the 2 attribute pages, but every example is white and Product Studio outputs white.
5. Google min size is changing: 100x100 (non-apparel) / 250x250 (apparel) enforced until 2027-01-31, then 500x500 for everything. Warnings since July 2026. Produce >= 1500 now.
6. Google Product Studio (free, manual, in Merchant Center) has a one-click "Remove background" that outputs the product on WHITE. It says it does not support wall art or light fixtures (our lamps and art). Automatic image improvements (off by default) only strip text/watermarks/logos; it does not cut out backgrounds.
7. Alpha WebP is for our own storefront only. Never let storefront badges, borders or text get baked into a channel file (eBay, Google and Etsy all ban them).
8. Repo CLAUDE.md says Crosslist imports from Etsy and fans out to eBay and Shopify. Crosslist's image ordering/passthrough is UNVERIFIED, but if true, the Etsy first photo becomes the main image on eBay and Shopify (and on Google if its feed comes via Shopify), and the Etsy set must be channel-safe for all of them.
9. Shared-file conflict: Google recommends the product fill 75-90% of the frame; Etsy says leave enough border to crop to square, portrait and landscape. One file cannot satisfy both (see section 6). Decide the aspect ratio for the whole set before the shoot: 1:1 is consistent with every verified channel statement.

## 1. Google Merchant Center

Sources: https://support.google.com/merchants/answer/6324350?hl=en (image_link, raw `01-gmc-image-link.md`),
https://support.google.com/merchants/answer/6324370?hl=en (additional_image_link, `01-gmc-additional-image.md`),
https://support.google.com/merchants/answer/12159030?hl=en (Image too small, `01-gmc-image-too-small.md`).

### Format and size (VERIFIED)
- Supported formats, both attributes: "JPEG (.jpg/.jpeg), WebP (.webp), PNG (.png), GIF (.gif), BMP (.bmp), and TIFF (.tif/.tiff)". Extension must match the real format; a mismatch (".jpg for a .png file") causes "Unsupported image type" errors.
- image_link size: "At least 500 x 500 pixels"; "recommend ... around 1500x1500 pixels or above"; "No image larger than 64 megapixels"; "No image file larger than 16MB". URL 1-2,000 chars, ASCII, RFC 3986.
- Timing, same-vendor pages differ in framing: image_link page says "new image size requirements of at least 500 x 500 pixels for all products beginning January 31, 2027". The "Image too small" page is more precise: enforcement of 500x500 begins 2027-01-31; "Until January 31, 2027, you can use an image that's at least 100 x 100 pixels for non-clothing and 250 x 250 pixels for clothing"; "Starting July 2026 you will see warnings" on images between old minimum and 500; YouTube Shopping ads need 500x500 to serve on TV. Today (2026-10-27) the enforced minimums are therefore 100 / 250, with 500x500 enforced in about 3 months. Treat 500 as the floor.
- additional_image_link: optional, "Include up to 10 additional images" (VERIFIED). Under-minimum additional images are not shown but do not disapprove the product ("won't be disapproved, but your images won't be shown"). May show staging, in-use, or partial/detail shots. There is also a separate `lifestyle_image_link` attribute (linked from both pages) for in-context shots.
- Robots: allow both Googlebot and Googlebot-image (VERIFIED). Use stable URLs (no timestamps/session IDs).

### Disapproval rules for the main image (VERIFIED, image_link page)
- No promotional elements or overlays: calls to action, price/shipping, warranty claims, promotional adjectives, "Condition or compatibility text ... such as 'New', '2-piece set'", barcodes/QR, watermarks/copyright/stamps, added brand/retailer names and logos (unless physically part of the product).
- No placeholder/generic image/graphic; "Your primary image must clearly display the exact item being sold." No "Coming soon" graphics, no store logo, no illustration or mockup instead of the product.
- No single-colour image that is only a square of colour. No border ("don't include borders around your image"). No products not sold together with the main product.
- Exceptions (generic graphics allowed) only for Hardware, Vehicles & Parts, Computer Software, and single-colour for a few paint categories. None apply to vintage goods.
- Best practices (recommendations, not rules): frame product "no less than 75%, but not more than 90%" of the image; one distinct image per variant; one variant per image. "Google may test subtle cropping on your image".
- Background: NEITHER attribute page states "white background is required" or "transparent is not allowed". UNVERIFIED as a rule. Every example row on the additional_image_link page is "on a white background", and Product Studio's remove-background output is white (below). A coloured solid background is not forbidden in the text I read, but only the white case is evidenced as safe.
- AI provenance (VERIFIED): images created with generative AI "must contain meta data indicating that the image was AI-generated (for example, the IPTC DigitalSourceType ... TrainedAlgorithmicMedia)"; do not strip it from images made by tools such as Product Studio. A pure segmentation cutout is not described as generative; if we ever inpaint/extend backgrounds with a generative model, keep or write that IPTC tag.

### Used / vintage (condition attribute)
Source: https://support.google.com/merchants/answer/6324469?hl=en (`01-gmc-condition.md`).
- `condition` is required for used/refurbished items. VERIFIED: `used` = "second-hand or has been modified from the original condition ... shows wear or has been used before". Allowed values: new, refurbished, used.
- That page contains NO image-specific rule for used items (grep for image/photo returned nothing). The only image-related interaction is the main-image rule above: do not print "Used" / "Vintage" / condition labels onto the photo. Also VERIFIED: used and refurbished products "aren't displayed on YouTube organic and Discover surfaces" (they can still run as ads).

### Does Google offer automatic cutout / enhancement today? (VERIFIED, vendor pages)
- Product Studio, https://support.google.com/merchants/answer/13708167?hl=en (`01-gmc-product-studio.md`): "a suite of free, AI-powered tools" to "create images, change backgrounds, increase image resolution, remove backgrounds, and generate product videos". In Merchant Center: Creative content > Product Studio; also in the Google & YouTube app on Shopify. Available to all Merchant Center users except those based in RU and FR.
- Remove background: manual per image ("Select the Remove background card ... select the image ... Remove background"), then "Add to Merchant Center" (optionally as main image). Quote: "Only your product will remain on a white background". So output is white, not transparent. No per-image count or size limit stated on that page.
- Caveats on that page (VERIFIED): "still experimental"; "works best with ... consumer packaged goods"; "doesn't support images with hands, walled [sic, wall] art, and light fixtures"; Google quality reviewers "may review your inputs and new images"; Terms of Service apply (https://support.google.com/merchants/answer/14579601). Our inventory has lamps and art, so Product Studio may not work for them.
- Automatic image improvements, https://support.google.com/merchants/answer/12724659?hl=en (`01-gmc-auto-image-improve.md`): "turned off by default"; enable under Products > "Automations". It tries "removing any text, watermarks, overlays, or logos" to fix disapprovals; may leave the original for "Complex multi-panel collages", "Heavy text overlapping main product features", "Strong or dense watermarks". It does NOT mention background removal. There is no vendor-documented automatic background-removal feature besides the manual Product Studio tool.

### Alpha PNG/WebP on Google
- Vendor docs: PNG and WebP are accepted formats; behaviour of transparent pixels is NOT documented. UNVERIFIED.
- Third-party: FeedArmy KB (blog, https://feedarmy.com/kb/how-to-fix-black-background-on-images-in-google-merchant-center/, `01-feedarmy-black-bg.md`) reports transparent images showing black in Merchant Center and recommends a solid white background. Its explanation (lossy compression strips alpha) is the blog's own theory. UNVERIFIED, but consistent with Etsy's verified behaviour. Treat as "do not rely on alpha".

## 2. Shopify

Sources: https://help.shopify.com/en/manual/products/product-media/product-media-types (`01-shopify-types.md`),
https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads (`01-shopify-file-uploads.md`),
https://help.shopify.com/en/manual/online-store/images/theme-images (`01-shopify-theme-images.md`),
https://help.shopify.com/en/manual/products/product-media/product-photography,
https://help.shopify.com/en/manual/ai-powered-tools/media-generation (`01-shopify-media-generation.md`).

- Size (VERIFIED): "any size up to 5000 x 5000 px, or 25 megapixels"; file "smaller than 20 MB". Recommended: "For square product images, a size of 2048 x 2048 px usually displays best."
- Aspect ratio (VERIFIED): to display same-size side by side on collection pages, use "a consistent aspect ratio" for all featured images; theme or CDN can also request consistent sizing. File-upload page: aspect ratio accepted "Between 100:1 and 1:100". No single mandated ratio.
- Formats: media-types page: "The best file type for most product images is PNG, followed by JPEG. Other accepted file types are TIFF, BMP, GIF, SVG, HEIC, and WebP." File-upload page lists only "JPEG, PNG, WEBP, HEIC, and GIF". Sources disagree (types page verified, upload page verified); use JPEG or PNG and it is safe either way. Theme-images page says "Use JPEG for product images" and PNG for logos/icons.
- Delivery (VERIFIED): "Images aren't compressed when you upload"; when served, Shopify picks the best format and delivers WebP/AVIF when the browser supports them; GIFs become animated WebP.
- Transparency (VERIFIED partial): "The PNG format also supports transparency" (theme-images). Photography page: for a transparent background use third-party retouching tools. Troubleshooting: replacing a JPEG with a PNG "might not have the expected transparency". Shopify's own AI tool "Color background" can "make it transparent" and says transparent results must be saved as PNG ("Other image formats can't save a transparent background"); generated images carry "an invisible watermark" that "doesn't restrict commercial use". What a product image's alpha looks like on a given theme (theme background showing through vs black) is NOT documented. UNVERIFIED. A community thread titled "Transparent Product Images are shown with black background Dawn" exists (search result only; page was walled, 42 bytes), so do not rely on alpha.
- Filename gotcha (VERIFIED): file names must not end with `pico, icon, thumb, testing, small, compact, medium, large, grande` (CDN may read them as resize commands).
- Google Product Studio is also available inside Shopify via the Google & YouTube app (VERIFIED on the Google pages).

## 3. Etsy

Sources: https://help.etsy.com/hc/en-us/articles/115015663347 "Requirements and Best Practices for Images in Your Etsy Shop" (`01-etsy-add-photos.md`),
https://help.etsy.com/hc/en-us/articles/360016260113 "How to Edit Your Listing Photos" (`01-etsy-thumbnails.md`),
https://help.etsy.com/hc/en-us/articles/115015628707 "How to Create a Listing" (`01-etsy-create-listing2.md`).
WALLED: etsy.com/legal/policy/listing-image-requirements/253962679005 (crawl4ai 4 bytes, WebFetch 403), Etsy seller handbook pages (4 bytes), etsy.com/legal vintage policy (4 bytes). Anything that depends on those pages is UNVERIFIED, including the "exceptions" to the unedited-photo rule.

- File types (VERIFIED): ".jpg, .gif, .png, .svg, or .heic. These are the only image file types Etsy supports." WebP is NOT in the list.
- Alpha (VERIFIED, exact quote): "Animated .gif files & transparent .png files are not supported. If a file contains transparency, the transparent parts of the image will appear black on Etsy."
- Size (VERIFIED): recommended "width and height of at least 2000 pixels or more". "Your first listing photo should have a width and height of at least 635 pixels to avoid showing up lower in searches." Uploader error "Listings look best with photos at least 2000 pixels wide" is advisory only; you can still publish.
- File size: help article says "Images larger than 1MB in file size may not finish uploading"; the create-listing troubleshooting says "Files bigger than 300k may time out". Sources disagree on the soft threshold (1 MB vs 300 KB); neither is a stated hard cap, and no hard max was found. Target <= 1 MB.
- Count (VERIFIED, create-listing page): "up to 20 photos and 2 videos that are 5-15 seconds in length".
- Colour: convert to sRGB (VERIFIED). Etsy recompresses, so images "may appear less sharp after being uploaded".
- Aspect ratio and thumbnail (VERIFIED): the first photo is the thumbnail and "dictates the shape of the photos that follow". First photo "should be horizontal (landscape) or square". Etsy crops thumbnails to 3 views (square, portrait, landscape) via a thumbnail adjustment tool; leave extra negative space around the item; "Avoid square crops. Upload horizontal or landscape images." (Etsy's own text is slightly inconsistent: square is acceptable for the first photo, but landscape is preferred.) No numeric ratio is given (UNVERIFIED if 4:3 or 3:2 is "right"). A main image that is "too dark, blurry, or are part of a photo-collage may result in your listing appearing lower in Etsy search results".
- Authenticity / edited photos (VERIFIED, Image authenticity section):
  - "All images must accurately reflect the item's true appearance, including color, condition, scale, and materials."
  - "Your listing must include at least one unedited photo of the actual item against a real background, meaning the photo hasn't been edited or changed in any way. Some exceptions may apply".
  - "Outside of your required unedited photo, you can still use photo-editing tools, including AI, to adjust lighting or color, crop or resize images, or change backgrounds."
  - "You can't use editing to hide flaws, conceal damage, or edit an item's appearance to make it look different from what the buyer will receive."
  - Best practice (not a rule): "Make your first listing photo the clearest, most realistic representation"; "If you use AI to edit any of your listing photos, note whether images were edited in your listing description."
  - So a cutout is allowed, but cannot be the only photo, and AI-edited photos should be disclosed. Whether Etsy treats a resized or lightly recompressed original as still "unedited" is not stated (needs review).
- Vintage (VERIFIED, create-listing page): "Vintage items must be at least 20 years old. Newer, vintage-style, or collectible items aren't allowed". No vintage-specific photo rule found on the help pages (the legal vintage policy is walled, so UNVERIFIED).

## 4. eBay

Sources: https://www.ebay.com/help/policies/listing-policies/picture-policy-ebay-pictures-policy?id=4370 (`01-ebay-picture-policy.md`),
https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148 (`01-ebay-adding-pictures.md`),
https://www.ebay.com/help/policies/listing-policies/images-videos-text-policy?id=4240 (`01-ebay-images-text-policy.md`).

- Policy not allowed (VERIFIED): "Photos that don't accurately represent the item"; "Placeholder images used to convey messages"; "Stock photos for used, damaged, or defective items"; "Photos with added borders"; "Photos with added text, artwork or marketing material"; "Watermarks of any type, including those used for ownership attributions".
- Min size: policy says "at least one photo that is 500 pixels on the longest side"; photo-tips page says "minimum resolution of 500 x 500 pixels but we recommend images that are about 1600 x 1600". Policy (longest side) vs tips (both sides): sources disagree, so make every side >= 1600.
- File size / formats (VERIFIED): "maximum 12MB each"; accepted "JPEG, PNG, GIF, TIFF, BMP, WEBP, HEIC, or AVIF".
- Count (VERIFIED): "You can add up to 24 pictures." Whether all 24 are free is not stated on this page (UNVERIFIED; historically free, confirm in Seller Hub fee table).
- Style (VERIFIED, photo tips): "Generally, photos in a 1:1 or 16:9 aspect ratio look best"; "uncluttered space against a neutral backdrop"; "White backgrounds are generally best, but for shiny or reflective items ... a darker background may work better"; main photo "should show the whole item face-on"; show flaws up close (set expectations, prevent returns); for single items "main photos should not include any variations".
- Used items (VERIFIED): "You can't use a catalog or stock photo if you're listing an item as used." Photos must show the actual item; images policy: "take your own images". Pre-owned vehicles must show the actual vehicle.
- eBay's own cutout tool (VERIFIED): the listing tool's "Background" icon "automatically replace[s] the background with a solid white color"; the app also offers AI-generated Studio/Surface/Outside backgrounds. So a white-background cutout of our own photo is something eBay itself produces; it does not violate "stock photo" or "border" language.
- Other (VERIFIED): pictures stored 90 days; Gallery Plus shows a 400x400 hover image.
- Alpha: not documented anywhere I read. UNVERIFIED. Blog results exist (isopeel, tomdahne) but I did not fetch them; do not rely on them.
- API image rules for the Inventory API `imageUrls` could not be read (the fetched developer page contained navigation only). UNVERIFIED; expect the same limits as the uploader, confirm before building the API push.

## 5. Alpha handling summary

| Channel | What docs say about transparent PNG/WebP | Status |
|---|---|---|
| Etsy | Not supported; "transparent parts ... will appear black" | VERIFIED |
| Google MC | PNG, WebP accepted; transparency not mentioned; Product Studio cutout outputs white; one blog reports black | docs silent, UNVERIFIED |
| eBay | Not mentioned; own tool outputs solid white; PNG and WEBP accepted | UNVERIFIED |
| Shopify | PNG "supports transparency"; product-image alpha rendering not documented; AI tool can output transparent PNG; replacing JPEG with PNG may not show transparency | partial, UNVERIFIED for rendering |
| Our own storefront | We control it: alpha WebP renders fine on any CSS background | n/a |

## 6. Recommendation: files to produce per item

| File | Spec | Used by |
|---|---|---|
| `orig` untouched camera file (+ any extra angle/flaw shots) | no edits; keep EXIF-orientation; full size in private storage | Archive; Etsy "unedited photo" slot (resized/recompressed copy is probably fine but unconfirmed, so upload the closest-to-untouched version, <= 1 MB if the uploader complains); eBay/Google additional photos (flaws, scale) |
| `flat.jpg` cutout flattened on solid colour (Google/eBay/Shopify flavour) | 2048 x 2048 px, 1:1, sRGB, baseline JPEG, quality ~85, target <= 1 MB (Etsy soft limit; caps: Google 16 MB / 64 MP, eBay 12 MB, Shopify 20 MB / 25 MP). Background #FFFFFF. Subject 75-90% of frame, centred (Google's recommendation, not a disapproval rule). No text, border, logo, badge | Google `image_link` (only if the Google feed is built directly from our files); eBay and Shopify main images when pushed directly rather than via Crosslist |
| `flat-etsy.jpg` same cutout, looser framing | same 2048 x 2048, 1:1, but subject ~60-70% of the side so Etsy's square/portrait/landscape thumbnail crops do not clip it (a 4:3 crop of a square keeps about 75% of one side; arithmetic, not an Etsy figure; Etsy gives no numeric fill) | Etsy slots after the unedited original. If Crosslist copies Etsy's first photo downstream, the Etsy first-photo choice IS the eBay/Shopify main-image choice |
| `alpha.webp` | transparent WebP, long side ~1200 px (2x of display), cap on our side (suggest <= 200 KB; our choice, no vendor figure) | Own storefront only (rows/columns of cutouts). Never in a feed, Crosslist, or channel upload |
Shoot instruction (drives how Ricky photographs): Etsy says the first photo "dictates the shape of the photos that follow", and cropping/resizing is listed as an allowed edit only OUTSIDE the required unedited photo. So shoot originals square (1:1, or framed so the intended 1:1 crop is already in the frame) with wide margins around the item, so the unedited original matches the cutouts without needing a crop. Otherwise a landscape phone original placed first reshapes every square cutout after it. 1:1 fits every verified statement: Etsy "landscape or square", eBay "1:1 ... look best", Shopify 2048 x 2048 square, Google no ratio stated. (A landscape alternative, e.g. 4:3, is not vendor-specified; UNVERIFIED.)

Rules for the pipeline:
- Names: keep the extension equal to the real format (Google errors on mismatch); do not end Shopify filenames with `thumb, small, medium, large, icon, pico, compact, testing, grande`; use stable URLs for the Google feed, and change the filename when an image changes.
- Keep every storefront overlay (badges, "SOLD", price, borders) out of the source layer. Render the flat export from the cutout only.
- Cutout must not alter the item (no removing cords, legs, chips, stains, patina). Etsy: "can't use editing to hide flaws"; eBay: "accurately represent". Add close-ups of flaws as normal photos.
- Etsy ordering: unedited original in the set; if we want the cutout first, accept that it is only allowed because an unedited photo exists elsewhere; add "AI-edited background" wording to the description if the cutout used an AI model (Etsy best practice).
- Google: if we use Product Studio instead of our own cutout, its output is white background and is generative-AI tagged; keep the IPTC metadata. Lamps (light fixtures) and wall art are listed as unsupported there.
- Google main image should be white-background and product-filling 75-90%; do not label condition or "vintage" on the image; set `condition=used`.

### Risk flags for a cutout MAIN image
- Etsy: HIGH if alpha (black). If flattened: allowed, but at least one unedited real-background photo is mandatory; AI disclosure recommended; first photo advised to be the most realistic one.
- Google: MEDIUM. Not a violation if clean, flat, white, product-forward; alpha behaviour undocumented; AI-edited images need IPTC tag; main image must be "the exact item"; 500x500 minimum enforced from 2027-01-31; Google may crop.
- eBay: LOW-MEDIUM. White-bg cutout is endorsed by eBay's own tool; risk is "doesn't accurately represent" if flaws hidden, and no borders/text/watermarks; used items cannot use stock photos.
- Shopify: LOW for flat JPEG. Alpha PNG risk is rendering on the theme (undocumented) and aspect-ratio inconsistency across rows.

## Open items (could not verify)
1. Etsy listing-image-requirements legal page (exceptions to "unedited" rule), Etsy vintage legal page, seller handbook: walled (403 / 4 bytes).
2. Etsy hard max file size (only soft 1 MB / 300 KB hints).
3. eBay alpha handling, eBay "24 free photos", eBay Inventory API imageUrls limits.
4. Google alpha handling (only a blog claim), and whether Google requires white backgrounds (not stated on the 2 attribute pages).
5. Shopify alpha PNG rendering in themes and Shopify community black-background thread (walled).

## Sources
- Google image_link: https://support.google.com/merchants/answer/6324350?hl=en
- Google additional_image_link: https://support.google.com/merchants/answer/6324370?hl=en
- Google Image too small: https://support.google.com/merchants/answer/12159030?hl=en
- Google condition: https://support.google.com/merchants/answer/6324469?hl=en
- Google Product Studio: https://support.google.com/merchants/answer/13708167?hl=en
- Google automatic image improvements: https://support.google.com/merchants/answer/12724659?hl=en
- Google Merchant Center home: https://merchants.google.com/
- FeedArmy (blog, UNVERIFIED): https://feedarmy.com/kb/how-to-fix-black-background-on-images-in-google-merchant-center/
- Shopify product media types: https://help.shopify.com/en/manual/products/product-media/product-media-types
- Shopify file uploads: https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads
- Shopify theme images: https://help.shopify.com/en/manual/online-store/images/theme-images
- Shopify product photography: https://help.shopify.com/en/manual/products/product-media/product-photography
- Shopify media editor: https://help.shopify.com/en/manual/shopify-admin/productivity-tools/media-editor
- Shopify media generation: https://help.shopify.com/en/manual/ai-powered-tools/media-generation
- Etsy image requirements: https://help.etsy.com/hc/en-us/articles/115015663347-Requirements-and-Best-Practices-for-Images-in-Your-Etsy-Shop
- Etsy edit listing photos: https://help.etsy.com/hc/en-us/articles/360016260113-How-to-Edit-Your-Listing-Photos
- Etsy create a listing: https://help.etsy.com/hc/en-us/articles/115015628707-How-to-Create-a-Listing
- eBay picture policy: https://www.ebay.com/help/policies/listing-policies/picture-policy-ebay-pictures-policy?id=4370
- eBay adding pictures: https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148
- eBay images, videos and text policy: https://www.ebay.com/help/policies/listing-policies/images-videos-text-policy?id=4240
- Source homepages for data citation: https://www.google.com/retail/ (Google Merchant Center), https://www.shopify.com/, https://www.etsy.com/, https://www.ebay.com/
