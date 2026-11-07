# Lane 16: Shopify apps for a one-of-one vintage shop (Holliewood and Vine)

Date 2026-11-07. Author: research subagent. Question: Which Shopify App Store apps fit a shop where every product is quantity one (sold items that stay visible, make-an-offer, fixed shipping classes, local pickup and delivery, oversize shipping, product video and room views, bundles for shop-the-room, reviews, Etsy sync), what do they cost, and what do their recent reviews say? Legend: V = page read today; U = unverified (snippet, memory, or page would not load).

Method note. WebSearch ran out of shared budget after the first round, so app handles were found by rendering Shopify App Store search pages (apps.shopify.com/search?q=...) and reading link targets. Every price, rating and review count below was read from the app's own listing on apps.shopify.com today. Review counts and ratings are as the listing showed them at fetch time. "Latest review" is the newest date seen on the listing or its reviews page. Shopify's App Store shows reviews in "most relevant" order on the listing, so the three dates per app are not always sorted.

## 0. Bottom line

- Most of what Hollie needs is already inside Shopify for free: pickup in store, local delivery (radius up to 100 miles, 10 zones per location), up to 99 custom shipping profiles for fixed shipping classes, product video and 3D on the product page (250 videos or models on the Basic plan), the free Shopify Bundles app for fixed bundles, the free Search & Discovery app for filters, Shopify Messaging (10,000 free emails a month), Shopify Inbox, Shopify Flow and Shopify Forms. Set these up before installing anything.
- Sold pieces stay visible by default. Shopify only hides out-of-stock products if you add a collection condition or use an app. For a "Sold" archive the free route is: leave inventory tracking on, do not add the hide condition, let the theme show its sold-out badge, and optionally use PushLast ($3.99 a month, 4.9 from 18 reviews) to push sold items to the bottom of collections. Instock by Pluglify is free and offers a Sold out badge and fading, but has zero reviews and launched July 2026.
- Make an offer: Magical Make an Offer (4.7, 170 reviews) is free to install with a 1% fee on paid orders, and its merchant summary names "vintage and consignment goods". Offerly (4.8, 74) is free to install with 0.9% on paid offers, or $20 a month flat. PriceMate (4.8, 35) has a true free plan "Ideal for selling under $100" with branding. Start with Magical Make an Offer; the 1% fee on a $400 lamp is $4.
- Etsy sync: Shopify's own Marketplace Connect no longer accepts new Etsy connections (help center, read today). Of the third-party apps, Shuttle has a real free plan (10 product and 10 order transfers a month, one Etsy shop, Etsy reviews import) and $12 a month for unlimited transfers; shopUpz is $9.99 a month for unlimited listing export and import, $18 for orders and quantity sync; QuickSync starts at $19; CedCommerce's $9 plan lists only 10 products and its 1-star reviews describe inventory drift. All Etsy apps carry an Etsy API caveat: QuickSync's listing says "Etsy restricts shipping addresses and tracking for US shops connected on or after 21 Oct 2024".
- Reviews: Judge.me is free with unlimited reviews, store reviews and "Sync with Shop App, Etsy, Amazon" on the free plan (5.0 from 49,783 reviews, newest review today). It replaces a separate Etsy review importer. Loox's free plan exists but its paid tier is $49.99 a month. Shopify's own Product Reviews app is gone; no Shopify-made review app appears in the App Store today.
- Shipping rules: Shopify shipping profiles cover fixed classes (small parcel, lamp, framed art, furniture, local only) for free. If a rate engine is ever needed, ShipX starts at $9.99 a month (5.0, 1,266) and Advanced Shipping Rules at $9 a month (4.8, 320). Intuitive Shipping ($70 a month) and ShipperHQ ($75 a month) are over budget. Rate engines usually need Shopify's carrier-calculated shipping feature, which is a plan matter (U; see the plans lane).
- Local pickup and delivery date pickers: Pickeasy (4.9, 1,344) and Bird (4.9, 519) both have free plans for 1 location and 10 orders a month. Zapiet now starts at $49.99 a month (4.9, 1,901) and a March 2026 review complains of required paid add-ons. Skip Zapiet at Hollie's volume.
- Room views and art previews: Picture It ($19 a month, 4.7 from 57) shows wall art in AR and in room mockups and is the only app found that targets art sellers. Hollie's own site already has a room editor, so this is only for the Shopify storefront. Vizup's free plan gives an unlimited shoppable video carousel.
- Skip: wishlists (Swym now starts at $29.99 a month, no free plan), apparel size-chart apps for furniture dimensions (use the description or metafields), Arty 3D viewer (2.1, 3 reviews, stale), Shop the Look: Easy Lookbooks (1.9, 2 reviews), Price it Make an offer (1.0, 1 review, 2023).

