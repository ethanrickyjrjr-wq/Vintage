# Verify lane 14: platform-native free tools (Etsy, eBay, Shopify)

Date: 2026-11-07. Author: research subagent (adversarial price and claim checker).
Question: Do the prices, free tiers, platform claims and availability claims recorded by the first lane-14 agent match the vendors' own pages today?
Legend: V = page read today (2026-11-07); U = unverified (page would not load, or claim not on the page read). Verdicts: confirmed = the exact figure or claim is on the page read; refuted = the page says something different; unreadable = page did not load after one alternative attempt.

Method: every page was fetched through the session's headless Chromium fetcher. WebSearch was exhausted by other agents in this run, so alternative URLs were guessed from vendor URL patterns. No Reddit, no roundups, no blogs except one Shopify blog attempt (404). 43 URL attempts, 36 pages loaded.

## 0. Bottom line

- The first agent's numbers hold up. Every price and fee on the Etsy, eBay and Shopify pages matched: Etsy $0.20 listing, 6.5% transaction, 3% + $0.25 USD processing, Plus $10 USD per month, Offsite Ads 15% capped at $100; eBay 250 free listings, $0.35 after, 13.6% final value fee, Store tiers $4.95 to $59.95 yearly; Shopify Basic $29 USD/mo yearly, $39 USD/mo monthly, 3 days free then $1/month for 3 months, POS Pro + $89 USD/month per location, 10,000 free emails, Shopify Tax free to $100,000 lifetime for new stores.
- Share & Save confirmed: 4% refund normally, 6.5% from October 20 to January 4. Gotcha not flagged before: links sent in Etsy Messages or placed in listing descriptions do not count, and an Offsite Ad last click overrides a Share & Save click.
- Two things the first agent got wrong or could not support: (1) the "Starter lacks collections" comparison refers to a Shopify plan that is not on shopify.com/pricing today; the $0/mo plan shown there is "Agentic" for AI channels, not a storefront. (2) The eBay Basic Store break-even lower bound of about $1,500 a month is not supported by the fee pages; on the 0.9-point final value fee difference it is about $2,440 a month on yearly billing or about $3,100 on monthly billing.
- Smaller corrections: eBay's per-order fee is $0.30 for orders of $10 or less and $0.40 above (not a flat $0.40); eBay Sourcing insights needs a Basic Store or above on ebay.com (not any Store, so not Starter); Etsy Make an Offer is USD-only and Etsy calls it a feature it is still testing; the Etsy Seller app does exist on Google Play (the first agent said the Android listing was unreachable).
- Two pages would not load: Shopify's Sidekick help page (HTTP 403; the shopify.com/sidekick marketing page loaded and says "BUILT INTO EVERY STORE") and Shopify's Starter plan help page (JavaScript error, blog alternative 404).
- No shutdown or acquisition notices on any page read. Etsy Plus, Share & Save, Marketplace Insights, eBay International Shipping and Shopify Email all show as live programs.

