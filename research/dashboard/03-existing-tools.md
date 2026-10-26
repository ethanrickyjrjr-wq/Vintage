# Existing tools: buy vs build for the Hollywood and Vine dashboard

Date: 2026-10-26. Author: research agent (Sonnet 5.5). Scope: commercial reseller tools, open-source projects, what resellers say, and a buy-vs-build matrix. Nothing was built.

Tags used on every claim:
- **[V]** read today (2026-10-26) on the cited page, by crawl4ai or the GitHub API.
- **[V-WF]** read today through the WebFetch tool, which returns a model-written summary of the page, so treat quotes as paraphrase-grade.
- **[U]** unverified: secondhand, a vendor claim not corroborated, a page that would not load, or an absence I could not prove.

Raw pages are in `research/dashboard/raw/tools-*.md` (listed at the end).

---

## 0. Read this first

1. **The test that matters is not "does it crosslist".** Ricky sells one-of-a-kind (qty 1) items on Etsy, eBay and Shopify. The question is: does the tool detect a sale on all three channels, delist the other two, and how late is it? The field splits on that (table 1.2).
2. **Three tools state a sale-detection latency for Etsy + eBay + Shopify: Crosslist and LitCommerce say 15 minutes, FLUF says 60 to 90.** Crosslist is the best documented: "Sales can take up to 15 minutes to be detected"; eBay, Etsy, Shopify are tracked on its servers, no browser needed; autodelist needs the Gold ($39.99) or Diamond ($44.99) plan. LitCommerce ($29) states 15-minute inventory sync and order import but assumes a Shopify store as the master. [V] https://docs.crosslist.com/knowledge-base/sales/sales-tracking and https://docs.crosslist.com/knowledge-base/sales/autodelist
3. **Vendoo is the cheapest of the established crosslisters (Vendoo / List Perfectly / Crosslist), but its published auto-delist list omits Shopify.** "Available for Poshmark, eBay, Mercari, Depop, Whatnot, and Etsy." Shopify appears only as a crosslist target. Shopify is absent from the detection list; whether a Shopify sale triggers a delist is unconfirmed (open question 2). Cheaper still: FLUF Starter $9, and the free tiers of Sellbrite (under 30 orders) and Flipwise (eBay only, up to 24 listings). [V] https://www.vendoo.co/cross-listing-app and https://www.vendoo.co/pricing
4. **FLUF Connect is the only reseller crosslister found with an API, MCP and webhooks** (Pro: read-only API; Priority, custom price: read+write+webhooks), and it covers Etsy, eBay, Shopify. Two inventory/multichannel tools also have APIs: Sellbrite (REST API, verified) and Zoho Inventory (APIs and webhooks listed), but neither is a crosslister built for resale. But it checks for sales only every 60 to 90 minutes, which is the double-sell window for a one-of-a-kind shop. [V] https://fluf.io/pricing
5. **Nobody sells what Ricky called the real gap: sourcing alerts by free-text description plus price range across sites.** Closest are Swoopa ($47/mo, vehicle-leaning), Crawlbench (Facebook only) and a brand-new open-source project, FlipWatch (11 days old, 5 stars). See section 4.
6. **Platform webhooks make the sync tool's API unnecessary for a sold-alert feed.** Etsy and Shopify both push webhooks (verified in sibling doc `research/dashboard/02-etsy-shopify.md`). The sync tool is the write path (list, delist); the dashboard can read straight from the platforms. Buying a tool with no API (Crosslist, Vendoo) does not block a custom dashboard.
7. **Scale check.** `research/inventory/2026-10-26-catalog.md` has about 39 catalogued rows (some are multi-item groups). That is a launch inventory of roughly 30 to 60 listings. Several free tiers may fit as-is (section 1.1).
8. **Dead or unusable:** inkFrog shut down 2026-06-01 (two sources). Zipsale is UK-only. OneShop's page is stamped 2024. Linnworks is quote-only enterprise.
9. **Reddit was unreadable** (old.reddit login-walled; WebFetch and WebSearch refuse reddit.com). Section 3 uses Trustpilot, Shopify App Store reviews, Capterra and reseller blog roundups instead, and cites Reddit only as secondhand quotes or titles.

---

## 1. Commercial tools

### 1.1 Comparison table

Prices are from each vendor's own page, read today, unless tagged otherwise. "Et / E / S" = Etsy / eBay / Shopify.

