# What the public Instagram, eBay and Depop pages say about Holliewood and Vine (2026-11-08)

Sources, all read 2026-11-08 UTC in Ricky's Chrome tab (Instagram and eBay are walled to the crawler) or by crawl4ai:
- https://www.instagram.com/holliewoodandvine/ (public view, not signed in; posts show only alt text)
- https://www.ebay.com/usr/holliewoodandvinellc
- https://www.depop.com/holliewoodandvine/ (`research/www.depop.com_holliewoodandvine_-20261108T072442Z.md`)
- https://poshmark.com/closet/holliewoodandvine and `/closet/holliewoodandvinellc`: both "Page Not Found"

Ricky confirmed `@holliewoodandvine` is the shop's account the same day. Until then the social manual and the desk wiki said no account existed.

## Facts

### Instagram `@holliewoodandvine`
- 347 followers, 512 following, 12 posts visible to a signed-out visitor (2026-07-17 to 2026-10-24). About one post a week in September, then nothing after 24 October.
- Name field: "Holliewood and Vine" (no keywords).
- Bio, in full: "Curated Vintage Showroom & Studio Rental. Located Loveland, OH & Bonita Springs, FL. Products posted on eBay @Holliewoodandvinellc, Vinted & Poshmark."
- Link: depop.com/holliewoodandvine (no link-in-bio page, no site link).
- Profile picture: a hand-lettered script "Holliewood & Vine" on a sign with a small plus, held up by two hands. This is a second logo, different from the Bodoni wordmark on the site and in Photoroom.
- Grid from alt text: a repost tagged `@flamingoislandfleamarket`, a mirror and miniskirt shot, a packing or moving scene (suitcase, box, hangers, hamper), a reel with a scarf, slip, mannequin and headscarf, glasses on a table, a rack of clothes. Captions and insights need a signed-in session.

### eBay seller `holliewoodandvinellc`
- Exists, "100% positive feedback (2)". The name carries "llc", so a business entity exists or is intended.
- 7 live listings on 2026-11-08: Kay Unger 2-piece damask skirt suit $45; Guess black pebbled shoulder bag $15; Worthington striped tote $12; Bassett free-form wood and glass coffee table $850; Steve Madden small black jean satchel $15; Alice + Olivia sandals $26 (auction, 0 bids); Nancy Glazier "Forever Free" framed licensed repro horse print 2004 $225.
- Photo style: garments flat on carpet or wood floor, bags on the floor, the table in a room. No white backgrounds, no form.

### Depop `holliewoodandvine`
- Empty shop: 0 reviews, 1 follower, 0 following, "Active over a week ago". The Instagram bio points here.

### Poshmark and Vinted
- No Poshmark closet under either handle. Vinted was not checked (member pages need a numeric id). The bio claims both.

## What it changes

1. **Photoroom Brand Library.** Two logos now exist. Either the script sign goes into Photoroom alongside the Bodoni wordmark (Ricky has to supply the file; the Instagram avatar is 150 px) or the Instagram avatar changes to the mark in `assets/brand/`. The brand description can add the two locations and the studio-rental line. Done so far: handle entered.
2. **Social manual.** Its tier plan starts from zero; it should start from 347 followers, one post a week, and a bio that already sells. Fixes that cost nothing: a Name field with keywords, a link-in-bio page or the site link instead of the dead Depop shop, and no pointer to a Poshmark closet that does not resolve.
3. **eBay plan.** The account exists, so the dashboard handoff's step 0 is partly done; what is missing is the developer keys, not the seller. The seven live listings are the before pictures for the eBay photo studio: same items reshot on white with the cut-out tool is the first real test of `tools/cutout/cutout.py` on stock that is actually for sale.
4. **Shopify and the site.** Two locations (Loveland, OH and Bonita Springs, FL) and "Studio Rental" are not on the site anywhere. The hire page and the honest-details section need a decision on both. Shipping research in Round D assumed Southwest Florida only.
5. **Cross-listing.** Products are already spread over eBay, Depop (empty), Vinted and Poshmark. The Vinted note in memory stands: Vinted US bars business use, and the eBay name says LLC. Pick the channels on purpose before Crosslist fans anything out.
6. **Desk wiki.** `vintage.md` and the social playbook were last updated 2026-10-30 and still say no account exists. This note is the compile source.

## Open
- Sign in to Instagram in the Chrome tab so captions, insights and highlights can be read.
- Which logo is the logo.
- The real Poshmark and Vinted handles, or drop them from the bio.
- Whether the LLC is formed and in which state.
