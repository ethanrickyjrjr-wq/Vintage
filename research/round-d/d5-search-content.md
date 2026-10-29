<!-- Saved verbatim by the parent Opus session from agent d5's final message, 2026-10-29 (the harness refuses subagent report writes). -->

# d5: search, Pinterest and content

Agent d5, accessed 2026-10-29. Raw captures: `research/round-d/raw/d5-*` (62 files: 16 SERP lists, 7 live HTML pages, the rest crawled docs).
Method: SearXNG (`tools/search.sh`, merged google cse / bing / startpage / yahoo) for 10 target searches plus 3 re-runs and 2 brand searches; crawl4ai (`tools/crawl.sh`) for vendor docs and guide pages; `curl` with a browser UA for 7 live shop/marketplace HTML pages so I could read their JSON-LD (crawl4ai strips script tags); WebFetch once (Etsy search doc, HTTP 403). About 40 pages read. Law pages are not in this lane.
SERP caveats, plainly: (1) order is SearXNG's merged order, not Google's ranking, and not local to Lee/Collier; (2) many rows were junk, so I filtered them with a blocklist: bare google/bing/duckduckgo/brave hosts, minecraft, virginia*, vinted, localvintagestores, vavtg, antiquestoresnearby, americanfleamarket, unique-vintage, yelp, and in the second batch merriam, dictionary, nocache, stackoverflow, hino; (3) `d5-serp-10.txt` came back empty after filtering and was re-run as `-14`; `-12` ("Hollywood Regency decor ideas") is all Hollywood-the-place junk; (4) two earlier queries (mid-century brass floor lamp, Murano identification) printed to the terminal but were not saved, so I cite only `d5-serp-01..16`.
Tags: `verified` = read live this session. `inferred` = my reading. `unverified` = not read on a primary page.

Walls and dead pages (not retried, no Patchright): Etsy "How Etsy Search Works" (crawl 4 bytes; WebFetch 403), Etsy market page via curl (403, 776 bytes), Pinterest Predicts (4 bytes), Pinterest merchant guidelines and Pinterest Tag help (126 bytes each), Hommes Studio Hollywood Regency guide (0 bytes), Yoast out-of-stock article (26 KB of nav and footer only, body did not parse). The Pinterest help URL I tried for product pins returned the same article as the rich-pins URL (byte-identical file). **Consequence: I have no first-party evidence on how Etsy ranks listings, and none on Pinterest search volume beyond the idea-page counters below.**

## TL;DR

1. **First decision for Ricky: can the hand-built site take payment?** Google's own docs split on it. "Merchant listings" are for purchase pages and need a seller `Offer`; "Product snippets" are for non-purchase pages. Pinterest's Product Pin rule says the same thing: "people need to be able to buy the product directly from your site before you can add the product Pin." Checkout is "unavailable" on the site today, so the site pages get product-snippet markup now, and Product Pins live on the Shopify/Etsy listings, not the site. `verified`.
2. **Who ranks.** Buy-intent queries ("vintage brass table lamp", "vintage hollywood regency mirror", "vintage chrome glass coffee table") return marketplace and big-retailer collection pages (eBay, Etsy, Chairish, 1stDibs, Pinterest) with a few independent vintage shops' product or collection pages. Identify/date/markings queries ("Stiffel lamp markings", "pink depression glass identification") return guides, Facebook-group threads and Reddit. Styling queries return editorial pages and Pinterest idea pages. `inferred` from a noisy sample.
3. **Page order to build:** shipping/returns node, product page that survives the sale, object-type collections, maker-and-mark guides, era/material guides, styling guides.
4. **Sold value: use `OutOfStock` in JSON-LD and `out of stock` in `og:availability`.** It is the only value in all three vendor lists (Google, Pinterest, Merchant Center). `SoldOut` is Google-only; Pinterest's lists omit it. `inferred`, flagged for review below.
5. **Condition: `UsedCondition` for every vintage piece**, with "rewired", "polished" and similar in plain words. Merchant Center defines refurbished as "professionally restored ... and comes with a warranty." `verified`.
6. **Real shops get this wrong.** Dovetail Chicago's vintage mirror page reads "Sold Out - $0.00" in the HTML while its JSON-LD says `InStock`, price `0.00`, valid until 2030. Four of five pages I parsed omit `itemCondition` entirely; only Chairish sets it. `verified`.
7. **Sold pages: keep at 200, mark clearly SOLD, give them enough substance to not read as an error page.** Google's docs cover 404 (page removed, no replacement) and 3xx (page moved), not "sold one-of-one that stays up". The recommendation is `inferred`.
8. **Brand search risk.** "Holliewood and Vine" returns an Instagram handle `@holliewoodandvine` and a Facebook page, but "Holliewood & Vine vintage" returns Poshmark's "Hollywood & Vine" brand page and an Etsy "Hollywood and Vine" market page. I did not verify who owns the social accounts. `verified` for what appeared; ownership `unverified`.

