# Lane 09: Inventory, bookkeeping, mileage and tax tools for Holliewood and Vine

Date 2026-11-07. Author: research subagent (lane 09-inventory-books-tax).
Question: Which tools track inventory, cost basis, profit, expenses, mileage and taxes for a one-person vintage reseller in Florida, and what do they cost?
Legend: V = vendor or government page read today (2026-11-07) with the fetch.sh headless browser or curl; U = unverified (snippet, roundup, memory, or the page would not load).

Method note. Pages were read with the session's fetch.sh (headless Chromium through the proxy, curl fallback). WebSearch was used to find URLs until the shared per-turn search budget ran out part-way through; after that, only direct fetches of known URLs were possible. Every price below is quoted from the vendor's own page as it rendered today. Prices are as the vendor writes them, with the billing period. "Per month, billed yearly" means the monthly figure is only available on an annual contract.

## 0. Bottom line

- Free stack that covers everything on day one: Airtable Free as the item ledger with cost basis (Ricky already has Airtable; 1,000 records per base, 1 GB of attachments per base), Zoho Books Free for the books (bank reconciliation, receipt autoscans, mileage tracking, P&L, 1 user + 1 accountant), TripLog Basic for automatic mileage ("Free forever", unlimited automatic GPS tracking), FreeTaxUSA to file (federal $0; Florida has no state income tax). Total: $0 a month.
- First paid tool, once Etsy and Shopify sales are flowing: Seller Ledger at $10 /month for up to 250 transactions a month. It imports eBay, Etsy, Shopify, Poshmark, Mercari and Amazon sales and fees. 30-day trial, no card.
- The reseller-specific inventory and bookkeeping app is My Reseller Genie. Etsy and eBay sync is only on Ultimate at $22.99 per month (monthly billing). It tracks inventory at cost, cash or accrual inventory, consignment, and gives P&L for the accountant. Web app only; the vendor recommends a computer or iPad.
- Taxes, verified on the IRS page updated 28-Oct-2026: a 1099-K comes only when payments exceed $20,000 in more than 200 transactions, but all income is reportable regardless. eBay's own page says the same for tax year 2025.
- Florida sales tax: 6% state plus county surtax (Lee 0.5% through Dec 31, 2028; Collier none, per the 2025 DR-15DSS). Etsy and eBay collect and remit as marketplace providers and Florida says a marketplace seller "must exclude sales made through the marketplace" from its own return. A Shopify site is Hollie's own responsibility: register with the Florida DOR (DR-1) before selling, then use Shopify Tax, which is free until $100,000 of lifetime sales for stores created on or after May 13, 2026, then 0.35% per order capped at $0.99.
- Registering as a Florida dealer also gives the Annual Resale Certificate, which lets Hollie buy inventory tax-free from registered sellers (estate sale companies, auction houses, dealers). It cannot be used for anything kept or used by the business or personally, and it expires December 31 each year.
- Lee County business tax receipt: $50.00 full year (Oct to Sept), prorated $25.00 or $12.50 for later starts, expires September 30, home-based businesses need the zoning affidavit. Collier County requires a county receipt for every business including home-based and inside Naples city limits; the fee did not render on their FAQ page (phone 239-252-2477).
- Label printer for SKU and QR labels: Brother QL-800 at $124.99 (USB, Windows). The wireless QL-810W is $169.99 if printing from the iPhone matters. Rollo printers ($199.99 USB, $279.99 wireless) are 4x6 shipping-label printers, not SKU label printers. Dymo's site blocked both fetch attempts today.

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| My Reseller Genie | Reseller bookkeeping: inventory at cost, sales sync from marketplaces, expenses, P&L, consignment | "Basic $11.99 per month", "Premium $16.99 per month", "Ultimate $22.99 per month" (monthly toggle) | None; "14 day money back guarantee" | Web app ("accessed on any internet-enabled device") | High: built for one-of-one resellers, Etsy + eBay sync, but Ultimate needed for any marketplace sync | V | https://discover.myresellergenie.com/ |
| Flipwise | eBay-only automation, inventory, profit, Schedule C expenses and mileage | "$19.99 /mo 100–499 listings"; "We charge based on the size of your store." | "Free Up to 24 listings (new members only)" | Web | Low until eBay matters: "Connect eBay once"; records Etsy sales only by hand | V | https://flipwise.app/pricing |
| Vendoo (inventory and analytics) | Crosslister with inventory, downloadable inventory spreadsheets, profit tracking | "STARTER $12.49 Per month, billed yearly" (includes "Analytics", "Unlimited Items"); Growth $24.99, Pro $49.99, all "billed yearly" | "Try Vendoo Free for 14 Days" | Web, mobile | Medium: crosslister lane owns the decision; analytics on every plan | V | https://www.vendoo.co/pricing |
| Crosslist (sales analytics) | Crosslister; "Sales analytics" listed at Gold and Diamond | "Gold $39.99 per month" (unchanged from 2026-10-26); Bronze $29.99, Silver $34.99, Diamond $44.99 | "20 free listings with our 3-day money-back guarantee" | Web, mobile | Medium: already the trial pick; analytics need Gold | V | https://crosslist.com/pricing |
| List Perfectly (Sales Analytics) | Crosslister; Sales Analytics, CSV download, SKU generator, inventory labels | "Business ... $49 Monthly" includes "Sales Analytics"; Simple $29 Monthly | Money-back guarantee listed, no free tier | Web, mobile | Medium: priciest of the three for analytics | V | https://listperfectly.com/pricing/ |
| Sortly | Photo inventory with QR and barcode labels | "Advanced $24 USD/mo.* Billed at $288/yr." for "500 Unique Items" | "Free $0 USD/mo. 100 Unique Items 1 User License" | Web, iOS, Android | Medium: free tier fits a small room; QR label creation is paid | V | https://www.sortly.com/pricing/ |
| BoxHero | Inventory with barcode scanning and label printing | "Business Plan ... $24 per team / month $288 annually" (1,000 items, 3 members) | Personal plan "100 items", "Free", includes "Barcode Scanning" | Web, iOS, Android | Medium: same shape as Sortly; free tier has scanning | V | https://www.boxhero.io/pricing |
| Airtable | Database with photos, forms, automations; Ricky has it | "Team $20USD per seat/month" ("$24 billed monthly") | "Free ... Unlimited bases 1,000 records per base 1 GB of attachments per base 100 automation runs" | Web, iOS, Android, Windows app | High as the free item ledger until the Supabase dashboard exists | V | https://airtable.com/pricing |
| Notion | Docs and databases; Ricky has it | "Plus $10 per member / month" | "Free $0 per member / month" | Web, iOS, Android, Windows | Medium: fine for notes and a simple ledger, weaker on photos and formulas than Airtable | V | https://www.notion.com/pricing |
| Google Sheets reseller templates | Spreadsheet ledgers with COGS, fees, profit columns | Spreadsheet Point: "three free reseller spreadsheet templates for Google Sheets"; Etsy paid templates not readable today | Free (Spreadsheet Point) | Web, iOS, Android | Medium: free and flexible; no photos, no sync | V (Spreadsheet Point), U (Etsy listings, 403) | https://spreadsheetpoint.com/templates/reseller-inventory-spreadsheet-template/ |
| QuickBooks Free | Basic income and expense tracking | "$0/mo No credit card required" | "Connect 1 bank", "Send 2 invoices per month", "Upload receipts (2 per month)", "Track mileage (5 trips per month)" | Web only ("Mobile app access and third-party integrations not currently available with QuickBooks Free") | Low: too capped, no phone app | V (curl) | https://quickbooks.intuit.com/pricing/ |
| QuickBooks Solopreneur (shown as "Lite") | Self-employed bookkeeping, receipts, mileage, Schedule C | "$20 $10/mo 50% off for 3 months*" | 30-day trial | Web, iOS, Android | Medium: "No accountant access"; built "instead of broader team and inventory features" | V (curl) | https://quickbooks.intuit.com/solopreneur/ |
| QuickBooks Simple Start | Full small-business books | "$38 $19/mo 50% off for 3 months*" | 30-day trial | Web, iOS, Android | Low: price above the budget for no inventory | V (curl) | https://quickbooks.intuit.com/pricing/ |
| Wave | Free invoicing and bookkeeping; paid bank import and receipts | "PRO Plan $190USD/year Billed annually"; receipts add-on "$8/month OR $72/year"; card payments "2.9% + $0.60 per credit card transaction" | "STARTER Plan $0 ... Create unlimited estimates, invoices, bills, and bookkeeping records" | Web, iOS, Android | Medium: free books by hand; bank auto-import only on Pro | V | https://www.waveapps.com/pricing |
| Xero | Small-business accounting | "Early $5.40 per month for the first 3 months Then $27 per month" | 30-day trial, "Get one month free" | Web, iOS, Android | Low: no free tier, no reseller inventory | V | https://www.xero.com/us/pricing-plans/ |
| Zoho Books | Accounting with bank reconciliation, receipts, mileage | "STANDARD $20 $15 Price/Org/Month Billed Annually" | "FREE $0 ... Receipt and Document Autoscans ... Mileage tracking ... Bank reconciliation ... P&L, Balance Sheet & 50+ Reports ... 1 User + 1 Accountant" | Web, iOS, Android, Windows | High: the strongest free books tier read today | V | https://www.zoho.com/us/books/pricing/ |
| FreshBooks | Invoicing-first accounting | "Lite $4.60 USD/mo 80% Off for 4 Months Was $23.00" | 30-day trial | Web, iOS, Android | Low: "Send invoices to 5 clients"; service-business shape | V | https://www.freshbooks.com/pricing |
| Found | Business bank account with built-in bookkeeping and tax tools | "Found Plus $35/mo; $315/yr"; "Found Pro $80/mo; $720/yr" | "$0/mo Your banking, bookkeeping, and tax platform" incl. "Scan receipt", "Mileage and home office deduction tracking", "Real-time tax estimates" | Web, iOS, Android | Medium: free and complete, but only if Hollie banks with Found | V (curl) | https://found.com/pricing |
| Seller Ledger | Bookkeeping for online sellers: imports eBay, Etsy, Shopify, Poshmark, Mercari, Amazon | "Up to 250 transactions per month $10 /month $100 /year" | "30-day free trial No credit card required" | Web | High: cheapest marketplace-native books; "Every Seller Ledger customer gets every feature" | V | https://sellerledger.com/pricing/ |
| A2X | Posts marketplace payouts into QuickBooks Online or Xero | "Etsy ... starting at: US$ 29 / MO"; Shopify and eBay also "US$ 29 / MO" each | "Try A2X for free" (trial) | Web (connector) | Low: needs paid QBO or Xero underneath; per-channel pricing | V | https://www.a2xaccounting.com/pricing |
| Link My Books | Same idea as A2X; UK vendor | Page renders in GBP ("£0/month" slider start); USD price not shown | "14-Day Free Trial" | Web (connector) | Low: UK-priced, needs Xero or QuickBooks | U (price) | https://linkmybooks.com/pricing |
| Nifty | Poshmark and eBay automation plus crosslisting and an inventory manager | "Bundle Plus ($62.99/month): Inventory manager" | "7-day free trial" | Web, mobile | Low: automation bots for Poshmark; over budget | V | https://nifty.ai/pricing |
| Zoho Inventory | Multi-channel stock control for SKUs with quantities | "STANDARD $ 29 per organization / month billed annually" | "Free 50 orders 1 user 1 location" | Web, iOS, Android | Low: built for quantity stock and reorder points | V | https://www.zoho.com/us/inventory/pricing/ |
| Stocksmith (was Craftybase) | Maker inventory with bill of materials | "Studio is $41/mo"; Indie "$99" monthly or "$83 USD/mo $990/yr, billed annually" | "Free 14 day trial" | Web | Low: "Craftybase → Stocksmith"; recipes and materials, not resale | V | https://stocksmith.io/pricing/ |
| Inventora | Maker inventory (Shopify, Etsy) | Pricing page 404 today | "Try Inventora free for 7 days" | Web | Low: maker focus | U (price) | https://inventora.com/ |
| Everlance | Automatic mileage, expenses, tax filing | "Starter $89.99 Per year or $10.99 per month"; "Professional $119.99 Per year or $19.99 per month" | "Basic ... $0 ... 30 automatically tracked trips a month Unlimited manually tracked trips" | iOS, Android, web dashboard | Medium: free tier covers sourcing runs if under 30 trips a month | V | https://www.everlance.com/pricing |
| MileIQ | Automatic mileage | "Unlimited $11.66 PER MONTH BILLED ANNUALLY" | "Free $0 40 FREE DRIVES EVERY MONTH" | iOS, Android, web | Medium: 40 free drives a month; owner now Bending Spoons | V | https://mileiq.com/pricing |
| TripLog | Automatic mileage, basic expenses | "Premium ... $4.99 Per month Paid annually" ("Paid annually as $59.99") | "Basic Unlimited automatic GPS mileage tracking & basic expense management ... Free forever" | iOS, Android, web | High for free mileage: unlimited automatic tracking at $0 | V | https://www.triplog.net/pricing |
| Hurdlr | Mileage, expenses, tax estimates; Pro adds filing | "Hurdlr Premium Pricing: -$100 annual plan ($8.34 a month, most popular) -$9.99 month-to-month plan"; "Hurdlr Pro is $200 per year" | Free: "unlimited semi-auto mileage tracking, manual finance tracking, and real-time tax estimates" | iOS, Android, web | Medium: free tier is semi-automatic | V (help center; pricing page shows no prices) | https://university.hurdlr.com/en/articles/1072143-what-are-the-premium-features-and-how-much-do-they-cost |
| Stride | Free mileage and expense tracker funded by insurance commissions | "All for free with no hidden fees." (Google Play listing) | Free | iOS, Android | Medium: free, but stridehealth.com walled both fetches today; Play listing shows 3.0 stars from 20.9K reviews | U (vendor site unreadable today; Play text came from a curl pull earlier today) | https://play.google.com/store/apps/details?id=com.stridehealth.stride |
| Keeper | Bookkeeping plus tax filing with a pro | "Bookkeeping Only $20/mo"; "Standard $199 /yr $16.58/mo, billed yearly" ("Federal + up to 2 state returns") | "14-day free trial" | iOS, Android, web | Medium: $199 a year is a fair all-in filing price, no inventory | V | https://www.keepertax.com/pricing |
| Expensify | Receipt scanning | "Collect $5 per member/month" | "Individuals can use New Expensify for free with unlimited SmartScans" | iOS, Android, web | Medium: free scans, but "expense categorization requires a paid plan" | V | https://www.expensify.com/pricing |
| Shoeboxed | Receipt scanning incl. mail-in envelopes, mileage | "Starter — $97/year ($8.08/mo) or $9/month. 50 digital scans/month" | "Try Risk-Free for 30 Days" (money-back) | iOS, Android, web | Low: paper mail-in is the differentiator; not needed | V | https://www.shoeboxed.com/pricing |
| Dext | Receipt and invoice capture for accountants | "$25.21 Per Month USD, Excludes Tax, $302.50 billed annually 250 Documents Per Month 5 Users" | "Start a free trial" | iOS, Android, web | Low: accountant tooling, over budget | V (home page; /us/pricing returned 404) | https://dext.com/us |
| Zoho Expense | Receipts with OCR, GPS mileage | "STANDARD $3 per user/month billed annually" | "FREE $0 ... Maximum users: 3 ... Receipt capture with AI-powered OCR ... Mileage expenses via GPS ... 5 GB receipt storage" | iOS, Android, web | Medium: free; overlaps Zoho Books Free | V | https://www.zoho.com/us/expense/pricing/ |
| FreeTaxUSA | Tax filing incl. Schedule C | "Federal Tax Returns Free", "State Tax Returns $15.99" | Free federal | Web | High: Florida has no state income tax, so $0 | V | https://www.freetaxusa.com/pricing/ |
| Shopify Tax | Sales tax calculation on a Shopify store | "Lifetime sales threshold $100,000 USD Maximum fee per order $0.99 USD"; "United States 0.25% [Plus] 0.35% [Basic, Grow, or Advanced]" | Free until the threshold | Shopify (built in) | High: the only thing the Shopify site needs for tax math | V | https://help.shopify.com/en/manual/taxes/shopify-tax/pricing |
| Brother QL-800 | Desktop label printer for SKU and QR labels (DK rolls) | "$124.99" | n/a (hardware) | Windows, Mac (USB) | High for labels | V | https://www.brother-usa.com/p/desktop-label-printers/QL800 |
| Brother QL-810W | Same, wireless | "$169.99" | n/a | Windows, Mac, iOS, Android (Wi-Fi) | Medium: pay $45 more only for iPhone printing | V | https://www.brother-usa.com/p/desktop-label-printers/QL810W |
| Rollo | Thermal shipping-label printers | "Rollo Wireless Label Printer $279.99", "Rollo USB Label Printer $199.99" | n/a | Windows, Mac, iOS, Android | Low for SKU labels (shipping lane) | V | https://www.rollo.com/shop/ |
| Dymo LabelWriter 550 | Desktop label printer | Site returned HTTP 403 twice | n/a | Windows, Mac | U | U | https://www.dymo.com/ |

