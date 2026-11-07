# Verification of lane 01: listing and crosslisting tools

Date 2026-11-07. Author: research subagent (adversarial price and claim checker). Question: Do the prices, free tiers, platform and availability claims in `01-listing-crosslisting.md` hold on the vendors' own pages today? Legend: V = page read today; U = unverified (snippet, roundup, memory, or the page would not load). Verdicts: confirmed = the exact figure or claim is on the page read today; refuted = the page says something different (correction given); unreadable = the page did not load after one alternative attempt.

Method: 38 vendor page reads with headless Chromium through the session proxy (curl fallback), plus the Apple iTunes Search and Lookup API for App Store records. Where a pricing page hides one billing period behind a tab, the tab was clicked with a small Playwright script and the revealed prices are recorded. No roundups or blogs were used for prices. Reddit, Etsy.com legal pages and eBay US help pages were not attempted. Every quote is verbatim from the page as rendered today; `...` marks skipped text.

## 0. Bottom line

- All eight PICKS hold on price. Crosslist Gold is still "$39.99 per month" with the "+$4.99/month" AI add-on; Vendoo Starter is "$12.49 Per month, billed yearly"; FLUF Starter is "$9 /month"; Voolist Starter is "$19.99 / month Billed monthly"; Closo Free is "$0 forever"; Etsy bulk edit, eBay's AI listing tools and Shopify Sidekick carry no extra charge.
- Two entries in TOOLS are refuted. PrimeLister's price was recorded as unknown because `/pricing` is 404; the real page is `/pricing/cross-listing` and shows "$49.99 Per Month" (or "$399.99 Per Year"), the dearest monthly price in the lane. Zipsale's Free plan is "10 items per month" today, not 30; the £25 tier is named Core, not Basic; a £15 "Part Time" tier exists; and the vendor says "Currently, Zipsale is made to be used in the UK."
- Two gaps are now filled. Vendoo's monthly prices (hidden behind the Pay Monthly tab) are "$14.99 Per month, billed monthly" for Starter, $29.99 Growth, $59.99 Pro. Crosslist's yearly prices (hidden behind the Yearly tab) are Bronze $24.99, Silver $28.99, Gold $32.99, Diamond $36.99 "per month billed yearly", AI "+$4.99/mo billed yearly".
- Flyp stays unreadable: flyp.com/pricing returns HTTP 403 and help.flyp.com fails its TLS certificate check. No Flyp crosslisting app appears in an App Store search.
- Shutdowns: inkfrog.com redirects to Wix's multichannel page today, consistent with the reported closure. No acquisition or shutdown notice was seen on any other vendor page read.
- Nothing else in the first agent's table was wrong on the pages read. Every other price, free tier, trial, listing cap and marketplace claim checked matched word for word.

