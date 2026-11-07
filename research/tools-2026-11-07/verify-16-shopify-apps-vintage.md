# Verification of lane 16: Shopify apps for a one-of-one vintage shop

Date 2026-11-07. Author: research subagent (adversarial price and claim checker). Question: Do the prices, free tiers, platform and availability claims recorded for lane 16 (`16-shopify-apps-vintage.md`) hold on the vendors' own pages today? Legend: V = page read today; U = unverified (snippet, roundup, memory, or the page would not load). Verdicts: confirmed = the exact figure or claim is on the page read today; refuted = the page says something different (correction given); unreadable = the page did not load after one alternative attempt.

Method: 18 vendor page reads with headless Chromium through the session proxy (curl fallback), all on apps.shopify.com or help.shopify.com. Every price was read from the Pricing block of the Shopify App Store listing or from the Shopify Help Center, never from a roundup. The Shopify App Store page for each app is the vendor's own plans page: the vendor sets those plan names and prices and Shopify bills them. Quotes are verbatim from the page as rendered today; `...` marks skipped text. No subagents were used. Reddit, Etsy.com and eBay pages were not attempted. Every page checked was also grepped for "acquired", "sunset", "shut down", "discontinued", "deprecated" and "no longer"; the only hit is the Marketplace Connect Etsy notice recorded below.

## 0. Bottom line

- All 16 checks are confirmed. No price, free-tier limit, platform or availability claim in the PICKS was wrong today. This lane's first agent did its reading.
- The eight PICKS hold: Shopify's built-in local delivery (100 miles, 10 zones), shipping profiles (99 custom) and product video (250 per store on Basic) cost nothing extra; Judge.me is "Forever Free" with Awesome at "$15 / month"; Magical Make an Offer Starter is "Free to install" with "1% on paid orders only"; Shuttle is Free, "$12 / month", "$19 / month", "$39 / month"; Instafeed and Vizup have real free plans; Tiny SEO gives "50 Free image optimizations monthly"; PushLast is "$3.99 / month"; shopUpz UNLIMITED is "$18 / month".
- The one availability claim that matters most also holds: Shopify's own help center says "New connections to Etsy can't be made at this time with the Shopify Marketplace Connect app." Shuttle or shopUpz is the only Etsy bridge for a new store.
- Four high-fit TOOLS also hold: Shopify Messaging ("first 10,000 emails each month are free"), Shopify Inbox (Free), Offerly ("Only 0.9% of paid orders via offers"; Pro "$20 / month"), Pickeasy (Free, "1 pickup or delivery location", "Upto 10 orders/month").
- Small refinements, not errors: Judge.me now shows 49,785 reviews (49,783 recorded); Instafeed's free Starter has no product tagging or shop buttons (those are Pro, $8 / month), so the free grid is not shoppable; Vizup Pro has a "3-day free trial"; Pickeasy's yearly prices for Smart ($215.99) and Premium ($323.99) were not recorded; Shuttle's marketing text says "no limits or quotas" while its Free plan is capped at 10/10/10 a month.
- Shopify Messaging's app page never says it was Shopify Email. The rename is confirmed on the help center instead: "Shopify Messaging, formerly known as Shopify Email".
- No page carried a shutdown, sunset or acquisition notice.

## 1. Checks

