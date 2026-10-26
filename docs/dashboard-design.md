# Hollywood and Vine ops dashboard: design v1

Date: 2026-10-26. Status: designed, nothing built. Build handoff: `docs/dashboard-handoff.md`.

Research base: ten Sonnet reports in `research/dashboard/01..10` (two waves of five), about 350 raw
vendor pages in `research/dashboard/raw/`, the data model and metric SQL run in PGlite, the vendor
contract sheet live-probed, the frontend install built and type-checked. Every number below has a
source in those reports; this document is the synthesis and the decisions.

## 1. What it is

One installable web app, on Ricky's phone and on the desktop, that answers four questions:

1. **What sold?** One feed across eBay, Etsy and Shopify, with real profit (gross, fees, shipping, cost basis).
2. **What do I own?** Every piece with cost, where it is stored, and its live status on each channel.
3. **What should I go buy?** eBay listings that fit a watch Ricky wrote in plain words plus a price cap.
4. **What needs me right now?** A sold item still live on another channel, an auction ending, a dead connection, a sale with no cost entered.

It pushes to the phone through Pushover. It never lists, delists, reprices or crosslists; a paid
crosslister owns that write path. It never buys; sourcing alerts end at a human tap.

## 2. The three decisions that shape everything

1. **Buy the write path, build the read path.** No product fills "sourcing alerts by description and price across sites", and nobody gives one profit number across three channels with cost basis. Everything else (crosslist, delist, inventory truth inside the tool) is bought for $9 to $40 a month. Source: `03` buy-vs-build matrix.
2. **Webhooks first, polling for correctness.** Etsy (`order.paid`, `inventory.out_of_stock`, `listing.*`), Shopify (`ORDERS_PAID`, `PRODUCTS_UPDATE`) and eBay (`ORDER_CONFIRMATION`, `LISTING`) all push to HTTPS. One Supabase Edge Function receives them. Polling exists only for eBay watches (Browse has no push), for reconciliation, and for eBay listings of record. Source: `05` section 0, `02` section 4, `01` section 3.
3. **eBay's license shapes the sourcing feature.** Watch hits are the most restricted data in the system: purge when the listing ends, at most 6 hours stale, shown in their own component, never used to suggest a price, train or score. So matching is deterministic rules plus optional per-listing LLM inference, and the "comps" panel is live links only. Source: `10` C5 to C12, `08` section 5.

## 3. Architecture: what runs where

```
 SELLING PLATFORMS (push)                 SUPABASE PRO  (one project, never pauses)                 PHONE / DESKTOP
 ------------------------                 ----------------------------------------                 ---------------
 Etsy    order.paid, listing.*  --+
 Shopify ORDERS_PAID, PRODUCTS_* --+--HTTPS-->  Edge Fn webhook-in: verify signature on raw bytes,
 eBay    ORDER_CONFIRMATION      --+            insert events (unique event id), return 200 fast
 eBay    MARKETPLACE_ACCOUNT_DELETION ---->  Edge Fn ebay-deletion: challenge + redact + deletion_log
                                                            |
                                   pg_cron (1 min) --> Edge Fn tick: drain events, reconcile polls,
                                                       eBay listings poll, watches (Browse), refresh/purge
                                                            |          \
 eBay Browse API  <---- poll ----------------------------'           '--> Healthchecks.io ping per job
 (5,000 calls/day)                                          v
                                   Postgres: items, channel_listings, sales, expenses, events,
                                             watches, candidates, alerts, integrations, deletion_log
                                             Vault: OAuth tokens      Storage: item photos
                                                |  alerts insert                    | Realtime postgres_changes
                                                v                                   v
                                   Edge Fn notify --> Pushover (priority 1 / 2) --> Pushover app  ("heard")
                                          '--> ntfy.sh/<existing topic> on non-2xx or unacked p2
                                                                            React 19 PWA (Home Screen)
                                                                            Cloudflare Pages or Vercel Pro
 CROSSLISTER (Crosslist Gold, trial first): owns list / delist / reprice. The dashboard never calls it.
 FEDORA BOX: not used in v1. Phase 2 only, outbound, best-effort, heartbeat row.
```

