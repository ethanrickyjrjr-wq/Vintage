# Online sourcing and deal-alert tools for Holliewood and Vine (lane 06)

Date 2026-11-07. Author: research subagent (Claude, lane 06-sourcing-online).
Question: Which apps, sites and alert tools help find underpriced vintage pieces to resell online, using each site's own allowed alert features, and what do they cost?
Legend: V = vendor page read today (2026-11-07) through the session fetcher; U = unverified (snippet, roundup, memory, or the page would not load).
Method: WebSearch to find URLs, then the page text read with headless Chromium plus a curl fallback. 48 pages rendered, 26 fetches failed (section 4). The WebSearch budget ran out part-way, so some help-center URLs were guessed and several 404'd. Prices are copied as the vendor writes them. Quotes are under 25 words.
Standing facts from earlier research, re-read today: eBay's User Agreement bans "any robot, spider, scraper, data mining tools, data gathering and extraction tools, or other automated means" (V), and Meta's terms say "You may not access or collect data from our Products using automated means (without our prior permission)" (V). Facebook Marketplace has no public API (earlier research). So this lane sticks to each site's own alert features and flags every tool that scrapes.

## 0. Bottom line

- Every source that matters has a free native alert. The gap is speed, and no vendor page states a delivery time except Proxibid (weekly default, daily option), Depop (weekly push) and Botifex (20 to 5 minute refresh by tier). eBay's own page promises email "when new items matching your search are listed" with no interval; community threads (U) say once a day.
- For vintage decor near Fort Myers and Naples, the two sign-ups to make today are free: EstateSales.net (daily emails, pick sale types, radius and lead days, free iOS and Android app, a "Treasure Tracker" keyword feature) and EstateSales.org (emails within 5 to 100 miles, pick weekdays, a separate "Online Auction Items" email, categories, gsalr yard-sale digest bundled).
- Auction aggregators: Proxibid's saved-search email alerts are verified with frequency choices. LiveAuctioneers' help center confirms saved searches and "search alerts". HiBid, Invaluable, EBTH, AuctionNinja, BidSquare and CTBids show the feature or a notifications menu on the home page, but the alert details would not load today (U).
- The "deal alert" apps that cover Facebook Marketplace and OfferUp (Botifex, Swoopa, Flipify) work by scraping and proxies. Meta's terms ban automated collection and eBay's User Agreement bans scrapers. The account risk sits with Hollie, not the vendor. Only eBay-API tools (uBuyFirst, SeeSpotBid, AutomatedSearches) stand on firm ground, and the eBay Browse API plan from earlier research covers the same need at no cost.
- Misspelling finders (FatFingers, BargainChecker, TypoHound) are free, web only, affiliate funded and still live in 2026. They are a search trick for eBay, not an alert.
- Web-change monitors have free tiers big enough for a few pages: Visualping 5 pages every 60 min, PageCrawl 6 pages every 60 min, Distill 25 monitors (5 in cloud at 6-hour intervals), changedetection.io self-hosted under Apache-2.0 at no cost (the Fedora box can run it) or hosted at $8.99 / Month. Pointing them at eBay or Facebook pages runs into the same automated-access terms, so use them on estate-sale company pages and auction-house calendars.
- IFTTT Free ($0.00 / month, 1,000 credits / month, Unlimited Applets) and Zapier Free ($0 /month, 100 tasks per month, two-step Zaps) can forward alert emails or RSS into Pushover. No vendor page read today confirms an RSS feed on eBay or Craigslist, so the "RSS trick" stays U.
- Storage auctions (StorageTreasures, Lockerfox) and government surplus (GovDeals, GSA Auctions, PublicSurplus) are free to join but low fit for one-of-one decor. Skip unless a lot is literally "household goods".

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| eBay saved searches | Native eBay alert on new matching listings | Free. "We'll send you email alerts when new items matching your search are listed." | Yes, whole feature | Web, eBay app (iOS, Android) | High. First alert to set. Interval not stated. | V | https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051 |
| eBay "Newly listed" sort | Sort any search by listing time to catch fresh items | Free | Yes | Web, app | High as a manual habit | U (not on a page read today) | https://www.ebay.com/ |
| FatFingers | Generates eBay typo variants and links to results | Free. "This site contains affiliate links for which I may be compensated" | Yes | Web | Medium. Trick, not alert. eBay US supported. | V | https://www.fatfingers.com/ |
| BargainChecker | eBay misspelled search with price range, title and description | Free. "This page may contain affiliate links." | Yes | Web | Medium. Covers eBay.com. "Copyright 2026". | V | https://www.bargainchecker.co.uk/ |
| TypoHound | "TypoHound generates common misspellings of the keyword you enter." | Free, affiliate funded | Yes | Web | Medium. eBay.com supported. | V | https://www.typohound.com/ |
| Goofbid | eBay typo and sniping tools | unknown | unknown | Web | Unknown. Page would not load. | U | https://www.goofbid.com/ |
| uBuyFirst | Real-time eBay new-listing alerts via eBay API | unknown (pricing page 404). "GET 30-DAY FREE ACCESS" | 30-day trial; iOS app listed "Free" | iOS/iPad app; desktop Windows only (U) | Medium-high. eBay-approved feed. Price unknown. | V (features), U (price) | https://ubuyfirst.com/ |
| SeeSpotBid | eBay search alerts with push notifications | "Free · In-App Purchases". PRO price not shown | "Free to use (with more advanced options available with PRO subscription)" | iPhone, iPad | Medium. eBay Developers Program member. Free tier pauses alerts 6 h/day (review). | V | https://apps.apple.com/us/app/seespotbid/id1452120217 |
| AutomatedSearches.com | "Search eBay Automatically With Free Email & Text Alerts" | Free. "Create a Free Account" | Yes | Web | Medium. Frequency not stated. Affiliate funded. | V | https://automatedsearches.com/ |
| EstateSales.net | Estate sale listings, photos, daily email alerts, app | Free for shoppers. "Free E-mail notifications: get notified via E-mail about upcoming sales near you!" | Yes | Web, iOS, Android | High. Daily emails, sale types, radius, "Treasure Tracker". | V | https://www.estatesales.net/ |
| EstateSales.org | Estate sale and online-auction listings with email alerts | No price shown on sign-up form. "Local estate sales delivered to your inbox" | Yes | Web | High. Radius 5 to 100 miles, weekdays, online-auction item emails. | V | https://estatesales.org/ |
| gsalr.com | Yard, garage and estate sales on a map, email digest | Free. "Go Ad Free for $4.99" (period not stated) | Yes. "Free daily emails with a list of the newest sales" | Web, mobile app | Medium. Keyword highlight in emails. Partner of EstateSales.org. | V | https://gsalr.com/ |
| GarageSaleFinder | Yard sale map and "local yard sale alerts" | Free. "free tool to help you find garage sales and yard sales" | Yes | Web | Medium-low | V | https://garagesalefinder.com/ |
| Yard Sale Treasure Map | Yard sale map app with routing | "Free · In-App Purchases" | Yes (ads) | iPhone, iPad ("Requires iOS 17.0 or later") | Medium-low. Reviews complain about ads. | V | https://apps.apple.com/us/app/yard-sale-treasure-map/id318649229 |
| YardSales.net | Yard sale listings | unknown | unknown | Web | Unknown. DNS failed. | U | https://www.yardsales.net/ |
| AuctionZip | Live and online auction calendar for antiques and art | Free to browse | Yes | Web | Medium. No alert text found on home or help page today. | V (site), U (alerts) | https://www.auctionzip.com/ |
| HiBid | Online auction platform with "Auctions Near Me" radius search | Free to browse and bid | Yes | Web, app (U) | Medium-high. Home nav shows "Manage Notifications" and "Watch List"; saved-search alert details U. | V (site), U (alerts) | https://hibid.com/ |
| LiveAuctioneers | Art and antiques auction aggregator; saved searches and "search alerts" | Free to browse and follow | Yes | Web, iOS app | High. Help center: "search alerts you set up ( My Searches tab)". Channel (email vs push) U. | V | https://help.liveauctioneers.com/hc/en-gb/search?query=saved+search |
| Invaluable | Auction aggregator with "Saved" and "Notifications" menus, iOS and Android app | Free to browse | Yes | Web, iOS, Android | Medium-high. Keyword alert details U (help pages 404). | V (site), U (alerts) | https://www.invaluable.com/ |
| EBTH | Online estate sale auctions | Free to browse. "Sign up to follow auctions, save searches, and start bidding!" | Yes | Web | Medium. Alert channel U (support center 401). | V (site), U (alerts) | https://www.ebth.com/ |
| ShopGoodwill | Goodwill online auctions with Saved Searches | Free | Yes. "click on the 'Save Search' button at the top left hand side of the page" | Web | Medium-high for lamps, glass, art. Email alert not stated on the page. | V | https://shopgoodwill.com/help/faqdetail/how-do-i-create-a-saved-search |
| GoodwillFinds | Goodwill fixed-price store | unknown | unknown | Web | Unknown. Would not load (proxy tunnel). | U | https://www.goodwillfinds.com/ |
| Facebook Marketplace saved search | In-app alerts on saved searches | Free | Yes (U) | iOS, Android, web | High inventory, but help page would not load. No API. | U (alerts), V (terms) | https://www.facebook.com/terms.php |
| Craigslist search alerts | "Search alerts send an automated email when new postings match one of your saved searches." | Free | Yes | Web, app | Medium. Per-city site. Searches "cannot be edited". | V | https://www.craigslist.org/about/help/account/features/searches |
| OfferUp | Local marketplace; email and push toggles per notification type | Free | Yes | iOS, Android, web | Medium. No saved-search alert article found in 35 help results. | V (prefs), U (saved search) | https://help.offerup.com/hc/en-us/articles/360032336071 |
| Nextdoor For Sale & Free | Neighborhood listings | Free | Yes | iOS, Android, web | Low-medium. Help center would not load. | U | https://help.nextdoor.com/ |
| Mercari (US) | Marketplace; notifications under "Profile > Settings > Notifications" | Free | Yes | iOS, Android, web | Medium. US saved-search alert not documented on pages read. | V (notifications), U (saved search) | https://www.mercari.com/us/help_center/article/115/ |
| Poshmark | Fashion marketplace | Free | Yes | iOS, Android, web | Low (fashion only). Support site would not load. | U | https://support.poshmark.com/ |
| Depop | Fashion marketplace; saved searches with weekly push | Free. "You can save up to 10 searches" | Yes | iOS, Android | Low-medium (80s and 90s fashion only). "weekly push notification". | V | https://depophelp.zendesk.com/hc/en-gb/articles/360019648117-Saved-Searches |
| StorageTreasures | Storage unit auctions; "Auction Notifications for units near you" | "Register Now - It's Easy & Free!" Pro upgrade price not found | Yes | Web, app | Low. Whole units, not pieces. | V | https://www.storagetreasures.com/ |
| Lockerfox | Storage unit auctions with email alerts | "No monthly plan or recurring subscription"; "Low 15% ($10.00 min.) buyer's premium on units you win" | Yes | Web | Low | V | https://www.lockerfox.com/ |
| GovDeals | Government surplus; Saved Search emails new and closing items | Free | Yes | Web | Low | V (blog), site 403 | https://blog.govdeals.com/saved-search |
| PublicSurplus | Government surplus | unknown | unknown | Web | Low. DNS failed. | U | https://www.publicsurplus.com/ |
| GSA Auctions | Federal surplus; "Subscribe" link in nav | Free | Yes | Web | Low | V (site), U (alert detail) | https://gsaauctions.gov/auctions/home |
| AuctionNinja | Estate sale and online auction listings; email list | Free to browse | Yes | Web | Medium. Only an "exclusive email list" opt-in found. | V (site), U (alerts) | https://www.auctionninja.com/ |
| BidSquare | Fine art and antiques auctions | Free to browse | Yes | Web | Medium. No alert text found. | V (site), U (alerts) | https://www.bidsquare.com/ |
| Proxibid | Auction platform; "Saved Search email alerts" with frequency | Free | Yes | Web | Medium-high. Default "once a week", or "daily, once every three days, or never". | V | https://discover.proxibid.com/comparison-shopping-hard-help |
| MaxSold | Online estate auctions, active in Florida | unknown | unknown | Web | Medium. Every MaxSold page returned 403. | U | https://maxsold.com/ |
| CTBids (Caring Transitions) | Online estate sale auctions; "Real time updates and notifications" | Free to browse; Premier "$99/year" | Yes | Web, iOS app | Medium-high for decor. Premier adds WorthPoint price guide and delivery guarantee. | V | https://ctbids.com/premier-membership |
| Visualping | Web page change alerts | "Free $0/mo ... 150 [checks] 5 [pages] Every 60 min"; "Personal 1K $14/mo $120/yr ($10/mo)" | Yes | Web | Medium. Good for auction-house calendars. | V | https://visualping.io/pricing |
| Distill.io | Web page change alerts, local or cloud | "Free $0"; "Starter $15/mon"; "Professional $35/mon" | 25 monitors (5 in cloud), 6-hour cloud interval, 30 email alerts/mon | Web, browser extension, phone app | Medium. Local monitors need the PC awake. | V | https://distill.io/pricing |
| changedetection.io | Open-source change monitor; hosted option | "$8.99 / Month Easy Subscription"; "5,000 page watches included" | Self-hosted free, "Apache-2.0 license" | Docker (Fedora box), web | Medium-high if self-hosted. "Re-check times from 5~ minutes". | V | https://changedetection.io/ |
| PageCrawl.io | Web page change alerts; markets Craigslist, Poshmark, Mercari alert templates | "Free Forever $0 / month Track 6 pages"; "Standard $13.33 / month $160 billed annually" | 6 pages, 220 checks, 60 min | Web | Medium. Marketplace templates raise the ToS question. | V | https://pagecrawl.io/pricing |
| Botifex | Scrapes 8 marketplaces for deal alerts, comps, cross-posting | "Free $0/mo"; "Basic $19.99/mo"; "Pro $49.99/mo"; "Ultra $126.99/mo" | Craigslist + eBay, 2 saved searches, 20-minute refresh, dashboard alerts only | Web (PWA), browser extension | Low-medium. Scraper and proxies against Meta and eBay terms. | V | https://botifex.com/pricing |
| Swoopa | Facebook Marketplace deal alerts (more on higher tiers) | "Swoopa Go $47/mo"; committed "$28/mo"; "Swoopa Turbo $144/mo"; "Swoopa Nitro $352/mo" | 7-day trial only | App (U) | Low. Facebook-only on Go; vehicles focus; over budget. | V (price), U (platform) | https://getswoopa.com/pricing |
| Flipify | Monitors "Facebook Marketplace, eBay, OfferUp, and more" for deals | unknown (pricing page 404). "Free trial available" | Trial | App (U) | Low-medium. "Premium checks every minute". Scraper. | V (features), U (price) | https://www.flipifyapp.com/ |
| IFTTT | Automation glue (email or RSS to push) | "Free $0.00 / month 1,000 credits / month"; "Starter $2.09 / month $25.08 billed annually" | Yes, "Unlimited Applets" | Web, iOS, Android | Medium as glue to Pushover | V | https://ifttt.com/plans |
| Zapier | Automation glue | "Free forever $0 /month ... (100 tasks per month)"; "Professional Starting from $19.99 /month" | Yes, "Two-step Zaps" | Web | Low-medium. 100 tasks is thin for alerts. | V | https://zapier.com/pricing |