Government and marketplace facts (not tools):

| Fact | Verbatim quote | V/U | Source URL |
|---|---|---|---|
| IRS 1099-K threshold | "required to report payments on Form 1099-K when the total amount of payments you receive for goods or services through the platform exceeds $20,000 in more than 200 transactions" (page updated 28-Oct-2026) | V | https://www.irs.gov/businesses/understanding-your-form-1099-k |
| eBay 1099-K | "2025 reporting threshold Gross payments exceeding $20,000 and More than 200 transactions" | V | https://www.ebay.com/help/selling/fees-credits-invoices/ebay-form-1099k?id=4794 |
| Etsy collects sales tax | "Etsy automatically calculates, collects, and remits US sales tax on behalf of sellers"; "Sellers can't opt out" | V | https://help.etsy.com/hc/en-us/articles/360000343968 |
| eBay collects in Florida | Florida section links a "Florida Marketplace Facilitator Certificate" | V | https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121 |
| Florida state rate | "Florida's general state sales tax rate is 6%" | V | https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx |
| County surtax | Lee ".5% Jan 1, 2019 Dec 31, 2028"; "Collier None" (DR-15DSS for 2025, R. 11/24) | V | https://floridarevenue.com/Forms_library/current/dr15dss.pdf |
| Marketplace seller rule | "the marketplace seller may not collect the tax and must exclude sales made through the marketplace from the marketplace seller's tax return" | V | https://floridarevenue.com/taxes/tips/Documents/TIP_21A01-03.pdf |
| Register before selling | "you must register as a sales and use tax dealer to collect, report, and remit sales and use tax before you begin conducting business in Florida" | V | https://floridarevenue.com/taxes/eservices/Pages/registration.aspx |
| Resale certificate | "allows business owners ... to buy or rent property or services tax free when the property or service is resold"; expires December 31 | V | https://floridarevenue.com/taxes/taxesfees/Pages/annual_resale_certificate_sut.aspx |
| Lee County BTR fee | "Full Year Fee (Oct – Sept): $50.00 Half Year Fee (Apr – Jun): $25.00 Quarter Year Fee (Jul – Sept): $12.50" | V | https://leetc.com/wp-content/uploads/2026/06/Business-Tax-Application-ADA062026.pdf |
| Lee County BTR term | "All business tax receipts expire September 30 of each year and can be renewed after July 1." | V | https://leetc.com/businesses/business-tax-guide-and-applications/ |
| Collier County BTR | "All businesses operating in Collier County, including those within Naples, Marco Island, or Everglades city limits, must obtain a county business tax receipt." Fee not shown. | V (requirement), U (fee) | https://colliercountyfl.qscend.com/311/knowledgebase/article/698 |

