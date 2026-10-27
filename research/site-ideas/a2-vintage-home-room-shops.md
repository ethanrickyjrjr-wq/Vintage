# a2: vintage home / lighting / glass / object-led shops (room and film-set feel)

Agent a2, accessed 2026-10-27. Raw captures: `research/site-ideas/raw/a2-*.md`, sample images in `research/site-ideas/raw/a2-img/`.
Method: SearXNG for URLs, crawl4ai for pages, curl for 5 sample images that I then looked at myself. Markdown crawls cannot show layout, so anything about spacing, color or motion is marked `inferred`. Anything I saw with my own eyes in a downloaded image is marked `seen`.

## TL;DR

1. Best match for the Holliewood and Vine spirit is **The Kitschy Maximalist** (one-of-one, maximalist, "Shop the Look", a "Shop soundtrack" button). Steal the voice and the tiles, not the hero photo (it looks AI-generated).
2. Best product-page craft is **The Old Above** (one-person lighting shop: labeled DETAILS / SIZE / CONDITION / SHIPPING block, bulb base and wiring status spelled out, "1 in stock") and **Show Pony Palm Beach** (graded condition plus an honest "style is not attribution" buying guide).
3. Best room-as-navigation is **Soho Home "Shop the Look"** (room index, named scenes, wide room photo, product rail whose hover image is the in-room shot). It is new goods, but the pattern is exactly what a one-of-one shop with a real room can do cheaper and better.
4. Best glass photography is **The Joy of Cocktails** (black background plus reflection for stems, bokeh lifestyle shot for the hero) and best lamp photography is **The Old Above** (lit, hung against a colored wall). Both beat white-box shots for glass and light.
5. I found **no vintage shop with real pin-style hotspots** on a room photo. Soho's "shop the look" is a rail, Kitschy's is JS-rendered and I could not see it. Hotspots on your own room would be a differentiator; it is also a build cost, so it is ranked below the cheap wins.

---

## 1. The Kitschy Maximalist (strongest vibe match)

- Homepage: https://thekitschymaximalist.com/
- Pages read: `/` (raw `a2-kitschy.md`), `/shop/` (`a2-kitschy-shop.md`), `/shop-the-look/` (`a2-kitschy-look2.md`), raw HTML `a2-kitschy-home.html`. Accessed 2026-10-27.
- What they do: one-person shop (curator "Stacie") of 80s-to-Y2K vintage, kitsch, "maximalist home decor". Home page runs: hero ("More is more, more or less.") then jewelry callout, "What even is this place?" explainer, Featured Finds, Fresh Finds, "Shop by Vibe", about, "Get first dibs" email.
- Evidence (verbatim from the page):
  - "Shop soundtrack Tap to play a little funk" (a labeled music control, in brand voice).
  - Shop the Look: "A few finds put together as one idea — the outfit, the corner, the whole mood. Every piece is one of a kind, and every one is a tap from its own page."
  - Shop by Vibe: "Every room of chaos. Pick your poison — they're all a little extra." Tiles carry a title, a one-line subtitle and a department count, e.g. "Home & Decor / Decor, books & art for the walls / 3 departments".
  - Footer fine print: "Every piece is one of a kind, so when it's gone, it's gone." and "US shipping is included in each find's price" and "Ask away before you buy — measurements, flaws, anything."
  - A label strip whose text appears twice back to back in the page text (so likely a scrolling ticker, `inferred`): "One of a Kind / Vintage / Kitsch Forever / Maximalism / Freshly Hunted / More is More".