## 1. Checks

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| Crosslist Gold | "$39.99 per month" (monthly billing) | confirmed | "Gold $39.99 per month Add 1000 new listings to your inventory every month." | https://crosslist.com/pricing | None. Yearly tab (clicked today): Gold "$32.99 per month billed yearly"; Bronze $24.99, Silver $28.99, Diamond $36.99. The first agent said the yearly toggle did not render. |
| Crosslist | AI add-on "+$4.99/month" on every plan | confirmed | "Upgrade with AI Get 1000 AI credits per month ... +$4.99/month" | https://crosslist.com/pricing | None. Yearly: "+$4.99/mo billed yearly". |
| Crosslist | No free plan; "20 free listings or 3-day refund" | confirmed | "Sign up now and get 20 free listings with our 3-day money-back guarantee*." | https://crosslist.com/pricing | None. Footnote: "Enjoy 3 days of Crosslist or 20 free listings, whichever comes first." |
| Crosslist | Autodelisting only from Gold ($39.99) | confirmed | Bronze and Silver lists read "9 images per listing All core features"; Gold adds "15 images per listing CSV import and export Autodelisting Sales analytics" | https://crosslist.com/pricing | None. "Sales detection" is a core feature on every plan; the automatic delist action is Gold and Diamond only. |
| Crosslist | Covers Etsy, eBay and Shopify | confirmed | "Shopify is an all-in-one e-commerce platform ... Etsy is a global marketplace for handmade, vintage, and craft goods." | https://crosslist.com/marketplaces | None. |
| Vendoo Starter | "$12.49 per month, billed yearly" | confirmed | "STARTER All you need to start crosslisting $12.49 Per month, billed yearly" | https://www.vendoo.co/pricing | Monthly tab (clicked today): "$14.99 Per month, billed monthly"; Growth "$29.99", Pro "$59.99" billed monthly. The first agent could not render it. |
| Vendoo | "14-day free trial" | confirmed | "Resell Smarter, Not Harder. Try Vendoo Free for 14 Days." | https://www.vendoo.co/pricing | None. Card requirement is behind a collapsed FAQ that did not render; U. |
| Vendoo | Auto-delist excludes Shopify | confirmed | "Sale Detection and Auto Delisting for Poshmark, eBay, Mercari, Depop, Whatnot, and Etsy." | https://www.vendoo.co/pricing | None. Marketplaces page lists Shopify and Etsy among "11 Markets". |
| Vendoo Go | iOS; "2 ratings at 2.0 stars" | confirmed | iTunes Lookup: `averageUserRating 2`, `userRatingCount 2`, released 2026-01-21, updated 2026-10-20 | https://itunes.apple.com/lookup?id=6746722923&country=us | None. |
| FLUF Connect Starter | "$9 /month"; "$85/year" first year; "7 days for $1" | confirmed | "Starter $9 /month −20% $85/year $108 First year ... Start 7 days for $1" | https://fluf.io/pricing/ | None. "Sales checked every 90 min" on Starter and "Team Accounts (+£20 p/m each)" both on the page. |
| FLUF Connect | Lists Etsy, eBay and Shopify as channels | confirmed | Channels page names "Etsy" and "Shopify"; "Crosslist from Shopify to Trendyol" | https://fluf.io/channels/ | None. |
| Voolist Starter | "$19.99 / month billed monthly"; 250 active listings; 14-day money-back; auto-delist on every plan | confirmed | "$ 19.99 / month Billed monthly Active listings 250 ... 14-day money-back guarantee ... Sales detection and auto-delist" | https://www.voolist.com/pricing | None. No free trial; "Try it risk-free for 14 days" refers to the refund. "Every Feature on Every Plan". |
| Voolist | Covers Etsy, eBay and Shopify | confirmed | "eBay, Poshmark, Depop, Etsy, Grailed, Whatnot, OfferUp, Vestiaire Collective, Shopify, and more" | https://www.voolist.com/marketplaces | None. |
| Closo Free | "$0 forever"; eBay and Shopify but no Etsy; no card | confirmed | "$0 forever No credit card. No caps on listings."; "Poshmark, eBay, Mercari, Depop, Vinted, Shopify" | https://closo.co/pages/pricing | None. Memberships "billed yearly": Member "$99 / year", Executive "$252 / year", Pro Trader "$499 / year". The only delist wording is the bulk action "Edit, delist, relist, clone"; no automatic delist is stated. |
| Etsy bulk edit | Free; no bulk upload, copy a listing instead | confirmed | "You can't bulk upload new listings, but you can copy listings to save time." | https://help.etsy.com/hc/en-us/articles/360000337307-Can-I-Create-or-Edit-Multiple-Listings-at-Once | None. Etsy Seller app (iTunes): "Free", rating 4.72 from 62,987. |
| eBay Seller Hub | "Multiple listings from photos" AI bulk drafts, desktop, free | confirmed | "Select “Multiple listings from photos” in the drop-down."; "now available to all sellers on desktop when opted in to Seller Hub" | https://www.ebay.co.uk/sellercentre/news/2025-january/ai-bulk-listings | None. This is a UK Seller Centre news page from January 2025; the US help page was not read. |
| eBay app | AI listing from photos in the app | confirmed | "Create a listing in a snap with the help of AI. Simply upload your photos, add your item description, and we’ll handle the rest." | https://apps.apple.com/us/app/ebay-online-shopping-selling/id282614216 | None. |
| Shopify Sidekick | Writes product descriptions at no extra cost | confirmed | "Sidekick writes text for the following: ... Product descriptions"; "Many of these features are available at no additional cost, but availability can vary by plan" | https://help.shopify.com/en/manual/ai-powered-tools | Caveat: Shopify says availability "can vary by plan, device, and language". The dedicated Sidekick help page returned HTTP 403 today. |
| Shopify Basic | "$29/mo yearly, $39/mo monthly"; 3-day trial then $1/month for 3 months | confirmed | "Pay monthly $39 USD/mo"; "Pay yearly $29 USD/mo"; "Try 3 days free, then $1/month for 3 months." | https://www.shopify.com/pricing | None. Same page: "Over 50 synced marketplace orders 1% up to $99/mo". |
| List Perfectly | Simple "$29 Monthly"; Sales Detection only at Pro $69; Auto Delist only at Pro Plus "$99+" | confirmed | "Simple $ 29 Monthly"; "Pro $ 69 Monthly ... Sales Detection"; "Pro Plus $ 99+ Monthly ... Auto Delist" | https://listperfectly.com/pricing/ | None. "Money Back Guarantee" row present; no trial wording on the pricing page. |
| SellerAider Crosslister | Standard "$12.99 / month"; Pro "$29.99 / month" with Automatic Delisting; 14-day trial, no card; Shopify not named | confirmed | "Crosslister Standard $12.99 / month"; "Crosslister Pro $29.99 / month ... Automatic Delisting"; "USE OUR 14 DAY FREE TRIAL"; crosslister page: "FOR FREE, NO CARD NEEDED" | https://selleraider.com/pricing/ and https://selleraider.com/crosslister/ | None. The crosslister page has zero mentions of Shopify (Etsy 4, eBay 3). Yearly toggle "YEARLY (20%+ OFF)". |
| PrimeLister | "price unknown (pricing page returned 404 today)" | refuted | "Pay Monthly $49.99 Per Month ... Auto Delisting Unlimited"; "Pay Yearly $33.33 Per Month When Paid Yearly $399.99 Per Year" | https://www.primelister.com/pricing/cross-listing | The price is public: $49.99 a month, or $399.99 a year. `/pricing` is 404, but the home page "Pricing" link goes to `/pricing/cross-listing`. One plan, unlimited crosslisting. Trial confirmed on the home page: "No credit card required ✓ 7-day free trial". Marketplaces named on the home page include Etsy, eBay, Shopify. |
| Posh Sidekick | Basic "$9.99/mo" 100 items; Silver $19.99 (250); Gold $29.99 (500); Enterprise $44.99 (1,000); 7-day trial, no card; 7 marketplaces, no Shopify | confirmed | "$9.99/mo Cross-post 100 items"; "7-day free trial [] No credit card required"; "All plans support Poshmark, eBay, Mercari, Depop, Etsy, Grailed and Whatnot crosslisting." | https://poshsidekick.com/pricing | None. "Auto de-list of sold items" ticked on every plan. Page served through the curl fallback. |
| Sellbrite (Shopify app) | Free up to 30 orders monthly, 2-hour sync; Pro 100 "$19 / month or $190/year"; 14-day trial on paid | confirmed | "Free Up to 30 Orders Monthly 2-hr Inventory Quantity Sync"; "$19 / month or $190/year and save 17% ... 14-day free trial" | https://apps.shopify.com/sellbrite | None. Pro 500 "$59 / month or $590/year"; Pro 2K "$99 / month or $990/year". |
| Shopify Marketplace Connect | Free to install; 50 synced orders free; 1% after; capped $99/month; no Etsy | confirmed | "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month"; channels "Amazon eBay Target Plus Walmart" | https://apps.shopify.com/marketplace-connect | None. |
| Zipsale | "Free £0/mo (30 items per month); Basic £25/mo or £21.25/mo billed yearly (200 items)" | refuted | "Free ... £0/mo billed monthly ... 10 items per month"; "Core ... £25/mo +VAT billed monthly ... 200 items per month"; "£15/mo +VAT ... 100 items per month" | https://www.zipsale.co.uk/pricing-subscriptions | Free plan is 10 items a month today, not 30. The £25 tier is "Core", not "Basic", and a £15 "Part Time" tier sits below it. All paid prices are "+VAT". The yearly price was not visible on the monthly tab. Top page: "From £15/month + VAT". |
| Zipsale | Usable from the US ("US availability unconfirmed", fit medium-low) | refuted | "Currently, Zipsale is made to be used in the UK. You can still ship your items internationally" | https://www.zipsale.co.uk/marketplaces | Vendor says UK only. Drop it for a Florida seller. Same page: "Zipsale is designed for single quantity items". |
| SellRaze Premium | "$3.75 per month or $44.99 / year" (annual only), 25 listings; Pro "$20 per month" (125); Elite "$30" (250); free trial, no card | confirmed | "$3.75 per month or $44.99 / year ... Up to 25 new listings/month"; "Start with a free trial. No credit card information required." | https://www.sellraze.com/pricing | None. Marketplaces are only described as "List to any marketplace"; Premium lists "Auto de-listing". |
| OneShop | "$45/month"; "Try 7 days free" | confirmed | "OneShop Premium ... $45/month"; home page: "Try 7 days free" | https://oneshop.com/pricing and https://oneshop.com/ | None. Footer still reads "© 2024 Inventory Systems, Inc." Supported marketplaces are not stated on either page. |
| Nifty | Crosslisting Plus "$35.99/month"; Crosslisting Pro "$53.99/month"; Bundle Plus "$62.99"; Automation "$22" single marketplace; 7-day trial; no Shopify | confirmed | "Crosslisting Plus ($35.99/month)"; "Crosslisting Pro ($53.99/month)"; "* $22 / month for Poshmark or eBay only"; "Explore our features with a 7-day free trial" | https://nifty.ai/pricing | None. Zero mentions of Shopify on the page; Etsy API notice present. |
| CedCommerce Etsy Integration | Beginner "$9 / month or $103/year" (10 products); Growth "$59 / month or $601/year" (1000); 7-day trial | confirmed | "$9 / month or $103/year and save 5% ... List up to 10 Products ... 7-day free trial" | https://apps.shopify.com/etsy-marketplace-integration | None. |
| Nembol | Basic "$39 / month or $351/year" (200 products); 14-day trial | confirmed | "$39 / month or $351/year and save 25% ... Manage up to 200 products ... 14-day free trial" | https://apps.shopify.com/nembol | None. Pro "$49 / month or $441/year"; Enterprise "$79 / month or $711/year". |
| LitCommerce | "From $29/mo"; 7-day free trial | confirmed | "From $29/mo"; "7-Day Free Trial Available for Multichannel Listing Tool." | https://litcommerce.com/pricing/ | None. |
| 3Dsellers Essential | "$19 /Mo" monthly or "$16" billed annually; 100 listings; 7-day trial, no card | confirmed | "$19 $16 /Mo Billed Annually SAVE $36! 100 Listings"; "Free 7-day trial No credit card required" | https://www.3dsellers.com/pricing | None. |
| Flip Press | iPhone app, solo developer, 4 ratings | confirmed | iTunes Search: "Flip Press: Reseller Toolkit", seller "Demitryus Richardson", rating 4.75, count 4, updated 2026-11-07 | https://itunes.apple.com/search?term=flyp+reseller&entity=software&country=us&limit=8 | None. Plan prices still not in App Store data. |
| Flyp | "price unknown (vendor site returned 403)" | unreadable | flyp.com/pricing: "HTTP 403 and 0 chars of text"; help.flyp.com: "SSL: no alternative certificate subject name matches target host name" | https://flyp.com/pricing | Still unreadable after the alternative. No Flyp crosslister in an App Store search for "flyp" (results are unrelated FLYP apps). Stays U. |
| inkFrog | "n/a (shut down)" | confirmed | inkfrog.com resolved to "https://www.wix.com/ecommerce/sell/multichannel", title "Multichannel Sales ... Wix eCommerce" | https://www.inkfrog.com/ | None. The redirect is the only evidence on vendor domains; the Wix page carries no inkFrog notice. |

