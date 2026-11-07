# Gaps review: online sourcing and deal-alert tools (lane 06-sourcing-online)

Date 2026-11-07. Author: research subagent (completeness critic for lane 06).
Question: Which apps, sites and alert tools that help find underpriced vintage pieces are MISSING from the lane 06 list, which listed tools are defunct or renamed, and what do the missing ones cost?
Legend: V = vendor's own page (or its App Store / Chrome Web Store listing) read today, 2026-11-07; U = unverified (snippet, competitor claim, memory, or the page would not load).
Method: the WebSearch budget for this turn was already used up when this agent started, so no web searches were run. Pages were found from vendor URLs already known, from category pages (Chrome Web Store results page, Apple App Store catalog lookups, GitHub topic page) and from the Botifex comparison pages, then read with the session's headless-Chromium fetcher. 50 URLs fetched, 12 would not load (section 4). Prices are copied as the vendor writes them. Quotes are under 25 words.
Standing fact, one line: eBay's User Agreement bans scrapers and Facebook Marketplace has no public API (FBM Alert's own Chrome listing says "Facebook Marketplace listing data is not available through a public API"), so every Facebook or OfferUp alert tool below works outside Meta's terms, and only the eBay tools that use eBay's API or Partner Network stand on firm ground.

## 0. Bottom line

- The biggest hole in the lane list is the free eBay push-alert apps. Trove (iOS and Android) is free with no subscription, promises alerts "usually within 60 seconds" and says eBay's Partner Network and Developer Program granted it permission. Dealerts and BayWatch are free-with-in-app-purchase iOS apps doing the same job. All three beat eBay's own email saved searches on speed and fit one-of-one hunting.
- A whole 2025 to 2026 crop of Facebook Marketplace alert tools is missing: Dibs (Chrome, free 3 searches every 15 minutes), Sift (Chrome, free desktop alerts, Pro $6.99 a month), DealHunter (web and PWA, 10 marketplaces, Basic $7.99 / month), Marketplace Alerts by GetWipfIt (iOS), plus FBM Alert, Marketplace Tracker, Marketplace Flipper and Deal Radar on the Chrome Web Store. All read Facebook pages without an API, so the account risk sits with Hollie.
- Two of the new Facebook tools are priced out of budget and built for dealers: Marketplace Monitor (Starter $24.99/ month for one search, up to $169.99/ month) and Pacto ($49/month to $399/month). Skip both.
- Auction aggregators: Lot-Art is missing. Searching upcoming lots is free; email Search Alerts need a membership from $7.90 monthly (2 alerts). Barnebys and Catawiki's websites both bot-walled (403), but Catawiki's App Store page confirms free "auction alerts" exist; most lots ship from Europe with a 9% buyer fee, so fit is low.
- Web-change monitors the list lacks: Wachete (FREE $0 / month, 5 pages, checks every 24 hours; $5.40 / month for 50 pages every 60 minutes, with iOS, Android and Windows apps) and Follow That Page (free, email only, 20 daily checks and 1 hourly check). Open-source: urlwatch (BSD-style licence, Python) and Huginn (MIT, Docker) run free on the Fedora box next to changedetection.io. Inoreader, RSS.app and Monitoro also have free tiers but their useful features sit behind paid plans.
- Gixen is a free eBay auction sniper (4 winning snipes a month free, Mirror $11.99 a year, Windows desktop manager). Not an alert, but it is the cheapest way to win a one-of-one auction without sitting at the screen.
- Defunct or changed: IFTTT's Craigslist service page is a 404 (so the "IFTTT RSS trick" seed is dead for Craigslist; IFTTT's eBay service is seller-side orders only). YardSales.net did not resolve in DNS twice today. EstateSales.org now has an official free iOS app (Estate Sale Finder), so its "web only" platform entry is out of date. Marketplace Monitor moved from marketplacemonitor.co.uk to marketplacemonitor.com. Flipify is alive (App Store build dated today).
- Blue Moon Estate Sales (weekly email newsletter per franchise) has nine Florida territories but none in Lee or Collier County, so it adds little for Fort Myers and Naples. Municibid has a free "Get notified when new auctions are listed!" subscription and a Furniture category; low fit for decor.