- Color (verified from HTML, role `inferred`): inline `background-color` values on the home page are `#FBF3E4` (8 uses, looks like the cream ground), then `#FF3E9A`, `#FF7A2F`, `#1FA98F`, `#7B68EE`, `#FFD6E8`, `#F4D03F`, `#E85D75`, `#E2434B`, `#C9A0FF`, `#8FD1D8`, `#FFB84D`. I did not map which element uses which. Cream page ground plus saturated tiles, not a full color-drench.
- Props and styling (`seen`, `raw/a2-img/kitschy-hero.jpg`, 1536x1024): a painted-orange shelf against a magenta wall, warm low light. Objects: pink flamingo, chrome ball on a tripod, three souvenir plates, leopard vase, brass pineapple, a small mirror ball, harlequin tumblers, plastic fruit. One shelf, one color story, a mirror ball and a chrome orb as the shine notes.
- **Watch out 1:** the plates and tumblers in that hero show gibberish lettering ("S MIRILLE"). It looks AI-generated to me; I cannot prove it. Steal the composition idea (one color-drenched shelf as a still life), shoot your real objects.
- **Watch out 2:** `/shop/` and `/shop-the-look/` rendered with no products in my crawl (product grids are loaded client-side; the site is a Next.js app, CSS path `/_next/static/css/`). That means crawlers and no-JS readers see an empty shop. Your native HTML site should ship the product cards as real markup.
- **Watch out 3:** 15 top-level groups (Style, Jewelry, Glasses/Hats, Home & Decor, Fab Kitchen, Beauty, Pop Culture, Holidays, Kids & Pets, Crafts, Fun Stuff, Fresh Finds, Ebooks, Consulting, Consignment). That is a thrift-mall shelf. You have four departments; do not copy the count.
- Also: "Local pickup in Decatur, GA" is theirs. Holliewood and Vine has no pickup; do not copy that line.
- **Steal this:** (a) the "Shop the Look" concept: three to six real pieces framed as one idea, each a tap from its own page; (b) subtitle microcopy under every tile; (c) the labeled music button; (d) the "Fine Print" footer block with "ask before you buy"; (e) "Freshly Hunted" as a tag instead of "New Arrivals".

## 2. The Old Above (lighting, one person, best spec block)

- Homepage: https://theoldabove.com
- Pages read: `/category/era/1970s/` (`a2-oldabove.md`), product `/product/1960s-hollywood-regency-brass-large-crystal-chandelier` (`a2-oldabove-prod.md`). Accessed 2026-10-27.
- What they do: restored vintage and antique lighting, owner-voiced ("Ross, vintage lighting expert"), WordPress/WooCommerce look (`inferred` from `/wp-content/`, `add-to-cart` links).
- Navigation is a facet list: **Room** (Bathroom, Bedroom, Dining Room, Hall/Foyer, Kitchen, Living Room, Porch), **Era** (Pre-1920 to 1970s, Art Deco, Mid-Century Modern), **Light Type**, **Light Style** (includes Hollywood Regency), **Home Style**, **Manufacturer**, **Colors** (Brass, Chrome, Pink, Gold, Orange and others) and **Matching Sets** ("A specialty here at The Old Above is whole house sets").
- Product page evidence (chandelier, "$2,780.00", "1 in stock", 10 photos): description in owner voice ("WOW!", "This is a very special chandelier."), then labeled blocks **DETAILS** ("candelabra base 25W bulbs (not included). Clear flame-style LED bulbs would look well."), **SIZE**, **CONDITION** ("I love writing this: there's no damage. Most of the sockets and their wiring are original (and in fine shape) with new paper insulators."), **SHIPPING** ("Insured shipping in the Continental US will be…FREE!"). Also "ready to hang, and comes with all the mounting hardware needed" and a "NOTE" about arms unscrewed for shipping. Related products show a price.
- Lamp photography (`seen`, `raw/a2-img/oldabove-chandelier.jpg`): chandelier hung and lit, bulbs on, crystals catching light, against a gold/ochre wall. Amateur but alive: you see what it does, not just what it is.
- **Watch out:** visually plain, no theater. The 1970s category page dumps every light on one infinite scroll ("ALL my lights will download, so you will not need to click Page 2").
- **Steal this:** a lighting spec block (bulb base and wattage, wiring new or original, hang drop and chain, shade included, ready to hang), shipping stated per item, and photographing every lamp lit and hung. Facets as filters (Room, Era, Color incl. Pink and Chrome), not as top nav; your stock is too small for eight menus.

## 3. Soho Home "Shop the Look" (room as navigation; new goods, copy the pattern)

