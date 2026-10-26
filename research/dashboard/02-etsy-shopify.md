# Etsy Open API v3 and Shopify Admin API: dashboard research

Date: 2026-10-26. Author: research subagent (Sonnet 5.5). Scope: research only, nothing built.
Shop: Hollywood and Vine (vintage, mostly quantity-1 items). Stack: Supabase Edge Functions (Deno), React 19, Vercel.

Claim tags: **[V]** = read in a page fetched today (2026-10-26) or the Wayback snapshot noted; **[I]** = my inference from verified facts, stated as such; **[U]** = unverified, not found in any fetched page.
Raw pages are in `research/dashboard/raw/etsy-shopify-*`. The raw files do not carry their source URL, so the file-to-URL table is in the Appendix.

---

## 0. Read this first: three premises in the brief did not hold

1. **Etsy v3 DOES have webhooks.** [V] Events: `order.paid`, `order.canceled`, `order.shipped`, `order.delivered`, `listing.created`/`updated`/`deleted`, `inventory.created`/`updated`/`deleted`/`out_of_stock`. Signed, retried. Source: https://developers.etsy.com/documentation/essentials/webhooks/ . A Seller App (the free, own-shop tier) shows "Go to Webhook portal" in its menu per https://github.com/etsy/open-api/discussions/1657 [V]. Wording mismatch to watch: the docs page says "available for both **commercial** and **personal** applications" but never names Seller Apps, and its portal steps say "your **commercial** app". So webhooks on a Seller App is confirmed only by a user's description in GH #1657, not by the docs page itself. Treat as [V-indirect].
2. **You can no longer create a custom app inside the Shopify admin.** [V] "Starting January 1, 2026, you can no longer create new custom apps in the Shopify admin... Existing custom apps aren't affected." Use a **Dev Dashboard** app instead: https://shopify.dev/changelog/posts/legacy-custom-apps-can-t-be-created-after-january-1-2026 and https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin . Own-store auth is the **client credentials grant** (24 h token). Gotcha: the app and the store must be in the **same Shopify organization**; owning the store is not enough (section 6).
3. **Shopify Marketplace Connect cannot make new Etsy connections.** [V] Shopify Help Center, stated twice: "New connections to Etsy can't be made at this time with the Shopify Marketplace Connect app. If you're already selling on Etsy through Marketplace Connect, then you can continue to use the app." https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect and https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/requirements . Its App Store listing names only Amazon, eBay, Target Plus, Walmart: https://apps.shopify.com/marketplace-connect . A shopify.com blog post titled "(2026)" still says to use Marketplace Connect for Etsy: https://www.shopify.com/blog/etsy-and-shopify . Verdict: help center verified, blog stale. Marketplace Connect is an eBay-only option for Ricky.

Other headline facts:
- Etsy has a free **Seller App** tier (announced 2026-07-13): own shop only, approved "within minutes". Right fit for Ricky. https://developers.etsy.com/documentation/ [V]
- Etsy API Terms prohibited-behavior #25 bans requesting Etsy content "for purposes of analytics" (section 5). A sales dashboard fits that literal text. Open question 1.
- Shopify REST is legacy; latest stable GraphQL version today is **2026-10**. [V]

---

## 1. Etsy: app registration and access tiers

Source for all of section 1 unless noted: https://developers.etsy.com/documentation/ [V]

| Tier | Who | Approval | Shop scope | Commercial use |
|---|---|---|---|---|
| **Seller App** | "Individual sellers building for their own shop" | "Eligible sellers are approved within minutes, with no manual review queue" | "Your shop only" | "Not permitted" |
| Personal App | Developers building beyond own shop at limited scale | "Deeper review process" | Limited-scale, approved use case | Limited |
| Commercial Access | Apps for many sellers | "reviewed manually", time varies | "Any seller who grants OAuth consent" | Permitted after approval |

- **Is personal access enough for one owner's dashboard? Use a Seller App instead.** [V] Seller App "includes access to all public and OAuth-authenticated endpoints, scoped only to your registered shop." Registration link on the docs page: https://www.etsy.com/developers/register-seller-app
- Eligibility [V]: "Any seller with an active Etsy shop in good standing who doesn't already have an active app." **Ricky needs a live Etsy shop first.** Announcement (2026-07-13): "two required fields instead of the previous multi-step application form"; a Seller App "replaces the Personal Key tier as the path for sellers": https://github.com/etsy/open-api/discussions/1647 [V].
- **Lock-in trap** [V]: Etsy staff reply in GH #1657 (2026-07-20): "A Commercial Upgrade is only available to Personal Apps. We do not allow users to have both Seller Apps **and** Personal/Commercial Apps... we will need to suspend your active seller app and you will need to reapply for **Personal** access." Also "Personal app access typically takes a couple of days, commercial access takes longer." https://github.com/etsy/open-api/discussions/1657 . If Ricky later wants a multi-seller product, he restarts. Not needed for a private dashboard.
- Commercial Access can be refused: one POD developer reports being "banned within 24 hours" twice after Personal approval: https://github.com/etsy/open-api/discussions/1764 [V as a user report, not an Etsy statement].
- **Cost**: no registration fee appears in any fetched Etsy page. [U] that none exists. The API Terms say Etsy "may condition acceptance of such requests [for higher rate limits] on your agreement to additional terms and/or charges" (Terms section 2, Wayback copy, see section 5).
- Dormancy [V]: "If an Application has not made a successful call to the Etsy API for six (6) consecutive months, Etsy reserves the right to suspend" (Terms section 3). Irrelevant if the dashboard polls.
- Auth header on every request [V]: `x-api-key: <keystring>:<shared_secret>` (keystring AND shared secret, colon-separated). https://developers.etsy.com/documentation/essentials/authentication . Etsy also has a "Rotating Your Shared Secret" tutorial (https://developers.etsy.com/documentation/tutorials/shared-secret-rotation, in the docs nav, not fetched [U]).

---

## 2. Etsy: OAuth 2.0 with PKCE