| Tool | Claim checked | Verdict | Evidence quote | URL | Correction |
|---|---|---|---|---|---|
| Shopify local delivery (built in) | Included in plan; 100-mile radius cap; 10 zones per location; not compatible with Apple Pay or PayPal express | confirmed | "The maximum delivery radius is 160 kilometers or 100 miles." ... "You can add up to 10 delivery zones per location." | https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/local-delivery | None. Refinement: "Local delivery works with Shop Pay, but doesn't work with other accelerated checkouts such as Apple Pay, Google Pay, Amazon Pay, or PayPal." |
| Shopify shipping profiles (built in) | Included in plan; up to 99 custom profiles | confirmed | "You can create up to 99 custom shipping profiles when you need different shipping rates for different products." | https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles | None |
| Shopify product media video and 3D (built in) | Included; Basic plan allows 250 videos or 3D models per store | confirmed | "Video and 3D model limits by plan ... Plan Limit per store ... Basic and Shopify Partner development stores 250 ... Grow 1,000" | https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads | None. Also: "Maximum video length of 10 minutes" |
| Judge.me Product Reviews | Forever Free with unlimited product and store reviews and Etsy sync; Awesome $15 / month; 5.0 from 49,783 reviews | confirmed | "Forever Free ... Unlimited product and store reviews ... Sync with Shop App, Etsy, Amazon ... Awesome $15 / month" | https://apps.shopify.com/judgeme | Review count is now "(49,785)"; drift, not an error |
| Magical Make an Offer | Starter Free to install with 1% on paid orders only; Growth $9 / month with 0.33%; Power $199 / month or $999/year; 170 reviews; names vintage | confirmed | "Starter Free to install 1% on paid orders only. No sales, no fee." ... "Growth $9 / month Only 0.33% on paid orders." ... "Power $199 / month or $999/year" | https://apps.shopify.com/make-an-offer | None. Listing text: "Good for art, vintage, collectibles, B2B, and clearance pricing." Reviews "(170)" |
| Shuttle Sync with Etsy | Free with 10 product, 10 order and 10 review transfers a month, one Etsy shop; Essential $12 / month or $120/year; Growth $19 / month or $190/year with real-time stock sync; Scale $39 / month; 229 reviews | confirmed | "10 product transfers per month 10 order transfers per month 10 Etsy reviews stored per month ... Connect one Etsy shop" ... "Essential $12 / month or $120/year" ... "Growth $19 / month ... Real-time stock sync (200 orders/mo)" ... "Scale $39 / month" | https://apps.shopify.com/shuttle-transfer-from-etsy | None. Gotcha: the description says "no limits or quotas" but the Free plan is capped as quoted. Reviews "(229)" |
| Instafeed Instagram Feed | Starter Free with no branding or watermarks and hourly sync; Pro $8 / month; Plus $20 / month or $180/year; 2,281 reviews | confirmed | "Starter Free ... Unlimited views No branding or watermarks Hourly auto-sync" ... "Pro $8 / month" ... "Plus $20 / month or $180/year and save 25%" | https://apps.shopify.com/instafeed | None. Refinement: "Tag products & collections" and "Shop now & add to cart buttons" are Pro features, so the free grid is not shoppable |
| Vizup Shoppable Video Carousel | basic Free with unlimited views, unlimited product tags, 6 widgets; Pro $19.99 / month or $199.99/year; 101 reviews | confirmed | "basic Free ... Unlimited video views ... tag unlimited products to videos 6 widget designs" ... "Pro $19.99 / month or $199.99/year and save 17%" | https://apps.shopify.com/shoppable-video-reels | None. Pro carries a "3-day free trial". Reviews "(101)" |
| Shopify Inbox | Free; 5,820 reviews | confirmed | "Pricing Free" ... "Reviews (5,820)" | https://apps.shopify.com/inbox | None |
| Tiny SEO Speed Image Optimizer | Free for 50 image optimizations a month with 30-day backup; Beginner $14 / month or $140/year; Advanced $23 / month; Expert $49 / month; 2,583 reviews | confirmed | "Free ... 50 Free image optimizations monthly 30 day image backup" ... "Beginner $14 / month or $140/year and save 17%" ... "Advanced $23 / month" ... "Expert $49 / month" | https://apps.shopify.com/smart-image-optimizer | None. Reviews "(2,583)" |
| PushLast Out of Stock Sold Out | $3.99 / month for 1000 products; $9.99 / month for 10,000; 14-day trial only, no free plan; 18 reviews | confirmed | "1000 Products $3.99 / month ... 14-day free trial" ... "10,000 Products $9.99 / month" ... "100,000 Products $19.99 / month" | https://apps.shopify.com/pushlast | None. Header reads "From $3.99/month. Free trial available." Reviews "(18)" |
| shopUpz Etsy Sync & Import | Free imports 20 listings; Starter $9.99 / month; UNLIMITED $18 / month with two-way quantity sync; PRO $38 / month; 198 reviews | confirmed | "Free to install ... Import 20 Listings from Etsy" ... "Starter $9.99 / month" ... "UNLIMITED $18 / month ... Sync UNLIMITED quantities, Locations" ... "PRO $38 / month" | https://apps.shopify.com/shopupz-inventory | None. Reviews "(198)" |
| Shopify Marketplace Connect | Free to install; first 50 synced orders a month free, then 1% per order capped at $99 a month; no new Etsy connections; 2,135 reviews | confirmed | "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month" ... "New connections to Etsy can't be made at this time with the Shopify Marketplace Connect app." | https://apps.shopify.com/marketplace-connect and https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/requirements | None. The help page says existing Etsy users "can continue to use the app." Reviews "(2,135)" |
| Shopify Messaging (formerly Shopify Email) | Free to install; first 10,000 emails a month free, then from $1 per 1,000 emails; renamed from Shopify Email; 4,816 reviews | confirmed | "Your first 10,000 emails each month are free. After, pricing starts at $1/1000 emails per month." ... help center: "Shopify Messaging, formerly known as Shopify Email" | https://apps.shopify.com/shopify-messaging and https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-email | None. The rename is stated only on the help center, not on the app page. Reviews "(4,816)" |
| Offerly: Make An Offer Button! | Starter Free to install with 0.9% of paid orders via offers; Pro $20 / month flat; Elite $50 / month; 74 reviews | confirmed | "Starter Free to install Only 0.9% of paid orders via offers. No sale, No fee!" ... "Pro $20 / month No additional fees. Flat Rate." ... "Elite $50 / month" | https://apps.shopify.com/offerly | None. Pro and Elite carry a "14-day free trial". Reviews "(74)" |
| Pickup Delivery Date Pickeasy | Free with 1 location and up to 10 orders a month; Starter $9.99 / month or $107.99/year; Smart $19.99 / month; Premium $29.99 / month; 1,344 reviews | confirmed | "Free ... 1 pickup or delivery location Upto 10 orders/month" ... "Starter $9.99 / month or $107.99/year and save 10%" ... "Smart $19.99 / month" ... "Premium $29.99 / month" | https://apps.shopify.com/order-delivery-date-time | None. Omitted yearly prices: Smart "$215.99/year", Premium "$323.99/year". Enterprise add-ons at "$59.99". Reviews "(1,344)" |

