# Verify on the PC: lanes 07 (enhance), 09 (Reddit), 10 (YouTube) and 12 (lighting)

Date 2026-11-07. Sonnet subagent report, saved as returned. Brief: check each snippet-level claim in those four lanes against the pages crawled into `raw/fetched-on-pc/` on the PC, quoting gear prices exactly and checking the handoff's shopping list; read-only, no network.

---

**Header.** Lanes 07, 09, 10, 12. Index rows 37 (30 page, 7 wall). Read all 30; 22 usable, 8 shells (3 eBay 404s, 2 wrong articles, Depop PDF = Depop homepage, one private video, one title-only video). Walled 7. Not fetched about 112 cited URLs (lane 09 about 30, lane 10 55 YouTube plus 5 guides, lane 12 22; lane 07 none beyond GitHub/PyPI pages the cloud run already fetched). Files are in raw/fetched-on-pc/, named by prefix. I could not word-count the final text (heredoc failed, file writes blocked); it is roughly 1,650 prose words, over 1,800 if table pipes are counted.

## Lane 07 enhance
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| eBay floor 500 px, 1600 recommended; zoom 800 vs 1600 | ebay.com/help/...photo-requirements?id=4113 | NOT ON PAGE (wrong article) | "Best practices for avoiding and handling issues with buyers". Other eBay URLs (lanes 06/08): "minimum resolution of 500 x 500 pixels, but we recommend 1600 x 1600" (www.ebay.com_sellercenter_listings_photo_tips.md); "800-1,600 pixels on the long side" (export.ebay.com_en_manage_listings_photo_tips.md) |
| Community: "colour off, need new pictures"; yellow 10% | community.ebay.com/...27847415 | NOT ON PAGE (404) | "The page you requested does not exist." |
| Grey card sets white point for whole image | en.wikipedia.org/wiki/Gray_card | CONFIRMED | "uses the data from the pixels in the gray card area of the photo to set the white balance point for the whole image" |
| Lightroom: WB from card, Copy Settings WB only; subscription | Adobe thread | NOT FETCHED; Shopify partly | "select a neutral gray area"; "deselect all the image settings you don't want to copy"; "Creative Cloud Photography Plan ... $19.99 per month" (www.shopify.com_blog_...lightroom.md) |
| iPhone tap-hold AE/AF lock; ProRAW; ProCamera | alanranger.com | CONFIRMED; ProCamera NOT ON PAGE | "Tap the screen where the product sits and hold until you see AE/AF lock."; "To enable ProRAW, go to Settings → Camera → Formats" |
| Apple camera lock; Pixelcut pricing | support.apple.com/102108; pixelcut.ai | NOT ON PAGE | Apple serves "Set advanced network settings in iOS Setup Assistant"; Pixelcut has no prices ("upscaling up to 16x resolution") |
| ImageMagick resize, unsharp, auto-level, distort, strip | imagemagick.org options | CONFIRMED, with warning | "-unsharp radius{xsigma}{+gain}{+threshold}"; -auto-level "is not typically used for real-life images, image scans, or JPEG format images" |
| XnConvert / IrfanView free licence | xnview.com, irfanview.com | CORRECTED: not for a shop | XnConvert "FREEWARE ... for private or educational use", company licence "15.00 €"; IrfanView "Freeware for non-commercial use" |
| Topaz Photo AI price | topazlabs.com | CONFIRMED (lane gave none) | Now "Topaz Photo": "Personal ... $199/yr Billed annually"; "$25/mo *With annual commitment" |
| Photoshop Image Processor | helpx.adobe.com | CONFIRMED | "Resize to Fit"; "Run Action"; "JPEG image quality between 0 and 12" |

## Lane 09 Reddit
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| Five Reddit searches | old.reddit.com/r/... | WALLED | Login redirect only (old.reddit.com/login/?reason=lor2) |
| Form or mannequin shows fit better than hangers | pages.ebay.com/.../CSA.html | NOT ON PAGE (404) | "Looks like this page is missing." |
| Vintage: north window, form, front/back/side, light edits | blondesinheaven.com | CONFIRMED | "Set up near a north-facing window"; "Include front, back, and one side angle for every dress."; "Resist the urge to over-edit." |
| Depop guide on styles and backgrounds | sellers.depop.com/...pdf | NOT ON PAGE (homepage) | "Buy preloved. Wear it your way" |
| Form vs flat lay thread (lane 04 file) | community.ebay.com/...32785890 | PARTLY | "the flat lay items are outselling the ones displayed on a mannequin". Sales rise after switching, hanger better, kimono: NOT ON PAGE |
| Ghost mannequin tool thread (lane 04 file) | community.ebay.com/...32239377 | NOT ON PAGE (404) | "Page not found" |
| About 28 other community, vendor, shop URLs | various | NOT FETCHED | |

