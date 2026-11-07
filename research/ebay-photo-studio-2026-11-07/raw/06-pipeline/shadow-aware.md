<!-- source: https://github.com/crispinzz/shadow-aware-bg-removal, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - crispinzz/shadow-aware-bg-removal: Remove the background from a product photo and keep the real shadow. Conventional removers delete the shadow with the background, or draw a fake one; this one measures it. Local, offline, MIT. · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fcrispinzz%2Fshadow-aware-bg-removal)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fcrispinzz%2Fshadow-aware-bg-removal)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=crispinzz%2Fshadow-aware-bg-removal)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/crispinzz/shadow-aware-bg-removal)

![crispinzz](https://avatars.githubusercontent.com/u/163873727?s=60&v=4)

**[shadow-aware-bg-removal](/crispinzz/shadow-aware-bg-removal)**

Public

-   [Notifications](/login?return_to=%2Fcrispinzz%2Fshadow-aware-bg-removal)You must be signed in to change notification settings
-   [Fork0 (0)](/login?return_to=%2Fcrispinzz%2Fshadow-aware-bg-removal)
-   [Star1 (1)](/login?return_to=%2Fcrispinzz%2Fshadow-aware-bg-removal)You must be signed in to star a repository

## About

Remove the background from a product photo and keep the real shadow. Conventional removers delete the shadow with the background, or draw a fake one; this one measures it. Local, offline, MIT.

### Topics

[alpha-matting](/topics/alpha-matting)[background-removal](/topics/background-removal)[birefnet](/topics/birefnet)[computer-vision](/topics/computer-vision)[ecommerce](/topics/ecommerce)[image-processing](/topics/image-processing)[image-segmentation](/topics/image-segmentation)[offline-first](/topics/offline-first)[onnx](/topics/onnx)[photo-editing](/topics/photo-editing)[product-photography](/topics/product-photography)[python](/topics/python)[shadow](/topics/shadow)[typescript](/topics/typescript)[white-background](/topics/white-background)

### Resources

[Readme](#readme-ov-file)

[License](#License-1-ov-file)

[Activity](/crispinzz/shadow-aware-bg-removal/activity)

### Stars

**1** star

### Watchers

**1** watching

### Forks

[**0** forks](/crispinzz/shadow-aware-bg-removal/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fcrispinzz%2Fshadow-aware-bg-removal&report=crispinzz+%28user%29)

[Branches](/crispinzz/shadow-aware-bg-removal/branches)[Tags](/crispinzz/shadow-aware-bg-removal/tags)

[](/crispinzz/shadow-aware-bg-removal/branches)[](/crispinzz/shadow-aware-bg-removal/tags)

Open more actions menu

## Latest commit

## History

[18 Commits](/crispinzz/shadow-aware-bg-removal/commits/master/)

[](/crispinzz/shadow-aware-bg-removal/commits/master/)18 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[docs](/crispinzz/shadow-aware-bg-removal/tree/master/docs "docs")

[docs](/crispinzz/shadow-aware-bg-removal/tree/master/docs "docs")

[server](/crispinzz/shadow-aware-bg-removal/tree/master/server "server")

[server](/crispinzz/shadow-aware-bg-removal/tree/master/server "server")

[src](/crispinzz/shadow-aware-bg-removal/tree/master/src "src")

[src](/crispinzz/shadow-aware-bg-removal/tree/master/src "src")

[training](/crispinzz/shadow-aware-bg-removal/tree/master/training "training")

[training](/crispinzz/shadow-aware-bg-removal/tree/master/training "training")

[web](/crispinzz/shadow-aware-bg-removal/tree/master/web "web")

[web](/crispinzz/shadow-aware-bg-removal/tree/master/web "web")

[.gitignore](/crispinzz/shadow-aware-bg-removal/blob/master/.gitignore ".gitignore")

[.gitignore](/crispinzz/shadow-aware-bg-removal/blob/master/.gitignore ".gitignore")

[LICENSE](/crispinzz/shadow-aware-bg-removal/blob/master/LICENSE "LICENSE")

[LICENSE](/crispinzz/shadow-aware-bg-removal/blob/master/LICENSE "LICENSE")

[README.md](/crispinzz/shadow-aware-bg-removal/blob/master/README.md "README.md")

[README.md](/crispinzz/shadow-aware-bg-removal/blob/master/README.md "README.md")

[index.html](/crispinzz/shadow-aware-bg-removal/blob/master/index.html "index.html")

[index.html](/crispinzz/shadow-aware-bg-removal/blob/master/index.html "index.html")

[package-lock.json](/crispinzz/shadow-aware-bg-removal/blob/master/package-lock.json "package-lock.json")

[package-lock.json](/crispinzz/shadow-aware-bg-removal/blob/master/package-lock.json "package-lock.json")

[package.json](/crispinzz/shadow-aware-bg-removal/blob/master/package.json "package.json")

[package.json](/crispinzz/shadow-aware-bg-removal/blob/master/package.json "package.json")

[tsconfig.json](/crispinzz/shadow-aware-bg-removal/blob/master/tsconfig.json "tsconfig.json")

[tsconfig.json](/crispinzz/shadow-aware-bg-removal/blob/master/tsconfig.json "tsconfig.json")

[vite.config.ts](/crispinzz/shadow-aware-bg-removal/blob/master/vite.config.ts "vite.config.ts")

[vite.config.ts](/crispinzz/shadow-aware-bg-removal/blob/master/vite.config.ts "vite.config.ts")

## Repository files navigation

[![SHARP — Shadow-Aware Retouch Pipeline](/crispinzz/shadow-aware-bg-removal/raw/master/docs/media/banner.png)](/crispinzz/shadow-aware-bg-removal/blob/master/docs/media/banner.png)

### Remove the background from a product photo — and keep the shadow the light actually made.

[](#remove-the-background-from-a-product-photo--and-keep-the-shadow-the-light-actually-made)

Every product pixel stays **byte-for-byte identical**. The backdrop becomes **pure white — or drops out to transparent**. The contact shadow survives with its **real shape and softness**. Runs locally — the photo never leaves the machine.

[![License](https://camo.githubusercontent.com/836326edeb7216775b1d15de45eb93ba111b94f47939c63752b7a0c1d410c132/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d616c6c25323072696768747325323072657365727665642d366336636666)](https://camo.githubusercontent.com/836326edeb7216775b1d15de45eb93ba111b94f47939c63752b7a0c1d410c132/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d616c6c25323072696768747325323072657365727665642d366336636666) [![Runs offline](https://camo.githubusercontent.com/2d006d0eaca9780e7cce7572692357f88ceae75b1cd3a10a1daf36aed0b580d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72756e732d3130302532352532306f66666c696e652d316231653233)](https://camo.githubusercontent.com/2d006d0eaca9780e7cce7572692357f88ceae75b1cd3a10a1daf36aed0b580d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72756e732d3130302532352532306f66666c696e652d316231653233) [![Python](https://camo.githubusercontent.com/a691b8ddbe447c7228080aca0fbf42eb3fe816f6911ad0cde6ac17da146daf96/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31312532422d366336636666)](https://camo.githubusercontent.com/a691b8ddbe447c7228080aca0fbf42eb3fe816f6911ad0cde6ac17da146daf96/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31312532422d366336636666) [![ONNX Runtime](https://camo.githubusercontent.com/64777e7a454f2364cd2e376bebe9deba19547c36f0d197a1e0fd69b3532e37e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f656e67696e652d4f4e4e5825323052756e74696d652d316231653233)](https://camo.githubusercontent.com/64777e7a454f2364cd2e376bebe9deba19547c36f0d197a1e0fd69b3532e37e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f656e67696e652d4f4e4e5825323052756e74696d652d316231653233) [![TypeScript](https://camo.githubusercontent.com/f368b51a4ad6bcb165d5502b56358baa55d36dbcbc19185133385951bbee262b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6d706f736974696e672d547970655363726970742d366336636666)](https://camo.githubusercontent.com/f368b51a4ad6bcb165d5502b56358baa55d36dbcbc19185133385951bbee262b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6d706f736974696e672d547970655363726970742d366336636666)

[![Before and after: a coloured studio sweep becomes pure white while the cast shadow stays](/crispinzz/shadow-aware-bg-removal/raw/master/docs/media/before-after.gif)](/crispinzz/shadow-aware-bg-removal/blob/master/docs/media/before-after.gif)

Real pipeline output. Source photo: [Unsplash](https://unsplash.com/photos/19682ca159de) (free licence) — no customer photos used.

```
background removal · keep shadow · product photography · e-commerce · white background
BiRefNet · ONNX Runtime · alpha matting · FastAPI · TypeScript · offline · proprietary
```

* * *

## Why this exists

[](#why-this-exists)

Conventional background removers cut out **the product** and throw everything else away. That is the whole job as they define it: find the subject, produce an alpha matte, delete the rest. The shadow is not the subject, so the shadow dies with the background — and with it the only cue that tells a viewer the object is _standing on something_ instead of floating in a void.

The ones that do offer a shadow usually **draw a new one**: an ellipse under the object, a blurred copy of the silhouette, a drop shadow at a fixed angle. It is a different shadow from the one the light in your studio actually made. Perspective, softness, direction, the way it stretches away from the camera — none of that is preserved, because none of it was measured.

This project measures it.

The insight is old and comes from retouchers, not from machine learning: **a shadow is not a shape to cut out, it is a multiplication.** On a white backdrop, a pixel in shadow is the backdrop times a number below 1. So instead of segmenting the shadow, you divide the background by the light it _would_ have had with no shadow on it. Clean fabric divides to 1 and becomes pure white. Shadow divides to 0.72 and comes back as 72% grey, in exactly the shape the light drew. This is what Photoshop retouchers do by hand with a Multiply layer and Blend If — here it is just arithmetic.

Conventional remover

This project

What is segmented

the product

the product

What happens to the shadow

deleted, or replaced by a synthetic one

measured and kept

Perspective of the shadow

lost, or faked at a fixed angle

the one your lights made

Product pixels

re-encoded, sometimes recoloured

untouched, byte for byte

Where it runs

usually a paid API

your machine, offline

* * *

## How it works

[](#how-it-works)

Four stages. The figures below are generated by `docs/make_figures.py` — they are the real intermediate buffers, not illustrations.

[![The stages: photo, alpha matte, shadow map, white backdrop, transparent cutout](/crispinzz/shadow-aware-bg-removal/raw/master/docs/media/pipeline.png)](/crispinzz/shadow-aware-bg-removal/blob/master/docs/media/pipeline.png)

### 1\. The photo

[](#1-the-photo)

A product on a seamless backdrop. The fabric has folds, the light falls off towards the corners, and the object casts a shadow to one side.

### 2\. The alpha matte — where the product is

[](#2-the-alpha-matte--where-the-product-is)

[BiRefNet](https://github.com/ZhengPeng7/BiRefNet) (MIT-licensed weights, ONNX Runtime, CPU) answers one question only: **which pixels are the product**. White is product, black is everything else. It produces no pixel that reaches the final image — the product's own photographed pixels do.

Two details matter here:

-   **The threshold is deliberately low (0.22).** Where the network answers in mid-tones — a white leg against white fabric, a chrome edge — a 0.5 cut eats part of the product. When in doubt, the pixel is product.
-   **Holes are closed.** On a dark part of the product the network can answer a low alpha, which would punch a white hole in the middle of the object. A hole is an island of "background" that does not touch the frame edge _and_ does not carry the backdrop's light. A real see-through gap (between the rungs of a ladder) shows the fabric, so it carries that light and is kept.

### 3\. The shadow map — how much each pixel darkens

[](#3-the-shadow-map--how-much-each-pixel-darkens)

For every background pixel: `factor = luminance / light the backdrop would have had there`.

The reference light is a wide local average taken **only over lit background pixels**, so the shadow itself never drags the reference down. White here means "nothing to keep". Grey is the shadow, with its gradient intact. Fabric folds land within 18% of the clean value and are rounded to white — that is how the wrinkles disappear without touching the shadow.

### 4\. The composite

[](#4-the-composite)

`white × factor` outside the product, original bytes inside, with a soft seam between the two. No colour correction, no saturation, no sharpening, no tone curve: lighting is a job for the softbox, not for the software.

### 5\. Or no backdrop at all

[](#5-or-no-backdrop-at-all)

Same matte, same shadow — composited onto alpha instead of white. The clean backdrop becomes fully transparent and the shadow is kept as semi-transparent black, so the product drops onto any page with its shadow intact. This is the **Transparent** toggle in the studio; it exports a PNG where white mode exports a JPEG.

* * *

## Install

[](#install)

git clone https://github.com/crispinzz/shadow-aware-bg-removal
cd shadow-aware-bg-removal

# segmentation server (Python 3.11+)
pip install -r server/requirements.txt
python server/baixar\_modelo.py birefnet-general-lite   # 224 MB, once (product matte)
python server/baixar\_modelo.py shadow-matte            # 6 MB, once (our shadow weights)
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --app-dir server

The server binds to `127.0.0.1` on purpose. Nothing is uploaded anywhere.

## Use it

[](#use-it)

### From the command line

[](#from-the-command-line)

python docs/make\_figures.py path/to/photo.jpg
# docs/figures/04-output.png is the result; 02-matte and 03-shadow-map show the reasoning

### From the browser

[](#from-the-browser)

`src/backdrop.ts` is dependency-free TypeScript that runs in any browser. Give it the photo and the matte; it does the compositing at full resolution:

import { smoothBackdrop } from "./src/backdrop";

const result \= await smoothBackdrop(
  photoBlob,        // the original file, full size
  "photo.jpg",
  shadowBrush,      // optional: a canvas where you painted over a faint shadow
  matteImage,       // the matte from the server, any size — it is scaled to fit
  eraserBrush,      // optional: a canvas where you painted objects to delete
);
// result.file      the finished JPEG
// result.coverage  fraction of the frame that became background

Two optional brushes exist because no model is right every time:

-   **Shadow brush** — paint over a shadow that is too faint to clear the fold threshold, and it is kept regardless.
-   **Eraser** — paint over anything the network insisted on calling product (a tripod, a box, the corner of a table) and it becomes background.

`web/` holds the React page these screenshots come from: a drag-and-drop stage with a before/after curtain, both brushes, light and dark themes.

## Training our own weights

[](#training-our-own-weights)

The product matte comes from [BiRefNet](https://github.com/ZhengPeng7/BiRefNet), and it should: segmenting the subject is a solved problem, and no single machine is going to beat weights trained on DIS5K with a cluster. Competing there would be vanity.

The weights worth training are for the question nobody else asks. `training/train_shadow.py` trains a **shadow matting** network: for every background pixel, _how much did the object darken the backdrop here_ — a continuous factor in \[0, 1\], not a binary mask. Every public shadow dataset but one ships binary masks, which throws away the very thing that makes a shadow look real. [ISTD](https://github.com/DeepInsight-PCALab/ST-CGAN) ships the shadow-free version of each frame, so the factor is directly computable as `shadow / shadow_free`, per pixel.

python training/train\_shadow.py --data /path/to/ISTD --epochs 40 --batch 8
python training/export\_onnx.py runs/shadow-best.pt server/modelos/shadow-matte.onnx

Heads up: the studio shadow is **analytic** (`src/backdrop.ts`), extracted from the photo itself, and the network is **not** wired into it. Trained as it is, the net never saw an object in frame — on a product-on-sweep shot it reads the object as shadow and returns a blur — so it stays a training artifact until it is retrained with the object composited in. See [docs/features/06-rede-de-sombra.md](/crispinzz/shadow-aware-bg-removal/blob/master/docs/features/06-rede-de-sombra.md). Per-feature docs live in [docs/features/](/crispinzz/shadow-aware-bg-removal/blob/master/docs/features).

The network is a deliberately small U-Net (1.9M parameters). A shadow is a low-frequency field: a deep decoder spends its capacity inventing grain that is then multiplied into the photo, where it shows immediately. The loss is L1 over the pixels where the ratio is meaningful, plus a gradient term — matching the derivative is what keeps the penumbra landing in the right place instead of becoming a blurred blob.

Honest about cost, measured rather than guessed. `training/bench_cpu.py` times a real training step on your machine; on an Intel i5-13400 with no GPU at all it prints:

side

batch

s/step

40 epochs on ISTD

256 px

4

1.6 s

6 h

320 px

4

2.9 s

11 h

384 px

4

4.3 s

16 h

A plain desktop CPU trains this overnight, and peak memory stays near 1.5 GB at 320 px. That is the payoff for keeping the network small: no GPU, no cloud bill, no CUDA. Fine-tuning a subject segmenter is the opposite — that one belongs on a rented GPU.

**Why a network beats the arithmetic.** The analytic method in `src/backdrop.ts` divides the background by the light it would have had. That holds on a plain seamless sweep and nowhere else. It has no answer for a textured or coloured backdrop (dividing out the light also divides out the texture), for a shadow that leaves the floor and climbs a wall (the reference light jumps), for two lights casting two shadows of different densities, or for a translucent object where part of the darkening is transmission rather than occlusion. Those are the cases where the factor map has to be predicted instead of measured.

## Tuning

[](#tuning)

Every constant lives at the top of `src/backdrop.ts` with the reason it has that value:

Constant

Default

What it decides

`ALFA_PRODUTO`

`0.22`

above this alpha, the pixel is product and is never touched

`RUGA`

`0.18`

up to 18% darker than clean backdrop counts as a fabric fold → white

`SOMBRA_MIN`

`0.55`

a shadow never darkens past this, or it reads as a hole

`SOMBRA_ALCANCE`

`0.06`

shadows are only kept this close to the product's bounding box

`RAIO_LUZ`

`1/22`

radius of the "light the backdrop would have had" average

## Requirements

[](#requirements)

Python 3.11+, ~2 GB RAM for inference, no GPU needed. A 12 MP photo takes about 25 s on a laptop CPU; the photo is downscaled to 1400 px for the network and the matte is scaled back up, because the network reasons at 1024 px anyway.

## Licence

[](#licence)

All rights reserved — see [LICENSE](/crispinzz/shadow-aware-bg-removal/blob/master/LICENSE). This project is proprietary; no use or redistribution without written consent. The BiRefNet weights are MIT, from [ZhengPeng7/BiRefNet](https://github.com/ZhengPeng7/BiRefNet), and keep their own licence.

* * *

### Keywords

[](#keywords)

remove background from product photo, keep shadow, preserve shadow background removal, white background product photography, e-commerce photo editing, alpha matte, BiRefNet ONNX, local background removal, offline rembg alternative, multiply shadow compositing, seamless backdrop wrinkle removal, catalogue photography automation.

## About

Remove the background from a product photo and keep the real shadow. Conventional removers delete the shadow with the background, or draw a fake one; this one measures it. Local, offline, MIT.

### Topics

[alpha-matting](/topics/alpha-matting)[background-removal](/topics/background-removal)[birefnet](/topics/birefnet)[computer-vision](/topics/computer-vision)[ecommerce](/topics/ecommerce)[image-processing](/topics/image-processing)[image-segmentation](/topics/image-segmentation)[offline-first](/topics/offline-first)[onnx](/topics/onnx)[photo-editing](/topics/photo-editing)[product-photography](/topics/product-photography)[python](/topics/python)[shadow](/topics/shadow)[typescript](/topics/typescript)[white-background](/topics/white-background)

### Resources

[Readme](#readme-ov-file)

[License](#License-1-ov-file)

[Activity](/crispinzz/shadow-aware-bg-removal/activity)

### Stars

**1** star

### Watchers

**1** watching

### Forks

[**0** forks](/crispinzz/shadow-aware-bg-removal/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fcrispinzz%2Fshadow-aware-bg-removal&report=crispinzz+%28user%29)

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.
