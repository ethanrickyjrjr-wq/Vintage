# eBay developer platform: end-to-end research for the Hollywood and Vine dashboard

Date: 2026-10-26. Author: research agent. Scope: buy-side alerts, sell-side sales/inventory, sold events, auth, limits, native eBay features, client libraries. Nothing built.

Labels used on every claim:
- VERIFIED = read today in a page, OpenAPI spec, or registry response I fetched (raw copy in `research/dashboard/raw/ebay-*`).
- UNVERIFIED = memory, inference, anecdote, or could not fetch. Marked inline.

How the facts were obtained: the developer.ebay.com docs site is a JS app, so the HTML fetch returns mostly nav chrome. The authoritative content came from (a) the official OpenAPI files at `https://developer.ebay.com/develop/api/spec/<name>.json` (browse_api, marketplace_insights_api, inventory_api, fulfillment_api, notification_api, buy_feed_api, feed_api, finances_api, taxonomy_api; the marketplace_insights one is YAML despite the extension) and (b) the `.md` twin of each guide/API page (append `.md`), plus the static guide pages. Raw file names are given as `raw/ebay-<slug>`.

## 0. Summary table

| Need | Use | Auth | Status |
|---|---|---|---|
| Buy alerts (new listings matching description + price) | Browse `GET /buy/browse/v1/item_summary/search` | App token (client credentials), scope `https://api.ebay.com/oauth/api_scope` | Endpoint VERIFIED. Production access for this exact call is a DOC CONFLICT, see 1.2. Test first. |
| Sold comps | Marketplace Insights `GET /buy/marketplace_insights/v1_beta/item_sales/search` | App token, scope `.../buy.marketplace.insights` | Restricted. Treat as unavailable. Seller Hub Product Research (manual UI) is the free substitute. |
| Our sales / orders | Sell Fulfillment `GET /sell/fulfillment/v1/order` | User token (auth code), scope `sell.fulfillment.readonly` | VERIFIED |
| Our inventory incl. listings made in eBay app/web | Trading API `GetMyeBaySelling` / `GetSellerList`, or Sell Feed `LMS_ACTIVE_INVENTORY_REPORT`. NOT the Inventory API. | User token | VERIFIED that Inventory API cannot see UI-made listings |
| Real-time "sold" push | Notification API topic `ORDER_CONFIRMATION` (user subscription) | Auth-code token with `sell.fulfillment` scopes | Topic VERIFIED to exist. Whether it fires for UI-made listings and is open to a plain dev keyset: UNVERIFIED |
| Mandatory compliance | `MARKETPLACE_ACCOUNT_DELETION` HTTPS endpoint | n/a | Required before first production call, see 3.3 |

## 1. Buy side (sourcing alerts)

### 1.1 Browse API `item_summary/search`

Source: OpenAPI spec https://developer.ebay.com/develop/api/spec/browse_api.json (raw/ebay-spec-browse_api.json), `.md` twin https://developer.ebay.com/develop/api/buy/browse_api.md (raw/ebay-api-buy-browse_api.md). All VERIFIED unless marked.

- Production server: `https://api.ebay.com/buy/browse/v1`; sandbox `https://api.sandbox.ebay.com/buy/browse/v1`. Endpoint: `GET /item_summary/search`. Other endpoints: `POST /item_summary/search_by_image`, `GET /item/{item_id}`, `GET /item/get_item_by_legacy_id`, `GET /item` (getItems), `GET /item/get_items_by_item_group`, `POST /item/{item_id}/check_compatibility`.
- Security scheme: OAuth2 clientCredentials, tokenUrl `https://api.ebay.com/identity/v1/oauth2/token`. Scope for search: `https://api.ebay.com/oauth/api_scope` ("View public data from eBay"). Doc text: "All methods in the Browse API require an Application access token, which is obtained using the client credentials grant flow." So no user token for search.
- `getItems` (`GET /item`) needs scope `https://api.ebay.com/oauth/api_scope/buy.item.bulk` and is the only Browse method whose spec says "This is a (Limited Release) available only to select Partners."
- `q`: "Maximum length: 100 characters" (longer is truncated). Space-separated keywords are AND. OR syntax: `q=(iphone, ipad)`. "The * wildcard character is not allowed in this field."
- `limit`: "Min: 1 Max: 200 Default: 50". `offset`: "Min: 0 Max: 9,999 Default: 0", must be 0 or a multiple of `limit`. "This method can return a maximum of 10,000 items in one results set." So pagination cap = 10,000 items, 50 pages at limit 200.
- `sort`: default Best Match. Values per spec: `price`, `-price`, `distance`, `newlyListed` ("Listing date ... sorted based on their itemOriginDate. Newly listed items are shown first."), `endingSoonest`.
- `category_ids`: "Currently, you can pass in only one category ID per request." (the same paragraph shows a comma-list example; treat as one). "If a top-level (L1) category is specified, you must also include a q query parameter." Category IDs are found via Taxonomy API (spec: raw/ebay-spec-taxonomy_api.json; 5,000 calls/day) or `fieldgroups=ASPECT_REFINEMENTS` -> `dominantCategoryId`.
- Default result set: "Only listings where FIXED_PRICE (Buy It Now) is a buying option are returned by default. To retrieve listings that do not have FIXED_PRICE as a buying option, the buyingOptions filter can be used."
- `fieldgroups`: `MATCHING_ITEMS` (default), `EXTENDED` (adds `shortDescription`, `itemLocation.city`), plus refinement groups.
- Headers: `X-EBAY-C-MARKETPLACE-ID` (default `EBAY_US`), `X-EBAY-C-ENDUSERCTX` (affiliate + sorting by price accuracy; contextualLocation example `country%3DUS%2Czip%3D19406`).
- Response `SearchPagedCollection`: `itemSummaries`, `total`, `limit`, `offset`, `next`, `prev`, `href`, `refinement`, `warnings`, `autoCorrections`. `ItemSummary` fields include `itemId`, `legacyItemId`, `title`, `price`, `condition`, `conditionId`, `buyingOptions`, `categories`, `leafCategoryIds`, `image`, `thumbnailImages`, `itemWebUrl`, `itemAffiliateWebUrl`, `itemCreationDate`, `itemOriginDate`, `itemEndDate`, `itemLocation`, `seller`, `shippingOptions`, `bidCount`, `currentBidPrice`, `watchCount`.
  - `itemOriginDate`: "will be retained if an item is relisted ... used to sort the response when sort=newlyListed".
  - `watchCount`: "restricted to applications that have been granted permission ... You must submit an App Check ticket".

