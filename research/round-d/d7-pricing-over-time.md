<!-- Saved verbatim by the parent Opus session from agent d7's final message, 2026-10-29 (the harness refuses subagent report writes; this one arrived as a persisted tool result). -->

# d7: pricing and selling one-of-ones over time

Agent d7, accessed 2026-10-29. Raw captures: `research/round-d/raw/d7-*` (about 70 files; walls and failed fetches are kept there on purpose). Parent: save this report as `research/round-d/d7-pricing-over-time.md`.

Method: SearXNG (`tools/search.sh`) for URLs, which was weak on plain-English queries (several returned dictionary pages), then crawl4ai (`tools/crawl.sh`) for about 55 pages, about 45 of them read or grepped for evidence. That is above the 15-25 target because the lane has eight sub-questions: three platforms' offer tools, markdown ladders, drop days, bundles/holds/layaway, shipping, price display plus law, and an hours check. WebFetch was a fallback five times. It was used for Emily Henderson after crawl4ai walled, for the Wadhwa and Zhang abstract, for the NBER PDF (it could not parse the PDF, but saved it, and I read it with `pdftotext`), and for Furnish Green (HTTP 429). WebSearch was used six times for leads only, and anything resting only on a snippet is tagged `unverified`. Notes on the fallback captures are in `d7-webfetch-websearch-notes.md`.

Tags: `verified` = read on the live page this session through crawl4ai. `verified (WebFetch)` = read through WebFetch's summarizing model, which is a lower grade. `inferred` = my reading or my arithmetic. `unverified` = a snippet or a claim I could not open. `prior capture` = from `research/pricing/` or `research/fabulous-from-online/` and not re-read. I used those for comps, never for vendor policy. Hours in section F are my estimates, tagged `inferred` throughout.

Walls and dead pages (not retried, no Patchright): ResearchGate (270 bytes), PsycNET (87 bytes, Incapsula), OUP (0 bytes), the NBER PDF crawl (4 bytes), Etsy seller handbook (4 bytes), Emily Henderson crawl (517 bytes), 1stDibs lamps (32 bytes), Furnish Green `old.` subdomain (maintenance page) and furnishgreen.com (HTTP 429 via WebFetch). Thin or unusable: wowedesign.squarespace.com (a 404 page), Adrienne's Domastudio portal (login shell), Chairish lamp collection (only 4 prices rendered), R&R product list (no prices rendered), Black Brick shelf page (no price in the capture, so I did not cite it), and Shopify's parent pricing page (1 KB; I used the child page).

---

## TL;DR

1. **Offers pull the realized price to about three quarters of list, and the data says so.** eBay's Best Offer dataset (88.4 million listings) shows buyers' average first offer at 61% of list and the modal first offer at half of the Buy It Now price. Sellers accept the first offer 33% of the time, decline 40% and counter 27%. Conditional on bargaining, the average sale price is 73% of list. Best-Offer-enabled listings carry much higher list prices than non-Best-Offer ones, a correlation the authors report, not a proven cause. Chairish says "more than 50%" of its transactions run through Make an Offer and sets a 50%-of-list floor. Etsy's tool is opt-in with a maximum discount you pick. If the shop takes offers freely, the list price is already an opening bid. `verified`.
2. **The ladder is the quiet version of the same cushion.** Both furniture shops that publish a ladder end near 30% off by day 90. Furniture Consignment Gallery goes 10/20/30% off the original at 30/60/90 days. The Millionaire's Daughter goes 10%, a further 10%, then a further 15%, which compounds to 31% off. Chairish tells sellers to check at 10-14 days, try 10% or new photos, and reassess at 30. A vendor blog's steeper 20-25% / 50% is the dissent. `verified`. The in-repo comps are mostly asking prices, and 14 of the 19 home-item rows in `research/pricing/SUMMARY.md` are "low" confidence. So the ladder doubles as price discovery.
3. **No online one-of-one shop with a named weekday price drop was found. This is a gap, not a negative.** Verified near-matches are Beyond Retro's weekly colour-tag deal (50-75% off in UK stores), FCG's "Recently Reduced" page, and Chairish's markdown, which notifies favoriters and bumps the listing to the top of its category and the Sale page. "Monday markdowns" at Furnish Green is a search snippet only (`unverified`). Tie the drop to the weekly drop the shop already decided on.
4. **"Was / now" is a legal claim, not just a design choice.** 16 CFR 233.1 says the former price must be "the actual, bona fide price at which the article was offered to the public on a regular basis for a reasonably substantial period of time". For a one-of-one that never sold at the higher price, the safe line is "Listed at $X on [date]. Now $Y." Never raise a price after a drop. Chairish blocks that by design. `verified` for the text. How it applies to Hollie needs a lawyer.
5. **$245 vs $250 is a non-decision. $295 vs $300 and $95 vs $100 are not.** The left-digit effect "occurs only when the leftmost digits of the prices differ (e.g., $2.99 vs. $3.00)". $9 endings raised demand in three catalog field tests, more for new items and less with "Sale" cues. Rounded prices "encourage reliance on feelings". `verified` / `verified (WebFetch)`. The FFO prices of $95 and $295 already sit under a hundred boundary, and $750 is round.
6. **Holds, layaway and bundles all exist in vintage, with small deposits and long windows.** Four vintage sellers run 15% non-refundable deposits (Sands of Time, Trademark Antiques), 25% down with a $300 minimum (Garlands), or 50% plus three monthly payments (A Dog's Tale). Payoff windows are 3 to 10 months. Chairish designer holds auto-expire at 48 hours. Etsy bundles take up to 3 listings and do not stack with sales. An accepted Etsy offer "does not reserve the item". `verified`.
7. **Free shipping and heavy, fragile pieces fight each other. Do not switch on Etsy's free shipping guarantee shop-wide.** It covers any US item or order of $35 and up. Etsy's own advice for furniture is to say shipping varies and quote it. Chairish's buyer pays unless the seller opts into free, and fragility, packing and an item that cannot be taken apart all raise the rate. Shopify can do price-based and weight-based tiers. `verified`.
8. **The FFO prices are launch pricing, not steady-state pay, and Casting Call is a deposit, not a labor fee.** At my likely hours (2.5 / 6 / 12.25) the tiers yield about $38 / $49 / $61 gross per hour. That is under the price book's own implied virtual rate of $100 (the $150 in-person Cameo at c3's 1.5x) and under R&R's $75. Because the $95 is credited toward the piece and a miss becomes store credit, Hollie's cash for a Casting Call is the 10% sourcing line ($9.50 on a $95 lamp, $27.50 on a $275 piece) or the margin on her own stock, and $0 on a miss. `inferred` hours, `verified` anchors. Section F.

---

## A. Offer features

