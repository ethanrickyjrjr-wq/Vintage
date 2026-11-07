# Lane 04: Pricing comps tools for Holliewood and Vine

Date 2026-11-07. Author: research subagent (Claude Fable 5.1, lane 04-pricing-comps).
Question: Which tools show what vintage pieces actually sold for (comps) across eBay, Etsy, auction houses and design marketplaces, help set a price, and what do they cost?
Legend: V = vendor page read today (2026-11-07) with the fetch.sh headless-Chromium script; U = unverified (snippet, third party, memory, or the page would not load).
Method note: WebFetch was broken; pages were read with Bash. The shared WebSearch budget ran out after three searches, so most URLs below were typed from the seed list and vendor site structure. About 70 URL attempts, about 40 readable pages. Every price below is quoted as the vendor wrote it.

## 0. Bottom line

- The free stack covers most of Hollie's pricing: eBay Product Research (ex-Terapeak) is "free to all sellers" with "the last 3 years of eBay sales data", on the web and in the eBay mobile apps (V). Poshmark's Sold filter shows real sold prices with no account (V). Chairish and 1stDibs show asking prices for the same kind of decor (V). EBTH's archive of past estate-sale lots is searchable with a free account (V). Google Lens is free for reverse image search (V).
- WorthPoint is the one paid comps tool worth considering, because it holds old eBay sold records beyond eBay's 3-year window. Its own pricing page returned HTTP 403 twice today; the only price seen is a third-party iOS snapshot (Price Guide Monthly $26.99, March 2026), so it is U. Verify in a normal browser before paying. App Store rating is 2.1 from 117 ratings (V).
- Etsy does not expose sold prices, so eRank, EverBee, Alura, Marmalead and Sale Samurai sell estimates and keyword data, not sold comps. EverBee's own FAQ asks "How accurate are the sales estimates" (V). For one-of-one items the per-listing estimate is near useless; the keyword tools are a different lane.
- Auction archives (LiveAuctioneers, Invaluable, Heritage, Barnebys) all walled or 404'd the fetcher today. Invaluable's help index confirms a Price Archive and a free account vs paid subscriptions exist (V) but the details did not load. Treat all four as U and check by hand.
- Art price databases cost real money and only cover expensive lots: Artnet Decorative Art is "$34 /30 days" or "$350 /year", and "both databases only include items estimated at $500 and above" (V). Use only for a signed painting that already looks valuable.
- Paid appraisals run $25 (Mearto, 1 appraisal) to $28 (ValueMyStuff, 1 credit) (V). Only for a suspected high-value piece, never for routine lamps and glass.
- Skip for this lane: ZIK Analytics and Algopix (dropship and Amazon oriented), Flipwise (eBay bookkeeping and relisting, not comps; it says itself it is "not a cross-listing tool"), Vendoo (crosslister; Crosslist Gold already chosen), and Chrome sold-comp extensions with 15 to 458 users. eBay bans scraping; prefer eBay's own Research tab.
- Signed memorabilia: PSA Auction Prices Realized covers "over 5 million auction results" and the PSA Price Guide includes autograph categories, but only for PSA-certified items (V). JSA's site shows no price guide (V).

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| eBay Product Research (ex-Terapeak) | Sold prices, average sale price, sold price range, sell-through, for eBay items | "The best part: it's free to all sellers." | Full tool free with a seller account; "Sourcing insights" needs a Basic Store ("Basic $27.95" monthly, "$21.95" yearly) | Web (Seller Hub Research tab) and eBay mobile apps | High: real sold prices, 3 years, phone-friendly | V | https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853 |
| eBay sold/completed search filter | Buyer-side search filtered to sold listings | free (eBay help page for the filter not reached; search page errored) | Free | Web, iOS, Android | High, but the eBay help page confirming details would not load | U | https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853 (FAQ mentions "eBay completed listings search results") |
| eBay pricing guidance in the selling flow | eBay suggests a price while you list | free; "Our pricing guidance within the selling flow may also be helpful." | Free | Web, eBay app | Medium: tuned to commodity items, weak on one-of-one | V | https://www.ebay.com/sellercenter/ebay-for-business/great-price-badge |
| WorthPoint Price Guide (plus MARKS, Vault) | Archive of sold prices from eBay and auction houses, "nearly 2 decades" | unknown: worthpoint.com/pricing and /plans returned HTTP 403. Third-party iOS snapshot (Mar 2026): Price Guide Monthly $26.99, Annual $249.99 (U) | App is "Free · In-App Purchases"; price lookups locked behind subscription | Web, iOS, iPad | High for old eBay records; pricey; app rated 2.1/5 | U (price) / V (App Store page) | https://apps.apple.com/us/app/worthpoint/id1472512649 |
| Google Lens | Reverse image search; results include similar images and shopping matches | free | Free | Web (Chrome, Firefox, Safari, Edge), Android, iPhone | High for identification leads; shows asking prices, not sold | V | https://support.google.com/websearch/answer/1325808 |
| Poshmark Sold filter | Search with Availability: Sold shows sold price and original list price | free | Free, no login needed to view | Web, iOS, Android | Medium: good floor comps for lamps, shades, small decor | V | https://poshmark.com/search?query=stiffel%20lamp&availability=sold_out |
| Mercari sold search | Search filtered to sold items | free (search page returned HTTP 403 today) | Free | Web, iOS, Android | Medium | U | https://www.mercari.com/search/?keyword=stiffel%20lamp&status=sold_out |
| Chairish | Design marketplace; asking prices, strike-through original prices, "Hide Sold Out" filter | free to browse | Free | Web (iOS app exists per footer, not read) | High: same buyer as Hollie's decor; asking not sold | V | https://www.chairish.com/collection/stiffel |
| 1stDibs | Trade-tier design marketplace; asking prices, price filters, maker pages with price ranges | free to browse; page states Stiffel items "begin at $2,800 and can go as high as $6,500" | Free | Web | Medium: ceiling reference only; no sold filter seen | V | https://www.1stdibs.com/creators/stiffel/furniture/ |
| EBTH (Everything But The House) | Online estate-sale auctions; archive of past lots searchable | free account; "You can search for both Active and Archived Items." | Free account (credit card required at sign-up) | Web, iOS | Medium-high: realized prices for decor, art, barware | V | https://www.ebth.com/faq |
| LiveAuctioneers Price Results | Realized auction prices from many houses | reported free with account (U); pages returned 404 and empty | Free account (U) | Web, iOS, Android | High if it works; could not verify today | U | https://www.liveauctioneers.com/pages/price-results/ |
| Invaluable Price Archive | Realized auction prices | unknown; help index lists "paid Subscriptions" vs "the free account" | Free account exists (V); limits unknown | Web, iOS, Android | High if free tier shows prices | V (exists) / U (price) | https://www.invaluable.com/inv/help/faq/search-price-archive/ |
| Barnebys realized prices | Aggregated auction results | unknown; HTTP 403 twice | unknown | Web | Medium | U | https://www.barnebys.com/realized-prices |
| Heritage Auctions archive | Realized prices for HA lots | reported free with account (U); HTTP 403 twice | unknown | Web, iOS | Low-medium: mostly coins, cards, fine art | U | https://www.ha.com/c/ref/auction-archives.zx |
| Kovels Price Guide | Antiques price guide with categories incl. "Lamps & Lighting", "Glass & Bottles" | price guide cost not found; magazine "Digital Only 1 year (12 issues) for just $24.95"; Antique Trader banner: "Start your FREE 7-Day Trial Now!" | Free newsletter; price guide behind "JOIN NOW" | Web | Medium: reference prices, not live comps | V (pages) / U (price) | https://www.kovels.com/ |
| Replacements.com | China, crystal and glass pattern catalog with their asking prices | free to browse (HTTP 403 twice today) | Free | Web | Medium for depression glass and crystal; asking prices, retail-high | U | https://www.replacements.com/ |
| Collectors Weekly | Category write-ups plus live eBay listings (affiliate) | free | Free | Web | Low-medium: asking prices only; good reading on depression glass | V | https://www.collectorsweekly.com/glassware/depression-glass |
| eRank | Etsy keyword, competitor and shop tools | "Free $0/mo", "Basic $5.99/mo", "Pro $9.99/mo", "Expert $29.99/mo" | Free: "5 keyword lookups/day", "1 shop, 50 listings" | Web, Chrome extension | Low for comps (no sold prices); other lane for SEO | V | https://erank.com/pricing |
| EverBee | Etsy sales and revenue estimates per listing, keyword research | "HOBBY $0 / month"; "GROWTH $24.99 / month ... $299 per year"; "BUSINESS $69 / month Billed annually at $828" | Free: "Product Analytics: views, reviews, favorites", "Keyword Research: 10 keywords" | Web, Chrome extension, MCP | Low-medium: estimates, not sold prices | V | https://www.everbee.io/pricing |
| Marmalead | Etsy keyword tool with a "priced to win" check | "$19/mo ... paid monthly"; "$190 USD paid annually"; "$300 USD paid ONCE" lifetime | None seen | Web | Low | V | https://marmalead.com/pricing |
| Alura | Etsy research, AI listing tools | "Free $0 / month"; Basic "$95.88 billed yearly"; Growth "$179.99 billed yearly"; Professional "$359.88 billed yearly" (monthly figures not rendered) | Free: "5 daily keyword & product searches", Chrome extension, "API & MCP access Included" | Web, Chrome extension, API/MCP | Low-medium | V | https://www.alura.io/pricing |
| Sale Samurai | Etsy search volume and listing spy | "$19.99 Monthly"; "$16.65/mo Billed as $199.90 yearly"; "3-day free trial" | Trial only | Web, Chrome extension | Low | V | https://salesamurai.io/pricing/ |
| Artnet Price Database | Auction results for fine art and decorative art | Decorative Art: "$34 /30 days*", "$350 /year*"; Fine Art One-Day Pass "$32.50 /day" (5 searches); Individual Rollover "$42.50 /30 days*" (10 searches) | None | Web | Low-medium: "only include items estimated at $500 and above" | V | https://www.artnet.com/price-database/ |
| Artprice | Auction results for art; paid estimate service | Member "€0.00 Free lifetime access"; estimate report "for only $72"; subscription tiers not rendered | Free member tier (follow 10 artists, news) | Web | Low | V (partial) | https://www.artprice.com/subscription |
| AskART | Artist auction records | unknown; Cloudflare block | unknown | Web | Low-medium for signed art | U | https://www.askart.com/Subscribe.aspx |
| PSA Auction Prices Realized | Sold prices for PSA-graded cards, tickets, coins, pins | no price shown on page; search is public | Appears free | Web | Medium only for PSA-certified pieces | V | https://www.psacard.com/auctionprices |
| PSA Price Guide | Guide prices incl. "PRESIDENTIAL AUTOGRAPHS", "SPORTS AUTOGRAPHS" | free online; "Last updated: 6/24/2025" | Free | Web | Medium for signed memorabilia if PSA-certified | V | https://www.psacard.com/priceguide |
| JSA (James Spence Authentication) | Authentication; no price guide on site | n/a | n/a | Web | Low for comps | V | https://www.spenceloa.com/ |
| Mearto | Paid online appraisal by specialists | "1 Appraisal $25", "3 Appraisals $70", "5 Appraisals $90", "10 Appraisals $170" | None | Web | Low: only for a suspected high-value piece | V | https://www.mearto.com/pricing |
| ValueMyStuff | Paid online appraisal in 24/48 h | "1 credit $28", "3 credits $70", "5 credits $99"; "24H EXPRESS 2 credits" | None | Web, iOS/Android app (footer) | Low | V | https://www.valuemystuff.com/us/pricing |
| ZIK Analytics | eBay product and competitor research, dropship oriented | "$1 trial"; PRO "$19.90 1st month" then "$39.90"; PRO+ "$29.90 1st month" then "$59.90" | $1 trial | Web, Chrome extension | Low: built for "Dropshipping Product Finder" | V | https://www.zikanalytics.com/pricing |
| Algopix | Multi-channel product lookups, Amazon sales estimator | unknown; pricing page 404, /plans 502 | unknown | Web, Chrome extension (Amazon US) | Low | U | https://algopix.com/pricing |
| Flipwise | eBay analytics, relisting, repricing, tax reports | "Free Up to 24 listings (new members only)"; "$19.99 /mo 100–499 listings" | Free up to 24 listings | Web | Low for comps; it is bookkeeping, "not a cross-listing tool" | V | https://flipwise.app/#pricing |
| Vendoo | Crosslister with AI listing enhancement | "STARTER $12.49", "GROWTH $24.99", "PRO $49.99" each "Per month, billed yearly"; 14-day trial | Trial only | Web, iOS, Android | Low here: no price estimator on pricing page; Crosslist already chosen | V | https://vendoo.co/pricing |
| Nifty (reseller app) | Said to have AI pricing | unknown; vendor site not found (nifty.app is an unrelated utilities site) | unknown | unknown | Unknown | U | n/a |
| Reeva (reseller app) | Said to have AI listing and pricing | unknown; reeva.ai is an industrial-engineering firm, reeva.co returned 402, reeva.app is a salon chatbot, getreeva.com is parked | unknown | unknown | Unknown | U | n/a |
| Comp Splitter (Chrome) | Side panel for eBay active vs sold comps | free (no price on listing) | Free | Chrome extension | Low-medium: "15 users", no ratings, v1.0.4 May 2026 | V | https://chromewebstore.google.com/detail/comp-splitter-ebay-sold-a/hlodpancnemoijbjedgoihffjngopgoc |
| eBay Sold and Completed (US & UK) (Chrome) | Quick sold/completed search, US/UK switch | free (no price on listing) | Free | Chrome extension | Low-medium: "458 users", 4.8 from 4 ratings | V | https://chromewebstore.google.com/detail/ebay-sold-and-completed-u/fkmoninpgodmojdbcclmigdimdmapidn |
| ex FlipScout (Chrome) | Average, median, range and profit after fees on eBay sold pages | "Free tier gives 3 lookups/day forever"; "Pro $14.99/mo for unlimited"; "Lifetime ($89)" | 3 lookups/day | Chrome extension | Low-medium: vendor marketing page, Chrome store listing not read | V (vendor page) | https://flipscout-app.pages.dev/how-to-check-ebay-sold-prices |
| Google Shopping | Asking prices across retailers | free | Free | Web | Low: new-retail asking prices; not fetched today | U | n/a |