## 2. Notes per tool

### eBay saved searches (V)
- Page read today: "By default you'll receive email alerts to your registered email address whenever new items match your search or if there are updates to your saved search." Searches also "appear in your feed when you're signed in".
- No frequency is stated. eBay community threads surfaced by search (U) describe one email a day only when there are new matches in the past 24 hours, and periods with no emails. Treat native eBay email as slow.
- Editing a search creates a new one: "when you edit an existing search, a new saved search will be created with the filters you've selected."
- The older help URL (id=4053) now 404s; the live page is id=4051.
- Automation gotcha (V, User Agreement id=4259): no "robot, spider, scraper, data mining tools, data gathering and extraction tools, or other automated means" without eBay's permission. The sanctioned route is the eBay API (Browse API plan, researched earlier, out of scope here).

### Misspelling finders: FatFingers, BargainChecker, TypoHound (V); Goofbid (U)
- All three are free, web only, and funded by eBay Partner Network affiliate links. All show 2026 copyright or current eBay site lists, so they are alive.
- BargainChecker adds min and max price, "Include correct spelling" and "Search Title and Description" toggles, plus a Motors typo search. TypoHound lists the error types it generates: doubled, omitted, swapped and adjacent-key characters.
- These are manual searches. None sends alerts. They fit a weekly "typo sweep" for lamp, chandelier, decanter and artist names (misspelled maker names are common on vintage listings).
- Goofbid's site would not load (proxy tunnel 502). Unverified.

