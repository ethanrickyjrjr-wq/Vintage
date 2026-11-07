# Gaps 14: Platform-native free tools inside Etsy, eBay and Shopify (completeness check)

Date 2026-11-07. Author: research subagent (completeness critic for lane 14). Question: Which built-in, free tools inside Etsy, eBay and Shopify did the lane 14 report miss, which listed tools are defunct, acquired or renamed, and what do the missing ones cost today? Legend: V = vendor page read today (2026-11-07) through the session fetcher; U = unverified (snippet, memory, collapsed page section, or the page would not load).

Method note: the shared web-search budget for this turn was already used up when this agent started, so no search engine was used. URLs came from the Etsy help center's own site-search API (help.etsy.com/api/v2/help_center/articles/search.json), link extraction from eBay Seller Center and Shopify help pages already known to load, and known vendor URLs. 47 fetches; 36 returned the intended vendor page. etsy.com itself was not tried (lane 14 reported 403 every time). ebay.com/help captcha-walled the tax page on two retries after one clean load. help.shopify.com returned 403 on three deep pages (Agentic plan, Selling on ChatGPT, Shop Pay Installments getting-paid on first try; the last loaded on retry).

## 0. Bottom line

- The lane missed the two native shipping stacks. Etsy sells USPS and FedEx labels inside Shop Manager at "discounted volume shipping rates" with no membership fee, $100 insurance included on Ground Advantage and Priority, and calculated shipping that previews cost for the buyer. eBay Labels does USPS, FedEx and UPS, "Save on retail prices", free scheduled USPS pickup, ShipCover insurance to $15,000, and a freight path for oversized pieces such as chairs. Both are free and both are V. A paid shipping tool is not needed at Hollie's scale.
- Sales tax is already handled on both marketplaces: Etsy and eBay calculate, collect and remit as marketplace facilitators, no fee, no opt-out. eBay's state list names Florida with a Marketplace Facilitator Certificate (V). Etsy's state list was collapsed on the page (Florida on Etsy is U, but the rule covers "US sales tax on behalf of sellers located anywhere in the world"). Only the Shopify store needs its own tax tool, and lane 14 already covered Shopify Tax.
- Star Seller is a free Etsy badge the lane skipped: 95% of first messages answered within 24 hours, 95% on-time shipping with tracking or an Etsy label, 4.8+ rating, at least 5 orders and $300 in 3 months, eligible 90 days after the first sale. It shapes the daily routine (answer within 24 hours, buy the label on Etsy). Local pickup orders count against it because they have no tracking.
- Etsy charges a one-time, non-refundable shop set-up fee. The amount is not printed on any help page read today ("If applicable, the set-up fee will be displayed and charged as part of the shop set-up process"). Budget for it; amount U.
- Two 2025-era AI channels are free and on by default: Etsy listings can be bought inside ChatGPT, Gemini, Google AI Mode and Copilot (US shoppers only, guest checkout, no coupons), and Shopify agentic storefronts put products into ChatGPT, Google AI Mode, Gemini, Copilot and Meta, "active by default for eligible stores". Shopify also now shows an "Agentic $0/mo" plan on its pricing page: Catalog listing in AI channels, pay only on sale, card rates from 2.9% + 30¢. Neither needs a third-party tool.
- Shopify Marketplace Connect (formerly Codisto) is Shopify's own crosslister to eBay, Amazon, Walmart and Target Plus: free to install, first 50 synced orders a month free, then 1% capped at $99 a month. It does NOT take new Etsy connections ("New connections to Etsy can't be made at this time"), and a review read today says the eBay sync broke for about a month. It does not replace the Crosslist Gold decision (Etsy first), but at Hollie's volume it is a free eBay bridge once the Shopify store exists.
- Etsy Pattern is alive, not defunct: $15.00 USD a month after a 30-day trial, no transaction fee, imports the Etsy shop. It is the cheapest own-site option on the table and worth knowing even though Shopify is the plan.
- Defunct or moved: eBay Collective (ebay.com/collective now lands on a generic Home & Garden browse page); the eBay help ID 4160 that used to be "printing shipping labels" now serves "Bulk listing tools"; the Seller Center Promoted Offsite page moved under /growth/ebay-advertising/. Shopify's help index still lists a legacy "Lite plan" that the pricing page does not sell. Linkpop's shutdown was already recorded by lane 14.

