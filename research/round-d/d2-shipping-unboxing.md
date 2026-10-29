<!-- Saved verbatim by the parent Opus session from agent d2's final message, 2026-10-29 (the harness refuses subagent report writes). -->

# d2: packing, shipping and the unboxing

Agent d2, accessed 2026-10-29. Raw captures are in `research/round-d/raw/d2-*.md`, with a `.log` beside each. The UPS PDF is saved as `d2-ups-packaging-guidelines.pdf`, with its text extracted to `.txt`. Parent: save this report verbatim to `research/round-d/d2-shipping-unboxing.md` (the harness refused my Write).

**Method.** SearXNG (`tools/search.sh`) found URLs and crawl4ai (`tools/crawl.sh`) read the pages. About 40 pages were read in full or grepped, which is over the 15-25 target. Three carriers, two platforms, an insurer and the supply prices each needed their own pages. WebFetch was used twice:
- The UPS Packaging Guidelines PDF came back as binary. I saved it, ran `pdftotext` on it, and read the text.
- The Etsy legal policy page returned HTTP 403. FedEx's `How_To_Pack.pdf` returned 404.

WebSearch was not used. Postage dollar figures are NOT in this report. I captured no rate tables, and every postage number has to come from a real label quote.

**Tags.** `verified` means read on the live page this session. `inferred` is my reading of what a page implies. `unverified` means anecdote, secondhand, or a source I could not check. `computed` means arithmetic on quoted prices.

**Walls and dead pages (not retried; no Patchright).**
- FedEx claims FAQ: 0 bytes.
- USPS FAQ "How can I use insurance": 0 bytes.
- Etsy legal policy page: 4 bytes by crawl, 403 by WebFetch.
- Etsy Seller Handbook shipping category: 4 bytes.
- Home Depot "How to Pack Pictures and Mirrors": 215 bytes.
- UPS Packaging_Guidelines PDF by crawl: 4 bytes. It was recovered through WebFetch and `pdftotext`.
- FedEx `How_To_Pack.pdf`: 404.
- Vistaprint postcards: captured, but no readable price came out.
- Uline "Corrugated Bin Dividers": captured, but these are warehouse bin dividers, not glass cells, so I did not use them.
- Shopify's USPS page: captured, but I used only its cubic-pricing mention.

---

## TL;DR

1. **No carrier or insurer page names a harp or finial.** FedEx says to remove lamp shades and "wrap them separately", and to bag hardware inside the package. Lighting New York says to remove "the lampshade, bulb, and any detachable decorative elements." The harp-and-finial step is `inferred` from those two. Carrier text agrees on 2 to 3 inches of cushion per side. UPS wants the outer box "six inches greater" in every dimension. FedEx wants "3" of cushioning in and around the interior box." That is the glass standard. `verified`
2. **The default insurer may not pay on some of Hollie's stock.** Etsy and Shopify both sell Shipsurance. Its exclusions on both platforms' terms list "neon items", "windows, plate glass, stained glass, float glass" and "any stone or ceramic slabs". Shopify says to claim with Shipsurance "and not the carrier" when it covers the label. So a stained-glass lamp or a neon piece may have no payout route. Whether a framed mirror counts as "float glass" is **unverified, needs review**. Ask Shipsurance in writing.
3. **Keep the outside of the box plain.** Shipsurance denies loss and theft cover when the packaging "describes, or alludes to, the nature of the contents". Damage stays covered. Put all branding, the card and the gift inside the box.
4. **Etsy calculated shipping will undercharge anything double-boxed.**
   - Etsy takes the item size "when packed" ("folded, but not boxed") and picks "the smallest and cheapest package".
   - It works only with USPS, and it has no handling-fee field.
   - If the recorded size is smaller than the real box, "USPS will... charge you if you underestimated."
   - **Use fixed shipping classes on Etsy. Use flat or weight rates, plus a handling fee, on Shopify.**
5. **The packing standard is also the claims defense.**
   - USPS refuses to pay on damage to articles "not properly wrapped for protection", on articles packed so they "could not have reached [their] destination undamaged", and on shock damage "without evidence of damage to the mailing container."
   - It also refuses if the addressee does not keep the box.
   - UPS's claim form asks for a photo of "how it was packaged inside the box".
6. **The tightest clock is the insurer's.**
   - Shipsurance covers concealed damage only if found within 15 days of delivery.
   - USPS damage claims are due within 60 days of mailing.
   - UPS claims are due within 60 days of the scheduled delivery.
   - Etsy needs a seller reply to a buyer within 48 hours.
7. **Etsy Purchase Protection is thin for fragile pieces.** It covers up to $250 of a refund. Damage is covered "for the first instance per calendar year". Etsy asks you to claim from any other coverage first. For anything over $250, insure it.
8. **Uline sells in bundles, so the minimum outlay is real.** A bubble roll is $61 to $67 but sold in bundles of 4. Mirror boxes come in bundles of 20 to 25. Free and small-lot sources matter more than the per-unit price suggests.

---

## 1. UPS: packaging tips page, packaging PDF, claims page

- URLs:
  - https://www.ups.com/us/en/support/shipping-support/packaging-tips (raw `d2-ups-packaging-tips.md`)
  - https://www.ups.com/assets/resources/webcontent/en_US/Packaging_Guidelines.pdf (raw `d2-ups-packaging-guidelines.pdf` / `.txt`)
  - https://www.ups.com/us/en/support/file-a-claim (raw `d2-ups-claim.md`)