## 2. Notes per tool

### eBay Product Research (Terapeak)
- Help page (V): "All sellers can now take advantage of insights on what to sell, when to sell, and how to sell on eBay, directly from the Seller Hub Research tab and the mobile apps."
- Data: "Product research gives you access to the last 3 years of eBay sales data for millions of items, including: Sales trends, Average sales price, Sold price range ... Sell through rate (for searches of items sold 90 days ago or less)".
- Seller Center (V): "The best part: it's free to all sellers. Find it under the Research tab in Seller Hub."
- "Sourcing insights" is a different feature and needs "a Basic Store subscription or above". Store fees page (V): Basic is "$27.95" monthly or "$21.95" yearly. Hollie does not need it.
- Gotcha: 3-year cap. Older sales (a Stiffel lamp sold in 2019) need WorthPoint. A third-party page claims Terapeak has a 250-result cap and needs a store subscription; eBay's own page contradicts the store claim, so treat the 250 figure as U.
- Terms: it is eBay's own tool, so no scraping risk.

### eBay sold/completed filter and pricing guidance
- The sold-items search page (ebay.com/sch/... LH_Sold=1) returned eBay's generic "Something went wrong" error to the fetcher; the buyer help page on search tips did not mention sold items. The Terapeak help page FAQ "How do Product research results differ from eBay completed listings search results?" confirms the filter exists (V). Date range of the buyer-side filter: not verified (U; memory says about 90 days).
- Great Price badge page (V): "Use Product Research ... to get competitive insights and price your items accordingly. Our pricing guidance within the selling flow may also be helpful." The badge itself "is not a paid feature".

