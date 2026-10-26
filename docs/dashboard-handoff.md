# Build handoff: Hollywood and Vine ops dashboard

For the next Claude Code session. Written 2026-10-26 after the research and design pass; nothing is
built yet. Read in this order, then start at section 0:

1. `docs/dashboard-design.md` (what and why; decisions already made, do not relitigate them)
2. `research/dashboard/09-contract-sheet.md` (every endpoint, header, scope, algorithm, limit; copy values from it, never from memory; its "Conflicts" and "smoke-test" sections are the Step 0 script)
3. `research/dashboard/06-data-model-metrics.md` (the DDL, fee estimator, metric SQL, ingest rules; all tested in PGlite)
4. `research/dashboard/07-ui-ux-frontend.md` (screens, wireframes, copy, tokens, the exact install line, the three shadcn edits)
5. `research/dashboard/10-compliance-security-reliability.md` section 4 (C1 to C50) and `08` sections 2, 3, 4, 5 (what to lift from Supabase examples and FlipWatch, the Claude draft request shape and schema, the comps rule)

House rules that apply: Vendor First (anything not on the contract sheet gets a `tools/crawl.sh`
before it ships), Plan Mode First, ponytail (fewest files, raw `fetch`, no framework for four
routes), shell syntax matches the tool, Claude pushes (pathspec adds only; `site/` belongs to the
storefront session; never `git add -A`). Secrets never enter the repo: `.env.local` is gitignored
and mirrors the desk `.env`.

## 0. Prerequisites: what only Ricky can do

None of these keys exist yet (`.env.local` was checked by name on 2026-10-26). The build cannot start
until the first four are done; the rest can land during Phase 1.