- Evidence, verbatim:
  - "The two-box method is recommended for sharp or fragile goods, bags and accessories, travel and luxury items." `verified`
  - "For the outer box, use a box that has a depth, width, and length six inches (15 centimetres) greater than the inner box." and "Secure your box with an additional three inches (76 centimetres) of cushioning material around the inner box". `verified`
  - "Use no less than two inches (five centimetres) of loose filler material around lightweight items for cushioning". `verified`
  - Air bags: "Use as void-fill material for lightweight items without sharp corners or edges." Also "Extreme hot or cold temperatures may affect the ability of air bags to provide adequate product protection." `verified`. Applying this to cut glass (sharp edges) is `inferred`.
  - "Do not use masking, cellophane, duct or water activated paper tapes, string or paper over-wrap." and "Place a duplicate address label inside the box". `verified`
  - PDF checklist: "Avoid re-using boxes." and "Use at least two inches of appropriate cushioning material to protect internal items from each other and the corners, sides, top and bottom of containers." `verified`
  - PDF disclaimer: "It is the responsibility of the Shipper to ensure that proper packaging is used". `verified`
  - Claims: "Start a claim within 60 days of the scheduled delivery for packages that have been lost or damaged". `verified`
  - Claims: "Keep any invoice that can provide value of the package. If you have a damaged package, hold on to the contents and the packaging." `verified`
  - Claims photos: "A photo showing the damaged item and how it was packaged inside the box. A close-up photo of the shipping label with tracking number (generally starts with 1Z). One photo of the outside of the package (showing any damage)." `verified`
  - "Unless additional investigation is required, you can typically expect a resolution to your claim in 8 to 10 business days." `verified`
  - "Research shows that damaged or lost packages resulting in a claim are often connected with boxes too large or too small, providing poor cushioning, labels that aren't properly placed on your package or having unclear delivery instructions." `verified`
  - The PDF's box-strength table is garbled by `pdftotext`. I read the 0-30 lb row as 200 lb test, single wall. That reading is `inferred`, and I did not rely on it.
- Not found: any UPS item-specific page for lamps or mirrors. UPS's own declared-value page was not read; the $100 UPS figure comes from Etsy's page (section 5).
- **Steal this:** (a) the three-photo set is the claim kit, so make it the buyer's card and your own pre-ship routine; (b) the 6-inch outer-box rule gives a box-size formula; (c) the duplicate address label inside; (d) the tape list.

## 2. USPS: packages page, insurance page, DMM 609

- URLs:
  - https://www.usps.com/ship/packages.htm (raw `d2-usps-packages.md`)
  - https://www.usps.com/ship/insurance-extra-services.htm (raw `d2-usps-insurance.md`)
  - https://pe.usps.com/text/dmm300/609.htm (raw `d2-usps-dmm609.md`)
- Evidence, verbatim:
  - "Use strong packaging with enough room to add cushioning for fragile items and to prevent items from shifting." `verified`
  - "If you're reusing a box (be careful: boxes can weaken during shipping), make sure all old logos, barcodes, shipping labels, and addresses are covered or blacked out." `verified`
  - "Use enough 2-inch-wide packing tape to close and secure all seams." `verified`
  - "Packages can't be larger than 130" total length (the longest side) + girth". Priority Mail "must be less than 108"". `verified`
  - "Priority Mail Express® and Priority Mail® services include up to $100 of insurance in the price." and "up to $5,000 in indemnity". "The price is based on declared value, starting at $2.80." `verified`
  - DMM 609, 2.0: "the addressee must retain the mailing container, including any damaged articles, all packaging, and any contents received... Failure to do so will result in denial of the claim." `verified`
  - 3.1: "Damaged or Missing Contents: customers should file a claim immediately but must file no later than 60 days from the date of mailing." `verified`
  - 3.2 proof of value: "A sales receipt, paid invoice or bill of sale, or statement of value from a reputable dealer." `verified`
  - 4.3 nonpayable (verbatim items):
    - 3: "Claim based solely on sentimental rather than actual value."
    - 8: "Damage by abrasion, scarring, or scraping to articles not properly wrapped for protection."
    - 12: "Fragile nature of article prevented its safe carriage in the mail, regardless of packaging."
    - 15: "Damage caused by shock, transportation environment, or x-ray, without evidence of damage to the mailing container."
    - 18: "any item packaged in such a manner that it could not have reached its destination undamaged in the normal course of the mail." `verified`
  - I did not read how USPS decides what is "properly wrapped" or "fragile nature".
- **Steal this:**
  - Item 15 is the glass failure mode: a box that looks fine outside with a broken piece inside. Photograph the finished packing before closing (that is `inferred` from items 8, 15 and 18).
  - Reusing a box is allowed if you cover the old markings.
  - A proof-of-value file (the Etsy receipt) should sit with every shipment.

## 3. FedEx: special care, furniture, artwork, clothes, declared value

- URLs and raw files:
  - `.../small-business/articles-insights/special-care-shipments.html` (`d2-fedex-special-care.md`)
  - `.../shipping/how-to-ship-furniture.html` (`d2-fedex-furniture.md`)
  - `.../shipping/how-to-ship-artwork.html` (`d2-fedex-artwork.md`)
  - `.../shipping/how-to-ship-clothes.html` (`d2-fedex-clothes.md`)
  - `.../shipping/declared-value.html` (`d2-fedex-declared.md`)
