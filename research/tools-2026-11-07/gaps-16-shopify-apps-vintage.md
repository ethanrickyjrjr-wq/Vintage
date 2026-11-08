# Gaps check, lane 16: Shopify apps for a one-of-one vintage shop

Date 2026-11-07. Author: research subagent (completeness critic for `16-shopify-apps-vintage.md`).
Question: which Shopify App Store apps, built-in Shopify features and renamed or dead tools did the lane 16 list miss, for a shop where every product is quantity one (sold items stay visible, make-an-offer, fixed shipping classes, local pickup and delivery, oversize shipping, product video, shop-the-room, reviews, Etsy sync)?
Legend: V = vendor page read today (2026-11-07) with the fetch script; U = unverified (snippet, memory, or page would not load).
Method note: the shared WebSearch budget was exhausted before this agent's first query, so every lead came from Shopify App Store category pages (Delivery and pickup, Shipping rates, Pricing quotes, Product reviews, Product display, Inventory, Wishlists) and from app slugs this agent already knew. No 2026 roundup, Product Hunt, Chrome Web Store or GitHub page was read. Prices are quoted from apps.shopify.com listings as Shopify renders them (USD, "/ month" or "/year"). "Newest review" is the first review date shown on the listing, which Shopify sorts by relevance, so the true newest review may be later.

## 0. Bottom line

- The biggest hole is Etsy review import. Reputon Etsy Reviews ($6.99 / month, 5.0 from 347 reviews) and FSL Etsy Reviews Importer ($4.99 / month, 5.0 from 18) pull Hollie's Etsy reviews onto the Shopify site. Neither is on the list, and no listed tool does this except Shuttle's 10-a-month cap.
- The Sold archive has a free baseline the list skipped: Shopify keeps a sold-out product published by default ("customers can't purchase an item until you adjust the inventory levels"), and hiding needs a collection condition, Flow or an app. MB Push Down Hide Out of Stock (free up to 50 products, "Tag sold-out items") and StockIQ (free to install up to 49 products) push sold pieces to the bottom instead of hiding them, cheaper than the listed PushLast at $3.99 / month.
- Reviews: AG Product Reviews (Air Reviews by Avada) is fully free with 4.9 from 3,208 reviews, and the Shop channel now collects 1-to-5-star product reviews on its own and syncs them with partner apps. Shopify's own Product Reviews app is gone ("not currently available on the Shopify App Store").
- Local pickup and delivery scheduling has three newer free apps the list lacks: Pickup : Delivery Date Picker by one8 (launched December 22, 2025, free for 200 orders a month), Delivery Date Picker Kite (launched January 21, 2026, free) and DS Pickup Delivery Date Rates (free, unlimited orders, one location). All three are 5.0 rated with 46 to 78 reviews.
- Oversize pieces: uShip (free, "White-Glove Delivery for Furniture, Antiques, Vintage & Household Goods Sellers", only 2 reviews) and ShipEasy White Glove & LTL (launched June 1, 2026, free to install, pay per freight shipment, 1 review) are the only freight-specific apps found. SMART Shipping Rates & Rules Pro at $19.99 / month adds dimension-based rates under the $50 ceiling and claims to work on the Basic plan without carrier-calculated shipping.
- Auctions fit one-of-one stock and were never searched: Auction Today (free for 1 auction, $9 / month for 15, includes a Make an Offer button, 4.9 from 331) and Tipo Product Auction (free for 1 auction order, $8.90 / month).
- Channels: the seeds named Shopify's free Pinterest and Google channel apps but the list has neither. Pinterest (free to install, 4.1 from 1,706) publishes Product Pins and refreshes the catalog daily; Google & YouTube (free to install, 4.5 from 5,613) syncs to Merchant Center. Facebook & Instagram (3.9 from 5,839) and TikTok (4.8 from 15,996) are also free to install.
- Defunct or renamed: Shopify Product Reviews and Wishlist Hero are unavailable; Trustoo is now "CWILL(Trustoo) Product Reviews"; Wishlist King is now "Swish"; Smart SEO is "Smart SEO AI & Image Optimizer"; Shogun's free plan is "Draft Mode" with "No Page Publishing". No tool on the first agent's list was found dead today.

