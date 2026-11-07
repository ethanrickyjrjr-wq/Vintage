[Skip to main content](https://withoutbg.com/models/birefnet-general#main-content)
[![withoutBG logo](https://withoutbg.com/images/logo-light.png) withoutBG](https://withoutbg.com/)
  * [Pro Model API](https://withoutbg.com/pro-model-api)
  * [Pro Model Self-Host](https://withoutbg.com/pro-model-self-host)
  * [Open Weights Model](https://withoutbg.com/open-model)


  * [Cars](https://withoutbg.com/car)


  * [Pricing](https://withoutbg.com/pro-model-api/pricing)
  * [Docs](https://withoutbg.com/docs)


Search docs...
`⌘K`
  * Try Pro Model
  * [Login](https://withoutbg.com/login)
  * [Sign Up](https://withoutbg.com/signup)


  1. [Home](https://withoutbg.com/)
  2. [Models](https://withoutbg.com/models)
  3. Birefnet General


# BiRefNet General (birefnet-general) background removal[#](https://withoutbg.com/models/birefnet-general#birefnet-general-birefnet-general-background-removal)
Bilateral Reference Network for high-quality dichotomous segmentation / matting-style cutouts.
Run it: `rembg i -m birefnet-general input.jpg output.png` [setup](https://withoutbg.com/models/birefnet-general#usage-heading)
## BiRefNet results on 33 images
Original, cutout and alpha matte for every Bench v0 image, with its MAE and MGE against the ground truth. Each opens the side-by-side comparison.
### People (12)
OriginalCutoutAlpha matte
[ ![bearded man portrait, original](https://withoutbg.com/images/compare/img/bearded-man-portrait.webp) ![bearded man portrait, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/bearded-man-portrait.webp) ![bearded man portrait, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/bearded-man-portrait.webp) bearded man portraitMAE 0.0093 · MGE 0.0153](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-bearded-man-portrait)[ ![blowing dandelion seeds, original](https://withoutbg.com/images/compare/img/blowing-dandelion-seeds.webp) ![blowing dandelion seeds, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/blowing-dandelion-seeds.webp) ![blowing dandelion seeds, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/blowing-dandelion-seeds.webp) blowing dandelion seedsMAE 0.0245 · MGE 0.0552](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-blowing-dandelion-seeds)[ ![confetti sunset portrait, original](https://withoutbg.com/images/compare/img/confetti-sunset-portrait.webp) ![confetti sunset portrait, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/confetti-sunset-portrait.webp) ![confetti sunset portrait, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/confetti-sunset-portrait.webp) confetti sunset portraitMAE 0.0116 · MGE 0.0358](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-confetti-sunset-portrait)[ ![messy bun cityscape, original](https://withoutbg.com/images/compare/img/messy-bun-cityscape.webp) ![messy bun cityscape, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/messy-bun-cityscape.webp) ![messy bun cityscape, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/messy-bun-cityscape.webp) messy bun cityscapeMAE 0.0083 · MGE 0.0182](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-messy-bun-cityscape)[ ![messy hair bearded portrait, original](https://withoutbg.com/images/compare/img/messy-hair-bearded-portrait.webp) ![messy hair bearded portrait, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/messy-hair-bearded-portrait.webp) ![messy hair bearded portrait, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/messy-hair-bearded-portrait.webp) messy hair bearded portraitMAE 0.0137 · MGE 0.0197](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-messy-hair-bearded-portrait)[ ![smiling man seaside sunset, original](https://withoutbg.com/images/compare/img/smiling-man-seaside-sunset.webp) ![smiling man seaside sunset, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/smiling-man-seaside-sunset.webp) ![smiling man seaside sunset, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/smiling-man-seaside-sunset.webp) smiling man seaside sunsetMAE 0.0028 · MGE 0.0062](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-smiling-man-seaside-sunset)[ ![smiling woman seaside, original](https://withoutbg.com/images/compare/img/smiling-woman-seaside.webp) ![smiling woman seaside, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/smiling-woman-seaside.webp) ![smiling woman seaside, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/smiling-woman-seaside.webp) smiling woman seasideMAE 0.0071 · MGE 0.0181](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-smiling-woman-seaside)[ ![street portrait man, original](https://withoutbg.com/images/compare/img/street-portrait-man.webp) ![street portrait man, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/street-portrait-man.webp) ![street portrait man, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/street-portrait-man.webp) street portrait manMAE 0.0037 · MGE 0.0108](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-street-portrait-man)[ ![sunset field portrait, original](https://withoutbg.com/images/compare/img/sunset-field-portrait.webp) ![sunset field portrait, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/sunset-field-portrait.webp) ![sunset field portrait, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/sunset-field-portrait.webp) sunset field portraitMAE 0.0085 · MGE 0.0188](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-sunset-field-portrait)[ ![windblown curly hair backpack, original](https://withoutbg.com/images/compare/img/windblown-curly-hair-backpack.webp) ![windblown curly hair backpack, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/windblown-curly-hair-backpack.webp) ![windblown curly hair backpack, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/windblown-curly-hair-backpack.webp) windblown curly hair backpackMAE 0.0118 · MGE 0.0334](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-windblown-curly-hair-backpack)[ ![windblown curly portrait, original](https://withoutbg.com/images/compare/img/windblown-curly-portrait.webp) ![windblown curly portrait, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/windblown-curly-portrait.webp) ![windblown curly portrait, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/windblown-curly-portrait.webp) windblown curly portraitMAE 0.0193 · MGE 0.0498](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-windblown-curly-portrait)[ ![woman street portrait glasses, original](https://withoutbg.com/images/compare/img/woman-street-portrait-glasses.webp) ![woman street portrait glasses, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/woman-street-portrait-glasses.webp) ![woman street portrait glasses, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/woman-street-portrait-glasses.webp) woman street portrait glassesMAE 0.0095 · MGE 0.0185](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-woman-street-portrait-glasses)
### Plants (7)
OriginalCutoutAlpha matte
[ ![balcony flower planter bokeh, original](https://withoutbg.com/images/compare/img/balcony-flower-planter-bokeh.webp) ![balcony flower planter bokeh, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/balcony-flower-planter-bokeh.webp) ![balcony flower planter bokeh, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/balcony-flower-planter-bokeh.webp) balcony flower planter bokehMAE 0.0291 · MGE 0.0339](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-balcony-flower-planter-bokeh)[ ![balcony plant bokeh, original](https://withoutbg.com/images/compare/img/balcony-plant-bokeh.webp) ![balcony plant bokeh, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/balcony-plant-bokeh.webp) ![balcony plant bokeh, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/balcony-plant-bokeh.webp) balcony plant bokehMAE 0.0066 · MGE 0.0337](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-balcony-plant-bokeh)[ ![compound leaf raindrops, original](https://withoutbg.com/images/compare/img/compound-leaf-raindrops.webp) ![compound leaf raindrops, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/compound-leaf-raindrops.webp) ![compound leaf raindrops, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/compound-leaf-raindrops.webp) compound leaf raindropsMAE 0.0033 · MGE 0.0142](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-compound-leaf-raindrops)[ ![grass seed stem bokeh, original](https://withoutbg.com/images/compare/img/grass-seed-stem-bokeh.webp) ![grass seed stem bokeh, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/grass-seed-stem-bokeh.webp) ![grass seed stem bokeh, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/grass-seed-stem-bokeh.webp) grass seed stem bokehMAE 0.0078 · MGE 0.0222](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-grass-seed-stem-bokeh)[ ![hanging plant window, original](https://withoutbg.com/images/compare/img/hanging-plant-window.webp) ![hanging plant window, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/hanging-plant-window.webp) ![hanging plant window, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/hanging-plant-window.webp) hanging plant windowMAE 0.0112 · MGE 0.0487](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-hanging-plant-window)[ ![orange berries branch, original](https://withoutbg.com/images/compare/img/orange-berries-branch.webp) ![orange berries branch, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/orange-berries-branch.webp) ![orange berries branch, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/orange-berries-branch.webp) orange berries branchMAE 0.0256 · MGE 0.0557](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-orange-berries-branch)[ ![red flower balcony bokeh, original](https://withoutbg.com/images/compare/img/red-flower-balcony-bokeh.webp) ![red flower balcony bokeh, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/red-flower-balcony-bokeh.webp) ![red flower balcony bokeh, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/red-flower-balcony-bokeh.webp) red flower balcony bokehMAE 0.0033 · MGE 0.0147](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-red-flower-balcony-bokeh)
### Objects with Details (6)
OriginalCutoutAlpha matte
[ ![autumn bouquet vase, original](https://withoutbg.com/images/compare/img/autumn-bouquet-vase.webp) ![autumn bouquet vase, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/autumn-bouquet-vase.webp) ![autumn bouquet vase, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/autumn-bouquet-vase.webp) autumn bouquet vaseMAE 0.0075 · MGE 0.0345](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-autumn-bouquet-vase)[ ![bike handlebar near beach, original](https://withoutbg.com/images/compare/img/bike-handlebar-near-beach.webp) ![bike handlebar near beach, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/bike-handlebar-near-beach.webp) ![bike handlebar near beach, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/bike-handlebar-near-beach.webp) bike handlebar near beachMAE 0.0066 · MGE 0.0178](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-bike-handlebar-near-beach)[ ![cargo ebike park tracks, original](https://withoutbg.com/images/compare/img/cargo-ebike-park-tracks.webp) ![cargo ebike park tracks, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/cargo-ebike-park-tracks.webp) ![cargo ebike park tracks, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/cargo-ebike-park-tracks.webp) cargo ebike park tracksMAE 0.0127 · MGE 0.0650](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-cargo-ebike-park-tracks)[ ![dried flowers clay vase, original](https://withoutbg.com/images/compare/img/dried-flowers-clay-vase.webp) ![dried flowers clay vase, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/dried-flowers-clay-vase.webp) ![dried flowers clay vase, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/dried-flowers-clay-vase.webp) dried flowers clay vaseMAE 0.0072 · MGE 0.0297](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-dried-flowers-clay-vase)[ ![spoked bike wheel, original](https://withoutbg.com/images/compare/img/spoked-bike-wheel.webp) ![spoked bike wheel, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/spoked-bike-wheel.webp) ![spoked bike wheel, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/spoked-bike-wheel.webp) spoked bike wheelMAE 0.0065 · MGE 0.0352](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-spoked-bike-wheel)[ ![two gravel bikes park, original](https://withoutbg.com/images/compare/img/two-gravel-bikes-park.webp) ![two gravel bikes park, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/two-gravel-bikes-park.webp) ![two gravel bikes park, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/two-gravel-bikes-park.webp) two gravel bikes parkMAE 0.0183 · MGE 0.0932](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-two-gravel-bikes-park)
### Motion (4)
OriginalCutoutAlpha matte
[ ![campfire flames night, original](https://withoutbg.com/images/compare/img/campfire-flames-night.webp) ![campfire flames night, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/campfire-flames-night.webp) ![campfire flames night, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/campfire-flames-night.webp) campfire flames nightMAE 0.0096 · MGE 0.0207](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-campfire-flames-night)[ ![elderly man running blur, original](https://withoutbg.com/images/compare/img/elderly-man-running-blur.webp) ![elderly man running blur, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/elderly-man-running-blur.webp) ![elderly man running blur, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/elderly-man-running-blur.webp) elderly man running blurMAE 0.0051 · MGE 0.0178](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-elderly-man-running-blur)[ ![sprinter motion blur, original](https://withoutbg.com/images/compare/img/sprinter-motion-blur.webp) ![sprinter motion blur, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/sprinter-motion-blur.webp) ![sprinter motion blur, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/sprinter-motion-blur.webp) sprinter motion blurMAE 0.0278 · MGE 0.0290](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-sprinter-motion-blur)[ ![street dancer studio pose, original](https://withoutbg.com/images/compare/img/street-dancer-studio-pose.webp) ![street dancer studio pose, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/street-dancer-studio-pose.webp) ![street dancer studio pose, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/street-dancer-studio-pose.webp) street dancer studio poseMAE 0.0031 · MGE 0.0144](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-street-dancer-studio-pose)
### Film Camera (2)
OriginalCutoutAlpha matte
[ ![small fishing boat bw, original](https://withoutbg.com/images/compare/img/small-fishing-boat-bw.webp) ![small fishing boat bw, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/small-fishing-boat-bw.webp) ![small fishing boat bw, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/small-fishing-boat-bw.webp) small fishing boat bwMAE 0.0061 · MGE 0.0209](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-small-fishing-boat-bw)[ ![two bikes field, original](https://withoutbg.com/images/compare/img/two-bikes-field.webp) ![two bikes field, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/two-bikes-field.webp) ![two bikes field, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/two-bikes-field.webp) two bikes fieldMAE 0.0942 · MGE 0.0798](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-two-bikes-field)
### animal (2)
OriginalCutoutAlpha matte
[ ![tabby cat portrait, original](https://withoutbg.com/images/compare/img/tabby-cat-portrait.webp) ![tabby cat portrait, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/tabby-cat-portrait.webp) ![tabby cat portrait, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/tabby-cat-portrait.webp) tabby cat portraitMAE 0.0758 · MGE 0.0420](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-tabby-cat-portrait)[ ![terrier dog mugshot, original](https://withoutbg.com/images/compare/img/terrier-dog-mugshot.webp) ![terrier dog mugshot, BiRefNet cutout](https://withoutbg.com/images/compare/birefnet-general/background-removed/terrier-dog-mugshot.webp) ![terrier dog mugshot, BiRefNet alpha matte](https://withoutbg.com/images/compare/birefnet-general/predicted-alpha-matte/terrier-dog-mugshot.webp) terrier dog mugshotMAE 0.0601 · MGE 0.0939](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general#example-terrier-dog-mugshot)
## How to run BiRefNet
BiRefNet ships with [rembg](https://github.com/danielgatis/rembg) as the session `birefnet-general`. The weights download on first use.
### Command line

```
pip install "rembg[cpu,cli]"
rembg i -m birefnet-general input.jpg output.png
```

### Python

```
from rembg import new_session, remove
from PIL import Image

session = new_session("birefnet-general")  # load once, reuse for every image
output = remove(Image.open("input.jpg"), session=session)
output.save("output.png")
```

Other sessions: [all rembg models](https://withoutbg.com/models/runtime/rembg).
## BiRefNet General as a free, open-source remove.bg alternative
remove.bg is a paid cloud service. BiRefNet General is open weights under MIT, so commercial use is allowed. It runs on your own machine (`rembg i -m birefnet-general input.jpg output.png`), offline, with no upload and no per-image cost. On Bench v0 it ranks #4 of 13 by accuracy (MAE); withoutBG Open Weights ranks #2.
remove.bg is not in Bench v0, so there is no score against it. [See withoutBG Open Weights and remove.bg side by side](https://withoutbg.com/compare/withoutbg-open-model-vs-remove-bg), or compare [all remove.bg alternatives](https://withoutbg.com/compare/remove-bg-alternatives).
## Quick take
  * **Best for:** High-quality open cutouts when you can afford heavier models
  * **Avoid when:** Strict latency or tiny ONNX footprints
  * **Notes:** Available as rembg session `birefnet-general`.


## When a hosted model is worth it
BiRefNet is free and runs on your machine; keep it if the results above are good enough. If you need finer hair and edges, or don't want to run large models locally, rembg also ships the withoutBG Pro Model as the `withoutbg` session, ranked #1 of 13 by accuracy on Bench v0. Images are sent to withoutBG's servers.
### Same command, hosted model

```
export WITHOUTBG_API_KEY=sk_...
rembg i -m withoutbg input.jpg output.png
```

[Sign up for 50 free credits](https://withoutbg.com/signup) (no credit card) or [See its results](https://withoutbg.com/pro-model-api/results).
## Bench v0 · 33 images MAE rank
     #4 of 130.0169 MGE rank
     #2 of 130.0338 Band MAE rank
     #4 of 130.0619
MAE: overall accuracy. MGE: edge quality. Lower is better.
## By category (rank)  
| Category  | MAE  | MGE  |  
| --- | --- | --- |  
| People (12)  | #4  | #4  |  
| Plants (7)  | #2  | #2  |  
| Objects with Details (6)  | #1  | #1  |  
## Compare with
  * [withoutBG Open Weights](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet-general)
  * [IS-Net](https://withoutbg.com/compare/birefnet-general-vs-isnet-general-use)
  * [U²-Net](https://withoutbg.com/compare/birefnet-general-vs-u2net)
  * [BiRefNet Massive](https://withoutbg.com/compare/birefnet-general-vs-birefnet-massive)
  * [BiRefNet DIS](https://withoutbg.com/compare/birefnet-general-vs-birefnet-dis)
  * [BiRefNet Portrait](https://withoutbg.com/compare/birefnet-general-vs-birefnet-portrait)
  * [BiRefNet HRSOD](https://withoutbg.com/compare/birefnet-general-vs-birefnet-hrsod)


## All models by MAE
  1. 1[withoutBG Pro Model API](https://withoutbg.com/pro-model-api)0.0115
  2. 2[withoutBG Open Weights](https://withoutbg.com/models/withoutbg-open)0.0132
  3. 3[BiRefNet (legacy)](https://withoutbg.com/compare/withoutbg-open-model-vs-birefnet)0.0146
  4. 4BiRefNet General0.0169
  5. 5[BiRefNet Massive](https://withoutbg.com/models/birefnet-massive)0.0223
  6. 6[BiRefNet DIS](https://withoutbg.com/models/birefnet-dis)0.0228
  7. 7[BiRefNet General Lite](https://withoutbg.com/models/birefnet-general-lite)0.0301
  8. 8[BiRefNet HRSOD](https://withoutbg.com/models/birefnet-hrsod)0.0304
  9. 9[IS-Net](https://withoutbg.com/models/isnet-general-use)0.0410
  10. 10[BiRefNet Portrait](https://withoutbg.com/models/birefnet-portrait)0.0509
  11. 11[U²-Net](https://withoutbg.com/models/u2net)0.0667
  12. 12[Silueta](https://withoutbg.com/models/silueta)0.0712
  13. 13[U²-NetP](https://withoutbg.com/models/u2netp)0.0721

[Leaderboard by MAE or MGE](https://withoutbg.com/compare#compare-leaderboard)
## Details Family
    BiRefNet License
    MIT · commercial use OK Deploy
    ONNX · rembg birefnet-general Input
    1024×1024 Size
    Large general ONNX (rembg birefnet-general)
## Links
  * [Paper](https://arxiv.org/abs/2401.03407)
  * [GitHub](https://github.com/ZhengPeng7/BiRefNet)
  * [Hugging Face](https://huggingface.co/ZhengPeng7/BiRefNet)
  * [All rembg models](https://withoutbg.com/models/runtime/rembg)
  * [Benchmark methodology](https://withoutbg.com/benchmarks/open-background-removal)
  * [remove.bg alternatives](https://withoutbg.com/compare/remove-bg-alternatives)
  * [withoutBG Open Model](https://withoutbg.com/open-model)


![withoutBG logo](https://withoutbg.com/images/logo.png)withoutBG
Background removal you can call as an API or run on your own hardware.
2026 © withoutBG API
## Links
  * [Privacy Policy](https://withoutbg.com/privacy)
  * [Terms](https://withoutbg.com/terms)
  * [About](https://withoutbg.com/about)
  * [Imprint](https://withoutbg.com/imprint)
  * [Open Model License](https://withoutbg.com/open-model/license)
  * [Affiliate Program](https://withoutbg.com/affiliate)
  * [Product Updates](https://withoutbg.com/updates)


## Guides
  * [API Documentation](https://withoutbg.com/docs)
  * [Tech](https://withoutbg.com/tech)
  * [Use cases](https://withoutbg.com/use-cases)
  * [Research](https://withoutbg.com/tech/image-matting-research)
  * [Compare](https://withoutbg.com/compare)
  * [Model leaderboard](https://withoutbg.com/compare#compare-leaderboard)
  * [remove.bg alternatives](https://withoutbg.com/compare/remove-bg-alternatives)
  * [Benchmark hub](https://withoutbg.com/benchmarks/open-background-removal)
  * [Open model directory](https://withoutbg.com/models)
  * [rembg models](https://withoutbg.com/models/runtime/rembg)
  * [Try](https://withoutbg.com/pro-model-api)
  * [Pro Model Self-Host](https://withoutbg.com/pro-model-self-host)


## Support
  * [Contact us](https://withoutbg.com/contact?from=footer)
  * ![Contact email address](https://withoutbg.com/images/cntct.png)