### eBay-API alert tools: uBuyFirst, SeeSpotBid, AutomatedSearches (V features)
- uBuyFirst (V home and App Store): "Realtime eBay Alerts for New Items", "eBay-approved direct feed", push plus "email, Telegram, WhatsApp, Discord or Slack". iOS app listed "Free"; "GET 30-DAY FREE ACCESS". Pricing page and plans page both 404 today, so the subscription price is unknown. Desktop is Windows-only per a search snippet (U). Built for high-volume arbitrage; likely over budget.
- SeeSpotBid (V App Store): "Free · In-App Purchases", "No eBay account required", "proud member of the eBay Developers Program". A 2026 review says the free tier now has "quiet hours" that pause alerts 6 hours a day; the developer replies that eBay caps their API calls. PRO price not on the page.
- AutomatedSearches.com (V): "Free Email & Text Alerts" for "New listings from saved eBay searches", "eBay auctions ending soon", "eBay item price drops". Contrasts itself with "eBay's once-a-day saved-searches emails." Alert interval not stated. Affiliate funded.
- Other eBay alert apps seen only as App Store "You Might Also Like" names (V names, no details): BayWatch, Dealerts, Madealert, Flippah.

### EstateSales.net (V)
- Home: "Free E-mail notifications", "Download the free app today!" (iOS and Android).
- FAQ (read today): "System wide, email notifications go out every day about upcoming sales." Users pick when (most "one day before a sale starts"), what sale types, and where. Companies can pick sale types because "users ... choose what sale types they want to receive emails about".
- Keyword alerts exist under the name "Treasure Tracker" (the FAQ tells sellers to use "terms that might be searched or used for Treasure Tracker"). Setup steps were not on a page read today.
- Photos: sellers are told "A sale with no photos will likely be overlooked" and can add photo captions with dimensions. Good for pre-screening lamps and art from the phone.
- Help center subdomain would not load (proxy tunnel).