- Homepage: https://www.sohohome.com/us/
- Pages read: `/us/inspiration/shop-the-look` (`a2-sohohome-look.md`), scene `/us/inspiration/shop-the-look/living-room/torno-sofa` (`a2-sohohome-scene.md`). Accessed 2026-10-27.
- Evidence: top nav tile "Interiors by Soho House / Discover our new collection by room". The index lists five rooms (Bedroom, Living room, Dining room, Bathroom, Outdoor), each with named scene tiles such as "Layered bedroom", "Sofa power", "Natural materials", "Modular style". A scene page is: wide room photo (`width=1000,height=500` crop in the image URL), a label and title ("Living room / Modular style"), one short paragraph, a link back to "All living room inspiration", then a row of product cards.
- The hover trick (verified from filenames): each card has a "Listing Image" and a "Hover Image". The hover images for the sofa and the chandelier carry the same frame id (`...mellow-house...4545-r2...`) as the scene hero, so hover shows the product in the room photo. That the swap happens on hover is `inferred` from the alt text "Hover Image".
- Margeaux cushion card shows color swatches and "+13 colours +2 shapes". Prices visible, e.g. "Elber Chandelier Regular price $2,595".
- **Watch out:** this is a rail of cards under a room photo, not pins on the photo. No hotspot overlay in the markup I read. New goods with stock depth, so "swap the colorway" logic does not apply to your one-of-ones.
- **Steal this:** index of rooms, named scenes ("Brass & Glass", "Pink Hour", "The Bar Cart"), one wide room photo, one sentence, then the three to six real objects, with a "gone" state when one sells (do not remove it; see Joy of Cocktails). Product card hover = object in the room.

## 4. The Joy of Cocktails (glass photography and condition grading)

- Homepage: https://thejoyofcocktails.com/
- Pages read: `/` (`a2-joyofcocktails.md`), `/pages/definitions-of-condition` (`a2-joc-condition.md`). Accessed 2026-10-27.
- Evidence, hero: "Behind Every Home Bar is a Story" and "The go to resource for planning, designing and styling your home bar". Nav has Home Bar Builds, Cocktails in Culture, Glassware Makers (about 17 maker pages), "Glassware Eras", "Glassware Glossary", "9 Essential Tips for Vintage Glassware Care".
- Evidence, condition scale (verbatim): Mint, Mint - Rare, Near Mint, Excellent, Excellent - Rare, Good, Good - Rare, Imperfect - Rare. Rules: "Excellent... light surface scratches, and maybe some wear to paint, gold gilt... No glassware with chips, flea bites or cracks can be labeled Excellent." Mint "may have 'as made' flaws such as air bubbles in the glass". And the disclaimer: "read the Condition Notes of any item you're interested in for detailed descriptions."
- Sold items stay up: featured products show "Sold out" at $71.99 and $109.99 next to an available $40.00 pair. (An archive of sold work doubles as proof you have good stock.)
- Glass photography (`seen`): product shot `joc-airtwist.jpg` is a stem macro on a **black ground with a mirror-like reflection under the foot**, air-twist spiral fully readable, small corner watermark. Hero `joc-hero.jpg` is a cut-crystal coupe with red drink, warm bokeh bottles and lights behind it: glass shown lit and in use, not on white.
- **Watch out:** standard Shopify chrome and testimonial cards; zero theater. Wording like "Mint" is a collector's scale, heavy for a quirky shop. Also their grade "Rare" is defined as "zero to minimal other online references", which is a claim you would need to verify per piece.
- **Steal this:** a site-wide short condition vocabulary (three or four grades max) plus a per-item "Condition Notes" block; black-ground macro for glass detail; one bokeh lifestyle hero that your pink neon and mirror ball can make.

## 5. Show Pony Palm Beach (Hollywood Regency "style edit", honest buying guide)

