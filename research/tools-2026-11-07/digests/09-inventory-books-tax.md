# Lane 09: Inventory, bookkeeping, mileage and tax

Question answered: which tools track inventory, cost basis, profit, expenses, mileage and taxes for a one-person vintage reseller in Florida, and what do they cost. Date 2026-11-07. Three files read (lane, verify, gaps); where the verify file disagrees with the lane, the verify file wins.

## Bottom line

- The $0 day-one stack survives the verify pass: Airtable Free as the item ledger (1,000 records per base, 1 GB of attachments per base), Zoho Books Free for the books (Receipt and Document Autoscans, Mileage tracking, Bank reconciliation, P&L, 1 User + 1 Accountant), TripLog Basic for mileage (Unlimited automatic GPS mileage tracking, Free forever), FreeTaxUSA to file (Federal Tax Returns Free; no Florida income tax). Correction: Zoho Books Free has no bank feeds (Standard, "$20 $15 Price/Org/Month Billed Annually"), so bank lines are imported or typed.
- Best gaps finds: two phone-first reseller ledgers undercut My Reseller Genie. Flippd is free for 20 items, 25 expenses and 30 mileage entries a month, then Pro "$8.33/mo billed annually ($99.99/yr), or $9.99/month", with one-way eBay sync and Schedule C reports. Inventory Now is free for ten items, then Personal "$10 BILLED $120 YEARLY" with Shopify, eBay, Etsy and QuickBooks Online connections; the Etsy connection shipped Nov 2, 2026.
- My Reseller Genie: only Ultimate at "$22.99 per month" has any marketplace sync; verify's raw-HTML read shows every integration, analytics, bank/PayPal and consignment struck through on Basic "$11.99 per month". Web app only.
- Seller Ledger stays the first paid books tool: "Up to 250 transactions per month $10 /month $100 /year", imports Etsy, eBay and Shopify, 30-day trial, no card. Monthly plans look back only 90 days.
- Stock sync across Etsy, eBay and Shopify was missing from the lane: Sellbrite Free (up to 30 orders monthly, 2-hour sync), Sellbrite Pro 100 "$19 / month" (15-minute sync), CedCommerce Etsy Integration "From $9/month" (real time, Shopify as hub). Shopify Marketplace Connect is free for 50 synced orders a month, no Etsy.
- Tax facts hold: 1099-K only above $20,000 in more than 200 transactions, all income reportable; Florida 6% plus Lee 0.5% through Dec 31, 2028, Collier none; Etsy and eBay remit, and those sales are excluded from the shop's own return; the Shopify site needs DOR registration (DR-1) first, then Shopify Tax, free until "$100,000 USD" lifetime for stores created on or after May 13, 2026, then 0.35% per order capped at "$0.99 USD". Verify corrections: no DOR page states a registration fee (U); Lee County's $50 is the October to March start rate ($25 April to June, $12.50 July to September); receipts expire September 30.
- Labels need no $124.99 printer: Avery Design & Print Online is free with a barcode and QR generator; NIIMBOT D110 is "Regular price $29.99 USD Sale price $20.90 USD" for printing at the rack.

## Table

Source files: lane = 09-inventory-books-tax.md, verify = verify-09-inventory-books-tax.md, gaps = gaps-09-inventory-books-tax.md.