## 1. Comparison table: missing tools

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Trove - Smart Alerts for eBay | Push alerts when new eBay listings match saved searches, plus ending-soon alerts | "Free to use" ... "No fees. No subscriptions. No limitations." | Whole app: "Up to 15 saved searches" (App Store) / "Up to 20 Searches" (site); "Lightning-fast alerts (usually within 60 seconds)"; affiliate funded | iOS (Requires iOS 15.6 or later), Android (site says "android and ios") | high: free, fast, eBay Partner Network permission stated; the first eBay alert app to install | V | https://apps.apple.com/us/app/trove-smart-alerts-for-ebay/id1536471650 and https://www.troveapps.com/ |
| Dealerts: Alerts For eBay | Push alerts for new eBay listings, seller and category filters, auction-ending reminders | "Free · In‑App Purchases"; "Paid plans add more saved searches and shorter search intervals." IAP prices not shown | "Dealerts is free to download and includes a set number of saved searches." | iOS, iPad (Requires iOS 15.0 or later) | medium-high: push instead of eBay email; a review (U) says premium searches cost $4 each | V | https://apps.apple.com/us/app/dealerts-alerts-for-ebay/id1663641861 |
| BayWatch - Alerts for eBay | eBay new-item watch alerts since 2015, Apple Watch push, item-ending alerts | "Free · In‑App Purchases" (IAP prices not shown) | Free download; "Available FREE on the App Store." | iOS, iPad, Apple Watch (Requires iOS 15.0 or later) | medium-high: 414 ratings, eBay Partner Network affiliate; reviewer says alerts arrived ten minutes after listing | V | https://apps.apple.com/us/app/baywatch-alerts-for-ebay/id977021097 and https://www.progressconcepts.com/baywatch |
| Marketplace Alerts (GetWipfIt) | Push alerts for Facebook Marketplace and OfferUp searches, AI title filter, price-drop alerts | "Free · In‑App Purchases"; "Try it with a free trial."; "OfferUp alerts ... Available on Pro plans." Prices not shown | Free trial only (U how long) | iOS, iPad (Requires iOS 15.6 or later) | medium-low: covers the two local marketplaces Hollie needs, but reads Facebook without an API; released 2025 | V | https://apps.apple.com/us/app/marketplace-alerts/id6752629061 |
| Dibs — Marketplace Alerts | Chrome extension re-runs saved Facebook, Craigslist and OfferUp searches in your own browser; push, Telegram, Discord, email, webhook | "Free: 3 saved searches, checked every 15 minutes, no card. Pro ($12/month): 10 searches ... Power ($29/month): 30 searches"; site: "$9.60 a month, billed yearly" | 3 searches every 15 minutes, every alert channel | Chrome extension (Windows PC must be on), dibs.deals web | medium: cheapest multi-site alert, no password handed over; still automated reading of Meta pages; 79 users, no ratings yet | V | https://chromewebstore.google.com/detail/dibs-%E2%80%94-marketplace-alerts/doffpofjccngambiibgglnbcefhdcfpi and https://dibs.deals/ |
| Sift: Facebook Marketplace Filter, Scam Checker, Alerts & Price History | Chrome extension filters dealers and junk, price history, desktop alerts for watched searches | "Sift Pro ... $6.99 a month or $49 a year, save 42%"; "Sift Max ... $15.99 a month or $119 a year, save 38%" | "Sift is free to use." Free: "Desktop alerts for new listings", 3 AI second opinions a month | Chrome extension; phone alerts on Pro "by Telegram, ntfy or email" | medium: free filtering plus desktop alerts is a real upgrade to raw Marketplace; phone alerts cost $6.99 a month | V | https://siftmarketplace.com/pricing |
| DealHunter | Web/PWA saved searches across 10 marketplaces (Mercari, eBay, Facebook, Poshmark, Craigslist, OfferUp, Depop, Vinted, Whatnot) with push and email | "Basic ... 5 saved searches $7.99 / month"; "Standard ... 10 saved searches $14.99 / month"; "Premium ... 20 saved searches $29.99 / month"; "Or $69 / year" (Basic) | "No card required. Start with one search"; homepage shows "Free search's daily check" | web, PWA ("no native iOS/Android store app required" per Botifex) | medium-low: broadest coverage under $10 a month, but scrapes Facebook and others; free tier checks once a day | V | https://dealhunter.io/pricing and https://dealhunter.io/ |
| Marketplace Monitor | Concierge Facebook Marketplace alert app with account manager | "Starter $24.99/ month ... No. of Searches 01 ... Find time* 5 mins"; "Expert Plus+ $169.99/ month" | None: "Free 7 day trial"; App Store review: "No Free version" | iOS app (Requires iOS 15.0.0 or later), web | low: over budget for one search; built for dealers | V | https://marketplacemonitor.com/pricing and https://apps.apple.com/us/app/marketplace-monitor/id6491068401 |
| Lot-Art | Auction search engine over "+ 5000 auction houses" with email Search Alerts, Wish List bid reminders, image search | "STARTER $7.90 MONTHLY" (2 Search Alerts); "EXPLORER $16.90 MONTHLY" (9); "COLLECTOR $50.90 MONTHLY" (unlimited); "DAY PASS $25 ONE TIME"; "Save 35% YEARLY" | "searching Upcoming auctions is Free"; alerts are paid | web | medium: art, design, glassware and tableware categories, but European-heavy and alerts cost money; Hollie can search free | V | https://www.lot-art.com/memberships/PRICEDB |
| Wachete | Web-page change monitor with email and phone alerts, mobile and Windows apps | "FREE $ 0 / month"; "STARTER $ 5.40 / month billed monthly"; "STANDARD $ 10.90 / month"; "PREMIUM $ 54.90 / month" | "Monitor 5 static pages Monitor 1 dynamic pages Checks every 24 hours No limit on number of checks" | web, iOS, Android, Windows, browser extensions | medium-high: cheapest hourly cloud monitor ($5.40) for estate-sale company and auction-house pages; not for eBay or Facebook pages (terms) | V | https://www.wachete.com/ |
| Follow That Page | Free email web-page change monitor | free (no paid tier shown) | "Per user, it can do 20 daily checks and 1 hourly check."; "Follow That Page does not send SMS" | web | medium: zero cost daily watch on a few sale calendars; one page hourly | V | https://www.followthatpage.com/faq |
| Catawiki | Curated online auctions (mostly Europe) with free "auction alerts" per saved search | "Free" (app); buyer fee per review (U): "the 9% auction fee paid by the buyer" | Browsing and alerts free | iOS (Requires iOS 17.0 or later), Android (U), web (bot-walled today) | low: shipping from Europe kills resale margin on decor; good for watching comps | V (App Store) / U (site) | https://apps.apple.com/us/app/catawiki-online-auctions/id926272969 |