### EstateSales.org (V)
- Home: "Local estate sales delivered to your inbox". The sign-up form (rendered on the 404 page) offers "Email me sales within" 5, 10, 15, 25, 50 or 100 miles, "Days to receive emails?" by weekday, "Online Auction Items Receive emails about newly added estate sale items that you can buy online", a category picker, and a gsalr.com yard-sale digest checkbox.
- No price appears anywhere on the form. Treat as free until a paywall shows.
- Caring Transitions (CTBids) and MaxSold-style online auctions appear in its national feed, so it doubles as a CTBids alert.

### Yard sale maps: gsalr.com, GarageSaleFinder (V), Yard Sale Treasure Map (V App Store), YardSales.net (U)
- gsalr: "Free daily emails with a list of the newest sales", "Add keywords to highlight sales with items you are looking for", "Over 250k subscribers". "Go Ad Free for $4.99" (one-time or monthly not stated). Mobile app mentioned. Partner sites include EstateSales.org.
- GarageSaleFinder: "Get local yard sale alerts", free map with printable directions, "4012 sales this week!" nationally.
- Yard Sale Treasure Map: iPhone and iPad, "Free · In-App Purchases", 37K ratings at 4.7, "Requires iOS 17.0 or later". One reviewer: "so many ads it's hard to tell yard sale photos from ad images". In-app prices not on the page.
- YardSales.net: DNS failed twice. Unverified.

