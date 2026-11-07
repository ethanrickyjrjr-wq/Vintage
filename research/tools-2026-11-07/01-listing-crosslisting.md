# Listing and crosslisting tools for Holliewood and Vine (lane 01)

Date 2026-11-07. Author: research subagent. Question: Which tools make creating a listing and posting it to Etsy, eBay and Shopify (and possibly other marketplaces) faster for one person, as of today, and what do they cost? Legend: V = page read today; U = unverified (snippet, roundup, memory, or the page would not load).

Method: 57 page reads with headless Chromium through the session proxy, plus the Apple App Store search API for app listings. Web search budget ran out after 11 searches, so the last third of the sweep used direct vendor URLs only. crawl4ai was not available. Prices are quoted as the vendor writes them. Where a page shows only the yearly-billed toggle, that is what is quoted and the monthly price is marked U.

## 0. Bottom line

- The cheapest tools that cover all three of Hollie's channels (Etsy, eBay, Shopify) from one form are FLUF Connect Starter ("$9 /month", V), Vendoo Starter ("$12.49 Per month, billed yearly", V) and Voolist Starter ("$19.99 / month, Billed monthly", V). All three list Etsy, eBay and Shopify on their own marketplace pages today.
- Crosslist Gold is still "$39.99 per month" (V, unchanged from 2026-10-26). Autodelisting and CSV only start at Gold; Bronze ($29.99) and Silver ($34.99) do not list them. AI features need a "+$4.99/month" add-on on every plan. The trial is "20 free listings with our 3-day money-back guarantee", not a free trial.
- Sale detection and auto-delist, the feature that stops a one-of-one item selling twice, is on the entry plan at Vendoo (but "for Poshmark, eBay, Mercari, Depop, Whatnot, and Etsy", not Shopify), Voolist (every plan), FLUF ("Sales checked every 90 min" on Starter), Posh Sidekick (all plans) and Nifty Crosslisting Plus. List Perfectly puts Sales Detection at $69 and Auto Delist at "$99+". SellerAider needs Crosslister Pro ($29.99). Zipsale excludes it from the Free plan.
- Free, built-in listing flows are better than they were: the eBay app creates a listing from photos with AI ("Create a listing in a snap with the help of AI", V), Seller Hub on desktop makes "Multiple listings from photos" (V), Etsy's Seller app creates and edits listings from the phone (V), and Shopify's Sidekick writes product descriptions at no extra cost on the Products page (V). Etsy still has no bulk upload: "You can't bulk upload new listings, but you can copy listings" (V).
- Closo now gives crosslisting away: "Crosslisting is free. Forever." to "Poshmark, eBay, Mercari, Depop, Vinted, Shopify" (V). No Etsy, so it is a partial fit only.
- Shopify-side sync apps are a different category (catalog and order sync, priced by orders): Shopify Marketplace Connect is free to install but has no Etsy; Sellbrite has a free plan ("Up to 30 Orders Monthly") covering Amazon, eBay, Etsy, Walmart; CedCommerce Etsy Integration's $9 plan only lists 10 products; Nembol starts at $39.
- Walls today: flyp.com (403), primelister.com/pricing (404), Reeva (no reseller site found; reeva.ai is an industrial software company), etsy.com/legal/api (403). inkfrog.com now redirects to Wix's multichannel page, consistent with the reported 2026-06-01 shutdown.
- eBay's User Agreement bans "any robot, spider, scraper, data mining tools ... or other automated means" without permission (V). Prefer tools that say they use the marketplace API for eBay and Etsy (Crosslist, Voolist, Nifty and SellerAider print Etsy API notices; Crosslist says it is "API-first whenever a marketplace supports it"). Facebook Marketplace posting always runs through a browser extension.

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Crosslist | One form to 11+ marketplaces incl. eBay, Etsy, Shopify, FBMP; autodelist from Gold | "Gold $39.99 per month"; Bronze "$29.99 per month"; AI "+$4.99/month" | "20 free listings with our 3-day money-back guarantee" | Web, iOS, Android, browser extension for non-API sites | Medium: covers all 3 channels, but autodelist needs the $39.99 tier | V | https://crosslist.com/pricing |
| Vendoo | Crosspost to 11 marketplaces incl. Shopify, eBay, Etsy; sale detection on Starter | "STARTER $12.49 Per month, billed yearly"; Growth "$24.99"; Pro "$49.99" (all billed yearly; monthly price not rendered) | "Try Vendoo Free for 14 Days" | Web, iOS, Android; Vendoo Go iOS | High: cheapest with all 3 channels and auto-delist on entry plan; auto-delist does not cover Shopify | V | https://www.vendoo.co/pricing |
| List Perfectly | Crosslist to 14 platforms incl. eBay, Etsy, Shopify | "Simple $29 Monthly"; "Business $49"; "Pro $69"; "Pro Plus $99+" | "Money Back Guarantee" row; platforms page says "Start Free Trial" | Web, "Mobile friendly" | Low: Sales Detection only at $69, Auto Delist at $99+ | V | https://listperfectly.com/pricing/ |
| FLUF Connect | Unlimited crosslisting to "70+ marketplaces" incl. eBay, Etsy, Shopify; AI listing from photo | "Starter $9 /month"; "$85/year" first year; "Pro $29 /month" | "Start 7 days for $1" | Web, "iPhone and Android app" | High: cheapest full-coverage tool; UK company, team seats priced in GBP | V | https://fluf.io/pricing/ |
| Nifty (ex Auto Posher) | Crosslister + automation for Poshmark, eBay, Mercari, Depop, Etsy, Whatnot | "Crosslisting Plus ($35.99/month)"; "Crosslisting Pro ($53.99/month)"; Bundle Plus "$62.99" | "7-day free trial" | Web (cloud); no mobile app seen | Low: no Shopify, $35.99 entry | V | https://nifty.ai/pricing |
| SellerAider | Chrome crosslister to eBay, Etsy, Poshmark and more; AI listing generation | "Crosslister Standard $12.99 / month"; "Crosslister Pro $29.99 / month" (Pro adds "Automatic Delisting") | "14 DAY FREE TRIAL" | Chrome extension, web, "Use on mobile" | Medium: cheap, but auto-delist needs Pro; Shopify not confirmed | V | https://selleraider.com/pricing/ |
| PrimeLister | Crosslist to Poshmark, eBay, Mercari, Depop, Etsy, Facebook, Grailed, Shopify; auto-delist | Price page 404 today; price unknown | "No credit card required, 7-day free trial" | Web, Chrome plugin, iOS app | Medium: features fit; price unverifiable | V (features) / U (price) | https://www.primelister.com/ |
| Flyp | Crosslister (competitor blogs say $9/month, 100-day trial) | unknown (site returns 403) | unknown | Web, app | U: could not read vendor page | U | https://crosslist.com/blog/flyp-cost (lead only) |
| OneShop | Reseller app: crosslist, auto-delist, bots | "$45/month" single "OneShop Premium" | "Try 7 days free" | iPhone app + web | Low: marketplace list not on vendor pages read; Poshmark heritage; 3.3 stars | V | https://oneshop.com/pricing |
| Zipsale | UK crosslister to 8 marketplaces incl. eBay, Etsy, Shopify, FBMP, Vinted | "Free £0/mo 30 items per month No autodelisting"; "Basic £21.25/mo £25/mo 15% OFF billed yearly 200 items"; credits "from £0.18 per item + VAT" | Free plan, 30 items/mo, no autodelist | Web | Medium-low: GBP pricing, US support unconfirmed | V | https://www.zipsale.co.uk/marketplaces |
| Posh Sidekick (Sidekick Tools) | Cross post to 7 marketplaces (Poshmark, eBay, Mercari, Depop, Etsy, Grailed, Whatnot) with auto de-list | "Basic $9.99/mo Cross-post 100 items"; "Silver $19.99/mo 250"; "Gold $29.99/mo 500" | "7-day free trial, No credit card required" | Web, iOS app | Low-medium: no Shopify; cheap for Etsy+eBay only | V | https://poshsidekick.com/pricing |
| ListingJoy | Crosspost tool, Etsy in title | "$39.99 / month" struck out, "100% FREE" (COVID-19 note) | Free for new users | Web | Skip: page looks unmaintained; gmail support | V | https://listingjoy.com/pricing/ |
| Hammoq | Enterprise resale platform (POS, AI identification) | no public price; "BOOK A DEMO" | none | Web | Skip: "Built for Goodwills, enterprises" | V | https://hammoq.com/ |
| Sellbrite | Shopify catalog sync to Amazon, eBay, Etsy, Walmart | Shopify app: "Free Up to 30 Orders Monthly"; "Pro 100 $19 / month"; "Pro 500 $59" | Free plan (2-hr sync) | Web, Shopify app | Medium: free Shopify-to-eBay/Etsy sync at low order volume; not a reseller listing form | V | https://apps.shopify.com/sellbrite |
| LitCommerce | Shopify multichannel listing to Etsy, eBay, TikTok Shop etc. | "Pay As You Go From $29/mo"; Shopify app "$29/month" | "7-Day Free Trial" | Web, Shopify app | Low-medium: Shopify-centric, $29 | V | https://litcommerce.com/pricing/ |
| 3Dsellers | eBay listing and store manager | "Essential $19 /Mo" monthly, "$16" billed annually, "100 Listings" | "Try 3Dsellers free for 7 days, no credit card needed" | Web | Low: eBay only unless Professional ($79) | V | https://www.3dsellers.com/pricing |
| Shopify Marketplace Connect | Shopify to Amazon, Target Plus, eBay, Walmart | "Free to install"; "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month" | Free | Shopify app | Medium for eBay only; no Etsy | V | https://apps.shopify.com/marketplace-connect |
| CedCommerce Etsy Integration | Shopify to Etsy sync | "Beginner $9 / month List up to 10 Products"; "Growth $59 / month List up to 1000 Products on Etsy" | "7-day free trial" | Shopify app | Low: $9 plan is 10 products | V | https://apps.shopify.com/etsy-marketplace-integration |
| Nembol | Shopify to eBay, Etsy, Amazon, TikTok Shop | "Basic $39 / month Manage up to 200 products" | "14-day free trial" | Shopify app | Low: $39 for 200 products | V | https://apps.shopify.com/nembol |
| Closo | Free crosslister to Poshmark, eBay, Mercari, Depop, Vinted, Shopify; paid "agents" | "Free $0 forever"; "Member $99 / year" | "No credit card. No caps on listings." | Web | Medium-low: free eBay+Shopify, but no Etsy; auto-delist not stated | V | https://closo.co/pages/pricing |
| FlowLister | AI eBay listing from photos; crosslist add-on to Poshmark and Mercari via Chrome | "Starter $19.99/mo" for "95 listing credits"; "Crosslisting add-on $499.99 once or $9.99/month" | "Free for 7 days. Card required." | Web, Chrome | Low: eBay only; no Etsy/Shopify | V | https://flowlister.com/pricing/ |
| Voolist | Cross-list to 11 platforms incl. eBay, Etsy, Shopify, WooCommerce; auto-delist on every plan | "Starter $19.99 / month Billed monthly 250 Active listings"; "Pro $29.99 / month" | "14-day money-back guarantee" (no free trial) | Web | High: all 3 channels, auto-delist on Starter, 25 AI listings/mo | V | https://www.voolist.com/pricing |
| SellRaze | AI listing from photos; "List to any marketplace"; auto de-listing | "Premium $3.75 per month or $44.99 / year" (annual only), "Up to 25 new listings/month"; "Pro $20 per month" 125 listings | "Start with a free trial. No credit card information required." | Web, iOS | Medium-low: cheap, but marketplace list not on pricing page | V | https://www.sellraze.com/pricing |
| Flip Press | iPhone app: photos to listings; eBay, Mercari, Poshmark, Etsy, Depop; auto delist | prices not in listing text | "Start with 7 days free. Every feature, every marketplace, no card." | iPhone + Chrome extension | Low-medium: no Shopify; solo developer, 4 ratings | V (features) / U (price) | https://apps.apple.com/us/app/flip-press-reseller-toolkit/id6751864685 |
| Etsy bulk edit + Seller app | Bulk edit titles, tags, descriptions, prices; copy listing; phone listing | free | free | Web, iOS, Android | High: the baseline | V | https://help.etsy.com/hc/en-us/articles/360000337307 |
| eBay magical listing / AI bulk | App listing from photos; Seller Hub "Multiple listings from photos" | free | free | iOS/Android app; Seller Hub web | High: free, eBay only | V | https://www.ebay.co.uk/sellercentre/news/2025-january/ai-bulk-listings |
| Shopify Sidekick (Magic) | Writes product descriptions in admin | included; Shopify Basic "$29/mo" yearly, "$39 USD/mo" monthly | n/a | Shopify admin | High for Shopify copy | V | https://help.shopify.com/en/manual/ai-powered-tools |
| Vendoo Go | Snap a photo, AI drafts, publish to "eBay and Mercari" | free app (needs Vendoo) | free download | iOS | Low today: 2 ratings, 2.0 stars, no Etsy/Shopify named | V | https://apps.apple.com/us/app/vendoo-go/id6746722923 |
| inkFrog | eBay listing tool, shut down | site redirects to Wix | gone | n/a | Skip | V (redirect) / U (date) | https://www.valueaddedresource.net/inkfrog-ebay-alternative-solutions/ |
| Reeva | AI listing app per competitor blogs | unknown | unknown | unknown | U: no vendor site found | U | none |