| Tool | Price per month | Et / E / S and detection | API, CSV, Zapier | Mobile app | Source |
|---|---|---|---|---|---|
| **Vendoo** | Starter $14.99, Growth $29.99, Pro $59.99 (monthly); $12.49 / $24.99 / $49.99 billed yearly. All unlimited items. Enterprise: contact sales. 14-day trial. [V] | Etsy yes, eBay yes, Shopify listed as a crosslist target but absent from the sale-detection list [V] | CSV inventory + sales export: yes, not in mobile app. Public API: none found [U]. Zapier: none found [U] | iOS + Android. Help page: "not yet available on the Vendoo mobile app: AI Descriptions, Bulk Delist/Relist, Sale Detection and Auto Delist, CSV Download, Stale Listing Warning System, Mercari, Facebook Marketplace, Sellwild and Shopify" [V] (says nothing about whether server-side delisting still runs) | https://www.vendoo.co/pricing , https://help.vendoo.co/en/articles/6260286-how-to-download-a-csv-file-of-your-inventory , https://help.vendoo.co/en/articles/9299090-can-i-use-vendoo-from-my-phone-or-tablet |
| **List Perfectly** | Simple $29, Business $49, Pro $69, Pro Plus $99+. [V] | Shopify integration only from Pro ($69). Auto Delist only on Pro Plus ($99+). [V] | CSV download + Sales Analytics from Business ($49). API/Zapier: none found [U] | "Mobile access ... on any browser"; no native app stated [V] | https://listperfectly.com/pricing |
| **Crosslist** | Bronze $29.99 (200 new listings/mo), Silver $34.99 (500), Gold $39.99 (1,000), Diamond $44.99 (unlimited); AI add-on +$4.99. 20 free listings, 3-day money-back. [V] | All three. Cloud sales tracking for eBay, Etsy, Shopify, up to 15 min. Shopify: first variant only. [V] | CSV import/export on Gold+. Sales analytics, cost of goods, estimated profit. No public API found [U] | Yes: "list, edit, and manage your inventory directly from your phone" [V] | https://crosslist.com/pricing , https://docs.crosslist.com/knowledge-base/sales/sales-tracking , https://docs.crosslist.com/knowledge-base/marketplaces/shopify/shopify-faq |
| **FLUF Connect** | Starter $9 ($85 first year), Pro $29 ($155 first year), Priority custom. FAQ instead says Starter $9 / Seller $29 / Pro $149 (conflict, section 5). 7 days for GBP 1. [V] | "70+ marketplaces" incl. Etsy, eBay, Shopify. Inventory sync on every plan. Sales checked every 90 min (Starter), 60 min (Pro). [V] | API + webhooks + MCP: Starter none, Pro read-only, Priority read+write+webhooks. [V] | iPhone + Android [V] | https://fluf.io/pricing , https://github.com/FLUF-io/fluf-mcp |
| **Flipwise** | By store size: 0-24 listings free; 25-99 $9.99; 100-499 $19.99; 500-999 $29.99; 1,000-1,999 $39.99; up to 10k-19.9k $69.99. 7-day money-back. [V] | **eBay only** [V] | No API or CSV export mentioned; imports from spreadsheet [V] | Not stated [U] | https://help.flipwise.app/article/95-how-much-does-flipwise-cost , https://flipwise.app/ |
| **My Reseller Genie** | Basic / Premium / Ultimate plans exist; **prices UNVERIFIED** (pricing page is images/JS). 14-day refund. | eBay + Etsy integrations; Vinted newly live; Mercari, Poshmark, Whatnot, Depop named in footer. Shopify not mentioned. [V] | No API/CSV/mobile stated [U] | Not stated [U] | https://www.myresellergenie.com/ , https://www.myresellergenie.com/pricing , https://support.myresellergenie.com/hc/en-us/articles/14825115256987-Daily-Use-Ultimate-Subscription |
| **Sellbrite** (GoDaddy) | Free under 30 orders/mo; Pro 100 $29; Pro 500 $79; Pro 2K $179 (third-party read of the vendor page dated 2026-09-29) [U]. Vendor help: "Paid plans starts at just $29 per month" [V]. Sellbrite for Shopify: Free (30 orders), $19, $59, $99 [U]. 14-day trial. | Amazon, BigCommerce, eBay, **Etsy**, Google Shopping, Newegg, Sears, **Shopify**, Walmart, WooCommerce [V]. Sync interval not read [U] | **REST API** at developer.sellbrite.com [V]; CSV inventory import/export listed [V] | Not stated [U] | https://support.sellbrite.com/en/articles/3367150-which-sellbrite-plan-is-right-for-me , https://www.sellbrite.com/pricing/ , https://developer.sellbrite.com/ , https://www.thegeeksclub.com/platforms/sellbrite/pricing/ |
| **LitCommerce** | Multichannel Listing "From $29/mo"; starts at 1,000 listings, unlimited orders, 3+ channels. 7-day trial. [V] | Shopify/Woo/BigCommerce stores; Etsy, eBay, TikTok Shop, Facebook and more. Inventory/price sync every 15 min, order import every 15 min. [V] | Bulk export/update, sales report [V]; API not read [U] | Not stated [U] | https://litcommerce.com/pricing/ |
| **3Dsellers** | Essential $19 ($16 yearly; 100 listings; 1 eBay account); Growth $39.90 ($29.90; 500 listings; 2 eBay accounts); Professional $79 ($59; 2,000+ listings; multichannel catalog). [V] | eBay-centric; nav lists "eBay to Etsy" and "eBay to Shopify" [V] | Nav lists Zapier, API, MCP integrations (docs not read) [U] | Not stated [U] | https://www.3dsellers.com/pricing |
| **Nifty** | Crosslisting Plus $39.99 ($35.99 yearly), Pro $59.99; Automation $39.99; Bundle Plus $69.99, Bundle Pro $89.99. 7-day trial. [V] | eBay, Etsy, Depop (API notices), Poshmark, Mercari. **Shopify: zero mentions** on pricing or home page [U] | Analytics + "tax-ready reports"; no API stated [V] | Not stated [U] | https://nifty.ai/pricing |
| **SellerAider** | Grow Standard $18, Grow Pro $25, Crosslister Standard $12.99, Crosslister Pro $29.99 (automatic delisting). 14-day trial. [V] | "15+ marketplaces"; **Shopify: zero mentions** on pricing page [U] | Inventory management; no API stated [V] | "Use on mobile" [V] | https://selleraider.com/pricing/ |
| **OneShop** | Premium $45/mo. Footer is 2024 and still lists Tradesy, so likely stale [U] | Poshmark, Mercari, Depop, Etsy, Kidizen named; eBay/Shopify not confirmed [U] | none stated | none stated | https://www.oneshop.com/pricing |
| **Zipsale** | From GBP 15/mo + VAT, or GBP 0.18 per item credits. **UK only.** [V] | Auto-delist for eBay, Etsy, Depop, Poshmark, Shopify, Woo, Asos, Vinted; not Facebook. Single-quantity items only. [V] | none stated | none stated | https://www.zipsale.co.uk/pricing |
| **inkFrog** | **Shut down 2026-06-01** (announced 2026-04-29, Wix-owned). [V] two sources | n/a | n/a | n/a | https://www.snaptolist.com/blog/inkfrog-shutting-down-june-2026 , https://www.3dsellers.com/blog/alternatives-to-inkfrog-shutting-down |
| **Linnworks** | Quote only, priced on order volume. Enterprise. [V] | 100+ channels | "Open API" developer portal [V] | n/a | https://www.linnworks.com/pricing/ |
| **Shopify Marketplace Connect** | Free to install; first 50 synced orders/mo free, then 1% per extra synced order, capped $99/mo. [V] | Amazon, Target Plus, eBay, Walmart. **No Etsy.** [V] | n/a | Shopify app | https://apps.shopify.com/marketplace-connect |
| **Zoho Inventory** | Free (50 orders/mo, 1 user); Standard $29 (500 orders, billed annually), Premium $79, Elite $129, Ultimate $249. [V] | Lists Etsy, eBay, Shopify, Amazon, Walmart, Woo. Whether the Free plan includes channels: [U] | Developer APIs, webhooks and custom functions listed [V] | not read | https://www.zoho.com/us/inventory/pricing/ |
| **Veeqo** (Amazon) | Free tier; paid from $19/mo by order volume; "Publish 10 free listings per month" on free. [V] | Amazon, Shopify, eBay, Walmart, Woo shown; Etsy not confirmed [U]. Shipping-first. | Rate-shopping API [V] | not read | https://www.veeqo.com/us/pricing |