Source: https://developers.etsy.com/documentation/essentials/authentication [V] unless noted.

1. Send the shop owner to `GET https://www.etsy.com/oauth/connect` with `response_type=code`, `client_id=<keystring>`, `redirect_uri` (must be `https://`, exact string match, registered in Your Apps), `scope` (space-separated, URL-encoded), `state`, `code_challenge`, `code_challenge_method=S256`.
2. Etsy redirects back with `code` (+ `state`).
3. `POST https://api.etsy.com/v3/public/oauth/token`, `application/x-www-form-urlencoded`: `grant_type=authorization_code`, `client_id`, `redirect_uri` (optional), `code`, `code_verifier`.
4. Response: `{"access_token":"<user_id>.<token>","token_type":"Bearer","expires_in":3600,"refresh_token":"<user_id>.<token>","scope":"..."}`.
5. Verifier: 43 to 128 chars from `[A-Za-z0-9._~-]`; challenge = base64url(SHA-256(verifier)). "The Etsy Open API requires a PKCE on every authorization flow request."
6. Refresh: `POST https://api.etsy.com/v3/public/oauth/token` with `grant_type=refresh_token`, `client_id`, `refresh_token`. The response returns a **new** `refresh_token`; store the latest each time.

Lifetimes [V]: access token "has a functional life of 1 hour" (`expires_in: 3600`); refresh token "longer functional lifetime (90 days)". Scope can't change on refresh; a scope change needs a fresh authorization-code flow. [I] Refresh at least weekly so the 90-day clock never lapses.

Scope strings [V] (complete list on the page): `address_r`, `address_w`, `email_r`, `listings_d`, `listings_r`, `listings_w`, `profile_r`, `profile_w`, `shops_r`, `shops_w`, `transactions_r`, `transactions_w`. Descriptions: `listings_r` "Read a member's inactive and expired (i.e., non-public) listings"; `transactions_r` "Read a member's purchase and sales data"; `shops_r` "See a member's shop description, messages and sections".