## 2. Notes per tool

My Reseller Genie (V). Three plans on the discover page, monthly toggle: Basic $11.99, Premium $16.99, Ultimate $22.99 per month. The FAQ says "Poshmark, eBay, Mercari, Whatnot, Etsy, Depop, and Vinted integration included in the Ultimate plan" and "bank, Paypal, and credit card integration included in the Premium and Ultimate plans", so Etsy sync costs $22.99 a month. Extra eBay accounts are "+$5/account". Supports "cash inventory and accrual inventory methods", consignment tracking, bulk matching of sales to inventory, P&L downloads for the accountant, CSV import from Vendoo or List Perfectly. Platform: "a web app that can be accessed on any internet-enabled device (we recommend using a device with a larger screen such as a computer or iPad". No native iPhone app. Refund: "If you cancel within the first 14 days of subscribing, email us and we will refund your money." Data on Google Firestore, bank links through Plaid, payments through Stripe. The main /pricing page rendered no prices today (they load from a widget); the discover landing page has them.

Flipwise (V). "Connect eBay once and your real numbers fill themselves in." Store size pricing: free for "Up to 24 listings (new members only)", "$19.99 /mo 100–499 listings"; the slider tier for 25 to 99 listings did not render as text. Features: unlisted inventory, lot cost splitting ("Enter what you paid once and Flipwise splits the cost across every item"), Schedule C expense categories, "Mileage tracking", cash or accrual reports. Other channels: "Record Amazon, Poshmark, Mercari, Etsy or offline sales right alongside eBay" by hand. 7-day money-back. Fit: eBay-first sellers; Hollie is Etsy-first.

