<!-- Saved verbatim by the parent Opus session from agent d6's final message, 2026-10-29 (the harness refuses subagent report writes). -->

# d6: being local in Southwest Florida

Agent d6, accessed 2026-10-29. Raw captures: `research/round-d/raw/d6-*` (73 files). Save this report verbatim as `research/round-d/d6-local-swfl.md`.
Method: SearXNG (`tools/search.sh`) for URLs, crawl4ai (`tools/crawl.sh`) for pages, about 60 pages fetched and about 48 usable. WebSearch was used 8 times for discovery only. Anything that rests only on a WebSearch summary is tagged `unverified`. The Florida DOR rate PDF came back 4 bytes from crawl4ai, so I read it through a WebFetch binary download plus pypdf text extraction (`d6-fl-dor-dr15dss26.txt`). The Lee County 2025 visitor report was read the same way (`d6-leevcb-2025-visitor-tracking.txt`, PDF deleted after extraction).
Tags: `verified` = read live this session. `inferred` = my reading. `unverified` = not read on a primary page.

Walls and dead pages (not retried, no Patchright): Gulfshore Life 2026 media kit (0 bytes), Naples Daily News "5Q For Business" form (0 bytes), Cape Coral Farmers Market application PDF (4 bytes), Nextdoor US FAQ (404), Nextdoor help article "How to claim your business page" (1.4 KB, no usable text), VMD `/faq/` (404), estatesales.net Fort Myers company directory (1 KB). Not read at all: the Pine Ridge vendor application PDF, the VMD vendor-profile steps past the first screen, the Gulfshore Life event calendar.

## TL;DR

1. **Google will only list Holliewood & Vine as a service-area business if Hollie really goes to customers.** Google: "If your business either has a physical location that customers can visit, or travels to customers where they are, you can create a Business Profile." A shop that only ships is not covered by those words. Fabulous From Online counts only if in-person visits or local delivery are offered, which the design doc says they are (payment online before any visit). `verified` (rule), `inferred` (fit).
2. **Whether Fabulous From Online can be a listed "service" is an account question.** The services editor is only for "Businesses in certain categories, like service businesses." Which categories get it cannot be checked without logging in. Services can carry "descriptions and prices." `verified`; category availability `unverified`.
3. **The one truly right event is Vintage Market Days "Fresh Finds and Sunshine," Jan 29-31, 2027, Lee Civic Center, Fort Myers.** The date is `verified`. The booth fee is **not published** (it sits behind a free vendor profile), so it is `unverified`. The $100-$225 figures a search returned belong to other VMD cities and are not used here.
4. **Verified fees are small and come with eligibility catches.** River District (Fort Myers) lists an Artist and Business Booth at $75 (+$10 without a city occupational license) and Art Walk at $50, but Art Walk says "Artist Vendors." Pine Ridge Road Farmers Market (Naples) is $40 per market day with a $160 non-refundable 4-week minimum and a tent required. Fine glass and lamps in an outdoor tent are a poor fit. `verified`.
5. **Surtax for local delivery: Lee 0.5% (6.5% total), Collier none (6% total).** Three sources agree. Surtax follows the delivery county, the $5,000 cap applies to goods, and Charlotte County's 1% is scheduled to expire Dec 31, 2026. The 2027 rate form is due in November. `verified`.
6. **Peak season is January to March by money, October to December by headcount.** Lee County 2025: Oct-Dec had the most visitors (913,200). Jan-Mar had the most visitor-days (6.19m), direct spending ($1.12b, 33.9% of the year), occupancy (73.2%) and room rate ($235.77). Collier was not fetched. The "November through April" Naples season comes from a real-estate blog. `verified` (Lee), `unverified` (Collier, Nov-Apr).
7. **Local press is reachable but not pitch-documented.** Gulfshore Life has Home + Design and Style > Shopping sections plus "Naples by Design" (Apr 7-8, 2027). The Naples Daily News takes press releases at one email. I could not verify any News-Press pitch route. `verified` / gaps flagged.
8. **The local design partner is IDS Southwest Florida, not ASID.** IDS says it is "located primarily in the Naples/Ft. Myers area." The ASID Florida West Coast chapter lists a Sarasota address and no Naples or Fort Myers mention. `verified`.

