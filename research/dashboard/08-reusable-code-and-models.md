# 08. Reusable code and models for the Hollywood and Vine dashboard

Date: 2026-10-26. Author: research agent (wave 2). Scope: library reuse tested on local Deno 2.7.13, official Supabase examples, a FlipWatch read, AI listing drafting from photos, and a license-compliant eBay comps panel. Nothing was built in the repo and nothing was committed.

Tags: **VERIFIED** = run on this machine today, or read on a live vendor page or repo file today (path or URL given). **UNVERIFIED** = inference, memory, or not run. **BLOCKED** = attempted and refused by the permission system.

## 0. Bottom line

- **Libraries: raw `fetch` wins almost everywhere.** `ebay-api`, both Shopify clients, both Etsy clients, `hono`, `web-push` and `@supabase/server` all load under Deno 2.7.13. None is needed for v1 except `web-push`, and only if Web Push (phase 2) happens. Pushover, ntfy, Healthchecks, Etsy and Shopify HMAC are about five lines each (section 1.2; snippets type-checked with `deno check`, the HMAC one has a pass/fail self-test).
- **Edge Runtime is still UNTESTED.** Supabase CLI 2.98.2 is installed on Windows, Docker is not. Docker Engine 29.7.2 runs inside WSL Ubuntu, and getting a Linux CLI there needs an external binary download, which the permission classifier refused (section 1.3). A ready probe function is staged for a one-command run.
- **FlipWatch (MIT, 11 days old) is worth lifting from file by file**, never as a dependency: query parsing, price-drop rules, the lease-based poll claim, backoff, Pushover/ntfy request builders, a 113-line push-only service worker. Pinned SHA `83870a982dbfb485b4e5e0fcaddf5539fd157a33`. Its price-check path feeds eBay prices to an LLM, which our license forbids (section 5).
- **AI drafting from one 1 MP photo costs about $0.00036 on Haiku 5.5 and $0.0072 on Sonnet 5.5** with thinking off (section 4). An unresized phone photo costs roughly 2x to 4x the image part. A local VLM on the Fedora box is not worth it.
- **The eBay license is stricter than report 01 says.** New in this pass: Section 9 item 5 bans using eBay Content "to suggest or model prices for items listed on eBay Site" (Ricky lists on eBay); the Public Display clause requires eBay content to be visually isolated from non-eBay content; Section 9 item 10 bans using it to train AI. The compliant comps panel is a live, unstored, isolated list of active asking prices with links, plus a link-out to eBay's own sold search. No computed price anywhere.

## 1. Libraries

### 1.1 Table (all Deno results VERIFIED today with `deno run -A --quiet` on Deno 2.7.13; scripts are in the scratchpad `reuse/` dir)

| Name | Version | Licence (npm / GitHub) | Last publish (npm) | Loads in Deno 2.7.13 via `npm:`? | Edge Runtime tested? | Verdict |
|---|---|---|---|---|---|---|
| `ebay-api` (hendt) | 10.0.2 | MIT / MIT | 2026-10-14 | YES. Constructs; `buy.browse.search` and `sell.fulfillment.getOrders` are functions, `commerce.notification` and `trading` are objects. `OAuth2.getApplicationAccessToken()` against the sandbox with fake creds returns "Request failed with status code 401", so the axios transport works. | NO | **SKIP for v1.** Raw fetch covers token mint, Browse and getOrders. 3.8 MB unpacked; deps axios, qs, debug, fast-xml-parser; `engines.node>=22`. Keep it as the escape hatch if Trading XML (`GetMyeBaySelling`) becomes necessary (report 01 section 2.4). |
| `@shopify/admin-api-client` | 2.0.1 | MIT / MIT | 2026-10-08 | YES. `createAdminApiClient({storeDomain, apiVersion, accessToken})` builds `https://<shop>.myshopify.com/admin/api/<ver>/graphql.json`; `request`, `fetch`, `getHeaders` present. | NO | **SKIP** (optional nicety). 218 KB, one dep. A GraphQL POST is five lines. Which `apiVersion` is current: report 02 section 6, not retested. |
| `@shopify/shopify-api` | 15.0.1 | MIT / MIT | 2026-10-08 | YES, after `import "npm:@shopify/shopify-api@15.0.1/adapters/web-api"`. Prints INFO banners on load. | NO | **SKIP.** Built for embedded apps (sessions, billing, flow). The one thing we would use, webhook HMAC validation, is six lines (1.2). The admin client above would already be enough if GraphQL helpers were wanted. |
| Etsy v3 client A: `etsy-ts` | 8.0.1 | **ISC** (npm) vs **MIT** (GitHub): mismatch | 2026-08-15 | YES. Exports an `Etsy` class with v3-shaped resource groups (`Shop`, `ShopListing`, `Payment`, `LedgerEntry`...). Deps axios, axios-auth-refresh. 44 stars, 1 open issue. | NO | **SKIP** |
| Etsy v3 client B: `@profplum700/etsy-v3-api-client` | 4.1.0 | MIT (npm) vs **none** (GitHub shows no licence): mismatch | 2026-10-24 | YES (90 exports). Constructor throws without `sharedSecret`. 1 star, created 2025-07-14, ships `@eslint/js` as a runtime dependency. | NO | **SKIP** |
| any other Etsy v3 TS client | | | | npm search "etsy" (top 20) and GitHub searches ("etsy open api v3", "etsy typescript", "etsy-api client") found nothing else maintained in TypeScript; best GitHub hit is `aserper/etsy-mcp` (10 stars), an MCP server, not a client. | | **raw fetch** |
| `web-push` | 3.6.7 | **MPL-2.0** (npm) vs NOASSERTION (GitHub API) | **2024-01-16** (stale, but 3,568 stars and pushed 2026-10-26) | YES. Offline: `generateVAPIDKeys`, `setVapidDetails`, `generateRequestDetails` with real P-256 subscription keys returns an aes128gcm body (115 bytes) plus TTL, Content-Encoding, Authorization, Urgency headers. Online: `sendNotification` to a local TLS server returned **201**; the server saw `content-encoding: aes128gcm` and `authorization: vapid t=...`. (My first attempt hung up because of the self-signed test certificate, not the library; a control run with plain `node:https` failed the same way. Passing `{agent: new https.Agent({rejectUnauthorized:false})}` fixed the harness.) | NO | **USE later, only if Web Push phase 2 ships** (FlipWatch depends on it too). MPL-2.0 is file-level copyleft, fine as an unmodified dependency. Alternative: `jsr:@negrel/webpush` (report 05). |
| `hono` | 4.13.14 (npm and JSR `@hono/hono` identical) | MIT / MIT | 2026-10-25 | YES via `npm:hono@4.13.14` and `jsr:@hono/hono@4.13.14`; `new Hono().basePath(...)` and `app.fetch(new Request(...))` returned 200. | NO | **SKIP for 4 routes** (etsy, shopify, ebay webhooks, tick): `export default { fetch(req) { switch (new URL(req.url).pathname) ... } }` is shorter than a framework. Supabase's routing doc uses `jsr:@hono/hono@^4` with `export default { fetch: app.fetch }` and says paths must start with the function name (`raw/reuse-sb-fn-routing.md`). Adopt only if routes grow. |
| `@supabase/server` | 1.9.2 | MIT | 2026-10-12 | YES. `withSupabase({auth: 'none'})` handled a POST; `auth: 'secret'` returned 401 with no key. Outside the platform it needs `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY` env (else 500 `MISSING_DEFAULT_PUBLISHABLE_KEY`). | NO | **OPTIONAL.** Every migrated official example uses it (section 2). Saves hand-rolling the pg_cron secret check (`auth: 'secret'`). |