- Homepage: https://showponypalmbeach.com/
- Pages read: `/collections/hollywood-regency` (`a2-showpony.md`), product `/product/vintage-brass-and-crystal-parrot-sconce-7fe81cf8` (`a2-showpony-prod.md`). Accessed 2026-10-27.
- Evidence, collection page: eyebrow "The style edit", H1 "Vintage Hollywood Regency Furniture & Decor", intro "Build a room around a confident silhouette, a reflective finish or a beautifully detailed accent." Inclusion rule stated openly: "Pieces appear here when Hollywood Regency is recorded in the listing title or style." Buying guide under the grid: "Check reflective surfaces closely... Ask about scratches, chips, clouding, replacement glass and repairs" and "Separate style from attribution... 'After' and 'in the style of' describe a relationship to a design, not confirmed authorship." Listings: a leopard swag bench at "$2,850.00".
- Evidence, product page: sconce "895.00 USD", "Available", sections Description / Details (Condition "Very Good", Condition notes, Period "Mid 20th Century Style", Style "Hollywood Regency", Materials, Dimensions) and an "Item number" (`SP0826-OW-610353`). Returns text: "Returns require contact within 2 days of delivery for an item significantly not as described or a wrong item; change of mind is not eligible."
- Images: first image file is named `bg-removed-...webp`; five more real photos follow (`additional photo 1-5`). I pulled the first (`seen`, `raw/a2-img/showpony-cutout.png`): a clean RGBA cutout of the parrot sconce, 800x800. So: cutout first, real photos after. That is the same approach you already use for the transparent styling pieces.
- **Watch out:** the description text reads like generated boilerplate ("exemplifies the decorative artistry of early to mid-20th-century lighting design", "pleasing patina indicative of its age and quality materials"). Patina notes should say what the patina is: where, how much, what it looks like. Two-day return window is stingy; verify your own policy against Etsy and Shopify rules separately (not researched here).
- **Steal this:** collection page as "style edit" with a short buying guide underneath; the "how pieces get into this collection" honesty line; the attribution language (maps directly to signed items and memorabilia: say "signed, unverified" or "verified, how"); an item number on every listing; cutout first image, real photos after.

## 6. Palm Springs Regency (curator origin story)

- Homepage and page read: https://palmspringsregency.com/ (`a2-regency.md`). Accessed 2026-10-27.
- Evidence: "THE Curators Corner... I am a third generation Curator. My mom Toni and her mom, my Little Grandma, Mary are my style icons" followed by a strip of what look like family 1960s photos (alt text: "1966 Chinese modern Silk Tufted Sofa and early shag carpet"). Copy references avocado shag and plastic-covered tufted silk sectionals.
- **Watch out:** it is a page-builder site that mostly redirects to Chairish and Kashew; "over 3,500 curated items... lists about 1200... About 250-300 pieces are available for purchase" and the catalog link is a Google Photos album. Showing what you cannot sell is the anti-pattern. Leftover alt text "EchoLuxe logo" is a template slip.
- **Steal this:** an About page that uses real photos of the person's own childhood rooms as the origin. Yours is the burgundy room and the neon; use real photographs of it.

## 7. Kelly Wearstler (luxury contrast, not vintage)

- Homepage and page read: https://www.kellywearstler.com/ (`a2-wearstler.md`). Accessed 2026-10-27.
- Evidence: Shop menu has Furniture, Lighting, Decor, Tabletop, **Materiality**, Featured. Hero tile reads "Entertaining" and links to the tabletop collection; the hero asset path contains `preview_images/...thumbnail`, which indicates a video poster (`inferred` from the URL only).
- Fit: low for a vintage shop (new goods, luxury). **Steal this:** one idea only, "Materiality" as a browse axis. For you that is Brass / Glass / Chrome / Pink / Lucite. Cheap to build as a filter row.

## 8. The Hour Shop (closed; taxonomy example only)

- Homepage and page read: https://thehourshop.com/ (`a2-hourshop.md`). Accessed 2026-10-27.
- Evidence: top line "The Hour is permanently closed. Thank you for 16 wonderful years!!" The nav is still live: Barware, Glassware (Collins, Coupe, Tiki, Roly Poly...), Shakers, Pitchers & Decanters, Bowls & Trays, and a "Designers" list of roughly 70 maker pages (my count of the raw file) incl. Blenko, Dorothy Thorpe, Georges Briard, Fenton.
- **Steal this:** nothing visual. Only the lesson that maker pages are how glass people search (Georges Briard, Dorothy Thorpe). A maker tag on each glass listing is free; a maker index is overkill at your stock size.

## 9. Retro Solstice (checked, thin)