Per-endpoint scopes come from the OpenAPI spec (section 3). Minimum set for the dashboard: **`listings_r listings_w transactions_r shops_r`**. `shops_r` is needed because `GET /v3/application/users/me` requires it (spec `getMe`). Add `listings_d` (delete) or `transactions_w` (post tracking) only if a feature needs them (Terms prohibited #17 bans requesting "more than the minimum amount of data").

Discrepancy in the Etsy docs (X verified, Y needs review): the refresh table says `grant_type` "Must be the value `refresh_token`", but the prose bullet says "`grant_type=refresh_code`". Use `refresh_token` (matches the table); test once.

---

## 3. Etsy: endpoints (verbatim paths, from the live OpenAPI spec)

Spec fetched: https://www.etsy.com/openapi/generated/oas/3.0.0.json (info.title "Etsy Open API v3", version 3.0.0) [V]. Reference UI: https://developers.etsy.com/documentation/reference

Discrepancy: the spec's `servers` entry is `https://openapi.etsy.com` ("Base URL for all Open API endpoints"), but the docs, the quickstart and the webhook `resource_url` all use `https://api.etsy.com/v3/...`. Use `api.etsy.com`; `openapi.etsy.com` needs a test before relying on it.

| Need | Method + path | Scope | Notes |
|---|---|---|---|
| Listings by shop (any state) | `GET /v3/application/shops/{shop_id}/listings` | `listings_r` | `state` enum: `active`, `inactive`, `sold_out`, `draft`, `removed`, `expired` (default `active`). `limit` 1 to 100 (default 25), `offset`. `includes`: Shipping, Shop, Images, User, Translations, Videos, Inventory (list truncated in my extract). |
| Active listings, no OAuth | `GET /v3/application/shops/{shop_id}/listings/active` | none (api key only) | `limit`, `offset`, `keywords`, `sort_on`, `sort_order`. |
| One listing | `GET /v3/application/listings/{listing_id}` | none | |
| **Receipts (sales)** | `GET /v3/application/shops/{shop_id}/receipts` | `transactions_r` | Filters: `min_created`, `max_created`, `min_last_modified`, `max_last_modified` (unix seconds, minimum value 946684800), `was_paid`, `was_shipped`, `was_delivered`, `was_canceled` (booleans). Paging: `limit` 1 to 100 (default 25), `offset`. `sort_on`: `created`, `updated`, `receipt_id`; `sort_order`: `asc`, `ascending`, `desc`, `descending`, `up`, `down`. Also `legacy` boolean. |
| One receipt | `GET /v3/application/shops/{shop_id}/receipts/{receipt_id}` | `transactions_r` | The webhook `order.paid` `resource_url` target. |
| Transactions (line items) by shop | `GET /v3/application/shops/{shop_id}/transactions` | `transactions_r` | `limit`, `offset`, `legacy`. |
| Transactions by receipt | `GET /v3/application/shops/{shop_id}/receipts/{receipt_id}/transactions` | `transactions_r` | |
| Transactions by listing | `GET /v3/application/shops/{shop_id}/listings/{listing_id}/transactions` | `transactions_r` | |
| Payments / ledger | `GET /v3/application/shops/{shop_id}/payments`; `GET /v3/application/shops/{shop_id}/payment-account/ledger-entries` (`min_created`, `max_created`) | `transactions_r` | Fee / payout reconciliation. |
| Post tracking | `POST /v3/application/shops/{shop_id}/receipts/{receipt_id}/tracking` | `transactions_w` | |
| Inventory read | `GET /v3/application/listings/{listing_id}/inventory` | `listings_r` | |
| **Inventory update** | `PUT /v3/application/listings/{listing_id}/inventory` | `listings_w` | JSON body: `products` (required), `price_on_property`, `quantity_on_property`, `sku_on_property`, `readiness_state_on_property`. |
| **Create listing (draft)** | `POST /v3/application/shops/{shop_id}/listings` | `listings_w` | `application/x-www-form-urlencoded`. Required: `quantity`, `title`, `description`, `price`, `who_made` (`i_did`/`someone_else`/`collective`), `when_made`, `taxonomy_id`. `when_made` enum: `made_to_order`, `2020_2026`, `2010_2019`, `2007_2009`, `before_2007`, `2000_2006`, `1990s`, `1980s`, `1970s`, `1960s`, `1950s`, `1940s`, `1930s`, `1920s`, `1910s`, `1900s`, `1800s`, `1700s`, `before_1700`. Optional: `shipping_profile_id`, `return_policy_id`, `tags`, `materials`, `styles`, `image_ids` (up to 20), `readiness_state_id`, `type` (`physical`/`download`/`both`), `is_supply`. |
| **Image upload** | `POST /v3/application/shops/{shop_id}/listings/{listing_id}/images` | `listings_w` | `multipart/form-data`: `image` (binary), `listing_image_id`, `rank`, `overwrite`, `is_watermarked`, `alt_text`. |
| Update / publish | `PATCH /v3/application/shops/{shop_id}/listings/{listing_id}` | `listings_w` | The `state` parameter text says a draft set to `active` is published. |
| Delete | `DELETE /v3/application/listings/{listing_id}` | `listings_d` | |
| Who am I | `GET /v3/application/users/me` | `shops_r` | Returns the user id; shop id via `GET /v3/application/users/{user_id}/shops` (no OAuth). |
| Ping | `GET /v3/application/openapi-ping` | none | Key check. |

Fields that matter for a dashboard [V, spec schemas]: `ShopReceipt` has `receipt_id`, `status`, `is_paid`, `is_shipped`, `create_timestamp`, `update_timestamp`, `grandtotal`, `subtotal`, `total_shipping_cost`, `total_tax_cost`, `transactions`, `shipments`, `refunds`, buyer name/address fields, `buyer_email` (null unless access approved "case-by-case"). `ShopReceiptTransaction` has `transaction_id`, `listing_id`, `product_id`, `sku`, `quantity`, `price`, `paid_timestamp`, `shipped_timestamp`. `ShopListing` has `state`, `quantity`, `price`, `last_modified_timestamp`, `when_made`, `taxonomy_id`.

Notes:
- Quantity-1 vintage items: a sold-out listing has state `sold_out` [V, enum]. Whether a `sold_out` listing can be restocked by `PUT .../inventory` or must be renewed is [U].
- Whether `shipping_profile_id` / `readiness_state_id` are effectively mandatory to publish a physical listing is [U] (optional in the create schema).
- `taxonomy_id` lookup (SellerTaxonomy endpoints) exists in the reference; I did not extract it. [U]
- Etsy listing and seller fees are outside the API docs and not covered here. [U]

---

## 4. Etsy: webhooks vs polling, and rate limits

### Webhooks [V] https://developers.etsy.com/documentation/essentials/webhooks/
- Events: Order `order.paid`, `order.canceled`, `order.shipped`, `order.delivered`; Listing `listing.created`, `listing.updated` (fires on `Title`, `Description`, `Personalization`, `Taxonomy`, `Images`, `Attributes`, `State`), `listing.deleted`; Inventory `inventory.created`, `inventory.updated` (fires on `Price`, `Readiness State`, `SKU`, `State`), `inventory.deleted`, `inventory.out_of_stock` ("delivered when a product's quantity reaches 0").
- **[I] Quantity is not in the `inventory.updated` trigger list.** For a quantity-1 piece, the sold signals are `order.paid` and `inventory.out_of_stock`. Do not rely on `inventory.updated` for stock.
- **Thin payloads**: only `event_type`, `resource_url`, `shop_id` (+ `listing_id`, `product_id`). Example: `{"event_type":"order.paid","resource_url":"https://api.etsy.com/v3/application/shops/{YOUR_SHOP_ID}/receipts/{RECEIPT_ID}","shop_id":"{YOUR_SHOP_ID}"}`. You must call `resource_url` (with the OAuth token) to get the receipt, so each webhook costs one API call.
- Delivery: HTTP POST to a public HTTPS callback. Headers: `webhook-id` (unique per call, same across retries; use for dedupe), `webhook-timestamp` (unix seconds), `webhook-signature`.
- Signature: `signed_content = webhook-id + "." + webhook-timestamp + "." + raw_body`; key = base64-decode of the signing secret after removing the `whsec_` prefix; `expected = base64(HMAC_SHA256(key, signed_content))`; compare to `webhook-signature` ("Check if any of the entries (if more than one) equals your expected_sig"). Replay guard in the docs: reject if `abs(now - webhook-timestamp) > 300`.
- Retries (exponential backoff): Immediately, 5 seconds, 5 minutes, 30 minutes, 2 hours, 5 hours, 10 hours, 10 hours (roughly 27 h total [I]). Manual retry and "Recover" (replay all failed since a date) in the portal.
- **Subscriptions are created in the Developer Portal UI only** ("Go to Webhook portal" > "+Add Endpoint"). [V by absence] The OpenAPI spec contains no webhook-management path. The endpoint URL and event choices are manual setup, not code.
- [I] A Supabase Edge Function can be the callback; read the raw body before JSON parse (needed for the signature).

### Rate limits [V] https://developers.etsy.com/documentation/essentials/rate-limits
- "application-based rate limits, which consist of Queries Per Day (QPD) and Queries Per Second (QPS)", applied "at the API key level".
- QPD is a **sliding rolling 24-hour window**, not a midnight reset.
- Headers on success: `x-limit-per-second`, `x-remaining-this-secon` (sic, exactly as printed in the docs; probably a doc typo for `x-remaining-this-second`; read case-insensitively and check a real response), `x-limit-per-day`, `x-remaining-today`. Over limit: `429` + `retry-after` (seconds). "Rate limits are evaluated in order: QPS first, then QPD."
- **The numbers 150 (QPS) and 100000 (QPD) on that page are labelled "Example Value", not defaults.** Etsy publishes no default per tier (third-party corroboration: https://vorplabs.com/agent-tools/etsy-api , "does not publish default values by tier"). The real limit is shown in the Developer Portal after app creation. [U] for Seller App values. Increases: email developer@etsy.com with "A detailed description of the application" and "An estimate of the required call usage".
- Budget math [I]: polling `getShopReceipts` + `getListingsByShop` every 15 min = 192 calls/day, plus one callback fetch per webhook. Small against any plausible daily limit, but confirm in the portal.

### Is there a push mechanism? Yes, webhooks. Enough alone? No.
Webhooks can be missed (handler down; the retry schedule ends after about 27 hours). Keep a reconciliation poll (see Recommendation).

---

## 5. Etsy: API Terms that affect a private dashboard

The live page returned 403 to crawl4ai and WebFetch. Source used: **Wayback snapshot dated 2026-10-12** of https://www.etsy.com/legal/api , footer "Last updated on Aug 18, 2026" [V]. The Aug 18, 2026 date is corroborated by https://vorplabs.com/agent-tools/etsy-api . Raw: `etsy-shopify-etsy-api-terms-wayback.md`. Section numbers are the page's own headings (1 to 5); the prohibited list is numbered inside "5. Use of the Etsy API".

- **Display / caching (Terms 5, "Display of Data")** [V]: "You will not display listing content more than six (6) hours older than the corresponding information on the Etsy Site or the Etsy Apps. You will not display any other Etsy content more than twenty-four (24) hours older... Once you've accessed, stored, or displayed Etsy content, you will not cache or store it longer than is reasonably necessary to provide service to your Application's users." [I] A Supabase mirror of listings must refresh within 6 h; sales-history retention is a gray area ("reasonably necessary"). Keep your own bookkeeping records in your own ledger; keep the Etsy-sourced listing mirror fresh.
- **Prohibited #25** [V]: "Use the Etsy API to collect, scan, or otherwise request Etsy content for purposes of analytics, machine learning, training artificial intelligence models, licensing, or content removal, unless expressly authorized in writing by Etsy." A sales dashboard is "analytics" on the literal text. [I] Likely aimed at market scraping and AI training, but ask developer@etsy.com before building a reporting product. The Seller App announcement frames the tier as for "tools and services for their own shop".
- **#24** [V]: bans "automated systems or browser extensions to access, analyze, or scrape the Etsy Site, the Etsy API or any Etsy data... unless expressly authorized in writing". Read literally, any API client is "automated"; clearly not the intent for an approved app. Same ask-Etsy item.
- **#2** [V]: no "Divert sales or migrate Etsy Members from Etsy, or drive traffic to external websites or services unrelated to the Etsy platform". Matters when the own site launches: do not use Etsy buyer data to market the own site.
- **#15** [V]: no use "to connect with any third-party advertising or marketing platform".
- **#16** [V]: no "sending to Etsy Members order, shipping and tracking information, whether via email, text or otherwise, unless expressly authorized in writing by Etsy". The dashboard must not message buyers.
- **#17** [V]: request no "more than the minimum amount of data needed".
- **#18** [V]: no transfer or commercializing of "Etsy Member content or data to any third party".
- **#13** [V]: handle Etsy Member data only with authorization. Terms 4: the developer acts as "a service provider to the applicable Etsy seller" for member personal information.
- **Trademark line**, two versions [V]. Terms section 1: `"The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy."` Docs review criteria (https://developers.etsy.com/documentation/): `"The term 'Etsy' is a trademark of Etsy, Inc. This application uses the Etsy API but is not endorsed or certified by Etsy, Inc."` The Terms are the binding text ("you must prominently display"). Put the Terms version in the dashboard footer.
- **Buyer email** [V]: `buyer_email` is null unless access is approved; the docs say Commercial Access apps using `transaction_r` "must request access to the `buyer_email` field separately". [U] whether a Seller App can request it.
- Rate-limit evasion [V]: "Creating or attempting to create additional API keys to circumvent these limitations is strictly prohibited"; one key = one Application.
- [I] If Ricky also uses a sync app (CedCommerce etc.) for Etsy, that app uses its own key, so it does not collide with the Seller-App key.

---

## 6. Shopify: GraphQL vs REST, versions, custom app, scopes

### REST status [V] https://shopify.dev/docs/api/admin-rest
Verbatim banner: "The REST Admin API is a legacy API as of October 1, 2024. Starting April 1, 2025, all new public apps must be built exclusively with the GraphQL Admin API." Also: "Some newer platform features may only be available in GraphQL." The banner restricts **public** apps; it does not say private integrations stop working. Build on GraphQL anyway.

### Version naming [V] https://shopify.dev/docs/api/usage/versioning
- "Shopify releases a new API version every three months at 5pm UTC on the first day of the quarter. Version names are date-based (for example, `2026-04`). Each stable version is supported for a minimum of 12 months, with at least nine months of overlap between consecutive versions."
- On 2026-10-26 the page shows: **2026-10 = Latest stable** (released Oct 1, 2026, supported to Oct 16, 2027); 2026-07, 2026-04, 2026-01 Stable; 2027-01 Release candidate; 2025-10 and older Unsupported. A request to an inaccessible version "falls forward" to the oldest accessible stable version.
- Endpoint: `https://{shop}.myshopify.com/admin/api/2026-10/graphql.json`, header `X-Shopify-Access-Token`. https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin [V]

### Is an admin-created custom app enough for one shop? It no longer exists for new apps. [V]
- Changelog: "Starting January 1, 2026, you can no longer create new custom apps in the Shopify admin... To create a new custom app after this date, use the Dev Dashboard to build the app, then install it on your store." https://shopify.dev/changelog/posts/legacy-custom-apps-can-t-be-created-after-january-1-2026
- Dev Dashboard flow (https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard): dev.shopify.com/dashboard > Create app > Start from Dev Dashboard > create a **Version** (App URL, Webhooks API version, Scopes) > Release > Install app on the store > authenticate.
- Auth for your own store, no redirect flow: **client credentials grant**. https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant [V]
  - `POST https://{shop}.myshopify.com/admin/oauth/access_token`, `application/x-www-form-urlencoded`, `grant_type=client_credentials`, `client_id`, `client_secret`. Response `{"access_token":"...","scope":"read_products","expires_in":86399}`; "Always 86399 (24 hours)". Cache and refresh before expiry.
  - **Gotcha** [V]: "only works when the app and the store belong to the same Shopify organization. 'Same organization' means both appear under the same org in the Dev Dashboard. Owning a store or having it installed doesn't automatically place it in your org." It cannot reach "a client's store".
  - New scopes in a new version are not auto-applied: "Merchants still need to manually approve the new scopes in the Shopify admin." (Ricky is the merchant, so a one-click step.)
- Existing admin-created custom apps keep working with a permanent token. Not applicable to a new store.

### Access scopes [V] https://shopify.dev/docs/api/usage/access-scopes
- `read_orders` / `write_orders`: orders "created within the last 60 days". **`read_all_orders`** extends to older orders; it "doesn't grant access on its own. Declare it alongside `read_orders` or `write_orders`". The 60-day gotcha is confirmed.
- "Apps created in the Dev Dashboard under a merchant organization for use on stores in that organization don't need to request Shopify approval for `read_all_orders`." (Partner-org apps must request it.) Add it to the version and release.
- `read_products` / `write_products`: Product, ProductVariant, Collection. `read_inventory` / `write_inventory`: InventoryItem, InventoryLevel. `read_locations`: Location.
- Check what you actually got: query `currentAppInstallation { accessScopes { handle } }`.
- **Protected customer data** [V] https://shopify.dev/docs/apps/launch/protected-customer-data : orders, webhooks "that relate to a single customer or order", and customer name/address/email count as protected. "By default, apps don't have access to any protected customer data... the API won't return data from non-development stores until your app is configured and approved for protected customer data use." The same page's table: Level 1 and Level 2 are "Always available" for a "Custom app" (Level 2 "Varies by plan" for an admin-created custom app). **Open question 4**: is a Dev Dashboard merchant-org app treated as "Custom app" and exempt from review? If not, buyer name/address come back redacted in sold alerts.

---

## 7. Shopify: webhooks and Flow

### Topics [V]
Reference list with sample payloads: https://shopify.dev/docs/api/webhooks . Scope requirements from the GraphQL enum https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic :
- `orders/create`, `orders/paid`, `orders/fulfilled`: "Requires at least one of the following scopes: read_orders, read_marketplace_orders." (`orders/updated` also exists.)
- `products/update`: "Occurs whenever a product is updated, ordered, or variants are added, removed or updated. Requires the `read_products` scope." **[I] A sale also fires `products/update`.**
- `inventory_levels/update`: "Occurs whenever an inventory level is updated. Requires the `read_inventory` scope."

### Subscribing [V] https://shopify.dev/docs/apps/build/webhooks/subscribe
- Two types: **app-specific** (recommended; "Defined in `shopify.app.toml`" and visible in the Dev Dashboard under Versions > Configuration > Subscriptions) and **shop-specific** (GraphQL Admin API `webhookSubscriptionCreate`).
- Delivery targets: HTTPS URL, Google Cloud Pub/Sub, Amazon EventBridge. "Shopify recommends using Google Pub/Sub".
- Table row "Troubleshooting": app-specific "Failing subscriptions will **not** be deleted by Shopify"; shop-specific "Failing subscriptions will be deleted by Shopify".
- Scopes for shop-specific subscriptions "cannot be set using the Admin API" (set in config or Dev Dashboard).

### Delivery, verification, retries [V]
Sources: https://shopify.dev/docs/apps/build/webhooks/delivery-structure and https://shopify.dev/docs/apps/build/webhooks/verify-deliveries
- HTTPS POST, JSON. Headers: `X-Shopify-Topic`, `X-Shopify-Hmac-Sha256`, `X-Shopify-Shop-Domain`, `X-Shopify-API-Version`, `X-Shopify-Webhook-Id` (dedupe key), `X-Shopify-Triggered-At`. Casing differs between the two pages (`X-Shopify-Hmac-SHA256` on the verify page); "Treat header names as case-insensitive".
- HMAC: "base64-encoded HMAC signature... generated using your app's client secret and the raw request body" (HMAC-SHA256). After rotating the client secret, "it can take up to an hour".
- Timeouts: "one-second connection timeout and a five-second timeout for the entire request"; any response outside 200 range (including 3XX) is an error.
- **Retries: "it retries 8 times over the next 4 hours. After 8 consecutive failures, the subscription is automatically deleted if it was configured using the Admin API."**
- "Shopify doesn't guarantee ordering"; use `X-Shopify-Triggered-At` or payload `updated_at`. "Your app shouldn't rely on receiving data from Shopify webhooks... use reconciliation jobs" with `updated_at` query filters. https://shopify.dev/docs/apps/build/webhooks
- Default payload is "the full REST resource for the topic"; `include_fields` trims it.
- [I] Supabase fit: the Edge Function must verify HMAC on the raw body and return 200 inside 5 s, so insert to a queue table and process async.

### Shopify Flow as a no-code alternative [V]
- Free app. https://help.shopify.com/en/manual/shopify-flow : "Shopify Flow is a free app available on the Basic, Grow, Advanced, and Plus plans... Stores on the Grow, Advanced, and Plus plans can use the Send HTTP Request action."
- Triggers include Order created, Order paid, Order fulfilled, Product variant out of stock, Product variant back in stock, Product variant inventory quantity changed. https://help.shopify.com/en/manual/shopify-flow/reference/triggers
- Actions index includes `Send HTTP request` and `Send internal email`; **no mobile-push action appears in the fetched actions index**. https://help.shopify.com/en/manual/shopify-flow/reference/actions
- [I] Flow is not needed for the dashboard: native webhooks work on every plan. Flow only helps for a no-code email alert; POSTing to the dashboard from Flow needs Grow ($105/mo monthly, $89 yearly).

---

## 8. Shopify: rate limits (verbatim)

Source: https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits [V]
- "Calls to the GraphQL Admin API are limited based on calculated query cost... based on the combination of the app and store."

| Plan | Rate limit |
|---|---|
| Standard | 100 points/second |
| Advanced Shopify | 200 points/second |
| Shopify Plus | 1000 points/second |
| Shopify for enterprise (Commerce Components) | 2000 points/second |

- "A single query may not exceed a cost of 1,000 points". Leaky bucket. The sample response block shows `"maximumAvailable": 1000`, `"restoreRate": 50`, `requestedQueryCost: 101`, `actualQueryCost: 46`.
- **Needs review (X verified, Y not):** per-second figures are verified; the **bucket size per plan** and **which plans count as "Standard"** are not stated. The sample's 1000/50 does not match "Standard = 100/s", so it is an illustrative response, not a plan figure. [I] Basic and Grow are probably "Standard"; confirm from a real `throttleStatus` after install.
- Other limits [V] https://shopify.dev/docs/api/usage/limits : array inputs max 250; pagination caps at 25,000 objects; stores with 500,000 variants limited to 10,000 new variants/day (irrelevant).
- [I] A one-shop dashboard (hundreds of products, tens of orders/day) uses a tiny fraction of 100 points/s.

---

## 9. Shopify as the inventory source of truth: apps for Etsy and eBay

### Shopify Marketplace Connect (formerly Codisto)
Listing: https://apps.shopify.com/marketplace-connect [V]
- Pricing: "Free to install. First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month." https://www.shopify.com/pricing also lists "50 synced marketplace orders per month: Free" on every plan.
- Marketplaces: Amazon, Target Plus (US), Walmart (US), eBay. **Etsy: no new connections** (section 0).
- Syncs: listings, orders, inventory (listing text and Help Center). Orders import into Shopify and "displays in the Orders section of your Shopify admin as though it was placed through your online store", with the marketplace name in the **Channel** field; fulfillment and tracking sync back. https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/manage-orders [V]
- Requirements [V] (https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/requirements): an online store not in private/password mode, an active payment provider, shipping rates set for target countries, a verified eBay seller account.
- Rating [V]: 4.1 from 2,131 reviews; 79% five-star, **15% one-star (309)**. Recent reviews (Sept 2026) report eBay sync stopped working, "Screws up prices and inventory", image upload failures, items listed then removed at price zero. Individual reviews, not verified product behavior.
- **Quantity-1 / one-of-a-kind limitations: no statement found in any fetched Shopify page.** [U] Check how it handles end-of-stock (does quantity 0 end the eBay listing, and how fast).
- Whether imported marketplace orders fire `orders/create` / `orders/paid` and the mobile push: docs say only that they appear "as though it was placed through your online store". [I] they do; not verified.

### Other Etsy/eBay sync apps (vendor listing claims, not verified behavior; fetched 2026-10-26)
| App | Channels | Rating (count) | Price (per listing) | Notable (vendor-stated) | URL |
|---|---|---|---|---|---|
| CedCommerce Etsy Integration | Etsy | 4.5 (1,249), Built for Shopify | Beginner $9/mo (10 products, 1 account, "Shopify to Etsy Inventory Syncing"); Growth $59/mo (1000 Etsy products, 500 orders/mo, 2 accounts); 7-day trial | sync "in real time" | https://apps.shopify.com/etsy-marketplace-integration |
| InfoShore Etsy Integration | Etsy | 4.9 (31), Built for Shopify | Free (5 items, no sync); $19.99 (1,500 items sync); $29.99 (6,000); $59.99 (15,000), per mo | "Automatic inventory sync both ways"; Etsy orders sync to Shopify | https://apps.shopify.com/etsy-importer-2 |
| CedCommerce eBay Integration | eBay | 4.7 (922) | Free (manage/sync 100 products); $19 / $49 / $89 per mo (order sync caps 10 / 100 / 1000 per month) | real-time inventory sync | https://apps.shopify.com/ebay-integration |
| Salestio | Amazon, eBay, Etsy, Walmart, Kaufland | 4.6 (85) | $29 (100 orders/mo, $0.15 per extra order), $49 (250), $79 (500), $199 (3000); 14-day trial | **"Order fetch every 30 minutes"** | https://apps.shopify.com/salestio-integration |
| LitCommerce | Etsy, eBay, Amazon, Walmart, more | 4.8 (976) | $29/mo pay-as-you-go: 1000 listings, 3 channels, price and inventory sync, unlimited orders sync; 7-day trial | "Near-instant sync inventory, price, SKU" | https://apps.shopify.com/litcommerce |

- **Oversell risk for quantity-1 items [I]:** Salestio's own listing says order fetch runs every 30 minutes, i.e. a window of up to 30 minutes in which one single piece can sell on two channels. The selection criterion for any sync app is **sale-to-delist latency across channels**, not price. No fetched listing states a delist latency for Etsy or eBay; test with a real quantity-1 item before paying for a year.
- Shopify's eBay blog (https://www.shopify.com/blog/shopify-ebay-integration, labelled 2026 but 2024-era content) lists CedCommerce, Marketplace Connect and InfoShore's eBay Importer and repeats vendor claims.
- Alternative to buying a sync app [I]: since Etsy offers webhooks, the dashboard could carry the delist logic itself (Etsy `order.paid` -> Shopify inventory mutation; Shopify `orders/paid` -> Etsy `PUT .../inventory`). That is code to own and test; an option, not a recommendation.

---

## 10. Shopify plan pricing and what the mobile app already does

### Plans [V] https://www.shopify.com/pricing (fetched 2026-10-26)
| Plan | Pay monthly | Pay yearly | Card rate | Notes |
|---|---|---|---|---|
| Basic | $39 USD/mo | $29 USD/mo | from 2.9% + 30c | 10 inventory locations; Flow available |
| Grow | $105 USD/mo | $89 USD/mo | from 2.7% + 30c | 5 staff |
| Advanced | $399 USD/mo | $359 USD/mo | from 2.5% + 30c | 15 staff |
| Plus | from $2,300 USD/mo | n/a | from 2.25% + 30c | |

- Trial: "free 3-day trial... After your trial, most plans start at just $0 per month for the first 3 months, then switch to standard monthly pricing."
- **Starter plan: UNVERIFIED.** It is not on shopify.com/pricing. The first-party page https://www.shopify.com/starter shows only "Start for free, keep building for $1/month" with no plan tile or feature list. The "$5/mo" figure comes only from a third-party article (https://www.demandsage.com/shopify-starter-plan/). [I] Starter probably excludes Flow (listed Basic and up) and Marketplace Connect (needs a public online store), so treat Basic as the floor for this project.

### Shopify mobile app (build none of this) [V]
https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details#activate-push-notifications : push notifications in the Shopify app for "Critical alerts, Fulfillments, New orders, Setup tips, Timeline mentions", plus an open-orders badge (iPhone). Email order alerts to staff or any address: https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications . This covers Shopify-originated "new order" pings for free. It does **not** cover Etsy/eBay sale alerts unless those orders are imported into Shopify (then [I] likely yes, unverified), and there are no buy alerts or cross-channel dashboard.

---

## Discrepancies and items needing review (X verified, Y need review)

| Item | Verified | Needs review |
|---|---|---|
| Etsy webhooks on Seller Apps | Webhooks exist; Seller App menu shows "Go to Webhook portal" (GH #1657) | Docs page says "commercial and personal", never names Seller Apps |
| Etsy base URL | Docs, quickstart, webhooks use `https://api.etsy.com/v3/...` | OpenAPI `servers` says `https://openapi.etsy.com` |
| Etsy refresh grant | Table: `refresh_token` | Prose: `refresh_code` |
| Etsy rate-limit numbers | 150 QPS / 100000 QPD are "Example Value" | Real defaults for Seller Apps unpublished; read from portal |
| Etsy header name | `x-remaining-this-secon` as printed | Probably a doc typo |
| Etsy trademark line | Terms section 1 wording is binding | Docs wording differs slightly |
| Etsy Terms source | Wayback 2026-10-12, "Last updated on Aug 18, 2026" | Live page 403 to crawler |
| Marketplace Connect + Etsy | Help Center: no new Etsy connections (x2) | shopify.com blog still recommends it |
| Shopify GraphQL limits | Per-second by plan table | Bucket size per plan; plan-name mapping |
| Shopify Starter | Not on pricing page; /starter shows "$1/month" promo | "$5/mo" is third-party only |
| Shopify HMAC header | `X-Shopify-Hmac-Sha256` | Casing differs between pages (case-insensitive) |
| Shopify "REST legacy" scope | Banner is about new public apps | Status for private integrations unstated |

---

## Recommendation

**Polling vs webhooks, per platform**
- **Etsy**: Seller App (free, own shop). In the Webhook portal subscribe to `order.paid` (sale alert), `inventory.out_of_stock` (sold-out signal for quantity-1 items), `order.canceled`, `order.shipped`, `listing.updated`. Add a **reconciliation poll about every 15 minutes** on `GET .../receipts?min_last_modified=<last_run>` (use `min_last_modified`, not `min_created`, so ship and cancel changes are caught), plus a listings sweep on `GET .../listings?state=active` and `state=sold_out` a few times per hour. That also satisfies the Terms' 6-hour listing freshness rule. Scopes: `listings_r listings_w transactions_r shops_r`.
- **Shopify**: Dev Dashboard app in the same org as the store, GraphQL `2026-10`, client credentials grant. Scopes: `read_orders` + `read_all_orders`, `read_products`, `read_inventory`; add `write_products` / `write_inventory` only if the dashboard creates listings or sets quantity. Use **app-specific** webhook subscriptions (set in the version config; not deleted on failure) for `orders/create`, `orders/paid`, `orders/fulfilled`, `products/update`, `inventory_levels/update`, plus a scheduled `updated_at` reconciliation query (Shopify's own guidance).
- Both: Supabase Edge Function receivers verify the signature on the raw body, insert into a queue table, return 200 fast (Shopify limit is 5 s), dedupe on `webhook-id` / `X-Shopify-Webhook-Id`.

**Is Shopify the single source of truth?** Viable only if Etsy reaches Shopify by a route that is not Marketplace Connect (which cannot add Etsy). Options: (a) a third-party sync app chosen by measured sale-to-delist latency on a quantity-1 test item; (b) the dashboard doing the cross-channel delist using the webhooks above. Until one is proven, the lower-risk first build is a read-only dashboard that reads Etsy and Shopify directly (eBay handled separately): no sync writes, no oversell logic yet. Do not make Shopify the hub before delist latency is measured.

**Which apps to pay for** (no winner named yet)
- eBay <-> Shopify: Marketplace Connect is the only first-party option and cheap (first 50 synced orders/mo free, then 1% capped at $99), but note the 15% one-star share and the Sept 2026 eBay sync complaints. Trial on a few real items first.
- Etsy <-> Shopify: shortlist CedCommerce ($9 to $59), InfoShore ($19.99 to $59.99), LitCommerce ($29, also covers eBay). Pay for none until a quantity-1 delist-latency test passes.
- Shopify plan: Basic ($39/mo, or $29 yearly) is the floor. Flow adds nothing the dashboard needs.
- Do not build: Shopify native mobile push for new orders and fulfillments.

---

## Open questions

1. **Etsy Terms #24/#25 vs a private sales dashboard.** Email developer@etsy.com: does a Seller App displaying the shop's own sales and analytics breach "for purposes of analytics"? Also ask about retention of sales history in our own DB.
2. **Do webhooks work on a Seller App?** Confirm in the portal at app creation; if not, the 15-minute poll is the only path.
3. **Actual Etsy QPS/QPD** for a Seller App (Developer Portal).
4. **Shopify protected customer data**: is a Dev Dashboard merchant-org app exempt (the "Custom app: Always available" row), or must we select fields and be approved? Otherwise buyer name/address are redacted.
5. **Do marketplace-imported orders** (Marketplace Connect or a third-party app) fire `orders/create` / `orders/paid` and the mobile push? Test with one eBay order.
6. **Quantity-1 delist latency** for each candidate sync app (Etsy and eBay sides). No fetched source states it.
7. **Can a `sold_out` Etsy listing be restocked** via `PUT .../inventory`, or must it be renewed? Does a relist cost a new listing fee? (Fees are not in the API docs.)
8. Is `shipping_profile_id` / `readiness_state_id` required in practice to publish a physical Etsy listing via API?
9. **Org creation**: exact steps to place the new store in the Dev Dashboard organization (same-org rule).
10. Starter plan: does it exist today, and does it allow Flow or third-party sync apps?
11. Does `openapi.etsy.com` work, or only `api.etsy.com`?

---

## Appendix: raw file to source URL (fetched 2026-10-26 unless noted)

Prefix every file name with `research/dashboard/raw/etsy-shopify-`. `*` marks third-party or secondary sources.

| Raw file suffix | Source URL |
|---|---|
| etsy-docs-home.md | https://developers.etsy.com/documentation/ |
| etsy-auth.md | https://developers.etsy.com/documentation/essentials/authentication |
| etsy-ratelimits.md | https://developers.etsy.com/documentation/essentials/rate-limits |
| etsy-webhooks.md | https://developers.etsy.com/documentation/essentials/webhooks/ |
| etsy-quickstart.md | https://developers.etsy.com/documentation/tutorials/quickstart |
| etsy-openapi.json | https://www.etsy.com/openapi/generated/oas/3.0.0.json |
| etsy-api-terms-wayback.md | https://web.archive.org/web/20261012174138/https://www.etsy.com/legal/api (live URL returned 403) |
| etsy-gh1647-seller-api.md | https://github.com/etsy/open-api/discussions/1647 |
| etsy-gh1657-commercial.md | https://github.com/etsy/open-api/discussions/1657 |
| etsy-gh1764-commercial.md * | https://github.com/etsy/open-api/discussions/1764 |
| vorplabs-etsy.md * | https://vorplabs.com/agent-tools/etsy-api |
| etsy-ratelimit-thirdparty.md * | https://github.com/J-DTurner/etsy-api-skill/blob/main/skills/etsy-api/references/04_rate_limits.md (no default numbers) |
| shopify-admin-rest.md | https://shopify.dev/docs/api/admin-rest |
| shopify-versioning.md | https://shopify.dev/docs/api/usage/versioning |
| shopify-ratelimits.md | https://shopify.dev/docs/api/usage/rate-limits (redirects to /usage/limits) |
| shopify-graphql-ratelimits.md | https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits |
| shopify-access-scopes.md | https://shopify.dev/docs/api/usage/access-scopes |
| shopify-protected-customer-data.md | https://shopify.dev/docs/apps/launch/protected-customer-data |
| shopify-legacy-custom-apps-changelog.md | https://shopify.dev/changelog/posts/legacy-custom-apps-can-t-be-created-after-january-1-2026 |
| shopify-admin-token.md | https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/generate-app-access-tokens-admin |
| shopify-devdash-create.md | https://shopify.dev/docs/apps/build/dev-dashboard/create-apps-using-dev-dashboard |
| shopify-client-credentials.md | https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant |
| shopify-webhooks.md | https://shopify.dev/docs/apps/build/webhooks |
| shopify-webhooks-subscribe.md | https://shopify.dev/docs/apps/build/webhooks/subscribe |
| shopify-webhooks-delivery-structure.md | https://shopify.dev/docs/apps/build/webhooks/delivery-structure |
| shopify-webhooks-verify.md | https://shopify.dev/docs/apps/build/webhooks/verify-deliveries (the /webhooks/subscribe/https and /ignore-duplicates URLs redirected here) |
| shopify-webhooks-reference.md | https://shopify.dev/docs/api/webhooks |
| shopify-webhook-topic-enum.md | https://shopify.dev/docs/api/admin-graphql/latest/enums/WebhookSubscriptionTopic |
| shopify-flow-overview.md | https://help.shopify.com/en/manual/shopify-flow |
| shopify-flow-triggers.md | https://help.shopify.com/en/manual/shopify-flow/reference/triggers |
| shopify-flow-actions.md | https://help.shopify.com/en/manual/shopify-flow/reference/actions |
| shopify-marketplace-connect.md | https://apps.shopify.com/marketplace-connect |
| shopify-help-marketplace-connect.md | https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect |
| shopify-help-mc-requirements.md | https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/requirements |
| shopify-help-mc-orders.md | https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/manage-orders |
| shopify-help-mc-products.md | https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/products |
| mc-ebay-quickstart.md | https://www.shopifymarketplaceconnecthelp.com/hc/en-us/articles/7241542309391-Quick-start-guide-for-eBay |
| shopify-blog-etsy-and-shopify.md * | https://www.shopify.com/blog/etsy-and-shopify |
| shopify-blog-ebay-integration.md * | https://www.shopify.com/blog/shopify-ebay-integration |
| app-cedcommerce-etsy.md | https://apps.shopify.com/etsy-marketplace-integration |
| app-infoshore-etsy.md | https://apps.shopify.com/etsy-importer-2 |
| app-cedcommerce-ebay.md | https://apps.shopify.com/ebay-integration |
| app-salestio.md | https://apps.shopify.com/salestio-integration |
| app-litcommerce.md | https://apps.shopify.com/litcommerce |
| shopify-pricing.md | https://www.shopify.com/pricing |
| shopify-starter.md | https://www.shopify.com/starter |
| demandsage-starter.md * | https://www.demandsage.com/shopify-starter-plan/ |
| shopify-help-order-details-push.md | https://help.shopify.com/en/manual/fulfillment/managing-orders/managing-order-details |
| shopify-help-staff-notifications.md | https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications |

Handling note: the raw pages contain vendor-doc example tokens (Etsy example keystring and access tokens, Shopify example `f85632...`). A secrets grep will flag them; they are documentation samples, not real secrets. Nothing here has been committed or pushed.