Import times were noisy between runs (hono 12 ms then 277 ms, etsy-ts 32 ms then 496 ms), so there is no timing column. Edge Runtime cold-start cost was not measured.

### 1.2 Raw fetch is enough (type-checked with `deno check`; request shapes from the raw vendor pages named)

Pushover (`raw/arch-pushover-api.md`: POST `https://api.pushover.net/1/messages.json`; required `token`, `user`, `message`; limits message 1024, title 250, url 512, url_title 100; priority 2 needs `retry` >= 30 and `expire` <= 10800). VERIFIED.

```ts
await fetch("https://api.pushover.net/1/messages.json", { method: "POST",
  body: new URLSearchParams({ token: PUSHOVER_APP_TOKEN, user: PUSHOVER_USER_KEY, title, message, url, priority: "1" }) });
```

ntfy (`raw/arch-ntfy-publish.md`: "To publish as JSON, you must PUT/POST to the ntfy root URL, not the topic URL"; `topic` is the only required field). VERIFIED.

```ts
await fetch("https://ntfy.sh/", { method: "POST",
  body: JSON.stringify({ topic: NTFY_TOPIC, title, message, click: url, priority: 4, tags: ["moneybag"] }) });
```

Healthchecks (`raw/reuse-healthchecks-ping-api.md`: "HEAD|GET|POST https://hc-ping.com/<uuid>"; append `/fail` to signal failure; "If you ping a check more than 5 times per minute, some of the requests may get rate limited"). VERIFIED.

```ts
await fetch(`https://hc-ping.com/${HC_UUID}${ok ? "" : "/fail"}`, { method: "POST", body: summary });
```

Etsy (`raw/etsy-shopify-etsy-auth.md`: header `x-api-key: <keystring>:<shared_secret>` on every v3 request; refresh is POST `https://api.etsy.com/v3/public/oauth/token` with `grant_type=refresh_token`, `client_id=<keystring>`, `refresh_token`; access token life 1 hour, refresh token 90 days; receipts need scope `transactions_r`; path and `min_last_modified` param confirmed in `raw/etsy-shopify-etsy-openapi.json`). VERIFIED. Doc discrepancy: the prose says `grant_type=refresh_code`, the parameter table and example say `refresh_token`; use `refresh_token`. UNVERIFIED: whether the token endpoint also wants `x-api-key`, and whether each refresh rotates the refresh token (persist the new one regardless; report 05 puts it in Vault).

```ts
const etsy = async (path: string, token: string) => {
  const r = await fetch(`https://api.etsy.com/v3/application${path}`,
    { headers: { "x-api-key": `${KEYSTRING}:${SHARED_SECRET}`, Authorization: `Bearer ${token}` } });
  if (!r.ok) throw new Error(`etsy ${r.status} ${await r.text()}`);
  return r.json();
};
const receipts = await etsy(`/shops/${shopId}/receipts?min_last_modified=${since}&limit=100`, accessToken);
const fresh = await fetch("https://api.etsy.com/v3/public/oauth/token", { method: "POST",
  body: new URLSearchParams({ grant_type: "refresh_token", client_id: KEYSTRING, refresh_token }) }).then((r) => r.json());
