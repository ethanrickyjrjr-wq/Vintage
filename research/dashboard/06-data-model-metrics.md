# Hollywood and Vine dashboard: data model, metrics, fees, tax

Date: 2026-10-26. Research note 06. Research only: nothing built, nothing committed, `site/` untouched.
Reads with: `01-ebay-platform.md`, `02-etsy-shopify.md`, `03-existing-tools.md`, `05-architecture-hosting-push.md` (raw pages in `research/dashboard/raw/`).

Tags on every claim:
- **VERIFIED** = read today (2026-10-26) on the cited live page or vendor spec. Raw copy is in `research/dashboard/raw/data-*` unless the source says otherwise.
- **V-secondary** = read today, but on a third-party page. Treat as a pointer, not a source.
- **UNVERIFIED** = memory, inference, or a page I could not read. A hypothesis.
- **TESTED** = I ran it: the DDL, the fee function and every metric query below were executed in PGlite 0.5.12 (Postgres 18.6 compiled to WASM) against seed data modeled on `research/inventory/2026-10-26-catalog.md`. The scratch harness lives outside the repo.

---

## 0. Read this first

1. **Nine tables, not eight.** The brief's list minus `heartbeats` (it is a column on `integrations`) plus two the numbers cannot do without: `events` (webhook inbox, raw payloads, idempotency key) and `expenses` (costs that belong to no single sale: Etsy listing fees, Crosslist, boxes, mileage). Without `expenses` the monthly P&L overstates profit.
2. **eBay's fee base includes sales tax, and I can prove it to the cent.** My `est_fees()` function reproduces all four worked examples on eBay's Seller Center fee page ($29.03, $12.04, $21.60, $73.89). The same page says the fee is "calculated based on the total amount of the sale, including the cost of the item and shipping, sales tax". The Fulfillment API's own field text says "item cost + shipping cost". The API text is incomplete; use `totalFeeBasisAmount` as the source of truth when it is present (section 5).
3. **Fee rate is a property of the listing, not of the item category.** Ricky's seven magazine issues (five Playboy, one Penthouse, Southern Peach) and the Chanel book fall under eBay "Books & Magazines" (15.3%, not 13.6%). The chunky gold chains fall under "Jewelry" (15%). So `channel_listings.fee_rule` exists and section 3 carries a catalog-id to rule map.
4. **Real fees need three different API shapes.** eBay: per-order net in `GET /sell/finances/v1/order_earnings`. Etsy: `Payment.amount_fees` is only the card-processing fee; the 6.5% transaction fee, listing fees and offsite ads live in ledger entries. Shopify: `OrderTransaction.fees[]`. Section 1.4.
5. **Only the Shopify own-site sales are Ricky's sales-tax liability.** Etsy (Florida since 2021-07-01) and eBay collect and remit on their own sales. Florida surtax applies to the first $5,000 of an item and is set by the delivery county. This is why `sales` has `tax_collected_by`, `tax_breakdown` and `ship_to_county`.
6. **1099-K is $20,000 AND more than 200 transactions, per platform.** At 30 to 60 listings Ricky is nowhere near it, but IRS says income is reportable whether or not a 1099-K arrives. So the books must be complete regardless. Query `m10b` watches it.
7. **What the three competitors publish.** Of the sell-through definitions I read, only My Reseller Genie documents one (items sold in a month divided by items purchased in the month). None of the pages I read define aging buckets or a stock-value metric. Those are where the dashboard can beat them.
8. **Deviations from the brief, deliberate:** (a) nine tables instead of eight (item 1); (b) `fee_rule` on `channel_listings` so the fee follows the listing (item 3); (c) buyer PII is stripped from raw payloads before they are stored. Raw payloads are still kept, indefinitely, but redacted (section 1.5 rule 5), so "keep raw so nothing is lost" holds for everything except buyer names, addresses, emails and phones.

---

## 1. Schema

### 1.1 Tables (9)

| Table | One line | Written by |
|---|---|---|
| `items` | One row per one-of-a-kind piece: SKU, cost basis, source, acquired date, category, brand, photos. | Ricky (PWA) |
| `channel_listings` | Where an item is or was for sale: channel, external id, url, price, status, `fee_rule`. | Listing sync (service role) |
| `sales` | One row per **order line**: money in, fees, label cost, tax, refunds, net. Generated `fees_total`, `net_proceeds`. | Webhook processor and reconcile poll |
| `expenses` | Costs not tied to one sale: listing fees, ads, subscriptions, supplies, mileage. | Ricky + ledger imports |
| `events` | Append-only webhook inbox. The unique key is the dedupe. Holds PII-redacted raw payloads, kept indefinitely. | Receiver Edge Function |
| `watches` | Saved eBay searches: keywords, exclusions, category, price band, cadence. | Ricky |
| `candidates` | Listings found by a watch: status new/seen/dismissed/bought/ended. | Poller |
| `alerts` | Things to push: sold, buy match, stale, integration down. `delivered_at` vs `acked_at`. | Triggers, cron, poller |
| `integrations` | One row per channel plus `pushover` and `fedora` (home runner). Cursors, token pointer, last ok, heartbeat. | Edge Functions |

Not built on purpose: a `customers` table (buyer PII is a liability, section 1.5), a `payouts` table (reconcile against the bank, not here), a price-history table, `shop_id` columns (single user; widen `is_owner()` later, section 1.6), a `fees` table (four numeric columns on `sales` are enough).

### 1.2 DDL (TESTED)

Run as a Supabase migration. Postgres 15+ is required for `security_invoker` views (Supabase RLS docs, VERIFIED: "In Postgres 15 and above, make a view obey the RLS policies of its underlying tables ... by setting `security_invoker = true`", `data-supabase-rls.md`). Which major version a new Supabase project gets today: UNVERIFIED, check the dashboard.

