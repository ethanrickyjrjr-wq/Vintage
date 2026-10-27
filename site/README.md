# Hollywood and Vine

A storefront using the actual shop photography and 24-second room walkthrough, with a small Worker for private room previews. No package installation is required.

## Preview

From this directory run `node dev.mjs`, then open http://127.0.0.1:4173. Set `PORT` if that port is busy. Local preview supports uploads and placement sketches; it makes no model calls.

## Build

Run `node build.mjs`. Static assets go to `dist/client/`, with the storefront at both `/` and `/storefront.html`. The room API is built as a dependency-free Worker in `dist/server/`. The build cleans only this site's generated `dist/` directory.

## Content and behavior

- `catalog-data.js` preserves the 35 original inventory records (34 browsable finds and the owner) and researched guide prices.
- `catalog.js` handles shelf filters, search, price sorting, saved finds, pagination, details and the room video. Saved finds stay in the current browser.
- `storefront.js` handles entrance reveals, the color theme and the header shortcut to saved finds.
- The real room's optimized photos, extracted frames, video and licensed fonts are self-hosted in `assets/`.
- `atmosphere.css` composes the entrance as a burgundy interior: raised lettering, a foreground lamp, a hanging chandelier, framed art and a disco ball. Category displays have varied proportions and frames. The original room is presented as the source of the designer's approach, not as an operating physical store.
- The entrance lamp, chandelier and painting open catalog details. The top disco ball starts off; clicking or tapping toggles spinning, sweeping mirror reflections and music together. `disco-music.js` plays one of four Kevin MacLeod disco tracks (`assets/music/`, CC BY 4.0, credited in the footer and in a "now playing" pill): each start plays the next song, a finished song rolls into the next, and the cycle position is remembered in localStorage. Nothing loads before a tap; audio stops when the page is hidden. To drop a song, delete its mp3 and its row in the `tracks` list. Reduced-motion settings suppress the visual animation. The buyer-gift section remains below. Copy reflects the owner's stated handout tradition without promising a gift with every order.
- Normal openings and reloads start at the top, including old `#disco` links. Product and collection deep links still work.
- Original catalog photographs remain unchanged. AI-assisted editorial cutouts are separate in `assets/editorial/`, with smaller responsive variants for phones. Asset prompts, provenance and the design audit are recorded in `../docs/storefront-art-direction.md`.
- Homepage photography uses responsive original exports. Builds omit unused large exports and walkthrough frames. The earlier category research remains in `../research/design-2026-10-26.md`; the dimensional direction supersedes its equal-frame recommendation.
- All prices remain provisional research guides. This preview does not accept orders or payments. Mature magazine covers require an explicit reveal. Attribution and authentication notes remain in item details.

The original Claude artifact is a separate preview; editing these files does not change it. Site identity and hosting configuration live in `.openai/hosting.json`.

## Try it in your room

`#your-room` accepts a room photo or the generated example in `assets/rooms/`. Shoppers can mark a spot, let Decorate choose a spot, or mark/describe an existing item to replace. Four local styling overlays stay exactly where placed and can be kept in the photo, combined with more finds, or undone without using the image service. The private renderer supports all 16 room-friendly inventory references; AI may adjust placement and product details. Original product photos are used as AI references, with artwork rectified in memory to exclude the shop wall. Results support original/preview comparison, undo, reset, and PNG download. Downloads are labeled as sketches or AI styling previews.

`room-worker.mjs` sends bounded, validated requests to the private Hugging Face Space described in `../room-renderer/`. It uses FLUX.2 Klein 4B on free ZeroGPU, with no paid API fallback. Images remain in memory; EXIF metadata is removed before sending. A D1 counter allows three previews per connection per UTC day and 30 across the shop. Provider failures refund the counter. The same free Hugging Face account's compute allowance is shared with other apps and may impose a lower effective limit or a queue.

Hosted runtime values are `ROOM_PREVIEW_ENABLED=true`, `ROOM_RENDERER_URL`, and secret `HF_TOKEN`. These belong in Sites runtime settings, never in JavaScript, the hosting manifest, or a committed environment file. `drizzle/0000_room_preview_usage.sql` creates the counter table during deployment. Run `node --test tests/room-worker.test.mjs` for server validation. See `../docs/room-preview.md` for the renderer archive, asset provenance, and verification record.
