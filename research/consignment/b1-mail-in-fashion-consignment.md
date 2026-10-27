# B1: Mail-in / consign-by-shipping platforms for fashion, accessories, handbags, jewelry, watches

Agent b1 · accessed 2026-10-27 · for Holliewood and Vine (Ricky Cooper, one-person vintage shop)
Raw crawls: `research/consignment/raw/b1-*.md` (every quote below is in one of those files).

## TL;DR

1. Two business models hide behind "send us your stuff": **consignment** (they hold it, you keep a percentage when it sells: The RealReal, ThredUp, Vestiaire's Consignment Service, Rebag's consign option) and **buyout** (they quote you, you ship, they pay and own it: Fashionphile, What Goes Around Comes Around, Crossroads, Beacon's Closet). Rebag does both.
2. Every one of them makes the owner send the item in (or hands it to a courier). **Shipping is free to the owner everywhere I verified** (prepaid label/bag/pickup), and in every case the platform photographs and lists it. Vestiaire's regular marketplace is the exception: you list it yourself and ship only after a sale.
3. "Commission" is used in opposite directions. TRR and ThredUp state what **you keep**; Rebag and Vestiaire state what **you pay**. The table at the bottom is normalized to "owner keeps".
4. All the big names are brand-gated or condition-gated (designer directories, size tags required, no jewelry at ThredUp). **Only Beacon's Closet's live page says "vintage or modern clothing"** and only WGACA calls itself a vintage dealer. Nobody automates intake for unbranded vintage, which is exactly why a one-person shop can do it by hand.
5. Copyable by one person: **photo pre-approval, then buyout, then prepaid label, with a minimum item count and a store-credit premium** (Beacon's / WGACA pattern). Not copyable: warehouse studio photography, in-house authentication, auto-markdown engines (TRR, ThredUp). Consignment is the risky one for a solo operator because you are holding other people's property.

---

## 1. The RealReal (consignment, they hold it)

- Homepage: https://www.therealreal.com
- Pages read: https://www.therealreal.com/seller/commissions (Earnings Guide), https://www.therealreal.com/sell-trr, https://www.therealreal.com/consignor_terms (Seller Terms), https://www.therealreal.com/returns, https://resources.therealreal.com/how-to-sell-on-the-real-real/ (blog dated 5.27.25), https://www.therealreal.com/designers. Third-party cross-check: https://www.underpriced.app/blog/the-realreal-consignment-guide-2026.
- Raw: `b1-trr-commissions.md`, `b1-trr-sell.md`, `b1-trr-consignor-terms.md`, `b1-trr-returns.md`, `b1-trr-how-to-sell.md`, `b1-trr-designers.md`, `b1-trr-underpriced-3p.md`.

**Commission (owner keeps), clothing.** Vendor blog (2025-05-27): "For clothing, our commission structure is: 20% – $0 – $99 · 30% – $100 – $149 · 45% – $150 – $199 · 55% – $200 – $299 · 60% – $300 – $749 · 65% – $750 – $4,999 · 70% – $5,000 or more". Branded fine jewelry: 20/30/45/55 to $299, "65% – $300 – $749", "70% – $750 or more".
**Rewards bonus (live Earnings Guide):** Trendsetter under $1,499 N/A; Influencer $1,500-$4,999 +1%; Tastemaker $5,000-$9,999 +2%; VIP $10K+ +5%. "Loyalty bonus applies to items $200+ based on loyalty tier at time of sold item."
**Handbags / watches / men's sneakers:** the live page crawl rendered only the Rewards table, and `therealreal.com/commission-chart` returned 0 bytes. The blog says only "Your earnings rate will differ for handbags, branded fine jewelry, watches...". Third-party (underpriced.app, says it checked the Earnings Guide Oct 16, 2026): handbags 70% from $1,500, 75% from $5,000, 80% from $7,500; watches 85% from $7,500. **Clothing/jewelry tiers verified (vendor blog May 2025 and third party Oct 2026 agree); bag/watch/sneaker tiers need review (third-party only).**

**Minimums.** None stated on pages read. Eligibility is by designer + condition (below). Free price valuations at events "on items worth over $995" (blog).

**Accepts / refuses.** Seller Terms: "generally to be accepted, the Consigned Property must be at a minimum (in Our sole discretion): (1) in fair to pristine condition; (2) listed in Our current Designer Directory at the time of evaluation ... (3) authentic". Vintage: the site has a Vintage shop section (designers page nav: "Vintage > Clothing / Bags / Shop All", URL filter `vintage=1`), so vintage designer pieces sell; whether non-designer vintage is accepted is not stated, and the Designer Directory gate implies no (**inference, UNVERIFIED**). For Holliewood and Vine's mostly unbranded stock, TRR is effectively closed.

**THE SHIPPING QUESTION.** Three intake routes (blog): free at-home appointment ("Each appointment is 60 minutes. A Luxury Manager will meet with you to collect your items"), in-store, or "Request a prepaid shipping label, package your items ... take your package to a UPS shipping location." TRR holds the goods. Owner keeps title until sale: "You, not The RealReal, will still own the Property ... even after You deliver" (Terms 2). Risk of loss: TRR accepts it "when (i) We take physical possession ... or (ii) You use Our approved, pre-paid shipping label"; lost/damaged items "will be treated as Sold" and the owner is paid a commission on an estimated price TRR sets.

**Photography.** TRR: "We will transport them, catalog and photograph them" and "We handle photography, pricing, customer service, and shipping" (sell-trr page).

**Payout.** Terms 2(f)(vi): "We typically begin processing Commission payments on the 15th day of every month for sales of Consigned Property that occurred during the previous month ... by direct deposit, in the form of Site credit, by physical check". Check "may ... be charged a processing fee" (amount only from third party: $12.50 per check; site credit +5%: both **third-party, need review**). Intake to listing: "about 2-3 weeks from receiving to listing" (blog).

**Unsold items.** Consignment period 365 days from acceptance. Terms: if unsold, TRR will "(A) return the Accepted Item to You ... or (B) re-purpose or donate the item to a charity of Our choice". TRR "may in Our sole discretion apply an immediate 20% discount" and further discounts "without notice". Early return request: Returns page, "Consignors who request to have an item returned before the end of the consignment window (365 days) will be charged $20 per item. A fee of $100 plus shipping costs will be applied to return requests for fine art and oversized items ... Rejected Items ... returned at no charge." VIPs exempt.

**Authentication.** "more than 90 in-house experts" (blog). Counterfeits can be confiscated; owner warrants authenticity and indemnifies (Terms 8).

**Also:** Get Paid Now = TRR buys outright for eligible items (Terms 3; offer valid 7 days; "ALL SALES ARE FINAL").

**Steal this:** price-tiered split (bigger share on pricier items, easy to explain); fixed monthly payout day; written lost/damaged rule. **Watch out:** TRR's own terms show what consignment costs the operator: title stays with owner, risk-of-loss clauses, per-item records, 365-day obligations, return handling. That is a warehouse business.

---

## 2. ThredUp Clean Out (consignment, they hold it, high volume)

- Homepage: https://www.thredup.com
- Pages read: https://www.thredup.com/cleanout (FAQ), https://www.thredup.com/cleanout/guide (the `/cleanout/earnings` URL returned byte-identical content, so it resolves to the Guide), https://help.thredup.com/en_us/what-is-a-clean-out-kit-rJ84OHkRWx.
- Raw: `b1-thredup-cleanout.md`, `b1-thredup-guide.md`, `b1-thredup-earnings.md` (identical), `b1-thredup-help-kit.md`.
- Note: the /cleanout page as crawled also showed "We don't offer our Clean Out service in your area at this time." That is what the crawler saw from its location/IP; unknown whether it applies to Ricky.

**Split (owner keeps).** Guide: "You'll earn a percentage of the selling price if your item sells in its consignment window. The more it sells for, the bigger your share." Sample rows: $200 -> 80% -> $160; $100 -> 60% -> $60; $50 -> 30% -> $15; $20 -> 15% -> $3; $5 -> 3% -> $0.15. The crawl does not say whether the sample is Standard or Premium (the page has tabs): **need review**.
**Fees.** /cleanout: "A service fee of $14.99 $0.00 (Standard) or $34.99 (Premium) is deducted from your earnings only after items sell. If you earn less than the fee amount, you won't be charged the difference." Options: "$2.99 $0.00 for our 30 lb capacity bag (Standard only, bags are free for Premium). Shipping labels to use on any box are always free." "$9.99 $5.99 to schedule an Uber pick-up", "$5.99 to reclaim an unsold item, plus return shipping." The page shows two prices with one struck through; I read it as a current promo (Standard fee $0.00 now, $14.99 list), but the crawl can't confirm which is struck: **both numbers quoted, need review**.

**Accepts / refuses.** "We accept all brands, though a small number with very low resale value are ineligible for a payout" (Old Navy, H&M, Target, Uniqlo, Forever 21; "If an ineligible item sells for $20 or more, you'll still receive a payout"). Refused: "Men's clothing and accessories; Items without size tags (exceptions for luxury brands and Lululemon); Undergarments, slips, PJs, slippers, and robes; Tailored, homemade, or altered items; Wedding dresses and ballgowns; ... Non-clothing items: jewelry (except watches) ..." Women's and kids' only. Accept rate: "60-80% of items sent in Standard Clean Outs, and 80-90% in Premium". Vintage: not mentioned; the size-tag rule alone kills much true vintage (inference).

**THE SHIPPING QUESTION.** Yes, owner ships, free: "Both options ship free" (bag up to 30 lbs arrives in about a week, or a printable label for your own box), UPS drop-off or a paid Uber pickup. ThredUp holds the item.
**Photography.** "We take 360 degree images", plus inspection and pricing (process section).
**Pricing control.** "Items in Standard Clean Outs can be increased by up to 10%, and ... Premium ... up to 80%. Both can be decreased to as low as $4.99." ThredUp "gradually lower[s] prices over time"; Premium buyer-discount impact on payout "capped at 20%".
**Payout.** Credit appears automatically, convertible to cash (PayPal / Stripe logos on the Guide) or partner-brand credit ("15% Bonus" on listed partners). "Final Sale Items: Credit is issued as soon as the item ships. All Other Items: Credit is issued after the 14-day buyer return window has ended." Timeline: processing 21-28 days (Standard) / 14 days (Premium); consignment window 30-45 days Standard, 60-90 days Premium; "10-14 weeks for most Standard Clean Outs, or 16-20 weeks for most Premium".
**Unsold.** "An average of 38% of accepted items don't sell within their consignment window." Reclaim in final 7 days for $5.99 + shipping; else it stays listed with falling prices; else reuse/recycle. Unaccepted items: Standard are reused/recycled; Premium returned by default. Donation option: "we donate $5 per donation bag to seller's selected charity" (help page).
**Authentication.** None advertised (inspection only).
**Also:** "Direct Listing (Beta): list and ship directly to buyers. Plus keep 100% of your earnings" (a self-serve lane next to the managed one).

**Steal this:** the "service fee only after sale, never charged more than you earned" promise; Premium vs Standard tiers (more money for nicer pieces, slower and pickier). **Watch out:** 38% unsold and 10-20 weeks to cash is the real price of "free".

---

## 3. Fashionphile (buyout, mail-in or in-person)

- Homepage: https://www.fashionphile.com
- Page read: https://www.fashionphile.com/pages/sell-with-us (raw `b1-fashionphile-sell.md`).
- **No consignment option on the page read** (I did not verify they never offered one).

**Model.** "We provide upfront offers. You're paid as soon as we receive and authenticate your item." Three routes: Online Offer ("complimentary shipping label"), In Person (Selling Studios), Luxury Sales (they come to you).
**Steps (online).** "Fill out our quick online form using a few photos ... We'll email you with an offer within 7-10 business days ... Send us your items with a complimentary shipping label or a free UPS Pick-Up ... Once received and authenticated, your payout will be deposited in your FASHIONPHILE Wallet."
**Shipping.** "Enjoy FREE & INSURED SHIPPING when you send us your items." Title passes to Fashionphile on acceptance of the offer (buyout; inference from "upfront offers ... paid").
**Payout.** "Estimated 2-4 days after your item is received and authenticated." Methods: store credit (+10% bonus), check, PayPal, direct deposit/ACH, wire, Neiman Marcus gift card (+10% bonus).
**Accepts.** "Check out our Designer Directory to see what we're accepting" (https://www.fashionphile.com/pages/designer-directory, not fetched). Vintage, rejects/returns, photography: **UNVERIFIED** (not on the page read; the Selling FAQ at help.fashionphile.com wasn't fetched).
**Tips on the page:** clear photos incl. wear areas, photo of tag/receipt, describe wear and included accessories.

**Steal this:** photo form -> quote -> free label only after you accept; store-credit +10%.

---

## 4. Rebag (consign, buyout, or trade)

- Homepage: https://www.rebag.com
- Pages read: https://www.rebag.com/selling-with-rebag/, https://support.rebag.com/hc/en-us/articles/19688130315917-What-is-Rebag-s-commission-structure, https://intercom.help/rebag/en/articles/8443724-what-does-consignment-look-like-at-rebag, https://support.rebag.com/hc/en-us/articles/49461205930381-How-and-when-do-I-get-paid, https://support.rebag.com/hc/en-us/articles/360038475472-How-do-I-send-my-item-to-Rebag, https://support.rebag.com/hc/en-us/articles/360038858071-What-happens-to-items-that-you-don-t-approve-Will-you-return-them. `rebag.com/terms/` and `rebag.com/consign/` crawled thin (walled/JS).
- Raw: `b1-rebag-selling.md`, `b1-rebag-commission.md`, `b1-rebag-intercom-consign.md`, `b1-rebag-paid.md`, `b1-rebag-send.md`, `b1-rebag-unapproved.md`.

**Model.** "Rebag offers three easy selling methods: Consign, Trade, and Buyout ... Rebag+ members get up to 5% higher payouts."
**Commission (SELLER PAYS).** Help center: "Commission rates, which are the fees that you pay ... as low as 8% ... Most items will typically fall in the 15-25% range ... Actual commission rates will be communicated individually for each quoted item." Consignment page: "8-35% Commission rates". **Both vendor pages agree on 8% floor and differ on the top (25% "typical" vs 35% max); these are consistent but from two help desks: need review.** Owner keeps roughly 65-92%.
**Accepts.** Handbag-led ("Handbag Vetting Process"); storefront also sells watches, jewelry, apparel, shoes. Brand list, vintage, minimums: **UNVERIFIED**.
**THE SHIPPING QUESTION.** Quote first, ship second: "After accepting your offer, kindly ship your items within 14 days ... Print the prepaid FedEx shipping label ... Pack your item safely in any plain shipping box ... FedEx Ship Center or schedule a pick up", or drop at a Rebag store. Rebag holds it.
**Photography.** Not stated on pages read. Listing speed: "5-10 days until item is listed" (consignment page).
**Payout.** Consignment: "When your item sells, the sale remains pending for up to 22 business days ... Your payout is then added to your Rebag Account within approximately 15 business days after the confirmation date." Buyout: "Processing is estimated to take approximately two to three weeks after we receive your item ... payout is then added to your Rebag account within approximately 40 business days after Processing is complete." Balance: +1% per month for up to 9 months (9% bonus); +10% when spent in-shop; bank transfer 5-7 business days; "Balances transferred within 15 calendar days ... 3% Early Transfer Fee".
**Rejected items.** "returned ... within 7 business days via FedEx ... flat $10 fee for shipping back a refused bag."
**Unsold consigned items:** not found: **UNVERIFIED**.
**Authentication.** "vetting process" (details not read).

**Watch out:** the slowest cash of the group (up to roughly 22 + 15 business days after a sale on consignment). **Steal this:** the "balance grows 1% a month if you leave it as credit" mechanic, a cheap way to keep money in the shop.

---

## 5. Vestiaire Collective (peer marketplace + a concierge Consignment Service)

- Homepage: https://www.vestiairecollective.com
- Pages read: https://faq.vestiairecollective.com/hc/en-us/articles/24659638721425-Seller-Selling-Fees, .../360006739537-Seller-Direct-Shipping, .../360004811778-Seller-Selling-with-authentication, and (en-gb) https://faq.vestiairecollective.com/hc/en-gb/articles/5768815208593-Seller-The-Consignment-Service-What-It-Is-and-How-It-Works.
- Raw: `b1-vc-fees.md`, `b1-vc-direct.md`, `b1-vc-auth.md`, `b1-vc-consignment.md`.

**Marketplace fees (SELLER PAYS), US/USD.** "Listing your items is free ... a Selling Fee of 17% will be deducted". Table: $0-75: $12 fee + $3 processing; $75-15,000: 17% + 3%; $15,000+: $2,500 + 3%. "A payment processing fee of 3% (min 3 USD)". "We cannot accept items listed for sale on Vestiaire Collective for less than $18 USD." **Effective date: "These selling fees apply to all new items listed from October, 15th 2026 onwards"** (an older schedule exists, linked on the page). Owner keeps, worked: $200 sale -> $34 + $6 = $40 fees -> keeps $160 (80%); $50 sale -> $12 + $3 = $15 -> keeps $35 (70%).
**THE SHIPPING QUESTION (two flows).**
- *Authenticated shipping:* seller lists and **holds the item until it sells**, then "you'll ship it directly to our warehouse"; must ship "within 7 days" or the sale is cancelled; prepaid label provided; arrives "within 2-7 days"; VC "check, approve, package, and ship it to the buyer within 2 business days".
- *Direct Shipping:* "the buyer receives their item directly from you, the seller, rather than having their items physically checked by Vestiaire Collective"; only same-region buyer+seller, items "less than $1000 USD"; "the Seller cannot opt out".
**Payout.** "We issue payment the next business day after Authentication & Quality Control is complete ... reflect in your account within 5 business days".
**Consignment Service (en-gb page; "Currently available in the EU, UK, and US"; US terms may differ: need review).** Eligibility: "Do you have at least 5 items ... luxury or designer brands ... very good condition?" They "arrange an appointment", then: "pick-up of the items", "Expert photography", descriptions, "Market-rate pricing", "Safe storage of your item until it sells", "Shipment of sold items to your buyer". "You will earn up to 80% of the item price." Unsold: "If you'd like your item returned, we will charge €20 per item." (The commission-rate table the page references did not render.)
**Authentication.** Authentication & Quality Control Report emailed to the seller. Vintage acceptance: **UNVERIFIED**.

**Steal this:** "min 5 items" gate for the white-glove tier; fixed fee on cheap items (a flat $12 on sub-$75 sales protects the floor). **Note:** this is the only platform here where the owner does the listing and photography.

---

## 6. What Goes Around Comes Around, "WGACA" (vintage luxury, buyout by email quote)

- Homepage: https://www.whatgoesaroundnyc.com
- Page read: https://www.whatgoesaroundnyc.com/en-us/sell-to-us.html (raw `b1-wgaca-sell.md`).

"We buy ... directly from our vintage-loving clients." Currently buying "luxury accessories by Chanel, Hermès, Gucci, Louis Vuitton, Dior, Fendi, Prada and YSL ... handbags, luggage, small leather goods, jewelry, belts, scarves, and home goods ... We do not accept footwear, items outside our list of accepted brands, or any items that have been damaged, altered, or customized."
**Process.** Email luxbuyers@wgacany.com, "reply within 7-10 business days"; after photos, "estimated offer"; if accepted, "prepaid FedEx shipping label ... We do not provide shipping materials"; in-house QA/QC may "confirm the estimated quote or propose a counteroffer"; "about 3 weeks total from acceptance to pay-out".
**Rejects / counteroffer declined.** "we will ship the item(s) back to you immediately at no expense to you" (if they can't authenticate, "you will need to provide us with a return label").
**Consignment?** "What Goes Around Comes Around buys outright; we do not offer consignment."
**Payout.** Check, direct deposit, or store credit "where you can earn an extra 20% more than a cash payment". No price-matching but "open to negotiations".

**Steal this:** the whole flow is one inbox: photos -> estimate -> label -> inspection -> confirm or counter -> pay; plus the +20% credit premium.

---

## 7. Beacon's Closet "bag it, sell by mail" (buyout, vintage explicitly welcome)

- Homepage: https://beaconscloset.com
- Page read: https://beaconscloset.com/pages/bag-it-sell-by-mail (raw `b1-beacons-mail.md`).

"receive cash or store credit for your vintage or modern clothing with our sell by mail service". **Pay:** "we pay 30% cash or 50% store credit" (percentage of what base is not stated on the page: **UNVERIFIED**; context says "price estimate quotes"). "you do not wait for your items to sell before you receive your money".
**Pre-approval gate.** "provide at least 3 photos of each piece: 1) front 2) back 3) detail" by email; "we will notify you within 48 hours of accepted items and their price estimates".
**Shipping.** Free mailer after approval: "due to shipping costs and for sustainability reasons, we cannot send a mailer for submissions with less than 5 accepted items. 50 item max per submission"; "one submission per client at a time"; prepaid label, UPS store drop.
**Payout.** "once we receive and process your approved item(s) you'll get cash or credit immediately"; PayPal "may take 3 to 5 days to clear".
**Fees.** "a 4% service fee charge for each submission ... calculated off the estimated retail total ... (the service fee is reduced to 2% for submissions with a retail total of $2,000+)".
**Bad submissions.** "approved items that are not accurately represented by customer, will be donated with no payment to customer, or can be returned at the sole cost of the customer."

**Steal this:** this is the closest live template to what Holliewood and Vine could run: photo gate, 48-hour answer, minimum item count, donate-or-return-at-your-cost rule, store-credit premium.

---

## 8. Crossroads Trading (buyout by mail, trend-gated, not vintage)

- Homepage: https://crossroadstrading.com
- Pages read: https://crossroadstrading.com/sell-by-mail/ (and the 2022 blog https://crossroadstrading.com/mail-in-clothes-to-sell/). Raw `b1-crossroads-sbm.md`, `b1-crossroads-mailin.md`.

"Request a bag ... pre-paid UPS bag"; "Current processing time is 4 weeks." "When you sell your clothes for cash, we pay 25-40% based on what we price your items to sell for in our stores. ... We pay 45% in trade". Payment via Zelle or trade credit. "we only buy outright on Sell by Mail items (no consignment)." Refuses kids and "Old Navy, Forever 21, Target or Walmart"; looks for current brands (Reformation, J. Crew, Madewell...). Shows the same pattern: credit pays more than cash.

---

## 9. Poshmark: not a consign-for-you service

- Homepage: https://poshmark.com
- Pages read: https://poshmark.com/posh_authenticate (raw `b1-posh-authenticate.md`); 2014 blog https://blog.poshmark.com/2014/12/04/introducing-posh-concierge-buy-and-sell-luxury-with-confidence/ (raw `b1-posh-concierge.md`). Fees article support.poshmark.com/s/article/297755057 returned 938 bytes (walled): **no Poshmark fee % cited.**

Poshmark is list-it-yourself. "Posh Concierge" (2014) was authentication: "your free shipping label will be addressed to Poshmark rather than to your buyer." That post is historical; whether the name is still live is **UNVERIFIED**. The current flow is Posh Authenticate: "When you purchase an item from select luxury brands and categories priced at $500 or higher, your order will be sent to Poshmark and undergo our expert authentication process", "When you make a sale, we will automatically route eligible items to Poshmark for authentication". Seller holds the item until it sells; the platform is a checkpoint, not a consignor. Not a model to copy.

## 10. Material World and Kidizen: could not be confirmed

- **Material World:** my only source is a 2022 sponsored listicle (https://www.giigs.us/make-money/sell-clothes/material-world.html, accessed 2026-10-27): "Material make you an offer upfront, up to 70% of the estimated resale value (no consignment ...) Payment by PayPal (3% transaction fee), or Material World shopping credit." No vendor page. A guess at `materialworld.co` returned an unrelated spam/gambling site, so that domain is **not** them. **Status UNVERIFIED; do not treat as live.**
- **Kidizen:** `kidizen.com` returned a 4-byte page (walled). Only a third party (https://www.underpriced.app/blog/kidizen-selling-guide-2026, "Updated Jul 27, 2026") says "Kidizen is no longer an active selling channel." **Status UNVERIFIED.** Kids-only anyway; low relevance.

---

## Comparison table (normalized: "owner keeps" = what the item's owner receives, before any tax)

| Platform | Model | Ship to them? | Who pays shipping | Who holds it while for sale | Owner keeps | Payout |
|---|---|---|---|---|---|---|
| The RealReal | Consign (also Get Paid Now buyout) | Yes (or in-home / in-store) | TRR (prepaid label) | TRR; owner keeps title until sold | Clothing 20% (<$100) up to 70% ($5k+); +1/+2/+5 pts on $200+ items by tier. Bags/watches: higher, third-party figures only | 15th of month after sale; direct deposit / site credit / check; 365-day window |
| ThredUp Clean Out | Consign | Yes | ThredUp (free label or bag) | ThredUp | Sample 3% ($5) to 80% ($200), minus $14.99 / $34.99 service fee (Standard fee shown $0.00 promo) | Credit after 14-day buyer return window; 10-14 wks (Standard), 16-20 wks (Premium) |
| Fashionphile | Buyout | Yes (or in person / they visit) | Fashionphile (free insured label / UPS pickup) | Fashionphile owns it after offer accepted | Quoted offer (no %) | 2-4 days after authenticated; credit +10% |
| Rebag | Consign / Buyout / Trade | Yes, after quote | Rebag (prepaid FedEx) | Rebag | Consign: 100% minus 8-35% (typical 65-85%); buyout: quoted | Consign: ~22 bus. days pending + ~15; buyout: 2-3 wks + up to ~40 bus. days |
| Vestiaire marketplace | Peer marketplace | Only after a sale | Prepaid label (authenticated) or seller (direct) | **Seller** until sold | ~80% above $75 (100 - 17 - 3); $12 + $3 flat below $75 | Next business day after QC, +5 bus. days |
| Vestiaire Consignment Service | Concierge consign (>=5 luxury items) | Pickup | Vestiaire | Vestiaire | "up to 80%" (en-gb page) | Not stated on page read |
| WGACA | Buyout (no consignment) | Yes, after email quote | WGACA (prepaid FedEx) | WGACA owns it | Quoted offer; credit +20% | ~3 weeks acceptance to payout |
| Beacon's Closet | Buyout, vintage OK | Yes, after photo approval, 5+ items | Beacon's (prepaid mailer) | Beacon's owns it | 30% cash / 50% credit (base unstated) minus 4% (2% over $2k) fee | On processing; PayPal 3-5 days |
| Crossroads | Buyout | Yes | Crossroads (UPS bag) | Crossroads owns it | 25-40% cash / 45% credit of their store price | After ~4 wk processing |
| Poshmark | Peer marketplace | Only after a sale (auth for $500+) | Prepaid label | **Seller** | Not fetched | Not fetched |
| Material World | UNVERIFIED | - | - | - | - | - |
| Kidizen | UNVERIFIED (reported shut) | - | - | - | - | - |

## Discrepancies and open items

- TRR clothing/jewelry tiers: verified (vendor blog May 2025 + third-party Oct 2026); handbag/watch/sneaker tiers, $12.50 check fee, +5% site credit: third-party only, need review. Live commission chart did not render.
- Rebag commission: "as low as 8%, most 15-25%" (support) vs "8-35%" (consignment page): consistent, need review for the top end. Unsold-consignment policy: not found.
- ThredUp fee prices show two numbers each (strikethrough promo): need review. Sample earnings table not labeled Standard vs Premium: need review. "Not available in your area" seen from the crawler.
- Vestiaire: fee schedule effective 2026-10-15; Consignment Service page was en-gb (EU/UK/US), US terms may differ.
- Fashionphile, Rebag, WGACA vintage handling: not stated on pages read.
- **Open legal questions, not researched here:** whether Etsy/Shopify allow listing goods you hold on consignment (owner's property, not yours), and Florida consignment/sales-tax treatment. Flag for another agent or a lawyer; I am not asserting a rule.

## Blunt read: which models can a one-person vintage shop copy?

**Copy (ranked):**
1. **Beacon's-style buy-by-mail, tiny version.** A form: 3 photos per piece (front/back/detail), you answer in 48 hours with a price, a prepaid label only goes out for approved pieces and only if 5+ are accepted (the label cost has to be amortized), you pay on receipt. Rule for misrepresented items: donate or return at the sender's cost. Offer a credit premium over cash (everyone does: Beacon's 50 vs 30, Crossroads 45 vs 25-40, WGACA +20%, Fashionphile +10%). Credit keeps cash in the shop. Nobody else does vintage; this is the gap. Risk: you are buying with your own money, so your own comps matter.
2. **WGACA-style email quote for the high-value one-offs.** No shipping until a quote is accepted; inspect; confirm or counter; if the counter is refused, ship it back free. Good for signed items, art, lighting you would not want to pay to ship blind.
3. **Invite-only, small-batch consignment** copying TRR's logic, not its scale: tiered split (bigger share on pricier items), one payout day per month, a stated window (TRR 365 days is generous; ThredUp 30-90 days is aggressive), a return fee for early pickup (TRR $20, ThredUp $5.99, Rebag $10 on refused, Vestiaire EUR 20), and a lost/damaged rule written down before the first box arrives. Do this only for a few local/known consignors.

**Do not copy:** ThredUp and TRR's mass intake (bags of unsorted clothes, studio photography per item, authentication staff, algorithmic markdowns, 38% unsold). Brand-authentication anything (you are not a luxury authenticator, and the owner indemnifies the platform for good reason). Vestiaire's marketplace is just Etsy with a warehouse.

**The honest warning:** consignment turns you into a bailee for strangers' property. TRR's terms are mostly risk allocation (risk of loss, title, set-off, indemnity), and they have lawyers. Buyout is simpler for one person: you pay, you own it, you list it in your own voice on Etsy, Shopify, and your own site. Consignment only works at this size if the consignors are few and you control the intake gate.