Notes by tool (only what changes a decision):

- **Vendoo.** Starter at $14.99 already includes unlimited items, all marketplaces, sale detection + auto-delisting, importing, analytics and the mobile app. [V] The compare-plans list also names "Downloadable Inventory Spreadsheets" and "Profit Tracking & Business Analytics". [V] https://www.vendoo.co/pricing . Its Chrome extension fills listings in the browser, with an authorized token for eBay and Etsy. [V] https://underpricedai.com/blog/best-cross-listing-apps (competitor-authored, see bias note in section 3).
- **List Perfectly.** The cheapest plan that auto-delists is $99+. Below that, "Mark Sold" is manual (Pro) or absent (Business). [V] https://listperfectly.com/pricing . Poor fit for qty-1 inventory on price.
- **Crosslist.** Profit: each sale carries sale price, cost of goods, shipping expense and other expenses, producing estimated profit and margin. [V] https://docs.crosslist.com/knowledge-base/sales/sales-tracking . Caveat from the same page: "Crosslist can only track sales for listings that are linked in Crosslist". Chrome-extension marketplaces need the browser open; eBay, Etsy and Shopify do not. Autodelist table: eBay, Etsy, Shopify all "Cloud-based", "Multi-quantity", "Reduces quantity". [V] https://docs.crosslist.com/knowledge-base/sales/autodelist . A qty-1 item that sells reaches zero and is removed.
- **FLUF.** The `fluf-mcp` server exposes six tools and five recipes (`morning_sales`, `dead_stock`, ...) for Claude and other agents. [V] https://github.com/FLUF-io/fluf-mcp . Team seats are GBP 20/mo each; prices are shown in $ while the trial and seats are in GBP. [V]
- **Flipwise.** Strongest profit view for eBay only: fees, shipping label costs and refunds import on their own; cost and location are entered by you; instant sold + storage-location alert. Not a multichannel answer. [V] https://flipwise.app/
- **Sellbrite.** The only vendor here with a documented REST API *and* a free tier *and* Etsy + eBay + Shopify. Free-tier channel coverage and sync speed are unverified. A Capterra review dated 2026-10-12 reports "continuous problems with overselling" and support blaming the user or Etsy/eBay. [V] https://www.capterra.com/p/149384/Sellbrite/reviews/
- **Shopify Marketplace Connect.** 4.1 stars over 2,131 reviews, 15% one-star. One-star reviews dated 2026-09-06 to 09-12 say the eBay integration "ceased to work last month" and stayed broken. [V] https://apps.shopify.com/marketplace-connect/reviews?ratings%5B%5D=1 . No Etsy, so it cannot be the whole answer anyway.

### 1.2 Sale detection and delist on Ricky's three channels (the deciding table)

| Tool | Etsy sale detected? | eBay? | Shopify? | Lag | Cheapest plan that does it |
|---|---|---|---|---|---|
| Crosslist | yes, cloud | yes, cloud | yes, cloud | up to 15 min | Gold $39.99 [V] |
| Vendoo | yes | yes | **not listed** | not stated [U] | Starter $14.99 (Etsy/eBay only) [V] |
| List Perfectly | not stated per channel | not stated | Shopify integration from Pro | not stated | Pro Plus $99+ [V] |
| FLUF Connect | yes (inventory sync) | yes | yes | 60 to 90 min | Starter $9 [V] |
| Sellbrite | Etsy listed | yes | yes | not stated [U] | Free under 30 orders [U] |
| LitCommerce | yes | yes | yes (store side) | 15 min | $29 [V] |
| Nifty | yes | yes | **unknown** | not stated | Crosslisting Plus $39.99 [V] |

### 1.3 Native platform analytics (free, already there)

