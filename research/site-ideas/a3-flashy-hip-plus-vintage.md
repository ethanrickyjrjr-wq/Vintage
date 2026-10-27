# a3: Flashy new web design x vintage subject (research, accessed 2026-10-27)

Agent a3, Group A (FLASH). Raw crawls: `research/site-ideas/raw/a3-*.md`. Nothing here was committed.

## TL;DR

1. The galleries barely contain vintage-resale sites. Awwwards' "Retro" tag is mostly portfolios, agency stunts and one JDM car-parts shop (NightKidz.shop). The flash is in the motion system (cursor trail, blend marquee, mosaic reveal, confetti on add-to-cart), not in the subject. Copy the motion grammar, not the look.
2. Holliewood and Vine already owns the one thing nobody else in these galleries has: a real reflected-light pipeline (WebGL mirror ball, 2D projected-light layer, beat clock). The cheapest, most distinctive flash is to make that engine touch the merchandise (glints land on chrome and glass, neon breathes with the beat, ball can be grabbed and spun), not to bolt on a library.
3. Everything that runs only after "Start the disco" is conversion-safe. Always-on effects (grain, marquee, trail) must be static or paused under `prefers-reduced-motion`, pause on hover/focus, and never sit on the buy path.
4. Do not build: arcade mini-game, camera hand-gestures, retro-OS desktop, Frutiger Aero gloss, full-page glitch, blocking boot screen, per-item 3D models. Reasons in the "Rejected" table.
5. Evidence limits: Godly, Siteinspire, FWA, Land-book, Httpster were NOT crawled. Poolsuite and Boogie Lover Band are walled. The interactive disco-ball demo returned 475 bytes. Library versions are almost never visible in markdown crawls; only two appear below.

## What our engine already exposes (read in this session, `site/disco.js`, `site/atmosphere.css`, `site/storefront.js`)

All sketches below hook these instead of adding a second loop:

- `frame()` rAF loop capped at 30 fps (`1000 / 30`), gated by `discoOn`, `!reduced.matches`, `!document.hidden`.
- `window.HNVDiscoMusic.sample()` returns `{playing, tempo, pulse, level}` (used as `music.pulse`, `music.level`, `music.tempo`).
- `drawLights(now, music)` projects mirror-facet reflections onto a fixed 2D canvas (`.disco-room-light`, `z-index: 8`, `mix-blend-mode: screen`, `pointer-events: none`, hidden under reduced motion). It owns a 64 px `star` sprite and a single `glint` object `{key, x, y, born, visible}` that lives about 420 ms and is picked from the highest-alpha facet (`alpha > .5`, 950 ms cooldown).
- `createRenderer(canvas, image).draw(angle, energy)` renders each `.disco-ball` in WebGL2; `balls.forEach(ball => ball.draw(phase, music.pulse))`.
- `storefront.js` has `allowDepth = matchMedia("(prefers-reduced-motion: no-preference) and (hover: hover) and (pointer: fine)")` and writes `--look-x/--look-y` CSS vars on `.salon-stage`; `.reveal` becomes `.revealed` via IntersectionObserver.
- Already built, so NOT re-proposed: dropping-ball loader with rotating copy, pointer-depth parallax, scroll reveal, now-playing credit.

---

## Sites and sources read

### 1. NightKidz.shop (Awwwards Honorable Mention, retro-tagged)

