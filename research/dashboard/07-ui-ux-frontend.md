# Dashboard UI/UX and frontend tooling: screens, interaction, verified stack, design tokens

Hollywood and Vine (Vintage repo) · research note 07 · **2026-10-26** · research and design only, nothing built in the repo.

Legend (same spirit as notes 03 and 05).
- **[V]** read today (2026-10-26) on the cited live page (crawl4ai) or queried live from the npm registry.
- **[V-WF]** read today through WebFetch/WebSearch, which returns a model-written summary, so treat quotes as paraphrase-grade.
- **[RUN]** I ran or built it today in a throwaway project in the session scratchpad (outside this repo, nothing committed). Compiles and builds are real; nothing was run against a live Supabase project.
- **[U]** UNVERIFIED: memory, inference, community report, or a page I could not read. A hypothesis, not a fact.

Raw pages are in `research/dashboard/raw/ui-*.md` (index at the end). Three pages that returned bot-wall stubs (two W3C WCAG pages, one Stack Overflow thread) were deleted; the WCAG ones were re-read via WebFetch.

---

## 0. Read this first

1. **Five tabs and one pushed screen, no "More" tab.** Today · Alerts · Watches · Inventory · Sales, plus Item detail (pushed from any row). Settings hangs off an avatar button, not a tab. Apple's tab-bar guidance says to avoid overflow "More" tabs [V-WF, search summary of the HIG page; the HIG page itself is JavaScript-rendered and was not read directly].
2. **The loop nobody sells (note 03) is the spine of the UI:** Buy alert → "Bought" (inventory item created with the price as cost basis) → listed by the sync tool → Sold alert → profit. Every screen is a view of one stage of that loop.
3. **The dashboard decides, records and links out. It does not list, delist or crosslist.** Note 03 says buy the sync tool and do not build a crosslister or delist engine. So the wireframes have "Open on eBay" buttons and read-only per-channel status chips, never "Delist" or "Post".
4. **The cardinal sin is a double sale** (03: missed sale → double sale, the top complaint for Vendoo, Crosslist and Sellbrite). So a sold alert always shows the other channels' listing status, and "still live elsewhere" is the top item on Today.
5. **Stack, all verified today** (section 3): Vite 8.3.5 + React 19.3.1 + Tailwind 4.3.3 + shadcn/ui 4.22.1 (CLI) + vite-plugin-pwa 2.0.0 + supabase-js 2.118.0 + **react-router 8.5.0** in declarative mode. Three things differ from the brief's assumptions: react-router **v8** is current (v7 is the previous major and `react-router-dom` no longer exists in v8); **TypeScript 7.0.2 is `latest` on npm but the Vite template still pins `~6.0.3`**; shadcn's default dark mode is **class-based**, not `prefers-color-scheme`.
6. **No chart library.** One Recharts bar chart added **+103.6 kB gzip** (137.97 → 241.54 kB) to a 138 kB baseline [RUN]. Sparklines are an inline SVG polyline, the monthly bar chart is flex divs. Both compile in the scratch project.
7. **No TanStack Query.** Realtime pushes the changes; a 25-line hook does select + `postgres_changes` + refetch on every `SUBSCRIBED` (section 3.6).
8. **shadcn's default (Nova preset) Button is 32 px tall** (`h-8`; `icon` is `size-8`; `lg` is `h-9`) [RUN, read from the generated `button.tsx`]. Under the 44 px target. The token sheet overrides the sizes (section 4.5).
9. **App-icon badge counts wait for Web Push (phase 2).** On iOS the badge appears only after notification permission is granted [V] https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/ . v1 has in-app tab badges only. Pushover is the "heard" channel.
10. **Pushover deep links on iPhone probably open Safari, not the installed app** [U], and Safari has no session. So the design never depends on a deep link: opening the app lands on the newest unread alert, and the Pushover `url` points at the listing.
11. **eBay and Etsy content rules shape five behaviours** (note 10, C5 to C10, C22, C50, C7): every eBay card prints "as of <time>" and disappears or is marked after 6 hours without a refresh; eBay cards live in their own section with no cost, margin or other-site columns, and never interleave with sales; ended listings vanish; no chart ranks one channel against another; a privacy page and the Etsy trademark sentence are in the footer. Section 2.10.

---

## 1. Information design for a one-person reseller

### 1.1 What the commercial tools put on a phone (read today)

| Tool | What the phone shows | Steal | Avoid | Source |
|---|---|---|---|---|
| **Vendoo** (mobile app) | Listing create/edit/delist/relist, sale detection (marketing page), label manager, multi-quantity, photo editor and background remover, 8 marketplaces. Inventory page splits items into **drafted / listed / sold**; filter and sort by status, title, SKU, price, platform listed, platform *not* listed, date created, date modified, **stalest**, custom labels; **tap a marketplace icon to open the live listing**. Analytics: profit, revenue, average sale price, top categories and brands, customisable by label. [V] | Status as the primary split; "stalest" as a sort; marketplace icon = link to live listing; labels | A learning curve that needs videos (App Store review); a mobile app that can not do what desktop does | https://www.vendoo.co/mobile-app , https://help.vendoo.co/en/articles/6260262-vendoo-inventory-management-tools , https://www.vendoo.co/reselling-analytics |
| **Crosslist** (mobile) | "List, edit, and manage your inventory across all major marketplaces directly from your phone"; relist, delist, update, AI listing; "account stays synced with desktop in real time". Sales tracking carries cost of goods, shipping, estimated profit and margin (note 03). [V] | One account state for phone and desktop | Listing tools (out of scope) | https://crosslist.com/features/mobile-app , https://docs.crosslist.com/knowledge-base/sales/sales-tracking |
| **Flipwise** (eBay only) | Live store view: sales, profit, costs, ROI, where buyers are. Inventory: what you have, **what it cost, where it is stored**. **"Sale & location alerts: tells you the instant something sells, and exactly where it's stored."** Unlisted inventory ("log items the moment you buy them, connect them to listings later"). Per-item **product timeline**. Error detection (duplicate shipping charges, failed relists). [V] | **Storage location on the sold alert** (so the item needs a `location` field); log-at-purchase; item timeline | eBay-only scope | https://flipwise.app/ |
| **Flippd** | Home surfaces automatic reports and a daily "Coach" card; P&L daily/monthly/YTD; **Aging Inventory Insights**; **Data Health** (items with no cost, sales with no price or platform, out-of-order dates, listings with no photo, duplicates); storage locations nested 3 deep; barcode scan-and-add; light and dark mode. Release notes: "saving an item on a slow connection no longer reports a failed save or creates a duplicate"; "open the live eBay listing for any synced item with one tap"; "number fields accept a comma as the decimal separator". [V] | Data Health as a to-do list; aging view; one-tap to live listing; **idempotent saves**; dark mode | AI coach (not asked for); mileage and tax suite | https://getflippd.com/features , https://apps.apple.com/us/app/flippd-reseller-inventory/id1633899291 |
| **Shopify app** | Orders, fulfilment, inventory, analytics (visitors, orders, campaigns), notifications, Quick Sale, Apple Watch stats, home-screen **widgets** (an Insights widget and an order Counter), biometric login. A staff member without permission for Home simply does not see the Home button. [V] | Counter-style "one number" glance; permission-trimmed UI | Everything else (store builder) | https://www.shopify.com/mobile , https://help.shopify.com/en/manual/shopify-admin/shopify-app/using-shopify-mobile-widgets |

Not read: Shopify's actual tab names, any screenshot of any app (marketing pages describe screens in prose; images were not inspected) **[U]**. The wireframes below are therefore designed from the feature lists and complaints, not copied from a screenshot.

### 1.2 What resellers complain about in the UI (and the rule each one produces)

Sources: note 03 section 3 (Trustpilot, Shopify App Store, Capterra; Reddit was unreadable), plus today's Vendoo App Store reviews (https://apps.apple.com/us/app/vendoo-a-sellers-best-friend/id1612168777 , raw `ui-vendoo-appstore-reviews.md`) [V]. Reviews are individual opinions, not measurements.