### Auction aggregators
- Proxibid (V): "Proxibid's Saved Search email alerts inform buyers when items matching their saved search criteria become available for sale." "Email alert notifications will have a default frequency of once a week, or choose to be notified daily, once every three days, or never." Button is "Create Saved Search" above results. Filter by category and buying method. Free.
- LiveAuctioneers (V help search): articles "How do I save a search I'm interested in?", "Edit a Saved Search", "How do I remove a saved search?". Saved searches live in "Followed Searches" / "My Searches" and "On the mobile app". The "For You" page shows "new items from your saved searches ( New Items ), search alerts you set up ( My Searches tab)". Email vs push not confirmed. Article pages are "2 years ago". iOS app "LiveAuctioneers: Bid @ Auction" is in the App Store.
- HiBid (V home): nav has "Manage Notifications", "Join Our Mailing List", "Watch List", "Auctions Near Me" with 25 to 500 mile radius. /faq and /help both say "We can't find that page". Saved-search alerts unverified. A Southwest Florida HiBid search is the quickest way to see local auction houses (local lane).
- Invaluable (V home): "Saved" and "Notifications" in the signed-in nav; "Download the Invaluable app and never miss an auction from your iOS or Android device." Help and FAQ URLs 404. Keyword alert details unverified.
- EBTH (V home): "Sign up to follow auctions, save searches, and start bidding!" Support center returned 401. Channel unverified.
- AuctionNinja (V home): "Auctions near me", "Estate sales near me", and a marketing opt-in "Yes, I want to be on AuctionNinja's exclusive email list!". FAQ URL 404. No saved-search alert text found.
- BidSquare (V home): fine art and antiques; no alert text found on home, /faq or /help ("Nothing Found").
- AuctionZip (V home): antiques, art and estate auction calendar; home has no alert text and /help shows "An error has occurred while processing this page." Alert feature unverified. AuctionZip and LiveAuctioneers share an owner (U).
- CTBids (V): home promises "Real time updates and notifications" and "Bidding Starts at $1". Premier Membership: "all six benefits for only $99/year" including Delivery Guarantee ("Valued up to $192"), "WorthPoint's Price Guide" access ("Valued up to $141") and a premier support line. Help center page returned empty. CTBids iOS app exists in the App Store. Saved-search alert detail unverified.
- MaxSold (U): maxsold.com, the seller landing page and the old Zendesk help center all failed (403 or closed). Apify sells a MaxSold scraper (search snippet). Do not use scrapers; check MaxSold's own account settings when signed in.

### ShopGoodwill (V) and GoodwillFinds (U)
- ShopGoodwill: "Make sure you are signed into your ShopGoodwill.com account to perform a search." Save from "the 'Save Search' button at the top left hand side of the page". The help index has sections "Personal Shopper" and "Saved Searches", but the Personal Shopper article body did not render. Whether a saved search emails you is not stated on the pages read; the "Personal Shopper" feature name suggests a notification service (U).
- Apify advertises a ShopGoodwill scraper with Slack and email alerts (search snippet). Unofficial; skip.
- GoodwillFinds would not load (proxy tunnel 502).

### Local marketplaces
- Facebook Marketplace: facebook.com/help/marketplace returned "Page not found", so the saved-search alert steps are U. Third-party blogs (U) describe a bell-icon "Save search" and in-app alerts that can arrive hours late. Meta Terms (V): "You may not access or collect data from our Products using automated means (without our prior permission)". No public Marketplace API. Any third-party Facebook alert tool is scraping a logged-in account.
- Craigslist (V): saved searches via the "save search" link; "Search alerts send an automated email when new postings match one of your saved searches." "Saved searches cannot be edited; you must create a new one and delete the old one." Each city site is separate (fort myers, sarasota, etc.), so set one per city.
- OfferUp (V): per-topic Email and Push toggles under Account > Account Settings > Manage Notifications; "In-app notifications are mandatory and cannot be disabled." A help-center search for "saved search" returned 35 results, none describing saved-search alerts. Unverified whether OfferUp alerts on new matching listings.
- Nextdoor: both help URLs failed (SSL and 502). Unverified.
- Mercari: US help article 115 (V) covers notification toggles and SMS (sales and deliveries only). The Japan help center (V) documents "Save this search", but that is the Japanese app. US saved-search alerts unverified; the App Store listing only promises "price drops and exclusive offers from sellers".
- Depop (V): up to 10 saved searches, "weekly push notification for all your saved searches", worldwide items, cannot edit a saved search. Fashion only.
- Poshmark: support site failed (SSL and 502). Unverified.