- Homepage: https://www.nightkidz.shop
- Pages read: https://www.awwwards.com/sites/nightkidz-shop ; https://www.awwwards.com/inspiration/night-drive-trail-cursor-image-stack-nightkidz-shop ; https://www.awwwards.com/inspiration/katakana-wordmark-difference-blend-marquee-nightkidz-shop ; https://www.awwwards.com/inspiration/monochrome-confetti-cart-confirmation-nightkidz-shop ; home crawl `raw/a3-nightkidz-home.md`
- Accessed: 2026-10-27
- What it is: a real store (JDM/USDM plate adapters, wheels such as "SSR Longchamp XR-4 $550.00", apparel; seen in the home crawl). Subject is car culture, not vintage resale. Awwwards lists it under the Retro tag with "Honorable Mention - Sep 11, 2026".
- Evidence (Awwwards submitter text): "Nightkidz motion is built like a signal story: analog noise, controlled distortion, clean lock-in. Token-driven transitions over a headless Next.js + Medusa stack."
- Awwwards element titles with their tags: "Night Drive Trail - Cursor Image Stack" (mouse interaction, cursor, image trail, hero); "Katakana Wordmark - Difference Blend Marquee" (mix blend mode, marquee, typography); "Pixel Block Entry - Logo Resolves" (loading); "Mosaic Reveal - Products Resolve on Scroll"; "Carried Across - Cart Items Into Checkout"; "Monochrome Confetti - Cart Confirmation" (confetti, add to cart, toast, canvas, feedback); "Katakana Scramble - Loading State as Type".
- Libraries: Awwwards technology tags list GSAP, Three.js, Next.js. These are third-party tags, not seen in markup. No versions visible.
- Visuals: I saw no rendered page. The home crawl shows a "Background slide 1" plus 16 `Nightkidz1..16.jpg` images (slideshow, inferred). How each effect looks is inferred from the element titles only.
- Steal this: the whole grammar of "a shop where every micro-moment has one flash and none block buying": hero image trail, blend-mode wordmark band, confetti at add-to-cart, products that "resolve" on scroll.
- Watch out: it is a headless Next.js stack with GSAP and Three.js. We are native HTML/CSS/JS, so every item below is rebuilt, not copied.

### 2. BEIGE FORCE!! (Awwwards Honorable Mention, retro-tagged)

- Homepage: https://beigeforce.com/
- Pages read: https://www.awwwards.com/sites/beige-force ; home crawl `raw/a3-beigeforce-home.md`
- Accessed: 2026-10-27
- Evidence: Awwwards: "BEIGE FORCE!! is a retro arcade game that satirizes bland hotel design, turning the fight against safe, beige mediocrity into a colorful Space Invaders-style battle." Home page loader text: "Gathering the forces... 0%". The makers' own line: "Let's be clear. Nobody needed this." and "every sound in the game should be made with our own mouths." Awwwards tags (third-party): CSS, Javascript, Canvas API; categories include Retro, Colorful, Games & Entertainment.
- Subject: a hotel-design studio's brand stunt, hospitality/nightlife-adjacent, not commerce.
- Steal this: the attitude (loud color, hand-made sound, a brand saying "bold over safe"). Our music is already the hand-made-sound equivalent.
- Watch out: it is a studio flexing, not a store. A mini-game on a one-of-one shop is a gimmick and a production sink. Their blocking "0%" loader is also the anti-pattern for a buy path.

### 3. Neutomni (Awwwards Site of the Day, retro-tagged; seen at listing/page level only)

- Homepage: https://neutomni.com/
- Pages read: https://www.awwwards.com/sites/neutomni
- Accessed: 2026-10-27
- Evidence: "Site of the Day - Oct 13, 2026", score 7.38, element titles "Interactive desktop", "CTA Animation", "Pricing Animation"; tags include Retro, Animation, Scrolling, Storytelling, GSAP, Webflow. Subject is a design agency, not vintage. I did not see the page itself.
- Use: signal only. The "desktop-OS as interface" metaphor shows up repeatedly in the retro tag (see also "EddyOS" in the Awwwards retro list, title only). I recommend against it for us (see Rejected).

### 4. Mochi Online Shoppu (retro e-commerce, Austria)

- Homepage: https://shoppu.mochi.at/
- Page read: same, crawl `raw/a3-mochi-shoppu.md`
- Accessed: 2026-10-27
- Verified in the crawled text: a marquee-style shipping ticker, "// VERSANDKOSTENFREI AB 100 € INNERHALB OESTERREICH // VERSANDVERPACKUNG 100% RECYCELBAR // 100 ユーロから送料無料 //..." (ticker repeats in the text) and a visible counter, "975435 Visits". Asset paths contain `/_nuxt/` (Nuxt build, inferred from URL).
- Colorlib claims not seen in the markup (need review): "buttons that physically depress on hover", "CSS animations use the steps() timing function", "custom pixel cursor". Verified: ticker and counter. Need review: everything else.
- Steal this: a ticker is normal on a real shop when it carries real information. Subject is a Japanese food shop, so this only proves the pattern, not a vintage fit.
- Watch out: a visit counter is only charming if true. Do not fake one.