| Part | Choice | Why (report) |
|---|---|---|
| Backend | Supabase **Pro**, new project in Ricky's existing org | Free tier pauses, has no backups, 1-day logs; the eBay deletion endpoint must never go dark (`05` 1.2, `10` C42) |
| Receivers | Edge Functions with `verify_jwt=false`, vendor signature checked first | all three vendors sign; `09` D, `10` C25 |
| Scheduler | pg_cron + pg_net calling `tick` with the Vault secret key | runs next to the DB, visible in `cron.job_run_details` (`05` section 3, `09` D) |
| Realtime | `postgres_changes` on the six UI tables, one channel | one viewer; swap to broadcast-from-trigger only if it ever matters (`08` section 2 discrepancy) |
| Auth | email OTP through Resend SMTP, sign-ups off after the first user | built-in SMTP is 2 emails/hour (`05` 1.6, `10` C35) |
| Push | **Pushover** primary ($4.99 once), ntfy.sh fallback on the topic Ricky already has | only channel with insist-until-acknowledged (`05` 4c) |
| UI hosting | Cloudflare Pages ($0, terms carry no non-commercial clause) or Vercel Pro ($20) if already paid | Vercel Hobby forbids commercial use (`05` 2.1, `raw/host-cloudflare-terms.md`) |
| Dead-man | Healthchecks.io free, one check per scheduled job | a dead cron chain is otherwise silent (`05` 7.3, `10` C46) |
| Libraries | raw `fetch` for eBay, Etsy, Shopify, Pushover, ntfy, Healthchecks | all tested; no client library needed (`08` section 1) |

## 4. Data flows

**Sold.** Webhook lands, `events` row inserted on conflict do nothing, 200 returned. `tick` drains
`events`: fetches the resource (Etsy sends only a `resource_url`), strips buyer PII, upserts `sales`
guarded by `source_updated_at`, matches the order line to an item by listing id then SKU. The
database trigger `alert_on_sale` writes the `sold` alert (ignores orders older than 24 h so a backfill
never pushes hundreds). Reconciliation: Etsy receipts by `min_last_modified` every 15 min, Shopify
orders by `updated_at` every 15 min, eBay `getOrders` by `lastmodifieddate` every 10 min, a daily
7-day sweep per channel. Webhooks are the fast path; sweeps are the correctness path.

**Listings (for the double-sale guard).** Etsy `listing.*` webhooks plus a 3-hour listings poll;
Shopify `PRODUCTS_UPDATE` plus a 3-hour products query; eBay Trading `GetMyeBaySelling` every 3 hours
(the Inventory API cannot see listings made in the eBay app, `01` 2.2), plus the `LISTING`
notification topic if a standard keyset can subscribe. Match to items by SKU (the crosslister's
custom label) then title.

**Oversell guard.** On every sale, if any other `channel_listings` row for that item is still
`active` 20 minutes later, raise `oversell_risk` (priority 2). If the crosslister delists inside its
documented 15 minutes, the row flips to `ended` and nothing fires.

**Watches.** `tick` claims due watches with a lease (`update ... where next_run_at <= now() ...
for update skip locked`), calls Browse `item_summary/search` with `sort=newlyListed`,
`filter=itemStartDate:[cursor..],price:[min..max],priceCurrency:USD,buyingOptions:{...},
conditions:{...},deliveryCountry:US`, `limit=200`, `fieldgroups=EXTENDED`. Tier 0 is the API filter,
tier 1 is a port of FlipWatch's `filters.ts` (quoted phrases, `-exclude`, `a OR b`, plural
tolerance). Survivors become `candidates` and one `buy_match` alert each, subject to cooldown and
quiet hours. Budget: 4,500 calls/day floor interval; hot watches every 3 min, normal every 30 min;
30 watches fit at about 81% (`04` 1.4). Every 5 hours a refresh pass calls `getItem` on live
candidates; ended ones are purged to a tombstone (`watch_id`, `external_id`, `status`, hash).

**Alerts.** Producers insert `alerts`; `notify` sends Pushover with `url` pointing at the listing
and the fit reason in the body. Priority 1 for buy matches and sold; priority 2 (retry 60 s, expire
30 min) for oversell risk and a starred auction ending. On non-2xx or an unacknowledged priority-2
receipt, send the same text to ntfy. Rules: at most one push per watch per 5 minutes (group the
rest), 6 per watch per hour, quiet hours 22:00 to 07:00 America/New_York with overrides for starred
auctions and priority 2. `seen_at` is written by the UI; `acked_at` only by the push receipt path.