### 1b. Also seen (verified today, below the 12 cut or lower fit)

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Pacto: Marketplace Alerts | Facebook Marketplace push alerts "in under 60 seconds", credit-metered speeds | "BASIC $49/month 30,000 credits/month"; "PRO $159/month"; "ELITE $399/month ... Instant alerts included" | "7-day free trial" only | iOS (Requires iOS 15.1 or later) | low: far over budget; a review says alerts never arrived | V | https://www.trypacto.com/ and https://apps.apple.com/us/app/pacto-marketplace-alerts/id6736342836 |
| FBM Alert — Facebook Marketplace Notifier | Chrome desktop notifications from your saved Facebook search | "FREE PLAN: 1 saved search, checked every 20 minutes."; "PRO PLAN ($9.99/mo): unlimited saved searches, checked every 10 minutes." | 1 search every 20 minutes | Chrome extension | low-medium: 61 users, no ratings, loads facebook.com in a background window | V | https://chromewebstore.google.com/detail/fbm-alert-%E2%80%94-facebook-mark/alfoifppdlinoghnbalocklkjegdfijc |
| Marketplace Tracker | Save Facebook searches from Chrome, email alerts from marketplacetracker.ca | "Basic Free 3 active searches Daily alerts"; "Premium $15/mo Unlimited active searches Hourly alerts" | 3 searches, daily email; "30-day free trial" of Premium | Chrome extension plus web app (Canadian) | low-medium: 16 users; daily email is no faster than Facebook itself | V | https://chromewebstore.google.com/detail/marketplace-tracker/epdfaioomcjhkcahcpmegnhhjagabbkm and https://marketplacetracker.ca/ |
| Marketplace Flipper | Chrome extension auto-reloads Marketplace and flags new listings with badges and sound | "Free for 7 days, then just $5/month." | 7-day trial | Chrome extension | low: needs the tab open on the PC; 83 users, 5 ratings | V | https://chromewebstore.google.com/detail/marketplace-flipper/ppbbkiojfobnjkadhmgacckfhhionoeo |
| Deal Radar | Chrome extension watching Facebook Marketplace and European sites; Telegram on the plan | "€9 A MONTH FOR 5 WATCHES" via Ko-fi | "Free in your browser" | Chrome extension | low: 3 users, Czech and German focus | V | https://chromewebstore.google.com/detail/deal-radar/nhkighmbmdkhocpoheeipbflcaekhbph |
| Gixen | Free eBay auction sniper, bids in the last seconds | "Gixen is a FREE eBay Auction Sniper Service."; "Cost of Gixen Mirror is a bargain at $11.99 a year." | "4 winning snipes per month."; "Gixen Desktop Manager ... from your Windows desktop" free | web, Firefox plugin, Windows desktop | medium: not an alert, but wins one-of-one auctions without watching; eBay-compatible application (U) | V | https://www.gixen.com/ |
| Whatnot | Live-auction shopping app with vintage and collectibles categories; both Botifex and DealHunter source from it | "Free" (app); "Just $1 to Start Bidding" | Browsing, following sellers, in-app notifications (U for search alerts) | iOS (Requires iOS 17.0 or later), Android (U), web | low-medium: deals exist in live auctions but it is a time sink; help center would not load | V (App Store) / U (alerts) | https://apps.apple.com/us/app/whatnot-shop-sell-connect/id1488269261 |
| Municibid | Government surplus auctions with email subscription for new auctions | "Create a FREE Account" | "Get notified when new auctions are listed! Subscribe" | web | low: "Furniture" category exists but stock is office and school surplus | V | https://municibid.com/ |
| Blue Moon Estate Sales | Franchise estate-sale company with a weekly email newsletter per territory | free | "sign up for our weekly sales newsletter." | web (email) | low for SWFL: Florida territories are Boca Raton, First Coast South, Fort Lauderdale, Tampa (x2), Orlando (x2), Palm Beach, Pinellas; none in Lee or Collier | V | https://bluemoonestatesales.com/have-an-estate-sale/ |
| Inoreader | RSS reader whose Pro plan adds "Web feeds & Track changes" for pages without RSS | "Pro $7.50 /month Billed annually, or $9.99 billed monthly" | "Free forever": 150 RSS feeds; web feeds and change tracking are Pro (20) | web, iOS, Android (U) | low-medium: only worth it if Hollie already reads RSS; the Pro web-feed cap is 20 | V | https://www.inoreader.com/pricing |
| RSS.app | Turns web pages into RSS feeds with alerts | "Basic $8.32 / month ... You save $20 by paying annually"; "$16.64 / month" Developer | "Free Plan ... Only 2 native RSS Feeds ... 24 Hour Refresh Rate" | web | low: free tier is 2 feeds refreshed daily | V | https://rss.app/pricing |
| Monitoro | No-code page monitor; free local extraction in the browser, cloud plans for business | "Free $0 free of charge 5 webpages 60 min to revisit a page"; "Standard $99.99 /month billed monthly" | 5 pages, hourly, 2 items per page, alerts to Discord, Telegram, Slack, Teams | Chrome extension (local), web | low-medium: free tier is fine for 5 sale pages; paid jump is $99.99 | V | https://monitoro.co/#pricing |
| urlwatch | Open-source Python page watcher, email and Pushover-style reporters | free; COPYING: "Redistribution and use in source and binary forms, with or without modification, are permitted" (BSD-style) | Everything; 3.1k stars, 974 commits | Python CLI (Fedora box, Windows) | medium: Hollie will not run it herself; a Claude session can, alongside changedetection.io | V | https://github.com/thp/urlwatch and https://raw.githubusercontent.com/thp/urlwatch/master/COPYING |
| Huginn | Open-source agents that "Scrape websites and receive an email when they change" | free; "MIT license" | Everything; "docker run -it -p 3000:3000 ghcr.io/huginn/huginn"; 50.4k stars | Docker (Fedora box via podman), web UI | medium-low: heavier than changedetection.io for the same job | V | https://github.com/huginn/huginn |
| Estate Sale Finder (EstateSales.org app) | Official EstateSales.org iOS app; corrects the lane's "web only" platform note | "Free" | Whole app; "Requires iOS 16.4 or later." | iOS, iPad | high (amends a listed tool): install next to the EstateSales.net app | V | https://apps.apple.com/us/app/estate-sale-finder/id6657955340 |