- Homepage and page read: https://retrosolstice.com/ (`a2-retrosolstice.md`). Accessed 2026-10-27.
- Evidence: rotating hero lines "Entertain In Style / With Mid-Century Glassware" and "Reuse, Repurpose, Redesign / Vintage Glassware"; banner "FREE SHIPPING ON ALL US DOMESTIC ORDERS $300 OR MORE!"; featured "Anchor Hocking - Mid-Century Black Square with 22-Karat Gold Atomic Burst Glasses (Set of 11)".
- Verdict: a competent glassware store with no room, no story and no style. Only takeaway is a free-shipping threshold line in the top bar; whether that suits quantity-1 stock is your call.

## Checked and rejected (so nobody redoes them)

| Site | URL read | Why not |
|---|---|---|
| Curiouz | https://curiouz.com/ | "Rare pieces, authenticated and delivered to your door." plus a four-item trust strip (vetted dealers, door-to-door delivery, 14-day returns, secure payment) and an "As seen in" logo row. Polished, sterile, and "authenticated" is a promise you cannot make on most of your stock. |
| Pamono | https://www.pamono.eu/vintage-lighting | Marketplace grid. Only warm copy: "shopping for vintage lighting is like taking a stroll through all the brightest spots in design history". |
| Oblist | https://oblist.com/ | Mixed new and vintage. Has "By Rooms" nav and "A singular curation of contemporary and vintage objects"; no scenes. |
| Jonathan Adler | https://jonathanadler.com/pages/shop-the-gallery | The URL returned a mega-nav and store-locator, not a shoppable gallery. Any "gallery" claim is UNVERIFIED. New goods anyway. |
| Lulu & Georgia | https://www.luluandgeorgia.com/collections/dining-details | Ordinary collection grid; no hotspot or scene in what I read. |
| McGee & Co | https://www.mcgeeandco.com/pages/shop-the-look-living-room | Nav has "Shop Dining Room Looks", "Shop Bedroom Looks"; I did not read a scene body. UNVERIFIED beyond the nav labels. |
| Vinterior | https://www.vinterior.co/ (blog guide read) | Generic buying guide. Page contradicts itself: "100,000 individual pieces" in the body versus "More than 200,000 products" in the module. 100,000 verified as written, 200,000 need review (the article path dates to 2019, so the body is probably stale; `inferred`). Useful crumb: filters for "price, dimensions, style genre, product type and condition", and a content series called "Colour Edit". |
| That Retro Piece | https://thatretropiece.com/ | Glass browsable "by Region" (American, Czech, Italian Murano, Nordic...). Plain; the region axis is a collector's axis, not a mood. |

## Blocked, failed, or UNVERIFIED