## 1. Comparison table of missing tools

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Reputon Etsy Reviews | Imports Etsy seller and listing reviews, auto-syncs, widgets | "Standard $6.99 / month or $62.99/year and save 25%" | "Free to install ... Free for development stores" only; 7-day free trial | Shopify app | high: Etsy trust on the new site; 5.0 from 347; newest Oct 23, 2026 | V | https://apps.shopify.com/reputon-etsy-reviews |
| FSL Etsy Reviews Importer (Flagstonelab) | Etsy shop and listing reviews synced daily with buyer photos | "All-inclusive $4.99 / month"; "14-day free trial" | none | Shopify app | medium: cheaper, 5.0 from 18, launched Dec 21, 2023 | V | https://apps.shopify.com/etsy-reviews |
| MB Push Down Hide Out of Stock (merchbees) | Pushes sold-out items to the bottom, tags them, optional hide after set days | "Free Plan ... Up to 50 products & 100 collections"; "Basic Plan $4.99 / month or $47.88/year and save 20%" | yes, 50 products | Shopify app | high: visible Sold archive at the bottom; 4.7 from 156; newest Oct 14, 2026 | V | https://apps.shopify.com/push-down-hide-out-of-stock |
| StockIQ Out Of Stock Manager (EGNITION) | Push down or hide out-of-stock, republish and redirect | "Bronze Free to install ... up to 49 products or up to 99 collections"; "Silver $5.99 / month or $57.48/year and save 20%" | yes, 49 products, paid add-ons | Shopify app | medium-high; "Real-time updates: +$2.99/mo" add-on; 4.8 from 137 | V | https://apps.shopify.com/push-down-out-of-stock-items |
| Nada Hide Out of Stock (Digismoothie) | Hide or push down sold-out products and variants | "Starter $9.99 / month Up to 100 Active or Draft products"; "Trial & Dev Free" | free only for trial and development stores | Shopify app | medium; 4.8 from 26; 60-day money-back | V | https://apps.shopify.com/nada-sort-hide-out-of-stock |
| Selling and hiding out-of-stock products (built in) | Sold product stays published; hide by collection condition, Flow or app | included in plan | built in | Shopify admin | high: zero-cost Sold archive baseline | V | https://help.shopify.com/en/manual/inventory-and-locations/setup/selling-when-out-of-stock |
| AG Product Reviews App & UGC (Air Reviews by Avada) | Product and store reviews, requests, SEO snippets | "Free" (pricing summary; no paid plan shown) | yes, whole app | Shopify app | high alternative to Judge.me; 4.9 from 3,208; newest Nov 4, 2026 | V | https://apps.shopify.com/air-reviews |
| Shop product reviews (built in) | Shop app asks buyers for 1 to 5 stars after delivery; syncs with partner apps | included with the free Shop channel | built in | Shop channel (iOS, Android, web) | high: "they can leave a product review in the Shop app" | V | https://help.shopify.com/en/manual/online-sales-channels/shop/product-reviews |
| CWILL(Trustoo) Product Reviews | Product and store reviews with photo and video | "Free ... Unlimited product and store reviews, Display 6 reviews per product"; "Essential $11.99 / month or $115.10/year" | yes | Shopify app | medium; 4.9 from 1,585 | V | https://apps.shopify.com/sealapps-product-review |
| Junip Product Reviews | Reviews with unlimited requests on free | "Free ... UNLIMITED orders, UNLIMITED review request emails"; "Core $29 / month" | yes | Shopify app | medium; Shop App syndication only on "Growth $79 / month"; 4.8 from 1,176 | V | https://apps.shopify.com/junip |
| Rivyo Product Reviews (Nexfal) | Reviews, CSV import, Etsy import | "Free to install ... 100 Import from Amazon/AliExpress/Etsy"; "Starter $9 / month or $86.40/year" | yes, 100 orders a month | Shopify app | medium; 4.9 from 938 | V | https://apps.shopify.com/rivyo-product-review |
| Reputon Customer Reviews App | Emails asking for Google, Trustpilot, Facebook reviews | "Beginner Free 50 emails / month"; "Lite $9.99 / month $1 per 15 extra emails" | yes | Shopify app | medium: Google reviews for a local SWFL shop; 4.9 from 1,164 | V | https://apps.shopify.com/reputon-store-reviews |
| Pickup : Delivery Date Picker (one8 commerce) | Local delivery and pickup date and time slots | "Free 200 orders/month"; "Basic $4.99 / month or $49.99/year and save 17%" | yes | Shopify app | high; launched Dec 22, 2025; 5.0 from 59; newest Nov 1, 2026 | V | https://apps.shopify.com/delivery-pickup |
| Delivery Date Picker Kite (KiteLane) | Pickup, local delivery and shipping slots, blackout dates | "Free ... Pickup, Local Delivery & Shipping, Date & Time Slot Picker"; "Grow $4.99 / month or $49.99/year" | yes | Shopify app | high; launched Jan 21, 2026; 5.0 from 46 | V | https://apps.shopify.com/kite-pickup-delivery-date |
| DS Pickup Delivery Date Rates (Devesha Solution) | Pickup, delivery, shipping listings with date picker and zip validation | "Free Unlimited orders & 1 location support"; "Beginner $5.99 / month or $65.99/year and save 8%" | yes | Shopify app | high; 5.0 from 78; newest Nov 5, 2026 | V | https://apps.shopify.com/ds-delivery-pickup-shipping |
| EasyRoutes Local Delivery (Roundtrip.ai) | Route planning, driver app, tracking | "Free ... 50 orders/month"; "Standard $39 / month" | yes | Shopify app, iOS and Android driver app | medium: only if Hollie drives deliveries; 4.9 from 290 | V | https://apps.shopify.com/easyroutes |
| Zapiet Rates by Zip Code | Delivery fee by zip | "$14.99 / month or $161.89/year and save 10%" | 14-day trial | Shopify app | low: built-in local delivery zones do this; 4.8 from 149 | V | https://apps.shopify.com/delivery-rates-by-zipcode |
| SMART Shipping Rates & Rules | Rates by dimensions, weight, zip, product; hide and rename rates | "Lite $9.99 / month or $95.88/year and save 20%"; "Pro $19.99 / month"; "Works on Basic plan, no CCS needed" | development stores only | Shopify app | medium-high: dimension rates for oversize under $20; 5.0 from 509; launched June 14, 2024 | V | https://apps.shopify.com/smart-shipping-rates-rules |
| Shipping Rates Rules & Zones (Octolize) | Postcode zones, WHEN-THEN cost rules | "PRO $9.99 / month or $99.99/year and save 17%" | development stores only | Shopify app | medium; 4.9 from 42; launched Sept 19, 2024 | V | https://apps.shopify.com/octolize-postcode-shipping |
| Shipping Rate Power Toy (MZL Solutions) | Reorder and hide rates | "Free ... Reorder rates, Hide rates for PO Boxes"; "Advanced $4.99 / month" | yes | Shopify app | low; 5.0 from 31 | V | https://apps.shopify.com/reorder-rates |
| Parcelify Shipping Rates | Custom rates by tags and collections | "Basic Plan $19.99 / month"; "14-day free trial" | none | Shopify app | low: built-in profiles do this; 4.8 from 179 | V | https://apps.shopify.com/parcelify |
| BS Better Shipping (Atom Yard) | Custom rates and rules | "Starter $29.99 / month 500 orders included"; "Free to try ... Try in Test Mode before going live" | test mode only | Shopify app | low; 4.8 from 88 | V | https://apps.shopify.com/better-shipping |
| Boxify | Dimensional packing and live rates | "Starter Plan $19 / month Up to 250 shipping calculations/month" | none | Shopify app | low; 4.8 from 146 | V | https://apps.shopify.com/boxify |
| uShip | White-glove carrier network for furniture, antiques, vintage; checkout quotes | "Free" (pricing summary) | yes | Shopify app | medium-high for oversize, but 5.0 from only 2 reviews; launched Apr 17, 2024 | V | https://apps.shopify.com/uship |
| ShipEasy White Glove & LTL | Quote and book LTL, curbside, room of choice, white glove; BOL | "Free to install"; "All-in rate per freight shipment, shown before you book." | free to install, pay per shipment via Shopify Billing | Shopify app | medium: launched June 1, 2026, 1 review | V | https://apps.shopify.com/shipeasy |
| Easyship | Discounted labels, tracking, 50 free shipments | "Free 50 Shipments/Month"; "Plus $29 / month or $276/year and save 21%" | yes | Shopify app, web | medium, lane 10 territory; 4.2 from 420; "External charges may be billed by Easyship separately" | V | https://apps.shopify.com/easyship |
| Auction Today (Apex Apps) | Auctions with reserve, buy-now, proxy bids, plus Make an Offer | "FREE 1 Auction"; "STARTER $9 / month 15 Auctions"; "Pro $35 / month Unlimited Auctions" | yes, 1 auction | Shopify app | medium-high for one-of-one pieces; 4.9 from 331; newest Oct 30, 2026 | V | https://apps.shopify.com/auction-today |
| Tipo Product Auction | Auctions with buy-now and minimum price | "FREE 1 auction order"; "SILVER $8.90 / month or $89/year and save 17%" | yes | Shopify app | medium; 4.6 from 109 | V | https://apps.shopify.com/tipo-product-auction |
| Request a Quote & Make Offers (Quoffer, Dreamlify) | Quote requests, price ranges, offer rules | "Free" | yes | Shopify app | low-medium: B2B wording, launched Jan 27, 2026, 4.8 from 10 | V | https://apps.shopify.com/quoffer |
| Downpay: Partial Pay & Deposit | Deposit now, balance later on saved card | "Essentials $29 / month Up to $5,000 in total order value processed with Downpay" | 7-day trial | Shopify app | medium: hold-with-deposit; 5.0 from 96 | V | https://apps.shopify.com/downpay |
| WishlistSuite Smart Wishlist (SimpleSuite) | Wishlist, guest wishlist, save for later, alerts | "Free" | yes | Shopify app | medium; 5.0 from 41; launched Dec 4, 2024 | V | https://apps.shopify.com/wishlist-suite |
| Joy Wishlist & Back in Stock | Wishlist with analytics | "Free" | yes | Shopify app | medium; 5.0 from 26; launched July 21, 2025 | V | https://apps.shopify.com/joy-wishlist |
| Hulk AI Wishlist & Favorites | Wishlist with price-drop and restock emails | "Free 500 wishlist items/month"; "GROWTH $9.90 / month or $99.99/year and save 16%" | yes, with branding | Shopify app | medium; "Remove Branding" only on paid; 4.9 from 141 | V | https://apps.shopify.com/my-wishlist-share-remind |
| Fish Wishlist (Native App Co) | Wishlist with POS, Flow triggers | "Free All Features Up to 100 customers"; "Grow $12 / month or $110/year" | yes | Shopify app | low-medium; 5.0 from 20 | V | https://apps.shopify.com/fish-wishlist |
| Smart Wishlist (Webmarked) | Wishlist | "$4.99/month. Free trial available."; "60-day free trial" | trial only | Shopify app | low; 4.3 from 80; first review shown Aug 22, 2025 | V | https://apps.shopify.com/smart-wishlist |
| Swish Wishlist & Accounts (was Wishlist King) | Wishlists, alerts, customer hub | "Starter $19 / month Plus usage charges 10,000 website sessions/month included" | 30-day trial | Shopify app | low: over budget for non-restocking stock; 5.0 from 290 | V | https://apps.shopify.com/wishlist-king |
| Quinn Shoppable Videos & Reels | Shoppable video and reels widgets | "Free 550 video views/month ... Upload up to 5 videos"; "Starter $9 / month or $90/year and save 17%" | yes | Shopify app | medium; 4.9 from 115; launched July 8, 2024 | V | https://apps.shopify.com/quinn-shoppable-videos |
| Tolstoy Shoppable Video | Shoppable video, AI studio | "Free ... 14-day trial for eligible accounts"; "Starter $19 / month or $180/year and save 21%" | limited | Shopify app | low-medium; 4.6 from 287 | V | https://apps.shopify.com/tolstoy |
| Smart SEO AI & Image Optimizer (Sherpas Design) | Meta tags, alt text, image optimization, structured data | "Free ... Image Optimization (50 images), 20 AI Generations"; "Pro $14.99 / month or $149.90/year and save 17%" | yes | Shopify app | medium-high; 5.0 from 958; seed named, list lacks it | V | https://apps.shopify.com/smart-seo |
| Avada AI SEO Image Optimizer | SEO audit, image optimizer, speed | "Free 100 Image optimizer ... Meta tags"; "Pro $34.95 / month or $348/year and save 17%" | yes | Shopify app | medium; 4.9 from 4,682 | V | https://apps.shopify.com/avada-seo-suite |
| Crush: Speed & Image Optimizer (Space Squirrel) | Image compression and SEO renaming | "Free 25 MB (one-time)"; "Micro $4.99 / month 500 MB of images/month" | yes, 25 MB once | Shopify app | medium; 4.8 from 455 | V | https://apps.shopify.com/crush-pics |
| Shogun Landing Page Builder | Visual page editor | "Draft Mode Free Create Draft Pages - No Page Publishing"; "$39 / month or $372/year and save 21%" | free plan cannot publish | Shopify app | low; seed named; 4.8 from 1,979 | V | https://apps.shopify.com/shogun |
| GemPages Landing Page Builder | Drag-and-drop pages, funnels | "Free to install ... 1 Published page"; "Build $29 / month" | yes, one page | Shopify app | medium; 4.9 from 4,261 | V | https://apps.shopify.com/gempages |
| EComposer Landing Page Builder | Pages and sections | "FREE Live 1 page/section"; "STANDARD $25 / month or $228/year and save 24%" | yes, one page or section | Shopify app | medium; 4.9 from 3,463; newest Nov 3, 2026 | V | https://apps.shopify.com/ecomposer |
| Sellbrite | Lists and syncs to Etsy, eBay, Amazon, Walmart | "Free Up to 30 Orders Monthly 2-hr Inventory Quantity Sync"; "Pro 100 $19 / month or $190/year and save 17%" | yes, 30 orders a month | Shopify app, web | medium: free Etsy sync, 2-hour lag; 3.9 from 120; "External charges may be billed by Sellbrite separately" | V | https://apps.shopify.com/sellbrite |
| Nembol eBay, Amazon, Etsy + | Multichannel listing and sync | "Basic $39 / month or $351/year and save 25% Manage up to 200 products" | 14-day trial | Shopify app | low: belongs to the Crosslist decision; 4.1 from 57 | V | https://apps.shopify.com/nembol |
| Trunk Stock Sync & Bundling | Real-time stock sync across channels | "Essential $35 / month"; "Pro $39 / month" | 14-day trial | Shopify app | low; 4.9 from 409 | V | https://apps.shopify.com/trunk |
| Fera Product Reviews | Reviews with photo and video | "Startup $9 / month Up to 200 Orders/month"; "30-day free trial" | trial only | Shopify app | low where free rivals exist; 4.8 from 2,026 | V | https://apps.shopify.com/fera |
| Stamped Product Reviews & UGC | Reviews | "Reviews $23 / month up to 200 orders a month" | none shown | Shopify app | low; 4.7 from 3,747 | V | https://apps.shopify.com/product-reviews-addon |
| Pinterest (PINTEREST inc) | Product Pins, daily catalog refresh, Pinterest Tag | "Free to install. Additional charges may apply."; "Pinterest charges only when ads are purchased" | yes | Shopify app | high: free organic reach for decor; 4.1 from 1,706 | V | https://apps.shopify.com/pinterest |
| Google & YouTube (Google LLC) | Merchant Center sync, free listings, optional ads | "Free to install"; "When you run a campaign, the ad spend is billed directly to your Google Ads account." | yes | Shopify app | high: free Google Shopping listings; 4.5 from 5,613 | V | https://apps.shopify.com/google |
| Facebook & Instagram (Meta) | Shops and ads on Facebook and Instagram | "Free to install" | yes | Shopify app | medium; 3.9 from 5,839 | V | https://apps.shopify.com/facebook |
| TikTok | TikTok Shop and ads | "Free to install" | yes | Shopify app | low for now; 4.8 from 15,996 | V | https://apps.shopify.com/tiktok |
| Metafields for dimensions (built in) | A Dimensions product metafield shown by the theme editor | included in plan | built in | Shopify admin | high: replaces size-chart apps for furniture | V | https://help.shopify.com/en/manual/custom-data/metafields |