---

## 1. What ranks: 10 target searches

Raw: `d5-serp-01..16.txt`. Page-type labels are mine (`inferred`); the URLs are what SearXNG returned.

| # | Query (file) | Page types in the usable rows | Read |
|---|---|---|---|
| 1 | vintage pink depression glass coupe glasses (01) | eBay brand page, Etsy market page, two independent shop product pages (lucidladybug.com on Wix, houseofmodernvintage.com on Shopify), a third independent product page (drjohnfleming.com), Pinterest idea page, LoveToKnow guide, Reddit ID thread, Facebook post | Marketplaces and small shops' single-product pages both rank; one guide |
| 2 | pink depression glass identification (02) | Top rows were Pink the singer; usable: Facebook group thread "Identifying depression pink glass versus other pink glassware?", LoveToKnow "Depression Glass Patterns: A Picture Identification Guide" | Guide and community thread; thin sample |
| 3 | what is Hollywood Regency style interior design (03) | Mostly Hollywood-the-place and a betting site; usable: Wikipedia "Hollywood Regency", Hommes Studio journal | Word "Hollywood" collides with the place |
| 4 | how to style a bar cart (04) | Mostly dictionary/"Style" junk; usable: Emily Henderson (EHD) formula post, Pinterest board | Thin sample; see 13 |
| 5 | Stiffel brass table lamp vintage (05) | stiffel.com category, remains.com product page (a dealer), Lighting New York brand page, Facebook antique-lighting group | Maker site plus dealer plus community |
| 6 | how to date a Stiffel lamp (06) | Date-calculator junk; usable: Lighting New York guide, same Facebook thread | Guide plus thread |
| 7 | vintage brass table lamp (07) | eBay search x4, 1stDibs collection x2, Chairish collection, Etsy market x2, Scully & Scully, Rejuvenation, Pottery Barn | 12 rows, all marketplace or large-retailer category pages; no guides, no independent vintage shop |
| 8 | vintage cut glass vase (08) | Pinterest board, eBay x2, Etsy market, wholesale/retail category pages (Jamali Garden, Bellamy's World, Terrain), JustAnswer Q&A, LoveToKnow guide, Collectors Weekly | Mixed; guides present |
| 9 | vintage hollywood regency mirror (09) | eBay category, Chairish collection, 1stDibs collection, Etsy market, Kathy Kuo (new-goods retailer product), dovetailchicago.com product page, Pinterest pin and idea pages, Facebook post, Instagram post | Marketplaces first; one independent vintage shop |
| 10 | vintage chrome glass coffee table for sale (14) | Etsy market, sunbeamvintage.com collection, 1stDibs, eBay, Chairish, Pinterest idea page, Whoppah, Reddit, theparadiseantiques.com product page, Foter | Marketplaces plus two independent shops |
| 11 | Stiffel lamp markings identify value (11) | Lighting New York guides x2, Facebook group thread, Pinterest idea page | Guides win |
| 12 | Hollywood Regency decor ideas (12) | All junk (Hollywood Bets, Britannica, Hollywood FL) | Bare "Hollywood Regency" needs a qualifier |
| 13 | vintage bar cart ideas styling (13) | Pinterest x2, The Spruce, Architectural Digest, West Elm guide, Joss & Main guide, EHD, Anastasia Co blog, Houzz, Facebook | Editorial and retailer guides plus Pinterest |
| 14 | Holliewood and Vine (15) | `instagram.com/holliewoodandvine`, a Facebook post titled "Holliewood and Vine added a new...", then Roblox and "Collectible Classics" noise | Brand name resolves, ownership unverified |
| 15 | Holliewood & Vine vintage (16) | Instagram handle again, Poshmark "Hollywood & Vine" brand page, Etsy `/market/hollywood_and_vine`, Facebook post about the 1965 intersection | Misspelling is near-certain to be read as "Hollywood" |

**Pinterest idea pages (public, crawled):** the counter on the page reads "747 people searched this" for "Vintage bar cart styling" (updated "1d" ago), "397 people searched this" for "Chrome and glass coffee table" ("4d"), "13 people searched this" for "Vintage 1920s brass table lamp" ("1d"). The pages carry no time window, so quote them as shown, not as monthly volume. `verified`. The Stiffel, Hollywood Regency mirror and pink champagne pages showed no counter. Raw: `d5-pinterest-ideas-*.md`.
**Steal this:** (a) the page-type map above is the build order; (b) the product pages that rank for independents are plain single-product pages with the object name in the title; (c) type the query exactly into a Pinterest board name when a counter exists.

## 2. Google structured data for one-of-ones

### 2a. Product snippet vs merchant listing
- URL: https://developers.google.com/search/docs/appearance/structured-data/product (raw `d5-google-product-sd.md`, page footer "Last updated 2025-12-10 UTC"). The page's own summary: "Two markup types exist: Product snippets for non-purchase pages, emphasizing reviews, and Merchant listings for purchase pages, highlighting product details like sizing and shipping." `verified` (it is the page's footer summary, not the body).
- Merchant listing doc: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing (raw `d5-google-merchant-listing-sd.md`, "Last updated 2026-09-08 UTC"). Required `Product`: `name`, `image`, `offers`. "merchant listings require an `Offer` ... as the merchant has to be the seller of the product in order to be eligible for merchant listing experiences." `Offer` required: `price` and `priceCurrency`, and "Unlike product snippets, merchant listing experiences require a price greater than zero." Recommended: `availability`, `hasMerchantReturnPolicy`, `itemCondition`, `priceValidUntil`, `shippingDetails`. `verified`.
- Product snippet doc: https://developers.google.com/search/docs/appearance/structured-data/product-snippet (raw `d5-google-product-snippet.md`). Required: `name`, plus "either `review` or `aggregateRating` or `offers`", with a warning that the Rich Results Test "may report a warning if you provide `offers` without `review` or `aggregateRating`." `verified`. A new shop has no reviews, so `offers` is the route, and do not invent reviews.
- Images: "Pictures clearly showing the product (for example, against a white background) are preferred" and "multiple high-resolution images (minimum of 50K pixels ...) with the following aspect ratios: 16x9, 4x3, and 1x1." `verified`. This matches the white-framed product photos already decided.
- `priceValidUntil`: "Your listing may not display if the `priceValidUntil` property indicates a past date." `verified`. A static site that does not rebuild on a schedule should omit it (`inferred`). Chairish's JSON-LD sets it a week out (2026-11-05 in the page I fetched); Remains sets 2026-11-08; Dovetail sets 2030-01-01 (`verified`, from the raw HTML).
- Markup must match the page: "Don't mark up content that is not visible to readers of the page" and "Provide up-to-date information." (https://developers.google.com/search/docs/appearance/structured-data/sd-policies, raw `d5-google-sd-policies.md`). `verified`.
- Shop-level policies: "We recommend you provide a global return policy for your business under `Organization` markup instead" and offers can reference it with only `@id`. The doc's own example type is `OnlineStore` (raw `d5-google-return-policy.md`, fields seen: `applicableCountry`, `returnPolicyCategory`, `merchantReturnDays`, `returnFees`). `verified`. There is no showroom, so use `OnlineStore`, and no `LocalBusiness` address or hours.
- **Steal this:** one `OnlineStore` node on the policies page, product pages point at it by `@id`.

### 2b. Merchant Center free listings and the condition attribute
- Condition: https://support.google.com/merchants/answer/6324469 (raw `d5-gmc-condition.md`). "Required for each used and refurbished product." "Use the condition attribute to tell potential customers about the condition of the product ... It's important to set this value correctly since it is used to refine search results." Used = "Your product is second-hand or has been modified from the original condition ... the product shows wear or has been used before, the original packaging has been opened or is missing". Refurbished = "professionally restored to working order so that it appears new, and comes with a warranty." Mapping: `used` = `DamagedCondition`, `UsedCondition`. Google's own example of a vintage item: title "Hot Pink Vintage High Heels - 1930s - Size 6", condition `used`. Note: "used and refurbished products aren't displayed on YouTube organic and Discover surfaces." `verified`. There is no "vintage" condition value; vintage goes in the title.
- Identifiers: https://support.google.com/merchants/answer/6324478 (raw `d5-gmc-identifier-exists.md`). "Products that might not have unique product identifiers include: Custom goods or one-of-a-kind products ... Products produced before GTINs were introduced, like vintage products, antiques". The trigger sentence is written for new products, so for used vintage goods whether `identifier_exists=no` is needed is `inferred`; the page names vintage as a no-identifier case. `verified` for the quote.
- Availability: https://support.google.com/merchants/answer/6324448 (raw `d5-gmc-availability.md`). Mapping: `out_of_stock` = Discontinued, InStoreOnly, OutOfStock, SoldOut. "For 'out of stock' products, you can display clear text such as 'sold out' or 'item not available' or use a disabled/greyed out 'buy' button." "If we find that a product is out of stock on your landing page or during checkout, but the availability attribute is set to `in_stock` in your product data, we disapprove the product." "For permanently discontinued products, delete them entirely from your data source rather than setting them to out of stock." `verified`.
- Free listings: https://support.google.com/merchants/answer/13889434 (raw `d5-gmc-free-listings.md`). "Free listings for products help your product pages appear in search results, not other pages like homepages, shipping and return policies, or product category pages." Free listings are on by default in new accounts. Shipping settings are required in listed countries, and the full line ends "...the United Kingdom, and the United States." `verified`. So collections and guides never become free listings; only product pages do.
- **Steal this:** feed `title` pattern from Google's example: object, "Vintage", decade, key dimension. `condition=used` always.

## 3. Sold pages: keep, redirect or 404

| Source | What it says | Tag |
|---|---|---|
| https://developers.google.com/search/docs/crawling-indexing/http-network-errors (`d5-google-http-status.md`) | 4xx (except 429): "the indexing pipeline removes the URL from the index if it was previously indexed. Newly encountered 404 pages aren't processed. The crawling frequency gradually decreases." An error-looking page returned 200 shows in Search Console as a `soft 404`. | verified |
| https://support.google.com/webmasters/answer/7440203 (`d5-gsc-soft404.md`) | A 404 is fine "for a page that you've removed and have no replacement for"; "If a page has been moved, you should return a 3XX redirect to the new page." | verified |
| https://developers.google.com/search/docs/crawling-indexing/301-redirects (`d5-google-301.md`) | A permanent redirect is "a signal that the redirect target should be canonical." | verified |
| https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites (`d5-google-ecom-url.md`) | Empty category: use `noindex`, or "consider returning a 404". This is about categories, not products. | verified |
| SEJ, "Google's John Mueller Explains Why Expired Product Pages May Become Soft 404s" (`d5-sej-mueller-expired.md`, 2019 per the image path, secondhand) | "If you're really replacing one product with another it might make sense to just redirect. If one product is gone completely ... you could put it in this soft 404 state where you say this product is no longer available." | verified that the article says it; date and quote chain unverified |

**X verified, Y need review.** Google's first-party docs cover removed pages (404) and moved pages (3xx). None covers a one-of-one that stays up as an archive entry. Mueller's 2019 remark is secondhand and is about redirect targets that say "no longer available".
**Recommendation (`inferred`):** because the sold archive is already decided, keep each sold page at HTTP 200, with a visible SOLD label, the original description and photos intact, `availability` flipped, and enough real content (marks, dimensions, condition notes, a link to the matching guide and collection) that it is not an empty "gone" page. If a piece is withdrawn rather than sold, 404 it. Do not redirect a sold lamp to a generic lamps page; per the Mueller piece that is the pattern that gets flagged as a soft 404. Never leave `InStock` on a sold page: Merchant Center disapproves that mismatch, and Dovetail shows how it happens.

## 4. What shops actually ship (live HTML parse)

Raw: `d5-html-*.html`, fetched 2026-10-29. I parsed `application/ld+json` blocks.

| Page | `itemCondition` | `availability` | Price / validity | Notes |
|---|---|---|---|---|
| chairish.com/collection/table-lamps/brass (48 Product nodes) | Always set: 38 `UsedCondition`, 5 `NewCondition`, 5 `RefurbishedCondition` (counted from the JSON) | `InStock` on 40, `LimitedAvailability` on 8 | `priceValidUntil` 2026-11-05 on the item I read | Also carries `color`, `material`, `depth`, `height`, `width`. Why 8 are `LimitedAvailability`: `unverified` |
| houseofmodernvintage.com pink depression coupes | absent | `InStock` | "118.00" USD | Has `gtin` key, `og:type=product` |
| dovetailchicago.com Hollywood Regency oval mirror | absent | JSON-LD says `InStock` | "0.00", `priceValidUntil` 2030-01-01 | **Page text: "Sold Out - $0.00".** Mismatch, and price 0 fails the merchant-listing price rule. Cause (theme default) is `unverified` |
| remains.com vintage turned brass Stiffel lamps | absent | `InStock` | 4500.0 USD, `priceValidUntil` 2026-11-08 | |
| lucidladybug.com pink depression coupes (Wix) | absent | `InStock` | "65" USD | Also `og:availability=InStock`, `product:price:amount` |
| sunbeamvintage.com/collections/floor-lamps | regex found no availability/condition strings | | | Not investigated further; may be JS-rendered |

Shopify's own docs for the `structured_data` filter (https://shopify.dev/docs/api/liquid/filters/structured_data, `d5-shopify-structured-data-filter.md`) show sample output with `"availability":"http://schema.org/OutOfStock"` and no `itemCondition`. Dawn calls it as `{{ product | structured_data }}` (`d5-dawn-main-product.liquid` line 752). `verified`. So Shopify's default markup flips to out of stock when sold but never says "used"; a vintage shop needs a small custom snippet or app for `itemCondition`.
**Steal this:** Chairish's pattern of `itemCondition` plus dimensions plus material on every item. **Do not steal:** Dovetail's $0 / InStock / 2030 combination, and Chairish's "Refurbished" for a piece with no warranty.

## 5. Pinterest Rich Pins

- Help: https://help.pinterest.com/en/business/article/rich-pins (`d5-pinterest-help-rich-pins.md`). "Rich Pins are Pins that automatically sync information from your site." Types: recipe, article, product. "We'll only show information about your product rich Pin if you've met our merchant guidelines and if the product is in stock." And: "This info will only show up on your product Pins if your product is in stock, the price is accurate, we've updated the data recently". "Product Pins lead people on Pinterest to your site where they can purchase your products. This means people need to be able to buy the product directly from your site before you can add the product Pin." Sync delay: "up to 24 hours". Opt-out tag: `<meta name="pinterest-rich-pin" content="false" />`. `verified`.
- Developer docs: https://developers.pinterest.com/docs/web-features/product-rich-pins/ (`d5-pinterest-dev-product-pins.md`). Open Graph required: `og:type=product`, `og:title`, `product:price:amount`, `product:price:currency`. Schema.org required: `url`, `name`, `price`, `priceCurrency`. `og:availability` values: `instock preorder backorder` (or `pending`), `out of stock`, `discontinued`; "discontinued items won't be a part of a daily scrape". Schema availability list: InStock, OnlineOnly, InStoreOnly, OutOfStock, PreOrder, Discontinued (no SoldOut). "Open Graph format only works for pages with a single product." "If you are using a Shopify website, then your page already has the correct metadata." Page-type priority when several are present: product, then recipe, then article. `verified`.
- Article Pins need only `og:title`, `og:description`, `og:type=article` (help page). "We do not consider listicles or pages with mostly images and little text to be articles." `verified`. So a guide needs real text to become an Article Pin.
- Application step: the developer page says "Once you've applied for Rich Pins ..." but the help article I read describes only the tags, so whether a validate/apply step is still required is a **need review**. The Pinterest Tag and merchant guidelines pages were walled.
- **Steal this:** (a) Product Pins from the Shopify listings (metadata already correct) once Shopify exists; (b) Article Pins from the guide pages, which can go live with no account beyond Pinterest itself; (c) a sold piece loses its price overlay but the Pin keeps working as an image that lands on the SOLD page, which is where the "find me one like it" prompt goes.

## 6. Era and maker guides as content

Raw: `d5-guide-*.md`, `d5-google-helpful-content.md`.
- Lighting New York, "How To Identify a Stiffel Lamp: A Collector's Guide" (https://lightingnewyork.com/k/lighting/wall-lights/lamps/how-to-identify-a-stiffel-lamp): about 2,500 words, H2s on key features, "Marks, Serial Numbers, and Other Identifiers", "How to Identify the Value?", a Q&A block, retailer trust badges. A lighting retailer ranking for identification queries. `verified` for structure.
- LoveToKnow "Pink Depression Glass": about 1,800 words, mostly a gallery of styled examples with H2s per object; ranks for the coupes query. `verified`.
- Collectors Weekly "Antique Cut Glass" and 20thcenturyglass.com Murano identification guide (with eBay and Etsy sections): reference-style guides that rank for identify queries. `verified` for existence and headings.
- EHD "bar cart styling formula": a short formula post (top shelf, bottom shelf). Wikipedia "Hollywood Regency": sections for characteristics, designers, architecture, gallery. `verified`.
- Google on people-first content: "Does your content clearly demonstrate first-hand expertise and a depth of knowledge", and a warning sign: "Are you mainly summarizing what others have to say without adding much value?" (https://developers.google.com/search/docs/fundamentals/creating-helpful-content). `verified`.
- Read: a retailer already ranks for "Stiffel markings" with a generic guide. What it cannot show is the shop's own stock photographed with its marks. That first-hand layer is the opening (`inferred`).
- **Steal this:** the H2 skeleton: what it is, features, marks and numbers, value, questions. **Do not steal:** generic text with no own-stock evidence.

## Where sources disagree

- **Sold value.** Google lists `SoldOut`, `OutOfStock`, `Discontinued` (merchant-listing doc). Pinterest lists `OutOfStock` and `Discontinued` and its `og:availability` allows `out of stock` and `discontinued`; `SoldOut` appears in neither Pinterest list. Merchant Center maps all three to `out_of_stock` and says to delete permanently discontinued items from the feed. Pinterest drops discontinued items from its daily scrape and shows product data only while in stock. X verified: `OutOfStock` is in all three. Y need review: whether `OutOfStock` ("currently out of stock") reads wrong to Google for a piece that is permanently gone. My pick is `OutOfStock` everywhere, `inferred`.
- **Condition.** Google structured data lists New/Refurbished/Used. Merchant Center maps `used` to `DamagedCondition` plus `UsedCondition` and defines refurbished as warranty-backed professional restoration. Chairish marks 5 of 48 items on the page I parsed as Refurbished. X verified: `used` fits any second-hand vintage piece. Y need review: any claim of `RefurbishedCondition` on a rewired lamp, because no warranty has been decided.
- **Sold pages.** Google's docs say 404 for removed with no replacement and 3xx for moved; the SEJ item (2019, secondhand) says redirect when replaced and a "no longer available" soft-404 state when gone. None addresses a retained sold one-of-one. Y need review: only Search Console's Page indexing report on the live site will show whether Google treats SOLD pages as soft 404s.
- **Pinterest application.** Developer page implies you apply; help page describes tags only. Y need review.
- **Shopify vs Dovetail.** Shopify's documented filter emits `OutOfStock` for a sold-out variant, yet the Dovetail page (not confirmed to be on that filter) emits `InStock` and $0. Cause unverified.

## Recommendation for Holliewood & Vine

### Page types to add, in order
0. **Shipping and returns page** with one `OnlineStore` node (return window, fees, shipping). Prerequisite for the `@id` references.
1. **Product page** (one URL per piece, kept after sale): see fields below. Object name and maker/decade in the `<title>` and H1.
2. **Sold state of the same page** (the sold archive): same URL, flipped markup, "find me one like it" prompt into Fabulous From Online.
3. **Object-type collection pages** (Lamps, Mirrors, Glass, Barware, Tables, Chairs, Rugs): short intro paragraph, then the cards. Marketplaces dominate these queries, but independents (Sunbeam, Dovetail) appear, so the long tail is winnable. Note: collections and guides do not become Google free listings.
4. **Maker-and-marks guides** (identification queries are where guides and community threads win).
5. **Era and material guides** (Hollywood Regency, Depression glass colors, cut vs pressed).
6. **Styling guides** (editorial and Pinterest territory; ties to the service).

### Structured-data fields for a listing
Pick the variant by checkout:
- **(b) Site sends buyers to Etsy/Shopify (today).** Type `Product`, product-snippet route. Fields: `name`, `image` (1x1, 4x3, 16x9), `description`, `sku`, `offers` as a single `Offer` with `url`, `price` (over zero), `priceCurrency`, `itemCondition` = `https://schema.org/UsedCondition`, `availability` = `https://schema.org/InStock`, `hasMerchantReturnPolicy` as `{"@id": ".../returns#policy"}`. Add `brand` only when a maker is established (never invent one). Add `color`, `material`, `height`, `width`, `depth` as Chairish does (`unverified` as a Google-recognized field here). Omit `priceValidUntil`, `gtin`/`mpn`, `review`, `aggregateRating`, `LocalBusiness`.
- **(a) Site has its own checkout.** Same as (b) plus `shippingDetails` (rate, destination US, handling and transit days) or an org-level shipping node. Add `og:type=product`, `product:price:amount`, `product:price:currency`, `og:availability=instock` for Product Pins. Merchant Center feed: `condition=used`, `availability=in_stock`, `identifier_exists=no` where there is no maker number.

### Structured-data fields for a sold listing
Same `Product`/`Offer`. Change: `availability` = `https://schema.org/OutOfStock`; `og:availability` = `out of stock`; keep the real `price` and `UsedCondition` (do not zero the price); remove any buy button or show it disabled; show "Sold" text on the page; leave `hasMerchantReturnPolicy` as is. In a Merchant Center feed, delete the item (permanent), do not park it as out of stock. Keep the page at 200.

### Five guide-page titles (shop voice; body facts to be sourced before publishing)
1. "Is That Brass Lamp a Stiffel? Check the Base Before You Get Excited"
2. "Pink Glass, Interrogated: Which Pieces Are Actually Depression Glass"
3. "Hollywood Regency Without the Costume: A Plain Guide to the Look"
4. "The Bar Cart Is a Stage. Here Is the Set."
5. "Cut Glass or Merely Pressed? Hold It to the Light"
(Keeps "Hollywood Regency" as a style name only, never the shop; no interior-design framing; no gift or disco-ball claims.)

### What to do now (no accounts needed)
- Decide variant (a) or (b) first; ship (b).
- Write the `OnlineStore` return/shipping node from the real policy text.
- Add `UsedCondition`, dimensions and a plain-words condition line to the product template; build the sold template with `OutOfStock`; test both in Google's Rich Results Test and the Schema.org validator (neither needs a login, `unverified` that no login is required).
- Build collection pages with a short intro and guides 1 and 3 first.
- Add Open Graph tags to guides so Pinterest can create Article Pins.
- Put a "Holliewood with an ie" line in the page title and About so the brand spelling is indexed.

### What needs an account, a fee or a lawyer
- Google Search Console (free, domain verification) to watch Page indexing for soft 404s on sold pages.
- Merchant Center account for free listings (free; new accounts have free listings on by default, `verified`), only after variant (a) exists.
- Pinterest business account and, if required, domain claim/validation (`unverified`; Pinterest docs partly walled).
- Shopify for Product Pins, plus a small custom snippet or app for `itemCondition` (Shopify's default omits it).
- A lawyer or the existing counsel review of the return/shipping wording that gets marked up, since the markup restates the policy publicly (ch. 538 handled separately per the brief).

## Ideas for Hollie

1. Sold pages that say "Gone. Not forgotten. Want one like it?" and route into Fabulous From Online. (Google 404/3xx docs; Pinterest in-stock rule)
2. A marks-and-labels photo glossary shot from the shop's own pieces: base stamp, paper label, cord tag. First-hand evidence beats the retailer guide. (Lighting New York Stiffel guide; Google helpful-content questions)
3. One "Is it a ...?" guide per maker where identify queries show guides and Facebook threads winning. (serp-05, -06, -11)
4. Pinterest boards named exactly like the idea pages that show a counter: "vintage bar cart styling" (747), "chrome and glass coffee table" (397). (Pinterest idea pages, no time window)
5. Never title a page "Hollywood Regency decor" alone; always "Hollywood Regency lamps/mirrors/bar carts" so the page is not buried by the place. (serp-03, -12)
6. A one-line condition label on every piece, in plain words ("Used. Rewired. Brass polished by hand."), mapped to `UsedCondition`, never "refurbished" without a warranty. (Merchant Center condition definitions)
7. A weekly-drop archive that is just dated collection pages, each card linking to a product page that stays up. (existing decision; Google 200-page guidance)
8. Confirm who owns `@holliewoodandvine` on Instagram and the Facebook page, and claim the handle on Pinterest. (serp-15, -16)
9. A short "Why we spell it Hollie, with ie" line in the About copy for the misspelling-corrected searches. (serp-16: Poshmark and Etsy "Hollywood & Vine" collisions)
10. Pin every guide as an Article Pin and only pin sale items from Shopify as Product Pins until the site has checkout. (Pinterest rich-pin docs)

## Gaps I could not fill
- Etsy search ranking factors (page walled, WebFetch 403). No Etsy claim in this report rests on a source.
- Pinterest Predicts, merchant guidelines, validator, and the apply step.
- Real Google SERPs for Lee/Collier. The SearXNG sample is generic and noisy.
- Whether `material`, `height`, `width`, `depth` are recognized by Google's merchant-listing parser; Chairish uses them, the docs I read did not list them.
- Whether Google treats retained SOLD pages as soft 404s. Only Search Console on the live site will answer that.