## 1. Checks

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| Etsy Share & Save | Free; 4% of order total refunded; 6.5% through January 4 | confirmed | "From October 20 to January 4, all sellers enrolled in Share & Save will earn 6.5% back on eligible orders." and "you get an instant refund of 4% off the eligible order total" | https://help.etsy.com/hc/en-us/articles/16981332744087 | None. Add gotcha: "Links sent to buyers through Etsy Messages or placed in listing descriptions will not count towards Share & Save benefits." |
| Etsy Seller app (iOS) | Free; iPhone | confirmed | "Free" ... "iPhone, iPad" ... "Requires iOS 15.0 or later." | https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1534619962 | None |
| Etsy Seller app (Android) | First agent: "Android listing not reachable today" | refuted (exists) | "Etsy Seller: Manage Your Shop / Etsy, Inc / 4.7 star / 57.1K reviews / 5M+ Downloads / Install" | https://play.google.com/store/search?q=etsy%20seller&c=apps | The app is on Google Play. Direct listing pages for guessed package ids returned 404, so the price field was not read; the catalog shows an Install button, not a price. |
| Etsy listing videos | Free; 2 silent videos per listing | confirmed | "You can add up to 2 videos per listing." and "Your video may be 3-15 seconds long and will not contain any audio" | https://help.etsy.com/hc/en-us/articles/360053206073 | None. Max 100 MB, aspect 2:1 or 1:2. |
| Etsy image rule | One unedited photo required; AI edits allowed elsewhere | confirmed | "Etsy requires at least one unedited photo for most items. For other images, you can use photo editing tools, including AI" | https://help.etsy.com/hc/en-us/articles/44297885802647 | None. "Your first listing image does not need to be the unedited photo". Unedited videos do not count toward the requirement. |
| Etsy Make an Offer | Free; set up on web only | confirmed | "is only available for sellers and buyers who have their currency set to USD, and is not available on the Etsy Seller app" | https://help.etsy.com/hc/en-us/articles/16792774373143 | Add: USD only; Etsy says it will "continue to test and improve this new feature". No fee is stated on the page. |
| Etsy Marketplace Insights | Free; 15 keyword searches a week; unlimited with Plus | confirmed | "Sellers can explore up to 15 keyword searches per week for free." and "If you're an Etsy Plus subscriber, you're able to search for unlimited keywords" | https://help.etsy.com/hc/en-us/articles/35122361353239 | None |
| Etsy Search Visibility page | Free, in Shop Manager | confirmed | "The Etsy search visibility page in Shop Manager shows how your shop is performing in three key areas" | https://help.etsy.com/hc/en-us/articles/25869947521175 | None. Optional title-recommendation tool "may" be available. |
| Etsy fees | $0.20 per listing, 4 months; 6.5% transaction on order incl. shipping | confirmed | "- $0.20 per listing." ... "A listing expires after 4 months." ... "6.5% of the total order amount in your designated listing currency. This fee applies to shipping and gift wrapping" | https://help.etsy.com/hc/en-us/articles/115014483627 | None |
| Etsy payment processing | 3% + $0.25 USD (US bank) | confirmed | "United States	3% + 0.25 USD" | https://help.etsy.com/hc/en-us/articles/115015628847 | None |
| Etsy Plus | $10 USD per month; $3 listing credits + $5 ads | confirmed | "The fee for an Etsy Plus subscription is $10 USD per month" ... "15 credits for creating or renewing listings" ... "$5 USD in Etsy Ads credit" | https://help.etsy.com/hc/en-us/articles/360001589928 | The page says 15 listing credits, not "$3"; $3 is 15 x $0.20, an inference. Credits "don't roll over month-to-month". Restock requests are the other headline feature, useless at quantity 1. |
| Etsy Offsite Ads | 15% per attributed order (12% above $10,000), cap $100; opt-out only under $10,000, lifetime above | confirmed | "Charged a 15% fee for orders attributed to an Offsite Ad" ... "required to participate for the lifetime of your shop" ... "will never exceed $100 USD" | https://help.etsy.com/hc/en-us/articles/360000338367 | None |
| Etsy Ads | Seller-set daily budget; starting max $25 per day | confirmed | "All sellers start with a maximum daily budget of $25." | https://help.etsy.com/hc/en-us/articles/360033701174 | Add: "there is a 15 day waiting period before you can begin an Etsy Ads campaign" after opening a shop. |
| Etsy Purchase Protection for Sellers | Free, automatic, up to $250 | confirmed | "Etsy will cover up to $250 of a refund" ... "will automatically cover qualifying orders with no setup required from the seller." | https://help.etsy.com/hc/en-us/articles/5850122619287 | None. Page suggests insuring orders over $250. |
| eBay selling fees (no Store) | 250 free listings then $0.35; 13.6% up to $7,500; $0.40 per order | confirmed (nuance) | "First 250 listings free per month, then $0.35 per listing" ... "13.6% on total amount of the sale up to $7,500 calculated per item" ... "For orders $10.00 or less the per order fee is $0.30, for orders over $10.00 the per order fee is $0.40." | https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822 | Per-order fee is $0.30 under $10.01, $0.40 above. 24 photos confirmed: "You can add up to 24 photos ... free of charge." Antiques and Art are in "Most categories" at 13.6% for non-Store sellers. |
| eBay Store fees | Starter $7.95/$4.95; Basic $27.95/$21.95; Premium $74.95/$59.95; charged monthly | confirmed | "Basic	$27.95	$21.95" ... "For either option, we charge the subscription fee on a monthly basis." | https://www.ebay.com/help/selling/fees-credits-invoices/store-fees?id=4809 | None on prices. Break-even corrected below. |
| eBay Basic Store break-even | "Basic only pays off above roughly $1,500 to $2,400 a month of Antiques and Art sales" | refuted (lower bound) | Basic+ Store table: "Antiques 12.7% on total amount of the sale up to $2,500 calculated per item / 2.35% on the portion of the sale over $2,500" vs non-Store 13.6% up to $7,500 | https://www.ebay.com/help/selling/fees-credits-invoices/store-fees?id=4809 | The saving is 0.9 points. $21.95 / 0.009 = about $2,440 a month (yearly billing); $27.95 / 0.009 = about $3,100 (monthly billing). The $1,500 figure is not supported. Separate point: the Store's 2.35% tier starts at $2,500, so a single $4,000 piece pays about $353 with a Basic Store vs $544 without. |
| eBay Seller Hub | Free | confirmed | "Seller Hub is the central place for managing your eBay business. It's free to use" | https://www.ebay.com/help/selling/selling-tools/seller-hub?id=4095 | None. "Some tools are only available to Store subscribers" (Marketing tab). |
| eBay Product research (Terapeak) | Free to Seller Hub sellers; Sourcing insights needs a Store | confirmed (nuance) | ebay.ca: "Sellers with access to Seller Hub can use Product research for free." ebay.com: "Sourcing insights is available at no extra cost to business sellers with a Basic Store subscription or above." | https://www.ebay.com/help/selling/selling-tools/terapeak?id=4853 and https://www.ebay.ca/help/selling/selling-tools/terapeak?id=4853 | Sourcing insights needs Basic or above, not Starter. The ebay.com page omits the word "free" for Product research; the ebay.ca page states it. "last 3 years of eBay sales data". |
| eBay Offers to Buyers and Best Offer | Free; rule-based automatic offers need a Store | confirmed | "eBay Store subscribers can save time and effort with rule-based automatic offers." and "you'll have the option to automatically send the same offer to future interested buyers" | https://www.ebay.com/sellercenter/growth/seller-hub-discounts/offers-to-buyers-best-offer | None. Repeat-the-same-offer automation is available without a Store; criteria-based rules need a Store. Targets "watchers or cart abandoners". |
| eBay Promoted Listings (general) | Ad rate 2% to 100%, charged only on sale; needs Above Standard or Top Rated | confirmed | "You choose an ad rate between 2% - 100% of the item's total sale amount" ... "Above Standard or Top Rated sellers with enough account activity can promote fixed price listings" | https://www.ebay.com/help/selling/ebay-advertising/promoted-listings/general-campaign-strategy?id=4164 | None. Charged when the item "sells within 30 days of a click on your ad". |
| eBay International Shipping | Free; automatic for eligible US sellers | confirmed | "There's no extra charge to ship your items with eBay International Shipping and you won't be charged an international fee." ... "If you're eligible, you'll be opted into the program." | https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/ebay-international-shipping-program?id=5348 | None. "available for eligible sellers in the US and Canada only". Buyers get an automatic 30-day return window; returned items "may not be returned to you". |
| Shopify Basic | $29 USD/mo yearly, $39 USD/mo monthly; 3 days free then $1/month for 3 months | confirmed | "Pay monthly	$39 USD/mo" ... "Pay yearly	$29 USD/mo" ... "Try 3 days free, then $1/month for 3 months." | https://www.shopify.com/pricing | None. Card rate "2.9% + 30¢" online, "2.6% + 10¢" in person on Basic. |
| Shopify Starter | "Starter lacks collections" (used as the reason to pick Basic) | unreadable | shopify.com/pricing shows "Basic", "Grow", "Advanced", Plus and "Agentic $0/mo For selling in AI channels"; no Starter row. Help index lists "Starter plan" and "Lite plan" but the Starter subpage printed "An error occurred. Unable to execute JavaScript." | https://www.shopify.com/pricing ; https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/starter-plan | Starter is not on the public pricing page today and shopify.com/starter redirects to the free-trial page. Treat the Starter comparison as unverified. The new "$0/mo" plan is Agentic (AI channels), not a storefront. |
| Shopify free themes | 24 free themes | confirmed | "24 themes" (free price filter) | https://themes.shopify.com/themes?price%5B%5D=free | None |
| Shopify Sidekick | Included with the plan | confirmed (weak) | "BUILT INTO EVERY STORE" (marketing page). Help page returned HTTP 403. | https://www.shopify.com/sidekick ; https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick | The FAQ "Does using Sidekick cost money?" is on the page but its answer did not render as text. No price shown anywhere. |
| Shopify Email (now "Shopify Messaging") | 10,000 free emails a month, then $1 USD per 1,000 | confirmed | "All stores on these plans have 10,000 free emails to send at the beginning of every month." ... "$1 USD per 1,000 additional emails up to 300,000 emails" | https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging/email/pricing | None. Add: "abandoned checkout emails are always free and don't count towards the monthly limit." Available on "Basic, Grow, Advanced, and Plus". |
| Shopify Flow | Free app | confirmed | "Pricing Free" | https://apps.shopify.com/flow | None |
| Shopify Tax | Free to $100,000 lifetime (stores created on or after May 13, 2026); then 0.35% per order on Basic/Grow/Advanced, max $0.99 | confirmed | "For stores that were created on or after May 13, 2026, Shopify Tax is free until you reach a lifetime threshold of sales." ... "United States and rest of the world	$100,000 USD	$0.99 USD" ... "Basic, Grow, or Advanced ... 0.35%" | https://help.shopify.com/en/manual/taxes/shopify-tax/pricing | None |
| Shopify POS | Basics included in every plan; POS Pro + $89 USD/month per location | confirmed | "+ $89 USD/month for each POS Pro location" ... "Casual in-person selling ... Included in every plan" | https://www.shopify.com/pos/pricing | None |
| Shopify shipping insurance | Basic gets labels but not the free $200 insurance | confirmed | "If you're on the Grow, Advanced, or Plus plan and use Shopify Payments ... Shopify automatically includes up to $200 USD of shipping insurance" | https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels/shipping-insurance | None. Labels page: "Discounts for shipping labels vary based on your Shopify plan" (no percentages published). |
| Shopify Inbox | Free | confirmed | "Pricing Free" | https://apps.shopify.com/inbox | None |
| Pinterest for Shopify | Free to install, ad spend extra | confirmed | "Free to install. Additional charges may apply." | https://apps.shopify.com/pinterest | None |