| # | Account | What to create | Values to put in the desk `.env`, then `.env.local` |
|---|---|---|---|
| 1 | **eBay** developer.ebay.com, signed in as the seller account | Production keyset. Then Application Keys > Notifications: marketplace account deletion endpoint URL (from task T2) and a verification token (32 to 80 chars). A RuName (redirect URL name) for the user-consent flow. | `EBAY_CLIENT_ID` (App ID), `EBAY_CLIENT_SECRET` (Cert ID), `EBAY_DEV_ID`, `EBAY_RUNAME`, `EBAY_VERIFICATION_TOKEN` |
| 2 | **Etsy** developers.etsy.com, needs a live Etsy shop | Seller App (free, own shop, approved within minutes). Application purpose, verbatim: "creating and publishing listings for my own shop, plus sales and inventory reporting and sold or low-stock alerts". Callback URL. Webhook portal: endpoint (task T3) and its signing secret. In the shop itself: one shipping profile and one return policy (the API drafts reference their ids). | `ETSY_KEYSTRING`, `ETSY_SHARED_SECRET`, `ETSY_SHOP_ID`, `ETSY_WEBHOOK_SECRET` (`whsec_...`) |
| 3 | **Shopify** dev.shopify.com Dev Dashboard | An organization that contains the store, then an app in that same org (admin-created custom apps ended 2026-01-01). Scopes: `read_orders`, `read_all_orders`, `read_products`, `read_inventory`. | `SHOPIFY_SHOP_DOMAIN`, `SHOPIFY_CLIENT_ID`, `SHOPIFY_CLIENT_SECRET` |
| 4 | **Supabase** existing org | New project, **Pro**, nearest US region, name `hv-desk`. Enable `pg_cron`, `pg_net`; Vault is on by default. Auth: custom SMTP (Resend) before the first login test; after Ricky's user exists, turn "Allow new users to sign up" off and set `raw_app_meta_data.shop_role = 'owner'` on his user. MFA on the Supabase account. | `SUPABASE_PROJECT_REF`, `SUPABASE_SECRET_KEY` (`sb_secret_...`, server only), `VITE_SUPABASE_URL`, `VITE_SUPABASE_PUBLISHABLE_KEY` |
| 5 | **Domain** | Pick the dashboard hostname now (manifest id, auth redirects, CSP and any passkey bind to it). DNS at Cloudflare if hosting there. | `DASHBOARD_ORIGIN` |
| 6 | **Pushover** | Buy the app ($4.99), create an application "HV Desk". | `PUSHOVER_APP_TOKEN`, `PUSHOVER_USER_KEY`; `NTFY_TOPIC` = the topic the fleet alerting already uses (desk `.env`) |
| 7 | **Resend** | Verify the sending domain, create SMTP credentials; paste them into Supabase Auth SMTP settings (not into the repo). | none in the repo |
| 8 | **Healthchecks.io** | Free account; one check per scheduled job is created during T4. | `HC_PING_BASE` (the account's ping URL prefix) |
| 9 | **Crosslister** | Start the Crosslist trial (20 free listings). Connect Etsy, eBay and Shopify; confirm it imports an existing Etsy listing from the phone app (its docs: "bulk import your existing inventory from any marketplace", `raw/ui-crosslist-features-mobile.md`). Put the same SKU string (`items.sku`) in each listing's custom label / SKU field. Independent of the build. | none |
| 10 | **Anthropic** console.anthropic.com | An API key in a workspace for this project with a monthly spend limit (about $10 covers thousands of drafts). Needed for T6b only. | `ANTHROPIC_API_KEY`, and `ANTHROPIC_WORKSPACE_ID` if the key is not workspace-scoped (`08` section 4) |

Add every name above to `.env.example` (names only) when the key lands.

## 1. Step 0: smoke tests, in order

Run these before writing feature code; each resolves an UNVERIFIED line in the contract sheet. Record
results in `research/dashboard/smoke-<YYYYMMDD>.md`: the call, the HTTP status, the relevant response
fields, never a token. The full script with exact parameters is `09` > "Unverified items the builder
must smoke-test first"; this is the checklist.

1. **eBay Browse in production with a standard keyset.** Mint an app token (client credentials, scope `https://api.ebay.com/oauth/api_scope`), then `GET /buy/browse/v1/item_summary/search?q=vintage%20lamp&limit=1` with header `X-EBAY-C-MARKETPLACE-ID: EBAY_US`. 200 with `itemSummaries`: buy alerts are API-driven, continue. 403 or `invalid_scope`: Phase 1b switches to eBay saved-search email ingestion and Ricky files an Application Growth Check. Then test the full filter string from `09` A3, including `buyingOptions:{AUCTION|FIXED_PRICE}` with `sort=newlyListed` (error 12034 means per-format calls), two `category_ids`, `fieldgroups=EXTENDED`.
2. **eBay deletion endpoint, then topics.** Deploy T2, register it, confirm the challenge passes. Then `GET /commerce/notification/v1/topic/ORDER_CONFIRMATION` and `.../LISTING`: record `authorizationScopes` and `status`. User consent for `sell.fulfillment.readonly`, `sell.fulfillment`, `commerce.notification.subscription`; `createSubscription`; `testSubscription` (expect 202 and a signed POST).
3. **eBay signature.** On the test POST, log raw body and `x-ebay-signature`; verify ECDSA/SHA-1 over (a) the raw body and (b) `JSON.stringify(JSON.parse(raw))`; record which passes and whether the Edge Runtime has `ssl3-sha1` (fallback: WebCrypto with DER to P1363 conversion).
4. **eBay `getOrders`.** `GET https://api.ebay.com/sell/fulfillment/v1/order?limit=1` with the user token (host is `api.`, not `apiz.`; live-probed). Confirm orders for listings made in the eBay app appear with `legacyItemId`.
5. **eBay Trading `GetMyeBaySelling`** with the user token: confirm the OAuth header name the Trading API wants (the sheet marks it unverified) and that app-made listings and their custom labels (SKU) come back.
6. **Shopify client-credentials token** (same-org check), then the orders query from `09` C2 plus `email`, `shippingAddress { name city }`, `customer { id }`. Nulls or an `errors` hash mean protected customer data is redacted: the ingest already tolerates that; do not apply for it. Read `throttleStatus` and `currentAppInstallation.accessScopes`.
7. **Shopify webhook route.** Add app-specific subscriptions in the app version config if the Dev Dashboard allows it; else `webhookSubscriptionCreate` (`uri`, `includeFields`) plus a daily job that lists subscriptions and re-creates any deleted after 8 failures. Send a real `orders/paid`; verify HMAC on the raw body.
8. **Etsy webhooks on the Seller App.** Find "Go to Webhook portal", add the endpoint, press Testing. Log `webhook-id`, `webhook-timestamp`, `webhook-signature`; confirm the `v1,` prefix and space-delimited list, the `whsec_` secret, the required response code.
9. **Etsy limits and refresh.** Read QPS/QPD from the portal and the response headers. Refresh once with `grant_type=refresh_token`; confirm whether a new `refresh_token` returns and persist it. If the token endpoint returns 403 "API key not found", add `x-api-key: <keystring>:<shared_secret>`.
10. **Supabase cron to function.** A 60-second `cron.schedule` calling `net.http_post(url := ..., headers := ..., body := ..., timeout_milliseconds := ...)` with the Vault secret key; the receiver uses `auth: 'secret'`. Confirm a `verify_jwt=false` + `auth: 'none'` receiver answers an anonymous `curl` with 200.
11. **Edge Runtime imports.** Deploy a probe function that imports `npm:fast-xml-parser` (and `npm:web-push` for later) and returns 200. This replaces the local test the research session could not run (no Docker on Windows).
12. **Pushover priority 2, ntfy, Healthchecks.** `priority=2&retry=60&expire=1800`, acknowledge on the phone, poll the receipt; measure latency. ntfy with a non-ASCII title from Deno `fetch` (switch to JSON publish if it mangles). Healthchecks ping body must be exactly `OK`, not `OK (not found)`.
13. **Etsy write path on the Seller App** (needs `listings_w` in the consent). `GET /v3/application/seller-taxonomy/nodes` and pick a vintage clothing node; `GET /v3/application/shops/{shop_id}/shipping-profiles` and the shop return-policies endpoint for the default ids. Then on a throwaway item: `POST /v3/application/shops/{shop_id}/listings` form-encoded (`quantity=1`, `title`, `description`, `price`, `who_made=someone_else`, `when_made=1980s`, `taxonomy_id`, `shipping_profile_id`, `return_policy_id`), one `POST .../listings/{listing_id}/images` multipart, confirm `state=draft` in the Etsy app, then `PATCH .../listings/{listing_id}` with `state=active` (Etsy charges its listing fee once) and immediately `state=inactive`. Record whether publish fails without `shipping_profile_id` or `readiness_state_id` (`02` open question 8). Values: `02` section 3 rows "Create listing (draft)", "Image upload", "Update / publish", from the live spec `raw/etsy-shopify-etsy-openapi.json`.
14. **Claude from the Edge Runtime.** One `POST https://api.anthropic.com/v1/messages` with `claude-haiku-5-5`, `anthropic-version: 2026-10-21`, `thinking: {type: "disabled"}`, the `08` section 4 schema in `output_config.format`, and the image as a 60-second signed Storage URL. If the URL source fails, resend as base64 and record which works. Record `usage` and compare with the `08` cost table.

## 2. Repo layout to create

Inside this repo (a new repo is a structure change and needs Ricky's word):

```
dashboard/
  README.md                       how to run, deploy, rotate a token, restore a backup
  supabase/
    config.toml                   per-function [functions.<name>] verify_jwt = false for receivers
    migrations/
      0001_schema.sql             06 section 1.2 verbatim
      0002_deltas.sql             section 4 below
      0003_cron.sql               cron.schedule rows + Vault secrets (09 D)
    functions/
      _shared/   hmac.ts  redact.ts  ebay.ts  etsy.ts  shopify.ts  pushover.ts  ntfy.ts  hc.ts  db.ts  claude.ts
      webhook-in/index.ts         Etsy, Shopify, eBay notifications; routes by path
      ebay-deletion/index.ts      GET challenge + POST notice
      tick/index.ts               drain events, reconcile, listings, watches, refresh, purge, watchdog
      notify/index.ts             alerts -> Pushover -> ntfy fallback
      list-etsy/index.ts          verify_jwt=true; Claude draft, Etsy draft listing + images, publish (T6b)
      tests/                      deno test: hmac, redact, filters, est_fees via PGlite seed
  web/                            Vite PWA (07 section 3.2 install line)
```

Local tooling present on this machine: Deno 2.7.13, Supabase CLI 2.98.2 (Windows), Node 22+. No
Docker on Windows, so `supabase functions serve` is unavailable here; deploy to the real project and
test there, or run the CLI in WSL (Docker Engine 29 is installed inside WSL).

## 3. Build order

Each task ends with a pathspec commit and push. "Done when" is the acceptance check.

**T1. Schema.** Apply 0001 (06 verbatim) and 0002 (section 4). Re-run 06's seed tests after the
deltas (RLS owner/non-owner, duplicate webhook id, out-of-order upsert, the 24-hour sold-alert rule).
Load `items` from `research/inventory/2026-10-26-catalog.md` with `sku` = catalog id and `fee_rule`
per 06 section 3. Done when the tests pass and `select count(*) from items` matches the catalog.

**T2. `ebay-deletion`.** `verify_jwt=false`, `auth:'none'`. GET: respond `{"challengeResponse": sha256(challengeCode + verificationToken + endpointURL)}` as `application/json`. POST: verify the signature when the public key is cached, else 202 and verify asynchronously; on a verified `MARKETPLACE_ACCOUNT_DELETION`, `update sales set buyer_ref = null where buyer_ref = $username`, strip the user from redacted payloads, insert `deletion_log`. Done when eBay's registration page shows the endpoint verified and a daily self-test (synthetic challenge) is scheduled.

**T3. Ingest.** `webhook-in`: read `await req.text()` first, verify (Etsy HMAC-SHA256 over `id.timestamp.body` with the `whsec_` secret and a 300 s replay window; Shopify HMAC-SHA256 base64 of the raw body with the client secret, header `X-Shopify-Hmac-Sha256`; eBay ECDSA per smoke test 3), `insert into events ... on conflict do nothing`, return 200 inside 5 s, no CORS headers, 405 on other methods, 413 over a body cap. `tick` lane "events": fetch the resource where the payload is thin (Etsy `resource_url`; eBay `orderId` via `getOrders`), redact PII per 06 section 1.5 rule 5, upsert `sales` with the `source_updated_at` guard, match item by listing id then SKU, allocate order-level money pro rata, estimate fees with `est_fees()` and replace with API fees when present (`fee_source`). Reconcile lanes: Etsy receipts `min_last_modified` 15 min; Shopify orders `updated_at` 15 min, own-store only (`sourceName`); eBay `getOrders` `lastmodifieddate` 10 min; daily 7-day sweep. Done when one test order on each channel appears once in `sales` within 15 minutes, a redelivered webhook changes nothing, and an order older than 24 h backfilled from eBay raises no alert.

**T4. Notify and watchdogs.** `notify` drains `alerts where delivered_at is null`: Pushover POST (`09` E1) with `url` = listing, title and body per kind, priority by severity; on non-2xx or an unacknowledged priority-2 receipt after `expire`, ntfy on the existing topic; write `delivered_at` and `delivery`. Quiet hours and cooldown per `dashboard-design.md` section 4. Healthchecks: one check per cron lane, pinged on start, success, fail; grace two cadences. Token watchdog (daily): eBay 60 days before `refresh_token_expires_in`, Etsy at 75 days, Shopify on any token failure; raises `token_expiring` with a re-consent link. Done when a fake `sold` alert reaches the phone in under a minute, a forced Pushover failure arrives via ntfy, and Healthchecks shows every lane green for 24 h.

**T5. Listings and the oversell guard.** Etsy `listing.*` webhooks plus a 3-hour `getListingsByShop` sweep; Shopify `PRODUCTS_UPDATE` plus a 3-hour products query; eBay Trading `GetMyeBaySelling` every 3 hours (raw fetch, `npm:fast-xml-parser`), plus the `LISTING` topic if smoke test 2 showed it subscribable. Upsert `channel_listings` on `(channel, external_id)`, match by SKU then title, stamp `last_seen_at`. Lane "oversell": for each sale in the last 24 h, any other `active` listing on the same item 20 minutes after `sold_at` raises `oversell_risk` (priority 2) once. Done when selling a test item on one channel shows the other channels' status on the Sold card and the alert fires only when the crosslister has not delisted.

**T6. PWA.** Scaffold with 07 section 3.2 (exact versions), make the three shadcn edits (dark mode via `prefers-color-scheme`, 44 px controls, drop `next-themes` and Geist), `registerType: 'prompt'`, `viewport-fit=cover`, real icons, manifest `id` and `start_url` on the final domain. Auth: email OTP with `shouldCreateUser: false`. One Realtime hook (`postgres_changes` on items, channel_listings, sales, watches, candidates, alerts; refetch on `SUBSCRIBED`, `visibilitychange`, `online`). Screens: Today, Alerts (Sold segment first), Inventory with Add sheet (photo, title, cost; SKU generated), Sales, Settings (Pushover test, connections, data health, install help, privacy, Etsy sentence), Item detail. Public `/privacy`. CSP `script-src 'self'`, `connect-src` the Supabase project. Deploy to Cloudflare Pages (SPA fallback) or Vercel Pro. Done when the app is installed on Ricky's phone and the real-phone checklist passes: OTP login inside the installed app, status bar and safe areas, a Pushover link's behaviour, sheets and toasts under the CSP.

**T6b. List from the phone (Phase 1; needs smoke tests 13 and 14).** The Add sheet takes up to ten
photos (resized in the browser to a 1,500 px long edge before upload, stored under
`items/{sku}/{rank}.jpg`), cost, and one `ai_notes` line for what the model cannot see
(measurements, flaws, maker marks). "Draft" calls `list-etsy` (owner JWT), which signs the photo URLs
for 60 s, calls Claude Haiku 5.5 with the `08` section 4 schema (title, description, condition notes,
visible defects, era and maker guesses with confidence, materials, keywords, tags,
`needs_better_photo`; no price), maps the keywords to a `taxonomy_id` through the seller-taxonomy
tree (cached in `integrations`, refreshed weekly), and writes `items.draft`, `draft_model`,
`drafted_at`. Item detail renders the draft with every guess marked and editable; the price is
Ricky's. "Create Etsy draft" posts the listing form-encoded (`quantity=1`, `who_made=someone_else`,
`when_made` from the era guess, the shop's default `shipping_profile_id` and `return_policy_id`,
`tags` up to 13), uploads the images in rank order, inserts `channel_listings` (`etsy`, `listing_id`,
`draft`), and shows the Etsy edit link. "Publish" is a separate labelled tap that sends
`state=active`; the `listing.created` / `listing.updated` webhook and the 3-hour sweep flip the row.
Never publish without the tap; never let the model emit category ids or a price; keep
`needs_better_photo` visible until the photo is replaced. If a 20-item side-by-side shows weak titles
or eras, switch to `claude-sonnet-5-5` with `thinking: {type: "between_tools"}`. Done when one real
item goes from camera to a live Etsy listing on the phone with no typing beyond cost, price and the
notes line, the draft never went live before the Publish tap, Crosslist imports the listing and posts
it to eBay and Shopify from its own app, and `channel_listings` shows the Etsy row `active` from the
webhook.

**T7. Watches (Phase 1b; needs smoke test 1 green).** `tick` lane "watches": claim due rows (`update watches set next_run_at = now() + greatest(cadence, '5 min') where id in (select id from watches where active and (next_run_at is null or next_run_at <= now()) order by next_run_at nulls first limit 10 for update skip locked) returning *`), Browse search per `09` A3 with cursor `itemStartDate:[cursor - 10 min..]`, tier-1 filter (port of FlipWatch `src/lib/engine/filters.ts` at SHA `83870a982dbfb485b4e5e0fcaddf5539fd157a33`, MIT notice kept), insert `candidates` on conflict update price and `last_seen_at`, `buy_match` alert with `fit_reason` from the matched terms, budget guard (4,500/day floor, demote tiers before the cap, read `getRateLimits`). Lane "refresh" every 5 h: `getItem` per live candidate; not found or ended means purge to tombstone. Watches screen with the editor and "Test" (one unsaved run, up to six thumbnails). Alerts Buy segment with Open / Not this (reason chips, Undo) / Bought sheet (creates the item with cost). Done when a real watch finds a real new listing and the push arrives within its cadence, "Bought" creates the inventory row, and a candidate older than 6 h without refresh is hidden.

**T8. Hardening.** `purge_ebay_data()` and `purge_etsy_data()` SQL functions; `deletion_log` re-apply after restore (documented in README); weekly `supabase db dump` off-site with its own Healthchecks check; daily "all green" digest alert; a day of logs reviewed for tokens or bodies (there must be none); `cron.job_run_details` cleanup job. Done when a restore drill on a branch database re-applies `deletion_log` and the dump check is green.

**Phase 2 (separate handoffs, in this order):** Haiku 5.5 tier-2 matching (`thinking` disabled, 20 listings per request, summary fields only, no eBay titles as examples), the comps panel (08 section 5: live, unstored, isolated, links only), saved-search email ingestion, Web Push, second user, and direct eBay and Shopify listing from the same draft (retiring the crosslister) only once T6b has proven the drafts and the import leg is the pain.

## 4. Schema deltas (migration 0002, on top of 06 verbatim)

```sql
-- watches: plain-language description for tier 2, push vs inbox, hot/normal tier, lease for the claim
alter table public.watches
  add column description text,
  add column alert_mode  text not null default 'push' check (alert_mode in ('push','inbox')),
  add column tier        text not null default 'normal' check (tier in ('hot','normal')),
  add column next_run_at timestamptz;
create index watches_due_idx on public.watches (next_run_at) where active;

-- candidates: what the Alerts card shows, plus a hash that survives the purge
alter table public.candidates
  add column fit_reason     text,
  add column fit_score      numeric(4,3) check (fit_score between 0 and 1),
  add column starred        boolean not null default false,
  add column dismiss_reason text check (dismiss_reason in ('wrong_item','too_expensive','bad_condition','bad_seller','already_have')),
  add column fingerprint    text;   -- sha256(seller | normalized title | price bucket); relists get new ids

-- alerts: UI-owned "seen", separate from the push-receipt "acked"
alter table public.alerts add column seen_at timestamptz;
create index alerts_unseen_idx on public.alerts (created_at desc) where seen_at is null;
grant update (acked_at, seen_at) on public.alerts to authenticated;

-- items: generated SKU; unknown cost (NULL) is not free cost (0)
create sequence public.items_sku_seq;
alter table public.items alter column sku set default ('HV-' || lpad(nextval('public.items_sku_seq')::text, 4, '0'));
alter table public.items drop column cost_basis;
alter table public.items alter column cost_purchase drop not null, alter column cost_purchase drop default;
alter table public.items add column cost_basis numeric(12,2)
  generated always as (coalesce(cost_purchase, 0) + cost_other) stored;
-- 06's "cost missing" reads become: cost_purchase is null  (update m3, m9, a1 and the UI asterisk accordingly)

-- items: what Ricky told the model, the Claude draft, which model, when (T6b)
alter table public.items
  add column ai_notes    text,
  add column draft       jsonb,
  add column draft_model text,
  add column drafted_at  timestamptz;

-- deletion_log: proof of eBay / Shopify deletion handling; must be re-applied after any restore
create table public.deletion_log (
  id              bigint generated always as identity primary key,
  source          text not null check (source in ('ebay','shopify','etsy','manual')),
  subject_ref     text not null,            -- ebay username or userId, shopify customer id
  notification_id text,
  received_at     timestamptz not null default now(),
  applied_at      timestamptz,
  rows_affected   int,
  note            text
);
alter table public.deletion_log enable row level security;
revoke all on public.deletion_log from anon, authenticated;
create policy owner_read on public.deletion_log for select to authenticated using ((select public.is_owner()));
grant select on public.deletion_log to authenticated;
```

Change 06's `a3_purge_ended_candidates` so a purged row keeps only `watch_id`, `external_id`,
`status = 'ended'`, `fingerprint`, `found_at`, and nulls `title`, `price`, `shipping`, `condition`,
`url`, `image_url`, `fit_reason`, `raw`.

## 5. Function contracts (pointers; copy values from `09`)

| Function | Auth | Does | Sheet |
|---|---|---|---|
| `webhook-in` | `verify_jwt=false`, `auth:'none'`, vendor signature | raw body, verify, `events` insert, 200 | A5 (eBay), B4 (Etsy), C3 (Shopify), D |
| `ebay-deletion` | same | challenge hash, notice redaction, `deletion_log` | A5.3 |
| `tick` | `auth:'secret'` from pg_cron via Vault key | lanes: events, reconcile-etsy, reconcile-shopify, reconcile-ebay, listings, oversell, watches, refresh, watchdog, digest; each lane pings its Healthchecks check and pages its work under the Edge wall-clock and 2 s CPU limits | A2 to A4, B2 to B3, C1 to C2, D, E3 |
| `notify` | `auth:'secret'` (DB webhook on `alerts` insert, plus a 1-minute sweeper) | Pushover then ntfy fallback | E1, E2 |
| `list-etsy` | `verify_jwt=true`, owner JWT (`shop_role = 'owner'`) | sign photo URLs, Claude draft (structured output), taxonomy map, Etsy draft + images, publish on request | `08` section 4 (Claude); `02` section 3 write rows and `raw/etsy-shopify-etsy-openapi.json` (Etsy; not on `09`, so the smoke test 13 record becomes the contract) |

Tokens: static vendor secrets in Edge Function secrets; rotating OAuth state in Vault, refreshed by
one writer under an advisory lock, new refresh token persisted in the same transaction, cached eBay
app token (7,200 s, 1,000 mints/day cap). Browser gets the publishable key only.

## 6. Do not build

A crosslister beyond the one Etsy draft step, a delist engine or a repricer. Direct eBay or Shopify listing in v1. Any auto-publish path. A customers table or any buyer PII. Average sold price,
deal score, "typical price", or any number computed from eBay content. Embeddings or few-shot prompts
built from eBay titles. Scrapers for eBay or for any site on `10` C23's banned list. Pull-to-refresh.
An offline write queue (revisit only if Ricky logs purchases with no signal). A chart library.
TanStack Query. Facebook anything. Anything on the Fedora box in v1.

## 7. Verification before calling v1 done

- `deno test` green for hmac, redact, filters, and the 06 seed suite after deltas.
- One real sale per channel appears once in `sales`, pushes once, shows the other channels' status.
- Healthchecks green for every lane for 24 hours; a deliberately broken lane pages within two cadences.
- eBay deletion self-test green; a synthetic `MARKETPLACE_ACCOUNT_DELETION` nulls `buyer_ref` and writes `deletion_log`.
- A watch finds a real listing within its cadence; "Bought" creates the item; candidates older than 6 h without refresh are hidden; an ended listing is purged to a tombstone.
- The app is installed on the phone, OTP login works inside it, dark mode follows the OS, every control is 44 px, no eBay card ever appears in Recent or a mixed list.
- One real item listed from the phone end to end (camera to live Etsy listing, then Crosslist to eBay and Shopify); the draft never went live without the Publish tap; the model never produced a price or a category id.
- `git grep` of `dashboard/` for tokens, signatures, buyer fields: nothing. `.env.example` lists every name.
- `CLAUDE.md` status line updated; `/compile` the smoke-test file and this handoff's outcome into the desk wiki.

## 8. Open questions and who answers

| Question | Who | Default if unanswered |
|---|---|---|
| iPhone or Android | Ricky | iPhone |
| Dashboard domain | Ricky | blocks T6 install; everything else proceeds |
| Cloudflare or Vercel Pro | Ricky | Cloudflare Pages |
| Crosslister pick after the quantity-1 delist test | Ricky | Crosslist Gold; the dashboard does not depend on it |
| Watch count, categories, auctions, quiet hours | Ricky | seed three watches from `research/pricing`, auctions on, 22:00 to 07:00 ET |
| Etsy shop live? Shopify plan? eBay keyset identity? | Ricky | blocks the respective smoke tests only |
| Browse production access, notification topics, signature bytes | smoke tests 1 to 3 | fallback paths named in section 1 |
| Shopify protected data on a merchant-org Dev Dashboard app | smoke test 6 | ingest tolerates nulls either way |
| Etsy Terms #25 vs an own-shop dashboard | email developer@etsy.com (Ricky sends) | register with the precise purpose and proceed |
| Edge Runtime and `fast-xml-parser` / `web-push` | smoke test 11 | `ebay-api` npm as the XML fallback |
| Etsy publish without `shipping_profile_id` / `readiness_state_id` | smoke test 13 | always send the shop defaults |
| Anthropic fetching a signed Storage URL | smoke test 14 | base64 of the resized JPEG |
| Anthropic API key | Ricky | blocks T6b only |
| CPA: inventory accounting method | Ricky's CPA | cash-basis COGS at sale (`m7`), not blocking |
