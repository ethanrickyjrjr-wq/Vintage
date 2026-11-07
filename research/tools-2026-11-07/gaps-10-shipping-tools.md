# Gaps review: lane 10, shipping label tools, freight and insurance services

Date: 2026-11-07. Author: research subagent (completeness critic for lane 10).
Question: What is missing from the lane 10 tool list (shipping label apps, freight and local delivery, shipping insurance, scales, printers and boxes for one person shipping lamps, art, glass and small furniture from Southwest Florida), and which listed tools are defunct, acquired or renamed?
Legend: V = vendor page read today (2026-11-07); U = unverified (page would not load, or the figure is not in the text layer of any page that loaded).

Method note: WebSearch's shared budget for this turn was already used up when this agent started, so no search engine was queried. Every page below was fetched directly at a vendor, help-center, app-store, developer-portal or GitHub URL through the session's headless Chromium fetcher (curl fallback). Leads came from the lane report's own seed list (1stDibs, ShipStation AI, address validation, box sourcing were seeds the first agent never reached), from the Shopify App Store's 2026 "Shipping solutions" category page, from GitHub topic pages, and from vendor pages that name each other (ShipSaver names Shipsurance; ParcelPath names Shipsurance; ShipWorks names ShipStation; Roadie names UPS). Product Hunt returned 403, Reddit was not read, and no subagents, environment, credential or permission tools were used. About 95 URLs were fetched; roughly 60 returned real content. Tools already on the lane list were not re-verified; that is the verify agent's job.

## 0. Bottom line

- The lane missed four free label apps that each do something Pirate Ship does not. ShipSaving (Starter "Free/ month", "Up to 50 labels/month", USPS, UPS, FedEx and DHL Express, a real iPhone app, QR codes for printer-free drop-off). Descartes XPS Ship ("Always Free", "Up to 50 shipments per month", USPS, UPS and FedEx, web). ParcelPath ("No monthly fees. No subscription. No minimums.", UPS and USPS, Shipsurance at "$0.60 per $100", plus PalletPath LTL freight quotes in the same account). Ordoro Shipping Essential (FREE, 100 labels a month, then "a temporary account lock"). All V. ShipSaving is the one worth a free account today, as the FedEx and iPhone backup to Pirate Ship.
- The lane missed ShipSaver, Shipsurance's own pay-as-you-go storefront for small shops: "No monthly fees (pay-as-you-go)", "Integrates with Shopify, Etsy, eBay, and BigCommerce", USPS domestic $0.65 up to $50 then "$1.00" per additional $100, and UPS and FedEx at "$0.75" per $100 up to $5,000. That is cheaper than Pirate Ship's InsureShield ($1.00 per $100) for UPS, and it covers eBay and Shopify orders that Etsy's $0.80 add-on cannot reach. V.
- The lane missed the free USPS pieces that matter before a printer is bought: Label Broker (QR code printed at the Post Office; eBay, Pirate Ship, ShipSaving and ParcelPath all support it), the USPS Label Delivery Service ("$1.65 fee (per label)" to have labels mailed), and the USPS Web Tools and Addresses 3.0 APIs, "free of charge". The free USPS address API makes the listed Smarty ($552 per year) unnecessary for the planned dashboard. V.
- For the planned dashboard, ShipEngine has been folded into ShipStation as "ShipStation Shipping API" with a "$0.00 /month" plan that lets you "Create labels and compare rates" on their carrier accounts. It belongs beside EasyPost on the list. V.
- Shopify-side gaps, for later: Route ("$0 /month", shopper-funded package protection; Shopify app "Free to install. Additional charges may apply."), Navidium ("$0 for up to 50 Orders a Month", self-funded, "Keep 100% fees collected"), the official FedEx Ship Manager app ("Free to install", needs a FedEx account; fills the no-FedEx gap in Pirate Ship), Boxify ("From $19/month", real-time carrier rates by box size, built for bulky items), and the tracking pages AfterShip (free 50 shipments a month) and Parcel Panel, now branded "CWILL Order Tracking" (free 20 orders a month). All V.
- Large items: Roadie (UPS-owned) delivers "oversized items up to 144" and 300 pounds same-day up to 100 miles" and has a sender sign-up portal, but no public price. Bungii lists "Fort Myers, FL", "Sarasota, FL" and "Tampa Bay, FL" among its 125 markets, with a 150-mile range and 2,500 lb capacity, but it sells to retailers and B2B and shows no price. TSI Shipping does blanket-wrapped consolidated furniture and art shipping cross-country, quote only. Freightquote ("no signup required") and FreightCenter ("50+ carriers") give instant LTL quotes for a crated chair or large canvas. All V for existence, U for price.
- Defunct, renamed or changed: Sendle's US site is a pre-launch placeholder today ("Sendle is almost here!"), so Sendle is not an option. ShipEngine now redirects to ShipStation. XPS Ship is now "Descartes XPS Ship". Parcel Panel is now "CWILL Order Tracking". The Nelko printer domain resolves to a parked page. Auctane's ShipWorks page quotes "ShipStation Plans ... $9.99 – $229.99/mo", which does not match the $14.99 Starter price on the lane list; the verify agent should look. Dolly to Taskrabbit Delivery was already on the list; nothing new.
- Pages that would not load: PayPal Shipping (403 at three URLs), Amazon Shipping (redirects to sign-in), Sendle US pricing (tunnel failure), Pitney Bowes' PitneyShip pricing sub-page (404; the shipping-software page loaded instead), DYMO product page (403), Product Hunt (403), Roadie support (401), uShip sub-pages (404). PayPal, Amazon Shipping and DYMO prices are U.