## 2. Notes per tool

Trove. App Store: "Real-time alerts. Smarter shopping. Completely free."; "Trove is supported through eBay partner affiliate links". Vendor site: "Disclaimer: Trove is an independent tool and is not affiliated with or endorsed by eBay Inc. Permission for the application logo and title has been granted through their Partner Network and Developer Program." Reviews on the page: one says alerts came in 6 minutes not 1; one says results stopped loading after a day; one bought a camera "ten minutes after it came out". 27 ratings, 4.3. Last build 2026-03-03. Android claimed on the site, not verified on Google Play.

Dealerts. Push, not email: "eBay's own saved search notifications arrive as emails. Dealerts sends a push notification to your phone for each new match". Filters: categories, exact phrase, seller allow and block lists, international eBay sites "included in the free version". IAP: "Yes" but no prices on the page. One review (U): "they charge $4 per premiu[m search]" and a free alert "arrived over a minute late". 71 ratings, 4.7, updated 2026-11-07. The developer's own app pages on getwipfit.com returned 404; the site index names "Marketplace Alerts" and "Dealerts" and says "Not affiliated with, endorsed by, or sponsored by Meta Platforms, Inc. or eBay Inc."

BayWatch. "Find new items first on eBay before anyone else."; affiliate funded ("eBay Partner Network"). Reviewer tip on the page: run several watches with different keyword sets for the same item. Site testimonial: bought a £150 item for £10 "As the item had only been listed ten minutes when I got the alert." IAP prices not shown. 414 ratings, 4.6.