- Evidence, verbatim:
  - "Double-box fragile items within a larger box and include 3" of cushioning in and around the interior box." `verified`
  - "Wrap fragile products individually in a minimum 3" thickness of air-cellular cushioning material, and then fill any empty spaces with foam peanuts or other cushioning material." `verified`
  - "Place the product in the middle of the box with ample cushioning on all sides." `verified`
  - "For a standard corrugated box, create an "H" by taping down the middle seam and on each edge." `verified`
  - "Always mark the box with "Fragile"". `verified`
  - Furniture page (it names lamps): "remove lamp shades from lamps and detachable legs from tables, and wrap them separately." `verified`
  - "Put knobs, screws, and other hardware in a small sealable bag and secure it inside the package." `verified`
  - "wrap the furniture first. Then measure... and add 3" to 5" to each dimension to allow for padding." `verified`
  - "We cannot ensure compliance with markings such as up arrows or "This End Up."" `verified`
  - The page's average-weight table lists a lamp at 5 lb. `verified` (a generic average, not a spec)
  - Artwork: "We recommend shipping artwork that has a lower maximum declared value and limit of liability of no greater than $1000. If you are shipping artwork valued over $500, we offer Premium Art Boxes lined with a plastic protector and foam." `verified`
  - Clothes: "place it face down on a clean surface and fold the sleeves backwards. Then fold the length of it in three." Also "Consider enclosing your items in a plastic bag or a polybag". Also "Acid-free paper or muslin cloth (for delicate items)" on the supplies list. `verified`
  - Clothes: "For multiple pieces or large bundles exceeding 5 inches in height, we recommend placing the items in a corrugate box." Also "a box that is too small can cause excessive wrinkling". `verified`
  - Declared value: "The first $100 of value in your shipment is included in your shipping rate at no extra charge as part of our standard $100 limit of liability." `verified`
  - "Declared value is not shipping insurance." `verified`
  - "As the shipper, it's your responsibility to prove any actual damages." `verified`
  - "No matter the amount you declare, our liability won't exceed your shipment's repair cost, its depreciated value, or its replacement cost—whichever is less." `verified`
  - "If a shipment is improperly packaged and/or packed and is subsequently damaged, FedEx will not be deemed at fault." `verified`
  - "You can purchase insurance from a third party, but you can't purchase it from FedEx." `verified`
  - Claims must be made "in writing"; the FedEx claim FAQ itself was walled.
- **Steal this:**
  - The "depreciated value" ceiling matters for vintage. A carrier can value a 1960s brass lamp below your retail price, which is a reason to prefer third-party insurance that pays against the invoice. `inferred`
  - The size formula: wrapped size plus 3 to 5 inches per side.
  - Fashion: face-down fold in thirds, a polybag, muslin or acid-free tissue.

## 4. The UPS Store: packing services and artwork pages

- URLs: https://www.theupsstore.com/pack-ship/packing-services (`d2-upsstore-packing.md`), https://www.theupsstore.com/pack-ship/artwork (`d2-upsstore-artwork.md`).
- Evidence, verbatim:
  - "As long as your items are packed by a participating The UPS Store, using materials purchased at that location, and shipped via UPS®, your shipment will be covered by our Pack & Ship Guarantee". `verified`
  - Reimbursed for "The item's value (subject to the lesser of actual value, replacement or repair cost)", "The full retail price you paid for packaging materials and services", and "Your cost for shipping". `verified`
  - The artwork page lists "Glass Shipping" under custom boxes and crates. `verified`
- Not found: the price of the service, or the guarantee's full terms (the linked page was not read).
- **Steal this:** the highest-value mirror or framed piece can be packed by them under a written guarantee. Treat the fee as a line in the shipping price once you have a quote.

## 5. Etsy: shipping setup, calculated shipping, free shipping, USPS labels, label insurance, Purchase Protection

- URLs and raw files:
  - `help.etsy.com/.../115014115187-How-to-Set-Up-Shipping-Information` (`d2-etsy-shipping-setup.md`)
  - `.../115013946647-How-to-Set-Up-Calculated-Shipping` (`d2-etsy-calculated.md`)
  - `.../360024198553-How-to-Offer-Free-Shipping` (`d2-etsy-free-shipping.md`)
  - `.../360000336887-USPS-Shipping-Labels-on-Etsy` (`d2-etsy-usps-labels.md`)
  - `.../360001988847-Insurance-and-Claims-for-Shipping-Labels` (`d2-etsy-label-insurance.md`)
  - `.../7471925990807-Etsy-s-Purchase-Protection-Program` (buyer-facing, `d2-etsy-purchase-protection.md`)
  - `.../5850122619287` (seller-facing, `d2-etsy-seller-pp.md`)