Vendoo (V). Prices shown are "Per month, billed yearly": Starter $12.49, Growth $24.99, Pro $49.99. The monthly-billing toggle did not render. Starter includes "Unlimited Items", "Analytics", "Importing", "Delist & Relist"; the comparison grid lists "Downloadable Inventory Spreadsheets", "Inventory Management", "Profit Tracking & Business Analytics". Page states "Vendoo is Tax-Deductible. Please consult with your tax advisor." Crosslisting decision belongs to another lane.

Crosslist (V). Bronze $29.99, Silver $34.99, Gold $39.99, Diamond $44.99 per month (monthly toggle). "Sales analytics" appears under Gold and Diamond only. Gold's price matches the 2026-10-26 figure. Add-on "+$4.99/month" per tier for extra AI credits. Trial: "3 days of Crosslist® or 20 free listings, whichever comes first"; annual refunds carry "a $9.99 processing fee".

List Perfectly (V). Simple $29, Business $49, Pro $69, Pro Plus $99+ Monthly. "Sales Analytics" and "CSV Download" start at Business. Inventory tools include "SKU Generator", "Inventory Labels", "Pick List", "Stale Listings".

Sortly (V). Free: "$0 USD/mo. 100 Unique Items 1 User License 2 Active Jobs". Advanced: "$24 USD/mo.* ... Billed at $288/yr." for 500 unique items with "Unlimited QR Code Label Creation". Barcode label creation starts at Ultra ($74 USD/mo, billed $888/yr). In-app scanning is on the grid; QR label creation is paid. A shop of 100 or fewer live pieces fits the free tier; Hollie's catalogue is already around that size.