### 5. Cameron's World ("web 1.0 on purpose")

- Homepage / page read: https://www.cameronsworld.net/ (crawl `raw/a3-camerons-world.md`), accessed 2026-10-27
- Evidence: "A love letter to the Internet of old." "Cameron's World is a web-collage of text and images excavated from the buried neighbourhoods of archived GeoCities pages (1994-2009)." Its browser chrome is called "Catscape Navigator 2.0".
- Steal this: nothing structural. Possible one-off spirit: a 404 page or footer easter egg.
- Watch out: not a shop; density and animated GIFs would bury one-of-one items.

### 6. Interactive Disco Ball demo (thin evidence)

- Page: https://mingxxxxxxxxx.github.io/Disco/ , accessed 2026-10-27. Crawl was 475 bytes (under the 1 KB rule), so treat as a self-description only.
- Evidence: "This project uses WebGL shaders, Three.js, GSAP, and hand gesture detection." "Gesture Control: Use hand gestures to control the ball's rotation." "Audio Responsive: The disco ball and background pulse with the music rhythm." "Camera access permission will be requested for hand gesture recognition."
- Takeaway: audio-reactive mirror ball is a known pattern; ours is already more physical (real facet reflections). The camera gesture control is the part not to copy: a permission wall for a gimmick. Pointer drag gives the same "grab the ball" feeling with zero permission.

### 7. Poolsuite (WALLED)

- Homepage: https://poolsuite.net/ , crawl was 77 bytes; the only content is "Preload for boot background" with image `https://poolsuite.net/boot/background.png`. Accessed 2026-10-27.
- Everything else comes from Colorlib's description (secondhand): "virtual retro computer experience that mimics a classic 90s operating system interface... draggable dialog boxes, pixelated icons... built-in music player." Marked UNVERIFIED by me. Boogie Lover Band (https://boogieloverband.com/) crawl was 4 bytes (walled), so only Colorlib's palette description exists (purple, cyan, hot pink, gold; secondhand).

### 8. Colorlib "18 Best Retro Websites ... 2026" (secondary roundup)

- Page: https://colorlib.com/wp/retro-websites/ , accessed 2026-10-27 (homepage https://colorlib.com/).
- Entries relevant to us, all secondhand (I fetched none of the underlying sites except Mochi and Sugarfire): Virtual Gas Museum ("early-2000s community-site aesthetic... table-based layout... matches the vintage gas-station collectibles it documents"; a collectibles subject done in deliberate web 1.0); We Luv Video ("Neon logo animation and VHS-heavy imagery"); Harvard Film Archive ("full-screen animated SVG curtain... opens every page load"); Sugarfire Pie ("clock hands that rotate with scroll position").
- Discrepancy: Colorlib says Sugarfire has animated neon SVG and scroll-rotating clock hands. My crawl of https://www.sugarfirepie.com/ (`raw/a3-sugarfire.md`) verified only a cookie banner, "Welcome to Pie Heaven", hours and prices. Sugarfire page text verified, animation claims need review. Treat Colorlib's descriptions as leads, not facts (the text quality is uneven).

### 9. Webflow "Y2K aesthetic for web design projects" (trend article)

- Homepage: https://webflow.com/ ; page: https://webflow.com/blog/y2k-aesthetic ; accessed 2026-10-27. Marketing blog, secondary.
- Quotes that matter: chrome/holo "use chrome or holographic accents around important elements like hero cards, feature blocks, or CTAs" (not whole layouts). Glow: "think of it as an accent for specific elements rather than a filter for the entire page." Glitch: "Glitching the entire page can be overwhelming, potentially leading to higher bounce rates, so keep this effect brief and targeted." Sticker look: "Add a soft outer glow or a thin white stroke to create a sticker-like appearance." Grain: "Adding grain to your photos... nods to the Y2K era without tanking image quality."
- Era note: Y2K is late 90s/early 2000s. Our stock is 70s-90s. Use only the techniques, not the Y2K palette.

### 10. Technique references (read as tutorials, not as vintage sites)

| Source | Page | What it verified |
|---|---|---|
| Codrops, "Image Trail Effects" (Aug 7, 2019) | https://tympanus.net/codrops/2019/08/07/image-trail-effects/ | "A set of brutalist effects for mouse-following image trails that show a random series of images." "The animations are powered by TweenMax." (library named, no version). "show the images quickly so that a trail forms along the movement of the mouse." Seven years old. |
| Effect.Labs, "CSS Holographic Effect" (4 Fev 2026) | https://effect-labs.com/en/pages/blog/effet-holographique-css.html | Pure-CSS foil: oversized multi-stop gradient, `::before` overlay with `mix-blend-mode: color-dodge`, `opacity: 0` until hover, plus a repeating line grid. Its demo also runs `animation: holoGradient 5s ease infinite` while hidden, which is wasteful. |
| CSS-Tricks, "Grainy Gradients" (images dated 2021/09) | https://css-tricks.com/grainy-gradients/ | Static noise via SVG: `<feTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch' />`, referenced as a CSS background; `mix-blend-mode` and `isolation: isolate` to control blending. |
| model-viewer | https://modelviewer.dev/ | Web component; quick-start loads `https://ajax.googleapis.com/ajax/libs/model-viewer/4.4.0/model-viewer.min.js` (the only versioned library I can quote); sample attributes include `camera-controls`, `poster`, `shadow-intensity`, `touch-action="pan-y"`. Supported on "the last two major versions of all evergreen desktop and mobile browsers, plus the last two versions of Safari". Needs a `.glb` per object. |
| MDN prefers-reduced-motion | https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion | Baseline "Widely available". Purpose: "to minimize the amount of non-essential motion"; MDN names scaling or panning large objects as vestibular triggers. |
| MDN animation-timeline | https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timeline | "Limited availability... not Baseline because it does not work in some of the most widely-used browsers." So scroll-driven CSS can only be progressive enhancement behind `@supports`. |
| MDN mix-blend-mode / Element.animate | https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode ; https://developer.mozilla.org/en-US/docs/Web/API/Element/animate | Both show Baseline "Widely available". |
| MDN DeviceOrientationEvent | https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent | Widely available; secure-context note; static method `requestPermission()` "Returns a Promise that resolves with a string of "granted" or "denied"". Which browsers need a user gesture for it: UNVERIFIED in my fetch; design as if a tap is required. |

### 11. Frutiger Aero Archive (era check)

- Homepage / page: https://frutigeraeroarchive.org/ , accessed 2026-10-27. "Frutiger Aero is an aesthetic widely used in technology and graphic design in the mid 2000s up to its demise in around 2013." Wrong era for a 70s-90s room. Skip the glossy-bubble look entirely.

### Listings read but NOT analyzed (names only, no site sections)

Awwwards Retro (https://www.awwwards.com/websites/retro/), Awwwards 3D (https://www.awwwards.com/websites/3d/), landing.love Retro (https://www.landing.love/style/retro/, mostly navigation in the crawl), Really Good Designs neo-brutalist list (https://reallygooddesigns.com/neo-brutalist-website-examples/, 16 names), Gempages Shopify retro list. I did not open the individual sites on those lists.

---

## Ranked flash moments (wow-per-effort, best first)

Effort scale: S = under a day, M = a day or two. Costs are my engineering judgment, not vendor figures.

### 1. Grab the ball (drag to spin, the 3D viewer we already own)

- Wow 5, Effort S.
- Technique: the hero mirror ball becomes an object you can pick up and spin, with a "gift" caption. Evidence for the pattern: the disco-ball demo (hand-gesture rotation) and model-viewer's `touch-action="pan-y"`; we skip the camera and the `.glb`.
- Cost: no new draw loop; WebGL ball already renders. A11y: give the ball a focus target and arrow-key rotation; scope `touch-action: pan-y` to the canvas so page scrolling still works on phones. Under reduced motion keep 1:1 drag, drop the inertia.
- Sketch:
  1. In `disco.js`, give each ball `offset = 0`; draw as `ball.draw(phase + ball.offset, pulse)`.
  2. Let `sync()` render when `discoOn || dragging` (today it requires `discoOn`), and render one frame on pointer events even with disco off.
  3. `pointerdown` -> `setPointerCapture`; `pointermove` adds `dx * 0.012` to `offset`; track velocity.
  4. `pointerup` -> if `!reduced.matches`, decay velocity per frame (`v *= .94`) until it stops.
  5. Caption (copy rule): "Disco balls go out as gifts" -- do NOT say "free with every order".
- Verdict: great. Cheap, distinctive, on-brand. Only risk is scroll-trap on mobile if `touch-action` is wrong.

### 2. Light lands on the merchandise (glints wink on chrome, brass, glass)

- Wow 4, Effort S-M.
- Technique: the beat-synced glint is steered to real hotspots on product cards (a lamp rim, a glass edge). Webflow's guidance backs glow "as an accent for specific elements".
- Cost: nearly free; runs only while the disco is on, and the light layer is already hidden under reduced motion. Needs per-item authoring of one hotspot (`--sx/--sy` percentages) for shiny items only.
- Sketch:
  1. Catalog data: optional `shine: [x%, y%]`; render `<article data-shine style="--sx:62%;--sy:18%">`.
  2. In `drawLights`, every ~500 ms collect visible hotspot centers (`getBoundingClientRect` once, not per facet).
  3. Candidate score = `alpha * (1 + 1.5 * nearHotspot)` where `nearHotspot` is 1 if the facet's projected `(x, y)` is within ~80 px of a hotspot. It stays a real facet reflection (the code comment insists the star never floats free of the ball).
  4. On glint birth, add `.wink` to the nearest card for 420 ms (matches `glint` life). CSS: `[data-shine]::after` radial star sprite at `(var(--sx), var(--sy))`, `mix-blend-mode: screen`, scale/opacity keyframe.
  5. Hover pinspot (always on, desktop only via `allowDepth`): cards sit slightly dimmed, hovered card gets a warm radial gradient.
- Verdict: the best "only we can do this" moment. Don't put hotspots on every card; shiny items only, or it becomes noise.

### 3. Neon and wordmark breathe with the beat

- Wow 4, Effort S.
- Technique: expose `music.pulse` to CSS and drive glow, not layout. Evidence: Webflow's glow section (AKARI tubelights on a dark canvas); NightKidz "analog noise, controlled distortion" motion language.
- Cost: only while `discoOn`. Setting a custom property every frame forces style recalculation, so scope it to 2-3 elements and prefer an `opacity` change on a pre-built glow layer over animating `text-shadow` radius.
- Sketch:
  1. In `frame()` after `music` is sampled: `root.style.setProperty("--pulse", music.pulse.toFixed(2))` (30 fps already).
  2. CSS: `.neon::after { opacity: calc(.55 + var(--pulse, 0) * .45) }` on a blurred pink copy; keep a static glow when `--pulse` is unset.
  3. Reset `--pulse` on stop so the page isn't left glowing.
- Verdict: tiny change, loud payoff. Use on the wordmark and "do it for the plot" sign only.

### 4. Mirror-burst on the primary action

- Wow 4, Effort S.
- Technique: NightKidz has a "Monochrome Confetti - Cart Confirmation" element (tags confetti, canvas, toast). Our version: 12-16 small silver mirror chips burst from the button.
- Cost: user-triggered, short, then gone; zero idle cost. A11y: skip the burst under reduced motion and keep a text confirmation.
- Sketch:
  1. On click of the primary CTA (whatever it ends up being: Hold this piece, Add to bag, Buy on Etsy), append 14 `<i class="chip">` to the button wrapper.
  2. For each: `el.animate([{translate:"0 0", opacity:1, rotate:"0deg"},{translate:`${dx}px ${dy}px`, opacity:0, rotate:`${r}deg`}], {duration: 650, easing: "cubic-bezier(.2,.7,.2,1)"})` (Element.animate is Baseline widely available per MDN), remove on `finish`.
  3. Chip CSS: 6 px square with the same silver gradient as the ball facets.
  4. If the click leaves the page (Etsy/Shopify link), open in a new tab; never delay navigation for the animation.
- Verdict: good, and it sits at the moment people commit. Do not let it delay checkout.

### 5. Tilt the phone, sweep the light (opt-in)

- Wow 4 on phones, Effort S-M.
- Technique: map device tilt to the light-origin offset, so projected patches slide across the wall; gives touch devices the parallax that `allowDepth` deliberately gives them none of.
- Cost: sensor handler stores two numbers; drawing stays on the existing 30 fps loop. Battery: only while the disco is on. A11y: it is optional and off by default.
- Sketch:
  1. In `toggleDisco()` (already a user gesture), `await DeviceOrientationEvent.requestPermission?.()` when that function exists; ignore a "denied".
  2. `addEventListener("deviceorientation", e => { tx = clamp(e.gamma / 45, -1, 1); ty = clamp((e.beta - 45) / 45, -1, 1); }, {passive:true})`.
  3. In `drawLights`: lerp `ox += (tx - ox) * .1`, then `originX + ox * width * .12`, same for Y.
  4. Remove the listener in `stopDisco()`.
- Verdict: very good if the permission piggybacks on "Start the disco". Which browsers actually require the gesture: UNVERIFIED, so test on a real iPhone and an Android.

### 6. Die-cut sticker treatment for extras (baked, not live filters)

- Wow 3-4, Effort S.
- Technique: transparent cutouts with a thick white edge, slightly rotated, lifting on hover. Evidence: Webflow "Add a soft outer glow or a thin white stroke to create a sticker-like appearance." The repo has `tools/cutout` and a recent commit about transparent styling pieces, so the inputs probably exist.
- Cost: a live multi-`drop-shadow` outline on many large images is expensive on mobile, so bake the white outline into the image offline (dilate alpha, fill white). At runtime use a single soft shadow.
- Sketch:
  1. Offline: dilate each cutout's alpha ~6 px, fill white, save `*-sticker.webp`.
  2. CSS: `.sticker { rotate: var(--r); filter: drop-shadow(0 6px 10px #0006); transition: .25s }`, hover: `rotate:0deg; translate:0 -4px; scale:1.04`.
  3. Peel hint: a corner `::after` linear-gradient triangle on hover.
  4. Use for extras only (about/gift strip, category chips, "1 of 1" tags), not for product photos.
- Verdict: fun, but a Y2K/zine idiom. In a 70s burgundy salon it can look pasted-on. Use sparingly.

### 7. Mirror-tile "resolve" reveal for product photos

- Wow 3-4, Effort S (veil) or M (true mosaic).
- Technique: NightKidz "Mosaic Reveal - Products Resolve on Scroll" (title only; mechanism inferred). Ours: product photos clear from a silver mirror-tile veil, so the ball's tiles literally "develop" the piece.
- Cost: one pseudo-element per card animating `opacity` only. A real per-tile random mosaic needs about 48 nodes per card or a shared canvas, so start with the cheap veil. Under reduced motion: no veil. `animation-timeline` is Limited availability per MDN, so don't tie the reveal to scroll timelines; keep the IntersectionObserver `.reveal` -> `.revealed` hook.
- Sketch:
  1. `.tile-reveal::after`: stacked `linear-gradient` grout lines over a silver gradient, `inset:0`, `pointer-events:none`.
  2. `.revealed::after { animation: tiles-off .7s steps(6, end) forwards; animation-delay: calc(var(--i) * 60ms) }`.
  3. Only the first 6-8 cards of a grid; once per card.
- Verdict: nice tie-in with the ball. The CSS-only version is a flickering mirrored veil, not a true mosaic. Say so before it disappoints.

### 8. Holographic "1 of 1" foil price sticker

- Wow 3-4, Effort S.
- Technique: Effect.Labs' foil recipe (rainbow gradient layer with `color-dodge`, hidden until hover), applied to a small "ONE OF ONE" label. Webflow: use chrome/holo on "important elements like hero cards, feature blocks, or CTAs", not whole layouts.
- Cost: animate only on pointer or tilt, not on a 5 s infinite loop (Effect.Labs' demo animates while invisible). Keep label text on a solid dark patch for contrast. Under reduced motion: static sheen.
- Sketch:
  1. `.foil { position:relative; isolation:isolate; overflow:hidden }`.
  2. `.foil::before { background: linear-gradient(125deg, ...rainbow...); background-size:200% 200%; background-position: calc(50% + var(--fx,0) * 40%) calc(50% + var(--fy,0) * 40%); mix-blend-mode: color-dodge; opacity:0; transition: opacity .3s }`.
  3. `--fx/--fy` come from the same pointermove code as `--look-x/--look-y`, or from the tilt values in moment 5.
  4. `.foil:hover::before, .foil:focus-visible::before { opacity:.55 }`.
- Verdict: reinforces the one-of-one story. Foil is 80s-90s (fine for stickers), wrong for 70s. Only on price tags.

### 9. Static film grain on the room, not the product

- Wow 2-3, Effort S.
- Technique: SVG `feTurbulence` noise tile (CSS-Tricks attributes above) as an inline data-URI background, low opacity, `mix-blend-mode: overlay`. Webflow: grain "nods to the Y2K era without tanking image quality".
- Cost: static tile means no battery drain. A fixed full-screen blended layer on top of the existing `z-index: 8` screen-blend light canvas stacks two full-viewport blend layers, which is a compositing cost on weak phones. Apply it to the stage/wall sections (`position:absolute`), not `position:fixed` globally. Do not animate it (flickering grain is a cliche and a battery sink). Watch for banding on big gradients.
- Sketch:
  1. `.grain::after { content:""; position:absolute; inset:0; background:url("data:image/svg+xml,...feTurbulence...") ; opacity:.07; mix-blend-mode:overlay; pointer-events:none }`.
  2. Add `.grain` to the hero stage and wall sections only; never on product photos (buyers judge condition from them).
- Verdict: a finish, not a moment. Do it last; keep it invisible.

### 10. Cursor image trail on the lookbook (desktop only)

- Wow 4 on desktop, Effort M.
- Technique: Codrops/VLNC-style mouse trail; NightKidz "Night Drive Trail - Cursor Image Stack". Codrops built it with TweenMax; native version needs only a pool of images and the Web Animations API.
- Cost: decorative, desktop only (`allowDepth` query), useless on touch. It also covers photos, which is a conversion risk if it sits over listings. Confine it to one hero or "all pieces" band; `pointer-events:none`.
- Sketch:
  1. Pre-create 8 `<img>` from existing product photos in a `position:absolute` band.
  2. On `pointermove`, if the pointer moved > 90 px since the last spawn, take the next image from the pool, place it at the cursor with a small random rotation.
  3. `img.animate([{opacity:0,scale:.7},{opacity:1,scale:1,offset:.2},{opacity:0,scale:1.1}], {duration:900})`.
  4. Clear on `pointerleave`; do nothing under reduced motion or on `(hover:none)`.
- Verdict: striking, but it is the most "agency portfolio" move here. One band, not site-wide. Skip it first if time is tight.

### 11. Difference-blend marquee band

- Wow 3, Effort S.
- Technique: NightKidz "Katakana Wordmark - Difference Blend Marquee" (tags: mix blend mode, marquee). Mochi shows a plain ticker on a real shop.
- Cost: pure CSS transform, nearly free. A11y: moving text must be pausable (hover, focus) and static under reduced motion. WCAG has a pause/stop/hide rule for moving content (SC 2.2.2); I did not fetch the W3C text, so UNVERIFIED here; check before shipping.
- Sketch:
  1. Markup: one real text instance, one `aria-hidden="true"` duplicate in a flex track.
  2. CSS: `@keyframes slide { to { translate: -50% 0 } }`, `animation: slide 40s linear infinite`, `.band:hover, .band:focus-within { animation-play-state: paused }`.
  3. `mix-blend-mode: difference` text over a photo strip; wrap in `isolation: isolate` so it doesn't blend with the whole page.
  4. `@media (prefers-reduced-motion: reduce) { .track { animation: none } }`.
  5. Copy rules: "ONE OF ONE", "DO IT FOR THE PLOT", piece counts. Never "free disco ball with every order"; nothing implying open hours or "visit us".
- Verdict: the most likely to look tacky or be unreadable. One band, one place, never above the buy button.

---

## Rejected (and why)

| Idea | Source | Why not |
|---|---|---|
| Arcade mini-game | BEIGE FORCE | Their own words: "Nobody needed this." It is a brand stunt with real build cost; a one-of-one shop needs listings, not a game. |
| Camera hand-gesture control | Disco-ball demo | Camera permission prompt for a gimmick; pointer drag (moment 1) does the same. |
| Blocking boot screen / "Gathering the forces... 0%" loader | BEIGE FORCE, Poolsuite boot preload, NightKidz "Pixel Block Entry" | Never block the path to a product. We already have the dropping-ball loader. |
| Retro-OS desktop with draggable windows | Poolsuite (walled, secondhand), Neutomni "Interactive desktop", EddyOS (titles) | Wrong era (90s Mac vs 70s salon), hides product info behind windows, high effort. |
| Frutiger Aero gloss | Frutiger Aero Archive | The archive dates it "mid 2000s up to its demise in around 2013". Wrong era for this stock. |
| Full-page glitch / VHS tearing | Webflow Y2K | Webflow itself warns of "higher bounce rates"; keep to a 404 page if at all. |
| Per-item 3D viewers | model-viewer 4.4.0 | Needs a `.glb` per item; stock is one-of-one. A dependency we don't use. At most one hero object, and the ball already is that. |
| Fake visit counter | Mochi Shoppu shows "975435 Visits" | Only charming if true; a made-up counter is dishonest. Use a real "pieces in the room" count. |
| Animated film-grain flicker | General Y2K/VHS trend | Battery sink and a cliche; static only. |
| Load-bearing scroll-driven CSS | MDN animation-timeline | Limited availability; progressive enhancement behind `@supports` only. |

## Final ranking, one line each

1. Grab the ball (drag-to-spin, gift caption) - S
2. Light lands on the merchandise (steered glints, pinspot) - S-M
3. Neon and wordmark breathe with the beat - S
4. Mirror-burst on the primary action - S
5. Tilt the phone, sweep the light (opt-in on "Start the disco") - S-M
6. Baked die-cut stickers for extras - S
7. Mirror-tile resolve reveal - S/M
8. Holo "1 of 1" foil price sticker - S
9. Static grain on stage and walls - S
10. Cursor image trail on one lookbook band - M
11. Difference-blend marquee band - S

## Blocked, thin, or unverified

- NOT crawled: Godly, Siteinspire, FWA, Land-book, Httpster (search returned godly.design, others untried). Awwwards Retro, Awwwards 3D, landing.love Retro and the Really Good Designs neo-brutalist list were read only at the listing level.
- Walled: Poolsuite (77 bytes), Boogie Lover Band (4 bytes). Thin: disco-ball demo (475 bytes).
- UNVERIFIED: Mochi's `steps()`, pixel cursor and button-press claims; Sugarfire's scroll clock hands; Harvard Film Archive's SVG curtain; We Luv Video's neon logo; Virtual Gas Museum's table layout (all Colorlib claims). Which browsers require a user gesture for `DeviceOrientationEvent.requestPermission()`. WCAG SC 2.2.2 wording. Browser support for View Transitions (relevant if copying NightKidz's "Carried Across" cart transition; not fetched, so do not rely on it).
- Library names seen in fetched page content: only model-viewer 4.4.0 and Codrops' TweenMax (no version). GSAP, Three.js, Next.js, Canvas API for NightKidz/BEIGE FORCE come from Awwwards tags, not markup.
- All visual descriptions are inferred from titles, tags and page text; no rendered page was viewed. Performance and accessibility costs are engineering judgment, with no measured figures.