| Tool | Does | Price (vendor wording, billing period) | Free tier | Platform | Verdict for Hollie | V or U | Source file and URL |
|---|---|---|---|---|---|---|---|
| Airtable | Item ledger with photos, forms, automations; Ricky has it | Team "$20USD per seat/month" billed annually, "$24 billed monthly" | "Unlimited bases 1,000 records per base Up to 5 editors 1 GB of attachments per base 100 automation runs" | Web, iOS, Android, Windows | Use now: free ledger until Supabase | V | lane, verify; https://airtable.com/pricing |
| Zoho Books | Books: receipt autoscans, mileage, reconciliation, P&L | "STANDARD $20 $15 Price/Org/Month Billed Annually" | "FREE $0 ... Receipt and Document Autoscans ... Mileage tracking ... Bank reconciliation ... P&L, Balance Sheet & 50+ Reports ... 1 User + 1 Accountant" | Web, iOS, Android, Windows | Use now; bank feeds are Standard, Etsy/eBay channel sync is Elite only ($150 monthly, $120 annual) | V | lane, verify; https://www.zoho.com/us/books/pricing/ |
| TripLog | Automatic mileage, basic expenses | Premium "$4.99 Per month Paid annually" ("Paid annually as $59.99") | Basic "Unlimited automatic GPS mileage tracking & basic expense management ... Free forever" | iOS, Android; web and unlimited reporting are Premium | Use now | V | lane, verify; https://www.triplog.net/pricing |
| FreeTaxUSA | Federal filing incl. Schedule C | "Federal Tax Returns Free", "State Tax Returns $15.99"; Self-Employed "$0 + $15.99 per state" | Free federal | Web | Use now at filing time; no Florida return | V | lane, verify; https://www.freetaxusa.com/pricing/ |
| Shopify Tax | Sales tax math on the Shopify store | Past threshold "0.35% [Basic, Grow, or Advanced]", "Maximum fee per order $0.99 USD" | Free until "Lifetime sales threshold $100,000 USD" (stores created on or after May 13, 2026) | Shopify, built in | Use now when the store opens | V | lane, verify; https://help.shopify.com/en/manual/taxes/shopify-tax/pricing |
| Avery Design & Print Online | Label design, free barcode and QR generator, prints on Avery sheets | Free ("Free online tools"); label sheets bought separately | All free | Web | Use now for SKU tags | V | gaps; https://www.avery.com/software/design-and-print/ |
| Flippd | Reseller ledger: cost per item, fees, net profit, expenses, auto mileage, P&L and Schedule C, one-way eBay sync | Pro "$8.33/mo billed annually ($99.99/yr), or $9.99/month" | "Every feature is free for up to 20 inventory items, plus 25 expenses and 30 mileage entries a month." | "iPhone, iPad, Android, web, Apple Watch" | Use now free; pay $9.99/month past 20 items; Etsy sales marked by hand | V | gaps; https://getflippd.com/pricing |
| Seller Ledger | Books for online sellers; imports Etsy, eBay, Shopify, Poshmark, Mercari, Amazon | "Up to 250 transactions per month $10 /month $100 /year" | "30-day free trial No credit card required" | Web | Pay when orders flow; monthly plans look back 90 days | V | lane, verify; https://sellerledger.com/pricing/ |
| Inventory Now | Item tracker with unit cost, profit, barcode scan; Shopify, eBay, Etsy, QuickBooks Online connections | Personal "$10 BILLED $120 YEARLY"; Professional "$20 BILLED $240 YEARLY" | "Free for your first ten items." (one device) | "IPHONE · IPAD · MAC · ANDROID · WEB" | Pay when three-channel stock sync is needed; Etsy connection is "Version 8.12.1 ... Nov 2, 2026" | V | gaps; https://www.inventorynow.com/ |
| My Reseller Genie | Reseller books: inventory at cost, marketplace sync, consignment, P&L | "Basic $11.99 per month", "Premium $16.99 per month", "Ultimate $22.99 per month" (Monthly toggle) | None; "14 day money back guarantee" | Web app only; vendor recommends a computer or iPad | Pay only if Etsy sync plus consignment in one ledger matters; all marketplace sync is Ultimate | V | lane, verify; https://discover.myresellergenie.com/ |
| Sellbrite (GoDaddy) | Multi-channel stock and listing sync: Etsy, eBay, Shopify, Amazon, Walmart | "Pro 100 $19 / month or $190/year and save 17%" | "Free ... Up to 30 Orders Monthly 2-hr Inventory Quantity Sync ... Unlimited Channels Unlimited SKUs" | Web, Shopify app | Use free once Shopify is live; pay $19 for 15-min sync if the 2-hour window double-sells | V (Shopify App Store listing) | gaps; https://apps.shopify.com/sellbrite |
| CedCommerce Etsy Integration | Real-time Etsy to Shopify listing, stock and order sync | "From $9/month"; "$9 ... or $103/year and save 5%" | Free trial only | Shopify app | Pay when real-time Etsy-Shopify sync is wanted; Shopify is the hub | V | gaps; https://apps.shopify.com/etsy-marketplace-integration |
| Shopify Marketplace Connect | Shopify's own eBay, Amazon, Walmart, Target Plus sync | "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month" | "Free to install." | Shopify app | Use free for eBay once Shopify is live; no Etsy | V | gaps; https://apps.shopify.com/marketplace-connect |
| NIIMBOT D110 | Bluetooth thermal label maker for phone-printed SKU and QR tags | "Regular price $29.99 USD Sale price $20.90 USD" | n/a (hardware) | Phone app, iOS and Android (U, app not read) | Pay when tags must print at the rack | V (store catalog) | gaps; https://www.niimbotlabel.com/collections/all |
| Brother QL-800 | USB desktop label printer (DK rolls) | "$124.99" | n/a | Windows, Mac (USB) | Skip for now: Avery or NIIMBOT covers SKU tags for less | V | lane, verify; https://www.brother-usa.com/p/desktop-label-printers/QL800 |
| Keeper | Books plus pro-signed tax filing | "Bookkeeping Only $20/mo"; "Standard $199 /yr $16.58/mo, billed yearly"; Premium "$399 /yr" | "14-day free trial" | iOS, Android, web | Pay only if Hollie wants a tax pro; "Track mileage Coming soon" | V | lane, verify; https://www.keepertax.com/pricing |
| Cash App Taxes | Free federal and state e-file incl. Schedule C | "100% free for state and federal returns" | All free; Cash App must be installed to log in | Web and phone | Skip: backup only, FreeTaxUSA is already $0 | V (page JSON-LD) | gaps; https://cash.app/taxes |
| ZipBooks | Free invoicing and basic books with one bank feed | "Smarter 15", "Sophisticated 35" (monthly; no currency sign on the page) | "Starter Free Send unlimited invoices ... Connect 1 bank account ... View Basic Reports" | Web | Skip unless a free bank feed outweighs Zoho's autoscans | V numbers, U currency | gaps; https://zipbooks.com/pricing/ |
| Wave | Free invoicing and hand-entered books | "PRO Plan $190USD/year Billed annually"; receipts "ADD-ON $8/month OR $72/year" | "STARTER Plan $0 ... unlimited estimates, invoices, bills, and bookkeeping records" | Web, iOS, Android | Skip: bank auto-import is Pro only | V | lane, verify; https://www.waveapps.com/pricing |
| QuickBooks Free | Basic income and expense tracking | "$0/mo No credit card required" | "Connect 1 bank", "Send 2 invoices per month", "Upload receipts (2 per month)", "Track mileage (5 trips per month)" | Web only, no mobile app | Skip: too capped | V (curl) | lane, verify; https://quickbooks.intuit.com/pricing/ |
| QuickBooks Solopreneur ("Lite") | Self-employed books, receipts, mileage | "$20 $10/mo 50% off for 3 months*" | 30-day trial | Web, iOS, Android | Skip: "No accountant access", no inventory | V (curl) | lane, verify; https://quickbooks.intuit.com/solopreneur/ |
| Found | Business banking with built-in books, receipts, mileage, tax estimates | "Found Plus $35/mo; $315/yr"; "Found Pro $80/mo; $720/yr" | "$0/mo Your banking, bookkeeping, and tax platform" | Web, iOS, Android | Skip unless Hollie banks there; $10 dormancy fee after 12 months idle | V (curl) | lane, verify; https://found.com/pricing |
| Zoho Expense | Receipt OCR, GPS mileage | "STANDARD $3 per user/month billed annually" | "FREE $0 ... Maximum users: 3 ... Receipt capture with AI-powered OCR ... Mileage expenses via GPS ... 5 GB receipt storage" | iOS, Android, web | Skip: redundant with Zoho Books Free; auto mileage is Premium | V | lane, verify; https://www.zoho.com/us/expense/pricing/ |
| Everlance | Automatic mileage, expenses | "Starter $89.99 Per year or $10.99 per month"; "Professional $119.99 Per year or $19.99 per month" | "Basic ... $0 ... 30 automatically tracked trips a month Unlimited manually tracked trips" | iOS, Android, web | Skip: TripLog is unlimited; trial needs a card, "all sales are non-refundable" | V | lane, verify; https://www.everlance.com/pricing |
| MileIQ | Automatic mileage | "Unlimited $11.66 PER MONTH BILLED ANNUALLY" | "Free $0 40 FREE DRIVES EVERY MONTH" | iOS, Android, web | Skip: TripLog is unlimited; owner Bending Spoons | V | lane, verify; https://mileiq.com/pricing |
| Hurdlr | Mileage, expenses, tax estimates | Premium "$100 annual plan ($8.34 a month, most popular)" or "$9.99 month-to-month plan"; Pro "$200 per year" | Free: "unlimited semi-auto mileage tracking, manual finance tracking, and real-time tax estimates" | iOS, Android, web | Skip: semi-auto; help article dated Nov 9, 2023 | V (Free, Premium), U (Pro) | lane, verify; https://university.hurdlr.com/en/articles/1072143-what-are-the-premium-features-and-how-much-do-they-cost |
| Flipwise | eBay-only inventory, profit, Schedule C, mileage | "$19.99 /mo 100–499 listings" | "Free Up to 24 listings (new members only)" | Web | Skip: Etsy sales typed by hand | V | lane, verify; https://flipwise.app/pricing |
| Sortly | Photo inventory with QR labels | "Advanced $24 USD/mo.* Billed at $288/yr."; verify: a 50%-off first-year flash sale, "You'll save $300!" puts list near $588/yr | "Free $0 USD/mo. 100 Unique Items 1 User License 2 Active Jobs" | Web, iOS, Android | Skip: Airtable ID on an Avery label does the job; QR label creation is paid | V | lane, verify; https://www.sortly.com/pricing/ |
| BoxHero | Inventory with barcode scanning, label printing | "Business Plan ... $24 per team / month $288 annually" (1,000 items, 3 members) | Personal "100 items", "Free", includes "Barcode Scanning" | Web, iOS, Android | Skip: same shape as Sortly | V | lane; https://www.boxhero.io/pricing |
| Taxomate | Posts Etsy, eBay, Shopify, Amazon payouts into QuickBooks Online, Xero or Wave | "Up to 200 [orders] $16 per month billed yearly, or $19 monthly"; Growth "$24 per month billed yearly, or $29 monthly" | "14-day free trial, card required" | Web connector | Skip: needs a paid accounting file ("Wave needs a Pro plan") | V | gaps; https://taxomate.com/pricing |