### A1. Etsy, "How to Use the Make an Offer Tool"
- URL: https://help.etsy.com/hc/en-us/articles/16792774373143-How-to-Use-the-Make-an-Offer-Tool . Raw: `d7-etsy-make-offer.md`.
- Evidence:
  - "Make an Offer is an optional pricing tool you can use to allow buyers to make price offers on some or all of your listings. You can set a maximum discount amount you'll consider from buyers, so they can't make offers that are below the amount you choose." `verified`
  - "At the moment, Make an Offer is only available for sellers and buyers who have their currency set to USD, and is not available on the Etsy Seller app." `verified`
  - "Select the maximum discount you're willing to consider from buyer offers, or choose **Receive all offers**." The page does not list the discount options. `verified`
  - "Once you send a final price, a buyer can't make a new offer without going to your listing and restarting the offer process from the beginning. ... the buyer has 48 hours to accept the offer." `verified`
  - "Accepting a buyer's offer does not make them obligated to purchase the item. It also does not reserve the item for the buyer, so it can still sell out." `verified`
  - "Changing the price of your item will void any open offers from buyers, and they will need to resubmit their offer." `verified`
  - "With the exception of free shipping offers, other sales and discounts can not be combined with buyer offers ... whichever is the highest discount will be applied". `verified`
  - Offer messages "are not subject to the Star Seller 24-hour response measurement." `verified`
- Consequences for Holliewood & Vine (`inferred`):
  - The Phase 1 plan lists from the phone, and this tool is not in the Seller App, so offers must be handled on a desktop.
  - A weekly markdown wipes any open offer on that piece.
  - Turning Make an Offer on for a listing is a manual per-listing edit, so "offers open at day 30" is a Drop Day chore.
- **Steal this:** the "maximum discount" cap, and the Etsy-supplied 48-hour pay window for a policy line.

### A2. Etsy, "How to Set Up Sales and Discounts"
- URL: https://help.etsy.com/hc/en-us/articles/115014260108-How-to-Set-Up-Sales-and-Discounts-for-Your-Shop . Raw: `d7-etsy-sales-discounts.md`.
- Evidence:
  - "Percentage off: Offer any percentage off between 5% and 75% off the list price ... The percentage off must be a whole number." `verified`
  - Bundles: "Add up to 3 listings to offer together." "Listings can only be part of one discounted bundle at a time." "Bundle discounts will not stack with other sales and promotions". `verified`
  - Targeted offers go to opted-in shoppers: abandoned cart ("in their cart for more than 2 hours", expires 60 days), favorited item (expires 60 days), interested shopper ("once every 30 days", expires 7 days) and thank you (expires 1 year). `verified`
  - "When you run a sale on Etsy, you are responsible for following applicable consumer protection laws and Etsy's policies." `verified`
  - The sale best-practices guide it links (seller-handbook article 1450964704111) returned 4 bytes. `unverified`
- **Steal this:** Etsy's favorited-item offer is the platform-run "you looked, now here's 10%" email, and it is the only discount that needs no policy text from Hollie. The cap is whatever she types in.

### A3. eBay, "Adding Best Offer to your listing and sending offers to buyers"
- URL: https://www.ebay.com/help/selling/listings/selling-buy-now/adding-best-offer-listing?id=4144 . Raw: `d7-ebay-best-offer.md`.
- Evidence:
  - "After receiving an offer, you have 24 hours to choose how to respond." "Each counteroffer expires after 96 hours". `verified`
  - Auto-responses: at or above your upper limit eBay accepts; below your lower limit it declines; between the limits it asks you. "Buyers can make up to three offers per item in most categories." `verified`
  - "You can't use automatic responses when: You've put an item on sale using the Sale event feature of Discounts Manager". `verified`
  - Seller-sent offers: "The amount must be at least 5% less than the Buy It Now price"; "Items must be in the buyer's cart for at least 2 days"; "Offers will be sent to the 30 most recent interested buyers"; "Each offer is valid for 96 hours". `verified`
  - "If you accept a Best Offer ... after any buyer clicked on one of your Promoted Listings general ads within the last 30 days, you'll be charged an ad fee". `verified`
  - Automatic offers pause if you "lower the price below the current automatic offer amount". `verified`
- Open question: whether Crosslist copies offer settings when it fans a listing out to eBay is `unverified` and needs an account. A Best Offer auto-accept on eBay could undercut an Etsy "no offers" price.
- **Steal this:** eBay's "split the difference" counter, plus the 5% minimum a seller-sent offer must beat, as the smallest gesture worth making.

### A4. Chairish, "Making Offers & Counter Offers", "Managing Offers & Counter Offers", "Reserve Prices"
- URLs: https://support.chairish.com/hc/en-us/articles/44252985370257 , https://support.chairish.com/hc/en-us/articles/44173070844689 , https://support.chairish.com/hc/en-us/articles/44170397686801 . Raw: `d7-chairish-offers-buyer.md`, `d7-chairish-offers-seller.md`, `d7-chairish-reserve.md`.
- Evidence:
  - "A significant percentage (more than 50%) of our transactions are facilitated through our Make an Offer feature". `verified`, and a vendor claim.
  - "All offers on Chairish listings must be at least 50% of the listing price of a single item." "your credit card will be charged for the full offer amount". `verified`
  - "As a Seller, you have 72-hours in which to respond to an offer". "Placing an offer does not 'hold' the item". `verified`
  - "If you are not willing to negotiate on price, please counter offers with your Asking Price." `verified`
  - Reserve Price: "Offers that are equal to or greater than your Reserve Price are automatically accepted." "Historically, we saw listings with Reserve Pricing selling 25% more, and up to 2 times faster than those without." "When creating a new listing, we set a suggested Reserve Price at a 20% discount. You may adjust your Reserve Price discount anywhere between 20%-5%." `verified`, and the 25% and 2x are Chairish's own claim.
  - "Coupon and Discount Codes ... cannot be redeemed when making an offer." `verified`
- **Steal this:** "counter with your Asking Price" is Chairish-sanctioned wording for "no", which fits a no-haggle voice.

### A5. NBER Working Paper 24306 (Backus, Blake, Larsen, Tadelis), eBay Best Offer
- URL: https://www.nber.org/papers/w24306 (abstract page, `d7-nber-w24306.md`). The PDF crawl returned 4 bytes. WebFetch saved the binary as `d7-nber-w24306.pdf`, and I extracted `d7-nber-w24306-text.txt` with `pdftotext`. The paper was later published in the Quarterly Journal of Economics (2020, 135(3), 1319-1361, per the NBER page).
- Evidence from the extracted text:
  - "approximately 88.4 million listings. Of these, 25.4 million received a bargaining offer." "The average list price (BIN) is $95, and the average sale price is 83% of the list price. ... conditional on bargaining occurring, the average sale prices comes down to 73% of the list price. We note that almost 80% of listings never receive an offer and do not sell." `verified`
  - "On average, buyers offer $86.60, which represents 61% of the list price. Bargaining is ultimately successful 45% of the time." `verified`
  - "sellers frequently decline the initial offer (40% of the time) ... Sellers accept the initial offer 33% of the time and provide a counteroffer 27% of the time." `verified`
  - "the modal initial offer is half of the BIN." "split-the-difference" is the common counter. `verified`
  - Best Offer is more common "in categories with more idiosyncratic or one-of-a-kind inventory, such as vehicles, business and industrial equipment, and collectibles". "In nearly every category, the ratio is far greater than one, suggesting that Best-Offer-enabled listings have a much higher list price than non-Best-Offer-enabled listings." `verified`
