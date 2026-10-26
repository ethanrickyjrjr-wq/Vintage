# Sourcing / buy alerts for Hollywood and Vine: what actually works

Date: 2026-10-26. Author: research subagent (read-only; nothing built, nothing outside this file edited).
Question: alert Ricky's phone, near real time, when a listing fits a description he wrote AND a price band he set. eBay first, then other sites.

**Legend.** VERIFIED (V) = I read the cited page or ran the cited query today (2026-10-26). UNVERIFIED (U) = vendor or blog claim, search-result snippet, inference, or a page I could not read. Raw pages are saved as `research/dashboard/raw/sourcing-*` (index in the Appendix).

---

## 0. Bottom line (read this first)

1. **eBay is the one site with a clean, ToS-safe, near-real-time path: the Browse API.** Polling it is cheap and fits the free 5,000 calls/day if watches are tiered (math in 1.4). V.
2. **The unresolved risk is access, not engineering.** eBay's docs say Buy API production use is "intended for eBay partners only", via an EPN application with "no guarantee" of approval. Four small 2026 GitHub projects say a plain production keyset (App ID + Cert ID) is enough. Per your rule 4: **docs verified, repo behavior needs review.** There is no eBay keyset in any of your key stores today (names-only check), so I could not run the one-call test. That test is Step 0 of Phase 1.
3. **Scraping eBay HTML is a ToS violation.** The User Agreement bans "robot, spider, scraper ... or other automated means (including ... LLM-driven bots ...)" without eBay's express permission. Alerts only; a human does the buying. V.
4. **Every other site is worse.** Of the 19 other sources you listed: only Etsy has an official buyer-side search API; 12 explicitly ban automated collection in the text I read (11 site ToS plus Meta's Automated Data Collection Terms); 6 I could not confirm; GoodwillFinds no longer exists (closed April 2025). The ToS-clean Phase 2 path is each site's own saved-search email, ingested and forwarded to the phone.
5. **Matching is cheap.** eBay's server-side filters plus deterministic rules do most of the work. A Claude Haiku 5.5 pass on survivors costs about **$0.08 per 1,000 listings with thinking disabled and about $0.31 with default adaptive thinking** (math in 3.2). Image models are optional and CPU-feasible on the Fedora box for a shortlist.

### Discrepancies (rule 4: "X verified, Y needs review")

| Topic | Verified | Needs review |
|---|---|---|
| Browse API production access | Docs: partner-only, EPN application, no guarantee ([buy-requirements](https://developer.ebay.com/api-docs/buy/static/buy-requirements.html)) | Repos say a plain keyset works ([go-ebay-tracker](https://github.com/firozt/go-ebay-tracker), [price-bot](https://github.com/mrballistic/price-bot), [FlipWatch](https://github.com/Crepe950/flipwatch), [BayRadar](https://github.com/ChrisKariofyllis/BayRadar)); I did not run any of them |
| Browse `category_ids` | Doc shows `category_ids=267,29792` as an example | Same entry says "Currently, you can pass in only one category ID per request" ([search method](https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search)); error 12030 implies a multi-category cap exists. Test it in Step 0. |
| `buyingOptions` + `sort=newlyListed` | Error 12034 exists: "The 'buyingOptions' filter value {filterValue} is not supported for the sort by {sortOption}" ([search method](https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search)) | The `sort` entry lists `price`, `distance`, `newlyListed`, `endingSoonest` with no stated restriction, so I do not know whether AUCTION is accepted with `newlyListed`. **Untested; first item in the Step 0 test list.** Fallback and budget impact in 1.4. |
| Craigslist RSS | HN, Oct 2020: search feeds return 410 ([thread](https://news.ycombinator.com/item?id=24840310)); my 2026 fetch got 403 and "Your request has been blocked" | Botifex (vendor, Jul 2026) says RSS exists ([post](https://botifex.com/blog/craigslist-new-listing-notifications)). The same post says Craigslist has "zero native alerts", which Craigslist's own help page contradicts ([alerts help](https://www.craigslist.org/about/help/account/features/alerts)), so I trust the vendor post less. |
| Poshmark saved-search alerts | Feature exists | "red dot only, no push" is a vendor claim ([Botifex](https://botifex.com/blog/poshmark-mercari-new-listing-notifications)) |
| eBay saved-search latency | Email on by default ([eBay help](https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051)) | eBay publishes no delivery-time guarantee ([CardboardSniper summary](https://cardboardsniper.com/blog/ebay-saved-search-alerts-not-working)); real latency unmeasured |

---

## 1. eBay

### 1.1 Browse API search surface (V: [search method](https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search), [filter reference](https://developer.ebay.com/api-docs/buy/static/ref-buy-browse-filters.html))

`GET https://api.ebay.com/buy/browse/v1/item_summary/search`

| Need | Parameter | Syntax and limits, as documented |
|---|---|---|
| Keywords | `q` | Space = AND. `(iphone, ipad)` = OR (parentheses plus commas). Max 100 chars (longer is truncated). No `*` wildcard. |
| Category | `category_ids`; filter `excludeCategoryIds` | Doc says one category per request despite a comma-list example (see Discrepancies). A request needs at least one of `q`, `category_ids`, `epid`, `gtin` (error 12001). |
| Price band | `filter=price:[10..60],priceCurrency:USD` | `price` must be paired with `priceCurrency` (error 12012). |
| Condition | `filter=conditions:{USED}` or `conditionIds:{3000\|5000}` | Pipe-delimited inside braces. Condition values vary by category. |
| **Auctions vs Buy It Now** | `filter=buyingOptions:{AUCTION\|FIXED_PRICE}` (valid values: `FIXED_PRICE`, `AUCTION`, `BEST_OFFER`, `CLASSIFIED_AD`) | **By default only listings with `FIXED_PRICE` are returned. Auctions are silently excluded unless you ask for them.** The filter "is defined at the leaf category level and should be used with a leaf category ID"; with a top-level category it "won't work". Behavior with a keyword-only search is not documented (U). A fixed-price item that receives a bid stops matching `FIXED_PRICE`. Error 12034 says some `buyingOptions` values are "not supported for the sort by {sortOption}" but the `sort` entry never says which (untested; see Discrepancies). |
| Extra fields per item | `fieldgroups=EXTENDED` | Adds `shortDescription` and `itemLocation.city` to each summary with no extra call (default group is `MATCHING_ITEMS`). Item aspects are not in search summaries; they need `getItem`. |
| New listings only | `sort=newlyListed` (sorts on `itemOriginDate`) plus `filter=itemStartDate:[ISO-8601]` | Start-only form: `itemStartDate:[2026-10-26T14:00:00.000Z]`. Range form: `itemStartDate:[a..b]`. Doc quirk: the `itemStartDate` row's examples are mislabeled `itemEndDate`; the filter name is `itemStartDate`. |
| Auctions ending soon | `sort=endingSoonest` plus `filter=itemEndDate:[from..to]` | Same date format; leading `..` means "ending before". |
| Location | `itemLocationCountry:US`; `deliveryCountry:US` (+ `deliveryPostalCode`); local pickup needs all of `pickupCountry`, `pickupPostalCode`, `pickupRadius`, `pickupRadiusUnit` (error 12010) | The Buy API requirements list `deliveryCountry` as **required** for domestic browse/search ([buy-requirements](https://developer.ebay.com/api-docs/buy/static/buy-requirements.html)), so always send `deliveryCountry:US`. |
| Page size | `limit` | 1 to 200 (error 12006). |
| Pagination | `offset` | 0 or a multiple of `limit`; **hard cap 10,000 items per result set** (error 12029 when offset >= 10,000). |
| Other | `sellers`, `excludeSellers`, `searchInDescription`, `maxDeliveryCost`, `returnsAccepted`, `aspect_filter` (needs a category) | Filter reference. |
| Marketplace | header `X-EBAY-C-MARKETPLACE-ID` | Required outside the US; US is the default. |

Response summary fields relevant to alerts: `itemId` (form `v1|123456789|0`), `legacyItemId`, `title`, `price`, `currentBidPrice`, `bidCount`, `buyingOptions`, `condition`, `image`, `thumbnailImages`, `itemWebUrl`, `itemAffiliateWebUrl`, `itemCreationDate`, `itemOriginDate`, `itemEndDate`, `seller{username, feedbackScore, ...}` (search-method page, response container).

Example, shape only:

```
GET /buy/browse/v1/item_summary/search
  ?q=stiffel lamp
  &category_ids=<leaf category id>
  &filter=price:[10..60],priceCurrency:USD,buyingOptions:{AUCTION|FIXED_PRICE},
          conditions:{USED},deliveryCountry:US,itemStartDate:[2026-10-26T14:00:00.000Z]
  &sort=newlyListed&limit=200&fieldgroups=EXTENDED
Authorization: Bearer <application token>
```

Also exists: `POST /item_summary/search_by_image` (listed in the [Browse overview](https://developer.ebay.com/api-docs/buy/browse/overview.html), V). Its limits and quality I could not read (U). It could replace a self-hosted image model for "looks like this photo" watches. The bulk `getItems` method is reported as Limited Release (partners only, scope `buy.item.bulk`) in the sibling file `research/dashboard/01-ebay-platform.md`; I did not re-read it (U), so this plan does not depend on it.

### 1.2 Does an app (client-credentials) token suffice? Yes (V)

- "All methods in the Browse API require an Application access token ... obtained using the client credentials grant flow" ([Browse overview](https://developer.ebay.com/api-docs/buy/browse/overview.html)).
- Search scope: `https://api.ebay.com/oauth/api_scope` ([search method, OAuth section](https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search)).
- No user login or consent. Token lifetime not read today (U); cache until the `expires_in` the token response returns.

### 1.3 The real gate: production access and housekeeping

- **Partner-only language (V).** "Many of the Buy APIs are a (Limited Release). The use of eBay's Buy APIs in production is intended for eBay partners only. You must apply for production access through the eBay Partner Network ... There is no guarantee that your application for production use of the APIs will be approved." Process: EPN account, Buy API questionnaire (EPN replies within 10 business days), a Developer Support ticket, compliance review, signed contracts ([buy-requirements](https://developer.ebay.com/api-docs/buy/static/buy-requirements.html)). Sandbox is open to any developer account.
- **Ambiguity (V that no badge was found).** The Browse overview and search pages carry no Limited Release badge that I could find; the requirements page says "many", not all, Buy APIs. One eBay community answer says production is "generally intended for business use cases" but personal projects can still use the APIs ([thread](https://community.ebay.com/forum/talk-to-your-fellow-developers-57970/topic/access-to-production-with-a-personal-application-169013/)); that is not an authoritative statement about Browse.
- **Repos that assume a plain keyset (U, not run):** go-ebay-tracker ("production API keys (App ID / Cert ID)"), price-bot, FlipWatch ("free eBay developer Production keyset"), BayRadar. None mention an EPN step.
- **Account-deletion notifications (V).** New developers "must subscribe to or opt out of eBay marketplace account deletion/closure notifications before they make their first production API call"; non-compliance can terminate access ([guide](https://developer.ebay.com/marketplace-account-deletion)). Subscribing means an HTTPS endpoint that answers a GET `challenge_code` with a SHA-256 of `challengeCode + verificationToken + endpoint` (about 30 lines in a Supabase Edge Function). Opt-out is for apps that store no eBay data; this app stores seller usernames, so subscribing is the safer reading (Ricky's call).
- **Key status today (V, names only, values never printed):** `.env.local` has no `EBAY_*` entries and neither does the desk `.env`; the desk wiki lists eBay keys as pending Ricky's identity (`dev/Chief Of Staff/wiki/dusklamp-sources.md`, line 87).
- **Other terms.** The User Agreement bans buy-for-me agents, LLM-driven bots and "any end-to-end flow that attempts to place orders without human review" ([eBay UA](https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259), V). The API License Agreement allows suspension if eBay believes tools undermine its business interests (paraphrase from [Vorp Labs](https://vorplabs.com/agent-tools/ebay-buy-api), U). Design consequence: alerts only, never auto-bid.
- **Finding API is gone.** The hendt/ebay-api README says eBay took the Finding API down in February 2025 ([README](https://github.com/hendt/ebay-api), secondary), so any older "eBay watcher" built on Finding no longer works.

### 1.4 Polling math (limits V, arithmetic mine)

Default limit: **Browse API, all methods except getItems: 5,000 calls/day** ([Buy API call limits](https://developer.ebay.com/develop/api/buy/api_call_limits)). Raising it requires an Application Growth Check ([page](https://developer.ebay.com/grow/application-growth-check)). Live quota is readable through the Developer Analytics `getRateLimits` call (listed on the same pages).

```
calls/day = N_watches x (1440 / M_minutes) x pages_per_poll
pages_per_poll = 1   because sort=newlyListed + itemStartDate:[last poll - small overlap] + limit=200
                     means one page covers every new listing unless >200 appear in one interval
```

| Watches (N) | M=2 min | M=5 | M=10 | M=15 | M=30 | M=60 |
|---|---|---|---|---|---|---|
| 10 | 7,200 (144%) | 2,880 (58%) | 1,440 (29%) | 960 | 480 | 240 |
| 20 | 14,400 | 5,760 (115%) | 2,880 (58%) | 1,920 | 960 | 480 |
| **30** | 21,600 | 8,640 (173%) | **4,320 (86%)** | 2,880 (58%) | 1,440 (29%) | 720 |
| 40 | 28,800 | 11,520 | 5,760 (115%) | 3,840 (77%) | 1,920 | 960 |

Reading it for **30 watches**:

- Flat schedule with 20% headroom (4,000-call budget): M >= 30 x 1440 / 4000 = **10.8 min**. At the raw 5,000 ceiling: 8.64 min. A flat 5-minute cadence is impossible (173%).
- **Tiered plan that fits:** 6 hot watches every 3 min = 6 x 480 = 2,880; 24 normal watches every 30 min = 24 x 48 = 1,152; total **4,032/day (81%)**, leaving about 970 for retries, single-item refreshes (`getItem`) and auction reminders. Worst-case latency: 3 min hot, 30 min normal.
- **Merge watches to buy cadence.** Watches that share a category and price band can share one call with `q=(a, b, c)` (100-char cap) and be separated locally by rules. 30 watches collapsed into 10 groups polled every 5 min = 10 x 288 = 2,880/day.
- **If error 12034 shows that AUCTION cannot be combined with `sort=newlyListed`**, each watch that wants both formats needs two calls (one per format) and the tiered plan doubles to about 8,000/day, which does not fit. Fallback budget: keep fixed-price polling as above (4,032) and poll auctions only for the watches that want them, hourly, with `sort=endingSoonest` and an `itemEndDate` window, e.g. 10 auction watches x 24 = 240 calls/day (total 4,272, 85%).
- **Enrichment is not free.** Search summaries carry title, price, condition, `shortDescription` (with `fieldgroups=EXTENDED`), thumbnails and seller stats, but not item aspects. Any `getItem` call per candidate comes out of the roughly 970 spare calls/day; enriching 1,200 survivors/day would blow the budget, so the LLM tier must run on the summary alone and enrich only starred items.
- Latency model: mean delay = M/2, worst case = M, plus eBay's own index lag between listing creation and appearing in search (U; measure in Step 0 by comparing `itemOriginDate` with first-seen time).

### 1.5 Cheaper or alternative signals, compared

| Signal | Latency | Control | Verdict | Source |
|---|---|---|---|---|
| **Browse API polling** | M minutes (3 to 30 per tier) | Full: price, condition, format, location, dedup | Primary | 1.1 to 1.4 |
| eBay saved-search email (default on) and eBay app push | Not documented; eBay gives no guarantee; users complain of unreliability (anecdote) | Price and other filters editable; no scoring, cooldown or "not this" | Free backstop, and the **ToS-clean fallback if production API access is denied**: forward the emails to an inbox the dashboard parses | [eBay help](https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051) V; [CardboardSniper](https://cardboardsniper.com/blog/ebay-saved-search-alerts-not-working) secondary; eBay's push-notification help page returned a CAPTCHA, so push specifics are U |
| eBay RSS | Dead | n/a | Skip. Sellers reported search RSS gone in 2022. RssBay.net still advertises feeds but I cannot confirm they work (U) | [Value Added Resource, Apr 2022](https://www.valueaddedresource.net/ebay-rss-feed-stores-search/), [RssBay](https://rssbay.net/) |
| Commerce Notification API | n/a for buyers | Topics are seller-side (listing, performance, account deletion); `item_availability` is ePN-partner-only | No buyer "new matching listing" push exists | [Topics](https://developer.ebay.com/develop/api/sell/notification_events) V |
| Finding API | Gone Feb 2025 | n/a | Skip | [hendt/ebay-api](https://github.com/hendt/ebay-api) secondary |
| Scrape eBay HTML or Apify actors | Fast | Full | **Violates the UA.** Apify has many (`caffein.dev/ebay-sold-listings` 4,262 users, `automation-lab/ebay-scraper` 1,130, `memo23/ebay-search-scraper-ppe` 820, `delicious_zebu` 1,094) | [UA](https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259) V |
| Paid alert SaaS (Botifex, Flipify, Copit, Swoopa) | "every 5 minutes on the Pro tier" (Botifex, vendor claim) | Vendor's | Buy-versus-build option; claims U | [Botifex](https://botifex.com/blog/poshmark-mercari-new-listing-notifications) |

---

## 2. Other sourcing sites

Apify counts come from the Apify MCP `search-actors` run today (users total / monthly active). GitHub counts come from `gh api search/repositories` because the GitHub MCP search tool returns no star counts. In "Scrape feasibility", **fetched** means my crawl4ai fetch (this session or the first-pass `research/` folder, 2026-10-26) returned a real page; **blocked** means a bot wall.

| Site | Official buyer-side API | RSS | Native alerts (latency) | Scrape feasibility and existing scrapers | ToS on automation | Sources |
|---|---|---|---|---|---|---|
| **eBay** | **Yes**: Browse API; production partner-gated (1.3) | Dead | Saved-search email plus app push; latency undocumented | Push-notification help page returned a CAPTCHA (saved-searches help fetched fine). Apify: 4,262 / 1,130 / 820 / 1,094 users | Bans automated access (UA) V | [UA](https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259) |
| **Mercari (US)** | None found (U) | None (vendor, U) | Saved-search push and/or email; email "often an end-of-day digest" (vendor, U). Settings page V | Apify `getascraper/mercari-us-scraper` 58/26 ($2.52/1k), `jongoose/mercari-scraper` 33/4 (reads Mercari's GraphQL). GitHub `kevinxo328/mercari-scraper` 5 stars, commit 2026-10-06 | No explicit scraping clause located; forbids circumventing technical measures. **Clause not located, U** | [ToS](https://www.mercari.com/tos/), [notifications help](https://www.mercari.com/us/help_center/article/115/), [Botifex](https://botifex.com/blog/poshmark-mercari-new-listing-notifications) |
| **Poshmark** | None (U) | None (vendor, U) | Saved search; "red dot only, not push" (vendor, U) | **Fetched**: 24 to 32 KB search pages in `research/poshmark.com_search_*`. Apify `piotrv1001` 117/14 ($1/1k), `parseforge` 43/25 ($14.66/1k), `shahidirfan` 20/6. GitHub `kcinnick/posh` 15 stars, 2023 | **Explicit ban**: "copy, scrape, harvest, crawl or use any technology, software or automated systems to collect any information" V | [ToS](https://poshmark.com/terms) |
| **Depop** | **Seller-only** Selling API (listings, offers, orders; Pro sellers). No buyer search | None (U) | Saved searches: **one weekly push**, max 10 searches V (useless for real time) | Apify `abotapi` 75/31, `piotrv1001` 172/19. GitHub `oxylabs/depop-scraper` 484 stars (promo for a paid API) | **Explicit ban**: "scrape or crawl the Service ... or use any bots" V | [API docs](https://partnerapi.depop.com/api-docs/), [saved searches](https://depophelp.zendesk.com/hc/en-gb/articles/360019648117-Saved-Searches), [ToS](https://depophelp.zendesk.com/hc/en-gb/articles/360001773148-Terms-of-Service) |
| **Facebook Marketplace** | None | None | A Marketplace notification category covers saved searches V; timing complaints are anecdotal (U) | Login required; account-ban risk (FlipWatch README, V). Apify official `apify/facebook-marketplace-scraper` 11,786/997 (3.91 stars), `curious_coder/facebook-marketplace` 5,550/617 (4.92), `memo23` 1,394/322 (monitoring mode). GitHub `BoPeng/ai-marketplace-monitor` 395 stars (logs in as you; AGPL) | **Meta Automated Data Collection Terms: no automated collection "without first obtaining Meta's express written permission"** V. Treat as a hard no. | [Meta terms](https://www.facebook.com/legal/automated_data_collection_terms/), [FB help](https://www.facebook.com/help/2229494877335159) |
| **Craigslist** | None | **Removed Oct 2020** (HN, V); vendor says present (U) | **Email search alerts** (account; max 20 results per email; frequency scales with result count) V. A 2020 HN user: "hours and hours" (anecdote) | **Blocked** ("Your request has been blocked") V. Apify `ivanvs` 1,130/62, `solidcode` 532/114 ($1.5/1k). GitHub `stephanlensky/hyacinth` 77 stars, last commit 2024-06-19 | **Explicit ban** on "robots, spiders, scripts, scrapers, crawlers, or any automated or manual equivalent (e.g., by hand)"; liquidated-damages clause V | [ToS](https://www.craigslist.org/about/terms.of.use), [alerts](https://www.craigslist.org/about/help/account/features/alerts), [HN](https://news.ycombinator.com/item?id=24840310) |
| **OfferUp** | None (U) | None (U) | Search alerts plus similar-item alerts, push V | Apify `igolaizola` 191/47 (needs US residential proxies). GitHub `jgdigitaljedi/gs-scraper` 56 stars: the OfferUp lib was "taken down due to a DMCA notice"; repo non-functional | **Explicit ban** on "harvesting bot, robot, spider, script, crawler, or scraper" V | [ToS](https://offerup.com/terms), [alerts help](https://help.offerup.com/hc/en-us/articles/360031995332-Get-notified-about-items-you-want) |
| **ShopGoodwill** | None official; the site has an internal JSON API that community scripts call (U) | None (U) | **Personal Shopper**: email when matching items are listed V (latency undocumented) | Apify `lulzasaur` 35/6, `getascraper` 20/7 (monitoring: new, repriced, closing), `scrapersdelight` 12/1 (Slack/webhook alerts). GitHub `scottmconway/shopgoodwill-scripts` 98 stars, commit 2025-08-11 (includes expiring-auction time alerts) | Bans "third-party applications" and "robot, spider, crawler, scraper, script ... not authorized by us" V | [ToS](https://shopgoodwill.com/about/terms-of-use), [Personal Shopper](https://shopgoodwill.com/Help/FaqDetail/how-do-i-set-up-personal-shopper-searches), [scripts](https://github.com/scottmconway/shopgoodwill-scripts) |
| **GoodwillFinds** | n/a | n/a | n/a | **Closed**: "Goodwill Shutters Online Marketplace GoodwillFinds", published Apr 1, 2025 V. No Apify actor. Drop it. | n/a | [RetailTouchPoints](https://www.retailtouchpoints.com/news/goodwill-shutters-online-marketplace-goodwillfinds/151013/) |
| **Etsy (as a source)** | **Yes**: Open API v3 `findAllListingsActive` with `keywords`, `min_price`, `max_price`, `sort_on=created` V. "Personal App" (deeper review) for use beyond your own shop; "Seller App" is scoped to your own shop. Limits are per-key QPS/QPD shown in the developer portal | None (U) | Not verified (no authoritative help page found) | Apify `epctex/etsy-scraper` 5,488/184, `yumitori/etsy-listings-scraper` 1,516/360, `automation-lab` 1,151/175 | Etsy's ToS and API terms pages were bot-walled: **U** | [Etsy API](https://developers.etsy.com/documentation/), [reference](https://developer.etsy.com/documentation/reference), [rate limits](https://developer.etsy.com/documentation/essentials/rate-limits/) |
| **Chairish** | None (U) | None (U) | "Follow This Search": email on new item or price drop; frequency adjustable V | **Fetched** (50 to 86 KB collection pages in `research/`). Apify `saswave` 8/0, `superslowsloth/chairish-listings` 2/1 (new listings and price drops), `devilscrapes` 2/1 | **Explicit ban**: "crawls, scrapes, or spiders any page, data, or portion" V | [saved searches](https://support.chairish.com/hc/en-us/articles/44253725332753-My-Saved-Searches), [ToS](https://support.chairish.com/hc/en-us/articles/44208742405649-Terms-of-Service) |
| **1stDibs** | None (U) | None (U) | "Follow" a search: **weekly** new-arrivals email V (too slow) | **Blocked** (32-byte response in `research/www.1stdibs.com_*`) V. Apify `saswave` 32/3, `lulzasaur` 9/3, `scrapesage` 3/2 (monitor mode) | Scraping clause not located: **U** | [follow help](https://support.1stdibs.com/hc/en-us/articles/14516797762715-Follow-Search-Results), [UA](https://www.1stdibs.com/about/user-agreement/) |
| **EstateSales.net** | None (U) | None (U) | **Treasure Tracker**: email when a sale within your distance matches a saved term V; free email notifications for sales near you V | Apify `lulzasaur` 34/6, `lexis-solutions` 21/2, `scrapelabmax` 14/2, `scrapersdelight` 12/3 (monitor mode plus alerts) | ToS not fetched: **U** | [Treasure Tracker](https://estatesales.zendesk.com/hc/en-gb/articles/23078824803857-Treasure-Tracker), [email alerts](https://estatesales.zendesk.com/hc/en-gb/articles/26947578346001-How-to-Receive-Email-Notifications-About-Upcoming-Sales) |
| **EstateSales.org** | None (U) | None (U) | Not verified | Apify `lulzasaur/estatesales-org-scraper` 4/0 | Not fetched: **U** | [Apify](https://apify.com/lulzasaur/estatesales-org-scraper) |
| **LiveAuctioneers** | None public (U) | None (U) | Saved-search "Search Alerts" at `/dashboard/search-and-alerts` (login-gated; details U) | Apify `ivanvs` 115/8, `scrapersdelight` 18/7. GitHub `dreamingspires/auction-scraper` 31 stars, last 2021 | **Explicit ban**; "the sites contain robot exclusion headers" V | [ToS](https://www.liveauctioneers.com/termsandconditions) |
| **Invaluable** | None (U) | None (U) | "Follow this Keyword" email alerts V | Apify `lulzasaur/invaluable-scraper` 12/5 | **Explicit ban** on "any robot, spider, other automatic device, or manual process to monitor or copy" V | [alerts FAQ](https://www.invaluable.com/inv/help/faq/emails-alerts/), [terms](https://www.invaluable.com/inv/agreements/) |
| **HiBid** | None official; one Apify actor says it reads "HiBid's own API" (U) | None (U) | Saved-search email updates V | Apify `scrapersdelight` 27/7, `parseforge` 19/9, `getascraper` 18/4, `ecomscrape`. GitHub `alexmi256/HiWatch` 9 stars, 2021 | **Explicit ban**: "web scraping, web harvesting, web data extraction" V | [help](https://help.hibid.com/en/articles/15960614-managing-email-and-notification-preferences), [terms](https://hibid.com/home/termsofuse) |
| **AuctionNinja** | None (U) | None (U) | `/saved-searches` page exists; behavior U | Apify `lulzasaur` 16/3, `getascraper` 4/2, `scrapersdelight` 6/1 (monitor mode) | My ToS fetch returned a vendor list, not the terms: **clause not located, U** | [saved searches](https://www.auctionninja.com/saved-searches) |
| **EBTH** | None public (U) | None (U) | Saved Searches help article exists (page walled; behavior U) | Apify `lulzasaur/ebth-scraper` 5/2 ($10/1k) | **Explicit ban** on "any robot, spider, scraper, data mining tools" V | [terms](https://www.ebth.com/terms), [Apify](https://apify.com/lulzasaur/ebth-scraper) |
| **Whatnot** | **Seller-only** REST API (products, inventory, orders, shows). No buyer search | None (U) | Bookmark a show, listing or search to "get notified" V | Apify `epicscrapers` 220/62, `devcake` 72/8, `crawloop` 29/5 (monitor mode) | **Explicit ban**: "scrape, spider, or crawl the App or harvest or manipulate data" V | [API](https://developers.whatnot.com/getting-started/introduction), [bookmark help](https://help.whatnot.com/hc/en-us/articles/9780885421069-Bookmark-a-show-listing-or-search), [terms](https://www.whatnot.com/terms) |

**What the table says**

- **Official buyer-side search API:** eBay and Etsy. That is all.
- **Explicit automation bans (V):** Poshmark, Depop, Craigslist, OfferUp, ShopGoodwill, Chairish, LiveAuctioneers, Invaluable, HiBid, EBTH, Whatnot (11 site ToS), plus Meta for Facebook, plus eBay. Unconfirmed: Mercari, Etsy, 1stDibs, EstateSales.net, EstateSales.org, AuctionNinja.
- **Enforcement signals (anecdote, not legal advice):** the OfferUp library in `gs-scraper` was DMCA'd; FlipWatch warns Facebook "can limit or ban accounts"; Craigslist's ToS carries liquidated damages. Rule of thumb: never scrape while logged in, never scrape Meta, and treat low-volume residential-IP polling of public pages as a per-site risk Ricky accepts or declines.
- **Native alerts fast enough to forward:** Craigslist email, ShopGoodwill Personal Shopper, EstateSales.net Treasure Tracker, Invaluable, Chairish, HiBid (all email, so ingestible), and eBay saved-search email. In-app push on Mercari, OfferUp, Facebook and Whatnot cannot be forwarded. Too slow: Depop (weekly), 1stDibs (weekly).
- **Apify as a polling engine is expensive at these cadences.** At $1.5 per 1,000 results: 10 watches x every 30 min x 20 results per run = 480 runs x 20 x $0.0015 = **$14.40/day (about $430/month)**. Use it on demand, not as the poller. Whether "new items only" actors bill only new items is U. An `APIFY_TOKEN` is already in `.env.local`.

---

## 3. Matching: options and cost

### 3.1 Tiered pipeline (recommended)

| Tier | What | Marginal cost | Strength | Weakness |
|---|---|---|---|---|
| **T0** server-side | eBay `q` (AND/OR), `category_ids`, `price` band, `conditions`, `buyingOptions`, `itemLocationCountry`/`deliveryCountry`, `itemStartDate` | API quota only | Cuts 99% of the catalog before it reaches your code | Keyword search is literal; vintage titles are messy |
| **T1** rules in TypeScript | Regex include/exclude on title and aspects, maker/brand lists, "for parts/not working" exclusion, lot/quantity detection, seller feedback floor, price <= X% of comp (from `research/pricing`) | $0 | Deterministic, instant, explainable | Misses synonyms and misspellings |
| **T2** LLM | Claude Haiku 5.5 reads the search-summary record (title, price, condition, category, `shortDescription` via `fieldgroups=EXTENDED`, seller feedback, optional thumbnail; **no item aspects**, which need a `getItem` call) against the watch description and returns `{match, score, why}` | See 3.2 | Understands "Stiffel-style" and "tole" vs "brass" nuances | Spend and a little latency; needs an eval set |
| **T3** optional | Embeddings (3.3) and image similarity (3.4) as a ranker or reference-photo match | Near $0 on your hardware | "Looks like this" and "more like the ones I liked" | Not a gate; models are fashion- or generic-biased |

### 3.2 Haiku cost math (prices V from [pricing](https://docs.claude.com/en/docs/about-claude/pricing), model IDs from [models overview](https://docs.claude.com/en/docs/about-claude/models/overview))

- **Model:** `claude-haiku-5-5`, released Oct 7, 2026. Input **$0.10 / MTok** (prompts up to 100k tokens), output **$0.50 / MTok**, cache read $0.01 / MTok, Batch API $0.05 in / $0.25 out ([model page](https://platform.claude.com/docs/en/models/haiku-5-5/overview)). Older Haiku 4.5 is $1 / $5.
- **Thinking is the cost swing (V).** Haiku 5.5 has adaptive thinking **on by default at `medium` effort**; "tokens Claude uses while thinking [are] billed as output tokens" ([steering thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)). You can turn it off with `thinking: {"type": "disabled"}` at `high` effort or below, or minimize it with `effort: "low"` ([what's new](https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5)). `max_tokens` caps thinking plus answer.
- **Tokenizer (V):** Haiku 5.5 counts the same text as roughly 30% more tokens than Haiku 4.5, so my token estimates below are rough; measure with the token-counting endpoint before trusting them.
- **Vision (V):** an image costs `ceil(width/28) x ceil(height/28)` tokens ([vision](https://docs.claude.com/en/docs/build-with-claude/vision)): 500x500 = 18 x 18 = **324**; 1000x1000 = 36 x 36 = **1,296**.

Assumptions (mine): watch description + instructions = 400 input tokens; listing record (title, price, condition, category, short description from the search summary) = 150 input tokens; compact JSON answer = 50 output tokens. So **550 in / 50 out** per listing.

```
cost per 1,000 listings = 1000 x (in_tokens x $0.10 + out_tokens x $0.50) / 1,000,000
```

| Scenario | Tokens in / out | Cost per 1,000 listings |
|---|---|---|
| **A. Thinking disabled, text only** | 550 / 50 | Per listing: 550 x $0.10/1e6 = $0.000055 in, 50 x $0.50/1e6 = $0.000025 out, total $0.000080; x 1,000 = **$0.080** |
| A2. As A, 20 listings per request sharing one rubric | 3,400 / 600 per 20 | 50 requests x (340 + 300 micro-dollars) = **$0.032** |
| B. A plus a 500px thumbnail | 874 / 50 | **$0.112** |
| B2. A plus a 1000px image | 1,846 / 50 | **$0.210** |
| **C. Default adaptive thinking (assume 500 output tokens incl. thinking)** | 550 / 500 | Per listing: 55 + 250 = 305 micro-dollars; x 1,000 = **$0.305** |
| D. A via Batch API (not real time) | 550 / 50 at half price | **$0.040** |
| For scale: A on Haiku 4.5 / Sonnet 5.5 | same tokens | $0.80 / $1.60 |

Monthly, if 1,200 listings/day survive T0 and T1 (assumption: 30 watches x ~40 new listings/day; unmeasured): A **$2.88**, B **$4.05**, C **$10.98**. At 12,000/day: $28.80 / $40.46 / $109.80. Caching the rubric would cut input further, but whether a ~400-token prefix meets the minimum cacheable length is U, so treat caching as upside only.

### 3.3 Embeddings in Supabase (pgvector)

- V: pgvector is available in Supabase ([docs](https://supabase.com/docs/guides/database/extensions/pgvector)); `gte-small` runs natively in Edge Functions via `new Supabase.ai.Session('gte-small')`, 384 dimensions, `mean_pool` and `normalize` ([semantic search guide](https://supabase.com/docs/guides/functions/examples/semantic-search)). No embedding-API bill.
- V: Edge Function limits: 256 MB memory, **2 s CPU per request**, wall clock 150 s (free) or 400 s (paid), request idle timeout 150 s ([limits](https://supabase.com/docs/guides/functions/limits)). The 2 s CPU cap bounds how many titles one invocation can embed; throughput per invocation is unmeasured (U), so embed in small batches.
- Storage: 384 floats x 4 bytes = 1,536 B per row; 36,000 rows/month is about 55 MB (my arithmetic).
- Use it as a ranker, not a gate: (a) cosine between the watch description and each title as a free pre-filter ahead of Haiku; (b) relist and near-duplicate detection; (c) suppress neighbors of "not this" rejections (section 4). Short noisy titles are where `gte-small` is weakest (my judgment).

### 3.4 Image similarity to a reference photo (Hugging Face, checked today)

| Model | Params | Image-tower GFLOPs (OpenCLIP profile) | License | Weights | Fit |
|---|---|---|---|---|---|
| [`patrickjohncyh/fashion-clip`](https://hf.co/patrickjohncyh/fashion-clip) (FashionCLIP 2.0, ViT-B/32, fine-tuned from LAION CLIP) | 151.3M | 8.82 | MIT | 605 MB | Clothing, shoes, bags |
| [`Marqo/marqo-fashionCLIP`](https://hf.co/Marqo/marqo-fashionCLIP) (ViT-B/16 fine-tune; ONNX and transformers.js included) | 149.6M | 35.13 | Apache-2.0 | 599 MB | Better fashion retrieval: text-to-image AvgRecall 0.192 vs FashionCLIP 2.0's 0.163 (model card); about 4x the CPU cost |
| [`Marqo/marqo-fashionSigLIP`](https://hf.co/Marqo/marqo-fashionSigLIP) | not read | not read | not read | not read | Exists (stat only) |
| [`openai/clip-vit-base-patch32`](https://hf.co/openai/clip-vit-base-patch32) | n/a in listing | 8.82 | not shown | n/a | Generic baseline for lamps, art, furniture |
| [`google/siglip2-base-patch16-224`](https://hf.co/google/siglip2-base-patch16-224) | 375.2M (both towers) | not in the profile CSV | Apache-2.0 | n/a | Generic, stronger than CLIP B/32 (my judgment) |

GFLOPs source: [OpenCLIP `model_profile.csv`](https://raw.githubusercontent.com/mlfoundations/open_clip/main/docs/model_profile.csv) (V). Both fashion models are fashion-tuned, which is the wrong prior for lamps, art and furniture; use a generic CLIP or SigLIP2 for those categories.

**Can the CPU-only Fedora box (i7-8565U, 15 GB, no GPU) run them?** Yes for a shortlist. Estimate, not measured (U): at an effective 30 to 60 GFLOPS, ViT-B/32 needs roughly 0.15 to 0.3 s per image (3 to 6 images/s) and ViT-B/16 roughly 0.6 to 1.2 s (about 1 image/s). At 1,200 shortlisted images/day, ViT-B/16 is roughly 20 to 25 CPU-minutes per day. Image download time will dominate. Do not embed every listing.

Alternatives with no self-hosting: eBay's `search_by_image` (U, see 1.1) and Haiku vision at $0.11 to $0.21 per 1,000 images (scenarios B and B2).

### 3.5 Recommendation

T0 + T1 in Phase 1, T2 (Haiku 5.5, thinking disabled, 20 listings per request, summary fields only) on T1 survivors, T3 only after Ricky has real "not this" data. Build a 100-listing labeled eval set from the first week of alerts before changing any tier.

---

## 4. Alert hygiene

| Concern | Design | Notes |
|---|---|---|
| **Dedup** | Primary key `(marketplace, itemId)`. Secondary fingerprint `(seller, normalized title, price bucket)` because relists get new ids; match the fingerprint within 30 days and suppress unless price dropped >= 10%. | `itemId` has the form `v1` + pipe + number + pipe + `0`; `legacyItemId` is the bare number (search response). Relist behavior is my inference (U). |
| **Seen store** | Table `seen_listings(marketplace, item_id, watch_id, first_seen_at, last_price, last_alerted_at, fingerprint)` with a unique index; insert-on-conflict-do-nothing is the dedup check. TTL 90 days, extended while an auction is live. | Postgres in Supabase (V that pg_cron and pgvector are available). |
| **Cooldown per watch** | At most 1 push per watch per 5 min; if 3+ matches queue inside the window, send one grouped push ("4 matches for Stiffel lamps"). Hourly cap per watch (default 6); overflow goes to the inbox only. | Prevents a bad watch from burning attention. |
| **Quiet hours** | Default 22:00 to 07:00 local: matches go to the inbox, no push. Overrides: starred auction ending within 60 min; score >= 0.9 and price <= 50% of comp. | Needs Ricky's timezone and thresholds (open questions). |
| **Auction-ending reminders** | On match, store `item_end_date`. If starred, push at T-60 min and T-10 min with current bid vs his max. Refresh the bid with one `getItem` call per reminder (about 2 calls per starred auction), not another search. | Search results carry `itemEndDate`, `currentBidPrice`, `bidCount`. Reminder arithmetic stays well inside the ~970 spare calls/day in 1.4. |
| **Price-drop re-alert** | Re-alert only if price falls >= 10% since `last_alerted_at` and the item is still inside the price band. | Fixed-price listings only. |
| **"Not this" button** | Reason chips: wrong item, too expensive, bad condition, bad seller, already have. Stores a `feedback` row. | See next row. |
| **What to do with "not this"** | (1) Suppress that item and its fingerprint forever. (2) Append the 8 most recent rejections (title plus reason) to that watch's Haiku prompt as "do not alert" examples. (3) If the same token appears in 3+ rejects, propose an exclude keyword and ask Ricky to confirm. (4) Mute a seller after 3 rejects. (5) With embeddings, suppress new titles with cosine >= 0.92 to a rejected one for 14 days. (6) Track weekly precision per watch (starred or bought divided by alerts) and suggest raising `min_score` or tightening the price band when precision is under 20%. | All design choices, none verified externally; keep each reversible. |
| **Human in the loop** | Alerts link to the listing (`itemWebUrl`, or `itemAffiliateWebUrl` if EPN is ever approved). No auto-bid, no auto-offer. | eBay UA bans buy-for-me and LLM order flows without human review (V). |

### 4.1 Scheduling and runtime (V from Supabase docs)

`pg_cron` jobs "can run anywhere from every second to once a year", can call an Edge Function over HTTP, and Supabase recommends no more than 8 concurrent jobs of at most 10 minutes each ([Cron](https://supabase.com/docs/guides/cron)). Plan: one cron job every minute invokes `poll-ebay`, which runs watches whose `next_poll_at <= now()`. Edge Function egress is a datacenter IP (my inference, U), which is fine for the official eBay API but wrong for any Phase 2 HTML scraper; those belong on the Fedora box's residential IP.

### 4.2 Getting the alert to a phone (checked today)

| Channel | Facts | Verdict |
|---|---|---|
| **Web Push in the dashboard (PWA)** | iOS and iPadOS 16.4 added Web Push for Home Screen web apps ([WebKit announcement, 2023](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/), V); current iOS behavior beyond that post not re-checked (U) | Free, no third party, fits React+Vite. Requires the user to install the PWA on iPhone. |
| **Pushover** | $4.99 one-time per platform; 10,000 messages per month free per user ([pricing](https://pushover.net/pricing), V) | Simplest reliable native push if budget is trivial. |
| **ntfy** | Free to publish by HTTP; the ntfy.sh public server "will always" be free but could add paid plans; the maintainer calls the **iOS app "very bare bones and quite frankly a little buggy"**; Android has "instant delivery" ([FAQ](https://docs.ntfy.sh/faq/), V) | Fine on Android or self-hosted; risky if Ricky is on iPhone. |
| Telegram, SMS | Not verified today | Many prior-art projects use Telegram (section 5); verify the Bot API before choosing. |

Phone type is unknown. His account email is an Apple private relay, which hints at an iPhone but proves nothing; confirm (open questions).

---

## 5. Prior art on GitHub (stars and default-branch last-commit dates from `gh api` today; "works in 2026?" is U unless I ran it, and I ran none)

| Repo | Stars | Last commit | Lang | What it polls | How it notifies | Works in 2026? |
|---|---|---|---|---|---|---|
| [firozt/go-ebay-tracker](https://github.com/firozt/go-ebay-tracker) | 1 | 2026-09-09 | Go | eBay Browse API (client-credentials), configurable interval; README math: 1-minute polling = ~1,440 calls/day of the 5,000 default | Discord webhook, ntfy, local sound webhook | Plausible (same surface as 1.1); U |
| [ChrisKariofyllis/BayRadar](https://github.com/ChrisKariofyllis/BayRadar) | 1 | 2026-10-20 | TypeScript (Next.js, SQLite) | eBay via App ID + Cert ID; checks due monitors every 30 s; has a mock mode for use before eBay approves keys | ntfy, Telegram, Discord, Gotify; "AI Title Gatekeeper"; Gixen snipe arming | New (created 2026-08-30); license NOASSERTION; U |
| [mrballistic/price-bot](https://github.com/mrballistic/price-bot) | 6 | 2026-10-26 | TypeScript | Reverb, eBay Browse (client credentials), Amazon; GitHub Actions cron every 30 min | Discord webhook plus dashboard | Active; U |
| [Crepe950/flipwatch](https://github.com/Crepe950/flipwatch) | 5 | 2026-10-17 | TypeScript | Craigslist, Kijiji, eBay (Browse keys), OfferUp, optional Facebook (logged in; README says "against Meta's Terms of Service") | Discord, Telegram, Slack, ntfy, email, browser push; Claude or OpenAI "deal analysis" | 11 days old (created 2026-10-15); MIT; U |
| [BoPeng/ai-marketplace-monitor](https://github.com/BoPeng/ai-marketplace-monitor) | 395 | 2026-10-18 | Python (GitHub tags it HTML) | Facebook Marketplace via Playwright, logged in as you; AI rates each listing (OpenAI, Anthropic, DeepSeek, Gemini, Ollama) | PushBullet, Pushover, Telegram, ntfy, HTML email, daily digest | Active; AGPL-3.0; README's own legal notice says Facebook's terms prohibit this; U |
| [stephanlensky/hyacinth](https://github.com/stephanlensky/hyacinth) | 77 | **2024-06-19** (its `pushed_at` of 2026-10-26 is bot-branch noise) | Python | Craigslist and Facebook Marketplace via a plugin system; search batching to avoid anti-bot limits; configurable polling | Discord bot | Stale 2+ years; likely broken by anti-bot changes; U |
| [orangecoding/fredy](https://github.com/orangecoding/fredy) | 1,596 | 2026-10-26 | JavaScript | Real-estate portals (per-provider scrapers), dedup across platforms | Slack, Telegram, email, ntfy, Discord, Pushover, Apprise and more; working hours | Active; different domain but the best architecture reference (Provider, Job, Channel) |
| [Fuyucch1/Vinted-Notifications](https://github.com/Fuyucch1/Vinted-Notifications) | 183 | 2025-10-27 | Python | Vinted (real-time listing alerts per repo description) | Not read | ~12 months since last commit; U |
| [scottmconway/shopgoodwill-scripts](https://github.com/scottmconway/shopgoodwill-scripts) | 98 | 2025-08-11 | Python | ShopGoodwill's authenticated API: bid sniper, favorites, expiring-auction time alerts | Script output | Plausible; GPL-3.0; U |
| [jgdigitaljedi/gs-scraper](https://github.com/jgdigitaljedi/gs-scraper) | 56 | 2020-05-18 | JavaScript | Craigslist, OfferUp (LetGo), garage sales | n/a | **Dead**: README says the OfferUp library was taken down by DMCA and the app "does not fully work" |
| [hendt/ebay-api](https://github.com/hendt/ebay-api) | 216 | 2026-10-14 | TypeScript | Client library for Browse and other eBay REST APIs; README says Finding API is gone | n/a | Active building block (Node and browser; Deno compatibility not checked) |
| [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io) | 35,309 | 2026-10-26 | Python | Any web page change | Notification fan-out | Active; generic fallback for pages with no API (still a ToS question) |
| [caronc/apprise](https://github.com/caronc/apprise) | 17,651 | 2026-10-25 | Python | n/a | Notification fan-out library | Active |
| [binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) | 35,091 | 2026-10-26 | Go | n/a | HTTP pub-sub push (see iOS caveat in 4.2) | Active |
| [huginn/huginn](https://github.com/huginn/huginn) | 50,149 | 2026-10-26 | Ruby | Generic agents (RSS, website) | Email and more | Active but heavy for this job |
| henryecw/ebay-monitor, devinmerch/ebay_webscraper | 3 / 3 | 2020 / 2022 | JS / Python | eBay search to Discord | Discord | Dead or Finding-era; the Finding API was shut down in Feb 2025 |

Takeaway: **no popular, maintained eBay buy-alert repo exists.** The eBay-specific projects are small and new (1 to 6 stars), and the popular multi-site ones (`ai-marketplace-monitor`, `hyacinth`) are Facebook/Craigslist scrapers that sit on the wrong side of those sites' terms. This is a build, with `hendt/ebay-api` and `fredy`'s Provider/Job/Channel shape as references.

---

## 6. Recommendation

### Step 0 (about an hour, needs Ricky's identity; resolves the one real risk)

1. Create the eBay developer account and a **Production** keyset.
2. Handle account-deletion notifications: subscribe with a small Edge Function (preferred, since seller usernames are stored) or file the opt-out.
3. Mint an application token (client credentials, scope `https://api.ebay.com/oauth/api_scope`).
4. Make one call: `item_summary/search?q=stiffel lamp&limit=1&filter=deliveryCountry:US`. **Record only the HTTP status and any `errorId`, never the token.**
5. Test list, in order, with the minimum number of calls:
   a. `buyingOptions:{AUCTION|FIXED_PRICE}` with `sort=newlyListed` (error 12034?), both with a leaf `category_ids` and with `q` only;
   b. `fieldgroups=EXTENDED` returns `shortDescription`;
   c. `category_ids` with two values (one-category-per-request note);
   d. `itemStartDate:[...]` start-only form accepted;
   e. index lag: newest `itemOriginDate` versus now.
6. **Outcome A, HTTP 200:** proceed to Phase 1. **Outcome B, 403 / errorId 1100 "insufficient permissions":** submit the EPN Buy API questionnaire (answer within 10 business days) and run the email-ingestion fallback in the meantime.

### Phase 1: eBay-only

- **Data (Supabase):** `watches` (description, `q`, category, price min/max, conditions, `buyingOptions`, tier hot/normal, min_score, cooldown, quiet hours, channel), `seen_listings`, `alerts`, `feedback`. Dashboard UI: watch editor, alert inbox with "Starred", "Not this", "Bought".
- **Poller:** `pg_cron` every minute, Edge Function `poll-ebay`; token cached in a table; per-watch call as in 1.1 with `sort=newlyListed`, `itemStartDate` = last poll minus a small overlap, `limit=200`, `fieldgroups=EXTENDED`, **`buyingOptions:{AUCTION|FIXED_PRICE}`** with a leaf `category_ids` (otherwise auctions never appear; split into per-format calls if Step 0 shows error 12034), `deliveryCountry:US`. Hot watches every 3 min, normal every 30 min, with a budget guard that reads `getRateLimits` and demotes watches before hitting 5,000.
- **Match:** T0 filters, T1 rules, T2 Haiku 5.5 (`thinking: {"type": "disabled"}`, 20 listings per request, text plus 500px thumbnail) on survivors. Expected spend $3 to $5 per month at 1,200 survivors/day.
- **Deliver:** Web Push from the dashboard PWA, plus Pushover as the "always works" channel (Ricky's choice). Alerts only; Ricky buys.
- **Measure from day 1:** first-seen minus `itemOriginDate` (latency), calls/day vs 5,000, alerts per day, precision per watch, Haiku spend.

### Phase 2: widen, in this order

1. **Email ingestion (ToS-clean):** Ricky creates saved searches on Craigslist, ShopGoodwill (Personal Shopper), EstateSales.net (Treasure Tracker), Invaluable, Chairish, HiBid and eBay; the emails are forwarded to an inbox the pipeline parses, then pass through the same dedup, scoring and push. Mechanism (Gmail API push, or an inbound-email webhook service) is U; run a Vendor-First check before building.
2. **Etsy Open API v3** as a second API source (keywords, price band, newest first). Apply for a Personal App early because of the review; Etsy's terms are U.
3. **Fedora-box pollers** for ShopGoodwill and HiBid only if Ricky accepts the ToS risk: public pages, no login, 1 request per minute or slower, residential IP.
4. **Apify on demand** for Mercari, Poshmark, Depop, OfferUp, with a hard monthly spend cap (cost math in section 2).
5. **Native-only, no automation:** Facebook Marketplace, OfferUp/Mercari/Whatnot in-app push, LiveAuctioneers. Do not scrape Meta.
6. **Skip:** GoodwillFinds (closed), 1stDibs (weekly emails, blocked), Depop alerts (weekly), AuctionNinja/EstateSales.org/EBTH until their terms are read.

---

## 7. Open questions

1. **Will eBay grant Browse production access to a personal sourcing tool?** Only Step 0 answers it. If not, are you willing to apply through EPN with a business model description?
2. **iPhone or Android?** It decides Web Push (iOS needs a Home Screen install) versus ntfy versus Pushover.
3. **How many watches, and which categories?** The hot/normal split and the Haiku volume assumption (1,200 listings/day) are guesses.
4. **Location:** estate sales, Craigslist, OfferUp and Facebook are local. Which ZIP and radius, and is shipping acceptable for eBay finds?
5. **Risk appetite on ToS:** 11 sites ban scraping and Meta needs written permission. Is "forward their own emails" the ceiling, or is low-volume public-page polling acceptable on some sites?
6. **How is "underpriced" defined?** A fixed price band per watch (as written), or relative to the comps in `research/pricing` (needs a comp lookup in T1 or T2)?
7. **Auctions in or out for Phase 1?** They need the reminder logic and the explicit `buyingOptions` filter.
8. **Timezone and quiet hours**, and whether any override (e.g. a starred auction closing) may wake him.
9. **Real eBay index lag** between listing creation and appearance in Browse search; unmeasured.
10. **Etsy:** does the Etsy shop exist yet (affects Seller App vs Personal App), and are its API terms acceptable?
11. **Embedding models on the Fedora box:** approve a CPU benchmark (not run, since I was read-only) before committing to image similarity.

---

## Appendix: raw pages and tool queries

Saved pages: `research/dashboard/raw/sourcing-*` (see the generated list below). Not saved as pages, but used: Apify MCP `search-actors` (about 30 queries), GitHub MCP `search_repositories` (returned no star counts, so `gh api` supplied stars and commit dates), Hugging Face MCP (`hub_repo_search`, `hub_repo_details`, `hf_fs`), WebFetch (HN thread, Craigslist RSS 403, EBTH help page "CSS error", RetailWire 429, Reddit blocked).

**Walls and failures (under 1 KB, or not the real page):** `sourcing-hn-craigslist-rss.md` (24 B, used WebFetch instead), `sourcing-craigslist-rss-test.md` (165 B, blocked), `sourcing-copit-poshmark.md` (90 B), `sourcing-etsy-api-terms.md` (4 B), `sourcing-tos-etsy.md` (4 B), `sourcing-ebth-saved-searches.md` (525 B). Other failures: eBay push-notification help page (CAPTCHA), Whatnot `/docs/getting-started/introduction` (404; the working path is `/getting-started/introduction`), AuctionNinja ToS (vendor list instead of terms), Craigslist and Facebook search pages (blocked or login-gated).

**Generated index of saved pages (name, bytes). Count: 93 files.**

```
8351 sourcing-1stdibs-follow-search.md
23576 sourcing-apify-ebth-scraper.md
103799 sourcing-auctionninja-saved-searches.md
11430 sourcing-botifex-craigslist.md
13283 sourcing-botifex-posh-mercari.md
10058 sourcing-cardboardsniper-saved-search.md
5524 sourcing-chairish-saved-searches.md
32645 sourcing-claude-adaptive-thinking.md
14308 sourcing-claude-haiku-5-5-overview.md
16389 sourcing-claude-haiku-5-5-whats-new.md
16093 sourcing-claude-models-overview.md
49133 sourcing-claude-pricing.md
32633 sourcing-claude-vision.md
90 sourcing-copit-poshmark.md
2858 sourcing-craigslist-alerts-help.md
165 sourcing-craigslist-rss-test.md
2053 sourcing-craigslist-searches-help.md
10575 sourcing-craigslist-tos.md
56908 sourcing-depop-api-terms.md
5834 sourcing-depop-saved-searches.md
5046 sourcing-depop-selling-api.md
47615 sourcing-ebay-account-deletion.md
36573 sourcing-ebay-api-browse-guide.md
33983 sourcing-ebay-browse-filters.md
35818 sourcing-ebay-browse-getitems.md
35437 sourcing-ebay-browse-overview.md
118363 sourcing-ebay-browse-search.md
35831 sourcing-ebay-browse-search-by-image.md
40529 sourcing-ebay-buy-call-limits.md
14685 sourcing-ebay-buy-overview.md
35267 sourcing-ebay-buy-requirements.md
89680 sourcing-ebay-call-limits.md
7069 sourcing-ebay-community-personal-app.md
9488 sourcing-ebay-community-rate-limit.md
9405 sourcing-ebay-growth-check.md
3521 sourcing-ebay-help-push-notifications.md
9719 sourcing-ebay-help-saved-searches.md
82809 sourcing-ebay-notification-api.md
427958 sourcing-ebay-notification-topics.md
95058 sourcing-ebay-oauth-cc.md
94691 sourcing-ebay-oauth-rate-limits.md
89680 sourcing-ebay-support-call-limits.md
162433 sourcing-ebay-user-agreement.md
525 sourcing-ebth-saved-searches.md
6057 sourcing-estatesales-net-email.md
7858 sourcing-estatesales-net-treasure-tracker.md
15217 sourcing-etsy-api-home.md
4 sourcing-etsy-api-terms.md
412057 sourcing-etsy-find-listings.md
9842 sourcing-etsy-rate-limits.md
4668 sourcing-fb-marketplace-notifications-help.md
25111 sourcing-gh-shopgoodwill-scripts.md
1672 sourcing-goodwillfinds-closed.md
25679 sourcing-goodwillfinds-closed2.md
7597 sourcing-hibid-notifications-help.md
24 sourcing-hn-craigslist-rss.md
12509 sourcing-invaluable-alerts-faq.md
23595 sourcing-liveauctioneers-alerts.md
6510 sourcing-mercari-help-notifications.md
13356 sourcing-ntfy-faq.md
236774 sourcing-ntfy-publish.md
7250 sourcing-offerup-notify-help.md
6167 sourcing-openclip-model-profile.csv
3148 sourcing-pushover-pricing.md
5527 sourcing-rssbay.md
24975 sourcing-scrapecreators-fb-alerts.md
4926 sourcing-shopgoodwill-personal-shopper.md
48432 sourcing-supabase-auto-embeddings.md
4913 sourcing-supabase-cron.md
11627 sourcing-supabase-edge-limits.md
20938 sourcing-supabase-pgvector.md
17759 sourcing-supabase-semantic-search.md
59980 sourcing-tos-1stdibs.md
128115 sourcing-tos-auctionninja.md
82904 sourcing-tos-chairish.md
266441 sourcing-tos-depop.md
95762 sourcing-tos-ebth.md
4 sourcing-tos-etsy.md
43728 sourcing-tos-hibid.md
50323 sourcing-tos-invaluable.md
69968 sourcing-tos-liveauctioneers.md
138583 sourcing-tos-mercari.md
19916 sourcing-tos-meta-automated.md
53620 sourcing-tos-offerup.md
1365994 sourcing-tos-poshmark.md
48299 sourcing-tos-shopgoodwill.md
21299 sourcing-vae-ebay-rss.md
25839 sourcing-vorplabs-ebay-buy-api.md
14095 sourcing-webkit-web-push-ios.md
1734 sourcing-whatnot-api-intro.md
5375 sourcing-whatnot-api-intro2.md
8252 sourcing-whatnot-bookmark-search.md
837711 sourcing-whatnot-terms.md
```
