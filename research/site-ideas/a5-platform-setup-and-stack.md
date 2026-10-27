# a5: Platform setup and stack for one-of-one vintage (Etsy + Shopify + own hand-built site)

Agent a5, accessed 2026-10-27. Raw pages: `research/site-ideas/raw/a5-*.md` (plus a few `a5-*-raw.html`).
Labels used: **verified** = read on a page fetched this session; **UNVERIFIED** = not read this session; **inferred** = my deduction from verified text, not stated by the vendor. "X verified, Y need review" marks a conflict.

## TL;DR

1. **Etsy "vintage" = 20+ years old.** Today (2026-10-27) that means made before roughly late 2006. 70s to 90s is fine; Y2K-era and "vintage-style" new goods are not sellable on Etsy, and neither are new disco balls for sale (Etsy bans reselling). The inventory catalog has one 2016-17 item (C7, "Southern Peach 2016-17", already tagged low value) that cannot go on Etsy.
2. **Ricky's real decision is which storefront customers land on.** If it is the hand-built site, a $220 to $500 Shopify theme is wasted money. Shopify then does checkout and inventory, and the site embeds it with Storefront Web Components (plain HTML, no framework, no token needed for basics).
3. **Quantity-1 on Shopify needs no paid app.** Native collection conditions ("Inventory stock is greater than 0") hide sold pieces from collections; the reverse condition gives a Sold archive. Shopify Flow can unpublish instead. Blink ($0 to $3.99) is optional.
4. **Crosslist Gold $39.99/month is still the only tool whose own docs state cloud auto-delist for Etsy + eBay + Shopify.** List Perfectly auto-delist starts at $99+. Vendoo's delist list omits Shopify. Nifty's pricing page never mentions Shopify. No conflict with `docs/dashboard-design.md`, two wording drifts flagged below.
5. **Recommendation:** Etsy first for discovery and the 20-year rule, own site as the showpiece reading live stock from Shopify, free theme on Shopify for now, Crosslist Gold after a one-item delist test. Full list and "Ricky must check" at the bottom.

---

## 1. Etsy: rules that matter to a reseller

- Homepage: https://www.etsy.com/
- **Access note.** `etsy.com` legal and seller-handbook pages are walled for crawl4ai (4-byte output) and for WebFetch (HTTP 403). I read them through Wayback snapshots, stated with each quote. `help.etsy.com` articles loaded live.

**Vintage definition (verified, Wayback snapshot 2025-07-09 of the live policy; page footer says "Last updated on Nov 16, 2018")**
- Page: https://www.etsy.com/legal/policy/vintage-items-on-etsy/242665563649 (read at https://web.archive.org/web/20250709223039/https://www.etsy.com/legal/policy/vintage-items-on-etsy/242665563649)
- Quote: "For an item to be considered vintage on Etsy, it must be at least **20 years old**."
- Etsy "may ask" where items come from, how age was determined, designer and collection year, and for clothing the fabric, brand label, care label and zipper/button material. "we may ask for photo documentation of key vintage indicators."
- Quote, cannot verify an item as vintage: "The item was purchased at an estate sale or yard sale." Also "Another vintage seller is selling the same item" and "handed down from a relative who has been deceased for over twenty years". **Watch out:** Ricky sources at estate sales, so every listing needs its own age evidence (maker's mark, label, tag photo), not "bought at an estate sale".
- A 2026-08-09 Wayback snapshot of the same page came back empty, so I cannot prove the text is unchanged this month. Corroboration, live: Etsy Help https://help.etsy.com/hc/en-us/articles/23948763872151-Does-Etsy-Allow-Drop-Shipping-or-Reselling (accessed 2026-10-27): "Reselling is not allowed on Etsy except for the following items that are handpicked or sourced by sellers: **Vintage items**: ... unique, handpicked items that are over 20 years old." Wording "at least 20" vs "over 20" differs by a hair; X verified (20 years), Y need review (exact boundary at year 20).
- Etsy Creativity Standards (Wayback snapshot 2026-10-25, https://web.archive.org/web/20261025165918/https://www.etsy.com/legal/creativity): vintage = "Items that are 20+ years old, that the seller personally curated or collected." Does not qualify: "Resold commercially available items that are newer than 20 years old, even if the item is designed to appear vintage". And: "Listings for items 'handpicked by a seller' must use photo or video content of the real, final product."

**Reselling (verified, Wayback snapshot 2026-10-27 of https://www.etsy.com/legal/sellers/)**
- Quote: "Dropshipping and reselling are not allowed on Etsy, except in the specific cases outlined in this Help article."
- Quote: sellers must "Provide honest, accurate information to Etsy and in your About section." That backs the house rule of never implying an operating public store.

**What this means for Holliewood and Vine (partly inferred)**
- 70s, 80s, 90s fashion: eligible. A piece dated after about 2006: not eligible on Etsy, list it on Shopify or the own site only.
- Disco balls as free gifts: not a listing, so the reselling ban does not obviously apply (inferred). Listing new disco balls for sale on Etsy would be reselling. Whether Etsy has a rule about free gifts in the box: UNVERIFIED, Ricky should ask Etsy support.
- Real-photo rule: the first Etsy photo must show the actual item. Cutouts and styled composites belong on the own site, not as Etsy image 1 (inferred from the quote above).

## 2. Etsy: how top vintage shops set up the shop

Sources:
- Etsy Help (live 2026-10-27): https://help.etsy.com/hc/en-us/articles/115015663247-How-to-Customize-Your-Shop-s-Appearance , https://help.etsy.com/hc/en-us/articles/115015663347-Requirements-and-Best-Practices-for-Images-in-Your-Etsy-Shop , https://help.etsy.com/hc/en-us/articles/360000343708-How-to-Add-a-Shop-Announcement-and-Shop-Title , https://help.etsy.com/hc/en-us/articles/115014372467-How-to-Set-Up-Your-Shop-Policies
- Two high-volume vintage shops via Wayback (their live pages are walled): GuermantesVintage (snapshot 2025-06-08) and jessjamesjake (snapshot 2025-02-24). Both are **clothing** shops. I found no top-rated lighting/barware/ephemera shop in budget, so this is a gap, not a finding.

**Banner (verified, live Help).** "Mini Banner: minimum 1200 x 160 pixels. Big Banner: minimum 1200 x 300." Recommended 1600 x 213 (mini) and 1600 x 400 (big); logo 500 x 500; profile photo 400 x 400; carousel and collage banners are "available to Etsy Plus subscribers". "If you do not want a banner ... your logo will be the most prominent branding."

**Announcement (verified).** "appears under the listings on your shop homepage"; "Keep your announcement short and sweet." Longer detail goes in About, policies, listing descriptions.
- Guermantes announcement is only: "INSTAGRAM: @guermantes.vintage www.guermantesvintage.com". jessjamesjake: "authentic vintage fashion • 1920s to 1990s • beautiful vintage clothing in all sizes".
- Steal this: era range plus the own-site link in the announcement. Watch out: whether Etsy permits an off-site link in the announcement for a new shop is UNVERIFIED; these two are established shops and the pattern is observed, not sanctioned.

**About (verified).** Guermantes (2,194 sales, 5 of 5 stars on 633 reviews, "Star Seller", 17,562 admirers, on Etsy since 2010) uses About as a brand essay: a Proust-based philosophy and a stated focus ("my clear focus is on my stock of exceptional 1920s and 1930s era vintage"), a slideshow, and links to its own site, Facebook and Instagram. Etsy's older vintage tips (handbook article, Wayback snapshot **2023-05-20**, so dated) say to add photos from "vintage-shopping adventures or your workspace". Steal this: About is the brand story, so the dimensional-lettering voice belongs here.

**Policies (verified).** Guermantes: "All sales are final. Guermantes Vintage does not accept returns or exchanges", "all items are vintage, used, and sold AS IS", firm prices, layaway, a sizing FAQ that tells buyers to compare measurements to a garment they own. Review evidence that honesty sells: "did not see the faint stain the seller was so honest about". Etsy rule (live Help): non-EU sellers "must set a return policy whenever you edit or create a new listing for a physical item, even if it is to let buyers know you do not accept returns", and "Policies can't be added or edited from the Etsy Seller app. Please use the mobile web or desktop versions". That last point matters for the phone-first listing flow in `docs/dashboard-handoff.md` (open question 11, shop defaults): policies must be created once on desktop before the API drafts reference them.

**Listing photos (verified, live Help).** At least 2000 px both ways recommended; first photo "at least 635 pixels to avoid showing up lower in searches"; first photo "should be horizontal (landscape) or square"; the first photo "dictates the shape of the photos that follow"; first photo should be "the clearest, most realistic representation of the item". Files over 1 MB "may not finish uploading". Etsy's vintage tips (2023 snapshot): "include five unique shots", a photo "of the tag or brand mark", and "If your vintage collection is more fun and eclectic, photograph your items with a few props and colorful backdrop." Maximum photos per listing: UNVERIFIED.
- Inferred photo order for this stock: 1 hero (real, landscape or square), 2 back/side, 3 mark/label/tag (Etsy's age-evidence ask), 4 flaw close-up, 5 scale shot, 6 styled in the room.

**Titles and tags.** Etsy's own title/keyword handbook pages were walled live and on Wayback, so the **140-character title limit and the 13-tag limit are UNVERIFIED this session**. Observed practice:
- Guermantes: `1940s Dress / 40s Red Knit Skirt and Sweater Set / Kimberly Knitwear` (long decade, short decade, category, descriptors, maker, slash-separated). Rare pieces get a leading "Rare" and a caps colour word, e.g. `Rare 1940s Pant Set / 40s Color Block Gabardine Slacks and Button Front Blouse / Two Piece Outfit / PINK Watermelon`.
- jessjamesjake: bullet-separated `Ruffle Dress • 1970s Day Dress • Ginkgo Dress • 70s Dress • ...` and short ones like `90s Corset Dress - Peplum Dress`. It also lists non-clothing: `Name Puzzles: Alexander and Charles - vintage 1970s letter puzzles`.
- Etsy's vintage tips (2023 snapshot): use "accurate terms that describe the time period or style" and "only use tags that are applicable"; condition tiers such as excellent and great vintage condition, explained in one sentence.
- Steal this: era in both forms ("1970s" and "70s"), category, maker, then a colour or standout word. Shop sections by category with counts (DRESSES 118, OBJECTS / ACCESSORIES 14, etc.) is how Guermantes organises 214 items.

## 3. Shopify themes (Shopify Theme Store, accessed 2026-10-27)

Homepage: https://themes.shopify.com/ . Pages read: each theme page below.
Caveat on fit: I never saw a rendered demo. "Suits a maximalist shop" is **inferred from the theme's own marketing copy and preset names**. The percentage beside each price is the page's positive-review share.

| Theme | Price | Reviews | Evidence / what it is | Demo URL (taken from the theme-store page HTML; I did not open the demo sites) |
|---|---|---|---|---|
| Impact (Maestrooo) | $400 USD | 85% | "Bold design made for entertainment and audio brands." "gradients, big headings ... subtle animations"; "over 35 sections". Presets: Impact, Cocoon, Balance. | https://impact-theme-sound.myshopify.com/ (found in the Impact page HTML; which preset it shows need review) |
| Broadcast (Presidio) | $420 USD | 95%, 284 reviews | "30+ fully customizable sections"; product badges, quick view, product videos, swatch filters. Presets: Broadcast, Relay, Airwave, Motif, Stellar. | https://broadcast-theme-main.myshopify.com |
| Prestige (Maestrooo) | $400 USD | 91%, 874 reviews | Luxury-leaning. Presets: Prestige, Couture, Vogue, Strass, Signature. | https://prestige-theme-allure.myshopify.com/ |
| Focal (Maestrooo) | $320 USD | not captured | Presets: Focal, Ivory, Quartz, Sapphire. | https://focal-theme-carbon.myshopify.com/ |
| Expression (Clean Canvas) | $220 USD | 90%, 71 reviews | "customisable sidebar, mini collection cards and editorial-style image & text columns". Presets: Expression, Oxford, Ocean, Innovate. | UNVERIFIED (two different `myshopify.com` URLs in the HTML, one looks like a merchant store) |
| Dawn, Sense (Shopify) | Free | 36% (Dawn, 291 reviews); 36% (Sense, 74 reviews) | Shopify's own. | theme-store page only |
| Horizon family (Vessel, Atelier, Pitch, Tinker, Heritage, Dwell, Horizon, Ritual, Savor, Fabric) | Free | 24% to 50% | "A new collection of free themes by Shopify." | https://themes.shopify.com/collections/horizon-themes |

- **Discrepancy / signal:** every free Shopify theme shows 24% to 50% positive reviews; the paid ones above show 85% to 95%+. X verified (numbers on the pages), Y need review (what drives the low free scores; I did not read the reviews).
- "Small catalogs" filter (https://themes.shopify.com/themes?catalog-size%5B%5D=few) is the right filter for a ~40-item quantity-1 shop. It lists, with price and review share: Editions $100 (91%), Bijou $100 (91%), Sable $100 (91%), Grip $100 (94%), Optimum $160 (98%), Story $280 (95%), Bloop $380 (100%), Adelle $380 (100%), Hehku $500 (100%). Not individually opened.
- **Settings a quantity-1 vintage theme needs (inferred checklist; I cannot open a theme editor):** sold badge on cards and product page; hide or default the quantity selector; no "low stock" countdown; large multi-image gallery with zoom and video; announcement bar; per-product notes block for condition and measurements; sold items either hidden from collections or shown greyed in an archive collection.
- **My opinion:** if customers land on the hand-built site, take a free theme and spend $0 on this. If Shopify's own storefront will be a real front door, Impact or Broadcast are the only ones whose copy points at bold, theatrical layouts, and Ricky should open the three demos before paying $400 to $420.

## 4. Shopify mechanisms for quantity-1 stock

**Hide sold pieces, native (verified, https://help.shopify.com/en/manual/inventory-and-locations/setup/hide-out-of-stock , accessed 2026-10-27).** Turn on inventory tracking, then for each collection add "**Inventory stock** is greater than **0**" with "**Match all conditions**". "Any out of stock products display in your collections again after you receive inventory." The default Catalog collection (`/collections/all`) needs its own override collection with the same condition. **Shopify Flow:** a pre-built "Publish and unpublish products based on inventory level" template, or the "Product variant inventory quantity changed" trigger plus the "Unpublish product" action.
- Collection-condition operators for inventory (verified, https://help.shopify.com/en/manual/products/collections/conditions): is equal to, is not equal to, is greater than, is less than. A Sold archive collection ("Inventory stock is less than 1") is **inferred** from those operators, not stated by Shopify. Conditions apply only to automatically matched products; "If you manually add products to a collection, then a condition doesn't remove them".
- **Sold archive vs unpublish (inferred):** collection filtering removes the product from collections, so its page URL should still resolve (keeps Google and the "museum of sold things" idea). Flow's Unpublish removes it from the channel. Test one sold item before relying on this.
- Whether Flow is included on the Basic plan: UNVERIFIED.

**Blink | Hide out of stock (verified, https://apps.shopify.com/auto-hide-unhide-products).** Free plan: "Manage upto 100 products", manual run. Basic $3.99/month ($38/year), up to 10,000 products, "Automatically hide & publish products", 7-day free trial. Pro $8.99, Advance $13.99. Rating 4.7 (73). Feature text: "Configurable to hide from search, collections but accessible via direct url". Opinion: skip unless the native conditions prove annoying.

**Bulk import (verified, https://help.shopify.com/en/manual/products/import-export/import-products).** CSV import; "Your product CSV can't exceed 15 MB"; option "Overwrite products with matching handles". Fits the Drive-to-Shopify catalog load.

**Etsy/eBay sync apps (verified).**
- Shopify Marketplace Connect (https://help.shopify.com/en/manual/online-sales-channels/marketplaces/marketplace-connect): marketplaces listed are Amazon, Target Plus, Walmart, eBay. "New connections to Etsy can't be made at this time." Shopify's pricing page also shows "50 synced marketplace orders per month: Free" on all plans.
- LitCommerce (https://apps.shopify.com/litcommerce): "$29/month. Free trial available.", rating 4.8 (978); "Automated sync listings, orders, and inventory in near real-time to prevent overselling." **X verified (listing says near real-time), Y need review:** `research/dashboard/03-existing-tools.md` quotes 15-minute sync; that figure is not on today's app listing.
- Dashboard `Shopify as hub: no` stands: Marketplace Connect cannot add Etsy (verified today), and nothing I read proves quantity-1 delist latency for sync apps.

**Shopify plan prices (verified, https://www.shopify.com/pricing).** Basic $39/month or $29/month billed yearly; Grow $105 / $89; Advanced $399 / $359; Plus from $2,300. Basic online card rate 2.9% + 30 cents; "Get your first 3 months free" banner; consistent with the dashboard doc's "Basic $39, or $29 yearly".

## 5. Cross-listing tools (live pricing pages, accessed 2026-10-27)

| Tool | Plans (verified) | Shopify / delist coverage (verified) |
|---|---|---|
| **Crosslist** https://crosslist.com/pricing | Bronze $29.99/mo (200 new listings/mo), Silver $34.99 (500), **Gold $39.99 (1000)**, Diamond $44.99 (unlimited); AI add-on +$4.99/month. Billing toggle: Monthly, Quarterly "-10%", Yearly "2 months free". "20 free listings" and "3-day money-back guarantee". | Docs https://docs.crosslist.com/knowledge-base/sales/autodelist : "To use this feature you need the Gold or Diamond subscription." eBay, Etsy, Shopify all "Cloud-based" detection. "Sales are usually detected within **15 minutes**." Warning: "Crosslist only detects sales for **linked listings**". Shopify FAQ https://docs.crosslist.com/knowledge-base/marketplaces/shopify/shopify-faq : takes "the **first variant**", "does not support multiple variants", "does not support Shopify metadata". |
| **List Perfectly** https://listperfectly.com/pricing | Simple $29/mo, Business $49, Pro $69, Pro Plus $99+. | Feature table: Shopify Integration from Pro; Mark Sold from Pro; **Auto Delist only on Pro Plus**; Import Existing Listings from Business. |
| **Vendoo** https://www.vendoo.co/pricing | Starter $14.99/mo ($12.49 billed yearly), Growth $29.99 ($24.99), Pro $59.99 ($49.99), Enterprise contact sales. Starter lists "Unlimited Items" and "Sale Detection and AutoDelisting". | https://www.vendoo.co/cross-listing-app : auto-delisting "Available for Poshmark, eBay, Mercari, Depop, Whatnot, and Etsy" (no Shopify), while the marketplace list includes Shopify. Trial length not re-read today. |
| **Nifty** https://nifty.ai/pricing | Crosslisting Plus $39.99/mo ($35.99 yearly), Crosslisting Pro $59.99, Automation $39.99 ($35.99 yearly; $25/$22 Poshmark or eBay only), Bundle Plus $69.99 ($62.99 yearly); "7-day free trial". Bundle Pro $89.99 was **not seen today: UNVERIFIED**. | Pricing page has zero Shopify mentions; automation is Poshmark, eBay, Mercari, Depop. Poor fit. |
| FLUF Connect, Sellbrite, SellerAider | **UNVERIFIED today.** Not re-fetched; `research/dashboard/03-existing-tools.md` has FLUF at Starter $9 with 60 to 90 minute checks. | |

**Dashboard conflicts (X verified, Y need review)**
- Crosslist detection wording: dashboard says sales "can take up to 15 minutes to be detected"; today's doc says "usually detected within 15 minutes". Same number, softer guarantee. Matters for a quantity-1 double-sale window.
- LitCommerce 15 minutes vs "near real-time" (section 4 above).
- Crosslist importing an existing Etsy listing (the dashboard's T6b flow, "bulk import your existing inventory from any marketplace"): UNVERIFIED this session. I only confirmed Shopify import (first variant). Ricky's smoke test 9 should prove the Etsy import leg.
- **Consistent with the dashboard, re-verified:** Gold or Diamond needed for auto-delist; Gold $39.99; List Perfectly auto-delist only at $99+; Vendoo delist list omits Shopify; Marketplace Connect cannot add Etsy; Shopify Basic $39 or $29 yearly; Crosslist's Shopify import takes the first variant only.
- **New to the dashboard docs:** Crosslist quarterly billing (-10%) and yearly "2 months free"; Crosslist has no Shopify metadata support, so any era/condition badge cannot ride Crosslist as a metafield (it must live in the title or description).

## 6. Own hand-built site next to Shopify (shopify.dev, accessed 2026-10-27)

Homepage: https://shopify.dev/ . Pages read: https://shopify.dev/docs/storefronts/headless/overview , .../headless/bring-your-own-stack , .../headless/building-with-the-storefront-api , https://shopify.dev/docs/api/storefront-web-components and its getting-started page, https://shopify.dev/docs/storefronts/themes/architecture/sections , https://help.shopify.com/en/manual/online-sales-channels/buy-button .

| Option | What Shopify says (verified) | Fit for a no-framework HTML/CSS/JS site |
|---|---|---|
| **Storefront Web Components** | "bring Shopify-powered commerce capabilities to any website. Display products, showcase collections, and offer a checkout, all with a few lines of embedded HTML." Uses `<shopify-store>` and `<shopify-context>`; `shopify-cart` uses a native HTML `<dialog>`. "You don't need an access token ... However, if you want to display the inventory count or any custom data about a product, then you need" a public token from the Headless channel. "Buy now" "redirects the customer to the checkout page." | **Best fit.** No build step. The exact script tag was not in the crawled text, so I am not quoting one; copy it from the getting-started page. |
| **Storefront API directly** | "serves products, collections, search, and the cart, and hands customers off to checkout." Tokenless: products, collections, search, pages and blogs, cart read/write, "query complexity limit of 1,000". Needs a token: product tags, metaobjects and metafields, menu, customers. Public token for client side, private token for server side. | Good if the site needs custom card layouts and sold/available logic; a few `fetch` calls. Tags need the public token, so era and condition tags work only with the Headless-channel token. |
| **Buy Button JS / Buy Button channel** | Headless overview lists "Storefront Web Components or Buy Button JS" for "buy buttons to a site that you already have". Help: Buy Buttons "on your non-Shopify website or blog"; the channel "is included in all Shopify subscription plans". Caution there: Shopify "does not recommend the use of Buy Buttons on your Shopify online store" (that is about on-store use, not an external site). | Works but older; Web Components is the newer path (inferred from the order of the overview table). |
| **Full headless (Hydrogen or bring-your-own)** | "A headless storefront costs more to build and run than a theme ... has developers to maintain the storefront after launch." | Overkill for one person. Skip. |
| **Custom section inside a Shopify theme** | "Sections are Liquid files that allow you to create reusable modules of content that can be customized by merchants." | Possible way to put a hero or the mirror-ball inside Shopify's own pages, but Liquid plus theme constraints; the WebGL ball and music would need to fit theme assets (inferred). Only worth it if Shopify's domain becomes the front door. |

**Concrete risks for this repo**
- **Hosting:** the memory note says the live site is on ChatGPT Sites, published by Ricky through Codex. Whether that host allows an external `<script>` from Shopify's CDN and calls to `*.myshopify.com` is **UNVERIFIED** and decides whether Web Components work at all. If it does not, call the Storefront API with `fetch` from the page, which still needs the same network permissions.
- **Stock drift:** `site/demo-products.js` and `catalog-data.js` are static data files (I read only the head of `demo-products.js`). On a quantity-1 shop they will show sold items as available unless the site reads availability from Shopify. Present Shopify as the stock source the site reads, not as the listing hub, so this does not contradict the dashboard's "Shopify as hub: no".
- **Checkout leaves the site:** both Web Components and the API hand off to Shopify checkout. The room experience stops at the cart.

## 7. Recommendations for Holliewood and Vine (ranked)

1. **Decide the front door first** (Ricky's call). My pick: the hand-built site is the showpiece and reads live stock from Shopify; Etsy is the discovery channel. Everything below follows from that.
2. **Etsy: list only 20+ year items, with age evidence in photos.** Hero real photo, label/mark photo, flaw photo. Create return policy, cancellations and shipping profile once on desktop. Put era range and own-site link in the announcement only after checking it is allowed.
3. **Shopify: free theme now, native collection conditions for sold handling, skip Blink.** Open the Impact, Broadcast and Prestige demos once; buy only if Shopify's storefront will be public. Plan: Basic, $29/month billed yearly or $39 monthly.
4. **Own site: Storefront Web Components for cards, cart and checkout hand-off.** Get a public token via the Headless channel to show inventory count. Test script loading on the ChatGPT Sites host before building on it.
5. **Cross-listing: Crosslist Gold ($39.99) after the dashboard's one-item delist test.** Do not buy List Perfectly (needs $99+ for auto-delist), Vendoo (no Shopify in the delist list) or Nifty (Poshmark/eBay automation, no Shopify).
6. **Title format:** `1970s <Category> / 70s <descriptors> / <Maker>` with the era stated in both forms; keep one sentence of condition tier in the description.
7. **Skip:** Marketplace Connect (no Etsy), LitCommerce at $29 (unproven quantity-1 latency), full headless, and a paid theme "just in case".

## What Ricky must check himself

- Etsy account: Seller Policy, Creativity Standards and vintage policy text on etsy.com directly (I only had Wayback copies; the vintage page's 2026 snapshot was empty).
- The 140-character title and 13-tag limits, and the maximum photo count: UNVERIFIED.
- Whether Etsy allows an own-site link in the announcement, and whether a free gift disco ball in the package is fine.
- Whether Shopify Flow is available on the plan he picks.
- Open the five theme demo URLs and the Expression demo (UNVERIFIED).
- Whether ChatGPT Sites allows the Shopify script and API calls.
- Crosslist: Etsy import leg and real sale-to-delist time on a single quantity-1 item before paying beyond the trial.

## Sources not reached

- Etsy title/keyword handbook pages (walled live and Wayback); FLUF, Sellbrite, SellerAider pricing (not re-fetched); theme demo sites (not opened); Crosslist import docs (not fetched).
