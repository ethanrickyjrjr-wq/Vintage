# Contract sheet: vendor surfaces for the Hollywood and Vine dashboard

Date: 2026-10-26. Author: verification agent. Scope: every endpoint, header, scope, algorithm, limit and price the build copies. Nothing built.
Paths: `raw/` = `research/dashboard/raw/`. Rule of the house (Vendor First): copy only values in this sheet; anything marked UV gets a smoke test before code depends on it.

## Status legend

- **VD** = VERIFIED-doc. Read today (2026-10-26) in a fetched vendor page, OpenAPI spec, source file or registry response. The raw copy is named in the row or in the evidence index.
- **VL** = VERIFIED-live. Observed today in a live call. The row says what the call proves. A call made with an invalid token proves routing and error shape, not access.
- **UV** = UNVERIFIED. Memory, inference, anecdote, or not reachable without Ricky's credentials.

No eBay, Etsy, Shopify, Pushover or Supabase credentials exist in `.env.local` (names checked, values not read), so no authenticated call was made. Live probes used invalid or no credentials: eBay API hosts, eBay token endpoint, Etsy hosts, Pushover, ntfy.sh (one throwaway topic), Healthchecks, public npm, and Shopify's unauthenticated schema proxy.

## 0. Where this sheet overrides the brief or wave-1 reports

1. eBay marketplace header is `X-EBAY-C-MARKETPLACE-ID` (hyphens). The brief wrote an underscore. VD, 12 hits in the Browse spec, no underscore variant in any fetched page.
2. `getOrders` host is `https://api.ebay.com/sell/fulfillment/v1/order`. Report 01 said trust the spec's `apiz`. Live routing probe says the opposite (A1).
3. eBay notification signature is ECDSA over SHA-1 (`ssl3-sha1` in the SDK) and the key is fetched by `kid` taken from the base64-decoded JSON header. eBay's SDK verifies over `JSON.stringify(parsedBody)`; whether eBay signs the raw bytes is UV (A5.4).
4. `net.http_post` argument order is `url, body, params, headers, timeout_milliseconds`. Use named arguments (D).
5. Etsy money fields are `Money {amount, divisor, currency_code}`, value = `amount / divisor`. The prose "A number equal to..." in the spec is wrong for the wire format (B3).
6. Every inbound webhook receiver (eBay, Etsy, Shopify) must be a Supabase function with `verify_jwt = false` and `auth: 'none'`, then verify the vendor's own signature (D).
7. Etsy `webhook-signature` is most likely `v1,<base64>` and space-delimited (Standard Webhooks). Etsy's page does not say so. Handle both (B4).
8. Healthchecks answers HTTP 200 to a ping for a check that does not exist. Read the body (E3).
9. Shopify `webhookSubscriptionCreate` takes `uri` in 2026-10; there is no `callbackUrl` (C3).
10. ntfy.sh free daily cap is 250 messages (VD). Report 05 had it as unverified.

---

## A. eBay

### A1. Hosts and routing

Method: `GET` with `Authorization: Bearer invalid` against both `api.ebay.com` and `apiz.ebay.com`. Reading: 401 "Invalid access token" = the route exists on that host; 404 "Resource not found" = it does not. Raw: `raw/contract-probe-ebay-hosts.md`.

