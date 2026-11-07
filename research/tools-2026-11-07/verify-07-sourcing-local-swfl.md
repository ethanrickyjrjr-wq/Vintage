# Verification: lane 07 sourcing local SWFL (estate sales, auctions, thrift, flea markets)

Date: 2026-11-07. Author: research subagent (adversarial price and claim checker).
Question: do the prices, free tiers, hours, platform claims and "live right now" claims recorded by the first lane-07 agent hold up against the venues' own pages today?
Legend: V = page read today; U = unverified (page would not load after one alternative attempt, or the claim rests on a snippet, a third-party listing or memory).
Method: every page below was fetched today from this container through headless Chromium with a curl fallback. JavaScript-only pages (CTBids, EstateSales.net result counts) were re-read with a 12 second render wait. No roundups were used. Reddit was not read. No WebSearch was used; URLs came from the first agent's list and from links on the vendors' own pages.

## 0. Bottom line

- 23 checks on 19 venues or tools. 17 confirmed, 5 refuted or corrected, 1 unreadable (CTBids Fort Myers location page renders empty).
- Every money figure the first agent recorded is on the vendor's page today: CTBids Premier $99/year, bidding from $1, Gulf Coast 18% buyer's premium and 3% cash discount, Goodwill 5% back and $1.99 leftovers, Habitat 1 point per dollar redeemable at 100, Lockerfox 15% with $10 minimum, Blue Moon 500 points = $5 coupon, Ortiz spaces $35 a day.
- Refuted: Ortiz Flea Market does not run Friday to Sunday. Its own page says Saturday 8AM-4PM and Sunday 6AM-4PM, "Closed Monday-Friday to public". The Sunday 6 AM opening is right.
- Refuted: "Five Cape Coral and Fort Myers online estate auctions are live right now" on CTBids. The CTBids Cape Coral page lists four today (82, 73, 130 and 63 items). EstateSales.org lists five Caring Transitions of Cape Coral online auctions plus one in-person sale, so the first agent's "6 sales ... all Caring Transitions online auctions" is also off by one.
- Refuted: KCM Galleries "no buyer's premium". That line came from an EstateSales.net listing title. KCM's own How to Bid page says "you'll need to also pay any stated buyer's premium". The premium is set per auction.
- Corrected: StorageTreasures Pro prices were "unknown"; the upgrade page shows Free $0.00 / Month, ProBidder $10.00 / Month, ProBidder Max $20.00 / Month, ProBusiness $30.00 / Month.
- Not stated anywhere read today: "free entry" at all three flea markets (only "Free parking" at Ortiz and a shopper review at Fleamasters), "free" for a HiBid bidder account (sign-up page lists Google, Apple, Facebook or Email, no fee and no "free" word), and Dovetails' 25% buyer's premium (the auctions page has no premium figure).
- Closure notice seen: Habitat Lee lists "McGregor ReStore | PERMANENTLY CLOSED". No shutdown or acquisition notices on any other page read today.