Filters (`filter=` param), from the filter reference https://developer.ebay.com/api-docs/buy/static/ref-buy-browse-filters.html (raw/ebay-browse-filters.md). VERIFIED:
- `price:[10..50],priceCurrency:USD` ("price ... must be used with the priceCurrency filter"; open-ended `price:[..50]` allowed).
- `conditionIds:{1000|1500}` (numeric codes) and `conditions:{NEW|USED}`.
- `buyingOptions:{FIXED_PRICE|AUCTION|BEST_OFFER|CLASSIFIED_AD}` ("This filter is defined at the leaf category level and should be used with a leaf category ID. If this filter is used with a top-level category ID, it won't work").
- `itemLocationCountry:US`, `deliveryCountry:US`, `deliveryPostalCode`, `maxDeliveryCost:0`, `returnsAccepted:true`, `searchInDescription:true`, `sellers:{a|b}` (max 250), `excludeSellers:{...}`, `excludeCategoryIds:{...}`, `bidCount:[1..5]`, `itemEndDate:[...]`, and `itemStartDate:[2018-11-14T07:47:48Z..]` ("based on the timestamp recorded by eBay the moment the listing became available"). Local pickup radius needs all four `pickup*` filters.
- Combined example: `filter=price:[10..50],priceCurrency:USD,conditions:{USED},buyingOptions:{FIXED_PRICE|AUCTION}`.

Incremental polling pattern (design inference from the above, UNVERIFIED in practice): one saved alert = one call with `q`, one leaf `category_ids`, `filter=itemStartDate:[<lastRunISO>],price:[a..b],priceCurrency:USD`, `sort=newlyListed`, `limit=200`; dedupe on `itemId`.

### 1.2 Does production Browse search need approval? DOCS CONFLICT (not resolved)