```

Shopify webhook HMAC (report 02 section 7: header `X-Shopify-Hmac-Sha256`, base64 HMAC-SHA256 of the raw body keyed with the app client secret). VERIFIED by a round-trip self-test (a good signature verifies, a body with one added space fails). Wrap `atob` in try/catch for a malformed header.

```ts
const raw = new Uint8Array(await req.arrayBuffer());             // raw body first, parse JSON after
const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(SHOPIFY_CLIENT_SECRET), { name: "HMAC", hash: "SHA-256" }, false, ["verify"]);
const sig = Uint8Array.from(atob(req.headers.get("x-shopify-hmac-sha256") ?? ""), (c) => c.charCodeAt(0));
const valid = await crypto.subtle.verify("HMAC", key, sig, raw);  // constant-time compare
```

eBay application token (FlipWatch `src/lib/marketplaces/ebay/auth.ts` does exactly this with `Buffer`; swap in `btoa`; grant types in report 01 section 4). Not run live (no credentials).

```ts
const t = await fetch("https://api.ebay.com/identity/v1/oauth2/token", { method: "POST",
  headers: { Authorization: `Basic ${btoa(`${APP_ID}:${CERT_ID}`)}`, "Content-Type": "application/x-www-form-urlencoded" },
  body: `grant_type=client_credentials&scope=${encodeURIComponent("https://api.ebay.com/oauth/api_scope")}` }).then((r) => r.json());