### WorthPoint
- worthpoint.com/pricing and /plans: HTTP 403 twice; help.worthpoint.com was refused by the session proxy. Prices are U.
- App Store listing (V): "Free · In-App Purchases", "117 RATINGS 2.1". Description: "Find accurate pricing trends with our Price Guide comprising nearly 2 decades of historical pricing data aggregated from the world's leading auction houses and online marketplaces." MARKS ("makers' marks, autographs, patterns, and symbols") and Vault are part of the suite. "Subscription automatically renews on selected term basis (monthly or annual)".
- Third-party snapshot (App Pricing Lab, dated 2026-03-21, via WebSearch summary, U): Price Guide Monthly $26.99, Price Guide + MARKS Monthly $37.99, Price Guide Annual $249.99, MARKS Premium Monthly $19.99.
- Complaints on the App Store page (V, user opinions): repeated forced logins and lockouts after the 2025 update; one reviewer: "if you are a reseller you really have no other options that allow you to see old eBay records". Several say the browser version is easier than the app.
- Gotcha: the free app shows items but locks prices; all value is behind the subscription. Terms of use not read today (U).

### Google Lens
- Help page (V): results "can include: AI overviews, Search results for objects in the image, Similar images, Websites with the image or a similar image." Works in "Chrome, Firefox, Safari, Edge" and on Android and iPhone. Tip on the page: "After you upload an image, type a description of your search into the 'Add to your search' box." Shopping-style price matches are not described on this page (U); prices it surfaces are asking prices.

