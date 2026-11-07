# Gaps review: lane 04, comps and pricing research tools

Date: 2026-11-07. Author: research subagent (completeness critic for lane 04-pricing-comps).
Question: Which tools that show what vintage pieces actually sold for (eBay, Etsy, auction houses, design marketplaces) are missing from the lane 04 list, and is anything on that list defunct, acquired or renamed?
Legend: V = vendor page read today (2026-11-07) with the fetch.sh headless-Chromium script; U = unverified (page would not load, or claim comes from a competitor or a redirect, not the vendor's own text).

Method note. WebSearch's shared budget for this turn was already used up when this agent started, so no new searches ran. Every candidate below came from known vendor URLs typed by hand. Roundup cross-checks (Shopify App Store, Chrome Web Store, Product Hunt, GitHub) could not be done; see section 5. Reddit was not read. No subagents. 63 page fetches, listed in section 6.

## 0. Bottom line

- The biggest hole in the lane list is the auction-aggregator layer that sits between eBay and the fine-art databases. Lot-Art (V) sells a Price Database of "75 million+ sale records from 5,000+ auction houses" since 2016 for $13.90 a month (Explorer) or a $9.90 one-time Day Pass, with categories for Design, Classic Furniture, Glassware and Tableware. Bidsquare (V) has a free "Past Auction Results And Sold Price" page whose houses include Sarasota Estate Auction and Coral Gables Auction, both in Florida.
- Artsy Price Database (V) is a free, no-search-limit auction results database for fine art. It covers signed art and prints only, but it is free where Artnet charges $34 for 30 days.
- For the turntable, HiFi Shark (V) is a free aggregator of used hi-fi listings from "400+ Sources" with a Sold/Expired tab, and Audiogon Bluebook (V page, price U) keeps a US transaction history by condition behind a login.
- WatchCount (V) is a free web search of eBay sold items, but its terms ban any automated or AI-assistant access, so it is a phone tool for Ricky, never a dashboard feed. The sanctioned route for the dashboard is eBay's Marketplace Insights API, whose docs sit behind a developer sign-in on a "marketplace-insights-private" path (U, gated).
- Appraisily (V) undercuts Mearto and ValueMyStuff: a signed appraisal is $59, and its Instant Screener gives a free identification with a $9 unlock for a working value.
- EtsyHunt has been renamed EHunt (ehunt.ai, V). Koalanda (V) has a $0.00 plan. Both are Etsy estimators, the same class as eRank and EverBee, and still do not show sold prices.
- Three list entries look dead or misidentified: Algopix returns HTTP 502 on its home page; reeva.ai is an industrial engineering AI company, not a reseller app; nifty.app is a page of developer utilities. Two classic eBay comps sites not on the list are also dead today: Checkaflip (HTTP 525) and Prices4Antiques (HTTP 502).
- Mavin and 130point, the two best known free eBay sold-price front ends, bot-wall headless browsers. They are U today and need a check from Ricky's own browser.

## 1. Comparison table: missing tools

Columns match the lane report. Prices are the vendor's own words with billing period. "Sold" means realized prices; "asking" means list prices.

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Lot-Art Price Database | Aggregator of 5,000+ auction houses; Price Database of 75M+ sold results since Jan 2016; image search; categories include Design, Classic Furniture, Glassware, Tableware, Collectibles | "Starter — $4.50/month" (no Price Database); "Explorer — $13.90/month ... plus Price Database access"; "Collector — $37.90/month"; "Day Pass — $9.90 one-time"; "All yearly plans include a 30% discount compared to the monthly rate" | "An account is free and gives you access to lot listings, the Wish List (limited), and basic search." Price Database needs Explorer, Collector or Day Pass | web (EN, FR, IT, DE) | high: sold prices for lamps, glass, design and art across many houses; Europe-heavy but US filter exists; a Day Pass covers a one-off check | V | https://www.lot-art.com/user-guide |
| Artsy Price Database | Free auction results for fine art, "Auction records from 300,000 artists"; artist-follow feed in the Artsy app | "Unlimited access to millions of auction results and art market data—for free." | "no search limits, no subscriptions, and no obligations" (sign-up may be required; not tested) | web, iOS, Android | medium: signed art and prints by auction-recorded artists only; nothing for lamps or glass | V | https://www.artsy.net/price-database |
| Bidsquare Past Auction Results | Past catalogs from US houses (Sarasota Estate Auction, Coral Gables Auction, DuMouchelles, Hess Fine Art); "Search For Past Items"; filters Last 30 days to Past 6 Months; categories include "Lamps, Lighting & Candlesticks" and "Mid Century Modern" | free to browse (no price shown); whether hammer prices show without login not confirmed | free | web (mobile menu has "Desktop View"; app not read) | high-medium: same regional houses Hollie competes with; sold-price visibility U | V | https://www.bidsquare.com/auctions/past |
| HiBid | Estate and consignment auction platform; "Auctions Near Me", "Auctions by State", closed-auction listing; categories "Antiques & Collectibles", "Home Goods & Decor", "Furniture", "Art" | free to browse (no price shown) | free | web | medium: Southwest Florida estate auctions for comps and sourcing; lot-level sold prices not confirmed in fetch; help center Cloudflare-blocked | V | https://hibid.com/ |
| AuctionZip | Auction directory with state pages (Florida listed) and a "Featured Prices Realized" block | free to browse (no price shown) | free | web | medium-low: prices realized exist but the full page URL was not found; useful for local sale calendars | V | https://www.auctionzip.com/ |
| WatchCount | eBay sold-item search plus most-watched live listings; filters by category, condition, listing type, "Newly Listed Within", min and max price | "unknown": Pricing link returns 404; search usable without login | free web search | web | medium for phone comps; zero for the dashboard: "Automated access is prohibited ... any automated agent, AI assistant, bot, crawler, or scraper" | V | https://www.watchcount.com/ |
| HiFi Shark | Aggregates used hi-fi listings "from 400+ Sources" (eBay, Kleinanzeigen, Subito, Finn and more); search shows "For Sale (3092)" and a "Sold/Expired" tab; saved searches with email | free (no paid tier found; /premium is 404) | free | web, "Hifishark Companion App" (vendor headline; store listing not read) | medium: turntable and any audio gear only; mixed currencies, Europe-heavy | V | https://www.hifishark.com/search?q=technics+sl-1200 |
| Audiogon Bluebook | US used hi-fi price guide: "Year of release, retail price, private party value, trade-in value and our own Agon Average"; transaction history by date and condition | "unknown": pricing page HTTP 403; "Log In to Get Started" | unknown | web | low-medium: one turntable; US market data; price not verifiable today | V (page), price U | https://www.audiogon.com/bluebook |
| eBay Marketplace Insights API | eBay's own API for sold-item data, for the planned dashboard; docs redirect to "Sign in to your eBay Developers Program account" under a marketplace-insights-private path | unknown | unknown (developer "Join" exists) | API | medium for the dashboard, low for Ricky directly; access is gated and the API License Agreement page did not render | U | https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html |
| Appraisily | Online appraisals with a signed PDF; free Instant Screener identification | "Standard $59 · Insurance $99 · Donation from $399"; "Identification is free. Unlock a working value, inspected sales and an unsigned PDF for $9." | free photo identification (Instant Screener, "Not signed or for formal use") | web | low: only for a suspected high-value piece; cheaper than Mearto ($25 and up) for a signed report | V | https://appraisily.com/ |
| EHunt (formerly EtsyHunt) | Etsy product, keyword, shop and ad research; estimates, not sold prices; "Etsy Extension" | "Free Annual: $0.00/month"; "Basic ... $7.99 /month $95.88 billed"; "Pro ... $15.99 /month $191.88 billed"; "Elite ... $29.99 /month $359.88 billed" (annual billing; monthly-toggle prices did not render) | "Product search 5 times/day", "Keyword search 5 times/day", "Connected shops 1 shops" | web, Chrome extension | low: same class as eRank and EverBee; dropshipping-oriented nav | V | https://ehunt.ai/pricing |
| Google Shopping | Asking-price comparison across retailers; a seed the first agent dropped | free | free | web (apps not read) | low-medium: asking prices for new goods; a ceiling for "new equivalent" lamps or barware | V | https://www.google.com/shopping?udm=28 |

### 1b. Also read, lower priority (not in the structured output)

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Koalanda | Etsy keyword, product and competitor research via the Etsy API | "Free $0.00 / month"; "Monthly $11.99 / month"; "Quarterly $9.99 / month Billed every 3 months as $29.97 USD"; "Yearly $5.99 / month Billed every year as $71.88 USD" | "Free access, Limited features included, Limited searches" | web | low: no sold prices | V | https://koalanda.pro/pricing |
| Christie's Auction Results | Past sale results, departments include Design, European Furniture & Works of Art, Sports Memorabilia | free | free | web | low: top of market only; useful ceiling for a signed piece | V | https://www.christies.com/en/results |
| Sotheby's Auction Results | "Auction Results SHOWING 7,954 RESULTS", filter by date, location, category | free | free | web, app ("Download the App") | low: top of market only | V | https://www.sothebys.com/en/results |
| Wright (Rago Wright) | Design auction house network: "RAGO \| WRIGHT", "WRIGHT \| TOOMEY & CO."; departments include Modern Design, Art Deco & Art Nouveau Lighting, American + European Glass; "Complimentary Evaluations of Property" | free to browse; past-auction URL guesses returned 404 | free | web | medium for design lamps and glass; sold-price page not reached today | V | https://www.wright20.com/ |
| AuctionNinja | Online estate sales and auctions, Northeast-heavy; "Local Pickup + Limited Shipping" | free to browse | free | web | low-medium: comps for estate-sale lamps and glass; sold visibility not checked | V | https://www.auctionninja.com/ |
| Goldin | "Goldin, an eBay company"; high-end collectibles and memorabilia with a Results page | free to browse | free | web | low: signed memorabilia ceiling only | V | https://goldin.co/results |
| JustAnswer Appraisals | Chat with an appraiser; recurring membership | "$65 /month per category one-time $5 join fee at signup"; "Pricing current as of November 3, 2025" | none | web | low; skip: "Monthly charges occur unless you cancel" | V | https://www.justanswer.com/help/pricing |
| Mavin | Free eBay sold-price averages (reputation; not verifiable today) | unknown | unknown | web | unknown | U (bot wall, 3 URLs) | https://mavin.io/ |
| 130point | Free eBay sold search including accepted best-offer prices (reputation; not verifiable today) | unknown | unknown | web | unknown | U (HTTP 403, 2 URLs) | https://130point.com/ |
| MaxSold | Online estate auctions with past results (reputation) | unknown | unknown | web | unknown | U (HTTP 403; help subdomain tunnel failed) | https://maxsold.com/ |

## 2. Notes per tool

Lot-Art. The nav link "Price Database" at /price-database rendered "Page Not Found" in the headless browser, and the /membership page loads its plan grid by JavaScript ("LOADING"), so the prices above come from the vendor's own 2026 user guide, section 6, which states "Prices shown are in USD billed monthly." The guide says "Status: Choose Upcoming (default), Past (sold lots with results), or Aftersale (unsold lots — Explorer and Collector plans)." Image search is "Available on all plans including Day Pass." Coverage starts January 2016, so older eBay history still needs WorthPoint. The country filter lists the United States but the house list is Europe-heavy. Quick reference gives lot-art.com/auction-sale-price-database as the working Price Database URL (not fetched).

Artsy. Vendor text: "The Artsy Price Database is for every collector—with no search limits, no subscriptions, and no obligations." Fine-art only; a Stiffel lamp or a depression-glass bowl will not be here. Good for a signed print or painting before paying Artnet.

Bidsquare. Title tag reads "Find Past Auction Results and Sold Auction Prices." The grep for "$" on the past-auctions page found only catalog blurbs, so whether hammer prices show to a logged-out visitor is unconfirmed. The /past-auctions guess returned "Nothing Found"; the working path is /auctions/past. Florida houses seen today: Sarasota Estate Auction, Coral Gables Auction LLC, Hess Fine Art.

HiBid. Closed auctions list fine ("Bidding Closed", "Prebidding Closed") but the fetch did not reach lot pages, so sold prices are unconfirmed. help.hibid.com answered with a Cloudflare "Sorry, you have been blocked" page. Default search radius UI (25 to 500 miles) makes it a local sourcing tool as much as a comps tool.

AuctionZip. Home page shows "Featured Prices Realized(View all)" with four items and prices. Two URL guesses for the full prices-realized page returned 404. Florida has a state home page.

WatchCount. Works without login and searches eBay sold items with rich filters. The 404 page carries the terms notice in full: "You may not use, or allow, any automated agent, AI assistant, bot, crawler, or scraper ... to access, search, copy, or extract data from any WatchCount.com page." This agent stopped fetching it after reading that. Treat as a human-only browser tool. Also note: "Certain content that appears on this site comes from Amazon."

HiFi Shark. Search results show source site, price and listing date, with a "Sold/Expired" tab beside "For Sale (3092)". Prices arrive in EUR, GBP, SEK, USD and others, so Ricky must convert. Listings are asking prices even under Sold/Expired (an expired listing is not a confirmed sale). Site says "Some listings contain affiliate links (e.g. eBay Partner Network)."

Audiogon Bluebook. The public page shows transaction history rows (date, condition, price) and "Recent Top Product Sales", but says "Log In to Get Started." /bluebook/pricing returned 403 and help.audiogon.com failed through the proxy. Disclaimer on page: "This data is provided as-is with no warranty." US-centric, which suits Ricky better than HiFi Shark for a US sale price.

eBay Marketplace Insights API. Both doc URLs redirected to /signin with return_to pointing at /api-docs/marketplace-insights-private/..., so the docs are behind a developer login. The public Buy APIs catalog page returned "Page Not Found" and the API License Agreement page returned no matching text in the grep. For the dashboard plan (Claude Haiku drafting listings), this is the only eBay-sanctioned way to pull sold comps; eBay's user agreement bans scraping, so the Chrome extensions on the lane list are a grey area for automation but fine for a human clicking.

Appraisily. Clear price ladder on the home page and refund promise: "If we cannot deliver a reasonably supported appraisal to our published standard, we refund your payment." Instant Screener is "Not signed or for formal use. Not for insurance, tax or court." Fit is a one-off check before pricing a suspected valuable painting or signed piece.

EHunt. etsyhunt.com/pricing redirected to ehunt.ai/pricing, so the rename is confirmed by the vendor's own redirect. The page defaulted to annual billing; the "Monthly" toggle did not render, so monthly prices are unknown. "Loved by over 2 million e-commerce sellers worldwide" is marketing, not evidence. Free tier includes "Etsy title and description generator 5 times/day" and "AI background editor Remove: 10 images/month".

Google Shopping. Loads as google.com/shopping?udm=28. Asking prices, mostly new retail. Not a comps tool, but it answers "what does a new equivalent cost," which is the ceiling a vintage lamp must undercut.

Koalanda. Footer: "This application uses the Etsy API but is not endorsed or certified by Etsy, Inc." Five connected shops on every tier including free. No sold prices.

Christie's and Sotheby's. Both results pages load without login. Sotheby's filter includes "Online Only" sales, where mid-range decor sometimes appears. Ceiling references only.

Wright. Now trades as "Rago Wright, LLC" with Toomey & Co. and other houses in one network. Departments match Hollie's stock better than any other house (lighting, glass, modern design), but neither /auctions/past nor /auctions/past-auctions exists; the /auctions page has a "PAST" tab whose content did not render in the fetch.

JustAnswer. $65 a month per category plus $5 join fee, and "Single question customers must cancel before 30 days to avoid incurring future monthly membership charges." Skip.

## 3. Defunct, renamed, acquired or misidentified (with evidence)

- Algopix (on the lane list). https://algopix.com/ returned HTTP 502 today; the first agent saw pricing 404 and plans 502. Treat as down or defunct; remove from recommendations.
- Reeva (on the lane list as "could not locate"). https://reeva.ai/pricing redirected to https://reeva.ai/, titled "Reeva | Engineering Intelligence for Industrial Enterprises." It is an industrial engineering data company, not a reseller app. https://www.reeva.co/ returned HTTP 402. The reseller "Reeva" seed, if it exists, lives at some other domain; unresolved.
- Nifty (on the lane list as "could not locate"). https://nifty.app/ is "Nifty Apps - Simple, Effective Tools": barcode generator, pastebin, hasher. Not a reseller app. Unresolved.
- ZIK Analytics (on the lane list). The ex FlipScout page claims "ZIK Analytics extension was removed from Chrome Web Store." Competitor claim, U; the Chrome Web Store page was not fetched. Worth a check before trialing ZIK's extension.
- EtsyHunt renamed EHunt. Vendor redirect etsyhunt.com/pricing to ehunt.ai/pricing; page header "Meet the new EHunt AI!" Relevant to lane 02 as well.
- Checkaflip (not on list; a well-known free eBay comps site). https://www.checkaflip.com/ returned HTTP 525 (TLS handshake failure) today. Appears dead; do not add.
- Prices4Antiques, p4A (not on list; a long-running paid antiques price database). https://www.prices4antiques.com/ returned HTTP 502 and "Connection reset by peer." Appears dead; do not add.
- Collectors.com. Now a corporate page for Collectors Holdings ("Our Brands PSA, PSA Vault, PCGS, Beckett, SGC, Card Ladder"). The older collectors.com sold-price aggregator is no longer at that URL. PSA's own Auction Prices Realized (already on the list) is the surviving tool.
- Antiques Navigator. Once a free eBay-archive price guide; today it is a WordPress marketplace ("Buy, sell and trade antiques and collectibles on the world's largest online antique store"). The "Antique Price Guides" page is a list of category links including "Depression Glass Price Guide" and "Hummel Figurines", but /price-guide/ redirects to an empty "Price Guide Details" page and the AI search page is 404. Changed beyond use until Ricky tests it in a browser.
- ShelfTrend. Former eBay analytics tool; /pricing is 404 and the home page is now a product-trend newsletter ("MANUFACTURERS, WHOLESALERS AND RETAILERS AROUND THE WORLD READ OUR NEWSLETTER"). Not a comps tool any more.
- Wright is now Rago Wright, LLC (footer "© Rago Wright, LLC 2026"; header "RAGO | WRIGHT" and "WRIGHT | TOOMEY & CO."). Rename or merger, still operating.
- Goldin is "an eBay company" (footer). Still operating.
- Terapeak to eBay Product Research: already recorded by the first agent; not re-checked.

## 4. Recommendation for Hollie

Free first, today:
1. Bookmark Bidsquare /auctions/past and HiBid on the iPhone. Both are free, both carry the Florida estate houses whose buyers overlap with Hollie's, and both show closed sales. Confirm in Safari whether hammer prices show without logging in; if not, a free account is the next step.
2. Sign up for Artsy (free) for any signed painting or print before paying Artnet.
3. Use WatchCount by hand on the phone for a second eBay sold view when Seller Hub Research is clumsy. Never wire it into the dashboard.
4. Check Mavin and 130point from Ricky's own browser; both blocked this agent. If they load, they are free eBay sold front ends and belong on the phone home screen.
5. For the turntable: HiFi Shark (free) for the spread of asking prices, Audiogon Bluebook (free login, price of any paid tier unknown) for US transaction history.

Pay only once it earns it:
- Lot-Art Day Pass at $9.90 one-time the first time a lamp, chandelier or signed piece looks worth more than about $300. Move to Explorer at $13.90 a month only if Hollie is checking auction comps weekly. This replaces most reasons to buy WorthPoint for post-2016 auction results, but not for old eBay records.
- Appraisily at $59 for a signed report, or $9 for the Instant Screener value, only for a suspected high-value piece.

Skip:
- JustAnswer ($65 a month recurring). EHunt and Koalanda (Etsy estimators, no sold prices; eRank's free tier already covers the keyword side). Algopix (down). Checkaflip and Prices4Antiques (dead). Christie's and Sotheby's results for anything under about $1,000.

For the dashboard build (Codex, later): the only eBay-sanctioned comps feed is the Marketplace Insights API, and its docs are gated. Budget a developer sign-in and an application step; do not plan on scraping WatchCount, Mavin or eBay pages.

## 5. Gaps and pages that would not load

- WebSearch budget was exhausted before this agent started, so no roundup cross-check (Shopify App Store, Chrome Web Store, Apple App Store, Product Hunt, GitHub) was possible. Tools launched in 2025 and 2026 that this agent did not already know by URL were not found. A follow-up turn with search should check: new AI "what is it worth" iPhone apps, any Mavin or 130point apps, GitHub projects around the eBay Marketplace Insights API.
- Mavin: https://mavin.io/, /about, /faq all bot-walled (about 216 chars of text).
- 130point: https://130point.com/ and /sales/ returned HTTP 403.
- MaxSold: HTTP 403; help.maxsold.com failed through the proxy tunnel.
- Audiogon: /bluebook/pricing HTTP 403; help.audiogon.com proxy tunnel failed.
- Lot-Art: /price-database showed "Page Not Found"; /membership plan grid is JavaScript-only. Prices taken from the vendor user guide instead.
- Bidsquare: /past-auctions is "Nothing Found" (correct path is /auctions/past); lot-level price visibility not confirmed.
- HiBid: /help 404; help.hibid.com Cloudflare block; lot-level sold prices not confirmed.
- Wright: /auctions/past and /auctions/past-auctions 404.
- AuctionZip: /prices-realized and /Prices-Realized/ 404.
- eBay: Marketplace Insights docs redirect to sign-in; Buy APIs catalog "Page Not Found"; API License Agreement grep returned nothing.
- EHunt: monthly-billing prices did not render (annual shown).
- HiFi Shark: /premium 404; companion app store listing not read.
- WatchCount: /pricing 404; further fetching stopped on reading its automated-access ban.
- Reeva and Nifty: the reseller apps named in the seeds were not found at reeva.ai, reeva.co or nifty.app.

## 6. Sources (every URL fetched today, in order)

https://mavin.io/  (FETCH FAILED, bot wall)
https://130point.com/  (FETCH FAILED, HTTP 403)
https://www.antiquesnavigator.com/  (200)
https://www.lot-art.com/price-database  (200, body "Page Not Found")
https://www.artsy.net/price-database  (200)
https://www.hifishark.com/  (200)
https://mavin.io/about  (FETCH FAILED, bot wall)
https://mavin.io/faq  (FETCH FAILED, bot wall)
https://130point.com/sales/  (FETCH FAILED, HTTP 403)
https://www.antiquesnavigator.com/price-guide/  (redirected to /price-guide-details/, 200, empty)
https://www.lot-art.com/membership  (200 via curl, plan grid not rendered)
https://www.hifishark.com/faq  (200)
https://www.audiogon.com/bluebook  (200)
https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html  (redirect to developer sign-in)
https://appraisily.com/  (200)
https://etsyhunt.com/pricing  (redirected to https://ehunt.ai/pricing, 200)
https://www.bidsquare.com/  (200)
https://hibid.com/  (200)
https://www.wright20.com/  (200)
https://koalanda.pro/pricing  (200)
https://www.checkaflip.com/  (FETCH FAILED, HTTP 525)
https://www.prices4antiques.com/  (FETCH FAILED, HTTP 502, connection reset)
https://reeva.ai/pricing  (redirected to https://reeva.ai/, 200, industrial AI company)
https://nifty.app/  (200, developer utilities)
https://algopix.com/  (FETCH FAILED, HTTP 502)
https://flipscout-app.pages.dev/  (200)
https://www.lot-art.com/user-guide  (200)
https://www.hifishark.com/premium  (404)
https://www.audiogon.com/bluebook/pricing  (FETCH FAILED, HTTP 403)
https://help.audiogon.com/  (FETCH FAILED, proxy tunnel)
https://developer.ebay.com/develop/apis/restful-apis/buy-apis  (Page Not Found)
https://www.bidsquare.com/past-auctions  (200, "Nothing Found")
https://hibid.com/help  (404)
https://www.wright20.com/auctions/past  (404)
https://shopping.google.com/  (redirected to https://www.google.com/shopping?udm=28, 200)
https://www.collectors.com/  (200, corporate page)
https://maxsold.com/  (FETCH FAILED, HTTP 403)
https://www.auctionninja.com/  (200)
https://www.christies.com/en/results  (200 via curl)
https://www.sothebys.com/en/results  (200)
https://www.auctionzip.com/  (200)
https://www.justanswer.com/appraisals/  (200)
https://www.watchcount.com/  (200)
https://www.shelftrend.com/pricing  (404)
https://goldin.co/  (200)
https://www.reeva.co/  (FETCH FAILED, HTTP 402)
https://www.antiquesnavigator.com/ai-search/  (404)
https://www.watchcount.com/pricing  (404, carries automated-access ban)
https://www.hifishark.com/search?q=technics+sl-1200  (200)
https://www.bidsquare.com/auctions/past  (200)
https://help.hibid.com/  (Cloudflare block)
https://hibid.com/auctions?status=closed  (200)
https://www.wright20.com/auctions/past-auctions  (404)
https://www.auctionzip.com/prices-realized  (404)
https://www.justanswer.com/help/pricing  (200)
https://www.shelftrend.com/  (200)
https://goldin.co/results  (200)
https://help.maxsold.com/  (FETCH FAILED, proxy tunnel)
https://www.antiquesnavigator.com/antique-price-guides/  (200)
https://developer.ebay.com/join/api-license-agreement  (fetched; grep for scraping and fee terms returned nothing)
https://www.wright20.com/auctions  (200, "PAST" tab present, content not rendered)
https://www.auctionzip.com/Prices-Realized/  (404)
https://developer.ebay.com/api-docs/buy/marketplace-insights/static/overview.html  (redirect to developer sign-in)