## 2. Notes per tool

**Etsy review import.** Reputon Etsy Reviews: "Import Etsy reviews & testimonials on website. No code required", "New reviews auto update", "Filter out bad reviews". The free tier is for development stores only, so budget $6.99 / month. Merchant summary on the listing: "very easy to install and use, quickly importing and auto-syncing large volumes of Etsy reviews". FSL Etsy Reviews Importer: "Etsy shop reviews, synced daily", "Buyer photos in the reviews", $4.99 / month, 18 reviews. Both import Hollie's own reviews; neither fakes anything. Reputon also sells eBay Reviews and Amazon Reviews importers (seen on the Product reviews category page, not read).

**Sold archive.** Shopify help: "An item is out of stock when inventory is tracked and the inventory level is at zero or below. By default, customers can't purchase an item until you adjust the inventory levels". The product stays published, so the theme shows its own sold-out state. Hiding is the opt-in: "You can use collections to hide out of stock products from your customers ... or use an inventory management app", and "Hide out of stock products using Shopify Flow". So a visible Sold archive costs nothing; an app only adds sorting and a badge. MB Push Down Hide Out of Stock free plan: "Up to 50 products & 100 collections", "Push down sold-out products", "Tag sold-out items" (the tag can drive a theme badge). StockIQ Bronze: "Free to install", "Store with up to 49 products or up to 99 collections", with "Real-time updates: +$2.99/mo" and "Advanced out-of-stock rules: +$3.99/mo" add-ons; without real-time the push-down lags. Nada's free plan is "For trial stores, For development stores" only.

