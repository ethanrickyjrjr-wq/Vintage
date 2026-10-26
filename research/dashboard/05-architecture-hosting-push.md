# Dashboard architecture: real-time, always-on, phone-reachable, cheap

Hollywood and Vine (Vintage repo) · research note 05 · **2026-10-26** · research only, nothing built.

Legend. **[V]** = read today (2026-10-26) on the live vendor page, quoted or closely paraphrased, URL given.
**[V*]** = read today in a raw page another agent fetched today into `research/dashboard/raw/`; same standard, different fetcher.
**[U]** = UNVERIFIED (memory, inference, or a page I could not get). Treat every [U] as a hypothesis (global rule: Vendor First).
Raw pages for every [V] are in `research/dashboard/raw/arch-*.md` (index at the bottom).

---

## 0. The one idea that decides most of this

**Sold alerts do not need polling. All three marketplaces push.** Put one public HTTPS receiver on Supabase and let the platforms call it:

- Etsy webhooks: `order.paid`, `order.canceled`, `order.shipped`, `inventory.out_of_stock`, listing events. "Webhook functionality is available for both **commercial** and **personal** applications!" Signed (`webhook-id`, `webhook-signature`, HMAC-SHA256) and retried. [V] https://developers.etsy.com/documentation/essentials/webhooks
- eBay Notification API event `ORDER_CONFIRMATION`: "sent to a seller when the buyer completes the checkout process and payment clears". Needs an Authorization Code Grant token with `sell.fulfillment` scopes. [V*] `raw/ebay-notification-events.md` (source https://developer.ebay.com/develop/api/sell/notification_events). The legacy Platform Notification `ItemSold` also exists. [V*] `raw/ebay-pn-item-sold.md`. The Notification API lets you "configure and manage destination endpoints" and create subscriptions. [V] https://developer.ebay.com/api-docs/commerce/notification/overview.html
- Shopify webhooks: HTTPS endpoint, HMAC verification, dedupe on `X-Shopify-Webhook-Id`. [V] https://shopify.dev/docs/apps/build/webhooks . Sibling report `02-etsy-shopify.md` covers topics and the Dev Dashboard app change; not repeated here.

A Supabase Edge Function is public HTTPS, and on Pro it never pauses. So the box at home needs **no inbound access**. That removes the Cloudflare Tunnel / Tailscale Funnel question for this design (4b).

Polling is needed for only three things: eBay **watches** and **buy alerts** (Browse API search has no push), reconciliation (webhooks get missed), and residential-IP scraping jobs.

Why eBay item watches still poll even though the Notification API has item-level topics: `ITEM_AVAILABILITY` ("Sent when a fixed-price item's availability type changes"), `ITEM_PRICE_REVISION` and `PRIORITY_LISTING_REVISION` are each noted "Currently, this topic is available for eBay Partner Network (ePN) partners in all marketplaces except the following: CA, AU, HK, SG, MY, and PH." So they are ePN-gated, not available to a plain developer keyset. [V*] `raw/ebay-notification-events.md` (source https://developer.ebay.com/develop/api/sell/notification_events). Whether Ricky could qualify as an ePN partner is not answered by those pages **[U]**; if he could, known-item watches could be push and only new-listing searches would poll.

---

## 1. Supabase: pieces, limits, prices

### 1.1 Plans (verbatim)

| Item | Free | Pro | Source |
|---|---|---|---|
| Price | "$0 / month" | "From $25 / month. First project included. Additional projects from $10/mo." | https://supabase.com/pricing [V] |
| Compute | Shared CPU, 500 MB RAM | "Paid plans include $10/mo in compute credits, enough to cover one Micro instance." Micro = $10, 1 GB RAM, shared, Direct 60 / Pooler 200 connections | same [V] |
| Pausing | "Free projects are paused after 1 week of inactivity. Limit of 2 active projects." | Pausing: "Never" | same [V] |
| Automatic backups | "Not included in free" | "7 days" (daily) | same [V] |
| Log retention (API and DB) | 1 day | 7 days | same [V] |
| DB size | 500 MB | 8 GB then $0.125/GB | same [V] |
| Spend cap | n/a | "The Pro Plan has a spend cap enabled by default" | same [V] |
| Team plan | | $599/month | same [V] |

**Free has no backups.** For a business holding sales and inventory data, that, more than pausing, is the reason to be on Pro ($25).

### 1.2 The free-tier pausing rule (exact wording)

> "Supabase pauses Free Plan projects that show low activity over a 7-day period to save server resources." ... "A Free plan project is considered inactive if it does not receive sufficient user database activity over the past week. ... While you may be actively using the project, it's possible that usage is not enough to exclude it from automatic pausing. Typically a few user requests to the database each day over the previous week is enough to keep the project from being paused." ... "Projects under a paid plan cannot be paused and are not subject to automatic pausing for inactivity." ... "You can restore a paused project for up to 1 year after it was paused"
> https://supabase.com/docs/guides/platform/free-project-pausing [V]

Implications for always-on polling:
- A poller that hits the REST API every minute would plausibly count as "user requests". **Whether pg_cron work done entirely inside Postgres counts as "user database activity" is not stated. [U]** Do not rely on it.
- The doc itself hedges ("it's possible that usage is not enough"). A paused project means every webhook receiver, poller and alert silently stops. Pro removes the rule outright.
- Doc inconsistency: the anchor reads `#90-day-window-to-restore` but the body says "1-year window". The body wording is the current one.

### 1.3 Realtime

| | Free | Pro | Source |
|---|---|---|---|
| Concurrent connections | 200 | 500 (then $10 per 1,000 peak) | https://supabase.com/docs/guides/realtime/limits and /pricing [V] |
| Messages / second | 100 | 500 | limits [V] |
| Messages / month included | 2 million | 5 million, then $2.50 per million | https://supabase.com/docs/guides/realtime/pricing [V] |
| Broadcast payload | 256 KB | 3,000 KB | limits [V] |
| Postgres change payload | 1,024 KB; above that, `new`/`old` keep only fields of 64 bytes or less | same | limits [V] |

`postgres_changes` vs `broadcast` for this app: one or two users, so **use `postgres_changes`** (add the table to the `supabase_realtime` publication, enable RLS). The scaling doc says per-subscriber authorization is the cost: "If you expect more than ~3,000 concurrent subscribers on the same changes, use Broadcast". Irrelevant at 1-2 viewers. Caveat: "RLS policies are not applied to DELETE statements" (soft-delete instead of hard delete). https://supabase.com/docs/guides/realtime/postgres-changes [V]

### 1.4 Cron, pg_net, Queues, Database Webhooks

| Piece | Verbatim facts | Source |
|---|---|---|
| Cron (pg_cron) | "can run anywhere from every second to once a year"; "For best performance, we recommend no more than 8 Jobs run concurrently. Each Job should run no more than 10 minutes." Jobs live in `cron.job`, runs in `cron.job_run_details`. Created via SQL or Dashboard "Integrations -> Cron". | https://supabase.com/docs/guides/cron [V] |
| Scheduling an Edge Function | "The hosted Supabase Platform supports the `pg_cron` extension ... In combination with the `pg_net` extension, this allows us to invoke Edge Functions periodically on a set schedule." There is no separate scheduler on the function; it is pg_cron + `net.http_post`. The docs example is "every minute"; keep the URL and key in Vault; the function accepts the secret key via `auth: 'secret'` and `verify_jwt = false`. | https://supabase.com/docs/guides/functions/schedule-functions [V] |
| pg_net | Async HTTP from SQL. "HTTP requests are not started until the transaction is committed." `timeout_milliseconds int default 2000`. "reliably execute up to 200 requests per second". Responses kept "6 hours". "requests and responses are stored in unlogged tables, which are not preserved during a crash or unclean shutdown". POST is JSON only. | https://supabase.com/docs/guides/database/extensions/pg_net [V] |
| Queues (pgmq) | "Durable Message Queues with Guaranteed Delivery in Postgres"; "A Message is delivered exactly once to a consumer within a customizable visibility window." | https://supabase.com/docs/guides/queues [V] |
| Database Webhooks | "a convenience wrapper around triggers using the pg_net extension. This extension is asynchronous, and therefore will not block your database changes". HTTP POST/GET with JSON. Call history in the `net` schema. Can target an Edge Function. | https://supabase.com/docs/guides/database/webhooks [V] |

Gotchas that bite polling designs:
1. **pg_net's 2,000 ms default timeout** applies to the call from Postgres. Either set `timeout_milliseconds` explicitly, or make the Edge Function return at once and do the work in `EdgeRuntime.waitUntil(...)` ("The Function instance continues to run until the promise provided to `waitUntil` completes"). https://supabase.com/docs/guides/functions/background-tasks [V]
2. Because pg_net queues are unlogged and lost on crash, **the cron schedule is the source of truth, not the queued request**. Make every tick idempotent (cursor in a `poll_state` table, upsert on natural keys).
3. pgmq is available but not needed at this volume. A simpler retry: an `alerts.notified_at` column plus a one-minute sweeper cron that re-sends anything unsent. [design advice, not a vendor claim]

### 1.5 Edge Functions

| Limit | Value | Source |
|---|---|---|
| Wall clock | "Free plan: 150s / Paid plans: 400s" | https://supabase.com/docs/guides/functions/limits [V] |
| CPU time | "2s (Amount of actual time spent on the CPU per request - does not include async I/O.)" | same [V] |
| Memory | 256MB | same [V] |
| Request idle timeout | 150s (504 if no response) | same [V] |
| Outbound | "Outgoing connections to ports `25` and `587` are not allowed." (no SMTP from a function; use an HTTP email API) | same [V] |
| HTML | "Serving of HTML content is only supported with custom domains (Otherwise `GET` requests that return `text/html` will be rewritten to `text/plain`)." **Supabase cannot host the SPA.** | same [V] |
| Secrets | max 100 per project, 48 KiB each, names must not start `SUPABASE_` | same [V] |
| Invocations | Free "500,000 included"; Pro "2 Million included then $2 per 1 Million" | https://supabase.com/docs/guides/functions/pricing [V] |

Poll-budget arithmetic (inputs [V]): five 1-minute ticks = 5 x 43,200 = 216,000 invocations/month. That fits Free's 500,000 and is about 11% of Pro's 2,000,000. Time spent waiting on eBay does not count against the 2 s CPU limit.

### 1.6 Auth for one user

- Magic link / OTP: "By default, a user can only request a magic link once every 60 seconds and they expire after 1 hour." https://supabase.com/docs/guides/auth/auth-email-passwordless [V]
- **Built-in email is throttled to "2 emails per hour"**; configurable only with custom SMTP or the Send Email hook. https://supabase.com/docs/guides/auth/rate-limits [V] Logging in from a phone a few times in an hour would lock Ricky out. Use custom SMTP (Resend, 4). Custom SMTP is "Included in free" and on Pro. https://supabase.com/pricing [V]
- Passkeys: "Passkey support is experimental. The API may change without notice." Needs `@supabase/supabase-js` v2.105.0+ and opt-in `experimental: { passkey: true }`. "Changing the Relying Party ID makes every existing passkey unusable". https://supabase.com/docs/guides/auth/passkeys [V] Not ready to be the only login.
- Pro adds "Single session per user" and "Session timeouts" (Free: "Not included"). https://supabase.com/pricing [V]
- Recommendation: **6-digit email OTP** (same template, no link) for the phone. A tapped magic link may open in Safari instead of the installed Home Screen app [U]. Add TOTP later if wanted (Basic MFA is "Included in free" [V], pricing page).
- Turn sign-ups off once the first user exists [U: setting not read today].

---

## 2. Vercel, and whether it is needed

### 2.1 Vercel facts (verbatim)

- Hobby restriction: "Hobby teams are restricted to non-commercial personal use only. All commercial usage of the platform requires either a Pro or Enterprise plan." Definition: "Commercial usage is defined as any Deployment that is used for the purpose of financial gain of anyone involved in any part of the production of the project, including a paid employee or consultant writing the code." Examples include "Any method of requesting or processing payment from visitors of the site" and "Advertising the sale of a product or service". https://vercel.com/docs/limits/fair-use-guidelines#commercial-usage [V] (page "Last updated September 14, 2026"). Also https://vercel.com/docs/plans/hobby [V].
- Honest read: a private dashboard used to run a for-profit shop is "used for the purpose of financial gain" under that definition. A private page is the weakest case, and Vercel says to contact support if unsure, but do not plan on Hobby. The storefront will be unambiguously commercial.
- Pro: "$20/month Pro platform fee; 1 deploying team seat included; $20/month in usage credit"; extra paid seats "$20/month each". https://vercel.com/docs/plans/pro-plan [V]. A 14-day trial comes with $20 in credits. https://vercel.com/docs/cron-jobs/usage-and-pricing [V]
- Cron minimums: Hobby "100 cron jobs | Once per day | Per-hour (±59 min)"; Pro "100 cron jobs | Once per minute | Per-minute". A Hobby cron `0 1 * * *` "will trigger anywhere between 1:00 am and 1:59 am". https://vercel.com/docs/cron-jobs/usage-and-pricing [V]
- Function duration (Fluid compute): Hobby "300s (5 minutes)" default and max; Pro default 300s, max 800s, "1800s (30 minutes) Beta". https://vercel.com/docs/functions/limitations [V]

Vercel cron and functions are not part of the recommended design: pg_cron + Edge Functions already run next to the data for $0 extra.

### 2.2 Is Vercel even needed for a static Vite SPA?

No. A static SPA needs a CDN with HTTPS and an SPA fallback rewrite. Options:

| Host | Cost for a static SPA | Commercial-use clause | Notes |
|---|---|---|---|
| Vercel Pro | $20/mo [V] | Allowed (it is the paid plan) | On-stack; preview deploys; one team also hosts the storefront later |
| Vercel Hobby | $0 | **Forbidden** for commercial [V] | Do not use |
| Cloudflare (Workers static assets / Pages) | $0 | **No clause found on the pages I read [U]**; confirm Cloudflare's terms before relying on it | "Requests to static assets are free and unlimited." https://developers.cloudflare.com/workers/platform/pricing/ [V]. Pages Free: 500 builds/month, 20,000 files, 100 custom domains/project, 20 min build timeout. https://developers.cloudflare.com/pages/platform/limits/ [V] |
| Netlify | Free plan "Build and deploy free forever"; paid plans are credit-based | Not read [U] | https://www.netlify.com/pricing/ [V] for plan structure only |
| Supabase | n/a | n/a | Cannot serve HTML without a custom domain (1.5) [V] |

Verdict: **either** pay Vercel Pro $20 (stay on-stack; worth it the day the storefront also deploys there, since one Pro team covers both) **or** host the SPA at Cloudflare for $0 after checking their terms. The SPA is static, so moving later costs an afternoon. Whichever host: **pick the final domain first** (open question 2).

---

## 3. Where the pollers and receivers run

Scale: 5 = best.

| | (a) Supabase pg_cron + pg_net + Edge Fn | (b) Daemon in podman on the Fedora box | (c) GitHub Actions `schedule` | (d) $4-6 VPS |
|---|---|---|---|---|
| Always-on reliability | **4**: managed; Pro never pauses; runs next to the DB | **2**: home Wi-Fi, LUKS root, sudo-less network fixes | **2**: "some queued jobs may be dropped" | **4**: datacenter, but a single box you patch |
| Latency | **4**: 1-minute ticks (pg_cron allows seconds [V]); cold start about low seconds [U] | **5**: any interval | **2**: "shortest interval ... once every 5 minutes", delayed at "the start of every hour" | **5**: any interval |
| Cost | **5**: $0 beyond the $25 Pro already needed | **5**: $0 (owned hardware) | **3**: free on public repos; private = 2,000 free min/month | **3**: DO from $4/mo, Hetzner from EUR 5.99/mo excl. VAT |
| Operational burden | **4**: SQL + one Deno function, all in the repo | **2**: podman, systemd, Wi-Fi, updates, secrets on disk | **4**: YAML only | **2**: you are the sysadmin (SSH, patches, backups) |
| Fails how | Visible in `cron.job_run_details` and `net._http_response` (6 h retention); next tick retries; down only if Supabase is down | **Silent for days**. Precedent below | **Silent drops**; public repos auto-disabled after 60 days idle | Silent unless monitored |

Sources: pg_cron/pg_net/Edge limits, section 1 [V]. GitHub schedule: "The shortest interval you can run scheduled workflows is once every 5 minutes"; "The `schedule` event can be delayed during periods of high loads ... High load times include the start of every hour. If the load is sufficiently high enough, some queued jobs may be dropped."; "In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days." https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows [V]. Free minutes: GitHub Free "2,000" min/month, Pro "3,000"; standard runners free in public repos; Linux 2-core $0.006/min. https://docs.github.com/en/billing/concepts/product-billing/github-actions [V]. VPS: DigitalOcean "Bundled Plans start from as low as $4 per month" ($4 = 512 MiB/1 vCPU; $6 = 1 GiB) https://www.digitalocean.com/pricing/droplets [V]; Hetzner "starting from ... EUR 5.99 per month, excl. VAT" https://www.hetzner.com/cloud [V].

GitHub Actions cost for a private repo at a 5-minute cadence: 8,640 runs/month. If each run bills even 30 s that is 4,320 min against 2,000 free; if billed per whole minute, 8,640 min. The page I read did not state per-job rounding **[U]**, so both are shown; either way it breaks the free quota. Fine for an hourly reconciliation, not a primary poller.

**The Fedora box, with evidence** (Ricky's desk wiki, read today, `C:\Users\ethan\dev\Chief Of Staff\wiki\machine-stack.md`): it "lives on Wi-Fi" with a "LUKS-encrypted root"; "The Spectre was off the network from 2026-09-26 17:16 ET until Ricky fixed its Wi-Fi at 12:07 on 09-29" (about 3 days; jobs failed with `EAI_AGAIN`); "`nmcli` changes need sudo over ssh, and Wi-Fi power-save still read `on`". On the plus side, linger is on and `podman-restart.service` is enabled `--user`, so containers return after a reboot. A dead-man check that runs *on the box* goes silent with the box.

So the box is a **best-effort lane for residential-IP jobs** (crawl4ai sold-comp scraping, anything geo/rate-limit sensitive), not the critical path. It makes outbound calls only and writes rows to Supabase. It writes a heartbeat row; a Supabase cron flags it stale after N minutes.

**External dead-man switch** (so a dead pg_cron chain is also noticed): the tick function pings a Healthchecks.io check at the end of every successful run. Hobbyist is "$0 / month, Monitor 20 jobs". https://healthchecks.io/pricing/ [V]. Integration types and free-tier alert latency **[U]**; plain email is the default.

eBay polling budget (it binds cadence): Browse API "5000 API calls per day"; the client-credentials mint endpoint "1,000 requests/day"; an Application access token has `expires_in: 7200`. [V*] `raw/ebay-buy-call-limits.md`; [V] https://developer.ebay.com/api-docs/static/oauth-tokens.html . 5,000/day is 3.5 calls/min, so 20 saved searches every 10 minutes (2,880/day) fits and every 5 minutes (5,760/day) does not. Cache the app token in the DB; never mint per tick. (The item-level push topics that would cut this budget are ePN-gated; see section 0.)

---

## 4. Getting alerts onto the phone

Ricky's phone OS is unknown (open question 1; the `IMG_6607`/`Video.mov` filenames in the Drive folder suggest iPhone, which is inference only). The design must work on both, with iOS as the harder case.

### 4.0 "Delivered" is not "heard"

The desk wiki's fleet-alerting page records it: "Delivered is not the same as heard. ... all three alerts landed on the topic (read back via `poll=1`) and Ricky still learned of it from a screenshot." and "Whether the phone actually notifies on this topic is unverified." It also logs deadman sends failing, "so alerts will sometimes not arrive." (`C:\Users\ethan\dev\Chief Of Staff\wiki\fleet-alerting.md`, read today.) The selection question is therefore: which channel can *insist*?

### 4.1 Comparison

| Channel | Cost (verbatim) | Setup work | "Heard" mechanism | iOS | Android | Source |
|---|---|---|---|---|---|---|
| (c) **Pushover** | "$4.99 USD one-time purchase" per platform; 30-day free trial; "Each user can send up to 10,000 messages per month for free"; Teams "$5 USD per-user, per-month" | Lowest: one POST to `https://api.pushover.net/1/messages.json` with app token + user key | **Emergency priority 2**: repeated until acknowledged; `retry` at least 30 s, `expire` at most 10800 s, receipts + callback | native app | native app | https://pushover.net/pricing , https://pushover.net/api [V] |
| (b) ntfy.sh (public) | Free without sign-up; paid "Supporter $6/$5 per month (2,500 daily messages), Pro $12/$10 (20k), Business $25/$20 (50k)"; free-tier daily limit **[U]** (the 60-burst / 1-per-5s figures are self-host config defaults, not ntfy.sh's anonymous limits) | Very low; Ricky's phone **already has a topic** per the wiki | None. "If you use ntfy without sign-up, the topic is essentially a password" | App via APNs through ntfy.sh | App (FCM on ntfy.sh) | https://ntfy.sh/ , https://docs.ntfy.sh/config/ [V] |
| (b') ntfy self-hosted on Fedora | $0 + a public path | Needs ingress AND an upstream: "you have to forward so called `poll_request` messages to the main ntfy.sh server"; `upstream-base-url: "https://ntfy.sh"`; without it "delivery can take hours" ("shouldn't take more than 20-30 minutes though") | None | still depends on ntfy.sh | foreground service unless you build your own apk for Firebase | https://docs.ntfy.sh/config/#ios-instant-notifications [V] |
| (a) Web Push from the PWA | $0 | Highest: VAPID keys, service worker, subscription table, library, install to Home Screen | None; on iOS, silent-push penalties and Focus modes can mute it | **Home Screen web app only**, iOS 16.4+ | Chrome / Samsung Internet | https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/ [V] |
| (d) Telegram bot | "By default, bots are able to message their users at no cost"; limits: 1 msg/s per chat, about 30/s bulk | Low: Bot API over HTTPS | None (user mutes apply) | Telegram app | Telegram app | https://core.telegram.org/bots/faq [V]. Latency not documented **[U]** |
| (e) SMS via Twilio | "$0.0083 per 160-character segment" base, plus automatic carrier fees (e.g. "AT&T charges $0.0035 for outbound SMS, while T-Mobile charges $0.0045") and US A2P 10DLC registration fees | High: number + registration | Carrier SMS | any | any | https://www.twilio.com/en-us/sms/pricing/us [V] |
| (f) Email via Resend | Free "3,000 emails / mo", "100 emails a day", 3 domains; Pro $20/mo, 50,000/mo | Low (needs a sending domain) | None | Mail app | Mail app | https://resend.com/pricing [V] |

### 4a. Web Push, if built (and the iOS caveats)

- Needs an active service worker to subscribe via `PushManager.subscribe()`; the endpoint "is a unique capability URL" and must be kept secret. https://developer.mozilla.org/en-US/docs/Web/API/Push_API [V]
- iOS: only for "a web app that has been added to the Home Screen"; the permission prompt must come "in response to direct user interaction"; it uses Apple Push Notification service and needs no Apple Developer membership; allow `*.push.apple.com`; integrates with Focus; Badging API supported. https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/ [V]
- iOS reliability traps: `userVisibleOnly: true` is required and "if an event handler doesn't show the user visible notification for any reason we revoke its push subscription"; ITP can delete service-worker registrations for sites "you haven't visited in a while". https://webkit.org/blog/16535/meet-declarative-web-push/ [V]. Home Screen web apps have their own usage counter, so "We do not expect the first-party in such a web application to have its website data deleted". https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/ [V]
- Mitigation: send **Declarative Web Push** payloads (iOS 18.4+): top-level `"web_push": 8030`, a `"notification"` object with a non-empty `"title"`, and a required `"navigate"` URL. There is "no penalty for service workers failing to display a notification", and the format is backwards compatible with browsers that lack it, provided the service worker `PushEvent` handler also reads the JSON. [V] same URL. I did not test Android Chrome with it.
- Deno library: JSR `@negrel/webpush` ("works with Cloudflare Workers, Deno, Bun, Browsers", v0.5.0 published a year ago; author's note: "hasn't been reviewed by crypto experts and may be unsecure"). https://jsr.io/@negrel/webpush [V]. The mainstream `web-push` is described as a "Web Push library for Node.js"; whether `npm:web-push` runs under Supabase's Deno runtime **[U]**. Supabase's own push example covers Expo and Firebase Cloud Messaging for native apps, not Web Push. https://supabase.com/docs/guides/functions/examples/push-notifications [V]
- Android is easier: Chromium needs a manifest with `name`/`short_name`, a 192 px and a 512 px icon, `start_url`, `display`, HTTPS. https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable [V]

### 4b. Self-hosting ntfy: not worth it

It needs a public ingress AND the `upstream-base-url` to ntfy.sh for iOS anyway (above), so it adds a moving part without removing the dependency. If an ingress were ever needed: Cloudflare Tunnel is outbound-only ("`cloudflared` initiates an outbound connection through your firewall"), https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/ [V]; its price on the free plan was not stated on pages I got **[U]**. Tailscale Funnel "is currently in beta" and "available for all plans", but **the free Personal plan "is only suitable for non-commercial use"** (https://tailscale.com/docs/features/tailscale-funnel and https://tailscale.com/pricing [V]), which excludes a business. Not needed under section 0.

### 4c. Recommendation: one primary, one fallback

- **Primary: Pushover.** $4.99 once, both OSes, one HTTPS POST from an Edge Function, and the only option here with a documented insist-until-acknowledged mode (priority 2). Use priority 1 for buy alerts and priority 2 only for "must act now" (an auction about to end, a payment failure). Latency is undocumented **[U]**; measure it in week one.
- **Fallback: ntfy.sh** (the topic and app Ricky already has). Fire it when the Pushover API call returns non-2xx, or when a priority-2 receipt expires unacknowledged. Independent vendor and relay (both end in APNs/FCM, so a phone-side problem such as Focus or Do Not Disturb hits both; that is a human fix).
- **Phase 2 (optional): Web Push** from the installed PWA once it is in daily use. In-app, the open dashboard already updates live over Supabase Realtime.
- **Email (Resend)** is not an alert channel; it is the Supabase Auth SMTP (the 2-per-hour fix) and the home for a daily digest.
- Skip Telegram unless Pushover disappoints (free, but a second app and no insist mode). Skip Twilio (per-message cost plus A2P registration).

---

## 5. Mobile UI delivery

### 5.1 PWA in 2026

| Topic | Fact | Source |
|---|---|---|
| Installability (Chromium) | manifest with `name`/`short_name`, `icons` incl. 192 px and 512 px, `start_url`, `display` and/or `display_override`, `prefer_related_applications` false or absent; HTTPS (or localhost). A service worker is not a requirement. | https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable [V] |
| Android | Real WebAPK only from "Chrome on devices with Google Mobile Services (GMS), and Samsung Internet on Samsung devices"; other browsers add a shortcut | same [V] |
| iOS install paths | "On iOS 16.4 and later, PWAs can be installed from the Share menu in Safari, Chrome, Edge, Firefox, and Orion." | same [V] |
| iOS 26 | "By default, every website added to the Home Screen opens as a web app" (toggle "Open as Web App"); "there are now zero requirements for 'installability' in Safari" | https://webkit.org/blog/17333/webkit-features-in-safari-26-0/ [V] |
| iOS push | Home Screen web apps only (4a); permission on user gesture | WebKit 13878 [V] |
| Icons on iOS | Manifest icons supported since iOS 15.4; `apple-touch-icon` takes precedence if both exist | WebKit 13878 [V] |
| Storage eviction | Home Screen web apps have their own usage counter; not expected to lose data | WebKit 10218 [V] |
| What iOS still lacks / differs | Push only after install; silent push forbidden; service-worker registrations can be evicted for unvisited sites (Safari tab). An Android-style `beforeinstallprompt` install prompt on iOS **[U]**. Background sync / silent wake-ups **[U]** (not read). | see above |

Safe areas: `viewport-fit=cover` ("The viewport is scaled to fill the device display. It's highly recommended to use the safe area inset variables") plus `env(safe-area-inset-top|right|bottom|left)` padding. https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport and https://developer.mozilla.org/en-US/docs/Web/CSS/env [V]. Tie this to the house rule: `h-full`/`dvh`, never `h-screen`; pad the bottom tab bar with `env(safe-area-inset-bottom)`.

Dark mode: `prefers-color-scheme` + `color-scheme` + manifest `theme_color`/`background_color` **[U]** (not fetched; standard but unverified here). Test in installed standalone mode on the real phone; iOS standalone status-bar styling differs from a Safari tab **[U]**.

### 5.2 Capacitor later?

Capacitor is "a cross-platform native runtime" that makes "Web Native apps" from an existing web project (v8 docs). https://capacitorjs.com/docs [V]. Costs: Google Play "a US$25 one-time registration fee" https://support.google.com/googleplay/android-developer/answer/6112435 [V]; Apple Developer Program fee **[U]** (the enrollment page I got showed no price; widely quoted as $99/yr). The main reason to wrap, reliable native push, is already covered by Pushover. **Defer Capacitor** until there is a feature the web cannot do (camera/barcode pipeline, App Store presence).

---

## 6. Secrets and token rotation

Where each secret lives:

| Secret | Home | Why |
|---|---|---|
| eBay cert/client secret, Etsy keystring + shared secret, Shopify client id/secret, VAPID keys, Pushover app token + user key, ntfy topic, Healthchecks ping URL, webhook signing secrets | **Edge Function secrets** (Dashboard or CLI; local `supabase/functions/.env`, gitignored) | Static values read via `Deno.env.get`; 100 secrets / 48 KiB; `SUPABASE_` prefix reserved. https://supabase.com/docs/guides/functions/secrets [V] |
| Rotating OAuth state (access + refresh tokens, expiry timestamps) | **Postgres: Vault** (`vault.create_secret` / `vault.update_secret`) or one `oauth_tokens` table with RLS on and no anon/authenticated policies | Edge secrets are env vars set from the Dashboard/CLI; a function cannot rewrite them hourly. Vault stores "using Authenticated Encryption on disk"; backups and replication keep that encryption. https://supabase.com/docs/guides/database/vault [V] |
| `pg_cron` -> function auth key | Vault (`vault.create_secret(... 'secret_key')`), per the schedule-functions doc | That doc warns: "Any role that can log in to your database can read the secret key while the request waits" in `net.http_request_queue`. [V] |
| Fedora box | `~/secrets.env` outside any repo, per desk wiki | wiki `machine-stack.md` 2026-09-25 [V]; prefer a Supabase key scoped to one insert-only RPC [design advice] |

Per-vendor token facts:

| Vendor | Access token | Refresh token | Rotation handling | Source |
|---|---|---|---|---|
| eBay | `"expires_in": 7200` (2 hours) | `"refresh_token_expires_in": 47304000` s = 547.5 days (about 18 months); "can be unexpectedly revoked" (user changes name, revokes consent, or eBay revokes) | Refresh grant returns a new access token; re-consent when the refresh token expires. App token (client credentials) is capped at 1,000 mints/day, so cache it. | https://developer.ebay.com/api-docs/static/oauth-tokens.html [V] |
| Etsy | `expires_in: 3600` (1 hour) | 90 days ("has a longer functional lifetime (90 days)") | The refresh response includes a `refresh_token` field and the doc says to send "the refresh token string sent with a prior Authorization Code Grant or Refresh Grant" (implies it can change). **Persist whatever comes back, every time.** PKCE required on authorization. | [V*] `raw/etsy-shopify-etsy-auth.md` (https://developers.etsy.com/documentation/essentials/authentication) |
| Shopify (Dev Dashboard app, client credentials) | "Tokens expire after 24 hours" (`expires_in` always 86399) | none (re-request with client id/secret) | Works only when "the app and the store belong to the same Shopify organization". | https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant [V] |

Rotation rules to build in [design advice]:
1. One refresher at a time: take a Postgres advisory lock (or `select ... for update`) around read-refresh-write, so two overlapping ticks cannot both spend a single-use refresh token.
2. Write the new refresh token in the same transaction that records the new access token.
3. Expiry watchdog: alert when a refresh token is within 14 days of expiry (Etsy's 90 days is the tight one; eBay returns `refresh_token_expires_in`).
4. Prefer webhooks (section 0) so a token problem degrades reconciliation, not sold alerts. Verify signatures on every inbound call (Etsy HMAC-SHA256, Shopify `X-Shopify-Hmac-Sha256`, eBay verification per `raw/ebay-guide-account-deletion.md`).

---

## 7. Cost and "what runs where"

### 7.1 Monthly cost, recommended architecture

| Line | Option A (on-stack) | Option B (cheapest sane) | Notes / source |
|---|---|---|---|
| Supabase Pro | $25 | $25 | includes $10 compute credit = one Micro instance [V] |
| SPA hosting | Vercel Pro $20 | Cloudflare $0 (terms check [U]) | [V] 2.1 / 2.2 |
| Edge Function invocations | $0 (about 216k of 2M included) | $0 | [V] 1.5 |
| Realtime | $0 (1-2 connections, far under 500 and 5M msgs) | $0 | [V] 1.3 |
| Pushover | $4.99 one time (not recurring) | same | per platform; $5/user/mo only on the Teams plan [V] |
| ntfy.sh fallback | $0 | $0 | free tier; daily cap [U] |
| Healthchecks.io | $0 (Hobbyist, 20 jobs) | $0 | [V] |
| Resend (auth SMTP) | $0 (3,000/mo, 100/day) | $0 | [V] |
| Fedora box | $0 incremental (electricity not estimated) | $0 | owned |
| GitHub Actions | $0 (not used for scheduling) | $0 | |
| Domain | about $1/mo | about $1/mo | **[U]** price not fetched |
| **Recurring total** | **about $45-46/mo** | **about $25-26/mo** | plus $4.99 once |
| Prototype floor | | $0 (Supabase Free + Cloudflare) | **not recommended**: no backups, pausing risk, 1-day logs |
| Later add-ons | Capacitor: Google Play $25 once [V], Apple program [U] | Twilio SMS about $0.012+ per message [V] | optional |

### 7.2 Diagram

```
 SELLING PLATFORMS (push first)               SUPABASE PRO ($25, never pauses)                       PHONE (iOS or Android)
 ------------------------------               --------------------------------                       ----------------------
 Etsy    --order.paid / out_of_stock--+
 eBay    --ORDER_CONFIRMATION---------+--HTTPS--> Edge Fn: webhook-in (verify sig, dedupe by id)
 Shopify --orders/* ------------------+                    | upsert
                                                           v
 eBay Browse API <--poll-- Edge Fn: tick <--pg_net-- pg_cron (1-10 min; idempotent; cursor in poll_state)
 (5,000 calls/day cap)         |  \                        |
                               |   '--ping--> Healthchecks.io (dead-man; emails you if the chain stops)
                               v                           v
                    Postgres: orders, inventory, watches, alerts, poll_state, heartbeats,
                              oauth_tokens (Vault)
                                    |  insert into alerts            | postgres_changes (Realtime, RLS)
                                    v                                v
              DB webhook --> Edge Fn: notify                  React 19 PWA (installed to Home Screen)
                    |  quiet hours, dedupe                    served by Vercel Pro OR Cloudflare static
                    |--> Pushover API (priority 1/2) ------------------------> native Pushover app = the "heard" channel
                    '--> on non-2xx / unacked: ntfy.sh/<topic> ----------------> ntfy app (fallback)
                    sweeper cron (1 min): resend alerts where notified_at is null

 FEDORA BOX (home, Wi-Fi) = best-effort lane, outbound only, no inbound port
   crawl4ai / SearXNG sold-comp jobs --insert--> Postgres
   writes a heartbeats row; Supabase cron flags it stale (box failure never blocks sold or buy alerts)
```

### 7.3 When each part fails

| Part | Symptom | Safety net |
|---|---|---|
| Supabase down | everything stops | status page; Healthchecks emails you; Etsy "automatically retries delivery" |
| pg_cron chain dies / Edge Fn errors | watches go stale | Healthchecks missed-ping email; sweeper retries; `cron.job_run_details` |
| Webhook missed | one sold alert lost | hourly reconciliation tick compares platform orders to `orders` |
| Pushover down or rejects | alert not delivered | ntfy.sh fallback on non-2xx |
| Phone-side mute (Focus/DND) | delivered, not heard | priority-2 receipt unacked -> fallback; otherwise a human fix |
| Refresh token revoked/expired | one platform goes dark | expiry watchdog + re-consent link in the dashboard |
| Fedora box offline | only scraping lanes stall | heartbeat-stale alert raised from the Supabase side |

---

## 8. Discrepancies and verified-vs-needs-review (rule 4)

- Verified: free-tier pausing wording; Pro never pauses; Vercel Hobby non-commercial; cron minimums; Edge limits; pg_cron seconds; iOS push facts; all three marketplaces have webhooks or notifications.
- **Supabase pausing page**: anchor `#90-day-window-to-restore` vs body "1-year window". Body used.
- **Etsy auth doc**: the refresh section's parameter table says `grant_type` must be `refresh_token`; the prose says `grant_type=refresh_code`. Use `refresh_token`. [V*] `raw/etsy-shopify-etsy-auth.md`
- **Tailscale**: Funnel "is available for all plans", yet Personal is "only suitable for non-commercial use". A business needs a paid plan.
- **ntfy pricing**: the page shows paired prices ("$6$5/ month", "$12$10", "$25$20") under a Monthly/Annually toggle; I could not tell which is which. Treat the higher number as monthly billing [U].
- **eBay**: "18 months" appears for legacy Auth'n'Auth tokens in prose and as `refresh_token_expires_in: 47304000` for OAuth; they agree.
- Needs review (UNVERIFIED): Cloudflare commercial terms; Cloudflare Tunnel price; ntfy.sh anonymous daily limit; `npm:web-push` under Deno; Pushover/Telegram latency; whether pg_cron-internal activity counts toward Free pausing; Apple $99 fee; dark-mode and iOS standalone status-bar behavior; whether OTP vs magic link opens inside the installed PWA; the Supabase "disable sign-ups" setting; Healthchecks free-tier integrations; GitHub per-job minute rounding.

---

## Recommendation

1. **Backend: Supabase Pro ($25).** Etsy, eBay and Shopify webhooks land on one Edge Function; pg_cron + pg_net ticks poll only eBay watches and run a reconciliation sweep. Everything idempotent, cursors in `poll_state`.
2. **Alerts: producers insert into `alerts`; one `notify` function** sends **Pushover** (primary, priority 2 for must-act) with **ntfy.sh** as fallback, while the open dashboard updates via Realtime `postgres_changes`. Web Push is phase 2.
3. **UI: installable React 19 PWA** (manifest, `viewport-fit=cover`, safe-area padding, `dvh`), email OTP login over Resend SMTP; host on Vercel Pro $20 or Cloudflare $0; fix the domain before installing anything.
4. **Fedora box: outbound-only, best-effort scraping lane** with heartbeat rows; no tunnel, no self-hosted ntfy. Healthchecks.io is the outside dead-man.
5. **Tokens:** static secrets in Edge secrets; rotating OAuth state in Vault with an advisory lock and an expiry watchdog.

## Open questions

1. **Phone: iPhone or Android?** (Filenames hint iPhone; unconfirmed.) Decides how much to invest in Web Push and whether Pushover alone suffices.
2. **Final domain.** Passkey RP ID ("Changing the Relying Party ID makes every existing passkey unusable"), the installed PWA origin, and a Web Push subscription ("Each subscription is unique to a service worker") all bind to it. Pick it before Ricky installs or enrolls anything.
3. **Vercel Pro vs Cloudflare** for the SPA: will the storefront land on Vercel (then Pro pays for both)? Confirm Cloudflare's commercial terms if choosing it.
4. **One Supabase project for dashboard and future storefront, or two?** Extra projects are "from $10/mo".
5. **How fresh must buy alerts be?** eBay's 5,000 Browse calls/day sets the cadence floor per saved search; is an Application Growth Check worth pursuing to raise it?
6. **eBay Notification API prerequisites** for Ricky's keyset: the account-deletion challenge flow is in `raw/ebay-guide-account-deletion.md`; whether it is mandatory for his production keyset was not confirmed.
7. **Fedora box**: move it to Ethernet / fix Wi-Fi power-save, or accept best-effort? Needs sudo for `nmcli`.
8. **Second user later?** Pushover is $4.99 per platform per user (or Teams $5/user/mo); RLS needs a `shop_id` or role model from day one.
9. Measure in week one: Pushover and ntfy end-to-end latency, and whether Focus/DND swallow either.

---

## Index of raw pages fetched (research/dashboard/raw/)

Supabase: `arch-sb-pricing`, `arch-sb-pausing`, `arch-sb-realtime-limits`, `arch-sb-realtime-pricing`, `arch-sb-realtime-pgchanges`, `arch-sb-cron`, `arch-sb-pgcron` (stub page), `arch-sb-pgnet`, `arch-sb-queues`, `arch-sb-db-webhooks`, `arch-sb-fn-limits`, `arch-sb-fn-pricing`, `arch-sb-fn-schedule`, `arch-sb-fn-bgtasks`, `arch-sb-fn-secrets`, `arch-sb-fn-push`, `arch-sb-vault`, `arch-sb-auth-passwordless`, `arch-sb-auth-ratelimits`, `arch-sb-passkeys`.
Vercel/hosting: `arch-vc-pricing`, `arch-vc-hobby`, `arch-vc-pro`, `arch-vc-fairuse`, `arch-vc-cron`, `arch-vc-cron-pricing`, `arch-vc-fn-limits`, `arch-cf-pages-limits`, `arch-cf-workers-pricing`, `arch-netlify-pricing`.
Schedulers/VPS: `arch-gh-events`, `arch-gh-billing`, `arch-healthchecks-pricing`, `arch-hetzner-cloud`, `arch-do-droplets`.
Push/alerts: `arch-mdn-push`, `arch-webdev-push`, `arch-webkit-webpush`, `arch-webkit-declarative-push`, `arch-webkit-itp-storage`, `arch-webkit-safari26`, `arch-jsr-negrel-webpush`, `arch-webpush-npm-readme`, `arch-ntfy-home`, `arch-ntfy-config`, `arch-ntfy-publish`, `arch-ntfy-faq`, `arch-pushover-pricing`, `arch-pushover-api`, `arch-telegram-api`, `arch-telegram-faq`, `arch-twilio-sms-2`, `arch-resend-pricing`, `arch-cf-tunnel`, `arch-cf-tunnel-pub`, `arch-cf-zerotrust`, `arch-cf-zt-plans`, `arch-ts-funnel`, `arch-ts-pricing`.
PWA/native: `arch-mdn-installable`, `arch-mdn-css-env`, `arch-mdn-viewport-meta`, `arch-capacitor-docs`, `arch-apple-memberships`, `arch-apple-enroll`, `arch-gplay-fee`.
Vendor tokens/webhooks: `arch-ebay-oauth-tokens`, `arch-ebay-notification-overview`, `arch-etsy-webhooks`, `arch-shopify-client-creds`, `arch-shopify-webhooks`.
Read from sibling raw files: `ebay-notification-events`, `ebay-pn-item-sold`, `ebay-buy-call-limits`, `ebay-guide-account-deletion`, `etsy-shopify-etsy-auth`. Desk wiki: `Chief Of Staff/wiki/machine-stack.md`, `fleet-alerting.md`.
Walled or empty (not relied on): Apple web-push docs page (272 bytes, deleted), first Twilio attempt (0 bytes, deleted; retried as `arch-twilio-sms-2`).