Marketplace Alerts (GetWipfIt). "Marketplace Alerts checks Facebook Marketplace and OfferUp for new listings that match your searches and sends you a push notification". AI filter "skips parts, accessories and items that do not match your search". Built-in eBay sold-comps link and fee calculator. "Marketplace Alerts is not affiliated with, endorsed by or sponsored by Meta, Facebook or OfferUp." No price text; 7 ratings. Reading Facebook pages for a user is automated collection under Meta's terms; the risk is Hollie's account.

Dibs. "Dibs re-opens each watched search in a collapsed background tab group, in your own signed-in session"; "No password to hand over, no shared account". "Every channel is on every plan, free included." Plans on the Chrome listing: Free 3 searches every 15 minutes; Pro $12/month, 10 searches, top 3 every 2 minutes; Power $29/month, 30 searches, top 5 every minute. Site: "$9.60 a month, billed yearly". 79 users, no ratings, so it is new. Same Meta-terms exposure as every tool here, and the PC must be on.

Sift. Free covers filters ("Dealers, sold items, $1 prices and listings you've already seen are gone"), price history, scam checks and desktop alerts for watched searches. Pro adds phone alerts by Telegram, ntfy or email, 50 AI second opinions a month and price-drop alerts on 10 listings. Max adds text alerts. "Prices in US dollars."; 7-day trials. Works on Kijiji too. Seen on both the Chrome Web Store results page and its own site.

DealHunter. Named by Botifex as a competitor and verified on its own site. "All plans include access to all 10 marketplaces"; "Every paid plan includes ... Email + push notifications"; "Speed compares our plans using the same marketplaces. The more marketplaces a search covers, the longer between checks." Free: "No card required. Start with one search and confirm current free-account details when you sign up." and the homepage contrasts "Paid member alerted" with "Free search's daily check", so free is once a day after the first 24 hours (Botifex says the same, checked Oct 26, 2026). Yearly: Basic $69 / year, Standard $129 / year. API access "Beta · by request" on Premium.

Marketplace Monitor. Site moved: marketplacemonitor.co.uk now lands on marketplacemonitor.com. Pricing is per search count and "Find time": Starter $24.99/ month (1 search, 5 mins), Intermediate $44.99/ month (3 searches, 3 mins), Expert $99.99/ month (5 searches, 2 mins), Expert Plus+ $169.99/ month (5 searches, Instant). Custom calculator covers Facebook Marketplace, Gumtree, OfferUp, eBay, Craigslist, Kijiji, Depop, Vinted, Shpock. App Store: 76 ratings, 3.3; a review says "Makes you sign up for minimum $30 plan just for 1 search"; developer reply: "designed primarily for dealers and small businesses".

Pacto. "Get Facebook Marketplace alerts in under 60 seconds."; credit-metered. App Store build 2026-01-12, 2 ratings; a review says "they want you to pay $30 a month" and no alerts arrived. Over budget at every tier.

Lot-Art. "LOT-ART is the leading search engine to invest in fine art and collectibles". Free: searching Upcoming lots, image search, aftersale lots, inquiries. Paid: Search Alerts (2 on Starter, 9 on Explorer, unlimited on Collector), Wish List reminders, price database. Three-month and yearly options; prices in EUR, USD or GBP. Auction highlights on the home page today were Dutch houses, so expect European lots.

Wachete. "Free to start, no credit card needed."; "Mobile apps ... on iOS, Android, and Windows."; "Browser extensions". The /pricing URL 404s; prices are on the home page. Free checks every 24 hours only. Starter $5.40 / month: 50 static pages every 60 minutes. Standard $10.90 / month: 100 pages every 10 minutes. Dynamic (JavaScript) pages are limited to 1 or 2 on every plan, so Wachete is for plain HTML sale calendars.

Follow That Page. One-person Dutch service; status is posted on Bluesky. Email only, filters for ignoring lines or blocks, no checks faster than every 10 minutes ("webmasters may choose to block our robot"). Free; no paid tier appears on the FAQ.

Catawiki. Web and help center both 403 today. App Store developer reply: "You can manage all your auction alerts here: https://www.catawiki.com/en/interests/search". Reviews on the page: "most auctions are overseas which means exorbitant shipping costs. Then there is the 9% auction fee paid by the buyer" (U, review). "Catawiki is my go to source for vintage watches" (review). 4.2K ratings, 4.7.

Gixen. "Gixen features, all absolutely free: ... 4 winning snipes per month. Free browser plugin for Mozilla Firefox. Gixen Desktop Manager ... Windows desktop." Mirror is "$11.99 a year" with unlimited snipes and two sending locations. Sniping is bidding, not scraping, and is allowed on eBay auctions; whether Gixen is an eBay-approved application was not stated on the page (U).

Whatnot. "Whatnot is the largest live shopping platform in the US, UK, and Europe"; both Botifex (8 marketplaces) and DealHunter (10) scrape it, which says resellers source there. Reviews complain about bid jumps and customer service. No saved-search alert text found; help.whatnot.com returned an empty page.

Municibid. "Municibid connects governments and schools selling no-longer-needed equipment and surplus goods with verified bidders"; "Get notified when new auctions are listed! Subscribe". Free account. Quick links include Automotive and Heavy Equipment; Furniture is a category. Low fit.

Blue Moon Estate Sales. "To learn more about Blue Moon estate sales near you, sign up for our weekly sales newsletter." Florida list on the franchise page: "Boca Raton - Sunrise - Pembroke Pines", "Florida's First Coast South", "Fort Lauderdale, FL", "Metro Tampa Central", "Metro Tampa East & North", "Orlando East", "Orlando West, FL", "Palm Beach & The Treasure Coast", "Pinellas County, FL". Grasons (grasons.com) loaded but showed no shopper alert feature, only franchise text.

Inoreader, RSS.app, Monitoro. Inoreader Free is RSS only; "Web feeds & Track changes" (follow pages without RSS, "monitor visual or textual changes like price fluctuations") is Pro, capped at 20. RSS.app Free: 2 feeds, 24-hour refresh, ads. Monitoro Free: "5 webpages 60 min to revisit a page", "Local extraction allows you to monitor pages on your computer", alerts to Discord, Telegram, Slack or Teams; Standard jumps to $99.99 /month.

urlwatch and Huginn. urlwatch: "Watch (parts of) webpages and get notified when something changes via e-mail, on your phone or via other means." Licence is a BSD-style notice (Copyright 2008-2024 Thomas Perl). Huginn: "Create agents that monitor and act on your behalf", MIT licence, one-container Docker image. Both appear on GitHub's website-monitoring topic page next to changedetection.io (35.6k stars, "MCP included").

Other Chrome Web Store sightings on the same results page, not fetched: Snipe Alerts (vehicles), PingPost (message alerts), Marketplace Description Search ("scheduled keyword alerts"), Sold Elsewhere (crosslisting sale alerts, lane 01 territory). Other App Store sightings from the catalog lookups, not fetched: Madealert, Auction Watch, BayScout, Deals Tracker, Flippah, Watchdog for eBay, Zero Bid Finder, Spottable: Marketplace Alerts, Estate Sales Near Me (Mysons Business, Jan 2026), OLA - Online Auction, VarageSale (still updated 2026-05-14), Vinted (fashion). Barnebys has no US App Store app under its name (the lookup returned Auctionet instead).

## 3. Recommendation for Hollie

Install today, all free:
1. Trove (iPhone) for eBay push alerts on maker names and categories; set up to 15 searches. Keep eBay's own saved searches running as the slow backstop.
2. Estate Sale Finder (the official EstateSales.org iOS app) next to the EstateSales.net app the lane already recommends.
3. Sift (Chrome on the Windows PC) for Facebook Marketplace filtering and desktop alerts. Accept that any tool reading Marketplace for you sits outside Meta's terms; Sift at least runs in Hollie's own browser with no password shared.
4. Follow That Page or Wachete Free for daily email watches on local estate-sale company pages and auction-house calendars (no eBay or Facebook URLs).

Pay only once it earns it:
- Wachete Starter $5.40 / month if a daily check is too slow for sale calendars.
- Sift Pro $6.99 a month (or $49 a year) if phone alerts for Marketplace prove to be where finds come from.
- Dealerts or BayWatch in-app purchases if Trove's 15 searches run out; compare prices in-app first, since neither lists them.
- Lot-Art Starter $7.90 monthly only if Hollie starts sourcing art or design lots from auction houses and wants email alerts; search is free without it.
- Gixen Mirror $11.99 a year if she wins auctions regularly.

Skip: Marketplace Monitor and Pacto (over budget and dealer-built), Deal Radar and Marketplace Flipper (tiny user bases, tab must stay open), DealHunter and Marketplace Alerts unless Hollie accepts the Meta-terms risk for breadth, Catawiki and Whatnot as sourcing channels (shipping and time), Municibid and Blue Moon for SWFL decor. Do not run Huginn; changedetection.io already covers it and urlwatch is the lighter second option on the Fedora box.

## 4. Gaps and pages that would not load

- No WebSearch was available in this turn (budget exhausted before the agent started). Candidate names came from catalog pages and competitor comparison pages, so niche tools that only appear in blog roundups may be missing. A follow-up with search could check Google Play for Trove and Dealerts Android builds and look for a Craigslist-only alert app (CPlus Classifieds is the only one the App Store catalog surfaced; not fetched).
- Barnebys: www.barnebys.com and www.barnebys.co.uk both HTTP 403 (bot wall). No US App Store app. Alert details and price unverified (U).
- Catawiki: www.catawiki.com/en/ and help.catawiki.com both HTTP 403. Verified only through the App Store page.
- Whatnot help center (help.whatnot.com): empty page. Alert mechanics unverified.
- LastMinuteAuction.com: HTTP 502 and connection reset. Possibly dead; U.
- Flipl.io: HTTP 403. Not verified; U.
- Wachete /pricing: 404; prices taken from the home page instead.
- Hexowatch /pricing: JavaScript pricing did not render (curl fallback only, no prices). U; it is a business tool anyway.
- GetWipfIt app pages (/apps/marketplace-alerts/, /apps/dealerts/): 404; the site index still lists both apps.
- Re-checks of listed tools that failed for the first agent: Goofbid (proxy tunnel 502), GoodwillFinds (proxy tunnel 502), YardSales.net (DNS: "Could not resolve host"), PublicSurplus (DNS failed on both www and bare host). Tunnel and DNS failures inside this container are not proof of closure, but YardSales.net failing DNS is the strongest hint of a dead domain among them.
- In-app purchase prices for Dealerts, BayWatch and Marketplace Alerts are not shown on their App Store pages; they need to be read inside the apps.

### Defunct, renamed or changed (evidence)

- IFTTT Craigslist service: https://ifttt.com/craigslist returns "404 error ... The requested page or file does not exist." The eBay service (https://ifttt.com/ebay) is alive but seller-side: "automate actions when you get a new order". So the "IFTTT RSS trick" seed is dead for Craigslist buying alerts.
- YardSales.net: DNS lookup failed twice today ("curl: (6) Could not resolve host: yardsales.net"). Treat as dead until a browser outside this container proves otherwise.
- EstateSales.org: the lane lists "web" only. It has an official free iOS app, Estate Sale Finder by EstateSales.org LLC, "Requires iOS 16.4 or later", updated 2026-10-26.
- Marketplace Monitor: marketplacemonitor.co.uk redirects to marketplacemonitor.com (domain move, same product).
- Flipify: alive. App Store listing "Flipify: Marketplace Alerts" by Sam Salfi, build dated 2026-11-07, 77 ratings. Botifex's compare page today repeats the earlier U claim: "Flipify is the speed-first hunting app: $5–$10 per watchlist, 1-minute Premium checks." Still U for Flipify's own pricing.
- Swoopa: alive on the App Store (556 ratings, build 2026-11-02); Botifex now describes it as "a native mobile hunter for private-party vehicles", which matches the lane's "low" fit.
- VarageSale (not on the list, seed-adjacent): still updated on the App Store (2026-05-14), so not defunct.
- PublicSurplus, Goofbid, GoodwillFinds: still unverifiable from this container (DNS or proxy tunnel), no evidence either way.

## 5. Sources (every URL fetched today, 2026-11-07)

Loaded:
- https://www.lot-art.com/
- https://www.lot-art.com/memberships/PRICEDB
- https://botifex.com/
- https://botifex.com/compare
- https://botifex.com/blog/best-marketplace-alert-tools-2026
- https://botifex.com/botifex-vs-dealhunter
- https://dealhunter.io/
- https://dealhunter.io/pricing
- https://www.marketplacemonitor.co.uk/ (redirects to https://marketplacemonitor.com/)
- https://marketplacemonitor.com/pricing
- https://apps.apple.com/us/app/marketplace-monitor/id6491068401
- https://apps.apple.com/us/app/marketplace-alerts/id6752629061
- https://getwipfit.com/apps/marketplace-alerts/ (404, site index shown)
- https://getwipfit.com/apps/dealerts/ (404, site index shown)
- https://apps.apple.com/us/app/dealerts-alerts-for-ebay/id1663641861
- https://apps.apple.com/us/app/baywatch-alerts-for-ebay/id977021097
- https://www.progressconcepts.com/baywatch
- https://apps.apple.com/us/app/trove-smart-alerts-for-ebay/id1536471650
- https://troveapps.com/ (redirects to https://www.troveapps.com/)
- https://apps.apple.com/us/app/pacto-marketplace-alerts/id6736342836
- https://trypacto.com/ (redirects to https://www.trypacto.com/)
- https://apps.apple.com/us/app/catawiki-online-auctions/id926272969
- https://apps.apple.com/us/app/whatnot-shop-sell-connect/id1488269261
- https://www.whatnot.com/
- https://apps.apple.com/us/app/estate-sale-finder/id6657955340
- https://chromewebstore.google.com/search/facebook%20marketplace%20alert
- https://chromewebstore.google.com/detail/dibs-%E2%80%94-marketplace-alerts/doffpofjccngambiibgglnbcefhdcfpi
- https://dibs.deals/
- https://chromewebstore.google.com/detail/fbm-alert-%E2%80%94-facebook-mark/alfoifppdlinoghnbalocklkjegdfijc
- https://chromewebstore.google.com/detail/marketplace-tracker/epdfaioomcjhkcahcpmegnhhjagabbkm
- https://marketplacetracker.ca/
- https://chromewebstore.google.com/detail/marketplace-flipper/ppbbkiojfobnjkadhmgacckfhhionoeo
- https://chromewebstore.google.com/detail/deal-radar/nhkighmbmdkhocpoheeipbflcaekhbph
- https://chromewebstore.google.com/detail/sift-facebook-marketplace/lonnmbinpocgfimglpcakjeehheifljo (link only, from the results page)
- https://siftmarketplace.com/
- https://siftmarketplace.com/pricing
- https://www.wachete.com/
- https://www.wachete.com/pricing (404)
- https://www.followthatpage.com/
- https://www.followthatpage.com/faq
- https://hexowatch.com/pricing (curl fallback, no prices rendered)
- https://hexowatch.com/pricing/ (curl fallback, no prices rendered)
- https://www.inoreader.com/pricing
- https://rss.app/pricing
- https://www.monitoro.co/pricing (redirects to https://monitoro.co/#pricing)
- https://github.com/thp/urlwatch
- https://raw.githubusercontent.com/thp/urlwatch/master/COPYING
- https://github.com/huginn/huginn
- https://github.com/topics/website-monitoring
- https://www.gixen.com/ (redirects to /main/index.php)
- https://ifttt.com/craigslist (404)
- https://ifttt.com/ebay
- https://municibid.com/
- https://www.bluemoonestatesales.com/ (redirects to https://bluemoonestatesales.com/)
- https://bluemoonestatesales.com/estate-sales (redirects to /blog/franchisingposts/estate-sales-101/)
- https://bluemoonestatesales.com/have-an-estate-sale/
- https://www.grasons.com/
- Apple App Store catalog lookups (itunes.apple.com/search, entity=software, country=us) for the terms: barnebys, catawiki, whatnot, cplus craigslist, marketplace alerts, ebay alerts, estate sale, auction alerts, craigslist

Would not load:
- https://www.barnebys.com/ (403)
- https://www.barnebys.co.uk/ (403)
- https://www.catawiki.com/en/ (403)
- https://help.catawiki.com/hc/en-us (403)
- https://help.whatnot.com/hc/en-us (empty page)
- https://www.lastminuteauction.com/ (502, connection reset)
- https://www.flipl.io/ (403)
- https://www.goofbid.com/ (proxy tunnel 502)
- https://www.yardsales.net/ (DNS could not resolve)
- https://www.publicsurplus.com/ and https://publicsurplus.com/ (DNS could not resolve)
- https://www.goodwillfinds.com/ (proxy tunnel 502)