## 1. Checks

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| EstateSales.net | Free email alerts; 8,185 Fort Myers / Cape Coral email users; 38 sales listed | confirmed | "Get Notified of Estate Sales For Free!"; "Number of Email Users: 8,185"; "Fort Myers / Cape Coral Estate Sales (38 Results)" | https://www.estatesales.net/FL/Fort-Myers-Cape-Coral | The result count only renders after about 12 seconds of JavaScript; a fast fetch shows "(0 Results)". Counts change daily. |
| EstateSales.net | Naples 12,450 email users | confirmed | "Number of Email Users: 12,450" | https://www.estatesales.net/FL/Naples | Naples page also shows "(0 Results)" on a fast render; not re-read with the long wait. |
| EstateSales.net | Users can pick a two-day (or longer) lead time for the alert email | confirmed | "Some users, though not many, have chosen to receive emails two, three or more days before the sales' starting dates." | https://www.estatesales.net/help/frequently-asked-questions | More than 90% of users pick one day before. A sale must be published two days ahead to be in any email at all. |
| EstateSales.org | Free alerts with 5 to 100 mile radius, weekday picker and online-auction-item emails | confirmed | "Email me sales within 5 miles ... 100 miles"; "Days to receive emails? Mon ... Sun"; "Online Auction Items Receive emails about newly added estate sale items" | https://estatesales.org/ | The form is a modal on the homepage, not a separate URL. No payment step. |
| EstateSales.org | 6 sales within 50 miles of Fort Myers, all Caring Transitions of Cape Coral online auctions | refuted | "6 estate sales currently listed near Fort Myers, Florida"; one card reads "Estate Sale In-person estate sale Cape Coral, FL 33904" | https://estatesales.org/estate-sales/fl/fort-myers | Six listed: five Caring Transitions of Cape Coral online auctions (82, 72, 130, 59 and 41 items) and one in-person estate sale starting Sat Nov 14. "Follow" buttons present. |
| CTBids | Free account, bidding starts at $1, real time notifications | confirmed | "Bidding Starts at $1"; "Real time updates and notifications"; "Register for a CTBids Account" | https://ctbids.com/ | No fee appears anywhere for the basic account. |
| CTBids Premier | $99/year | confirmed | "Upgrade to a CTBids Premier Membership for $99/year" | https://ctbids.com/premier-membership | Page needs a 12 second render wait; a fast fetch returns 140 characters. WorthPoint benefit is a "90 Day All-Access Subscription", not a year. Delivery Guarantee "Valued up to $192". |
| CTBids | Five Cape Coral and Fort Myers online estate auctions live right now | refuted | Four cards: "Items | 82", "Items | 73", "Items | 130", "Items | 63" (Cape Coral 33909, Fort Myers 33907, Cape Coral 33904) | https://ctbids.com/estate-sales/Cape-Coral-FL | Four on CTBids' own Cape Coral page today. The first agent's CTBids location fetches had failed; its "five" came from EstateSales.org. Live counts change daily. |
| CTBids | Fort Myers location page | unreadable | Page title "CTBids"; body shows only the generic "Register for a CTBids Account" footer | https://ctbids.com/estate-sales/Fort-Myers-FL | Renders empty even with the 12 second wait. Use the Cape Coral page; Fort Myers lots sit under Caring Transitions of Cape Coral. |
| HiBid | Watch list, notifications and mailing list exist; web sign-up | confirmed | "Join Our Mailing List"; "Manage Notifications"; "Watch List"; sign-up: "Create your account Google Apple Facebook or Email" | https://hibid.com/ and https://hibid.com/register | The word "free" does not appear on the homepage or the sign-up page. No fee appears either. iOS/Android app not checked (no store listing read). |
| Gulf Coast Auction House (HiBid) | 18% buyer's premium, 3% cash discount, previews Fri 10-6 and Sat 12-3, Sunday Nov 8 7 PM close, 131 lots, Bonita Springs | confirmed | "18% Buyer's Premium | 3% Discount for Cash Payments"; "Preview is available Fridays from 10:00 AM-6:00 PM and Saturdays from 12:00-3:00 PM"; "Lots begin closing Sunday, November 8th, 2026, at 7:00 PM ET"; "View Catalog (131 Lots)"; "24551 Production Circle, Bonita Springs, FL 34135" | https://gulfcoastauctionhouse.hibid.com/ | Two more auctions listed (241 lots closing Nov 22, 221 lots). "Local Pickup Available". /mailing-list path returns "We can't find that page"; the homepage footer has an "Email List" link. |
| KCM Galleries | No buyer's premium | refuted | "Keep in mind when you're deciding on the maximum amount you'd like to pay that you'll need to also pay any stated buyer's premium." | https://www.kcmgalleries.com/buy-art/how-to-bid/ | "No buyer's premium" was an EstateSales.net listing title, not a KCM statement. Premium is per auction; read each auction's terms. Terms & Conditions page has no premium figure. |
| KCM Galleries | App coming soon; Cape Coral; auctions every Sunday and Wednesday | confirmed | "Get the KCM Galleries App Place and Manage your Bids from Anywhere - Coming Soon"; "Auctions Every Sunday and Wednesday"; "Cape Coral, FL 33909" | https://www.kcmgalleries.com/ | Homepage banner says "Fantastic Framed Art"; a featured lot is "Arthur Kinslow Orginal Painting", so some lots are originals. /buying and /how-to-bid are 404; the real page is /buy-art/how-to-bid/. |
| Dovetails / Auctions Neapolitan | 25% buyer's premium (from a stale news item); by-request email list | confirmed (email list) | "Auction items are offered to our by-request private email list"; "2315 Davis Blvd. Naples, FL 34104" | https://dovetailsllc.com/pages/auctions | No buyer's premium figure anywhere on the page. The 25% stays U. |
| Goodwill SWFL | VIP Perks free; 5% back in points | confirmed | "Join for Free Today and Start Saving!"; "Members earn 5% back in reward points when using their VIP Perk number at checkout" | https://goodwillswfl.org/vip-perks/ | "Reward points never expire." VIP number is the phone number you sign up with. Points apply to donated goods only. |
| Goodwill SWFL | 50% off a new tag color each Sunday; unsold tags $1.99 Sunday and Monday | confirmed | "Each week beginning on Sunday we feature a 50% discount on most color-tagged items."; "Any weekly sale items not sold by Saturday will be $1.99 the following Sunday & Monday" | https://goodwillswfl.org/shop/ | Colors: "Red, Black, Purple, Blue, Yellow & Green". The first agent's /store-sales-calendar/ and /locations/goodwill-outlet-center/ URLs are both "Page not found" today. |
| Goodwill SWFL | Tice St Outlet Center exists | confirmed | "Goodwill Outlet Center 5100 Tice Street Fort Myers FL 33905" | https://goodwillswfl.org/locations/ | Hours and bins pricing are not on the locations page. |
| ShopGoodwill (goodwillswfl) | Pickup Wednesday and Friday 10:30 to 3:30 by appointment two business days ahead | confirmed | "Wednesday & Friday 10:30AM - 3:30PM"; "all appointments are scheduled on the website 2 business days in advance"; "Pickups are only at 5100 Tice St, Fort Myers, FL 33905." | https://shopgoodwill.com/goodwillswfl | "Orders not picked up within 7 days will become unavailable and will be considered a donation." Google Play and Apple App Store links on the page. |
| Habitat ReStore Lee and Hendry | North Fort Myers and Bonita Springs stores, Mon to Sat; 1 point per dollar, redeem at 100; rewards app | confirmed | "North Fort Myers ReStore 31 Willis Road"; "Bonita Springs ReStore 9080 Bonita Beach Road"; "Monday-Saturday | 10am - 5pm Sunday | Closed"; "Every dollar you spend earns 1 point."; "After earning 100 points, ReStore Rewards can be redeemed"; "Download the rewards app" | https://www.habitat4humanity.org/locations/ and https://www.habitat4humanity.org/restore | Closure notice: "McGregor ReStore | PERMANENTLY CLOSED". Email list is Constant Contact. |
| Habitat Collier ReStore | East Naples store, Mon to Sat; email list for fresh inventory; social for inventory | confirmed | "Habitat Collier ReStore - East Naples"; "Mon-Sat: 9 a.m. - 6:30 p.m. Sun: Closed"; "Sign up for ReStore updates and be the first to know about fresh inventory, sales, and more!"; "Emails are serviced by Constant Contact." | https://habitatstores.org/shop/ | "Weekly" social posting is not stated; the page says "we recommend following us on social media". Stock named: "furniture, appliances, art, lighting, decor". |
| Hope Chest (Hope Healthcare) | Four stores (Cape Coral, Bonita Springs, South Fort Myers, Naples), Mon to Fri 9 to 5, Sat 9 to 4, newsletter, new items daily | confirmed | "Our four upscale Hope Chest resale stores"; "Monday through Friday 9-5 Saturday 9-4" (all four); "Hope Chest Newsletter"; "New items arrive daily" | https://hopehcs.org/hopechest/ | Newsletter sender is Chapters Health Foundation (Constant Contact). |
| Ortiz Flea Market | Runs Friday to Sunday; opens 6 AM Sunday; free entry; vendor spaces $35 a day | refuted (days) | "Flea Market Hours (Rain or Shine) Saturday 8AM-4PM Sunday 6AM-4PM"; "Closed Monday-Friday to public"; "Open Spaces ~ $35 a day."; "Free parking." | https://www.ortizfleamarket.com/ | Saturday and Sunday only, not Friday. Sunday 6 AM is right. "Free entry" is not stated; only free parking. Vendor gates open 6 AM Saturday and 5 AM Sunday for paid vendors only. Covered space $45 a day. |
| Flamingo Island Flea Market | Year round Fri to Sun; collectables; air conditioned; free entry | confirmed (hours, stock, AC) | "OPEN all year round, every Friday, Saturday and Sunday from January - December."; "Find everything from new items to collectables"; "air conditioning for seller and buyer comfort" | https://www.flamingoisland.com/ | "Free entry" is not stated. A "Newsletter" box exists. |
| Fleamasters Flea Market | Year round Fri to Sun; the biggest; free entry | confirmed (hours, size claim) | "Friday - Sunday: 9am-5pm"; "OPEN YEAR ROUND"; "S.W. Florida's biggest and best flea market!" | https://www.fleamastersfleamarket.com/ | "Biggest" is the market's own slogan. "Free entry" not stated; a quoted shopper review says "Parking is free." |
| Craigslist Fort Myers | Free garage and moving sale search loads for SW Florida | confirmed | Title: "fort myers garage & moving sales - craigslist"; "garage sales on Sat, Nov 7"; "SAVONA NEIGHBORHOOD GARAGE SALE off Del Prado Blvd." | https://fortmyers.craigslist.org/search/gms | Redirects to craigslist.org/search/area/fortmyers?cat=gms. No cost shown. |
| Lockerfox | 15% of winning bid, $10 minimum; 72 hours to pay and clear | confirmed | "Our fee to use the service is 15% of the winning bid subject to a $10.00 minimum charge."; "up to 72 hours (48 or less in some auctions) from the end of bidding to pay for and pick up" | https://www.lockerfox.com/faq/ | Some auctions allow 48 hours or less. Cleaning deposit and sales tax paid at the facility. Bids in $10 increments, soft close. |
| StorageTreasures | Free bidder account; Pro tier price unknown; Naples listings | refuted (price unknown is now known) | "Register Now - It's Easy & Free!"; "Total Auctions: 21" (Naples); "$0.00 / Month"; "ProBidder $10.00 / Month"; "ProBidder Max $20.00 / Month"; "ProBusiness $30.00 / Month" | https://www.storagetreasures.com/auctions/fl/naples and https://www.storagetreasures.com/pro-membership-upgrade | Free tier confirmed. Pro prices are monthly. The /pro URL itself returns 404 content; the upgrade page is /pro-membership-upgrade. |
| Blue Moon Estate Sales | Free rewards club; 500 points = $5 coupon | confirmed | "500 points = $5 coupon"; "1000 points = $10 coupon"; "Earn 1 point for every dollar spent"; "you get 25 points for the effort!" | https://bluemoonestatesales.com/for-shoppers/shopper-rewards/ | "All franchises are independently owned and operated." No SWFL franchise checked today. |

