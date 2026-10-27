# Private styling photo pack

October 27, 2026. Ricky requested clearer photographs of similar pieces for a
private demonstration of the storefront and real-time room decorating. His
follow-up emphasized keeping the existing style and using ready-made transparent
images from Google Images where possible. Nothing in this task is published.

Run `node dev.mjs` from `site/`. Open `/demo#your-room` for the storefront with
the sample photos, or `/demo-photos.html` for side-by-side comparisons and sources.
The sample room loads automatically in the demo. Each replacement is labeled as a
styling sample; it does not inherit the original item's research price.

The private storefront and review page use a white background throughout, with
burgundy type and buttons. Image panels, room controls and details share that white
surface, so a source photo's white background does not form a cream-bordered box.
Saved evening-mode preferences do not darken this preview. The painted mannequin
remains a source photograph rather than a transparent placement layer.

`site/assets/demo/` contains source-photo exports, ten transparent replacement
cutouts, three additional ready-made transparent options, and `sources.json`.
The latter records source pages, direct image URLs, dimensions, alpha, processing,
and the final built-in imagegen prompts where extraction was needed. Original
downloads and full-resolution generated PNGs remain in ignored local artifacts and
Codex's generated-images directory. Source exports retain the downloaded composition.

| Item | Selected replacement and style match | Preparation |
| --- | --- | --- |
| A13 | Gold Egyptian bust lamp, wide cream rectangular shade | Imagegen background extraction |
| A14 | Seated upright spotted ceramic leopard, complete paws and curled tail | Imagegen background extraction |
| A15 | Low black wood armchair, rust/cream/black Southwestern star pattern | Imagegen background extraction |
| A16 | Dark cherry wood tabletop radio, horizontal grille and near-round dial | Existing transparent PNG from PNGimg |
| A17 | Brass reservoir, short pedestal and clear chimney | Imagegen background extraction |
| A19 | Brown-and-white cowhide with natural outline | Imagegen background extraction |
| A20 | White accordion/honeycomb paper chair, rather than natural cardboard | Imagegen background extraction |
| A10 | Vintage peach-rose champagne coupe | Existing transparent PNG from Options |
| A8 | Pair of silver head-and-neck mannequin busts | Imagegen background extraction |
| A9 | Black vintage two-reel projector | Existing transparent PNG from Wallpapers.com |
| A22 | High-resolution colorful painted mannequin torso | Source photo only; image service declined extraction |

Extra ready-made options are a matching rose flute, a pale pink faceted coupe,
and a black-and-cream cowhide. The white mannequin head, all-fours leopard, natural
cardboard chair, and unrelated lamp shapes were not selected. The radio is a visual
stand-in for the original radio/record player; it is not the same device. The torso
differs from the original full-body dress form and stays unavailable for placement.
Glass photos retain pale highlights inside the bowls; these are approximate styling
overlays. Sources document the borrowed photos, not permission for public use.

The existing urn lamp, chandelier and original A3/A4 artwork are retained. Actual
inventory photographs in `catalog-data.js` are unchanged. `/demo` injects only local
sample data. `build.mjs` excludes the whole borrowed-photo directory, and its
explicit source list excludes the demo scripts, review page and stylesheet.
This task does not change the published storefront's audience or deployment.

## Round two: more transparent pieces (2026-10-27)

Ricky asked for more items in the shop's style with transparent backgrounds and good
resolution. Three Sonnet scouts (decor and lighting, furniture and textiles, fashion
and accessories) returned 41 pieces, all ready-made alpha from pngimg.com
(CC BY-NC 4.0, private demo only). They sit under `alternatives` in
`site/assets/demo/sources.json` and render grouped on `/demo-photos.html`. They are
review material only: none is wired into `/demo`'s room editor or `demo-products.js`.

Gate: RGBA with alpha 0 to 255, long side at least 1000 px, whole subject, no
watermark or person, checked on burgundy and white. Sources are 900 to 8000 px;
`site/assets/demo/` WebPs are trimmed and capped at 1600 px. Per-scout records,
including rejects and gaps, are `research/demo-photo-sourcing/round2-*.json`. A
cross-lane duplicate mirror was dropped, as was a 1000 px shag rug.

Caveats: the three disco balls are rendered illustrations, not photographs. The ruby
lamp has a faint fringe and the oval mirror a hard edge at 100% zoom. Tight crops
touch their canvas edges (tangent contact, not clipping). Still not found as hi-res
alpha: fringed western boots, feather fascinator, studded chain belt, clear mules,
blush trench, neon windbreaker, ceramic animal figurines, black-and-gold shaker, a
photographic disco ball, a record-player console and a jukebox. pngall, purepng, pngegg
and Wikimedia Commons were queried but never crawled.

## Verification

Pixel checks confirm genuine transparent surroundings on all ten replacement
cutouts. Warm-background review checks complete silhouettes and baked checkerboards.
The review page links every full-size source and original listing. Browser QA checks
sample-room loading, multiple new cutouts, independent placement, keyboard movement,
and the review page. The twelve existing room-service tests pass. The publication
build is checked separately for absence of all demo assets, scripts and pages.
This does not validate the other session's automatic room arrangement.

Vendor references checked through crawl4ai in this session:
[Node HTTP responses](https://nodejs.org/api/http.html),
[Pillow image operations](https://pillow.readthedocs.io/en/stable/reference/Image.html),
and [WebP encoding](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#webp).