### Poshmark Sold filter
- Search with `availability=sold_out` loaded without login (V) and showed "SOLD" items with sold price and, where discounted, the original list price. Stiffel lamps and shades in the sample ranged "$15" to "$325". Useful floor for brass lamps and shades; Poshmark buyers skew to fashion and small home.

### Mercari sold search
- Search URL with `status=sold_out` returned HTTP 403 and the help center home page had no sold-filter article (V, but no content). U.

### Chairish
- Stiffel collection page (V): asking prices with "Original price" strike-throughs (for example "$115 Original price: $165"), price buckets "Under $200" to "$800 and up", and an Availability filter "Hide Sold Out" (so sold-out items are shown by default, with their last asking price). Whether Chairish shows the final negotiated price is not stated; treat as asking.
- Fit: Chairish is the closest buyer set to Hollie's decor. Use it for ceilings and for how dealers word listings.

### 1stDibs
- Stiffel maker page (V): "on 1stDibs, these items begin at $2,800 and can go as high as $6,500, while a piece like these, on average, fetch $3,800." The same page's FAQ: Stiffel lamps "typically sell for anywhere between $100 and $500." Both are 1stDibs's own words and show the gap between trade asking and general market. No "Sold" labels appeared in the page text. Asking only.

### EBTH
- FAQ (V): "You can search for both Active and Archived Items." and "If you only want to follow an item for future bidding or just to watch the final sales price, click the Follow button". Account creation asks for a card: "WHY DO I HAVE TO INPUT CREDIT CARD INFORMATION TO SIGN UP?" The items?status=sold URL guess failed. EBTH lots are exactly Hollie's mix (lamps, art, barware, figurines), so archived hammer prices are good comps once logged in.

