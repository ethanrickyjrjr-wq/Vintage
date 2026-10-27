# Hollywood and Vine

A buildless storefront redesign using the actual shop photography and 24-second room walkthrough. No package installation is required.

## Preview

From this directory run `python -m http.server 4173 --bind 127.0.0.1`, then open http://127.0.0.1:4173/storefront.html.

## Build

Run `node build.mjs`. The deployable static site is written to `dist/`, with the storefront at both `/` and `/storefront.html`.

## Content and behavior

- `catalog-data.js` preserves the 35 original inventory records (34 browsable finds and the owner) and researched guide prices.
- `catalog.js` handles shelf filters, search, price sorting, saved finds, pagination, details and the room video. Saved finds stay in the current browser.
- `storefront.js` handles entrance reveals, the color theme and the header shortcut to saved finds.
- The real room's optimized photos, extracted frames, video and licensed fonts are self-hosted in `assets/`.
- `atmosphere.css` composes the entrance as a burgundy interior: raised lettering, a foreground lamp, a hanging chandelier, framed art and a disco ball. Category displays have varied proportions and frames. The original room is presented as the source of the designer's approach, not as an operating physical store.
- The entrance lamp, chandelier and painting open catalog details. The top disco ball starts off; clicking or tapping toggles spinning, sweeping mirror reflections and an original instrumental disco groove together. `disco-music.js` synthesizes the music locally after a tap; audio stops when the page is hidden. Reduced-motion settings suppress the visual animation. The buyer-gift section remains below. Copy reflects the owner's stated handout tradition without promising a gift with every order.
- Normal openings and reloads start at the top, including old `#disco` links. Product and collection deep links still work.
- Original catalog photographs remain unchanged. AI-assisted editorial cutouts are separate in `assets/editorial/`, with smaller responsive variants for phones. Asset prompts, provenance and the design audit are recorded in `../docs/storefront-art-direction.md`.
- Homepage photography uses responsive original exports. Builds omit unused large exports and walkthrough frames. The earlier category research remains in `../research/design-2026-10-26.md`; the dimensional direction supersedes its equal-frame recommendation.
- All prices remain provisional research guides. This preview does not accept orders or payments. Mature magazine covers require an explicit reveal. Attribution and authentication notes remain in item details.

The original Claude artifact is a separate preview; editing these files does not change it. Site identity and hosting configuration live in `.openai/hosting.json`.