Dropped: Dext, Dext Commerce (was Greenback), A2X, Synder (need a paid accounting file); Link My Books, Hangar (UK, GBP); Shoeboxed, Neat, Expensify (receipt pipelines Zoho Books Free covers); Xero, FreshBooks (no free tier); Notion, Google Sheets templates, Tiller (weaker than Airtable or Sheets-only); Kick (250 free transactions a year); Nifty, OneShop, Vendoo, Crosslist, List Perfectly (crosslister lane; Crosslist "Gold $39.99 per month" unchanged); Zoho Inventory, Stocksmith (was Craftybase), Inventora (alive, "Starter $23 /mo"), Veeqo, Trunk, Odoo, InvenTree, Homebox, Manager.io, GnuCash, Akaunting (quantity stock, makers, ERP or self-hosting); Orca Scan, Driversnote, Smart Receipts, SimplyWise, Veryfi, Stride (free tiers weaker than TripLog, Zoho Books or Sortly; Stride confirmed free); Bench, Lili, Quicken, TaxJar, FlyFin (pricier or wrong shape); ItemIQ, Flippr (new, sourcing or live-selling); syncX (feed sync); Rollo, Phomemo PM241 (shipping lane); Dymo (403), Flyp (502), Square (429): U.

## Picks

Use now (free):
- Airtable Free: one table with the Spreadsheet Point cost-basis columns; link Drive photos. Stopgap until Supabase.
- Zoho Books Free: import statements, autoscan receipts, invite the accountant seat.
- TripLog Basic for sourcing mileage.
- Flippd free for the first 20 pieces, to test a phone-first cost ledger.
- Avery Design & Print Online for SKU and QR labels on the existing printer.
- FreeTaxUSA at filing time.
- When Shopify opens: Shopify Tax, Sellbrite Free, Shopify Marketplace Connect.
- Paperwork: Florida DR-1 before the first Shopify order, the Annual Resale Certificate (expires December 31), Lee County BTR $50 for an October to March start.

