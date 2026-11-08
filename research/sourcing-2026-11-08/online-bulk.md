# Lane A: online bulk and wholesale sourcing (Sonnet subagent report, saved verbatim)

Saved 2026-11-08 by the parent session. Brief: online sourcing of cheap vintage inventory a small SWFL reseller can buy today, bulk or by the piece. Tools: WebSearch for discovery (SearXNG was down, Fedora unplugged), `tools/crawl.sh` for every page read. Raw crawls are in `research/` with host and UTC timestamp names from 2026-11-08T07.

---

# Online sourcing for cheap vintage inventory: Holliewood and Vine
Date: 2026-11-08. Lane: online sourcing a small SWFL reseller can buy today.

**Method notes**
- `tools/search.sh` failed because the Fedora box is unplugged. I used WebSearch for discovery only. Every number below came from a page I crawled with `tools/crawl.sh`, unless it is listed under "Could not verify".
- Every row was seen 2026-11-08. A page's own date is in parentheses where it shows one.
- Cost-per-piece figures marked "(my calc)" are my arithmetic.
- Failed fetches:
  - `shopgoodwill.com/help/buyerfaq`: 404.
  - `joinfleek.com/faq`: 404.
  - `fleek.co`: suspended domain.
  - GovDeals terms: 42-byte wall.
  - PublicSurplus FAQ: HTTP 500.
  - EBTH help-center articles: login wall.
  - Torgom: the crawl returned only the page shell.

## 1. ShopGoodwill (Goodwill SWFL pickup is the standout)
| Source | What you get | Price / minimum | Shipping to SWFL | Catch | URL | Seen |
|---|---|---|---|---|---|---|
| ShopGoodwill auctions, general | Donated goods from 135+ Goodwills; auction plus Buy It Now. Max-bid proxy. | No minimum. Pay within ~7 days of close. No percentage buyer's premium appears on any official page fetched. | Ships from the selling Goodwill, flat or carrier-calculated. Usually FedEx, UPS or USPS, ~5 business days after payment. Dimensional weight applies. | The effective fee is a seller-set handling fee, shown before you bid. Insurance and signature fees can be added. The platform collects sales tax by ship-to location, and some states tax shipping and handling. | shopgoodwill.com/help/faqdetail/how-are-shipping-and-handling-charges-determined; blog.shopgoodwill.com/english/the-ultimate-guide-shipping-handling | (help 2024-04-22; blog 2026-06-23) |
| Goodwill SWFL storefront, local pickup | Local listings with no shipping cost. | Snapshot showed current bids of $9.97 with 0 to 1 bids and ~11h left. Item types were not captured. Handling fee still applies on pickup. | Pickup at 5100 Tice St, Fort Myers 33905, Wed and Fri 10:30 to 3:30. Appointment booked 2 business days ahead; phone 239-995-2106 ext 2275. | Collect within 7 days of payment or the order becomes a donation. No add-on orders. | shopgoodwill.com/goodwillswfl; shopgoodwill.com/help/faqdetail/can-items-be-picked-up-from-the-selling-goodw | 11-08 (help 2024-04-04) |
| Combining and one-cent shipping | Fewer shipping charges across wins. | Combined weight is capped at 20 lb. There is a "One-Cent Shipping" section; I did not capture what is in it. | Same Goodwill location, closes within 7 days of each other, same carrier. | Buy It Now items cannot be combined. You must wait for all auctions to end before paying. | shopgoodwill.com/help/faqdetail/how-do-i-combine-items | (2024-04-22) |

Landed cost = winning bid + seller handling + shipping (zero if you pick up) + tax.

I have no data on which Goodwill regions ship cheaply to Florida. Shipping depends on each seller. The substitute is the SWFL pickup above, plus Advanced Search has a "show pickup items only" filter.