## 1. Missing tools

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| ShipSaving | Discounted USPS, UPS, FedEx and DHL Express labels; QR codes for printer-free drop-off; store connections; pickups | Starter "Free/ month"; Pro "$15/ month(starting at)"; API "Pay as you go, only $0.05/label" | "Up to 50 labels/month", "No credit card required", "Unlimited store connections" | Web; iPhone and iPad app (free, "Requires iOS 17.0 or later"); Google Play app linked | Medium-high. Free FedEx and DHL backup to Pirate Ship with a real phone app; a reviewer mentions an Etsy connection | V | https://www.shipsaving.com/en/pricing and https://apps.apple.com/us/app/shipsaving-ship-save/id6502415198 |
| Descartes XPS Ship | Multi-carrier label software with "Discount shipping for USPS, UPS, and FedEx" | "FREE Always Free"; "STARTUP $9.95/month"; "GROWTH $29.95/month" | "Up to 50 shipments per month", "1 User", "1 Sales channel" | Web | Medium. Higher free cap than Shippo's 30 and includes FedEx; Shopify, Amazon and eBay named, Etsy not named | V | https://xpsship.com/pricing/ |
| ParcelPath and PalletPath | Free UPS and USPS labels, mobile barcode printing at UPS Store or Post Office, Shipsurance cover, LTL freight quotes from 22 carriers | "No monthly fees. No subscription. No minimums."; insurance "$0.60 per $100 in declared value" | Everything free; pay postage | Web | Medium. Cheapest per-$100 insurance seen today and a freight desk in the same login; eBay and TikTok Shop named, Etsy not named | V | https://parcelpath.com/ |
| Ordoro Shipping (Essential) | Label app with discounted carriers, 1 sales channel, barcode scanning, return labels | "ESSENTIAL FREE"; "ADVANCED $59/mo"; "PREMIUM $149/mo" | "Monthly Label Count 100*"; "*Surpassing 100 labels/mo will result in a temporary account lock." | Web | Low-medium. 100 free labels is generous; carriers are not named on the pricing page | V | https://www.ordoro.com/pricing |
| PitneyShip Pay-as-you-go | Pitney Bowes label software: "Discounted rates for USPS, FedEx, UPS", stamps, mobile app | "$0 monthly fee*"; "*... A 5% usage fee will be applied to the price of each label printed."; "Premium $34.99/month" | No monthly fee but a 5% per-label fee | Web, mobile app | Low. FedEx without a subscription, but the 5% fee loses to Pirate Ship and ShipSaving at $0 | V | https://www.pitneybowes.com/us/shipping-software.html |
| Ship.com (Ship AI) | Label platform with an AI "shipping manager" that fills package details and buys labels | "Starter $4.99/mo"; "Growth $19.99/mo"; "Executive $29.99 per month (or $22/month with annual billing)" | 30-day trial only; Starter is "Up to 10 Shipments/mo" | Web | Low. No free plan; the AI buys labels on your approval, a feature Pirate Ship lacks but not worth $4.99 at this volume | V | https://www.ship.com/ |
| ShipStation Shipping API (formerly ShipEngine) | Developer API to rate, buy and track labels; free plan uses their carrier accounts | "Free ... $0.00 /month"; "Advanced ... 1,000 labels per month $75.00 /month +$0.075 per additional label" | Free plan: "Create labels and compare rates", "Connect with our carrier accounts", sandbox | API (web console) | Medium for the planned dashboard; sits beside EasyPost (listed). "Validate any address" is on the $75 plan only | V | https://www.shipstation.com/shipping-api/pricing/ |
| ShipSaver (by Shipsurance) | Pay-as-you-go shipping insurance for small shops, with optional discounted USPS labels; integrates Shopify, Etsy, eBay, BigCommerce | USPS domestic "$0.01 – $50.00 $0.65", "Each additional $100 $1.00"; "UPS & FedEx Standard ... Per $100 of declared value $0.75"; UPS SurePost or FedEx SmartPost "$1.00 per $100" | "No monthly fees (pay-as-you-go)" | Web | Medium-high. Cheaper than InsureShield for UPS and FedEx and covers eBay and Shopify orders. Limits "up to $5,000" (USPS international $1,000). Can insure a parcel labelled elsewhere | V | https://www.shipsaver.com/insurance-calculator/ |
| InsureShield (UPS Capital) direct | Business shipping insurance for UPS, multi-carrier parcels, LTL and international freight | "Estimated premium per package $0.80 to $10.50" for "$100 to $1,000"; "Estimate only." | None; "Talk to an expert" sales model | Web | Low direct. Reach the same cover inside Pirate Ship at $1.00 per $100 | V | https://www.insureshield.com/us/en/shipping-insurance.html |
| Secursus | Third-party insurance per package, fixed rate, "High-value items up to $120,000" | "FROM$2.00"; "Minimum rate of $2.00"; "Only pay for what you insure without any commitment or subscription." | None | Web | Low-medium. Only for the rare piece above the $5,000 Shipsurance and USPS InsureShield caps; "Works for carriers offering a signed-for shipping"; the rate percentage is in a calculator, not the text | V | https://www.secursus.com/en-us/pricing/ |
| Route Protection and Tracking | Shopper-funded package protection, tracking and returns for Shopify stores | "$0 /month"; "No monthly or hidden fees. Zero cost, zero risk, full coverage." | Shopify listing: "Free to install. Additional charges may apply." | Shopify app, web | Medium once Shopify is live. Shopper pays the premium at checkout; Route handles claims. 72 one-star reviews out of 375 on the listing | V | https://www.route.com/pricing and https://apps.shopify.com/route |
| Navidium Shipping Protection | Self-funded protection fee at the cart; Hollie keeps the fee and pays claims herself | "$0 for up to 50 Orders a Month"; "$29.99 for < 501 orders/mo, $49.99 for < 1001 orders/mo, $99.99 for unlimited orders" | Free up to 50 orders a month | Shopify app | Medium once Shopify is live. "No Rev Share. Keep 100% fees collected." It is not insurance; a broken chandelier is paid from the collected fees | V | https://apps.shopify.com/navidium-shipping-protection |
| FedEx Ship Manager (official Shopify app) | Pushes Shopify orders into FedEx Ship Manager to create labels on your own FedEx account | "Free to install. Additional charges may apply." | Free app; pay FedEx rates | Shopify app | Medium once Shopify is live. Fills the FedEx gap in Pirate Ship; needs a FedEx account; only 9 reviews | V | https://apps.shopify.com/fedex-ship-manager |
| Boxify | Shows carrier-calculated rates at Shopify checkout using the actual box size per item | "From $19/month"; Starter "$19" with "Up to 250 shipping calculations/month" | 14-day trial text not read; no free plan shown | Shopify app | Medium later. Merchants recommend it for "bulky items, or products that ship alone"; exactly the lamp and chair problem | V | https://apps.shopify.com/boxify |
| Intuitive Shipping | Rules for how shipping is priced and displayed at Shopify checkout | "Sandbox Free"; "Growth $70 / month 500 orders included" | Sandbox only | Shopify app | Low. $70 a month is over budget | V | https://apps.shopify.com/intuitive-shipping |
| AfterShip Order Tracking | Branded tracking page and notifications | "Free to install 50 shipments/month"; Essentials "$11 ... includes 100 shipments/month; $0.08 per extrashipment" | 50 shipments a month | Shopify app, web | Low-medium. A reviewer warns "You're billed for every order you print, whether or not the customer ever opens the tracking portal" | V | https://apps.shopify.com/aftership |
| Parcel Panel (now CWILL Order Tracking) | Branded tracking page and notifications | "Free 20 orders/month"; "$11 ... 200 orders/month"; "$0.05 per additional quota" | 20 orders a month | Shopify app, web | Low-medium. Enough at Hollie's volume; renamed under the CWILL brand | V | https://apps.shopify.com/parcelpanel |
| Packlink PRO | Multi-carrier label platform, 30+ carriers | "Free plan available"; "$29 ... €25+VAT/mo" | Free plan | Shopify app, web | Low. Carriers shown are "DHL DPD Evri Royal Mail UPS Yodel", UK and EU centric | V | https://apps.shopify.com/packlink-pro |
| USPS Label Broker, Label Delivery Service and Web Tools APIs | Print labels at the Post Office from a QR code; have labels mailed to you; free APIs including Addresses 3.0 for address validation | Label Delivery: "We'll print and deliver the labels to you for a $1.65 fee (per label)."; APIs "free of charge" | Label Broker free; APIs free | Web, Post Office counter, API | High. Lets Hollie ship before buying a printer, and replaces Smarty for the dashboard's address check | V | https://www.usps.com/business/business-shipping.htm and https://developers.usps.com/addressesv3 |
| Roadie (a UPS company) | Same-day and next-day local delivery by independent drivers | No price on pages read; "deliver oversized items up to 144" and 300 pounds same-day up to 100 miles" | n/a; sender portal "New to Roadie? Sign Up" | Web sender portal, driver app | Medium for a lamp or chair within 100 miles of Fort Myers (Naples, Sarasota). Price U | V (price U) | https://www.roadie.com/ and https://send.roadie.com/sign-in |
| Bungii | On-demand big and bulky delivery, 150-mile range, 2,500 lb | No price on pages read; "We deliver in 125 markets across the United States." | n/a | Web, app; retail and B2B sales model | Medium-low. Fort Myers, Sarasota and Tampa Bay are listed markets, but the site sells to retailers and logistics firms, not individuals | V (price U) | https://bungii.com/cities/ |
| TSI Shipping | Small moves and single-item furniture, antique, art and clock shipping across the US; consolidated blanket-wrap or custom crating | Quote only ("Get Started With a Free Quote", 1-800-626-1257) | n/a | Web quote form, phone | Medium for a one-off out-of-state chair or large canvas. Box-only shipments need "minimum of 5 medium-sized boxes" | V (price U) | https://www.tsishipping.com/shipping |
| Freightquote by C.H. Robinson | Instant LTL and truckload quotes | "Get hassle free freight quotes with no signup required." | Free quotes | Web | Low-medium. For a crated or palletized piece; LTL is for "pallets ... under 15,000 pounds" | V (price U) | https://www.freightquote.com/ |
| FreightCenter | Instant LTL quotes and agent-handled freight, white glove listed | "Compare instant freight quotes from 50+ carriers in seconds." | Free quotes | Web | Low-medium. Same use as Freightquote; white-glove sub-page was 404 | V (price U) | https://www.freightcenter.com/ |
| 1stDibs shipping program | Marketplace-managed shipping for approved sellers: In-Home Delivery, Front Door Freight with custom crating, Parcel, Courier | Seller cost not on buyer-facing help pages | n/a | Web (seller dashboard) | Low. A juried channel; "fully insured delivery" is handled by 1stDibs partners. Seller-side fees U | V (fees U) | https://support.1stdibs.com/hc/en-us/articles/14516879314587-Shipping-Methods |
| Polono 4x6 Bluetooth thermal printer | Wireless 4x6 label printer "Support Android, iPhone, Windows, and Mac" | "$89.99" (struck "$139.99") | n/a | Bluetooth and USB; Windows, Mac, iPhone, Android | Medium. One line: a Munbyn-class price with Bluetooth for the iPhone | V | https://www.polono.com/collections/label-printer |
| Phomemo PM241-BT | Bluetooth 4x6 shipping label printer | "From $110.99" (struck "$159.99") | n/a | Bluetooth and USB | Low-medium. One line: dearer than Polono and Munbyn | V | https://phomemo.com/collections/shipping-label-printer |
| DYMO LabelWriter 5XL | 4x6 desktop label printer | Price not in text; product page 403 | n/a | USB; "Connect to a PC or Mac" | Low. One line: DYMO's own labels are proprietary and dear; price U | U | https://www.dymo.com/label-makers-printers/labelwriter-label-printers/ |
| EcoEnclose | Recycled and compostable mailers and boxes | No prices in text; "FREE SAMPLES"; "Low Minimums. Fast Turnaround." | Free samples | Web | Low now. Branded eco packaging later | V (price U) | https://ecoenclose.com/ |
| Packlane | Custom printed shipping and mailer boxes | No prices in text; "Tiny minimums. No maximums."; "free 3D Design Tool" | n/a | Web | Low now. Branding later, like BoxUp | V (price U) | https://packlane.com/ |
| Sendle (US) | Small-business parcel carrier | US page is a placeholder: "Sendle is almost here! We're completing our final system integrations and testing" | n/a | Web | None today. Register-interest page only | V | https://www.sendle.com/us |
| PayPal Shipping (ShipStation-powered) | Labels from PayPal transactions | Not readable; 403 at three URLs | U | Web | U. Not worth chasing while Pirate Ship is free | U | https://www.paypal.com/us/business/shipping |
| Amazon Shipping | Amazon's carrier for non-Amazon orders | Not readable; redirects to Amazon sign-in | U | Web (Amazon seller login) | U. Reachable through Veeqo (listed) if ever needed | U | https://ship.amazon.com/ |

## 2. Notes per tool

- ShipSaving. Starter plan: "Access discounted rates", "Unlimited user logins", "Unlimited store connections", "Generate labels/QR codes", "Up to 50 labels/month", "No credit card required". Pro from $15 a month adds automations, branded tracking emails and up to 5,000 labels, "Start 30-day Free Trial". The App Store listing is free, iPhone and iPad, "Requires iOS 17.0 or later", and says "Schedule free USPS pickups or UPS pickups starting at just $4—directly from the app." A home-page review says "the connection to Etsy is a nice touch" with the caveat "(when it works)". Gotcha: the 50-label cap is per month across all stores.
- Descartes XPS Ship. Free plan is "1 Sales channel" and includes "Expert help via chat, phone and email". Own carrier accounts only from Growth ($29.95 a month). The brand is now "Descartes XPS Ship" throughout. Etsy is not named on the home page; Shopify, Amazon and eBay are.
- ParcelPath. Rates table shows UPS Ground Saver, UPS Ground, USPS Ground Advantage, UPS 3 Day Select, USPS Priority Mail and UPS 2nd Day Air; no FedEx. Printer-free: "use our mobile barcode at any UPS Store® for free printing, or the USPS Label Broker® at any Post Office." The "$0.60 per $100" Shipsurance line sits in the general features block, below the PalletPath block; whether it applies to parcels and freight alike is not stated. PalletPath: "Access 22 vetted national LTL carriers, instant transparent quotes with no hidden fees, and auto-generated Bills of Lading." A customer review contrasts it with a bidding marketplace that "put my request out for bidding".
- Ordoro. The free Essential plan has "Access to Ordoro Discounted Carriers" but the carriers are not named on the pricing page. "15-day free trial. No credit card required." applies to paid plans. The FAQ heading "Is Ordoro Shipping REALLY free?" exists but its answer is not in the text layer.
- PitneyShip. Pay-as-you-go: "1 user", "1 location", "Discounted rates for USPS®, FedEx®, UPS®", "Bring your own DHL account", "Stamp printing". Footnote: "No monthly subscription fee. A 5% usage fee will be applied to the price of each label printed." Premium is "$34.99/month after free trial**" with Certified Mail features. A mobile app is mentioned: "Ship, print, and track anywhere with our mobile app".
- Ship.com. Plans: Starter $4.99/mo (10 shipments), Growth $19.99/mo (100 shipments), Executive $29.99/mo (unlimited; "$22/month with annual billing"). "Free trial: Enjoy a 30-day free trial — pay only the postage, no subscription fee, no credit card required." Ship AI "prices your ready orders, shows one combined total, and asks for your approval to buy the label." Claims "up to 89% off USPS retail prices and up to 87% off UPS standard rates". Marketing-heavy page; the founder is named on it.
- ShipStation Shipping API. The old shipengine.com/pricing URL now lands on shipstation.com/shipping-api/pricing with "?r=shipengine". Free: "Unlock discounted carrier rates coupled with essential API access", "$0.00 /month", "Connect with our carrier accounts", "Create labels and compare rates", "Track your parcels", "Create tracking webhooks", "Sandbox environment". Advanced: "1,000 labels per month $75.00 /month", "Bring your own carrier accounts", "Validate any address". The same page says "Access exclusive 80% – 90% discounts from every major carrier from parcel to LTL freight".
- ShipSaver. "Our partner Shipsurance has helped businesses insure shipments for over 20 years. Coverage is underwritten by an A-rated insurer." Rates "as of November 2026": USPS domestic $0.65 for $0.01 to $50, then $1.00 each additional $100 (so a $100 parcel is $1.65; the calculator showed "$1.65" with "Coverage limit: $5,000"); USPS international $0.95 to $6.25 by band up to $500, then +$1.25 per $100 to $1,000; UPS and FedEx Standard $0.75 per $100 to $5,000; SurePost and SmartPost $1.00 domestic, $1.25 international per $100 to $1,000. "Tracking is required for all insured shipments." Exclusions listed include "Jewelry valued at $500 or more" and "Laptops, tablets, iPads and mobile phones, regardless of value." FAQ headings include "Purchasing Insurance - Without ShipSaver Label" and "Can I insure my shipping and handling costs?" Claim payment "a mailed check (typically 4–10 days) or instant PayPal."
- InsureShield direct. "Insure eligible shipments across all parcel, ocean, and freight carriers, including UPS, FedEx, DHL, and USPS." The slider estimate is "$0.80 to $10.50" per package for values "$100 to $1,000", with "Estimate only. Actual pricing and availability depend on the shipment, customer, coverage option, and applicable policy terms." No self-serve sign-up on the page; "Talk to an expert".
- Secursus. "Our rates stay the same no matter what item you send and no matter where you send it to." "Minimum rate of $2.00", "Coverage up to $120,000". "Works for carriers offering a signed-for shipping", so signature confirmation is required. US coverage is placed through "Hylant Group, Inc., a licensed insurance producer". FAQ headings include "Can I insure used, refurbished, or second-hand items?" and "Is it possible for individuals to subscribe to Secursus protection?"; the answers are not in the text layer. Business contracts start at "more than 500 shipments per month".
- Route. Merchant price "$0 /month": "Access the entire post-purchase platform with consumer funded pricing". The shopper pays. The Shopify listing adds "External charges may be billed by RouteApp LLC separately from your Shopify invoice." Review spread on the listing: 264 five-star, 72 one-star of 375. For one-of-one stock, note that a replacement is impossible, so any claim ends in a refund; this is an inference, not a line on the page.
- Navidium. "Navidium is a self-service shipping protection app to manage your own package protection / shipping insurance offering". "$0 for up to 50 Orders a Month", then "$29.99 for < 501 orders/mo". "No Rev Share. Keep 100% fees collected." and "Automatically upgrades to the next billing plan when you exceed 500 orders in your billing cycle." Gotcha: Hollie is the insurer; a lost $400 lamp is paid from fees she collected, or from her pocket.
- FedEx Ship Manager Shopify app. "Still creating shipments for your orders manually in the FedEx Ship Manager? With this app you can connect your store directly to our Ship Manager." "Create shipments faster with shipment profiles and connecting your label printer". Rates are whatever the FedEx account gives; no discount claim on the page. Nine reviews; one says "Good that it is a free app."
- Boxify. "Boxify displays at checkout carrier-calculated shipping rates that reflect the needed box size." Plans $19, $39, $69, $99 by calculations per month. "Merchants recommend this app for complex shipping needs, especially with many sizes, bulky items, or products that ship alone or in multiple boxes." Needs Shopify's carrier-calculated rates feature on the store.
- Intuitive Shipping. Free Sandbox is for setup only ("Set up, test, then enable rates"); live use starts at Growth $70 a month. Skip.
- AfterShip Order Tracking. Free "50 shipments/month; Free first import: up to 500 shipments*". Essentials "$11" a month "or $108/year", "$0.08 per extrashipment". A review: "Be careful how this app charges. You're billed for every order you print, whether or not the customer ever opens the tracking portal".
- Parcel Panel. Listing title is now "CWILL Order Tracking - Parcel Panel". Free "20 orders/month"; Essentials "$11" a month for "200 orders/month", "$0.05 per additional quota". A review mentions "TrackingMore which is part of CWILL".
- Packlink PRO. Carriers shown are "DHL DPD Evri Royal Mail UPS Yodel"; paid plan priced in euros ("€25+VAT/mo"). Not built for a US seller.
- USPS. Business Shipping page: "You can access Click-N-Ship® with your free USPS.com account." "USPS Label Delivery Service. Request physical outbound and return labels. We'll print and deliver the labels to you for a $1.65 fee (per label)." "Developers and technicians can easily integrate a variety of USPS & Web Tools into their website, shipping operation, or customer service center, free of charge." The Addresses 3.0 developer page loaded and documents ZIP+4 standardization; its live "Try it" widget showed "Service is unavailable." at the time of reading, which is the sandbox, not the API's status.
- Roadie. B2B pages throughout: "Roadie allows businesses to offer exceptional delivery experiences". Big and Bulky: "deliver oversized items up to 144" and 300 pounds same-day up to 100 miles". "Roadie for UPS Customers: Maximize your UPS account by adding Roadie." The sender portal at send.roadie.com has "Sender Sign In" and "New to Roadie? Sign Up"; whether a sole proprietor is accepted and what a Fort Myers to Naples lamp costs is not public. Support site returned 401.
- Bungii. "Too big for parcel, too small for LTL?" "150 MILE DELIVERY RANGE", "2,500 POUND CAPACITY", "Two-hour delivery windows and 95% on-time delivery." Markets page lists Daytona Beach, Fort Myers, Gainesville, Jacksonville, Melbourne, Miami, Orlando, Panama City, Pensacola, Port St. Lucie, Sarasota and Tampa Bay in Florida. Industries served: Retail, B2B, Transportation and Logistics. No consumer booking or price on the pages read.
- TSI Shipping. "TSI is your best choice for shipping unique items that you wouldn't take to the local parcel store." Options: "Consolidated shipping – your items will be blanket wrapped and transported with other items going in the same direction. This saves you money and is a great option if your timing is flexible." and "Custom crating – to protect valuable and fragile items, we can build custom crates on your property". Antiques: "on-site crating and full-value insurance". A customer: "My antique chairs, though not restored, were handled with great care". Box shipping needs "minimum of 5 medium-sized boxes".
- Freightquote. "No signup quoting. Get hassle free freight quotes with no signup required." LTL defined as "when your pallets don't fill an entire truck trailer and weigh under 15,000 pounds". The how-to LTL page was 404. Freight needs a pallet or crate and a bill of lading; residential and liftgate accessorials were not read today.
- FreightCenter. "Compare live rates from 50+ top carriers", LTL "ideal for shipping 1 to 6 pallets". Rewards program "Joining is completely free." White-glove page 404.
- 1stDibs. Buyer-facing help: "Different shipping options are available to you depending on the size, fragility and location of the item." Methods: In-Home Delivery ("amply padded ... via a commercial truck"), Front Door Freight ("a custom crate is built around the item"), Parcel ("the seller ... will receive a shipping label"), Courier. "We partner with leading providers to offer fully insured delivery". Seller fees and the application process were not on readable pages; 1stdibs.com/sell/ was 404.
- Printers. Polono's own store lists "POLONO Bluetooth Thermal Shipping Label Printer, Wireless 4x6 Shipping Label Printer for Small Business, Support Android, iPhone, Windows, and Mac" at $89.99 (struck $139.99). Phomemo lists "Phomemo PM241-BT Bluetooth Shipping Label Printer From $110.99" (struck $159.99). DYMO's category page lists the LabelWriter 5XL but the product page returned 403. nelkoprinter.com resolves to a parked page through the proxy, so Nelko is U.
- Boxes. EcoEnclose offers "FREE SAMPLES" and "Low Minimums. Fast Turnaround."; Packlane "Tiny minimums. No maximums." and a "free 3D Design Tool"; The Boxery loaded with almost no text. None shows a price in the text layer. Uline (on the list, U) stays U; it was not retried here.
- Open source. GitHub topics "shipping-labels" and "shipping" surface libraries, not apps: Shopify/active_shipping (814 stars, "simple shipping abstraction library"), goshippo/shippo-php-client (167 stars), EasyKeys.Shipping (.NET: "DHL Express, Amazon Shipping, FedEx, Usps, Stamps.com Shipping Implementations"), and snake-label (German DHL and Hermes label conversion for 62mm printers). Buying US postage needs a licensed vendor account, so there is no free open-source label buyer; these are dashboard building blocks only.
- ShipStation AI (a seed the first agent did not cover). The fulfillment page says "Combine AI intelligence with rule-based workflows across parcel and freight to speed up fulfillment" and "Smarter Shipping Intelligence". No AI-specific price or feature list was readable; nothing here changes the lane's "low now" verdict on ShipStation.