## 1. Google Business Profile (service-area business)

- URLs: https://support.google.com/business/answer/3038177 (guidelines, raw `d6-gbp-guidelines.md`), https://support.google.com/business/answer/9157481 (service areas, `d6-gbp-service-area.md`), https://support.google.com/business/answer/2853879 (address, `d6-gbp-address.md`), https://support.google.com/business/answer/9455399 (services, `d6-gbp-manage-services.md`). Accessed 2026-10-29.
- Eligibility, verbatim: "If your business either has a physical location that customers can visit, or travels to customers where they are, you can create a Business Profile on Google." `verified`
- Service-area business (SAB) definition: "A business that visits or delivers to customers directly but doesn't serve customers at their business address." `verified`
- Hide the address: "If you're a service-area business, you should hide your business address from customers." and "if you're a plumber and run your business from your residential address, clear the address from your Business Profile." Also: "The address on your Business Profile is public. If you don't serve customers at your business address ... you can choose to not show your address and list your service area instead." `verified`
- No storefront signage: "If your business doesn't have permanent on-site signage, it's not eligible as a storefront and should be listed as a service-area business." `verified`
- Service areas: "You can set up to 20 service areas based on the cities, postal codes, or other areas you serve." "You can't set your service area as a radius distance." "The boundaries of your overall area shouldn't be more than about 2 hours of driving time from where your business is based." Edits "may take up to 48 hours." `verified`. Lee plus Collier fits inside two hours of driving (`inferred`; I did not measure).
- Virtual offices and mailboxes are out: "P.O. boxes or mailboxes located at remote locations aren't acceptable." A rented address where you don't operate "isn't eligible." `verified`. So a mailbox store address cannot stand in for Hollie's address.
- Hours: businesses that "operate only by appointment" "shouldn't provide hours." `verified`. This fits Hollie.
- Name rule: "Represent your business as it's consistently represented and recognized in the real world across signage, stationery, and other branding." Name "should reflect your business's real-world name, as used consistently on your storefront, website, stationery, and as known to customers." `verified`. **Hollie must pick one spelling ("Holliewood and Vine" or "Holliewood & Vine") and use it on Google, Nextdoor, Etsy and the site.**
- Description limits: no "special promotions, prices, and offer sales" and "No links of any type are allowed." Categories: "Use as few categories as possible"; pick what "This business IS a," not "HAS a." `verified`
- Services editor: "Businesses in certain categories, like service businesses, might have the option to showcase their offerings directly on their Business Profile." "You can also create and add custom services options." "you can group services into categories and include additional details, like descriptions and prices." `verified`
- **X verified, Y need review:** the Google page says services can carry "descriptions and prices" (verified). A WebSearch summary of a different help-page version said custom services "can't include phone numbers, URLs, or prices." That is `unverified` and conflicts. Test on the real account.
- What I could not check without an account: which primary category unlocks "Edit services," and what verification method Google demands for a hidden-address profile. Both are `unverified`.
- **Can it list "Fabulous From Online"?** Only if (a) the business qualifies as an SAB through real in-person visits or local delivery, and (b) the chosen primary category shows the services editor. A video-only, photo-only, email-only service would not qualify on its own. `inferred`. Category wording ("interior designer," "stager") touches the ch. 481 title rules: see `research/fabulous-from-online/c5-florida-legal.md` wording table.
- **Steal this:** (1) one SAB profile, address hidden, up to 20 city/ZIP areas across Lee and Collier; (2) services list with plain names and prices ("Screen Test," "Corner," "Room," "Home") once the category allows it; (3) no hours, appointment only; (4) description without links or promos.

## 2. Nextdoor business pages

