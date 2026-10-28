# The sample storefront

October 28, 2026. Ricky requested the complete polished photo collection on the live homepage,
presented as the shop could look with good product photography. The previous publication shipped
the original inventory catalog and explicitly excluded the selected photographs, leaving the work
visible only through the local `/demo` route.

The homepage now initializes `demo-products.js` before the catalog and room editor. It supplies all
52 unique selected photographs, seven shopping categories, descriptions, source links and explicit
sample prices. Original inventory records and their price research remain in `catalog-data.js`.
Sample prices are independent of those research estimates.

The complete product grid sits immediately after the entrance/category navigation, ahead of the
larger category displays, 3D showroom invitation and room story. Every listing appears without a
load-more step. Transparent images sit on pure white framed panels and use `object-fit: contain`
in cards, details and the room controls. The room editor uses each listing's exact full-size image
as its transparent placement layer for home goods. Fashion items are excluded from the room editor.

The entrance keeps its burgundy composition, dimensional type, pointer depth and disco controls.
Ricky's correction on October 28 restores the original brass-and-cream urn lamp, sea-glass
chandelier and cubist painting. These signature entrance objects must not be replaced with sample
catalog photographs. Their click targets keep the original titles, photos and guide prices,
separate from the 52 sample listings. White belongs to the product-photo framing; page backgrounds
remain burgundy in both lighting palettes. The original neon-lit room photograph remains.
The owner’s original mirror selfie appears in the owner section. Rough catalog photography,
walkthrough-derived listings and the superseded generated room video are omitted from the homepage.

Cards and details offer Add to bag. The bag persists locally in this browser, limits each unique
sample piece to one entry, supports removal and calculates its subtotal. Saved finds still work
independently. Prices are labeled as illustrative; the checkout control is disabled and says
Checkout coming soon. No inventory, orders, payments or shipping are connected.

`build.mjs` whitelists the 52 selected photographs from `assets/demo/`, plus the existing public
3D models/viewer. It includes `demo-products.js`, `sample-shop.css` and 104 responsive transparent
WebP derivatives in `assets/thumbnails/`. Raw downloaded source exports, unselected alternatives,
the photo-comparison page, cutout lab and source-processing manifest remain excluded. Each listing
links its original photograph source; the source record does not assert ownership of a piece.

Validation covers the complete catalog and room-image mapping, separate sample prices, every
responsive asset, initialization order, existing room layout/server safeguards and the packaged
public image paths. Browser QA checks desktop/phone layout, filters/search/sorting, saved finds,
bag persistence/removal/subtotal, full item details and transparent room placement.