## Lane 10 YouTube (pages carry title, channel, date, description, chapters; no transcript text, only a "Show transcript" button)
| Claim | URL (v=) | Verdict | Evidence |
|---|---|---|---|
| #1, #2 Dresses, jeans on bright white plus measurements | 9xBRV9UfNBM, YYYoNMDF6iI | CONFIRMED, thin | That's What Shannon Said, May 2020: "crisp white photos of dresses for Ebay & Poshmark and also how to do measurements"; #2 description wrongly says "skirts" |
| #11 Shoot and edit ghost mannequin | p-YpsLSaYas | CONFIRMED | BidPixel (sells the service), Jun 2021, 10:21; chapter "Setting up your Ghost Mannequin 1:01" |
| #13 Dress, brand unconfirmed; #17 Blazer | zm7PRDUDlJ0, -WI4b419vmk | CONFIRMED: both Profoto | "Profoto e-commerce", 2016 and 2017; "Learn more about our mannequins"; "Blazers are particularly great to shoot on a mannequin ... seeing the inner lining and fit." |
| #36 White background | MNnIvZu-PQ0 | CONFIRMED | Laredo Montoneri, Jul 2019; chapter "Small vs large light sources 6:01"; "Useful for eBay" |
| #44, #46 Photo stations | EG746TUpw4s, r0lYqGRVj4I | THIN SHELL | #44 ProSoloFlipper, May 2022, description only; #46 title and "0:00 / 9:53" only |
| #7 15 items in 15 minutes | _EvqC0AN864 | NOT ON PAGE | "This is a private video." |
| Steam; clips on excess; tissue | botika.com | CONFIRMED | "Steam everything. On camera, a crease reads as a defect." |
| Sheers need clips | photorobot.com | CONFIRMED | "we have to use clips with sheer fabric, as pins simply won't hold the material firmly enough" |
| 55 other videos, 5 other guides (flippertools "6 photos") | various | NOT FETCHED | |

## Lane 12 lighting
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| NK200: 2 softboxes, 2 35W 5700K bulbs, 7 ft stands, bag | neewer.com/products/lighting-studio-66600013 | CONFIRMED | "2 x Softbox, 2/3 x Light Bulb, 2 x Light Stand, 1 x Carrying Bag"; "83"/210cm Light Stand" |
| Price "From $119.99", 3-bulb $149.99 | same | CORRECTED | "NEEWER NK200 24x24"/60x60CM 700W Photography Softbox Kit ... Regular priceFrom $139.99"; "prices vary by location"; "Up to 50% Off Sitewide" banner |
| CRI 90+ bulbs | same | NOT ON PAGE | No CRI listed; "standard E26 socket, so you can use compatible E26-base bulbs" |
| Tents from $39.99 and $89.99 | neewer.com/collections/shooting-tent | CONFIRMED | "LB30B/LB40B ... From $39.99"; "LP40/LP50/LP60 ... From $89.99" |
| Savage #01 $44.99 at B&H; #66 $44.99 (Samy's, Adorama) | bhphotovideo.com/...45607 | #01 CONFIRMED; #66 NOT FETCHED | "Savage #01 Super White Seamless Background Paper (53" x 36')", "$44.99"; "#66 Pure White - Even whiter than Super White" |
| Nonreflective; store vertically; 53 in width | B&H | CONFIRMED | "Fine-Tooth, Nonreflective Surface"; 53": "full-length portraits of a single individual"; 86" and 107" listed, unpriced |
| Backdrop stand $29.59 to $45.99 | walmart, emartus | NOT FETCHED | Neewer's own: "10x7ft Background Support System Regular price $59.99" |
| eBay: light ground for dark, dark for light | pages.ebay.com/...clothes.html | NOT ON PAGE (404) | Corroborated at www.ebay.com/sellercenter/selling/selling-clothes (lane 08 file): "a black or dark background for lighter clothes." |
| Godox SL60IIBI kit $429; r/Flipping | bhphotovideo.com/...1739483; reddit.com/r/Flipping | WALLED | Cloudflare "Performing security verification"; 221-byte challenge |
| 22 others (Neewer 660, dpreview distance, tripods) | various | NOT FETCHED | 5 to 6 ft distance still unverified |