## 1. Comparison table

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Shopify pickup in store (built in) | Lets buyers choose pickup at checkout | included in plan; "You need to have at least one location that fulfills online orders." | yes, built in | Shopify admin | High. Zero cost, mixes ship and pickup in one order | V | https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store |
| Shopify local delivery (built in) | Delivery option by radius or postal codes | included; "The maximum delivery radius is 160 kilometers or 100 miles." | yes, built in | Shopify admin | High for Fort Myers and Naples; "up to 10 delivery zones per location" | V | https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/local-delivery |
| Shopify shipping profiles (built in) | Different rates per product group | included; "You can create up to 99 custom shipping profiles" | yes, built in | Shopify admin | High. Fixed classes for lamps, art, furniture, local-only | V | https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles |
| Shopify product media (built in) | Video and 3D on product pages | included; video "Maximum of 1 GB", "Maximum video length of 10 minutes"; Basic plan "250" videos or models per store | yes, built in | Shopify admin | High. Walkthrough clips per piece without an app | V | https://help.shopify.com/en/manual/products/product-media and https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads |
| Shopify Bundles | Fixed bundles and multipacks | "Free" | yes | Shopify app (Shopify-made) | Medium. Works for "buy the set"; 2.9 rating (570); bundle price does not auto-update | V | https://apps.shopify.com/shopify-bundles |
| Shopify Search & Discovery | Filters, boosts, recommendations | "Free" | yes | Shopify app (Shopify-made) | Medium. 2.6 rating (515); Oct-Nov 2026 reviews say synonyms were removed | V | https://apps.shopify.com/search-and-discovery |
| Shopify Messaging (was Shopify Email) | Email, SMS, WhatsApp marketing | "Your first 10,000 emails each month are free. After, pricing starts at $1/1000 emails per month." | yes | Shopify app (Shopify-made) | High for a small list | V | https://apps.shopify.com/shopify-messaging |
| Klaviyo | Email and SMS marketing | "Free to install"; Free "Up to 250 active profiles", "Up to 500 emails/month"; Email "$20 / month" for 251-500 contacts | yes | Shopify app, web | Low now; covered in another lane | V | https://apps.shopify.com/klaviyo-email-marketing |
| Shopify Inbox | Chat with buyers from admin and phone | "Free" | yes | Shopify app, iOS, Android | High. Handles offer conversations without an offer app | V | https://apps.shopify.com/inbox |
| Shopify Flow | Automation (tags, collections, emails) | "Free" | yes | Shopify app (Shopify-made) | High. Can tag sold items into a Sold collection | V | https://apps.shopify.com/flow |
| Shopify Forms | Lead and inquiry forms | "Free" | yes | Shopify app (Shopify-made) | Medium. A "hold this piece" or offer form | V | https://apps.shopify.com/shopify-forms |
| Shop channel | Lists products in the Shop app, Shop reviews | "Free" | yes | Shopify channel | Medium. Free discovery and third-party reviews | V | https://apps.shopify.com/shop |
| Pinterest channel | Product pins, ads | "Free to install"; "Pinterest charges only when ads are purchased" | yes | Shopify channel | Medium. 4.1 rating (1,706) | V | https://apps.shopify.com/pinterest |
| Google & YouTube channel | Google Shopping feed, ads | "Free to install"; "ad spend is billed directly to your Google Ads account" | yes | Shopify channel | Medium. 4.5 (5,613) | V | https://apps.shopify.com/google |
| Shopify Marketplace Connect | Sync to Amazon, Target Plus, Walmart, eBay | "Free to install"; "First 50 marketplace-synced orders/mo free, 1% fee per additional synced-order, capped at $99/month" | yes | Shopify app (Shopify-made) | Medium for eBay later; none for Etsy: "New connections to Etsy can't be made at this time" | V | https://apps.shopify.com/marketplace-connect and https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/requirements |
| Shop Pay Installments (built in) | Buyer pays in installments, merchant paid in full | included with Shopify Payments; eligible orders "$35 to $30,000 USD in the United States" | yes | Shopify checkout | High as the layaway substitute | V | https://help.shopify.com/en/manual/payments/shop-pay-installments |
| Magical Make an Offer | Offer button, auto accept, decline, counter | Starter "Free to install" "1% on paid orders only. No sales, no fee."; Growth "$9 / month" "Only 0.33% on paid orders."; Power "$199 / month" | free to install, usage fee | Shopify app | High. 4.7 (170); summary cites "vintage and consignment goods" | V | https://apps.shopify.com/make-an-offer |
| Offerly: Make An Offer Button! | Offer button, auto accept, counter | Starter "Free to install" "Only 0.9% of paid orders via offers. No sale, No fee!"; Pro "$20 / month"; Elite "$50 / month" | free to install, usage fee | Shopify app | High. 4.8 (74); latest review Sept 21, 2026 | V | https://apps.shopify.com/offerly |
| PriceMate Make An Offer | Offer widget | FREE "Ideal for selling under $100"; Silver "$7.99 / month" "Remove branding"; Gold "$17.99 / month"; Platinum "$40 / month" | yes, with branding | Shopify app | Medium. 4.8 (35) | V | https://apps.shopify.com/bargain-make-an-offer |
| Price it Make an offer | Offer button | "Free to install"; "We only charge 1% of the offer amounts that convert" | free to install | Shopify app | Low. 1.0 (1), last review 2023 | V | https://apps.shopify.com/price-it-make-an-offer |
| PushLast Out of Stock Sold Out | Pushes sold-out products to the end of collections | "$3.99 / month" for 1000 products | 14-day trial only | Shopify app | High for a Sold archive. 4.9 (18) | V | https://apps.shopify.com/pushlast |
| Instock by Pluglify | Hide, fade, push down or badge sold-out items | "Free" | yes | Shopify app (theme extension) | Medium. 0 reviews, launched "July 6, 2026" | V | https://apps.shopify.com/instock-1 |
| SmartStock: Sold out variants | Grey overlay on sold-out variants | "From $3.99/month" | trial only | Shopify app | Low. Variant-level; 0 reviews, launched May 2026 | V | https://apps.shopify.com/smartstock-app |
| Lably Product Labels & Badges | Custom badges by rule | Free "1 active label rule / 1 active badge rule / Unlimited products"; Basic "$7.99 / month" | yes | Shopify app | Medium. One free rule can be a SOLD badge. 5.0 (677) | V | https://apps.shopify.com/lably |
| Smart Product Badges | SALE, NEW, Sold Out badges | "$2.99 / month" | trial only | Shopify app | Low. 0 reviews, launched June 2026 | V | https://apps.shopify.com/smart-product-badges |
| Advanced Shipping Rules (Bambri) | Product-group shipping rules, blending | Lite "$9 / month" "Up to 2 Product Groups"; Standard "$29"; Pro "$59"; Unlimited "$99" | "Unlimited Free Trial in Test Mode" | Shopify app | Medium. 4.8 (320). Only if profiles fall short | V | https://apps.shopify.com/vendor-shipping-rules-1 |
| ShipX Shipping Rates & Rules | Rates by zip, weight, product, dimensions | Free "Configure and test in testing mode"; Starter "$9.99 / month"; Smart "$19.99"; Premium "$34.99" "Dimension based rates" | test mode only | Shopify app | Medium. 5.0 (1,266) | V | https://apps.shopify.com/shipping-rates |
| CBB Shipping Rates Calculator | Shows shipping rates in cart | "$4.99 / month or $49.90/year" | 14-day trial | Shopify app | Low. Display only; 4.7 (239), last review June 2026 | V | https://apps.shopify.com/shipping-rates-calculator-plus |
| Intuitive Shipping | Dimensional, multi-box, rules | Sandbox "Free"; Growth "$70 / month" "500 orders included" | sandbox only | Shopify app | Low at this budget. 5.0 (497) | V | https://apps.shopify.com/intuitive-shipping |
| ShipperHQ | Carrier rules at checkout | Essentials "$75 / month" "2 Carriers / 5 Shipping Rules" | 15-day trial | Shopify app | Low. 4.7 (74) | V | https://apps.shopify.com/shipperhq |
| Zapiet Pickup + Delivery | Pickup and delivery date slots, zones | Essential "$49.99 / month" "1 location / 250 orders/month"; Advanced "$79.99"; Professional "$179.99" | 14-day trial | Shopify app | Low. 4.9 (1,901) but priced for bakeries and caterers | V | https://apps.shopify.com/click-and-collect |
| Pickup Delivery Date Pickeasy | Date and time slots for pickup and delivery | Free "1 pickup or delivery location / Upto 10 orders/month"; Starter "$9.99 / month" | yes | Shopify app | High if a date picker is wanted. 4.9 (1,344) | V | https://apps.shopify.com/order-delivery-date-time |
| Bird Pickup & Delivery Date | Date and time picker | Free "10 orders / month / 1 store location"; Essential "$19.99 / month" | yes | Shopify app | High alternative. 4.9 (519) | V | https://apps.shopify.com/store-pickup-and-delivery-date |
| Local Delivery + Pickup: SE | Delivery widget, routes, driver app | Essential "$19 / month" | 7-day trial | Shopify app, iOS, Android driver app | Low. 5.0 (134); built for fleets | V | https://apps.shopify.com/local-delivery-store-pickup |
| Shuttle Sync with Etsy | Transfer products, orders, reviews; stock sync | Free "10 product transfers per month / 10 order transfers per month / 10 Etsy reviews stored per month"; Essential "$12 / month"; Growth "$19 / month" "Real-time stock sync (200 orders/mo)" | yes | Shopify app | High. 4.7 (229); manual transfers on free | V | https://apps.shopify.com/shuttle-transfer-from-etsy |
| shopUpz Etsy Sync & Import | Export and import listings, orders, quantity sync | Free "Import 20 Listings from Etsy"; Starter "$9.99 / month" "Export UNLIMITED listings to Etsy"; UNLIMITED "$18 / month" "Manage UNLIMITED orders / Sync UNLIMITED quantities"; PRO "$38" | yes (import only) | Shopify app | High. 4.7 (198); one-developer app | V | https://apps.shopify.com/shopupz-inventory |
| QuickSync: Etsy Integration | Inventory, product and order sync | Lite "$19 / month" "Up to 1,000 syncing variants"; Pro "$29 / month" "New Etsy order syncing"; Ultra "$69"; Ultra+ "$99" | "Free: $0, 100-variant stock sync for eligible shops" | Shopify app | Medium. 4.8 (2,022); 1-star reviews allege review-begging | V | https://apps.shopify.com/quicksync-etsy |
| CedCommerce Etsy Integration | Listing, inventory, order sync | Beginner "$9 / month" "List up to 10 Products"; Growth "$59 / month" "List up to 1000 Products on Etsy" | 7-day trial | Shopify app | Low. 4.5 (1,248); drift complaints in 2026 | V | https://apps.shopify.com/etsy-marketplace-integration |
| DPL Etsy Integration | Product, inventory, order sync | Silver "$19.99 / month" "Up to 1,000 products sync / Sync & Fulfill 200 Orders/month" | 7-day trial | Shopify app | Medium. 4.9 (966) | V | https://apps.shopify.com/etsy-integration-dpl |
| LitCommerce eBay Etsy Amazon + | Multichannel listing from Shopify | "$29 / month or $278/year" "From 1000 Listings, 3 Channels" | 7-day trial | Shopify app, web | Medium later. 4.8 (983); overlaps the crosslister lane | V | https://apps.shopify.com/litcommerce |
| Judge.me Product Reviews | Reviews, store reviews, Etsy and Shop sync | Forever Free "Free" "Unlimited product and store reviews" "Sync with Shop App, Etsy, Amazon"; Awesome "$15 / month" | yes | Shopify app | High. 5.0 (49,783); newest review Nov 7, 2026 | V | https://apps.shopify.com/judgeme |
| Loox Product Reviews | Photo and video reviews | Beginner "Free" "Up to 500 orders"; Convert "$49.99 / month"; Unlimited "$299.99 / month" | yes | Shopify app | Medium. 4.9 (10,054); paid tier over budget | V | https://apps.shopify.com/loox |
| Reputon Etsy Reviews | Imports Etsy reviews | Standard "$6.99 / month or $62.99/year" | dev stores only | Shopify app | Low. Judge.me free does this. 5.0 (347) | V | https://apps.shopify.com/reputon-etsy-reviews |
| Trustify Etsy Reviews Importer | Imports Etsy reviews | Member "$5.99 / month" "200 reviews/ products" | listing says "Free plan available" but only a $5.99 plan is shown | Shopify app | Low. 4.9 (118) | V | https://apps.shopify.com/etsy-reviews-importer |
| Timesact Preorder Now | Preorder, deposit, waitlist, wishlist | Free "20 orders per month (unlimited products)" "Timesact branding"; CORE Flex "$5 / month" "Split Payments, Deposit"; PRO Flex "$7 / month" "NEW: Wishlist" | yes | Shopify app | Medium. 5.0 (2,136); deposits on a hold | V | https://apps.shopify.com/timesact-discount-pre-order |
| Reservo Deposits & Layaway | Stock holds, deposits, layaway | In-person only "$19 / month"; In-person & Online "$29 / month"; Automation "$39 / month" | 7-day trial | Shopify app, POS | Medium. Exactly the "hold it for me" case; 4.8 (6) | V | https://apps.shopify.com/pos-layaway-stock-reservations |
| Downpay Partial Pay & Deposit | Deposit now, balance later | Essentials "$29 / month" "Up to $5,000 in total order value processed" | 7-day trial | Shopify app | Low. 5.0 (96); value-capped tiers | V | https://apps.shopify.com/downpay |
| Layaway: Reserve & Deposit (Molsoft) | POS layaway | Basic "$17 / month" | 7-day trial | Shopify POS app | Low. 0 reviews, launched May 2026 | V | https://apps.shopify.com/layaway-1 |
| Kiwi Size Chart & Recommender | Size charts | Free Plan "Publish Up to 3 Size Charts" "Kiwi Watermark Included"; Premium "$7.99 / month" | yes, watermark | Shopify app | Low. Apparel-shaped; 4.7 (1,244) | V | https://apps.shopify.com/kiwi-sizing |
| MP Size Chart & Size Guide | Size charts | Starter "Free" "Publish up to 3 size charts"; Growth "$6.95 / month" | yes | Shopify app | Low. 5.0 (881); same reason | V | https://apps.shopify.com/avada-size-chart |
| Instafeed Instagram Feed | Instagram grid on the store | Starter "Free" "No branding or watermarks" "Hourly auto-sync"; Pro "$8 / month" "Tag products"; Plus "$20 / month" | yes | Shopify app | High. 4.9 (2,281) | V | https://apps.shopify.com/instafeed |
| Essential Trust Badges & Icons | Payment and trust icons | Free Plan "Up to 5000 monthly views"; Starter "$6.99 / month" | yes | Shopify app | Medium. 5.0 (1,163) | V | https://apps.shopify.com/essential-icon-badge-banners |
| Conversion Bear Trust Badges | Trust badges | "Free" | yes | Shopify app | Medium. 4.8 (381); last review Sept 2026 | V | https://apps.shopify.com/ultimate-trust-badges |
| HelpLab FAQ Page, Product FAQs | FAQ page and product FAQs | Basic "Free" "10 FAQs" "No copyright"; Essentials "$3.99 / month"; Professional "$7.99 / month" | yes | Shopify app | Medium. 5.0 (220) | V | https://apps.shopify.com/faqs-plus |
| Trusted Help Center & FAQ | FAQ page | FREE "Main FAQ in a separate URL"; Monthly "$4.99 / month"; Lifetime "$79 one-time charge" | yes | Shopify app | Medium. 5.0 (92) | V | https://apps.shopify.com/faqapp |
| Tiny SEO Speed Image Optimizer (TinyIMG) | Image compression, alt text, SEO audits | Free "50 Free image optimizations monthly"; Beginner "$14 / month or $140/year"; Advanced "$23"; Expert "$49" | yes | Shopify app | High on free. 5.0 (2,583) | V | https://apps.shopify.com/smart-image-optimizer |
| Smart SEO AI & Image Optimizer | Meta tags, alt tags, image optimizer | Free "Image Optimization (50 images)" "20 AI Generations"; Pro "$14.99 / month or $149.90/year" | yes | Shopify app | Medium. 5.0 (958); pick one of the two | V | https://apps.shopify.com/smart-seo |
| PageFly Page Builder | Landing and product page builder | Free "1 published slot (1 page or 1 section)"; Builder "$24 / month"; Accelerate "$99 / month" | yes | Shopify app | Medium. 4.9 (5,927); theme sections first | V | https://apps.shopify.com/pagefly |
| Shogun Landing Page Builder | Page builder | Draft Mode "Free" "Create Draft Pages - No Page Publishing"; Build "$39 / month or $372/year" | drafts only | Shopify app | Low. 4.8 (1,979) | V | https://apps.shopify.com/shogun |
| Vizup Shoppable Video Carousel | Shoppable video carousel, gallery | basic "Free" "Unlimited video views" "tag unlimited products to videos"; Pro "$19.99 / month" | yes | Shopify app | High on free. 5.0 (101); newest review Nov 7, 2026 | V | https://apps.shopify.com/shoppable-video-reels |
| SalesUp Shoppable Video Slider | Video slider | "Free" | yes | Shopify app | Low. 5.0 (7) | V | https://apps.shopify.com/salesup-slider |
| Picture It: AR & Art Previews | AR wall preview and room mockups for art | Room Mockups Only "$19 / month" "Up to 200 activated products"; Starter "$19 / month" AR; Professional "$39 / month" "Removed Picture It branding" | 14-day trial | Shopify app (works on phone browsers for AR) | Medium. Only art-specific app found; 4.7 (57) | V | https://apps.shopify.com/picture-it |
| Arty 3D model viewer | 3D and AR viewer | "From $19/month" | 14-day trial | Shopify app | Low. 2.1 (3), reviews from 2024-2025 | V | https://apps.shopify.com/arty-model-viewer |
| Lookfy Lookbook: Image Gallery | Shop-the-look galleries | Free "Create 1 Gallery" "50 Photos Each Gallery" "Shop The Look" "No brandmark"; Starter "$5.99 / month" | yes | Shopify app | High for one shop-the-room page. 4.8 (234) | V | https://apps.shopify.com/lookfy-lookbook-gallery-1 |
| Byte Lookbook & Shop The Look | Lookbooks with hotspots | Free "Create 1 Lookbook" "No brandmark"; Growth "$19 / month or $150/year" | yes | Shopify app | Medium. 5.0 (117); last review Aug 2026 | V | https://apps.shopify.com/shop-the-look-4 |
| Hotshop Product Image Hotspot | Hotspots on product images | Free "Create 2 hotspots"; Basic Fit "$5.99 / month" | yes | Shopify app | Low. 4.2 (5) | V | https://apps.shopify.com/hotshop-product-image-hotspot |
| Shop the Look: Easy Lookbooks | Lookbooks | "Free" | yes | Shopify app | Low. 1.9 (2) | V | https://apps.shopify.com/shop-the-look |
| Swym Wishlist Plus | Wishlist | Starter "$29.99 / month or $299.99/year" | 30-day trial, no free plan today | Shopify app | Low. 4.7 (1,477); over budget | V | https://apps.shopify.com/swym-relay |
| Swish Wishlist & Accounts | Wishlist, customer hub | Starter "$19 / month" "Plus usage charges" | 30-day trial | Shopify app | Low. 5.0 (290) | V | https://apps.shopify.com/wishlist-king |

