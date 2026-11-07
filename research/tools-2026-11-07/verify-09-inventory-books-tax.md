# Verify lane 09: inventory, bookkeeping, mileage and tax tools

Date: 2026-11-07. Author: research subagent (adversarial price and claim checker).
Question: do the prices, free tiers, platform claims and availability claims recorded by the first lane-09 agent hold up against the vendors' own pages read today?
Legend: V = vendor page read today; U = unverified (snippet, memory, or the page would not load).
Verdicts: confirmed = the exact figure or claim is on the page read today; refuted = the page says something different; unreadable = the page would not load after one alternative, or the claim is not stated on any page that loaded.

Method: every page was read with the session fetch helper (headless Chromium through the proxy, curl fallback) or plain curl, between 22:55 and 23:15 UTC on 2026-11-07. Pages that only render check marks (My Reseller Genie) were re-read from the raw HTML so that struck-through items could be told apart from included ones. WebSearch's shared budget ran out partway through, so the Florida, Lee County and QuickBooks alternates were found by direct URL and by listing links on the sites themselves. Twenty-one checks in all: the eight PICKS plus thirteen of the highest-fit TOOLS.

## 1. Checks

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| Airtable Free | Free; 1,000 records per base; Team $20 per seat/month annual, $24 monthly | confirmed (V) | "Free includes: ... Unlimited bases 1,000 records per base Up to 5 editors 1 GB of attachments per base 100 automation runs" and "$20USD per seat/month billed annually ... $24 billed monthly" | https://airtable.com/pricing | None. Free also lists "iOS and Android mobile apps" and 500 AI credits per editor each month. |
| Zoho Books Free | $0; receipt autoscans, mileage tracking, bank reconciliation, P&L; 1 user + 1 accountant; Standard $20 monthly / $15 billed annually | confirmed (V) | "FREE ... $0 ... Receipt and Document Autoscans ... Mileage tracking ... Bank reconciliation ... P&L, Balance Sheet & 50+ Reports ... 1 User + 1 Accountant" | https://www.zoho.com/us/books/pricing/ | None. Note "Add-ons are not supported in the FREE plan, except for Document autoscans." Bank feeds are Standard. "Connect online sales channels (Etsy, eBay, Amazon)" is Elite ($150 monthly, $120 annual) only. |
| TripLog Basic | Unlimited automatic GPS mileage tracking, free forever; Premium $4.99/month paid annually ($59.99) | confirmed (V) | "Basic Unlimited automatic GPS mileage tracking & basic expense management ... Free forever" and "Premium ... $4.99 Per month Paid annually ... Paid annually as $59.99" | https://www.triplog.net/pricing | None. Web app access and unlimited reporting are Premium ("With 7-day pass" on Basic). |
| FreeTaxUSA | Federal free; state $15.99; Schedule C (self-employed) at $0 | confirmed (V) | "Federal Tax Returns Free State Tax Returns $15.99" and "Self-Employed ... Freelancers Small businesses Contractors $0 + $15.99 per state" | https://www.freetaxusa.com/pricing/ | None. Page is labelled "2026 returns". Optional: Deluxe Support $7.99, Audit Defense $19.99, Pro Support $44.99, pay-with-refund $24.99. |
| Florida DOR registration | $0 to register as a sales and use tax dealer | unreadable (pages loaded, fee not stated) | Registration page: "you must register as a sales and use tax dealer to collect, report, and remit sales and use tax before you begin conducting business in Florida." DR-1N (R. 01/26): "Register online - it's fast and secure!" | https://floridarevenue.com/taxes/eservices/Pages/registration.aspx and https://floridarevenue.com/Forms_library/current/dr1n.pdf | No DOR page, the DR-1 form or the DR-1N instructions read today states a registration fee or says registration is free. The $0 figure is unproven, not wrong. The annual resale certificate page cited by the first agent says nothing about fees. |
| Lee County BTR | $50.00 full year | confirmed (V), with a proration correction | "a flat tax rate based on the start date of the business as follows: October – March $50 April – June $25 July – September $12.50" | https://leetc.com/businesses/fees-exemptions/ | $50 applies to a start date from October to March. "All business tax receipts expire September 30 of each year and can be renewed after July 1." Late renewal adds $3 (October) to $7.50 (January and later). Exempt accounts are "established at no cost or for a reduced fee". |
| Shopify Tax | Free until $100,000 lifetime sales, then 0.35% per order capped at $0.99 | confirmed (V) | "Lifetime sales threshold ... United States and rest of the world $100,000 USD $0.99 USD" and "Basic, Grow, or Advanced ... United States ... 0.35%" | https://help.shopify.com/en/manual/taxes/shopify-tax/pricing | None. Lifetime threshold applies to "stores that were created on or after May 13, 2026"; older stores get a $100,000 threshold per calendar year with a $5,000 yearly cap. First fetch returned HTTP 403; the retry loaded. |
| Seller Ledger | $10 /month up to 250 transactions; 30-day trial, no card | confirmed (V) | "Up to 250 transactions per month $10 /month $100 /year" and "30-day free trial ... No credit card required" | https://sellerledger.com/pricing/ | None. "Your 30-day free trial and monthly plans include up to 90 days of transaction history"; prepaying a year imports back to Jan 1 of the tax year. Etsy, eBay and Shopify are listed as supported platforms. |
| My Reseller Genie Ultimate | $22.99 per month; Etsy and eBay sync Ultimate-only; 14-day refund window; no free tier | confirmed (V) | "Ultimate $22.99 per month" and "14 day money back guarantee"; raw HTML: "eBay Integration" and "Etsy Integration" carry text-decoration:line-through on Basic and Premium and text-decoration:none on Ultimate | https://discover.myresellergenie.com/ | None. Also: Basic $11.99 includes only Core Features (sales analytics, bank/PayPal integration, consignment and every marketplace integration are struck through); Premium $16.99 adds analytics, bank/PayPal and consignment; all seven marketplace integrations are Ultimate-only. Prices read with the Monthly toggle. |
| Everlance | Basic $0 with 30 automatic trips a month; Starter $89.99/yr or $10.99/mo; Professional $119.99/yr or $19.99/mo | confirmed (V) | "Basic ... $0 ... 30 automatically tracked trips a month Unlimited manually tracked trips"; "Starter ... $89.99 Per year or $10.99 per month"; "Professional ... $119.99 Per year or $19.99 per month" | https://www.everlance.com/pricing | None. "all sales are non-refundable"; the 7-day trial needs a credit card. |
| MileIQ | Free $0, 40 free drives every month; Unlimited $11.66 per month billed annually | confirmed (V) | "Free ... $0 40 FREE DRIVES EVERY MONTH" and "Unlimited ... $11.66 PER MONTH BILLED ANNUALLY" | https://mileiq.com/pricing | None. Ownership note: footer reads "© 2026 Bending Spoons Operations S.p.A." |
| Keeper | Bookkeeping Only $20/mo; Standard $199/yr ($16.58/mo billed yearly) with a pro-signed return; Premium $399/yr | confirmed (V) | "Standard ... $199 /yr $16.58/mo, billed yearly"; "Bookkeeping Only $20/mo"; "Premium ... $399 /yr"; "Reviewed & signed by a tax pro" | https://www.keepertax.com/pricing | None. "Track mileage Coming soon", so Keeper is not a mileage tool today. 14-day free trial on every plan. |
| QuickBooks Free | $0/mo; connect 1 bank; 2 invoices a month; 2 receipts a month; 5 mileage trips a month; web only | confirmed (V) | Pricing page: "Free ... $0 / mo No credit card required ... 1 user No accountant access ... Send 2 invoices per month ... Connect 1 bank" and "Mobile app access and third-party integrations not currently available with QuickBooks Free." Solopreneur page: "Upload receipts (2 per month) Track mileage (5 trips per month)" | https://quickbooks.intuit.com/pricing/ and https://quickbooks.intuit.com/solopreneur/ | None on substance. The receipt and mileage limits are on the Solopreneur page, not the pricing page the first agent cited. Both pages returned HTTP 502 to headless Chromium three times and were read with plain curl over HTTP/1.1. |
| QuickBooks Solopreneur (Lite) | $20, shown as $10/mo 50% off for 3 months; no accountant access | confirmed (V) | "Lite ... $20 $10 ... 50% off for 3 months* ... No accountant access ... Unlimited receipts and mileage" | https://quickbooks.intuit.com/solopreneur/ | None. Simple Start ($38, $19 for 3 months) is the cheapest plan "With accountant access". |
| Wave | Starter $0 with unlimited bookkeeping records; Pro $190USD/year billed annually; receipts add-on $8/month or $72/year | confirmed (V) | "STARTER Plan ... $0 ... Create unlimited estimates, invoices, bills, and bookkeeping records"; "PRO Plan ... $190USD/year Billed annually"; "Digitally capture unlimited receipts ADD-ON $8/month OR $72/year" | https://www.waveapps.com/pricing | None. "Auto-import bank transactions" is Pro only. Card payments 2.9% + $0.60 on Starter. |
| Found | $0/mo banking, bookkeeping and tax with receipts, mileage, tax estimates; Found Plus $35/mo or $315/yr; Found Pro $80/mo or $720/yr | confirmed (V, curl fallback) | "$0/mo Your banking, bookkeeping, and tax platform"; "Found Plus $35/mo; $315/yr Found Pro $80/mo; $720/yr"; "Mileage and home office deduction tracking [Included]" on Found Free | https://found.com/pricing | None. "Found is a financial technology company, not a bank. Banking services are provided by Lead Bank". A $10 dormancy fee applies after 12 months of inactivity. Only useful if Hollie banks there. |
| Sortly | Free $0: 100 unique items, 1 user, 2 active jobs; Advanced $24 USD/mo billed at $288/yr | confirmed (V), with a promo correction | "Free ... $0 USD/mo. ... 100 Unique Items 1 User License 2 Active Jobs"; "Advanced ... $24 USD/mo.* ... Billed at $288/yr."; "* 50% discount applies only to first year of new customer subscriptions." | https://www.sortly.com/pricing/ | $24 is a "Flash Sale: 50% off yearly plans!" first-year price. "You'll save $300!" puts list near $588/yr. "After the first year, a 20% discount applies to all yearly plans." |
| Flipwise | Free up to 24 listings (new members only); $19.99/mo for 100 to 499 listings | confirmed (V) | "Free Up to 24 listings (new members only)"; "$19.99 /mo 100–499 listings"; "7-DAY MONEY-BACK GUARANTEE" | https://flipwise.app/pricing (resolves to https://flipwise.app/#pricing) | None. eBay-only sync; other channels are typed in by hand: "Record Amazon, Poshmark, Mercari, Etsy or offline sales right alongside eBay." |
| Hurdlr | Free: unlimited semi-auto mileage, manual finance tracking, tax estimates; Premium $100/yr ($8.34 a month) or $9.99 month-to-month; Pro $200/yr | confirmed (V) for Free and Premium; Pro price not on the page | "unlimited semi-auto mileage tracking, manual finance tracking, and real-time tax estimates"; "-$100 annual plan ($8.34 a month, most popular) -$9.99 month-to-month plan, cancel anytime" | https://university.hurdlr.com/en/articles/1072143-what-are-the-premium-features-and-how-much-do-they-cost | The article is dated "November 9, 2023", so the prices may be stale. "Pro $200 per year" is not on this page; it links to a separate Pro article that was not read today. Treat Pro as U. |
| Brother QL-800 | $124.99 one-time | confirmed (V) | "Brother QL-800 High-speed Professional Label Printer $124.99" | https://www.brother-usa.com/p/desktop-label-printers/QL800 | None. USB desktop printer; "Create and print labels instantly without installing software using the 'Plug & Label' feature." |
| Zoho Expense Free | $0: 3 users, receipt OCR, GPS mileage, 5 GB storage; Standard $3 per user/month billed annually | confirmed (V) | "FREE $0 ... Maximum users: 3 Receipt capture with AI-powered OCR ... Mileage expenses via GPS ... 5 GB receipt storage" and "STANDARD $3 per user/month billed annually" | https://www.zoho.com/us/expense/pricing/ | None. "Auto mileage capture with live tracking" is Premium ($5 per user/month billed annually); the free tier's GPS mileage is start-and-stop. |