## 5. Data model

Adopt the nine-table DDL in `06` section 1.2 as migration 0001; it ran in PGlite with RLS, trigger
and upsert tests. Tables: `items`, `channel_listings`, `sales` (one row per order line, generated
`fees_total` and `net_proceeds`), `expenses`, `events` (webhook inbox, idempotency key, redacted raw
payload), `watches`, `candidates`, `alerts`, `integrations` (cursors, token pointer, heartbeat).

Deltas decided here (exact SQL in the handoff, section 4):

| Change | Why |
|---|---|
| `candidates` + `fit_reason`, `fit_score`, `starred`, `dismiss_reason` | the Alerts card shows "Fits:", star for auctions, reason chips (`07` 1.4) |
| `watches` + `description`, `alert_mode`, `tier`, `next_run_at` | plain-language sentence for tier 2, push vs inbox, hot/normal, lease claim (`04`, `08`) |
| `alerts` + `seen_at` | an in-app glance must not stop a priority-2 escalation (`07` 1.4) |
| `items.sku` default from a sequence (`HV-0001`) | the Add sheet never asks for a SKU (`07`) |
| `items.cost_purchase` nullable; `cost_basis` uses `coalesce` | NULL = unknown, 0 = free; today they collide (`07` open question 10) |
| new `deletion_log` | eBay account-deletion proof that survives a restore (`10` C13, C14) |
| `candidates` purge keeps id, status, hash only | eBay content must go when the listing ends (`10` C8, `08` section 5) |