## 2. Bulk vintage clothing and wholesale
| Source | What you get | Price / minimum | Shipping to SWFL | Catch | URL | Seen |
|---|---|---|---|---|---|---|
| Fleek (marketplace, ~2,000 suppliers per Fortune) | Bundles, bales and "handpicks" from suppliers mostly in India, Pakistan and Dubai. A video handpick lets you choose each piece. Buyer Protection on every order. | Bundles from 10 to 20 pieces. Bundle prices are behind the app, not on the web pages. Pay-later up to 30 days (terms apply). | Shipping is built into the checkout total. US duties and tariffs are covered. Overseas orders take 21 to 28 working days; US sellers take 6 to 7 business days. Sea freight is ~90 days. | Brand tiles lean to streetwear and Y2K (Carhartt, Ralph Lauren, Stussy, Nike, Levi's). Check fit with this shop's look. Items are graded A, B or C. | joinfleek.com/resources/new-reseller; support.joinfleek.com (customs and shipping articles); fortune.com 2026-07-08 | 11-08 |
| Bulk Vintage Clothing, Philadelphia | Mixed men's and women's vintage, sold by the pound. Also bundles by category, including Christmas sweaters. | $200 for 20 lb, $500 for 50 lb, $850 for 100 lb, $1,700 for 200 lb. Stated at 0 to 3 pieces per lb. At 100 lb that is about $2.83 to $8.50 per piece (my calc), before shipping. | UPS Ground, priced by weight and boxes, with a $2 minimum handling fee. No free shipping. | The seller says they "grab armfuls." Grade 1 to 3, may include damaged items and modern pieces. Orders cancelled after packing carry a 30% restocking fee. Bundle prices were not visible. | bulkvintage.com/product/wholesale-vintage-clothing-byweight.html; bulkvintage.com/shipping.html | 11-08 (© 2026) |
| Dust Factory Vintage | Bales of 50, 100 or 500 lb. | Listed at $350 for 50 lb, $600 for 100 lb, $2,000 for 500 lb. | Not stated. | Page is © 2024, so prices may be stale. It says only 10 to 15% of a bale is usable for the vintage market. | dustfactoryvintage.com/vintage-clothing-by-the-pound/ | 11-08 |
| Torgom Vintage (LA) | Bales and handpicks. | Not verified, see Could not verify. | Banner reads "FREE SHIPPING ON ALL BALES." | Banner also reads "ALL SALES FINAL. NO RETURNS." | torgomvintage.com/online-orders | 11-08 |
| Goodwill Bluebox (Gulfstream Goodwill, West Palm Beach) | Curated boxes, restocked Fridays 6 PM ET. | 5 lb jewelry lot for $49.99 ("for parts and jewelry making", random pack). 12-piece mixed-brand apparel bundle for $24.99, about $2.08 per piece (my calc). | $7 per used-condition box. In-state shipper. | The apparel bundle is modern mall brands, not vintage. The 5 lb weight includes the box. The only independent review (affiliate-linked, 2021, then $34.99 plus $5) found valuables had been removed. | buybluebox.com; frompenniestoplenty.com/blog/goodwill-bluebox-jewelry-mystery-box-review | 11-08 (review 2021-07-03) |

## 3. Liquidation marketplaces
| Source | What you get | Price / minimum | Shipping to SWFL | Catch | URL | Seen |
|---|---|---|---|---|---|---|
| Bulq | Returns and excess-inventory lots. | Closed. | n/a | Optoro shut it on 2025-07-28 (trade press). | valueaddedresource.net/optoro-bulq-shut-down/ | (2025-07-21) |
| B-Stock | Retailer return pallets via storefronts. | Reseller's certificate required. | Platform arranges shipping; you pay the shown cost. You cannot arrange your own. | The FAQ I fetched is a template storefront ("Bohannon" / "Test Production"), so treat the rules as indicative. Wire payment within 2 business days, binding bids, reinstatement fees of $100 to $1,000. | bstock.com/bohannon/faq/ | 11-08 |
| Liquidation.com | Same category. | No premium or minimum found on the fetched FAQ. | Varies by lot. | The fetched FAQ showed no vintage or decor sections. | liquidation.com/aucbuyerfaq | 11-08 |

Verdict: skip all of them for vintage. I saw nothing vintage or decor-specific; this is my judgment from what I read, not a catalog audit.

## 4. Government and estate auctions
| Source | What you get | Price / minimum | Shipping to SWFL | Catch | URL | Seen |
|---|---|---|---|---|---|---|
| MaxSold | Online estate and downsizing sales, local pickup. | 18% buyer's premium, and it is taxed. | Pickup by default. Shipping only if the seller offers it. | I did not fetch a live sale. Past Cape Coral, Naples and Fort Myers sales appear in search listings. A pickup-time change can cost $20. | support.maxsold.com/hc/en-us/articles/203144004 | 11-08 (about a year old) |
| EBTH | Curated estate lots. | The fetched Terms list taxes, shipping, handling, storage and insurance as add-ons, and no premium appears there. | Shipping quoted per item. Shipment Protection is free up to $99 and $2.52 from $100 to $199. | Handling is at least $20 per moved lot. Storage runs $5 to $120 a week. Late payment costs 20% or 1.5% a month. | ebth.com/terms | 11-08 |
| HiBid (example lot) | Auction-house online sales. | One Iowa sale charged a 15% premium plus 3% card fee. | "Shipping Available," set by each house. | Terms are per auction house. | hibid.com/lot/250078876/buyers-premium | (lot 2025-06-18) |

## 5. Mystery and bundle boxes
Bluebox is covered above. The only reseller account I read said valuables had been removed, and the price has since risen. Treat these as parts, gift or fill stock, not listable vintage.

## Best three to start with this month
1. **ShopGoodwill with Goodwill SWFL pickup.** It is the only option that passes all three tests: landed cost known before you pay, no shipping to Fort Myers, and single listable pieces.
2. **MaxSold (check for an open SWFL sale).** Pickup in-county and single pieces. The 18% premium and tax are known upfront. Whether a sale is open now is unchecked; if none is, it drops to "watch."
3. **Fleek, video handpick only.** Pick each piece, shipping and duty are in the checkout total, and the minimum is 10 to 20 pieces. Look at the app prices first. It leans to streetwear, so use it only if clothing fits the shop.

## Skip
- **Bulq:** closed.
- **B-Stock and Liquidation.com:** no vintage evidence, wire payment and certificate friction.
- **Torgom:** the one thing I verified is no returns.
- **Dust Factory and Bulk Vintage bales:** need sorting and cleaning, damaged items are expected, and Bulk Vintage's UPS cost is unquoted. A 20 lb Bulk Vintage test ($200) is the only reasonable trial.
- **Bluebox mystery jewelry:** parts-grade.
- **GovDeals and PublicSurplus:** unverified, pickup-only.

## Could not verify
All "(search result, not fetched)" except where stated otherwise.
- **Torgom:** $500 / $1,000 / $3,000 minimums, a 1,000 lb minimum, and a business license plus seller's permit requirement.
- **Fee percentages:** B-Stock 10% premium; Liquidation.com 5 to 10%. A 15% ShopGoodwill premium (blogs conflict; none on official pages).
- **GovDeals:** 12.5% premium and storage fees.
- **PublicSurplus:** about 10%, set per agency.
- **EBTH:** "no premiums" and the $80 / $120 delivery figures.
- **LiveAuctioneers:** all fees.
- **Whatnot:** buyer-claim windows, and anything about wholesale lots.
- **Closures and supplier lists:**
  - Tundra closed in 2023.
  - LA Vintage and Garson & Shaw minimums.
  - Optoro acquired by Blue Yonder.
- **Fleek:** Trustpilot refund and delay complaints.
- **ShopGoodwill:** whether a Florida resale certificate removes tax; jewelry-jar and misspelled-title tips (anecdotes from Closo, a reseller-tools vendor); the one-cent section's contents.
- **Direct Liquidation:** nothing found.

## Sources (crawled and read)
- shopgoodwill.com/help/faqdetail/how-are-shipping-and-handling-charges-determined
- shopgoodwill.com/help/faqdetail/why-am-i-being-charged-tax
- shopgoodwill.com/help/faqdetail/how-do-i-combine-items
- shopgoodwill.com/help/faqdetail/pure-buy-now
- shopgoodwill.com/help/faqdetail/what-is-new-shopgoodwill-all-about
- shopgoodwill.com/help/faqdetail/can-items-be-picked-up-from-the-selling-goodw
- shopgoodwill.com/goodwillswfl
- blog.shopgoodwill.com/english/the-ultimate-guide-shipping-handling
- blog.shopgoodwill.com/english/the-ultimate-guide-to-bidding-buying
- fortune.com/2026/07/08/fleek-an-online-marketplace-connecting-vintage-clothing-wholesalers-and-retailers-raises-25-million-in-new-funding/
- joinfleek.com/home
- joinfleek.com/resources/new-reseller
- joinfleek.com/pages/how-it-works
- support.joinfleek.com/hc/en-us/articles/10148050957083-Customs-Taxes
- support.joinfleek.com/hc/en-us/articles/10148250330395-How-does-shipping-work-
- bulkvintage.com/product/wholesale-vintage-clothing-byweight.html
- bulkvintage.com/shipping.html
- bulkvintage.com/category/wholesale-vintage-womens-by-bundle.html
- bulkvintage.com/category/wholesale-vintage-womens-dresses-by-bundle.html
- dustfactoryvintage.com/vintage-clothing-by-the-pound/
- torgomvintage.com/online-orders
- torgomvintage.com/faqs
- goodwillbluebox.com
- goodwillbluebox.com/pages/about-us
- buybluebox.com/products/5lbs-vintage-modern-jewelry-lot-mixed-recycled-jewelry
- buybluebox.com/products/adult-apparel-mixed-brands-bundle-12-pieces
- frompenniestoplenty.com/blog/goodwill-bluebox-jewelry-mystery-box-review
- valueaddedresource.net/optoro-bulq-shut-down/
- bstock.com/bohannon/faq/
- liquidation.com/aucbuyerfaq
- support.maxsold.com/hc/en-us/articles/203144004-What-does-buyer-s-premium-mean
- ebth.com/faq
- ebth.com/terms
- hibid.com/lot/250078876/buyers-premium
- trust.whatnot.com/buyer-protection

Saved crawl files are in `C:\Users\ethan\dev\Vintage\research\` (named by host and UTC timestamp, 2026-11-08).