| Platform | Analytics and export | Alerts and mobile | Source |
|---|---|---|---|
| **eBay Seller Hub** | Performance and Reports tabs exist; CSV/XLSX reports and a Manage-orders download. Exact current menu paths [U] (eBay help pages are bot-walled to the crawler and to WebFetch; search snippets only). | eBay app push: "real-time push notifications ... orders, offers, and auctions" [V]. My eBay has Watchlist, Saved Searches, Saved Sellers [V]. | Push: https://pages.ebay.com/push-notifications/ . My eBay nav: https://www.ebay.com/sellercenter/selling/seller-hub-reports . Reports claims rest on search snippets only (help page https://www.ebay.com/help/selling/selling-tools/seller-hub?id=4095 is walled). |
| **Etsy Stats** | Shop Manager > Stats: Visits, Orders, Conversion rate, Revenue; data from November 2017; compare to previous year. CSV download of listings, orders, Etsy Payments sales and deposits (Settings > Options > Download Data). [V] | Etsy Seller app: manage orders, track shipments, add photos/video. Push notifications not stated on that page [U]. | https://help.etsy.com/hc/en-us/articles/115015774268-How-to-Use-Etsy-Stats-for-Your-Shop , https://help.etsy.com/hc/en-us/articles/360000343328-How-to-Download-a-Spreadsheet-of-Your-Sold-Transactions , https://www.etsy.com/sell-mobile |
| **Shopify Analytics** | Dashboard + Reports on all plans; export CSV, XML, JSONL, Parquet. [V] | Shopify app (iPhone, Android, Apple Watch): "Notifications let you know when a new order comes in". Staff email on new order. [V] | https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports , https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/custom-reports/export-reports , https://help.shopify.com/en/manual/shopify-admin/shopify-app , https://help.shopify.com/en/manual/fulfillment/setup/notifications/staff-notifications |

What the native stack does not give: one feed, one number. Three apps, three pings, three CSV schemas, and no cross-channel profit.

---

## 2. Open-source alternatives (GitHub, via `gh api`, 2026-10-26) [V]

### 2.1 General commerce platforms

| Repo | Stars | Last push | Lang | License (API) | Channel sync or inventory only? | Realistic effort |
|---|---|---|---|---|---|---|
| saleor/saleor | 23,480 | 2026-10-26 | Python | BSD-3-Clause | Storefront/OMS API. No Etsy/eBay sync read; an Etsy-Saleor connector exists by search title but its page did not load [U] | Weeks. You still build the channel layer. |
| medusajs/medusa | 36,953 | 2026-10-26 | TypeScript | NOASSERTION | Commerce engine. Community plugin `@jytextiles/medusa-plugin-etsy-sync` pushes Medusa products to one Etsy shop as drafts via Etsy Open API v3; one-way, no eBay [V] https://medusajs.com/integrations/@jytextilesmedusa-plugin-etsy-sync (plugin stars not checked) | Days to run; weeks to make it a reseller dashboard. Same stack family as Ricky's. |
| odoo/odoo | 55,344 | 2026-10-26 | Python | NOASSERTION | Native eBay connector reported **discontinued in v18** in an Odoo forum thread (user reports plus a reply that says the Belgium dev team stopped supporting it; not an official notice); paid third-party bridges remain [V] https://www.odoo.com/forum/help-1/ebay-connector-replacement-267902 | Heavy ERP. Overkill for 40 items. |
| frappe/erpnext | 40,634 | 2026-10-26 | Python | GPL-3.0 | `frappe/ecommerce_integrations` (211 stars, pushed 2026-10-23) supports Shopify, Unicommerce, Zenoti, Amazon. No eBay or Etsy. [V] | Heavy ERP, wrong channels. |
| vendurehq/vendure | 8,544 | 2026-10-26 | TypeScript | NOASSERTION | Headless commerce; no Etsy/eBay plugin found [U] | Same as Saleor. |
| bagisto/bagisto | 28,272 | 2026-10-23 | PHP | MIT | eBay connector is a **$199 paid extension** that syncs products, categories, orders [V] https://bagisto.com/en/extensions/laravel-ecommerce-ebay-connector/ | PHP/Laravel, off-stack. |
| OCA/connector-ecommerce | 52 | 2026-09-28 | Python | AGPL-3.0 | Odoo connector framework layer, not a channel | n/a |

Verdict: all six big platforms are active; none syncs Etsy + eBay + Shopify out of the box (per the pages read). They are shop engines, not reseller sync layers. Running one buys a storefront Ricky does not need, since Shopify is that.

### 2.2 Reseller-specific repos