- Evidence, verbatim:
  - Shipping setup: "choose **Free shipping** or **Fixed price**". `verified`
  - "If you're located in the US or Canada and you ship your orders with the USPS, Global Postal Shipping, or Canada Post, you can use calculated shipping on Etsy." `verified`
  - "Enter the size of the item after it's been prepared for packaging but not yet packaged (for example: folded, but not boxed)". `verified`
  - "Calculated shipping automatically calculates the smallest and cheapest package to use for each order". `verified`
  - "You may choose to incorporate any package or handling fees into your listing item price." `verified` (no handling field)
  - "If the item size is greater than any of the preferences you've set up, we'll use the item's dimensions as the package size." You can add custom package preferences. `verified`
  - Too-big items can use fixed rates: "The package is bigger than the carrier's maximum dimensions (furniture, for example)". `verified`
  - USPS labels: "If you record a different size or weight of your parcel than USPS when purchasing labels from Etsy, USPS will refund you the difference if you overestimated, or charge you if you underestimated." `verified`
  - USPS insurance on Etsy: "Includes $100 insurance: Ground Advantage®, Priority Mail® and Priority Mail Express®". `verified`
  - Rate note: "Starting April 26, USPS is implementing a temporary 8% rate increase for select shipping services... The increase is expected to last through January 17, 2027." `verified`
  - Cubic pricing: package must weigh "less than 20 pounds", measure "up to 0.5 cubic feet for Priority Mail® and 1 cubic foot for Ground Advantage®", and have "sides less than 18 inches". `verified`
  - Extra $4 USPS fee for "Packages whose contents cause the parcel to roll or lose integrity". `verified`
  - Label insurance: "All FedEx labels purchased through Etsy come with up to $100 of liability insurance." Same wording for UPS. `verified`
  - "you have the option to add shipping insurance for up to $5,000 USD. Parcel insurance on Etsy is provided by Shipsurance Insurance Services, Inc." `verified`
  - Free shipping guarantee: applies to "An individual item $35 USD and up" or "An order with a total cost of $35 USD and up". "Once set up, the free shipping guarantee is also applied to new listings that are over $35 USD". It is opt-in. `verified`
  - Etsy's own pricing example: "Imagine that you sell a $35 item, and you currently charge a $5 flat rate to ship it. By adjusting the item price to $40, you recover your shipping cost without charging a separate shipping fee." `verified`
  - Buyer page: refund when an item "Arrives damaged" or "Differs significantly from the item description or photos". A buyer can ask Etsy to step in once "it's been 48 hours since you first messaged the seller". `verified`
  - Seller page: "Etsy will cover up to $250 of a refund... and any remaining amount will be charged to the seller." `verified`
  - Seller page: "Their item arrived damaged (for the first instance per calendar year)". `verified`
  - Seller page: "You obtain insurance from a third-party source, or have carrier and/or payment processor coverage. We ask that you first submit a claim to your primary source of coverage instead." `verified`
  - Eligibility lines: "You responded to the buyer's Help with Order message within 48 hours", "The order was shipped within your stated processing time", and "matches the photos and description". `verified`
  - "To help protect the full order value, consider purchasing shipping insurance for orders over $250." `verified`
  - "For cases opened prior to May 7, 2026, refer to the... policy in effect at that time." `verified`
- **Steal this:** the opt-in free-shipping rule and Etsy's own "build shipping into the item price" example. The Etsy-reported 48-hour reply window goes on the card and in your own habits. The "matches the photos" line is why condition-grade photos double as claim defense.

## 6. Shopify: shipping rates, insurance, claims

- URLs: `help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates` (`d2-shopify-rates.md`); `.../shipping-labels/shipping-insurance` (`d2-shopify-insurance.md`); `.../shipping-carriers/shipping-claims` (`d2-shopify-claims.md`).
- Evidence, verbatim:
  - Rate types are "Flat rates" (flat, order amount, weight) and "Carrier or app calculated rates". `verified`
  - "Most merchants charge a single flat rate per order regardless of the number of products." `verified`
  - "You can use built-in carrier integrations that are available on all plans, such as USPS in the United States". The US table lists USPS, DHL and UPS. Connecting your own UPS or FedEx account "requires specific Shopify plans or an additional monthly fee". `verified`
  - "Handling fee: enter a percentage or a fixed amount to add to the carrier rate. You can use this to account for packaging and handling costs." `verified`
  - "You need to enter accurate product weights to ensure accurate carrier-calculated rates". `verified`
  - Insurance: "up to $5,000 USD". "up to $200 USD of shipping insurance is automatically included on each eligible label" only with Shopify Payments and a Grow, Advanced or Plus plan. Domestic premium "$0.89 USD per $100 USD of coverage". `verified`. Do not apply that rate to Etsy; Etsy's rate is not captured.
  - "any claims for lost, damaged, or stolen shipments should be filed with Shipsurance and not the carrier." Also "does not stack or combine with coverage provided by the carrier." Claims run "up to 120 days from the shipping date". `verified`
  - "USPS First Class Mail shipping service isn't eligible for insurance." `verified`
- **Steal this:** the handling-fee field exists, so when you add Shopify, use a percentage or fixed fee to carry the materials cost.

## 7. Shipsurance terms (Shopify and Etsy versions)