## 2. Notes per tool

### Crosslist (V)
- Pricing page, read today: Bronze "$29.99 per month" ("Add 200 new listings to your inventory every month", "9 images per listing"), Silver "$34.99" (500 listings), Gold "$39.99" ("Add 1000 new listings", "15 images per listing", "CSV import and export", "Autodelisting", "Sales analytics"), Diamond "$44.99" (unlimited, 24 images). Toggle shows "Quarterly -10%" and "Yearly 2 months free"; those prices did not render. Vendor blog pages seen earlier list annual Bronze at $24.99/mo and Gold at $32.99/mo (vendor's own blog, not the pricing page).
- AI: every plan card shows "Get N AI credits per month" but the line under it reads "Upgrade with AI ... +$4.99/month". The AI add-on page: "Create listings with AI. Upload a photo and let AI create or complete your entire listing in a few seconds. Consumes 1 credit per request." Bulk create from camera roll "1 credit per 10 images". Vendoo's blog (competitor) says the same: "you must pay an additional $4.99 per month".
- Trial: "Enjoy 3 days of Crosslist or 20 free listings, whichever comes first." Annual refunds carry "a small $9.99 processing fee".
- Marketplaces page: eBay, Poshmark, Facebook Marketplace, Depop, Mercari, Grailed, Shopify, Etsy, Whatnot, WooCommerce, OfferUp. "Crosslist is currently available in the United States, the United Kingdom, Canada, and Australia."
- How it posts: "Crosslist is API-first whenever a marketplace supports it ... When an API isn't available for the workflow needed, Crosslist uses a secure browser extension that runs inside your own browser".
- Mobile: iOS app "Crosslist" v0.5.4 (App Store, updated 2026-11-06), Android claimed on site.
- Change vs 2026-10-26: Gold still $39.99. Nothing changed.

### Vendoo (V)
- Pricing page renders the yearly toggle: "STARTER $12.49 Per month, billed yearly", "GROWTH $24.99", "PRO $49.99". Monthly-billing prices were not in the page text; the 2026-10-26 figure of $14.99 Starter monthly is therefore U today. Vendoo's own blog (2026-05-06): "Vendoo starts at just $12.49 per month".
- Starter includes "Unlimited Items", "All Marketplaces", "Sale Detection and Auto Delisting", "Listing Templates", "Importing", "Delist & Relist", "Analytics". The feature grid says: "Sale Detection and Auto Delisting for Poshmark, eBay, Mercari, Depop, Whatnot, and Etsy." Shopify is not in that list, so a sale on the Shopify site would not pull the Etsy and eBay copies down automatically.
- "AI Listing Enhancement" is on Growth and above. Background removal: "300 background removals powered by PhotoRoom" on Growth, 0 on Starter.
- Marketplaces page: "Shopify, Whatnot, Grailed, eBay, Depop, Sellwild, Poshmark, FBMP, Mercari, VC, Etsy".
- Trial: "Try Vendoo Free for 14 Days."
- Apps: Vendoo iOS 4.5 stars (2.9K ratings); "crosspost to 8 top marketplaces" from the phone (eBay, Etsy, Poshmark, Mercari, Grailed, Depop, VC, Whatnot). Vendoo Go (iOS, Oct 2026) "Snap a photo, let AI generate your item details, and publish directly to platforms like eBay and Mercari with just one tap." 2 ratings, 2.0 stars.

### List Perfectly (V)
- "Simple $29 Monthly" ("Crosslist to all marketplaces", "25 background removals", "AI Listing Assistant" 25/mo, "Mark sold"), "Business $49" (bulk, CSV), "Pro $69" ("Sales Detection", "Pro Description Builder"), "Pro Plus $99+" ("Auto Delist", "Sub Accounts"). "All plans include the features of the previous tier."
- Platforms page: "Cross-list to 14 marketplaces": eBay, Poshmark, Mercari, Depop, Grailed, Vestiaire Collective, Etsy, Facebook Marketplace, Instagram, Shopify, Whatnot, Listing Party, Vinted, Reverb.
- Trial: pricing table has a "Money Back Guarantee" row; the platforms page button says "Start Free Trial". SellerAider's comparison (competitor) says no free trial, 5-day money back. Unclear; treat as money-back.
- Change vs 2026-10-26: Simple still $29.
- Fit: the two features Hollie needs most (sale detection, auto delist) sit at $69 and $99+.

### FLUF Connect (V)
- "Starter $9 /month", "$85/year" first year ("-20%", list "$108"); "Pro $29 /month", "$155/year" first year ("-55%", list "$348"); "Priority Custom". FAQ: "Starter is $9/month, Pro $29/month, and Priority is custom. Every plan has unlimited crosslisting. Paying yearly saves 40%." The page also carried a countdown banner "55% off Pro Annual: pay once, done for 2027".
- Included on every plan: "All 70+ marketplaces", "Inventory sync", "Bulk editing tools", "Intesa AI assistant", "iPhone and Android app". "Team Accounts (+£20 p/m each)" shows the company is UK-based and bills some extras in GBP.
- Plan differences: "Sales checked every 90 min" (Starter) vs "60 min" (Pro); "Free AI product creations 50 / mo" vs "250 / mo"; analytics "Last 3 months" vs "Full history"; API "Read only" on Pro.
- Trial: "Start 7 days for $1". Also "Sign up for free" (account creation).
- Channels page lists eBay, Etsy ("8 countries"), Shopify, Facebook Marketplace, Depop, Vinted, WooCommerce and many EU classifieds. App Store (FLUF Ltd, v2.12, 2026-11-02): "Take a photo and FLUF's AI writes the listing ... Then publish to Depop, Vinted, eBay, Etsy, Facebook Marketplace, Poshmark, Mercari, Whatnot, Vestiaire Collective, Shopify, Amazon and many more, in one go."
- Change vs 2026-10-26: Starter still $9.

### Nifty (V)
- Crosslisting Plus "$35.99/month" ("Up to 1,500 active items", "500 smart credits per month", "AI-powered listing generation", "Sale detection and auto-delisting", "Drafts and scheduled posts"); Crosslisting Pro "$53.99/month". Automation "$35.99" or "$22 / month for Poshmark or eBay only". Bundle Plus "$62.99/month", Bundle Pro "$80.99/month". "Save up to 12%" yearly. "7-day free trial".
- Home FAQ: "Nifty's crosslisting and analytics features support Poshmark, eBay, Mercari, Depop, Etsy, and Whatnot. Automation runs on Poshmark, eBay, Mercari, and Depop." No Shopify. Formerly Auto Posher.
- Footer prints Etsy and eBay API notices ("This application uses the eBay API").

### SellerAider (V)
- "Crosslister Standard $12.99 / month": "Crosslist between 15+ all marketplaces", "Bulk delete, relist, mark sold", "AI listing generation", "Inventory Management", "Use on mobile". "Crosslister Pro $29.99 / month" adds "Photo Editing", "Accurate Price Suggestions", "Automatic Delisting" and the Grow Pro automation. Grow Standard "$18 / month", Grow Pro "$25 / month" (automation only). "YEARLY (20%+ OFF)". "14 DAY FREE TRIAL".
- Product page: "Crosslist to Marketplaces like Ebay, Etsy, Poshmark & More!", "Supports: U.K, U.S, C.A, FR & More", "INSTALL ON CHROME". Shopify is not named on the pages read.
- Their comparison article lists "Standard: $9.99 first month offer, then $12/month after", which does not match the pricing page ($12.99); the pricing page wins.

### PrimeLister (V features, U price)
- Home: "List once, sell on Poshmark, eBay, Mercari & more", "Manage inventory with auto-delist when sold", "No credit card required, 7-day free trial". Example copy names Poshmark, eBay, Mercari, Depop, Etsy, Facebook, Grailed, Shopify.
- primelister.com/pricing and app.primelister.com/pricing both failed (404 / empty). Price U.
- App Store listing (4.9, 2.4K ratings) describes the Poshmark bot first; a review mentions "the cross listing chrome plugin", so the crosslister is a Chrome extension plus web app.

### Flyp (U)
- flyp.com and flyp.com/pricing returned 403 or an empty page; help.flyp.com failed TLS. The App Store search for "flyp" returns unrelated apps. Only competitor blogs describe it: Crosslist's blog (updated 2026-09-24) says "Flyp costs $9/month" with "a 100-day free trial" and notes Etsy support is limited. Unverified. Ricky can check flyp.com in his own browser.

### OneShop (V)
- "One single subscription ... $45/month". "Try 7 days free". Home copy: "Automatically delist when you sell." The supported-marketplace list is not on the pricing or home page; the footer trademark line names Poshmark, Mercari, Tradesy, Depop, Etsy, Kidizen. App Store: iPhone only, 3.3 stars (471 ratings), "In-App Purchases". Vendor blog on crosslisting is dated 2021. Low fit.

### Zipsale (V)
- UK company; all prices GBP + VAT. Marketplaces page plan grid: "Free £0/mo ... 30 items per month No autodelisting"; "Basic £21.25/mo £25/mo 15% OFF billed yearly 200 items per month Autodelisting"; "Start £38.25/mo £45/mo ... 500 items"; up to "Business £126.65/mo £149/mo". Pricing page headline says "From £15/month + VAT", which does not match the grid; grid wins. Credits: "from £0.18 per item + VAT".
- "8 marketplaces": Vestiaire Collective, WooCommerce, Facebook Marketplace, Vinted, Shopify, Depop, eBay, Etsy. "*FB marketplace is not a part of autodelisting." Testimonial on the site: "A must for any vintage seller."
- US availability unconfirmed; help centre did not load.

### Posh Sidekick / Sidekick Tools (V)
- Cross Posting plans: Basic "$9.99/mo Cross-post 100 items", Silver "$19.99/mo 250", Gold "$29.99/mo 500", Enterprise "$44.99/mo 1,000" (adds AI stock photos, background remover). Every tier: "Auto de-list of sold items", "Bulk editing tools", "Relisting: 20/day". "All plans crosslist to 7 marketplaces: Poshmark, eBay, Mercari, Depop, Etsy, Grailed and Whatnot." "7-day free trial. No credit card required."
- No Shopify. The company's roots are Poshmark bots; its eBay and Mercari automations are the kind of activity eBay's User Agreement restricts (see Terms below).

### ListingJoy (V)
- Page shows "$39.99 / month" struck through to "100% FREE" because of "the COVID-19 crisis"; support "listingjoy@gmail.com". Reads as abandoned. Skip.

### Hammoq (V)
- "Built for Goodwills, enterprises, resale brands, and resellers." No price, "BOOK A DEMO" only. /pricing serves the home page. Skip.

### Sellbrite (V)
- sellbrite.com/pricing: "Free to start + unlimited access for 14 days. No credit card required." Plan prices are behind a JS tab; the Shopify App Store listing shows them: "Free ... Up to 30 Orders Monthly, 2-hr Inventory Quantity Sync"; "Pro 100 $19 / month or $190/year"; "Pro 500 $59 / month"; "Pro 2K $99 / month". Channels: "Amazon, eBay, Etsy, Walmart". Rating 3.9 (120). A merchant review: "Started out with the free plan, which does clearly start that each update is every 2 hours."
- This is a catalog and order sync for a Shopify store, not a reseller listing form. For a shop with under 30 orders a month the free plan would push Shopify products to eBay and Etsy and keep quantity 1 in sync every 2 hours.

### LitCommerce (V)
- "Pay As You Go From $29/mo", "Start from 1,000" listings, "Start from 3" channels, "15 mins" sync. "AI-Powered Listing Optimization Available for Etsy, eBay." Shopify app: "$29/month or $278/year", "7-day free trial". Shopify-centric; Etsy and eBay are target channels.

### 3Dsellers (V)
- eBay-only on the two lower plans: "Essential $19 /Mo" monthly or "$16 ... Billed Annually", "100 Listings", "1 eBay account". Growth "$39.90" ($29.90 yearly), "500 Listings". Professional "$79" ($59 yearly) adds "Multichannel catalog" (Shopify, WooCommerce, Amazon). "Try 3Dsellers free for 7 days, no credit card needed." AI Bulk Actions add-on "Starts at $9/mo". Its inkFrog migration page exists.

### Shopify Marketplace Connect (V)
- "Free to install. Additional charges may apply." "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month." "Works with Amazon eBay Target Plus Walmart." No Etsy. 4.1 stars (2,134). Shopify's own pricing page repeats the fee table. apps.shopify.com/shopify-marketplace-connect is a dead URL; the live slug is /marketplace-connect.

### CedCommerce Etsy Integration (Shopify app, V)
- "Beginner $9 / month ... List up to 10 Products ... Shopify to Etsy Inventory Syncing"; "Growth $59 / month ... List up to 1000 Products on Etsy, Sync up to 500 Orders per month". "7-day free trial". 4.5 stars (1,248). The $9 plan is far too small for 52+ items; the next step is $59.

### Nembol (Shopify app, V)
- "Basic $39 / month or $351/year", "Manage up to 200 products", "1 account for each sales channel", "14-day free trial". Channels: eBay, Etsy, Amazon, TikTok Shop, Facebook. 4.1 stars (57). More than a reseller crosslister for less coverage.

### Closo (V)
- "Crosslisting is free. Forever. List to all six marketplaces free, no card, no caps, no clock." Free plan: "Crosslist to all 6 marketplaces: unlimited", "Your own shop, 0% commission", "Listing Booster, 5 actions a day". Marketplaces: "Poshmark, eBay, Mercari, Depop, Vinted, Shopify". Paid: "Member $99 / year", "Executive $252 / year" (Auto-Pricer, Auto-Offers, Auto-Share), "Pro Trader $499 / year". "All memberships are billed yearly."
- Gotchas: no Etsy; sale detection and auto-delist are not named anywhere on the pricing page (U); "Your passwords never leave you" suggests a browser-side posting method. Worth a free look for the eBay+Shopify pair only.

### FlowLister (V)
- "Starter $19.99/mo" for "95 listing credits a month" (about $0.21 a listing); Pro "$49.99/mo" 375 credits. "Free for 7 days. Card required. Then $19.99/mo unless you cancel." "Crosslisting add-on $499.99 once or $9.99/month": "Posts an eBay listing to Poshmark and Mercari from your own Chrome browser." eBay-first AI listing writer founded 2025. No Etsy or Shopify. Skip.

### Voolist (V)
- "Starter $19.99 / month Billed monthly": "Active listings 250", "Drafts and inactive 1,000", "AI listings a month 25", "Accounts per marketplace 1". Every plan: "Cross-list to 11 platforms from one form", "Sales detection and auto-delist", "Bulk cross-listing", "One-click import or CSV upload", "AI listing writer", "Bulk edit, delist and relist", "Live chat support". Pro "$29.99 / month" (750 listings, 250 AI listings, "Two eBay accounts or two Shopify stores"). Power "$49.99". Yearly: "2 months free". "14-day money-back guarantee" rather than a free trial.
- Marketplaces footer: eBay, Poshmark, Depop, Etsy, Grailed, Whatnot, OfferUp, Vestiaire Collective, Shopify, BigCommerce, WooCommerce. Prints the Etsy API notice.
- Fit: 250 active listings covers the whole catalog several times over; auto-delist on every plan; all three channels. Newer company ("3000+ sellers"), so check support responsiveness during the money-back window.

### SellRaze (V)
- "Premium $3.75 per month or $44.99 / year" (billed annually only), "Up to 25 new listings/month", "AI-generated listing details", "Suggested pricing", "List to any marketplace", "Auto de-listing". "Pro $20 per month monthly billing", "Up to 125 new listings/month", "Bulk listing creation", "AI photo editing tools". "Elite $30 per month", 250 listings. "Start with a free trial. No credit card information required." Marketplaces are not named on the pricing page (App Store: "toggle your favorite marketplaces"). Cheap enough to test, but confirm Etsy and Shopify support in the app first.

### Flip Press (V features, U price)
- App Store (solo developer, 4 ratings, iPhone only): "Five marketplaces run from your phone: eBay, Mercari, Poshmark, Etsy and Depop", "Facebook Marketplace is supported too, on your computer ... through the Chrome extension", "Auto Delist Sold", "Upload your photos and get complete listings", "every plan includes 300 credits a month for the AI tools". "Start with 7 days free. Every feature, every marketplace, no card." Prices not in the listing text. No Shopify.

### Etsy built-in (V)
- Help: "You can edit multiple listings at once from your Listings page. Select the listings you want to edit, then select Editing options. You can't bulk upload new listings, but you can copy listings to save time." Bulk-editable: "Titles, Tags, Descriptions, Prices, Custom options, Production partners, Renewal options, Processing profile, Shipping profiles." Copy: "Copying creates a brand new listing with all of the info from the copied listing in place."
- Etsy Seller app (iOS, free, 4.7, 63K ratings, v2.10 on 2026-11-03): "create and edit listings", "Add and edit listing videos and photos straight from your phone." A help article URL guessed for the app was a 404.

### eBay built-in (V)
- Help "Creating a listing": "Quick listing tool, a guided, step-by-step flow for casual sellers", "Advanced listing tool, a unified listing experience available in Seller Hub", "Scan to list tool". Drafts: "You can save up to 250 drafts via the quick listing tool, or 5,000 through Seller Hub's bulk tools. Drafts expire 75 days after their last edit." The dedicated bulk-listing help URL redirected to a payments article, so the bulk editor's own help page was not read.
- Magical listing on mobile (eBay Inc. news, 2025-04-09): "take or upload a product image and use AI to help fill in item specifics", "now available in the eBay mobile app in the U.S., U.K., and Germany for private sellers across all categories." App Store description today: "Create a listing in a snap with the help of AI. Simply upload your photos, add your item description, and we'll handle the rest."
- AI bulk listing from photos (UK Seller Centre, Jan 2025): "available to all sellers on desktop when opted in to Seller Hub", "Head to your Listings page on Seller Hub and click 'Create listings.' Select 'Multiple listings from photos'". The US news post (Sep 2024) said it started with trading cards and would expand.
- Terms: eBay User Agreement, "Using eBay": you may not "use any robot, spider, scraper, data mining tools, data gathering and extraction tools, or other automated means ... to access our Services for any purpose, except with the prior express permission of eBay". API-based crosslisting is the permitted path; extension-driven eBay bots (relist, share, offer automations) are the risk.

### Shopify built-in (V)
- shopify.com/magic now redirects to the Sidekick page. Help Center "AI-powered tools": Sidekick "writes text for ... Product descriptions"; "Many of these features are available at no additional cost, but availability can vary by plan, device, and language." Products: "Get a suggested product category and category metafields based on your product details." Shopify pricing: Basic "$29/mo" paid yearly, "$39 USD/mo" monthly; "Try 3 days free, then $1/month for 3 months"; a new "Agentic $0/mo" plan for selling only in AI channels.

### inkFrog (V redirect, U date)
- inkfrog.com resolves to wix.com/ecommerce/sell/multichannel today. Value Added Resource (third party, 2026-05-15): "The Wix-owned listing and inventory management platform will shut down on June 1, 2026". Consistent with the 2026-10-26 sheet. Dead; skip.

### Reeva (U)
- reeva.ai is "Engineering intelligence for industrial enterprises"; reeva.io did not load; App Store search returns unrelated apps. Competitor blogs describe an AI listing app for Poshmark and eBay at $9 to $59 a month. Not findable today; treat as not available.

### Photoroom (out of lane, V page, no price text)
- The pricing page rendered plan names (Pro, Max, Ultra) and credits but not dollar amounts; it has a "Product & Listing AI tools" section and "Faster product listings" copy. Photo lane covers it. Vendoo resells "background removals powered by PhotoRoom" (300 on Growth).

### Terms and licence gotchas (summary)
- eBay bans scrapers and automated access without permission (V, quoted above). Prefer API-based tools for eBay and Etsy.
- Etsy's API terms page (etsy.com/legal/api) returned 403 today; Etsy-API notices are printed by Crosslist, Nifty, Voolist and SellerAider, which is a sign they went through Etsy's developer programme (U as to approval status).
- Facebook Marketplace has no listing API; every tool that offers it runs a browser extension (Crosslist: "uses a secure browser extension"; Flip Press: "through the Chrome extension") and Zipsale excludes it from autodelisting.
- Crosslist is not offered to EU residents; Florida is fine.
- Free tiers: Zipsale Free has "No autodelisting"; Sellbrite Free syncs every 2 hours; Closo Free is uncapped but has no Etsy; Crosslist's "free" is 20 listings or 3 days.
- Vendoo Starter auto-delist does not include Shopify; a Shopify sale needs a manual "mark sold".
- No watermark issues were seen on any crosslister page read.

## 3. Recommendation for Hollie

Free first (install today, costs nothing):
1. Etsy Seller app on the iPhone for photos and the first draft of each listing; Etsy web Shop Manager for bulk edits of titles, tags, descriptions, prices and shipping profiles. Etsy cannot bulk-create, so the copy-listing trick is the only shortcut for near-identical pieces (pairs of lamps, glass sets).
2. eBay app: list from photos with the AI flow ("Create a listing in a snap with the help of AI"). On the Windows PC, Seller Hub "Create listings > Multiple listings from photos" for batches. Both free, both eBay only.
3. Shopify Sidekick for product descriptions once the Shopify store exists (included in Basic).
4. Optional free crosslister for the eBay+Shopify pair: Closo Free ("$0 forever", "No caps on listings"). Not for Etsy. Check whether it detects sales before trusting it with one-of-one stock.

First paid step, only once listing by hand across three sites hurts (under $50 a month):
- Trial Vendoo Starter first (14 days free, no card requirement stated on the page): "$12.49 Per month, billed yearly"; Etsy, eBay and Shopify in one form; sale detection on Etsy and eBay. Know that a Shopify sale will not auto-delist elsewhere.
- If the yearly commitment or the Shopify gap bothers Ricky, Voolist Starter at "$19.99 / month Billed monthly" has auto-delist on every plan and all three channels, with a 14-day money-back window instead of a trial.
- FLUF Connect Starter at "$9 /month" ("Start 7 days for $1") is the cheapest with all three channels and unlimited listings. UK company; sales are checked every 90 minutes on Starter. Good second trial if Vendoo's phone app or pricing disappoints.
- Crosslist Gold stays the decided trial at "$39.99 per month", but note today's facts: autodelisting is Gold-only, AI costs "+$4.99/month" more, and the refund window is 3 days or 20 listings. At $44.98 with AI it is the most expensive option that fits. Trial it last, after Vendoo and FLUF, so the 3-day window is spent on a real comparison.

Pay only once it earns it:
- Vendoo Growth ("$24.99" yearly-billed) for AI listing enhancement and 300 background removals, or Crosslist's AI add-on, only if the free rembg + Claude Haiku pipeline in the planned dashboard is not ready.
- Sellbrite Pro 100 ($19/month) only if the Shopify store becomes the master catalog and 2-hour sync on the free plan causes a double sale.

Skip and why:
- List Perfectly: sale detection at $69, auto delist at $99+.
- Nifty ($35.99), Posh Sidekick, Flip Press, FlowLister, 3Dsellers: no Shopify (and the last two are eBay-only).
- OneShop ($45): marketplace list not even on its own site; Poshmark-first; 3.3 stars.
- CedCommerce Etsy ($9 = 10 products), Nembol ($39 for 200 products): store-sync apps priced above the reseller tools for less coverage.
- Hammoq (enterprise), ListingJoy (abandoned page), inkFrog (shut), Reeva (cannot be found), Flyp (vendor site walled; if Ricky can open flyp.com and it really is $9/month with a 100-day trial, it is worth a look).

What changed since the 2026-10-26 sheet: Crosslist Gold $39.99 unchanged. FLUF Starter $9 unchanged. List Perfectly Simple $29 unchanged. Vendoo Starter now reads $12.49 billed yearly on the pricing page; the $14.99 monthly figure could not be re-verified because the monthly toggle did not render. inkFrog's domain now redirects to Wix. New names worth knowing: Voolist, Closo (free), SellRaze, Flip Press, Vendoo Go.

## 4. Gaps and pages that would not load

- flyp.com, flyp.com/pricing (HTTP 403 / empty), help.flyp.com (TLS name mismatch, 502). Flyp price and Etsy support unverified.
- primelister.com/pricing (404), app.primelister.com/pricing (empty). PrimeLister price unverified.
- Reeva: reeva.ai is a different company; reeva.io empty. No reseller vendor page found.
- etsy.com/legal/api (403). Etsy API terms not read.
- help.zipsale.co.uk (proxy tunnel failed). Zipsale US availability unverified.
- oneshop.com/features (404), vendoo.co/features (404), vendoo.co/marketplaces/facebook-marketplace (404), listperfectly.com/marketplaces (404; /platforms worked), nifty.ai/features (404), apps.shopify.com/shopify-marketplace-connect (404; /marketplace-connect worked), apps.shopify.com/quicksync-for-etsy (404), sellbrite.com/pricing/sellbrite/ (404), simplylisted.com (TLS error), help.etsy.com Etsy Seller app article (guessed URL, 404).
- ebay.com help "bulk listing and editing tool" id=4185 redirected to the payments article; eBay's own bulk-editor help was not read.
- Vendoo monthly-billing prices, Crosslist quarterly and yearly prices, Sellbrite's own pricing tabs and Photoroom's dollar prices are behind JS toggles that did not render as text.
- Mobile app existence for Nifty and Voolist not confirmed either way.
- Web search budget was exhausted after 11 searches; Photoroom-to-listing features, QuickSync, ResaleOS and SimplyListed were not researched beyond one direct URL each.

## 5. Sources

Pages fetched 2026-11-07 (V unless noted):
- https://crosslist.com/pricing
- https://crosslist.com/marketplaces
- https://crosslist.com/marketplaces/facebook
- https://crosslist.com/marketplaces/etsy
- https://crosslist.com/blog/flyp-cost (competitor blog, lead only, U for Flyp facts)
- https://www.vendoo.co/pricing
- https://www.vendoo.co/marketplaces
- https://blog.vendoo.co/how-much-is-crosslist (vendor blog)
- https://apps.apple.com/us/app/vendoo-a-sellers-best-friend/id1612168777
- https://apps.apple.com/us/app/vendoo-go/id6746722923
- https://listperfectly.com/pricing/
- https://listperfectly.com/platforms/
- https://fluf.io/pricing/
- https://fluf.io/channels/
- https://nifty.ai/pricing
- https://nifty.ai/
- https://selleraider.com/pricing/
- https://selleraider.com/crosslister/
- https://selleraider.com/crosslisting-app/ (vendor comparison article, competitor claims not used)
- https://www.primelister.com/
- https://apps.apple.com/us/app/primelister-crosslisting-app/id6478108527
- https://oneshop.com/pricing
- https://oneshop.com/
- https://oneshop.com/blog/crosslisting-app (vendor blog, 2021, stale)
- https://apps.apple.com/us/app/oneshop/id1577487407
- https://www.zipsale.co.uk/pricing
- https://www.zipsale.co.uk/marketplaces
- https://poshsidekick.com/pricing
- https://listingjoy.com/pricing/
- https://hammoq.com/ (and https://hammoq.com/pricing, same page)
- https://www.sellbrite.com/pricing/
- https://apps.shopify.com/sellbrite
- https://litcommerce.com/pricing/
- https://apps.shopify.com/litcommerce
- https://www.3dsellers.com/pricing
- https://apps.shopify.com/marketplace-connect
- https://apps.shopify.com/etsy-marketplace-integration
- https://apps.shopify.com/nembol
- https://closo.co/pages/pricing
- https://flowlister.com/pricing/
- https://www.voolist.com/pricing
- https://www.sellraze.com/pricing
- https://apps.apple.com/us/app/flip-press-reseller-toolkit/id6751864685
- https://help.etsy.com/hc/en-us/articles/360000337307-Can-I-Create-or-Edit-Multiple-Listings-at-Once
- https://apps.apple.com/us/app/etsy-seller-manage-your-shop/id1534619962
- https://www.ebay.com/help/selling/listings/creating-managing-listings/creating-listing?id=4105
- https://www.ebay.com/help/policies/member-behavior-policies/user-agreement?id=4259
- https://innovation.ebayinc.com/stories/ebay-reduces-the-time-to-list-on-mobile-with-new-simplified-selling-tool-now-featuring-magical-listing-ai-technology/
- https://innovation.ebayinc.com/stories/magical-bulk-listing-tool-is-ebays-latest-ai-powered-time-saver-for-sellers/
- https://www.ebay.co.uk/sellercentre/news/2025-january/ai-bulk-listings
- https://apps.apple.com/us/app/ebay-online-shopping-selling/id282614216
- https://help.shopify.com/en/manual/ai-powered-tools (redirect from .../shopify-magic)
- https://www.shopify.com/sidekick (redirect from https://www.shopify.com/magic)
- https://www.shopify.com/pricing
- https://www.wix.com/ecommerce/sell/multichannel (redirect from https://www.inkfrog.com/)
- https://www.valueaddedresource.net/inkfrog-ebay-alternative-solutions/ (third party, U for the date)
- https://www.photoroom.com/pricing (prices not rendered)
- https://itunes.apple.com/search?term=...&entity=software (App Store search API, several queries)

Failed today (see section 4): https://flyp.com/ , https://flyp.com/pricing , https://www.flyp.com/ , https://help.flyp.com/ , https://www.primelister.com/pricing , https://app.primelister.com/pricing , https://reeva.ai/pricing (different company) , https://www.reeva.io/ , https://www.etsy.com/legal/api , https://help.zipsale.co.uk/ , https://oneshop.com/features , https://www.vendoo.co/features , https://www.vendoo.co/marketplaces/facebook-marketplace , https://listperfectly.com/marketplaces/ , https://nifty.ai/features , https://apps.shopify.com/shopify-marketplace-connect , https://apps.shopify.com/quicksync-for-etsy , https://www.sellbrite.com/pricing/sellbrite/ , https://www.simplylisted.com/pricing , https://help.etsy.com/hc/en-us/articles/360000343828-How-to-Use-the-Etsy-Seller-App , https://www.ebay.com/help/selling/listings/creating-managing-listings/bulk-listing-editing-tool?id=4185 (redirected to an unrelated article).

Web searches used (11, leads only): FLUF pricing; Nifty pricing; Flyp pricing; OneShop pricing; Closo pricing; best crosslisting app 2026; Reeva; inkFrog shutdown; eBay magical listing; Etsy bulk edit; (one more exhausted the budget).