BoxHero (V). Personal plan: "100 items", "Free", with "Barcode Scanning. Use your phone or a barcode scanner". Business: "$24 per team / month $288 annually" with 1,000 items, 3 members, "Custom Barcode Printing". Add-ons only on Business: "$5 per member / month", "$10 per 1,000 items / month". Trial: "No credit card required during trial period."

Airtable (V). Free: "Unlimited bases 1,000 records per base 1 GB of attachments per base 100 automation runs". Team: "$20USD per seat/month" annual, "$24 billed monthly". Gotcha: 1 GB of attachments fills fast with product photos; keep originals in Drive and store links or small previews. Ricky already has an account.

Notion (V). Free "$0 per member / month" with databases; "File uploads" and "Charts" are listed under Plus "$10 per member / month". The FAQ mentions a "block storage limit on a Free Plan" but the text did not render. Fine for notes and procedures; a weaker ledger than Airtable.

Google Sheets templates (V for Spreadsheet Point; U for Etsy). Spreadsheet Point offers "three free reseller spreadsheet templates for Google Sheets" and lists the columns a ledger needs: "Purchase date and purchase price (COGS)", "Listing date and status (listed, sold, returned, donated)", "Fees and shipping cost so net profit stays accurate", "Profit and profit margin". Etsy listing pages for paid templates returned HTTP 403 and a Payhip listing hit a Cloudflare wall, so paid template prices are unverified.

QuickBooks (V, curl; headless browser got HTTP 502). Free plan: "$0/mo No credit card required", "1 user", "No accountant access", "Connect 1 bank", "Send 2 invoices per month", and on the Solopreneur page "Upload receipts (2 per month)", "Track mileage (5 trips per month)". Footnote: "Mobile app access and third-party integrations not currently available with QuickBooks Free." The Solopreneur page shows the paid tier labelled "Lite": "$20 $10/mo 50% off for 3 months*", "No accountant access", "Unlimited receipts and mileage", "Mobile app". The FAQ: Solopreneur "focuses on essentials like automated transaction sorting, goals, and tax-readiness instead of broader team and inventory features." Simple Start: "$38 $19/mo 50% off for 3 months*" with "access for 2 accountants". Essentials $85, Plus $140 (Plus has inventory, far over budget).

Wave (V). Starter: "$0", "Create unlimited estimates, invoices, bills, and bookkeeping records", card payments "2.9% + $0.60 per credit card transaction", "3.4% + $0.60 per Amex transaction". Pro: "$190USD/year Billed annually" adds "Auto-import bank transactions", "Digitally capture unlimited receipts". Receipts alone: "ADD-ON $8/month OR $72/year". Gotcha: on Starter every bank transaction is typed by hand.

Xero (V). "Early $5.40 per month for the first 3 months Then $27 per month"; Growing $59, Established $97 after promo. No free tier.

Zoho Books (V). Free "$0" plan lists "Receipt and Document Autoscans", "Mileage tracking", "Bank reconciliation", "Accept online payments", "P&L, Balance Sheet & 50+ Reports", "1 User + 1 Accountant", "Email Support". Standard "$20 $15 Price/Org/Month Billed Annually" (the page shows both the monthly and annual figure). Inventory tracking starts at Professional ($50 monthly, $40 annual) and is quantity-based. For a one-person shop the Free plan is the most complete $0 bookkeeping read today.

FreshBooks (V). Lite "$4.60 USD/mo 80% Off for 4 Months Was $23.00"; "Send invoices to 5 clients". Invoice-first for service work. Skip.

Found (V, curl). Free: "$0/mo Your banking, bookkeeping, and tax platform", "Categorize expenses, scan receipts, view P&L", "Real-time tax estimates", "Mileage and home office deduction tracking", "Unlimited free invoicing". Plus "$35/mo; $315/yr", Pro "$80/mo; $720/yr". Gotcha: it is a bank account; the bookkeeping only sees money that moves through Found.

Seller Ledger (V). "Every Seller Ledger customer gets every feature. Your price is based only on your monthly billable transaction volume." Tiers: "Up to 250 transactions per month $10 /month $100 /year", 1,000 for $20, 5,000 for $50. Channels on the page: Amazon, eBay, Shopify, Etsy, Poshmark, Mercari. Overage: "We simply charge you the difference between the higher tier and the one you are on." Trial: "30-day free trial No credit card required", "up to 90 days of transaction history"; yearly prepay imports "back to Jan 1 of the most current tax year". No per-item inventory at cost on the pricing page; it is books, not an inventory ledger.

A2X (V). "Etsy ... starting at: US$ 29 / MO", Shopify and eBay also from US$29 each. Requires QuickBooks Online, Xero or NetSuite. Three channels would be about $87 a month plus the accounting subscription. Skip.