```sql
-- ===== helpers =====
create function public.shop_tz() returns text language sql immutable as $$ select 'America/New_York' $$;
create function public.local_today() returns date language sql stable
  as $$ select (now() at time zone 'America/New_York')::date $$;

create function public.set_updated_at() returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;

-- Single-user gate. app_metadata is writable only by the service role / dashboard, never by the user
-- (Supabase RLS docs: raw_app_meta_data "cannot be updated by the user").
-- Set once:  update auth.users set raw_app_meta_data = raw_app_meta_data || '{"shop_role":"owner"}' where email = '...';
create function public.is_owner() returns boolean language sql stable set search_path = ''
  as $$ select coalesce((select auth.jwt() -> 'app_metadata' ->> 'shop_role') = 'owner', false) $$;

-- ===== items: one row per one-of-a-kind piece =====
create table public.items (
  id            uuid primary key default gen_random_uuid(),
  sku           text not null unique,            -- master SKU; put the SAME string on every channel listing
  title         text not null,
  brand         text,
  category      text not null check (category in ('fashion','art','lamp','decor','print','furniture','rug','other')),
  subcategory   text,
  condition     text,
  era           text,
  tags          text[] not null default '{}',
  source        text,                            -- 'estate sale','thrift','auction','ebay',... (ROI by source)
  source_detail text,
  source_url    text,
  acquired_on   date,
  cost_purchase numeric(12,2) not null default 0 check (cost_purchase >= 0),
  cost_other    numeric(12,2) not null default 0 check (cost_other >= 0),   -- freight-in, repair, frame, cleaning
  cost_basis    numeric(12,2) generated always as (cost_purchase + cost_other) stored,
  target_price  numeric(12,2),
  floor_price   numeric(12,2),
  status        text not null default 'draft' check (status in ('draft','active','sold','withdrawn')),
  withdrawn_on  date,
  withdrawn_reason text check (withdrawn_reason in ('personal_use','donated','lost_damaged','other')),
  location      text,                            -- bin / shelf / room
  photo_refs    jsonb not null default '[]',     -- [{"kind":"drive","id":"..."},{"kind":"storage","path":"..."}]
  notes         text,
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now(),
  check ((status = 'withdrawn') = (withdrawn_on is not null))
);
create index items_status_idx on public.items (status);
create index items_category_idx on public.items (category);

-- ===== channel_listings: where an item is (or was) for sale =====
create table public.channel_listings (
  id          uuid primary key default gen_random_uuid(),
  item_id     uuid not null references public.items(id) on delete cascade,
  channel     text not null check (channel in ('etsy','ebay','shopify')),
  external_id text not null,                     -- etsy listing_id | ebay ItemID (= legacyItemId on orders) | shopify product legacyResourceId
  variant_id  text,                              -- shopify variant | etsy product_id (order lines can carry these)
  external_sku text,
  category_ref text,                             -- ebay leaf category id/name as shown on the listing
  fee_rule    text check (fee_rule in ('ebay_most','ebay_media','ebay_jewelry','ebay_bags','ebay_sneakers',
                                       'etsy_us','shopify_payments','shopify_3p')),   -- which est_fees() branch applies
  url         text,
  price       numeric(12,2),
  currency    text not null default 'USD' check (currency = 'USD'),
  status      text not null default 'active' check (status in ('draft','active','sold','ended')),
  listed_at   timestamptz,
  ended_at    timestamptz,
  watchers    int,                               -- etsy num_favorers | ebay WatchCount
  last_seen_at timestamptz,                      -- Etsy terms: listing data must not be > 6 h old
  raw         jsonb,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),
  unique (channel, external_id)
);
create index channel_listings_item_idx on public.channel_listings (item_id);
create index channel_listings_active_idx on public.channel_listings (channel) where status = 'active';

-- ===== sales: one row per ORDER LINE; order-level money is allocated to lines pro rata by price =====
create table public.sales (
  id                uuid primary key default gen_random_uuid(),
  channel           text not null check (channel in ('etsy','ebay','shopify','in_person','other')),
  external_order_id text not null default gen_random_uuid()::text,   -- etsy receipt_id | ebay orderId | shopify order id
  external_line_id  text not null default '1',                       -- etsy transaction_id | ebay lineItemId | shopify line item id
  item_id           uuid references public.items(id) on delete set null,    -- NULL = unmatched, must stay visible
  listing_id        uuid references public.channel_listings(id) on delete set null,
  sold_at           timestamptz not null,                            -- payment time
  status            text not null default 'paid'
                    check (status in ('paid','shipped','delivered','cancelled','refunded','partially_refunded')),
  currency          text not null default 'USD' check (currency = 'USD'),
  item_price        numeric(12,2) not null check (item_price >= 0),  -- after item discounts, before tax
  shipping_charged  numeric(12,2) not null default 0 check (shipping_charged >= 0),
  tax_collected     numeric(12,2) not null default 0 check (tax_collected >= 0),
  tax_collected_by  text not null default 'none' check (tax_collected_by in ('marketplace','seller','none')),
  tax_breakdown     jsonb,                                           -- [{"title":"FL State Tax","rate":0.06,"amount":1.20}]
  fee_marketplace   numeric(12,2) not null default 0,  -- ebay FVF + per-order | etsy 6.5% transaction | shopify 3rd-party txn fee
  fee_payment       numeric(12,2) not null default 0,  -- etsy 3% + 0.25 | shopify card | in-person card
  fee_ads           numeric(12,2) not null default 0,  -- etsy offsite ads | ebay promoted listings
  fee_other         numeric(12,2) not null default 0,  -- ebay international fee etc.
  fees_total        numeric(12,2) generated always as (fee_marketplace + fee_payment + fee_ads + fee_other) stored,
  fee_source        text not null default 'estimated' check (fee_source in ('api','estimated','manual')),
  shipping_cost     numeric(12,2),                     -- what Ricky paid for the label; NULL = not known yet
  refund_amount     numeric(12,2) not null default 0 check (refund_amount >= 0),   -- refunded item + shipping
  refunded_at       timestamptz,
  returned_to_stock boolean not null default false,    -- true when the refunded item physically came back and can be resold
  is_effective      boolean generated always as (status <> 'cancelled' and not (status = 'refunded' and returned_to_stock)) stored,
  net_proceeds      numeric(12,2) generated always as
                    (item_price + shipping_charged - refund_amount
                     - (fee_marketplace + fee_payment + fee_ads + fee_other) - coalesce(shipping_cost, 0)) stored,
  ship_to_state     text,                              -- 2-letter; nexus + 1099-K sanity, not an address
  ship_to_county    text,                              -- FL surtax reporting, only when tax_collected_by = 'seller'
  buyer_ref         text,                              -- marketplace handle; NULL it on eBay account-deletion notices
  source_updated_at timestamptz,                       -- etsy update_timestamp | ebay lastModifiedDate | shopify updatedAt
  raw               jsonb,                             -- latest order object, PII-redacted (no addresses / emails)
  created_at        timestamptz not null default now(),
  updated_at        timestamptz not null default now(),
  unique (channel, external_order_id, external_line_id)
);
create index sales_sold_at_idx on public.sales (sold_at);
create index sales_item_idx on public.sales (item_id);
create index sales_unmatched_idx on public.sales (sold_at) where item_id is null;

-- ===== expenses: everything that is not tied to one sale =====
create table public.expenses (
  id          uuid primary key default gen_random_uuid(),
  incurred_on date not null,
  category    text not null check (category in
              ('marketplace_fee','advertising','shipping_supplies','software','subscription','mileage','sourcing_travel','booth_rent','other')),
  channel     text check (channel in ('etsy','ebay','shopify','in_person','other')),
  item_id     uuid references public.items(id) on delete set null,
  amount      numeric(12,2) not null,                  -- negative = credit / refund
  vendor      text,
  note        text,
  source      text not null default 'manual' check (source in ('manual','etsy_ledger','ebay_finances','shopify_bill','import')),
  external_key text,                                   -- e.g. 'ledger:123456'; NULLs never collide, so manual rows are fine
  created_at  timestamptz not null default now(),
  unique (source, external_key)
);
create index expenses_incurred_idx on public.expenses (incurred_on);

-- ===== events: webhook inbox + raw payloads + idempotency =====
create table public.events (
  id              bigint generated always as identity primary key,
  source          text not null check (source in ('etsy','ebay','shopify')),
  idempotency_key text not null,          -- etsy: webhook-id | shopify: X-Shopify-Webhook-Id | ebay: notification.notificationId
  topic           text not null,
  payload         jsonb not null,
  headers         jsonb,                  -- allow-list only (event id, timestamp, topic); never signatures or secrets
  received_at     timestamptz not null default now(),
  processed_at    timestamptz,
  attempts        int not null default 0,
  error           text,
  unique (source, idempotency_key)
);
create index events_pending_idx on public.events (received_at) where processed_at is null;

-- ===== watches / candidates: eBay sourcing =====
create table public.watches (
  id             uuid primary key default gen_random_uuid(),
  name           text not null,
  keywords       text not null check (char_length(keywords) <= 100),   -- Browse q max length 100
  keywords_exclude text[] not null default '{}',                      -- applied after fetch
  category_id    text,                                                -- ONE eBay leaf category per call
  price_min      numeric(12,2),
  price_max      numeric(12,2),
  conditions     text[] not null default '{}',                        -- eBay filter: NEW | USED (or conditionIds)
  buying_options text[] not null default '{FIXED_PRICE,AUCTION}',
  filters        jsonb not null default '{}',                         -- escape hatch: extra raw Browse filter params
  cadence_minutes int not null default 15 check (cadence_minutes between 1 and 1440),
  active         boolean not null default true,
  cursor_at      timestamptz,                                         -- itemStartDate cursor
  last_run_at    timestamptz,
  last_ok_at     timestamptz,
  last_error     text,
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now(),
  check (price_min is null or price_max is null or price_min <= price_max)
);

create table public.candidates (
  id            uuid primary key default gen_random_uuid(),
  watch_id      uuid not null references public.watches(id) on delete cascade,
  external_id   text not null,                    -- Browse itemId, e.g. 'v1|123456789012|0'
  title         text,
  price         numeric(12,2),
  shipping      numeric(12,2),
  condition     text,
  buying_option text,
  bid_count     int,
  url           text,
  image_url     text,
  item_origin_at timestamptz,                     -- itemOriginDate
  end_at        timestamptz,                      -- itemEndDate (auctions)
  found_at      timestamptz not null default now(),
  last_seen_at  timestamptz not null default now(),   -- eBay license: refresh <= 6 h or purge
  status        text not null default 'new' check (status in ('new','seen','dismissed','bought','ended')),
  item_id       uuid references public.items(id) on delete set null,   -- set when bought -> became inventory
  raw           jsonb,                                                 -- eBay content: purge when the listing is gone
  unique (watch_id, external_id)
);
create index candidates_inbox_idx on public.candidates (found_at desc) where status = 'new';
create index candidates_seen_idx on public.candidates (last_seen_at);

-- ===== alerts =====
create table public.alerts (
  id          uuid primary key default gen_random_uuid(),
  kind        text not null check (kind in
              ('sold','buy_match','price_drop','stale_listing','oversell_risk','integration_down','token_expiring','digest')),
  severity    text not null default 'normal' check (severity in ('low','normal','high')),
  title       text not null,
  body        text,
  payload     jsonb not null default '{}',
  dedupe_key  text not null unique,                -- 'sold:ebay:<order>:<line>' | 'buy:<watch>:<ext id>' | 'stale:<item>:2026-10'
  item_id     uuid references public.items(id) on delete set null,
  created_at  timestamptz not null default now(),
  delivered_at timestamptz,                        -- push provider ACCEPTED it (not "heard")
  delivery    jsonb not null default '{}',         -- {"pushover":{"receipt":"..."},"ntfy":{...}}
  attempts    int not null default 0,
  acked_at    timestamptz
);
create index alerts_undelivered_idx on public.alerts (created_at) where delivered_at is null;
create index alerts_unacked_idx on public.alerts (created_at desc) where acked_at is null;

-- ===== integrations: one row per channel/runner; doubles as the heartbeat =====
create table public.integrations (
  channel          text primary key check (channel in ('etsy','ebay','shopify','pushover','fedora')),
  status           text not null default 'disconnected' check (status in ('disconnected','ok','degraded','error')),
  account_ref      text,                     -- etsy shop_id | ebay userId | shopify shop domain
  token_ref        text,                     -- NAME of the Vault secret. Never the token itself.
  scopes           text[] not null default '{}',
  token_expires_at timestamptz,              -- refresh-token expiry watchdog (etsy 90 d, ebay ~18 mo)
  cursor           jsonb not null default '{}',   -- {"orders_since":"...","listings_since":"..."}
  last_ok_at       timestamptz,
  last_error_at    timestamptz,
  last_error       text,
  heartbeat_at     timestamptz,
  meta             jsonb not null default '{}',
  updated_at       timestamptz not null default now()
);

-- ===== updated_at triggers =====
create trigger t_items_upd        before update on public.items            for each row execute function public.set_updated_at();
create trigger t_listings_upd     before update on public.channel_listings for each row execute function public.set_updated_at();
create trigger t_sales_upd        before update on public.sales            for each row execute function public.set_updated_at();
create trigger t_watches_upd      before update on public.watches          for each row execute function public.set_updated_at();
create trigger t_integrations_upd before update on public.integrations     for each row execute function public.set_updated_at();

-- ===== sold alert, inside the database so no code path can skip it =====
-- Ignores orders older than 24 h: the first eBay sync can backfill up to two years of orders and must not push hundreds of alerts.
create function public.alert_on_sale() returns trigger language plpgsql security definer set search_path = '' as $$
declare t text;
begin
  select title into t from public.items where id = new.item_id;
  insert into public.alerts (kind, severity, title, payload, dedupe_key, item_id)
  values ('sold', 'high',
          'SOLD on ' || new.channel || ': ' || coalesce(t, 'unmatched item') || ' $' || new.item_price,
          jsonb_build_object('sale_id', new.id, 'channel', new.channel, 'order', new.external_order_id),
          'sold:' || new.channel || ':' || new.external_order_id || ':' || new.external_line_id,
          new.item_id)
  on conflict (dedupe_key) do nothing;
  return new;
end $$;
create trigger t_sales_alert after insert on public.sales for each row
  when (new.channel in ('etsy','ebay','shopify') and new.status in ('paid','shipped') and new.sold_at > now() - interval '24 hours')
  execute function public.alert_on_sale();

-- ===== views (security_invoker so the base tables' RLS applies; Postgres 15+) =====
-- stock_state is DERIVED from sales + listings, so a cancelled or returned order can never leave an item stuck as 'sold'.
-- items.status is a convenience flag for the UI; reports use stock_state.
create view public.v_item_state with (security_invoker = true) as
select i.id, i.sku, i.title, i.brand, i.category, i.source, i.status, i.acquired_on, i.withdrawn_on, i.withdrawn_reason,
       i.cost_basis, i.target_price,
       min(cl.listed_at)                                   as first_listed_at,
       coalesce(bool_or(cl.status = 'active'), false)      as is_live,
       sl.sold_at,
       case when sl.sold_at is not null then 'sold'
            when i.status = 'withdrawn'  then 'withdrawn'
            when coalesce(bool_or(cl.status = 'active'), false) then 'active'
            else 'draft' end                               as stock_state,
       (sl.sold_at is null and i.status <> 'withdrawn')    as in_stock,
       public.local_today() - coalesce(i.acquired_on, i.created_at::date) as days_on_hand,
       public.local_today() - (min(cl.listed_at) at time zone public.shop_tz())::date as days_listed
from public.items i
left join public.channel_listings cl on cl.item_id = i.id
left join lateral (select min(s.sold_at) as sold_at from public.sales s
                   where s.item_id = i.id and s.is_effective) sl on true
group by i.id, sl.sold_at;

-- Every non-cancelled order line, INCLUDING refunded ones: fees and label costs on a refunded order are real losses.
-- revenue already nets out refund_amount; COGS is dropped only when the item came back (returned_to_stock).
create view public.v_sale_pnl with (security_invoker = true) as
select s.*, i.sku, i.title, i.category, i.brand, i.source as item_source, i.cost_basis,
       s.item_price + s.shipping_charged - s.refund_amount                       as revenue,
       case when s.returned_to_stock then 0 else coalesce(i.cost_basis, 0) end   as cogs,
       s.net_proceeds - case when s.returned_to_stock then 0 else coalesce(i.cost_basis, 0) end as profit,
       (s.sold_at at time zone public.shop_tz())::date                           as sold_on_local
from public.sales s
left join public.items i on i.id = s.item_id
where s.status <> 'cancelled';

-- ===== RLS + grants =====
alter table public.items            enable row level security;
alter table public.channel_listings enable row level security;
alter table public.sales            enable row level security;
alter table public.expenses         enable row level security;
alter table public.events           enable row level security;
alter table public.watches          enable row level security;
alter table public.candidates       enable row level security;
alter table public.alerts           enable row level security;
alter table public.integrations     enable row level security;

create policy owner_all  on public.items            for all    to authenticated using ((select public.is_owner())) with check ((select public.is_owner()));
create policy owner_all  on public.channel_listings for all    to authenticated using ((select public.is_owner())) with check ((select public.is_owner()));
create policy owner_all  on public.sales            for all    to authenticated using ((select public.is_owner())) with check ((select public.is_owner()));
create policy owner_all  on public.expenses         for all    to authenticated using ((select public.is_owner())) with check ((select public.is_owner()));
create policy owner_all  on public.watches          for all    to authenticated using ((select public.is_owner())) with check ((select public.is_owner()));
create policy owner_all  on public.candidates       for all    to authenticated using ((select public.is_owner())) with check ((select public.is_owner()));
create policy owner_read on public.events           for select to authenticated using ((select public.is_owner()));
create policy owner_read on public.integrations     for select to authenticated using ((select public.is_owner()));
create policy owner_read on public.alerts           for select to authenticated using ((select public.is_owner()));
create policy owner_ack  on public.alerts           for update to authenticated using ((select public.is_owner())) with check ((select public.is_owner()));

-- scoped to OUR objects only: other tables in this project (e.g. a storefront) keep their grants
revoke all on public.items, public.channel_listings, public.sales, public.expenses, public.events, public.watches,
  public.candidates, public.alerts, public.integrations, public.v_item_state, public.v_sale_pnl from anon, authenticated;
grant select, insert, update, delete on public.items, public.channel_listings, public.sales, public.expenses,
      public.watches, public.candidates to authenticated;
grant select on public.events, public.integrations, public.alerts, public.v_item_state, public.v_sale_pnl to authenticated;
grant update (acked_at) on public.alerts to authenticated;      -- the PWA may only acknowledge alerts
-- service_role bypasses RLS: Edge Functions write events, sales, listings, candidates, alerts, integrations.
```