Pay when it earns it:
- Flippd Pro, $9.99/month or $99.99/yr: past 20 items (the gaps file counts the room at 50-plus, so month one if adopted).
- Inventory Now Personal, "$10 BILLED $120 YEARLY": three-channel stock sync from the phone, once the Nov 2, 2026 Etsy connection tests clean.
- Seller Ledger, $10 /month: hand entry becomes a chore; start the month of the first sale or prepay $100 /year.
- Sellbrite Pro 100 "$19 / month" or CedCommerce "$9/month": the 2-hour window double-sells a piece.
- NIIMBOT D110, $29.99 USD ($20.90 on sale): tagging at the rack from the phone.
- Keeper Standard, $199 /yr: Hollie wants a pro-signed return.
- My Reseller Genie Ultimate, $22.99 per month: consignment plus Etsy sync in one ledger outweighs price.

Skip: see the table's skip rows. In short: Flipwise (eBay only); QuickBooks, Wave, ZipBooks (capped or bank import paid); Found (bank switch); Zoho Expense (redundant); Everlance, MileIQ, Hurdlr (TripLog is unlimited and free); Sortly, BoxHero (an Airtable ID on an Avery label suffices); Taxomate (paid accounting file underneath); Brother QL-800 (Avery or NIIMBOT for less); Cash App Taxes (needs a Cash App account).

