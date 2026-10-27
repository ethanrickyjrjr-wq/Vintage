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

## Polished-photo preview, October 27

Reading this as: a photography refresh for the vintage storefront, preserving the
existing layout and mouse interactions while presenting whole items on white mats.
The existing editorial typography, burgundy accents, varied category frames and
hover transforms remain. Design variance / motion intensity / visual density stay
at 7 / 5 / 4; this pass adds no motion or design-system dependency.

`/demo` now uses 52 selected, complete product photographs from the original photo
pack and Sonnet's additional sources. A single list in `site/demo-products.js`
feeds the collection, product details, saved finds, room picker and placement
layers. Every placement layer uses the same transparent image as its catalog card.
White image panels use a thin outer frame and inset mat; category frames keep their
existing tilt and hover lift. Clothing and accessories can be placed manually;
automatic arrangement still leaves unsupported kinds out with an explanation.

Ricky explicitly kept the original neon-lit store photo (`IMG_6610--960.webp`).
The entrance lamp, chandelier, painting and disco-ball composition also remain.
Other rough shop photos, video stills, the incomplete mannequin and the mirror
selfie no longer appear in the preview. Print has no selected polished replacement
and is omitted from this pass. Room-tour links lead to the kept store photograph.
The earlier room-render video is hidden because it uses the superseded item mix.

The three new illustrated disco balls are not product photographs and were not
selected. Duplicate mirror files are represented once. The rest of the approved
photographic alternatives, including the rugs and additional seating, are browsable.

Borrowed samples have no inherited inventory prices or availability claims. Their
source notes remain in `site/assets/demo/sources.json` and the round-two manifests
in `research/demo-photo-sourcing/`. `catalog-data.js` retains the actual inventory.
The owner introduction remains as text while its unfinished selfie is omitted.

This is the private review pass. `/demo` injects the photo list and white framing;
`build.mjs` continues to exclude all demo assets, scripts and review pages. It does
not change the published storefront or its audience.

## Verification

The polished-photo refresh passes the existing 19 room-layout/server tests and the
publication build. A data check confirms 52 unique samples, matching catalog and
room images, real transparency in every selected WebP and no inherited inventory
prices. The public build still omits the private photo pack.

Browser review verified the eight initial framed cards, full-image product details,
52 room choices, placement of the pink lamp and emerald chair, and dragging the
chair as an independent transparent layer. A 390-pixel phone viewport shows two
card columns without page overflow. The original neon-lit room photograph remains;
no other rough photographs appear outside the retained entrance composition.

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