## 3. Defunct, renamed or changed

- Sendle US: paused or relaunching. sendle.com/us reads "🚀 Sendle is almost here! We're completing our final system integrations and testing to ensure a seamless customer experience. Launch is just around the corner, so register your interest today". The pricing and small-business URLs return "Page Not Found" and the root site is Australian (GST, kg). Not on the lane list; it was a candidate and is excluded. V. https://www.sendle.com/us
- ShipEngine: now "ShipStation Shipping API". shipengine.com/pricing redirects to https://www.shipstation.com/shipping-api/pricing/?r=shipengine. V.
- XPS Ship: now "Descartes XPS Ship" (page title "Shipping Plans & Pricing | Descartes XPS Ship"). V. https://xpsship.com/pricing/
- Parcel Panel: now "CWILL Order Tracking - Parcel Panel" on the Shopify App Store; a review says "TrackingMore which is part of CWILL". V. https://apps.shopify.com/parcelpanel
- ShipStation pricing discrepancy: Auctane's ShipWorks pricing page says "ShipStation Plans. Plans from $9.99 – $229.99/mo", while the lane list records Starter at $14.99 and Premium at $349.99. Not resolved here; flagged for the verify agent. V for the ShipWorks page. https://www.shipworks.com/pricing/
- Nelko (printer brand, not on the list): nelkoprinter.com redirects to a parked ww19 subdomain; the vendor's current site is unknown. U.
- No change found today on ShippingEasy or Stamps.com home pages (no shutdown, migration or rename notice; Stamps.com still offers "Risk-Free 30-Day Trial" and a "free scale" in the welcome kit). V.
- Dolly to Taskrabbit Delivery: already on the lane list; no new evidence gathered.
- Roadie is "a UPS company" (home page nav "Roadie for UPS Customers"); no rename.