- URLs: https://www.shipsurance.com/shopify/terms_t (`d2-shipsurance-terms.md`); https://www.shipsurance.com/etsy/terms (`d2-shipsurance-etsy-terms.md`).
- Evidence, verbatim:
  - Exclusions (both versions): "neon items", "any stone or ceramic slabs", "windows, plate glass, stained glass, float glass". `verified`
  - "Loss, damage, shortage, or non-arrival of any parcel or freight and its contents which is addressed incorrectly or packed insufficiently to withstand the normal rigors of transit." `verified`
  - "Loss, shortage, or non-arrival... when it bears a descriptive label or packaging which describes, or alludes to, the nature of the contents." FAQ: damage in such packaging is covered; loss, shortage and theft are not. `verified`
  - Claim rules: "All packaging material and damaged goods must be kept in the original form as received... photographs will be required. Failure to comply will result in the denial of the claim due to insufficient packing." `verified`
  - "Concealed damage allows for the discovery of loss or damage up to 15 days after final delivery." `verified`
  - Filing: a claim form, "a copy of the carrier's tracer form, a copy of the invoice or recent appraisal, photos of damaged goods and packaging, a repair estimate, a claim statement signed by the recipient", within 120 days of shipment. `verified`
  - Limits: $5,000 per package on DHL, FedEx, UPS and USPS; $1,000 per package on Ground Economy and Ground Saver. `verified`
- **X verified, Y need review:** the exclusion list is verified. Whether it removes a framed mirror, a stained-glass lamp shade or a vintage neon piece is **needs review**. I read the words, not Shipsurance's interpretation. Email Shipsurance with a photo of each class.
- **Steal this:** the plain outer box, and the signed statement from the buyer, which belongs in your claim kit.

## 8. Supplies and costs: Uline and the free sources

- Uline URLs (all captured 2026-10-29; the mirror-box page footer stamps "10/29/2026"):
  - Artwork/Mirror Boxes (`d2-uline-mirror-boxes.md`)
  - Deluxe Artwork Shippers (`d2-uline-artwork-shippers.md`)
  - Bubble Roll S-2194P (`d2-uline-bubble-roll.md`)
  - Double-wall box S-4731 (`d2-uline-dw-box.md`)
  - Tall box S-4713 (`d2-uline-tall-box.md`)
  - Peanuts S-1128 (`d2-uline-peanuts.md`)