**Reviews.** AG Product Reviews (Air Reviews by Avada) lists one price: "Free". Features: "Automated requests", "Discounts for reviews", "SEO snippets". It shows as "AG Product Reviews App & UGC" with developer "Air Reviews by Avada". CWILL(Trustoo) free: "Display 6 reviews per product" cap, "Google snippet" only on Essential $11.99 / month. Junip free: "UNLIMITED orders", but "Shop App Syndication" sits on Growth $79 / month. Rivyo free: "Collect Reviews from 100 Orders/mo" and "100 Import from Amazon/AliExpress/Etsy"; its loyalty and referral modules are paid add-ons ($29 and $19 a month). Shop product reviews (built in): "After an order is delivered, customers receive a notification ... requesting a review. Customers can leave a rating from 1 to 5 stars", and "If you collect product reviews using a supported third-party app in addition to Shop, then you can also display partner app-collected reviews on Shop." Judge.me (on the list) is such a partner. Fera and Stamped have no free plan and start at $9 and $23 a month.

**Pickup and delivery.** one8 Pickup : Delivery Date Picker free: "200 orders/month", "Locations up to Shopify limit", "Cut-off and Preparation Time", "Display on Cart or Product page"; zip validation needs Basic $4.99. Kite free: "Pickup, Local Delivery & Shipping", "Blackout & Holiday Dates", "Rates by Cart Price & Weight"; "Delivery Zone by ZIP Code or Radius" needs Grow $4.99. DS free: "Unlimited orders & 1 location support", "Zip code validation for local delivery". All three are young (2025 to 2026 launches) with 5.0 ratings on under 80 reviews each. Shopify's built-in local delivery (on the list) still handles the fee and radius; these add the calendar. EasyRoutes is a route planner for a driver, 50 orders a month free, not a storefront widget.