Evidence for "open to any keyset":
- Spec: `item_summary/search` carries no Limited Release note (only getItems does). VERIFIED (raw/ebay-spec-browse_api.json).
- Sign-up modal on developer.ebay.com: "New accounts include a free access tier ... No time limit -- always free! 5,000 API calls per day". VERIFIED (raw/ebay-mi-overview.md, same boilerplate on any page).
- Call-limits table lists Browse at "5000 API calls per day" with no gate. VERIFIED (https://developer.ebay.com/develop/api/buy/api_call_limits, raw/ebay-buy-call-limits.md).
- A community post (about 1 year old): "Whilst I still don't have access to the buy API, the browse api seems to work" using client_credentials with scope `https://api.ebay.com/oauth/api_scope`. Anecdote only. https://community.ebay.com/forum/browse-57957/topic/getting-access-to-browse-api-468137/ (raw/ebay-community-browse-access.md).

Evidence for "gated":
- Buy APIs Requirements: "Many of the Buy APIs are a (Limited Release). The use of eBay's Buy APIs in production is intended for eBay partners only. You must apply for production access through the eBay Partner Network ... There is no guarantee that your application for production use of the APIs will be approved." https://developer.ebay.com/api-docs/buy/static/buy-requirements.html (raw/ebay-buy-requirements.md). Process: EPN application, "Within 10 business days, the eBay Partner Network will respond", then a "Buy API Production Access (eBay user ID)" support ticket, then contracts.
- Call-limits table footnote on every Buy API row: "* Buy APIs require an additional license. See the API documentation for details."
- Get Started on a Buying Application, Step 4: "The Application Growth Check is a mandatory step for using restricted Buy APIs in Production." https://developer.ebay.com/develop/get-started/get-started-on-a-buying-application (raw/ebay-get-started-buying.md). It does not say which Buy APIs are "restricted".
- Growth Check page: required to "Increase the API call limits" or "Use restricted APIs in production". https://developer.ebay.com/grow/application-growth-check (quoted in raw/ebay-guide-get-started-with-apis.md).

Conclusion: the docs do not say which side Browse search falls on. Mark UNVERIFIED either way. First action after keys exist: mint a production app token with scope `https://api.ebay.com/oauth/api_scope` and call `item_summary/search?q=vintage lamp&limit=1` once. Success = buy alerts can be an API feature. 403/invalid_scope = fall back to native saved searches (section 6) and/or file the Growth Check / EPN application.

### 1.3 Budget math (derived from the verified 5,000/day limit)

One alert polled every 5 min = 288 calls/day (about 17 alerts inside 5,000). Every 15 min = 96/day (about 52 alerts). Pagination multiplies this only when more than 200 new items appear between polls. Token minting is a separate limit (section 4): cache the 7,200 s app token.

### 1.4 Marketplace Insights API (sold comps)

- Endpoint VERIFIED: `GET https://api.ebay.com/buy/marketplace_insights/v1_beta/item_sales/search`, scope `https://api.ebay.com/oauth/api_scope/buy.marketplace.insights`, client credentials. Description: "retrieves the listings that have ended or been completed in the last 90 days." Filters: `buyingOptions`, `conditionIds`, `conditions`, `itemLocationCountry`, `lastSoldDate`, `price`, `priceCurrency`; sort only by price; limit max 200; 10,000-item cap. (raw/ebay-spec-marketplace_insights_api.json)
- Access: not in the default scope set. License agreement defines "Restricted APIs" as APIs that "provide information about market trends, pricing strategies, sales volumes ... Access is specially granted to select Developers." https://developer.ebay.com/join/api-license-agreement (raw/ebay-api-license-agreement.md, line 90). VERIFIED.
- Anecdotal denials: community thread "I did this and was denied access. They said they no longer provide access besides for major partner" (https://community.ebay.com/forum/talk-to-your-fellow-developers-57970/topic/marketplace-insights-api-access-168586/, raw/ebay-community-mi-access.md). A community quote of an older Buy requirements page said access to "Order API | Offer API | Marketplace Insights API cannot be granted upon request" (raw/ebay-community-browse-access.md); that sentence is NOT on the current page I fetched.
- MI is not in the call-limits tables at all. VERIFIED.
- Verdict: do not plan on it. UNVERIFIED that a request would be refused for Ricky, but the anecdotes and the license definition say expect no.

### 1.5 Buy Feed API

- VERIFIED (raw/ebay-spec-buy_feed_api.json): `https://api.ebay.com/buy/feed/v1`, `GET /file`, `GET /file/{file_id}/download`, `GET /feed_type`, `GET /access`; scope `https://api.ebay.com/oauth/api_scope/buy.item.feed`. "download TSV_GZIP feed files containing eBay items and an hourly snapshot file for a specific category, date, and marketplace." Access per application is `ALLOWED` or `RESTRICTED` per marketplace and L1 category.
- Limits: Feed v1 "75,000 API calls per day"; Feed Beta item/item_group/item_priority "10,000 API calls per day". VERIFIED (raw/ebay-buy-call-limits.md).
- Fit: whole-category catalog dumps, not per-query alerts. Skip. Whether a small dev gets non-RESTRICTED access: UNVERIFIED.

### 1.6 RSS feeds

- Reported dead: the `_rss=1` search URL stopped working for .com in Jan 2023 per seller reports (https://www.valueaddedresource.net/ebay-rss-feed-stores-search/, raw/ebay-vac-rss-feed.md) and "Just talked to eBay support, they 'retired' the feature" (https://www.reddit.com/r/Flipping/comments/ty009f/ebay_rss_feeds_completely_gone/, raw/ebay-reddit-rss-gone.md). Third-party reports from 2022-2023 only.
- Live test today inconclusive: `curl` of `https://www.ebay.com/sch/i.html?...&_rss=1` returned 403 from AkamaiGHost (bot wall, not proof). Status: likely retired, not live-verified. Not an official channel anyway; do not build on it.

### 1.7 License terms that constrain a watch/alert dashboard

From the API License Agreement (https://developer.ebay.com/join/api-license-agreement, raw/ebay-api-license-agreement.md, section 8.1). VERIFIED text:
- Public Display: "When the eBay Content is no longer publicly available, you must delete it from your Application." So ended/sold listings pulled from Browse must be purged from the "watch" store. Do not build a Browse-fed sold-history table.
- "Displayed item listing information may not be more than six (6) hours older than information displayed on the eBay Site ... you will disclose in your Application how much older". Show "as of" timestamps on watch cards, re-poll at least every 6 h.
- Written permission needed for anything enabling "Average selling price or gross merchandise sold for any eBay category" and "site-wide statistics". Per-category average-sold dashboards from eBay data are out.
- Personal data of other users: delete on request or when no longer needed.

## 2. Sell side (our listings, inventory, orders)

### 2.1 Which API for what

| API | Production base | Reads UI-created listings? | Use in 2026 |
|---|---|---|---|
| Sell Inventory | `https://api.ebay.com/sell/inventory/v1` | NO (see 2.2) | Only if listings are created through it. Skip. |
| Sell Fulfillment | `https://apiz.ebay.com/sell/fulfillment/v1` | Spec shows no creation-source restriction. Orders carry `legacyItemId`. Not proven by a live call. | YES for sales/orders |
| Sell Finances | `https://apiz.ebay.com/sell/finances/v1` | order-level, not listing-level | Optional: fees, payouts, net earnings |
| Trading (XML/SOAP) | `https://api.ebay.com/ws/api.dll` (UNVERIFIED host, memory) | YES | Read active/sold listings made in UI |
| Sell Feed | `https://api.ebay.com/sell/feed/v1` | Report is "all of the active listings for a specific seller" | Bulk active-inventory snapshot |

### 2.2 Inventory API only sees what it created (VERIFIED, with the official source)

- eBay KB 5276: "The Inventory API is ONLY compatible with the Inventory API. Meaning if an item was listed using any of the tools available via the UI on eBay.com or was listed using the Trading API, they will not surface using the Inventory API." Fix offered: `bulkMigrateListing`. https://edp.ebay.com/support/kb-article?KBid=5276 (raw/ebay-kb-5276-inventory-no-listings.md).
- `POST /bulk_migrate_listing`: scope `https://api.ebay.com/oauth/api_scope/sell.inventory`; "an array of one to five eBay listing IDs"; requirements: fixed-price only, seller-defined SKU on every item/variation, Business Policies on the listing, postal code or city set. Features like listing-level Buyer Requirements and bold titles survive but "the seller will be completely blocked (in APIs or My eBay) from revising these features/settings once the migration takes place." (raw/ebay-spec-inventory_api.json; also https://developer.ebay.com/api-docs/sell/static/inventory/migrating-listings.html, raw/ebay-inv-migrating-listings.md)
- Overview: "Currently, listings created through the Inventory API cannot be edited through Seller Hub or any other listing platform." https://developer.ebay.com/api-docs/sell/inventory/overview.html (raw/ebay-inv-overview.md). Ricky lists from the eBay app/web, so do not adopt this API.
- Inventory limits (if ever used): `getInventoryItems` limit "Min: 1 Max: 200 Default: 25"; scopes `sell.inventory.readonly` / `sell.inventory`; "2 Million API calls per day".

### 2.3 Fulfillment `getOrders` (VERIFIED, raw/ebay-spec-fulfillment_api.json)

- `GET /sell/fulfillment/v1/order`, scopes `https://api.ebay.com/oauth/api_scope/sell.fulfillment` or `.../sell.fulfillment.readonly`; authorizationCode flow (user token).
- Production server in the spec is `https://apiz.ebay.com{basePath}` with basePath `/sell/fulfillment/v1`. The prose example in the guide (`GET https://api.ebay.com/sell/v1/order?`, raw/ebay-api-sell-fulfillment_api.md line 103) omits `fulfillment` and uses `api.`: that is a doc typo vs the spec. DISCREPANCY: trust the spec (`apiz`), confirm on first live call. (The Browse guide prose has the same kind of typo: `https://api.ebay.com/buy/v1/item_summary/search`, versus the spec's `/buy/browse/v1`.)
- Params: `filter` with `creationdate:[ISO..ISO]`, `lastmodifieddate:[ISO..]`, `orderfulfillmentstatus:{NOT_STARTED|IN_PROGRESS}` (also FULFILLED combos); "If creationdate and lastmodifieddate are both included, only creationdate is used"; `limit` "Maximum: 200 Default: 50" (above 200 errors); `offset`; `orderIds` (max 50, ignores other params); `fieldGroups=TAX_BREAKDOWN`. "By default, when no filters are used this call returns all orders created within the last 90 days." "getOrders can return orders up to two years old."
- `Order` fields: `orderId`, `creationDate`, `lastModifiedDate`, `orderFulfillmentStatus`, `orderPaymentStatus`, `buyer`, `lineItems[]` (`lineItemId`, `legacyItemId`, `sku`, `title`, `quantity`, `lineItemCost`, `total`, `soldFormat`, `listingMarketplaceId`), `pricingSummary`, `paymentSummary`, `totalMarketplaceFee`, `salesRecordReference`.
- Limit: Order resource (all methods) "100,000 API calls per day". Polling `lastmodifieddate:[lastRun..]` every minute is about 1,440/day, trivially inside the limit.
- Digital signatures: required only for EU/UK-domiciled sellers and only for the Finances API and `issueRefund` (https://developer.ebay.com/develop/guides-v2/digital-signatures-for-apis.md, raw/ebay-guide-digital-signatures.md). Not needed for a US seller.

### 2.4 Trading API status in 2026

- Not deprecated as a whole. Deprecation table (https://developer.ebay.com/develop/get-started/api-deprecation-status, raw/ebay-deprecation-status.md) lists only specific Trading items: GeteBayDetails (decommission 2027/03/15), ShoppingCartItemEndingSoon notification (2027/01/11), shipping discount profile calls (2027/01/19), UploadSiteHostedPictures (2026/09/30), and already-decommissioned GetCategories, GetCategoryFeatures, GetAdFormatLeads, ItemMarkedPaid notification event. `GetMyeBaySelling` and `GetSellerList` are not on the list. Finding API and Shopping API were decommissioned 2025/02/04 and replaced by Browse. All VERIFIED.
- `GetMyeBaySelling` returns the My eBay Active, Sold, Unsold, Scheduled lists (raw/ebay-trading-getmyebayselling.md). `GetSellerList`: EntriesPerPage "must be between 1 and 200", date ranges "less than 120 days" (raw/ebay-trading-getsellerlist.md). Call limit "5,000 API calls per day" (raw/ebay-sell-call-limits.md).
- Auth for Trading: eBay's guide says OAuth is recommended and "eBay's older Auth'n'Auth process is still available for older applications" (raw/ebay-guide-authorization.md). OAuth tokens work with Traditional APIs. VERIFIED. Header name for passing the OAuth token to Trading (`X-EBAY-API-IAF-TOKEN`): UNVERIFIED, from memory.
- Cost: XML parsing in Deno (the npm lib `ebay-api` wraps this with `fast-xml-parser`). Only needed if the dashboard must show listing-level data for UI-created listings.

### 2.5 Sell Feed active-inventory report

`POST /sell/feed/v1/inventory_task` with `feedType: LMS_ACTIVE_INVENTORY_REPORT` and optional `filterCriteria.listingFormat` (`AUCTION` or `FIXED_PRICE`): "returns a report that contains price and quantity information for all of the active listings for a specific seller." Scope `sell.inventory` (authorization code). VERIFIED in spec (raw/ebay-spec-feed_api.json). Limit "100,000 API calls per day". Whether it includes UI-created listings in practice, and its column set: UNVERIFIED (spec wording says "all active").

### 2.6 Finances API (optional, sales margin view)

`GET /sell/finances/v1/order_earnings`, `/order_earnings_summary` (scope `sell.finances.earnings.read`), `/transaction`, `/payout`, `/seller_funds_summary` (scope `sell.finances`); "15,000 API calls per day". VERIFIED (raw/ebay-spec-finances_api.json). Gives fees/net per order, useful for real profit on sold items.

## 3. Sold events and notifications

### 3.1 Notification API (REST, push webhooks)

- Base `https://api.ebay.com/commerce/notification/v1`. Methods: `GET/PUT /config`, `POST/GET /destination`, `GET/PUT/DELETE /destination/{destination_id}`, `GET /public_key/{public_key_id}`, `POST/GET /subscription`, `POST /subscription/{id}/test|enable|disable`, `POST /subscription/{id}/filter`, `GET /topic`, `GET /topic/{topic_id}`. VERIFIED (raw/ebay-spec-notification_api.json).
- Delivery: "HTTPS is currently the only supported delivery protocol of all notification topics." "JSON is currently the only supported format." Each topic page: Method "HTTPS webhook (POST)", "Retries 3", header `X-EBAY-SIGNATURE` ("ECC message signature"). Destination endpoint "should use the HTTPS protocol, and it should not contain an internal IP address or localhost"; verification token "between 32 and 80 characters. Allowed characters include alphanumeric characters, underscores (_), and hyphens (-)". VERIFIED.
- Subscription scopes: application subscription = client-credentials token with `https://api.ebay.com/oauth/api_scope`; user subscription = authorization-code token with `https://api.ebay.com/oauth/api_scope/commerce.notification.subscription`. VERIFIED (https://developer.ebay.com/develop/guides-v2/sell-communications-guide.md, raw/ebay-guide-sell-communications.md). Error 195011 returned "if your authorization does not include the list of scopes required for the topic".
- Envelope (from the topic page): `metadata {topic, schemaVersion, deprecated}` and `notification {notificationId, eventDate, publishDate, publishAttemptCount, data}`. VERIFIED.
- Filters: only topics with `filterable: true`; filter = JSON Schema 2020-12 document; created in `PENDING` then reviewed to `ENABLED`. VERIFIED.
- Verification of each delivery: base64-decode `X-EBAY-SIGNATURE`, pass to `GET /public_key/{public_key_id}`, verify the signature over the payload; cache the key ("one-hour is recommended") to avoid burning call limits; eBay ships SDKs (Node: https://github.com/eBay/event-notification-nodejs-sdk) that return 412 on failure. VERIFIED (raw/ebay-guide-account-deletion.md).
- Notification API call limit: "10,000 API calls per day". VERIFIED.

### 3.2 Topic list in 2026 (VERIFIED, https://developer.ebay.com/develop/api/sell/notification_events, raw/ebay-notification-events.md)

The page warns: "Some topics in the Commerce Notification API are restricted and require specific OAuth scopes. Access to these topics is controlled and may only be available to approved partners. To determine the required scope(s) for each topic, use the getTopics method."

- Order Management: `ITEM_MARKED_SHIPPED`, `BUYER_REQUESTED_PURCHASE_QUOTE`, `ORDER_CONFIRMATION`, `PURCHASE_QUOTE_CANCELLATION_ACTIVITY`, `ORDER_CANCELLATION_ACTIVITY`, `ITEM_COMMITMENT_CANCELLATION_ACTIVITY`, `ORDER_RETURN_ACTIVITY`, `ORDER_INQUIRY_ACTIVITY`.
- Listing Management: `ITEM_AVAILABILITY` (note: "available for eBay Partner Network (ePN) partners"), `LISTING_PREVIEW_CREATION_TASK_STATUS`, `LISTING` (created/updated/ended; scope `sell.listing.read`).
- Account Management: `SELLER_STANDARDS_PROFILE_METRICS`, `AUTHORIZATION_REVOCATION`, `FEEDBACK_STAR_RATING`, `MARKETPLACE_ACCOUNT_DELETION`, `SELLER_CUSTOMER_SERVICE_METRIC_RATING`, `AUCTION_ACTIVITY`, `AUCTION_ENDED`, `WATCHLIST_REVISION` (scope `buy.watchlist.read`), `BULK_DATA_TRANSFER_THRESHOLD`.
- Offers and Leads: `OFFER_ACTIVITY`.
- Communication: `BUYER_QUESTION`, `FEEDBACK_LEFT`, `FEEDBACK_RECEIVED`, `NEW_MESSAGE`, `REGULATORY_GUIDELINE`.
- Marketing: `PLA_CAMPAIGN_BUDGET_STATUS`. Inventory Discovery: `ITEM_PRICE_REVISION`, `PRIORITY_LISTING_REVISION`, `ITEM_AVAILABILITY` (the two price/priority topics go to "eBay Partner Network partners").

So the answer to "only MARKETPLACE_ACCOUNT_DELETION or an order/sold topic?": there IS a sold-order topic.

`ORDER_CONFIRMATION` (the sold signal): "Notification sent to seller when buyer completes checkout ... when the buyer completes the checkout process and payment clears for a fixed price or auction listing." Needs the standard scope plus an auth-code token with `https://api.ebay.com/oauth/api_scope/sell.fulfillment` and `.../sell.fulfillment.readonly`. Payload `data`: `user {userId, username}`, `order {orderId, orderLineItems[{orderLineItemId, listingId, quantity}]}`. Thin by design: use `orderId` to call `getOrder` for detail. VERIFIED.
`ITEM_MARKED_SHIPPED` needs scope `commerce.shipping`. `WATCHLIST_REVISION` is the buyer's own watchlist, not "someone watched my listing".
UNVERIFIED: whether a plain, non-partner dev keyset may subscribe to `ORDER_CONFIRMATION`, and whether it fires for listings not created by the app. Only a live `getTopics` / `createSubscription` call settles it (getTopics returns `authorizationScopes`, `status`, `scope`, `filterable`, `supportedPayloads`).

### 3.3 Account-deletion endpoint (mandatory, VERIFIED)

Source: https://developer.ebay.com/develop/guides-v2/marketplace-user-account-deletion.md (raw/ebay-guide-account-deletion.md); keyset note in raw/ebay-guide-get-started-with-apis.md line 228.
- "Before you can use your Production keyset, you must subscribe to or opt out of eBay marketplace account deletion/closure notifications." "New third-party developers ... must subscribe to or opt out ... before they make their first production API call." Non-compliance: "termination of your access to the Developer Tools, and/or reduced access to all or some APIs."
- Opt-out ("Not persisting eBay data" toggle) is only for apps that store no eBay data. A dashboard that stores orders/buyers in Supabase persists data, so plan to implement the endpoint. "failure to provide correct information may result in penalties or having their account disabled."
- Challenge: eBay sends `GET https://<callback_URL>?challenge_code=123`. Respond `200` with `Content-Type: application/json` and `{"challengeResponse":"<hex>"}` where hex = SHA-256 over challengeCode + verificationToken + endpoint, in that exact order (concatenated strings, hex digest). Use a JSON library, not hand-built strings, because a BOM breaks the parse.
- Notification: `POST` with `metadata.topic = MARKETPLACE_ACCOUNT_DELETION`, `data {username, userId, eiasToken}`. Ack with 200/201/202/204 immediately; unacked for 24 h -> endpoint marked down, email, "up to 30 days" to fix or "marked as non-compliant". On receipt, delete that user's data. Setup UI: developer account > Application Keys > Notifications link > "Alerts and Notifications" page (or the REST `destination` + `subscription` flow).
- The endpoint must be public HTTPS and support GET and POST: a Supabase Edge Function URL fits (Supabase hosting of this is a different agent's question).

### 3.4 Legacy Platform Notifications (Trading, SOAP)

- Events relevant: `ItemSold` ("sent to the subscribed seller when an eBay listing ends in a sale"), `FixedPriceTransaction`, `AuctionCheckoutComplete`, `ItemListed`, `ItemRevised`, `ItemClosed`, `ItemUnsold`, `ItemWon`, `WatchedItemEndingSoon`, `ItemAddedToWatchList`. VERIFIED (raw/ebay-trading-notif-event-types.md, raw/ebay-pn-item-sold.md).
- Transport: SOAP/XML POST to a URL you set with `SetNotificationPreferences` (`ApplicationDeliveryPreferences.ApplicationURL`, up to 25 URLs). "Notifications do not count as API calls, and do not count against your daily API call limit." Respond `200 OK`. (https://developer.ebay.com/api-docs/static/platform-notifications-landing.html, raw/ebay-pn-landing.md) VERIFIED.
- GOTCHA, verbatim: "After notification delivery is enabled for your application, eBay will send notifications related to listings that your application has submitted using AddItem, RelistItem, and ReviseItem. ... The application's AppId is then associated with the listing." Because Ricky lists in the eBay app/web, `ItemSold` and `FixedPriceTransaction` very likely never fire for his listings. (Inference from that sentence; not tested.) The guide also says to "verify that you have also configured the periodic polling of GetOrders".
- Verdict: do not use. Poll `getOrders`, optionally add `ORDER_CONFIRMATION` as an accelerator.

## 4. Auth

Source: https://developer.ebay.com/develop/guides/authorization.md (raw/ebay-guide-authorization.md). VERIFIED unless marked.

| Flow | Token | Used for | Lifetime | Mint endpoint limit |
|---|---|---|---|---|
| Client credentials, `grant_type=client_credentials`, `scope=<space-separated, URL-encoded>` | Application token | Browse, Taxonomy, Notification (app subs), Buy Feed, MI | `expires_in: 7200` (2 h) | "1,000 requests/day" |
| Authorization code (`GET https://auth.ebay.com/oauth2/authorize`, then `POST https://api.ebay.com/identity/v1/oauth2/token`, `grant_type=authorization_code`, `redirect_uri` = RuName) | User token + refresh token | Fulfillment, Finances, Inventory, Trading (OAuth), Notification (user subs), Sell Feed | access `expires_in: 7200`; `refresh_token_expires_in: 47304000` (547.5 days, about 18 months) | "10,000 requests/day" |
| Refresh (`grant_type=refresh_token`) | New user access token | all user-token calls | 2 h | "50,000 requests/day" |

- Token request: `POST https://api.ebay.com/identity/v1/oauth2/token`, headers `Content-Type: application/x-www-form-urlencoded`, `Authorization: Basic base64(clientId:clientSecret)`. Sandbox: `https://api.sandbox.ebay.com/identity/v1/oauth2/token`.
- Refresh tokens "can be unexpectedly revoked" (user changes name, revokes consent, eBay revokes), and a scope change forces re-consent. Plan a re-auth screen and an alert when refresh fails. When the refresh token expires (about 18 months) Ricky must re-consent once.
- Design implication: serverless must cache the 2 h app token (1,000 mints/day is plenty if cached, not if minted per invocation) and keep the refresh token in Supabase Vault/secret.
- Scopes by call (all VERIFIED in specs unless noted):
  - Browse search: `https://api.ebay.com/oauth/api_scope` (app).
  - Marketplace Insights: `https://api.ebay.com/oauth/api_scope/buy.marketplace.insights` (app; restricted).
  - Fulfillment getOrders: `.../sell.fulfillment.readonly` or `.../sell.fulfillment` (user).
  - Finances: `.../sell.finances`, `.../sell.finances.earnings.read` (user).
  - Inventory: `.../sell.inventory.readonly`, `.../sell.inventory` (user).
  - Notification subs: `.../commerce.notification.subscription` (user), `.../commerce.notification.subscription.readonly`; topic add-ons: `sell.fulfillment`, `sell.listing.read`, `commerce.shipping`, `buy.watchlist.read`.
  - Which scopes your keyset is allowed to mint: Application Keys page > "OAuth Scopes" / "User Tokens" link. Scopes outside the keyset return `invalid_scope` (seen in the community thread).
- Sandbox vs production: separate keysets and tokens ("it's possible the Sandbox and Production environments support different sets of scopes"). Production keyset is disabled until the account-deletion step (3.3) is done. Sandbox hosts: `api.sandbox.ebay.com`, `auth.sandbox.ebay.com`.
- Consent UX: the user token needs a one-time "Grant Application Access" consent through an RuName redirect URL; build one Edge Function for the redirect callback.
- Trading with OAuth: allowed, Auth'n'Auth legacy still exists (see 2.4).

## 5. Limits and costs

- Program cost: "eBay Developers Program membership is free". VERIFIED (https://developer.ebay.com/develop/guides-v2/get-started-with-ebay-apis.md, raw/ebay-guide-get-started-with-apis.md line 26). Free tier: "No time limit -- always free! 5,000 API calls per day" (sign-up modal, raw/ebay-mi-overview.md). The same modal lists a "Premium access tier available to all members: Developer Technical Support, Higher API call limits, eBay Compatible Application logo"; its price is not stated anywhere I fetched (UNVERIFIED). DTS page calls it "a premium developer service" (raw/ebay-dts.md).
- Selling fees still apply to API listings (same as UI). Not relevant to a read-only dashboard.
- Default call limits, verbatim from https://developer.ebay.com/develop/api/buy/api_call_limits and https://developer.ebay.com/support/api-call-limits (raw/ebay-buy-call-limits.md, raw/ebay-support-call-limits.md), VERIFIED:
  - Browse "All methods except getItems: 5000 API calls per day"; getItems "5000 API calls per day".
  - Notification "10,000 API calls per day".
  - Fulfillment Order resource (all methods) "100,000 API calls per day"; payment_dispute "250,000".
  - Inventory "2 Million API calls per day". Finances "15,000". Account "25,000". Sell Feed "100,000". Taxonomy "5,000". Catalog "10,000". Sell Analytics 100-400/day per resource. Trading "5,000 API calls per day". Identity "5,000".
  - Buy Feed v1 "75,000"; Feed Beta item "10,000". Marketplace Insights: not listed.
  - OAuth mint limits: see section 4.
- Raising limits: "Application Growth Check" is "a free service ... Requesting an Application Growth Check is required if you want to: Increase the API call limits for your application; Use restricted APIs in production". Steps: activate developer support (Profile & Contacts > Activate Support), MyAccount > App Growth Check tab, form with "estimated call peak, both hourly and daily volume, for each of the API calls", needs "a working application that we can test". VERIFIED (raw/ebay-guide-get-started-with-apis.md lines 442-691).
- Approval time for Growth Check: NOT stated in any page I fetched. UNVERIFIED. The only stated SLA is for the separate Buy API EPN application: "Within 10 business days, the eBay Partner Network will respond" (raw/ebay-buy-requirements.md).
- Call-limit scope note: limits are per application (keyset), per day; the exact day boundary/timezone: UNVERIFIED. The Developer Analytics API `getRateLimits` reports live usage (spec: raw/ebay-spec-developer_analytics_api.json, 5,000/day).

## 6. Native eBay features: what we can skip building

Help-center pages on ebay.com were captcha-walled for my fetcher, so the quotes below come from the eBay Canada and UK mirrors of the same help articles and from eBay's own Seller Center page.

| Native feature | What it does (VERIFIED where quoted) | Skip building? |
|---|---|---|
| Saved searches | "We'll send you email alerts when new items matching your search are listed." Save via "Save this search" on results; edit filters such as price, color, listing type; envelope icon toggles email alerts. https://www.ebay.ca/help/buying/search-tips/saved-searches?id=4051 (raw/ebay-help-saved-searches-ca.md). Max number of saved searches, alert frequency, and push (vs email) for saved searches: UNVERIFIED. | Yes for v1 buy alerts. Free, no API approval, covers "keywords + price + condition". Gaps: no webhook into our dashboard, no custom match scoring, no dedupe against our inventory. |
| eBay app push | "Enable real-time push notifications and get information about orders, offers, and auctions"; "updated on price drops, offers, and stock alerts"; sellers "monitor your listed items, keep track of orders". Settings: My eBay > Settings > Notifications. https://pages.ebay.com/push-notifications/ (raw/ebay-pages-push-notifications.md). Exact notification type list (item sold, etc.): UNVERIFIED (the push help article was walled). | Yes for "you sold something" phone alerts. Our dashboard only needs to add cross-channel (Etsy/Shopify/eBay) sold alerts. |
| Seller Hub Reports | Reports tab: "Upload, download, and schedule reports", orders and listings templates, order date range "from 1-90 days", .csv/.xlsx. https://www.ebay.co.uk/help/selling/selling-tools/seller-hub-reports?id=4096 (raw/ebay-help-seller-hub-reports-uk.md). | Yes for ad-hoc sales exports and a CSV fallback if API tokens fail. |
| Seller Hub Product Research (Terapeak) | "Research recent marketplace price trends and real-world sales data ... it's free to all sellers. Find it under the Research tab in Seller Hub." https://www.ebay.com/sellercenter/growth/ebay-research-tools (raw/ebay-sellercenter-research-tools.md). Manual UI, no API found. | Yes. This is the sold-comps substitute for the unavailable Marketplace Insights API. Sourcing Insights needs a Basic-or-above Store subscription. |

Honest take: for pricing a thrifted lamp today, a saved search plus Terapeak in Seller Hub does most of "buy alerts + sold comps" for $0 and zero approval risk. The API-built version earns its keep only for: a single dashboard across Etsy/Shopify/eBay, custom rules (price band per category, exclude sellers), pushing to the phone via our own PWA/web-push, and joining eBay sales with inventory and cost basis.

## 7. Client libraries for Deno / TypeScript

- `ebay-api` (hendt/ebay-api): npm latest `10.0.2` published 2026-10-14; MIT; releases 9.5.1 (Apr) to 10.0.2 (Oct) 2026; GitHub 216 stars, 57 forks, 5 open issues, pushed 2026-10-14, not archived. Wraps RESTful and Traditional APIs, TypeScript, includes Browse, Marketplace Insights, Feed, Inventory, Fulfillment, Notification, Trading. Declares `engines.node >= 22.0.0`, dependencies `axios`, `qs`, `debug`, `fast-xml-parser`. VERIFIED (raw/ebay-npm-ebay-api.json, raw/ebay-gh-hendt-ebay-api.json, raw/ebay-gh-ebay-api-README.md). Maintained.
- Deno test I ran today (local Deno 2.7.13, scratchpad script, no repo files touched): `import eBayApi from "npm:ebay-api@10.0.2"` loaded; `typeof eBay.buy.browse.search`, `eBay.sell.fulfillment.getOrders`, `eBay.sell.inventory.getInventoryItems` = function, `eBay.commerce.notification` and `eBay.trading` = object; a real call to the sandbox with fake credentials returned `invalid_client`, proving the network path works. VERIFIED for local Deno only. Supabase Edge Runtime: UNTESTED.
- Recommendation: the surface here is small (token mint, Browse search, getOrders, notification verify, maybe 2 Trading calls), so plain `fetch` in an Edge Function is lighter than pulling axios and a node>=22 library. Keep `ebay-api` as the escape hatch if Trading XML is needed (it handles XML for you).
- eBay's own Event Notification SDKs exist for Node, Java, .NET, PHP, Go (https://github.com/eBay/event-notification-nodejs-sdk); eBay says OpenAPI specs can generate clients "in one of 40+ supported programming languages" (raw/ebay-join-benefits.md). Deno compatibility of the Node SDK: UNVERIFIED; the verify step is short (base64 header, GET public key, signature check) and can be hand-written after reading the SDK.

## Recommendation

1. Day 0 (no approvals needed): create developer account (free), create a Production keyset, deploy a public HTTPS Supabase Edge Function for the account-deletion challenge + POST (3.3) and register it. This unlocks the keyset. Delete the user data named in each POST.
2. Smoke tests, in this order, each ONE call: (a) client-credentials token with `https://api.ebay.com/oauth/api_scope` then `GET /buy/browse/v1/item_summary/search?q=vintage lamp&limit=1`; (b) `GET /commerce/notification/v1/topic?limit=100` to read real `ORDER_CONFIRMATION` scopes/status. These two calls resolve the two biggest UNVERIFIED items (1.2, 3.2).
3. Sales + inventory (the part that definitely works): one auth-code consent for scopes `sell.fulfillment.readonly`, `sell.finances`/`sell.finances.earnings.read` (optional), `sell.inventory` (only for the Sell Feed report), `commerce.notification.subscription`. Store the refresh token server-side; refresh the 2 h token on demand. Poll `GET https://apiz.ebay.com/sell/fulfillment/v1/order?filter=lastmodifieddate:[<cursor>..]&limit=200` every 1-5 min from a scheduled function; that is the source of truth for "sold" and for the sales chart. Add `ORDER_CONFIRMATION` push only if the topic is open, purely to cut latency to seconds; always reconcile with the poll.
4. Listings/inventory of record for eBay: read via Trading `GetMyeBaySelling` (or the Sell Feed `LMS_ACTIVE_INVENTORY_REPORT`) instead of the Inventory API; our own Supabase `items` table (SKU) remains master across Etsy/Shopify/eBay. Do NOT call `bulkMigrateListing` on real listings (locks features, makes editing in Seller Hub risky).
5. Buy alerts: if smoke test (a) passes, implement alerts as Browse queries on a 15-min cron (about 96 calls/day each; keep total under about 4,000/day to leave headroom): `q`, one leaf `category_ids`, `filter=itemStartDate:[cursor],price:[min..max],priceCurrency:USD,buyingOptions:{FIXED_PRICE|AUCTION},conditions:{USED}`, `sort=newlyListed`, dedupe by `itemId`. Honor the license: purge ended items, stamp "as of", refresh watch cards within 6 h. If (a) fails, use eBay saved searches + app push for v1 and apply for the Growth Check/EPN only if it is worth it.
6. Sold comps: use Seller Hub Product Research manually; store Ricky's own comps notes in our DB (his data, not eBay content). Do not attempt Marketplace Insights, do not build an eBay-derived average-sold-price feature (license 8.1.4).
7. Skip: Inventory API, Platform Notifications (SOAP), Buy Feed, RSS, Marketplace Insights, `ebay-api` npm lib (unless Trading XML becomes necessary), digital signatures (EU/UK only).
8. Day-1 hygiene: cache the 2 h app token (1,000 mints/day cap), cache the notification public key about 1 h, log response headers, watch the deprecation table (https://developer.ebay.com/rss/api-deprecation).

## Open questions

1. Browse search in production with only a standard keyset: allowed or Growth-Check/EPN gated? (1.2) Settled by one live call.
2. Is `ORDER_CONFIRMATION` subscribable on a non-partner keyset, and does it fire for listings created in the eBay app/web? (3.2) Settled by `getTopics` + `createSubscription` + `testSubscription` and one real sale.
3. Does `getOrders` return orders for UI-created listings? Spec shows no restriction and `legacyItemId` mapped to Trading ids, but no live proof. Which host is right, `apiz.ebay.com` (spec) vs `api.ebay.com` (doc prose typo)?
4. Does the Sell Feed `LMS_ACTIVE_INVENTORY_REPORT` include UI-created listings and what columns (SKU, ItemID, title)? Trading `GetMyeBaySelling` is the fallback.
5. Growth Check turnaround time and what volume justifies raising 5,000/day: not published.
6. Price of the "Premium access tier": not published in the pages fetched.
7. Max saved searches, alert cadence, and the exact app push types for sold items: eBay.com help was captcha-walled; confirm in the phone app (My eBay > Settings > Notifications).
8. Trading API OAuth header name and endpoint for Deno `fetch` (from memory only), and whether Supabase Edge Runtime runs `npm:ebay-api` (untested).
9. RSS: likely retired, not live-verified (Akamai 403 to curl).
10. Which eBay account/identity will own the developer keyset (Ricky's seller account vs a business account): affects consent and the deletion-notification "persisting data" answer.

## Raw pages and files fetched (all under `research/dashboard/raw/`, prefix `ebay-`)

Specs: spec-browse_api.json, spec-marketplace_insights_api.json (YAML), spec-inventory_api.json, spec-fulfillment_api.json, spec-notification_api.json, spec-buy_feed_api.json, spec-feed_api.json, spec-finances_api.json, spec-developer_analytics_api.json, spec-taxonomy_api.json.

API/guide pages: api-buy-browse_api.md, api-sell-inventory_api.md, api-sell-fulfillment_api.md, api-sell-notification_api.md, notification-events.md, guide-authorization.md, guide-authorization-html.md, guide-account-deletion.md, guide-sell-communications.md, guide-using-restful.md, using-restful-html.md, guide-digital-signatures.md, guide-get-started-with-apis.md, api-browse-static.md, browse-filters.md, buy-requirements.md, get-started-buying.md, buy-call-limits.md, call-limits.md, sell-call-limits.md, support-call-limits.md, gs-use-app-growth.md, deprecation-status.md, versioning.md, inv-overview.md, inv-migrating-listings.md, kb-5276-inventory-no-listings.md, appseconnect-inv-limit.md, mi-overview.md, join-benefits.md, dts.md, api-license-agreement.md.

Legacy: trading-getsellerlist.md, trading-getmyebayselling.md, trading-notif-event-types.md, pn-landing.md, pn-item-sold.md.

Native, help, community: help-saved-searches-ca.md, help-saved-searches-uk.md, help-seller-hub-reports-uk.md, pages-push-notifications.md, sellercenter-research-tools.md, vac-rss-feed.md, reddit-rss-gone.md, reddit-mi-access.md, community-mi-access.md, community-browse-access.md.

Libraries: npm-ebay-api.json, gh-hendt-ebay-api.json, gh-ebay-api-README.md.