### LiveAuctioneers, Invaluable, Barnebys, Heritage
- LiveAuctioneers: /pages/price-results/ returned the site's 404; /price-guide/ returned an empty page (bot wall). support.liveauctioneers.com is the seller admin help site. WebSearch summary (U) said the Price Results database is free with a bidder account.
- Invaluable: help index "Search and Price Archive" (V) lists "What is the Price Archive? How does it work?" and "I saw something about paid Subscriptions. How is this different from the free account?" The answers are collapsed and the guessed URLs 404'd. So: a free account and paid subscriptions exist; limits and prices unknown.
- Barnebys: HTTP 403 on home and realized-prices. Collectors Weekly's footer shows Barnebys as a sister site of "Auctions Online USA Ltd" (V).
- Heritage: HTTP 403 on two archive paths. Heritage is strongest in coins, cards, comics and fine art, not decor.

### Kovels and Antique Trader
- kovels.com home (V): price guide categories include "Lamps & Lighting", "Glass & Bottles", "Design", "Fashion, Accessories & Textiles"; "JOIN NOW" gates it. /price-guide/ returned HTTP 405; /join, /pricing, /membership 404. The subscriptions shop category page was empty of prices.
- kovels.com/subscribe redirected to the Kovels Antique Trader magazine order page (V): "Print Only 1 year (12 issues) for just $29.95", "Digital Only ... $24.95", "Print + Digital ... $34.95", auto-renewing.
- antiquetrader.com home (V): banner "KOVELS ANTIQUE TRADER PRICE GUIDE Start your FREE 7-Day Trial Now!" The /price-guide path 404'd. Price guide subscription cost: U.
- Gotcha: Kovels prices are guide values compiled from sales, not a live sold feed.

### Replacements.com
- HTTP 403 on home and search. Known as the catalog for china, crystal and glass patterns with Replacements' own (retail-high) asking prices. U today.

### Collectors Weekly
- Depression glass page (V): "We are a part of eBay Affiliate Network", shows "eBay (492)" live listings with asking prices and watcher counts, plus pattern history (Hocking Cameo, Mayfair, Moderntone, American Sweetheart). Links to the National Depression Glass Association. Asking prices only.

### Etsy estimate tools (eRank, EverBee, Marmalead, Alura, Sale Samurai)
- Etsy hides sold prices on shop sold pages (prior research; not re-verified today, U). None of these tools shows a sold price for a specific sold listing; they estimate sales from views, reviews and favorites.
- eRank (V): Free "5 keyword lookups/day", "1 shop, 50 listings"; Basic $5.99/mo; Pro $9.99/mo; Expert $29.99/mo. Footer: "This app uses the Etsy API but is not endorsed or certified by Etsy."
- EverBee (V): Hobby $0; Growth "$24.99 / month" shown with "$299 per year"; Business "$69 / month Billed annually at $828". Product analytics page: "Real monthly sales and revenue across 206 million listings". FAQ heading: "How accurate are the sales estimates provided by EverBee?" Growth includes "MCP access"; "MCP and the API are priced per record."
- Marmalead (V): "$19/mo" monthly, "$190 USD paid annually", "$300 USD paid ONCE". Feature list includes "Make sure you are priced to win" with no detail.
- Alura (V): Free "$0 / month" with "5 daily keyword & product searches" and "API & MCP access Included" ("100 per month" API credits). Paid tiers quoted yearly only.
- Sale Samurai (V): "$19.99 Monthly" or "$16.65/mo Billed as $199.90 yearly", "3-day free trial".
- Fit: for one-of-one vintage, a competitor listing's estimated monthly sales says little about what Hollie's single piece will fetch. These belong to the SEO lane.

### Art databases (Artnet, Artprice, AskART)
- Artnet (V): Decorative Art database "$34 /30 days*" or "$350 /year*", unlimited searches. Fine Art and Design: One-Day Pass "$32.50 /day" with "5" searches; Individual Rollover "$42.50 /30 days*" with "10**" searches; Expert "$450 /year*"; Appraiser "$1,175 /year*". "Please note that both databases only include items estimated at $500 and above." Auto-renewing.
- Artprice (V, partial): Member tier "€0.00 Free lifetime access" (follow 10 artists, news). Paid tiers did not render. "Artpricing service will provide you with a complete valuation report within 72 hours, for only $72."
- AskART: Cloudflare "Sorry, you have been blocked". U.

### Signed memorabilia (PSA, JSA)
- PSA Auction Prices Realized (V): "auction results for cards, tickets, packs, coins, and pins graded by PSA"; "Access over 5 million auction results from leading platforms like eBay, Goldin, and more"; "Updated daily". No login or price shown on the page.
- PSA Price Guide (V): "486,427 Current PSA Prices Last updated: 6/24/2025"; categories include "PRESIDENTIAL AUTOGRAPHS" and "SPORTS AUTOGRAPHS". "Prices listed in the PSA Price Guide are based on PSA-certified/graded collectibles." Uncertified signed pieces are not covered.
- JSA home (V): authentication service; the only pricing-related line is marketing ("Increase the value of your signed memorabilia."). No price guide.

### Paid appraisals (Mearto, ValueMyStuff)
- Mearto (V): "1 Appraisal $25", "3 Appraisals $70", "5 Appraisals $90", "10 Appraisals $170". Its price-database URL 404'd.
- ValueMyStuff (V): "1 credit $28" down to "100 credits $1,800"; "48H STANDARD 1 credit", "24H EXPRESS 2 credits"; "Credits don't have any expiration date." Operator: VMS Grosvenor Ltd.
- Use only when a piece might be worth several hundred dollars and comps are thin (a signed painting, an unmarked chandelier that looks like Murano).

### eBay research and dropship tools (ZIK, Algopix, Flipwise)
- ZIK (V): "$1 trial, cancel anytime"; PRO "$19.90 1st month" then "$39.90"; PRO+ "$29.90 1st month" then "$59.90"; yearly "2 months free". Feature list is dropship-first ("Dropshipping Product Finder Amazon, Walmart, AliExpress & more", "Listing Integrations AutoDS, SuperDS, Hustle Got Real"). Company is in Paphos, Cyprus.
- Algopix: pricing 404 on two hosts, /plans 502. Nav (V) shows "Sales Estimator Get accurate sales data for Amazon US locale" and a Chrome extension "while you browse Amazon US". Not for vintage.
- Flipwise (V): pricing "based on the size of your store"; "Free Up to 24 listings (new members only)"; "$19.99 /mo 100–499 listings"; "7-DAY MONEY-BACK GUARANTEE". It syncs eBay sales, relists, reprices and builds a P&L. It is a bookkeeping and automation tool, not a comps tool. Could matter later for taxes; outside this lane.

### Crosslisters with AI (Vendoo, Nifty, Reeva)
- Vendoo (V): "STARTER $12.49", "GROWTH $24.99", "PRO $49.99", each "Per month, billed yearly"; "Try Vendoo Free for 14 Days". Growth adds "AI Listing Enhancement" and "300 background removals powered by PhotoRoom". No price-estimate feature appears on the pricing page. Crosslist Gold is already the chosen crosslister.
- Nifty: the reseller app's domain could not be found without search (nifty.app is an unrelated utilities site; getnifty.com failed to connect). U.
- Reeva: reeva.ai is an industrial engineering-data company; reeva.co returned HTTP 402; reeva.app is an Arabic salon chatbot; getreeva.com is parked. The reseller app, if it still exists, was not found. U.

### Chrome extensions for eBay sold comps
- Comp Splitter (V): "Compare eBay active and sold comps from a side panel without scraping listing data." "15 users", "No ratings", version 1.0.4 updated May 26, 2026, developer "Non-trader", declares no data collection.
- eBay Sold and Completed (US & UK) (V): "458 users", "4.8 (4 ratings)", version 1.3.9 updated March 11, 2026, handles "Website content". It is a shortcut to eBay's own sold search plus "live stats, and watch alerts".
- ex FlipScout (V, vendor page on pages.dev): "Free tier gives 3 lookups/day forever", "Pro $14.99/mo for unlimited", "Lifetime ($89)". Shows "average sold price, median, price range, and your real profit after eBay's 12.99% + $0.30 fee". Its claim that Seller Hub "requires an eBay Store subscription starting at $21.95/month" is wrong per eBay's own page; its Terapeak "250 cap" claim is U.
- Gotcha: eBay's user agreement bans scraping and automated data collection (prior knowledge, U today). Extensions that read sold pages in your own browser sit in a grey zone; tiny user counts mean little support. eBay's Research tab does the same job inside the rules.

## 3. Recommendation for Hollie

Free first, in this order:
1. eBay Product Research. Open Seller Hub > Research on the PC, or the Research tab in the eBay app on the iPhone. Search the maker or pattern, filter Condition to Used, read "Average sales price" and "Sold price range" over 3 years. This is the backbone. Cost: $0.
2. Poshmark Sold filter on the phone or web for lamps, shades, small decor and the 80s/90s fashion. Cost: $0, no login.
3. Chairish (leave "Hide Sold Out" off) and 1stDibs maker pages for the ceiling and for listing language. Both asking prices. Cost: $0.
4. EBTH: make the free account (card required), then search Archived Items for realized estate-sale prices on decor and barware. Cost: $0.
5. Google Lens from the iPhone camera roll on anything unmarked to get a maker name, then run that name through steps 1 to 4.
6. LiveAuctioneers and Invaluable: register free accounts by hand in a normal browser and check whether the price results show without paying. Both walled the fetcher today, so this is a 10-minute manual check, not a purchase.

Pay only once it earns it:
- WorthPoint when a piece is older than eBay's 3-year window or when eBay shows fewer than five sold comps. Expect roughly $27 a month on the iOS snapshot (U); confirm on worthpoint.com in a browser first. Buy monthly, cancel when the backlog is priced. Note the 2.1-star app; use the website.
- Artnet Decorative Art, "$34 /30 days", only in a month when a signed or attributed artwork or design piece that already looks like $500-plus needs auction comps. Otherwise skip.
- Mearto ($25) or ValueMyStuff ($28) for one piece where the comps disagree by hundreds of dollars.

Skip and why:
- ZIK Analytics, Algopix: dropship and Amazon tooling; wrong sellers.
- Flipwise: useful later for eBay bookkeeping, not for comps.
- Vendoo, Nifty, Reeva: crosslisters; Crosslist Gold is already the trial. Nifty and Reeva could not even be located today.
- eRank, EverBee, Marmalead, Alura, Sale Samurai for pricing: they estimate, they do not show sold prices. Any pick among them belongs to the SEO lane. If the dashboard later wants Etsy data by API, EverBee (Growth) and Alura (Free) both list MCP access.
- Chrome sold-comp extensions: 15 to 458 users, grey-zone with eBay's terms, duplicate what Seller Hub Research already gives.

## 4. Gaps and pages that would not load

- WebSearch's shared budget ran out after three searches, so Nifty, Reeva, Mercari help, Chairish help and category-specific guides (Stiffel, barware) were not searched; URLs were typed from the seeds.
- Walled or missing (see list below): WorthPoint pricing (403), LiveAuctioneers price results (404 and empty), Invaluable price archive details (404s), Barnebys (403), Heritage (403), AskART (Cloudflare), Replacements.com (403), Mercari sold search (403), eBay sold search results page (error), Kovels price guide subscription page (405 and 404s), Antique Trader price guide (404), Algopix pricing (404, 502), Google Play listings (all failed), EBTH sold-items URL (failed).
- Not fetched: Google Shopping, eBay user agreement text on scraping, Etsy's statement that sold prices are hidden, the Chrome Web Store listing for ex FlipScout, WorthPoint terms of use, National Depression Glass Association.
- Hammer Price (App Store) turned out to be a collector-car auction tracker; dropped as off-topic.

Unreadable or failed URLs today:
- https://www.worthpoint.com/pricing (HTTP 403)
- https://www.worthpoint.com/plans (HTTP 403)
- https://www.liveauctioneers.com/pages/price-results/ (site 404)
- https://www.liveauctioneers.com/price-guide/ (empty page, bot wall)
- https://www.invaluable.com/features/price-guide (404)
- https://www.invaluable.com/subscriptions/ (404)
- https://www.invaluable.com/priceguide/ (failed)
- https://www.invaluable.com/price-archive/ (failed)
- https://www.invaluable.com/inv/help/faq/what-is-the-price-archive-how-does-it-work/ (404, guessed slug)
- https://www.barnebys.com/realized-prices (HTTP 403)
- https://www.barnebys.com/ (HTTP 403)
- https://www.ha.com/c/ref/auction-archives.zx (HTTP 403)
- https://www.ha.com/information/auction-archives.s (HTTP 403)
- https://www.askart.com/Subscribe.aspx (Cloudflare block)
- https://www.replacements.com/search?q=pink+depression+glass (HTTP 403)
- https://www.replacements.com/ (HTTP 403)
- https://www.mercari.com/search/?keyword=stiffel%20lamp&status=sold_out (HTTP 403)
- https://www.ebay.com/sch/i.html?_nkw=stiffel+lamp&LH_Sold=1&LH_Complete=1 (eBay error page)
- https://www.ebay.com/sellercenter/tools/terapeak (404)
- https://www.ebay.com/help/selling/listings/creating-managing-listings/pricing-items?id=4154 (404)
- https://www.ebay.com/sellercenter/listings/pricing (404)
- https://www.kovels.com/price-guide/ (HTTP 405)
- https://www.kovels.com/join/ , /join-now/ , /pricing/ , /membership/ (404)
- https://www.antiquetrader.com/price-guide (404)
- https://algopix.com/pricing (404), https://www.algopix.com/pricing (404), https://algopix.com/plans (502)
- https://app.mearto.com/price-database (404)
- https://www.ebth.com/items?status=sold (failed)
- https://play.google.com/store/apps/details?id=com.worthpoint.worthpoint , ...com.worthpoint.app , ...com.liveauctioneers.android , ...com.liveauctioneers.liveauctioneers (failed)
- https://www.getnifty.com/ (tunnel failed), https://www.reeva.co/ (HTTP 402), https://getreeva.com/ (parked)

## 5. Sources (every URL fetched today, readable unless listed above)

- https://www.ebay.com/help/selling/selling-tools/terapeak-research?id=4853
- https://www.ebay.com/sellercenter/growth/ebay-research-tools
- https://www.ebay.com/sellercenter/ebay-for-business/great-price-badge
- https://www.ebay.com/help/selling/fees-credits-invoices/store-selling-fees?id=4809
- https://www.ebay.com/help/buying/search-tips/search-tips?id=4021
- https://www.ebay.com/sellercenter/listings/create-great-listings
- https://apps.apple.com/us/app/worthpoint/id1472512649
- https://support.google.com/websearch/answer/1325808
- https://poshmark.com/search?query=stiffel%20lamp&availability=sold_out
- https://www.mercari.com/us/help_center/
- https://apps.apple.com/us/app/mercari-your-marketplace/id896130944
- https://www.chairish.com/collection/stiffel
- https://www.1stdibs.com/creators/stiffel/furniture/
- https://www.ebth.com/faq
- https://support.liveauctioneers.com/hc/en-us
- https://www.invaluable.com/inv/help/faq/search-price-archive/
- https://www.kovels.com/
- https://www.kovels.com/subscribe/ (redirected to https://my.antiquetrader.com/pubs/WS/AQT/antique_trader_digital.jsp)
- https://www.kovels.com/product-category/subscriptions/
- https://www.antiquetrader.com/
- https://www.collectorsweekly.com/glassware/depression-glass
- https://erank.com/pricing (redirects to https://erank.com/plans)
- https://www.everbee.io/pricing
- https://www.everbee.io/product-analytics
- https://marmalead.com/pricing
- https://www.alura.io/pricing
- https://salesamurai.io/pricing/
- https://www.artnet.com/price-database/
- https://www.artprice.com/subscription
- https://www.artprice.com/pricing
- https://www.psacard.com/auctionprices
- https://www.psacard.com/priceguide
- https://www.spenceloa.com/
- https://www.mearto.com/pricing
- https://www.valuemystuff.com/us/pricing
- https://www.zikanalytics.com/pricing
- https://flipwise.app/#pricing
- https://vendoo.co/pricing
- https://vendoo.co/compare/vendoo-vs-nifty
- https://nifty.app/ (unrelated site)
- https://reeva.ai/ (unrelated company)
- https://reeva.app/ (unrelated company)
- https://chromewebstore.google.com/detail/comp-splitter-ebay-sold-a/hlodpancnemoijbjedgoihffjngopgoc
- https://chromewebstore.google.com/detail/ebay-sold-and-completed-u/fkmoninpgodmojdbcclmigdimdmapidn
- https://flipscout-app.pages.dev/how-to-check-ebay-sold-prices
- https://apps.apple.com/us/app/hammer-price/id1020784331 (off-topic, car auctions)
- WebSearch summaries used as leads only (U): App Pricing Lab WorthPoint IAP snapshot https://apppricinglab.com/iap/apple/1472512649 ; LiveAuctioneers price results leads (estatesales.net guide, Holy Cross libguide); Chrome extension leads.