## 2. Notes per tool

### Built-in Shopify features (read on help.shopify.com today)

- Pickup in store. Requirement: "You need to have at least one location that fulfills online orders." Buyers can mix: "A customer can choose to have some items shipped and some items picked up in the same order." Supported themes show pickup availability on the product page. Shopify Plus can swap in a custom pickup app; Hollie does not need that.
- Local delivery. "You can offer delivery within a set distance from your location, or for certain postal codes." Limits: 100 miles radius, "up to 10 delivery zones per location", "up to 3 additional price-based rules per zone". Gotchas: "Using any third-party shipping apps might conflict with Shopify's local delivery method." and "Local delivery works with Shop Pay, but doesn't work with other accelerated checkouts such as Apple Pay, Google Pay, Amazon Pay, or PayPal." Buyers "can't choose to have some items shipped and some items locally delivered on the same order". When using a radius, "your business location must be verified".
- Shipping profiles. "You can create up to 99 custom shipping profiles when you need different shipping rates for different products." Note on the page: "Shipping profiles and shipping rates are gradually moving to shipping options by market", existing setups migrate automatically. This is the free answer to fixed shipping classes and oversize pieces: one profile per class with flat rates, plus a "local pickup or delivery only" profile for furniture with no shipping rate.
- Product media. "Product media can include images, 3D models, and videos." You need "a theme that supports 3D models and videos". File limits: video "Maximum of 1 GB", "Maximum video length of 10 minutes", formats "MOV, MP4, and WEBM"; "These limits don't apply to embedded Vimeo or YouTube links." Per-store video and 3D model count: Basic 250, Grow 1,000, Advanced 5,000. For a shop of 50 to 100 live pieces, 250 is enough if sold items' videos are deleted or hosted on YouTube.
- Shopify Bundles (free, Shopify-made). Help: "a free first-party bundles app that allows you to create and edit fixed product bundles and multipacks right from your Shopify admin, and is available on all Shopify plans." Limits: "Fixed bundles: Up to 30 components", "Maximum of 3 options and 100 variants total per bundle", "When the price of one of the bundled products updates ... the bundle price doesn't update", "Bundles aren't compatible with purchase options, which includes subscriptions, pre-orders". Listing rating 2.9 (570). Newest reviews: Oct 16, 2026 "A bundle containing two products counts as only ONE item for quantity-based free shipping"; Aug 1, 2026 "it doesnt bring over the imagery - so you basically have to redo all the work". For one-of-one pieces a fixed bundle of two unique items works because "Inventory is updated in real-time, so you're protected from overselling": when one component sells alone, the bundle goes out of stock.
- Search & Discovery (free, Shopify-made). Listing promises "Customize filters", "Make synonym groups", "product boosts". Rating 2.6 (515). Newest reviews, Oct-Nov 2026: "Please restore the synonym feature." (Nov 6), "Why would you remove Synonyms without any notice?" (Oct 13), "Only 25 filters makes literally no sense" (Oct 6), "shows every single item in search" (Oct 23). Treat the synonym feature as unreliable right now. Filters by availability, price and attributes still work per the help page.
- Selling and hiding out of stock. "By default, customers can't purchase an item until you adjust the inventory levels to add more stock." Products are not hidden unless you add a collection condition: "When you hide out of stock products, they're removed from your collections". So a Sold archive is the default state; the sold-out badge text itself is set by the theme (not verified today, U).
- Shop Pay Installments. Eligible orders "$35 to $30,000 USD in the United States, including discounts, shipping, and taxes". Needs Shopify Payments and Shop Pay and an eligible US business entity. This covers "can I pay over time" without any layaway app; the merchant is paid up front (U on payout timing; help page lists a "Getting paid" section not read).
- Marketplace Connect. Help: "New connections to Etsy can't be made at this time with the Shopify Marketplace Connect app. If you're already selling on Etsy through Marketplace Connect, then you can continue to use the app." Listing is 4.1 (2,135) and still lists eBay, Amazon, Walmart, Target Plus. Pricing: 50 synced orders a month free, then 1% per order capped at $99 a month. Newest reviews (Nov 4 and 7, 2026) are Walmart listing complaints. Keep in mind for eBay once Shopify is live; it is not an Etsy tool.
- Shopify Messaging (the listing at apps.shopify.com/shopify-email redirects here). "Free to install. Additional charges may apply." and "Your first 10,000 emails each month are free." 4.8 (4,816). Shopify Inbox 4.5 (5,820), Flow 4.7 (15,345), Forms 4.5 (767), Shop channel 4.8 (10,169). A Shop channel reviewer: "The reviews alone are worth it. They're third party, on a platform people already trust".