**Shipping rates and oversize.** SMART Shipping Rates & Rules: "Rates by weight, cart total & quantity" on Lite $9.99; "Dimension & volumetric weight rates" on Pro $19.99; "Works on Basic plan, no CCS needed" (CCS is Shopify's carrier-calculated shipping add-on). Octolize: "Custom shipping zones by postcode, state", "WHEN-THEN cost calculation logic", $9.99 / month. uShip: "White-glove checkout quotes for oversized and high-value items", "Auto-create and manage shipments directly from Shopify", price "Free" (uShip earns on the shipment). ShipEasy: "Curbside, Room of Choice, and White Glove Delivery", "Your Bill of Lading is ready the moment you book", "Paid for via Shopify Billing", carriers "AIT Worldwide Alliance Air Freight CEVA Logistics". Note the name collision: apps.shopify.com/shipeasy is this June 2026 freight app, not Logbase's older "Shipeasy" rate calculator. Easyship free: "50 Shipments/Month", "Order Sync, Labels & Tracking"; live checkout rates need Plus $29 / month. Parcelify, Better Shipping, Boxify and Zapiet Rates by Zip Code all cost $14.99 to $29.99 a month for things Shopify shipping profiles and local delivery zones already do for a one-person shop.

**Offers and auctions.** Auction Today: "Reserve Price, Buy Now, Proxy Bidding, Buyers Premium, Popcorn & Penny Auctions" plus "add 'Make an Offer' button so customers ca[n]..." (listing text). Free plan "1 Auction"; Starter $9 / month "15 Auctions". Tipo: free "1 auction order", "Charge per bid", "Checkout Protection". Quoffer: free, "B2C Flexible Pricing: Price selection and automated offer rules", but the copy is B2B wholesale and it launched January 27, 2026 with 10 reviews. Downpay is a deposit tool: "customers pay a deposit and their card is saved. You collect the balance in one payment", $29 / month up to $5,000 processed; a "hold it for me" option but dearer than Reservo on the list.

**Wishlists.** The list only had Swym (paid). Free options: WishlistSuite ("Free", "guest wishlist, Save for Later"), Joy Wishlist ("Free", launched July 21, 2025, by the Joy loyalty developer), Hulk AI Wishlist ("Free 500 wishlist items/month", branding removal paid), Fish Wishlist ("Up to 100 customers" free). Wishlist Hero is gone. Smart Wishlist's first shown review is from August 2025 and it has a 60-day trial but no free plan. Swish (ex Wishlist King) starts at $19 / month "Plus usage charges". For quantity-one stock a wishlist mostly tells Hollie which pieces draw interest; price-drop emails still work.

**Video.** Quinn free: "550 video views/month", "Upload up to 5 videos", "Import from Instagram/TikTok"; Starter $9 / month "5000 video views/month". Tolstoy's free plan is effectively a 14-day trial ("14-day trial for eligible accounts", "Uncapped on-site views for 14 days"). Shopify's own product video upload (on the list) stays the first choice.

**SEO, images, pages.** Smart SEO free: "Image Optimization (50 images)", "20 AI Generations", "Broken Links Check (100 pages)"; Pro $14.99 / month. Avada free: "100 Image optimizer", "Basic Google Structured Data". Crush free: "25 MB (one-time)" then $4.99 / month. Running two SEO apps that both rewrite meta tags is a known conflict; pick one of TinyIMG (on the list), Smart SEO or Avada. Shogun: "Draft Mode Free Create Draft Pages - No Page Publishing", so its free plan is a demo; publishing starts at $39 / month. GemPages free "1 Published page" and EComposer free "Live 1 page/section" match PageFly's free tier.

**Etsy and multichannel sync.** Sellbrite free: "Up to 30 Orders Monthly", "2-hr Inventory Quantity Sync", "Unlimited Channels", but rating 3.9 from 120 and billing outside Shopify. Nembol from $39 / month and Trunk from $35 / month are over the budget line and compete with the Crosslist Gold decision, so they are leads only.

**Channels.** Pinterest: "quickly publish Product Pins, automatically update your product catalog every day, and track performance with the Pinterest Tag". Google & YouTube: "Sync your products, deals, and shipping to Merchant Center". Both are free to install; ads are optional and billed by the ad platform. Facebook & Instagram carries a 3.9 rating from 5,839 reviews; TikTok 4.8 from 15,996.

**Built-in dimensions.** Shopify help: "If you have a furniture store and you want to display detailed measurements, then you might add a Product metafield called Dimensions ... you can display width, height, and depth in a dedicated section of your theme". This removes the need for Kiwi or any size-chart app for furniture.

### 2b. Defunct, renamed or unavailable (with evidence)

- Shopify Product Reviews (a seed): page reads "This app is not currently available on the Shopify App Store. If you have support questions, contact Shopify directly." https://apps.shopify.com/product-reviews. Shop product reviews (built in) and partner apps replace it.
- Wishlist Hero (Revamp): "This app is not currently available on the Shopify App Store. If you have support questions, contact Revamp directly." https://apps.shopify.com/wishlist-hero
- Trustoo: apps.shopify.com/trustoo returns "Oh no! That page doesn't exist." The app lives on as "CWILL(Trustoo) Product Reviews" at https://apps.shopify.com/sealapps-product-review (developer CWILL).
- Wishlist King: the slug wishlist-king now shows "Swish ‑ Wishlist & Accounts" by Swish, from $19 / month plus usage. https://apps.shopify.com/wishlist-king
- Smart SEO (a seed): now titled "Smart SEO AI & Image Optimizer" (Sherpas Design), same slug. https://apps.shopify.com/smart-seo
- Air Reviews: now titled "AG Product Reviews App & UGC", developer "Air Reviews by Avada", same slug. https://apps.shopify.com/air-reviews
- Avada SEO Suite: now "Avada AI SEO Image Optimizer", same slug. https://apps.shopify.com/avada-seo-suite
- Shogun (a seed): still listed, but the free plan is "Draft Mode ... No Page Publishing". https://apps.shopify.com/shogun
- Store Pickup + Delivery (CreativeR) (a seed): slugs store-pickup-delivery and store-pickup-and-delivery both 404 today, and it is not on the first page of the Delivery and pickup category. Status unknown. U.
- Shipeasy (Logbase rate calculator, a common roundup name): the slug shipeasy is now "ShipEasy ‑ White Glove & LTL", a different developer launched June 1, 2026. Logbase's app was not located. U on Logbase.
- Fast Bundle and Vimotia: guessed slugs 404; not located, U. Not needed given Shopify Bundles and Lookfy on the list.
- No tool on the first agent's list was found defunct, acquired or renamed today beyond what that agent already recorded (Shopify Email to Shopify Messaging; Shipping Rates Calculator Plus to CBB; Tiny SEO to TinyIMG).

## 3. Recommendation for Hollie

Free first, install today:
- Turn on the Shop channel's product reviews (built in) and pick one review app: AG Product Reviews (free, 4.9 from 3,208) or Judge.me Forever Free from the list. Not both.
- MB Push Down Hide Out of Stock, free plan (50 products). Use "Tag sold-out items" so the theme badge reads Sold and sold pieces sink to the bottom but stay visible. If the catalog passes 50 live products, Basic is $4.99 / month.
- Pickup : Delivery Date Picker by one8 (free, 200 orders a month) for Fort Myers and Naples delivery and pickup slots, on top of Shopify's built-in local delivery zones and fees.
- Pinterest app and Google & YouTube app (both free to install, no ads). Pinterest's Product Pins suit lamps, art and barware.
- A Dimensions metafield (built in) for every furniture piece instead of a size-chart app.

Pay for it once it earns it:
- Reputon Etsy Reviews at $6.99 / month as soon as the Etsy shop has reviews worth showing on the Shopify site. FSL at $4.99 / month if 18 reviews is enough trust in the vendor.
- SMART Shipping Rates & Rules Pro at $19.99 / month only if shipping profiles cannot express an oversize class; it claims dimension-based rates without the carrier-calculated add-on.
- Auction Today Starter at $9 / month when a signed piece or a chandelier deserves a reserve-price auction; the free plan allows one auction to test.
- Quinn Starter at $9 / month only if the free 550 views a month run out.

Skip, and why:
- Shogun: the free plan cannot publish; PageFly, GemPages and EComposer each publish one page free.
- Nembol, Trunk, Sellbrite paid tiers: they duplicate the Crosslist Gold trial and Shuttle's free Etsy transfer; Sellbrite free (30 orders) is a fallback only.
- Swish, Smart Wishlist, Swym: paid wishlists for stock that never restocks; WishlistSuite or Joy Wishlist are free if a wishlist is wanted at all.
- Zapiet Rates by Zip Code, Parcelify, Better Shipping, Boxify: built-in shipping profiles and local delivery zones cover a one-person shop.
- Fera, Stamped, Downpay, Tolstoy: paid where a free equivalent exists or the trial is dressed as a free plan.
- uShip and ShipEasy: keep as leads for white-glove furniture freight; 2 and 1 reviews are too few to trust with a $900 chandelier today.

## 4. Gaps and pages that would not load

- WebSearch: the shared budget was already spent when this agent started, so no 2026 roundups, Product Hunt, Chrome Web Store or GitHub pages were read. The "appears in two independent roundups" test could not be applied; every candidate came from Shopify App Store category pages and listings.
- help.shopify.com/en/manual/online-sales-channels/shop/shop-reviews (a guessed URL) returned HTTP 403; the real page is /shop/product-reviews and was read.
- apps.shopify.com/categories redirected to the App Store home page; subcategory pages were reached by their full slugs.
- 404 (page does not exist): apps.shopify.com/nada, /advanced-wishlist, /trustoo, /fast-bundle, /vimotia, /wishlistsuite, /store-pickup-delivery, /store-pickup-and-delivery.
- Unavailable listings: apps.shopify.com/wishlist-hero and /product-reviews (see 2b).
- Not located: Logbase Shipeasy, CreativeR Store Pickup + Delivery, Amai Local Pickup & Delivery, Hulk Advanced Wishlist's current slug (Hulk AI Wishlist was read instead).
- Review dates are the first dates on each listing page as Shopify orders them; "newest" dates in the table may understate recency. Only the first page of each category was read, so apps ranked lower were not seen.
- Etsy.com and eBay pages were not needed for this lane and were not fetched.

## 5. Sources (every URL fetched today, 2026-11-07)

https://apps.shopify.com/pinterest
https://apps.shopify.com/google
https://apps.shopify.com/smart-seo
https://apps.shopify.com/shogun
https://apps.shopify.com/nada (404)
https://apps.shopify.com/wishlist-hero (unavailable)
https://apps.shopify.com/advanced-wishlist (404)
https://apps.shopify.com/smart-wishlist
https://apps.shopify.com/air-reviews
https://apps.shopify.com/fera
https://apps.shopify.com/product-reviews (unavailable)
https://apps.shopify.com/downpay
https://apps.shopify.com/shipeasy
https://apps.shopify.com/store-pickup-delivery (404)
https://apps.shopify.com/sellbrite
https://apps.shopify.com/gempages
https://apps.shopify.com/etsy-reviews
https://apps.shopify.com/categories (redirected to https://apps.shopify.com/)
https://help.shopify.com/en/manual/online-sales-channels/shop/shop-reviews (403)
https://help.shopify.com/en/manual/online-sales-channels/shop
https://apps.shopify.com/product-reviews-addon
https://apps.shopify.com/trustoo (404)
https://apps.shopify.com/wishlist-king
https://apps.shopify.com/parcelify
https://apps.shopify.com/better-shipping
https://apps.shopify.com/easyroutes
https://apps.shopify.com/nembol
https://apps.shopify.com/trunk
https://apps.shopify.com/tolstoy
https://apps.shopify.com/fast-bundle (404)
https://apps.shopify.com/ecomposer
https://apps.shopify.com/avada-seo-suite
https://apps.shopify.com/facebook
https://apps.shopify.com/tiktok
https://apps.shopify.com/crush-pics
https://apps.shopify.com/uship
https://apps.shopify.com/boxify
https://apps.shopify.com/vimotia (404)
https://apps.shopify.com/joy-wishlist
https://apps.shopify.com/wishlistsuite (404)
https://apps.shopify.com/shop
https://help.shopify.com/en/manual/custom-data/metafields
https://help.shopify.com/en/manual/products/inventory/getting-started-with-inventory (redirected to https://help.shopify.com/en/manual/inventory-and-locations/setup)
https://apps.shopify.com/categories/store-design
https://apps.shopify.com/categories/selling-products
https://apps.shopify.com/categories/orders-and-shipping
https://apps.shopify.com/categories/marketing-and-conversion
https://apps.shopify.com/categories/store-design-product-display
https://apps.shopify.com/categories/orders-and-shipping-shipping-solutions
https://apps.shopify.com/categories/selling-products-pricing
https://apps.shopify.com/categories/marketing-and-conversion-social-trust
https://apps.shopify.com/categories/store-design-search-and-navigation
https://apps.shopify.com/categories/orders-and-shipping-shipping-solutions-delivery-and-pickup/all
https://apps.shopify.com/categories/selling-products-pricing-pricing-quotes/all
https://apps.shopify.com/categories/orders-and-shipping-shipping-solutions-shipping-rates/all
https://apps.shopify.com/categories/marketing-and-conversion-social-trust-product-reviews/all
https://apps.shopify.com/categories/orders-and-shipping-inventory
https://apps.shopify.com/categories/marketing-and-conversion-customer-loyalty-wishlists/all
https://apps.shopify.com/nada-sort-hide-out-of-stock
https://apps.shopify.com/push-down-out-of-stock-items
https://apps.shopify.com/push-down-hide-out-of-stock
https://apps.shopify.com/quoffer
https://apps.shopify.com/auction-today
https://apps.shopify.com/tipo-product-auction
https://apps.shopify.com/delivery-pickup
https://apps.shopify.com/ds-delivery-pickup-shipping
https://apps.shopify.com/delivery-rates-by-zipcode
https://apps.shopify.com/smart-shipping-rates-rules
https://apps.shopify.com/octolize-postcode-shipping
https://apps.shopify.com/easyship
https://apps.shopify.com/reputon-etsy-reviews
https://apps.shopify.com/reputon-store-reviews
https://apps.shopify.com/sealapps-product-review
https://apps.shopify.com/junip
https://apps.shopify.com/rivyo-product-review
https://apps.shopify.com/quinn-shoppable-videos
https://apps.shopify.com/wishlist-suite
https://apps.shopify.com/my-wishlist-share-remind
https://apps.shopify.com/fish-wishlist
https://apps.shopify.com/store-pickup-and-delivery (404)
https://apps.shopify.com/reorder-rates
https://apps.shopify.com/kite-pickup-delivery-date
https://help.shopify.com/en/manual/online-sales-channels/shop/product-reviews
https://help.shopify.com/en/manual/inventory-and-locations/setup
https://help.shopify.com/en/manual/inventory-and-locations/setup/selling-when-out-of-stock
https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock
