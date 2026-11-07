# Gaps 09: Inventory, bookkeeping, mileage and tax tools the first lane missed

Date 2026-11-07. Author: research subagent (completeness critic for lane 09-inventory-books-tax).
Question: Which inventory, cost-basis, profit, expense, mileage and tax tools for a one-person vintage reseller in Florida are missing from the lane 09 list, and what do they cost?
Legend: V = vendor, app-store or government page read today (2026-11-07) with the session's fetch.sh headless browser or curl; U = unverified (snippet, catalog row, memory, or the page would not load).

Method note. WebSearch's shared per-turn budget was already used up when this agent started, so no web searches were made. Leads came from vendor catalog pages read directly: Apple's App Store search API (itunes.apple.com/search, nine queries), the Shopify App Store search page, GitHub topic pages, and known vendor domains. Every price below is quoted from the vendor's own page as it rendered today, with the billing period as the vendor writes it. Prices from an App Store listing are marked as such. The reader ("fetch.sh") returns visible text only, so a few collapsed FAQ answers and one price with a hidden decimal were checked in the raw HTML; those cases are called out.

## 0. Bottom line

- The biggest hole in the lane list is reseller-native apps that track cost basis per item from the phone. Flippd (getflippd.com) is free for up to 20 items, 25 expenses and 30 mileage entries a month, and Pro is $8.33/mo billed annually ($99.99/yr) or $9.99/month, with eBay sync, mileage and Schedule C reports, on iPhone, Android and web. Inventory Now (inventorynow.com) is free for the first ten items, then Personal $10/month ($120 yearly) with Shopify, eBay, Etsy and QuickBooks Online connections; its two-way Etsy stock sync shipped on Nov 2, 2026. Both undercut My Reseller Genie Ultimate ($22.99).
- One-of-one stock sync across Etsy, eBay and Shopify (so a lamp sold on Etsy disappears from Shopify before it sells twice) was not covered by the lane. Options read today: Sellbrite Free (up to 30 orders monthly, 2-hour inventory sync) or Pro 100 at $19/month; CedCommerce Etsy Integration from $9/month; Shopify Marketplace Connect free for the first 50 marketplace-synced orders a month (eBay, Amazon, Walmart, Target Plus, not Etsy); Veeqo Inventory from $19/month; Trunk from $35/month.
- Free bookkeeping the lane lacked: ZipBooks Starter (free, unlimited invoices, connect 1 bank account), Manager.io desktop (free forever on Windows, Mac and Linux), Akaunting self-hosted (free, but a BSL licence, not OSI open source), GnuCash (GPL v2 or later; its website returned HTTP 502 twice today). Kick's free plan caps categorization at 250 transactions a year, too small to matter.
- Cheaper marketplace-to-books connector than A2X: Taxomate at $16 per month billed yearly or $19 monthly for up to 200 orders on one channel. Greenback has been renamed Dext Commerce; Starter is $19.00/mo billed monthly for 200 transactions. Both still need a paid QuickBooks Online, Xero or Wave Pro file underneath.
- Tax filing: Cash App Taxes is "100% free for state and federal returns" including 1099 and self-employed income, but you must install Cash App on the phone to log in. IRS Direct File pages return 404 today ("Sorry, this page is not available."). FreeTaxUSA from the lane list already costs $0 for a Florida filer, so this is a backup, not a change.
- Labels from the iPhone: NIIMBOT D110 is $29.99 USD regular, $20.90 USD on sale today; Phomemo D30 from $28.99. Avery Design & Print Online is free, has a free barcode and QR generator, and prints on label sheets in any printer, so SKU labels need no new hardware at all.
- Mileage and receipts: Driversnote Free (15 trips a month) and Smart Receipts Free (manual entry, phone only) do not beat the lane's TripLog Basic (unlimited automatic trips, free) plus Zoho Books Free (receipt autoscans). Nothing to change there.
- Status corrections: Greenback is now Dext Commerce (V). Bench paused in December 2024 and is now an Employer.com company (V), with Bookkeeping Light at $199/mo. Inventora is not dead; its pricing page moved to /pricing-plans/ (Starter $23 /mo) (V). Stride's vendor page loaded today and confirms the app is free (V). Flyp (flyp.app) returned HTTP 502 on both hosts (U, possibly gone). Craftybase's rename to Stocksmith is confirmed on the Shopify App Store ("Stocksmith Inventory & Sync").

## 1. Comparison table (missing tools)

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Flippd | Reseller inventory with cost of goods, fees, net profit per item, expenses, automatic mileage, P&L and Schedule C reports, one-way eBay sync, AI "Coach" | "Free for up to 20 items. Pro from $8.33/mo."; "$8.33/mo billed annually ($99.99/yr), or $9.99/month. Cancel anytime." | "Every feature is free for up to 20 inventory items, plus 25 expenses and 30 mileage entries a month." | "iPhone, iPad, Android, web, Apple Watch" | High: built for one-of-one flips, under $10 a month, phone-first; Etsy sales are marked by hand (only eBay syncs, one way) | V | https://getflippd.com/ and https://getflippd.com/pricing |
| Inventory Now | Item tracker with unit cost, profit after expenses, barcode scanning, Square checkout, Shopify/eBay/Etsy/QuickBooks connections | "Personal is $10 a month" ("$10 BILLED $120 YEARLY"); Professional "$20 BILLED $240 YEARLY" | "Free for your first ten items." ("The free tier keeps up to 10 items on one device.") | "IPHONE · IPAD · MAC · ANDROID · WEB" | High: $10 gets Etsy, eBay and Shopify connections; "Etsy joins App Connections" shipped in "Version 8.12.1 ... Nov 2, 2026", so expect early bugs | V | https://www.inventorynow.com/ |
| Sellbrite (GoDaddy) | Multi-channel listing and inventory sync hub for Amazon, eBay, Etsy, Walmart, Shopify | Shopify listing: "Pro 100 $19 / month or $190/year and save 17%"; Pro 500 "$59 / month" | "Free ... Up to 30 Orders Monthly 2-hr Inventory Quantity Sync ... Unlimited Channels Unlimited SKUs" | Web, Shopify app | Medium-high: free one-of-one sync across Etsy, eBay and Shopify, but a 2-hour window can double-sell; a Feb 13, 2026 review: "each update is every 2 hours" | V (Shopify App Store listing; sellbrite.com/pricing rendered no plan prices) | https://apps.shopify.com/sellbrite and https://www.sellbrite.com/pricing |
| CedCommerce Etsy Integration | Syncs Etsy listings, inventory, orders and prices with Shopify in real time; Shopify is the hub | "From $9/month. Free trial available."; "$9 ... or $103/year and save 5%" | Free trial only | Shopify app | Medium: cheapest real-time Etsy-Shopify stock sync read today; 4.5 stars from 1,248 reviews | V | https://apps.shopify.com/etsy-marketplace-integration |
| Shopify Marketplace Connect | Shopify's own app to list and sync inventory to eBay, Amazon, Walmart, Target Plus | "Free to install. Additional charges may apply."; "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month" | Free to 50 synced orders a month | Shopify app | Medium: free eBay sync from the Shopify site; no Etsy; a review warns it is thin "if you have a inventory over 200 items" | V | https://apps.shopify.com/marketplace-connect |
| Veeqo (Amazon) | Free multichannel shipping; paid inventory sync, listings, profit analyzer | "Inventory ... From $19 /month"; "High Volume ... From $350 /month" | "Shipping ... Free ... Unlimited orders / month ... Unlimited products and SKUs" | Web | Medium: free shipping tier is the shipping lane's call; inventory sync costs $19; today's integration line names "Amazon, Shopify, eBay, Walmart, WooCommerce, Rithum" and not Etsy; "acquired by Amazon in 2021" | V | https://www.veeqo.com/pricing |
| Trunk | Real-time stock sync between Etsy, Shopify, eBay, Faire, Square and others | Shopify listing: "From $35/month."; "Essential $35 / month ... or $45/mo: 101-200 orders/mo" | "14-day free trial No credit card required" | Web, Shopify app | Low-medium: does exactly the one-of-one job but costs more than Sellbrite's free tier; trunkinventory.com/pricing returned HTTP 405 | V (Shopify listing and vendor home page) | https://apps.shopify.com/trunk and https://www.trunkinventory.com/ |
| Taxomate | Posts Etsy, eBay, Shopify, Amazon payouts into QuickBooks Online, Xero or Wave | "Up to 200 [orders] $16 per month billed yearly, or $19 monthly"; Growth (2+ channels) "$24 per month billed yearly, or $29 monthly" | "14-day free trial, card required" | Web connector | Low-medium: cheaper than A2X ($29 per channel) but "Wave needs a Pro plan or Wave Advisors package for third-party connections" | V | https://taxomate.com/pricing |
| Dext Commerce (formerly Greenback) | Same connector idea; pulls sales and expenses from marketplaces into QuickBooks or Xero | "Starter Starts at $19 00 /mo billed monthly" (visible text renders "$1900/mo"; raw HTML shows "$19" and "00"); "Includes 200 transactions per month*" | "Start a free trial" | Web connector | Low: needs a paid accounting file; renamed, so old roundups say Greenback | V | https://www.greenback.com/pricing |
| Synder | Accounting sync for multichannel sellers | "Basic ... $52/mo Billed yearly" | "15-day free trial" | Web connector | Low: over budget | V | https://synder.com/pricing/ |
| Kick | AI bookkeeping with auto-categorization, receipt matching, P&L | "Free $0 /m"; "Basic $40 /m" ("$480 billed annually") | Free plan: "Categorization limit 250 transactions / year" | Web | Low: free cap is a few months of a shop's transactions | V | https://www.kick.co/pricing |
| Tiller | Bank and card feeds into Google Sheets or Excel, with templates | "After 30 days, Tiller is just $99/year, never any ads or hidden fees." | 30-day trial ("up to 60 days risk-free") | Web (Google Sheets, Excel) | Medium: only if Hollie keeps the books in Sheets; the one way to get bank feeds into a spreadsheet ledger | V | https://tiller.com/pricing/ |
| ZipBooks | Free invoicing and basic books with one bank feed | "Smarter 15" and "Sophisticated 35" (the page renders the numbers with no currency sign; monthly plans) | "Starter Free Send unlimited invoices ... Connect 1 bank account ... View Basic Reports" | Web | Medium: free books with a bank feed, which Wave Starter lacks; no inventory | V | https://zipbooks.com/pricing/ |
| Manager.io | Desktop double-entry accounting with inventory items | Desktop: "Free Forever"; Cloud Edition: "59 USD per month Unlimited Users + Unlimited Businesses" | Desktop is free | Windows, Mac, Linux (desktop); web (cloud) | Medium: a free Windows ledger with inventory items; no phone app for the desktop edition | V | https://www.manager.io/ and https://www.manager.cloud/ |
| Akaunting | Open-source-style online accounting; self-host free or pay for cloud | "STANDARD CLOUD ... $8 per month" (page toggle shows MONTHLY / YEARLY "(4 months free)"); "1 User + 1 Accountant", "1,000 Invoices" | "The Standard plan of the On-Premise (self-hosted) version is free in terms of price and freedom (source code available)." | Web (cloud or self-hosted) | Low: self-hosting a PHP app is work; GitHub says "Akaunting is released under the BSL license", which is not an OSI open-source licence | V | https://akaunting.com/plans and https://github.com/akaunting/akaunting |
| GnuCash | Free desktop double-entry accounting | Free; LICENSE: "licensed under the GNU General Public License, Version 2, or (at your option) Version 3." | All free | Windows, Mac, Linux | Low-medium: capable and free, steep for a non-accountant; gnucash.org returned HTTP 502 twice today, GitHub reachable | V (GitHub); U (website) | https://github.com/Gnucash/gnucash and https://raw.githubusercontent.com/Gnucash/gnucash/stable/LICENSE |
| Odoo One App Free | Hosted ERP; one app (for example Inventory or Accounting) free | "One App Free $ 0 One app, unlimited users Odoo Online"; "Standard $ 24 .90 ... / user / month" | One app free | Web, iOS, Android | Low: enterprise-shaped; one free app means inventory or accounting, not both | V | https://www.odoo.com/pricing |
| Homebox | Self-hosted home inventory with photos, locations and labels | "No Cost Forever Free"; LICENSE: "GNU AFFERO GENERAL PUBLIC LICENSE Version 3" | All free | Self-hosted web app (Go, Docker) | Low-medium: free and could run on the Fedora box, but it is "built for the Home User", no sales or COGS | V | https://homebox.software/en/ and https://raw.githubusercontent.com/sysadminsmedia/homebox/main/LICENSE |
| InvenTree | Open-source parts inventory | Free; "InvenTree is an open-source inventory management system which provides intuitive parts management and stock control." | All free | Self-hosted web app | Low: parts and suppliers, not one-of-one resale | V | https://inventree.org/ |
| Orca Scan | Barcode and QR inventory sheets with scanning | "Starter $39 /mo Billed at $468/yr" | "Free $0 Free Forever 100 Rows 1 User 1 Sheet" | Web, Android, Windows (downloads listed); iOS app in Apple's catalog today | Low-medium: 100 free rows fits the room, but Sortly and BoxHero already cover this | V | https://orcascan.com/pricing |
| Driversnote | Automatic mileage log | "Pro 11 USD/ mo" | "Free 0 USD/ mo ... Easy reporting of up to 15 trips" (per month) | "Available on iOS, Android and web" | Low-medium: TripLog Basic (lane list) is unlimited for free | V | https://www.driversnote.com/pricing |
| Smart Receipts | Receipt photos, AI extraction, PDF/CSV reports | "Pro is $99.99 a year ($8.33/mo), or $12.99 a month. Max is $139 a year ($11.58/mo), or $17.99 a month." | "FREE Mobile app only ... Manual receipt entry Basic expense reports No ads" | "iPhone, iPad, Apple Watch, Android, and the web" | Medium: 4.8 stars from 12,861 App Store ratings; free tier is manual only, so Zoho Books Free autoscans win | V | https://smartreceipts.co/ |
| SimplyWise | Receipt scanner and expense reports | Unknown; vendor /pricing redirects to the home page ("Download - it's free") | "Free · In-App Purchases · Designed for iPhone." (App Store) | iOS only ("Only for iPhone") | Medium on reviews (4.9 stars, 38K ratings), price U | U (price) | https://apps.apple.com/us/app/simplywise-receipts-expenses/id1538521095 and https://www.simplywise.com/ |
| Veryfi Receipts OCR & Expenses | Receipt OCR app with line-item extraction; QuickBooks Online project bookkeeping | App subscription price not shown; the vendor pricing page is for its API: "Free Process up to 100 docs/mo $0 Free Forever" | Free API tier; app "Free" with a trial per reviews | iOS ("iPhone, iPad"), Android (U), web | Low-medium: aimed at construction bookkeeping; price U | U (app price) | https://apps.apple.com/us/app/veryfi-receipts-ocr-expenses/id804152735 and https://www.veryfi.com/pricing/ |
| Cash App Taxes | Free federal and state e-file including Schedule C | "Yes, Cash App Taxes is 100% free for state and federal returns." | All free | Web and phone, but "You'll need to download Cash App to log in and use Cash App Taxes." | High as a $0 backup to FreeTaxUSA: "If you're self-employed, have a side gig ... you can still file your taxes for free." Needs a Cash App account | V (FAQ answers read from the page's JSON-LD) | https://cash.app/taxes |
| FlyFin | AI deduction finder plus CPA filing for 1099 workers | Unknown; /pricing returned 404; home page shows no price | Not shown | Web, iOS, Android | Low: price U; marked pricier by design (CPA service) | U (price) | https://flyfin.tax/ |
| Bench | Human bookkeeping service | "Bookkeeping Light ... $199/mo" ("*For businesses doing $250K a year or less in revenue."); "Bookkeeping ... $399/mo" | None | Web, iOS, Android | Low: pricier option, listed as such; "Bench paused operations in December 2024 and was acquired within days by Employer.com" | V | https://www.bench.co/pricing and https://www.bench.co/about |
| Lili | Business bank account with paid expense and bookkeeping tiers | "Lili Pro $15/mo" ("$9 /mo for 3 months"); "Lili Smart $35/mo"; "Lili Premium $55/mo" | "Lili Core $0 /mo" (banking only) | Web, iOS, Android | Low-medium: like Found, but the P&L reports sit on Smart at $35/mo; only if Hollie banks there | V | https://lili.co/plans |
| Quicken Business & Personal | Cloud app for self-employed: business and personal in one, invoices, tax tracking | "$4.99 /month $8.99 44% off Billed annually" | Trial ("Try Quicken for free") | Web, iOS, Android ("cloud-based web & mobile app") | Low-medium: cheap, no inventory or marketplace import | V | https://www.quicken.com/products/pricing-comparison-products/ |
| Neat | Document and receipt capture with human verification | "$200/year"; add-ons "+ $50/year", "+ $150/year" | "Try Neat Free" (trial) | Web, iOS, Android | Low: $16.67 a month for receipts alone | V | https://www.neat.com/pricing |
| TaxJar (Stripe) | Sales tax reporting and filing | "Starter ... $39 / mo" ("for marketplace sellers"); "Professional ... $99 / mo" | "Start a free, 30-day trial, no credit card required" | Web, Shopify integration | Skip: Shopify Tax (lane list) already does the Florida math for a one-state seller | V | https://www.taxjar.com/pricing |
| NIIMBOT D110 label maker | Bluetooth thermal label printer for SKU and QR labels from a phone | "2024 New Niimbot D110 Label Maker Regular price $29.99 USD Sale price $20.90 USD"; "B21 Label Bundles ... Sale price From $59.90 USD" | n/a (hardware) | Phone app, iOS and Android (U; app not read today) | High: a $21 to $30 printer for the item tags the Brother QL-800 ($124.99) would otherwise print | V (store catalog) | https://www.niimbotlabel.com/collections/all |
| Phomemo D30 / M110 label makers | Bluetooth thermal label printers | "Phomemo D30 Portable Bluetooth Home Label Maker From $28.99" ("Regular price $44.39"); "Phomemo M110 ... From $51.99" | n/a (hardware) | Phone app (U) | High as the alternative to NIIMBOT; prices are "Black Friday - Save up to 60% Off" sale prices today | V (store home page) | https://phomemo.com/ |
| Avery Design & Print Online | Free label design with templates, barcode and QR generator; prints on Avery sheets in any printer | Free: "Free online tools to make your design fit, look good, and print the way you want." | All free (you buy label sheets) | Web | High: zero hardware; "Use our free barcode generator to create unique barcodes and QR codes for product labels" | V | https://www.avery.com/software/design-and-print/ |
| Hangar | Shelf-and-box stock tracker for Vinted, Depop, eBay | "Wardrobe: £3.99 a month. Up to 50 items in stock, for one person."; "Seller: £7.99 a month. Up to 200 items" | "Hangar is free for 14 days." | iOS ("Only for iPhone") | Low: UK fashion resale focus, GBP pricing, launched 2026 with no ratings yet | V (App Store) | https://apps.apple.com/us/app/hangar-reseller-inventory/id6804022154 |
| ItemIQ | Photo-to-listing inventory for consignment and live sellers | "Free" (no in-app purchases listed) | Free | iOS ("iPhone, iPad") | Low-medium: new (5 ratings), live-selling shape | V (App Store) | https://apps.apple.com/us/app/itemiq-reseller-inventory/id6747400464 |
| Flippr | AI sourcing scanner with eBay sold comps and eBay autolister (a different product from Flippd) | Unknown; useflippr.com/pricing returned 404; App Store: "Free · In-App Purchases"; "Start free and upgrade for more scans." | Free scans with caps | "Available on iOS and Android", web app | Low for this lane (sourcing and listing, not books); a review complains that after "paying for the monthly subscription ... my scan history still disappears" | U (price) | https://useflippr.com/ and https://apps.apple.com/us/app/flippr-complete-reselling-app/id6746770511 |
| OneShop | Crosslister with inventory (Inventory Systems, Inc.) | "One single subscription ... $45/month" | None shown | Web, iOS | Low: crosslisting lane's territory; over budget | V | https://oneshop.com/pricing |
| syncX: Stock Sync | Shopify inventory feed sync from Google Sheets, FTP, URLs, other stores | "$7 or $77/year" ("$1 for first 30 days, $5 per additional feed") | "Free plan available." | Shopify app | Low: feed-based, not an Etsy or eBay connector | V | https://apps.shopify.com/stock-sync |

## 2. Notes per tool

Flippd. Vendor site read today (getflippd.com and /pricing). The free plan caps are "20 items, plus 25 expenses and 30 mileage entries every month". Pro is "$8.33 per month Billed $99.99/year" or $9.99 month to month. The App Store page adds: "Automatic drive detection logs sourcing trips; US sellers get the IRS mileage rate and an audit-ready log", "Profit and loss and Schedule C reports for tax time", and "With Pro, connect eBay to bring your listings and sales in automatically. That sync is one-way". Etsy has no sync; you "mark each sale on the platform it sold on". Reviews on the App Store are positive ("I have been using this app now for 2 years"). Location permission warning on the listing: "This app may use your location even when it isn't open, which can decrease device battery life." Licence or terms gotcha: none seen; eBay sync is read-only, which avoids automation-policy risk. Fit: a room of 50-plus one-of-one pieces exceeds the free cap, so this is a $9.99 tool from month one.

Inventory Now. Vendor site read today. "Free for your first ten items. No account, no card." Personal "$10 BILLED $120 YEARLY", Professional "$20 BILLED $240 YEARLY" with "Shopify, eBay, Etsy and QuickBooks Online connections" and "Web app on any computer". The changelog says "Version 8.12.1 went live on Nov 2, 2026" and "Etsy joins App Connections: paid and unpaid Etsy orders come in as orders, stock follows your counts both ways, and new items push to Etsy as drafts. A listing that hits zero is paused". That is five days old today, so test before trusting it. App Store rating 4.7 from 694. Terms: it uses the official Etsy, eBay and Shopify APIs by description; nothing read suggests scraping.

Sellbrite. The vendor's own pricing page rendered only the feature grid; plan prices came from Sellbrite's Shopify App Store listing, which is still the vendor's own text. Free: "Up to 30 Orders Monthly 2-hr Inventory Quantity Sync 2-hr Multi-Channel Price Sync Unlimited Channels Unlimited SKUs Unlimited Users". Pro 100: "$19 / month or $190/year and save 17%" with "15-min Inventory Quantity Sync". Note "External charges may be billed by Sellbrite separately from your Shopify invoice." Rating 3.9 from 120 on Shopify. Gotcha for one-of-one: a two-hour sync window is long enough to sell the same decanter twice on a busy day; the paid 15-minute window is the real product. Sellbrite's integration list on its own site includes Amazon, eBay, Etsy, Shopify and Walmart.

CedCommerce Etsy Integration. "Sync Etsy listings, inventory, orders & pricing with Shopify automatically and in real time." "$9 ... or $103/year and save 5%". Shopify is the hub, so Etsy listings get created from Shopify products. 4.5 stars from 1,248. Nothing read on terms. The Shopify search page also listed Shuttle ‑ Sync with Etsy (229 reviews), shopUpz ‑ Etsy Sync & Import (198), SP Etsy Importer & Sync (47), velopLab Etsy Sync & Importer (68) and Market Sync (62); guessed listing slugs for Shuttle and shopUpz returned the App Store's 404 page, so those remain leads (U).

Shopify Marketplace Connect. Shopify's own app. "Free to install." "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month". Channels in the title: "Amazon, Target Plus, Walmart, and eBay". No Etsy. A review on the page: "if you have a inventory over 200 items and plan to list on other marketplaces, I highly recommend looking for a more polished tool". 4.1 stars from 2,135.

Veeqo. "Our shipping features are free to use for everyone. We make a small commission on labels purchased through Veeqo". Inventory plan "From $19 /month" priced by order volume, adds "Automated inventory sync across channels" and "Multichannel listings". FAQ: "Veeqo was founded in the UK ... acquired by Amazon in 2021." Etsy is not in the integrations line read today ("Amazon, Shopify, eBay, Walmart, WooCommerce, Rithum and more"), so treat Etsy support as U. Data-use gotcha: it is an Amazon company holding your multichannel sales data; that is a judgment call, not a violation.

Trunk. Vendor site: "Keep inventory synced in real-time between Etsy & Shopify" (rotating headline), "14-day free trial No credit card required". Shopify listing: Essential "$35 / month" up to 100 orders, Pro "$39 / month" adds bundling and "Duplicate SKU syncing". 4.9 stars from 409. The vendor pricing URL answered HTTP 405 to both the browser and curl.

Taxomate. "Choose Starter for one sales channel or Growth for two or more, then pick your monthly orders." Up to 200 orders: Starter "$16 per month billed yearly, or $19 monthly"; Growth "$24 per month billed yearly, or $29 monthly". Targets "QuickBooks Online, Xero or Wave" but "Wave needs a Pro plan or Wave Advisors package for third-party connections." "A card is required." Refund "if you ask within 7 days of your first charge." Overage rule: "Until December 31, 2026, you move up a tier".

Dext Commerce (Greenback). Page title today: "Pricing Greenback | Dext Commerce". Starter "Starts at $19 00 /mo billed monthly ... Includes 200 transactions per month*"; the visible-text reader printed "$1900/mo" because the cents are a separate element; the raw HTML shows "$19" and "00". Growth "$5900/mo" reads the same way ($59.00). "Pay Upfront SAVE 15% Annual Commitment". Needs one accounting file (QuickBooks or Xero).

Synder. "Basic ... $52/mo Billed yearly", "Up to 500 sales transactions/mo". Over budget; included so the synthesis does not re-find it.

Kick. "Free $0 /m" with "Categorization limit 250 transactions / year"; "Basic $40 /m" or "$480 billed annually". Integrations listed: Plaid, Stripe, "+50". Features include "MCP/CLI", which is interesting for the planned Claude dashboard, but the free cap is too small for a shop.

Tiller. "$99/year" after a 30-day trial, "never any ads or hidden fees", and "Sales tax will be added to your invoice after the free trial if required in your state." Works through "your Microsoft or Google account". It is a bank-feed engine for a spreadsheet, not accounting software.

ZipBooks. Starter is free with "Send unlimited invoices", "Accept digital payments (Square or PayPal)", "View Basic Reports", "Connect 1 bank account". Smarter and Sophisticated render as "15" and "35" with no currency sign on the page; raw HTML confirms "<strong>15</strong>" and "<strong>35</strong>". Treat them as $15 and $35 per month (U on the currency, V on the numbers). No inventory, no marketplace import.

Manager.io. Desktop edition "Free Forever" for "Windows, Mac and Linux"; the demo company shows "Inventory Items" as a module. Cloud Edition on manager.cloud: "59 USD per month Unlimited Users + Unlimited Businesses", "14-day free trial. No credit card required." The /pricing and /cloud paths on manager.io are 404; pricing lives on manager.cloud. Desktop data stays on the PC, so no phone access without the cloud edition.

Akaunting. Marketing says "free, open-source", but GitHub says "Akaunting is released under the BSL license" (Business Source License), which the OSI does not list as open source. Self-hosting is free; cloud Standard is "$8 per month" under a MONTHLY / YEARLY toggle whose yearly side promises "(4 months free)", so confirm which side $8 belongs to before quoting it to Ricky. "1 User + 1 Accountant", "1,000 Invoices", "4 Apps Included". The /pricing URL timed out; /plans loaded.

GnuCash. "GPL v2 or later" (LICENSE file). gnucash.org answered HTTP 502 on both tries today; the GitHub repo and raw LICENSE loaded. Mature desktop software; no phone app; no marketplace imports.

Odoo. "One App Free $ 0 One app, unlimited users Odoo Online". Paid "Standard $ 24 .90 ... / user / month" with a struck "US$ 31.10 *" (discount "valid for 12 months"). An ERP for a one-person vintage shop is the wrong size.

Homebox. "100% Open Source", "No Cost Forever Free", "Self-Hosted Full Control", AGPL-3.0. It is "built for the Home User" and has no sales or COGS, so at best it is a free photo catalog with QR labels that the Fedora box could run in podman.

InvenTree. Open source, parts-oriented ("Organize Parts", "Manage Suppliers"). Not a resale tool.

Orca Scan. "Free $0 Free Forever" with "100 Rows 1 User 1 Sheet"; Starter "$39 /mo Billed at $468/yr". "Download for Android", "Download for Windows" on the page; the iOS app ("Barcode Scanner - Orca Scan") appeared in Apple's catalog today. Overlaps Sortly and BoxHero from the lane list.

Driversnote. Free "0 USD/ mo" for "up to 15 trips" a month; Pro "11 USD/ mo"; "Includes free iBeacon with yearly subscription 40 USD value". Fine app, but TripLog Basic is unlimited for free.

Smart Receipts. Free is "Mobile app only" with "Manual receipt entry"; "Web access starts with Pro." Pro "$99.99 a year ($8.33/mo), or $12.99 a month"; Max adds "Bank connections (US and Canada)" at "$139 a year ($11.58/mo), or $17.99 a month". "In-app purchase prices may differ." 4.8 stars from 12,861 App Store ratings.

SimplyWise. 4.9 stars from 38K ratings, "Only for iPhone", "Free · In-App Purchases". The vendor's /pricing URL redirected to the home page, which only says "Download - it's free"; the subscription price is U.

Veryfi. The App Store app is "Free" with "Designed for iPad"; a review mentions a "14 day trial period". The vendor pricing page is API pricing ("Free Process up to 100 docs/mo $0 Free Forever", "$0.08 per receipt" beyond). Positioning is "especially for AEC industries" (construction). Not for Hollie.

Cash App Taxes. JSON-LD FAQ on the page: "Yes, Cash App Taxes is 100% free for state and federal returns." and "if you received a 1099 from work, a bank, or anywhere else ... If you're self-employed, have a side gig, do some contract work, or own a small business, you can still file your taxes for free." Gotcha: "You'll need to download Cash App to log in and use Cash App Taxes." Then "file your taxes from your phone or computer at cash.app/taxes". Florida has no state return, so FreeTaxUSA ($0 federal) already costs the same without a Cash App account.

FlyFin. "World's #1 AI and CPA tax filing service" for "freelancers, self-employed, business owners, 1099 & W-2 workers"; /pricing is 404 and the home page shows no price. Pricier by nature (CPA files the return). U on price.

Bench. "Bookkeeping Light ... $199/mo" for "$250K a year or less in revenue"; "Bookkeeping ... $399/mo"; "Bookkeeping + Tax ... $649/mo". About page: "Bench paused operations in December 2024 and was acquired within days by Employer.com, resuming service in January 2025." A human bookkeeper at 20x the budget; listed as the pricier option.

Lili. "Lili Core $0 /mo" is banking only. Pro "$15/mo" adds "Organize your expense transactions into tax categories", receipts and quarterly reports. Smart "$35/mo" adds "Accounting Software ... profit & loss and cash flow statements". "30-day free trial. Tax-deductible." Found (lane list) gives bookkeeping and receipts at $0, so Lili only wins on banking features.

Quicken Business & Personal. "$4.99 /month $8.99 44% off Billed annually"; "Manage business & personal finances in one cloud-based app", "Stay ahead of cash flow & taxes year-round", "Invoice clients". The old /pricing URL is 404; pricing lives at /products/pricing-comparison-products/. No inventory.

Neat. "$200/year" with "Data capture with human verification". Too much for receipts alone when Zoho Books Free autoscans.

TaxJar. Starter "$39 / mo" is "Designed for new businesses to get started and for marketplace sellers"; Professional "$99 / mo". Skip: Etsy and eBay collect Florida tax as marketplace providers, and Shopify Tax covers the Shopify site.

NIIMBOT. Official US store (Shopify-powered). "2024 New Niimbot D110 Label Maker Regular price $29.99 USD Sale price $20.90 USD". Labels: "B18/N1 Label ... $9.90 USD"; "B21 Label Bundles Regular price $119.99 USD Sale price From $59.90 USD". The D-series prints 12 to 25 mm labels; the B21 prints wider labels. The phone app and its iOS support were not read today (U). Gotcha, from memory and marked U: these printers take the maker's own label rolls.

Phomemo. Home page lists "Phomemo D30 Portable Bluetooth Home Label Maker From $28.99" (regular "$44.39"), "Phomemo M110 Bluetooth Portable Thermal Business Label Maker From $51.99" (regular "$96.00"), "Phomemo M221 ... $64.99". Banner: "Black Friday - Save up to 60% Off", so the "From" prices are sale prices. Also sells a "PM241-BT Bluetooth Shipping Label Printer From $110.99" (shipping lane).

Avery Design & Print Online. "Free online tools"; "Use our free barcode generator to create unique barcodes and QR codes for product labels or to add sequential numbering to raffle tickets & price tags." Prints to any inkjet or laser printer on Avery label sheets. The cheapest working SKU-label setup read today.

Hangar. New in 2026 (App Store id6804022154), "an inventory app for Vinted, Depop and eBay sellers", priced in pounds ("Wardrobe: £3.99 a month. Up to 50 items"). UK fashion shape. Low fit.

ItemIQ. "Free", "Built for resellers, consignment teams, and live sellers who need every item photographed, identified, located, and listed". 5 ratings. Watch, do not adopt.

Flippr vs Flippd. Two different companies. Flippr (Flippr Inc., useflippr.com, launched 2025, 4.7 stars from about 2K) is a sourcing scanner that values a shelf of items from "eBay sold listings" and autolists to eBay; it says "This application uses the eBay API but is not endorsed or certified by eBay". Its pricing page is 404 and the App Store page lists in-app purchases without prices (U). Flippd (Flippd LLC, getflippd.com, since 2022, 4.8 stars from 157) is the inventory and profit ledger in the table.

OneShop. "$45/month", one plan, "Inventory Systems, Inc." Crosslisting lane's territory; over budget. 3.3 stars from 471 on the App Store.

syncX: Stock Sync. "Free plan available", paid "$7 or $77/year". It syncs stock from feeds (Google Sheets, FTP, URLs) and between Shopify stores; it is not an Etsy or eBay connector.

## 3. Recommendation for Hollie

Free first, today:
- Install Flippd (free) on the iPhone and open the web app on the Windows PC. Enter the first 20 pieces with cost basis and let it log sourcing drives. If it fits, Pro is $9.99 month to month or $99.99 a year; that replaces a My Reseller Genie Ultimate subscription ($22.99) for everything except Etsy sync, which neither free tool has.
- Try Inventory Now free (10 items) alongside, because it is the one phone-first tool read today that connects Etsy, eBay and Shopify at $10 a month. Its Etsy connection is five days old; test it on a few listings before relying on it.
- Make SKU labels with Avery Design & Print Online on label sheets in the existing printer (free). Buy a NIIMBOT D110 ($20.90 on sale, $29.99 regular) only if printing from the phone at the rack turns out to matter.
- Keep the lane's free books stack (Zoho Books Free, TripLog Basic, FreeTaxUSA). Cash App Taxes is a free backup for filing if FreeTaxUSA ever charges; it needs a Cash App account.

Pay only once it earns it:
- Stock sync across Etsy, eBay and Shopify when the Shopify site is live: start with Sellbrite Free (30 orders a month, 2-hour sync) and watch for double-sells; move to Sellbrite Pro 100 ($19/month, 15-minute sync) or CedCommerce Etsy Integration ($9/month, real-time, Shopify as hub) if the window bites. Shopify Marketplace Connect is free for eBay sync from the Shopify site (50 orders a month) but does not touch Etsy.
- Taxomate ($16 a month billed yearly for 200 orders) only if Hollie later moves to QuickBooks Online or Xero; with Zoho Books or Seller Ledger it is not needed.
- Tiller ($99/year) only if Hollie insists on keeping the ledger in Google Sheets and wants bank transactions to land there.

Skip and why:
- Veeqo Inventory, Trunk, Synder, Dext Commerce: over budget or redundant with Seller Ledger and Sellbrite.
- Kick: the free plan's 250 transactions a year is too small; $40 a month is over budget.
- Bench, Neat, TaxJar, FlyFin, Lili Smart, Odoo, Akaunting cloud: pricier or wrong shape for a one-person shop.
- Homebox, InvenTree, GnuCash, Manager.io: free, but they add self-hosting or desktop-only work without marketplace imports; keep as fallbacks if every SaaS option fails.
- Driversnote, Smart Receipts, SimplyWise, Veryfi, Orca Scan: fine apps whose free tiers are weaker than TripLog, Zoho Books and Sortly from the lane list.

## 4. Gaps and pages that would not load

- WebSearch was unavailable (shared budget exhausted before this agent started). Leads came only from vendor catalogs reachable by direct URL (Apple's App Store search API, the Shopify App Store search page, GitHub topic pages). Chrome Web Store and Product Hunt were not checked.
- Square (squareup.com pricing pages): HTTP 429 twice. Square's free POS and inventory tier is a known candidate for a one-of-one room and remains U.
- Flyp (flyp.app and www.flyp.app): HTTP 502 on both. Status unknown; may be gone.
- Easy Auctions Tracker (easyauctionstracker.com): HTTP 405 (bot wall). U.
- GoDaddy Bookkeeping (bookkeeping.godaddy.com): tunnel failed. Widely reported shut down in 2022 (memory, U); some roundups still list it.
- IRS Direct File: irs.gov/filing/irs-direct-file-for-free and irs.gov/filing/irs-direct-file both return the IRS 404 page ("Sorry, this page is not available."); directfile.irs.gov would not connect. Program status not confirmed from a live IRS page (U), but it never supported Schedule C in any case (memory, U).
- Memento Database: home page loads ("Get Memento free") but /pricing and /pricing/ are 404. Price U.
- FlyFin /pricing 404; Foreceipt /pricing/ 404 (Foreceipt not otherwise read; U).
- Flippr /pricing 404; in-app prices not printed on the App Store page.
- SimplyWise /pricing redirects to the home page; in-app prices not printed.
- Trunk vendor pricing page HTTP 405; Shopify listing used instead.
- Sellbrite vendor pricing page rendered features but no prices; Shopify listing used instead.
- Shopify App Store: guessed slugs for Shuttle and shopUpz, and the category URL tried, returned the App Store 404 page. The search page (apps.shopify.com/search?q=etsy inventory sync) loaded and gave the leads listed in section 2.
- Akaunting /pricing timed out; /plans loaded.
- gnucash.org HTTP 502 twice; GitHub used.
- Apple's search API returned empty bodies for two of nine queries ("smart receipts", "my reseller genie"); the other seven worked.
- Etsy and eBay help pages were not needed for this lane and were not fetched.
- Not re-verified (another agent's job): every tool already on the lane list. Stride and Inventora were touched only because their status needed a check; both are alive.

## 5. Sources

Vendor and catalog pages read today (HTTP 200 unless noted):
https://getflippd.com/
https://getflippd.com/pricing
https://apps.apple.com/us/app/flippd-reseller-inventory/id1633899291
https://www.inventorynow.com/
https://apps.apple.com/us/app/inventory-now-stock-tracker/id313140115
https://apps.shopify.com/sellbrite
https://www.sellbrite.com/pricing
https://apps.shopify.com/etsy-marketplace-integration
https://apps.shopify.com/marketplace-connect
https://apps.shopify.com/stock-sync
https://apps.shopify.com/trunk
https://www.trunkinventory.com/
https://apps.shopify.com/search?q=etsy%20inventory%20sync
https://www.veeqo.com/pricing
https://taxomate.com/pricing
https://www.greenback.com/pricing
https://synder.com/pricing/
https://www.kick.co/pricing
https://tiller.com/pricing/
https://zipbooks.com/pricing/
https://www.manager.io/
https://www.manager.cloud/
https://www.manager.io/pricing (404 page)
https://www.manager.io/cloud (404 page)
https://akaunting.com/
https://akaunting.com/plans
https://github.com/akaunting/akaunting
https://github.com/Gnucash/gnucash
https://raw.githubusercontent.com/Gnucash/gnucash/stable/LICENSE
https://www.odoo.com/pricing
https://homebox.software/en/
https://github.com/sysadminsmedia/homebox
https://raw.githubusercontent.com/sysadminsmedia/homebox/main/LICENSE
https://inventree.org/
https://github.com/topics/inventory-management
https://github.com/topics/reseller
https://orcascan.com/pricing
https://www.driversnote.com/pricing
https://smartreceipts.co/
https://www.simplywise.com/ (redirect from /pricing)
https://apps.apple.com/us/app/simplywise-receipts-expenses/id1538521095
https://www.veryfi.com/pricing/
https://apps.apple.com/us/app/veryfi-receipts-ocr-expenses/id804152735
https://cash.app/taxes
https://flyfin.tax/
https://www.bench.co/pricing
https://www.bench.co/about
https://lili.co/plans
https://lili.co/pricing (404 page)
https://www.quicken.com/products/pricing-comparison-products/
https://www.quicken.com/pricing/ (404 page)
https://www.neat.com/pricing
https://www.taxjar.com/pricing
https://www.niimbotlabel.com/
https://www.niimbotlabel.com/collections/all
https://phomemo.com/
https://www.avery.com/software/design-and-print/
https://apps.apple.com/us/app/hangar-reseller-inventory/id6804022154
https://apps.apple.com/us/app/itemiq-reseller-inventory/id6747400464
https://useflippr.com/
https://apps.apple.com/us/app/flippr-complete-reselling-app/id6746770511
https://oneshop.com/pricing
https://inventora.com/pricing-plans/
https://inventora.com/pricing (404 page)
https://www.stridehealth.com/tax
https://mementodatabase.com/
https://www.irs.gov/filing/irs-direct-file-for-free (IRS 404 page)
https://www.irs.gov/filing/irs-direct-file (IRS 404 page)
https://apps.shopify.com/categories/store-management-inventory-management (App Store 404 page)
https://apps.shopify.com/shopify-marketplace-connect (App Store 404 page)
https://apps.shopify.com/shuttle (App Store 404 page)
https://apps.shopify.com/shopupz (App Store 404 page)
https://www.useflippr.com/pricing (404 page)

Failed fetches (no page content):
https://squareup.com/us/en/pricing (HTTP 429)
https://squareup.com/us/en/point-of-sale/pricing (HTTP 429)
https://flyp.app/ (HTTP 502)
https://www.flyp.app/ (HTTP 502)
https://www.easyauctionstracker.com/ (HTTP 405)
https://bookkeeping.godaddy.com/ (tunnel failed)
https://directfile.irs.gov/ (tunnel failed)
https://gnucash.org/ (HTTP 502)
https://www.gnucash.org/ (HTTP 502)
https://akaunting.com/pricing (timeout)
https://www.trunkinventory.com/pricing (HTTP 405)
https://flyfin.tax/pricing (HTTP 404)
https://foreceipt.com/pricing/ (HTTP 404)
https://mementodatabase.com/pricing (HTTP 404)
https://mementodatabase.com/pricing/ (HTTP 404)
https://flippd.app/ (HTTP 502; not the vendor's domain, which is getflippd.com)
https://flippr.com/ (empty; not the vendor's domain, which is useflippr.com)

Apple App Store catalog queries (itunes.apple.com/search, country=us, entity=software): "flyp reseller", "reseller inventory", "reseller bookkeeping", "veryfi receipts", "foreceipt", "stride tax", "inventory barcode scanner" (results used as leads only); "smart receipts" and "my reseller genie" returned empty bodies.