## 2. What the first agent got wrong or left open

1. PrimeLister price "unknown". Wrong. The pricing page is at `https://www.primelister.com/pricing/cross-listing` (the `/pricing` path is 404). It shows one Cross Listing plan at "$49.99 Per Month" or "$33.33 Per Month When Paid Yearly" ($399.99 a year), with unlimited crosslisting and "Auto Delisting Unlimited". At monthly billing that is $10 more than Crosslist Gold, so the fit drops from medium to low on price.
2. Zipsale Free plan "30 items per month". Wrong today. The subscription page reads "10 items per month". The £25 tier is "Core", not "Basic", and there is a cheaper "Part Time" tier at "£15/mo +VAT" for 100 items. All paid prices add VAT. The yearly discount figure (£21.25) was not visible on the monthly tab and stays U.
3. Zipsale "US availability unconfirmed". Now answered by the vendor: "Currently, Zipsale is made to be used in the UK." Skip it.
4. Vendoo "monthly price not visible". Now filled: Starter "$14.99 Per month, billed monthly", Growth "$29.99", Pro "$59.99". The $12.49 figure is the yearly-billed rate and was quoted correctly.
5. Crosslist "yearly toggle did not render". Now filled: Bronze "$24.99", Silver "$28.99", Gold "$32.99", Diamond "$36.99" per month billed yearly; AI "+$4.99/mo billed yearly". The $39.99 Gold monthly figure stands.
6. Shopify Sidekick "included at no extra cost". Right in substance, but Shopify's own wording is softer: "Many of these features are available at no additional cost, but availability can vary by plan, device, and language." Keep the caveat.
7. Nothing else checked was wrong. All other prices, trial lengths, listing caps and marketplace lists matched the vendor pages word for word.

