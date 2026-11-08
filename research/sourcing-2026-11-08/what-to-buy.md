# Lane C: what to buy, buy ceilings and the fee math (Sonnet subagent report, saved verbatim)

Saved 2026-11-08 by the parent session. Brief: which vintage categories give the best money for the least listing friction, with buy ceilings and the 2026 fee and postage math. Tools: WebSearch for discovery (SearXNG was down, Fedora unplugged), `tools/crawl.sh` for every page read. Raw crawls are in `research/` with host and UTC timestamp names 20261108T0722 to T0738.

---

# Lane: WHAT TO BUY (Holliewood and Vine), 2026-11-08

Tags: [R#] = read from a crawled page (key at bottom). [S] = WebSearch result summary only, NOT read. The Fedora SearXNG box was down, so discovery used WebSearch and fetching used crawl.sh.

## Fee and shipping math (read first)
Assumptions: price includes free shipping; 6% sales tax (the figure in eBay's own worked example [R1]); 1 lb Commercial Ground Advantage, Zone 5, $9.29 [R2, Notice 123 effective 2026-10-04]; plus $1.50 packing. All figures are before Promoted Listings and before item cost.

| Sale | eBay 13.6% fees | eBay net | eBay 15% category (jewelry, watches, women's bags) fees / net | Etsy fees | Etsy net | Etsy net if Offsite Ads hit (15%) |
|---|---|---|---|---|---|---|
| $25 | $4.00 | $10.21 | $4.38 / $9.83 | $2.87 | $11.34 | $7.59 |
| $45 | $6.89 | $27.32 | $7.56 / $26.65 | $4.81 | $29.40 | $22.65 |
| $90 | $13.37 | $65.84 | $14.71 / $64.50 | $9.16 | $70.05 | $56.55 |

- eBay [R1, crawled 2026-11-08]: FVF 13.6% of the total including shipping and sales tax, plus $0.40 per order over $10 ($0.30 at $10 or less). 15% for Jewelry & Watches (not parts) and Women's Bags & Handbags; Books 15.3%. First 250 listings a month free, then $0.35.
- Etsy [R4, pub. 2026-07-19, rates "June 2026"]: $0.20 listing; 6.5% on price plus shipping, tax excluded; 3% + $0.25 processing on the full amount including tax; Offsite Ads 15% under $10k a year (opt-out allowed), 12% above and mandatory. I did not read Etsy's own fee page.
- Label sensitivity [R2]: Commercial 1 lb is $8.01 at Zone 1 and $11.22 at Zone 8. Commercial 2 lb is $10.50 at Zone 5 and $13.42 at Zone 8. Under 1 lb is a flat $8.24 at Zone 5. Retail 1 lb Zone 5 is $11.70, so use an eBay or Pirate Ship label. Zone-by-distance from Fort Myers was not fetched; Zone 5 is an assumption.
- Heavier: 3 lb $12.12, 5 lb $14.53, 10 lb $17.81, 25 lb $48.69 (Zone 5, commercial) [R2].
- Over 1 cubic foot (1,728 in3) the label is billed on dimensional weight; USPS cut the divisor from 166 to 139 on 2026-07-12 and now rounds dimensions up [R3, R2]. Length over 22 in adds $4.50, over 30 in adds $10. More than 2 cubic feet adds $21. Tubes, cans and wood or metal boxes add $4.50 [R2]. A 24x12x12 lamp box bills as about 25 lb, roughly $48.69 + $4.50 at Zone 5.
- Hazmat: a $50 non-compliance fee for undeclared hazmat (lighter fluid, perfume, nail polish) started 2026-07-12 [R3].

**Buy-ceiling rule, applied to every row:** ceiling = 0.5 x Net(P_low). P_low is the bottom of the middle-half sold range for the exact variant (not the median). Net = P - fees - label - packing. Shortcut at 13.6%, Zone 5: 1 lb Net = 0.856P - 11.19; under 1 lb Net = 0.856P - 9.64.
1 lb lookup, sale price to ceiling: $25 to $5, $35 to $9, $45 to $13, $60 to $20, $90 to $33, $120 to $45. Heavier items use the real label.

## 1. Home and decor
| Category | Names to look for | Typical sold range (source) | Buy ceiling | Listing friction | Notes |
|---|---|---|---|---|---|
| Pyrex | Pink Gooseberry, Butterprint, Snowflake, Terra Stripe, colored Cinderella sets | All vintage Pyrex median $29.90, middle half $17.99-$56.94, 5,174 sales Jul-Oct 2026 [R6]. Pink Gooseberry $60-$199, median $79 (42 sales); Butterprint $31-$75, median $40; Snowflake $24-$49, median $30 [R7]. Top sales $563-$1,528 for sets and rare colors [R6] | Pink Gooseberry piece $19 (2 lb, $60 low); Butterprint $6; Snowflake $3 (skip). 4-bowl Cinderella sets: rule gives about $225, cap $150 because the top-10 list is outliers | 1-3 photos; model number and lid are the title; 2-10 lb, needs double-boxing | 32% of sales are under $20 and 12% are $100+ [R6]. Only named patterns and sets clear the shipping |
| Fire-King, Anchor Hocking, CorningWare, Depression glass | Jane Ray jadeite | 12-pc Jane Ray set median $50, $24-$166, 146 sales [R9]. Category medians $18-$20 [R5] | Singles $2-3; sets pass (about 12 lb, label $17.81-$22.90) | Heavy | Saturated |
| Brass | Virginia Metalcrafters, Sarreid, Baldwin, Mottahedeh, Chapman | Plain pair median $35, 97 sales, $10-$450; bell pair median $61, 13 sales [R9]. VM "$50-$500" and no Sarreid or Chapman sold data [S] | Plain pair $7 (3 lb); marked maker or Italian pair $15 only with a sold comp | 2-3 photos; height and weight; sub-1 cu ft box | Dealer asking prices (1stDibs, Chairish) are not sold evidence |
| MCM lamps and small decor | Small table lamps, ceramic accents | MCM category median $31 (5,363 sales, $18-$68) [R5]. The "vintage lamps $73" figure is polluted: its sample shows car headlights [R10]. Do not use | Lamp $15 if it fits 12x12x12 and comps are $60 or more; otherwise pass | Wiring and "does it work" returns; box size decides profit | Wiring is the return risk |
| Art glass | Blenko, Empoli, Murano, Viking | Blenko vase median $75, 84 sales, $19-$632; Empoli goblet vase median $36.50, 119 sales, $9-$499 [R9]. Unmarked Murano-style $100-$250 [S]. Viking: no data | Blenko $12 (5 lb); Empoli $6; Murano only with label and comp | 3-4 photos; no measurements beyond height; fragile, double-box | Labeled pieces only |
| Barware | Culver, Georges Briard, Dorothy Thorpe, ice buckets | Mod floral ice bucket median $34.95 but only 7 sales (a snippet said 106 sales and $26, which the page does not support) [R9]. One Culver set sold $118.99 [S]. No Briard or Thorpe sold data (auction estimates only) [S] | Bucket $8. Boxed gold-band 8-glass set $20 if you find a $70+ sold comp | Sets need counts and condition photos; 5-6 lb | Plating wear is a return driver |
| Kitsch, studio pottery, frames and prints, 80s postmodern | Florida and beach souvenirs, golf, signed pottery, Memphis | Flamingo figurines $20-$40 and Florida souvenirs $13-$62 asking [S]. Memphis originals $250-$9,415 on 1stDibs [S]. Pottery, frames and prints: nothing found | $3 on kitsch; pass on the rest until you pull comps | Frames carry glass breakage | Fits the brand look, but I could not verify it as a money lane |

## 2. Fashion for SWFL
| Category | Names to look for | Typical sold range (source) | Buy ceiling | Listing friction | Notes |
|---|---|---|---|---|---|
| Lilly Pulitzer | "The Lilly" label, pre-1985 shifts | Sample median $27, $18-$45, but the sample includes pens and eyeglass frames [R10]. Brand median down 29% year over year [S]. "$200-$2,000" founder-era is one vendor's claim, and a vintage "The Lilly" dress in that same sample sold at $32 [R10] | Labeled pre-1985 shift $8; modern $2 | Needs size and measurements; fit returns | Do not buy modern |
| Hawaiian shirts | Reyn Spooner, Tori Richard | Tori Richard median $23 [S; the Closo page was walled for me]; eBay sales $14.99 and $22.99; Reyn Spooner $29.95 [S] | $4 | Under 1 lb; 3 photos plus chest and length | Cheap, low upside |
| Band and tourist tees | Single-stitch, tour tees | Vintage clothing median $35, $21-$81, 255 sales [R5]. Grail tees $3,200-$5,000 are outliers [R15] | $4 blind; $14 with a sold comp of $45 or more | Chest, length, tag photo | Outlier-driven |
| Denim | Levi's Big E, orange tab, 501/505/517, Lee, Wrangler | Levi's median $41, $24-$76, 1,016 sales [R5]. Markers are named, no prices [R13] | $4 plain; $11 for Big E or orange tab with a $41+ comp | 1.5-2 lb; waist and inseam | Fit returns |
| 90s bags | Coach, Dooney, Fendi | Coach $104 median (4,426 sales) [R5] vs $80 (500 sales) [R10]. Dooney All-Weather satchel median $59.97, 182 sales, $11-$319 [R9]. Fendi Baguette $500-$2,500 [S] | Coach $20; Dooney $10; Fendi pass without authentication | 15% fee; creed and serial photos | Counterfeit risk |
| Vintage sunglasses | Bausch & Lomb Ray-Ban, case included | Vintage averages $37.88 realized against $115.96 asked; 37.2% 30-day sell-through [R12]. B&L aviators sold $449.99, $269.99, $80, $44.99 [S] | $11 blind; more with B&L comps | Under 1 lb; 2 photos | Authenticate temples |
| Boots and sneakers | Tony Lama, Justin | Tony Lama $63, Justin $44 [S, Closo, walled]. Nike median $36 [R5] | $12 | Fit returns; 4 lb | Skip sneakers; no data |

## 3. Small valuables
| Category | Names to look for | Typical sold range (source) | Buy ceiling | Listing friction | Notes |
|---|---|---|---|---|---|
| Costume jewelry | Trifari, Monet, Napier, Weiss, Sarah Coventry | Vintage jewelry median $19, $10-$37, 1,678 sales [R5]. Value-page median $17 (its sample includes a trinket box) [R10]. Napier median $15 [S]. Signed "$30-$800" bands come from seller sites [S]; a signed Coro brooch sold $12 [R10] | Single piece $3; lots only | 15% fee; macro photos of hallmark | The signed-name premium is not proven by sold data |
| Watches | Running, named brands | ZIK vintage watches 19.9% sell-through, $117 average [R11]; sold-report median $61, only 107 sales [R5] | $25 with an $80 comp | 15% fee; test it runs | Not-running returns |
| Zippo | Pictorial models | One model: $27.90 median, $22-$50, 57 sales (updated 2026-10-27) [R9] | $4 | Under 1 lb | Ship empty, declare hazmat [R3] |
| Pens, film cameras | Parker 51, Sheaffer | Dealer asking prices only [S] | Pass | Test risk | No sold data |
| LEGO, Hot Wheels | Vintage sets; Redlines | Vintage LEGO median $38, $18-$90 [R5]. Hot Wheels median $12.95, 62% under $20, lots median $20; Redlines reach $2,795-$10,096 [R8] | LEGO set $10; Redline individually checked; skip loose cars | Count pieces; Redline base and wheel photos | Skip by-the-pound LEGO (unsorted sells at $6-$12/lb retail [S]) |

## 4. Sell-through and seasonality
- ZIK, Sept 2026 [R11]: vintage overall 13.6% 30-day sell-through, $43.77 average (about 86% of listings do not sell in a month). By segment: watches 19.9%, clothing and signs 16.9%, decor 15.0% ($29.69), jewelry 14.0% ($32.88), toys 10.6%, postcards 7.3%.
- Calendar [R14]: Black Friday Nov 27, Cyber Monday Nov 30, Christmas Eve Dec 24 peak. The same page says apparel and accessories are the top gift (71%) and gift spending is expected down 3%; the survey year is not shown.
- Practical: list light giftables (sunglasses, watches, bags, Levi's, Hot Wheels, Zippo) by about Nov 20. After mid-December, buy Christmas items (Shiny Brite sets sold $37-$64 [S]; one Pyrex Christmas casserole $1,500 [R6]) as stock for next year. Etsy's brass, silver and disco-ball trend notes are [S] only.
- Underpriced's Q4 guide [R16] has no category sell-through; it only says to limit restoration-heavy buys in November.

## Top ten for a Florida estate sale this month
1. Pink Gooseberry or Butterprint Cinderella sets and rare Pyrex colors (cap $150 per set).
2. Running, named vintage watches (ceiling $25, 19.9% sell-through).
3. Coach and Dooney leather bags with creed or serial (ceilings $20 and $10).
4. Bausch & Lomb Ray-Ban and branded sunglasses with cases ($11).
5. Levi's Big E, orange tab and 501s ($11 with comps).
6. Labeled Blenko and Italian art glass ($6-$12).
7. Vintage Hot Wheels Redlines, checked one by one.
8. Marked solid brass pairs ($7-$15).
9. Small lamps that fit under 1 cubic foot ($15).
10. Boxed Shiny Brite and Christmas pieces, bought for next season.

## Do not buy
- Heavy low-value glass: a $30 five-pound piece nets about $7.75 before cost (my math). Fire-King sets, Depression glass, Anchor Hocking, CorningWare ($18-$20 medians [R5]), common Snowflake singles.
- Furniture (antique furniture median $22 [R5]), large framed glass, lamp boxes over 1 cu ft, anything over 70 lb ($200 overweight fee from 2026-07-12 [R3]).
- Loose modern Hot Wheels, sports cards (median $9), Funko ($18) [R5], modern Lilly, Tori Richard above $4.
- Unauthenticated Fendi, Louis Vuitton or Ray-Ban; unmarked "Murano".
- Pens, cameras and electronics you cannot test; unsorted LEGO and costume lots with no signed pieces.
- Fuel-bearing lighters unless you ship them declared and empty.

## Discrepancies: X verified, Y needs review
- eBay FVF 13.6% verified on eBay's page; a 12.9% figure in one snippet is an outlier.
- USPS Notice 123 verified; third-party rate snippets ($8.85/$10.00, $9.55) need review.
- Coach: $104 (sold report) vs $80 (value page) needs review.
- ZIK sunglasses: the snippet said about $135 average; the crawled page says $37.88. ZIK vintage sell-through: snippet said about 7%; the crawled page says 13.6%.
- Barware: the ice-bucket snippet and the crawled page disagree.

## Could not verify
- From search summaries only, never read: Closo pages (walled by Anubis, so Tori Richard, Tony Lama, Justin, Napier and the Lilly brand trend are all unverified), Appraisily Murano, latestcost Virginia Metalcrafters, estimonia pens, LEGO per-pound, Shiny Brite, B&L sunglasses sales, Fendi ranges, Etsy 2025-26 trend reports.
- No usable data at all: frames and art prints, studio pottery, Viking glass, Sarreid, Mottahedeh, Chapman, Dorothy Thorpe, Georges Briard, Florida kitsch sold prices, current camera and pen prices, vintage sneakers, per-maker jewelry beyond Napier, Dooney and Fendi sold ranges beyond the pages above.
- eBay Authenticity Guarantee US thresholds: not found.
- The ebayadvertising holiday page redirected to a generic page. The octagonal ice bucket page returned 4 bytes. Guessed `underpricedai.com/value/*` slugs returned under 1 KB, possibly because the pages do not exist rather than being walled.
- Florida ch. 538 secondhand-dealer holds may apply to jewelry or precious metals bought from private individuals rather than estate-sale companies. Not verified, does not block.
- Fort Myers zone assignment and exact box sizes are assumptions.

## Sources read (crawled 2026-11-08 unless noted)
- R1 https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822
- R2 https://pe.usps.com/text/dmm300/Notice123.htm
- R3 https://support.pirateship.com/en/articles/15453569-july-2026-usps-rate-and-rule-changes
- R4 https://checkoutpage.com/blog/etsy-fees
- R5 https://underpricedai.com/sold-report
- R6 https://underpricedai.com/blog/what-vintage-pyrex-sold-for-jul-to-oct-2026-5-174-sales
- R7 https://underpricedai.com/value/vintage-pyrex/pink-gooseberry (also /butterprint, /snowflake)
- R8 https://underpricedai.com/blog/hot-wheels-sold-prices-2026-what-23-483-single-pieces-went-for
- R9 underpricedai.com/worth/ pages: pair-of-vintage-brass-bell-candlesticks-with-wide-drip-trays; pair-of-vintage-solid-brass-turned-candlesticks-with-faceted-knop-and-square-stepped-bases; fire-king-jane-ray-jadeite-12-piece-set-with-fiesta-yellow-plates; vintage-dooney-bourke-all-weather-leather-bonebritish-tan-zip-top-satchel-handbag; vintage-1960s-70s-mod-floral-fabric-covered-ice-bucket-with-swing-handle-and-lucite-lid; empoli-italian-art-glass-large-balloon-goblet-vase-in-tealpeacock-blue-with-optic-ribbing-and-twiste; blenko-handcraft-amethyst-art-glass-vase-with-textured-circle-pattern-and-green-rim; vintage-zippo-camel-joe-biker-on-motorcycle-pewter-emblem-lighter-with-box
- R10 https://underpricedai.com/value/lilly-pulitzer, /vintage-lamps, /vintage-jewelry, /coach
- R11 https://www.zikanalytics.com/reports/ebay/best-selling/vintage-items
- R12 https://www.zikanalytics.com/reports/ebay/best-selling/sunglasses
- R13 https://blog.vendoo.co/a-resellers-guide-to-vintage-fashion
- R14 https://export.ebay.com/en/resources/seasonal-guide-for-ebay-sellers/winter/
- R15 https://www.thrifted.com/blogs/the-edit/highest-selling-vintage-t-shirts-on-ebay-in-2025-in-the-usa
- R16 https://www.underpriced.app/blog/fall-winter-reselling-strategy-guide-2026
- Also crawled: https://www.pirateship.com/usps/commercial-pricing and /usps/ground-advantage (no rates), https://www.ebayadvertising.com/en/?p=168107 (generic), closo.co Tori Richard, Tony Lama and Justin pages (walled).

## Files for the parent to commit (this lane only, all under C:\Users\ethan\dev\Vintage\research\)
Stage by path with `git commit -- <paths>`, because many other untracked files in that folder belong to other lanes. Prefixes from 20261108T0722 to T0738, filenames as listed in the `ls research` output:
- www.ebay.com_help_selling_fees_credits_invoices_selling_fees-20261108T072247Z.md
- pe.usps.com_text_dmm300_Notice123.htm-20261108T072440Z.md
- support.pirateship.com_en_articles_15453569_july_2026_usps_r-20261108T072333Z.md
- www.pirateship.com_usps_commercial_pricing-20261108T072351Z.md
- www.pirateship.com_usps_ground_advantage-20261108T072420Z.md
- checkoutpage.com_blog_etsy_fees-20261108T072540Z.md
- underpricedai.com_sold_report-20261108T072701Z.md
- underpricedai.com_blog_what_vintage_pyrex_sold_for_jul_to_oc-20261108T072626Z.md
- underpricedai.com_blog_hot_wheels_sold_prices_2026_what_23_4-20261108T073027Z.md
- underpricedai.com_value_{lilly_pulitzer-T072908Z, vintage_lamps-T072916Z, vintage_jewelry-T072924Z, coach-T072931Z}.md
- underpricedai.com_value_vintage_pyrex_{pink_gooseberry-T073827Z, butterprint-T073834Z, snowflake-T073840Z}.md
- underpricedai.com_worth_ files with timestamps T073042Z, T073034Z, T073550Z, T073600Z, T073608Z, T073617Z, T073627Z, T073641Z
- www.zikanalytics.com_reports_ebay_best_selling_vintage_items-20261108T072749Z.md and ..._sunglasses-20261108T073050Z.md
- blog.vendoo.co_a_resellers_guide_to_vintage_fashion-20261108T073200Z.md
- export.ebay.com_en_resources_seasonal_guide_for_ebay_sellers-20261108T073150Z.md
- www.thrifted.com_blogs_the_edit_highest_selling_vintage_t_sh-20261108T073016Z.md
- www.underpriced.app_blog_fall_winter_reselling_strategy_guid-20261108T072824Z.md
- www.ebayadvertising.com_en_p_168107-20261108T072844Z.md
- closo.co_tools_closo_c_brand_tori_richard-20261108T073649Z.md, ..._tony_lama_shoes-20261108T073657Z.md, ..._justin_boots_shoes-20261108T073704Z.md (walled stubs, 2 KB each; optional)

I deleted my six 4-byte failed probe files. Nothing was committed.