- Caveats: it covers all eBay categories, with an average list of $95, so mostly lower-priced goods. The sample years were not re-checked (a chart in the paper tabulates 2005-2015). The "higher list price" finding is correlational.
- **Steal this:** if offers are on, expect roughly 17% off on average (83% of list) and about 27% off when a negotiation happens (73%). That is why Chairish's default reserve is 20%, and why the ladder below ends at 30% off.

---

## B. Markdown ladders and public drop days

### B1. Chairish, "Marking an Item Down" and "Pricing Guidance"
- URLs: https://support.chairish.com/hc/en-us/articles/44170940096657 , https://support.chairish.com/hc/en-us/articles/44170363829009 . Raw: `d7-chairish-markdowns.md`, `d7-chairish-pricing-guidance.md`.
- Evidence:
  - "Marking your item down will notify anyone who has added the item to their favorites, and will bump your listing to the top of its category and the 'Sale' page ... there is a markdown minimum of 10%." "markdowns are permanent. Once an item is marked down, the price cannot be raised." `verified`
  - "Monitor and adjust: If views are high but saves/inquiries are low after 10-14 days, consider a 10% price adjustment or refreshed photos. Reassess at 30 days if needed." `verified`
  - "Our Curators always consider fair margins for markdowns, which typically start at about 30% more than the minimum you are willing to accept for a product." `verified`
  - "Pricing off outlier asks: Use realized sales and true comparables, not just the highest active listing." `verified`
  - "High freight costs can suppress demand; sharper pricing can offset this." `verified`
- Read of the 30% line (`inferred`): list at 1.3 times the floor means buyers are expected to land about 23% under list.
- **Steal this:** check views against saves before cutting, a permanent-markdown rule (never go back up), and a 10% minimum step so a drop is a real drop.

### B2. Furniture Consignment Gallery, "Our Consignment Terms"
- URL: https://www.furnitureconsignment.com/pages/our-consignment-terms . Raw: `d7-furnitureconsignment-terms.md`. Location not stated on the page I read.
- Evidence: "Minimum of a 60 day consignment period." "MARKDOWN SCHEDULE: After 30 days on the sales floor the price of the item will drop by 10% of the original sale price. After 60 days ... 20% of the original sale price. After 90 days ... 30% of the original sale price." "FCG has the exclusive right to negotiate with buyers and to conduct impromptu sale events, notwithstanding the scheduled price adjustments." The nav has a "Recently Reduced" collection. `verified`
- **Steal this:** the steps are a percent of the original, not compounding; the "Recently Reduced" shelf; and a reserved right to run an impromptu sale.

### B3. The Millionaire's Daughter, consignment FAQ
- URL: https://themillionairesdaughter.com/faq . Raw: `d7-millionairesdaughter-consign.md`. Location not stated on the page I read.
- Evidence: "First 30 Days: The item is listed at the initial price. After 30 Days: The price is reduced by 10%. After 60 Days: The price drops an additional 10%. After 90 Days: The price is further reduced by 15% and remains at this final price for the last month". "We keep items in our stores for up to 150 days (5 months), but most furniture sells within the first 60 days." `verified` (the second sentence is the shop's claim). Compounded: 0.9 x 0.9 x 0.85 = 0.69, so about 31% off. `inferred` arithmetic.
- **Steal this:** a final plateau. The last step is held, and the price does not keep sliding.

### B4. Aravenda, "How Long Should I Hold Unsold Consignment Items Before Markdown or Return?"
- URL: https://www.aravenda.com/blog/how-long-should-i-hold-unsold-consignment-items-before-markdown-or-return/ . Raw: `d7-aravenda-markdown.md`. This is a consignment-software vendor blog.
- Evidence: "Most consignment shops run a 60- to 90-day consignment period, with automatic markdowns at 30 and 60 days, commonly 20-25% off at day 30 and 50% off at day 60." "Higher-value categories (furniture, luxury goods) sometimes run longer windows". "Fast-turning categories like everyday apparel often compress this schedule to 30 or 45 days". The rationale it lists includes "Training customers to wait for a markdown instead of buying at full price, if discounts are unpredictable". The 30-to-90-day pattern is attributed on the page to NARTS and to a business guide, and I did not open either. `verified` that the page says it. The numbers are `unverified` as an industry norm.
- **Steal this:** write the schedule down. The page's real advice is that predictability, not the exact numbers, is what prevents disputes and waiting games.

### B5. The RealReal, consignor FAQ
- URL: https://www.therealreal.com/faq/consign . Raw: `d7-trr-consign-faq.md`.
- Evidence: "Our goal is to sell your item within 30 days of it going live on the website. Items that remain unsold after 30 days may need a price reduction". "If you do not respond to these emails within 7 days, The RealReal will automatically reduce the price of your item." Dynamic pricing: "real-time advanced pricing algorithms". That passage is about its price-review category, which the page ties to items priced $995 and up. `verified`
- **Steal this:** a 30-day clock with a human checkpoint before the cut.

### B6. Beyond Retro, "Always On" weekly colour tag
- URL: https://retail-focus.co.uk/beyond-retro-launches-always-on-weekly-colour-deal-system-keeping-quality-fashion-in-circulation-and-out-of-landfill/ . Raw: `d7-beyondretro-colour.md`. Article date not visible in the capture. UK vintage clothing chain, stores.
- Evidence: "a brand-new Weekly Colour Tag Deal System across all stores — offering customers 50% to 75% off specially marked vintage items every week. ... each week, a new colour sticker will mark the discounted pieces in store." `verified`
- **Steal this:** a weekly public rhythm tied to a visible marker. For Hollie that would be the tag colour or the neon.

### B7. Furnish Green, "Monday Markdowns" (snippet only)
- Source: a WebSearch snippet citing https://old.furnishgreen.com/?p=72440 . The page returned a maintenance screen (`d7-furnishgreen-monday.md`), and furnishgreen.com returned HTTP 429.
- The snippet said the shop "reviews its prices weekly and lowers a handful of pieces each Monday" and "5-7 pieces every Monday". `unverified`. I could not open the page.

---

## C. Bundles, holds and layaway

### C1. Chairish, "Managing Hold Requests"
- URL: https://support.chairish.com/hc/en-us/articles/44173140399121 . Raw: `d7-chairish-holds.md`.
- Evidence: "Sellers often get requests from Trade Program members (designers) to put products on hold so that they have enough time to get approvals from clients." "Designer initiated holds automatically expire in 48 hours." "While your item is on hold, other customers will not be able to add the item to their cart or make any offers". Sellers can also place a personal hold with an end date. `verified`
- Link to FFO: the design doc already has "collection pieces hold 48 hours". Chairish's designer hold is the same number from a marketplace that serves designers.
- **Steal this:** while a hold is active, the piece cannot be carted or offered on, but it can still be favorited.

### C2. Four vintage layaway policies
| Shop | Deposit | Window | Other terms | Raw |
|---|---|---|---|---|
| Sands of Time Antiquities (sandsoftimedc.com/pages/layaway-payment-plan-1) | "A non-refundable deposit of 15% of the total price" | "balance must be paid within six months of the order date or you risk forfeiture" | "Property title remains with Sands of Time Antiquities, Inc. until payment is made in full." | `d7-sandsoftime-layaway.md` |
| Trademark Antiques | 15%, "non-refundable if you decide to cancel" | "up to 10 months" | "we set the item aside exclusively for you"; layaway allowed during sales | `d7-trademark-layaway.md` |
| Garlands (shopgarlands.com/pages/layaway) | "25% down" | "6 months" | "$300 minimum, and you can combine several pieces"; "0% interest and no fees"; pieces "taken off the website" on deposit | `d7-garlands-layaway.md` |
| A Dog's Tale Collectibles | "50% at the time of purchase" | three equal monthly installments | "We remove the item(s) from inventory upon your first payment"; unpaid items are reposted; Affirm offered as an alternative | `d7-adogstale-layaway.md` |

All `verified`. The WebSearch lead said it found no furniture or lamp shop with a published layaway policy. These are jewelry, art, antiques and collectibles sellers.
- **Steal this:** take the piece off the shelf on the first payment, keep title until paid, and a minimum order that is high enough to matter.
- Etsy: no official layaway article turned up. Community threads (not read) suggest custom listings or the "Other" payment method, and one poster claims deposit listings break the terms. `unverified`. Etsy's own page says a custom listing is "for a private sale to a particular buyer" and costs the "$0.20 USD standard fee" (`d7-etsy-fees.md`, `verified`).

---

## D. Shipping and free-shipping thresholds

### D1. Etsy, "How to Offer Free Shipping"
- URL: https://help.etsy.com/hc/en-us/articles/360024198553-How-to-Offer-Free-Shipping . Raw: `d7-etsy-free-shipping.md`.
- Evidence: "A free shipping guarantee automatically applies free shipping for US buyers when they purchase ... An individual item $35 USD and up ... An order with a total cost of $35 USD and up". The page walks through setting it up, so it is a seller's choice. The smart-pricing tool raises prices "by the average amount US buyers would pay at checkout on Etsy, rounded up to the nearest dollar." Etsy's own example builds in a flat $5. `verified`
- The page does not say whether the guarantee affects search placement. That is not verified either way.
- In-repo shipping numbers (`prior capture`, `research/pricing/`): glass "budget $18-25", a projector listing with "$75.10" shipping, a rolled cowhide "about $25 to $40". A $42 crystal decanter (A12) shipped free would give away roughly 40-60% of its price. `inferred`.

### D2. Etsy, "How to Set Up Shipping Information"
- URL: https://help.etsy.com/hc/en-us/articles/115014115187-How-to-Set-Up-Shipping-Information . Raw: `d7-etsy-shipping-setup.md`.
- Evidence: "What if I sell very bulky or heavy items? If you sell very heavy items, like furniture, consider mentioning in your listing descriptions that shipping prices vary. Ask buyers to contact you before checking out for a shipping quote. Then, create a custom listing for your buyer." Calculated shipping uses weight and dimensions (USPS). "It isn't possible to set discounted rates for listings with calculated shipping". `verified`

### D3. Chairish, "Calculating Shipping Costs" and "Available Shipping Methods for Sellers"
- URLs: https://support.chairish.com/hc/en-us/articles/44246494892817 , https://support.chairish.com/hc/en-us/articles/44167972846097 . Raw: `d7-chairish-shipping-costs.md`, `d7-chairish-shipping-methods.md`.
- Evidence: "The Buyer always pays for shipping unless the seller offers free shipping on an item." Costs depend on distance, size and weight, "Fragility and packing needs" ("custom crating for fragile pieces add weight and size"), service level, and form factor ("If an item cannot be dismantled, it must ship as one large piece"). Parcel delivery limits: under 150 pounds, no longer than 108 inches or length plus girth within 165 inches. Larger items use in-home delivery. "Extremely heavy or bulky items that require special equipment (ex. cranes, etc.) will be declined." Buyers can filter for local pickup or delivery and for "Shipping Under $50". `verified`

### D4. Shopify, "Setting up shipping zones and rates"
- URL: https://help.shopify.com/en/manual/fulfillment/setup/shipping-rates/setting-up-shipping-rates . Raw: `d7-shopify-shipping-rates.md`.
- Evidence: weight-based rates, price-based rates, "offer free shipping" with a minimum order amount, and carrier-calculated rates exist. The page's examples are Shopify's, not recommendations, for instance "$5 USD for orders over $50 USD, or offer free shipping for orders over $100 USD". `verified`

---

## E. How prices are shown

### E1. FTC Guides Against Deceptive Pricing, 16 CFR Part 233
- URL: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-233 . Raw: `d7-ecfr-16cfr233.md`.
- Evidence (233.1):
  - "If the former price is the actual, bona fide price at which the article was offered to the public on a regular basis for a reasonably substantial period of time, it provides a legitimate basis for the advertising of a price comparison."
  - "A former price is not necessarily fictitious merely because no sales at the advertised price were made. The advertiser should be especially careful, however ... that the price is one at which the product was openly and actively offered for sale, for a reasonably substantial period of time ... And the advertiser should scrupulously avoid any implication that a former price is a selling, not an asking price (for example, by use of such language as, 'Formerly sold at $___'), unless substantial sales at that price were actually made."
  - "An advertiser who claims that an item has been 'Reduced to $9.99,' when the former price was $10, is misleading the consumer".
  - 233.5: "They should not offer an advance sale under circumstances where they do not in good faith expect to increase the price at a later date".
  All `verified`.
- Read for a one-of-one (`inferred`): it supports "Listed at $X on [date]" and rules out "Was sold at $X". Keep each reduction large (10% or more). Do not raise a price and then cut it.

### E2. Florida Statutes 501.203 (FDUTPA definitions)
- URL: http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.203.html . Raw: `d7-fl-501-203.md`.
- Evidence: a "violation of this part" may be based on "(a) Any rules promulgated pursuant to the Federal Trade Commission Act ... (b) The standards of unfairness and deception set forth and interpreted by the Federal Trade Commission or the federal courts". `verified`
- How 233 (a "guide", not a rule) feeds into this is `inferred` and needs a lawyer.

### E3. Thomas and Morwitz 2005, left-digit effect
- URL: https://ideas.repec.org/a/oup/jconrs/v32y2005i1p54-64.html . Raw: `d7-thomas-morwitz.md`.
- Evidence: "nine-ending prices are perceived to be smaller than a price one cent higher. First, this occurs only when the leftmost digits of the prices differ (e.g., $2.99 vs. $3.00)." "The closer the two prices being compared, the more likely is the left-digit effect." `verified` (abstract).

### E4. Anderson and Simester 2003, $9 price endings
- URL: https://ideas.repec.org/a/kap/qmktec/v1y2003i1p93-110.html . Raw: `d7-anderson-simester-ideas.md` (Kellogg listing: `d7-anderson-simester-kellogg.md`).
- Evidence: "use of a $9 price ending increased demand in all three experiments. Second, the increase in demand was stronger for new items than for items that the retailer had sold in previous years. There is also some evidence that $9 price endings are less effective when retailers use 'Sale' cues. ... $9-endings may be more effective when customers have limited information". `verified` (abstract). The experiments were catalog mailings, not antiques.

### E5. Wadhwa and Zhang 2015, rounded prices
- URL: https://academic.oup.com/jcr/article-abstract/41/5/1172/2962090 (crawl4ai got 0 bytes; WebFetch only).
- Evidence: Journal of Consumer Research 41(5), pp. 1172-1185. "rounded prices (e.g., $200.00) encourage reliance on feelings." `verified (WebFetch)`. WebFetch declined to give the full abstract. I count only those two short excerpts.

### E6. What real vintage shops' price lists look like (a small observed sample)
- Vestige Vintage (Punta Gorda, FL), `collections/all`, raw `d7-prices-vestige.md`: $200, $100, $80, $25, $20, $125, $50, $30, $70, $35, $45. Every price is a multiple of $5, and the page is mostly style boxes and a few items, so the sample is small. Sold-out items stay on the page with "Sold out". `verified`
- Mercer Vintage (Houston), `collections/all`, raw `d7-prices-mercer.md`: $385, $345, $145, $122, $125, $158, $288, $44, $545, $72, $128, $254, $178, $62. Many are non-round. `verified`
- Black Cat Interiors (design services, not vintage stock), raw `d7-blackcat-micro.md`: Shelf Styling is shown as "~~$ 150.00~~ Original price was: $150.00. $112.00 Current price is: $112.00." `verified`. That is a real strikethrough example of the "was / now" format.
- Chairish listing prices in `research/pricing/decor.md` (prior capture) are not round: a $891 ask with offers shown at $846 / $801 / $757, which are 5 / 10 / 15% off. Chairish's help pages (A4) describe a 50% minimum offer and a 5-20% reserve discount, not 5 / 10 / 15%. The two are different features, so the prior capture may be showing private offers. See section G.

### E7. Shopify, "Setting sale prices for products"
- URL: https://help.shopify.com/en/manual/products/details/product-pricing/sale-pricing . Raw: `d7-shopify-sale-pricing.md`.
- Evidence: "set the value of the Compare-at price field ... to the original price of the product." "only the sale price is displayed at checkout". Strikethrough for automatic discounts "you need to use a third-party discount app". `verified`

---

## F. Time check on Fabulous From Online prices

Context: `docs/fabulous-from-online-design.md` (read this session) sets Casting Call "from $95, credited toward the piece", Close-Up "from $295", Leading Role "from $750". Included in those prices:
- the Screen Test, "Free by default"
- the free Logline
- a board in 7-10 business days
- "two rounds of changes"
- no 3D rendering
- the Cameo in-person add-on at $150 an hour, and c3's note that in-person runs "1.5x virtual"
- a 10% sourcing fee on sourced pieces and a 90-day store credit if nothing is found

### F1. What published sellers say about hours (anchors)
- **Independent designer, "5 Hours of Design Time"**, https://jennag.next.mydomastudio.com/store/HourlyServices/5HoursOfDesignTime-1680397874 , raw `d7-jennag-5hours.md`. The studio name is not shown on the page I read. "$1000.00 USD." "Typically we can find, collaborate and order about 3-5 different product solutions during a 5-hour period." "Typically 2-3 layout options for 1 room can be derived during this time." "*This is not enough time for a concept board containing a fully sourced room or render." `verified`. That is $200 an hour, about 1.0 to 1.7 hours per product solution, and more than 5 hours for a sourced room board.
- **Rescued and Reimagined Relics**, https://www.rescuedandreimaginedrelics.online/sourcing-trade , raw `d7-rr-sourcing.md`. "$75 per hour | 2-hour minimum"; "Starting sourcing fee: $150"; "The $250 retainer includes the first three hours of dedicated sourcing. Additional sourcing time is $75 per hour and will not be performed without your approval." `verified`. It is the nearest sourcing comparable: a two-hour minimum job.
- **Morel Interiors, "Designer for a Day"**, https://morelinteriors.mydomastudio.com/store/designpackage/DesignerForADay-InteriorDesignService-1622593648883 , raw `d7-morel-dfad.md`. "$1250.00 USD." "6 working hours by your side" plus "2 additional office hours". "By the end of the day all of your major items will be selected". `verified`. That is $156 an hour, and 8 hours for a space's major selections. Location not stated.
- **Annie Wise Design, "90 Minute Design Consult"**, https://www.anniewise.com/product-page/90-minute-consult , raw `d7-anniewise-90.md`. "$475.00"; "additional time will be charged at $200 per hour, in 15 minute increments"; a "Google Slides Presentation" summary follows the consult. `verified`. That is $317 an hour for the live time, and the follow-up time is unstated.
- **Amanda Katherine Interiors, "Room Refresh E-Design Package"**, https://amandakatherine.com/?p=1195 , raw `d7-amandakatherine-roomrefresh.md`. "397.00" per room; "a phone call to chat for 20 minutes"; "1 floor plan layout, mood board, and secret Pinterest board ... within 7 business days"; "up to 3 new options per item ... any options over 3 are subject to additional fees"; "Design process typically takes 2 weeks." `verified`. It is the closest board-only room product, and it states no hours.
- **Noeka Home**, https://noekahome.com/pages/virtual-design , raw `d7-noeka-virtual.md`. "$450 per room", "$650 per room" (twice), "$295 per table*", "$495 per room". `verified` for prices. In the prior capture (c1, not re-read) the table package has "Up to two iterations" and "Up to six place settings".
- **Sandringham Interiors**, https://www.sandringhaminteriors.com/pricing-services , raw `d7-sandringham-pricing.md`. "$175 (1 hr min call or In-home visit)"; "Mini Vignettes $425"; "Concept E-Design Service ... $875": a 1-hour call, one room concept with two board edits, one wall elevation, and a shopping list. `verified`
- **Black Cat Interiors**, https://www.blackcatinteriors.com/product-category/micro-services/ , raw `d7-blackcat-micro.md`. "Designer On Call ... $95.00 ... A focused, one-question consult ... Responses are delivered within 2-3 business days." `verified`
- **Emily Henderson (Style by EH)**, https://stylebyemilyhenderson.com/how-much-it-really-costs-to-work-with-a-designer , read through WebFetch after crawl4ai walled at 517 bytes (`d7-webfetch-websearch-notes.md`). "The total amount of time I've spent on the design process (so far) is right at 80 hours." "prior to installation services, which will likely add another 10 or so", for "three small rooms; living, dining, and TV, plus ... a custom cabinet design", and a typical room "to take 35-50 hours and span the course of up to 8 or 9 months". Rates quoted: "friends & family rate of $75/hour", "designers charging hourly typically average between $100-200/hour". `verified (WebFetch)`. No year is visible ("Jan 15"), so it may be stale. It is full-service work with installation, so treat 35-50 hours as a ceiling, not a comparable.
- **Hourly bands, secondary:** Rae Keller (Charleston) citing a Studio Designer survey and Sweeten lists entry $50-75, mid-level $100-200 and senior $300-500 (`d7-renae-keller-hourly.md`, `verified` that the page says it, a blog). Studio Designer: "a firm principal might charge $175-$200 per hour" (`d7-studiodesigner-pricing.md`, `verified`). Prior captures (c3, not re-read): Fort Myers stager labor "$110 to $120" and Cape Coral "$120 to $130" per hour.
- **Floors:** BLS, interior designers: "$67,190 per year, $32.31 per hour" median, May 2025. That is an employee median with no business overhead (https://www.bls.gov/ooh/arts-and-design/interior-designers.htm , `d7-bls-interior-designers.md`, `verified`). Florida: "Effective September 30, 2026, the Florida minimum wage will be $15.00 per hour" (`d7-fl-min-wage.md`, `verified`). Stripe: "2.9% + 30¢ per successful transaction for domestic cards" (`d7-stripe-pricing.md`, `verified`), which comes off the gross.
- **Dakota Design Company** (flat-fee blog): "if you're basing your flat fee on how many hours it takes to complete something, you're billing hourly" and new designers should "track your time carefully" (`d7-dakota-flatfee.md`, `verified`).

Gap: no published designer states hours for a "corner" or "vignette" scope. The Casting Call and Close-Up bands rest on jennag's per-solution rate and the board-only products' task lists, not on a stated figure.

### F2. Hours per tier, with the implied hourly rate

Hours are my estimates, `inferred`, built from the task list in the design doc and the anchors in F1. Every tier includes the free Screen Test or Logline time and the two included revision rounds. Inquiries that never convert cost more time and are not counted. I have no conversion data.

| Tier (price) | Hours low / likely / high | Gross $/hr at those hours | Net of Stripe, likely | Price needed for $75/hr (low / likely / high) | Price needed for $100/hr | Hours the price buys at $75 / $100 |
|---|---|---|---|---|---|---|
| Casting Call, if the $95 is treated as a labor fee | 1.5 / 2.5 / 4.0 | $63 / $38 / $24 | $36.78 | $113 / $188 / $300 | $150 / $250 / $400 | 1.3 / 0.95 |
| Close-Up ($295) | 4.0 / 6.0 / 10.0 | $74 / $49 / $30 | $47.69 | $300 / $450 / $750 | $400 / $600 / $1,000 | 3.9 / 2.9 |
| Leading Role ($750) | 7.5 / 12.25 / 20.0 | $100 / $61 / $38 | $59.42 | $563 / $919 / $1,500 | $750 / $1,225 / $2,000 | 10.0 / 7.5 |

Stripe fees on the full price are $3.06, $8.86 and $22.05.

How the hours were built (`inferred`; low / likely / high):
- Casting Call 1.5 / 2.5 / 4.0
  - intake, including a Screen Test or Logline: 0.5 / 0.75 / 1.0
  - searching the collection and outside: 0.5 / 1.0 / 1.75
  - write-up with photos, measurements and prices: 0.25 / 0.5 / 0.75
  - one revision: 0.25 / 0.25 / 0.5
  - anchors: R&R's 2-hour minimum, and jennag's 1.0-1.7 hours per solution
- Close-Up 4.0 / 6.0 / 10.0
  - intake: 0.75 / 1.0 / 1.5
  - concept: 0.5 / 0.75 / 1.25
  - sourcing and pulling: 1.25 / 2.0 / 3.5
  - board: 0.75 / 1.25 / 2.0
  - two rounds: 0.5 / 0.75 / 1.25
  - admin: 0.25 / 0.25 / 0.5
  - anchors: jennag's 3-5 solutions in 5 hours for a corner of 4-6 pieces; Amanda Katherine's 20-minute call
- Leading Role 7.5 / 12.25 / 20.0
  - intake: 1.0 / 1.5 / 2.0
  - layout and concept: 1.0 / 2.0 / 3.0
  - sourcing a whole room: 2.5 / 4.0 / 7.0
  - board: 1.25 / 2.0 / 3.5
  - presentation: 0.5 / 0.5 / 1.0
  - two rounds: 0.75 / 1.5 / 2.5
  - admin: 0.5 / 0.75 / 1.0
  - anchors: Morel's 8 hours for a space's major picks; jennag's ">5 hours" for a sourced room board; Henderson's 35-50 hours as the full-service ceiling (with installation and trades, so the board-only low end should sit well under it)

**Casting Call, second row: what Hollie actually earns.** The fee is a deposit (`docs/fabulous-from-online-design.md`: "credited toward the piece", and a miss becomes "90-day store credit"). R&R states the opposite model: sourcing fees "are not deposits toward merchandise". Real SUMMARY targets at 2.5 likely hours:
- **Sourced piece:** the only labor line is the 10% sourcing fee. A1 lamp $95 gives $9.50 ($3.80 an hour). A15 armchair $165 gives $16.50 ($6.60 an hour). A22 dress form $245 gives $24.50 ($9.80 an hour). A3 or A20 at $275 gives $27.50 ($11.00 an hour). A11 shaker $28 gives $2.80 ($1.12 an hour).
- **Collection piece:** Hollie's pay is the margin on her own stock. The repo has no cost basis, so I cannot compute it. The $95 credit comes out of that margin.
- **Nothing found:** $0 cash, with a 90-day store credit.

**Consistency check (`inferred`, from `docs/fabulous-from-online-design.md`).** The price book charges $150 an hour in person and cites c3's rule that in-person is about 1.5 times virtual. That implies about $100 an hour virtual. At likely hours the three tiers pay 38%, 49% and 61% of that, and 51%, 66% and 82% of R&R's $75.

**Sane or not?**
- **Floor:** the likely-hour figures ($37-$59 an hour net of Stripe) are above Florida's $15 and above BLS's $32.31 median for an employee. But $32.31 carries no overhead, and a solo business pays its own self-employment tax and costs. I did not compute those, and a CPA should.
- **Published solo bands:** $75 (R&R), $75-$200 mid-level (Henderson's quoted rates, Rae Keller, Studio Designer), $200 (jennag), $200 (Annie Wise overage), $175 (Sandringham). The tiers sit at or below the bottom of these.
- **Verdict:** defensible as an intro price for a stylist with no portfolio yet, and a good fit with the free Screen Test as a lead-in. It is not a steady-state rate, and Casting Call is the weak spot. A fair reading is "launch pricing for roughly the first ten bookings, with a hard cap on hours, then reprice". The doc itself says to revisit the rush price after ten bookings.
- **Three fixes, for Ricky and Hollie to choose (not applied):**
  1. Print the hours in the price: "includes about 2 / 6 / 12 hours of Hollie. More time is $100 an hour in 30-minute steps, and never without your yes" (R&R's approval clause).
  2. Reprice at likely hours and $75 an hour: about $190 / $450 / $920.
  3. Split the Casting Call fee into a non-credited search fee (for example $45) plus a credited balance, which is R&R's approach. c2 (prior capture, not re-read) also lists 12% with a $25 minimum and a $175 cap at BrandWhy.

---

## G. Where sources disagree

- **Markdown step size.** 10% steps at 30 / 60 / 90 days (FCG, Millionaire's Daughter, both `verified`, ending near 30% off) vs "20-25% off at day 30 and 50% off at day 60" (Aravenda, vendor blog, `verified` that it says so, `unverified` as industry norm). Need review: the right steepness for a one-of-one with only 14-of-19 "low" confidence comps.
- **When to make the first cut.** Chairish says 10-14 days to check and 10% or new photos, then reassess at 30 (`verified`). FCG, Millionaire's Daughter and TRR all start at 30 days (`verified`). Need review: reconcile as "check at 14, cut at 30".
- **Chairish offer tiers.** `research/pricing/art.md` says "Chairish's own offer tiers are 5/10/15% off", and `decor.md` shows $846 / $801 / $757 on $891. The live help pages say a 50%-of-list minimum offer and a 5-20% seller reserve (`verified`). Need review: those are two features, and the 5 / 10 / 15% figures come from listing pages, not a help page.
- **SUMMARY vs lighting.md on stamped Stiffel.** SUMMARY's A1 row says "$120+ if Stiffel-stamped". `research/pricing/lighting.md` recommends $225 / $325 / $450 for a stamped single. Need review before A1 gets a ladder.
- **Layaway deposits.** 15% (Sands of Time, Trademark), 25% (Garlands), 50% (A Dog's Tale), all `verified`. Need review: no data on which converts or defaults least.
- **Hourly bands.** Rae Keller's "$100 to $200" mid-level (secondary, via Sweeten), Henderson's "$75/hour" friends-and-family and "$100-200" typical, and BLS's $32.31 employee median. These measure different things (a business rate, a polled rate, a wage). Need review before any one is called "the market".
- **Offer data vs the shop's tagline.** eBay data say offers realize about 73-83% of list, while the tagline says "Absolutely no offers". Not a source conflict, but a brand decision. See H2.

---

## H. Deliverables

### H1. Markdown ladder for Holliewood & Vine

The percentages and timing are my synthesis (`inferred`) from FCG, Millionaire's Daughter, Chairish and TRR. The steps happen only on the weekly drop day. The shop's cost basis is not in the repo, so the floor needs Hollie's numbers.

**Setup**
- Floor = what Hollie must clear = cost basis + Etsy's 6.5% transaction fee on the order (item plus shipping) + $0.20 listing + payment processing (rate not on the page I read) + packing + her time.
- Ask = Floor / 0.70, so the day-90 step lands on the floor.

**Home pieces (lamps, mirrors, art, chairs, rugs, glass sets)**
| Day since listing | Step | Move | Source basis |
|---|---|---|---|
| 0-14 | Full price | none | all |
| about 14 | Checkpoint: views vs saves. If views are high and saves low, reshoot and retitle first. | none | Chairish |
| 30 (the first drop day on or after) | Step 1 | 10% off the original, rounded down to the next $5. Offers open (see H2). | FCG, Millionaire's Daughter, TRR |
| 60 | Step 2 | 20% off the original | FCG; Millionaire's Daughter ends at about 19% by 60 |
| 90 | Step 3, "last call" | 30% off the original, which is the floor. Hold there. | FCG; Millionaire's Daughter about 31% |
| 120 | Off the shelf | Fold into a bundle or a Room Look, move to local pickup, or pack away. Owner's call. | Aravenda lists return, donate or convert to store ownership |

**Small and fast (glass, fashion, accessories under about $60)** (`inferred`, from Aravenda's "compress this schedule to 30 or 45 days" and Beyond Retro's weekly cycle)
- Day 21: 15% off.
- Day 42: 30% off, which is the floor.
- Day 60: bundle or retire.

**Rules**
- Round every reduced price down to the next $5. That keeps each reduction at least as large as the percentage advertised (233.1(e)).
- Prices only go down. Never raise a price after a drop (Chairish locks it, and a raise-then-cut is the fictitious-price pattern).
- Show the drop as "Listed at $[ask] on [date]. Now $[price]." Use this form on the compressed ladder in particular, where the "reasonably substantial period" is shorter. Do not write "Was sold at".
- A drop voids open Etsy offers. Do not move a price mid-negotiation.
- Batch the steps to the weekly drop day and add a "Recently Reduced" row (FCG has one).
- Check that the shop's comps hold before starting: the ladder is also how weak comps get corrected.

**Worked arithmetic on real SUMMARY targets** (arithmetic only, not listings):
| Item | Ask | Day 30 | Day 60 | Day 90 |
|---|---|---|---|---|
| A3 cubist acrylic | $275 | $245 | $220 | $190 |
| A15 black armchair | $165 | $145 | $130 | $115 |
| A1 brass and cream urn lamp | $95 | $85 | $75 | $65 |

The unrounded values are 247.50 / 220.00 / 192.50, 148.50 / 132.00 / 115.50 and 85.50 / 76.00 / 66.50. Each step is at least the stated percentage.

### H2. Offer policy in Hollie's voice

**Needs a decision first.** The tagline "Collector of good things. Excellent taste. Absolutely no offers." conflicts with any offer policy. I have drafted one recommended policy that keeps the tagline as the headline and makes the exceptions the joke. It is Ricky's and Hollie's call, and I have not overridden the tagline silently. The no-offers alternative is just the ladder in H1 plus bundles, with Make an Offer left off, and Chairish's sanctioned reply to any offer is "counter with your Asking Price".

> **Offers**
> Absolutely no offers. (Absolutes are made to be broken, darling, but only by appointment.)
> **The first 30 days.** The price is the price. Good things don't haggle.
> **After 30 days** a piece may be talked to. Make an offer (the button on Etsy, or an email to Hollie). She'll say yes, no, or "how about this" within 48 hours. Offers within 10% of the tag are usually a yes. After day 60, within 20% is possible. Below that, a gracious no.
> **Two or more pieces?** Say so and ask for the bundle. That's the one place Hollie bargains on day one.
> **A yes is a promise, not a hold.** Pay within 48 hours or the piece goes back on the rack for the next admirer.
> **Prices only go down.** If a piece drops after you offered, the lower price wins, and Hollie will tell you.
> **Disco balls** are gifts, not terms.

How it maps to the platforms (`verified` mechanics):
- **Etsy:** set the maximum discount in Make an Offer to 10% and add the listings that pass day 30 at each drop day. After day 60 the cap would have to be raised, or handled by message. The 48-hour pay window matches Etsy's; the policy line "a yes is a promise, not a hold" matches the page. It needs desktop, not the Seller App.
- **eBay (via Crosslist):** leave Allow offers off until day 30. Whether Crosslist copies it is `unverified` and needs an account.
- **Chairish:** offers cannot be fully turned off on most products. Leave Reserve Price unset so nothing auto-accepts. Counter with the asking price to say no.
- **Own site:** an email link with the price and "offer" in the subject.

### H3. Hours-per-tier table
See F2. The short version, at likely hours: Casting Call about $38 an hour, Close-Up about $49, Leading Role about $61, against a $75-$100 benchmark. Casting Call's cash pay is the 10% line on sourced pieces ($9.50-$27.50 on the SUMMARY targets above), so it is a deposit, not a labor fee.

---

## I. Recommendation for Holliewood & Vine

### I1. What to do now (no accounts needed)
1. **Write the ladder and the Drop Day into the plan.** Use H1: 30 / 60 / 90 days, 10 / 20 / 30% off the original, rounded down to $5, a 14-day views-versus-saves checkpoint, and a floor that Hollie sets from her real costs. Tie it to the weekly drop.
2. **Choose the "was / now" wording.** "Listed at $X on [date]. Now $Y." Never "was sold at". Never raise a price after a drop.
3. **Set price endings.** List in multiples of $5. Where a step is within about $5 of a hundred boundary, land under it ($195, $295, $495), because the left-digit effect exists only when the leftmost digit changes. Do not spend effort on $245 versus $250.
4. **Decide the tagline question** (H2) and the offer window (open at day 30, 10% cap, bundles on day 1).
5. **Draft the hold and layaway cards.** Hold: 48 hours, then back on the shelf. Layaway for pieces of $300 and up only, if at all: 25% down, up to 6 months, title stays with the shop, the piece comes off the shelf on the deposit. Terms are copied from Garlands and Sands of Time, so a lawyer should review them first.
6. **Shipping rule.** Do not turn on Etsy's shop-wide free shipping guarantee. Quote shipping for lamps, mirrors, chairs and rugs, free local pickup and delivery in Lee and Collier, and free shipping only as a sale on small, light items.
7. **Reprice FFO or cap its hours** (F2). Print the hours in each tier, and fix the Casting Call credit before it goes live.
8. **Count the cost of the 14-of-19 "low" comps.** Treat the first 60 days of every listing as price discovery.

### I2. What needs an account, a fee or a lawyer
- **Account:**
  - Etsy: Make an Offer, bundles, targeted offers, sales, custom listings.
  - eBay: Best Offer.
  - Chairish: reserve prices and holds. Its seller commission page was not read, so that fee is unknown.
  - Shopify: compare-at price.
  - Crosslist: whether it syncs price drops and offer settings is `unverified`.
  - Cal.com with Stripe for FFO deposits.
- **Fee:** Etsy $0.20 per listing and 6.5% of the order amount including shipping, plus a payment processing fee whose rate the page did not state. Stripe 2.9% + 30¢. A custom listing costs another $0.20.
- **Lawyer or CPA:**
  - "Was / now" wording under 16 CFR 233.1 and FDUTPA 501.203.
  - Layaway deposits that are non-refundable, and sales-tax timing on layaway.
  - Credit and store-credit terms for the Casting Call, and how they sit with the Cooling-Off Rule already flagged in the design doc.
  - Self-employment tax and overhead on top of the hourly figures in F2.

---

## J. Ideas for Hollie

1. **Drop Day.** Same day as the weekly drop: new pieces in, anything crossing day 30 / 60 / 90 steps down, and a "Recently Reduced" shelf under it. [FCG nav, Beyond Retro, Chairish markdown bump]
2. **Colour of the week.** This week's tag or neon colour marks the last-call pieces (day 90). [Beyond Retro]
3. **"Listed at $275 on [date]. Now $245."** In place of a slashed "was". [16 CFR 233.1(b), Black Cat strikethrough as the visual]
4. **Offers open at day 30.** "Seasoned pieces take offers." [Etsy Make an Offer per listing, FCG 30-day first step]
5. **The Pair.** Etsy bundle of up to 3 listings: lamp, shade and mirror. [Etsy bundles]
6. **Forty-eight hours, then back on the rack.** One hold card used everywhere (offers, holds, FFO collection pieces). [Chairish holds, Etsy 48-hour offer window]
7. **The Slow Burn.** Layaway for $300+ pieces: 25% down, six months, the piece comes off the shelf. [Garlands, Sands of Time; lawyer first]
8. **Prices under the hundred.** $195, $295, $495 where a step crosses the line, and $5 multiples otherwise. [Thomas and Morwitz, Vestige's price list]
9. **Free local delivery in Lee and Collier** for chairs, rugs and mirrors, and shipping at cost for everything else. [Chairish in-home delivery, Etsy furniture advice]
10. **Print the hours.** "Includes about 2 / 6 / 12 hours of Hollie; more at $100 an hour, never without your yes." [R&R's approval clause, jennag's 5-hour block]

---

## K. Gaps

- No online one-of-one shop with a named weekday public price drop was found. Furnish Green's Monday markdown is the only lead and is unverified. I did not find "Sunday price drops" anywhere.
- No published hours for a corner or vignette scope exist, so the Casting Call and Close-Up bands are estimates.
- Etsy's payment-processing percentage, Crosslist's handling of offers and markdowns, Etsy's search treatment of the free-shipping guarantee, and Chairish's seller commission were not verified.
- The eBay data are older, cover all categories (average list $95) and are correlational on the list-price finding.
- Emily Henderson's page has no visible year.