// { access_token, expires_in }. Cache the token in Postgres, not in memory: Edge workers are not durable.
```

### 1.3 Supabase Edge Runtime: UNTESTED

- **State of the box (VERIFIED):** `supabase --version` = 2.98.2 (Windows, `C:\Users\ethan\.supabase\bin`). `docker`, `podman`, `nerdctl` are not found on Windows (Git Bash or PowerShell). `wsl.exe` shows an Ubuntu distro with Docker Engine 29.7.2 running (14 containers, one up, unrelated to this work; I ran read-only `docker info`, `ps`, `images` there and nothing else). The Windows CLI cannot reach it.
- **What I tried:** download the matching Linux CLI (`supabase_linux_amd64.tar.gz`, v2.98.2) from GitHub releases into WSL and run `supabase functions serve` there. **BLOCKED:** the permission classifier denied downloading and executing an external binary. I did not work around it (no Docker Desktop install, no `docker run` of the edge-runtime image).
- **To unblock (your call):** approve that download, or install Docker Desktop (then the Windows CLI works), or run it yourself in WSL. The probe imports the exact tested specifiers, constructs each client, runs the web-push ECDH encryption, makes one sandbox call to eBay with fake creds (expects 401) and returns JSON per step. It passes under local Deno 2.7.13 (all five steps OK).
  - Probe: `C:\Users\ethan\AppData\Local\Temp\claude\C--Users-ethan-dev-Vintage\634dc484-d184-46e6-a7b4-91d20e747c83\scratchpad\reuse\edge-probe\supabase\functions\probe\index.ts`
  - Run: copy it into a scratch project's `supabase/functions/probe/`, then `supabase functions serve probe --no-verify-jwt` and `curl localhost:54321/functions/v1/probe`. Whether `functions serve` also needs `supabase start` first: UNVERIFIED.
- **What the docs say instead (VERIFIED, https://supabase.com/docs/guides/functions/dependencies, `raw/reuse-sb-fn-dependencies.md`):** Edge Functions support npm modules, built-in Node APIs (via Deno's Node compatibility), JSR and deno.land/x; use `npm:` specifiers and a per-function `deno.json`. The page lists no npm-specific limitations or unsupported packages (I grepped it for "not supported" and "limitation" and found nothing relevant); for what Node APIs work it points to Deno's Node compatibility page, https://docs.deno.com/runtime/manual/node/compatibility, which I did not fetch. Limits (`raw/arch-sb-fn-limits.md`): 256 MB memory, **2 s CPU per request**, 150 s (free) / 400 s (paid) wall clock, 20 MB bundle via the CLI (5 MB if bundled server-side). Deploy with the CLI so the 20 MB cap applies; `ebay-api` alone is 3.8 MB before axios.
- **Residual risk (UNVERIFIED):** the Edge Runtime tracks its own Deno version, which may differ from local 2.7.13. The Node-compat surface that matters is `node:crypto` (web-push ECDH) and `node:http/https` (axios, web-push). Both worked locally.

## 2. Supabase official examples worth copying

Repo `supabase/supabase`, directory `examples/edge-functions/supabase/functions/` (listed with `gh api` today). Freshness check: the ones below use the current pattern `export default { fetch: withSupabase({...}) }` from `npm:@supabase/server@^1`; none use the old `std/http` `serve`. `oak-server` (last commit 2023-11-27) is the stale one; skip it.

| Path / URL | Last commit | What to lift |
|---|---|---|
| `.../stripe-webhooks/index.ts` | 2026-06-26 (d5fde19) | The webhook skeleton: read `await req.text()` first because "verification relies on the raw request body rather than the parsed JSON"; wrap verify in try/catch and return 400 on failure; deploy with `verify_jwt = false` (`supabase functions deploy --no-verify-jwt`). Swap Stripe's verifier for our HMAC snippets; the Etsy scheme is in report 02 section 4 (`webhook-id.webhook-timestamp.body`, 300 s replay window). Add: insert into a queue table and return 200 inside Shopify's 5 s limit. |
| `.../background-upload-storage/index.ts` | 2026-06-26 | `withSupabase({ auth: 'secret' })` (the pg_cron-callable mode) and a background-task pattern. The supported primitive is `EdgeRuntime.waitUntil(promise)` (`raw/arch-sb-fn-bgtasks.md` line 117): respond fast, finish after. |
| `.../restful-tasks/index.ts` | 2026-06-22 | A routed function with `auth: 'user'`: the template for PWA-facing endpoints. |
| `.../unit-testing/` (README, `deno.json`, `_shared`, `tests`) | 2026-06-19 | How Supabase lays out `deno test` for functions; a cheap home for the HMAC and dedup tests. |
| `.../_shared/cors.ts` | 2026-08-11 | CORS headers for the PWA calling functions from the browser. |
| https://supabase.com/docs/guides/functions/schedule-functions (`raw/arch-sb-fn-schedule.md` lines 110 to 250) | read in wave 1 | The SQL to copy verbatim: `vault.create_secret(..., 'project_url')`, `vault.create_secret(..., 'secret_key')`, then `cron.schedule(...)` calling `net.http_post(url := (select decrypted_secret from vault.decrypted_secrets where name = 'project_url') || '/functions/v1/<fn>', headers := ... 'apikey' ...)`. Receiver: `verify_jwt = false` plus `auth: 'secret'`. |
| https://supabase.com/docs/guides/database/vault (`raw/arch-sb-vault.md`) | read in wave 1 | `vault.create_secret`, `vault.update_secret`, `vault.decrypted_secrets` for rotating Etsy and eBay user tokens. |
| `examples/slack-clone/nextjs-slack-clone/lib/Store.js` | 2025-08-18 | A React store subscribing to `postgres_changes` with unsubscribe. Next.js, so lift the subscription code only. |
| `examples/prompts/use-realtime.md` | 2026-05-04 | **Discrepancy to decide:** this official guide says "Don't use `postgres_changes` for new applications (single-threaded, doesn't scale well)" and to use `broadcast` from database triggers (`realtime.broadcast_changes`) on private channels. Report 05 chose `postgres_changes` for 1 to 2 viewers (its source says the cost bites past ~3,000 subscribers). Both are defensible at this size; broadcast-from-trigger is the "official" one and about ten lines of SQL. Pick one in the design. |

## 3. FlipWatch deep read (plus two others, ideas only)

Repo https://github.com/Crepe950/flipwatch. Shallow-cloned (read only, no install, no run) into the scratchpad; HEAD `83870a982dbfb485b4e5e0fcaddf5539fd157a33` ("Docker: don't require APP_PASSWORD", 2026-10-16). Licence MIT, "Copyright (c) 2026 FlipWatch contributors". Created 2026-10-15, 5 stars, 0 open issues, 471 files. Lifting any file means keeping that copyright and licence notice with it. It moves daily, so copy files at the pinned SHA and never depend on the repo.

**Stack:** Next.js 16, React 19, Tailwind 4, Drizzle on embedded PGlite or Postgres, vitest; localhost-only with an optional password. Library code takes `db` as its first argument and is framework-free (`src/lib`), which is why single files lift cleanly.

**Data model (`src/lib/db/schema.ts`, 381 lines):** `searches` (query, `excludeTerms`, `titleMustMatch`, min/max price cents, `expectedResaleCents`, marketplaces[], `pollIntervalSec`, `maxListingAgeHours`, `notifyMinDealScore`, `nextRunAt`, `lastError`), `listings` (unique `(marketplace, external_id)`, `priceCents`, `originalPriceCents`, `imageUrls`, `status active|gone`, `raw` jsonb, `firstSeenAt`, `lastSeenAt`), `price_history`, `search_matches` (unique `(search_id, listing_id)`, `lastEvent new|price_drop`, `lastEventAt`, `dealScore`, `dealScoreReason`, `silent`, `notifiedAt`, `seen`, `dismissed`), `blocked_sellers`, `notification_channels`, `notification_log`, `push_subscriptions`, `scrape_runs`, `marketplace_health`, `deals` and `deal_messages` (flip pipeline), `ai_evaluations`, `price_checks`. Money is integer cents plus currency.

**Matching (`src/lib/engine/filters.ts`, pure, 284 lines):** `parseQuery` splits a free-text query into what the marketplace receives and what the filter enforces: `ps5 -broken -"for parts"`, `a OR b`, `a|b`, quoted phrases. `normalizeText` strips diacritics and apostrophes; plural tolerance applies only to plain words ("iphone 4" does not match "iphone 4s"); exclude terms can be `title:`-only; stop words are dropped from `titleMustMatch`. This is exactly "description plus price range" for Ricky's watches.

**Scoring (`scoring.ts`, 122 lines, pure):** Tukey outlier removal on comps with the fence floored at 25% of the median, needs at least 5 comps, score = 50 + 1.25 per percent below the median, or margin against `expectedResaleCents`, averaged if both exist; prices of $1 or less are placeholders and never scored. Caution: its comps are the search's own matched listings, which for eBay rows is the aggregate the license restricts (section 5). Use it only with Ricky's own `expected_resale` and non-eBay comps.

**Match events (`matches.ts`):** a price drop must be at least 1% and at least 100 cents below the reference price, where the reference is the price at the match's last event, read from `price_history`, so every watch sees a drop even if another watch's run saw it first. A match is recorded silently (no alert) when: it is the first run for a (search, marketplace); a "new" listing is older than `maxListingAgeHours` and found while catching up after a gap; or it scores below the minimum. `alreadyNotified` compares `notifiedAt >= lastEventAt`, which makes retries idempotent.

**Polling (`scheduler.ts`, `ebay-quota.ts`, `backoff.ts`):** pollers (inline loop, external worker, or `GET/POST /api/cron/tick` with `Authorization: Bearer $CRON_SECRET` checked by a hashed `timingSafeEqual`) claim due searches with a compare-and-set UPDATE on `next_run_at`; the claim is a lease of max(interval, 5 min), replaced by finish + interval; a crashed worker's lease just expires. Jitter is plus or minus 10%; concurrency 3, claim limit 10. eBay: one Browse call per run, daily budget 4,500 of the 5,000 quota, floor interval = `ceil(86,400 * enabledEbaySearches / 4,500)` seconds. Backoff: rate-limited = Retry-After or 2^n x 60 s (max 1 h); blocked = 15 min x n (max 6 h); other = 2^n x 30 s (max 30 min); shared per marketplace via `marketplace_health`.

**eBay adapter (`marketplaces/ebay/`):** plain `fetch`, no eBay library. `GET https://api.ebay.com/buy/browse/v1/item_summary/search` with `sort=newlyListed`, `limit` default 50 (max 200), `filter=price:[a..b],priceCurrency:USD,buyingOptions:{FIXED_PRICE|BEST_OFFER},itemLocationCountry:US`; headers `X-EBAY-C-MARKETPLACE-ID` and `X-EBAY-C-ENDUSERCTX`. Auctions are opt-in because an auction's price is a bid that only goes up and "would score as a huge deal and report false price drops". Sold data: `ebay-sold.ts` is an 11-line function that builds a link to eBay's own sold search for the user's browser; its comment says eBay blocks automated clients and real sold data needs restricted Marketplace Insights, matching report 01.

**Notification path (`notify/`):** `Alert` -> per-channel `buildXRequest` (pure) -> `deliver()` which races a hard 10 s timeout, never throws, classifies permanent versus transient errors and writes `notification_log`; after 5 individual alerts per search per run the rest become one digest. The Pushover and ntfy builders are about 50 lines each and match the vendor pages (limits 250/1024/512/100 confirmed in `raw/arch-pushover-api.md`; ntfy via JSON to the root URL). Pushover priority 1 and ntfy priority 5 when deal score is at least 80.

**UI structure:** `app/(feed)` (cards with score-with-reason, stats strip, filters, quiet badge), `listings/[id]` (photo gallery, price-history chart, AI panel, outreach composer, block seller), `searches` (editor, "Test search" preview), `pipeline` (lead -> contacted -> bought -> listed -> sold, with profit and ROI), `hunt`, `settings`, `setup`. `public/sw.js` (113 lines): push, notificationclick, pushsubscriptionchange, "no offline caching".

**Liftable into our design (MIT, copy at the SHA, keep the notice):**

| File | Use |
|---|---|
| `src/lib/engine/filters.ts` (`parseQuery`, `normalizeText`, `createListingFilter`) | Watch matching as is. Drop the `haversineKm` import if we skip radius. |
| `src/lib/engine/matches.ts` (`isPriceDrop`, `referencePrice`, `isSilent`, `alreadyNotified`) | Alert rules and idempotency; port the drizzle queries to SQL. |
| `scheduler.ts` claim idea, `ebay-quota.ts`, `backoff.ts` | Our `tick` Edge Function: `UPDATE watches SET next_run_at = $lease WHERE id IN (SELECT id FROM watches WHERE enabled AND (next_run_at IS NULL OR next_run_at <= now()) ORDER BY next_run_at NULLS FIRST LIMIT 10 FOR UPDATE SKIP LOCKED) RETURNING *` (my Postgres rewrite of their compare-and-set; not their code). |
| `marketplaces/ebay/browse-request.ts`, `auth.ts`, `parse.ts` | Port to Deno `fetch`; replace the in-memory token map with a Postgres row. |
| `notify/channels/pushover.ts`, `ntfy.ts`, `delivery.ts` (timeout race, digest) | Alert sender. |
| `public/sw.js` | Only if Web Push phase 2. |
| `scoring.ts` | Only with Ricky's `expected_resale` and non-eBay comps (section 5). |
| `ebay-sold.ts` | Straight into the comps panel. |