Shutdown or acquisition notices: none found on any page read today. The only ownership signal is MileIQ's footer ("Bending Spoons Operations S.p.A."). Stocksmith (formerly Craftybase), Inventora and Dymo were not re-checked.

## 2. What the first agent got wrong or left loose

1. Florida DOR "$0 state registration". Not on any page read today. The annual resale certificate page the agent cited has no fee text. The registration page, the DR-1 form (R. 01/26) and the DR-1N instructions mention no fee at all. Unproven rather than refuted. Ricky will see any fee on the final screen of the online Florida Business Tax Application.
2. Lee County "$50.00 full year". The $50 is the rate for a business that starts between October and March. The receipt expires September 30 regardless of start date, and is prorated to $25 (April to June) or $12.50 (July to September). A November 2026 start pays $50 for a receipt that runs to 2027-09-30, then renews each year by September 30.
3. Sortly Advanced "$24 USD/mo". This is a flash-sale first-year price. The page's own "You'll save $300!" puts list near $588 a year. Hollie only needs the Free tier, so the error does not change the recommendation.
4. Hurdlr "Pro $200 per year". Not on the page the agent cited, which only prices Premium and is dated November 9, 2023. Pro stays U.
5. QuickBooks Free details. The "2 receipts, 5 mileage trips" limits are real but live on the Solopreneur page, not the pricing page the agent cited. The pricing page itself only lists 1 user, no accountant access, 2 invoices, 1 bank, chat support.
6. My Reseller Genie. The Ultimate-only Etsy and eBay claim is correct, and is actually stronger than the agent said: every marketplace integration, plus sales analytics, bank/PayPal integration and consignment tracking, are struck through on Basic $11.99. Basic buys only the Core Features list.
7. Everything else in the PICKS held exactly: Airtable 1,000 records, Zoho Books Free scope, TripLog free unlimited GPS, FreeTaxUSA $0 federal and $15.99 state, Shopify Tax thresholds and fees, Seller Ledger $10 a month and 30-day card-free trial, MRG Ultimate $22.99.