Link My Books (U for price). Page renders in GBP with a "£0/month" slider; supports "eBay Shopify Etsy" to "Xero QuickBooks". UK vendor. Skip.

Nifty (V). "Full Automation ($35.99/month)" for Poshmark, eBay, Mercari, Depop sharing and relisting; "Bundle Plus ($62.99/month): Inventory manager". Automation of marketplace actions is a terms-of-service risk and the price is over budget. Skip.

Zoho Inventory (V). "Free 50 orders 1 user 1 location"; Standard "$ 29 per organization / month billed annually" for 500 orders. Built for quantity SKUs, reorder points and warehouses. Low fit.

Stocksmith, formerly Craftybase (V). Banner: "Craftybase → Stocksmith · Same team, same software, just a new name." Studio "$41/mo"; Indie "$99" monthly or "$83 USD/mo $990/yr, billed annually". Bill of materials for makers. Skip.

Inventora (U). /pricing returned 404; home page says "Try Inventora free for 7 days", Shopify and Etsy integrations, maker focus. Skip.

Everlance (V). Basic "$0 ... 30 automatically tracked trips a month Unlimited manually tracked trips". Starter "$89.99 Per year or $10.99 per month". Professional "$119.99 Per year or $19.99 per month" adds "Automatic expense tracking", "Free tax filing", "$1 million dollar audit defense". Gotchas: the 7-day trial needs a card ("You will need to enter your credit card"), and "all sales are non-refundable".

MileIQ (V). Free "40 FREE DRIVES EVERY MONTH". Unlimited "$11.66 PER MONTH BILLED ANNUALLY"; no month-to-month price shown. Footer: "© 2026 Bending Spoons Operations S.p.A."

TripLog (V). Basic: "Unlimited automatic GPS mileage tracking & basic expense management ... Free forever". Premium "$4.99 Per month Paid annually" ("Paid annually as $59.99") adds unlimited reporting, OCR receipts, bank integration. Optional hardware "TripLog Drive $79.99". Best free mileage tier read today.

Hurdlr (V via help center). hurdlr.com/pricing redirects to the home page with no prices. Help articles: free version has "unlimited semi-auto mileage tracking, manual finance tracking, and real-time tax estimates"; Premium "$100 annual plan ($8.34 a month, most popular)" or "$9.99 month-to-month plan"; Pro "$200 per year" including "Annual tax filing (federal + 1 state)". Articles dated November 2023 and May 2024, so treat as current but unrefreshed.

Stride (U). stridehealth.com returned zero bytes on two fetches (bot wall), the Apple App Store and Google Play URLs returned 404 today. A curl pull of the Google Play listing made earlier today in this session reads "Save an average of $710/year on taxes by using Stride! All for free with no hidden fees." and shows "3.0star 20.9K reviews". Stride is funded by insurance commissions. Free, but unverified from the vendor's own site today.

Keeper (V). "Bookkeeping Only $20/mo"; Standard "$199 /yr $16.58/mo, billed yearly" with "Federal + up to 2 state returns", "Reviewed & signed by a tax pro"; Premium "$399 /yr". Features: "Connect unlimited bank and card accounts", "Scan receipts", "Track mileage". "Try any plan free for 14 days".

Expensify (V). "Individuals can use New Expensify for free with unlimited SmartScans, but additional functionality such as expense categorization requires a paid plan." Collect "$5 per member/month". Good as a free receipt camera that emails PDFs, nothing more.

Shoeboxed (V). "Starter — $97/year ($8.08/mo) or $9/month. 50 digital scans/month, 20 paper scans/year, 1 Magic Envelope/year, unlimited mileage tracking". Overkill unless paper receipts pile up.

Dext (V, home page). "$25.21 Per Month USD, Excludes Tax" or "$302.50 billed annually" for "250 Documents Per Month 5 Users". The /us/pricing and /en-us/pricing URLs returned a 404 page ("Something doesn't add up"). Accountant tooling. Skip.

Zoho Expense (V). Free: "Maximum users: 3", "Receipt capture with AI-powered OCR", "Mileage expenses via GPS", "5 GB receipt storage". Standard "$3 per user/month billed annually". Redundant if Zoho Books Free is used, since Books has autoscans and mileage.

FreeTaxUSA (V). "Federal Tax Returns Free", "State Tax Returns $15.99", "Amended Tax Returns $16.98". Self-employed and 1099 situations are listed at "$0 + $15.99 per state". Florida has no personal income tax, so a Florida filer pays nothing.

Shopify Tax (V). "Shopify Tax pricing depends on when your store was created." Stores created on or after May 13, 2026: free until a "Lifetime sales threshold $100,000 USD", then "United States 0.25% [Shopify Plus] 0.35% [Basic, Grow, or Advanced]" with "Maximum fee per order $0.99 USD". Older stores get the $100,000 threshold per calendar year. "Fees are charged only in regions ... where you've activated tax collection." Charged on the Shopify invoice, "isn't charged to your customers".

Label printers (V except Dymo). Brother QL-800 "$124.99" (USB; prints black/red DK labels; up to 93 labels per minute). Brother QL-810W "$169.99" (wireless). Rollo shop page: "Rollo Wireless Label Printer $279.99", "Rollo USB Label Printer $199.99"; Rollo is a 4x6 shipping printer and its Rollo Ship software is "no monthly fee". Dymo: HTTP 403 on the product page and the home page, so LabelWriter 550 price is unverified.