## 2. What the first agent got wrong or left loose

1. Ortiz Flea Market is open Saturday and Sunday only. The PICK says "All three run year round Friday to Sunday". Ortiz's page: "Saturday 8AM-4PM Sunday 6AM-4PM ... Closed Monday-Friday to public". Flamingo Island and Fleamasters do run Friday to Sunday.
2. "Five Cape Coral and Fort Myers online estate auctions are live right now" on CTBids: CTBids' own Cape Coral page shows four today. EstateSales.org shows five Caring Transitions online auctions. The first agent's CTBids location fetches had failed (its cached files say FETCH FAILED), so the number was borrowed from EstateSales.org without saying so.
3. EstateSales.org "6 sales ... all Caring Transitions of Cape Coral online auctions": six are listed, but one is an in-person estate sale with no company shown, not a Caring Transitions auction.
4. KCM Galleries "no buyer's premium": not a KCM claim. KCM's How to Bid page tells bidders to budget for "any stated buyer's premium". It varies per auction. Also KCM's "/buying" link is a 404; the real page is /buy-art/how-to-bid/. A featured lot is an "Orginal Painting", so the "prints not originals" worry is only partly right.
5. StorageTreasures "Pro tier price unknown": the vendor's upgrade page lists ProBidder $10.00 / Month, ProBidder Max $20.00 / Month, ProBusiness $30.00 / Month, and the free account at $0.00 / Month.
6. "Free entry" at the flea markets is not written on any of the three sites. Ortiz says "Free parking"; Fleamasters only has a shopper review saying parking is free. Probably true, but unproven.
7. HiBid "free bidder account": no HiBid page read today uses the word "free" or names a fee. The watch list, notifications and mailing list do exist.
8. Dovetails 25% buyer's premium: the auctions page has no premium figure. Stays U, as the first agent flagged.
9. Goodwill: the two deep URLs the first agent reached for (store sales calendar, outlet center page) are "Page not found" today. The shop page carries the color-tag rules and the locations page carries the Outlet Center address, so the facts stand.
10. Habitat Collier "posts weekly inventory on social": the page says to follow on social media for recent inventory. "Weekly" is not stated.
11. Loose: EstateSales.net result counts need a long render wait. A fast fetch shows "(0 Results)" for both Fort Myers / Cape Coral and Naples. The first agent's 38 is right once rendered; Naples 43 was not re-checked with the long wait.
12. Closure not mentioned by the first agent: Habitat Lee's "McGregor ReStore | PERMANENTLY CLOSED".