Platform for every row: Shopify app or Shopify admin feature (web). Shopify Inbox also ships iOS and Android apps per the first agent; that claim was not re-checked here because the app page does not list platforms.

## 2. What the first agent got wrong

Nothing on price, free tier, platform or availability. Sixteen of sixteen checks confirm. Items worth a note:

- Judge.me review count drifted from 49,783 to 49,785 between the two reads. Not an error.
- The Instafeed PICK says "Free Instagram grid without watermark". True, but the free grid cannot tag products or show shop buttons; those are Pro at $8 / month. The PICK text did not claim shoppable on free, so no correction, only a caution for the synthesis.
- Shuttle's listing says "no limits or quotas" in its description while its Free plan is capped at 10 product transfers, 10 order transfers and 10 reviews a month. The first agent recorded the caps correctly. Anyone reading the description alone would be misled.
- Pickeasy's Smart and Premium yearly prices ($215.99 and $323.99) and Vizup Pro's 3-day trial were omitted. Omissions, not errors.
- The "formerly Shopify Email" label is not on the Shopify Messaging app page. It is confirmed on the help center. The first agent cited the app page for a fact that lives elsewhere.
- The Marketplace Connect requirements page loaded through the curl fallback rather than Chromium, but its text is complete and the Etsy notice is verbatim.

## 3. Gaps

- No page failed to load. Etsy.com, eBay and Reddit were not attempted; nothing in this lane needed them.
- Launch dates on the app pages did not render in the text extraction (the "Launched" label prints with a blank line after it), so the first agent's "launched July 6, 2026" claim for Instock by Pluglify was not re-checked. Instock was not in the 16 checks.
- Lookfy, Bird Pickup, Shop Pay Installments, Lably, Timesact and the rest of TOOLS were not re-checked; the 16-check cap was reached with the PICKS plus the four highest-fit TOOLS.

## 4. Sources (every URL fetched today)

https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/local-delivery
https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles
https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads
https://apps.shopify.com/judgeme
https://apps.shopify.com/make-an-offer
https://apps.shopify.com/shuttle-transfer-from-etsy
https://apps.shopify.com/instafeed
https://apps.shopify.com/shoppable-video-reels
https://apps.shopify.com/smart-image-optimizer
https://apps.shopify.com/pushlast
https://apps.shopify.com/shopupz-inventory
https://apps.shopify.com/marketplace-connect
https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/requirements
https://apps.shopify.com/inbox
https://apps.shopify.com/shopify-messaging
https://apps.shopify.com/offerly
https://apps.shopify.com/order-delivery-date-time
https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-email