| Repo | Stars | Last push | Lang | License | What it is | Fit |
|---|---|---|---|---|---|---|
| Crepe950/flipwatch | 5 | 2026-10-17 (created 2026-10-15) | TypeScript | MIT | Saved searches (keywords, price range, area) across Craigslist, Kijiji, eBay, OfferUp, optional Facebook; alerts via Discord, Telegram, Slack, ntfy, email, browser push; AI deal scoring (Claude/OpenAI); flip tracker. Next.js 16, React 19, Tailwind 4, Drizzle on PGlite or Postgres. Runs on 127.0.0.1; phone access via Tailscale. README says the Facebook path "is against Meta's Terms of Service". | Closest thing to the sourcing-alert gap and on Ricky's stack. 11 days old, 5 stars: a reference, not a dependency. |
| BoPeng/ai-marketplace-monitor | 395 | 2026-10-26 | HTML (label) | AGPL-3.0 | Facebook Marketplace only; keyword/price/location rules; AI rating; Pushbullet/Pushover/Telegram/ntfy. Needs FB login + Playwright; its own legal notice says FB terms prohibit automated collection. | Facebook-only, ToS risk. |
| ChrisKariofyllis/BayRadar | 1 | 2026-10-20 | TypeScript | NOASSERTION (README badge says GPLv3) | eBay-only deal radar: monitors, scam/box filters, AI title gatekeeper, ntfy/Telegram/Discord/Gotify, Gixen sniping. Next.js + SQLite + Docker. | Good design reference for eBay-side alerts. |
| quangshuynh/flipper | 7 | 2026-10-16 | Python | MIT | Local-first research + inventory + eBay reconciliation + realized-profit tracker. | Reference for COGS/profit modelling. |
| And1zle/eBayOS | 2 | 2026-04-12 | TypeScript | MIT | "Multi-platform seller dashboard"; crosslists to Poshmark/eBay/Facebook via Chrome extension. | Not Etsy/Shopify. |
| GasWhatWeSmoke/BlackCatReseller | 0 | 2026-10-16 | TypeScript | MIT | Windows desktop beta: inventory + crosslisting + sales for clothing. | Desktop only. |
| FLUF-io/fluf-mcp | 1 | 2026-09-27 | TypeScript | MIT | MCP client for the commercial FLUF Connect API. | Only useful if FLUF is bought. |
| JakobAIOdev/Vintrack-Vinted-Monitor | 194 | 2026-10-25 | TypeScript | MIT | Vinted monitor, Discord alerts, dashboard. | Wrong marketplace. |
| passivebot/facebook-marketplace-scraper | 404 | 2024-04-29 | Python | none | Archived. | Dead. |
| Poshmark bots (pikachu/poshmarkBot 12, posh-a-matic 4, others) | 0 to 12 | 2016 to 2026 | various | various | Share/follow bots. | Not relevant to Etsy/eBay/Shopify. |
| FLUF-io/awesome-reseller-tools | 9 | 2026-10-19 | n/a | n/a | Curated list. **Published by FLUF, a vendor, so treat as biased.** [V] https://github.com/FLUF-io/awesome-reseller-tools | Landscape only. |

Searches for open-source multi-channel *crosslisters* ("crosslist", "crosslister", "reseller inventory ebay", "ebay etsy sync inventory") returned only one-to-two-star hobby repos (for example `ridwan-salau/crosslister-ebay`, 1 star, a Chrome extension). No credible open-source Etsy + eBay + Shopify sync turned up. [V as a negative search result today, not proof of absence]

---

## 3. What resellers say (2025 to 2026)

**Access note.** Reddit r/Flipping, r/reselling, r/EtsySellers, r/eBaySellers: old.reddit.com returned a login wall, WebFetch refuses reddit.com, WebSearch refuses reddit.com, and I did not try to get around that. Thread bodies were **not read**. Thread titles surfaced by the search script (titles only, content unread [U]):
- "Cross listing Apps for resellers" (r/reselling) https://www.reddit.com/r/reselling/comments/1uuygal/cross_listing_apps_for_resellers/
- "What crosslisting software do large resellers use besides Vendoo?" https://www.reddit.com/r/reselling/comments/1rkszog/what_crosslisting_software_do_large_resellers_use/
- "how are you guys actually tracking your profit??" (r/Flipping) https://www.reddit.com/r/Flipping/comments/1uvtbog/how_are_you_guys_actually_tracking_your_profit/
- "How are you tracking inventory & profit once things start scaling?" https://www.reddit.com/r/reselling/comments/1pmqn1x/how_are_you_tracking_inventory_profit_once_things/
- "Is there no way to save a search and get alerts from FB Marketplace??!" https://www.reddit.com/r/Flipping/comments/bjhufo/is_there_no_way_to_save_a_search_and_get_alerts/

**Secondhand Reddit content (from vendor-authored articles):**
- A Reddit user (2026-07-13) quoted in a Nifty article: "Nifty didn't really sync well sometimes; not always, but enough to get me annoyed at times. They also have limited marketplaces ... and quite expensive". [V that the article says it; the Reddit post itself unread] https://nifty.ai/post/best-inventory-software-for-ebay
- ScrapeCreators (an API vendor) describes a public Reddit thread where Facebook's built-in alert "was too slow and good deals were sold before the notification arrived". [V that the article says it] https://scrapecreators.com/blog/facebook-marketplace-alerts

**Direct user reviews read today:**
- **Vendoo, Trustpilot: 4.2 over 251 reviews** [V-WF] https://www.trustpilot.com/review/vendoo.co . Recent complaints: 2026-10-15 "not detecting a sale and me double selling it"; 2026-10-24 "often having to reconnect depop and mercari due to it disconnecting randomly"; 2026-09-05 "so often it is not able to correctly pull items from eBay"; 2026-09-25 add-ons paywall imports after upgrade; 2026-10-06 "Trying to find the chat button is almost impossible now". Praise: auto delist "helps prevent selling the same item on two different platforms" (2026-10-03).
- **Crosslist, Trustpilot: 4.5 over 1,134 reviews** [V-WF] https://www.trustpilot.com/review/crosslist.com . 2026-10-12 "the auto delist does not delist from other platforms leading to double item sales"; 2026-09-03 paid for AI + auto-delisting and "it says i don't have it"; a billing dispute over a $4.99 fee (Crosslist publicly disputes it). Etsy and Shopify are not mentioned in the visible reviews. This contradicts Crosslist's docs on cloud detection; one review is not a measurement.
- **Shopify Marketplace Connect, Shopify App Store: 4.1 over 2,131** [V]; September 2026 one-star reviews: eBay integration broken for more than a month; "Screws up prices and inventory". **Sellbrite for Shopify: 3.9 over 120, 16% one-star** [V] https://apps.shopify.com/sellbrite/reviews?ratings%5B%5D=1
- **Sellbrite, Capterra** (2026-10-12): overselling despite a full inventory count, support deflecting. [V] https://www.capterra.com/p/149384/Sellbrite/reviews/
- **My Reseller Genie review** (undated; images from March 2022 [U]): "difficult to upload existing inventory if you do not have excel", no sourcing-location field, other expenses entered manually. [V-WF] https://theecommercemom.com/my-reseller-genie-review/

**Recurring complaints (my synthesis; each bullet has a source above):**
1. **Missed sale, then a double sale.** The cardinal sin for qty-1 inventory. Appears for Vendoo, Crosslist, Sellbrite.
2. **Random disconnects and failed pulls** from eBay, Depop, Mercari; the Shopify eBay app broke for a month.
3. **Paywalled essentials and billing friction:** imports, bulk delist, auto-delist and "all marketplaces" gated by tier or add-on; refund disputes.
4. **Browser-extension dependence** for non-API marketplaces (Facebook, Poshmark, Mercari): the browser must stay open. Not an issue for eBay, Etsy, Shopify on Crosslist (cloud).
5. **Support is hard to reach.**
6. **Profit is only as good as the manually entered cost.** Even Flipwise: "You add only what eBay can't see: your cost, where you bought it, and where it's located." The spreadsheet route is alive: a $14 one-time Excel/Google Sheets "Reseller Tracker 2026" computes net profit after fees, shipping and COGS per platform incl. Etsy and eBay [V] https://quirepaper.com/reseller-tracker/
7. **Facebook Marketplace alerts are slow or flaky**; no API exists.

**What's missing (per these sources):** sourcing alerts that cover more than one site with a free-text rule; a single real-time sold feed; published per-sale latency (only Crosslist, FLUF and LitCommerce state one).