Fit notes that matter for one-of-one resale: Keeper's mileage is "Coming soon", so it cannot replace TripLog; Zoho Books Free has no bank feeds (Standard) and no Etsy/eBay channel sync below Elite; Seller Ledger's monthly plan only looks back 90 days, so start it in the month the first Etsy sale lands or prepay the year.

## 3. Every URL fetched today (2026-11-07)

Loaded (HTTP 200 or readable):
- https://airtable.com/pricing
- https://www.zoho.com/us/books/pricing/
- https://www.triplog.net/pricing
- https://www.freetaxusa.com/pricing/
- https://sellerledger.com/pricing/
- https://discover.myresellergenie.com/ (rendered text, plus raw HTML via curl for the struck-through plan items)
- https://help.shopify.com/en/manual/taxes/shopify-tax/pricing (HTTP 403 on the first try, 200 on retry)
- https://help.shopify.com/en/manual/taxes/shopify-tax
- https://www.shopify.com/tax (rendered text, plus raw HTML via curl for the collapsed FAQ answer)
- https://floridarevenue.com/taxes/taxesfees/Pages/annual_resale_certificate_sut.aspx
- https://floridarevenue.com/taxes/eservices/Pages/registration.aspx
- https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx
- https://floridarevenue.com/Forms_library/current/dr1n.pdf (PDF, R. 01/26)
- https://floridarevenue.com/Forms_library/current/dr1.pdf (PDF)
- https://floridarevenue.com/Forms_library/current/gt800002.pdf (PDF; an e-file requirements table, not a fee page)
- https://taxapps.floridarevenue.com/taxregistration/ (login page only)
- https://www.leetc.com/
- https://leetc.com/businesses/
- https://leetc.com/businesses/fees-exemptions/
- https://leetc.com/businesses/business-tax-guide-and-applications/
- https://www.everlance.com/pricing
- https://mileiq.com/pricing
- https://www.keepertax.com/pricing
- https://quickbooks.intuit.com/pricing/ (HTTP 502 to headless Chromium three times; read via plain curl over HTTP/1.1)
- https://quickbooks.intuit.com/solopreneur/ (HTTP 502 to headless Chromium; read via plain curl over HTTP/1.1)
- https://www.waveapps.com/pricing
- https://found.com/pricing (curl fallback)
- https://www.sortly.com/pricing/
- https://flipwise.app/pricing (redirects to https://flipwise.app/#pricing)
- https://university.hurdlr.com/en/articles/1072143-what-are-the-premium-features-and-how-much-do-they-cost
- https://www.brother-usa.com/p/desktop-label-printers/QL800
- https://www.zoho.com/us/expense/pricing/

Would not load:
- https://floridarevenue.com/taxes/registration/Pages/default.aspx (HTTP 404)
- https://floridarevenue.com/taxes/registration/Pages/registration.aspx (HTTP 404)
- https://floridarevenue.com/faq/Pages/default.aspx (HTTP 404)
- https://floridarevenue.com/taxes/registration (HTTP 405 in the browser; DNS failure in curl)
- https://floridarevenue.com/Forms_library/current/gt300015.pdf (HTTP 404)
- https://www.leetc.com/business-tax, https://www.leetc.com/business-tax/, https://www.leetc.com/businesses/business-tax/ (all redirect to a PDF viewer stub at https://leetc.com/document/business-tax-application-2/)
- https://www.leetc.com/business-tax-receipt/ (page not found)
- https://quickbooks.intuit.com/free/ (HTTP 502)