- URLs: https://business.nextdoor.com/en-us/blog/guide-to-claiming-your-nextdoor-business-page (`d6-nextdoor-claim-guide.md`), https://business.nextdoor.com/en-us/getting-started/business-page (`d6-nextdoor-business-page.md`), https://business.nextdoor.com/local (`d6-nextdoor-local.md`). Accessed 2026-10-29. The claim guide is dated "Oct 7, 2019" and says "This article was updated on July 26, 2023." Treat it as read live but dated.
- Free page: "Claim your free Business Page now!" and "Reach local customers with unlimited free posts: updates, expert advice, and more!" `verified` (current page).
- Hidden address: "If you'd like to display your address on your public page, check the box 'Show above address in contact information.' Conversely, if you'd prefer to keep your address hidden (if you work out of your home, for example), keep this box unchecked." `verified` (2023-updated blog).
- Reach: "With a free post, you'll instantly reach all neighbors within two miles of your business and can post twice per month. Note: You must be verified to use Business Posts." "With a paid ad, you can target neighbors up to 30 miles from your business." Up to 10 categories. `verified` (2023-updated blog).
- Fit: "Business Pages on Nextdoor are ideal for businesses that are truly local." `verified`. Nextdoor's own marketing claims "1 in 3 US households are on Nextdoor" and "76% of neighbors have been influenced by a recommendation." `verified` as vendor claims, not independently checked.
- **X verified, Y need review:** the free page and hidden-address option are verified. The post cap conflicts: "unlimited free posts" (current page) vs "twice per month" (2023-updated blog). The 2-mile radius is measured from "your business." With a hidden address I could not confirm what point Nextdoor uses. Ask on the account.
- **Steal this:** (1) claim the page, keep address unchecked; (2) ask first buyers for a recommendation ("Faves"); (3) use the Story section to say what Fabulous From Online is, since categories are generic; (4) a two-mile free radius is a neighborhood tool (HOA, condo building, one street), not a county tool.

## 3. Local markets, pop-ups and booths

### 3a. Vintage Market Days South Gulf Coast Florida (Fort Myers)
- URLs: https://vintagemarketdays.com/market/south-gulf-coast-florida/index.php (`d6-vmd-sgc-home.md`), `/vendor.php` (`d6-vmd-sgc-vendor.md`), `/create-profile.php` (`d6-vmd-sgc-create-profile.md`), `/tickets.php` (`d6-vmd-sgc-tickets.md`), `/contact.php` (`d6-vmd-sgc-contact.md`). Accessed 2026-10-29.
- Dates: "January 29 - 31, 2027 / Lee Civic Center / 11831 Bayshore Rd. / Fort Myers, FL 33917." Fri Jan 29 "Early Buying Event 10:00 am to 4:00 pm"; Sat 10-4; Sun 10-3. Ticket page title: "Vintage Market Days presents 'Fresh Finds and Sunshine'." 3-day early-buy ticket "$7.50 + Sales tax + $1.20 fee." `verified`
- What it is: "an upscale, vintage and vintage-inspired indoor/outdoor market featuring original art, antiques, clothing, jewelry, handmade treasures, home décor." `verified`
- Rules: "a juried event accepting vendors based on variety, originality, and quality of goods sold." "Vendor applications will not be considered if photos or links to on-line photos are not included." "Booth availability is on a first come, first serve basis." "create your FREE vendor profile." `verified`
- Category fit: "Vintage Home and Goods: 90% of items presented are antique, vintage, retro, re-purposed, and/or up-cycled. (Market, new, wholesale or vintage inspired items for the home only must be limited to 10% or less of entire exhibit)." Clothing and Accessories: "100% of goods ... on-trend, vintage inspired, vintage, retro, re-purposed, up-cycled, and/or hand crafted." `verified`. Hollie's one-of-one stock fits.
- **Booth fee: not published** on any page I could read. `unverified`. Ask: sgulfcoastfl@vintagemarketdays.com (published on the contact page).
- A search-result snippet title reads "1/23-25 Lee Civic Center #swfl" from the VMD Instagram, suggesting a late-January slot last year. `unverified` (snippet only).
- **Steal this:** (1) apply with merchandised room photos, since the jury wants proof of "ability to merchandise"; (2) pick the Vintage Home and Goods category and keep any new stock under 10%; (3) apply early because spaces are first come.

