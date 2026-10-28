# Private showroom (3D spin + cutout lab)

October 27, 2026. Ricky asked to see everything the site could do with good pictures,
including side and back shots. `site/demo-showroom.html` is local and private; it is
linked from `/demo-photos.html` and is not in the publication build.

Run `node dev.mjs` from `site/` (restart it: `.glb`, `.gltf` and `.bin` content types
were added), then open `/demo-showroom.html`.

**01 Spin it.** Eleven open-licensed 3D models rendered with Google `<model-viewer>`
4.3.1 (Apache-2.0, vendored at `assets/demo/vendor/`). Per model: Front, 3/4, Side,
Back and Top camera buttons, backdrops (white, burgundy, neon, gold, Ricky's wall
photo), shadow, auto-spin, and colorway chips read from the file's
`KHR_materials_variants` (the sofa and the sneaker have them). Each model auto-shoots
five transparent stills with `toDataURL`, cropped to their visible pixels, as a
listing-style photo set; picking a colorway re-shoots them. The shoe and the
projector set `yaw: 90` because their native front is the profile. The oil lamp's
glass chimney is made translucent in script (its BLEND material has no alpha
channel). Camera orbit, variants and the materials API were checked against
modelviewer.dev docs in-session.

**02 Cutout lab.** The 45 round-two cutouts (`sources.json` `alternatives`) on the same
backdrops with floor shadow, a flipped fading reflection, a hover loupe into the 1600 px
pixels, and an approximate CSS hue-rotate recolor.

| Model | Source | License |
| --- | --- | --- |
| Glam Velvet Sofa, Chair Damask Purple Gold, Materials Variants Shoe | KhronosGroup/glTF-Sample-Assets | CC BY 4.0 (Wayfair, Wayfair, Shopify): credit shown on the page |
| Filmstrip Projector 8mm, Vintage Oil Lamp, Horse Statue 01, Mid Century Lounge Chair, Chandelier 01, Boombox, Vintage Video Camera, Marble Bust 01 | Poly Haven API, 1k glTF | CC0 |

`research/demo-photo-sourcing/showroom-models.json` has URLs, hashes and the license
text. These are stand-in models, not scans of Ricky's pieces. The 3D views are real
geometry, not generated back sides.

Not done: Hugging Face image-to-3D or multi-angle generation. The connector's
`invoke` is disabled (`gradio=none`), and a rotation LoRA would invent the back.
Next if wanted: hotspots on the 3D pieces, a real phone scan of a shop piece, and
wiring the cutouts into the room editor.