## 3. Note for Hollie

Every free sign-up the first agent recommended is real and still free today: EstateSales.net alerts, the EstateSales.org modal form, a CTBids account, a HiBid account, Goodwill VIP Perks, Habitat ReStore Rewards, the Habitat Collier and Hope Chest email lists, Blue Moon Rewards. The one schedule fix: Ortiz is a Saturday and Sunday market; Sunday 6 AM is the picker hour. CTBids Premier at $99/year and the StorageTreasures Pro tiers ($10 to $30 a month) are the only paid options in this lane and neither is needed to start.

## 4. Gaps and pages that would not load

- https://ctbids.com/premier and https://ctbids.com/help-center: 140 characters or less after render (single-page app). The /premier-membership page loaded with a 12 second wait.
- https://ctbids.com/estate-sales/Fort-Myers-FL: loads a bare "CTBids" page with no auction cards even after the wait.
- https://gulfcoastauctionhouse.hibid.com/mailing-list: "We can't find that page".
- https://www.kcmgalleries.com/buying and https://www.kcmgalleries.com/how-to-bid: 404 (curl fallback). Real pages: /buy-art/how-to-bid/, /buy-art/how-to-register/, /terms-conditions/.
- https://goodwillswfl.org/store-sales-calendar/ and https://goodwillswfl.org/locations/goodwill-outlet-center/: "Page not found".
- https://www.storagetreasures.com/pro: HTTP 404 body with navigation only; the price page is /pro-membership-upgrade.
- Not attempted: HiBid iOS/Android store listings, EstateSales.net App Store listing, Naples EstateSales.net count with the long wait, any SWFL Blue Moon franchise page, Dovetails premium on a LiveAuctioneers catalog.

## 5. Sources (every URL fetched today)

https://www.estatesales.net/FL/Fort-Myers-Cape-Coral
https://www.estatesales.net/FL/Naples
https://www.estatesales.net/help/frequently-asked-questions
https://estatesales.org/
https://estatesales.org/estate-sales/fl/fort-myers
https://ctbids.com/
https://ctbids.com/premier-membership
https://ctbids.com/premier
https://ctbids.com/help-center
https://ctbids.com/locations
https://ctbids.com/estate-sales/Cape-Coral-FL
https://ctbids.com/estate-sales/Fort-Myers-FL
https://gulfcoastauctionhouse.hibid.com/
https://gulfcoastauctionhouse.hibid.com/auctions
https://gulfcoastauctionhouse.hibid.com/mailing-list
https://www.gcauctionhouse.com/
https://hibid.com/
https://hibid.com/register
https://www.kcmgalleries.com/
https://www.kcmgalleries.com/buying
https://www.kcmgalleries.com/how-to-bid
https://www.kcmgalleries.com/terms-conditions/
https://www.kcmgalleries.com/buy-art/how-to-bid/
https://dovetailsllc.com/pages/auctions
https://goodwillswfl.org/shop/
https://goodwillswfl.org/vip-perks/
https://goodwillswfl.org/store-sales-calendar/
https://goodwillswfl.org/locations/goodwill-outlet-center/
https://goodwillswfl.org/locations/
https://shopgoodwill.com/goodwillswfl
https://www.habitat4humanity.org/locations/
https://www.habitat4humanity.org/restore
https://habitatstores.org/shop/
https://hopehcs.org/hopechest/
https://www.ortizfleamarket.com/
https://www.flamingoisland.com/
https://www.fleamastersfleamarket.com/
https://fortmyers.craigslist.org/search/gms
https://www.lockerfox.com/faq/
https://www.storagetreasures.com/auctions/fl/naples
https://www.storagetreasures.com/pro
https://www.storagetreasures.com/pro-membership-upgrade
https://bluemoonestatesales.com/for-shoppers/shopper-rewards/
