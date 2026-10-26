# Hollywood and Vine: a room made for the web

October 26, 2026. This pass follows the owner's correction that the site should express the designer's way of putting things together, rather than represent the original physical store as still operating. The owner also confirmed that disco balls are an important buyer handout.

## Design read and audit

Reading this as an expressive vintage storefront for people drawn to eclectic objects and fashion, with a theatrical interior language built in native HTML/CSS. Retain the existing Bodoni wordmark, burgundy, cream and pink identity. The serif is justified by the existing vintage brand. No framework or UI library migration.

The previous composition used a symmetrical split hero, a flat color field, equal portrait category tiles, and repeated headline treatments. The original room's objects supplied personality but the page offered little difference between background and foreground. The room story described a physical shop in the present tense.

Existing dials: DESIGN_VARIANCE 5, MOTION_INTENSITY 4, VISUAL_DENSITY 4. Target: DESIGN_VARIANCE 8, MOTION_INTENSITY 5, VISUAL_DENSITY 4. Desktop uses varied scales, offsets, cast shadows, framed images and a ledge. Mobile explicitly repositions the scene; the browsing categories and product grid keep two columns for comparison. Both lighting palettes remain in the same burgundy family. Frame treatments deliberately reference different objects; the functional buttons stay rectangular.

## Implementation

- The entrance has background wall molding and framed art, raised text in the middle, and transparent lamp/chandelier assets in front. A small hanging disco ball links to the gift section.
- Pointer depth is bounded to a few pixels and uses one requested animation frame per pointer update. Touch and reduced-motion settings disable it. Automatic disco rotation was removed after the performance audit showed it extending the largest-contentful-paint measurement.
- The four category displays vary in frame, aspect ratio and elevation. Their names, links and filters remain intact.
- The room story explains the mix of chrome, brass, pink glass and art. Its object links open original catalog details.
- The gift section says: “A little gift for our buyers: a mirror ball to carry the Hollywood & Vine feeling home.” It does not assert gift eligibility, fulfillment timing, dimensions, or a gift with every order.
- Search, sorting, pagination, saved finds, item links, guide prices, preparation/authentication notes and mature-cover consent remain in place. Saved counts are included in the header's accessible name.
- The tour is identified as the original room and does not preload its video. Editorial images use responsive WebP variants. Original item photographs are not replaced with generated images.

## Editorial asset provenance and final prompts

Generated with the built-in imagegen tool, then resized and encoded with Sharp while preserving alpha. These are decorative compositions, not condition or authenticity evidence. Original generated PNGs remain in the local Codex generated-images folder. Production files are in `site/assets/editorial/`.

### urn-lamp.webp and urn-lamp--400.webp

Edit target: `site/assets/photos/IMG_6616.webp`.

Final prompt: Use case: background-extraction. Edit target: supplied photograph of the brass and cream urn table lamp. Create a precise photographic cutout of ONLY that lamp including its full linen drum lampshade, brass stem, cream urn base and small finial if visible. Preserve the actual object shape, proportions, patina, textile texture, and warm lit appearance. Remove burgundy wall, light switch, hangers, frames, Elvis photo, and all surrounding objects. Complete only the tiny cropped top margin of the drum shade naturally so the complete lamp is in frame. No redesign, no extra ornaments. Tall vertical composition, lamp centered with 4% transparent padding. Genuine transparent alpha background, no checkerboard, no cast shadow baked into canvas. This is a decorative editorial cutout for a vintage website, separate from unedited catalog photos.

### chandelier.webp and chandelier--300.webp

Edit target: `site/assets/photos/IMG_6614.webp`.

Final prompt: Use case: background-extraction. Edit target: supplied photograph of the frosted sea-glass tiered chandelier. Precisely isolate ONLY the actual chandelier, keeping its gold rings, every frosted irregular glass shard, warm light and small silver disco ball at upper left. Remove the burgundy wall and price tag. Preserve photographed proportions, perspective, object texture, original design, imperfections. Do not redesign the fixture. Keep full object inside a vertical canvas with little empty margin. Genuine transparent alpha background including gaps between the glass pieces; no checkerboard or solid background, no fake floor shadow. For an atmospheric editorial website composition, separate from untouched item photographs.

### disco-ball.webp and disco-ball--240.webp

New illustrative asset, not an image of a promised exact gift model.

Final prompt: Create a photorealistic silver mirror disco ball as a transparent cutout asset for Hollywood and Vine, an eclectic vintage shop website with burgundy walls and warm lamps. One round sphere made of many small square glass mirror tiles, imperfections and subtle irregular angles, highly tactile. Three-quarter warm studio lighting with a soft champagne highlight from upper left, muted pink reflected light on right and darker burgundy reflections on underside. Keep ball recognizably silver, not pink overall. A small metal hanging eyelet at top, no chain extending above it. Entire circular silhouette visible, centered, ball fills 88% of square canvas. Actual transparent alpha background, no floor, no drop shadow, no solid backdrop, no checkerboard, no text, no stars, no extra objects. Editorial decorative asset, not a product listing image.

## Verification

Browser review at 1440, 390 and 320 CSS pixels; no page-level horizontal overflow. Both lighting palettes reviewed. Checked framed-art and story-object links, modal close/focus return, mobile menu, search, empty-state recovery, save/unsave, and the disco anchor. No browser console errors observed. JavaScript syntax and static build checks passed. Lighthouse results and proof screenshots are saved in the ignored `artifacts/` directory; they are local lab measurements, not production field data.

Technical references checked in-session: [MDN text-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow), [transform](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform), [reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion), and [Sharp output](https://sharp.pixelplumbing.com/api-output/). The text-shadow page was also captured through the repository's crawl4ai workflow.