### 1.3 Fee estimator (TESTED against eBay's own examples)

Used only when the API has not yet reported real fees (`sales.fee_source = 'estimated'`). Rates and sources are in section 3.

```sql
-- Fee estimator, used only when the API has not reported real fees yet (sales.fee_source = 'estimated').
-- Inputs are order-level (item = after item discounts, ship = shipping charged, tax = sales tax charged to buyer).
-- Returns the first three fee buckets of public.sales. Rates verified 2026-10-26, see section 3 of the report.
create function public.est_fees(p_rule text, p_item numeric, p_ship numeric, p_tax numeric)
returns table (fee_marketplace numeric, fee_payment numeric)
language sql immutable as $$
  with b as (select p_item + p_ship + p_tax as base, p_item + p_ship as base_no_tax)
  select round(case p_rule
      -- eBay: percentage of (item + shipping + sales tax), plus a per-order fee ($0.30 if order total <= $10, else $0.40)
      when 'ebay_most'      then 0.136 * least(base, 7500) + 0.0235 * greatest(base - 7500, 0) + case when base <= 10 then 0.30 else 0.40 end
      when 'ebay_media'     then 0.153 * least(base, 7500) + 0.0235 * greatest(base - 7500, 0) + case when base <= 10 then 0.30 else 0.40 end
      when 'ebay_jewelry'   then (case when base <= 5000 then 0.15 else 0.09 end) * base       + case when base <= 10 then 0.30 else 0.40 end
      when 'ebay_bags'      then (case when base <= 2000 then 0.15 else 0.09 end) * base       + case when base <= 10 then 0.30 else 0.40 end
      when 'ebay_sneakers'  then 0.08 * base                                                    -- sneakers $150+: no per-order fee
      -- Etsy: 6.5% transaction fee on item + shipping (not tax)
      when 'etsy_us'        then 0.065 * base_no_tax
      -- Shopify third-party gateway fee, Basic plan: 2% of (products - discounts) + tax + shipping. Gateway's own fee not included.
      when 'shopify_3p'     then 0.02 * base
      else 0 end, 2),
    round(case p_rule
      -- Etsy Payments, US seller: 3% + $0.25 of item + shipping + sales tax
      when 'etsy_us'            then 0.03 * base + 0.25
      -- Shopify Payments, Basic, online standard card: 2.9% + $0.30 (base assumed = amount charged; UNVERIFIED)
      when 'shopify_payments'   then 0.029 * base + 0.30
      else 0 end, 2)
  from b;
$$;
```

| eBay Seller Center worked example (VERIFIED, `data-ebay-sellercenter-fees.md`) | Inputs to `est_fees` | eBay says | Function returns |
|---|---|---|---|
| Golf clubs: $150 item, $50 shipping, $10.50 tax | `ebay_most`, 150, 50, 10.50 | $29.03 | $29.03 |
| Skirt: $80 item, free shipping, $85.60 after tax | `ebay_most`, 80, 0, 5.60 | $12.04 | $12.04 |
| Sneakers over $150: $250 item, $270 after tax | `ebay_sneakers`, 250, 0, 20 | $21.60 | $21.60 |
| Phone: $500 + $5 shipping, 7% tax, no store | `ebay_most`, 500, 5, 35.35 | $73.89 | $73.89 |

(In the phone example the page does not state the tax base; 7% of $505 = $35.35 is the base that reproduces its $73.89, and its Basic-Store figure of $50.92 follows from 9.35% of the same base plus $0.40.)

### 1.4 Field-to-API mapping

Fields below were read from the live specs today: Etsy OpenAPI `https://www.etsy.com/openapi/generated/oas/3.0.0.json` (`etsy-shopify-etsy-openapi.json`), eBay Fulfillment and Finances OpenAPI (`ebay-spec-fulfillment_api.json`, `ebay-spec-finances_api.json`), eBay Trading `GetMyeBaySelling` page (`ebay-trading-getmyebayselling.md`), Shopify Admin GraphQL 2026-10 (`data-shopify-gql-*.md`). Money: Etsy returns `{amount, divisor, currency_code}` (integer amount); eBay and Shopify return decimal strings. Convert Etsy with `amount / divisor` and pass **strings** into `numeric(12,2)`, never floats.

**`channel_listings`**

| Column | Etsy | eBay | Shopify |
|---|---|---|---|
| `external_id` | `ShopListing.listing_id` | Trading `GetMyeBaySelling` ... `Item.ItemID`; equals `legacyItemId` on order lines | `Product.legacyResourceId` |
| `variant_id` | `ShopReceiptTransaction.product_id` | `lineItems[].legacyVariationId` (multi-variation only) | line item `variant` id |
| `external_sku` | transaction `sku` (nullable) | `Item.SKU` / `lineItems[].sku` (optional on Trading listings) | `LineItem.sku` (nullable) |
| `url` | `ShopListing.url` | `ListingDetails.ViewItemURL` | `Product.onlineStoreUrl` |
| `price` | `ShopListing.price` (Money; "minimum possible price") | `SellingStatus.CurrentPrice` | `Product.priceRangeV2` |
| `status` | `state`: active; sold_out to sold; draft; inactive/expired/removed to ended | list section: ActiveList, SoldList, UnsoldList, ScheduledList | `Product.status` ACTIVE/DRAFT/ARCHIVED; `totalInventory = 0` means sold |
| `listed_at` | `original_creation_timestamp` (epoch s) | `ListingDetails.StartTime` | `Product.publishedAt` |
| `ended_at` | `ending_timestamp` / `state_timestamp` | `ListingDetails.EndTime` | `Product.updatedAt` when archived |
| `watchers` | `num_favorers` | `WatchCount` | none |

**`sales`** (one row per order line; order-level amounts allocated to lines, section 1.5)

| Column | Etsy | eBay | Shopify |
|---|---|---|---|
| `external_order_id` | `ShopReceipt.receipt_id` | `Order.orderId` | `Order.legacyResourceId` (webhook `id`) |
| `external_line_id` | `ShopReceiptTransaction.transaction_id` | `lineItems[].lineItemId` | `LineItem.id` |
| `sold_at` | transaction `paid_timestamp` (fallback receipt `create_timestamp`) | `paymentSummary.payments[].paymentDate` (fallback `creationDate`) | `Order.processedAt` |
| `status` | receipt `status` (paid, completed, open, payment processing, canceled, fully refunded, partially refunded) + `is_shipped` | `orderPaymentStatus` (PAID, PARTIALLY_REFUNDED, FULLY_REFUNDED, PENDING, FAILED) + `orderFulfillmentStatus` + `cancelStatus.cancelState` | `displayFinancialStatus`, `displayFulfillmentStatus`, `cancelledAt` |
| `item_price` | transaction `price` x `quantity`, minus the line's share of `discount_amt` | `lineItemCost`, or `discountedLineItemCost` when a promotion applied | `LineItem.discountedTotalSet` |
| `shipping_charged` | `total_shipping_cost` (allocated) | `lineItems[].deliveryCost.shippingCost` minus `discountAmount` | `Order.totalShippingPriceSet` (allocated) |
| `tax_collected` | `total_tax_cost` | `pricingSummary.tax` / `lineItems[].taxes[].amount` | `Order.totalTaxSet` |
| `tax_collected_by` | `marketplace` | `marketplace` iff `Order.ebayCollectAndRemitTax = true`, else `none` | `seller` when tax > 0 |
| `tax_breakdown` | none | `taxes[].taxType` (needs `fieldGroups=TAX_BREAKDOWN`) | `Order.taxLines` (title, rate, priceSet) |
| `refund_amount` | `refunds[].amount` | `paymentSummary.refunds[].amount` (`OrderRefund`) / `lineItems[].refunds[]` | `Order.totalRefundedSet` |
| `ship_to_state` | receipt `state` | `fulfillmentStartInstructions[].shippingStep.shipTo.contactAddress.stateOrProvince` | `shippingAddress.provinceCode` |
| `buyer_ref` | `buyer_user_id` (id, never email) | `buyer.username` (may be absent: the spec says select developers stopped receiving it on 2025-09-26) | none |
| `source_updated_at` | `update_timestamp` | `Order.lastModifiedDate` | `Order.updatedAt` |

**Fee columns on `sales`** (what makes `fee_source = 'api'` true)

| Column | Etsy | eBay | Shopify |
|---|---|---|---|
| `fee_marketplace` | 6.5% transaction fee: ledger entry (`PaymentAccountLedgerEntry`: `amount`, `description`, `ledger_type`, `reference_type`, `reference_id`). Which `reference_type` value marks it: **UNVERIFIED**, the spec does not enumerate. | `Order.totalMarketplaceFee` ("cumulative fees accrued for the order and deducted from the seller payout"); split by type from `order_earnings` `orderEarningsSummary.expenses.marketplaceFees[]` (`FINAL_VALUE_FEE`, `FINAL_VALUE_FEE_FIXED_PER_ORDER`) | third-party gateway fee is on Shopify's **bill**, not on the order: estimate with `shopify_3p`, true-up from the monthly bill into `expenses` |
| `fee_payment` | `Payment.amount_fees` = "original card processing fee of the order" (not the other Etsy fees) | none: no separate line on the Seller Center page | `OrderTransaction.fees[]` (`amount`, `rate`, `flatFee`, `type`). Whether it is populated for third-party gateways: **UNVERIFIED** |
| `fee_ads` | offsite-ads ledger entry (type value UNVERIFIED) | `AD_FEE` in `order_earnings` marketplaceFees (attribution to the order: UNVERIFIED) | none |
| `fee_other` | none | `INTERNATIONAL_FEE`, other `FeeTypeEnum` values | none |
| `shipping_cost` | label purchases in the ledger (type UNVERIFIED) | `order_earnings` `expenses.shippingLabels` | none; enter by hand or from the crosslister |

Do not use `Order.paymentSummary.totalDueSeller` as net: the spec says Collect-and-Remit tax is included in it.

**`watches` to the Browse request** (`GET /buy/browse/v1/item_summary/search`, application token, scope `https://api.ebay.com/oauth/api_scope`; semantics from `01` section 1.1 and the filter reference, VERIFIED in wave-1; parameter names re-read today in `ebay-spec-browse_api.json`: `q, category_ids, filter, sort, limit, fieldgroups`)

| Column | Browse parameter |
|---|---|
| `keywords` | `q`: "Maximum length: 100 characters"; space-separated words are AND, `(a, b)` is OR, no `*` wildcard |
| `keywords_exclude` | no parameter; applied by our function after the fetch (whether Browse has a NOT operator: **UNVERIFIED**) |
| `category_id` | `category_ids`: one leaf category per call; a top-level category also needs `q` |
| `price_min`, `price_max` | `filter=price:[min..max],priceCurrency:USD` |
| `conditions` | `filter=conditions:{USED}` (or numeric `conditionIds:{...}`) |
| `buying_options` | `filter=buyingOptions:{FIXED_PRICE\|AUCTION}`; the default result set is FIXED_PRICE only, and the filter works at leaf-category level |
| `cursor_at` | `filter=itemStartDate:[<cursor>..]` with `sort=newlyListed` and `limit=200` |
| `filters` | any other entry from the Browse filter reference, e.g. `maxDeliveryCost:0`, `itemLocationCountry:US`, `excludeSellers:{...}` |
| `cadence_minutes` | not an API field; the cron interval. Cost: `1440 / cadence` calls per day per watch against the shared 5,000/day |

**`candidates` from `ItemSummary`** (field names VERIFIED in the Browse spec today)

| Column | `ItemSummary` field |
|---|---|
| `external_id` | `itemId` (RESTful id, e.g. `v1\|123456789012\|0`) |
| `title` | `title` |
| `price` | `price.value` for fixed price; `currentBidPrice.value` for auctions (which one the API fills for an auction: **UNVERIFIED**) |
| `shipping` | `shippingOptions[].shippingCost.value` (cheapest option) |
| `condition` | `condition` |
| `buying_option` | `buyingOptions` |
| `bid_count` | `bidCount` (auctions only) |
| `url` | `itemWebUrl` (not `itemAffiliateWebUrl`) |
| `image_url` | `image.imageUrl` |
| `item_origin_at` | `itemOriginDate` ("retained if an item is relisted") |
| `end_at` | `itemEndDate` |
| `last_seen_at` | our poll or `getItem` refresh time |
| `raw` | the `ItemSummary` object, purged with the row content when the listing is gone |

**`expenses`**: an Etsy ledger entry id becomes `external_key = 'ledger:<entry_id>'`. eBay Finances `GET /transaction` rows of `transactionType = NON_SALE_CHARGE` (fee types such as `INSERTION_FEE`, `AD_FEE`, `EBAY_STORE_SUBSCRIPTION_FEE`) become `external_key = 'ebay:<transactionType>:<transactionId>'` (the spec: `transactionId`, "combined with the transactionType", is unique). Shopify bills and everything else: manual. **Double-count rule:** a fee tied to one order goes in `sales.fee_*`; only charges with no order go in `expenses`.

**`events` headers:** Etsy `webhook-id`, `webhook-timestamp`; Shopify `X-Shopify-Webhook-Id`, `X-Shopify-Event-Id`, `X-Shopify-Triggered-At`, `X-Shopify-Topic`; eBay `notification.notificationId`, `publishAttemptCount`, `eventDate`. Never store signature headers or secrets.

**`integrations`:** `token_ref` is the name of a Vault secret. The Etsy refresh token lasts 90 days and eBay's about 547.5 days (`refresh_token_expires_in: 47304000`), both from wave-1 (`02` section 2, `01` section 4). Store the expiry in `token_expires_at` and alert before it lapses.

### 1.5 Idempotency and ingestion rules

| Path | Key | Behavior |
|---|---|---|
| Etsy webhook | `webhook-id` header ("unique per call, same across retries", `02` section 4) | `insert into events ... on conflict (source, idempotency_key) do nothing`, return 200 |
| Shopify webhook | `X-Shopify-Webhook-Id` = "a unique composite key per delivery ... to identify and deduplicate individual deliveries"; `X-Shopify-Event-Id` = "a unique ID shared across all deliveries produced by the same merchant action" (VERIFIED, `etsy-shopify-shopify-webhooks-delivery-structure.md`) | same. Dedupe on Webhook-Id; the sale upsert below makes a second topic for the same order harmless |
| eBay notification | `notification.notificationId` (`01` section 3.1) | same |
| Order sale row | `unique (channel, external_order_id, external_line_id)` | upsert guarded by `source_updated_at` (SQL below, TESTED) |
| Listings | `unique (channel, external_id)` | upsert |
| Candidates | `unique (watch_id, external_id)` | insert, do nothing on conflict; update price and `last_seen_at` on re-sight |
| Alerts | `dedupe_key unique` | `on conflict do nothing`; the `sold` alert is a database trigger |
| Expenses | `unique (source, external_key)` | upsert |
| Cursors | `integrations.cursor`, `watches.cursor_at` | re-read from `cursor - 10 minutes`; safe because every write above is idempotent |

Out-of-order-safe upsert. The `is null` branch matters: without it the comparison is NULL and the update silently never applies (TESTED: NULL stored then newer applies; older is ignored).

```sql
insert into public.sales (channel, external_order_id, external_line_id, sold_at, item_price, status, source_updated_at /* , ... */)
values ($1, $2, $3, $4, $5, $6, $7)
on conflict (channel, external_order_id, external_line_id) do update
  set status = excluded.status, item_price = excluded.item_price, source_updated_at = excluded.source_updated_at /* , ... */
  where sales.source_updated_at is null or excluded.source_updated_at > sales.source_updated_at;
```

Rules the ingest code must follow (not enforceable in SQL):

1. **Match order line to item:** listing id first (`channel_listings.external_id` always exists on the order line), then SKU (`items.sku`, often null on eBay Trading listings and Etsy). No match: insert with `item_id = null`; the `sold` alert still fires and query `m9` counts it.
2. **Allocate order-level money to lines** (shipping, tax, discounts, order fees) pro rata by `item_price`; the last line takes the rounding remainder so cents add up.
3. **Shopify: ingest own-store orders only.** If eBay or Etsy orders are ever imported into Shopify (Marketplace Connect, LitCommerce, CedCommerce; `02`, `03`), the same sale arrives twice under two channels and `m8a` would call it a double sale. Filter on `Order.sourceName` ("such as web, mobile_app, or pos") and `Order.app` (VERIFIED fields, `data-shopify-gql-order.md`; the webhook sample shows `"source_name": "web"`). What those fields hold for imported orders: **UNVERIFIED**. Quarantine unknown sources in `events.error` rather than guessing.
4. **Item status.** `items.status` is a UI flag. Reports use the derived `v_item_state.stock_state`, so a cancelled or returned order cannot strand an item as sold. On a refund where the piece comes back, set `sales.returned_to_stock = true`; the item then reappears in stock and its COGS leaves the P&L, while the lost fees and label cost stay.
5. **PII.** Shopify's default webhook payload is the full resource, including `email`, `phone`, `customer`, `billing_address`, `shipping_address` (VERIFIED in the sample payload, `etsy-shopify-shopify-webhooks-reference.md`). Etsy API Terms #17 ask for the minimum data needed (`02` section 5) and eBay's account-deletion duty (`01` section 3.3) means buyer data must be deletable. So: (a) subscribe to Shopify with `include_fields`, which Shopify supports ("the delivery payload includes only the specified fields", VERIFIED); (b) strip before insert: Etsy receipt `name, first_line, second_line, city, zip, formatted_address, buyer_email, seller_email, payment_email, message_from_*, gift_message, gift_sender`; eBay order `buyer.buyerRegistrationAddress`, `shipTo` (keep only the state), `buyerCheckoutNotes`; (c) once stripped, the payloads carry no buyer PII, so they are kept indefinitely (a few KB per order) next to the redacted `sales.raw`; (d) on an eBay `MARKETPLACE_ACCOUNT_DELETION` notice, `update sales set buyer_ref = null where buyer_ref = $username`.
6. **Candidates are eBay content with a clock.** The eBay API License (`01` section 1.7, VERIFIED text) says displayed listing data may not be more than 6 hours old and eBay content must be deleted when it is no longer public. The poller searches with `itemStartDate:[cursor..]`, which returns only new listings, so an old candidate's `last_seen_at` never advances on its own. Needed: a refresh pass, `GET /buy/browse/v1/item/{item_id}` (in the Browse spec, VERIFIED in wave-1; the bulk `getItems` is partner-only), one call per candidate still in `new`/`seen`, about every 5 hours. Budget: 50 live candidates x about 5 calls/day = 250 calls, 5% of the 5,000/day Browse limit (`01` section 1.1). Without that pass, candidates live 6 hours and query `a3` purges them, keeping a tombstone (`watch_id`, `external_id`, `status`) so the same listing does not alert twice. Whether keeping the tombstone id is allowed: **UNVERIFIED** legal reading.
7. **Backfill must not alert.** The first eBay sync can return up to two years of orders (`getOrders`, `01` section 2.3). The `sold` alert trigger therefore ignores orders whose `sold_at` is more than 24 hours old. TESTED: 3-40 day old seed orders and a 400-day-old shipped order produce no alert; one fresh order produces exactly one; a redelivery of it still one.

### 1.6 RLS (in the DDL above, TESTED)

- Every table has RLS enabled; `anon` and `authenticated` default grants are revoked and re-granted per table. Supabase's current guide: "Enable RLS on every table in an exposed schema. On projects that still grant `anon` and `authenticated` by default, revoke those grants. Adding policies doesn't remove them." (VERIFIED, `data-supabase-rls.md`).
- One gate, `public.is_owner()`: `auth.jwt() -> 'app_metadata' ->> 'shop_role' = 'owner'`. `raw_app_meta_data` "cannot be updated by the user, so it's a good place to store authorization data" (VERIFIED). Caveat from the same page: a JWT is not refreshed instantly, so removing a role takes effect at the next token refresh. The second user from `05` open question 8 is a metadata flag, not a schema change.
- Policies call `(select public.is_owner())`, the wrapped form Supabase recommends so Postgres caches it per statement (VERIFIED, "Wrapping the function causes an `initPlan`").
- Writers are `service_role` (bypasses RLS: "It bypasses RLS, so keep it server-side", VERIFIED). The PWA gets full CRUD on `items`, `channel_listings`, `sales`, `expenses`, `watches`, `candidates` (it must enter in-person sales and costs), read-only on `events` and `integrations`, and on `alerts` only `select` plus `update (acked_at)`.
- Views carry `security_invoker = true`. Supabase warns that views "bypass RLS by default". TESTED: a non-owner gets 0 rows through `v_item_state`, the owner gets all 15 seed items.
- Tested outcomes: owner can ack an alert; owner cannot edit an alert title (permission denied); owner cannot write `events`; no claims means zero rows; two deliveries with the same `webhook-id` leave one row.

---

## 2. Reseller metrics

### 2.1 Definitions

All dates are in `America/New_York` (`shop_tz()`); month bucketing in UTC would move a late-evening Florida sale into the next month. "Effective sale" = not cancelled, and not (refunded and returned to stock).

| Query | Metric | Exact definition |
|---|---|---|
| `m1` | Sell-through, 30 d | items sold in the window / items **on offer** in the window. On offer = first listed before the window ended and not sold or withdrawn before it started. Relists do not create new offers (first listing date wins, the same rule as Flipwise "New Listings"). |
| `m1b` | Cohort sell-through | of items first listed in month M, share sold within 30 / 60 / 90 days of first listing. Right-censored: an unsold item counts only once it is old enough for that horizon. The honest number for one-offs. |
| `m1c` | Sell-through, Genie-style | items sold in a month / items purchased in that month. Shown only for comparison; it is N/A for any month with no purchases and swings with estate-sale timing. |
| `m2` | Aging buckets | for stock not yet sold or withdrawn: `days_on_hand = today - acquired_on`, buckets 0-30, 31-60, 61-90, 91-180, 181+; items, cost tied up, list value, never-listed count. `days_listed` is also on `v_item_state`. |
| `m3` | Profit, margin, ROI | `profit = net_proceeds - cogs`; `margin = profit / revenue`; `ROI = sum(profit) / sum(cogs)` over sales with cost > 0 (found-for-free items would make ROI infinite; Flipwise excludes them too). Ratios are computed on sums, never averaged. Sliced by channel, category, source, brand. Refunded-and-returned orders stay in: fees and labels are real losses. |
| `m4` | Cash tied up | `sum(cost_basis)` of in-stock items, by category, plus list value, unlisted cost, and the count of items with no cost recorded. |
| `m5` | Days to sell | by category: average and **median** of first listing to sale (skewed, so the median matters), average acquisition to sale, average acquisition to first listing (the "pile" metric). |
| `m6` | Fees per channel per month | sale-tied fees from `sales` (all non-cancelled orders, refunded ones included because they were charged) plus `marketplace_fee`/`advertising` rows from `expenses`. |
| `m7` | Monthly P&L | revenue (item + shipping - refunds, **excludes sales tax**) - sale fees - label costs - COGS (cost of items sold that month) - overhead (all `expenses`) - write-offs (`lost_damaged`/`other` withdrawals). Personal-use and donated withdrawals are not an expense. |
| `m7b` | Cash-flow view | money spent on stock per month. A view, not an IRS method; see section 4. |
| `m8` | Double-sale guards | `m8a`: an item with 2+ effective sales. `m8b`: an effective sale more than 15 minutes old while another listing of the item is still active (15 minutes = Crosslist's stated detection time, `03` section 0). |
| `m9` | Data quality | unmatched sales, in-stock items with no cost, sales older than 7 days with no label cost, estimated fees older than 3 days. |
| `m10` | Tax | `m10a`: tax Ricky collected himself (Shopify), by month and county. `m10b`: per-platform gross payments including shipping and tax, and the transaction count, against the 1099-K test. |
| `a1`-`a3` | Maintenance | stale-listing alerts (listed 60+ days), integration-down alerts, candidate purge. |

Reconciliation property (TESTED): for the seed month, `m6` sale fees ($73.73) equal `m7` sale fees ($73.73). Before the refunded-order fix they disagreed ($69.56 vs $73.73).

### 2.2 SQL (TESTED)

#### `m1_sell_through_30d`

```sql
-- Sell-through (30 d) = items sold in the window / items that were on offer at any point in the window
-- (listed before the window ended AND not yet sold/withdrawn before it started).
select coalesce(category, 'ALL') as category,
       count(*) filter (where sold_at >= w.s and sold_at < w.e)                               as sold,
       count(*)                                                                                as on_offer,
       round(100.0 * count(*) filter (where sold_at >= w.s and sold_at < w.e) / count(*), 1)   as sell_through_pct
from public.v_item_state v
cross join (select now() - interval '30 days' as s, now() as e) w
where v.first_listed_at is not null
  and v.first_listed_at < w.e
  and (coalesce(v.sold_at, v.withdrawn_on::timestamptz) is null            -- still on the shelf ...
       or coalesce(v.sold_at, v.withdrawn_on::timestamptz) >= w.s)           -- ... or left during the window
group by rollup (category)
order by category nulls last;
```

#### `m1b_cohort_sell_through`

```sql
-- Of the items first listed in month M, what share sold within 30 / 60 / 90 days of first listing.
-- Right-censored: an unsold item only counts once it is old enough for that horizon.
select cohort, count(*) as listed,
       round(100.0 * count(*) filter (where sold_at <= first_listed_at + interval '30 days')
             / nullif(count(*) filter (where sold_at <= first_listed_at + interval '30 days' or first_listed_at <= now() - interval '30 days'), 0), 1) as sold_30d_pct,
       round(100.0 * count(*) filter (where sold_at <= first_listed_at + interval '60 days')
             / nullif(count(*) filter (where sold_at <= first_listed_at + interval '60 days' or first_listed_at <= now() - interval '60 days'), 0), 1) as sold_60d_pct,
       round(100.0 * count(*) filter (where sold_at <= first_listed_at + interval '90 days')
             / nullif(count(*) filter (where sold_at <= first_listed_at + interval '90 days' or first_listed_at <= now() - interval '90 days'), 0), 1) as sold_90d_pct
from (select date_trunc('month', first_listed_at at time zone public.shop_tz())::date as cohort, first_listed_at, sold_at
      from public.v_item_state where first_listed_at is not null) c
group by cohort order by cohort;
```

#### `m1c_sell_through_purchase_based`

```sql
-- My Reseller Genie's definition: items sold in the month / items purchased in the month (N/A when nothing was bought).
-- Lumpy for a sourcing-by-estate-sale shop; keep it only as a comparison with the on-offer definition above.
with b as (select date_trunc('month', coalesce(acquired_on, created_at::date))::date as month, count(*) as bought
           from public.items group by 1),
     s as (select date_trunc('month', sold_on_local)::date as month, count(*) as sold from public.v_sale_pnl where is_effective group by 1)
select coalesce(b.month, s.month) as month, coalesce(b.bought, 0) as bought, coalesce(s.sold, 0) as sold,
       round(100.0 * s.sold / nullif(b.bought, 0), 1) as sell_through_pct
from b full join s on s.month = b.month order by 1;
```

#### `m2_aging_buckets`

```sql
select case when days_on_hand <= 30 then '0-30' when days_on_hand <= 60 then '31-60' when days_on_hand <= 90 then '61-90'
            when days_on_hand <= 180 then '91-180' else '181+' end as bucket,
       count(*)                                         as items,
       sum(cost_basis)                                  as cash_tied_up,
       sum(target_price)                                as list_value,
       count(*) filter (where first_listed_at is null)  as never_listed
from public.v_item_state
where in_stock
group by 1
order by min(days_on_hand);
```

#### `m3_roi_margin`

```sql
-- profit = net_proceeds - cogs ; margin = profit / revenue ; ROI = SUM(profit) / SUM(cogs).
-- Ratios are computed on sums, never averaged. ROI skips sales whose item has no recorded cost (Flipwise does the same),
-- otherwise found-for-free items would give an infinite ROI. Refunded-and-returned orders stay in: their fees and labels are real losses.
select case when grouping(channel) = 0     then 'channel: '  || channel
            when grouping(category) = 0    then 'category: ' || coalesce(category, '(unmatched sale)')
            when grouping(item_source) = 0 then 'source: '   || coalesce(item_source, '(none)')
            when grouping(brand) = 0       then 'brand: '    || coalesce(nullif(brand, ''), '(none)')
            else 'ALL' end                                                    as slice,
       count(*) filter (where is_effective)                                   as sales,
       sum(revenue)                                                           as revenue,
       sum(fees_total)                                                        as fees,
       sum(coalesce(shipping_cost, 0))                                        as label_cost,
       sum(cogs)                                                              as cogs,
       sum(profit)                                                            as profit,
       round(100.0 * sum(profit) / nullif(sum(revenue), 0), 1)                as margin_pct,
       round(100.0 * sum(profit) filter (where cogs > 0)
             / nullif(sum(cogs) filter (where cogs > 0), 0), 1)               as roi_pct,
       round(avg(revenue) filter (where revenue > 0), 2)                      as avg_gross_per_sale,
       round(avg(profit) filter (where is_effective), 2)                      as avg_profit_per_sale,
       count(*) filter (where shipping_cost is null)                          as provisional_no_label_cost
from public.v_sale_pnl
where sold_on_local >= public.local_today() - 90
group by grouping sets ((channel), (category), (item_source), (brand), ())
order by 1;
```

#### `m4_cash_tied_up`

```sql
select coalesce(category, '(all)') as category,
       count(*)                                          as items,
       sum(cost_basis)                                   as cash_tied_up,
       sum(target_price)                                 as list_value,
       sum(cost_basis) filter (where first_listed_at is null) as unlisted_cost,
       count(*) filter (where cost_basis = 0)            as cost_missing
from public.v_item_state
where in_stock
group by rollup (category)
order by category nulls last;
```

#### `m5_days_to_sell_by_category`

```sql
select category, count(*) as n,
       round(avg(d_listed), 1)                                   as avg_days_listed_to_sold,
       percentile_cont(0.5) within group (order by d_listed)      as median_days_listed_to_sold,
       round(avg(d_held), 1)                                     as avg_days_acquired_to_sold,
       round(avg(d_held - d_listed), 1)                          as avg_days_acquired_to_listed
from (select category,
             (sold_at at time zone public.shop_tz())::date - (first_listed_at at time zone public.shop_tz())::date as d_listed,
             (sold_at at time zone public.shop_tz())::date - acquired_on                                           as d_held
      from public.v_item_state where sold_at is not null and first_listed_at is not null) t
group by category order by category;
```

#### `m6_fees_per_channel_per_month`

```sql
-- sale-tied fees (sales.fee_*) + non-sale fees and ads (expenses). Cancelled orders excluded; refunded orders still paid fees.
select month, channel, round(sum(sale_fees), 2) as sale_fees, round(sum(other_fees), 2) as listing_and_ad_fees,
       round(sum(sale_fees + other_fees), 2) as total_fees
from (
  select date_trunc('month', sold_at at time zone public.shop_tz())::date as month, channel, fees_total as sale_fees, 0::numeric as other_fees
  from public.sales where status <> 'cancelled'
  union all
  select date_trunc('month', incurred_on)::date, coalesce(channel, 'unassigned'), 0, amount
  from public.expenses where category in ('marketplace_fee', 'advertising')
) u
group by month, channel order by month, channel;
```

#### `m7_monthly_pnl`

```sql
-- Accrual / specific-identification: COGS = cost_basis of items in the month they SELL.
-- Excluded on purpose: sales tax (pass-through), personal-use and donated withdrawals (not an expense; see Pub 334 line 36 and donation rules).
with s as (
  select date_trunc('month', sold_on_local)::date as month,
         sum(revenue) as revenue, sum(fees_total) as sale_fees, sum(coalesce(shipping_cost, 0)) as labels, sum(cogs) as cogs
  from public.v_sale_pnl group by 1),
e as (
  select date_trunc('month', incurred_on)::date as month, sum(amount) as overhead from public.expenses group by 1),
w as (
  select date_trunc('month', withdrawn_on)::date as month, sum(cost_basis) as write_offs
  from public.items where status = 'withdrawn' and withdrawn_reason in ('lost_damaged', 'other') group by 1)
select coalesce(s.month, e.month, w.month) as month,
       coalesce(s.revenue, 0) as revenue, coalesce(s.sale_fees, 0) as sale_fees, coalesce(s.labels, 0) as labels,
       coalesce(s.cogs, 0) as cogs, coalesce(e.overhead, 0) as overhead, coalesce(w.write_offs, 0) as write_offs,
       coalesce(s.revenue, 0) - coalesce(s.sale_fees, 0) - coalesce(s.labels, 0) - coalesce(s.cogs, 0)
         - coalesce(e.overhead, 0) - coalesce(w.write_offs, 0) as net_profit
from s full join e on e.month = s.month full join w on w.month = coalesce(s.month, e.month)
order by 1;
```

#### `m7b_cash_flow_purchases`

```sql
-- Cash-FLOW view: money spent on stock per month, as Genie's "Cash Inventory Method" and Flipwise's "Spent on New Inventory" show it.
-- NOT asserted to be the IRS-correct deduction timing (UNVERIFIED, see report section 4). The same data supports either timing.
select date_trunc('month', coalesce(acquired_on, created_at::date))::date as month, count(*) as items, sum(cost_basis) as purchases
from public.items group by 1 order by 1;
```

#### `m8a_double_sold`

```sql
select i.sku, i.title, count(*) as sales, array_agg(s.channel order by s.sold_at) as channels
from public.sales s join public.items i on i.id = s.item_id
where s.is_effective
group by i.id having count(*) > 1;
```

#### `m8b_sold_but_still_listed`

```sql
select i.sku, cl.channel, cl.external_id, s.sold_at, now() - s.sold_at as sold_ago
from public.sales s
join public.items i on i.id = s.item_id
join public.channel_listings cl on cl.item_id = s.item_id and cl.status = 'active'
where s.is_effective and now() - s.sold_at > interval '15 minutes';
```

#### `m9_data_quality`

```sql
select 'unmatched_sales' as check_name, count(*) as n from public.sales where item_id is null and status <> 'cancelled'
union all select 'items_missing_cost_in_stock', count(*) from public.v_item_state where in_stock and cost_basis = 0
union all select 'sales_without_label_cost_over_7d', count(*) from public.sales
  where shipping_cost is null and channel in ('etsy','ebay','shopify') and status not in ('cancelled','refunded') and sold_at < now() - interval '7 days'
union all select 'estimated_fees_older_than_3d', count(*) from public.sales where fee_source = 'estimated' and channel in ('etsy','ebay','shopify') and sold_at < now() - interval '3 days';
```

#### `m10a_sales_tax_owed`

```sql
-- Only tax the SELLER collected (Shopify own-site) is a liability to Florida DOR. Marketplace-collected tax is remitted by the marketplace.
select date_trunc('month', sold_at at time zone public.shop_tz())::date as month, ship_to_county,
       sum(tax_collected) as tax_collected, sum(item_price + shipping_charged) as taxable_sales
from public.sales
where tax_collected_by = 'seller' and status <> 'cancelled'
group by 1, 2 order by 1, 2;
```

#### `m10b_1099k_watch`

```sql
-- 1099-K is triggered per platform when gross payments > $20,000 AND transactions > 200 (IRS). Gross includes shipping and tax.
select channel, extract(year from sold_at at time zone public.shop_tz())::int as yr,
       round(sum(item_price + shipping_charged + tax_collected), 2) as gross_payments,
       count(distinct external_order_id) as transactions,
       (sum(item_price + shipping_charged + tax_collected) > 20000 and count(distinct external_order_id) > 200) as would_get_1099k
from public.sales where channel in ('etsy', 'ebay', 'shopify') and status <> 'cancelled'
group by 1, 2 order by 2, 1;
```

#### `a1_stale_listing_alerts`

```sql
insert into public.alerts (kind, severity, title, payload, dedupe_key, item_id)
select 'stale_listing', 'low', 'Listed ' || days_listed || ' days, still unsold: ' || title,
       jsonb_build_object('days_listed', days_listed, 'cost', cost_basis, 'target', target_price),
       'stale:' || id || ':' || to_char(public.local_today(), 'IYYY-IW'), id
from public.v_item_state
where in_stock and is_live and days_listed >= 60
on conflict (dedupe_key) do nothing
returning title;
```

#### `a2_integration_down_alerts`

```sql
insert into public.alerts (kind, severity, title, payload, dedupe_key)
select 'integration_down', 'high', channel || ' has not checked in since ' || to_char(heartbeat_at, 'YYYY-MM-DD HH24:MI'),
       jsonb_build_object('channel', channel), 'down:' || channel || ':' || to_char(date_trunc('hour', now()), 'YYYYMMDDHH24')
from public.integrations
where status <> 'disconnected' and heartbeat_at < now() - interval '15 minutes'
on conflict (dedupe_key) do nothing
returning title;
```

#### `a3_purge_ended_candidates`

```sql
-- BACKSTOP. The refresh job (GET /buy/browse/v1/item/{item_id}, one call per live candidate) bumps last_seen_at every ~5 h.
-- Anything it could not re-verify, or that eBay says is gone, is purged: eBay API License says delete eBay content once it is no longer
-- publicly available. A tombstone (watch_id, external_id, status) stays so the same listing does not alert twice (legal reading UNVERIFIED).
update public.candidates
set title = null, price = null, shipping = null, url = null, image_url = null, raw = null, status = 'ended'
where status in ('new', 'seen', 'dismissed') and last_seen_at < now() - interval '6 hours'
returning external_id;
```

### 2.3 What the existing tools track (docs read today) and what is missing here

| Metric | Flipwise | My Reseller Genie | Vendoo | Crosslist | This schema |
|---|---|---|---|---|---|
| Gross sales, net profit | Gross incl. buyer-paid shipping; `Net profit = Gross Sales - (COGS + Shipping + Marketplace Fees + Other Sales Expenses)` | gross profit, profitability dashboard | revenue, profit; profit from COG + sale price + marketplace fees + shipping fees | sale price, COGS, shipping expense, other expenses, estimated profit and margin (`03`) | yes (`m3`) |
| Margin, ROI | `NPM = Net Profit / Gross Sales`; `ROI = Net Profit / Inventory Cost`, ignores sales with no purchase price; also averages per sale | not defined on the pages read | not stated | margin | yes, same conventions |
| Average per sale | avg gross, avg net, avg NPM, avg ROI per sale | average sales price | ASP with prior-period comparison | n/a | avg gross and avg profit; prior-period compare is a UI job |
| By marketplace / source / category / brand | marketplace, source | department, category, sub-category, brand | marketplace, categories, sub-categories, brands, custom labels | n/a | channel, source, category, brand (`tags[]` = labels) |
| Sell-through | not in the definitions page | yes: sold in month / purchased in month | not stated | n/a | two definitions + cohort (`m1`, `m1b`, `m1c`) |
| Time to list / time to sell | avg time to list (purchase to list), avg time to sell (list to sale) | n/a | n/a | n/a | yes, plus median (`m5`) |
| Aging, stale stock | auto-reprice and delayed promotion of unsold items (automation, not a metric) | n/a | stale listing warning exists (not in the mobile app, `03`) | n/a | aging buckets + stale alert (`m2`, `a1`) |
| Cash tied up in stock | "what it cost, where it is stored" per item; no stock-value metric in the definitions page | inventory report for accrual users | n/a | n/a | yes (`m4`) |
| Spent on new inventory | yes | via cash/accrual inventory method | n/a | n/a | `m7b` |
| Fees by channel | marketplace fees, shipping labels (separate lines) | transaction fees, shipping costs, other costs per sale | in the CSV | n/a | `m6` |
| Expense ledger, mileage | yes (Schedule C categories, mileage) | yes, bank/card import, mileage | no | n/a | `expenses` (mileage as an amount; no miles column) |
| Tax report, P&L | cash or accrual tax report, income statement | detail + summary P&L, estimated income tax, cash or accrual inventory method | CSV for bookkeeping | n/a | `m7` P&L; no tax estimator |
| Sales tax by state | n/a | a help article exists for a "sales tax by state" report | n/a | n/a | `m10a` (Florida only, by county) |
| Buyer locations | map | n/a | n/a | n/a | `ship_to_state`; one `group by` |
| Double-sell guard | n/a | n/a | n/a | n/a | `m8a`, `m8b` |

Sources, all read today: Flipwise `help.flipwise.app/article/55-sales-insights-metrics-definitions` (updated 2026-04-09) and `flipwise.app` (`data-flipwise-metric-defs.md`, `tools-flipwise-home.md`); Genie `myresellergenie.com/salesanalytics`, `/taxes`, help articles on sell-through and the Ultimate plan (`data-genie-*.md`, `tools-genie-*.md`); Vendoo `help.vendoo.co/en/articles/6260264`, `/6260293`, `vendoo.co/reselling-analytics` (`data-vendoo-*.md`); Crosslist from `03-existing-tools.md`. "n/a" means the pages I read do not mention it, not that the product lacks it.

**Missing here on purpose:** bank/card feed, income-tax estimator, relist/reprice automation (the crosslister's job), buyer messaging. **Worth adding if wanted:** a miles column on `expenses`, prior-period deltas in the UI.

---

## 3. Fee schedules, verified today

The eBay help page `ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822` returned a captcha to crawl4ai and WebFetch (`data-ebay-selling-fees.md`; two URL variants did the same). The **eBay Seller Center fee page** loaded in full and is eBay's own: `https://www.ebay.com/sellercenter/selling/start-selling-on-ebay/seller-fees` (`data-ebay-sellercenter-fees.md`). Everything eBay below is from it unless noted. Etsy: help-center articles. Shopify: pricing page and billing help.

### 3.1 eBay (US, individual seller, no Store)

| Fee | Value | Tag |
|---|---|---|
| Insertion fee | 250 free listings/month, then $0.35 each. "Category exclusions apply." | VERIFIED |
| Final value fee, "Most categories (exceptions apply)" | 13.6% of the total amount of the sale up to $7,500 per item, plus 2.35% on the portion above $7,500 | VERIFIED |
| Books & Magazines, Movies & TV, Music (except Vinyl Records) | 15.3% up to $7,500, 2.35% above | VERIFIED |
| Most Jewelry & Watches | 15% if the sale is $5,000 or less; 9% on the whole sale if over $5,000 (a step, not marginal) | VERIFIED |
| Women's Bags & Handbags | 15% if $2,000 or less; 9% if over | VERIFIED |
| Sneakers over $150 | 8%, no per-order fee | VERIFIED |
| Per-order fee | $0.30 for orders of $10.00 or less; $0.40 over $10.00 | VERIFIED |
| Fee base | "the total amount of the sale, including the cost of the item and shipping, sales tax, and other applicable fees" | VERIFIED, and reproduced to the cent by four worked examples (1.3) |
| Promoted Listings Standard | an ad fee only if the item sells; rate chosen by the seller | existence VERIFIED; rate range and base **UNVERIFIED** |
| International fee | exists when the buyer's address or delivery address is outside the US | existence VERIFIED; the 1.65% figure is **V-secondary** (`sellmath.com`) |
| Store subscription | Starter $4.95/mo, Basic $21.95/mo (annual billing). Basic and up: most categories 12.7% up to $2,500, then 2.35% | VERIFIED (`data-ebay-store-subs.md`, `data-ebay-sellercenter-fees.md`) |
| Store break-even (derived) | $21.95 / (13.6% - 12.7%) = about $2,440 of eBay sales per month | my arithmetic |
| 1099-K | eBay issues one for more than $20,000 and more than 200 transactions (page says 2025) | VERIFIED (`data-ebay-tax-info.md`) |

Fee-on-tax check: eBay charges its percentage **on sales tax and shipping too**, so a 7% tax state costs an extra 0.95 percentage points of fee on the item price. That is part of why eBay shows the highest fee of the three channels in section 3.4.

Catalog id to `fee_rule` (set it on the `channel_listings` row at listing time). eBay category exceptions beyond the Seller Center table, e.g. sub-categories, could not be checked because the full help page is walled: **UNVERIFIED**.

| Catalog ids (`research/inventory/2026-10-26-catalog.md`) | Item | `fee_rule` |
|---|---|---|
| C1 to C7 | Playboy x5, Penthouse, Southern Peach (magazines) | `ebay_media` (15.3%) |
| C8 | Chanel coffee-table book | `ebay_media` (books, 15.3%) |
| B11 | Chunky gold chain necklaces | `ebay_jewelry` (15%) |
| A5 | Elvis signed 8x10 (memorabilia) | `ebay_most` |
| A1-A4, A8-A17, A19-A20, A22-A23 | lamps, art, decor, furniture, turntable (not vinyl), projector, mannequins | `ebay_most` |
| B1, B5-B7, B9-B10, B12-B15, B18 | clothing, hat, belt, boots, shoes | `ebay_most` (no handbags or sneakers $150+ in stock) |
| any item on Etsy | | `etsy_us` |
| any item on Shopify | | `shopify_payments` (or `shopify_3p` if another gateway) |

Whether a magazine is categorised under Books & Magazines or a Collectibles paper category decides 15.3% vs 13.6%: **UNVERIFIED**. The API settles it after the first sale: `Order.totalMarketplaceFee` against `Order.totalFeeBasisAmount`.

### 3.2 Etsy (US seller, Etsy Payments)

| Fee | Value | Tag |
|---|---|---|
| Listing fee | $0.20 per listing; added when listed; $0.20 again when a listing expires after 4 months and auto-renews; charged whether or not it sells | VERIFIED (`data-etsy-help-fees.md`) |
| Transaction fee | 6.5% of the total order amount, which includes shipping and gift wrapping when charged | VERIFIED. Whether discounts reduce the base: **UNVERIFIED** |
| Payment processing, United States | 3% + $0.25, "taken from the item's total sale price, including its shipping fees, and any applicable sales tax"; credited proportionally on a refund | VERIFIED (`data-etsy-processing-fees.md`, row "United States 3% + 0.25 USD") |
| Offsite Ads | 15% if the shop made under $10,000 in any consecutive 365 days (can opt out); 12% at $10,000 or more (required); never more than $100 per order; only when a buyer clicks an ad and buys within 30 days | VERIFIED (`data-etsy-offsite-ads.md`) |
| Etsy Ads | variable, seller-set | VERIFIED |
| Regulatory operating fee | UK, France, Italy, India, Spain, Turkiye, Vietnam, Canada only, so not US | VERIFIED |
| Currency conversion | 2.5% when conversion is needed (not for a USD shop with a USD account) | VERIFIED |
| Shop set-up fee | one-time, "cost varies by location"; the US amount is not on the page | **UNVERIFIED** |

### 3.3 Shopify (Basic, online, US)

| Fee | Value | Tag |
|---|---|---|
| Plan | $29/mo billed yearly; $39/mo monthly (`02` section 10; today's page shows $29 on the yearly toggle) | VERIFIED |
| Shopify Payments, online standard cards | 2.9% + 30c (Grow 2.7%, Advanced 2.5%, Plus 2.25%) | VERIFIED (`data-shopify-pricing.md`) |
| Shopify Payments, "premium" cards | 3.5% + 30c; what counts as premium: **UNVERIFIED** | rate VERIFIED |
| Online international | +1% | VERIFIED |
| PayPal wallet | starting at 3.49% + 49c | VERIFIED |
| In-person card (the physical room) | 2.6% + 10c; manual entry 3.5% + 10c | VERIFIED |
| Third-party gateway fee | Basic 2%, Grow 1%, Advanced 0.6%, Plus 0.2%, **in addition to** the gateway's own fees. Formula: `[(cost of products - discounts) + tax + shipping charges] x rate`, computed for a 30-day period. Not returned on refunds. Not charged on POS or manual payments. Exempt when paid through Shopify Payments or Shop Pay; PayPal is exempt if Shopify Payments is the primary provider. | VERIFIED (`data-shopify-3p-fees.md`, pricing page) |
| Base of the Shopify Payments percentage (item only, or item + shipping + tax) | the pricing page does not say; modeled as the amount charged | **UNVERIFIED** |

### 3.4 Net-calculation formulas (one order, before allocation to lines)

Let `item` be the price after item discounts, `ship` shipping charged, `tax` sales tax charged to the buyer, `B = item + ship + tax`.

| Channel | `fee_marketplace` | `fee_payment` | `fee_ads` (API only) | Per-order and fixed cost |
|---|---|---|---|---|
| eBay, most categories | `0.136 x min(B, 7500) + 0.0235 x max(B - 7500, 0) + (0.30 if B <= 10 else 0.40)` | 0 | `AD_FEE` | insertion $0.35 after 250 listings/month |
| eBay, media | same with 0.153 | 0 | `AD_FEE` | same |
| eBay, jewelry | `(0.15 if B <= 5000 else 0.09) x B + per-order fee` | 0 | `AD_FEE` | same |
| Etsy | `0.065 x (item + ship)` | `0.03 x B + 0.25` | offsite ads: 15% or 12%, capped at $100 | $0.20 per listing and per 4-month renewal (`expenses`) |
| Shopify + Shopify Payments | 0 | `0.029 x B + 0.30` (online standard card) | 0 | plan fee $29-39/mo (`expenses`) |
| Shopify + other gateway | `0.02 x B` | gateway's own | 0 | plan fee |

Same order on each channel, `item $100`, `ship $12`, 7% tax (TESTED output of `est_fees`):

| Rule | Item + ship | Tax | Estimated fees | % of item + ship |
|---|---|---|---|---|
| `ebay_most` | $112 | $7.84 | $16.70 | 14.9% |
| `etsy_us` (no ads) | $112 | $7.84 | $11.13 | 9.9% |
| `shopify_payments` | $112 | $7.84 | $3.78 | 3.4% (plus $29-39/mo) |
| `shopify_3p` | $112 | $7.84 | $2.40 | 2.1% (plus the gateway's fee, plus the plan) |
| `ebay_media` ($28 + $5 ship) | $33 | $2.31 | $5.80 | 17.6% |
| `ebay_jewelry` ($40 + $5 ship) | $45 | $3.15 | $7.62 | 16.9% |

Etsy with an attributed offsite ad adds 15% of the order on top: about 25% in total. The cheap channel per sale is the one Ricky has to drive traffic to himself.

---

## 4. Tax basics that change the data model

**Form 1099-K.** VERIFIED (IRS, `irs.gov/businesses/understanding-your-form-1099-k` and the IR-2025-107 FAQ release, `data-irs-1099k*.md`): a payment app or online marketplace must send a 1099-K when payments for goods or services total **over $20,000 in more than 200 transactions**; the One, Big, Beautiful Bill "retroactively reinstated" the pre-2021 threshold. The page carries no 2026-specific change and no expiry. A platform "may send" one below the threshold, and "whether or not you receive a Form 1099-K, you must still report any income". Pub 334 (2025) adds that a 1099-K amount "may include items that are not included in your receipts (such as sales tax)". Model effect: keep sales tax and shipping as separate columns (done) so book revenue can be tied to a 1099-K; count per platform (`m10b`); keep the books complete even at zero 1099-Ks.

**Florida sales tax.**
- VERIFIED (FDOR, `floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx`): businesses selling taxable goods in Florida must register and collect sales tax; "marketplace providers are required to electronically register to collect and electronically remit sales and use tax on taxable sales they facilitate for marketplace sellers for delivery into Florida" (effective 2021-07-01); the return must not include tax collected in gross sales; discretionary surtax is reported by county on the back of the return.
- VERIFIED: **Etsy** "automatically calculates, collects, and remits" and lists Florida "as of 07/01/2021"; "Sellers can't opt out" (`data-etsy-sales-tax.md`). **eBay** lists Florida among its collect-and-remit jurisdictions (`data-ebay-tax-info.md`; the page's own jurisdiction count is dated 2021).
- VERIFIED (FDOR surtax page, `data-fl-surtax.md`): surtax is collected when delivery is made into a county that imposes one; rates run 0.5% to 2%; it "applies to the first $5,000 of the sales amount" of an item of tangible personal property.
- **Shopify own-site: Ricky is the dealer.** He must register with FDOR and collect state tax plus the surtax for the delivery county. That Shopify is not a marketplace facilitator comes from TaxJar only (**V-secondary**, `data-taxjar-fl-mf.md`: software that lets sellers build their own store "would not be considered a marketplace facilitator"); the FDOR page does not name Shopify. TaxJar also says a registered seller who sells only through collecting marketplaces may still have to file (possibly zero) returns: **V-secondary**.
- Model effect: `sales.tax_collected_by` (marketplace / seller / none) so only `seller` rows count as a liability (`m10a`); `tax_breakdown` and `ship_to_county` for the county split; tax never inside revenue. How Shopify Tax exposes the county (title string vs zip lookup): **UNVERIFIED**.

**Cost of goods sold, cash basis.**
- VERIFIED (IRS Pub 334 (2025), `data-irs-p334.md`): a "small business taxpayer" (average annual gross receipts of $31 million or less over the 3 prior years, indexed) "can choose not to keep an inventory, but you must still use a method of accounting for inventory that clearly reflects income"; a method that "treats inventory as non-incidental material or supplies" is accepted. If inventory is kept, accrual applies and COGS is Schedule C Part III lines 35 to 42: opening inventory + "purchases less cost of items withdrawn for personal use" + labor + materials + other costs - closing inventory. Donated inventory has its own basis rule. Pub 538 (Rev. 01/2022) states the threshold as $26 million (older); cite Pub 334.
- Pub 538 also names **specific identification** ("when you can identify and match the actual cost to the items in inventory") as a cost method. For quantity-1 pieces that is the natural fit.
- **UNVERIFIED:** in which year the non-incidental-supplies treatment lets a small business deduct inventory cost (when bought vs when sold). No page I read says. Ask the CPA. Do not read `m7b` as the answer.
- Model effect (holds under any answer): a cost per item (`cost_purchase`, plus `cost_other` for freight-in, repair, frame), `acquired_on`, `sold_at`, and `withdrawn_on` + `withdrawn_reason` (personal use and donation leave the P&L; loss does not). `m7` is the COGS-at-sale view, `m7b` the money-out view; both come from the same rows. Genie and Flipwise both offer a cash/accrual switch, which confirms the need for a per-item acquisition date and cost.

---

## 5. Discrepancies (X verified, Y need review)

| Item | Verified | Needs review |
|---|---|---|
| eBay fee base | Seller Center text + 4 worked examples + Finances spec `feeBasisAmount` ("includes ... eBayCollectedTaxAmount, and shipping charges") all include sales tax | Fulfillment spec `totalFeeBasisAmount` says "item cost + shipping cost". Use the API number when present; the estimator uses B with tax |
| Etsy processing-fee base | processing article: "including its shipping fees, and any applicable sales tax" | the fees overview says tax counts "if you charge tax on the listing"; Etsy collects tax in Florida, so tax counts either way |
| Etsy offsite-ads base | cap $100, 15%/12% | fees overview: "on the order total"; offsite page: "on the amount you made from your sale before the advertising fee was applied" |
| Small-business threshold | Pub 334 (2025): $31M, indexed | Pub 538 (01/2022): $26M. Pub 538 is stale |
| eBay international fee | the fee exists (Seller Center FAQ) | 1.65% only on sellmath |
| Shopify not a marketplace facilitator | FDOR describes marketplace providers (Etsy and eBay behavior verified) | the Shopify statement is TaxJar only |
| eBay store break-even | store prices and 12.7% verified | break-even is my arithmetic |
| eBay jurisdictions count | Florida listed | page text still says "as of July 1, 2021 ... 46 jurisdictions" |
| Shopify plan price | $29 yearly seen today; $39 monthly in `02` | monthly price not re-seen today |
| Seller Center fee table vs full help page | the table lists the exceptions | full help page walled; sub-category exceptions unchecked |
| `etsy.com/legal/fees` | help-center articles read instead | the legal page returned nothing |
| Flipwise inventory feature page | `help.flipwise.app` definitions read | `flipwise.app/features/ebay-inventory-management` returned a stub |

---

## Recommendation

1. **Adopt the nine-table schema as is.** It is tested end to end: constraints, generated columns, the sold-alert trigger, RLS (owner, non-owner, ack-only, service-role writes), the out-of-order upsert, and every metric. Load `items` from the catalog first (SKU = catalog id), put the SKU on every listing, and set `fee_rule` when listing.
2. **Store API fees when available, estimate otherwise, and surface the gap.** eBay: `getOrders` plus `order_earnings` (per-order net, fee types, label costs). Etsy: receipts + payments + ledger. Shopify: GraphQL orders with `transactions.fees`. `m9` shows how many sales still run on estimates; replace estimates as soon as the first real sale on each channel shows the true numbers.
3. **First dashboard screen (six cards):** cash tied up and aging (`m4`, `m2`); 30-day sell-through (`m1`); profit by channel (`m3`); this month's P&L (`m7`); double-sale and unmatched-sale guards (`m8`, `m9`). Aging, cash tied up, cohort sell-through and the double-sale guard are not in any competitor definition I read.
4. **Price by channel, not by gut:** the section 3.4 table says an order of a $100 item plus $12 shipping costs about 3.4% in fees on Shopify Payments, 9.9% on Etsy (about 25% if an offsite ad is attributed) and 14.9% on eBay (more for magazines and jewelry). Use that to pick where each item is listed first.
5. **Tax:** register with FDOR before the Shopify site takes its first order; keep tax out of revenue (done); ask a CPA about the inventory method before year end and hand them `m7`, `m7b` and `m10`.
6. **Do not build:** a customers table, a bank feed, an income-tax estimator, repricing. The crosslister owns repricing; a bookkeeper owns the ledger.

## Open questions

1. Which eBay category will each magazine go in? 15.3% (Books & Magazines) vs 13.6% (e.g. a Collectibles paper category) is about a $0.50 difference on a $30 issue.
2. Etsy ledger: which `ledger_type` / `reference_type` values mark the 6.5% transaction fee, listing fees, offsite ads and label purchases? The spec does not enumerate them. One real sale answers it.
3. Does `Order.totalMarketplaceFee` include the promoted-listing ad fee and the international fee, and does `order_earnings` attribute `AD_FEE` to the order? Check on the first sale with an ad.
4. Is `OrderTransaction.fees` populated for a third-party gateway or only for Shopify Payments? If not, estimate and true-up from the bill.
5. What do `Order.sourceName` / `Order.app` hold for orders imported by Marketplace Connect or a sync app? Needed before enabling the own-store filter safely.
6. Etsy API Terms #25 ("for purposes of analytics") vs this dashboard: carried from `02` open question 1. If Etsy says no, the fallback is the manual order CSV (`tools-etsy-download-sold.md`) into `sales` with `channel = 'etsy'`.
7. Inventory timing for tax: when is non-incidental-supplies inventory deductible? And is the entity a sole proprietor or an LLC (affects who receives any 1099-K)?
8. What is the real Postgres major version of the Supabase project? `security_invoker` views need 15+.
9. eBay license reading: may a tombstone (`external_id`, `status`) survive the purge, or must the row go entirely? Worst case, the same listing can re-alert.
10. Will Ricky sell in person in the physical room? If yes, which reader's fees go in `fee_payment` for `in_person` (Shopify POS: 2.6% + 10c on Basic, verified; Square or other: not read)?
11. Does an Etsy discount reduce the 6.5% base? Does Shopify's 2.9% apply to tax and shipping? Both confirm on the first sale.
12. Pub 334's $31M figure is indexed yearly; the 2026 value was not read. Irrelevant at this scale, but the citation should be refreshed at filing time.

---

## Raw pages fetched for this note

All under `research/dashboard/raw/`. Walls and blanks are listed because they are findings.

| File | URL | Status |
|---|---|---|
| `data-ebay-sellercenter-fees.md` | https://www.ebay.com/sellercenter/selling/start-selling-on-ebay/seller-fees | full |
| `data-ebay-store-subs.md` | https://www.ebay.com/sellercenter/payments-and-fees/subscriptions-and-fees | full |
| `data-ebay-tax-info.md` | https://www.ebay.com/sellercenter/resources/tax-information | full |
| `data-ebay-selling-fees.md`, `data-ebay-fees-fr.md`, `data-ebay-fees-mp.md` | https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822 and two URL variants | captcha wall (WebFetch also walled) |
| `data-sellmath-ebay-fvf.md` | https://sellmath.com/en/guide/ebay-final-value-fees-by-category | V-secondary |
| `data-etsy-help-fees.md` | https://help.etsy.com/hc/en-us/articles/115014483627 | full |
| `data-etsy-processing-fees.md` | https://help.etsy.com/hc/en-us/articles/115015628847 | full |
| `data-etsy-offsite-ads.md` | https://help.etsy.com/hc/en-us/articles/360000338367 | full |
| `data-etsy-sales-tax.md` | https://help.etsy.com/hc/en-us/articles/360000343968 | full |
| `data-etsy-legal-fees.md` | https://www.etsy.com/legal/fees/ | blank (removed) |
| `data-shopify-pricing.md` | https://www.shopify.com/pricing | full |
| `data-shopify-3p-fees.md` | https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/third-party-transaction-fees | full |
| `data-shopify-gql-order.md`, `-lineitem.md`, `-ordertransaction.md`, `-transactionfee.md`, `-product.md` | https://shopify.dev/docs/api/admin-graphql/latest/objects/ (Order, LineItem, OrderTransaction, TransactionFee, Product) | full (2026-10) |
| `data-irs-1099k.md`, `data-irs-1099k-faq-obbb.md` | https://www.irs.gov/businesses/understanding-your-form-1099-k ; https://www.irs.gov/newsroom/irs-issues-faqs-on-form-1099-k-threshold-under-the-one-big-beautiful-bill-dollar-limit-reverts-to-20000 | full |
| `data-irs-p334.md`, `data-irs-p538.md` | https://www.irs.gov/publications/p334 (2025) ; /p538 (01/2022) | full |
| `data-fl-sales-tax.md`, `data-fl-surtax.md` | https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx ; /discretionary.aspx | full |
| `data-fl-tip-21a01-03.md`, `data-fl-mf-guidance-newsletter.md` | FDOR TIP 21A01-03 PDF; a law-firm newsletter PDF | blank (removed) |
| `data-taxjar-fl-mf.md` | https://www.taxjar.com/blog/05-21-florida-marketplace-facilitator-law | V-secondary |
| `data-supabase-rls.md`, `data-supabase-jwts.md` | https://supabase.com/docs/guides/database/postgres/row-level-security ; /auth/jwts | full |
| `data-flipwise-metric-defs.md` | https://help.flipwise.app/article/55-sales-insights-metrics-definitions | full |
| `data-flipwise-inventory.md` | https://flipwise.app/features/ebay-inventory-management | blank (removed) |
| `data-genie-sales-analytics.md`, `data-genie-taxes.md`, `data-genie-sellthrough.md` | https://www.myresellergenie.com/salesanalytics ; /taxes ; support article 16138855676955 | full |
| `data-vendoo-analytics-help.md`, `data-vendoo-profit-calc.md`, `data-vendoo-analytics-page.md` | https://help.vendoo.co/en/articles/6260264 ; /6260293 ; https://www.vendoo.co/reselling-analytics | full |

Re-read from wave-1 (fetched earlier today): `ebay-spec-fulfillment_api.json`, `ebay-spec-finances_api.json`, `ebay-spec-browse_api.json`, `ebay-trading-getmyebayselling.md`, `etsy-shopify-etsy-openapi.json`, `etsy-shopify-shopify-webhooks-*.md`, `tools-flipwise-home.md`, `tools-genie-*.md`.