Government pages (V). IRS: threshold "exceeds $20,000 in more than 200 transactions"; "No matter the amount of reported payments ... you must report all income"; this "includes payments for any goods you sell (including personal items such as clothing or furniture sold at a gain)". eBay: "Form 1099-K ... does not include any adjustments, for example, credits, discounts, fees, refunds", so gross will exceed net. Florida DOR: 6% state rate; "The county surtax rate applies to a taxable item or service delivered into a county imposing a surtax"; DR-15DSS is "updated yearly in November" (the copy read is the 2025 edition, R. 11/24; check the 2026 edition when posted). Resale certificate may not be used for property "used ... but not resold" or "for personal purposes, such as furniture, office equipment, computers, or supplies"; "There are criminal and civil penalties for the fraudulent use of a resale certificate"; if a tax-free purchase is later kept, "you must report and pay use tax on the item". Marketplace rule (TIP 21A01-03): "the marketplace seller may not collect the tax and must exclude sales made through the marketplace from the marketplace seller's tax return". Lee County: $50.00 full year, prorated, "expire September 30", online card payment "2.35% service fee ($1.85 minimum) per transaction", home-based businesses "complete the Home/Truck affidavit" if on the zoning exemption list. Collier County: county receipt required everywhere in the county including inside Naples; the Tax Collector FAQ page lists the question "What is required to open a business from your home in Collier County?" but the answers did not render; fee unknown; "239-252-2477 or email btr@colliertax.com".

## 3. Recommendation for Hollie

Free first, today:
1. Airtable Free as the item ledger. One base, one table: ID, name, photo link (not the file), source, purchase date, cost, repair or cleaning cost, listed date, listed price, channel, sold date, sold price, fees, shipping, net. 1,000 records per base is plenty. Use the Spreadsheet Point column list as the checklist. This is a stopgap until the Supabase dashboard carries the same fields.
2. Zoho Books Free for the books. Connect the business bank card, let it reconcile, snap receipts with its autoscan, log mileage in it or in TripLog. Invite the accountant as the free accountant seat.
3. TripLog Basic on the iPhone for automatic sourcing mileage at $0. Everlance Free (30 auto trips a month) or MileIQ Free (40 drives a month) are fine alternatives. Stride is free but could not be verified from its own site today.
4. FreeTaxUSA at filing time: federal $0, no Florida state return.
5. Paperwork, no software: register with the Florida DOR as a sales and use tax dealer (Form DR-1 online) before the Shopify site takes its first order, print the Annual Resale Certificate it unlocks, carry it to estate sales and auction houses, and buy the Lee County business tax receipt ($50 full year; $25 if starting April to June). If the room is in Collier, the county receipt is required too; call 239-252-2477 for the fee.
6. Turn on Shopify Tax when the Shopify store opens. It costs nothing until $100,000 of lifetime sales.

Pay only once it earns it:
- Seller Ledger, $10 /month, when Etsy plus Shopify produce enough orders that hand entry in Zoho Books becomes a chore. It pulls fees and payouts from eBay, Etsy and Shopify into one P&L. 30-day trial, no card.
- My Reseller Genie Ultimate, $22.99 per month, if per-item cost basis, sold-through analytics by category or source, and consignment tracking matter more than general bookkeeping. It overlaps Seller Ledger; choose one. Try it in a month with heavy sourcing; refund window is 14 days.
- Brother QL-800, $124.99 one-time, when the room needs SKU or QR tags on every piece. Pair it with the free Sortly or BoxHero tier (100 items) only if a phone-scan workflow is wanted; otherwise the Airtable ID on the label is enough.
- Keeper Standard, $199 a year, only if Hollie wants a pro to review and sign the return. FreeTaxUSA handles a Schedule C for $0 otherwise.

Skip and why:
- Flipwise: eBay only, and Hollie is Etsy-first.
- QuickBooks Free (no phone app, 2 receipts a month), Simple Start ($38), Xero ($27), FreshBooks (5 clients): priced or shaped for other businesses.
- A2X and Link My Books: connectors that need a paid accounting system underneath.
- Zoho Inventory, Stocksmith, Inventora: built for quantity stock and makers, not one-of-one resale.
- Nifty: marketplace automation bots, over budget.
- Dext, Shoeboxed: accountant-grade receipt pipelines; Zoho Books Free and Expensify Free already scan receipts.
- Found: only makes sense if Hollie wants to switch business banking to Found.
- Rollo for SKU labels: it is a shipping-label printer (shipping lane decides).

## 4. Gaps and pages that would not load

- WebSearch budget for the turn ran out after about ten searches, so Dymo, Collier fee, barcode-app and receipt-app roundups were not searched; those sections rely on seed URLs and direct fetches.
- My Reseller Genie /pricing renders its plan table from a widget that printed no prices; prices were taken from the vendor's discover.myresellergenie.com landing page and FAQ.
- Flipwise: the price tier for 25 to 99 listings did not render (slider).
- Vendoo: only "billed yearly" prices rendered; monthly-billing prices unknown.
- Stride: stridehealth.com and stridehealth.com/tax returned zero bytes (bot wall); Apple App Store and Google Play URLs returned 404 on direct fetch. The Google Play text quoted came from a curl pull made earlier today in this session's scratchpad.
- Hurdlr: hurdlr.com/pricing redirects to the home page with no prices; help-center articles supplied the prices.
- Dext: /us/pricing and /en-us/pricing returned a 404 page; the home page carried the Business price.
- Dymo: www.dymo.com and the LabelWriter 550 product page returned HTTP 403.
- Etsy listing pages for Google Sheets templates returned HTTP 403; Payhip returned a Cloudflare challenge.
- QuickBooks pricing pages returned HTTP 502 to the headless browser; plain curl worked and was used.
- Florida DOR "Taxation of Remote Sales" page: four guessed URLs returned 404; the TIP 21A01-03 PDF and the registration page covered the marketplace rule instead.
- Collier County Tax Collector: the Business Tax FAQ page lists questions but the answers and fee schedule did not render; fee unverified.
- Rollo product page returned 404; the shop page supplied prices.
- Inventora /pricing returned 404.
- Notion Free plan file-upload and block limits did not render in the FAQ.
- Link My Books prices render in GBP only.
- DR-15DSS read is the 2025 edition (R. 11/24); the 2026 edition is published each November and was not located.

