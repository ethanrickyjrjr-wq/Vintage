# Gaps review for lane 01: listing and crosslisting tools missing from the first sweep

Date 2026-11-07. Author: research subagent (completeness critic for lane 01). Question: Which tools that make creating a listing and posting it to Etsy, eBay and Shopify faster for one person are missing from the lane 01 list, and is anything on that list defunct, acquired or renamed? Legend: V = page read today (vendor page, or the vendor's App Store or Shopify App Store listing); U = unverified (snippet, roundup, memory, or the page would not load).

Method. The shared WebSearch budget was already used up when this agent started, so no web searches were run. Discovery used category pages and catalogs read directly: the Apple App Store catalog (10 search queries and 13 app lookups through Apple's public lookup API, which returns the same text as the apps.apple.com listing), Shopify App Store category pages (Sales channels, Marketplaces), eight GitHub topic pages, the Crosslist blog roundup "Best 10 Cross Listing Apps in 2026 for Resellers" (last updated September 30, 2026) that the lane 01 agent fetched earlier today, and the competitor comparison pages already in the scratchpad. Each candidate's own pricing page was then read with headless Chromium through the session proxy. 75 fetch attempts, 62 returned content, 13 failed (listed in section 5). Product Hunt returned 403 on every page, and the Chrome Web Store was not reachable without extension IDs, so those two category sources are missing. Tools already on the lane 01 list were not re-verified, except where a page read for another reason gave rename or shutdown evidence (section 2).

## 0. Bottom line

- Three tools launched in 2025 and 2026 cover all three of Hollie's channels and are missing from the list. Swiftlisted (Australia; web, Chrome extension, iPhone app released 2026-11-05): "Starter $6 USD/mo $72 USD billed yearly", with "sold detection and auto-delisting" on the cheapest plan and a "30-day free trial and no credit card"; eBay and Shopify go through APIs, Etsy through the Chrome extension. Secnd (Canada; web and iPhone, released 2026-03-10): "Free $0 CAD/mo Free forever" including "Inventory sync + automatic delisting", then "$29 CAD/mo"; prints Etsy and Shopify API notices. VendorSnap (iPhone and Android, released 2026-06-16): Pro "$6.67/month Billed yearly at $79.99", lists on "eBay, Etsy, Facebook Marketplace, Vinted, Depop and Poshmark", eBay and Etsy "through their official APIs"; no Shopify.
- Cheapest phone-first listers the list lacks: VendorSnap Pro (above), EzList PRO "$9.99 / month" for 100 listings to eBay, Etsy, Reverb, Depop, Mercari and Facebook Marketplace beta with "Your first 3 listings are free", and Hero (2,071 App Store ratings) at "$10 / month" for 10 items but eBay and Facebook Marketplace only.
- Shopify-side Etsy sync apps the list lacks, all V from the Shopify App Store today: QuickSync ("Free: $0, 100-variant stock sync for eligible shops"; Lite "$19 / month"; 4.8 stars, 2,022 reviews), Shuttle (free plan of "10 product transfers per month"; Growth "$19 / month" with "Real-time stock sync (200 orders/mo)"), shopUpz ("$9.99 / month" for "Export UNLIMITED listings to Etsy"; "$18 / month" to "Sync UNLIMITED quantities, Locations") and InfoShore (Bronze "$19.99 / month"). Trunk ("From $35/month") is the only tool read today that syncs stock across Shopify, Etsy and eBay in real time; it creates no listings.
- Windows desktop options exist and were absent: SixBit "Home & Hobby Edition $29.99/mo" works with eBay and Etsy on every edition but "Works with Shopify" only from the $99.99 Enterprise edition; 30-day trial, card required. Auctiva is eBay-only from "Base+ $9.95/ mo" with "100 Included Listings / mo" and a GMV cap.
- ExportYourStore appears in Crosslist's September 2026 roundup and in the App Store but was missing: "Starter $23/mo billed annually" for "100 listings included 1 source store unlimited selling channels", eBay, Etsy and Shopify integrations, "Sync Frequency 2 HOURS". It "is now part of Threecolts".
- Open source: stallkit (MIT, 26 stars) is an Etsy-only local tool for "bulk listings from CSV" via "the official Etsy Open API v3", which Etsy itself lacks; BlackCatReseller (MIT, Windows beta) crosslists to eBay, Depop, Poshmark, Mercari and "eligible Etsy" by browser automation, which eBay's user agreement restricts. No open-source tool covers all three channels by API.
- Defunct, acquired or renamed: inkfrog.com redirects to Wix's multichannel page; Shopify Marketplace Connect is "formerly Codisto"; Sellbrite's footer reads "GoDaddy Sellbrite, Inc."; ExportYourStore is under Threecolts; Posh Sidekick's app is published as "Sidekick Tools". Reeva could not be found on any domain or in the App Store and should be dropped from the sheet. Flyp, ResellKit, SimplyListed, ResaleOS and SpareDollar were all unreachable today.
- Caution for one-of-one stock: Secnd, Swiftlisted, VendorSnap and EzList are months old with 0 to 48 App Store ratings each. Their free tiers and trials cost nothing to test, but sold-detection should be proven on a cheap item before trusting it with a lamp that exists once.

## 1. Comparison table: tools missing from the lane 01 list

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Swiftlisted | Crosslister: eBay and Shopify by API from phone or web; Etsy, Depop, Grailed, Vinted, Whatnot, FBMP, Vestiaire via Chrome extension; AI listing from photo; sold detection every 30 min | "Starter $6 USD/mo $72 USD billed yearly"; "Pro $22 USD/mo $264 USD billed yearly"; "Expert $49 USD/mo" (yearly toggle rendered; monthly prices U) | "Free trial $0 for 30 days 30 days. No credit card."; "Is there a free plan? No." | Web, Chrome extension, iPhone | High: all three channels, auto-delist on the cheapest plan; Etsy runs through the extension, not the API; brand new | V | https://www.swiftlisted.ai/pricing |
| Secnd | Cross-listing and inventory for resellers and consignment shops; eBay, Etsy, Shopify, Depop; Square and Shopify sync; auto-delist | "Free $0 CAD/mo Free forever"; "Starter $29 CAD/mo Billed monthly"; "Growth $60 CAD/mo"; "All prices in Canadian dollars." | Free plan: "Unlimited cross-posting", "AI listings — 5 / month", "Sale detection", "Inventory sync + automatic delisting" | Web, iPhone | High on paper: free, all three channels, auto-delist; tiny (17 ratings), CAD billing, eBay named only in examples | V | https://www.secnd.ca/pricing |
| VendorSnap | Phone crosslister: one photo prices and lists on eBay, Etsy, FBMP, Vinted, Depop, Poshmark; mark sold once and all copies come down; in-person register | Pro "$6.67/month Billed yearly at $79.99. Save 33%."; Business "$15.00/month Billed yearly at $179.99." (monthly toggle prices U) | Free plan ("No credit card needed", inventory, register, "150 Price Checks and 60 Shelf Checks a month"); listing online needs Pro; "7-day free trial for new subscribers" | iPhone, Android | High for Etsy + eBay from the phone: "eBay and Etsy list through their official APIs"; no Shopify | V | https://vendorsnap.app/ |
| EzList | Photo to finished listing on FBMP, eBay, Etsy, Reverb, Depop, Mercari; one-tap delisting | "EzList PRO $9.99 / month Up to 100 published listings a month." | "Free $0 3 published listings, no time limit"; "No card required" | iPhone, Android | Medium: Etsy + eBay cheap; no Shopify; 2 App Store ratings; Texas LLC | V | https://ezlistiapp.com/ |
| Hero (Hero Stuff) | AI listing from a photo, price from eBay sold data, posts to eBay and Facebook Marketplace; Shopify catalog import | "Starter $10 / month For selling up to 10 items each month."; "Semi Pro $20 / month"; "Pro $30 / month" unlimited; "Business $199 / month" | "5 price checks and 1 published item every 30 days. No credit card required." | Web, iPhone, Android | Low-medium: "currently supports ... eBay and Facebook Marketplace"; no Etsy or Shopify posting; 2,071 ratings, 4.7 | V | https://www.herostuff.com/pricing |
| Flippr | Bulk photo valuation from eBay sold data plus an eBay autolister | No price on the site; pricing page 404. App Store: "Start free and upgrade for more scans." | Free scans (App Store text) | iPhone, Android, web | Low: eBay only, sourcing-first; 1,970 ratings | V features / U price | https://useflippr.com/ |
| Lista | Phone crosslister: "post it to eBay, Mercari, Poshmark, Depop, and Grailed instantly"; AI measurements and photos | In-app subscription; no price in listing text | "free trial period if offered" | iPhone | Low: no Etsy or Shopify; 146 ratings | V (App Store) / U price | https://apps.apple.com/us/app/lista-ai-crosslisting-tools/id1634103692 |
| SellOut | AI listing generator, "crosslisted to major marketplaces like eBay, Poshmark, Depop, and more" | In-app; no price in listing text | unknown | iPhone | Low: no Etsy or Shopify named; last update 2026-04-18 | V (App Store) / U price | https://apps.apple.com/us/app/sellout-ai-powered-listing/id6462701350 |
| Reclaim | Photo to listing for eBay and Facebook Marketplace; "COMING SOON One-click crosslisting" | Pricing page 404; price unknown | unknown | iPhone | Low: eBay + FBMP only, crosslisting not shipped | V (App Store) / U price | https://apps.apple.com/us/app/reclaim-sell-with-ai/id6748927454 |
| SixBit | Windows desktop listing and inventory software (since 1997): eBay US/UK/CA/AU and Etsy on every edition; Shopify from Enterprise | "Home & Hobby Edition $29.99/mo"; "Small Business Edition $49.99/mo"; "Enterprise Edition $99.99/mo" | "try it for 30 days free! (NEW Customers Only)"; "A card is required to start your trial" | Windows ("Windows 8, 10 & Windows Server 2012 or newer") | Medium-low: native on Ricky's PC and covers Etsy + eBay, but $29.99 for two channels, Shopify only at $99.99, "Automatic Quantity Adjustments" only at Enterprise | V | https://www.sixbitsoftware.com/pricing/ |
| Auctiva | eBay listing tool and templates; multi-channel plan exists | eBay Only: "Base+ $9.95/ mo" ("100 Included Listings / mo", "$1,000 included GMV"); "Plus+ $16.95/ mo Unlimited Listings"; "Max+ $24.95/ mo" (Multi-Channel tab prices did not render, U) | "30-day free trial" | Web | Low: eBay first; Etsy and Shopify support not confirmed on the page | V | https://www.auctiva.com/ |
| ExportYourStore (Threecolts) | Sync one source store (Shopify or eBay) to unlimited channels incl. eBay, Etsy, Shopify, Amazon; AI listing enhancements | "Starter $23/mo billed annually" ("100 listings included 1 source store unlimited selling channels unlimited orders"); Growth "$47/mo billed annually" 500 listings; "Unlimited AI enhancements - $8.99/mo" (monthly toggle prices U) | "Start Free Trial" (length not stated) | Web, iOS companion app | Medium: works if Shopify is the master catalog and stock stays under 100; "Sync Frequency 2 HOURS" is a double-sale window | V | https://www.exportyourstore.com/pricing |
| QuickSync: Etsy Integration | Shopify app: Shopify and Etsy stock, product and order sync | "Lite Plan $19 / month or $205/year and save 10%"; "Pro Plan $29 / month"; "Ultra Plan $69 / month" | "Free: $0, 100-variant stock sync for eligible shops."; "14-day free trial" | Shopify app | Medium-high: free stock sync for a 52-item shop; order sync needs Pro; 4.8 stars (2,022) | V | https://apps.shopify.com/quicksync-etsy |
| Shuttle ‑ Sync with Etsy | Shopify app: product, inventory, order and review sync with Etsy | "Essential $12 / month or $120/year and save 17%"; "Growth $19 / month" with "Real-time stock sync (200 orders/mo)"; "Scale $39 / month" | Free: "10 product transfers per month 10 order transfers per month", "Connect one Etsy shop"; "Optional 14-day all-features trial" | Shopify app ("Built for Shopify") | Medium: real-time stock sync starts at $19; free tier is for manual transfers; 4.7 (229) | V | https://apps.shopify.com/shuttle-transfer-from-etsy |
| shopUpz ‑ Etsy Sync & Import | Shopify app: import and export listings between Shopify and Etsy, SKU link, quantity sync | "Starter $9.99 / month" ("Export UNLIMITED listings to Etsy"); "UNLIMITED $18 / month" ("Sync UNLIMITED quantities, Locations"); "PRO $38 / month" | Free: "Import 20 Listings from Etsy"; "3-day free trial" | Shopify app ("Built for Shopify") | Medium: cheapest unlimited Shopify-to-Etsy export; quantity sync is the $18 tier; 4.7 (198) | V | https://apps.shopify.com/shopupz-inventory |
| InfoShore Etsy Integration | Shopify app: Etsy inventory, order and product sync with price markup | "Bronze $19.99 / month or $199/year and save 17%" ("Import 500 items/month", "Inventory Sync", "Real time Sync"); "Silver $29.99"; "Gold $59.99" | Free: "Manage/Import 5 items No Product Sync No Inventory Sync" | Shopify app ("Built for Shopify") | Medium-low: priced like QuickSync Lite with fewer reviews (4.9, 29) | V | https://apps.shopify.com/etsy-importer-2 |
| Trunk | Real-time stock sync across Shopify, Etsy, eBay, Faire, Amazon, Square; no listing creation | "From $35/month. Free trial available."; "$35" plan "or $45/mo: 101-200 orders/mo"; second plan "$39" | "14-day free trial", "no credit card required" | Web, Shopify app | Medium: the only tool read that keeps Shopify, Etsy and eBay quantities in step in real time; $35 buys sale detection, not listing | V | https://apps.shopify.com/trunk |
| Sellbery | Multichannel listing and order sync: Shopify, eBay, Etsy, Amazon; AI copy | "Marketplaces $19 /mo 100 orders per month"; "Dropshippers $39 /mo 500 orders" | "Try Sellbery free for 7 days, then start your first month for $1 no credit card required" | Web | Medium-low: "Every 1 hour Orders sync" on the $19 plan; built for volume sellers | V | https://sellbery.com/pricing/ |
| Koongo | EU feed and marketplace manager; eBay listed, Etsy not seen | "Free €0 per month"; "Lite € 35 per month" ("Updates every 6 hours") | "1 store, 100 items, 1 feed, 1 marketplace, 1 ad channel and up to 10 orders per month." "no time limit" | Web | Low: euro billing, Etsy not found on the channels page, 6-hour updates | V | https://www.koongo.com/pricing/ |
| stallkit (open source) | Local Etsy automation: "bulk listings from CSV, order and tracking sync, SEO analysis, and designs-to-drafts via the official Etsy Open API v3" | Free; "MIT License Copyright (c) 2026 stallkit contributors" | "no account to create, no subscription and no server in between" | Runs locally, opens in the browser at localhost; needs your own Etsy developer app | Low-medium: Etsy only, built for design and print sellers, but it gives Etsy a CSV bulk-create that Etsy lacks | V | https://github.com/MoneyPrintLabs/stallkit |
| BlackCatReseller (open source) | "Free, local-first Windows inventory, crosslisting, and sales app for clothing resellers. MIT licensed." Crosslists to eBay, Depop, Poshmark, Mercari, "eligible Etsy" | Free, MIT | Free | Windows ("Status: Windows beta.", unsigned installer) | Low: "Browser automation requires a connected second monitor and signed-in Chrome"; eBay bans automated access; clothing focus; no Shopify | V | https://github.com/GasWhatWeSmoke/BlackCatReseller |
| ClosetPilot | Poshmark sharing bot with a free plan | "$0 / month 100 shares per day"; paid "$29.99" after "Try it FREE for 7 days" | Free forever | Web | Skip: Poshmark only, not a lister for Hollie's channels | V | https://closetpilot.com/pricing/ |
| CrazyLister | eBay and Amazon listing templates and bulk lister (alive, not defunct) | "USD $20 / mo" for "Up to 100" active listings; "USD $32 / mo" | "Unlimited for 7 Days, No Credit Card Required" | Web | Skip: eBay and Amazon only, template tool | V | https://crazylister.com/pricing |
| Listing Mirror | Multichannel listing and inventory (enterprise) | Pricing URL redirected to a feature page; no prices shown | unknown | Web | Skip: enterprise sales motion | U | https://www.listingmirror.com/pricing/ |

Seen in the App Store catalog but not researched further (each under 10 ratings or no marketplace list): CrossFlip (released 2026-08-16), Crosslist AI by Hoftware (clothing only, export not post), Ivy Crosslisting (Safari extension for FBMP, OfferUp, Craigslist), Resylr, List Forge AI, Shelvio, ListIt, SnapDone, ARC Resell, ListOnce, Ruit, ListSmarter, QuickList, Trendy Lister, Vendly, Klysto. None of these names Shopify or Etsy in its listing title.

## 2. Defunct, acquired or renamed (with evidence read today)

- inkFrog (on the list, "shut down"): https://www.inkfrog.com/ resolves to https://www.wix.com/ecommerce/sell/multichannel (V). Value Added Resource, "Published: May 15 2026": "Wix-Owned InkFrog to Shut Down June 1 as eBay Sellers Seek Alternatives" (V page, third-party claim on the date). Confirmed gone. The same article says inkFrog co-founder Tomas Salas "is retooling and relaunching SpareDollar"; sparedollar.com returned an empty page today (U).
- Codisto became Shopify Marketplace Connect (on the list under the new name): "Shopify Marketplace Connect (formerly Codisto) is the fastest and easiest way to sell across top global marketplaces" (V, https://apps.shopify.com/marketplace-connect). Any roundup still naming Codisto means this app.
- Sellbrite (on the list) is a GoDaddy brand: footer "©2024 GoDaddy Sellbrite, Inc. All rights reserved." (V, https://www.sellbrite.com/).
- ExportYourStore (missing from the list) is now owned by Threecolts: "We're expanding! ExportYourStore is now part of Threecolts" (V, https://www.exportyourstore.com/); the iOS companion app is published by "Threecolts UK LTD" (App Store catalog).
- Posh Sidekick (on the list) publishes its app as "Sidekick Tools" (developer Michael Chierchio, 2,353 ratings) in the App Store catalog (V). The site is still poshsidekick.com.
- Nifty (on the list) was Auto Posher; the lane agent recorded this from nifty.ai today. Not re-read.
- Reeva (on the list as U): no reseller product found anywhere today. reeva.ai is an industrial software company (lane agent, today); reeva.app is a Saudi salon WhatsApp sales bot (V, Arabic page); reeva.co returned HTTP 402; www.reeva.com returned 502; getreeva.com returned an empty page; the App Store catalog search for "reeva" returns a beauty booking app, a Taiwanese hardware app and a video generator, no reseller app. Recommend removing Reeva from the sheet unless Ricky has a URL.
- Flyp (on the list as U): flyp.com returned 64 characters of text today (same wall the lane agent hit); the App Store catalog search for "flyp" returns "FLYP - Fashion Design Studio" and "FLYP - BUSINESS", neither a reseller tool. Crosslist's September 2026 roundup still names Flyp 48 times, so it probably still operates. Status U.
- ResellKit (named in OneShop's and Vendoo's comparison pages): resellkit.com/pricing returned 223 characters and www.resellkit.com failed TLS ("unrecognized name") and 502. Possibly dead. U.
- SimplyListed and ResaleOS (lane agent's unresearched leads): simplylisted.com fails with a certificate name mismatch on both hosts; resaleos.com fails at the proxy tunnel (502). Both U, both likely gone or parked.
- CrazyLister and Auctiva, two old eBay names, are alive and selling plans today (V, see table). Frooition is alive (its pricing URL is a 404 but the site serves eBay software pages).
- Turbo Lister: SixBit's testimonials refer to it in the past tense ("Way better than Turbo Lister"); eBay retired it years ago. Not on the list; noted so nobody re-adds it.

## 3. Notes per tool

### Swiftlisted (V)
- Pricing page shows the yearly toggle: Starter "$6 USD/mo" "$72 USD billed yearly" (250 stored items, unlimited crosslisting, 150 AI listings a month, "Automatic sold detection & delisting"); Pro "$22 USD/mo" "$264 USD billed yearly" (1,000 items, marketplace imports, bulk cross-listing, relisting); Expert "$49 USD/mo" "$588 USD billed yearly". Monthly-billing prices did not render; U.
- Trial: "Every account starts with a 30-day free trial and no credit card. The first 7 days include Pro features"; after 30 days "Account locks ... until you choose a plan".
- Sold detection: "Every plan, including the free trial, scans your active listings every 30 minutes." Auto-delist on every paid plan.
- How it posts: the iPhone app posts "to eBay or Shopify from your phone"; for "Depop, Grailed, Vinted, Etsy, Whatnot, Facebook Marketplace and Vestiaire Collective, the phone sends the item to Swiftlisted open on your computer, and the Swiftlisted Chrome extension posts it." Pricing FAQ: "Swiftlisted handles automation locally within your browser extension session." So Etsy is extension-driven, not API-driven, and the PC must be on.
- Company: "Swiftlisted is a product of Institor Pty Ltd (ABN 58 701 476 226), Australia." USD billing offered. App Store listing released 2026-11-05 with 0 ratings.
- Fit: the cheapest tool with all three channels and auto-delist on the entry plan, but it is days old on mobile. Trial it for 30 days at no cost; judge the Etsy extension flow on the Windows PC.

### Secnd (V)
- "Free $0 CAD/mo Free forever": "Unlimited cross-posting", "Connect unlimited marketplaces", "AI listings — 5 / month", "Sale detection", "Inventory sync + automatic delisting". Starter "$29 CAD/mo Billed monthly" adds "Automatic offers" and 100 AI listings; Growth "$60 CAD/mo". "Every plan includes cross-listing, inventory sync, automatic delisting, sale detection, and AI listing generation".
- Channels: home page shows eBay, Etsy and Shopify in its examples and footers print API notices for Etsy, Depop and Shopify. No eBay API notice is printed; eBay support is shown only in examples and a fee calculator. Check in the trial.
- Platform: "Use SECND on web or mobile"; iPhone app released 2026-03-10, 17 ratings, 4.1. Aimed at "Consignment stores, Thrift & antique stores, Vendor malls, Estate sale companies", which matches Hollie's stock better than the fashion-first apps. Canadian company; CAD billing.
- Fit: free plan is the strongest zero-cost offer found for all three channels. Verify eBay posting and sale detection on a cheap item first.

### VendorSnap (V)
- Pricing is on the home page (the /pricing URL is a 404): Free ("No credit card needed", inventory with QR price tags, register, "150 Price Checks and 60 Shelf Checks a month", "2 shops"); Pro "$6.67/month Billed yearly at $79.99. Save 33%." ("List on eBay, Etsy, Facebook Marketplace, Vinted, Depop and Poshmark", "Mark it sold, and it's taken down everywhere", "Stage with AI: 90 studio photos a month", "7-day free trial for new subscribers"); Business "$15.00/month Billed yearly at $179.99." The Monthly toggle exists but its prices did not render; U. "Plans renew until you cancel in your App Store or Google Play settings".
- How it posts: "eBay and Etsy list through their official APIs. Facebook Marketplace, Vinted, Depop and Poshmark are filled in on your phone, through your own sign-in". Sold: "eBay and Etsy end through their APIs ... your phone takes them down for you" on the others. "Change a price or a photo and your eBay and Etsy listings update in place."
- Platform: "The reseller app for iPhone and Android"; "no laptop, no browser extension, nothing left running at home." App Store released 2026-06-16, 48 ratings, 4.9.
- Gotchas: no Shopify; no desktop. Its copy names "antiques and estate lots" and a "BRASS LAMP" example, so the item types fit. Good phone companion to a Shopify store if Shopify stock is synced by another tool.

### EzList (V)
- "Free $0 3 published listings, no time limit", "Failed listings do not count", "No card required". "EzList PRO $9.99 / month Up to 100 published listings a month. Cancel anytime." "Cross listing to every marketplace", "One-tap delisting".
- Channels: "Facebook Marketplace, eBay, Etsy, Reverb, Depop and Mercari" (FBMP "beta" per App Store). No Shopify. iPhone and Android ("DOWNLOAD ON THE App Store GET IT ON Google Play"). "© 2026 Epitaxy Lab LLC · Denton, Texas". App Store released 2026-04-29, 2 ratings.
- Fit: cheap and covers Etsy + eBay from the phone; tiny user base; sale detection not described beyond one-tap delisting.

### Hero (V)
- Plans: "Starter $10 / month For selling up to 10 items each month."; "Semi Pro $20 / month" (30 items); "Pro $30 / month" ("Publish as many items as you need"); "Business $199 / month". Free account: "5 price checks and 1 published item every 30 days. No credit card required."
- Channels: "Hero Stuff currently supports popular selling platforms including eBay and Facebook Marketplace." Shopify and WooCommerce are import sources only ("connect Shopify, import your catalog, list everything" to eBay and FBMP). No Etsy.
- Platform: web (herostuff.com), iOS and Android ("Rated five stars on Apple and Google App Store"); 2,071 App Store ratings, 4.7; released 2024-09-20.
- Fit: polished and popular, but wrong channel mix for Hollie.

### Flippr (V features, U price), Lista, SellOut, Reclaim (App Store records, U price)
- Flippr: "Snap a photo of a pile ... Flippr identifies multiple items, pulls real marketplace sold comps" and has an "eBay autolister"; "Start free and upgrade for more scans." Site has no price; pricing page 404. Sourcing tool first. 1,970 ratings.
- Lista: "Create your listing once and post it to eBay, Mercari, Poshmark, Depop, and Grailed instantly." iPhone only, subscription in-app. No Etsy, no Shopify.
- SellOut: "crosslisted to major marketplaces like eBay, Poshmark, Depop, and more"; last update 2026-04-18. No Etsy or Shopify named.
- Reclaim: "Integrated: eBay Facebook Marketplace"; "COMING SOON One-click crosslisting to eBay, Facebook Marketplace, Whatnot, Depop, Poshmark". Not a crosslister yet.

### SixBit (V)
- Windows desktop software ("Client Machine Windows 8, 10 & Windows Server 2012 or newer"). "Home & Hobby Edition $29.99/mo" (2 selling accounts, batch edits, custom fields, CSV import/export), "Small Business Edition $49.99/mo" (inventory tracking, P&L, "Free Listing Scheduling"), "Enterprise Edition $99.99/mo" ("Automatic Relisting", "Automatic Quantity Adjustments", Shopify). Feature grid: "Works with eBay US, UK, CA and AU" and "Works with Etsy" on all editions; "Works with Shopify" only Enterprise and above.
- Trial: "Pick a package, try it for 30 days free! (NEW Customers Only)"; "A card is required to start your trial, but you won't be charged until your trial ends."
- Fit: the only Windows-native lister found. For Hollie it buys eBay + Etsy for $29.99 with no Shopify and no cross-channel quantity sync below $99.99, so the cloud crosslisters beat it on price.

### Auctiva (V)
- eBay Only tab: "Base+ $9.95/ mo" ("100 Included Listings / mo", "$1,000 included GMV"), "Plus+ $16.95/ mo" ("Unlimited Listings", "$2,000 included GMV", "AI-Powered Item Attributes"), "Max+ $24.95/ mo" ("$3,500 included GMV"). "30-day free trial". The Multi-Channel tab prices did not render (U). GMV caps mean fees above the included sales volume.
- "For more than four years, Auctiva has consistently operated as an eBay Gold Solution Partner." eBay-first; Etsy and Shopify were not named on the page read.

### ExportYourStore (V)
- Yearly toggle rendered: "Starter $23/mo billed annually save $72!" with "100 listings included 1 source store unlimited selling channels unlimited orders support: email only 25 AI enhancements"; "Growth $47/mo billed annually" 500 listings; "Business $79/mo"; "Enterprise $199/mo". Extras: "Unlimited AI enhancements - $8.99/mo", "Additional source store - $19/mo". Comparison table: "Sync Frequency 2 HOURS" on every plan. Monthly prices did not render (U).
- Integrations page lists eBay, Etsy, Shopify, WooCommerce, Amazon and more. Model: one source store (import from) pushed to target channels (export to). The iOS app is only a dashboard ("companion app for the ExportYourStore platform").
- Ownership: "ExportYourStore is now part of Threecolts". Appears in Crosslist's "Best 10 Cross Listing Apps in 2026" roundup (September 30, 2026) and in the App Store, so it met the two-source bar.
- Fit: workable if the Shopify store becomes the master and stock stays under 100 listings, but the 2-hour sync leaves a double-sale window on one-of-one items; yearly billing.

### QuickSync: Etsy Integration (Shopify app, V)
- "From $19/month. Free trial available." Plans: "Lite Plan $19 / month or $205/year and save 10%" ("Inventory syncing", "Import Etsy products", "Up to 1,000 syncing variants", "14-day free trial"); "Pro Plan $29 / month" adds "Product detail syncing", "New Etsy order syncing", 2,500 variants; "Ultra Plan $69 / month". Fine print: "Free: $0, 100-variant stock sync for eligible shops. Lite: 2 shops; extras $19/mo each."
- 4.8 stars, 2,022 reviews, developer "R. I. T. N. S.", "Based in United States". The lane agent's URL /quicksync-for-etsy was a 404; the live slug is /quicksync-etsy.
- Fit: a 52-item shop sits under the 100-variant free limit, so Shopify and Etsy quantities can stay in step at no cost. Order import needs Pro. Does not touch eBay.

### Shuttle ‑ Sync with Etsy (Shopify app, V)
- Free: "10 product transfers per month 10 order transfers per month 10 Etsy reviews stored per month Unlimited product updates Connect one Etsy shop Manual transfers". "Optional 14-day all-features trial". "Bulk runs & auto-sync on paid plans".
- "Essential $12 / month or $120/year and save 17%" (unlimited transfers, SKU auto-match, "Auto-transfer new products"); "Growth $19 / month or $190/year" ("Real-time stock sync (200 orders/mo)", "Automatic order transers", "Prevent overselling instantly"); "Scale $39 / month".
- 4.7 stars (229), developer Illumiko, "Built for Shopify". A review asks for manual match/unmatch of products.
- Fit: stock sync that stops a double sale is the $19 tier; the free tier only moves 10 products a month by hand.

### shopUpz ‑ Etsy Sync & Import (Shopify app, V)
- Free: "Import 20 Listings from Etsy". "Starter $9.99 / month": "Export UNLIMITED listings to Etsy", "Import UNLIMITED listings from Etsy", "Update Etsy Listing Prices", "Generate SKUs". "UNLIMITED $18 / month": adds "Manage UNLIMITED orders", "Sync UNLIMITED quantities, Locations". "PRO $38 / month": two Etsy stores. "3-day free trial" on paid plans. 4.7 stars (198).
- Fit: the cheapest way to push a Shopify catalog to Etsy; quantity sync (the one-of-one safeguard) is the $18 plan.

### InfoShore Etsy Integration (Shopify app, V)
- Free: "Manage/Import 5 items", "No Product Sync", "No Inventory Sync". "Bronze $19.99 / month or $199/year and save 17%": "Import 500 items/month", "Sync upto 1500 items", "Inventory Sync", "Price Sync", "Real time Sync". "Silver $29.99", "Gold $59.99". 4.9 stars (29). "Set different Etsy prices automatically — cover fees with a % or fixed markup".

### Trunk (V)
- Shopify App Store: "From $35/month. Free trial available."; plan "$35" "or $45/mo: 101-200 orders/mo, or $59/mo: 201-400 orders/mo"; second plan "$39" (bundling). "14-day free trial". Home: "It's a 14-day free trial and includes all features with no credit card required." Channels on the home page: eBay, Etsy, Shopify, Faire, Amazon, Square. 4.9 stars (409). "Trunk doesn't care about your listing content when it comes to syncing stock levels"; "Etsy listings require special handling when they need to be adjusted out of stock."
- Fit: it is sale detection across all three of Hollie's channels in real time, which no crosslister on the list offers for Shopify. It does not create listings. $35 is inside the budget but buys only this.

### Sellbery (V)
- "Marketplaces $19 /mo 100 orders per month 75,000 Words Sellbery AI Unlimited Channels Unlimited SKUs Every 1 hour Orders sync". "Dropshippers $39 /mo" (500 orders, "Every 10 min"). "Try Sellbery free for 7 days, then start your first month for $1 no credit card required". Channel logos include Shopify, eBay, Etsy. Hourly sync; volume-seller framing.

### Koongo (V)
- "Free €0 per month 1 store, 100 items, 1 feed, 1 marketplace, 1 ad channel and up to 10 orders per month." "no time limit". "Lite € 35 per month ... Updates every 6 hours". "All paid plans include a 7-day free trial." Channels page shows Amazon and eBay; Etsy did not appear in the page text. FAQ: "sell on multiple channels like Amazon, Google Shopping, and European marketplaces." EU-centred; low fit.

### stallkit (open source, V)
- Repository title: "Open-source Etsy seller automation CLI: bulk listings from CSV, order and tracking sync, SEO analysis, and designs-to-drafts via the official Etsy Open API v3. Runs locally with your own API app." README: "Double-click it and it opens in your browser at http://localhost:3000"; "It talks to the official Etsy Open API v3 through your own free Etsy app. There is no account to create, no subscription and no server in between." LICENSE: "MIT License Copyright (c) 2026 stallkit contributors". 26 stars. Setup needs an Etsy developer app ("Create an app at https://www.etsy.com/developers/register-seller-app") and a callback URL; much of the README is in Turkish.
- Licence: MIT, commercial use fine. Fit: Etsy only, built for design and print-on-demand sellers; the CSV bulk-create is the one thing a vintage seller might borrow.

### BlackCatReseller (open source, V)
- "A free, local-first Windows workspace for clothing resellers." "Open source under the MIT License." "Status: Windows beta." "Crosslists through your signed-in eBay, Depop, Poshmark, Mercari, and eligible Etsy accounts". "Browser automation requires a connected second monitor and signed-in Chrome." "This beta is unsigned; if Windows blocks it, report the result ... rather than disabling security protections."
- Gotchas: browser automation against eBay is the activity eBay's User Agreement restricts (lane 01 report quotes it); clothing focus; no Shopify; beta quality. Not for Hollie's stock.

### Terms and licence notes for the new names
- API-based posting (safer under eBay's and Etsy's terms): VendorSnap (eBay, Etsy), Swiftlisted (eBay, Shopify), Secnd (prints Etsy, Depop, Shopify API notices), all Shopify sync apps (Shopify and Etsy APIs), Trunk, ExportYourStore, Sellbery, SixBit, Auctiva, stallkit.
- Extension or phone automation (riskier, needs a device on): Swiftlisted for Etsy and the non-API marketplaces; VendorSnap for FBMP, Vinted, Depop, Poshmark; BlackCatReseller for everything; Flyp unknown.
- Currency: Secnd bills in CAD; Swiftlisted offers USD; Koongo in EUR; Zipsale (on the list) in GBP.
- No watermark or non-commercial licence issue was seen on any page read. Both open-source tools are MIT.

## 4. Recommendation for Hollie (additions to the lane 01 picks)

Free first, install today:
1. Secnd free plan (web, plus the iPhone app for intake). It is the only zero-cost tool found with eBay, Etsy and Shopify plus "Inventory sync + automatic delisting". Test with two cheap items: list, buy or end one on eBay, and watch whether the Etsy and Shopify copies come down.
2. Swiftlisted 30-day trial (no card). Compare its eBay-by-API and Etsy-by-extension flow with Secnd's. If it wins, Starter is "$6 USD/mo" on yearly billing, the cheapest all-three-channels plan with auto-delist.
3. VendorSnap free, then its 7-day Pro trial, for listing from the iPhone in the room: Etsy and eBay through official APIs, mark-sold takes both down. Keep Shopify in sync some other way.
4. When the Shopify store exists: QuickSync's free 100-variant stock sync between Shopify and Etsy, or Shuttle's free tier for the first product transfers. Neither costs anything.

Pay only once it earns it (all under $50 a month):
- Trunk at "$35/month" if, and only if, Shopify, Etsy and eBay all carry the same one-of-one items and a crosslister's sale detection has missed one. It is the only real-time three-way stock sync read today.
- Shuttle Growth "$19 / month" or shopUpz "$18 / month" for Shopify-to-Etsy quantity sync if the free QuickSync tier is not available to the shop.
- EzList PRO "$9.99 / month" only as a phone-only fallback if VendorSnap fails; it has no Shopify and almost no users.

Skip and why:
- Hero, Flippr, Reclaim, Lista, SellOut: no Etsy or no Shopify posting; built for eBay plus Facebook or fashion apps.
- SixBit ($29.99 for eBay + Etsy, Shopify at $99.99) and Auctiva (eBay only): the cloud crosslisters on the list do more for less.
- ExportYourStore ($23 yearly-billed for 100 listings, 2-hour sync), Sellbery, Koongo, InfoShore: sync tools priced above the reseller crosslisters, or EU-centred.
- BlackCatReseller: browser-automation crosslisting is the eBay terms risk the lane 01 report warns about. stallkit: Etsy only and aimed at print sellers.
- Reeva: cannot be found; remove from the sheet. Flyp: still walled; only Ricky's own browser can settle it.

## 5. Gaps and pages that would not load

- WebSearch: zero searches were possible (shared per-turn budget exhausted before this agent ran). Discovery relied on the App Store catalog, Shopify App Store categories, GitHub topics and roundups already in the scratchpad. Android-only tools and tools with no App Store or Shopify listing may be missed.
- Product Hunt: https://www.producthunt.com/products/vendorsnap and /products/swiftlisted returned HTTP 403. Chrome Web Store pages need extension IDs and were not attempted.
- Monthly-billing prices did not render for Swiftlisted, VendorSnap and ExportYourStore (yearly toggle shown; monthly U). Auctiva's Multi-Channel tab prices did not render.
- Failed fetches: https://vendorsnap.app/pricing (404; prices are on the home page), https://www.useflippr.com/pricing (404), https://www.reclaimstuff.com/pricing (404), https://www.auctiva.com/pricing (404), https://www.frooition.com/pricing (404), https://www.trunkinventory.com/pricing (405; home and Shopify listing used instead), https://apps.shopify.com/categories/sales-channels-marketplaces (404), https://apps.shopify.com/etsy-integration-quicksync and /etsy-quicksync (404; live slug /quicksync-etsy), https://apps.shopify.com/shuttle, /shuttle-sync-with-etsy, /shuttle-etsy (404; live slug /shuttle-transfer-from-etsy), https://resellkit.com/pricing and https://www.resellkit.com/ (empty / TLS unrecognized name / 502), https://sparedollar.com/ (empty), https://flyp.com/ (64 chars, wall), https://reeva.co/ (402), https://www.reeva.com/ (502), https://getreeva.com/ (empty), https://resaleos.com/ (proxy tunnel 502), https://simplylisted.com/ (certificate mismatch), https://raw.githubusercontent.com/GasWhatWeSmoke/BlackCatReseller/main/LICENSE (404; README states MIT and links LICENSE.txt), https://www.listingmirror.com/pricing/ (redirected to a feature page without prices).
- Secnd's eBay support is shown in examples, not in an API notice; confirm in the trial. Koongo's Etsy support was not found on its channels page.
- Lista and SellOut have no vendor site in their App Store records; prices are in-app only.
- The Crosslist roundup used as a second source was fetched earlier today by the lane 01 agent; its URL was not preserved in the saved text (title "Best 10 Cross Listing Apps in 2026 for Resellers", "Last updated on: September 30, 2026", crosslist.com/blog).

## 6. Sources

Pages fetched 2026-11-07 by this agent (V unless marked failed):
- https://itunes.apple.com/search?term=crosslist&entity=software&country=us (App Store catalog; also terms crosslisting, cross list reseller, reseller listing, reeva reseller, reeva, flyp, list perfectly, closo, voolist)
- https://itunes.apple.com/lookup?id=6479718293 (Hero), 6746770511 (Flippr), 1634103692 (Lista), 6462701350 (SellOut), 6778664113 (VendorSnap), 6745438570 (CrossFlip), 6754613112 (Secnd), 6813712271 (Swiftlisted), 6748927454 (Reclaim), 6758005659 (Crosslist AI), 6762538109 (EzList), 6764057253 (ExportYourStore), 6747253063 (Ivy)
- https://apps.apple.com/us/app/lista-ai-crosslisting-tools/id1634103692 (record via lookup API)
- https://apps.apple.com/us/app/sellout-ai-powered-listing/id6462701350 (record via lookup API)
- https://apps.apple.com/us/app/reclaim-sell-with-ai/id6748927454 (record via lookup API)
- https://apps.apple.com/us/app/vendorsnap-crosslisting/id6778664113 (record via lookup API)
- https://apps.apple.com/us/app/swiftlisted-crosslist-sell/id6813712271 (record via lookup API)
- https://apps.apple.com/us/app/secnd-list-sell-sync/id6754613112 (record via lookup API)
- https://apps.apple.com/us/app/ezlist-smart-cross-listing/id6762538109 (record via lookup API)
- https://apps.apple.com/us/app/hero-ai-reseller-listing-app/id6479718293 (record via lookup API)
- https://apps.apple.com/us/app/flippr-complete-reselling-app/id6746770511 (record via lookup API)
- https://apps.apple.com/us/app/exportyourstore/id6764057253 (record via lookup API)
- https://apps.shopify.com/categories (redirected to the App Store home)
- https://apps.shopify.com/categories/sales-channels
- https://apps.shopify.com/categories/sales-channels-selling-online-marketplaces/all
- https://apps.shopify.com/categories/sales-channels-marketplaces (failed, 404)
- https://apps.shopify.com/quicksync-etsy
- https://apps.shopify.com/etsy-integration-quicksync (failed, 404)
- https://apps.shopify.com/etsy-quicksync (failed, 404)
- https://apps.shopify.com/shuttle-transfer-from-etsy
- https://apps.shopify.com/shuttle (failed, 404)
- https://apps.shopify.com/shuttle-sync-with-etsy (failed, 404)
- https://apps.shopify.com/shuttle-etsy (failed, 404)
- https://apps.shopify.com/shopupz-inventory
- https://apps.shopify.com/etsy-importer-2
- https://apps.shopify.com/trunk
- https://apps.shopify.com/marketplace-connect
- https://github.com/topics/crosslisting
- https://github.com/topics/ebay-seller
- https://github.com/topics/etsy-api
- https://github.com/topics/reseller
- https://github.com/topics/crosslist
- https://github.com/topics/cross-listing
- https://github.com/topics/ebay-listing
- https://github.com/topics/poshmark
- https://github.com/And1zle/eBayOS
- https://github.com/MoneyPrintLabs/stallkit
- https://raw.githubusercontent.com/MoneyPrintLabs/stallkit/main/LICENSE
- https://github.com/malikad778/nexus-inventory
- https://github.com/GasWhatWeSmoke/BlackCatReseller
- https://raw.githubusercontent.com/GasWhatWeSmoke/BlackCatReseller/main/README.md
- https://raw.githubusercontent.com/GasWhatWeSmoke/BlackCatReseller/main/LICENSE (failed, 404)
- https://www.swiftlisted.ai/pricing
- https://www.secnd.ca/pricing
- https://www.secnd.ca/
- https://vendorsnap.app/
- https://vendorsnap.app/crosslisting
- https://vendorsnap.app/features
- https://vendorsnap.app/download
- https://vendorsnap.app/pricing (failed, 404)
- https://ezlistiapp.com/
- https://www.herostuff.com/pricing
- https://www.herostuff.com/
- https://useflippr.com/
- https://www.useflippr.com/pricing (failed, 404)
- https://www.reclaimstuff.com/pricing (failed, 404)
- https://www.sixbitsoftware.com/pricing/
- https://www.sixbitsoftware.com/
- https://www.auctiva.com/
- https://www.auctiva.com/pricing (failed, 404)
- https://www.exportyourstore.com/pricing
- https://www.exportyourstore.com/integrations
- https://www.exportyourstore.com/
- https://www.trunkinventory.com/
- https://www.trunkinventory.com/pricing (failed, 405)
- https://sellbery.com/pricing/
- https://www.koongo.com/pricing/
- https://www.koongo.com/channels/
- https://closetpilot.com/pricing/
- https://www.listingmirror.com/pricing/ (redirected to /pricing-management/, no prices; U)
- https://crazylister.com/
- https://crazylister.com/pricing
- https://www.frooition.com/pricing (failed, 404)
- https://resellkit.com/pricing (failed, empty)
- https://www.resellkit.com/ (failed, TLS)
- https://sparedollar.com/ (failed, empty)
- https://www.producthunt.com/products/vendorsnap (failed, 403)
- https://www.producthunt.com/products/swiftlisted (failed, 403)
- https://reeva.co/ (failed, 402)
- https://www.reeva.com/ (failed, 502)
- https://getreeva.com/ (failed, empty)
- https://reeva.app/ (loaded; Saudi salon WhatsApp bot, not a reseller tool)
- https://flyp.com/ (failed, wall)
- https://resaleos.com/ (failed, 502)
- https://simplylisted.com/ (failed, TLS)
- https://www.inkfrog.com/ (redirects to https://www.wix.com/ecommerce/sell/multichannel)
- https://www.valueaddedresource.net/inkfrog-ebay-alternative-solutions/ (third party)
- https://www.sellbrite.com/

Scratchpad pages fetched earlier today by the lane 01 agent and reused as leads only: Crosslist blog "Best 10 Cross Listing Apps in 2026 for Resellers" (Sept 30, 2026), OneShop blog on crosslisting apps, Vendoo blog "how much is Crosslist", SellerAider crosslisting-app comparison, 3Dsellers pricing (its "3Dsellers vs Auctiva / InkFrog / CrazyLister" links).