### 3b. River District Alliance, Fort Myers
- URLs: https://www.myriverdistrict.com/vendor-application/ (`d6-riverdistrict-vendor.md`), https://www.myriverdistrict.com/art-walk-applicaton/ (`d6-riverdistrict-artwalk.md`), https://www.myriverdistrict.com/events/ (`d6-riverdistrict-events.md`). Accessed 2026-10-29.
- Fees: "Artist and Business Booth $75." Without a city occupational license: "No (a $10 fee will be added to application price)." Events on the form: July 4th Freedom Fest, New Year's Downtown Countdown, St. Patrick's Day. "Events will run rain or shine – no refunds." "We do not provide electricity." "Vendor is responsible for the collection and payment of Florida Sales Tax – 6.5%." Vendors handle "the security, protection and insurance of their own equipment and merchandise." `verified`
- Art Walk: "The RDA welcomes Artist Vendors," "The cost of participation is $50 for a 10×10 space," "Applications must be received at least 5 days prior to the event," "We reserve the right to assign spaces, primarily to ensure that an artist is not located near a store or vendor with similar items." Contact on page: events@rdafortmyers.com. `verified`
- Dates on the events page: November Art Walk Nov 6, 2026; December Art Walk Dec 4, 2026; Downtown NYE Celebration Dec 31, 2026 - Jan 1, 2027. `verified`. Computed Art Walk deadlines: about Nov 1 (for Nov 6) and about Nov 29 (for Dec 4). St. Patrick's Day date: not verified.
- **X verified, Y need review:** both fee quotes ($75 Artist and Business Booth; $50 Art Walk) are verified. Which one applies to a vintage resale booth, and whether a reseller counts as an "artist," need review. `inferred`: Art Walk is for makers. Ask events@rdafortmyers.com before paying.
- **Steal this:** the cheapest verified door into downtown Fort Myers foot traffic, and it states Lee's 6.5% tax out loud.

### 3c. Pine Ridge Road Farmers Market (Naples Marketplace)
- URLs: https://www.naplesmarketplace.net/vendors/ (`d6-naples-marketplace-vendors.md`), `/vendors/rules-and-regulations/` (`d6-naples-marketplace-rules.md`), `/vendors/application/` (`d6-naples-marketplace-app.md`). Accessed 2026-10-29.
- Fees: "PRICES FOR THE 2026-2027 SEASON: $40.00 for a single space / per market day"; "A 4-week minimum deposit ($160.00 for a single space) is required up front"; "All deposits are non-refundable"; "We offer monthly terms only"; "We are now accepting new vendors for the 2026-2027 season." `verified`
- Rules: "Market hours are from 9AM to 1PM. Rain or shine." "All vendors MUST have a tent and weights ... Minimum 20 lbs per leg." Max tent "10'x10'." "Items listed by vendor on page 1 of 3 of the Vendor Application form are the only items that the vendor will be permitted to sell." "Applicants must be approved first by the Market Manager." Manager text line published: 239-200-4401. Vendors get "all necessary licenses and permits to operate ... in Florida/Collier County." `verified`
- Market day: the rules say vendors "may elect to miss a Sunday," so Sunday is `inferred`. The pages never state the day plainly.
- Whether resale vintage is accepted: `unverified` (application PDF not read; jewelry vendors are closed out).
- Collier has 0% surtax, so booth sales here carry 6%. `inferred` from DOR (section 7).
- **Steal this:** a $160 test for smalls and brand awareness in Naples. It is a poor fit for lamps, glass and mirrors outdoors.

### 3d. Leads found, fees not published (all `unverified` for fees)
- Buckingham Farms, Fort Myers, "Market & Music" series by Golden Shellback Media: Sat Nov 28, Sat Dec 5 ("Christmas on the Farm," 10-3, "Vendor Setup: 8:00 AM"), Sat Jan 16, 2027. Eventbrite attendee pages show no vendor fee (`d6-eb-christmas-farm.md`, `d6-eb-support-small-biz-farm.md`). Verified dates only.
- Edison Mall Holiday Market, Fort Myers: "Sat, Dec 19, 11:00 AM + 1 more" (`d6-eb-edison-mall-holiday.md`). No vendor fee shown.
- Paradise Vintage Market, Fort Myers (an antique mall, not an event): "Open 7 days a week," 10AM-6PM. Booth rent: "Small-Room 1: $250 a month," "Large: $395," "Display Case: $160 a month," "Clothing Rack: $95 a month." Page copyright is 2024, so prices may be stale. **Its Feb 8/15/22 "outdoor market" dates are stale** (those Saturdays match 2025, not 2026), so I used the rent prices only. Contact 239-362-3811 (`d6-paradise-vendor.md`, `d6-paradise-events.md`). Rent prices `verified` as posted, currency `unverified`.
- Not a fit: Arts Bonita festivals (juried fine art; `d6-artsbonita-exhibitors.md` had no fee text). A WebSearch summary of third-party listings put Naples fine-art fairs at roughly $595-$830 per booth and the Naples Coastal Gallery Show at $70 per day for artists. All `unverified`, artist-only.

### 3e. The three events worth a booth
| # | Event | Date | Fee | Catch |
|---|---|---|---|---|
| 1 | Vintage Market Days "Fresh Finds and Sunshine," Lee Civic Center, Fort Myers | Jan 29-31, 2027 (`verified`) | **Not published** (`unverified`); ask sgulfcoastfl@vintagemarketdays.com | Juried, photos required, first come. Only true vintage fit. Inside the Jan-Mar peak. |
| 2 | River District Fort Myers: Art Walk, or the NYE vendor booth | Art Walk Nov 6 and Dec 4, 2026; NYE Dec 31 (`verified`) | $50 Art Walk 10x10 or $75 Artist and Business Booth, +$10 without city license (`verified`) | Art Walk says "Artist Vendors"; ask first. Apply by about Nov 1 and Nov 29. No power, no refunds. |
| 3 | Pine Ridge Road Farmers Market, Naples | 2026-2027 season, 9-1, apparently Sundays (`inferred`) | $40 per day, $160 non-refundable 4-week minimum (`verified`) | Outdoor tent, monthly terms, resale vintage unconfirmed. Use for smalls only. |

Honest read: only #1 is an actual vintage-shopper audience. #2 and #3 are cheap tests. Skip any event whose organizer will not confirm a resale vendor is eligible.

## 4. The snowbird calendar (October to April)