### Storage and government auctions (low fit)
- StorageTreasures (V): "Register Now - It's Easy & Free!", app with "real-time bid notifications", "Auction Notifications for units near you". "Upgrade To Pro" exists but the price page did not render.
- Lockerfox (V): "No monthly plan or recurring subscription", "15% of the winning bid subject to a $10.00 minimum charge", "we'll send out email notifications when new storage auctions are posted near you!"
- GovDeals (V blog): Saved Search emails "whenever anything new shows up or when listings are about to close"; "Deleting Saved Searches are the only way to stop receiving communications". govdeals.com itself returned 403 today.
- GSA Auctions (V home): "Subscribe" in the nav; FAQ URL 404. PublicSurplus: DNS failed.

### Web-change monitors
- Visualping (V): table on the pricing page: "Free $0/mo Not sold annually 150 5 Every 60 min 1" (150 checks a month, 5 pages, hourly, 1 user). "Personal 1K $14/mo $120/yr ($10/mo) 1,000 10 Every 15 min". "REST API and MCP server access come with every plan, including the free one."
- Distill.io (V): Free "$0", "Monitors 25 (5 in cloud)", "Minimum Interval in cloud 6 hours", "Checks/month in cloud 1000", "Webhook & Emails Alerts 30/mon (email only)", "Phone Push Notifications 100/mon". Starter "$15/mon" (50 monitors, 10 minutes, 30,000 checks). Local monitors run in the browser extension, so the Windows PC must be on.
- changedetection.io (V): GitHub shows "Apache-2.0 license" and "docker compose up -d". Hosted plan "$8.99 / Month", "Up to 5,000 URLs", "Re-check times from 5~ minutes", "Over 85 different notification types". Self-hosting on the Fedora box costs nothing and keeps checks off Hollie's accounts.
- PageCrawl.io (V): "Free Forever $0 / month", "Pages: Up to 6", "Checks: Up to 220", "Frequency: Up to 60 min". Standard "$13.33 / month $160 billed annually", 200 pages, 15 min. It markets Craigslist, Poshmark and Mercari alert templates (blog pages, U); those point a monitor at marketplace search pages, which is automated access under those sites' terms.
- Botifex (V): also sells "Marketplace Monitor" and "DealHunter" comparisons on its pricing page (U for those vendors).

### Scraper-based deal alert apps
- Botifex (V): Free "$0/mo" covers "Craigslist + eBay", "2 saved searches / hunt profiles", "20-minute refresh cycle", "Dashboard alerts only after trial". Basic "$19.99/mo" adds "Facebook Marketplace + OfferUp", "10-minute refresh", "Email alerts and daily digest", "1GB monthly proxy data". Pro "$49.99/mo": "All eight marketplaces", "5-minute refresh, email + SMS alerts", "eBay sell-through rate & resale comps". Ultra "$126.99/mo". The pricing page itself calls the Poshmark, Mercari, Depop and Whatnot connectors "scrapers" and meters "proxy data". That is automated collection under Meta's and eBay's terms.
- Swoopa (V): Go "$47/mo" monthly or "$28/mo" on a 12-month commitment ("$336"), "Only Facebook marketplace", "Basic alert speed", "No price drop alerts". Turbo "$144/mo" monthly or "$99/mo" for 6 months; Nitro "$352/mo" or "$199/mo". "Start free for 7 days." Feature list ("AI VIN & title detection") shows a vehicle focus. Over budget and off target.
- Flipify (V home): "monitors Facebook Marketplace, eBay, OfferUp, and more around the clock", "Premium checks every minute", "Free trial available". Pricing page 404. Botifex's comparison (U) lists "$5 Basic / $10 Premium per watchlist".
- Spottable (U): landing page 404.

### Glue
- IFTTT (V): "Free $0.00 / month 1,000 credits / month All features unlocked Unlimited Applets". Starter "$2.09 / month $25.08 billed annually 5,000 credits / month Faster Applet speeds". Pro "$5.49 / month $65.88 billed annually". Pro+ "$13.99 / month $167.88 billed annually". Free Applets run slower (paid tiers sell "Faster Applet speeds").
- Zapier (V): "Free forever $0 /month", "100 tasks per month", "Two-step Zaps". Professional "Starting from $19.99 /month" for multi-step Zaps and webhooks. The FAQ asks "Does checking (or polling) for new data use tasks?" (answer not read).
- RSS trick: no eBay or Craigslist page read today mentions RSS. Treat as U until a feed URL is confirmed.

## 3. Recommendation for Hollie

Free, today, in this order:
1. EstateSales.net account: turn on free sale notifications for the Fort Myers and Naples metros, one day ahead, sale types estate and tag sale plus online auction, and install the free app. Then find the Treasure Tracker keyword feature in the account and add "lamp", "chandelier", "decanter", "depression glass", "mannequin", "turntable".
2. EstateSales.org sign-up: 50 miles, every weekday, tick "Online Auction Items", pick the Home Decor, Art, Glass and Lighting categories, and accept the gsalr yard-sale digest.
3. eBay saved searches for each category, sorted by Newly listed, with the envelope icon on. Expect roughly daily email. Add a weekly manual sweep through FatFingers or TypoHound for maker names.
4. Proxibid saved searches set to daily email. LiveAuctioneers saved searches (free account, mobile app). Sign in to HiBid, Invaluable, EBTH and CTBids and look for saved-search or notification settings; nothing on those pages could be verified today.
5. Craigslist search alerts on the fort myers and sarasota city sites (email per new post).
6. changedetection.io self-hosted on the Fedora box (podman, Apache-2.0, no cost) for estate-sale company calendars, MaxSold's Florida page and auction-house upcoming pages. Pushover is already in the dashboard plan; changedetection supports it. If nothing should be installed, Visualping Free (5 pages, hourly) or PageCrawl Free (6 pages, hourly) does the same for a handful of pages.

Pay only once it earns it:
- CTBids Premier at $99/year, only if Hollie is winning CTBids lots monthly; the WorthPoint access and shipping guarantee are the value, not alerts.
- Visualping Personal 1K ($14/mo monthly, $10/mo yearly) or Distill Starter ($15/mon) if more than five pages need watching and self-hosting is off.
- An eBay-API alert tool (uBuyFirst, SeeSpotBid PRO) only if daily eBay email proves too slow for a specific high-value hunt. Get the uBuyFirst price from the vendor first; the pricing page is down. The earlier eBay Browse API plan does this for free inside the dashboard.

Skip:
- Botifex, Swoopa, Flipify and any Facebook Marketplace or OfferUp alert app. They scrape logged-in sessions through proxies. Meta's terms ban automated collection, eBay's User Agreement bans scrapers, and a ban would hit the same account Hollie sells from. Swoopa is also over budget ($47/mo for Facebook only).
- Apify scrapers for ShopGoodwill, MaxSold, StorageTreasures, Craigslist. Same reason.
- Storage auctions and government surplus for a decor shop. Free to join, but whole units and office surplus do not match one-of-one lamps and art.
- Zapier for alert routing. 100 free tasks a month runs out fast; IFTTT Free (1,000 credits) or changedetection's own Pushover notifier is enough.

## 4. Gaps and pages that would not load

- Facebook Help Center (facebook.com/help/marketplace): "Page not found". Saved-search alert steps and delivery speed remain U.
- MaxSold: maxsold.com 403, sellerlp.maxsold.com 403, maxsold.zendesk.com "Help Center Closed". Native alert feature unknown.
- GoodwillFinds, Goofbid, help.estatesales.net: proxy tunnel failures (502).
- Nextdoor help and Poshmark support: curl SSL "unable to get local issuer certificate" and browser 502.
- PublicSurplus, YardSales.net, www.gsalr.com, www.garagesalefinder.com, www.ctbids.com: DNS failures on the www host (gsalr, garagesalefinder and ctbids loaded without www).
- govdeals.com 403 (the blog loaded); support.ebth.com 401; help.liveauctioneers.com article 652 404 (the help search page loaded instead); invaluable.com/help and /faq 404; hibid.com/faq and /help "We can't find that page"; auctionzip.com/help "An error has occurred"; auctionninja.com/faq 404; bidsquare.com/faq and /help "Nothing Found"; gsaauctions.gov/auctions/faq not found.
- Pricing pages 404: ubuyfirst.com/pricing and /plans; flipifyapp.com/pricing. Those two prices are U.
- Mercari US help article 114 returned 403; article 115 loaded via the /us/ path.
- Spottable landing page 404; Product Hunt (Auction Search) 403.
- WebSearch budget for the session ran out after 19 searches, so the remaining URLs were guessed from site conventions. Unanswered by any page read today: eBay email alert interval, eBay app push for saved searches, HiBid and Invaluable keyword alert mechanics, ShopGoodwill saved-search emails, OfferUp saved-search alerts, Mercari US saved searches, StorageTreasures Pro price, IFTTT or Zapier RSS triggers for eBay or Craigslist.

## 5. Sources (every URL fetched today, one per line; failures marked)

https://www.fatfingers.com/
https://www.estatesales.net/
https://www.estatesales.net/help/frequently-asked-questions
https://help.estatesales.net/ (FAILED: proxy tunnel)
https://estatesales.org/
https://estatesales.org/subscribe (404 page, sign-up form text rendered)
https://visualping.io/pricing
https://distill.io/pricing
https://changedetection.io/
https://github.com/dgtlmoon/changedetection.io
https://pagecrawl.io/pricing
https://ifttt.com/plans
https://zapier.com/pricing
https://botifex.com/
https://botifex.com/pricing
https://getswoopa.com/pricing
https://www.flipifyapp.com/
https://www.flipifyapp.com/pricing (FAILED: 404)
https://spottable-lp.pages.dev/ (FAILED: 404)
https://www.ebay.com/help/buying/searching-items/saving-searches?id=4053 (FAILED: redirected to error page)
https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051
https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259
https://www.facebook.com/terms.php
https://www.facebook.com/help/marketplace (FAILED: Page not found)
https://www.craigslist.org/about/help/account/features/searches
https://help.offerup.com/hc/en-us/articles/360032336071
https://help.offerup.com/hc/en-us/search?query=saved+search
https://help.nextdoor.com/s/article/Best-practices-For-Sale-Free (FAILED: SSL / 502)
https://help.nextdoor.com/s/article/How-to-use-For-Sale-and-Free (FAILED: SSL / 502)
https://www.mercari.com/help_center/article/114/ (FAILED: 403)
https://www.mercari.com/us/help_center/article/114/ (redirected to article 115, loaded)
https://gl.help.jp.mercari.com/en/guide/articles/gl_0002/
https://apps.apple.com/us/app/mercari-buying-selling-app/id896130944
https://support.poshmark.com/s/global-search/saved%20search (FAILED: SSL / 502)
https://support.poshmark.com/s/ (FAILED: SSL / 502)
https://depophelp.zendesk.com/hc/en-gb/articles/360019648117-Saved-Searches
https://shopgoodwill.com/help/faqdetail/how-do-i-create-a-saved-search
https://shopgoodwill.com/help
https://shopgoodwill.com/help/faqdetail/what-is-personal-shopper (nav only, body did not render)
https://www.goodwillfinds.com/ (FAILED: proxy tunnel)
https://www.auctionzip.com/
https://www.auctionzip.com/help (error page)
https://www.auctionzip.com/Auction-Alerts (FAILED: 404)
https://hibid.com/
https://hibid.com/faq (not found page)
https://hibid.com/help (not found page)
https://apps.apple.com/us/app/id1452120217 (resolved to SeeSpotBid, not HiBid)
https://www.liveauctioneers.com/
https://help.liveauctioneers.com/hc/en-gb
https://help.liveauctioneers.com/hc/en-gb/search?query=saved+search
https://help.liveauctioneers.com/article/652-how-do-i-view-my-saved-items-searches-and-auctioneers (FAILED: 404)
https://www.invaluable.com/
https://www.invaluable.com/help/ (FAILED: 404)
https://www.invaluable.com/faq (FAILED: 404)
https://www.ebth.com/
https://support.ebth.com/hc/en-us (FAILED: 401)
https://www.auctionninja.com/
https://www.auctionninja.com/faq (FAILED: 404)
https://www.bidsquare.com/
https://www.bidsquare.com/faq (Nothing Found)
https://www.bidsquare.com/help (Nothing Found)
https://discover.proxibid.com/comparison-shopping-hard-help
https://maxsold.com/ (FAILED: 403)
https://maxsold.zendesk.com/hc/en-us (Help Center Closed)
https://sellerlp.maxsold.com/1-resellers (FAILED: 403)
https://www.ctbids.com/ (FAILED: DNS)
https://ctbids.com/
https://ctbids.com/premier-membership
https://ctbids.com/help-center (FAILED: empty)
https://www.storagetreasures.com/
https://www.storagetreasures.com/pro (nav only)
https://www.storagetreasures.com/upgrade (nav only)
https://www.lockerfox.com/
https://www.lockerfox.com/faq/
https://blog.govdeals.com/saved-search
https://www.govdeals.com/ (FAILED: 403)
https://www.publicsurplus.com/ (FAILED: DNS)
https://publicsurplus.com/ (FAILED: DNS)
https://gsaauctions.gov/auctions/home
https://gsaauctions.gov/auctions/faq (not found)
https://www.gsalr.com/ (FAILED: DNS)
https://gsalr.com/
https://www.yardsales.net/ (FAILED: DNS)
https://www.garagesalefinder.com/ (FAILED: DNS)
https://garagesalefinder.com/
https://apps.apple.com/us/app/yard-sale-treasure-map/id318649229
https://www.bargainchecker.co.uk/
https://www.typohound.com/
https://www.goofbid.com/ (FAILED: proxy tunnel)
https://ubuyfirst.com/
https://ubuyfirst.com/docs/features-faq/
https://ubuyfirst.com/pricing/ (FAILED: 404)
https://ubuyfirst.com/plans/ (FAILED: 404)
https://apps.apple.com/us/app/ubuyfirst-alerts-for-ebay/id1525884557
https://automatedsearches.com/
https://www.producthunt.com/products/auction-search-auction-bid-assistant (FAILED: 403)