| Surface | Verbatim value | Status | URL |
|---|---|---|---|
| OAuth token endpoint | `POST https://api.ebay.com/identity/v1/oauth2/token` | VD + VL (bad client returns 401 `{"error":"invalid_client","error_description":"client authentication failed"}`; raw/contract-probe-ebay-token.md) | https://developer.ebay.com/develop/guides/authorization |
| Authorize page (user consent) | `GET https://auth.ebay.com/oauth2/authorize` | VD (spec `authorizationUrl`); VL: host answers 302 | https://developer.ebay.com/develop/api/spec/notification_api.json |
| Browse search | `https://api.ebay.com/buy/browse/v1/item_summary/search` | VD + VL: api=401, apiz=404 | https://developer.ebay.com/develop/api/spec/browse_api.json |
| Fulfillment getOrders | `https://api.ebay.com/sell/fulfillment/v1/order` | VL only: api=401, apiz=404. The spec says apiz (see Conflicts #1) | https://developer.ebay.com/develop/api/spec/fulfillment_api.json |
| Fulfillment payment_dispute (not needed) | `https://apiz.ebay.com/sell/fulfillment/v1/payment_dispute_summary` | VL: apiz=401, api=404 | same spec |
| Finances (optional) | `https://apiz.ebay.com/sell/finances/v1/transaction` | VD + VL: apiz=401, api=404 | https://developer.ebay.com/develop/api/spec/finances_api.json |
| Notification API | `https://api.ebay.com/commerce/notification/v1` | VD + VL: api=401, apiz=404 | https://developer.ebay.com/develop/api/spec/notification_api.json |
| Sell Feed / Inventory | `https://api.ebay.com/sell/feed/v1/inventory_task`, `https://api.ebay.com/sell/inventory/v1/inventory_item` | VL routing: both api=401 | specs in raw/ebay-spec-feed_api.json, raw/ebay-spec-inventory_api.json |

### A2. OAuth

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Client-credentials request | `POST /identity/v1/oauth2/token`; headers `Content-Type: application/x-www-form-urlencoded`, `Authorization: Basic base64(client_id:client_secret)`; body `grant_type=client_credentials&scope=<URL-encoded space-separated scopes>` | VD | https://developer.ebay.com/develop/guides/authorization (raw/ebay-guide-authorization.md) |
| Client-credentials response | `{"access_token":"v^1.1#i^1#p^1#r^0#I^3#f^0#t^H4s ... wu67e3xAhskz4DAAA","expires_in":7200,"token_type":"Application Access Token"}` | VD (doc example) | same |
| Browse scope | `https://api.ebay.com/oauth/api_scope` ("View public data from eBay") | VD (spec `securitySchemes`, per-operation `security`) | https://developer.ebay.com/develop/api/spec/browse_api.json |
| Auth-code consent URL | `GET https://auth.ebay.com/oauth2/authorize?client_id=<id>&redirect_uri=<RuName>&response_type=code&scope=<URL-encoded scopes>&state=<opaque>` (optional `locale`, `prompt=login`). `redirect_uri` is the RuName value eBay generates, not a URL | VD (guide shows the sandbox host; production host from spec) | raw/ebay-guide-authorization.md |
| Auth-code exchange | `POST /identity/v1/oauth2/token`, same headers; body `grant_type=authorization_code&code=<URL-encoded code>&redirect_uri=<RuName>` | VD | same |
| Auth-code response | `{"access_token":"v^1.1#...","expires_in":7200,"refresh_token":"v^1.1#...","refresh_token_expires_in":47304000,"token_type":"User Access Token"}` (47,304,000 s = 547.5 days, about 18 months) | VD (doc example) | same |
| Refresh request | body `grant_type=refresh_token&refresh_token=<token>&scope=<scopes>`. `scope` optional; if sent it must equal or be a subset of the consented scopes | VD | same |
| Refresh response | `{"access_token":"v^1.1#...","expires_in":7200,"token_type":"User Access Token"}` (no new refresh token returned) | VD | same |
| Refresh revocation | "if a seller changes their eBay member log-in name or the password for their eBay account, any active refresh tokens associated with the account will be automatically revoked by eBay. In addition, sellers can choose to revoke a token themselves" | VD | same |
| Scope change | "if you update the scopes needed by your app, you must update both the access token and the refresh token, starting with Getting the third-party consent" | VD | same |
| getOrders scope | `https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly` (or `.../sell.fulfillment`) | VD (spec `/order` security) | https://developer.ebay.com/develop/api/spec/fulfillment_api.json |
| Notification subscription scopes | user-based subscription: `https://api.ebay.com/oauth/api_scope/commerce.notification.subscription` (read-only variant `...subscription.readonly`); application-based: `https://api.ebay.com/oauth/api_scope` via client-credentials | VD | https://developer.ebay.com/develop/guides-v2/sell-communications-guide |
| ORDER_CONFIRMATION extra scopes | "In addition to the standard OAuth scope (https://api.ebay.com/oauth/api_scope), this topic requires an access token created using the Authorization Code Grant flow with the following scopes: .../sell.fulfillment, .../sell.fulfillment.readonly". So the one consent request carries: `api_scope`, `commerce.notification.subscription`, `sell.fulfillment`, `sell.fulfillment.readonly` | VD | https://developer.ebay.com/develop/api/sell/notification_events |
| Token-mint limits (per app, per day) | client credentials "1,000 requests/day"; authorization code "10,000 requests/day"; refresh "50,000 requests/day" | VD | https://developer.ebay.com/develop/guides/authorization (raw/ebay-guide-authorization.md, lines 310-335; same numbers in raw/sourcing-ebay-oauth-rate-limits.md) |

### A3. Browse `item_summary/search`

Request, with every value from the spec (URL-encode parameter values; the docs leave examples unencoded "for readability"):

```
GET https://api.ebay.com/buy/browse/v1/item_summary/search
    ?q=vintage lamp
    &category_ids=<ONE leaf category id>
    &filter=price:[10..80],priceCurrency:USD,conditions:{USED},buyingOptions:{FIXED_PRICE|AUCTION},itemStartDate:[2026-10-26T00:00:00.000Z..],itemLocationCountry:US
    &sort=newlyListed&limit=200&offset=0
Authorization: Bearer <application token>
X-EBAY-C-MARKETPLACE-ID: EBAY_US
```

Composition of the full filter string is UV (each filter is VD; the spec's own combined example is `filter=price:[10..50],sellers:{rpseller|bigSal}`).

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Headers | `X-EBAY-C-MARKETPLACE-ID` "identifies the seller's eBay marketplace. It is required for all marketplaces outside of the US ... If the marketplace ID value is invalid or missing, the default value of `EBAY_US` is used." Optional `X-EBAY-C-ENDUSERCTX` (affiliate revenue sharing, price-sort accuracy: `contextualLocation=country%3DUS%2Czip%3D19406`). Optional `Accept-Language` | VD | raw/ebay-spec-browse_api.json |
| `q` | "Maximum length: 100 characters"; space = AND; `(iphone, ipad)` = OR; "The `*` wildcard character is not allowed in this field" | VD | same |
| `category_ids` | "Currently, you can pass in only one category ID per request." | VD | same |
| `limit` / `offset` | limit "Min: 1 Max: 200 Default: 50"; offset "Min: 0 Max: 9,999 Default: 0", "must be either zero or a multiple of the `limit` value"; "This method can return a maximum of 10,000 items in one results set." | VD | same |
| `sort` | `price`, `-price`, `distance`, `newlyListed` ("sorted based on their `itemOriginDate`"), `endingSoonest`; default Best Match | VD | same |
| `fieldgroups` | default `MATCHING_ITEMS`; `EXTENDED` "adds the following fields to the response: shortDescription itemLocation.city" | VD | same |
| Default result set | "Only listings where `FIXED_PRICE` (Buy It Now) is a buying option are returned by default. To retrieve listings that do not have `FIXED_PRICE` as a buying option, the `buyingOptions` filter can be used" (an auction that gets a bid drops FIXED_PRICE) | VD | same |
| Filter `price` | `filter=price:[10..50]` or open-ended `price:[..50]`, "**must** be used with the **priceCurrency** filter": `filter=price:[50..500],priceCurrency:USD` | VD | https://developer.ebay.com/api-docs/buy/static/ref-buy-browse-filters.html |
| Filter `conditions` | `filter=conditions:{NEW\|USED}`; valid values (case sensitive) NEW, USED, UNSPECIFIED. For specific grades use `conditionIds:{1000\|1500}` | VD | same |
| Filter `buyingOptions` | `filter=buyingOptions:{FIXED_PRICE\|BEST_OFFER}`; values FIXED_PRICE, AUCTION, BEST_OFFER, CLASSIFIED_AD. "This filter is defined at the leaf category level and should be used with a leaf category ID. If this filter is used with a top-level category ID, it won't work" | VD | same |
| Filter `itemStartDate` | `filter=itemStartDate:[2018-11-14T07:47:48Z..2018-12-14T07:47:48Z]`; start-only form `[<start>]` or `[<start>..]`; "based on the timestamp recorded by eBay the moment the listing became available"; UTC ISO 8601 `yyyy-MM-ddThh:mm:ss.sssZ`. The open-ended example lines on the page say `itemEndDate` by mistake (copy-paste typo) | VD | same |
| Filter `itemLocationCountry` | `filter=itemLocationCountry:US`; "Only one country code value can be used"; two-character ISO 3166, case sensitive; ignored with `pickup*` filters; error if combined with `itemLocationRegion` | VD | same |
| Response envelope | `SearchPagedCollection`: `href`, `total`, `limit`, `offset`, `next`, `prev`, `itemSummaries[]`, `refinement`, `warnings`, `autoCorrections` | VD | spec |
| Response fields stored | `itemId` string ("unique RESTful identifier"; also `legacyItemId`); `title` (max 80 chars); `price.value` string + `price.currency` (ConvertedAmount, plus `convertedFromValue`/`convertedFromCurrency` when converted); `condition` string (text, e.g. New/Used) + `conditionId` string; `itemWebUrl`; `image.imageUrl`; `itemEndDate` (UTC, scheduled end); `buyingOptions[]`; `seller.username` (+ `feedbackScore`, `feedbackPercentage`); `itemLocation` {`country`, `postalCode` (anonymized), `stateOrProvince`, `city` only with `fieldgroups=EXTENDED`}; `itemCreationDate` ("always returned"); `itemOriginDate` ("retained if an item is relisted") | VD | spec |
| `seller.username` caveat | "Effective September 26, 2025, select developers will no longer receive username data for U.S. users through this field. Instead, an immutable user ID will be returned in its place." The linked page scopes this to "API users in China (and its territories), Russia, North Korea, Cuba, Iran, and Venezuela" and adds that "only a certain amount of unique user data can be retrieved over a given time period" for U.S. usernames. Treat the field as an opaque id | VD | https://developer.ebay.com/api-docs/static/data-handling-update.html (raw/contract-ebay-data-handling-update.md) |
| Production access for this call | **Docs conflict, not resolved** (Conflicts #4). Needs the first smoke test | UV | see Conflicts |
| `watchCount` | "restricted to applications that have been granted permission" | VD | spec |

### A4. Sell Fulfillment `getOrders`

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Request | `GET https://api.ebay.com/sell/fulfillment/v1/order?filter=lastmodifieddate:[2026-10-26T00:00:00.000Z..]&limit=200&offset=0` with a user token (`sell.fulfillment.readonly`). Percent-encode `[` `%5B`, `]` `%5D`, `{` `%7B`, `\|` `%7C`, `}` `%7D` | host VL, rest VD | https://developer.ebay.com/develop/api/sell/fulfillment_api (raw/ebay-api-sell-fulfillment_api.md) |
| `filter` grammar | `creationdate:[<ISO>..<ISO>]`, `lastmodifieddate:[<ISO>..]` ("identifies orders modified on or after the given timestamp"), `orderfulfillmentstatus:{NOT_STARTED\|IN_PROGRESS}` or `{FULFILLED\|IN_PROGRESS}` (only these combinations). "If creationdate and lastmodifieddate are both included, only creationdate is used." Timestamps ISO 8601 UTC | VD | spec |
| Defaults / windows | "By default, when no filters are used this call returns all orders created within the last 90 days." "getOrders can return orders up to two years old." | VD | spec |
| Pagination | `limit` "Maximum: 200 Default: 50" ("If a requested limit is more than 200, the call fails and returns an error"); `offset` zero-based; response `total`, `limit`, `offset`, `next`, `prev`, `href`, `warnings`, `orders[]`. `orderIds` (max 50) overrides all other params | VD | spec |
| Order fields stored | `orderId`; `creationDate`, `lastModifiedDate` (ISO UTC, e.g. `2015-08-04T19:09:02.768Z`); `orderFulfillmentStatus` = FULFILLED \| IN_PROGRESS \| NOT_STARTED; `orderPaymentStatus` = FAILED \| FULLY_REFUNDED \| PAID \| PARTIALLY_REFUNDED \| PENDING; `pricingSummary.total` (Amount {value string, currency}); `totalMarketplaceFee` (Amount); `buyer.username`; `salesRecordReference` | VD | spec |
| Line item fields stored | `lineItems[].lineItemId`, `.legacyItemId` ("legacy listing item ID"), `.title` (the item id appears here instead of the title if the listing is on hold for a policy violation), `.sku`, `.quantity`, `.lineItemCost` (Amount, selling price before discounts, price x quantity), `.total`, `.soldFormat` = AUCTION \| FIXED_PRICE \| OTHER \| SECOND_CHANCE_OFFER | VD | spec |
| Gotcha | "In this call, the `cancelStatus.cancelRequests` array is returned but is always empty. Use the `getOrder` call instead" | VD | spec |
| `buyer.username` caveat | same username-replacement note as A3 | VD | data-handling page |
| Does it return orders for listings made in the eBay app/web? | spec shows no creation-source filter; no live proof | UV | |

### A5. Notification API

**A5.1 Setup order.** Tokens: `/config`, `/destination`, `/topic` and `/public_key` calls take the client-credentials application token (`api_scope`). `createSubscription` for `ORDER_CONFIRMATION` must use the user (authorization-code) token carrying `commerce.notification.subscription` plus `sell.fulfillment` and `sell.fulfillment.readonly`; an application token there gives an application-scope subscription or error 195011. (a) `PUT /config` body `{"alertEmail":"<email>"}` returns 204. (b) `POST /destination` body `{"name":"<name>","status":"ENABLED","deliveryConfig":{"endpoint":"https://<public https url>","verificationToken":"<32-80 chars of [A-Za-z0-9_-]>"}}` returns 201 with the new id in the `Location` header; eBay immediately sends the challenge GET (A5.3). (c) `GET /topic/{topic_id}` to read scopes, status, `supportedPayloads[].schemaVersion`. (d) `POST /subscription` body `{"topicId":"ORDER_CONFIRMATION","destinationId":"<id>","status":"ENABLED","payload":{"deliveryProtocol":"HTTPS","format":"JSON","schemaVersion":"<from getTopic>"}}` returns 201 with `Location`; error 195011 "if your authorization does not include the list of scopes required for the topic". (e) `POST /subscription/{id}/test` returns 202 with a mocked payload; "Use the notificationId to tell the difference between a test payload and a real payload." Status: field names VD (spec `DestinationRequest`, `DeliveryConfig`, `CreateSubscriptionRequest`, `SubscriptionPayloadDetail`, `Config`); the `schemaVersion` value is UV until `getTopic` is called.

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Enums | `DestinationStatusEnum` ENABLED, DISABLED, MARKED_DOWN (eBay-set only); `SubscriptionStatusEnum` ENABLED, DISABLED; `ProtocolEnum` HTTPS; `FormatTypeEnum` JSON; topic `status` ENABLED, DISABLED, DEPRECATED; topic `scope` APPLICATION, USER | VD | https://developer.ebay.com/develop/api/spec/notification_api.json |
| Endpoint rules | "should use the HTTPS protocol, and it should not contain an internal IP address or localhost in its path"; "HTTPS is currently the only supported delivery protocol"; "JSON is currently the only supported format" | VD | spec, account-deletion guide |
| Topic ids | `ORDER_CONFIRMATION`, `MARKETPLACE_ACCOUNT_DELETION` (both listed). `ORDER_CONFIRMATION`: "sent to a seller when the buyer completes the checkout process and payment clears for a fixed price or auction listing" | VD | https://developer.ebay.com/develop/api/sell/notification_events |
| Delivery | "Method: HTTPS webhook (POST)"; "Retries: 3"; header `X-EBAY-SIGNATURE` ("The ECC message signature. This signature is used to process and validate the message payload.") | VD | same |
| Envelope (all topics) | `{"metadata":{"topic","schemaVersion","deprecated"},"notification":{"notificationId","eventDate","publishDate","publishAttemptCount","data":{...}}}` | VD | same |
| `ORDER_CONFIRMATION` `data` | `{"user":{"userId","username"},"order":{"orderId","orderLineItems":[{"orderLineItemId","listingId","quantity"}]}}`. Thin: call `getOrder`/`getOrders` for the money fields | VD | same |
| `MARKETPLACE_ACCOUNT_DELETION` `data` | `{"username","userId","eiasToken"}`; sample envelope has `"topic":"MARKETPLACE_ACCOUNT_DELETION","schemaVersion":"1.0"` | VD | https://developer.ebay.com/develop/guides-v2/marketplace-user-account-deletion |
| Can a non-partner keyset subscribe to `ORDER_CONFIRMATION`, and does it fire for UI-made listings? | The topics page warns "Some topics ... are restricted and require specific OAuth scopes. Access to these topics is controlled and may only be available to approved partners." | UV | smoke test 2 |

**A5.2 Ack.** Respond fast with `200 OK`, `201`, `202` or `204` (deletion guide; the SDK returns `204` on success and `412 Precondition Failed` when the signature fails). Unacked for 24 h: callback "marked down", alert email; "up to 30 days" to fix or "marked as non-compliant". VD.

**A5.3 Account-deletion challenge (mandatory before the production keyset works).** VD, https://developer.ebay.com/develop/guides-v2/marketplace-user-account-deletion (raw/ebay-guide-account-deletion.md) and eBay's SDK `lib/validator.js`.

| Item | Verbatim value |
|---|---|
| Request | `GET https://<callback_URL>?challenge_code=123` |
| Hash | SHA-256 over the three strings in this order: `challengeCode + verificationToken + endpoint`; hex digest. SDK: `createHash('sha256'); update(challengeCode); update(verificationToken); update(endpoint); digest('hex')` |
| `endpoint` | the exact URL string registered with eBay. Store it in a secret; do not rebuild it from `req.url` inside the function (it may not equal the public URL) |
| Response | `200 OK`, header `Content-Type: application/json`, body `{"challengeResponse":"<64 hex chars>"}` |
| Gotcha | "We strongly advise that implementations use a JSON library to create their response body ... a byte order mark (BOM) is often prepended" |
| Verification token | "between 32 and 80 characters ... alphanumeric characters, underscore (_), and hyphen (-)" |

**A5.4 Signature verification of every POST (VD from eBay's own SDK; account-deletion and communications guides are incomplete).** Source: https://github.com/eBay/event-notification-nodejs-sdk (`lib/validator.js`, `lib/client.js`, `lib/constants.js`; copies in `raw/contract-gh-ebay-notif-sdk-*`). Algorithm check: `raw/contract-probe-ebay-ecdsa-selftest.md`.

1. Header name `x-ebay-signature` (HTTP headers are case-insensitive).
2. Base64-decode the header, `JSON.parse` it: an object with `kid` and `signature` (the SDK reads exactly those two keys; any other keys, e.g. an algorithm or digest name, are UV).
3. `GET https://api.ebay.com/commerce/notification/v1/public_key/{kid}` with `Authorization: Bearer <application token>` (scope `https://api.ebay.com/oauth/api_scope`). Response `{"algorithm":"...","digest":"...","key":"..."}` (spec text: "such as Elliptic Curve Digital Signature Algorithm (ECDSA)" and "such as Secure Hash Algorithm 1 (SHA1)"). Cache by `kid`; eBay: "one-hour is recommended".
4. PEM = `-----BEGIN PUBLIC KEY-----\n` + `key` + `\n-----END PUBLIC KEY-----` (the SDK regex-inserts the header and footer around the returned string).
5. `crypto.createVerify('ssl3-sha1')`, `update(JSON.stringify(parsedBody))`, `verify(PEM, signature, 'base64')` (signature is DER). True = deliver; false = respond 412.
6. Under Deno: `node:crypto` does this unchanged (VL self-test, local Deno 2.7.13, generated P-256 key). `crypto.subtle` `{name:"ECDSA",hash:"SHA-1"}` works only with a raw r\|\|s (P1363) signature; a DER signature returns false.

Not verified: eBay's real key curve; whether eBay signs the raw bytes or the re-serialised JSON (try raw body first, then `JSON.stringify(JSON.parse(raw))`); `node:crypto` `ssl3-sha1` inside the Supabase Edge Runtime. UV.

### A6. eBay limits (verbatim)

| API | Default limit | Status | URL |
|---|---|---|---|
| Browse, all methods except getItems | "5000 API calls per day" (row carries "* Buy APIs require an additional license. See the API documentation for details.") | VD | https://developer.ebay.com/develop/api/buy/api_call_limits |
| Notification | "10,000 API calls per day" | VD | https://developer.ebay.com/support/api-call-limits |
| Fulfillment, Order resource (all methods) | "100,000 API calls per day" | VD | same |
| Finances | "15,000 API calls per day" | VD | same |
| Sell Feed | "100,000 API calls per day" | VD | same |
| Inventory | "2 Million API calls per day" | VD | same |
| Trading | "5,000 API calls per day" | VD | same |
| Taxonomy / Identity | "5,000 API calls per day" each | VD | same |
| Developer Analytics (`getRateLimits`) | "5,000 API calls per day" | VD | same |
| OAuth mint | see A2 | VD | |
| Raising limits | "Application Growth Check" is free; required to "Increase the API call limits" or "Use restricted APIs in production"; turnaround not published | VD / UV | https://developer.ebay.com/develop/get-started/get-started-on-a-buying-application |

---

## B. Etsy

### B1. App tier and base

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Tier | Seller App: "Individual sellers building for their own shop"; "Eligible sellers are approved within minutes"; scoped "only to your registered shop"; register at https://www.etsy.com/developers/register-seller-app | VD | https://developers.etsy.com/documentation/ |
| API host | `https://api.etsy.com/v3/...` (docs, quickstart, webhook `resource_url`). The OpenAPI file says `https://openapi.etsy.com`; VL: both hosts return the identical 403 for a bad key on `/v3/application/openapi-ping` and `/v3/public/oauth/token` | VD + VL | raw/contract-probe-etsy-hosts.md |
| Required header on every call | `x-api-key: <keystring>:<shared_secret>` (colon-separated). Example from the page: `x-api-key: 1aa2bb33c44d55eeeeee6fff:a1b2c3d4e5`. VL: bad key returns 403 `{"error":"API key not found or not active, or incorrect shared secret for API key."}` | VD + VL | https://developers.etsy.com/documentation/essentials/authentication |
| Auth header on scoped calls | `Authorization: Bearer <access_token>` where the token is `<user_id>.<token>`; quickstart: "Scoped endpoints require a bearer token ... Authorization:`Bearer ${access_token}`" | VD | https://developers.etsy.com/documentation/tutorials/quickstart |

### B2. OAuth 2.0 with PKCE

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Authorize | `GET https://www.etsy.com/oauth/connect?response_type=code&client_id=<keystring>&redirect_uri=<https URL>&scope=<space-separated, URL-encoded>&state=<opaque>&code_challenge=<challenge>&code_challenge_method=S256`. `redirect_uri` must be `https://`, exact match to the one registered | VD | https://developers.etsy.com/documentation/essentials/authentication |
| PKCE | verifier 43 to 128 chars from `[A-Za-z0-9._~-]`; challenge = URL-safe base64 of SHA-256(verifier). "The Etsy Open API requires a PKCE on every authorization flow request." | VD | same |
| Token exchange | `POST https://api.etsy.com/v3/public/oauth/token`, `application/x-www-form-urlencoded`: `grant_type=authorization_code`, `client_id`, `redirect_uri` (optional), `code`, `code_verifier` | VD | same |
| Token response | `{"access_token":"12345678.<token>","token_type":"Bearer","expires_in":3600,"refresh_token":"12345678.<token>"}` | VD | same |
| Lifetimes | access token "has a functional life of 1 hour" (`expires_in: 3600`); refresh token "has a longer functional lifetime (90 days)" | VD | same |
| Refresh | `POST https://api.etsy.com/v3/public/oauth/token`: `grant_type=refresh_token`, `client_id`, `refresh_token`. Response carries a `refresh_token`; persist the newest every time. Prose bullet on the same page says `grant_type=refresh_code` (Conflicts #6). VL could not discriminate (bad key rejected first) | VD; wire value UV | same |
| Scope strings (complete list) | `address_r address_w email_r listings_d listings_r listings_w profile_r profile_w shops_r shops_w transactions_r transactions_w` | VD | same + OpenAPI `securitySchemes.oauth2` |
| Scopes per endpoint used | receipts: `transactions_r`; `getListingsByShop`: `listings_r`; `findAllActiveListingsByShop`, `getListing`, `getListingImages`: none (api key only); `getMe`: `shops_r`; `getListingInventory`: `listings_r` | VD | https://www.etsy.com/openapi/generated/oas/3.0.0.json |

### B3. Endpoints and stored fields

All VD from the OpenAPI file unless noted. Money fields are objects: `{"amount": <int>, "divisor": <int>, "currency_code": "USD"}`; value = `amount / divisor`. Collections return `{"count": <int>, "results": [...]}`.

| Call | Verbatim path and params | Notes |
|---|---|---|
| `getShopReceipts` | `GET /v3/application/shops/{shop_id}/receipts` params `min_created`, `max_created`, `min_last_modified`, `max_last_modified` (integer unix seconds, minimum 946684800), `limit` (1 to 100, default 25), `offset` (default 0), `sort_on` created\|updated\|receipt_id (default created), `sort_order` asc\|ascending\|desc\|descending\|up\|down (default desc), `was_paid`, `was_shipped`, `was_delivered`, `was_canceled` (booleans), `legacy` | scope `transactions_r` |
| `getShopReceipt` | `GET /v3/application/shops/{shop_id}/receipts/{receipt_id}` | webhook `resource_url` target |
| `ShopReceipt` stored fields | `receipt_id`, `status` ("One of: `paid`, `completed`, `open`, `payment processing` or `canceled`"), `is_paid`, `is_shipped`, `create_timestamp` and `created_timestamp` (both exist, epoch seconds), `update_timestamp` and `updated_timestamp`, `grandtotal`, `subtotal`, `total_price`, `total_shipping_cost`, `total_tax_cost`, `discount_amt` (all Money), `buyer_user_id`, `seller_user_id`, `transactions[]`, `shipments[]`, `refunds[]`; `buyer_email` is null unless access is approved case by case | |
| `ShopReceiptTransaction` | `transaction_id`, `listing_id`, `product_id`, `title`, `sku`, `quantity`, `price` (Money), `shipping_cost` (Money), `paid_timestamp`, `shipped_timestamp`, `receipt_id`, `buyer_user_id` | |
| `getListingsByShop` | `GET /v3/application/shops/{shop_id}/listings` params `state` (active\|inactive\|sold_out\|draft\|removed\|expired, default `active`), `limit` (1 to 100, default 25), `offset`, `sort_on` created\|price\|updated\|score (works "only when combined with one of the search options"), `sort_order`, `includes` (Shipping, Shop, Images, User, Translations, Videos, Inventory ...) | scope `listings_r`; response `ShopListingsWithAssociations` |
| `findAllActiveListingsByShop` | `GET /v3/application/shops/{shop_id}/listings/active` params `limit`, `offset`, `keywords`, `sort_on`, `sort_order` (no `state`) | no OAuth needed |
| `getListingImages` | `GET /v3/application/listings/{listing_id}/images` | no OAuth; `ListingImage`: `listing_image_id`, `rank`, `url_75x75`, `url_170x135`, `url_570xN`, `url_fullxfull`, `full_height`, `full_width`, `alt_text` |
| `ShopListing` stored fields | `listing_id`, `title`, `state`, `quantity`, `url`, `price` (Money; "the minimum possible price"), `taxonomy_id`, `creation_timestamp` and `created_timestamp`, `last_modified_timestamp` and `updated_timestamp`, `state_timestamp`, `has_variations` | |
| `getMe` / shop id | `GET /v3/application/users/me` (`shops_r`) then `GET /v3/application/users/{user_id}/shops` | |
| Ping | `GET /v3/application/openapi-ping` | VL: reachable on api.etsy.com |
| Quantity-1 detail | a listing with quantity 0 moves to `state` = `sold_out`. Whether it can be restocked in place: UV | |

### B4. Webhooks

Source: https://developers.etsy.com/documentation/essentials/webhooks/ (raw/etsy-shopify-etsy-webhooks.md), plus https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md (raw/contract-standard-webhooks-spec.md) for the header format.

| Item | Verbatim value | Status |
|---|---|---|
| Events | `order.paid`, `order.canceled`, `order.shipped`, `order.delivered`; `listing.created`, `listing.updated`, `listing.deleted`; `inventory.created`, `inventory.updated`, `inventory.deleted`, `inventory.out_of_stock` ("delivered when a product's quantity reaches 0"). `inventory.updated` fires on `Price`, `Readiness State`, `SKU`, `State` only (not quantity) | VD |
| Create a subscription | Developer Portal only: Manage your apps > dropdown > "Go to Webhook portal" > "+Add Endpoint" > enter callback URL and event > Create. The page words the dropdown as "your **commercial** app". A Seller App showing "Go to Webhook portal" is reported in https://github.com/etsy/open-api/discussions/1657. No API path for subscriptions exists in the OpenAPI file | VD; Seller App eligibility VD-indirect (user report) |
| Delivery | HTTP POST, JSON, to a public callback URL. Headers `webhook-id` ("unique ID of the webhook call (even on retries)"), `webhook-timestamp` ("unix timestamp (seconds)"), `webhook-signature` | VD |
| Payload | `{"event_type":"order.paid","resource_url":"https://api.etsy.com/v3/application/shops/{YOUR_SHOP_ID}/receipts/{RECEIPT_ID}","shop_id":"{YOUR_SHOP_ID}"}`; listing events add `listing_id`; inventory events add `listing_id` and `product_id`. `resource_url` for listing events ends `?includes=Images,Personalization`. Each event needs one follow-up API call with the OAuth token | VD |
| Signed content | `signed_content = webhook-id + "." + webhook-timestamp + "." + raw_body` where `raw_body` is "the exact bytes/string of the HTTP body before any JSON parsing" | VD |
| Key | take the secret from the Webhook Portal, remove the `whsec_` prefix, Base64-decode the rest to bytes. The page's pseudo-code `secret.split("_")[1]` is ambiguous if the base64 part contains `_` (use "strip the leading `whsec_`") | VD |
| Algorithm | `expected_sig = base64_encode(HMAC_SHA256(secret_bytes, signed_content))`; "Check if any of the entries (if more than one) equals your expected_sig"; no match = reject | VD |
| Header value format | Standard Webhooks: "The signature header is a space delimited list of signatures" and each is `v1,<base64>` (example `v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=`). Etsy's page never mentions the `v1,` prefix. Builder: split on spaces, strip a leading `v1,`, compare each in constant time | UV for Etsy specifically |
| Replay guard | "if abs(now - webhook-timestamp) > 300: reject" | VD |
| Retry schedule | "Immediately, 5 seconds, 5 minutes, 30 minutes, 2 hours, 5 hours, 10 hours, 10 hours (in addition to the previous)"; manual retry and "Recover" in the portal. Required ack status code and response timeout are not stated | VD; ack rule UV |
| Testing | Portal > event details > Testing tab | VD |

### B5. Etsy rate limits

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Model | "application-based rate limits, which consist of Queries Per Day (QPD) and Queries Per Second (QPS)", "applied at the API key level"; QPD is a "Sliding Window ... last rolling 24-hour period"; "evaluated in order: QPS first, then QPD" | VD | https://developers.etsy.com/documentation/essentials/rate-limits |
| Where the numbers are | "You can see your application's current rate limits in the Developer Portal." The page prints `150` (`x-limit-per-second`) and `100000` (`x-limit-per-day`) under the column "Example Value". They are examples, not defaults. No default per tier is published | VD; real Seller App numbers UV | https://developers.etsy.com/documentation/essentials/rate-limits |
| Headers | `x-limit-per-second`, `x-remaining-this-secon` (spelled exactly so on the page, probably a typo for `...second`), `x-limit-per-day`, `x-remaining-today`; on breach `429` plus `retry-after` (seconds) | VD; exact remaining-per-second header name UV | https://developers.etsy.com/documentation/essentials/rate-limits |
| Raising | email developer@etsy.com with "A detailed description of the application" and "An estimate of the required call usage (QPD/QPS)" | VD | https://developers.etsy.com/documentation/essentials/rate-limits |

---

## C. Shopify

### C1. Dev Dashboard app and client-credentials grant

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Why not an admin custom app | "Starting January 1, 2026, you can no longer create new custom apps in the Shopify admin" | VD | https://shopify.dev/changelog/posts/legacy-custom-apps-can-t-be-created-after-january-1-2026 (raw/etsy-shopify-shopify-legacy-custom-apps-changelog.md) |
| Setup | dev.shopify.com/dashboard > Create app > Start from Dev Dashboard > create a Version (App URL, Webhooks API version, Scopes; if not embedded use the default `https://shopify.dev/apps/default-app-home`) > Release > Install app on the store > App settings has Client ID and Client secret | VD | https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard |
| Token request | `POST https://{shop}.myshopify.com/admin/oauth/access_token`, `Content-Type: application/x-www-form-urlencoded`, body `grant_type=client_credentials&client_id=<id>&client_secret=<secret>` | VD | https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant |
| Token response | `{"access_token":"f85632530bf277ec9ac6f649fc327f17","scope":"read_products","expires_in":86399}` ("Always 86399 (24 hours)"). The request does not ask for scopes; `scope` is a readback of the version's scopes | VD (doc example token) | same |
| Same-org rule | "The client credentials grant only works when the app and the store belong to the same Shopify organization. 'Same organization' means both appear under the same org in the Dev Dashboard. Owning a store or having it installed doesn't automatically place it in your org." | VD | same |
| New scopes | "Merchants still need to manually approve the new scopes in the Shopify admin." Check with `currentAppInstallation { accessScopes { handle } }` | VD | dev-dashboard page; https://shopify.dev/docs/api/usage/access-scopes |
| Scopes needed | `read_orders`, `read_all_orders` ("Despite its read_ prefix ... Declare it alongside read_orders"; default window is orders "created within the last 60 days"; "Apps created in the Dev Dashboard under a merchant organization for use on stores in that organization don't need to request Shopify approval for read_all_orders"), `read_products`, `read_inventory` | VD | access-scopes page |

### C2. GraphQL Admin API 2026-10

Evidence: `raw/contract-probe-shopify-graphql-validate.md`. Schema from `POST https://shopify.dev/admin-graphql-direct-proxy/2026-10` (3,716 types). Queries were validated with graphql-js against it, a deprecation scan of the 32 fields used found 0 problems, and the proxy also executed them against a Shopify demo store (shapes and costs are real; the demo store is not Ricky's).

| Item | Verbatim value | Status |
|---|---|---|
| Endpoint | `POST https://{shop}.myshopify.com/admin/api/2026-10/graphql.json`, headers `X-Shopify-Access-Token: <token>`, `Content-Type: application/json`. 2026-10 is "Latest stable" (released Oct 1, 2026, supported to Oct 16, 2027) | VD (https://shopify.dev/docs/api/usage/versioning) |
| Orders query | the document in the evidence file: `orders(first:25, after:$after, query:$query, sortKey:UPDATED_AT)` selecting `id name createdAt updatedAt displayFinancialStatus displayFulfillmentStatus totalPriceSet{shopMoney{amount currencyCode}} subtotalPriceSet{...} totalShippingPriceSet{...} totalTaxSet{...} lineItems(first:5){edges{node{id title sku quantity originalUnitPriceSet{shopMoney{amount currencyCode}} product{id}}}}`. Incremental filter: `query: "updated_at:>='2026-10-26T00:00:00Z'"` | VD (schema-valid) + VL (executed on proxy) |
| Products query | `products(first:25, after:$after, query:$query, sortKey:UPDATED_AT)` selecting `id title status onlineStoreUrl updatedAt variants(first:5){edges{node{id sku price inventoryQuantity}}}` | VD + VL |
| Response types | money `amount` is a decimal string (`"66.0"`); `sku` can be `""`; `onlineStoreUrl` is `null` off the Online Store; `LineItem.product` and `Order.subtotalPriceSet`/`totalTaxSet`/`ProductVariant.inventoryQuantity` are nullable; ids are `gid://shopify/...` | VL |
| Enums | `displayFinancialStatus`: PENDING, AUTHORIZED, PARTIALLY_PAID, PARTIALLY_REFUNDED, VOIDED, PAID, REFUNDED, EXPIRED. `displayFulfillmentStatus`: UNFULFILLED, PARTIALLY_FULFILLED, FULFILLED, RESTOCKED, PENDING_FULFILLMENT, OPEN, IN_PROGRESS, ON_HOLD, SCHEDULED, REQUEST_DECLINED, FULFILLMENT_NOT_REQUIRED. `ProductStatus`: ACTIVE, ARCHIVED, DRAFT, UNLISTED | VD |
| Cost (live, requested/actual) | orders 50x50 lineItems = 121/9; 25x5 = 56/18; products 50x50 variants = 72/23; 25x5 = 38/26. The single-query cap of 1,000 is on requested cost, so these are far under it | VL (demo store) |
| Protected customer data | "By default, apps don't have access to any protected customer data ... You can add the relevant scopes to your app, but the API won't return data from non-development stores until your app is configured and approved for protected customer data use." "GraphQL requests to unapproved types will return an HTTP 200 Ok response with an error message in the errors hash." Unapproved fields are "redacted" (null). The queries above select no email/name/address. Whether a Dev Dashboard merchant-org app counts as the "Custom app: Always available" row: UV | VD; applicability UV |

### C3. Webhooks

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Topic enum names | `ORDERS_CREATE`, `ORDERS_PAID`, `ORDERS_FULFILLED`, `ORDERS_UPDATED`, `PRODUCTS_UPDATE`, `INVENTORY_LEVELS_UPDATE` (REST-style `orders/create`, `orders/paid`, `orders/fulfilled`, `products/update`, `inventory_levels/update`) | VD (enum doc + introspection) | https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic |
| Scopes per topic | `orders/*`: "Requires at least one of the following scopes: read_orders, read_marketplace_orders."; `products/update`: "Occurs whenever a product is updated, ordered, or variants are added, removed or updated. Requires the `read_products` scope." (a sale also fires it); `inventory_levels/update`: "Requires the `read_inventory` scope." | VD | same |
| Option A, app-specific (recommended) | `shopify.app.toml`: `[webhooks]` `api_version = "2026-10"` then `[[webhooks.subscriptions]]` `topics = ["orders/create"]` `uri = "https://<endpoint>"`; deploy with `shopify app deploy`. "Failing subscriptions will **not** be deleted by Shopify." Needs the Shopify CLI. Whether the Dev Dashboard UI can add subscriptions without the CLI: UV | VD; UI route UV | https://shopify.dev/docs/apps/build/webhooks/subscribe |
| Option B, shop-specific | `webhookSubscriptionCreate(topic: ORDERS_PAID, webhookSubscription: {uri: "https://<endpoint>", format: JSON})` with the client-credentials token. `WebhookSubscriptionInput` fields in 2026-10: `format, includeFields, filter, metafieldNamespaces, metafields, name, uri`. "Failing subscriptions will be deleted by Shopify." List with the `webhookSubscriptions` query. Scopes cannot be set via the Admin API | VD (introspection) | same + evidence file |
| Delivery headers | `X-Shopify-Topic`, `X-Shopify-Hmac-Sha256` ("Base64-encoded HMAC signature ... HTTPS only"), `X-Shopify-Shop-Domain`, `X-Shopify-API-Version`, `X-Shopify-Webhook-Id` ("A unique composite key per delivery. Use to identify and deduplicate"), `X-Shopify-Triggered-At`, `X-Shopify-Event-Id`, optional `X-Shopify-Name`. "Treat header names as case-insensitive" | VD | https://shopify.dev/docs/apps/build/webhooks/delivery-structure |
| HMAC | "compute HMAC-SHA256 of the raw request body using your app's client secret as the key, then compare it to the decoded header value." Node sample: `crypto.createHmac('sha256', appClientSecret).update(rawBody).digest('base64')`, `timingSafeEqual`. After rotating the secret "it can take up to an hour" | VD | https://shopify.dev/docs/apps/build/webhooks/verify-deliveries |
| Timeout | "Shopify has a one-second connection timeout and a five-second timeout for the entire request." Any non-2xx (including 3xx) is an error | VD | same |
| Retries and deletion | "it retries 8 times over the next 4 hours. After 8 consecutive failures, the subscription is automatically deleted if it was configured using the Admin API." Warning emails go to the app's emergency developer email. "Shopify doesn't guarantee ordering"; build a reconciliation job | VD | same + https://shopify.dev/docs/apps/build/webhooks |
| Dedupe | `X-Shopify-Webhook-Id` per delivery; `X-Shopify-Event-Id` shared across deliveries from the same merchant action | VD | verify-deliveries |

### C4. Shopify rate limits (verbatim)

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Per plan | "Standard: 100 points/second; Advanced Shopify: 200 points/second; Shopify Plus: 1000 points/second; Shopify for enterprise (Commerce Components): 2000 points/second" | VD | https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits |
| Model | leaky bucket; "Each combination of app and store is given a bucket size and restore rate based on the store's plan"; "A single query may not exceed a cost of 1,000 points, regardless of plan limits. This limit is enforced before a query is executed based on the query's requested cost." Cost: scalar 0, enum 0, object 1, connection "Sized by first and last", mutation 10 | VD | same |
| Bucket size per plan, and which Shopify plans count as "Standard" | not stated. Docs sample shows `maximumAvailable: 1000, restoreRate: 50`; the demo store showed `maximumAvailable: 2000, restoreRate: 100`. Read `extensions.cost.throttleStatus` from Ricky's first response | UV | https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits |

---

## D. Supabase

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| `cron.schedule` | `select cron.schedule('job-name', '* * * * *', $$ select ... $$);` (name, schedule, command). "Job names are case sensitive and cannot be edited once created. Attempting to create a second Job with the same name (and case) will overwrite the first Job." | VD | https://supabase.com/docs/guides/cron/quickstart |
| Interval | "can run anywhere from every second to once a year"; seconds syntax `'30 seconds'` "as long as you're on Postgres version 15.1.1.61 or later". "no more than 8 Jobs run concurrently. Each Job should run no more than 10 minutes." Jobs live in `cron.job`; runs in `cron.job_run_details`, which "is never cleaned up automatically": schedule `delete from cron.job_run_details where end_time < now() - interval '7 days'` | VD | https://supabase.com/docs/guides/cron |
| `net.http_post` signature | `net.http_post(url text, body jsonb default '{}'::jsonb, params jsonb default '{}'::jsonb, headers jsonb default '{"Content-Type": "application/json"}'::jsonb, timeout_milliseconds int default 2000) returns bigint`. Use named arguments (`url:=`, `body:=`, `headers:=`, `timeout_milliseconds:=`). "HTTP requests are not started until the transaction is committed." Responses kept 6 hours in `net._http_response`; "reliably execute up to 200 requests per second". POST body is JSON | VD | https://supabase.com/docs/guides/database/extensions/pg_net |
| pg_cron to Edge Function with the key | Snippet D1 below. Header is `apikey` carrying the project's secret key (from Vault); URL from Vault | VD | https://supabase.com/docs/guides/functions/schedule-functions |
| Warning | "Any role that can log in to your database can read the secret key while the request waits." (pg_net writes the decrypted key to `net.http_request_queue`) | VD | same |
| Receiving side (our own cron calls) | `supabase/config.toml`: `[functions.<name>]` `verify_jwt = false`; handler `withSupabase({ auth: 'secret' }, ...)` from `npm:@supabase/server@1`; "validates the key against the secret key named `default`" | VD | https://supabase.com/docs/guides/functions/auth |
| Receiving side (eBay, Etsy, Shopify) | "External providers such as Stripe or GitHub don't send Supabase credentials. They sign the request body with their own shared secret. Use `auth: 'none'` to skip the wrapper's credential check, then verify the provider's signature inside the handler. Keep `verify_jwt = false`." Default is `verify_jwt = true`, which would 401 the vendors | VD | same |
| Vault | `select vault.create_secret('secret', 'unique_name', 'description');` read with `select decrypted_secret from vault.decrypted_secrets where name = 'unique_name'`; update with `vault.update_secret(<uuid>, <secret>, <name>, <description>)`. Stored with "Authenticated Encryption" | VD | https://supabase.com/docs/guides/database/vault |
| Function secrets | `supabase secrets set NAME=value`; `supabase secrets set --env-file .env`; `supabase secrets list`; read with `Deno.env.get('NAME')`. Names "can't start with `SUPABASE_`". Limits: 100 secrets, name up to 256 chars, 48 KiB each. Injected: `SUPABASE_URL`, `SUPABASE_DB_URL`, `SUPABASE_PUBLISHABLE_KEYS`, `SUPABASE_SECRET_KEYS` (JSON dictionaries; key `default`) | VD | https://supabase.com/docs/guides/functions/secrets |
| Edge limits | memory 256MB; wall clock "Free plan: 150s; Paid plans: 400s"; CPU "2s (Amount of actual time spent on the CPU per request - does not include async I/O.)"; "Request idle timeout: 150s"; function size 20MB (CLI) / 5MB; "Outgoing connections to ports 25 and 587 are not allowed."; `text/html` GET responses rewritten to `text/plain` without a custom domain | VD | https://supabase.com/docs/guides/functions/limits |
| Realtime subscribe | Snippet D2 below (the page's own table-filter example; `event: '*'` listens to all events, `filter` is optional) | VD | https://supabase.com/docs/guides/realtime/postgres-changes |
| Publication | `alter publication supabase_realtime add table your_table_name;` (or Dashboard > Database > Publications). Enable RLS and add a select policy. "RLS policies are not applied to DELETE statements" | VD | same |
| Database Webhooks | "a convenience wrapper around triggers using the pg_net extension. This extension is asynchronous, and therefore will not block your database changes." SQL: `create trigger "my_webhook" after insert on "public"."my_table" for each row execute function "supabase_functions"."http_request"('<url>', 'POST', '{"Content-Type":"application/json"}', '{}', '1000');` The page says to put the secret key in Vault and use a trigger function with `net.http_post` instead of embedding it | VD | https://supabase.com/docs/guides/database/webhooks |
| `@supabase/supabase-js` | latest `2.118.0`, published 2026-10-15T12:57:17Z (`@supabase/server` latest `1.9.2`) | VL (npm registry) | https://registry.npmjs.org/@supabase%2Fsupabase-js ; raw/contract-probe-npm-versions.md |
| Pro price | "From $25 / month. First project included. Additional projects from $10/mo."; "Paid plans include $10/mo in compute credits, enough to cover one Micro instance."; Free pauses "After 1 week of inactivity", Pro "Never"; Edge invocations Pro "2 Million included then $2 per 1 Million" | VD | https://supabase.com/pricing (raw/arch-sb-pricing.md) |

**Snippet D1 (VD, https://supabase.com/docs/guides/functions/schedule-functions, with `timeout_milliseconds` from the pg_net page):**

```sql
select vault.create_secret('https://project-ref.supabase.co', 'project_url');
select vault.create_secret('YOUR_SUPABASE_SECRET_KEY', 'secret_key');

select cron.schedule(
  'invoke-function-every-minute',
  '* * * * *',
  $$
  select net.http_post(
    url := (select decrypted_secret from vault.decrypted_secrets where name = 'project_url') || '/functions/v1/function-name',
    headers := jsonb_build_object(
      'Content-type', 'application/json',
      'apikey', (select decrypted_secret from vault.decrypted_secrets where name = 'secret_key')
    ),
    body := concat('{"time": "', now(), '"}')::jsonb,
    timeout_milliseconds := 5000
  ) as request_id;
  $$
);
```

**Snippet D2 (VD, https://supabase.com/docs/guides/realtime/postgres-changes):**

```ts
const changes = supabase
  .channel('table-filter-changes')
  .on(
    'postgres_changes',
    { event: 'INSERT', schema: 'public', table: 'todos', filter: 'id=eq.1' },
    (payload) => console.log(payload)
  )
  .subscribe()
```

```sql
alter publication supabase_realtime
add table your_table_name;
```


---

## E. Pushover, ntfy, Healthchecks

### E1. Pushover

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Endpoint | `POST https://api.pushover.net/1/messages.json`; "HTTPS is required"; POST required; example `Content-Type: application/x-www-form-urlencoded` | VD + VL (invalid token returns HTTP 400 `{"token":"invalid","errors":["application token is invalid, see https://pushover.net/api"],"status":0,"request":"<uuid>"}`; raw/contract-probe-pushover.md) | https://pushover.net/api |
| Required params | `token` (app token), `user` (user or group key), `message` | VD | same |
| Optional params | `title`, `url`, `url_title`, `priority` (`-2`,`-1`,`0` default,`1`,`2`), `sound`, `device`, `html`=1, `timestamp`, `ttl` ("ignored for messages with a priority value of 2"), `attachment`, `retry`, `expire`, `callback`, `tags` | VD | same |
| Priority 2 | "To send an emergency-priority notification, the `priority` parameter must be set to `2` and the `retry` and `expire` parameters must be supplied." `retry` "must have a value of at least `30` seconds"; `expire` "a maximum value of at most `10800` seconds (3 hours), though the total number of retries will be capped at 50". Response adds `receipt` (30 chars `[A-Za-z0-9]`). Priority 1 "bypass a user's quiet hours"; priority `-1`/quiet hours = no sound | VD | same + https://pushover.net/api/receipts |
| Receipts | `GET https://api.pushover.net/1/receipts/<receipt>.json?token=<app token>` "no faster than once every 5 seconds"; fields `acknowledged`, `acknowledged_at`, `acknowledged_by`, `expired`, `called_back`. Cancel: `POST https://api.pushover.net/1/receipts/<receipt>/cancel.json`. Optional `callback` URL called on acknowledge (retried in one minute on non-2xx) | VD | https://pushover.net/api/receipts |
| Message limits | "Messages are currently limited to `1024` UTF-8 characters (up to 4 bytes each), with a title of up to `250` characters. Supplementary URLs are limited to `512` characters, and URL titles to `100` characters." | VD | https://pushover.net/api |
| Quota | "Each account is permitted to send `10,000` messages per month for free"; at the cap requests get `429`; resets "00:00:00 Central Time on the 1st of each month"; headers `X-Limit-App-Limit`, `X-Limit-App-Remaining`, `X-Limit-App-Reset` | VD | same |
| Response codes | 200 + `{"status":1,"request":"..."}`; 4xx = invalid input (do not retry unchanged); 5xx = retry | VD | same |
| App price | "$4.99 USD one-time purchase" per platform, "free for 30 days"; Teams "$5 USD per-user, per-month" | VD | https://pushover.net/pricing |
| Latency to the phone | not published | UV | |

### E2. ntfy.sh (fallback)

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Publish | `POST https://ntfy.sh/<topic>` with body = message; headers `Title`, `Priority` (1 min, 2 low, 3 default, 4 high, 5 max/urgent, or names), `Click` (URL opened on tap), `Tags` (comma-separated). Long forms `X-Title`, `X-Priority`, `X-Click`, `X-Tags` also accepted | VD + VL (200 JSON `{"id","time","expires","event":"message","topic","title","message","priority":4,"tags":["warning","lamp"],"click":"https://example.com/x"}`; message kept 12 h; raw/contract-probe-ntfy.md; first call returned an empty body, retry succeeded, so treat empty/non-2xx as failure) | https://docs.ntfy.sh/publish/ |
| Non-ASCII titles | "ntfy supports UTF-8 in HTTP headers, but not every library or programming language does"; use RFC 2047 or JSON publish: `POST https://ntfy.sh/` (root URL, not the topic URL) with a JSON object. Whether Deno `fetch` throws on a non-ASCII header value: UV | VD; Deno behaviour UV | same |
| ntfy.sh limits | "Each message can be up to 4,096 bytes long"; "On ntfy.sh, the daily message limit is 250."; requests "By default ... 60 requests per visitor at once, and then refills ... one request per 5 seconds" (stated as the default config; whether ntfy.sh overrides it is not stated); title limit 1 KB, tags 512 bytes, "On ntfy.sh, the daily bandwidth limit is 200 MB." | VD | same |
| Secrecy | "If you use ntfy without sign-up, the topic is essentially a password" | VD | https://ntfy.sh/ |

### E3. Healthchecks.io

| Item | Verbatim value | Status | URL |
|---|---|---|---|
| Ping | `HEAD\|GET\|POST https://hc-ping.com/<uuid>`; `/start`, `/fail`, `/log`, `/<exit-status>` variants; or `https://hc-ping.com/<ping-key>/<slug>`; optional `rid=<uuid>` query. POST body up to 100 kB stored | VD | https://healthchecks.io/docs/http_api/ |
| Unknown check | VL: `GET https://hc-ping.com/00000000-0000-4000-8000-000000000001` returned HTTP 200 with body `OK (not found)` (header `ping-body-limit: 100000`); the doc lists "200 OK (not found)". A real ping returns body `OK`. Check the body | VL | raw/contract-probe-healthchecks.md |
| Rate limit | "If you ping a check more than 5 times per minute, some of the requests may get rate limited"; response "200 OK (rate limited)" | VD | http_api page |
| Free tier | "Hobbyist: $0 / month, Monitor 20 jobs" | VD | https://healthchecks.io/pricing/ (raw/arch-healthchecks-pricing.md) |

---

## Conflicts (both quotes shown; X verified, Y needs review)

| # | Item | Source 1 | Source 2 | Resolution |
|---|---|---|---|---|
| 1 | getOrders host | Spec top-level `"url": "https://apiz.ebay.com{basePath}"`, `basePath /sell/fulfillment/v1` (raw/ebay-spec-fulfillment_api.json) | Doc prose `GET https://api.ebay.com/sell/v1/order?` (raw/ebay-api-sell-fulfillment_api.md, missing `/fulfillment`) | VL probe: `api.ebay.com/sell/fulfillment/v1/order` = 401 route found; `apiz.ebay.com/...` = 404. Use `api.`. The `/payment_dispute*` and Finances routes are the ones that live on `apiz`. Re-confirm with the first authenticated call |
| 2 | Marketplace header | Brief: `X-EBAY-C-MARKETPLACE_ID` | Spec x12: `X-EBAY-C-MARKETPLACE-ID` | Hyphen |
| 3 | Public-key id | Account-deletion guide: base64-decode the header, "This decoded value will be passed into the end of the getPublicKey URI" | Communications guide: "extract the Base64-encoded X-EBAY-SIGNATURE header ... Pass this value as a path parameter" | eBay's SDK: decode, JSON-parse, pass `kid`. Use the SDK behaviour (A5.4) |
| 4 | Browse search in production | Open: spec carries no Limited Release note on `item_summary/search`; call-limit row "5000 API calls per day"; sign-up modal "always free! 5,000 API calls per day"; community post "the browse api seems to work" with client credentials | Gated: "The use of eBay's Buy APIs in production is intended for eBay partners only. You must apply for production access through the eBay Partner Network ... There is no guarantee that your application for production use of the APIs will be approved." and "The Buy APIs listed above are intended for certain approved eBay partners" (Browse is in that list) and "The Application Growth Check is a mandatory step for using restricted Buy APIs in Production" | Not resolvable from docs. Smoke test 1 |
| 5 | Etsy API host for OAuth | Auth page: `https://api.etsy.com/v3/public/oauth/token` | OpenAPI `tokenUrl`: `https://openapi.etsy.com/v3/public/oauth/token` and `servers` `https://openapi.etsy.com` | VL: both hosts answer identically. Use `api.etsy.com` (docs, quickstart, webhook `resource_url`) |
| 6 | Etsy refresh `grant_type` | Parameter table: "Must be the value `refresh_token`" | Prose: "`grant_type=refresh_code` is required" | Use `refresh_token`; confirm on first refresh |
| 7 | Etsy webhook signature details | Page: "Check if any of the entries (if more than one) equals your expected_sig"; pseudo-code `secret.split("_")[1]` | Standard Webhooks spec: header "space delimited list" of `v1,<base64>` | Strip `whsec_` by prefix, split header on spaces, strip `v1,`; confirm from the Testing tab |
| 8 | Etsy webhooks for a Seller App | Page: "available for both **commercial** and **personal** applications"; steps say "your **commercial** app" | GH #1657 user: Seller App menu "only shows 'Edit callback URLs' and 'Go to Webhook portal'" | Treat as available; confirm at app creation |
| 9 | Etsy rate-limit numbers | Page prints 150 QPS / 100000 QPD | Same table header: "Example Value"; "You can see your application's current rate limits in the Developer Portal" | Read the portal |
| 10 | Etsy timestamps | Spec has both `create_timestamp` and `created_timestamp` (and `update_timestamp` / `updated_timestamp`, `creation_timestamp` / `last_modified_timestamp` on listings) | | Store one pair; both appear in the schema. Check a live response |
| 11 | Shopify HMAC header casing | delivery-structure: `X-Shopify-Hmac-Sha256` | verify-deliveries prose: `X-Shopify-Hmac-SHA256` | Case-insensitive |
| 12 | Shopify bucket | Docs sample `maximumAvailable: 1000, restoreRate: 50` | "Standard: 100 points/second"; demo store `maximumAvailable: 2000, restoreRate: 100` | Read Ricky's own `throttleStatus` |
| 13 | Supabase cron key | Cron quickstart: `headers:=jsonb_build_object('Content-Type','application/json', 'apikey', 'YOUR_PUBLISHABLE_KEY')` | Schedule-functions: "Don't use your publishable key, because it's public and anyone who has it can call a function that accepts it." | Use the secret key from Vault, `verify_jwt=false`, `auth:'secret'` |
| 14 | Browse `itemStartDate` examples | Syntax line `itemStartDate:[...]` | Open-ended example lines print `filter=itemEndDate:[...]` | Doc typo; use `itemStartDate` |
| 15 | Browse sort vs start filter | `sort=newlyListed` sorts by `itemOriginDate` ("retained if an item is relisted") | `itemStartDate` is "the moment the listing became available" | Relisted items can sort high but fail an `itemStartDate` cursor. Dedupe on `itemId`; do not trust either alone |
| 16 | eBay usernames | Browse/Fulfillment/Notification field notes: "select developers will no longer receive username data for U.S. users" | Data Handling page scopes it to developers in China, Russia, North Korea, Cuba, Iran, Venezuela | Likely returns real usernames for a U.S. developer; treat as opaque anyway |
| 17 | ntfy.sh limits | `publish` page: defaults "60 requests per visitor ... one request per 5 seconds" | Same page: "On ntfy.sh, the daily message limit is 250." | 250/day is ntfy.sh-specific VD; the 60/5 s is a default-config statement |

## Unverified items the builder must smoke-test first (in this order)

1. **eBay Browse production access.** Mint an app token (`grant_type=client_credentials`, `scope=https://api.ebay.com/oauth/api_scope`), then `GET /buy/browse/v1/item_summary/search?q=vintage%20lamp&limit=1` with `X-EBAY-C-MARKETPLACE-ID: EBAY_US`. 200 with `itemSummaries` = buy alerts can be API-driven. 403 or `invalid_scope` = fall back to eBay saved searches and consider EPN / Application Growth Check. Then test the full filter string from A3.
2. **eBay account-deletion endpoint, then topic access.** Deploy a public function with `verify_jwt=false` that answers the challenge exactly as A5.3 and persists nothing it should not. Register it. Then with the app token `GET /commerce/notification/v1/topic/ORDER_CONFIRMATION`: read `authorizationScopes`, `status`, `supportedPayloads[].schemaVersion`. Then user consent with the four scopes, `createSubscription`, `testSubscription` (expect 202 and a POST with a signature), then one real sale.
3. **eBay signature on a real POST.** Log the raw body and `x-ebay-signature`. Verify with `node:crypto` `createVerify('ssl3-sha1')` over (a) the raw body and (b) `JSON.stringify(JSON.parse(raw))`; record which passes. Confirm the Edge Runtime supports `ssl3-sha1`; if not, use `crypto.subtle` with DER to P1363 conversion. Confirm the key's curve.
4. **eBay `getOrders` after user consent.** Call `https://api.ebay.com/sell/fulfillment/v1/order?limit=1` with the user token. Confirm the host, and that orders for app/web-made listings appear with `legacyItemId`.
5. **Shopify protected data, first.** After the client-credentials token works (same-org check), run the orders query plus `email` and `shippingAddress { name city }` and `customer { id }`. If the response is HTTP 200 with an `errors` hash or nulls, the approval path for protected customer data is needed before buyer fields can be stored. Also read `throttleStatus` and `currentAppInstallation.accessScopes`.
6. **Shopify webhook setup route.** Try the Dev Dashboard version page for adding subscriptions. If it cannot, use `webhookSubscriptionCreate` (Option B) and add a reconciliation job that lists `webhookSubscriptions` and re-creates any deleted after 8 failures. Send a real `orders/paid` and verify HMAC on the raw body.
7. **Etsy webhooks on a Seller App.** Create the app, find "Go to Webhook portal", add the endpoint, press Testing. Log all three headers; confirm the `v1,` prefix, single vs multiple signatures, the `whsec_` secret format, and which response code and time Etsy requires.
8. **Etsy limits and refresh.** Read QPS/QPD from the portal and from `x-limit-per-day` / `x-remaining-today` (exact remaining-per-second header name). Refresh once with `grant_type=refresh_token`; confirm a new `refresh_token` comes back and persist it. If the token exchange returns the 403 "API key not found ..." message, add `x-api-key: <keystring>:<shared_secret>` to the token request (the probes sent none, so whether that endpoint needs it is UV).
9. **Supabase cron to function.** Schedule a 60-second job as in D (Vault secret key, `apikey` header, `timeout_milliseconds` set). Confirm the function with `auth:'secret'` accepts it and that a `verify_jwt=false` + `auth:'none'` receiver returns 200 to an anonymous `curl`. Add the `cron.job_run_details` cleanup job.
10. **Pushover priority 2 end to end.** Send `priority=2&retry=60&expire=1800`, expect `receipt`; acknowledge on the phone; poll the receipt (no faster than 5 s). Measure delivery latency (not published).
11. **ntfy non-ASCII.** Send an item title with an accent or emoji in a `Title` header from Deno `fetch`; if it throws or mangles, switch to JSON publish at `https://ntfy.sh/`.
12. **Healthchecks.** After creating the check, ping it and assert the body is exactly `OK` (not `OK (not found)`).

## Evidence index

Created by this pass in `research/dashboard/raw/` (all prefixed `contract-`):
- Live probes: `contract-probe-ebay-hosts.md`, `contract-probe-ebay-token.md`, `contract-probe-etsy-hosts.md`, `contract-probe-pushover.md`, `contract-probe-ntfy.md`, `contract-probe-healthchecks.md`, `contract-probe-npm-versions.md`.
- Computed evidence: `contract-probe-shopify-graphql-validate.md` (schema validation, enums, cost, sample shapes), `contract-probe-ebay-ecdsa-selftest.md` (signature algorithm under Deno).
- Fetched pages: `contract-ebay-data-handling-update.md`, `contract-standard-webhooks-spec.md`, `contract-shopify-events-webhooks.md`, `contract-supabase-functions-auth.md`, `contract-supabase-cron-quickstart.md`, `contract-healthchecks-http-api.md`, `contract-pushover-receipts.md`.
- eBay SDK source (https://github.com/eBay/event-notification-nodejs-sdk): `contract-gh-ebay-notif-sdk-lib-validator.js`, `-lib-client.js`, `-lib-constants.js`, `-lib-index.js`, `-lib-processor-*.js`, `-README.md`, `-examples-example.js`, `-examples-config.json` (placeholders only).

Relied on from wave 1 (re-read today): `raw/ebay-spec-{browse,fulfillment,notification,finances,feed,inventory}_api.json`, `raw/ebay-guide-authorization.md`, `raw/ebay-guide-account-deletion.md`, `raw/ebay-guide-sell-communications.md`, `raw/ebay-notification-events.md`, `raw/ebay-browse-filters.md`, `raw/ebay-api-sell-fulfillment_api.md`, `raw/ebay-api-sell-notification_api.md`, `raw/ebay-*call-limits.md`, `raw/ebay-buy-requirements.md`, `raw/ebay-get-started-buying.md`, `raw/etsy-shopify-etsy-{auth,webhooks,ratelimits,openapi,docs-home,gh1657-commercial}`, `raw/etsy-shopify-shopify-{client-credentials,devdash-create,access-scopes,protected-customer-data,versioning,webhooks-subscribe,webhooks-delivery-structure,webhooks-verify,webhook-topic-enum,graphql-ratelimits}`, `raw/arch-sb-{pgnet,vault,fn-schedule,fn-secrets,fn-limits,realtime-pgchanges,db-webhooks,pricing,cron}`, `raw/arch-pushover-{api,pricing}.md`, `raw/arch-ntfy-publish.md`, `raw/arch-healthchecks-pricing.md`.

Not touched: `site/`. Nothing committed.