## Shopping list check (handoff section 5)
| Item | Handoff says | Page says | File |
|---|---|---|---|
| Softbox kit | "Two Neewer 24-inch softbox kits with stands, $80 to $120" | "NEEWER NK200 ... Softbox Kit Regular priceFrom $139.99" (one kit holds two softboxes) | neewer.com_products_lighting_studio_66600013.md |
| Backdrop stand | "$30 to $46" | "10x7ft Background Support System Regular price $59.99" | same |
| Paper | "Savage 53-inch pure white ... about $45" | "Savage #01 Super White ... (53" x 36')" "$44.99" | www.bhphotovideo.com_c_product_45607_... |
| Bulbs | "CRI 90 or better" | "35W 5700K LED Light Bulb", no CRI | neewer product file |

Tripod unchecked. Total with NK200 $139.99, paper $44.99, tripod $7 to $20: $222 to $251 using the $30 to $46 stand, $252 to $265 using Neewer's $59.99, before sale codes.

## What changes in the docs
- Doc section 5: "two Neewer 24-inch softbox kits $80 to $120 ... a Savage 53-inch pure white paper roll $45 ... about $165 to $230 all in." Replace with "one Neewer NK200 kit (two 24-inch softboxes, two 35W 5700K bulbs, two 83-inch stands, bag), from $139.99 at neewer.com on 2026-11-07; a 10 by 7 foot stand, Neewer's own $59.99 (Walmart/EMART $30 to $46 unchecked); Savage #01 Super White 53 in x 36 ft, $44.99 at B&H; tripod $7 to $20 (unchecked); about $222 to $265 all in, before Neewer's sale."
- Handoff section 5: "Two Neewer 24-inch softbox kits with stands, $80 to $120." Same fix. "Savage 53-inch pure white seamless paper roll, about $45 (check whether coats and the feather hat need the 107-inch roll)." Replace with "Savage #01 Super White, 53 in x 36 ft, $44.99 at B&H; 86 in and 107 in rolls exist (unpriced); B&H calls 53 in the one-person size."
- Doc section 5 and handoff: "Same bulbs in every light, 5500 to 5700 K, CRI 90 or better." Append "(the Neewer kit's bulbs state 5700K and no CRI; its sockets take other E26 bulbs)."
- Doc section 5: "Pale garments go on a pale grey or dark backdrop per eBay's own clothing page". eBay says "a black or dark background for lighter clothes"; pale grey is its advice for dark clothes. Change "pale grey or dark" to "dark". Lane 12 recommendation 4 repeats the error.
- Doc section 5 "two soft lights at 45 degrees" is newly supported ("diffused soft boxes on both sides at 45 degrees", blondesinheaven.com). "Five or six feet" stays unverified.
- Doc section 5 pinning kit: add "clips, not pins, on sheers"; Photorobot warns of "residue gaffa tape can leave on clothes", so test tape on a hidden seam of vintage fabric.
- Doc section 5 "buy the smaller form and pad up" is newly supported by Botika (an AI-photo vendor): "a form built for a medium will read loose in every shot".
- Doc section 4 upscaler bullet stands unchanged; Topaz itself pitches its Wonder model for "photos with extremely low resolution".

## Surprising
- ImageMagick's page undercuts lane 07 recommendations 2 and 3: -auto-level is a levels stretch, not a grey-card white balance, and is "not typically used for real-life images".
- Lane 10's top "watch" #7 is private; the set spans 2016 to 2022 (lane said 2021 to 2022); both Profoto videos are vendor content.
- Six other community.ebay.com files (lanes 04, 16: ghost-mannequin-tool, remove-background apps, six-photos, lighting, flat-lay-vs-mannequin, photo-editor) are also 404s. No first-party eBay page on disk backs "model or form shows fit better".
- eBay file size: export.ebay.com says "7MB each"; www.ebay.com help says "maximum 12MB each", which the doc follows. "Eight to twelve photos" rests on a seller-tool blog (underpriced.app, lane 15: "8-12 images minimum on mid-value items").