## 1. Missing tools (same columns as the lane report)

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Etsy shipping labels (USPS, FedEx) and calculated shipping | Buy and print USPS or FedEx labels from the order page; calculated shipping quotes the buyer by zip and weight; package data flows from the order into the label | "you may receive discounted volume shipping rates. Aside from Etsy's standard fees, there are no additional membership fees to use shipping labels purchased on Etsy." / "Includes $100 insurance: Ground Advantage, Priority Mail and Priority Mail Express" / FedEx: "come with up to $100 of liability insurance" | Free; pay postage only | Web (Shop Manager), Etsy Seller app | High: glass and ceramics ship USPS with $100 cover built in; FedEx for heavier lamps; "furniture, for example" is called out as too big for calculated shipping, so chairs need manual rates | V | https://help.etsy.com/hc/en-us/articles/360000336887-USPS-Shipping-Labels-on-Etsy |
| Etsy Star Seller | Monthly badge shown on the shop for customer-service stats | "Message response rate: reply to 95% of first messages in a thread within 24 hours" / "On-time shipping & tracking: 95% of orders ship on time, with valid tracking or a shipping label purchased on Etsy" / "Average review ratings: 4.8+" / "at least 5 orders and $300 in sales over the past 3 months" | Free, automatic | Web (Customer service stats dashboard), Seller app | High: the free trust badge; sets the rule "answer within 24 hours, buy labels on Etsy" | V | https://help.etsy.com/hc/en-us/articles/4403058372503-What-is-the-Star-Seller-Badge |
| Etsy shop set-up fee (platform cost) | One-time charge when the shop is opened | "You will be charged a one-time, non-refundable fee for opening your shop." / "If applicable, the set-up fee will be displayed and charged as part of the shop set-up process." | n/a | Web (shop onboarding) | Must-know cost; amount not published on the help pages read today (U for the number) | V (existence), U (amount) | https://help.etsy.com/hc/en-us/articles/115014483627-What-are-the-Fees-and-Taxes-for-Selling-on-Etsy |
| Etsy and eBay marketplace sales-tax collection | Both marketplaces calculate, collect and remit US state sales tax on the seller's behalf | Etsy: "Etsy doesn't charge any additional administration charges for calculating, collecting and remitting sales tax." / eBay: "there are no charges or fees for eBay automatically calculating, collecting, and remitting sales tax." | Free, automatic, no opt-out | Platform | High: no tax tool needed for marketplace sales; eBay's list names Florida (V); Etsy's state list was collapsed (Florida on Etsy U) | V | https://help.etsy.com/hc/en-us/articles/360000343968-How-US-State-Sales-Tax-and-Fees-Applies-to-Etsy-Orders and https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 |
| Etsy listings in ChatGPT, Gemini, Google AI Mode and Copilot | Some Etsy listings can be bought inside the AI assistants; buyer checks out as an Etsy guest | "Etsy has partnered with OpenAI, Google, and Microsoft to allow some Etsy listings to be purchased directly in ChatGPT, Gemini, Google AI Mode, and Copilot." / "only shoppers in the United States" | Free (standard Etsy fees assumed; seller fee page not found, U) | Platform (buyer side in ChatGPT, Gemini, Copilot apps) | Medium: free extra reach for one-of-one decor; seller cannot use coupons there and messages require the buyer to link an Etsy account | V (buyer page), U (seller terms) | https://help.etsy.com/hc/en-us/articles/34208252828695-Purchasing-Etsy-Items-Through-ChatGPT-Gemini-Google-AI-Mode-and-Copilot |
| Etsy Pattern | Etsy's own standalone website that imports the Etsy shop; custom domain optional | "Having a Pattern website $15.00 USD per month, after 30-day free trial" / "There is no transaction fee on Pattern." / "Listings that appear only on Pattern are free." | 30-day trial; free to design before publishing | Web | Medium: cheapest own site on the table, auto-synced with Etsy; no room editor or custom code, so not a Shopify replacement for the designed storefront | V | https://help.etsy.com/hc/en-us/articles/360000337067-Pricing-and-Fees-for-Pattern |
| eBay Labels (USPS, FedEx, UPS), ShipCover, freight | Buy carrier labels in Seller Hub or the app; insurance in the same flow; freight options for oversized items | "Save on retail prices with USPS Shipments." / "You can easily arrange a free scheduled USPS pickup in most zip codes" / "USPS shipments can be covered for up to $15,000 by ShipCover Insurance when you use eBay Labels." / Freight: "If you're selling oversized items, consider listing and shipping with freight carriers." | Free; pay postage only; discount percent not printed | Web (Seller Hub), eBay app | High: covers small glass to accent chairs (flat-rate freight or rate tables by region) | V | https://www.ebay.com/sellercenter/shipping/choosing-a-carrier-and-service/usps-and-ebay-labels and https://www.ebay.com/sellercenter/shipping/choosing-a-carrier-and-service/freight |
| eBay Promoted Offsite | Pushes eligible fixed-price listings to Google and other external channels | "applies a cost-per-click model" / "You only pay when a potential buyer clicks on your ad." / "we'll calculate your monthly budget as 30.4 times your target daily budget" / "eBay may spend above your daily budget up to twice" | None; budget-based | Web (Seller Hub Advertising) | Low: pay per click with no sale guarantee is wrong for quantity-1 items; General (pay on sale) is the better eBay ad | V | https://www.ebay.com/help/selling/advertising/promoted-offsite?id=5471 |
| Shopify Marketplace Connect (formerly Codisto) | Shopify's own channel app that lists the Shopify catalog on eBay, Amazon, Walmart and Target Plus and syncs orders and inventory | "Free to install. Additional charges may apply." / "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month" / "New connections to Etsy can't be made at this time with the Shopify Marketplace Connect app." | 50 synced orders a month free | Shopify app (web admin) | Medium: free Shopify-to-eBay bridge at Hollie's volume, but no Etsy, and a review read today says the eBay sync "stopped working" for a month; does not replace Crosslist for Etsy-first | V | https://apps.shopify.com/marketplace-connect and https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect |
| Shopify agentic storefronts and the Agentic plan | Products appear and can be bought in ChatGPT, Google AI Mode, Gemini, Microsoft Copilot and Meta through Shopify Catalog; a $0 plan exists for AI channels only | Help: "Agentic storefronts is active by default for eligible stores." / Pricing page: "Agentic $0/mo For selling in AI channels" / "Only pay when you make a sale" / "Card rates from 2.9% + 30¢ USD online" | Included with every plan; Agentic plan itself is $0/mo | Web admin (Sales channels settings) | High: free AI-channel reach on top of Basic; the $0 Agentic plan is not a site replacement (direct checkout off by default, no storefront) | V | https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts and https://www.shopify.com/pricing |
| Shopify Forms and Shopify Search & Discovery (Shopify-built free apps) | Forms: popups and inline forms that grow the email list; Search & Discovery: storefront filters, search tuning, recommendations | Forms: "Pricing Free" / Search & Discovery: "Free" and "Customize filters to let shoppers refine their search by multiple categories." | Entirely free | Shopify apps (web admin) | High: Forms feeds the free Shopify Email quota; Search & Discovery gives the collection filters (era, material, room) without a paid search app | V | https://apps.shopify.com/shopify-forms and https://apps.shopify.com/search-and-discovery |
| TikTok Shop channel app (TikTok Inc.) | Syncs the catalog to TikTok Shop for LIVE shopping and shoppable videos; TikTok ads and pixel | "Free to install. Additional charges may apply." / Help: "LIVE shopping: When you're LIVE on TikTok, your viewers can browse and purchase products directly from your LIVE." | Free to install; TikTok Shop fees and ad spend extra (not read) | Shopify app; TikTok on iOS and Android | Medium: fits the on-camera plan in docs/video-direction.md; TikTok Shop seller fees were not on the pages read (U) | V | https://apps.shopify.com/tiktok and https://help.shopify.com/en/manual/online-sales-channels/social-commerce/tiktok |

Also noted (not counted among the 12):

| Item | Finding | Quote | V/U | Source URL |
|---|---|---|---|---|
| Etsy Insider (buyer loyalty beta) | Invite-only US buyer membership; Etsy pays the shipping discount; nothing for sellers to set up | "there's no cost to you." / "Etsy will cover up to $6 in shipping costs on the least expensive US domestic shipping option for orders over $15 per shop." | V | https://help.etsy.com/hc/en-us/articles/24858135478039-What-is-Etsy-Insider |
| Shop Pay Installments | Buy-now-pay-later on the Shopify store for orders $35 to $30,000; the merchant pays a higher transaction fee whose rate is only shown inside admin | "There's no cost to activate Shop Pay Installments on your store. When a customer uses Shop Pay Installments, you're charged a higher transaction fee" / "$35 to $30,000 USD in the United States" | V (rate U) | https://help.shopify.com/en/manual/payments/shop-pay-installments/getting-paid |
| eBay coded coupons | Confirms lane 14: Store subscribers only | "eBay Store subscribers can find coded coupons on the Marketing tab within Seller Hub." | V | https://www.ebay.com/sellercenter/growth/seller-hub-discounts/coded-coupons |
| Local pickup | Etsy has no tool; Shopify has pickup and local delivery built in as delivery methods; eBay's pickup help page was not reached | Etsy: "Etsy doesn't have a built-in tool for offering local pickup or delivery to your buyers." / Shopify: "Offer pickup in store so customers can collect orders at your retail locations." | V | https://help.etsy.com/hc/en-us/articles/360000338067-How-to-Offer-Local-Pickup-or-Delivery and https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods |

## 2. Notes per tool

**Etsy shipping labels and calculated shipping (V).** USPS labels: domestic and international, "discounted volume shipping rates", no membership fee, $100 insurance on Ground Advantage, Priority Mail and Priority Mail Express, none on Media Mail; a temporary 8% USPS surcharge notice is on the page. USPS charges $4 extra for cylindrical rolls and some special package types. FedEx labels: up to $100 liability insurance, extra insurance through Shipsurance, "no additional fees, outside Etsy's normal fees". Calculated shipping needs USPS or Global Postal Shipping and fails for oversized pieces: "The package is bigger than the carrier's maximum dimensions (furniture, for example)", so chairs and large lamps get manual rates. Gotcha: Purchase Protection and Star Seller both lean on "a shipping label purchased on Etsy", so buying labels elsewhere costs more than postage.

**Star Seller (V).** Reviewed on the 1st of every month over the previous 3 months. Eligible 90 days after the first sale. Needs 5 orders and $300 USD in sales, 95% first-message replies within 24 hours, 95% on-time shipping with tracking or an Etsy label, 4.8+ average rating, and the case-rate standard. Local pickup orders cannot be excepted: "we're unable to make exceptions for local pickup orders." A seller's helper with shared access can keep the 24-hour clock.

**Shop set-up fee (V existence, U amount).** Both the fees page and the How to Open an Etsy Shop page describe a "one-time, non-refundable" fee charged during set-up and shown there; neither prints a figure. The Payoneer line says the fee is in USD and taxes may apply. The Etsy help search API has no article titled for the fee. Treat the number as unknown until Ricky sees it on the set-up screen.

**Marketplace sales tax (V).** Etsy: "Based on applicable US State enacted marketplace facilitator tax laws, Etsy automatically calculates, collects, and remits US sales tax on behalf of sellers located anywhere in the world"; no admin charge; no opt-out; remitted tax shows in the Payment account as "Sales tax paid by buyer (Remitted)". The state list is a collapsed accordion that the fetcher did not expand, so Florida on Etsy is U. eBay: same model, "no charges or fees", no opt-out, and its printed list includes Florida with a Marketplace Facilitator Certificate. eBay also taxes seller fees for sellers registered in Hawaii, South Dakota, Texas and Washington, not Florida. Gotcha: the Shopify store is not a marketplace, so Shopify Tax (lane 14) still applies to direct sales.

**Etsy listings in AI assistants (V buyer side).** Buyer-facing help only: US shoppers, USD, card, Link bank, Apple Pay, Google Pay; Etsy gift cards and coupons cannot be used; orders are guest orders until the buyer links an Etsy account, which they must do to message the seller or leave a review. No seller-side page with fees, opt-out or eligibility was found through the help search API, so those are U. Expect fewer messages and reviews from these orders.

**Pattern (V).** Still sold: free to design, 30-day trial after publishing, then $15.00 USD a month plus tax where applicable; WHOIS privacy $3.00 a year; domain registration through Tucows extra; no transaction fee on Pattern sales; Pattern-only listings free; Etsy Payments processing fees still apply; 2.5% currency conversion when applicable. "we'll automatically import most content and inventory from your shop". Fit: a cheap, synced landing site. Not the designed burgundy room, no custom code, and sales there earn no Etsy search traffic.

**eBay Labels, ShipCover and freight (V).** USPS page: free scheduled pickup, free Priority flat-rate supplies, retail-price savings (percent not printed), ShipCover insurance to $15,000 integrated in the label flow, weight and size limits per service (Ground Advantage to 70 lb; cubic-foot caps for cubic pricing). FedEx and UPS pages exist in the same section (not read). Freight: flat-rate freight or rate tables for up to 100 US regions; eBay tracks a list of freight carriers. Fit: this is how an accent chair ships on eBay without a third-party freight broker, though the carrier quote still has to come from the carrier.

**eBay Promoted Offsite (V).** Cost per click set by eBay from partner charges and history; target daily budget with a monthly cap of 30.4 times the daily figure; eBay may spend up to twice the daily budget on a given day; sales attributed within 30 days of any click. A $10 daily target can cost $304 a month with no sale. Skip for one-of-one stock.

**Shopify Marketplace Connect (V).** Help page lists Amazon, Target Plus (US only), Walmart (US only) and eBay; Etsy is closed to new connections. App page: 2,135 reviews; pricing "Free to install", 50 synced marketplace orders a month free, then 1% per order, capped at $99 a month. Complaints read today: a Walmart listing failure from missing fields and an eBay sync outage "about a month ago". The app also surfaces third-party Etsy connectors (CedCommerce, InfoShore) as alternatives, which are not Shopify-built. Fit: once the Shopify store exists it is a free way to push the catalog to eBay; Etsy still needs Crosslist or hand listing.

**Shopify agentic storefronts and Agentic plan (V).** Help: on by default for eligible stores; products reach AI channels through Shopify Catalog, or Google Merchant Center for Google AI Mode and Gemini; ChatGPT buyers finish checkout on the store in an in-app browser; Google, Copilot and Meta surfaces can use Shopify's direct checkout if activated. The Agentic plan keeps an existing store but has direct checkout off by default; the plan's own help page returned 403 and then redirected to the plan-features index, so its full feature list is U. The pricing page shows "Agentic $0/mo", "Add your products to Shopify's Catalog", "Choose which AI channels to sell in", "Only pay when you make a sale", "Card rates from 2.9% + 30¢ USD online". The "Selling on ChatGPT" sub-page was 403, so US-only or Shopify Payments eligibility details are U.

**Shopify Forms and Search & Discovery (V).** Both are Shopify-built and listed at "Free" with no tiers (767 and 515 reviews). Forms writes subscribers straight into the customer list that Shopify Email (10,000 free emails a month, lane 14) sends to. Search & Discovery adds custom filters, multi-filter and filter display controls and product recommendations; it is the native answer to the collection filters in the sample storefront.

**TikTok Shop channel (V).** App "Free to install. Additional charges may apply." with 15,996 reviews; help page describes LIVE shopping and shoppable in-feed videos with fulfilment from Shopify admin. TikTok Shop's own seller commission and any US account requirements were not on the pages read (U). Terms gotcha: TikTok Shop has its own seller policies and payout schedule outside Shopify.

**Etsy Insider (V).** Seasonal (3-month) or annual paid buyer membership, invite-only beta, US only; members get up to $6 shipping covered by Etsy on orders over $15 per shop and 5% back in Etsy credit. "As a seller, you don't need to opt into the program"; earnings and fees unchanged. Nothing to do.

**Shop Pay Installments (V, rate U).** Needs Shopify Payments and Shop Pay, US business entity, USD; order range $35 to $30,000; funded by Affirm; merchant fee is higher than the standard card rate and the fee is not returned on refunds; the exact rate is only visible in admin. A $400 chandelier is in range; weigh the fee before turning it on.

## 3. Recommendation for Hollie

Free first, today:
1. Buy every Etsy label inside Etsy (USPS for glass and ceramics, FedEx for heavy lamps) and turn on calculated shipping for everything that fits a USPS box. It protects Purchase Protection and Star Seller at the same time.
2. Work the Star Seller rules from day one: reply to first messages within 24 hours, ship on time with an Etsy label, keep 4.8+. Nothing to install.
3. Let both marketplaces collect sales tax; do not add a tax tool for Etsy or eBay. Check the Florida line in Etsy's collapsed state list once logged in (U today).
4. Leave Etsy's AI-assistant purchasing and Shopify agentic storefronts on; they cost nothing and reach buyers who ask ChatGPT for "pink depression glass".
5. On Shopify Basic, install Shopify Forms and Shopify Search & Discovery (both free, Shopify-built) before any paid popup or filter app. Install the TikTok app only when the on-camera schedule starts producing shoppable videos.
6. On eBay, use eBay Labels with ShipCover for anything over the $100 USPS cover, and freight rate tables for chairs.

Pay only once it earns it:
- Shopify Marketplace Connect stays free under 50 synced orders a month; use it as the Shopify-to-eBay bridge once the store is live, and keep Crosslist for Etsy. Watch the eBay sync complaints.
- Etsy Pattern ($15 a month) only if the Shopify store is delayed and a synced landing page is wanted now.
- Shop Pay Installments only after reading the admin fee rate; it lifts conversion on $300-plus pieces but the fee is not refunded on returns.

Skip:
- eBay Promoted Offsite: pay per click, monthly cap of 30.4 times the daily budget, no sale guarantee.
- The Shopify Agentic $0 plan as a site substitute: no storefront, direct checkout off by default.
- eBay coded coupons: Store-only, same as sale events.

Budget note: the Etsy shop set-up fee is a real one-time cost with no published figure on the help pages read today; Ricky will see it on the set-up screen.

## 4. Defunct, renamed or moved (evidence)

- **eBay Collective** (eBay's curated antiques and vintage decor marketplace): https://www.ebay.com/collective redirected today to https://www.ebay.com/b/Home-Garden/11700/bn_1853126, a generic "25+ Home & Garden for sale" browse page. No Collective page exists. V.
- **Shopify Marketplace Connect** is the renamed **Codisto** ("Shopify Marketplace Connect (formerly Codisto)" on both the app page and help page), and its **Etsy connection is closed to new users** ("New connections to Etsy can't be made at this time"). V.
- **Etsy Pattern** is NOT defunct, contrary to the common assumption: pricing page live at $15.00 USD a month, "What is Pattern?" page live. V.
- **Linkpop**: lane 14 already recorded the app as "not currently available on the Shopify App Store"; not re-fetched here.
- **Shopify "Lite plan"** still appears in the help center's plan-features index (Starter, Lite, Retail, Basic, Grow, Advanced, Plus, enterprise, Agentic) although the pricing page sells no Lite plan; treat the name as legacy. V (index page).
- **Shopify Agentic plan** is new on the pricing page ("Agentic $0/mo For selling in AI channels"); its help page URL returned 403 and then redirected to the index. V (pricing), U (help detail).
- **eBay help ID 4160** (the old "printing shipping labels" link) now serves "Bulk listing tools"; the Seller Center URL /sellercenter/marketing/promoted-offsite returned 404 and the live page is /sellercenter/growth/ebay-advertising/promoted-offsite. Stale links, not defunct tools. V.
- **Terapeak**, **Seller Hub Reports (formerly File Exchange)** and **Promoted Listings General (formerly Standard)**: renames already recorded by lane 14; not re-verified.

## 5. Gaps and pages that would not load

- Web search budget was exhausted before this agent started; no search engine was used. Roundup cross-checks (Shopify App Store category pages, Chrome Web Store, Product Hunt, GitHub) were therefore not possible, so "appears in two independent 2026 roundups" could not be tested; missing tools were found through vendor help-center navigation and site search instead.
- Etsy shop set-up fee amount: not printed on https://help.etsy.com/hc/en-us/articles/115014483627 or https://help.etsy.com/hc/en-us/articles/115015672808; the "Learn more about the set-up fee" link points back to the fees page anchor. U.
- Etsy state sales-tax list is a collapsed section the fetcher did not expand; Florida on Etsy is U.
- Etsy seller-side terms for ChatGPT, Gemini, Google AI Mode and Copilot sales (fees, opt-out) not found via the help search API; only the buyer article exists. U.
- https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 loaded once (first 14,000 characters, which included the sales-tax collection section and the Florida entry) and captcha-walled on two retries.
- https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/offering-local-pickup?id=4136 served the "How sellers can cancel an order" article; eBay local pickup is unverified today.
- https://www.ebay.com/sellercenter/shipping/ebay-labels and https://www.ebay.com/sellercenter/marketing/promoted-offsite returned navigation only (404 in the browser path).
- https://apps.shopify.com/shopify-marketplace-connect 404; the live handle is /marketplace-connect.
- https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/agentic-plan 403 then redirected to the index; https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/chatgpt 403; https://www.shopify.com/shop-pay/installments 404. Shop Pay Installments merchant rate is U (shown only in admin per Shopify).
- https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup returned navigation only; the parent Delivery methods page loaded.
- TikTok Shop seller commission and US eligibility not on the pages read. U.
- eBay FedEx and UPS Labels pages and the Shopify Catalog page were found by link extraction but not read.

## 6. Sources

Every URL fetched today, one per line. Status in brackets.

Etsy
- https://help.etsy.com/api/v2/help_center/articles/search.json?locale=en-us&query=... [V, Etsy help site-search API; queries: shipping labels, Star Seller, shop set-up fee, sales tax, ChatGPT, Pattern, Etsy Insider, calculated shipping, onboarding fee, FedEx shipping labels, state sales tax, Star Seller badge, Pattern website, Etsy Insider sellers, sell through ChatGPT, AI shopping agents listings, Set-Up Fee, shop setup fee new sellers, local pickup, AI generated description listing]
- https://help.etsy.com/hc/en-us/articles/360000336887-USPS-Shipping-Labels-on-Etsy [V]
- https://help.etsy.com/hc/en-us/articles/360000337447-FedEx-Shipping-Labels-on-Etsy [V]
- https://help.etsy.com/hc/en-us/articles/115013946647-How-to-Set-Up-Calculated-Shipping [V]
- https://help.etsy.com/hc/en-us/articles/4403058372503-What-is-the-Star-Seller-Badge [V]
- https://help.etsy.com/hc/en-us/articles/29665255990039-How-to-Track-Your-Progress-Toward-Becoming-a-Star-Seller [V]
- https://help.etsy.com/hc/en-us/articles/115015672808-How-to-Open-an-Etsy-Shop [V, set-up fee described, no amount]
- https://help.etsy.com/hc/en-us/articles/115014483627-What-are-the-Fees-and-Taxes-for-Selling-on-Etsy [V, set-up fee section, no amount; link extraction]
- https://help.etsy.com/hc/en-us/articles/115015746068-Adding-Sales-Tax-to-Listings [V]
- https://help.etsy.com/hc/en-us/articles/360000343968-How-US-State-Sales-Tax-and-Fees-Applies-to-Etsy-Orders [V, state list collapsed]
- https://help.etsy.com/hc/en-us/articles/34208252828695-Purchasing-Etsy-Items-Through-ChatGPT-Gemini-Google-AI-Mode-and-Copilot [V]
- https://help.etsy.com/hc/en-us/articles/360000337067-Pricing-and-Fees-for-Pattern [V]
- https://help.etsy.com/hc/en-us/articles/360000344088-What-is-Pattern [V]
- https://help.etsy.com/hc/en-us/articles/24858135478039-What-is-Etsy-Insider [V]
- https://help.etsy.com/hc/en-us/articles/360000338067-How-to-Offer-Local-Pickup-or-Delivery [V]

eBay
- https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 [V on first fetch; captcha on two retries]
- https://www.ebay.com/sellercenter/shipping/choosing-a-carrier-and-service/usps-and-ebay-labels [V]
- https://www.ebay.com/sellercenter/shipping/choosing-a-carrier-and-service/freight [V]
- https://www.ebay.com/help/selling/advertising/promoted-offsite?id=5471 [V]
- https://www.ebay.com/sellercenter/growth/seller-hub-discounts/coded-coupons [V]
- https://www.ebay.com/sellercenter/growth/seller-hub-discounts/offers-to-buyers-best-offer [V, used for link extraction]
- https://www.ebay.com/help/selling/ebay-advertising/promoted-listings-overview?id=5295 [V, used for link extraction]
- https://www.ebay.com/collective [redirected to https://www.ebay.com/b/Home-Garden/11700/bn_1853126; Collective gone]
- https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/printing-shipping-labels-ebay?id=4160 [served "Bulk listing tools"; miss]
- https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/offering-local-pickup?id=4136 [served "How sellers can cancel an order"; miss]
- https://www.ebay.com/sellercenter/marketing/promoted-offsite [404; navigation only]
- https://www.ebay.com/sellercenter/shipping/ebay-labels [navigation only]

Shopify
- https://www.shopify.com/pricing [V, Agentic $0/mo tier]
- https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features [V, plan index incl. Lite and Agentic]
- https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/agentic-plan [403, then redirected to the index]
- https://help.shopify.com/en/manual/online-sales-channels [V, overview and link extraction]
- https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts [V]
- https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/chatgpt [403]
- https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect [V]
- https://help.shopify.com/en/manual/online-sales-channels/shopify-marketplace-connect [redirected to the Sales channels overview]
- https://apps.shopify.com/marketplace-connect [V]
- https://apps.shopify.com/shopify-marketplace-connect [404]
- https://apps.shopify.com/shopify-forms [V]
- https://apps.shopify.com/search-and-discovery [V]
- https://apps.shopify.com/tiktok [V]
- https://help.shopify.com/en/manual/online-sales-channels/social-commerce/tiktok [V]
- https://help.shopify.com/en/manual/payments/shop-pay-installments [V]
- https://help.shopify.com/en/manual/payments/shop-pay-installments/faq [V]
- https://help.shopify.com/en/manual/payments/shop-pay-installments/getting-paid [403 first try; V on retry]
- https://www.shopify.com/shop-pay/installments [404]
- https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup [navigation only]
- https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup/setting-up-pickup [redirected to Delivery methods overview; V]
