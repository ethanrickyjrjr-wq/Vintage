# Holliewood and Vine

A sample storefront showing all 52 selected transparent product photographs on white panels, with illustrative prices, saved finds, a browser-local shopping bag and room decorating. The original neon-lit room remains the inspiration photograph. No package installation is required.

## Preview

From this directory run `node dev.mjs`, then open http://127.0.0.1:4173. Set `PORT` if that port is busy. Room photos and layers stay in the browser; Decorate downloads its model and runs locally.

## Build

Run `node build.mjs`. Static assets go to `dist/client/`, with the storefront at both `/` and `/storefront.html`. The room API is built as a dependency-free Worker in `dist/server/`. The build cleans only this site's generated `dist/` directory.

## Content and behavior

- `catalog-data.js` preserves the 35 original inventory records and researched guide prices. `demo-products.js` replaces the active public collection with the 52 selected samples, seven useful categories and explicitly illustrative prices. Original inventory research is not applied to samples.
- `catalog.js` displays the complete collection without pagination and handles category filters, search, price sorting, saved finds, item details and the sample bag. Saved finds and the bag stay in the current browser. Checkout is visibly unavailable; no orders or payments are taken.
- `storefront.js` handles entrance reveals, the color theme and the header shortcut to saved finds.
- `homepage.css` adds the sticky navigation, category shortcuts, responsive controls and the public showroom entry points. The collection precedes the longer room story. The header's Saved finds shortcut resets category/search filters so it always shows the whole saved collection.
- `showroom.html` is the public 3D showroom, with eleven licensed sample models, camera presets, colorways, backdrop selection and an on-demand five-angle gallery. It includes individual attribution. The build now also ships the 52 selected sample photographs from `assets/demo/`, along with the models and viewer; raw downloads, unselected images, private review pages and cutout experiments remain excluded.
- `assets/thumbnails/` contains 480px and 960px WebP derivatives for catalog and homepage delivery, including 104 transparent sample derivatives. Full sample images remain the detail and room-placement assets. When replacing a sample, prepare its matching derivative files before publishing.
- The real room's optimized photos, extracted frames, video and licensed fonts are self-hosted in `assets/`.
- `atmosphere.css` composes the entrance as a burgundy interior: raised lettering, a foreground lamp, a hanging chandelier, framed art and a disco ball. Category displays have varied proportions and frames. The original room is presented as the source of the designer's approach, not as an operating physical store.
- The entrance lamp, chandelier and painting open catalog details. The top disco ball starts off; clicking or tapping toggles spinning, projected mirror reflections and music together. Both balls and the reflected light share one rotation clock: one turn per 64 beats, using the composer's published tempos (118, 120, 115 and 120 BPM). A Web Audio analyser reads actual bass attacks for restrained brightness accents; small, crisp reflections follow mirror-ray geometry rather than preset paths. `disco-music.js` plays one of four Kevin MacLeod disco tracks (`assets/music/`, CC BY 4.0, credited in the footer and in a "now playing" pill): each start plays the next song, a finished song rolls into the next, and the cycle position is remembered in localStorage. Nothing loads before a tap; audio and animation stop when the page is hidden. To drop a song, delete its mp3 and its row in the `tracks` list. Reduced-motion settings keep music available while suppressing the moving lights and sphere animation. The buyer-gift section remains below. Copy reflects the owner's stated handout tradition without promising a gift with every order.
- Normal openings and reloads start at the top, including old `#disco` links. Product and collection deep links still work.
- Original catalog photographs remain unchanged. AI-assisted editorial cutouts are separate in `assets/editorial/`, with smaller responsive variants for phones. Asset prompts, provenance and the design audit are recorded in `../docs/storefront-art-direction.md`.
- Homepage photography uses responsive original exports. Builds omit unused large exports and walkthrough frames. The earlier category research remains in `../research/design-2026-10-26.md`; the dimensional direction supersedes its equal-frame recommendation.
- `sample-shop.css` keeps the burgundy entrance and white product panels, including details and room controls. Item details link each source photograph. All public catalog prices are illustrative sample prices. The original price research and preparation labels remain in `catalog-data.js` for future actual listings.

The original Claude artifact is a separate preview; editing these files does not change it. Site identity and hosting configuration live in `.openai/hosting.json`.

## Try it in your room

`#your-room` accepts a room photo or the generated example in `assets/rooms/`. Build a tray of picks, drag them onto the photo (or choose Place), then drag, resize, flip, bring forward or remove each independent layer. Touch users can place with a button and drag with a finger; the size slider and arrow keys provide alternatives. Contact shadows are drawn locally. Undo restores layouts, comparison shows the original, and PNG downloads omit selection handles and include a placement-sketch label. Photos and layouts are held only in tab memory and clear on reload.

Decorate with my favorites reads the catalog's saved finds, including same-tab/session-only saves; Decorate with my picks reads only the tray. Each creates a fresh, undoable starting layout. `room-segmentation.js` lazily loads pinned Transformers.js 4.3.1 and the 44.5 MB q8 DETR panoptic model in a dedicated single-thread WASM worker. `room-layout.js` converts masks into conservative candidate slots and assigns numeric positions deterministically. Lamps require an inferred side table or broad cabinet; generic tables cannot receive lamps. Missing cutouts, unsupported finds, uncertain surfaces and items that cannot fit are explicitly listed. Model failure or cancellation preserves the prior layout and manual editing. Mask errors remain possible; proportions are visual estimates, not measured inches.

Four styling assets are available: the existing editorial urn lamp/chandelier and newly rectified original A3/A4 paintings. The proposed A5/A22/A8/A9/A10 cutouts failed visual source review and remain unavailable, along with seven video-still items. See `../docs/room-cutout-review.md` and `../research/room-editor/03-browser-benchmark.md`.

The old `room-worker.mjs` / private Klein service remains archived for possible future lighting/shadow polish. The editor makes no requests to it, and publication sets `ROOM_PREVIEW_ENABLED=false`. Replace is absent. No generative model chooses placement. Room-guide asset download failures get one fresh-worker retry; cancellation and inference failures do not restart the model. Any later polish needs its separate ten-run quality/quota test before re-enabling a service. Existing renderer secrets stay only in Sites runtime settings. Run `npm test` for layout safeguards and the retained legacy server tests. See `../docs/room-preview.md` for implementation and verification details.
