# Lane 14: Platform-native free tools inside Etsy, eBay and Shopify

Date 2026-11-07. Author: research subagent. Question: Which built-in, free tools inside Etsy, eBay and Shopify already make the process easier for a one-person vintage shop, and what do the platforms themselves cost today? Legend: V = page read today (vendor's own page, fetched 2026-11-07); U = unverified (search snippet, third-party page, memory, or the page would not load).

Method note: 60-plus page fetches through the session's headless-Chromium fetcher. Web search budget ran out midway (shared session limit), so the second half of the sweep used vendor help-center search pages, the Etsy help center's own search API and Seller Center navigation to find URLs. etsy.com (legal and news pages) returned 403 every time. help.etsy.com, ebay.com/help (most pages), ebay.com/sellercenter, export.ebay.com, pages.ebay.com, help.shopify.com, shopify.com and apps.shopify.com loaded. Several ebay.com/help pages returned a captcha wall on the first try and loaded on the retry; two never loaded (listed in section 4).

## 0. Bottom line

- Etsy's native stack is the most complete for a one-person vintage shop and is free apart from fees: Seller app (iOS, free), bulk edit, Sales and Discounts, Make an Offer, Stats, Search Visibility, Marketplace Insights (15 free keyword searches a week), listing videos, Purchase Protection (up to $250), shared access (5 helpers). Nothing here needs a third-party tool. V.
- Etsy fees today: $0.20 per listing (renews every 4 months), 6.5% transaction fee on item plus shipping, 3% + $0.25 payment processing (US bank), Offsite Ads 15% on attributed orders (12% once the shop has made $10,000 in any 365 days), capped at $100 per order. Etsy Plus is $10 USD per month and is not worth it for Hollie yet. V.
- Share & Save is the one Etsy thing to turn on today. It refunds 4% of the order total when a buyer arrives through Hollie's own link and buys within 30 days, and it is 6.5% back (the whole transaction fee) from October 20 to January 4. Free to join. V.
- eBay costs nothing to list up to 250 items a month, then $0.35 a listing. Final value fee 13.6% of the sale including shipping, plus $0.40 per order over $10. There is no separate payment processing fee. Seller Hub and Product Research (Terapeak) are free. An eBay Store (Starter $4.95 a month on yearly renewal, Basic $21.95) is not needed at launch; Basic only lowers Antiques and most Art to 12.7% on the first $2,500 per item, which pays off only above roughly $1,500 to $2,400 a month of sales in those categories (my arithmetic, section 2). V.
- eBay International Shipping is free, automatic for eligible US sellers, and removes international returns and customs work. Leave it on. Promoted Listings general strategy charges only when the item sells (ad rate 2% to 100%, seller sets it) but requires Above Standard or Top Rated status with enough activity, so it is a later tool. eBay Live is beta, select sellers only. V.
- Shopify is $29 USD a month on Basic paid yearly ($39 paid monthly), with a 3-day free trial then $1 a month for 3 months. Card rate 2.9% + 30¢. Included at no extra charge on Basic: Sidekick AI assistant, Shopify Inbox, 10,000 free marketing emails a month, Shopify Flow, Shopify Tax (free until $100,000 lifetime sales for stores created on or after May 13, 2026), Shopify POS basic features for markets, discounted shipping labels, 24 free themes, and the free-to-install Pinterest, Google & YouTube and Facebook & Instagram channel apps. V.
- The Shopify Starter plan exists in the help center (product links, Spotlight theme only, no collections) but its price is not on Shopify's US pricing page today; the page shows Basic, Grow, Advanced, Plus and an "Agentic $0/mo" tier for AI channels. Starter would not suit a 50-plus item vintage catalog anyway. V for features, U for Starter price.
- Linkpop is gone. apps.shopify.com/linkpop says the app is not currently available. Do not plan around it. V.

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Etsy fees (platform cost) | Listing, transaction, payment processing, Offsite Ads | "$0.20 per listing." / "6.5% of the total order amount in your designated listing currency." / "United States 3% + 0.25 USD" / "charged a 15% fee on the order total" (under $10,000) | No monthly fee; pay per listing and per sale | Web, iOS app | High: no fixed cost, one-of-one friendly | V | https://help.etsy.com/hc/en-us/articles/115014483627 ; https://help.etsy.com/hc/en-us/articles/115015628847 |
| Etsy Plus | Subscription with listing credits, ads credit, shop customization, restock requests, unlimited Marketplace Insights searches | "The fee for an Etsy Plus subscription is $10 USD per month" | None (15 listing credits and $5 ads credit per month are part of the paid plan) | Web | Low: credits worth $3 plus $5 ads; skip | V | https://help.etsy.com/hc/en-us/articles/360001589928 |
| Etsy Seller app | Create and edit listings, add photos and videos, orders, messages, stats, Etsy Ads, Share & Save links from the phone | "Free" | Whole app is free | iOS (also Android, listing not reachable today) | High: phone-first listing as Ricky wants | V | https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1534619962 |
| Etsy Share & Save | Refund of fees on orders from Hollie's own trackable links | "you get an instant refund of 4% off the eligible order total" / "From October 20 to January 4, all sellers enrolled in Share & Save will earn 6.5% back" | Free to enroll | Web (Shop Manager), Seller app | High: Hollie drives her own traffic from video | V | https://help.etsy.com/hc/en-us/articles/16981332744087 |
| Etsy Offsite Ads | Etsy advertises listings on Google, social and partner sites, fee only on attributed sales | "Charged a 15% fee for orders attributed to an Offsite Ad" / "The Offsite Ads fee for any individual order will never exceed $100 USD" | Automatic; shops under $10,000 can opt out | Web | Medium: on by default; decide opt-in or out early (section 2) | V | https://help.etsy.com/hc/en-us/articles/360000338367 |
| Etsy Ads | Paid placement inside Etsy search, daily budget | "All sellers start with a maximum daily budget of $25." / "there is a 15 day waiting period before you can begin an Etsy Ads campaign" | No free tier; set any daily budget | Web, Seller app | Low to medium: one-of-one items give ads little time to learn | V | https://help.etsy.com/hc/en-us/articles/360033701174 |
| Etsy Sales and Discounts | Sales, promo codes, bundles, targeted offers (thank-you, abandoned cart, favorites) | "four ways to discount items in your shop: sales, promo codes, discounted bundles of items, and targeted offers" / "between 5% and 75% off" | Free | Web, Seller app | High: targeted offers to favoriters suit one-of-one stock | V | https://help.etsy.com/hc/en-us/articles/115014260108 |
| Etsy Make an Offer | Buyers propose a price; seller sets maximum discount | Free tool; "only available for sellers and buyers who have their currency set to USD, and is not available on the Etsy Seller app" | Free | Web only (desktop or mobile browser) | High: haggling is native to vintage; 48-hour buyer window | V | https://help.etsy.com/hc/en-us/articles/16792774373143 |
| Etsy Stats and Search Analytics | Visits, views, conversion, traffic sources, year-over-year compare | Free; "You can view your shop stats from November 2017 to the present." | Free | Web, Seller app | High | V | https://help.etsy.com/hc/en-us/articles/115015774268 |
| Etsy Search Visibility page | Shows shop, listing and service-quality factors that affect search placement, optional title recommendations | Free; "US listings with domestic shipping prices lower than $6 will be prioritized in search" | Free | Web | High: free SEO checklist | V | https://help.etsy.com/hc/en-us/articles/25869947521175 |
| Etsy Marketplace Insights | Real Etsy search volume per keyword, related terms, 30-day trends | "Sellers can explore up to 15 keyword searches per week for free." | 15 searches a week; unlimited with Etsy Plus | Web (Shop Manager > Stats) | High: replaces a paid keyword tool at Hollie's scale | V | https://help.etsy.com/hc/en-us/articles/35122361353239 |
| Etsy listing videos | Up to 2 short silent videos per listing | Free; "You can add up to 2 videos per listing." / "3-15 seconds long and will not contain any audio" / "maximum size is 100 MB" | Free | Web, Seller app | High: lamps, turntable, chandeliers need motion | V | https://help.etsy.com/hc/en-us/articles/360053206073 |
| Etsy Purchase Protection for Sellers | Etsy refunds the buyer for lost or damaged orders and seller keeps earnings | "Etsy will cover up to $250 of a refund" | Automatic, no setup | Platform | High for glass and ceramics; needs Etsy label or valid tracking | V | https://help.etsy.com/hc/en-us/articles/5850122619287 |
| Etsy bulk edit | Edit many listings at once (tags, prices, sections, shipping) | Free; "You can't bulk upload new listings, but you can copy listings to save time." | Free | Web | Medium: good for price and tag sweeps | V | https://help.etsy.com/hc/en-us/articles/360000337307 |
| Etsy shared access | Up to 5 helpers manage orders, listings, messages with their own logins | Free; "invite up to 5 team members" | Free | Web | Medium: lets a helper or a future assistant work without the password | V | https://help.etsy.com/hc/en-us/articles/43600112070807 |
| Etsy quick list form and Stats assistant (tests) | AI suggests titles, tags, attributes from photos; AI answers stats questions | Free, limited rollout: "testing a new form that suggests titles, tags, attributes" / "expanding the beta of our AI-powered Stats assistant" | Free when available | Web | Medium: not controllable; keep Haiku draft plan | V | https://help.etsy.com/hc/en-us/articles/10603291042967 |
| Etsy vintage and AI-image rules | Policy, not a tool, but gates every listing | "vintage items that are at least 20 years old" / "Etsy requires at least one unedited photo for most items." | n/a | Policy | High: one untouched photo per listing; cutouts fine for the rest | V | https://help.etsy.com/hc/en-us/articles/360024112614 ; https://help.etsy.com/hc/en-us/articles/44297885802647 |
| eBay fees, no Store (platform cost) | Insertion, final value, per-order fee | "First 250 listings free per month, then $0.35 per listing" / "13.6% on total amount of the sale up to $7,500 calculated per item" / "for orders over $10.00 the per order fee is $0.40" | 250 zero-insertion-fee listings a month | Web, iOS, Android | High: no fixed cost; 24 photos free | V | https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822 |
| eBay Store subscription | More free listings, lower fees in Antiques and Art, Store-only marketing tools | "Starter $7.95 $4.95" / "Basic $27.95 $21.95" (monthly renewal, yearly renewal, both charged monthly) / Basic and up: "Antiques 12.7% on total amount of the sale up to $2,500" | None | Web | Low at launch; Basic maybe later (section 2 math) | V | https://www.ebay.com/help/selling/fees-credits-invoices/store-fees?id=4809 ; https://export.ebay.com/en/growth/ebay-store/subscriptions-and-fees/ |
| eBay Seller Hub | Listings, orders, marketing, performance, research, reports in one place | "It's free to use and consolidates all our selling tools into one location." | Free | Web | High | V | https://www.ebay.com/help/selling/selling-tools/seller-hub?id=4095 |
| eBay Product Research (Terapeak) | 3 years of sold-price data by keyword, condition, filters | "Sellers with access to Seller Hub can use Product research for free." / "it's free to all sellers. Find it under the Research tab in Seller Hub." | Free; Sourcing Insights needs a Store | Web, eBay app | High: comps for every one-of-one piece | V (eBay.ca help page and ebay.com Seller Center; the ebay.com help page captcha-walled) | https://www.ebay.ca/help/selling/selling-tools/terapeak?id=4853 ; https://www.ebay.com/sellercenter/growth/ebay-research-tools |
| eBay Promoted Listings (general) | Pay a percent of the sale only when a promoted item sells after a click | "You choose an ad rate between 2% - 100% of the item's total sale amount" / "Above Standard or Top Rated sellers with enough account activity can promote fixed price listings" | No fee unless sale | Web | Medium, later: need seller standing first; fee base includes shipping and tax | V | https://www.ebay.com/help/selling/ebay-advertising/promoted-listings/general-campaign-strategy?id=4164 |
| eBay Offers to Buyers and Best Offer | Send private discounts to watchers and cart-adders; auto-repeat; Best Offer on listing | Free; "Items a buyer is watching" / "Items added to a buyer's cart" / rule-based automation: "eBay Store subscribers can save time and effort with rule-based automatic offers" | Free (rules need a Store) | Web (Seller Hub), app | High: same haggle logic as Etsy Make an Offer | V | https://www.ebay.com/sellercenter/growth/seller-hub-discounts/offers-to-buyers-best-offer |
| eBay Sale events and Discounts Manager | Strikethrough sale pricing, coded coupons, order discounts | Free with Store: "eBay Store subscribers can find sale events on the Marketing tab within Seller Hub." | Store subscribers only | Web | Low at launch: Store-gated | V | https://www.ebay.com/sellercenter/growth/seller-hub-discounts/sale-events ; https://www.ebay.com/help/selling/selling-tools/seller-hub?id=4095 |
| eBay bulk edit and Seller Hub Reports | Edit many listings at once; CSV or XLS upload and download | Free; "Create and manage listings, individually or in bulk" / "Seller Hub Reports, formerly known as eBay File Exchange" | Free | Web | Medium | V | https://www.ebay.com/help/selling/selling-tools/seller-hub?id=4095 ; https://www.ebay.com/sellercenter/listings/ebay-bulk-listing-tools |
| eBay seller videos and photos | Video after first image on the app; 24 photos | "Buyers can see your videos on the View Item page of the eBay app." / "You can add up to 24 photos with zoom and enlarge ... free of charge." | Free | Web, app | High | V | https://www.ebay.com/sellercenter/listings/seller-uploaded-videos ; https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822 |
| eBay AI descriptions and magical listing | AI writes title and description from a photo in the app; background removal | Free. eBay Inc 2023 page: "take or upload a photo in the eBay app (iOS-only for now) and watch AI fill in item information details" | Free | eBay app (iOS, Android for descriptions) | Medium: fast first draft, must be checked for vintage attribution | V for the 2023 eBay Inc page; U for current desktop availability | https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/ |
| eBay International Shipping | Ship to a US hub; eBay handles customs, international leg, returns | "There's no extra charge to ship your items with eBay International Shipping and you won't be charged an international fee." | Free, automatic for eligible sellers | Platform | High: worldwide reach with domestic effort | V | https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/ebay-international-shipping-program?id=5348 |
| eBay Live | Livestream auctions and sales in the eBay app | "eBay Live is currently in beta with select sellers." | n/a | eBay app | Low now: apply via interest form; approved categories only | V | https://pages.ebay.com/ebaylive-faq/ ; https://www.ebay.com/help/policies/member-behavior-policies/ebay-live-policy?id=5478 |
| Shopify plans (platform cost) | Hosted store, checkout, admin | "Try 3 days free, then $1/month for 3 months." / "Pay monthly $39 USD/mo $105 USD/mo $399 USD/mo" / "Pay yearly $29 USD/mo $79 USD/mo $299 USD/mo" / "Online standard card rates 2.9% + 30¢" (Basic) | 3-day trial then $1 a month for 3 months | Web, iOS, Android app | High when the own site is wanted; Basic yearly is the right tier | V | https://www.shopify.com/pricing |
| Shopify Starter plan | Product links for social and messages, Spotlight theme only | Price not on the US pricing page today; features: "The Starter plan lets you create product links" / "Other themes and customization options aren't available on the Starter plan." | n/a | Web | Low: no collections, one theme, no third-party carrier rates | V (features), U (price) | https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/shopify-starter-plan |
| Shopify Sidekick and AI tools | AI assistant in admin and app: descriptions, images with transparent backgrounds, tasks, theme blocks; background color replace in file editor | "Many of these features are available at no additional cost, but availability can vary by plan, device, and language." | Included | Web admin, Shopify app, voice | High: free drafting inside the store | V | https://help.shopify.com/en/manual/ai-powered-tools ; https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick ; https://www.shopify.com/sidekick |
| Shopify Email (now Shopify Messaging) | Email campaigns and automations | "All stores on these plans have 10,000 free emails to send at the beginning of every month." / "$1 USD per 1,000 additional emails" | 10,000 emails a month on Basic, Grow, Advanced, Plus | Web | High: more than enough for a small list | V | https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging/email/pricing |
| Shopify Flow | No-code automation (tag, notify, hide sold items) | "Shopify Flow is a free app available on the Basic, Grow, Advanced, and Plus plans." | Free on Basic and up; HTTP request action needs Grow | Web | Medium: Pushover-style alerts can come from here later | V | https://help.shopify.com/en/manual/shopify-flow |
| Shopify Tax | Sales tax calculation and collection | "For stores that were created on or after May 13, 2026, Shopify Tax is free until you reach a lifetime threshold of sales." / "$100,000 USD" / then "0.35%" on Basic, Grow, Advanced, max "$0.99 USD" per order | Free to $100,000 lifetime | Web | High: Florida sales tax handled free for years at Hollie's volume | V | https://help.shopify.com/en/manual/taxes/shopify-tax/pricing |
| Shopify POS (basic) | Sell in person at markets with the phone; POS Pro add-on | "+ $89 USD/month for each POS Pro location" / Basic in-person card rate "2.6% + 10¢ USD in person" / POS "Included in every plan" | Basic POS features included with any plan | iOS, Android | Medium: markets and pop-ups; the word "Lite" no longer appears on the pricing page | V | https://www.shopify.com/pos/pricing ; https://help.shopify.com/en/manual/sell-in-person/shopify-pos |
| Shopify Shipping | Discounted USPS, UPS, DHL labels from admin; insurance | "Discounts for shipping labels vary based on your Shopify plan." / "Up to $200 insurance at no extra cost on every order" (Grow, Advanced, Plus only) | Included; percent discount not published on the pages read | Web, app | Medium: Basic gets labels but not the free $200 insurance | V | https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels ; https://www.shopify.com/shipping |
| Shopify Inbox | Live chat with an AI sales associate trained on the catalog | "Pricing Free" | Free | Web, Shopify app | High: answers "is it still available" at 2 a.m. | V | https://apps.shopify.com/inbox |
| Shop app channel and Shop Campaigns | Free listing in the Shop app; pay-per-conversion ads | Listing: automatic if eligible. Campaigns: "You're charged only when a customer converts, with no upfront budget or subscription fee." | Free channel | Shop app (iOS, Android) | Medium | V | https://help.shopify.com/en/manual/online-sales-channels/shop ; https://help.shopify.com/en/manual/online-sales-channels/shop/shop-campaigns |
| Shopify Collabs | Affiliate and creator program | "Free to install" / "+ 2.9% commission processing fee on automatic payments may apply" | Free to install | Web | Low: Open Access is on by default and one review reports commission fraud | V | https://apps.shopify.com/collabs |
| Linkpop | Link-in-bio page | "This app is not currently available on the Shopify App Store." | Gone | n/a | None: discontinued | V | https://apps.shopify.com/linkpop |
| Shopify free themes | Theme Store free filter | "24 themes" listed Free, including Dawn, Craft, Studio, Origin, Refresh, Sense, Crave, Publisher, Taste, Colorblock, Ride, Rise | 24 free | Web | High: Studio or Craft suit art and objects; Hollie already has a custom site design anyway | V | https://themes.shopify.com/themes?price%5B%5D=free |
| Pinterest, Google & YouTube, Facebook & Instagram channel apps | Catalog sync to each network, tags, ads from Shopify | Each: "Free to install. Additional charges may apply." (ad spend) | Free to install | Shopify apps by Pinterest Inc, Google LLC, Meta | High for Pinterest and Google (free organic product pins and listings); Meta needs a commerce account | V | https://apps.shopify.com/pinterest ; https://apps.shopify.com/google ; https://apps.shopify.com/facebook |

## 2. Notes per tool

### Etsy

**Fees (V).** Listing $0.20, charged again on auto-renew every 4 months and $0.20 per extra quantity sold (irrelevant for quantity 1). Transaction 6.5% of item plus shipping plus gift wrap. Payment processing 3% + $0.25 for a US bank account. Currency conversion 2.5% only if listing currency differs from the bank currency (list in USD). Regulatory operating fee applies in some non-US countries only. Worked example, my arithmetic: $100 item plus $12 shipping, no Offsite Ad: $0.20 + $7.28 + $3.61 = $11.09 (9.9% of $112). If the sale is attributed to an Offsite Ad at the 15% rate, add $16.80, total $27.89 (24.9%).

**Offsite Ads (V).** "You can't choose which listings are advertised." Shops that have never made $10,000 in any 365 days are enrolled automatically but may opt out in Shop Manager. Once the shop crosses $10,000, participation is mandatory for the shop's lifetime at 12%. Attribution is last click within 30 days; if the last click was an Etsy Ad, only the Etsy Ads fee applies. Fee cap $100 per order. Decision for Hollie: for high-ticket one-of-ones (chandeliers, signed memorabilia) a 15% hit on a $400 sale is $60. Opt out while under $10,000 if her own video traffic is the plan; opt in if she wants Etsy to buy Google Shopping placement for her. Either way the choice disappears at $10,000.

**Etsy Plus (V).** $10 a month buys 15 listing credits ($3 of value), $5 of Etsy Ads credit, restock requests (useless for quantity 1), banner and layout options, and unlimited Marketplace Insights searches. Credits expire monthly. Skip unless the 15-search weekly cap on Marketplace Insights becomes a real block.

**Etsy Seller app (V, App Store).** Free, 63K ratings, requires iOS 15.0 or later. Vendor list: add and edit listing videos and photos from the phone, orders, messages with repeat-buyer tags, listing-level stats. Help pages confirm the app can set up Etsy Ads, add listing videos, copy Share & Save links for promo codes and shop sections, and show Stats. Not in the app: Make an Offer setup (web only). Complaints in the App Store reviews read today: a draft listing cannot be saved half-finished ("I have to completely finish all fields"), listing search inside the app misses items, expired listings must be renewed one by one, listings cannot be rearranged from the phone. Reviews are undated in the fetched text; treat as a pattern, not a current bug list.

**Share & Save (V).** Free to enroll. 4% of the order total (item plus shipping, before tax) refunded instantly when a buyer orders within 30 days of clicking a trackable link to yourshopname.etsy.com, a listing, a promo code or (app only) a shop section. Holiday promotion: 6.5% back from October 20 to January 4, which is the whole transaction fee. Exclusions: links in Etsy Messages or listing descriptions do not count; if the buyer's last click was an Offsite Ad the order is not eligible. This is the direct payoff for the video plan in docs/video-direction.md: every TikTok, Instagram and YouTube link should be the Share & Save link.

**Etsy Ads (V).** Daily budget, starting maximum $25 a day, recalculated weekly. 15-day wait after opening the shop. Below a $25 maximum all listings use the "Efficient Spending" strategy; at $25 or more the seller can pick strategies per listing. Can be managed in the Seller app. Fit: weak for quantity-1 items because the ad learns on a listing that disappears when it sells. Try $1 to $3 a day on evergreen categories only if Offsite Ads is off and search traffic stalls.

**Sales and Discounts, Make an Offer (V).** Four native discount types: sales (5% to 75%, or free shipping), promo codes, bundles, targeted offers. Multiple sales cannot stack; the highest applies. Make an Offer: seller sets a maximum discount or accepts all offers; offers arrive as Messages (excluded from the Star Seller 24-hour clock); seller sends a final price; buyer has 48 hours; accepting does not reserve the item. USD-only, web-only setup, still labeled a test.

**Stats, Search Visibility, Marketplace Insights (V).** Stats back to November 2017 with year-over-year compare. Search Visibility lists shop, listing and customer-service factors and offers title recommendations; it states US listings with domestic shipping under $6 get priority, which matters for lamps and chairs (consider building shipping into price). Marketplace Insights: 15 free keyword searches a week with 30-day search and listing counts, related terms and trends; Plus removes the cap. New in the Newly Crafted page: side-by-side graphs, personalized keyword recommendations (test) and an AI Stats assistant (beta, by request).

**Listing videos (V).** Up to 2 per listing, 3 to 15 seconds, audio stripped, 100 MB max, 2:1 or 1:2 aspect ratio, ideal 1080px. Uploadable in the Seller app. Vendor says videos "can also help improve how your listings appear in Etsy search."

**Purchase Protection for Sellers (V).** Etsy refunds the buyer up to $250 for lost-in-transit or damaged (first damage case per calendar year) orders when the order shipped within processing time with valid tracking or an Etsy label, and the seller keeps the sale. Above $250 the remainder is charged to the seller, so insure the chandelier separately. Automatic, no setup.

**Bulk edit and copy (V).** Multi-select on the Listings page, then Editing Options for tags, prices, sections, shipping profiles and more. No bulk upload of new listings; copy an existing listing instead. Enough for Hollie's scale; a crosslister handles the rest.

**Shared access (V).** Up to 5 team members with their own Etsy logins; they manage orders, listings and messages but not finances. Free. Useful if a helper photographs or ships.

**Quick list form and AI features (V, Newly Crafted page).** Etsy is testing a listing form that suggests titles, tags and attributes from photos and descriptions, "with a limited number of sellers." Not something to rely on; the planned Haiku draft step stays. Appeals for removed listings expand to all sellers by end of 2026.

**Vintage and image policy (V).** Vintage means at least 20 years old. At least one unedited photo per listing: "the actual item against a real background," no lighting changes; crop, resize, watermark allowed. Other photos may use AI or editing tools including background changes "as long as those edits don't make the item appear different." The first image need not be the unedited one. This fits the rembg cutout workflow if every listing keeps one raw photo. AI-created items must be disclosed; AI prompt bundles and AI instructions are banned. Community Announcements (V) headline an "UPDATED NOV 6: Important updates to AI on Etsy" post and a new "€2 handling fee, starting November 1, 2026" for shipments into the EU. Third-party reports (U) say new AI terms effective December 16 let Etsy use shop content to train AI tools with no clear US opt-out; the Etsy post itself could not be read.

### eBay

**Fees without a Store (V).** 250 zero-insertion-fee listings a month, then $0.35 each. Good 'Til Cancelled listings renew monthly and count against the 250 each month, so 60 live one-of-ones use 60 of the 250 every month. Final value fee for most categories 13.6% of the total sale (item plus shipping plus tax) up to $7,500 per item, 2.35% above, plus $0.30 per order up to $10 and $0.40 over $10. No separate payment processing fee ("you don't have to worry about third-party payment processing fees"). Books, movies and music are 15.3%; women's handbags 15% to $2,000. Optional upgrades: Gallery Plus is free in Art, Antiques, Collectibles and Pottery & Glass. 24 photos and scheduled listings are free. Worked example, my arithmetic: $100 item plus $12 shipping: 13.6% of $112 = $15.23 + $0.40 = $15.63 (14.0%), versus Etsy's $11.09 without Offsite Ads. Penalties: Below Standard adds 6% to final value fees; a Very High "not as described" return rate adds 5%.

**Store subscriptions (V).** Starter $7.95 monthly renewal or $4.95 yearly renewal (both billed monthly), 250 free listings then $0.30. Basic $27.95 or $21.95, 1,000 free listings then $0.25, plus a quarterly eBay-branded shipping supplies coupon ($25 for Basic per export.ebay.com). Basic and above lower Antiques and most Art to 12.7% on the first $2,500 per item (2.35% above). Starter keeps the 13.6% rate. Break-even, my arithmetic: 0.9 points saved times monthly Antiques and Art sales must beat $21.95, so about $2,440 a month of sales in those categories; counting the $25 quarterly coupon as $8.33 a month, about $1,510. Below that, no Store. Store-only tools: Sourcing Insights, rule-based automatic offers, sale events and Discounts Manager, Markdown.

**Seller Hub (V).** Free. Tabs: Overview, Orders, Listings (individual or bulk), Marketing (some tools Store-only), Store, Performance (sales, costs as a percent of sales, traffic sources), Research, Reports (CSV/XLSX upload and download, the old File Exchange). Discounts Manager is for Store subscribers.

**Product Research, formerly Terapeak (V via eBay.ca and ebay.com Seller Center; ebay.com help page captcha-walled twice).** Free to everyone with Seller Hub since April 2021. Three years of sold data filtered by keyword, condition, brand, location, with average shipping and free-shipping share. Also in the eBay app. Sourcing Insights needs a Store. This replaces a paid comps tool for pricing one-of-ones.

**Promoted Listings (V).** General strategy: fee is a percent of the total sale (including shipping and tax) charged only when a promoted item sells within 30 days of a click; seller sets 2% to 100%, fixed or dynamic. Priority strategy is pay-per-click. Promoted Offsite pushes to Google. Eligibility: Above Standard or Top Rated with enough account activity, so a brand-new account cannot use it yet. For one-of-ones a 3% to 5% general rate on slow pieces is a reasonable later experiment; never set dynamic without a cap.

**Offers to Buyers and Best Offer (V).** Free. Send a private discount to watchers and cart-adders from the Listings tab ("Send offers-eligible" filter), singly or in bulk; option to auto-repeat the same offer to future interested buyers. Rule-based automation by category, price and condition is Store-only. Best Offer is a listing option that invites negotiation; both can run on the same listing. Counteroffer limit (3 each per the search summary) is U.

**Sale events and Discounts Manager (V).** Strikethrough "before and now" pricing, coded coupons, order-size and shipping discounts. Store subscribers only.

**Bulk editing, videos and photos (V).** Seller Hub bulk edit is free; Seller Hub Reports does CSV/XLS; Merchant Integration Platform is for feed files (overkill). Seller videos show after the first photo in the app. 24 photos free.

**AI listing tools (V for eBay Inc 2023 page, U for today).** eBay's own 2023 article: AI descriptions from a title and category rolled out to all US app users on iOS and Android; the photo-to-listing "magical" flow was iOS-only then; a background removal tool ships in the app. Third-party reports from the search phase (U) say the desktop description generator appeared and disappeared and that AI misidentified items. For vintage, the AI will guess maker and era; Hollie must check every attribution.

**eBay International Shipping (V).** Eligible US and Canada sellers are opted in automatically; the seller ships to a domestic hub and eBay handles customs, international shipping and returns. No extra charge and no international fee. Protection from "not as described" returns, negative feedback on international handling, item-not-received claims and chargebacks once the hub accepts the item. Items must be export-eligible; fragile glass is Hollie's risk only to the hub. Opt out in Shipping Preferences if ever needed.

**eBay Live (V).** Beta with select sellers; interest form required; sellers may list only in categories approved for eBay Live. Bid increments table on the FAQ ($1 steps from $1 to $29.99, up to $100 steps above $5,000). Third-party reports (U) say access is opening wider with a first-stream sales match. Not a launch tool.

### Shopify

**Plans and trial (V).** Basic $29 USD a month paid yearly or $39 paid monthly; Grow $79 or $105; Advanced $299 or $399; Plus from $2,300. Trial: 3 days free then $1 a month for 3 months. Basic card rates 2.9% + 30¢ online, 2.6% + 10¢ in person, 2% extra if a third-party payment provider is used. 1% back on sales as credits up to $5,000 on Basic. Marketplace sync: 50 synced marketplace orders a month free, then 1% up to $99 a month (relevant if Shopify Marketplace Connect were used; the decided crosslister is Crosslist). The pricing page also lists "Agentic $0/mo" for selling in AI channels, "Only pay when you make a sale." The Starter plan is absent from this page; its help page (V) describes product links, Spotlight theme only, no collections, no templates, no third-party carrier-calculated shipping, no staff. Starter price today is U.

**Sidekick and AI tools (V).** Sidekick works from any admin page, in the Shopify app, by voice and screen share; it drafts product descriptions and emails, generates and edits images (transparent-background generation announced on the Sidekick page), and runs multi-step tasks. The help center: "Many of these features are available at no additional cost, but availability can vary by plan, device, and language." The file editor can replace an image background with a color. Tinker is a free Shopify mobile app with 100-plus AI image and video tools. For Hollie: free second opinion on descriptions; the cutout engine stays rembg, but Sidekick's background-color replace is a free fallback.

**Shopify Email, now Shopify Messaging (V).** Basic and up: 10,000 free emails a month, then $1 per 1,000. Abandoned checkout emails are always free. Unused allowance does not carry over.

**Shopify Flow (V).** Free app on Basic and up. Send HTTP Request (needed to hit Pushover or Supabase directly) requires Grow. On Basic, Flow can still tag, email, hide sold-out products and the like.

**Shopify Tax (V).** New stores (created on or after May 13, 2026) get Shopify Tax free until $100,000 lifetime sales; older stores had an annual threshold. After that 0.35% on Basic, Grow and Advanced for US orders where tax is collected, max $0.99 per order, max $5,000 a year per region. Florida tax collection is therefore free for Hollie for years.

**Shopify POS (V).** Basic POS features are included with every plan ("Included in every plan"); POS Pro is +$89 USD a month per location. The pricing page no longer uses the name "Lite." In-person card rate 2.6% + 10¢ on Basic. Works on iOS and Android for markets and pop-ups. A card reader is extra hardware; price not read today.

**Shopify Shipping (V).** Discounted labels bought in admin; "Discounts for shipping labels vary based on your Shopify plan." Up to $200 shipping insurance at no cost only on Grow, Advanced and Plus with Shopify Payments. Basic can add paid insurance from the US. Specific carrier discount percentages were not on the pages read.

**Shopify Inbox (V).** Free. AI "Inbox agent" answers from the catalog and policies; merchant controls tone and rules; 5,820 reviews. Complaint read today: no API and no reply-by-email, so it stays a storefront chat, not a help desk.

**Shop channel and Shop Campaigns (V).** Store and products are listed in the Shop app automatically if the store meets the Shop Merchant Guidelines; Shop Pay and Shop Cash come with it. Shop Campaigns are pay-per-conversion with no upfront budget.

**Shopify Collabs (V).** Free to install; 2.9% commission processing fee on automatic affiliate payouts. A review read today warns that "Open Access" is on by default and lets anyone claim commissions; turn it off if ever installed. Low relevance now.

**Linkpop (V).** Not available on the App Store. Search snippets (U) date the shutdown to July 2025. Use the Shopify store's own landing page or a free link-in-bio tool from another lane.

**Themes and channel apps (V).** 24 free themes. Pinterest (Pinterest Inc), Google & YouTube (Google LLC) and Facebook & Instagram (Meta) apps are each "Free to install. Additional charges may apply," the charges being ad spend. Pinterest and Google sync the catalog for free organic product pins and Google listings; Google's app includes Product Studio image tools. These are the free distribution channels for a vintage catalog. Note: these are first-party channel apps, so they are in scope here; third-party apps are in other lanes.

## 3. Recommendation for Hollie

Free first, today:

1. **Etsy: enroll in Share & Save** the moment the shop opens and use that link everywhere (video bios, pinned comments, QR at markets). 4% back always, 6.5% back through January 4. Free.
2. **Etsy Seller app (iOS)** for listing from the phone: photos, 2 silent videos per listing, orders, messages, Stats, Ads. Keep one unedited photo per listing to satisfy the image rule; cutouts go in the other slots. Free.
3. **Etsy native marketing**: turn on Make an Offer (web) with a maximum discount, set a favorites and abandoned-cart targeted offer, and use Marketplace Insights' 15 free searches a week plus the Search Visibility page instead of a paid SEO tool. Free.
4. **Decide Offsite Ads before the first sale**: opt out while under $10,000 if the video plan is the traffic engine; otherwise leave it on and price high-ticket pieces knowing 15% may come off.
5. **eBay: open a plain seller account, no Store.** 250 free listings a month covers the whole catalog. Use Seller Hub, Product Research for comps, Best Offer on every listing, Offers to Buyers to watchers, 24 photos and a video. Leave eBay International Shipping on. Free.
6. **Shopify when the site is ready: Basic paid yearly, $29 a month**, after the 3-day free trial and the $1-a-month 3 months. Install the free Shopify Inbox, Flow, Pinterest and Google & YouTube apps, keep Shopify Tax (free to $100,000) and the included POS for markets. Sidekick drafts and Shopify Messaging's 10,000 free emails are already inside. This is the only recurring platform cost in the lane.

Pay only once it earns it:

- **eBay Basic Store ($21.95 a month yearly)** only when Antiques and Art sales on eBay pass roughly $1,500 to $2,400 a month, or when Hollie wants sale events and rule-based automatic offers.
- **eBay Promoted Listings general** at a fixed 3% to 5% on slow pieces once the account is Above Standard; never dynamic without a cap.
- **Shopify Grow ($79 a month yearly)** only if the $200 free shipping insurance, Flow HTTP requests to Pushover, or staff accounts become necessary.

Skip:

- **Etsy Plus ($10 a month)**: $3 of listing credits, $5 of ads, restock alerts for items that never restock.
- **Etsy Ads** beyond small tests: quantity-1 listings vanish before the ad learns.
- **Shopify Starter**: no collections, one theme; a 50-item vintage catalog needs Basic.
- **Shopify Collabs**, **eBay Live**, **Linkpop**: not relevant, beta, and gone, respectively.

## 4. Gaps and pages that would not load

- Web search budget for the session ran out midway; the remaining URLs came from vendor help-center search and API pages. Items not found through that route: an Etsy help article specific to the Seller app's feature list (App Store page used instead), Etsy's Share & Save program terms on etsy.com, and eBay's current help page for AI descriptions and the magical listing tool (only the 2023 eBay Inc article was readable).
- etsy.com returned HTTP 403 for https://www.etsy.com/legal/fees/ and https://www.etsy.com/news/newly-crafted-how-weare-investing-in-seller-success-fall-2026 . The help-center fee pages and the "Newly Crafted: Etsy Updates for Your Shop" help article covered the same ground.
- The Etsy Community post "UPDATED NOV 6: Important updates to AI on Etsy" is listed on the announcements index (read) but its own page URL was not recoverable; the Community API path 404ed. The December 16 AI-training terms claim is U.
- https://help.etsy.com/hc/en-us/articles/34707360607511 (creativity standards removal reasons) returned 404.
- Google Play listing for Etsy Seller (com.etsy.android.soe) returned 404 through the fetcher; Android availability is U today.
- ebay.com/help captcha-walled https://www.ebay.com/help/selling/selling-tools/terapeak-research-and-SEO?id=4853 twice; the eBay Canada help page and ebay.com Seller Center research page were used. Store fees, Seller Hub and eBay Live policy pages captcha-walled once each and loaded on retry.
- eBay help IDs 4165 and 4132 resolved to unrelated articles ("Page views", "Selling internationally"); treat those two fetches as misses. https://www.ebay.com/help/search?query=AI+description returned the 404 page.
- ebay.com/sellercenter pages for Stores overview, subscriber discounts, create great listings and bulk-listing-and-editing returned navigation only through the curl fallback (browser path blocked); the bulk tools, videos and research tools pages did load.
- help.shopify.com returned 403 for the shopify-magic URL on first try (resolved to the AI-powered tools page on retry) and for /sell-in-person/shopify-pos/pos-pricing. Shopify Starter plan price and Shopify Shipping carrier discount percentages were not on any page read. POS card reader hardware price not read.
- Sidekick's "Does using Sidekick cost money?" FAQ answer is collapsed on the marketing page and did not render; the help center's "no additional cost" line was used instead.
- eBay Offers to Buyers counteroffer limits, eBay Live's wider rollout and $100 first-stream match, and Linkpop's July 2025 shutdown date are U (search summaries only).

## 5. Sources

Every URL fetched today. Status in brackets.

Etsy
- https://help.etsy.com/hc/en-us/articles/115014483627 [V, fees and taxes]
- https://help.etsy.com/hc/en-us/articles/115015628847 [V, payment processing fees]
- https://help.etsy.com/hc/en-us/articles/360001589928 [V, Etsy Plus]
- https://help.etsy.com/hc/en-us/articles/360000338367 [V, Offsite Ads]
- https://help.etsy.com/hc/en-us/articles/16981332744087 [V, Share & Save]
- https://help.etsy.com/hc/en-us/articles/16792774373143 [V, Make an Offer]
- https://help.etsy.com/hc/en-us/articles/360033701174 [V, Etsy Ads setup]
- https://help.etsy.com/hc/en-us/articles/115014260108 [V, Sales and Discounts]
- https://help.etsy.com/hc/en-us/articles/360053206073 [V, listing videos]
- https://help.etsy.com/hc/en-us/articles/5850122619287 [V, Purchase Protection for Sellers]
- https://help.etsy.com/hc/en-us/articles/360000337307 [V, bulk edit]
- https://help.etsy.com/hc/en-us/articles/115015774268 [V, Stats]
- https://help.etsy.com/hc/en-us/articles/25869947521175 [V, Search Visibility page]
- https://help.etsy.com/hc/en-us/articles/35122361353239 [V, Marketplace Insights]
- https://help.etsy.com/hc/en-us/articles/360024112614 [V, What Can I Sell on Etsy]
- https://help.etsy.com/hc/en-us/articles/44297885802647 [V, listing image requirements and AI]
- https://help.etsy.com/hc/en-us/articles/10603291042967 [V, Newly Crafted: Etsy Updates for Your Shop]
- https://help.etsy.com/hc/en-us/articles/43600112070807 [V, Shared Access for Shop Owners]
- https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1534619962 [V, Etsy Seller app, App Store]
- https://community.etsy.com/announcements/ [V, announcements index]
- https://help.etsy.com/hc/en-us/search?query=share+and+save [V, discovery]
- https://help.etsy.com/hc/en-us/search?query=payment+processing+fees [V, discovery]
- https://help.etsy.com/hc/en-us/search?query=Etsy+Ads [V, discovery]
- https://help.etsy.com/api/v2/help_center/articles/search.json?locale=en-us&query=... (queries: share and save, payment processing fees, Etsy Ads campaign, listing videos, Purchase Protection, bulk edit, sales and discounts, Etsy Seller app, AI creations, manage your shop on the go, Etsy Seller app notifications, shared access) [V, discovery]
- https://www.etsy.com/legal/fees/ [FAILED 403]
- https://www.etsy.com/news/newly-crafted-how-weare-investing-in-seller-success-fall-2026 [FAILED 403]
- https://help.etsy.com/hc/en-us/articles/34707360607511 [FAILED 404]
- https://help.etsy.com/api/v2/help_center/en-us/articles/search.json?query=... [FAILED 404, wrong API path]
- https://community.etsy.com/api/2.0/search?q=... [FAILED, page not found]
- https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1543685519 [FAILED 404, wrong id]
- https://play.google.com/store/apps/details?id=com.etsy.android.soe&hl=en_US [FAILED 404]

eBay
- https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822 [V, selling fees]
- https://www.ebay.com/help/selling/fees-credits-invoices/store-fees?id=4809 [V on retry, Store selling fees]
- https://export.ebay.com/en/growth/ebay-store/subscriptions-and-fees/ [V, Store subscriptions and fees]
- https://www.ebay.com/help/selling/selling-tools/seller-hub?id=4095 [V on retry, Seller Hub]
- https://www.ebay.ca/help/selling/selling-tools/terapeak?id=4853 [V, Product research, eBay Canada help]
- https://export.ebay.com/en/resources/important-updates/ebay-news-archive/terapeak/ [V, Terapeak free since 2021]
- https://www.ebay.com/sellercenter/growth/ebay-research-tools [V, research tools]
- https://www.ebay.com/help/selling/ebay-advertising/promoted-listings/general-campaign-strategy?id=4164 [V, Promoted Listings general]
- https://www.ebay.com/help/selling/ebay-advertising/promoted-listings-overview?id=5295 [V, Promoted Listings overview]
- https://www.ebay.com/sellercenter/growth/ebay-advertising/promoted-listings [V, Seller Center Promoted Listings]
- https://www.ebay.com/sellercenter/growth/seller-hub-discounts/offers-to-buyers-best-offer [V, Offers to Buyers and Best Offer]
- https://www.ebay.com/sellercenter/growth/seller-hub-promotions/markdown-sale-events [V, redirected to sale-events]
- https://www.ebay.com/sellercenter/growth/seller-hub-discounts/sale-events [V, Sale events]
- https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/ebay-international-shipping-program?id=5348 [V, eBay International Shipping]
- https://pages.ebay.com/ebaylive-faq/ [V, eBay Live FAQ]
- https://www.ebay.com/help/policies/member-behavior-policies/ebay-live-policy?id=5478 [V on retry, eBay Live policy]
- https://www.ebay.com/sellercenter/listings/ebay-bulk-listing-tools [V, bulk listing tools]
- https://www.ebay.com/sellercenter/listings/seller-uploaded-videos [V, seller videos]
- https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/ [V, eBay Inc 2023 article]
- https://www.ebay.com/sellercenter/listings [V, little content]
- https://www.ebay.com/help/selling/fees-credits-invoices/zero-insertion-fee-listings?id=4165 [loaded but resolved to "Page views"; miss]
- https://www.ebay.com/help/selling/listings/creating-managing-listings/editing-listings?id=4132 [loaded but resolved to "Selling internationally"; miss]
- https://www.ebay.com/help/selling/selling-tools/terapeak-research-and-SEO?id=4853 [FAILED, captcha twice]
- https://www.ebay.com/help/search?query=AI+description [FAILED 404]
- https://www.ebay.com/sellercenter/listings/bulk-listing-and-editing [nav only via curl]
- https://www.ebay.com/sellercenter/listings/create-great-listings [nav only via curl]
- https://www.ebay.com/sellercenter/ebay-stores/overview [nav only via curl]
- https://www.ebay.com/sellercenter/ebay-stores/subscriber-discounts [nav only via curl]

Shopify
- https://www.shopify.com/pricing [V, plans and trial]
- https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/plans-features/shopify-starter-plan [V, Starter plan features]
- https://www.shopify.com/starter [V, redirected to /free-trial-offer]
- https://www.shopify.com/free-trial-offer [V, trial offer]
- https://www.shopify.com/magic [V, redirected to /sidekick]
- https://www.shopify.com/sidekick [V, Sidekick marketing page]
- https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick [V, Sidekick help]
- https://help.shopify.com/en/manual/ai-powered-tools [V, AI-powered tools help; reached from the shopify-magic URLs]
- https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/product-descriptions [V, resolved to AI-powered tools]
- https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/media-editing [V, resolved to AI-powered tools]
- https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic?locale=en [V, resolved to AI-powered tools]
- https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging/email/pricing [V, email pricing]
- https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-email/shopify-email-cost [V, redirected to the Messaging email pricing page]
- https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-email/pricing [V, redirected to Shopify Messaging overview]
- https://help.shopify.com/en/manual/shopify-flow [V, Flow]
- https://help.shopify.com/en/manual/taxes/shopify-tax/pricing [V, Shopify Tax pricing]
- https://www.shopify.com/pos/pricing [V, POS pricing]
- https://help.shopify.com/en/manual/sell-in-person/shopify-pos [V, POS overview]
- https://www.shopify.com/shipping [V, Shopify Shipping]
- https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels [V, shipping labels]
- https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels/carriers [V, third-party carrier-calculated shipping]
- https://help.shopify.com/en/manual/shipping/shopify-shipping [V, redirected to shipping labels]
- https://apps.shopify.com/inbox [V, Shopify Inbox]
- https://help.shopify.com/en/manual/online-sales-channels/shop [V, Shop channel]
- https://help.shopify.com/en/manual/online-sales-channels/shop/shop-campaigns [V, Shop Campaigns]
- https://apps.shopify.com/collabs [V, Shopify Collabs]
- https://help.shopify.com/en/manual/promoting-marketing/shopify-collabs [V, resolved to Marketing and promotions overview]
- https://apps.shopify.com/linkpop [V, not available]
- https://themes.shopify.com/themes?price%5B%5D=free [V, free themes]
- https://apps.shopify.com/pinterest [V]
- https://apps.shopify.com/google [V]
- https://apps.shopify.com/facebook [V]
- https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic [FAILED 403 on first try]
- https://help.shopify.com/en/manual/sell-in-person/shopify-pos/pos-pricing [FAILED 403]
- https://help.shopify.com/en/manual/sell-in-person/shopify-pos/pos-plans [V, redirected to POS overview]

Search-phase leads used only for discovery (U, not cited for facts): help.erank.com, alura.io, valueaddedresource.net, litcommerce.com, insightagent.app, taplink.at, biosites.com, techradar.com, howtosellyourstuff.substack.com, 3dsellers.com, retaildive.com.