**Bias and staleness warnings.**
- Roundups from tool vendors (Underpriced AI, Nifty, ScrapeCreators, FLUF's awesome-list) are marketing.
- Two third-party roundups carry **wrong or stale prices** for Vendoo and List Perfectly (section 5). Do not copy numbers from roundups.
- Underpriced AI's phrase "Crosslist ... API-first" means Crosslist uses the marketplaces' APIs. It does not mean Crosslist offers Ricky an API. [V] https://underpricedai.com/blog/best-cross-listing-apps

---

## 4. Buy-vs-build matrix

| Capability | Cheapest adequate option | Why, and the catch | Build? |
|---|---|---|---|
| **Crosslist** (create once, post to Etsy / eBay / Shopify) | **Buy.** FLUF Starter $9, Vendoo Starter $14.99, or Crosslist Gold $39.99. Sellbrite Free if orders stay under 30/mo [U]. | All are small against a ~40-item launch. Vendoo is cheapest but misses Shopify delist; Crosslist is dearest but documents the full path. | No |
| **Inventory truth** (one record, no double-sell) | **Buy.** Crosslist Gold (15 min, cloud, all three channels) is the documented option. FLUF Starter/Pro is cheaper but polls every 60 to 90 min. | For a qty-1 shop the tool's catalog is the truth. A Supabase `items` table is only a read copy for the dashboard. Crosslist only tracks linked listings. | Only a read copy |
| **Sales rollup** (all channels, one number) | **Native + buy.** Each platform's own Stats/Analytics/Seller Hub for free; Crosslist/Vendoo analytics for a combined view. | Three native dashboards do not combine. Crosslist/Vendoo give one rollup inside their app, no API. For a custom page, read each platform's API/webhooks directly. | Optional (one page) |
| **Profit / COGS** | **Buy.** Crosslist sales tracking (cost of goods per item, estimated profit and margin) or Vendoo Starter analytics. Flipwise if eBay-only. | Everyone needs cost entered by hand. Decide where cost lives once. A Supabase `cost` column also works and is the only way to have profit inside a custom dashboard. | Small (a column) |
| **Sourcing / buy alerts** (description + price range) | **Build**, with native alerts as a stopgap (Facebook "Notify Me" free; eBay saved searches). | The gap: see below. | **Yes** |
| **Sold alerts** (phone, real time) | **Native** apps are free (eBay push, Shopify app, Etsy Seller app [push unverified]). Unified feed: **build** on platform webhooks (Etsy and Shopify verified in `02-etsy-shopify.md`). | Tool pollers lag 15 to 90 min, so even a paid API is slower than the platforms' own webhooks. FLUF webhooks are on custom-priced Priority only. | Yes, thin |
| **Mobile** | **Native** apps (eBay, Etsy Seller, Shopify) plus the sync tool's app (Crosslist, Vendoo, FLUF). For the custom dashboard, a PWA on Vercel. | Vendoo's app lacks sale detection, auto-delist, CSV and Shopify. List Perfectly is browser-only. | PWA only |

### The gap no product fills well

**Cross-site sourcing alerts with a custom description and a price range.** What exists, and why it falls short:
- **Facebook "Notify Me"**: free; created in the mobile app per search with location, radius, optional price range. No timing control; users report delays (anecdote, not measured). [V] https://dealhunter.io/blog/facebook-marketplace-alerts (vendor-authored)
- **eBay saved searches**: email alerts, reportedly a daily digest. [U] eBay community replies via search snippet; eBay help pages walled. Saved Searches exist in My eBay [V].
- **Swoopa**: monitors Facebook Marketplace, Craigslist, OfferUp, Kijiji, Gumtree, Nextdoor, eBay; basic Go plan $47/mo month-to-month ($28 with a 12-month term); "leans heavily toward vehicle sourcing". [V that the ScrapeCreators article says so; the vendor pricing page failed to load] https://scrapecreators.com/blog/facebook-marketplace-alerts
- **Crawlbench**: Facebook Marketplace alert + price-check app, with a "Resellers: Furniture, electronics, tools and more" page; price not read. [V] https://crawlbench.com/
- **Estate-sale and auction sources** (where a vintage shop actually buys): Invaluable has saved-search and keyword/artist alerts; Catawiki emails weekly. [V-WF, from search snippets] LiveAuctioneers, EstateSales.net and AuctionZip alert features are **not confirmed**. [U]
- **Open source**: FlipWatch (closest, 11 days old), AI Marketplace Monitor (Facebook only, ToS risk), BayRadar (eBay only).
- **Legal/ToS**: Facebook has no Marketplace API. Every Facebook path scrapes a logged-in session, which FlipWatch's and AIMM's own READMEs say violates Meta's terms. The defensible build is eBay Browse API plus sources that publish feeds or APIs (see the sibling sourcing research, not restated here).

A custom build is also where the shop's vocabulary lives: "Stiffel-style brass lamp under $80", "1970s Playboy under $25", "Chanel coffee-table book", "Vitra Gehry cardboard chair" are descriptions, not SKUs. No product found matches free text plus per-rule price caps across eBay, estate-sale and auction sites.

### Could the whole dashboard be a paid tool plus a thin custom layer?

Yes for most of it. Honestly:
- **Paid tool covers:** crosslisting, delist, inventory truth, sales rollup inside its UI, profit per sale, mobile listing. $9 to $40/month.
- **Free native apps cover:** per-channel sold pings.
- **The thin custom layer is two things:** (1) a unified sold feed + simple sales/profit page, fed by platform webhooks into Supabase and pushed to a PWA; (2) sourcing alerts. Everything else on the original wish list is buyable.
- **What not to build:** a crosslister, a delist engine, a general inventory system.
- The sold feed is a convenience, not a necessity: three native pings already exist. Sourcing alerts are the only true product gap.

---

## 5. Discrepancies (X verified, Y need review)

Verified: vendor-page prices for Vendoo, List Perfectly, Crosslist, FLUF, Flipwise, Nifty, SellerAider, 3Dsellers, Zoho, Shopify Marketplace Connect, LitCommerce; Crosslist cloud detection and the 15-minute figure; inkFrog shutdown (two sources); GitHub stats (API today).

Need review:
1. **Vendoo plans.** Vendor page and Underpriced AI (2026-10-13) agree: Starter $14.99 / Growth $29.99 / Pro $59.99, unlimited items. thriftflipping.com (2026-08-15) lists Free / Starter $8.99 / Simple $19.99 / Plus $29.99 / Pro $49.99 / Advanced $99.99 / Expert $149.99, quota-based, with $4.99 add-ons. The Underpriced showdown (2026-10-01) lists Growth $19.99 / Business $29.99 / Enterprise $49.99 / Boss $89.99. The two roundups disagree with the vendor and with each other. Treat them as stale. https://thriftflipping.com/blog/article-167-vendoo-pricing-2026-real-cost.html , https://www.underpriced.app/blog/crosslisting-software-showdown-list-perfectly-vendoo-2026
2. **List Perfectly.** Vendor: Simple $29 / Business $49 / Pro $69 / Pro Plus $99+, unlimited listings. Underpriced showdown: Business $59, Pro $89, Simple "150 active listings". Vendor wins.
3. **FLUF page contradicts itself.** Table: Starter $9 / Pro $29 / Priority custom. FAQ: Starter $9 / Seller $29 / Pro $149 / Priority custom. Currency mixed ($ vs GBP). Confirm at checkout before relying on a "Pro" tier having API access.
4. **Sellbrite prices** come from a third-party page citing the vendor's page on 2026-09-29; the vendor chooser page did not render numbers; vendor help says paid from $29, the third party says Sellbrite for Shopify from $19.
5. **Crosslist auto-delist:** docs say cloud-based and Gold+; a 2026-10-12 Trustpilot review says it "does not delist from other platforms". Unreconciled.
6. **BayRadar license:** README badge says GPLv3; the GitHub API reports NOASSERTION.
7. **Odoo, Medusa, Vendure licenses:** API reports NOASSERTION; not resolved here.
8. **My Reseller Genie prices:** not readable. Unverified; not filled from memory.
9. **Vendoo API:** a SoftwareSuggest listing mentions "Api Access" (aggregator, no detail); no developer docs found. Treated as no public API. [U]
10. **Zapier:** `zapier.com/apps/vendoo|list-perfectly|crosslist/integrations` returned 404. Those were guessed slugs, so this shows "no Zapier app at that slug", not "no Zapier integration".

---

## Recommendation

1. **Buy the write path; do not build it.** Trial **Crosslist** first (20 free listings, 3-day money-back; Gold at $39.99 is the plan that auto-delists and exports CSV). It is the one option whose docs state cloud sale detection on eBay + Etsy + Shopify within 15 minutes, with cost-of-goods profit and a phone app. Cheaper option to test in parallel: **FLUF Starter** ($9, 7 days for GBP 1), accepting 90-minute polling. Skip List Perfectly (auto-delist at $99+). Vendoo Starter at $14.99 is the budget pick for Etsy + eBay only; skip it if Shopify auto-delist matters on day one.
2. **Build the read path and the gap, thin.** One Supabase project: an `items` table (id, cost, status), an `events` table fed by Etsy and Shopify webhooks (eBay per the sibling doc), Realtime to a PWA on Vercel, and a `watch_rules` table (description, price cap, source) with a cron poller for alerts. This does not need the sync tool's API at all.
3. **Sourcing alerts: build, starting with the eBay Browse API**, with native Facebook "Notify Me" as a free stopgap. Read FlipWatch's `src/lib/marketplaces/<id>/` adapter layout and BayRadar's monitor model as design references. Do not depend on an 11-day-old repo, and do not build a Facebook scraper on Ricky's real account.
4. **Shopify-master alternative.** LitCommerce ($29, 15-minute sync, Etsy + eBay) and Sellbrite for Shopify assume Shopify is the source of truth, so they need a paid Shopify plan (Basic is $39/mo or $29 yearly per `02-etsy-shopify.md` section 10). Crosslist needs no master store. If Shopify is live on day one, LitCommerce undercuts Crosslist Gold on price; if "own site later", Crosslist or FLUF avoids paying for Shopify early. The sibling doc `02-etsy-shopify.md` (section 9 and Recommendation) reaches the same rule: pay for none until a quantity-1 delist-latency test passes on a real item. This doc and that one do not conflict; both defer the pick to that test.
5. **Do not self-host Saleor, Medusa, Odoo, ERPNext, Vendure or Bagisto.** None solves channel sync for his three channels and each adds an ops burden.

## Open questions

1. Does Sellbrite's free tier (under 30 orders/mo) include Etsy, eBay and Shopify channels, and what is its sync interval? Trial it or read its help centre.
2. Does Vendoo detect Shopify sales at all, even though its auto-delist list omits Shopify? Check Vendoo's Shopify help article.
3. Which List Perfectly plan really auto-delists, and what do recent List Perfectly reviews say? (Its Trustpilot URL returned 404; not read.)
4. FLUF's actual plan names and prices (table vs FAQ), and whether Pro's read-only API exposes sales and inventory or only listings.
5. Reddit thread bodies (section 3) are unread. Ricky could paste the two or three he trusts.
6. eBay Seller Hub report details and saved-search alert cadence (eBay help is bot-walled): confirm from inside a logged-in seller account.
7. Do LiveAuctioneers, EstateSales.net, AuctionZip or Chairish offer saved-search alerts or feeds? This decides how wide the sourcing build can be.
8. Expected order volume per month. Under about 30 orders changes which free tiers apply.
9. Does Ricky need auto-delist across all channels instantly (platform webhooks plus a custom delister) or is 15 minutes acceptable for qty-1 items?
10. My Reseller Genie prices, and whether its eBay/Etsy sync gives item-level COGS (bookkeeping vs inventory focus).

---

## Raw pages fetched (research/dashboard/raw/)

All files are `tools-<slug>.md`.

- **Vendoo:** vendoo-pricing, vendoo-sale-detection, vendoo-marketplaces-help, vendoo-csv-help, vendoo-mobile-help.
- **List Perfectly / Crosslist:** listperfectly-pricing, crosslist-pricing, crosslist-docs, crosslist-marketplaces, crosslist-shopify-faq, crosslist-autodelist, crosslist-sales-tracking.
- **Others:** flipwise-home, flipwise-cost, genie-pricing, genie-home, genie-ultimate-help, sellbrite-pricing, sellbrite-plan-help, sellbrite-geeks, sellbrite-api, litcommerce-pricing, 3dsellers-pricing, nifty-pricing, nifty-home, selleraider-pricing, oneshop-pricing, zipsale-uk-pricing, zipsale-help-sync, linnworks-pricing, fluf-pricing, shopify-mc, veeqo-pricing, zoho-inventory-pricing, zapier-vendoo, zapier-listperfectly, zapier-crosslist (the three Zapier files are 404 pages).
- **Native:** ebay-pages-push, ebay-sellerhub-seller-center, ebay-sc-reports, ebay-export-sellerhub-reports, ebay-sellerhub, ebay-sellerhub-reports, ebay-push-notifs (the last three are bot-wall pages), etsy-stats, etsy-download-sold, etsy-sell-mobile, shopify-export-reports, shopify-staff-notifs, shopify-analytics-overview, shopify-app-help.
- **Open source:** gh-awesome-reseller-tools, gh-Crepe950-flipwatch-README, gh-ChrisKariofyllis-BayRadar-README, gh-And1zle-eBayOS-README, gh-quangshuynh-flipper-README, gh-GasWhatWeSmoke-BlackCatReseller-README, gh-frappe-ecommerce_integrations-README, gh-FLUF-io-fluf-mcp-README, odoo-ebay-forum, odoo-ebay-docs, medusa-etsy-plugin, bagisto-ebay-ext.
- **Reseller opinion and sourcing:** rd-underpriced-showdown, rd-underpricedai-best, rd-thriftflipping-vendoo, rd-nifty-inventory-ebay, rd-shopify-mc-reviews, rd-sellbrite-shopify-reviews, rd-capterra-sellbrite, rd-quirepaper-tracker, rd-scrapecreators-fb-alerts, rd-dealhunter-fb-alerts, src-crawlbench, src-ai-marketplace-monitor-readme, inkfrog-shutdown, inkfrog-3dsellers.
- **WebFetch only (no raw file):** Trustpilot Vendoo, Trustpilot Crosslist, theecommercemom Genie review, and web searches on eBay Seller Hub reports, eBay saved-search alerts, auction-site alerts, Vendoo API/export, List Perfectly Zapier/API.
- **Deleted as empty or bot-wall stubs (my own files only):** eight `tools-reddit-*` old.reddit login walls; `tools-etsy-stats-help.md` and `tools-etsy-stats-real.md` (wrong article); `tools-lp-marketplaces.md` (no content); `tools-apiworx-etsy-saleor.md`, `tools-flipwise-pricing.md`, `tools-inkfrog-pricing.md`, `tools-rd-trustpilot-{crosslist,listperfectly,vendoo}.md`, `tools-src-swoopa-pricing.md`, `tools-vendoo-itqlick.md`, `tools-zipsale-pricing.md`.