## 4. Recommendation for Hollie

- Today, free: open a ShipSaving Starter account on the iPhone (free, 50 labels a month) as the FedEx and DHL backup to Pirate Ship, and because its QR codes plus USPS Label Broker mean no printer is needed on day one. Keep Pirate Ship as the primary.
- Today, free: bookmark ShipSaver. For any eBay or Shopify order worth more than $100 that Etsy's $0.80 add-on cannot cover, insure it there: $0.75 per $100 on UPS or FedEx, $1.65 for a $100 USPS parcel.
- For the dashboard build: use the free USPS Addresses 3.0 API instead of Smarty, and compare the ShipStation Shipping API free plan against EasyPost before writing label code.
- When Shopify goes live: install the FedEx Ship Manager app only if a FedEx account exists; look at Route (shopper-funded, $0) before Navidium (self-funded); consider Boxify at $19 a month only if flat-rate shipping on lamps and chairs starts losing money.
- Large items: request one TSI quote and one Freightquote quote the first time a chair or oversized canvas sells out of state, so the real numbers are known. Locally, GoShare (listed) stays first; Roadie and Bungii are worth one sign-up attempt each to learn whether they take a one-person shop and what a Fort Myers to Naples run costs.
- Skip: PitneyShip (5% per-label fee), Ship.com ($4.99 minimum), Intuitive Shipping ($70), Packlink PRO (UK and EU carriers), Sendle (not launched), Ordoro (free but carriers unnamed and an account lock at 100 labels).