## Contradictions with earlier decisions

- Supabase: Flippd and Inventory Now keep the cost-basis ledger in their own cloud, while the Airtable pick is a stopgap "until the Supabase dashboard exists". Flippd Pro would be a second permanent home. Evidence: gaps table, Flippd row ("cost of goods, fees, net profit per item ... P&L and Schedule C reports"). Decide one home before paying.
- Crosslist Gold (trial): not refuted; the lane confirms "Gold $39.99 per month" unchanged, "Sales analytics" at Gold and Diamond. Two soft notes: Vendoo Starter "$12.49 Per month, billed yearly" includes "Analytics" and "Unlimited Items" (lane), so Gold is not the cheapest analytics seat; and the gaps file's Sellbrite and CedCommerce stock-sync picks may duplicate Crosslist delisting a sold piece elsewhere. No file says whether Crosslist auto-delists; the crosslister lane owns that call.
- rembg BiRefNet, Buffer Free, Canva Free, Instagram Edits, Claude Haiku drafts, Pushover, fixed Etsy shipping classes: nothing in these files.

## Check by hand

- Florida DOR registration fee: https://taxapps.floridarevenue.com/taxregistration/ . Any fee shows on the final screen of the online Florida Business Tax Application; no DOR page read states one.
- Collier County BTR fee: https://colliertaxcollector.com/faq/business-tax-faq/ (answers did not render) or 239-252-2477. Only if the room is in Collier.
- Inventory Now Etsy connection: https://www.inventorynow.com/ changelog "Version 8.12.1 ... Nov 2, 2026". Look for two-way sync complaints.
- NIIMBOT phone app: App Store listing, iPhone support; not read today.
- DR-15DSS 2026 edition: https://floridarevenue.com/Forms_library/current/dr15dss.pdf . Copy read is 2025 (R. 11/24); confirm Lee 0.5%, Collier none.
- Hurdlr Pro "$200 per year": https://university.hurdlr.com/en/articles/3703110-what-are-the-pro-features-and-how-much-does-it-cost-pro . Verify did not read it.
- Square free POS and inventory: https://squareup.com/us/en/pricing . 429 twice; unread candidate.

## Sources

- research/tools-2026-11-07/09-inventory-books-tax.md
- research/tools-2026-11-07/verify-09-inventory-books-tax.md
- research/tools-2026-11-07/gaps-09-inventory-books-tax.md