| Complaint (evidence) | Rule for this dashboard |
|---|---|
| Missed sale, then a double sale (03: Vendoo, Crosslist, Sellbrite reviews, 2026-09 to 2026-10) | Every sold alert shows per-channel listing status; "still live elsewhere" is Today's first row and escalates after 20 minutes (threshold is a guess, tune it) |
| "Pretty big learning curve ... diligent to watching videos" (Vendoo App Store) | Five tabs, plain nouns, no jargon, no onboarding video. Empty states teach (section 2.5) |
| "Marketplace connections on the mobile app and desktop platform are managed separately" (Vendoo's own reply to a one-star review) | One Supabase state; phone and desktop are the same React app. Nothing is configured per device |
| "I only have four products and it showed around 100 used" (Vendoo item-limit counter) | Never show a counter the user can not reconcile by eye. Counts equal the visible list length, filters included |
| "Error messages often and have to close it out and re-start" (Vendoo App Store) | Errors render in place with a Retry button; the app never needs a restart. Stale data is shown with a timestamp, not blanked |
| Random disconnects: "often having to reconnect depop and mercari" (03, Trustpilot 2026-10-24) | A Connections row on Settings, and a banner on Today when a channel token or the poller heartbeat is stale (05 has the heartbeat table) |
| Profit is only as good as manually entered cost (03: Flipwise "you add only what eBay can't see: your cost, where you bought it, and where it's located"; My Reseller Genie: no sourcing-location field) | Cost, source and location are first-class item fields, captured at purchase. "Bought" from an alert prefills them. Profit shows an asterisk when a sale has no cost, and the asterisk links to the fix list |
| Features shown but locked or in beta inside the flow (Vendoo "Import & Merge" beta; add-ons that paywall imports, 03) | No dead buttons. If a thing is not built it is not rendered |
| Duplicate records after a bad connection (Flippd's own fix note) | Client-generated UUIDs on every insert, `insert ... on conflict do nothing`, so a retry can never duplicate |

### 1.3 The screens

Six screens: five tabs and one pushed detail. Each has one job and one primary action.

| # | Screen | One job | Primary action | Shows | Realtime tables |
|---|---|---|---|---|---|
| 1 | **Today** | "Is anything on fire, and what did I make?" | Tap the top "Needs you" row | Sold today / 7 days / month with a sparkline, profit (asterisk if cost missing), **Needs you** list, recent activity | `sales`, `alerts`, `channel_listings`, `integrations` |
| 2 | **Alerts** | Decide on each match; confirm each sale | Bought / Not this / Open on eBay | Segmented Buy · Sold · All. Buy cards: photo, price vs your cap, source, distance, **"Fits" reason**, auction countdown. Sold cards: channel, gross, fees, net, cost, profit, **location**, other-channel status | `candidates`, `alerts`, `sales`, `channel_listings` |
| 3 | **Watches** | Say what to hunt for | Create / toggle a watch | List: name, on/off, price cap, source, cadence, last match, matches this week. Editor (full-height sheet): see the editor wireframe in 1.5 | `watches`, `candidates` (for counts) |
| 4 | **Inventory** | Know what I own, what it cost, where it is | Add item (FAB) | Filter chips (status, channel, aged, missing cost, no photo), search, rows with thumb, cost → ask, margin before fees, per-channel status chips, age in days, location | `items`, `channel_listings` |
| 5 | **Sales** | Know the real numbers | Switch month | Month switcher; Revenue · Fees · Cost · Profit · Margin; 12-month bars; by-channel table with fees; sale list | `sales` |
| 6 | **Item detail** (pushed) | Everything about one thing | Edit / Open on channel | Photos, per-channel status with Open links, money, location, source, timeline (bought, listed, alerts, sold), notes | `items`, `channel_listings`, `sales` |

Not screens: **Settings** (avatar menu: account, notifications and a Pushover test button, quiet hours, connections health, Data Health, install help, sign out), the **Add item** sheet, the **Watch editor** sheet, and the **Bought** confirm sheet.

### 1.4 Data the UI reads, mapped onto note 06's tables

Note 06 (`06-data-model-metrics.md`) holds a tested DDL: `items`, `channel_listings`, `sales` (one row per order line), `expenses`, `events`, `watches`, `candidates`, `alerts`, `integrations`. This note was designed from the screens first; the table below maps each screen need onto 06 and lists what 06 **lacks** for the UI. Those gaps are requests to the schema owner, not decisions. Column names in the wireframes follow the screens; this table is the translation.

| UI need | 06 column that serves it | Gap or mismatch |
|---|---|---|
| Item title, category, condition, source, location, notes, ask price | `items.title`, `category`, `condition`, `source`, **`location`**, `notes`, `target_price` | none. `location` already exists (the Flipwise "where is it stored" idea) |
| Item status chip | `items.status` = `draft` · `active` · `sold` · `withdrawn` | UI labels: Draft, **Listed** (= `active`), Sold; Withdrawn hides behind a filter. No `hold` or `archived` |
| Per-channel chips and "Open on eBay" | `channel_listings.channel`, `status` (`draft` · `active` · `sold` · `ended`), `url`, `price`, `listed_at`, `ended_at`, `last_seen_at` | The table is `channel_listings`, not `listings`; "live" in the wireframes is `active`. No `error` status; a listing-sync failure shows through `integrations` instead |
| Cost and the "missing cost" asterisk | `items.cost_purchase`, `cost_other`, generated `cost_basis` | `cost_purchase` is `not null default 0`, so **"unknown" and "free" are the same value**. 06's own SQL treats `cost_basis = 0` as `cost_missing`. The UI follows 06: `0` renders as `Cost --` and counts toward the asterisk. A genuinely free item needs a way to be confirmed (a "Free" toggle, or a nullable column). Decision for the schema owner |
| Add item without typing an id | `items.sku` is `not null unique` | The Add sheet must never ask for it. It needs a DB default or trigger (`HV-0001`, `HV-0002`, ...) or client-side generation |
| Add item category | `items.category` check: `fashion`, `art`, `lamp`, `decor`, `print`, `furniture`, `rug`, `other` | The category control is a native `<select>` of exactly these eight |
| Photos | `items.photo_refs` jsonb: `[{"kind":"drive","id":...},{"kind":"storage","path":...}]` | The UI resolves each ref to a URL; photos taken on the phone are written as `kind: "storage"` |
| Sale totals, fees, profit | `sales.item_price`, `fees_total` (generated), **`fee_source`** (`api` · `estimated` · `manual`), `shipping_cost`, `net_proceeds` (generated), `status`, `is_effective`; the profit views in 06 section 2 | **Estimated fees must look estimated** (a `~` prefix and a footnote). `shipping_cost` is nullable ("not known yet"), so profit can be provisional on two axes: cost and shipping |
| Unmatched sales | `sales.item_id` is nullable; index `sales_unmatched_idx` ("must stay visible") | The UI needs an **"Unmatched sale" row with a Match button** (a sheet that picks an item), on Sales and in Today's hygiene row |
| Alerts, unread, badge | `alerts.kind` (`sold`, `buy_match`, `price_drop`, `stale_listing`, **`oversell_risk`**, `integration_down`, `token_expiring`, `digest`), `severity`, `title`, `body`, `payload`, `acked_at` | There is no `read_at`. **Open decision for the 06/05 owner:** 06 indexes `acked_at is null` as the unacknowledged set, and 05's ntfy fallback keys off an unacknowledged priority-2 receipt, so an in-app glance that wrote `acked_at` could silently stop an escalation. Recommended: a separate UI-owned `seen_at` (unread = `seen_at is null`), leaving `acked_at` to the push-receipt path. Buy tab = `buy_match` (+ `price_drop`), Sold tab = `sold`, All also shows the system kinds. `oversell_risk` is exactly the "still live elsewhere" row on Today |
| Buy card | `candidates.title`, `price`, `shipping`, `condition`, `buying_option`, `bid_count`, `url`, `image_url`, `end_at`, `found_at`, `status`, `item_id` (set when bought) | **Missing:** `fit_reason` (the one-line "Fits:" text), `fit_score`, `starred` (auction watch), `dismiss_reason` (the five chips in note 04), and a distance string. `status` also has `ended`, which the UI greys out and sorts last |
| Watch list and editor | `watches.name`, `keywords` (max 100 chars, the eBay `q`), `keywords_exclude[]`, `category_id` (one eBay leaf), `price_min`, `price_max`, `conditions[]`, `buying_options[]`, `cadence_minutes` (1 to 1440), `active`, `last_run_at`, `last_ok_at`, `last_error` | **Missing:** the plain-language `description` the tier-2 matcher reads, and `alert_mode` (push or inbox only). The editor's category select needs a small lookup from friendly names to eBay leaf ids. "Skip if it says" = `keywords_exclude`; "must include" words fold into `keywords`. The editor's "Include auctions" toggle maps to `buying_options` (note 04: Browse silently excludes auctions unless asked; 06 defaults to both) |
| Connections row and Today's connection banner | `integrations.status`, `last_ok_at`, `last_error`, `heartbeat_at`, `token_expires_at` | none; this is the heartbeat table 05 described |
| Item timeline | derive from `items.acquired_on` / `created_at`, `channel_listings.listed_at` / `ended_at`, `alerts`, `sales.sold_at` | No new table. `events` is the raw webhook inbox, not a user-facing history |

Notes. 06 stores money as `numeric(12,2)` **dollars**, not cents, and PostgREST returns `numeric` as JSON numbers; do totals in SQL views, format with `Intl.NumberFormat`, and never add prices in JavaScript floats. Today's totals and the Sales rollup come from one view or RPC per month. Profit is null-aware in the UI exactly as 06's views define it; the asterisk means "some of these rows have no cost or no shipping cost yet".


### 1.5 Wireframes (phone, 390 px wide, one frame = one screen)

Conventions. `[Text]` is a 44 px-tall button. `( )` is a segmented control or toggle. `*` after a number means "partial: some sales lack a cost". Tab labels in production are Today, Alerts, Watches, Inventory, Sales (shortened here to fit 34 characters). Channel chips use a letter code plus a state glyph, never colour alone: `E` eBay, `Et` Etsy, `S` Shopify; `+` live, `-` not listed, `!` needs a look, `$` sold.

**Screen 1: Today**

```text
+----------------------------------+
| ~ OS status bar ~ (safe-area top)|
+----------------------------------+
| Hollywood & Vine      * Live  (R)|
+----------------------------------+
| SOLD TODAY                       |
| $184                      2 sales|
| __/\__/\_/\/_  7-day sparkline   |
| Week $612        Month $2,140    |
| Profit (month) $1,020*    48%    |
+----------------------------------+
| NEEDS YOU                       4|
| [!] Scarf sold on Etsy. Still    |
|     LIVE on eBay.      [Open >]  |
| [$] 2 new buy matches [Review >] |
| [~] Auction ends in 1h 40m       |
|                          [View >]|
| [?] 3 sales lack a cost*  [Fix >]|
+----------------------------------+
| RECENT                           |
| (img) SOLD  Silk scarf  +$28.90  |
| (img) BOUGHT Brass lamp    -$18  |
| (img) SOLD  Rug 5x8      +$210   |
+----------------------------------+
| Today Alerts Watches Stock Sales |
|       (3)                        |
| ~ home indicator ~ (safe-area)   |
+----------------------------------+
```

How to read it. The header dot is the Realtime state (`Live`, `Reconnecting`, `Offline, saved 4:12 PM`); tapping it forces a refetch. `(R)` is the avatar button that opens Settings. **Needs you** is ordered by severity: (1) double-sale risk, (2) unread buy matches, (3) starred auctions ending within 24 h, (4) connection or heartbeat problem, (5) data hygiene (missing cost, aged 90+ days). Show at most four rows and a "See all" link; an empty list says "Nothing needs you" in the muted colour, which is a feature. **Recent never lists eBay watch hits**: note 10 (C9) requires them to stay visually isolated from non-eBay content, so Today shows only the count of new matches, never their titles.

**Screen 2: Alerts** (a Buy card, then a Sold card; scroll between them)

```text
+----------------------------------+
| Alerts              Mark all read|
| ( Buy 2 )   Sold 1    All        |
+----------------------------------+
| * NEW                       2 min|
| +--------+ Stiffel brass lamp    |
| |        | $62         cap $80   |
| | photo  | eBay, Buy It Now      |
| |        | Fort Myers, 12 mi     |
| +--------+                       |
| Fits: brass, Stiffel-style, 22in,|
| under your $80 cap.              |
| Watch: Stiffel lamps  as of 9:41 |
| [Open on eBay]    [Not this v]   |
| [      Bought at $62      ]      |
+----------------------------------+
| AUCTION  ends 1h 40m   [Star]    |
| Vtg Playboy lot (12)  bid $14    |
| ...                              |
+----------------------------------+
| $ SOLD                    9:12 am|
| Silk scarf          Etsy $38.00  |
| Fees ~$3.10     Net $34.90       |
| Cost $6.00      Profit $28.90    |
| Stored: Rack B, hook 3           |
| Other channels                   |
|  eBay     [ok] ended             |
|  Shopify  [!] STILL LIVE         |
|                  [Open Shopify >]|
| [Seen]                           |
+----------------------------------+
| Today Alerts Watches Stock Sales |
|       (3)                        |
+----------------------------------+
```

- **Swipe is an accelerator, never the only path.** Swipe right = Bought, swipe left = Not this, and both are always visible as buttons (WCAG 2.2 SC 2.5.7 requires a single-pointer alternative to dragging [V-WF] https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html ).
- **Not this** opens a one-row chip picker (the five reasons in note 04: wrong item, too expensive, bad condition, bad seller, already have) and then dismisses with a 5-second **Undo** toast. The reason is optional; tapping outside dismisses with no reason.
- **Bought** opens a small sheet (below), then creates the inventory item with `cost_cents` = the price paid and `origin_candidate_id` set. This is the single most valuable tap in the product: it is where cost basis is captured for free.
- **Open on eBay** goes to `itemWebUrl` (human in the loop; note 04 says eBay forbids auto-buy flows).
- **Compliance on this card (note 10).** The "as of 9:41" stamp is `candidates.last_seen_at`; a card whose last refresh is older than 6 hours is hidden or marked "N h older than eBay" (C5, C50). eBay cards are their own component in their own section: **the "All" segment is grouped (Buy matches, then Sales), never one merged timeline**, and a buy card carries no cost, margin, comp or other-site column (C9). A card disappears when its listing ends (C8). Its "Fits:" line is per-listing inference and expires with the listing (C11).
- The **Sold** card reads the other channels from `channel_listings`; note 06 already has an `oversell_risk` alert kind for the same condition. A channel that is not `ended` or `sold` after 20 minutes turns the row red, adds the item to Today's top row, and (backend) can fire a priority-1 Pushover. If the sync tool (Crosslist) auto-delists within its documented 15 minutes (note 03), the row flips to `ended` by itself and nothing escalates.
- Unread = `alerts.seen_at is null` (a recommended new column; see the `acked_at` decision in 1.4). A card is marked seen when it has been on screen for 1.5 seconds, not on tab open, so a glance at a locked-screen preview does not clear anything.

**Bought sheet** (bottom sheet over Alerts)

```text
+----------------------------------+
| Bought: Stiffel brass lamp       |
+----------------------------------+
| Paid for it                      |
| [ $62.00 ]  (prefilled, editable)|
| Shipping + tax (optional)        |
| [ $ 0.00 ]                       |
| Bought from                      |
| [ eBay seller brasslamps_fl ]    |
| Stored at                        |
| [ Rack B, hook 3 ]               |
| [    Add to inventory    ]       |
| Cancel                           |
+----------------------------------+
```

Three fields beyond the prefilled price, all optional except the price. The sheet's primary button is 44 px or taller and sits above the keyboard; the numeric field uses `inputmode="decimal"` so a comma decimal works (Flippd shipped a fix for exactly that).

**Screen 3: Watches** (list, then the editor sheet)

```text
+----------------------------------+
| Watches                     [ + ]|
+----------------------------------+
| Stiffel lamps             (ON  o)|
| brass lamp stiffel, skip repro   |
| up to $80 - eBay - every 15 min  |
| Last match 2 min - 14 this week  |
+----------------------------------+
| Vintage Playboy           (ON  o)|
| 1970s issues, complete, no cut   |
| up to $25 - eBay - every 30 min  |
| Last match 3 h - 4 this week     |
+----------------------------------+
| Chanel books           (paused o)|
| up to $60 - eBay - every 1 h     |
| Last match 2 d                   |
+----------------------------------+
| Today Alerts Watches Stock Sales |
+----------------------------------+
```

```text
+----------------------------------+
| Cancel       New watch       Save|
+----------------------------------+
| Describe it, in plain words      |
| [ brass table lamp, Stiffel     ]|
| [ style, not a reproduction     ]|
| Must include (optional)          |
| [ brass  lamp ]                  |
| Skip if it says                  |
| [ repro  reproduction  parts ]   |
| Price   Min [____]  Max [ 80 ]   |
| Condition  (Any) New  Used       |
| Include auctions     (On)  Off   |
| Category   [ Lamps          v ]  |
| Where to look                    |
| [x] eBay  [ ] ShopGoodwill  ...  |
| Check every   [ 15 minutes v ]   |
| Alert me      (Push) Inbox only  |
| [ Test: what would this find? ]  |
+----------------------------------+
| Last run would have matched 3:   |
| (img)(img)(img)                  |
+----------------------------------+
```

- The first field is a **plain-language sentence** (note 04's tier-2 matcher reads it); "must include" and "skip" are the cheap deterministic filters that run first. This is the product gap in note 03, so the form puts the sentence first, not a keyword grid.
- **Test** runs the watch once against the source without saving or alerting and shows up to six thumbnails. It is the fastest way to teach Ricky what the matcher understands, and it is the one watch-editor feature worth building in v1.
- Cadence options come from the API budget in note 04 (3, 15, 30, 60 minutes, daily); do not offer a faster cadence than the budget allows.
- Native `<select>`, `<input type="number" inputmode="decimal">` and `<input type="checkbox">` everywhere. iOS and Android render their own pickers for free; shadcn's Select adds nothing on a phone.

**Screen 4: Inventory** (list, FAB, and the Add sheet)

```text
+----------------------------------+
| Inventory                41 items|
| [ Search title, SKU, location  ] |
| All 41 Listed 28 Draft 9 Sold 4  |
| Aged 60+   No cost   No photo    |
| Sort: Stalest first          v   |
+----------------------------------+
| (img) Brass lamp, Stiffel        |
|       Cost $18  Ask $85   79%    |
|       E+ Et+ S-   34 d           |
|       Rack B, hook 3             |
+----------------------------------+
| (img) Velvet chair               |
|       Cost --  (!)  Ask $240     |
|       Et+          92 d          |
|       Floor, back room           |
+----------------------------------+
| (img) Silk scarf            SOLD |
|       Cost $6  Sold $38  Et$     |
|       E x  S !    (check)        |
+----------------------------------+
|                       [ + Add ]  |
| Today Alerts Watches Stock Sales |
+----------------------------------+
```

```text
+----------------------------------+
| Cancel       New item        Save|
+----------------------------------+
| [ Take photo ]  [ From library ] |
| (img)(img)(img)                  |
| What is it?                      |
| [ Brass table lamp, Stiffel     ]|
| What did you pay?                |
| [ $ ____ ]                       |
| Bought from                      |
| [ Estate sale, Cape Coral       ]|
| Stored at                        |
| [ Rack B, hook 3                ]|
| More: category, condition, ask,  |
| notes                           v|
| [        Save item        ]      |
| Save and add another             |
+----------------------------------+
```

- The sheet never asks for the SKU (06 makes `items.sku` `not null unique`; generate it in the database or on the client). Three fields are enough: photo, title, cost. Everything else is optional and the item saves as `draft`. This is the Flipwise "log items the moment you buy them" idea and the answer to "profit is only as good as the entered cost".
- The photo picker is `<input type="file" accept="image/*" capture="environment">` plus a second input without `capture` for the library [U: standard HTML behaviour, not re-read today]. Uploads go to Supabase Storage; resize on the client before upload.
- Each row's channel chips are links: tapping one opens that live listing (Vendoo's pattern), not the item detail. Tapping anywhere else on the row opens Item detail.
- The "No cost" filter is the Data Health view in one chip. A row with no cost shows `--` and a `(!)` glyph, and counts toward the asterisk on Today.

**Screen 5: Sales**

```text
+----------------------------------+
| Sales                < Oct 2026 >|
+----------------------------------+
| Revenue   Fees    Cost    Profit |
| $2,140    $212    $880   $1,048* |
| Margin 49%   17 sales   avg $126 |
+----------------------------------+
| Last 12 months                   |
|          #                       |
|        # #   #       #  # #      |
|  # # # # # # # # # # # # # #     |
|  N D J F M A M J J A S O         |
+----------------------------------+
| BY CHANNEL                       |
| eBay      9   $1,010  fee $131   |
| Etsy      6     $790  fee  $60   |
| Shopify   2     $340  fee  $21   |
+----------------------------------+
| SALES (17)                       |
| Oct 25  Silk scarf   Et  +$28.90 |
| Oct 24  Rug 5x8      S   +$131.0 |
| Oct 22  Lamp pair    E    +$55.4 |
+----------------------------------+
| Today Alerts Watches Stock Sales |
+----------------------------------+
```

- "Profit" is net of fees, shipping and cost; the `*` means "N sales have no cost or shipping cost yet, tap to fix". Note 06 records `fee_source` (`api`, `estimated`, `manual`): an estimated fee renders with a `~` prefix and the footer reads "~ = estimate until the platform reports the real fee".
- A sale with no matching item (`item_id` null) renders as an **Unmatched sale** row with a Match button; 06 insists these stay visible.
- **By channel** is a fixed alphabetical block of Ricky's own numbers with no "best channel" highlight, ranking or commentary (note 10, C22). Buyer names never appear; if a geography view is ever wanted it is state-level only (C15).
- The bar chart is flex divs with a `role="img"` and an `aria-label` that reads the numbers; a visually-hidden table gives the same data to a screen reader.
- CSV export is a desktop-only button in the header (accountant at tax time; Flippd and Vendoo both export). Not on the phone.

**Screen 6: Item detail** (pushed; back arrow top-left, swipe-back must work)

```text
+----------------------------------+
| < Back       Brass lamp, Stiffel |
+----------------------------------+
| [ photo carousel  1 / 4 ]        |
| LISTED - 34 days - Rack B, hook 3|
+----------------------------------+
| CHANNELS                         |
| eBay     live   $85    [Open >]  |
| Etsy     live   $89    [Open >]  |
| Shopify  not listed              |
+----------------------------------+
| MONEY                            |
| Cost $18.00   Ask $85.00         |
| Margin before fees  79%          |
| Bought: Estate sale, Oct 2       |
+----------------------------------+
| TIMELINE                         |
| Oct 2   Bought, $18, Rack B      |
| Oct 3   Listed on eBay, Etsy     |
| Oct 24  Price lowered to $85     |
+----------------------------------+
| Notes                            |
| [ Missing finial, see photo 3 ]  |
| [        Edit item        ]      |
+----------------------------------+
```

No "List on Shopify" button: listing is the sync tool's job (note 03). "Not listed" is just a status. If Shopify listing from the dashboard is ever wanted, that is a separate decision, not a UI default.

**Settings** (avatar button; a pushed list, not a tab)

```text
+----------------------------------+
| < Back              Settings     |
+----------------------------------+
| Signed in as ricky@...           |
| [ Sign out ]                     |
+----------------------------------+
| NOTIFICATIONS                    |
| Pushover key       [ Test push ] |
| Quiet hours      22:00 to 07:00  |
| Alerts in this app only?   (off) |
+----------------------------------+
| CONNECTIONS                      |
| eBay      ok   checked 2 min ago |
| Etsy      ok   checked 1 min ago |
| Shopify   ! token expired        |
|                        [Fix >]   |
| Poller heartbeat   ok  4 min ago |
+----------------------------------+
| DATA HEALTH                      |
| 3 sales without a cost    [Fix >]|
| 2 items without a photo   [Fix >]|
+----------------------------------+
| Install on iPhone                |
| Share > Add to Home Screen       |
+----------------------------------+
| ABOUT                            |
| Privacy policy                   |
| Etsy trademark notice            |
+----------------------------------+
```

The About block carries the footer notices note 10 requires (C7): a public `/privacy` route that works without logging in, and the sentence "The term 'Etsy' is a trademark of Etsy, Inc. This Application uses Etsy's API, but is not endorsed or certified by Etsy.", in smaller type than the app's own branding. The same footer appears on the login screen.

### 1.6 Desktop layout (same components, sidebar instead of bottom tabs)

One React tree, one component set. Only the shell and three layouts change at Tailwind breakpoints (`md` 768 px and `lg` 1024 px; Tailwind's defaults [U: not re-read today]).

```text
 < md (phone)                    md to lg (tablet)       lg and up (desktop)
 +--------------------+          +----+-------------+    +---------+---------------+--------------+
 | header             |          |rail| content     |    | sidebar | list          | detail       |
 | content (scrolls)  |          |72px|             |    |  240px  | (Alerts,      | (selected    |
 |                    |          |icon|             |    | Today   |  Inventory)   |  card or     |
 +--------------------+          |+lbl|             |    | Alerts  | 420px         |  item)       |
 | 5 tabs + safe area |          +----+-------------+    | Watches |               |              |
 +--------------------+                                   | Stock   |               |              |
                                                          | Sales   |               |              |
                                                          | ------  |               |              |
                                                          | Settings|               |              |
                                                          +---------+---------------+--------------+
```

- **Shell.** `h-dvh flex`; below `md` a bottom `<nav>`; at `md` a 72 px icon rail with labels under the icons; at `lg` a 240 px sidebar. The same `NavLink` list renders all three, so badge counts and the active state are one implementation.
- **Today** becomes two columns: KPIs and Needs you on the left, Recent on the right.
- **Alerts and Inventory become master/detail** at `lg`: the list stays at 420 px on the left and the selected alert card or Item detail renders on the right instead of pushing. The detail component is the same; only its container differs. On a phone, selecting pushes a route; on desktop the route renders into the right pane (React Router nested routes with an `<Outlet />`).
- **Inventory** gains a real table below the chip row at `lg` (columns: photo, title, status, cost, ask, margin, channels, age, location), because a dense table is a desktop affordance and a bad phone one. Do not use shadcn's Table on the phone.
- **Sales** adds the CSV export button and widens the bar chart to 24 months.
- **Pointer-aware sizing.** `pointer-coarse:h-11 pointer-fine:h-9` builds correctly in Tailwind 4.3.3 (it emitted `@media (pointer:coarse)`) [RUN]. Use it on dense desktop rows, but keep every phone target at 44 px.
- **Keyboard (desktop only, optional):** `j` / `k` move through alerts, `b` Bought, `d` Not this, `o` open the listing. Cheap to add with one `keydown` listener once the list has a selection; skip until asked.


---

## 2. Navigation and interaction

### 2.1 Navigation

- **Bottom tab bar on phones, five items, icon plus text label always visible** (icons from `lucide-react`; an icon-only bar is a guessing game). Height 56 px plus `env(safe-area-inset-bottom)`; each tab is a full-cell target about 78 × 56 px. Active tab: brand colour, a 2 px top indicator, and `aria-current="page"`. Apple's guidance is to use only as many tabs as navigation needs, keep the bar visible during navigation, use it for navigation and not actions [V-WF, search summary of the HIG].
- **State lives in the URL.** `/` Today · `/alerts?tab=buy|sold|all` · `/watches` · `/inventory?status=listed&aged=60&nocost=1&q=lamp` · `/sales?month=2026-10` · `/items/:id` · `/settings`. Filters in the query string mean Back works, a filter set on the desktop can be opened on the phone, and nothing needs a state library. Scroll position per tab: a module-level `Map<pathname, scrollTop>` saved on route change and restored on return (about 10 lines) **[U: not built]**.
- **Back button in the header of every pushed screen.** An installed iOS web app has no browser chrome, so a visible back arrow is mandatory; whether the iOS edge-swipe-back gesture works in a Home Screen web app is **[U]**, test on the real phone.
- **Sheets, not pages, for short tasks** (Bought, Add item, Watch editor, Not-this reasons): `vaul` bottom drawer on phones (what shadcn's `drawer` installs for the Radix style [RUN]); the same content in a centred dialog at `md` and up.
- **From push to app.** Pushover messages carry one supplementary URL (`url` up to 512 characters, `url_title` up to 100, message up to 1,024; re-read in note 09 E1) that opens in the device browser (or the app configured for it) [V] https://pushover.net/api#urls (raw `arch-pushover-api.md`). Set `url` to the **listing**, put title, price and the fit reason in the message body (so the glance is enough), and rely on "open the app, newest unread is on top". A link into the PWA would likely open Safari, which has a separate storage container from the Home Screen app and therefore no login **[U]**; test it on the real phone before designing anything around it.

### 2.2 Realtime instead of pull-to-refresh

No pull-to-refresh gesture. Four freshness mechanisms instead:

1. **`postgres_changes` over one WebSocket** keeps every list current (section 3.6 has the hook). Free-tier limits are far above one user (200 concurrent connections, 2 million messages a month; 05 section 1.3).
2. **Refetch on every `SUBSCRIBED`.** The supabase-js `subscribe((status, err) => ...)` callback reports `SUBSCRIBED`, `CHANNEL_ERROR` and `TIMED_OUT` [V] https://supabase.com/docs/reference/javascript/subscribe . A phone that was in a pocket reconnects, gets `SUBSCRIBED`, and the hook reselects, so a gap never leaves a stale list. (A suspended iOS WebSocket is the reason Pushover, not the page, is the "heard" channel; 05 section 4.)
3. **Refetch on `visibilitychange` → visible and on the `online` event.** Cheap insurance. Not built **[U]**.
4. **The header dot is a manual refresh.** `Live` (neon pink dot) · `Reconnecting` (amber) · `Offline, saved 4:12 PM` (grey, with the timestamp). Tapping it refetches. When not live, show "Updated 3 min ago" under the title.

Why not build the gesture: iOS Home Screen web apps reportedly have no native pull-to-refresh **[U: community forum threads only; Apple documents nothing and the Stack Overflow thread was walled]**, so it would be a custom touch handler for a problem Realtime already solves. On Android Chrome the native pull-to-refresh would reload the whole SPA mid-edit; set `overscroll-behavior-y: contain` on the main scroller. MDN: you can use `overscroll-behavior` "to get rid of unwanted scroll chaining and the browser's 'pull to refresh'-type behavior" [V] https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior ; Tailwind 4.3.3 emits `overscroll-behavior-y:contain` for `overscroll-y-contain` [RUN]. Whether it fully suppresses the reload inside an installed Android PWA is **[U]**.

### 2.3 Swipe actions on Alert cards

- Right = **Bought** (opens the Bought sheet, because the cost has to be confirmed), left = **Not this** (opens the reason chips, then dismisses). Both are also always-visible buttons (section 1.5). Swipe is an accelerator.
- Commit threshold about 35% of the card width; below it the card springs back. Use pointer events with `touch-action: pan-y` so vertical scrolling still works, about 40 lines, no library (`react-swipeable` 7.0.2 and `@use-gesture/react` 10.3.1 exist [V npm]; not measured, not needed).
- Ignore a swipe that starts within about 20 px of the left screen edge, to avoid fighting a possible system back gesture **[U]**.
- Every dismissal is optimistic and shows a **5-second Undo toast** (`sonner` 2.0.8, the toast component shadcn now ships). Undo restores the previous `status`. Never a confirm dialog.

### 2.4 Badge counts

- **Single source:** `count(alerts where seen_at is null)`, computed from the same Realtime-fed array the list renders, so the badge can never disagree with the list.
- **Where:** Alerts tab (pill, caps at `9+`), the segmented control (`Buy 2`, `Sold 1`), and the desktop sidebar item. Today and Inventory get no badge. One style: neon-pink pill on dark, deep-pink on light, `aria-label="3 unread alerts"`.
- **Desktop browser tab title:** `(3) Hollywood & Vine` when unread > 0. Free and works in a background tab.
- **App-icon badge** via `navigator.setAppBadge(n)` / `clearAppBadge()` (Badging API, also callable from a service worker) [V] https://developer.mozilla.org/en-US/docs/Web/API/Badging_API . On iOS it needs notification permission first: "Once a user gives permission to allow notifications, the icon on the Home Screen will immediately display the current badge count" [V] https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/ . So it ships with Web Push in phase 2, not in v1.

### 2.5 Empty states (copy is part of the design)

Each says what is true, what happens next, and offers one button. No illustrations in v1.

| Screen | Copy | Button |
|---|---|---|
| Today, day one | "Nothing sold yet. When something sells on eBay, Etsy or Shopify it shows up here." | none |
| Today, nothing urgent | "Nothing needs you." (muted) | none |
| Alerts · Buy, no watches | "You have no watches yet. Describe what you hunt for, like 'brass table lamp, Stiffel style, under $80'." | Create a watch |
| Alerts · Buy, watches exist | "No new matches. Your watches look every 15 minutes." | none |
| Alerts · Sold | "No sales alerts yet." | none |
| Watches | "A watch is a saved hunt: words, a price cap, a place to look. You get a push when something fits." | Create a watch |
| Inventory | "Add the first thing you own: a photo, a name, and what you paid." | Add item |
| Inventory, filter returns none | "Nothing matches these filters." | Clear filters |
| Sales, empty month | "No sales in October 2026." | none |
| Any list, load failed | "Couldn't load this. Showing saved data from 4:12 PM." (or "Nothing saved yet.") | Retry |

### 2.6 Loading

- **Skeleton rows with the final row height** (shadcn `Skeleton`), shown only if loading exceeds 150 ms. Because Ricky's own lists (items, sales, watches, sold alerts) are seeded from a localStorage snapshot (section 2.7; eBay and Etsy content is deliberately excluded), a returning visit usually shows data instantly and refreshes underneath.
- **Buttons**: label stays, a spinner replaces the icon, the button disables while pending. Disabling is a convenience; the real double-submit protection is the client-generated UUID and `on conflict do nothing`.
- **Photos**: fixed aspect-ratio box in the surface colour, `loading="lazy"`, `decoding="async"`, so no layout shift. Thumbnails come from a resized variant, not the original.

### 2.7 Offline behaviour

- **The shell works offline.** vite-plugin-pwa's default `generateSW` build precached the app (6 entries, about 525 KiB, including the Geist font files) [RUN].
- **Reads: a snapshot of Ricky's own data only.** `items`, `sales`, `watches` and `sold` alerts are written to `localStorage` after a successful load (cap 200 rows) and read first on the next launch. **Never snapshotted: `candidates`, `channel_listings` and `buy_match` alerts.** They hold eBay and Etsy listing content that note 10 (C5, C6, C8, C50) says may not be shown more than 6 hours stale and must be deleted when the listing ends. Offline, the Buy tab says "Buy matches need a connection (eBay's licence limits how long they can be shown)" and Item detail channel rows drop their prices. The banner says "Offline, saved copy from 4:12 PM". Every `localStorage` access sits in try/catch because it can throw or come back empty in private windows or after site data is cleared **[U: general browser behaviour, not re-read today]**.
- **Writes: disabled while offline, with the reason in the banner. No general write queue in v1.** A queue means conflict handling and duplicate protection; Flippd's own release notes show duplicates after slow saves are a real failure mode. `navigator.onLine` is not trusted **[U]**; "offline" is derived from the Realtime state plus a failed request.
- **One exception worth deciding on (open question 6):** logging a purchase at an estate sale with bad signal. If that is common, add a single-purpose **outbox for Add item only**: a pending item (UUID, fields, photo blobs in IndexedDB) that retries an idempotent upsert when online. Not built; not needed if he always has signal.

### 2.8 Dark mode and the shop palette

- **`prefers-color-scheme` only, no in-app toggle in v1.** The OS decides; `color-scheme: light dark` on `:root` makes native controls follow **[U: standard CSS, not re-read today]**.
- **shadcn's generated CSS is class-based and has to be changed.** `shadcn init` wrote `@custom-variant dark (&:is(.dark *))` and a `.dark { ... }` block [RUN]. Replacing the variant with `@custom-variant dark (@media (prefers-color-scheme: dark))` and moving the variables into `@media (prefers-color-scheme: dark) { :root { ... } }` builds cleanly and emits the media blocks [RUN]. With every colour a variable on `:root`, components rarely need `dark:` classes at all.
- **`shadcn add sonner` imports `next-themes`** (a Next.js-oriented package; its `useTheme` does nothing useful in a plain Vite app). Delete the import and pass `theme="system"`; both are in the generated file and the edit builds [RUN].
- **Address-bar colour per scheme:** `<meta name="theme-color" content="#faf7f2" media="(prefers-color-scheme: light)">` and a second tag for dark; MDN documents the `media` attribute on `theme-color` [V] https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color . The web manifest takes only one `theme_color` and `background_color`, and vite-plugin-pwa's guide says the manifest value "must match" the meta tag [V]; pick the dark value for the manifest (a dark splash is on-brand) and treat the light-mode splash flash as a known trade-off **[U: how each OS paints the splash was not tested]**.
- **Accent rules (the "sparingly" part).** The base is neutral warm paper (light) or near-black plum (dark). Accents cover at most about 10% of any screen, one accent per component:
  - **Burgundy** `#6b2540`: primary buttons and the wordmark in light mode.
  - **Rose** `#e58fb0`: the same role in dark mode.
  - **Neon pink** `#b8135f` light / `#ff5fae` dark: unread badge, `Live` dot, `NEW` tag, focus ring. Nothing else.
  - **Gold** `#7f6200` light / `#e0b84a` dark: money in (SOLD tag, positive profit). Nothing else.
  - No gradients. No glow. One badge pulse when a new alert arrives, disabled under `prefers-reduced-motion`.

### 2.9 Accessibility checklist

| Rule | Detail | Evidence |
|---|---|---|
| Touch targets 44 × 44 CSS px | Every phone control. Spacing of at least 8 px between neighbours. shadcn's Nova defaults (32 px button, 24 px `xs`) must be overridden (4.5). | WCAG 2.2 SC 2.5.5 (AAA) "at least 44 by 44 CSS pixels" [V-WF] https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html ; SC 2.5.8 (AA) floor "at least 24 by 24 CSS pixels" [V-WF] https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html . Apple's own 44 pt figure was **not** read: **[U]** |
| Text contrast ≥ 4.5:1 (large text ≥ 3:1) | Every token pair is computed in 4.1. Large text is 18 pt or 14 pt bold | SC 1.4.3 [V-WF] https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html |
| UI components and focus indicators ≥ 3:1 | Input borders use the `--control-border` token (4.1), not the decorative card hairline | SC 1.4.11 [V-WF] https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html |
| No colour-only state | Every chip carries a letter and a glyph; errors carry an icon and words; losses say "loss" or show a minus sign | design rule |
| Single-pointer alternative to swipe | Buttons for every swipe | SC 2.5.7 [V-WF] https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html |
| Labels | Visible `<label>` on every input; `aria-label` on icon-only buttons and on the badge; segmented controls use `role="tablist"` or radio semantics | design rule |
| Live announcements | A polite `aria-live` region announces "New match: Stiffel brass lamp, $62" on a Realtime insert; toasts use `role="status"` | design rule |
| Focus | Visible 2 px ring, 3:1 against its background; sheets trap and restore focus (Radix and vaul do this) **[U: not tested]** | |
| Reduced motion | `prefers-reduced-motion` disables the pulse and turns sheet springs into fades | design rule |
| Inputs ≥ 16 px font | Prevents iOS Safari zooming on focus **[U: widely reported, not read today]** | |
| Zoom | rem-based sizes, no fixed-height text boxes; test at 200% | design rule |

### 2.10 Compliance behaviours the UI must honour (from note 10)

Note 10 (`10-compliance-security-reliability.md`, another session's file, tags its own claims VERIFIED text / INFERRED) turns licence terms into requirements. These are the ones that land in the interface. I relied on its readings; I did not re-read the eBay or Etsy terms.

| Requirement (note 10) | UI behaviour |
|---|---|
| C5, C50: eBay and Etsy listing content at most 6 h stale; older cards hidden or age-stamped | "as of <time>" on every buy card and every channel row; hide or mark "N h older than eBay" past 6 h; the header dot goes amber when the poller lags |
| C8: delete eBay watch hits when the listing ends | An ended candidate disappears (06's `ended` status is a transition, not a resting state) |
| C9: eBay results in their own component, isolated, no cost, margin or other-site columns | Grouped sections; Today and Recent never show watch titles; no margin on buy cards |
| C10, C22: no site-wide statistics from eBay content; no ranking of marketplaces | Sales rollups use only Ricky's own sales; By channel is alphabetical with no "best" label |
| C11: eBay content is never used to model prices or build learned scores | No "typical price" or "good deal" badge on buy cards; the fit reason is a per-listing sentence |
| C12: sourcing alerts end at a human decision | No auto-buy, no auto-offer; Bought is recorded after Ricky buys elsewhere |
| C15, C16: no buyer names, addresses, emails or phones stored; every buyer field may be null | None of those fields appears in any list, card or export |
| C7: public `/privacy` page and the Etsy trademark sentence in the footer | A public route and the About block in Settings and on the login screen |
| C35: email OTP, custom SMTP first, `shouldCreateUser: false`, sign-ups off after the first account | 3.6 |
| C37: fix the production domain before installing the PWA | Manifest `id` and `start_url` on the final domain (3.3) |
| C38: CSP with `script-src 'self'`, `connect-src` limited to the Supabase project | 3.5 notes the interactions with vite-plugin-pwa, sonner and vaul |


---

## 3. Frontend tooling (verified today)

### 3.0 How this was verified

1. Versions: `npm view <pkg> version` against the live registry on 2026-10-26 [V], plus peer and engine fields.
2. Docs: the vendor pages below, fetched with crawl4ai into `research/dashboard/raw/ui-*.md` [V].
3. **A throwaway build** [RUN]: I copied `template-react-ts` out of the `create-vite@9.3.1` tarball (the CLI is interactive; the tarball is exactly what it scaffolds), installed everything in 3.2, ran `shadcn init` and `shadcn add`, wrote a small app using React Router, supabase-js, the PWA virtual module, an SVG sparkline and a Recharts bar chart, and ran `tsc -b && vite build` (exit 0, PWA plugin generated `sw.js` and a manifest). The project lives in the session scratchpad, not in this repo. Nothing ran against a live Supabase project, a real phone, or a deployed host.

### 3.1 Packages, exact versions, sources

| Package | Version (npm `latest`, 2026-10-26) | Why / what to know | Source |
|---|---|---|---|
| `vite` | **8.3.5** | Needs Node `^20.19.0 \|\| >=22.12.0`. [V] | https://vite.dev/guide/ , https://www.npmjs.com/package/vite |
| `@vitejs/plugin-react` | **6.1.2** | Peer `vite ^8.0.0` only. [V npm] | https://www.npmjs.com/package/@vitejs/plugin-react |
| `react`, `react-dom` | **19.3.1** | `@types/react` and `@types/react-dom` 19.3.0 | https://www.npmjs.com/package/react |
| `typescript` | npm `latest` is **7.0.2**, but the template pins **`~6.0.3`** | Keep the template's pin. `tsc -b` passed clean on 6.0.3 with the toolchain below [RUN]. I did **not** test 7.x with this stack. | create-vite 9.3.1 `template-react-ts/package.json` [RUN], https://www.npmjs.com/package/typescript |
| `tailwindcss`, `@tailwindcss/vite` | **4.3.3** | Plugin peer `vite ^5.2 \|\| ^6 \|\| ^7 \|\| ^8`. CSS-first: `@import "tailwindcss";`, no `tailwind.config.js`. shadcn's Tailwind v4 page warns v4 "uses bleeding-edge browser features and is designed for modern browsers". [V] | https://tailwindcss.com/docs/installation/using-vite , https://ui.shadcn.com/docs/tailwind-v4 |
| `shadcn` (CLI, and a runtime dependency) | **4.22.1** | Offers `-t vite`, `-b radix\|base\|aria`, `-p <preset>`, `-y`. The generated CSS does `@import "shadcn/tailwind.css"`, so `shadcn` stays in `dependencies`. [RUN] | https://ui.shadcn.com/docs/installation/vite |
| `vite-plugin-pwa` | **2.0.0** (released 2026-10-03) | v2.0.0's only listed change is allowing `@vite-pwa/assets-generator ^2.0.0` as a peer; Vite 8 peer support arrived in v1.3.0 (May 2026). Depends on `workbox-build` and `workbox-window` 7.4.1. Node `>=20.19.0`. [V] | https://vite-pwa-org.netlify.app/guide/ , https://github.com/vite-pwa/vite-plugin-pwa/releases |
| `@supabase/supabase-js` | **2.118.0** | Node `>=22.0.0`. Realtime and auth ship inside it. [V npm] | https://supabase.com/docs/reference/javascript |
| `react-router` | **8.5.0** | Released June 2026 (8.0.0 on 2026-06-17). Node `>=22.22.0`, React `>=19.2.7`, Vite 7+, ESM only. **`react-router-dom` was removed in v8**; import everything from `react-router`. v7 is the previous major (`7.18.4`). [V] | https://reactrouter.com/changelog |
| `lucide-react` | **1.61.0** | Icons; shadcn's `iconLibrary` | npm |
| `radix-ui` | 1.8.1 | Installed by `shadcn init -b radix` | npm |
| `class-variance-authority` 0.7.1 · `tw-animate-css` 1.4.0 · **`cn` 0.5.0** | | shadcn now writes `export { cn } from "cn"` (maintainer: shadcn, repo `shadcn-ui/cn`), a drop-in for `clsx` plus `tailwind-merge`, so you do not install those two. [RUN] | https://github.com/shadcn-ui/cn |
| `vaul` 1.1.2 | | What `shadcn add drawer` installs for the Radix style. The docs page I fetched describes the **Base UI** drawer (which replaced Vaul there), so docs and the Radix-style output differ (3.9). [RUN] | https://ui.shadcn.com/docs/components/drawer |
| `sonner` 2.0.8 | | Toasts (Undo). `shadcn add sonner` also pulls in `next-themes`; remove it (2.8). [RUN] | https://ui.shadcn.com/docs/components/sonner |
| `@fontsource-variable/geist` 5.3.0 | | Added by the Nova preset: 5 `woff2` files, about 76 kB, all precached. Delete and use the system font stack (4.2). [RUN] | |
| `workbox-window` | 7.4.1 | **Already a dependency of vite-plugin-pwa 2.0.0** (3.9) | npm |
| `recharts` 3.10.1 · `chart.js` 4.6.1 · `uplot` 1.6.32 | | **Not used** (3.8) | npm |
| `@tanstack/react-query` 5.105.0 · `@tanstack/react-router` 1.170.46 | | **Not used** (3.7) | npm |
| `@types/node` | template pins `^24.19.2`; npm `latest` is 26.6.5 | Keep the template's. Needed for the `@` alias in `vite.config.ts`. | |

**Node on the host and in CI: 22.22 or newer (or 24).** The strictest engine field wins: react-router 8.5.0 needs `>=22.22.0`, supabase-js 2.118.0 `>=22.0.0`, Vite 8.3.5 `^20.19.0 || >=22.12.0`. Pin it explicitly in the host's build settings and in `package.json` `engines` **[U: how each host sets it was not read; both Vercel and Cloudflare Pages have a setting for it]**. The machine used for the scratch build is Node 24.19.0.

### 3.2 The install, exactly

```bash
# scaffold = create-vite 9.3.1 react-ts (vite ^8.3.4, react ^19.3.1, plugin-react ^6.1.2, typescript ~6.0.3, oxlint)
npm create vite@latest hv-desk -- --template react-ts
cd hv-desk && npm i

# the npm i line (versions are the ones resolved and built on 2026-10-26)
npm i react-router@8.5.0 @supabase/supabase-js@2.118.0 tailwindcss@4.3.3 @tailwindcss/vite@4.3.3 lucide-react@1.61.0
npm i -D vite-plugin-pwa@2.0.0 @types/node

# shadcn adds radix-ui, class-variance-authority, cn, tw-animate-css, shadcn, @fontsource-variable/geist itself
npx shadcn@latest init -t vite -b radix -p nova -y
npx shadcn@latest add button input drawer switch badge skeleton sonner
```

Notes on that block.
- The installs and `shadcn init` ran as written except unpinned (they resolved to the versions in 3.1) and with `recharts` also installed; the `add` line is a subset of what I ran (I also added `card`, `tabs`, `chart`, which this design does not use). No peer-dependency warnings were printed [RUN].
- `shadcn init` is interactive unless you pass `-p <preset>`; without it the run stalls on a preset menu (Nova, Vega, Maia, Lyra, Mira, Luma, Sera, Rhea, Custom) [RUN].
- The `tsconfig` alias: shadcn's page tells you to add `baseUrl` **and** `paths` to `tsconfig.json` and `tsconfig.app.json`. I added only `paths` (`"@/*": ["./src/*"]`) and `tsc -b` passed with TypeScript 6.0.3 [RUN]. Whether `baseUrl` is deprecated under TS 6 was not read **[U]**.
- `vite.config.ts` needs the `@` alias too: `resolve: { alias: { '@': path.resolve(import.meta.dirname, './src') } }` (shadcn's page uses `__dirname`; `import.meta.dirname` worked under Node 24 [RUN]).
- Add `"vite-plugin-pwa/react"` to `compilerOptions.types` (or a `/// <reference types="vite-plugin-pwa/react" />` line) so `virtual:pwa-register/react` type-checks [V] https://vite-pwa-org.netlify.app/frameworks/react .
- `index.html` needs `viewport-fit=cover` in the viewport meta tag. The template does not have it; after adding it the built `index.html` contained it [RUN].
- The manifest icon files (`pwa-192.png`, `pwa-512.png`) did not exist in the scratch project and **the build still passed**, so a green build does not prove installability. Generate real icons (the docs recommend `@vite-pwa/assets-generator` [V]; it is at 2.0.0 and optional, not run) and run Lighthouse's installability check on the deployed build.

### 3.3 `vite.config.ts` (built and type-checked [RUN])

```ts
import path from 'node:path'
import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
    VitePWA({
      registerType: 'prompt',            // see 3.5: forms are in this app, so no silent reload
      includeAssets: ['favicon.svg', 'apple-touch-icon.png'], // built with favicon.svg only
      manifest: {
        id: '/',
        name: 'Hollywood and Vine Desk',
        short_name: 'H&V Desk',
        description: 'Shop dashboard',
        theme_color: '#130d10',
        background_color: '#130d10',
        display: 'standalone',
        start_url: '/',
        icons: [
          { src: 'pwa-192.png', sizes: '192x192', type: 'image/png' },
          { src: 'pwa-512.png', sizes: '512x512', type: 'image/png' },
          { src: 'pwa-512.png', sizes: '512x512', type: 'image/png', purpose: 'maskable' },
        ],
      },
    }),
  ],
  resolve: { alias: { '@': path.resolve(import.meta.dirname, './src') } },
})
```

Differences from what I built: `id: '/'` (iOS identifies a Home Screen web app by its manifest `id` [V] https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/ ; note 10 C37 says the domain, `id` and `start_url` must be final before anyone installs), the `apple-touch-icon.png` include and the `maskable` entry were added afterwards from vite-pwa's icon guidance, and the icon files do not exist yet; `theme_color` there was `#1a1114`, here it is the dark `--background` token. The manifest keys come from vite-pwa's minimal-requirements page: a name, a short name, a description, a `theme_color` that **must match** the `<meta name="theme-color">`, and 192 and 512 px icons; it suggests separate `any` and `maskable` entries rather than one `any maskable` icon [V] https://vite-pwa-org.netlify.app/guide/pwa-minimal-requirements . Both a Chromium-installability list (name or short_name, 192 and 512 icons, start_url, display, HTTPS) and the iOS notes are in 05 section 5.1.

### 3.4 Router: React Router 8.5.0, declarative mode

- React Router has three modes (declarative, data, framework); features are additive [V] https://reactrouter.com/start/modes . **Declarative** is `<BrowserRouter>`, `<Routes>`, `<Route>`, `<NavLink>`, `useNavigate`, `useLocation`, `useSearchParams`. Install is `npm i react-router`, then render `<BrowserRouter>` (imported from `"react-router"`) around the app [V] https://reactrouter.com/start/declarative/installation .
- Data mode adds `loader`/`action`/`useFetcher`. That is a second data layer fighting Realtime; skip.
- **Why not v7 (the brief's assumption):** v8 is `latest`. It is a "boring" major whose breaking changes were future flags in v7; the visible ones for this app are Node 22.22+, ESM only, and **`react-router-dom` is gone** [V] https://reactrouter.com/changelog (v8.0.0, 2026-06-17). Starting a new app on v7 buys nothing and ties you to a line that will go to maintenance. The next major is planned for around May 2027, aligned to Node 22's end of life [V, same changelog].
- **Why not TanStack Router (1.170.46):** its pitch is 100% inferred types, type-safe navigation and typed search params [V] https://tanstack.com/router/latest/docs/framework/react/overview . Typed search params are attractive for this design (filters live in the URL). But it brings a route-tree generation step and its own concepts, for six routes. If filter state grows into something that really needs types, revisit. Not chosen.
- Host config: a SPA needs a "serve `index.html` for unknown paths" rewrite on the host **[U: not read today for either host]**.

### 3.5 PWA with vite-plugin-pwa 2.0.0

How the service worker gets registered [V] https://vite-pwa-org.netlify.app/guide/register-service-worker : `injectRegister` defaults to `'auto'`. If your code imports **none** of the plugin's virtual modules, the plugin falls back to a generated `registerSW.js` script tag; if you import one (such as `virtual:pwa-register/react`), that import registers the worker for you. We import the React one, so registration happens through the hook.

Update behaviour. `autoUpdate` reloads open tabs when a new version is ready, and the vendor warns "the user can lose data in any browser windows/tabs in which the application is open and is filling in a form ... we recommend you to change the behavior to use default `prompt`", and that changing from `autoUpdate` to `prompt` later "can be a pain" [V] https://vite-pwa-org.netlify.app/guide/auto-update . This app has forms (add item, watch editor), so use `prompt` and a small toast: the React docs' `ReloadPrompt` pattern, reduced to its core and type-checked [RUN]:

```tsx
import { useRegisterSW } from 'virtual:pwa-register/react'

export function ReloadPrompt() {
  const { needRefresh: [needRefresh], updateServiceWorker } = useRegisterSW()
  return needRefresh ? (
    <button className="h-11 ..." onClick={() => updateServiceWorker(true)}>Update ready. Reload</button>
  ) : null
}
```

The hook's options "are not reactive"; pass stable callbacks [V] https://vite-pwa-org.netlify.app/frameworks/react .

Content Security Policy. Note 10 (C38) wants `script-src 'self'`, `connect-src` limited to the Supabase project and `frame-ancestors 'none'`. The `injectRegister: 'inline'` mode would put an inline script in the page and break `script-src 'self'`; the default `auto` with our virtual-module import registers from bundled code instead [V register docs]. Whether sonner and vaul (both inject inline styles) and the image sources (Supabase Storage, Drive thumbnails, eBay image hosts) pass a strict policy was **not tested [U]**; `style-src` and `img-src` will need real values from a browser test.

Build output [RUN]: `mode generateSW`, `precache 6 entries (525.05 KiB)`, files `sw.js`, `workbox-<hash>.js`, `manifest.webmanifest`. That is the offline shell. Data is not cached by the service worker (it comes over Supabase's WebSocket and REST); see 2.7.

iOS caveats (collected; the first column says where each was verified).

| Caveat | Verified in |
|---|---|
| Web Push works only for a Home Screen web app, iOS 16.4+, and the permission prompt must follow a direct user tap | WebKit blog 13878 [V], note 05 |
| App-icon badge needs notification permission | WebKit blog 13878 [V] |
| Declarative Web Push (iOS 18.4+) avoids the "revoked subscription if you do not show a notification" penalty | note 05 section 4a [V] |
| Home Screen app storage is separate from Safari's, so a link opened in Safari has no session | note 05 [V] for the storage counter; the "no session" consequence is my inference **[U]** |
| `apple-touch-icon` takes precedence over manifest icons if both exist; manifest icons supported since iOS 15.4 | note 05 [V] |
| Safe areas need `viewport-fit=cover` plus `env(safe-area-inset-*)` | MDN [V], and built [RUN] |
| No `beforeinstallprompt` on iOS; show "Share, then Add to Home Screen" instructions in Settings and hide them when running standalone | note 05 **[U]** |
| Status-bar style meta tag and splash images on iOS 26 | not read; **[U]**, test on the phone |

### 3.6 Supabase: Realtime and OTP sign-in

**Client** (the docs now show a `sb_publishable_...` key in `createClient`) [V] https://supabase.com/docs/guides/realtime/postgres-changes :

```ts
import { createClient } from '@supabase/supabase-js'
export const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY, // a publishable key, safe in the browser; RLS is the lock
)
```

**Realtime setup SQL** [V, same page]: turn RLS on for the table, then `alter publication supabase_realtime add table your_table_name;` (or toggle the table under Database → Publications). Subscribing: `supabase.channel('name').on('postgres_changes', { event: '*', schema: 'public', table: 't', filter: 'col=eq.x' }, cb).subscribe()`. `event` is `INSERT`, `UPDATE`, `DELETE` or `*`. Several `.on()` calls can share one channel. "RLS policies are not applied to DELETE statements", and filtering DELETE events, or receiving the `old` row on UPDATE/DELETE, needs `replica identity full`. So **soft-delete** (`status = 'archived'`), as 05 already advises.

**The hook that replaces TanStack Query** (type-checks against supabase-js 2.118.0 [RUN]; not run against a live database **[U]**):

```ts
import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'

type Row = { id: string }

export function useLiveTable<T extends Row>(table: string, columns: string, order: string) {
  const [rows, setRows] = useState<T[]>([])
  const [ready, setReady] = useState(false)
  useEffect(() => {
    let alive = true
    const load = async () => {
      const { data } = await supabase.from(table).select(columns).order(order, { ascending: false }).limit(200)
      if (alive && data) { setRows(data as unknown as T[]); setReady(true) }
    }
    const ch = supabase
      .channel(`live-${table}-${crypto.randomUUID()}`)          // unique per mount: two screens can use one table
      .on('postgres_changes', { event: '*', schema: 'public', table }, (p) => {
        setRows((cur) => {
          if (p.eventType === 'DELETE') return cur.filter((r) => r.id !== (p.old as Row).id)
          const row = p.new as T
          return [row, ...cur.filter((r) => r.id !== row.id)]
        })
      })
      .subscribe((status) => { if (status === 'SUBSCRIBED') void load() })   // first connect AND every reconnect
    return () => { alive = false; void supabase.removeChannel(ch) }
  }, [table, columns, order])
  return { rows, ready }
}
```

Call it per table with explicit columns and the right sort column, for example `useLiveTable<Candidate>('candidates', 'id,title,price,found_at,last_seen_at,end_at,status', 'found_at')` and `useLiveTable<Sale>('sales', 'id,item_id,channel,sold_at,item_price,fees_total,fee_source,net_proceeds', 'sold_at')`. Never `select('*')`: 06's `raw` jsonb holds the full marketplace object, which should not ride along on every load (the Realtime payload still carries the whole row, so keep `raw` out of heavily-written subscribed tables if payloads grow).

Known ceilings (add when they bite): money columns are `numeric` and arrive as JSON numbers, so do sums in SQL views (06), not here; 200-row cap with no pagination; new rows are placed on top regardless of `order`; no localStorage snapshot (4 lines, 2.7); no generated types (`supabase gen types`). The unique channel name avoids a collision when Today and Alerts both watch `candidates`; every channel rides the client's single WebSocket **[U: realtime-js behaviour from memory]**.

**Email OTP sign-in** [V] https://supabase.com/docs/guides/auth/auth-email-passwordless . Email OTP is enabled by default and shares its implementation with Magic Links: edit the **Magic Link** email template to include `{{ .Token }}`, for example `<p>Please enter this code: {{ .Token }}</p>`. By default a user can request an OTP once every 60 seconds and it expires after 1 hour (configurable under Authentication → Sign In / Providers → Email). Compiled [RUN]:

```ts
// step 1: send the 6-digit code (shouldCreateUser:false = nobody new can sign up)
await supabase.auth.signInWithOtp({ email, options: { shouldCreateUser: false } })
// step 2: verify the code the user types; returns { data: { session }, error }
await supabase.auth.verifyOtp({ email, token: '123456', type: 'email' })
```

Create Ricky's user first (dashboard invite or one initial sign-in with `shouldCreateUser` left at its default) and then ship with `shouldCreateUser: false` **[U: the exact dashboard path was not read]**. Supabase's built-in mailer is limited to 2 emails per hour, so custom SMTP is a prerequisite (05 section 1.6 [V]). Install to the Home Screen first and sign in inside the installed app, so the session lives in the right storage **[U]**. Note 10 (C35) adds: custom SMTP configured before the first login test, sign-ups turned off once Ricky's account exists, a 10-minute OTP lifetime (the docs default is 1 hour, configurable), and MFA on the Supabase account itself.

### 3.7 TanStack Query: not needed

TanStack Query is "the missing data-fetching library": caching, request dedupe, background refetch, structural sharing [V] https://tanstack.com/query/latest/docs/framework/react/overview . This app is one user, six small lists (hundreds of rows), pushed updates, and single-row mutations. Realtime already delivers freshness; the hook above does the initial load and the reconnect refetch; optimistic updates are a local `setRows`. Adding it means a second cache that has to be kept consistent with the Realtime stream (invalidate on every event), which is more code than the hook. **Ceiling:** if several screens start sharing derived queries (monthly P&L cached per month, per-item aggregates), add it then. Aggregates (Sales) are one RPC per selected month, fetched in a plain effect.

### 3.8 Charts: inline SVG and CSS, no library

Measured, same app, same build [RUN]:

| Build | JS (minified) | JS gzip | CSS gzip |
|---|---|---|---|
| Baseline: React, React Router, supabase-js, `workbox-window`, SVG `Spark` and flex-div `Bars` | 475.8 kB | **138.0 kB** | 9.3 kB |
| + one Recharts `BarChart` through shadcn's `ChartContainer` | 807.0 kB | **241.5 kB** | 9.5 kB |

One bar chart costs **+103.6 kB gzip**, three quarters of the whole baseline. The design needs a handful of sparklines (an SVG `<polyline>`, 6 lines) and one bar chart of at most 24 bars (flex divs, 8 lines). Both components compiled in the scratch app and live in this note's recommendation. `shadcn add chart` is a Recharts wrapper ("We use Recharts under the hood", chart now on Recharts v3 [V] https://ui.shadcn.com/docs/components/chart ), so skipping Recharts means skipping that component too. I did not measure `uplot` (1.6.32, last published 2025-03) or `chart.js` (4.6.1); neither is needed for this. If axes, tooltips and zoom are ever wanted, measure uPlot first; Recharts is the heaviest realistic choice.

```tsx
export function Spark({ values, w = 96, h = 28 }: { values: number[]; w?: number; h?: number }) {
  const max = Math.max(...values, 1)
  const pts = values.map((v, i) => `${(i / (values.length - 1)) * w},${h - (v / max) * (h - 2) - 1}`).join(' ')
  return <svg viewBox={`0 0 ${w} ${h}`} width={w} height={h} role="img" aria-label="trend">
    <polyline points={pts} fill="none" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" />
  </svg>
}
```

### 3.9 Which shadcn pieces to add, and what to fix after

Add: `button`, `input`, `drawer`, `switch`, `badge`, `skeleton`, `sonner`. Skip: `chart` (Recharts), `card` (a bordered div does it), `tabs` and `select` (a segmented control and native `<select>` are better on a phone), `table` (use list rows on the phone and a real `<table>` at `lg`).

After generating, edit (all built and type-checked [RUN]):
1. `index.css`: dark mode to a media query (2.8); delete the `@fontsource-variable/geist` import and use the system stack (4.2).
2. `sonner.tsx`: remove the `next-themes` import and `useTheme`, pass `theme="system"`.
3. `button.tsx`: raise the sizes to 44 px (4.5).
4. `package.json`: remove `next-themes` and `@fontsource-variable/geist`.
5. `drawer.tsx` starts with a `"use client"` directive (a Next.js marker; harmless in Vite).

### 3.10 Web Push later (the hook point, not built)

Switch the plugin to `strategies: 'injectManifest'` with `srcDir: 'src'` and `filename: 'sw.ts'`; the custom worker must call `precacheAndRoute(self.__WB_MANIFEST)` [V] https://vite-pwa-org.netlify.app/guide/inject-manifest . In `sw.ts` add `push` and `notificationclick` handlers (both are service-worker events [V] https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/push_event ). Subscribe from a **button tap** (iOS requires a user gesture, 3.5): `registration.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey })`, store the subscription in a `push_subscriptions` table. Every `push` must end in `showNotification` or iOS revokes the subscription; Declarative Web Push (iOS 18.4+) avoids that trap (note 05 4a). The same phase turns on `setAppBadge`. A sketch, **not compiled [U]**:

```ts
/// <reference lib="webworker" />
import { cleanupOutdatedCaches, precacheAndRoute } from 'workbox-precaching'
declare const self: ServiceWorkerGlobalScope
cleanupOutdatedCaches(); precacheAndRoute(self.__WB_MANIFEST)
self.addEventListener('push', (e) => {
  const d = e.data?.json() ?? {}
  e.waitUntil(self.registration.showNotification(d.title ?? 'Hollywood & Vine', { body: d.body, data: { url: d.url } }))
})
self.addEventListener('notificationclick', (e) => {
  e.notification.close()
  e.waitUntil(self.clients.openWindow(e.notification.data?.url ?? '/'))
})
```

### 3.11 Discrepancies (X verified, Y need review)

- **Router:** the brief says "react-router v7 vs TanStack Router". React Router 8.5.0 is `latest` (v7.18.4 is the `version-7` tag). X verified (changelog, npm); Y: no benchmark of v7 vs v8 for a declarative app was needed.
- **TypeScript:** npm `latest` is 7.0.2; `create-vite` 9.3.1's template pins `~6.0.3`. X verified: the build is clean on 6.0.3. Y need review: TS 7 with this toolchain (untested).
- **shadcn tsconfig step:** the docs add `baseUrl` and `paths`; only `paths` was needed [RUN]. Y: baseUrl deprecation status under TS 6 unread.
- **`workbox-window`:** the vite-pwa React page says to add it as a dev dependency; vite-plugin-pwa 2.0.0 already lists it as a dependency and `virtual:pwa-register/react` built without installing it separately [RUN]. Y: the docs sentence is probably stale; either way installing it explicitly is harmless.
- **Node floor:** the vite-pwa Getting Started page (last updated 2025-11-27) says "Vite requires Node.js version 18.x.x or 20+"; vite.dev says 20.19+ or 22.12+; React Router 8.5.0 needs 22.22+. X verified, all three read; use the strictest.
- **shadcn drawer:** the live docs page documents the Base UI drawer ("now uses Base UI instead of Vaul"); `shadcn add drawer` with `-b radix` generated a `vaul` drawer [RUN]. X verified both; Y: which base to standardise on is a taste call, Radix chosen because that is what ran.
- **Vendoo mobile:** the marketing page lists "sale detection" among the mobile app's features today; the help article quoted in note 03 lists "Sale Detection and Auto Delist" as *not yet available* on mobile. X verified: both pages exist; Y need review: which is current (the help article may be stale, or detection may run server-side).
- **Apple HIG:** tab-bar guidance came from a search summary of Apple's page and a mirror, not the page itself (JavaScript-rendered). Y need review before citing it as Apple's words.
- **UI assumptions vs note 06's tested DDL** (section 1.4 has the full mapping): X verified, 06's tables cover most screens. Y need review: no `fit_reason` / `starred` / `dismiss_reason` on `candidates`, no plain-language `description` or `alert_mode` on `watches`, `cost_purchase` cannot say "unknown", `items.sku` is mandatory, `alerts` has `acked_at` not `read_at`.
- **Money units:** note 06 stores `numeric(12,2)` dollars; note 10 C44 says "stores money as integer minor units". Not mine to settle; the UI formats whichever wins with `Intl.NumberFormat`.
- **Contrast and size figures** are WCAG as summarised by WebFetch ([V-WF]); the normative sentences quoted match what I know of WCAG 2.2, but they were not read as raw text.


---

## 4. Design-token sheet

Everything here maps onto the variable names shadcn already generates (`--background`, `--card`, `--primary`, `--border`, `--ring`, ...), so the generated components pick it up with no per-component edits, plus five semantic additions (`--surface-2`, `--control-border`, `--signal`, `--money`, `--good/--bad/--warn/--info`).

Where the palette comes from. The storefront CSS (`site/storefront.css`, read only) defines burgundy `#451c2b`, deep burgundy `#321520`, cream `#f6efdf`, a pastel pink `#e5a6b4`, rust `#b75834`, and a dark paper `#2c2024` [V, local file]. It has **no gold and no neon variable**; those two come from the room itself (pink neon sign, lamps), so the neon-pink and gold hex values below are **my choices, not a brand spec** (open question 6). The dashboard's burgundy is lighter than the storefront's so it holds as a button fill with white text; the storefront burgundy `#451c2b` is kept for the wordmark.

### 4.1 Colour tokens, light and dark, with contrast computed

Hex on purpose: the ratios below were computed on exactly these values with the WCAG relative-luminance formula in a 30-line Node script in the session scratchpad [RUN]. Thresholds: 4.5:1 for text (SC 1.4.3), 3:1 for UI components and focus (SC 1.4.11) [V-WF].

| Token | Role | Light | Dark |
|---|---|---|---|
| `--background` | page | `#faf7f2` | `#130d10` |
| `--card` / `--popover` | surface (cards, sheets) | `#ffffff` | `#1d1417` |
| `--surface-2` (`--muted`, `--secondary`, `--accent`) | chips, segmented bg, hover | `#f1ebe3` | `#271b20` |
| `--foreground` | text | `#231a1d` | `#f3eadf` |
| `--muted-foreground` | secondary text | `#6a5c60` | `#b3a39f` |
| `--border` | decorative hairline (cards, dividers) | `#d9cfc5` | `#4a3a40` |
| `--input` / `--control-border` | borders of inputs, switches, outlined buttons | `#857579` | `#8f7e84` |
| `--primary` (= brand) | primary buttons, active tab | `#6b2540` | `#e58fb0` |
| `--primary-foreground` | text on primary | `#ffffff` | `#1a0d13` |
| `--ring` / `--signal` | focus ring, unread badge, Live dot, NEW tag | `#b8135f` | `#ff5fae` |
| `--money` | sold tag, positive profit | `#7f6200` | `#e0b84a` |
| `--good` | listed live, ok | `#17693a` | `#58c98a` |
| `--bad` / `--destructive` | still live elsewhere, loss, error | `#b3261e` | `#ff7b72` |
| `--warn` | stale, reconnecting, aging | `#8a4b00` | `#f0a050` |
| `--info` | neutral notices | `#2b5f8a` | `#7fb8ea` |

Computed contrast (all pass their threshold except the one row marked decorative):

| Pair | Light | Dark | Needs |
|---|---|---|---|
| foreground on background / on card | 15.89 / 16.98 | 16.15 / 15.15 | 4.5 |
| muted-foreground on background / card / surface-2 | 5.93 / 6.34 / 5.35 | 7.92 / 7.43 / 6.85 | 4.5 |
| primary-foreground on primary | 10.69 | 8.00 | 4.5 |
| primary as text on background | 10.01 | 8.13 | 4.5 |
| signal on background / card | 5.96 / 6.37 | 6.86 / 6.44 | 4.5 |
| money on background / card | 5.38 / 5.75 | 10.18 / 9.55 | 4.5 |
| good / bad / warn / info on card | 6.73 / 6.54 / 6.80 / 6.76 | 8.70 / 7.15 / 8.46 / 8.54 | 4.5 |
| Chip text on a 14% tint of its own colour over card: signal / money / good / bad / warn / info / brand | 5.01 / 4.73 / 5.46 / 5.19 / 5.51 / 5.51 / 8.29 | 5.24 / 7.26 / 6.83 / 5.73 / 6.53 / 6.63 / 6.03 | 4.5 |
| control-border on card / background | 4.36 / 4.08 | 4.71 / 5.02 | 3.0 |
| border on background / card (decorative only) | 1.44 / 1.53 | 1.80 / 1.69 | not required; never the only boundary of a control |

Wiring (the dark mode change is the one that matters; this form built and emitted the media blocks [RUN]):

```css
@import "tailwindcss";
@import "tw-animate-css";
@import "shadcn/tailwind.css";
@custom-variant dark (@media (prefers-color-scheme: dark));   /* shadcn wrote (&:is(.dark *)) */

:root {
  color-scheme: light dark;
  --background: #faf7f2;  --foreground: #231a1d;
  --card: #ffffff;        --card-foreground: #231a1d;
  --popover: #ffffff;     --popover-foreground: #231a1d;
  --muted: #f1ebe3;       --muted-foreground: #6a5c60;
  --secondary: #f1ebe3;   --secondary-foreground: #231a1d;
  --accent: #f1ebe3;      --accent-foreground: #231a1d;
  --border: #d9cfc5;      --input: #857579;     --control-border: #857579;
  --primary: #6b2540;     --primary-foreground: #ffffff;
  --ring: #b8135f;        --signal: #b8135f;     --money: #7f6200;
  --good: #17693a;        --destructive: #b3261e; --warn: #8a4b00; --info: #2b5f8a;
  --radius: 0.625rem;
}
@media (prefers-color-scheme: dark) {
  :root {
    --background: #130d10;  --foreground: #f3eadf;
    --card: #1d1417;        --card-foreground: #f3eadf;
    --popover: #1d1417;     --popover-foreground: #f3eadf;
    --muted: #271b20;       --muted-foreground: #b3a39f;
    --secondary: #271b20;   --secondary-foreground: #f3eadf;
    --accent: #271b20;      --accent-foreground: #f3eadf;
    --border: #4a3a40;      --input: #8f7e84;     --control-border: #8f7e84;
    --primary: #e58fb0;     --primary-foreground: #1a0d13;
    --ring: #ff5fae;        --signal: #ff5fae;     --money: #e0b84a;
    --good: #58c98a;        --destructive: #ff7b72; --warn: #f0a050; --info: #7fb8ea;
  }
}
@theme inline {
  /* shadcn's generated --color-* mappings stay; add the five new ones */
  --color-signal: var(--signal);  --color-money: var(--money);  --color-control-border: var(--control-border);
  --color-good: var(--good);      --color-warn: var(--warn);  --color-info: var(--info);
  --font-sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
```

Because `@theme inline` reads the variables at runtime, the `@media` override recolours every `bg-card`, `text-muted-foreground` and `border-border` utility with no `dark:` classes.

### 4.2 Type scale

Font: the **system stack** (zero font bytes; delete the Geist import the Nova preset adds, which is about 76 kB of precache). Numbers use `tabular-nums` (Tailwind's utility built in the scratch app [RUN]) and right-align in lists. The storefront's display face (Bodoni Moda) belongs to the wordmark only: export the wordmark once as an SVG so the dashboard ships no font for it.

| Token | Size / line-height | Weight | Used for |
|---|---|---|---|
| `caption` | 12 / 16 px | 500 | chip text, timestamps, tab labels (nothing below 12 px) |
| `body-sm` | 14 / 20 | 400 | meta lines, secondary row text |
| `body` | 16 / 24 | 400 | default text; **all inputs** (16 px stops iOS zooming on focus **[U]**) |
| `label` | 14 / 20 | 600 | field labels, button text |
| `title` | 18 / 24 | 600 | card titles, sheet titles |
| `h2` | 22 / 28 | 650 | screen titles |
| `kpi` | 32 / 36 | 700, tabular | Revenue, Fees, Cost, Profit |
| `hero` | 44 / 48 | 700, tabular | "Sold today" |

At `lg`: `kpi` 36 / 40, `hero` 56 / 60, dense table rows drop to `body-sm`. Letter-spacing 0 everywhere except `hero` at −0.01em. Define sizes in `rem` so browser text-size settings work.

### 4.3 Spacing

Tailwind's 4 px grid, restricted to 4 · 8 · 12 · 16 · 24 · 32 · 48.

| Use | Value |
|---|---|
| Page gutter | 16 px (`md` 24, `lg` 32) |
| Card padding | 16 |
| Gap between cards / sections | 12 / 24 |
| List row | min-height 64, thumbnail 48 × 48 with radius 8, 12 px vertical padding |
| Gap between adjacent tap targets | at least 8 |
| Tab bar | 56 + safe-area-inset-bottom |
| Header | 56 + safe-area-inset-top |

### 4.4 Radius and elevation

Keep shadcn's derived radius scale from `--radius: 0.625rem` (10 px): `rounded-sm` 6 (chips, tags), `rounded-md` 8 (thumbnails), `rounded-lg` 10 (inputs, buttons), `rounded-xl` 14 (cards), `rounded-2xl` 18 (sheet top corners), `rounded-full` (badge, avatar, segmented pills). The multipliers (`0.6, 0.8, 1, 1.4, 1.8`) are what `shadcn init` wrote into the CSS [RUN].

Elevation is mostly **borders and surface steps, not shadows** (shadows disappear on near-black):

| Level | Use | Treatment |
|---|---|---|
| 0 | page | `--background` |
| 1 | cards, rows | `--card` + 1 px `--border`; no shadow |
| 2 | header, tab bar | solid `--card` + 1 px border on the edge touching content; **no translucency or blur** (keeps contrast predictable) |
| 3 | sheets, popovers, toasts | `--card` (dark: `--surface-2`) + 1 px border + `0 -8px 32px rgb(0 0 0 / 0.28)`; scrim `rgb(0 0 0 / 0.5)` |

Layering: header 10 · tab bar 20 · FAB 30 · scrim 40 · sheet 50 · toast 60.

### 4.5 Touch-target sizes (the shadcn override)

The generated Nova `button.tsx` sizes are `default h-8`, `xs h-6`, `sm h-7`, `lg h-9`, `icon size-8` [RUN, read from the file]. All below 44 px. Replace with:

| Size | Phone | `pointer-fine` (desktop mouse) |
|---|---|---|
| `default` | `h-11` (44) | `pointer-fine:h-9` |
| `lg` (primary action in a sheet) | `h-12` (48) | `pointer-fine:h-10` |
| `icon` | `size-11` | `pointer-fine:size-9` |
| `sm`, `xs` | delete | delete |

Inputs and selects: `h-11 text-base`. Switch: wrap in a label whose hit area is 44 px even though the track is smaller. Where a visual element must stay small (a chip, the 8 px unread dot), extend the hit area with padding or a `before:` pseudo-element with `-inset-2`, and make sure no two hit areas overlap. `pointer-coarse:` and `pointer-fine:` variants build in Tailwind 4.3.3 (it emitted `@media (pointer:coarse){...}`) [RUN].

### 4.6 Safe-area and `dvh` rules

1. **Viewport meta**: `width=device-width, initial-scale=1.0, viewport-fit=cover` (the template's tag lacks `viewport-fit=cover`; present in the built page after the edit [RUN]). MDN: with `viewport-fit=cover` it is "highly recommended to use the safe area inset variables" (05 section 5.1, MDN [V]).
2. **Height: `dvh`, never `vh`/`h-screen`** (house rule 5). MDN: "all default viewport units (`vh`, `vw`, etc.) are equivalent to their large viewport counterparts", so `100vh` runs behind a retractable browser bar; `svh`, `lvh` and `dvh` are the small, large and dynamic versions [V] https://developer.mozilla.org/en-US/docs/Web/CSS/length . Tailwind 4.3.3's `h-dvh` emitted `100dvh` [RUN]. Shell: `h-dvh flex flex-col`; the only scroller is `min-h-0 flex-1 overflow-y-auto overscroll-y-contain`. Full-page screens (login, install help): `min-h-dvh`. Sheets: `max-h-[85dvh]`.
3. **Insets**: header `pt-[env(safe-area-inset-top)]`; tab bar `pb-[env(safe-area-inset-bottom)]` and height `calc(3.5rem + env(safe-area-inset-bottom))`; sheet footers `pb-[max(1rem,env(safe-area-inset-bottom))]`; shell `pl-[env(safe-area-inset-left)] pr-[env(safe-area-inset-right)]` for landscape on notched phones. `pb-[env(safe-area-inset-bottom)]` built and emitted verbatim [RUN]; on desktop the values are 0 [V] https://developer.mozilla.org/en-US/docs/Web/CSS/env .
4. **Floating button (Add)**: `bottom-[calc(3.5rem+env(safe-area-inset-bottom)+1rem)] right-4`.
5. **Sticky filter chips** sit at `top-0` inside the scroller, not `position: fixed`.
6. **On-screen keyboard** on iOS overlays the page and `dvh` does not shrink for it **[U]**: in sheets with inputs, scroll the focused field into view and keep the primary button reachable; verify on the phone.
7. **iOS status-bar style** (`apple-mobile-web-app-status-bar-style`) and how iOS 26 draws a standalone app under `viewport-fit=cover`: **[U]**, test on the device.

### 4.7 Motion

Press feedback 120 ms; sheet enter/exit and swipe release 200 ms; easing `cubic-bezier(0.2, 0, 0, 1)`; all of it 0 ms (or a plain fade) under `prefers-reduced-motion: reduce`. The only attention animation in the product is one pulse on the Alerts badge when a new alert arrives.

---

## Recommendation

1. **Build five tabs plus Item detail**, as wireframed. Cut order if time is short: keep Alerts, Inventory + Add + Bought, Today; Sales and the Watch editor can follow (seed watches in SQL at first).
2. **Stack:** `npm create vite@latest -- --template react-ts`, then the line in 3.2. Declarative React Router 8.5.0, no TanStack Query, no chart library, seven shadcn components, system font, Tailwind CSS-first config.
3. **Three edits to what `shadcn init` generates** are not optional: dark mode to `prefers-color-scheme` (2.8, 4.1), button and input sizes to 44 px (4.5), and delete `next-themes` and Geist (3.9).
4. **`registerType: 'prompt'`** from day one (the vendor says switching later is painful), `viewport-fit=cover` in the template, real icons before the first deploy.
5. **Make the double-sale check the first feature on Today**, and make "Bought" create the inventory item with its cost. Those two behaviours are what the commercial tools lack.
6. **Before writing real screens, spend one session on the real phone** answering what this note could not: does a Pushover link open Safari or the app; does the 6-digit OTP login work inside the installed app; how does iOS 26 draw the status bar and safe areas for this build; does a strict CSP break the sheets and toasts.
7. **Apply note 10's display rules from the first card**: "as of" stamps, no snapshot of eBay or Etsy content, grouped sections. They are cheap now and expensive to retrofit.

## Open questions

1. **iPhone or Android?** Unconfirmed (05 inferred iPhone from file names). Decides the install instructions, the status-bar and keyboard tests, and how much the badge and push caveats matter.
2. **Which sync tool does he buy (03)?** The "still live elsewhere" row reads `listings.status`; whether that is fed by platform webhooks or by the tool's own state is open. Vendoo's Shopify delist coverage is the specific hole.
3. **Does he log purchases where there is no signal** (estate sales)? If yes, add the Add-item-only outbox (2.7); if no, skip it.
4. **Time zone and week start** for Today/Week/Month. Store UTC, display in the browser's zone; confirm Florida and Monday.
5. **Estimated fees on screen.** Note 06 stores `fee_source` (`api` / `estimated` / `manual`). The UI marks estimates with `~`. Confirm that is acceptable, or say if estimates should be hidden until the platform reports the real number.
6. **Palette sign-off.** Neon pink `#b8135f` / `#ff5fae` and gold `#7f6200` / `#e0b84a` are my picks, and the PWA splash is dark (`#130d10`) in both OS themes.
7. **Is the "Not this" reason chip worth the extra tap?** Note 04 uses the reasons to tune each watch; the UI makes it optional. Ricky decides whether he will actually tap them.
8. **"Test this watch"** runs one search on demand and spends eBay API quota (note 04's budget). Fine at a handful of tests a day; confirm.
9. **One user forever?** A second login (a helper at the shop) changes RLS (05) and Settings.
10. **"Unknown cost" vs "free".** 06 cannot tell them apart (`cost_purchase` defaults to 0). Add a nullable cost or a "Free" confirmation? It affects every profit asterisk.
11. **Schema gaps the UI needs** (1.4): `candidates.fit_reason`, `fit_score`, `starred`, `dismiss_reason`; `watches.description`, `alert_mode`; an auto-generated `items.sku`. Who adds them?
12. **Wordmark:** is the dashboard titled "Hollywood & Vine" or something shorter on the Home Screen (`short_name` is "H&V Desk" here)?

13. **`seen_at` vs `acked_at`.** Add a UI-owned `seen_at` to `alerts`, or let an in-app view write `acked_at` and accept that opening the app also acknowledges? The second can silently stop an escalation (1.4).
14. **Minor units or dollars?** Notes 06 and 10 disagree (3.11).
15. **CSP.** `script-src 'self'` is compatible with the PWA setup; inline styles from sonner and vaul and the image hosts need a browser test (3.5).

## Raw pages fetched (`research/dashboard/raw/`, 47 files)

Frontend tooling: `ui-vite-guide`, `ui-tailwind-vite`, `ui-shadcn-vite`, `ui-shadcn-tailwind4`, `ui-shadcn-chart`, `ui-shadcn-drawer`, `ui-shadcn-sheet`, `ui-shadcn-sonner`, `ui-vitepwa-guide`, `ui-vitepwa-react`, `ui-vitepwa-register`, `ui-vitepwa-minreq`, `ui-vitepwa-injectmanifest`, `ui-vitepwa-autoupdate`, `ui-vitepwa-prompt`, `ui-vitepwa-releases`, `ui-supabase-pgchanges`, `ui-supabase-otp`, `ui-supabase-js-subscribe`, `ui-rr-modes`, `ui-rr-declarative-install`, `ui-rr-changelog`, `ui-tanstack-router-overview`, `ui-tanstack-query-overview`.
Platform references: `ui-webkit-webpush`, `ui-mdn-push-event`, `ui-mdn-badging`, `ui-mdn-env`, `ui-mdn-length-dvh`, `ui-mdn-overscroll`, `ui-mdn-theme-color`.
Competitor UI: `ui-vendoo-mobile`, `ui-vendoo-inventory-tools`, `ui-vendoo-analytics`, `ui-vendoo-appstore-reviews`, `ui-flippd-features`, `ui-flippd-app`, `ui-flippd-appstore`, `ui-flipwise-home`, `ui-crosslist-features-mobile`, `ui-crosslist-docs-mobile` (a docs sidebar page; little UI content), `ui-crosslist-sales-tracking`, `ui-shopify-mobile`, `ui-shopify-app-help`, `ui-shopify-using-app`, `ui-shopify-widgets`, `ui-margeo-profit-trackers` (read; not cited).
Not saved as raw files: the W3C WCAG 2.2 pages (2.5.5, 2.5.8, 2.5.7, 1.4.3, 1.4.11; read through WebFetch because the W3C site returned a bot-wall stub to crawl4ai) and the Apple HIG tab-bar search (WebSearch).
Not reproducible from this repo: the throwaway scratch build and the contrast script live in the session scratchpad and were not committed.

Cross-read for consistency (other sessions' files, not edited): notes 06 (data model), 09 (contract sheet) and 10 (compliance). Section 1.4 maps the UI onto 06; section 2.10 and 3.5 use 10; 09 confirmed the Pushover field limits.