## 5. Gaps and pages that would not load

- WebSearch was unavailable for the whole task (shared budget exhausted), so roundup cross-checks were limited to the Shopify App Store 2026 category pages and GitHub topics. Product Hunt returned 403. Chrome Web Store was not read (it needs a search).
- PayPal Shipping: 403 at paypal.com/us/business/tools/shipping and paypal.com/shiplabel/; 404 at two more. U.
- Amazon Shipping: ship.amazon.com redirects to Amazon sign-in; veeqo.com/amazon-shipping is a JavaScript shell. U.
- Sendle: try.sendle.com/en-us/pricing and support.sendle.com failed at the proxy tunnel (502). The US landing page loaded and is a placeholder.
- Pitney Bowes: two PitneyShip URLs were 404; pitneybowes.com/us/shipping-software.html loaded with full plan text.
- Roadie: roadie.com/pricing, /faq and /send returned a JavaScript shell with no text; support.roadie.com returned 401. Price U.
- Bungii: /locations/ and /cities-we-serve/ were 404; /cities/ loaded.
- TSI: shiptsi.com was 404; tsishipping.com loaded.
- uShip: /how-it-works/ and /furniture-shipping/ were 404 (uShip stays U as on the lane list).
- 1stDibs: 1stdibs.com/sell/ was 404; the support center and three shipping articles loaded, buyer-facing only.
- Secursus: /en/ was 404; /en-us/ and /en-us/pricing/ loaded. The percentage rate is inside a calculator widget, not in text.
- DYMO 5XL product page 403; category page loaded without prices.
- Nelko: domain parked.
- The Shopify "shipping labels" sub-category slug guessed first was 404; the real sub-category is orders-and-shipping-shipping-solutions, which loaded.
- Freightquote LTL how-to and FreightCenter white-glove pages were 404.