### Make an offer

- Magical Make an Offer (Magical Apps). 4.7 (170). "What merchants think": "reliably boosts sales and revenue, often by 12-20%+, especially on slow-moving or high-ticket items like vintage and consignment goods". Reviewers include "Betel Restored Furniture" (Sept 11, 2026, "working without any major issues"), "Le Shoppe Modern" (Jan 29, 2026, "Almost 5 years using the app") and an artist (Oct 13, 2026). Gotchas from 1-star reviews: Aug 19, 2025 "You've approved an app with a usage limit of $499.00 USD every 30 days" (Shopify's usage pre-approval cap at install; the developer replied it "only applies at very high sales volumes"); Sept 30, 2025 a merchant disputed a "2.99%" charge versus the advertised 1% (developer replied "charges up to 1% on completed sales"). Free tier is usage-based, not flat. Fit: high. A one-of-one shop lives on offers; the 1% fee scales with sales.
- Offerly (Nakatomi Apps). 4.8 (74). Starter is free to install with 0.9% on offers that pay; Pro is $20 a month flat with "No additional fees". Review June 1, 2026 notes initial difficulty "setting up emails so they came from my store rather then Offerly's email", fixed by support. Latest review Sept 21, 2026. Fit: high; the $20 flat plan beats 1% once offer sales pass about $2,000 a month.
- PriceMate (bargain-make-an-offer). 4.8 (35). The only true flat free plan, "Ideal for selling under $100", with branding until Silver ($7.99). Latest review Sept 16, 2026. Fit: medium; small review base.
- Price it. 1.0 (1), last review June 2023. Skip.

### Sold items that stay visible

- Native: leave sold pieces published with zero inventory. Do not add the "inventory greater than 0" collection condition. Optionally run a Shopify Flow that tags a product "sold" when inventory hits zero and feeds an automated "Sold" collection (Flow is free; the exact trigger was not verified today, U).
- PushLast. "$3.99 / month" for up to 1000 products. "Push sold out products to the bottom of the product list and add them back to the top when the product is back in stock". 4.9 (18). Latest review July 30, 2026. Fit: high and cheap; keeps live pieces first and the archive underneath.
- Instock by Pluglify. Free. "Hide them from collection pages, fade them while keeping product pages live, move them to the bottom, or show a Sold out badge." Built "with a Shopify theme app extension". Zero reviews, launched July 6, 2026. Fit: medium; try it, but it is unproven.
- Lably. Free plan allows one label rule and one badge rule on unlimited products; a rule can target out-of-stock products for a custom SOLD badge (the listing describes rule-based badges; the out-of-stock condition was not confirmed on the page, U). 5.0 (677). Latest review Oct 23, 2026.
- SmartStock and Smart Product Badges: new (May and June 2026), zero reviews, variant-focused. Skip.

### Shipping rate apps

- Shopify profiles first (free). Rate apps generally require Shopify's carrier-calculated shipping feature, which is tied to plan or annual billing; this was not verified today and belongs to the plans lane (U). ShipX advertises "Rename, hide, reorder rates without CCS API", which implies its rate features do use it.
- Advanced Shipping Rules (Bambri, handle vendor-shipping-rules-1). Lite $9 a month: "Up to 2 Product Groups", "1 Blended Rate", "*No Hide/Show Rules*". "Unlimited Free Trial in Test Mode". 4.8 (320). Latest review Sept 1, 2026.
- ShipX. Free is test mode only. Starter $9.99 a month covers "Rates by Cart Total, Weight, Quantity" and zip or distance rates; Smart $19.99 adds "Set rates by each product"; Premium $34.99 adds "Dimension based rates using meta fields". 5.0 (1,266). Latest review Oct 15, 2026.
- CBB Shipping Rates Calculator. $4.99 a month. Shows rates in the cart; it is not a rules engine. 4.7 (239). Last review June 22, 2026.
- Intuitive Shipping. Free sandbox, then $70 a month. Merchant summary: "accurate dimensional and multi-box rating for bulky, heavy, or perishable items". A reviewer (Oct 27, 2026): "Significantly less expensive than ShipperHQ". Over budget.
- ShipperHQ. $75 a month minimum. 4.7 (74). Over budget.

### Local pickup and delivery apps

- Zapiet Pickup + Delivery. Now "From $49.99/month" (a search snippet earlier today still said $29.99; the listing is the price). Essential: "1 location", "250 orders/month". 4.9 (1,901), latest review Nov 6, 2026, mostly bakeries and caterers. 1-star March 2, 2026: "requires either an add-on zip code app ($14.99/mo) or a google API key ($100/mo)". 1-star Aug 27, 2026 about a refused annual refund. Fit: low; too much and too dear for a one-person decor shop.
- Pickeasy (order-delivery-date-time). Free: "1 pickup or delivery location", "Upto 10 orders/month", "ZIP/postal code validation". Starter $9.99 a month adds POS and product-specific fulfillment methods. 4.9 (1,344). Latest review Oct 19, 2026. Fit: high if Hollie wants buyers to pick a pickup slot; otherwise native pickup is enough.
- Bird Pickup & Delivery Date. Free: "10 orders / month", "1 store location". Essential $19.99 a month for 250 orders. 4.9 (519). Latest review Nov 3, 2026.
- Local Delivery + Pickup: SE. $19 a month, driver app and routes. Built for fleets. Skip.

### Etsy sync apps

- Shuttle (Illumiko). Free plan: "10 product transfers per month", "10 order transfers per month", "10 Etsy reviews stored per month", "Connect one Etsy shop", "Manual transfers, you stay in control". Essential $12 a month: "Unlimited product & order transfers", "Etsy reviews on your Shopify store", "Full variations, images & videos". Growth $19 a month adds "Real-time stock sync (200 orders/mo)" and "Prevent overselling instantly". 4.7 (229). Newest reviews Oct 2026 are positive; one Oct 5 review was confused that transfers land "in Etsy as draft listings". Fit: high. Free covers a shop that lists about ten pieces a month; $12 covers unlimited; real-time delist-on-sale needs the $19 tier.
- shopUpz. Free: "Import 20 Listings from Etsy". Starter $9.99 a month: "Export UNLIMITED listings to Etsy", "Import UNLIMITED listings from Etsy", "Update Etsy Listing Prices", "Generate SKUs". UNLIMITED $18 a month: "Manage UNLIMITED orders", "Sync UNLIMITED quantities, Locations". Merchant summary: "reliable inventory sync (especially with matching SKUs)" and "Etsy order import into Shopify with tracking sent back to Etsy". 4.7 (198). Latest review Nov 3, 2026. All replies are signed by one person ("Shirly"), so support depth is one developer. Fit: high at $18 for two-way sync.
- QuickSync (R.I.T.N.S.). Lite $19 a month is inventory sync and import only; order sync needs Pro $29. The listing says "Free: $0, 100-variant stock sync for eligible shops" and warns "Etsy restricts shipping addresses and tracking for US shops connected on or after 21 Oct 2024; other regional limits may apply." 4.8 (2,022). 1-star Sept 21, 2026: support "will ask you repeatedly to leave 5 star feedback before you've even had a chance to use the app"; Nov 2, 2026: "It's literally never worked." Fit: medium.
- CedCommerce. $9 plan lists only 10 products; $59 for 1,000. 4.5 (1,248). 1-star Sept 16, 2026: "The app would routinely remove inventory from Etsy or add too much"; Oct 20, 2026: "would sell and item that was out of stock bc CED Commerce does not seem to update in real time". Fit: low.
- DPL. $19.99 a month, 1,000 products, 200 orders. 4.9 (966). 1-star Sept 8, 2026: setup "about to upload duplicate products" and "several hours manually matching the SKUs". Fit: medium.
- LitCommerce. $29 a month, 1,000 listings across 3 channels. 4.8 (983). This is a crosslister that lives inside Shopify; it competes with Crosslist and belongs to that decision, not this one.
- Etsy API caveat for all of them: the QuickSync listing's note about US shops connected after Oct 21, 2024 means order addresses may not flow into Shopify for a new Etsy connection. Treat Etsy order fulfillment as happening on Etsy, and use these apps for listings and inventory. Etsy's own API terms were not read today (U).
- Etsy review importers (Reputon $6.99, Trustify $5.99) are unnecessary because Judge.me's free plan syncs Etsy reviews.

### Reviews

- Judge.me. Free plan: "Unlimited product and store reviews", "Unlimited visual reviews (photos/videos)", "Google reviews sync & rich snippets", "Trust badge and medals", "Sync with Shop App, Etsy, Amazon". Awesome $15 a month adds Q&A, coupons, Klaviyo integration. 5.0 (49,783), reviews posted today. Merchant summary: "generous free plan, fair fixed pricing". For one-of-one stock, product reviews pile up one per sold piece; store reviews and the all-reviews page do the work, and both are free here.
- Loox. Free Beginner lists "Up to 500 orders"; Convert is $49.99 a month. 4.9 (10,054). Over budget for the paid tier; free is fine but Judge.me's free plan does more.
- Shopify Product Reviews. Discontinued; search results today point to 2023-2024 shutdown dates on community and vendor pages, not an official page (U). The App Store search for "shopify reviews" shows no Shopify-made review app (V).

### Pre-order, hold, layaway

- Native: Shop Pay Installments for buyer financing. Draft orders with a deposit are also native but were not verified today (U).
- Timesact. Free 20 orders a month with "Timesact branding"; CORE Flex $5 a month adds "Split Payments, Deposit, 0 down preorder". 5.0 (2,136), newest review Nov 6, 2026. A 1-star April 1, 2026 review alleges the "3x" bonus limit requires a video testimonial and is a lifetime cap; the developer called the review "bad faith". Fit: medium; preorders do not apply to one-of-one pieces, but deposits on a hold do.
- Reservo Deposits & Layaway. "A paid deposit creates a Shopify order and commits stock", "Real stock holds that auto-expire and return unsold items to your inventory". Online deposits need the $29 a month tier. 4.8 (6), newest review Oct 19, 2026. Fit: medium; it is the exact "hold the chandelier" feature, but it is new and $29.
- Downpay from $29 a month with order-value caps; Molsoft Layaway $17 a month, zero reviews. Skip.

### Furniture dimensions

- Kiwi and MP size charts are built for apparel. Both allow three free charts; Kiwi's free plan has "Kiwi Watermark Included". For lamps and chairs, a dimensions table in the description or a metafield shown by the theme is free and clearer. No app needed.

### Social, badges, FAQ, SEO, pages, video

- Instafeed free: "No branding or watermarks", "Hourly auto-sync", "Unlimited views". Product tagging on the grid needs Pro ($8 a month). 4.9 (2,281).
- Essential Trust Badges free up to 5,000 monthly views; Conversion Bear Trust Badges free. A one-person shop can also write the policies in the theme's footer for free.
- HelpLab FAQ free for 10 FAQs with "No copyright" (no branding); Trusted Help Center & FAQ free for a main FAQ page, $79 lifetime for product FAQs. Theme collapsible sections may already cover this (U).
- Tiny SEO (developer TinyIMG; the handle "tinyimg" returns a 404, the live handle is smart-image-optimizer): free 50 image optimizations a month with alt text, filename optimization and "30 day image backup". An earlier search snippet quoted a reviewer whose images disappeared after filename generation (U). Smart SEO: free 50 images and 20 AI generations. Pick one.
- PageFly free is "1 published slot (1 page or 1 section)"; Builder $24 a month. Shogun free cannot publish. Theme sections are free; a page builder is a later luxury.
- Vizup free: "Unlimited video views", "tag unlimited products to videos", "6 widget designs". 5.0 (101), newest review Nov 7, 2026. Pairs with native product-page video.
- Picture It. "Live 3D previews for wall art in augmented reality. View your artwork on a wall or virtual room"; "Room Mockup add-on to preview art or furniture in different rooms"; "Import dimensions for accurate, realistic AR previews". $19 a month for AR or for room mockups, $10 a month to add the other, $39 to remove branding. 4.7 (57). Newest reviews: Oct 13, 2026 "amazing in helping resolve a display issue"; Sept 16, 2026 "a little buggy but the customer service is really responsive"; Sept 15, 2026 "such a lifesaver for any wall art shop". Fit: medium. Hollie's own site has a room editor; on Shopify this is the paid stand-in and it only covers art, not lamps.

### Shop the room

- Shopify Bundles (free) for "buy both" sets; Lookfy free for one gallery of up to 50 photos with shop-the-look pins and no brandmark; Byte free for one lookbook. Gotcha for one-of-one stock: pins point at pieces that sell, so the gallery needs editing after each sale. A lookbook of the room photo with pins is cheap to maintain at Hollie's scale.

## 3. Recommendation for Hollie

Install or switch on today, all free:
1. Shopify pickup in store and local delivery (Settings > Shipping and delivery). Set a radius that covers Fort Myers and Naples, under the 100-mile cap.
2. Shipping profiles: small parcel, lamp, framed art, oversize or local only. No app.
3. Product video on each listing from the phone (MP4 under 1 GB, under 10 minutes). No app.
4. Judge.me free. Turn on store reviews and Etsy review sync.
5. Instafeed free, Vizup free, Shopify Inbox, Shopify Flow, Shopify Forms (an "ask about this piece" or "hold request" form).
6. Magical Make an Offer on the free Starter plan (1% of paid offers). Note the Shopify usage cap screen at install; it is a pre-approval, not a charge.
7. Shuttle on the free plan to move the first Etsy listings into Shopify and keep Etsy reviews.
8. Tiny SEO free for alt text on the 50 or so photos a month.

Pay for only once it earns it:
- PushLast $3.99 a month once the Sold archive grows past one screen.
- shopUpz $18 a month or Shuttle $19 a month when Etsy and Shopify both sell live and quantity must go to zero on both within minutes.
- Offerly Pro $20 a month if offer-driven sales pass about $2,000 a month (then it is cheaper than 1%).
- Pickeasy $9.99 a month if more than 10 pickup or delivery orders a month need scheduled slots.
- Reservo $29 a month only if "hold it for me" requests are frequent and worth a deposit flow.
- Picture It $19 a month for AR art previews on the Shopify store, if art is a top seller there.

Skip and why:
- Zapiet ($49.99 a month, paid add-ons reported), Intuitive Shipping ($70), ShipperHQ ($75): priced for volume.
- CedCommerce Etsy ($9 plan lists 10 products; drift complaints).
- Wishlists (Swym $29.99, Swish $19 plus usage): one-of-one stock does not restock.
- Size-chart apps for furniture; Loox paid tier; Shogun; Arty 3D; Easy Lookbooks; Price it; the new zero-review badge apps.
- Shopify Marketplace Connect for Etsy: closed to new Etsy connections. Keep it in mind for eBay.

## 4. Gaps and pages that would not load

- WebSearch budget was exhausted after the first round, so roundup discovery stopped early; discovery continued through Shopify App Store search pages only.
- help.shopify.com/en/manual/products/product-media/media-requirements returned HTTP 403 (used the file-uploads page instead, which carries the same limits).
- help.shopify.com/en/manual/online-store/search-and-discovery returned HTTP 403 (used the storefront-search page).
- help.shopify.com/en/manual/fulfillment/shopify-shipping returned HTTP 403; the alternate URL redirected to the shipping-labels page, which does not list carrier weight or size limits. Oversize carrier limits are unverified (U).
- apps.shopify.com/shopify-marketplace-connect, /tinyimg, /advanced-shipping-rules and /magical-make-an-offer are 404; the live handles are /marketplace-connect, /smart-image-optimizer, /vendor-shipping-rules-1 and /make-an-offer.
- Not verified today: Shopify's carrier-calculated shipping plan requirement; theme sold-out badge wording; Shopify Flow's exact inventory trigger; draft-order deposits; Etsy's API terms; the official Shopify Product Reviews shutdown date.
- Rating and review counts are as shown at fetch time; counts in search snippets differed and were ignored.

## 5. Sources

https://apps.shopify.com/judgeme
https://apps.shopify.com/judgeme/reviews?sort_by=newest
https://apps.shopify.com/make-an-offer
https://apps.shopify.com/make-an-offer/reviews?sort_by=newest
https://apps.shopify.com/make-an-offer/reviews?ratings%5B%5D=1&sort_by=newest
https://apps.shopify.com/offerly
https://apps.shopify.com/offerly/reviews?sort_by=newest
https://apps.shopify.com/bargain-make-an-offer
https://apps.shopify.com/price-it-make-an-offer
https://apps.shopify.com/loox
https://apps.shopify.com/loox/reviews?sort_by=newest
https://apps.shopify.com/pagefly
https://apps.shopify.com/shogun
https://apps.shopify.com/intuitive-shipping
https://apps.shopify.com/intuitive-shipping/reviews?sort_by=newest
https://apps.shopify.com/shipping-rates-calculator-plus
https://apps.shopify.com/shipperhq
https://apps.shopify.com/vendor-shipping-rules-1
https://apps.shopify.com/shipping-rates
https://apps.shopify.com/klaviyo-email-marketing
https://apps.shopify.com/shopify-email (redirects to https://apps.shopify.com/shopify-messaging)
https://apps.shopify.com/pinterest
https://apps.shopify.com/google
https://apps.shopify.com/search-and-discovery
https://apps.shopify.com/search-and-discovery/reviews?sort_by=newest
https://apps.shopify.com/shopify-bundles
https://apps.shopify.com/shopify-bundles/reviews?sort_by=newest
https://apps.shopify.com/click-and-collect
https://apps.shopify.com/click-and-collect/reviews?sort_by=newest
https://apps.shopify.com/click-and-collect/reviews?ratings%5B%5D=1&sort_by=newest
https://apps.shopify.com/local-delivery-store-pickup
https://apps.shopify.com/order-delivery-date-time
https://apps.shopify.com/store-pickup-and-delivery-date
https://apps.shopify.com/etsy-marketplace-integration
https://apps.shopify.com/etsy-marketplace-integration/reviews?sort_by=newest
https://apps.shopify.com/etsy-marketplace-integration/reviews?ratings%5B%5D=1&sort_by=newest
https://apps.shopify.com/quicksync-etsy
https://apps.shopify.com/quicksync-etsy/reviews?sort_by=newest
https://apps.shopify.com/quicksync-etsy/reviews?ratings%5B%5D=1&sort_by=newest
https://apps.shopify.com/shopupz-inventory
https://apps.shopify.com/shopupz-inventory/reviews?sort_by=newest
https://apps.shopify.com/shuttle-transfer-from-etsy
https://apps.shopify.com/shuttle-transfer-from-etsy/reviews?sort_by=newest
https://apps.shopify.com/etsy-integration-dpl
https://apps.shopify.com/etsy-integration-dpl/reviews?ratings%5B%5D=1&sort_by=newest
https://apps.shopify.com/litcommerce
https://apps.shopify.com/marketplace-connect
https://apps.shopify.com/marketplace-connect/reviews?sort_by=newest
https://apps.shopify.com/reputon-etsy-reviews
https://apps.shopify.com/etsy-reviews-importer
https://apps.shopify.com/smartstock-app
https://apps.shopify.com/instock-1
https://apps.shopify.com/pushlast
https://apps.shopify.com/lably
https://apps.shopify.com/smart-product-badges
https://apps.shopify.com/instafeed
https://apps.shopify.com/smart-image-optimizer
https://apps.shopify.com/smart-seo
https://apps.shopify.com/shop-the-look-4
https://apps.shopify.com/shop-the-look
https://apps.shopify.com/hotshop-product-image-hotspot
https://apps.shopify.com/lookfy-lookbook-gallery-1
https://apps.shopify.com/swym-relay
https://apps.shopify.com/wishlist-king
https://apps.shopify.com/timesact-discount-pre-order
https://apps.shopify.com/timesact-discount-pre-order/reviews?ratings%5B%5D=1&sort_by=newest
https://apps.shopify.com/layaway-1
https://apps.shopify.com/downpay
https://apps.shopify.com/pos-layaway-stock-reservations
https://apps.shopify.com/kiwi-sizing
https://apps.shopify.com/avada-size-chart
https://apps.shopify.com/essential-icon-badge-banners
https://apps.shopify.com/ultimate-trust-badges
https://apps.shopify.com/faqapp
https://apps.shopify.com/faqs-plus
https://apps.shopify.com/shoppable-video-reels
https://apps.shopify.com/salesup-slider
https://apps.shopify.com/arty-model-viewer
https://apps.shopify.com/picture-it
https://apps.shopify.com/picture-it/reviews?sort_by=newest
https://apps.shopify.com/inbox
https://apps.shopify.com/flow
https://apps.shopify.com/shopify-forms
https://apps.shopify.com/shop
https://apps.shopify.com/search?q=advanced+shipping+rules (and the same page for: tinyimg, wishlist, pre-order, size+chart, trust+badges, faq, product+video, 3d+model, sold+out+badge, layaway, local+delivery, make+an+offer, etsy, shopify+reviews, shop+the+look)
https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods
https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/local-delivery
https://help.shopify.com/en/manual/fulfillment/setup/delivery-methods/pickup-in-store
https://help.shopify.com/en/manual/products/product-media
https://help.shopify.com/en/manual/fulfillment/setup/shipping-profiles
https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads
https://help.shopify.com/en/manual/online-sales-channels/marketplace-connect
https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect/requirements
https://help.shopify.com/en/manual/payments/shop-pay-installments
https://help.shopify.com/en/manual/products/bundles
https://help.shopify.com/en/manual/products/bundles/shopify-bundles
https://help.shopify.com/en/manual/products/bundles/eligibility-and-considerations
https://help.shopify.com/en/manual/inventory-and-locations/setup
https://help.shopify.com/en/manual/inventory-and-locations/setup/selling-when-out-of-stock
https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock
https://help.shopify.com/en/manual/online-store
https://help.shopify.com/en/manual/online-store/storefront-search
https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/shipping-labels
Failed (not readable today): https://help.shopify.com/en/manual/products/product-media/media-requirements ; https://help.shopify.com/en/manual/online-store/search-and-discovery ; https://help.shopify.com/en/manual/fulfillment/shopify-shipping ; https://apps.shopify.com/shopify-marketplace-connect (404) ; https://apps.shopify.com/tinyimg (404) ; https://apps.shopify.com/advanced-shipping-rules (404) ; https://apps.shopify.com/magical-make-an-offer (404)