## 3. Pages that would not load

- https://www.primelister.com/pricing (HTTP 404) and https://app.primelister.com/pricing (empty): replaced by https://www.primelister.com/pricing/cross-listing, which loaded.
- https://flyp.com/pricing (HTTP 403) and https://help.flyp.com/ (TLS certificate name mismatch): Flyp stays unreadable.
- https://help.shopify.com/en/manual/sidekick (HTTP 403): the parent page https://help.shopify.com/en/manual/ai-powered-tools loaded and carries the product-description claim.
- Vendoo's pricing FAQ answers (card requirement) are collapsed accordions and did not render; https://www.vendoo.co/faqs has no price text.
- Not attempted: Reddit, etsy.com/legal, eBay US help pages, Chrome Web Store pages.

## 4. Sources (every URL fetched today)

https://crosslist.com/pricing
https://crosslist.com/marketplaces
https://www.vendoo.co/pricing
https://www.vendoo.co/marketplaces
https://www.vendoo.co/faqs
https://itunes.apple.com/lookup?id=6746722923&country=us
https://fluf.io/pricing/
https://fluf.io/channels/
https://www.voolist.com/pricing
https://www.voolist.com/marketplaces
https://closo.co/pages/pricing
https://help.etsy.com/hc/en-us/articles/360000337307-Can-I-Create-or-Edit-Multiple-Listings-at-Once
https://itunes.apple.com/search?term=etsy+seller&entity=software&country=us&limit=3
https://www.ebay.co.uk/sellercentre/news/2025-january/ai-bulk-listings
https://apps.apple.com/us/app/ebay-online-shopping-selling/id282614216
https://help.shopify.com/en/manual/ai-powered-tools
https://help.shopify.com/en/manual/sidekick (HTTP 403)
https://www.shopify.com/pricing
https://listperfectly.com/pricing/
https://selleraider.com/pricing/
https://selleraider.com/faq/
https://selleraider.com/crosslister/
https://www.primelister.com/pricing (HTTP 404)
https://app.primelister.com/pricing (empty)
https://www.primelister.com/
https://www.primelister.com/pricing/cross-listing
https://apps.apple.com/us/app/primelister-crosslisting-app/id6478108527
https://itunes.apple.com/search?term=primelister&entity=software&country=us&limit=5
https://poshsidekick.com/pricing
https://apps.shopify.com/sellbrite
https://apps.shopify.com/marketplace-connect
https://www.zipsale.co.uk/pricing
https://www.zipsale.co.uk/pricing-subscriptions
https://www.zipsale.co.uk/marketplaces
https://www.sellraze.com/pricing
https://oneshop.com/pricing
https://oneshop.com/
https://nifty.ai/pricing
https://apps.shopify.com/etsy-marketplace-integration
https://apps.shopify.com/nembol
https://litcommerce.com/pricing/
https://www.3dsellers.com/pricing
https://flyp.com/pricing (HTTP 403)
https://help.flyp.com/ (TLS failure)
https://itunes.apple.com/search?term=flyp+reseller&entity=software&country=us&limit=8
https://itunes.apple.com/search?term=flyp&entity=software&country=us&limit=10
https://www.inkfrog.com/ (redirects to https://www.wix.com/ecommerce/sell/multichannel)