- Rejuvenation vintage (https://www.rejuvenation.com/shop/vintage/ and `/pages/antiques-vintage/`): walled, 123 bytes both times. Not evaluated.
- Vintage Murano Gallery (https://www.vintagemuranogallery.com/): 572 bytes, walled. Not evaluated.
- House of Hackney (https://www.houseofhackney.com/en-intl/): crawl hung, no output. Not evaluated.
- Four first-attempt crawls hung; I stopped that job and deleted their 0-byte output files (`a2-hackney`, `a2-kitschy-look`, `a2-murano`, `a2-retropiece`). The retries that worked are `a2-kitschy-look2.md`, `a2-retropiece2.md`, `a2-murano2.md` (walled, 572 bytes).
- `raw/a2-img/` holds five photos from other businesses' sites and `raw/a2-kitschy-home.html` is a copy of a third-party page. They are evidence only, copyrighted by their owners; do not commit or republish them. The report cites them by filename.
- Kitschy "Shop the Look" grid and `/shop/` product list are client-rendered; I verified the copy but not what the look tiles contain.
- Rendered color, spacing and motion on every site: `inferred` or not covered, except where I marked `seen`.
- Not researched: AURA Modern Home's "Free Shoppable Hotspot Image Maker" (turned up in search; no page read). Do not cite it as a method.

---

## Ranked recommendations for Holliewood and Vine

Ranked by fit (burgundy room, one-of-ones, theatrical, one person) and by cost.

1. **"Shop the Room" scene pages** (Soho Home pattern + Kitschy "Shop the Look"). A wide photo of the real room, a title, one sentence, a rail of the real pieces in it, sold pieces stay with a "gone" tag. Hover on a card shows the object in the room photo. Cost low, fit highest. This is the page that turns a catalog into "a room you walk into".
2. **Condition vocabulary plus per-item condition notes** (Joy of Cocktails, Show Pony, Old Above). Three or four grades site-wide, then one sentence per item saying where the wear is and what it looks like. Replace "pleasing patina" with specifics. Cost low, cuts returns and builds trust. Carry the same wording to Etsy and Shopify.
3. **Lighting spec block on every lamp** (Old Above): bulb base and wattage, wiring new or original, cord length, hang drop, shade included, tested lit. Cost low, lamps are your hero category.
4. **Photograph light and glass the way they behave** (Old Above lit and hung; Joy of Cocktails black-ground macro plus one bokeh hero; Show Pony cutout first, real photos after). You already have cutouts and a pink neon; one bokeh shot and one dark-ground glass macro per glassware item is the missing piece.
5. **Style-edit collection pages with a short buying guide** (Show Pony): "Brass & Glass", "Pink Hour", "Hollywood Regency". Include the honesty rule ("pieces appear here when the listing says so") and a one-line attribution policy for signed items and memorabilia. Cost low, trust high, and it is SEO text.
6. **"Shop by Vibe" tiles, capped at about six, with a one-line subtitle each** (Kitschy). Add "Materiality" as a filter row (Kelly Wearstler idea): Brass / Glass / Chrome / Pink / Lucite. Do not copy their 15 groups.
7. **Fine-print footer in the shop's voice** (Kitschy): "one of a kind, when it's gone it's gone", shipping line, "ask before you buy: measurements, flaws, anything". Remove the pickup line.
8. **About page from real photos of the actual room** (Palm Springs Regency "Curators Corner"). Cost low.
9. **A labeled music control in voice** (Kitschy "Tap to play a little funk"). You already have music; label it like a character, do not autoplay (browser autoplay behavior not verified here).
10. **Real hotspot pins on the room photo.** Nobody I read does this for vintage. It is a differentiator and a build cost; do it after #1 works, as plain `<a>` elements positioned over the image so it stays native HTML and accessible.

**Gimmicks or poor fit:** Curiouz-style trust strips with "authenticated" claims; a 70-maker index (Hour Shop); 15 top-level categories; "AI boilerplate" descriptions (Show Pony); showing inventory you cannot sell (Palm Springs Regency); marketplace grids (Pamono, Oblist); server-hidden product grids (Kitschy's client-rendered shop).

## Page patterns worth copying (each tied to its source)

| Section | Pattern | Seen at |
|---|---|---|
| Hero | Punny one-line headline over a single color-drenched still-life shelf, two CTAs, a labeled music control | Kitschy Maximalist (shelf photo `seen`; button text verbatim) |
| Hero | Lit glass in use, shot close with warm bokeh behind it, one sentence, two buttons | Joy of Cocktails (`seen`) |
| Collection tile | Room-scene tile with a name ("Layered bedroom"), not a category | Soho Home |
| Collection tile | Title + one-line subtitle + department count | Kitschy "Shop by Vibe" |
| Collection page | Eyebrow "The style edit", H1, inclusion rule, grid, buying guide underneath, "Keep exploring" cards with one-sentence pitches | Show Pony Palm Beach |
| Scene page | Wide room photo, label + title, one paragraph, product rail, hover image = in-room shot | Soho Home (hover matching verified by filename) |
| Product page | Labeled DETAILS / SIZE / CONDITION / SHIPPING in owner voice, "1 in stock", 10 photos, ready-to-hang note | The Old Above |
| Product page | Condition grade + condition notes + period + materials + dimensions + item number | Show Pony Palm Beach |
| Product page | Site-wide condition definitions page linked from every item | Joy of Cocktails |
| Product images | Transparent cutout as image 1, real photos as 2 to N | Show Pony Palm Beach (`seen`) |
| Product images | Glass on black with reflection and a small corner watermark | Joy of Cocktails (`seen`) |
| Product images | Lamp hung and lit against a colored wall | The Old Above (`seen`) |
| Footer | "The Fine Print" block: one-of-a-kind line, shipping line, "ask before you buy" | Kitschy Maximalist |
| Footer | "Join my email list and get updates when lights are added to the shop!" (lights-only list) | The Old Above |