## 2. What the first agent got wrong or left out

1. Shopify Starter. The pick's reasoning "Starter lacks collections" compares against a plan that is not on shopify.com/pricing today. The page lists Basic, Grow, Advanced, Plus and "Agentic $0/mo For selling in AI channels". The help center still indexes "Starter plan" and a "Lite plan", but the Starter page would not render and shopify.com/starter redirects to the free-trial offer. The Basic recommendation stands on its own; drop the Starter comparison or re-verify it from a readable page.
2. eBay Basic Store break-even. The fee difference for Antiques and Art is 13.6% (no Store) vs 12.7% (Basic Store), 0.9 points. $21.95 / 0.009 is about $2,440 a month on yearly billing and $27.95 / 0.009 is about $3,100 on monthly billing. The "$1,500" lower bound is not supported by the fee pages. One extra fact the first agent missed: the Basic Store's lower 2.35% tier starts at $2,500 instead of $7,500, so a Store saves real money on any single piece priced above $2,500 (about $191 on a $4,000 sale).
3. eBay per-order fee. It is $0.30 for orders of $10 or less and $0.40 for orders over $10. The pick wrote "$0.40 per order" flat. Minor at Hollie's prices.
4. eBay Sourcing insights. ebay.com says "Basic Store subscription or above", so a Starter Store does not unlock it. The first agent wrote "needs a Store".
5. Etsy Seller app on Android. The first agent said the Android listing was not reachable. Google Play's catalog shows "Etsy Seller: Manage Your Shop, Etsy, Inc, 4.7, 57.1K reviews, 5M+ Downloads". Ricky is on iPhone, so this changes nothing for Hollie, but the claim was wrong.
6. Etsy Make an Offer. The first agent did not flag that it is USD-only and that Etsy still calls it a feature under test. It is also web-only, which the agent did record.
7. Etsy Plus credits. The page gives "15 credits for creating or renewing listings", not a dollar figure. "$3" is a correct multiplication (15 x $0.20) but not a quote.
8. Share & Save gotchas not recorded: links in Etsy Messages or listing descriptions do not count; an Offsite Ad as the last click takes the order out of Share & Save; custom domains must forward to yourshopname.etsy.com.
9. Shopify Email is now branded "Shopify Messaging" in the help center; abandoned-checkout emails are always free and do not count toward the 10,000. Not wrong, just missing.
10. Etsy Ads: a 15-day waiting period after opening the shop before any campaign. Not recorded.

Everything else in PICKS and the high-fit TOOLS rows matched the vendor pages verbatim.

## 3. Gaps and pages that would not load

- https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick : HTTP 403 in browser and curl. Alternative https://www.shopify.com/sidekick loaded; it says "BUILT INTO EVERY STORE" but the cost FAQ answer did not render.
- https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/starter-plan : page printed "An error occurred. Unable to execute JavaScript." Alternative https://www.shopify.com/blog/shopify-starter-plan : 404. https://www.shopify.com/starter redirected to https://www.shopify.com/free-trial-offer.
- https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/agentic-plan : redirected to the plan index; the Agentic plan's own page URL is unknown.
- https://play.google.com/store/apps/details?id=com.etsy.android.soe and ?id=com.etsy.seller : 404 (guessed package ids). The Play catalog search page did load and lists the app.
- https://help.etsy.com/hc/en-us/search?query=Etsy+Seller+app : loaded but returned only an API article; the Etsy help page for the Seller app itself was not found without web search.
- WebSearch was exhausted (shared 200-call budget for this run) after the first two attempts, so no new alternative URLs could be discovered. All checks used the first agent's URLs or vendor URL patterns.
- Not checked (no price claim or low fit): eBay Live, eBay magical listing, Etsy bulk edit and shared access, Etsy Share & Save holiday promotion terms page, Shopify Google & YouTube and Facebook & Instagram channel apps.