- Evidence, verbatim from the tables, all `verified`:
  - S-4768 Small Art/Mirror, 28 x 5½ x 38", 200#: $5.83 at 5-25, bundle 20.
  - S-4554 Medium Art, 36 x 5 x 30": $4.54, bundle 20.
  - S-4552 Small Art, 24 x 5 x 18": $2.09, bundle 25.
  - S-4832 4-piece mirror/art box, 30 x 3½ x 40": $11.64.
  - Telescopic 2-piece boxes run $12.62 to $22.81.
  - The table's footnote marks some boxes "SHIPS VIA MOTOR FREIGHT". That describes how Uline delivers the empty box, not a limit on the packed item.
  - Uline says "Corrugated and foam Frame Protectors available" (no price captured).
  - Deluxe Artwork Shippers: "Approved by most major air and ground carriers, including UPS and FedEx®." S-17580 (fits a 14 x 19 x 2" frame) is $58 at 1, $50 at 10+. Larger double-wall units run $131 to $299+.
  - Bubble roll S-2194P, 3/16", 12" x 300': $67 at 4, $63 at 8, $61 at 12+, "SOLD IN FULL BUNDLES" of 4 rolls.
  - Double-wall S-4731, 18 x 18 x 18": $5.49, bundle 10.
  - Tall S-4713, 12 x 12 x 52": $5.88 at 15, bundle 15.
  - Peanuts S-1128, 7 cu ft bag: $25 each at 1, $21 at 20+.
- `computed` from those prices (not a quote):
  - Minimum outlay: bubble $268 (4 rolls at $67), double-wall boxes $54.90 (10 at $5.49), Small Art/Mirror boxes $116.60 (20 at $5.83), tall boxes $88.20 (15 at $5.88).
  - Bubble costs $0.20 to $0.22 per linear foot of the 12" roll.
  - A 12 x 12 x 12" inner box inside an 18 x 18 x 18" outer leaves 4,104 cubic inches, about 2.4 cubic feet. At the quoted peanut price that is roughly $7.13 to $8.48 of fill, more than the box itself.
- Free sources, `unverified` (anecdote only):
  - Reddit r/LifeProTips: "try your local liquor stores first. Most stores are happy to give away boxes for free". A commenter says "I love the liquor boxes bottle divider cardboard insert things... so great for packing dishes, especially glasses, cups, and mugs."
  - Etiquette from the same thread: ask which day their delivery is, "you might have to come in same day as our delivery", and "please don't harass the workers over the 'types' of boxes you want."
- UPS and USPS disagree on reused boxes; see "Where sources disagree" below.
- **Steal this:** use liquor-store boxes and their cell dividers as **inner** cells and inner boxes only. Buy the outer box new. Hold the Uline order until you know your monthly mix, because of the bundle minimums.

## 9. Lamp-specific guidance: Lighting New York

- URL: https://lightingnewyork.com/k/lighting/wall-lights/lamps/how-to-ship-lamps (`d2-lightingny-lamps.md`). This is a lighting retailer's marketing page, not a carrier.
- Evidence, verbatim:
  - "Disassemble the Lamp: Carefully remove the lampshade, bulb, and any detachable decorative elements. Wrap each item separately in bubble wrap and secure with tape." `verified`
  - "Place the shade in a separate box". `verified`
  - "Neatly coil the lamp cord and secure it with a zip tie or tape." `verified`
  - "Photograph the lamp before packing to document its condition." `verified`
  - "Glass lamps are extremely fragile... consider double-boxing for added security." `verified`
- **Steal this:** the disassembly order and the pre-pack photo. Harp and finial are `inferred` from "detachable decorative elements" plus FedEx's "small sealable bag" rule.

## 10. Seller anecdotes: eBay community, Reddit r/EtsySellers

- URLs: eBay community threads (`d2-ebay-fragile-glass.md`, `d2-ebay-rant.md`); https://www.reddit.com/r/EtsySellers/comments/1982f35/broken_item_during_shipping/ (`d2-reddit-etsy-broken.md`). All of this is `unverified` (forum posts).
- Evidence, verbatim:
  - A glass seller: "I do not mark my packages "Fragile."" and "I wrap the glass in bubble-wrap until I cannot feel a hard edge anywhere. Then I center it in a good box so that there's at least 2 inches of space between the item and all the walls of the box".
  - The same seller: "Items that are more fragile than usual get double-boxed, with the inner box being about 4 inches smaller, all around, than the outer box."
  - The same seller: "Air pillows are not safe for glass because they usually deflate when the airplane reaches a higher altitude".
  - Another poster: "QUIT WRITING FRAGILE on your packages. It's making a target."
  - r/EtsySellers: "Always ask for photos and tell customer it is for insurance purposes." and "a replacement for a damaged item should never be contingent upon the customer returning the broken one."
- **Steal this:** "wrap until you cannot feel a hard edge", and don't make a refund wait on the broken piece coming back. The "Fragile = target" claim and the airplane claim are anecdotes. UPS's air-bag temperature note is the only verified backing.

## 11. Extras in the box: disco ball, insert card

- URLs:
  - Amazon listing 40-pack, 2" balls (`d2-amazon-mirrorball.md`), and its recommended items
  - https://www.moo.com/us/postcards/standard (`d2-moo-postcards.md`)
- Evidence, `verified` on the live pages 2026-10-29 (marketplace prices drift):
  - Amazon: "40 Pack Mirror Disco Ball, 2 Inch" at $17.99 ($0.45/count). Related listings: "17 Pcs Small Disco Balls... 3.2 Inch" at $31.99 ($1.88/count), and "4 Pack Mirror Disco Ball, 6 Inch" at $25.99 ($6.50/count).
  - MOO standard postcards, "4" x 6" Postcards", "Double-sided, full-color", "Up to 25 different designs on each Standard Postcard for FREE". Quantity table: 25 for $24.00 ($0.96 each), 50 for $41.00, 100 for $61.00 ($0.61), 250 for $100.00 ($0.40), 500 for $149.00. The captured table does not name the paper tier, so confirm that before ordering.
- `computed`: ball plus card is about $0.85 (2" ball and a 250-run card) to about $7.11 (6" ball and a 100-run card), before tissue, tape and labels.
- **Steal this:** MOO allows up to 25 designs per order at one price, so each category (lamp, glass, mirror) can have its own card. Wrap the ball like glass, because it is glass-and-mirror; that is `inferred`. It stays a sometimes-gift, never promised.

## 12. Unboxing as content

- URLs: https://www.shopify.com/blog/16991592-how-to-create-a-memorable-and-shareable-unboxing-experience-for-your-brand (`d2-shopify-unboxing.md`); https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking (`d2-ftc-endorsement.md`).
- Evidence, verbatim:
  - Shopify: "include a handwritten note with every order."
  - Shopify: Pela's "card insert" includes "a hashtag that customers can quote when sharing social content". `verified`
  - Shopify: "Encourage customers to share unboxing experiences on social media... with incentives such as discount codes". `verified`
  - Shopify: "In 2023, videos with the word "unboxing" in the title received more than 25 billion views on YouTube." `unverified` (secondhand figure, citing YouTube).
  - FTC: "The answer depends on whether knowing about that gift or incentive would affect the weight or credibility your readers give to your recommendation. If it could, you should disclose it." `verified`
  - FTC: "Even an incentive with no financial value might affect the weight or credibility of an endorsement and would need to be disclosed." `verified`
- **Steal this:** one unboxing film does two jobs, content and claim evidence (idea 1 below). If you ever give a creator a free piece, or offer a discount for an unboxing post, that is an FTC disclosure question.

---

## Where sources disagree ("X verified, Y need review")

1. **Marking the box "Fragile".** FedEx says "Always mark the box with "Fragile"" (verified), but its furniture page says "We cannot ensure compliance with markings" (verified). Sellers say stickers draw rough handling (unverified). **X verified, Y need review.** Standard: pack as if the sticker does nothing. If you use one, use "Fragile" and never a word that names the contents (Shipsurance, section 7).
2. **Cushion depth.** UPS general floor is 2 inches (verified). FedEx wants 3 inches wrap on the item and 3 inches around the inner box (verified). UPS two-box is 3 inches per side by its 6-inch rule (verified). **They agree at 3 inches for glass; 2 inches is the floor.**
3. **Reusing boxes.** The UPS PDF says "Avoid re-using boxes." (verified). USPS allows reuse if old markings are covered, with the caution "boxes can weaken" (verified). A reddit thread says liquor stores give boxes free (unverified). **X verified, Y need review.** Standard: free boxes only as inner cells and inner boxes; outer box is new.
4. **Etsy coverage amounts.** The buyer page promises "a full refund" (verified). The seller page says Etsy covers "up to $250" and the rest is charged to the seller (verified). Both are true: the buyer is made whole, and the excess lands on the seller. Reddit's "one damaged claim per year" is now **confirmed** as "first instance per calendar year" (verified), and the $250 cap is new information.
5. **Where to claim.** Etsy: claim from other coverage first (verified). Shopify: if Shipsurance covers the label, claim with Shipsurance "and not the carrier" (verified). Shipsurance: do not file with the carrier (verified). **No conflict, but the order matters:** insurer first, carrier never (if insured), Etsy protection for what's left.
6. **Insurance defaults.** USPS Priority Mail and Etsy's Ground Advantage list: $100 included (verified). Etsy FedEx and UPS: $100 liability (verified on Etsy's page; I did not read UPS's own). Shopify Grow and up with Shopify Payments: $200 included (verified). These do not stack with each other or with the carrier (verified, Shopify).

---

## Deliverable 1: Packing standard by item type

Common to all (verified sources named): use a rigid, new outer box; 2-inch tape, H-seal, three strips top and bottom; no masking, duct, cellophane or string; remove or cover old labels; label on the largest face; duplicate address label inside; the outer box says nothing about the contents.

**Glass (pink, cut, pressed)**
1. Wrap each piece individually, no nesting, until no hard edge can be felt (eBay seller, `unverified`), minimum 3 inches of air-cellular thickness (FedEx).
2. Use liquor-store cell dividers or foam as inner cells (the reddit tip, `unverified`).
3. Double-box: inner box in the middle, outer box 6 inches larger each way (UPS), 3 inches of peanuts or crumpled paper all round (FedEx).
4. No air bags or air pillows with cut glass (UPS sharp-edge caveat, `inferred`).
5. Shake test; nothing may move. Photograph packed and open (`inferred` from DMM 609).

**Lamp**
1. Photograph before packing (Lighting NY).
2. Take off shade, bulb and loose parts; wrap each separately (FedEx, Lighting NY).
3. Harp: bubble-wrap flat, then bag with the finial in a small sealable bag, taped inside the base box. `inferred` from FedEx's hardware bag and Lighting NY's "detachable decorative elements".
4. Base: heavy ones get extra layers and cardboard reinforcement (Lighting NY, marble). Coil the cord and zip-tie it.
5. Shade: its own box, "slightly larger than the shade" (Lighting NY), then the double-box.
6. Box size is wrapped size plus 3 to 5 inches per side (FedEx). A 12 x 12 x 52" tall box is available for floor lamps (Uline).
7. Stained-glass or neon lamps are an insurance problem; see the checklist.

**Mirror**
1. Purpose-built mirror and art box (Uline S-4768 or S-4554); telescoping 2-piece box for large ones.
2. Frame protectors on the corners (Uline lists them).
3. Wrap the face and back; nothing may touch the glass.
4. Packing of mirrors beyond that is **not verified this session** (the Home Depot guide was walled); use a shop-packed option for the best pieces.
5. Over 36 inches, consider local pickup or Hollie's own delivery. USPS limits are 130 inches length plus girth, and under 108 for Priority Mail.

**Framed art**
1. Same box family as mirrors; foam or corrugated frame protectors.
2. For anything valued over $500, FedEx recommends a Premium Art Box, and keeping declared value at or under $1,000.
3. For the best pieces, pay The UPS Store or FedEx Office to pack and ship under their written guarantee.

**Fashion**
1. Fold face-down, sleeves back, in thirds (FedEx).
2. Add acid-free tissue or muslin for delicate pieces, in a polybag (FedEx).
3. One or two small items can go in a poly mailer; bundles over 5 inches high go in a box (FedEx).
4. A garment box or wardrobe box suits high-value pieces (FedEx).
5. A sealed polybag matters more in Southwest Florida humidity (`inferred`).

Not covered here: rugs and chairs. FedEx says to roll a rug on a core and box or bag it, and its furniture page covers chairs.

## Deliverable 2: Shipping-price rule

1. **Fixed shipping classes, not live rates, on Etsy.** Set A (small glass), B (table lamp or one pack), C (mirror or art box), D (oversize: local pickup or custom quote). Reasons: calculated shipping is USPS-only, uses the item size "when packed", picks the "smallest and cheapest" package, and has no handling field. If it guesses smaller than the real double-box, USPS charges the difference to you.
2. **Charge = a real label quote for the real outer box, plus a materials line, plus the insurance premium share.** Get the label quote by pricing one test box per class. The materials line comes from your actual supplies at the quoted prices above.
3. **Free shipping only by building it into the item price** (Etsy's $35 to $40 example). Do not opt into the free-shipping guarantee casually: once set up it applies to "an individual item $35 USD and up" and to new listings over $35, which is almost everything in the shop.
4. **Insure by value.**
   - Up to $100: use the included coverage.
   - Over $100 and fragile: buy insurance to the sale price.
   - Over $250: always insure, because Etsy's protection stops at $250 and only covers the first damage per calendar year.
   - Put the premium share in the shipping charge.
5. **On Shopify later:** flat or weight rates per class, or carrier-calculated with a percent or fixed handling fee for materials. Check that Shopify Payments plus the Grow plan gives the $200 included coverage.
6. **Review date.** Etsy notes an 8% temporary USPS increase through January 17, 2027. Re-quote every class on January 18, 2027.

## Deliverable 3: Claims checklist

**Before it ships**
- [ ] Condition-grade photos on the listing (Etsy covers "differs significantly from the item description or photos").
- [ ] Photograph the item before packing, packed inside the box, the sealed box, and the label close-up (UPS's three photos plus the pre-pack shot).
- [ ] Keep the sale receipt as proof of value (USPS lists a "sales receipt, paid invoice or bill of sale").
- [ ] Ship inside your stated processing time and upload tracking (Etsy eligibility).
- [ ] Plain outer box; duplicate address label inside.
- [ ] Insure per the rule. Before listing any stained-glass lamp, neon piece or mirror, get Shipsurance's written answer.

**What the buyer card asks for**
- [ ] Open it on camera. Photograph the open box before pulling anything out.
- [ ] Keep every scrap of box and packing until the claim is closed (UPS, USPS, Shipsurance all deny claims otherwise).
- [ ] Message within 48 hours if anything is wrong. Etsy gives sellers 48 hours to reply, and Shipsurance's hard limit is 15 days from delivery.

**When something is broken**
- [ ] Ask for the three photos if you don't already have them (UPS set).
- [ ] Refund or replace the buyer first; don't make it wait on the insurer or on the broken piece coming back (reddit advice, `unverified`).
- [ ] Insured through Shipsurance: file there only, within 120 days of shipment, with the claim form, tracer form, invoice, photos, repair estimate and the buyer's signed statement.
- [ ] Not insured: file with the carrier. UPS within 60 days of scheduled delivery; USPS within 60 days of mailing, "immediately"; FedEx in writing, with proof of damage and proof FedEx is at fault.
- [ ] On Etsy, claim from any other coverage first. Etsy then covers up to $250 for the first damage of the calendar year.

**Clocks, tightest first:** 15 days from delivery (Shipsurance, concealed damage); 48 hours (Etsy seller reply); 60 days (UPS from scheduled delivery, USPS from mailing); 120 days (Shipsurance from shipment).

---

## Recommendation for Holliewood & Vine

**Do now (no accounts, no fee)**
- Adopt the packing standard above as a one-page sheet. Photograph every pack-out.
- Start collecting liquor-store boxes and cell dividers for inner cells. Ask for the delivery day. Never as the outer box.
- Keep the outer box plain. Move all branding inside.
- Email Shipsurance a photo of each class (framed mirror, stained-glass lamp shade, neon, cut-glass lamp) and ask for a written yes or no.
- Draft the buyer card: open on camera, keep the box, tell Hollie in 48 hours.
- Write the shipping classes A to D and the insurance rule.
- Decide the gift policy: a ball only sometimes, wrapped as glass, never promised.

**Needs an account, a fee or a professional**
- **Account:** Etsy or Shopify labels (insurance, discounted postage, the real Etsy Shipsurance rate); a Uline account (bundle minimums: $268 for bubble alone).
- **Fee:** MOO cards ($61 per 100 or $100 per 250); a UPS Store or FedEx Office packing quote for the best mirrors and art.
- **Fee:** the first test label per class to set the fixed prices.
- **CPA, Florida:** whether shipping and handling charges are taxable on a sale, and how gifts given away are treated. I did not research this.
- **Lawyer (optional):** the terms-of-sale wording about reporting windows and risk of loss, and the disclosure wording for creator gifting.

---

## Ideas for Hollie

1. **"Open it on camera."** The card line that makes the unboxing the claim. (UPS three photos; Shipsurance photos; Shopify unboxing)
2. **Plain brown outside, everything inside.** The outer box says nothing; the card, tissue and gift do. (Shipsurance descriptive-packaging exclusion)
3. **A 15-second packing reel before sealing.** It is content and claim evidence. (DMM 609 items 8, 15, 18; Shopify "create your own unboxing content")
4. **A "parts bag" tied to every lamp, labeled HARP, FINIAL, BULB.** It reads as a gift and keeps the pieces together. (FedEx hardware bag; Lighting NY)
5. **One card per category, same print run.** Lamp care, glass care, mirror care, up to 25 designs at one MOO price. (MOO)
6. **A hashtag on the card, no incentive.** If a discount ever rewards posts, disclose it. (Shopify Pela example; FTC)
7. **Make friends with the nearest wine shop.** Ask for dividers on delivery day. Bring a thank-you. (Reddit r/LifeProTips, `unverified`)
8. **Sell "white-glove packing" as a line item for the best pieces.** The UPS Store or FedEx Office packs; the guarantee is the proof. (UPS Store; FedEx artwork)
9. **Wrap the disco ball like glass, in the void space.** Never promised. (Amazon prices; UPS cushioning rules)
10. **A "how this traveled" line on the listing.** "Ships double-boxed, insured to sale price." It also supports the "matches description" test. (Etsy seller protection)

## Gaps I could not fill
- No postage rates, no Etsy Shipsurance premium rate, and no UPS Store packing fee.
- The FedEx claim page, the USPS FAQ, the Etsy legal policy and the Etsy handbook were walled.
- No carrier page on mirror packing method (tape, corner boards). The Home Depot guide was walled.
- Whether Shipsurance treats a mirror or a stained-glass lamp as excluded is unanswered.
- Florida tax on shipping charges and gifts is untouched.