- Lee County 2025 Visitor Tracking Report (Lee VCB, https://www.visitfortmyers.com/sites/default/files/2026-03/2025%20Visitor%20Tracking%20Report.pdf; text in `d6-leevcb-2025-visitor-tracking.txt`). Quarterly comparison, verbatim table:
  - Visitors: Jan-Mar 782,000; Apr-Jun 862,700; Jul-Sep 762,800; **Oct-Dec 913,200**.
  - Visitor days: **Jan-Mar 6,193,400**; 4,926,000; 4,256,400; 5,716,600.
  - Direct expenditures: **Jan-Mar $1,121,810,900**; $754,888,900; $643,172,500; $791,304,300. Full year $3,311,176,600. Jan-Mar share is 33.9% (my computation).
  - Occupancy: **73.2%**; 52.4%; 45.3%; 54.4%. ADR: **$235.77**; $172.89; $139.90; $156.95.
  - `verified`. Do not write "most visitors in Q1": Oct-Dec has the most visitors, Jan-Mar the most spending and stay-days. This is Lee (Fort Myers and the beaches) only, covers all visitor types, not just seasonal residents, and Collier tourism data was not fetched (gap).
- Season length: a Naples real-estate blog (Dec 18, 2025) says "the season typically runs November through April, with the busiest stretch in January through March." `unverified` (marketing source, `d6-gcl-snowbird.md`). Its Jan-Mar claim agrees with the Lee table.
- Dated hooks in the season (all `verified` dates): VMD Jan 29-31; River District Art Walks (first Fridays: Nov 6, Dec 4) and NYE Dec 31; Gulfshore Life "Naples by Design" Apr 7-8, 2027; Edison Mall Holiday Market Dec 19; Buckingham Farms Nov 28, Dec 5, Jan 16.
- Naples Design District describes its audience as "locals, seasonal residents, and tourists." `verified` (`d6-naples-design-district.md`).

## 5. Estate sales and auctions as sourcing

- https://www.estatesales.net/FL/Naples (`d6-estatesales-naples.md`): "Naples Estate Sales (34 Results)," filters include Estate Sales, Online Estate Sales, Auctions, Buyouts Or Cleanouts. "Number of Email Users: 12,451" for the Naples area, which tells you how many other buyers get the same alerts. `verified`.
- Companies listed for Naples (`d6-estatesales-companies-naples.md`): Allegro Estate Sales & Services, King's Road Auctions, Estate Love of Southwest Florida, Bluestar Move Management & Estate Sales, Dovetails LLC / Auctions Neapolitan, Burchard Galleries, Gulf Coast Auctions & Estates, Sara's Estate Sales. Names only, no endorsement. The Fort Myers directory was walled.
- Freeman's Naples (https://freemansauction.com/locations/naples, `d6-freemans-naples.md`): "Established in 2010 as the firm's first regional office," in "Old Naples," categories include "Furniture and Decorative Arts, Modern Design." `verified`. It serves consignors, so it is both a sourcing watch-list and a referral partner for appraisals.
- Ch. 538: do not re-research. See `research/fabulous-from-online/c5-florida-legal.md` section 5. It lists exemptions for "Any person at antique, coin, or collectible shows or sales" and "an auction business," and marks whether the buyer on the other side is covered as `unverified`. This lane adds nothing to it.
- **Steal this:** build a short buy list per company (lamps, glass, mirrors, chairs), and buy from compliant dealers or sources per c5. I did not verify any estate-sale company's dealer-preview policy.

## 6. Partners: designers, stagers, trade

- IDS Southwest Florida chapter (https://interiordesignsociety.org/chapters/southwestflorida, `d6-ids-swfl-chapter.md`): "located primarily in the Naples/Ft. Myers area of Florida"; the national body serves "the residential interior design industry"; the page links a "FIND A DESIGNER" directory (theidslist.com/homeowner). `verified`. Membership cost and non-designer membership rules: `unverified`.
- ASID Florida West Coast chapter (https://flwc.asid.org/, `d6-asid-flwc.md`): address "5330 Desoto Rd. Unit 2318 Sarasota, FL 34235"; no Naples or Fort Myers mention on the page. `verified` for the address; territory `unverified`.
- Naples Design District (https://naplesdesigndistrict.com/, `d6-naples-design-district.md`): "Shoppers can explore a mix of thrift, consignment and luxury finds ... From vintage gems to high-end fashion" and "High-end builders, interior designers and home design shops are the heartbeat of the neighborhood." A 501(c)6 organization with a newsletter. `verified`.
- Gulfshore Life "Chairs for Charity" (https://gulfshorelife.com/home-design/chairs-for-charity, `d6-gulfshorelife-chairs.md`): "2nd Annual ... one-of-a-kind chairs creatively reimagined by leading local design firms," hosted at Wilson Lighting. No date on the page. `verified`.
- Trade programs: no local vintage trade program was verified. The closest model is R&R Relics's 20% trade program and the Chairish/1stDibs sourcing perks in `research/fabulous-from-online/c2-vintage-sourcing.md`. Stager associations: not verified (a RESA find-a-stager page surfaced in search and was not read).
- **Steal this:** (1) offer IDS members a "first look" email, not a discount; (2) get on the Naples Design District newsletter; (3) pitch vintage chairs and lamps to the designers behind Chairs for Charity.

## 7. Local press

- Gulfshore Life (`d6-gulfshorelife-contact.md`, `-shopping.md`, `-naples-by-design.md`, `-submit-event.md`). Contact page: Gulfshore Life Media, LLC, 12641 Corporate Lakes Dr., Fort Myers, FL 33913, (239) 498-8500; Editor in Chief Stephanie Granada (stephanie.granada@gulfshorelife.com), Publisher Carin Keane. Sections: Home + Design (Home Tours, Design Inspiration, Naples by Design, Chairs for Charity), Style > Local Designers and Shopping. Shopping headlines include "Where to Shop in Naples" and "New Boutiques Bringing Fresh Style to Southwest Florida." "Naples by Design ... April 7-8, 2027 ... Presented by Gulfshore Life HOME," with a speaker described as an "Art & Collecting Expert ... antiques, provenance and collecting." There is a "Submit Your Event" form (category list includes "Shopping"). `verified`. No pitch guidelines, editorial calendar or lead times: the media kit was walled. `unverified`.
- Naples Daily News (https://static.naplesnews.com/participate/, `d6-naplesnews-participate.md`): "We are no longer able to accept news stories and news releases to post directly to our website. If you have a press release you would like to send to us, please email it to news@naplesnews.com. It will be reviewed by an editor for a news story." Forms exist for "5Q For Business" (form walled) and events. `verified`. No home section or pitch route found.
- News-Press (Fort Myers): the site has Contact Us, a staff directory and a Shopping tab (`d6-newspress-about.md`). Neither a home section nor a pitch route was verified. Gap. I make no claim about ownership of either paper.
- **Steal this:** a two-sentence pitch to Gulfshore Life Home + Design built on a real hook (a dated event, a sold-archive story, or a chair), plus free event-calendar submissions for anything public.

## 8. County sales surtax (Florida DOR)

- URLs: https://floridarevenue.com/taxes/taxesfees/Pages/discretionary.aspx (`d6-fl-dor-surtax.md`), https://floridarevenue.com/Forms_library/current/dr15dss_26.pdf (form DR-15DSS "for Calendar Year 2026," `R. 11/25`; text in `d6-fl-dor-dr15dss26.txt`), https://pointmatch.floridarevenue.com/General/DiscretionarySalesSurtaxRates.aspx (`d6-fl-dor-pointmatch.md`, shows 25 of 68 rows; Collier 0.00%, Lee not on the first page). Accessed 2026-10-29.
- Rule: "You must collect discretionary sales surtax when the transaction occurs in – or delivery is made into – a county that imposes a surtax, and the sale is subject to state sales and use tax." "...surtax is collected at the county rate where the delivery is made." `verified`
- Rates (DR-15DSS 2026): "Lee .5% Jan 1, 2019 Dec 31, 2028"; "Collier None"; "Charlotte 1% Apr 1, 1995 Dec 31, 2026." `verified`. Totals: Lee 6.5%, Collier 6%, Charlotte 7%. A tax-law blog (floridasalestax.com, Aug 2026, `d6-floridasalestax-blog.md`) shows Lee 6/0.5/**6.5%**, Collier 6/0/**6%**, Charlotte 6/1/**7%**. River District's own vendor rule says "Florida Sales Tax – 6.5%." Three sources agree: **3 verified.**
- Cap: "Discretionary sales surtax applies to the first $5,000 of the sales amount on the sale ... of any item of tangible personal property." "The $5,000 cap does not apply to ... sales of services." `verified`. Delivery charges are taxable as part of the item's cost: see TAA 02A-014 answer 10 quoted in c5 section 2b.
- Timing: the rate form is "updated yearly in November," so the 2027 form lands within weeks. Recheck Charlotte (its 1% shows an end date of Dec 31, 2026). `verified`.
- Booth sales: tax follows where the sale occurs. `inferred`: an event in Fort Myers carries Lee 0.5%, an event in Naples carries 0%.
- Marketplace (Etsy) and Shopify tax settings were not researched in this lane.

## Where sources disagree (X verified, Y need review)
- Google services and price: "descriptions and prices" on the live help page verified; a search summary saying custom services cannot carry prices needs review.
- Nextdoor posting: free page verified; "unlimited free posts" (current page) vs "twice per month" (2023-updated blog) need review. Radius center with a hidden address needs review.
- River District: $75 Artist and Business Booth and $50 Art Walk both verified; which applies to resale, and whether resale qualifies, need review.
- Season: Lee 2025 quarterly figures verified; Naples "Nov-Apr" and Collier demand need review.
- VMD fee: no source. Other VMD cities' fees from a search summary are not applicable.
- Surtax: Lee 6.5% and Collier 6% verified by three sources; Charlotte's post-Dec-2026 rate needs review in November.

## Recommendation for Holliewood & Vine

**What to do now (no accounts needed)**
1. Fix one shop spelling and use it everywhere (Google's name rule is "consistently represented").
2. Write the Google and Nextdoor copy as plain text: no links or prices in the Google description, a Story paragraph for Nextdoor. Decide the primary category with c5's wording table open.
3. Email VMD (sgulfcoastfl@vintagemarketdays.com) for the Jan 29-31 booth fee, and email events@rdafortmyers.com about Art Walk eligibility before about Nov 1.
4. Text the Pine Ridge manager (239-200-4401) to ask the market day and whether resale vintage is accepted, before paying anything.
5. Shoot 6-10 merchandised room photos for the VMD application.
6. Write a two-sentence pitch for Gulfshore Life Home + Design and a "first look" note for IDS Southwest Florida designers.
7. Put Lee 6.5% / Collier 6% into the local-delivery note, and calendar the November DR-15DSS recheck.
8. Browse estatesales.net Naples and Fort Myers weekly as price research; browse Freeman's Naples.

**What needs an account, a fee or a lawyer**
- Google Business Profile: a Google account and verification; category availability for the services list; confirm Hollie will actually make in-person visits or local deliveries first.
- Nextdoor: a free page needs verification to post; ads reach up to 30 miles.
- Fees: VMD booth (unpublished), Pine Ridge $160 minimum, River District $50-$75 (+$10 without a city occupational license), IDS dues (unknown), Paradise rack $95 per month (2024 price).
- Business tax receipt, Florida sales-tax registration and resale certificate, ch. 481 wording on the category, and ch. 538 buying: all in `research/fabulous-from-online/c5-florida-legal.md` (sections 1, 2, 5). Booth insurance: River District makes vendors responsible for their own; no minimum found.

**Local plan for this season (Oct 2026 to Apr 2027)**
- Oct 29-Nov 1: fix spelling; send the VMD, River District and Pine Ridge emails; Art Walk application due about Nov 1.
- November: set up Google (if visits are offered) and Nextdoor; recheck DR-15DSS when the 2027 form posts; choose between Dec 4 Art Walk (apply by about Nov 29) and the Dec 31 NYE vendor booth.
- December: holiday gifting is Oct-Dec headcount; optionally test Buckingham Farms Dec 5 or Edison Mall Dec 19 if fees are sane; apply early to VMD.
- January: VMD Jan 29-31 in the Jan-Mar peak (33.9% of Lee's annual visitor spending).
- Feb-March: pitch Gulfshore Life ahead of Naples by Design; IDS designer outreach.
- April: Naples by Design Apr 7-8; snowbirds head north, so lean on shipping.

## Ideas for Hollie
1. "Send it north": offer to ship or deliver to the buyer's northern home after the season; the Jan-Mar peak then flips to online orders in April (Lee VCB quarterly table).
2. Treat the VMD booth as lead-gen: a QR card pointing to Screen Test, the free Fabulous From Online intro (VMD vendor page).
3. Build the VMD application from the room photos: the jury wants merchandising proof (VMD vendor page).
4. Pitch vintage chairs to designers behind Chairs for Charity (Gulfshore Life Chairs for Charity).
5. "First look" email for IDS Southwest Florida members, instead of a discount (IDS chapter page; c2 R&R trade model).
6. A Naples Design District vintage pop-up, since the district markets "thrift, consignment" and "vintage gems" (Naples Design District).
7. Ask first buyers for a Nextdoor recommendation, since pages with recommendations are said to get far more views (Nextdoor claim guide, vendor claim).
8. A dated Gulfshore Life hook: a "room dressed from one estate sale" story timed to April 7-8 (Naples by Design page).
9. A three-month Paradise Vintage Market clothing rack ($95 per month, 2024 price) as a no-storefront test (Paradise vendor page).
10. A "Lee or Collier?" line at local checkout explaining 6.5% vs 6% so surtax is never a surprise (Florida DOR).