## 4. Sources (every URL fetched today, in order)

https://help.etsy.com/hc/en-us/articles/16981332744087
https://www.shopify.com/pricing
https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822
https://help.etsy.com/hc/en-us/articles/360001589928
https://help.etsy.com/hc/en-us/articles/360000338367
https://help.etsy.com/hc/en-us/articles/115014483627
https://www.ebay.com/help/selling/fees-credits-invoices/store-fees?id=4809
https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/ebay-international-shipping-program?id=5348
https://help.etsy.com/hc/en-us/articles/35122361353239
https://help.etsy.com/hc/en-us/articles/115015628847
https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1534619962
https://help.etsy.com/hc/en-us/articles/360053206073
https://help.etsy.com/hc/en-us/articles/44297885802647
https://help.etsy.com/hc/en-us/articles/16792774373143
https://help.etsy.com/hc/en-us/articles/5850122619287
https://www.ebay.com/help/selling/selling-tools/seller-hub?id=4095
https://www.ebay.ca/help/selling/selling-tools/terapeak?id=4853
https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging/email/pricing
https://help.shopify.com/en/manual/taxes/shopify-tax/pricing
https://www.shopify.com/pos/pricing
https://www.ebay.com/sellercenter/growth/seller-hub-discounts/offers-to-buyers-best-offer
https://www.ebay.com/help/selling/ebay-advertising/promoted-listings-overview?id=5295
https://apps.shopify.com/inbox
https://apps.shopify.com/pinterest
https://apps.shopify.com/flow
https://www.shopify.com/starter (redirected to https://www.shopify.com/free-trial-offer)
https://help.etsy.com/hc/en-us/articles/360033701174
https://play.google.com/store/apps/details?id=com.etsy.android.soe (404)
https://www.ebay.com/help/selling/selling-tools/terapeak?id=4853
https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick (403)
https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels
https://www.ebay.com/help/selling/ebay-advertising/promoted-listings/general-campaign-strategy?id=4164
https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels/shipping-insurance
https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features
https://www.shopify.com/sidekick
https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/starter-plan (JavaScript error, curl fallback shell only)
https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/agentic-plan (redirected to the plan index)
https://play.google.com/store/search?q=etsy%20seller&c=apps
https://help.etsy.com/hc/en-us/search?query=Etsy+Seller+app
https://themes.shopify.com/themes?price%5B%5D=free
https://help.etsy.com/hc/en-us/articles/25869947521175
https://www.shopify.com/blog/shopify-starter-plan (404)
https://play.google.com/store/apps/details?id=com.etsy.seller (404)