**Not liftable:** the Next.js/Drizzle/PGlite stack; the Facebook, OfferUp, Craigslist and Kijiji scrapers (ToS; FlipWatch's own README says Facebook use is "against Meta's Terms of Service"); the in-process scheduler loop and in-memory token cache (our Edge Functions are stateless); the AI engines; the Discord bot; and the AI price check, which hands eBay "comparables" to an LLM to estimate resale value (`src/lib/ai/price-check.ts`) and would breach items 5 and 10 of Section 9 of the eBay license for us. Its default model string is `claude-haiku-4-5`, stale next to today's `claude-haiku-5-5`.

**Ideas only, both AGPL-3.0 (do not copy their code):**
- `BoPeng/ai-marketplace-monitor` (395 stars, pushed 2026-10-26): listing identity is a content hash of `(title, description, price, post_url with the query string stripped)`, with image, seller and date excluded; plus per-user notification status NOTIFIED / EXPIRED / LISTING_CHANGED / LISTING_DISCOUNTED. Same idea as FlipWatch's `price_history`, which is cleaner.
- `stephanlensky/hyacinth` (77 stars): dedup is a time cursor, not a seen-set: poll for listings created after `max(last stored listing time, now - backdate hours)`, with a per-(notifier, search) `last_notified`. Works only where the source returns a reliable creation time (Browse has `itemOriginDate`, report 04). Also a boolean-algebra filter util for rule combinations.

## 4. AI listing drafting from photos

All facts fetched live today from `platform.claude.com` (report 04 cites the `docs.claude.com` paths for the same pages). Raw: `raw/reuse-claude-models-overview.md`, `reuse-claude-pricing.md`, `reuse-claude-vision.md`, `reuse-claude-structured-outputs.md`, `reuse-claude-api-overview.md`, `reuse-claude-versioning.md`, `reuse-claude-haiku-5-5.md`, `reuse-claude-sonnet-5-5.md`, `reuse-claude-sonnet-5-5-whats-new.md`.

**Models and prices (VERIFIED, https://platform.claude.com/docs/en/about-claude/pricing and https://platform.claude.com/docs/en/models/overview):** all current models take text and image input.

| Model | API ID | Input / Output per MTok | Batch (50% off) |
|---|---|---|---|
| Claude Haiku 5.5 | `claude-haiku-5-5` | $0.10 / $0.50 (prompts up to 100k tokens; higher above) | $0.05 / $0.25 |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | $2 / $10 | $1 / $5 |
| Claude Opus 5.5 | `claude-opus-5-5` | $4 / $20 | $2 / $10 |
| Claude Fable 5.1 | `claude-fable-5-1` | $10 / $50 | $5 / $25 |

**Image token formula (VERIFIED, https://platform.claude.com/docs/en/build-with-claude/vision):** `ceil(width/28) * ceil(height/28)` visual tokens per image. Two tiers: high-resolution for "Claude 4.7 and later models" (max long edge 2,576 px, max 4,784 tokens) and standard (1,568 px, 1,568 tokens) for the rest. Haiku 5.5 and Sonnet 5.5 fall in the first by version number (INFERRED: the model pages do not name a tier; the Haiku 5.5 what's-new page, `raw/sourcing-claude-haiku-5-5-whats-new.md`, says it shares the 4.7-and-later tokenizer). Doc table: 1000x1000 = 1,296 tokens; 2000x1500 = 3,888 (not resized in the high-res tier); 3840x2160 resized to 2576x1449 = 4,784. Limits: 10 MB base64 per image, 600 images per request (100 for 200k-context models), 32 MB request cap, JPEG/PNG/GIF/WebP. "Claude works best when images come before text." The doc recommends resizing before upload.

**Request shape (header and body fields VERIFIED; the combination in one call is UNVERIFIED, no live call was made):**
- `POST https://api.anthropic.com/v1/messages`; headers `x-api-key` (legacy fallback for `Authorization: Bearer`, "still supported"), `anthropic-version: 2026-10-21` (the current version; `2023-06-01` is still listed), `content-type: application/json`. `anthropic-workspace-id` is required for an API key that is not scoped to a workspace.
- Version 2026-10-21 removes `temperature`, `top_p` and `top_k`: sending any of them returns **400 on every model**. Do not copy older snippets that set them.
- Structured output needs no beta header: the schema goes in `output_config.format` as `{type: "json_schema", schema}`. Supported on Haiku 4.5/5.5, Sonnet 4.5/4.6/5/5.5, Opus 4.5 to 5.5. Output is grammar-constrained to the schema; first use of a schema adds compile latency (cached 24 h); incompatible with citations and message prefill. Schemas need `additionalProperties: false`; `minLength/maxLength/minimum/maximum` are unsupported (move them into descriptions).
- Thinking is adaptive, on by default, and **billed as output tokens**. Haiku 5.5: `thinking: {"type": "disabled"}` works at `high` effort or below. **Sonnet 5.5: `{"type": "disabled"}` returns 400; send `{"type": "between_tools"}`** (its lowest setting, accepted at low, medium or high effort). Sonnet 5.5 also rejects forced `tool_choice` (`any` or a named tool), so use `output_config.format`, not the force-a-tool JSON trick. Whether `between_tools` means exactly zero thinking on a request that has no tools: UNVERIFIED.

```ts
const r = await fetch("https://api.anthropic.com/v1/messages", { method: "POST",
  headers: { "x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2026-10-21", "content-type": "application/json" },
  body: JSON.stringify({
    model: "claude-haiku-5-5", max_tokens: 1200,
    thinking: { type: "disabled" },                       // Sonnet 5.5: { type: "between_tools" }
    messages: [{ role: "user", content: [
      { type: "image", source: { type: "url", url: signedStorageUrl } },   // or { type: "base64", media_type: "image/jpeg", data }
      { type: "text", text: PROMPT }] }],
    output_config: { format: { type: "json_schema", schema: LISTING_SCHEMA } } }) });
const text = (await r.json()).content.find((b: { type: string }) => b.type === "text").text;  // JSON.parse(text)
```

**Cost per listing** (computed with `node` from the formula and prices above; assumptions: 300 text tokens of instructions, 400 output tokens, thinking off, no caching):

| Case | Image tokens | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|---|
| One 1 MP photo (1000x1000) | 1,296 | **$0.00036** ($0.00018 on Batch) | **$0.00719** | $0.01438 |
| Five 1 MP photos | 6,480 | $0.00088 | $0.01756 | $0.03512 |
| One unresized 12 MP phone photo (high-res cap) | 4,784 | $0.00071 | $0.01417 | $0.02834 |
| Per 1,000 listings, 1 photo | | $0.36 | $7.19 | $14.38 |

Each extra 1,000 thinking tokens billed as output adds $0.0005 on Haiku and $0.0100 on Sonnet, so on Haiku turning thinking off matters more than any other knob. The Batch API (`POST /v1/messages/batches`, 50% off, asynchronous) suits an overnight pass over a pile of new inventory.

**Design notes:**
- **Resize in the PWA before upload** (canvas or `createImageBitmap`, long edge about 1,000 to 1,568 px). Decoding or resizing in an Edge Function risks the 2 s CPU cap, and Supabase's `image-manipulation` example leans on ImageMagick WASM. Send the image as a `url` source with a short-lived signed Supabase Storage URL so the function never touches the bytes (that Anthropic can fetch a signed Storage URL: UNVERIFIED, test once; base64 of a ~200 KB JPEG is the fallback).
- **Schema fields:** `title`, `description`, `condition_notes`, `visible_defects[]`, `era_guess` + `maker_guess` + `confidence`, `materials[]`, `category_keywords[]`, `suggested_tags[]`, `needs_better_photo[]`. **No price field** (nothing to base it on, and item 5 of Section 9 stops us from basing it on eBay data). Present guesses as guesses for Ricky to confirm; era and maker from a photo is where small models are weakest.
- **Never let the model emit category IDs.** Take its keywords and map them through the marketplace taxonomy. eBay Taxonomy `GET /commerce/taxonomy/v1/category_tree/{id}/get_category_suggestions` works with the basic `https://api.ebay.com/oauth/api_scope` app token (VERIFIED in `raw/ebay-spec-taxonomy_api.json`), and `get_item_aspects_for_category` lists required item specifics to constrain a second fill-in pass. Etsy has `GET /v3/application/seller-taxonomy/nodes` and `/{taxonomy_id}/properties` (VERIFIED in `raw/etsy-shopify-etsy-openapi.json`). Shopify taxonomy: report 02.
- **Model choice:** start on Haiku 5.5; if title and era quality disappoint in a 20-item side-by-side, move to Sonnet 5.5 for about 20x the cost, still under a cent a listing. Confirm real `usage` with the token-counting endpoint (`POST /v1/messages/count_tokens`) before trusting the table. No live API call was made in this pass.

**Hugging Face vision-language models on the Fedora box: no.** Candidates from the Hub search: https://hf.co/Qwen/Qwen3-VL-4B-Instruct (Apache-2.0, 3.9M downloads, GGUF build at https://hf.co/Qwen/Qwen3-VL-4B-Instruct-GGUF), https://hf.co/Qwen/Qwen2.5-VL-3B-Instruct (no licence tag shown by the connector, so check before use) and https://hf.co/HuggingFaceTB/SmolVLM2-2.2B-Instruct all fit in 15 GB RAM. But the box is a CPU-only i7-8565U at about 7 tokens/s on a 4B text model (project CLAUDE.md). Back-of-envelope, not benchmarked: a 400-token JSON answer is about a minute of generation, plus 1,000+ image tokens of prefill at tens of tokens per second, so roughly 1.5 to 3 minutes per listing against 2 to 5 seconds on Haiku. Quality on maker marks, era and materials of vintage goods is lower at 2B to 4B. The saving is $0.00036 per listing, so 1,000 listings a year is 36 cents. Not worth the setup, the wait or the worse drafts. Revisit only if images must stay local.

## 5. Pricing aid within the eBay license

Source: `raw/ebay-api-license-agreement.md` (https://developer.ebay.com/join/api-license-agreement). Section 9 item numbers are exact (the list runs 1 to 15 in order); for Section 8 I cite the clause title and raw-file line because the markdown flattens its sub-numbering. Report 01 section 1.7 already covers the 6-hour and delete-when-gone rules and the no-average-selling-price rule; this adds what it missed.

| Clause | Text (VERIFIED, quoted or close paraphrase) | Effect on us |
|---|---|---|
| 8, "Public Display" (line 128) | Public eBay content may be displayed "to promote eBay and enable Your Users to search and browse listings"; (1) delete it "when the eBay Content is no longer publicly available"; (2) it "may not be co-mingled or combined with non-eBay Content ... must be visually isolated from third-party listings or other non-eBay information" | A panel of eBay listings is allowed. It must sit in its own box, never in the same table, chart or feed as Etsy, Shopify or other-site rows. This also constrains the unified sourcing feed in report 04. |
| 8, "Age of Displayed eBay Content" (line 129) | Item listing info no more than 6 hours older than eBay's site; other content 24 h; disclose how much older if not current | Fetch live when the panel opens and stamp "as of HH:MM". Re-poll stored watch cards at least every 6 h or hide them. |
| 8, "Prohibited Use and Derivation" (lines 130 to 135) | Written permission needed for anything enabling "Average selling price or gross merchandise sold for any eBay category" or site-wide statistics | No category averages. |
| **9 item 5** (line 182) | Not allowed: "Use eBay Content, either alone or in combination with third-party information, to suggest or model prices for items listed on eBay Site." | **Ricky lists on eBay.** No suggested price, no median, mean or range, no chart, and never prefill a price field from eBay data. Showing the raw list for a human to read is "search and browse"; computing a number is where the line sits (my reading; ask eBay for certainty). |
| 9 item 10 (line 187) | Not allowed: use eBay Content "to train algorithms, conduct machine learning, develop synthetic data sets, train large learning models, and/or train artificial intelligence systems" | No eBay titles or prices in training data, fine-tunes or few-shot "style" examples. Inference-only matching of a title against a watch (report 04 tier T2) is not training but treat it as gray (below). |
| 9 item 7 (line 184), and 8 "Using and Displaying eBay Content" intro (line 126) | No "copy, store ... eBay Content, other than for the purposes allowed"; "use and display eBay Content only within your Application" | Store the minimum. Sending a title, price and link to Pushover or ntfy leaves the Application: gray, common practice (FlipWatch does it), UNVERIFIED how eBay reads it. |
| 8, "Displaying Aggregated Content" (line 144) | No framing or mirroring of eBay-served pages | Link out, never iframe. |
| 8, Restricted APIs (lines 160 to 168) | Data from Restricted APIs (Marketplace Insights etc.) may not be ingested into non-eBay AI, bulk-downloaded or used for pricing tools without written consent | Marketplace Insights stays unavailable, as in report 01. |
| `raw/ebay-buy-requirements.md` | Browse display rules (eBay logo, eBay image, full title) are written for guest-checkout partners | We do no checkout, so they do not bind; showing eBay's own image URL, the title and the `itemWebUrl` link is the safe default anyway. |

**Minimal compliant "comps" panel (what to build):**
1. A button on an item or draft opens **"Similar active listings on eBay (asking prices, not sold prices)"**. An Edge Function calls Browse `item_summary/search` with Ricky-editable keywords (default: the AI's `category_keywords`), `limit=12`, using FlipWatch's request builder. The label says active asking prices; never "sold", "average" or "market value".
2. The response is mapped to `{title, price, currency, condition, image.imageUrl, itemWebUrl, fetchedAt}` and **not written to the database or any persistent client cache** (React Query in memory only, short `staleTime`; do not enable query persistence to IndexedDB for this key). Nothing to purge, nothing to go stale.
3. Rendered in its own bordered card, visually separate from Ricky's own listing data and from any Etsy or Shopify figure. Each row links to eBay (`itemWebUrl`, new tab) and shows "as of 14:05". No totals, no summary row, no "use this price" button.
4. A second link, **"Sold on eBay"**, opens `https://www.ebay.com/sch/i.html?_nkw=<keywords>&LH_Sold=1&LH_Complete=1` in a new tab (FlipWatch `src/lib/ebay-sold.ts`; it is eBay's public website in Ricky's own browser, not API content). The `LH_Sold` / `LH_Complete` parameters are UNVERIFIED against eBay docs: open it once to confirm. A third link goes to Seller Hub, Research (Terapeak), "free to all sellers" (report 01 section 6), for sold data inside eBay's own UI.
5. Panel data is never sent to Claude and never logged.

**Where this collides with earlier reports (surface for the design):**
- Report 04's `seen_listings` with a 90-day TTL "extended while an auction is live": store only `(item_id, fingerprint_hash, first_seen_at, last_alerted_at)`, no title, price or image, and delete rows when the item ends. Ids plus hashes are the least-risk dedup. The "append the 8 rejected titles to the Haiku prompt" idea uses eBay titles as in-context examples: low risk (not training) but prefer the reject pattern text over eBay content.
- Report 04's embeddings of eBay titles for "not this" suppression are derived from eBay Content: keep them ephemeral or skip; gray.
- FlipWatch-style `computeDealScore` over eBay comps: avoid. Score a buy-side deal against Ricky's own max price per watch and `expected_resale`, not an eBay-derived median.
- Alerts that carry eBay title, price and link through Pushover or ntfy are gray; keep them to title, price and the eBay link. Worth one question to eBay Developer Technical Support (report 01, `raw/ebay-dts.md`) if this goes beyond personal use.

## 6. Open questions

1. Approve (or do yourself in WSL, or install Docker Desktop for) the Edge Runtime probe in 1.3. It is the one missing fact for `ebay-api` and `web-push` under Supabase.
2. `postgres_changes` (report 05) or broadcast-from-trigger (Supabase's own guide)?
3. `@supabase/server`'s `withSupabase` for auth modes, or hand-rolled secret and HMAC checks only?
4. Haiku 5.5 or Sonnet 5.5 for drafting: needs a 20-item side-by-side with real `usage` numbers. Does a signed Storage URL work as the `url` image source?
5. eBay gray areas (alerts leaving the Application, LLM matching of eBay titles, my reading of item 5 for a raw comps list): worth an email to eBay developer support before any launch beyond personal use.
6. Etsy: does the token endpoint need `x-api-key`, and does refresh rotate the refresh token?

## 7. Raw pages fetched this pass (`research/dashboard/raw/`)

New: `reuse-claude-pricing.md`, `reuse-claude-models-overview.md`, `reuse-claude-vision.md`, `reuse-claude-structured-outputs.md`, `reuse-claude-api-overview.md`, `reuse-claude-versioning.md`, `reuse-claude-haiku-5-5.md`, `reuse-claude-sonnet-5-5.md`, `reuse-claude-sonnet-5-5-whats-new.md`, `reuse-sb-fn-dependencies.md`, `reuse-sb-fn-routing.md`, `reuse-healthchecks-ping-api.md`, `reuse-healthchecks-signaling.md`.

Reused from earlier passes: `ebay-api-license-agreement.md`, `ebay-buy-requirements.md`, `ebay-spec-taxonomy_api.json`, `arch-pushover-api.md`, `arch-ntfy-publish.md`, `etsy-shopify-etsy-auth.md`, `etsy-shopify-etsy-openapi.json`, `arch-sb-fn-schedule.md`, `arch-sb-fn-limits.md`, `arch-sb-fn-bgtasks.md`, `arch-sb-vault.md`, `sourcing-claude-haiku-5-5-whats-new.md`.

Read through `gh api` and not saved to raw: the Supabase examples tree and files, ai-marketplace-monitor and hyacinth source files, npm and GitHub metadata. FlipWatch was shallow-cloned into the scratchpad.

Scratch work (not in the repo): `C:\Users\ethan\AppData\Local\Temp\claude\C--Users-ethan-dev-Vintage\634dc484-d184-46e6-a7b4-91d20e747c83\scratchpad\reuse\` (load tests, snippets, HMAC test, edge probe, FlipWatch clone).