Money stays `numeric(12,2)` dollars with every sum done in SQL views (`06` is tested that way; `10`
C44's "integer minor units" is advice, not a vendor rule). Buyer PII is stripped before any row is
written: order id, dates, item, prices, fees, tax, ship-to state, marketplace handle only.

Fees: estimate with `06`'s `est_fees()` (reproduces eBay's own four worked examples to the cent;
eBay's base includes sales tax), replace with the platform's number when the API reports it, and mark
estimates with `~` in the UI. Fee rule follows the listing: magazines and the Chanel book are eBay
"Books & Magazines" at 15.3%, chains are "Jewelry" at 15%, most else 13.6% plus $0.40 per order.

## 6. Screens

Five tabs plus one pushed screen. Full wireframes, copy for empty states, and the token sheet are in
`07`; this is the contract.

| Tab | One job | Primary action |
|---|---|---|
| **Today** | Is anything on fire, and what did I make | tap the top "Needs you" row |
| **Alerts** | decide on each buy match; confirm each sale | Bought / Not this / Open on eBay |
| **Watches** | say what to hunt for, in plain words | create or toggle a watch; "Test" runs it once |
| **Inventory** | what I own, what it cost, where it is | Add item: photo, title, cost, nothing else required |
| **Sales** | the real numbers by month and channel | switch month |
| Item detail (pushed) | everything about one piece | edit, open on channel |

Rules that are not negotiable in the UI:

- "Needs you" order: double-sale risk, unread buy matches, starred auctions ending in 24 h, connection problems, data hygiene (missing cost, aged 90+ days).
- "Bought" on a buy card creates the inventory item with the paid price as cost basis. That tap is where profit tracking becomes free.
- Every eBay card prints "as of HH:MM", disappears when the listing ends, carries no cost, margin, comp or other-site column, and never interleaves with sales or Recent. The "All" segment is grouped, not merged.
- No "good deal" badge, no typical price, no channel ranking. By-channel is alphabetical with no commentary.
- Buyer names, addresses, emails, phones appear nowhere.
- 44 px targets, visible labels, no colour-only state (channel chips carry a letter and a glyph), swipe is an accelerator with buttons always present, dark mode follows the OS.
- Palette: warm paper / near-black plum base; burgundy `#6b2540` (rose `#e58fb0` dark) for primary; neon pink `#b8135f` / `#ff5fae` only for unread, Live dot, NEW, focus; gold `#7f6200` / `#e0b84a` only for money in. Accents cover at most about 10% of a screen.
- Footer on login and Settings: public `/privacy`, and the sentence "The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy."

Frontend: Vite 8.3 + React 19.3 + Tailwind 4.3 + shadcn (button, input, drawer, switch, badge,
skeleton, sonner) + react-router 8.5 declarative + supabase-js 2.118 + vite-plugin-pwa 2.0
(`registerType: 'prompt'`). No chart library (one Recharts chart cost +104 kB gzip; sparklines are
SVG, bars are flex divs). No TanStack Query (a 25-line Realtime hook). Three mandatory edits to
shadcn's output: dark mode to `prefers-color-scheme`, buttons and inputs to 44 px, delete
`next-themes` and Geist. Layout uses `dvh` and safe-area insets, never `h-screen`.

## 7. Compliance baked in

The full list is `10` section 4 (C1 to C50). The ones that change code:

- Etsy Seller App registered with the purpose "sales and inventory reporting and sold or low-stock alerts for my own shop"; Etsy is never a sourcing source; no buyer messaging. (C1 to C3)
- eBay watch hits: purge on end, 6-hour staleness, visual isolation, no price modelling, no training, no auto-buy. (C5, C8 to C12)
- eBay account-deletion endpoint before the first production call; `deletion_log`; redact on notice. (C13, C14)
- Shopify ingest works with every buyer field null; 30-day deletion on uninstall. (C16, C17)
- Signatures on raw bytes before any parse or DB write; event-id dedup; 200 within Shopify's 5 s. (C25 to C28)
- RLS on every table, default grants revoked, `security_invoker` views, secret keys never in the browser. (C32 to C34)
- Supabase Pro from the first webhook; seven daily backups plus a weekly off-site dump; token watchdog (eBay 60 days before expiry, Etsy at 75 days, Shopify on any failure). (C42, C43, C47)

## 8. Phases

**Step 0: accounts and smoke tests (Ricky plus one session, about half a day).** Developer accounts
and keys for eBay, Etsy, Shopify; Supabase Pro project; domain; Pushover; Resend; Healthchecks. Then
the twelve ordered smoke tests in `09` ("Unverified items the builder must smoke-test first"). The
first one decides whether buy alerts can be API-driven at all: one production Browse search with a
standard keyset. If it fails, sourcing falls back to eBay's own saved-search emails until an
Application Growth Check or Partner Network application lands.

**Phase 1: sold feed, inventory, profit (the part that definitely works).** Schema, deletion
endpoint, webhook receiver, processors and reconciliation polls, listings sync, oversell guard,
notify, Healthchecks, token watchdog, PWA with Today, Alerts (Sold), Inventory with Add, Sales,
Settings, Item detail. Installed on the phone.

**Phase 1b: watches.** Watches and candidates tables in use, `tick` watch lane, refresh and purge,
Watches screen with Test, Alerts Buy tab, Bought sheet.

**Phase 2, in order of value.** Haiku 5.5 tier-2 matching on tier-1 survivors (about $0.08 per
1,000 listings with thinking disabled; build a 100-listing labelled set from week one first). AI
listing drafts from a photo (about $0.0004 per photo on Haiku 5.5, $0.007 on Sonnet 5.5). The
compliant comps panel (live eBay asking prices, unstored, isolated, plus a link to eBay's own sold
search and Terapeak). Saved-search email ingestion for Craigslist, ShopGoodwill, EstateSales.net,
Invaluable, Chairish, HiBid. Web Push and the app-icon badge. A second user (a metadata flag, not a
schema change).

## 9. Cost

| Line | Monthly | Notes |
|---|---|---|
| Supabase Pro | $25 | includes compute credit; required (pausing, backups, deletion endpoint) |
| UI hosting | $0 Cloudflare, or $20 Vercel Pro | Vercel Hobby is non-commercial |
| Pushover | $0 ($4.99 once per platform) | 10,000 messages/month free per user |
| ntfy.sh, Healthchecks.io, Resend | $0 | ntfy 250/day cap; Healthchecks 20 checks; Resend 3,000/month |
| Domain | about $1 | |
| Claude Haiku 5.5 (phase 2) | $3 to $5 | at about 1,200 tier-1 survivors a day |
| Crosslister (Ricky's pick) | $9 to $40 | Crosslist Gold $39.99 is the documented 15-minute all-three-channel option |
| **Dashboard total** | **about $26 to $46** | plus $4.99 once |

## 10. Decisions made in this design

| Decision | Chosen | Not chosen, and why |
|---|---|---|
| Where pollers run | Supabase pg_cron + Edge Functions | Fedora box (off the network 3 days in September, silent); GitHub Actions (5-min floor, drops jobs) |
| Realtime mechanism | `postgres_changes` | broadcast-from-trigger is Supabase's current advice but adds SQL per table for one viewer |
| Money type | `numeric(12,2)` dollars, sums in SQL | integer cents would mean re-testing all of `06` |
| eBay listings of record | Trading `GetMyeBaySelling` 3-hourly, raw fetch + `fast-xml-parser` | Inventory API is blind to app-made listings; Sell Feed report is async and unverified for UI-made listings |
| eBay client library | none (raw fetch) | `ebay-api` 10.0.2 works in Deno but pulls axios and a Node 22 engine; keep as escape hatch for Trading XML |
| Matching v1 | tier 0 + tier 1 rules | LLM (phase 2) and embeddings (never on eBay titles: C11) |
| Comps | live links only, nothing stored or computed | eBay license 9.5 bans suggesting prices for items listed on eBay |
| Crosslister | trial Crosslist Gold; dashboard independent of the choice | Vendoo omits Shopify delist; FLUF polls every 60 to 90 min; List Perfectly delists at $99+ |
| Shopify as hub | no | Marketplace Connect cannot add Etsy any more; sync apps unproven on quantity-1 delist latency |
| Pull-to-refresh | none; Realtime plus refetch on `SUBSCRIBED`, `visibilitychange`, `online` | iOS Home Screen apps have no native gesture; Android's reloads the SPA |
| Offline writes | none in v1 | duplicates after slow saves are a real failure mode; revisit if estate sales have no signal |
| Capacitor / app store | not now | Pushover already gives reliable push; nothing else needs native |
| Repo | `dashboard/` inside this repo | a new repo is a structure change and needs Ricky's word |

## 11. Decisions Ricky owns (defaults in bold; the build proceeds on the defaults)

1. Phone: **iPhone** (inferred from file names) or Android. Changes install steps and the real-phone tests only.
2. Dashboard domain, fixed before the PWA is installed (manifest id, auth redirects, CSP bind to it). Suggestion: a subdomain of the shop domain.
3. Hosting: **Cloudflare Pages ($0)**, or Vercel Pro if that team is already on Pro.
4. Crosslister to trial: **Crosslist Gold**, measured on one quantity-1 item for sale-to-delist latency before paying.
5. Watches: how many, which categories, auctions **in**, price caps **fixed per watch** (relative-to-comps is not allowed with eBay data), timezone **America/New_York**, quiet hours **22:00 to 07:00**.
6. Accounts: does the Etsy shop exist yet (the Seller App needs a live shop); which Shopify plan (Basic $39, or $29 yearly); which eBay account owns the developer keyset (**the seller account**).
7. Non-eBay sourcing appetite: **their own saved-search emails only** (ToS-clean), or low-rate polling of the few sites with no scraping clause.
8. A second login later (a helper)? **Not now.**
9. Email developer@etsy.com to confirm an own-shop sales dashboard is fine under API Terms #25? **Register with the precise purpose and proceed**; the email is cheap insurance.
10. CPA: inventory accounting method before year end. Not blocking.

## 12. Known unknowns that only Step 0 resolves

- Browse search in production with a standard keyset (docs conflict).
- `ORDER_CONFIRMATION` and `LISTING` subscribable on a non-partner keyset, and firing for listings made in the eBay app.
- Whether eBay signs the raw body or re-serialised JSON, and whether the Edge Runtime has `ssl3-sha1`.
- Etsy webhooks on a Seller App, the real QPS/QPD, and the `v1,` signature prefix.
- Shopify protected customer data on a Dev Dashboard app in the merchant's org.
- Supabase Edge Runtime running `npm:fast-xml-parser` (and `web-push` later); the probe is staged in the session scratchpad and resolves by deploying it.
- Pushover and ntfy delivery latency; whether a Pushover link opens Safari or the installed app.