## 6. Sources (every URL fetched today, including failures)

https://www.shipsaving.com/pricing (resolved to https://www.shipsaving.com/en/pricing)
https://www.shipsaving.com/
https://apps.apple.com/us/app/shipsaving-ship-save/id6502415198
https://parcelpath.com/pricing/ (404)
https://parcelpath.com/
https://xpsship.com/pricing/
https://xpsship.com/
https://try.sendle.com/en-us/pricing (tunnel failed)
https://www.sendle.com/us
https://www.sendle.com/us/pricing (Page Not Found)
https://www.sendle.com/us/small-business (Page Not Found)
https://www.sendle.com/
https://support.sendle.com/hc/en-us (tunnel failed)
https://www.pitneybowes.com/us/shipping-and-mailing/online-shipping-software/pitneyship.html (404)
https://www.pitneybowes.com/us/pitneyship.html (resolved to https://www.pitneybowes.com/us/shipping-software.html)
https://www.pitneybowes.com/us/shipping-and-mailing/shipping-software/pitneyship-pricing.html (404)
https://www.ordoro.com/pricing
https://www.paypal.com/us/business/shipping (404)
https://www.paypal.com/us/webapps/mpp/shipping (404)
https://www.paypal.com/us/cshelp/article/how-do-i-create-and-print-a-shipping-label-help267 (redirected to an unrelated article)
https://www.paypal.com/us/business/tools/shipping (403)
https://www.paypal.com/shiplabel/ (403)
https://www.ship.com/
https://www.shipstation.com/features/ (resolved to https://www.shipstation.com/fulfillment/)
https://www.shipengine.com/pricing/ (resolved to https://www.shipstation.com/shipping-api/pricing/?r=shipengine)
https://www.shipworks.com/pricing/
https://shippingeasy.com/
https://www.stamps.com/
https://www.shipsaver.com/
https://www.shipsaver.com/insurance-calculator (resolved to https://www.shipsaver.com/insurance-calculator/)
https://www.shipsaver.com/faq (resolved to https://www.shipsaver.com/faq/)
https://www.insureshield.com/us/en/home.html (resolved to https://www.insureshield.com/us/en/securecommerce.html)
https://www.insureshield.com/us/en/shipping-insurance.html
https://www.secursus.com/en/ (404)
https://www.secursus.com/ (resolved to https://www.secursus.com/en-us/)
https://www.secursus.com/en-us/pricing (resolved to https://www.secursus.com/en-us/pricing/)
https://www.route.com/pricing
https://apps.shopify.com/route
https://navidiumapp.com/pricing/
https://apps.shopify.com/navidium-shipping-protection
https://apps.shopify.com/categories/orders-and-shipping
https://apps.shopify.com/categories/orders-and-shipping-shipping-solutions
https://apps.shopify.com/categories/orders-and-shipping-shipping-solutions-shipping-labels (404)
https://apps.shopify.com/fedex (404)
https://apps.shopify.com/fedex-ship-manager
https://apps.shopify.com/packlink-pro
https://apps.shopify.com/boxify
https://apps.shopify.com/intuitive-shipping
https://apps.shopify.com/aftership
https://apps.shopify.com/parcelpanel
https://www.roadie.com/
https://www.roadie.com/send (JavaScript shell)
https://www.roadie.com/pricing (JavaScript shell)
https://www.roadie.com/faq (JavaScript shell)
https://support.roadie.com/hc/en-us (401)
https://send.roadie.com/ (resolved to https://send.roadie.com/sign-in)
https://bungii.com/
https://bungii.com/locations/ (404)
https://bungii.com/cities-we-serve/ (404)
https://bungii.com/about-us/
https://bungii.com/cities/
https://www.shiptsi.com/ (404)
https://www.shiptsi.com/furniture-shipping/ (404)
https://www.tsishipping.com/
https://www.tsishipping.com/shipping
https://www.freightquote.com/
https://www.freightquote.com/how-to-ship-freight/ltl-freight-shipping/ (404)
https://www.freightcenter.com/
https://www.freightcenter.com/freight-services/white-glove-delivery/ (404)
https://www.uship.com/how-it-works/ (404)
https://www.uship.com/furniture-shipping/ (404)
https://www.1stdibs.com/sell/ (404)
https://support.1stdibs.com/hc/en-us
https://support.1stdibs.com/hc/en-us/categories/14416669159067-Shipping-Tracking
https://support.1stdibs.com/hc/en-us/articles/14517339089947-Shipping-and-Handling-Time
https://support.1stdibs.com/hc/en-us/articles/14516879314587-Shipping-Methods
https://support.1stdibs.com/hc/en-us/articles/14514694880923-Freight-Shipping
https://ecoenclose.com/
https://packlane.com/
https://www.theboxery.com/
https://www.nelkoprinter.com/ (parked domain)
https://phomemo.com/
https://phomemo.com/collections/shipping-label-printer
https://www.polono.com/
https://www.polono.com/collections/label-printer
https://www.dymo.com/label-makers-printers/labelwriter-5xl-label-printer/SP_2112554.html (403)
https://www.dymo.com/label-makers-printers/labelwriter-label-printers/
https://developers.usps.com/addressesv3
https://www.usps.com/business/shipping-tools.htm (404)
https://www.usps.com/business/business-shipping.htm
https://ship.amazon.com/ (redirects to Amazon sign-in)
https://www.veeqo.com/amazon-shipping (JavaScript shell)
https://github.com/topics/shipping-labels
https://github.com/topics/shipping
https://www.producthunt.com/topics/shipping (403)
Link scans (anchor extraction only): https://support.1stdibs.com/hc/en-us, https://bungii.com/, https://www.roadie.com/, https://apps.shopify.com/categories/orders-and-shipping, https://apps.shopify.com/categories/orders-and-shipping-shipping-solutions, https://www.shipsaving.com/