## 5. Sources

Read successfully today (V):
https://www.myresellergenie.com/pricing
https://discover.myresellergenie.com/
https://www.myresellergenie.com/faqs
https://flipwise.app/pricing
https://www.vendoo.co/pricing
https://crosslist.com/pricing
https://listperfectly.com/pricing/
https://www.sortly.com/pricing/
https://airtable.com/pricing
https://www.notion.com/pricing
https://quickbooks.intuit.com/pricing/ (curl)
https://quickbooks.intuit.com/solopreneur/ (curl)
https://www.waveapps.com/pricing
https://www.xero.com/us/pricing-plans/
https://www.zoho.com/us/books/pricing/
https://www.freshbooks.com/pricing
https://found.com/pricing (curl)
https://linkmybooks.com/pricing
https://www.everlance.com/pricing
https://mileiq.com/pricing
https://www.keepertax.com/pricing
https://www.expensify.com/pricing
https://www.shoeboxed.com/pricing
https://dext.com/us
https://university.hurdlr.com/en/articles/1072143-what-are-the-premium-features-and-how-much-do-they-cost
https://university.hurdlr.com/en/articles/3703110-what-are-the-pro-features-and-how-much-does-it-cost-pro
https://university.hurdlr.com/en/collections/2848814-subscriptions-premium-and-pro (curl, link list only)
https://www.triplog.net/pricing (redirect from https://triplogmileage.com/pricing/)
https://www.zoho.com/us/expense/pricing/
https://www.freetaxusa.com/pricing/
https://www.irs.gov/businesses/understanding-your-form-1099-k
https://www.ebay.com/help/selling/fees-credits-invoices/ebay-form-1099k?id=4794
https://www.ebay.com/help/selling/fees-credits-invoices/taxes-import-charges?id=4121
https://help.etsy.com/hc/en-us/articles/360000343968-How-US-State-Sales-Tax-and-Fees-Applies-to-Etsy-Orders
https://help.shopify.com/en/manual/taxes/shopify-tax/pricing
https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx
https://floridarevenue.com/taxes/taxesfees/Pages/annual_resale_certificate_sut.aspx
https://floridarevenue.com/taxes/eservices/Pages/registration.aspx
https://floridarevenue.com/taxes/tips/Documents/TIP_21A01-03.pdf (curl + pdftotext)
https://floridarevenue.com/Forms_library/current/dr15dss.pdf (curl + pdftotext)
https://leetc.com/businesses/business-tax-guide-and-applications/
https://leetc.com/wp-content/uploads/2026/06/Business-Tax-Application-ADA062026.pdf (curl + pdftotext)
https://leetc.com/fees/
https://colliercountyfl.qscend.com/311/knowledgebase/article/698
https://colliertaxcollector.com/faq/business-tax-faq/
https://www.brother-usa.com/p/desktop-label-printers/QL800
https://www.brother-usa.com/p/desktop-label-printers/QL810W
https://www.rollo.com/
https://www.rollo.com/shop/
https://www.boxhero.io/pricing
https://stocksmith.io/pricing/ (redirect from https://craftybase.com/pricing)
https://stocksmith.io/ (redirect from https://craftybase.com/)
https://www.zoho.com/us/inventory/pricing/
https://sellerledger.com/pricing/
https://nifty.ai/pricing
https://www.a2xaccounting.com/pricing
https://spreadsheetpoint.com/templates/reseller-inventory-spreadsheet-template/
https://inventora.com/ (redirect from https://www.inventora.co/)
https://support.stridehealth.com/hc/en-us (index only)
https://play.google.com/store/apps/details?id=com.stridehealth.stride (curl pull earlier today in this session; direct re-fetch returned 404)

Would not load today (U):
https://www.stridehealth.com/tax (0 bytes)
https://www.stridehealth.com/ (0 bytes)
https://play.google.com/store/apps/details?id=com.stridehealth.stride&hl=en_US (404)
https://apps.apple.com/us/app/stride-mileage-tax-tracker/id1052454566 (404)
https://apps.apple.com/us/app/hurdlr-mileage-expense-tax/id953002197 (404)
https://www.hurdlr.com/pricing (redirects to home page, no prices)
https://dext.com/us/pricing (404 page)
https://dext.com/en-us/pricing (404 page)
https://www.dymo.com/label-makers-printers/labelwriter-550-label-printer/SP_2112552.html (403)
https://www.dymo.com/ (403)
https://www.etsy.com/listing/4536854443 (403)
https://payhip.com/b/JhGuL (Cloudflare challenge)
https://www.inventora.co/pricing (404)
https://www.rollo.com/products/rollo-wireless-printer (404)
https://floridarevenue.com/taxes/taxesfees/Pages/remote_sales.aspx (404)
https://floridarevenue.com/taxes/taxesfees/Pages/remote_sellers.aspx (404)
https://floridarevenue.com/RemoteSellers/Pages/default.aspx (404)
https://floridarevenue.com/taxes/businesses/Pages/remote_sales.aspx (404)
https://quickbooks.intuit.com/pricing/ via headless browser (502; curl succeeded)
