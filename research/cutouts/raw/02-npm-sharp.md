⚠️
npm tokens that bypass 2FA are being restricted — account changes (Aug 2026) and direct publishing (Jan 2027). [Learn how to prepare →](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/)
×
skip to:[content](https://www.npmjs.com/package/sharp#main)[package search](https://www.npmjs.com/package/sharp#search)[sign in](https://www.npmjs.com/package/sharp#signin)
Light mode — click for dark
  * [Pro](https://www.npmjs.com/products/pro)
  * [Teams](https://www.npmjs.com/products/teams)
  * [Pricing](https://www.npmjs.com/products)
  * [Documentation](https://docs.npmjs.com)


npm
[](https://www.npmjs.com/)
Search
[Sign Up](https://www.npmjs.com/signup)[Sign In](https://www.npmjs.com/login)
#  sharp
![TypeScript icon, indicating that this package has built-in type declarations](https://static-production.npmjs.com/4a2a680dfcadf231172b78b1d3beb975.svg)
0.35.5 • Public • Published a month ago
  * [ Readme](https://www.npmjs.com/package/sharp?activeTab=readme)
  * [Code Beta](https://www.npmjs.com/package/sharp?activeTab=code)
  * [3 Dependencies](https://www.npmjs.com/package/sharp?activeTab=dependencies)
  * [10987 Dependents](https://www.npmjs.com/package/sharp?activeTab=dependents)
  * [194 Versions](https://www.npmjs.com/package/sharp?activeTab=versions)


# sharp
[](https://www.npmjs.com/package/sharp#sharp)
[![sharp logo](https://camo.githubusercontent.com/d67b9b942197ac50f871ce2090c96f3ac34a07c2ca899e6daaa04d44a9bcd3d1/68747470733a2f2f73686172702e706978656c706c756d62696e672e636f6d2f73686172702d6c6f676f2e737667)](https://camo.githubusercontent.com/d67b9b942197ac50f871ce2090c96f3ac34a07c2ca899e6daaa04d44a9bcd3d1/68747470733a2f2f73686172702e706978656c706c756d62696e672e636f6d2f73686172702d6c6f676f2e737667)
The typical use case for this high speed Node-API module is to convert large images in common formats to smaller, web-friendly JPEG, PNG, WebP, GIF and AVIF images of varying dimensions.
It can be used with all JavaScript runtimes that provide support for Node-API v9, including Node.js (>= 20.9.0), Deno and Bun.
Resizing an image is typically 4x-5x faster than using the quickest ImageMagick and GraphicsMagick settings due to its use of [libvips](https://github.com/libvips/libvips).
Colour spaces, embedded ICC profiles and alpha transparency channels are all handled correctly. Lanczos resampling ensures quality is not sacrificed for speed.
As well as image resizing, operations such as rotation, extraction, compositing and gamma correction are available.
Most modern macOS, Windows and Linux systems do not require any additional install or runtime dependencies.
## Documentation
[](https://www.npmjs.com/package/sharp#documentation)
Visit [sharp.pixelplumbing.com](https://sharp.pixelplumbing.com/) for complete [installation instructions](https://sharp.pixelplumbing.com/install), [API documentation](https://sharp.pixelplumbing.com/api-constructor), [benchmark tests](https://sharp.pixelplumbing.com/performance) and [changelog](https://sharp.pixelplumbing.com/changelog).
## Examples
[](https://www.npmjs.com/package/sharp#examples)

```
npm install sharp
```


```
// ESM
import sharp from 'sharp';

// CJS
const sharp = require('sharp');
```


```
await sharp(inputBuffer)
  .resize({ width: 320, height: 240 })
  .toFile('output.webp', (err, info) => { ... });
```


```
const output = await sharp('input.jpg')
  .autoOrient()
  .resize({ width: 200 })
  .jpeg({ mozjpeg: true })
  .toBuffer();
```


```
const semiTransparentRedPng = await sharp({
  create: {
    width: 48,
    height: 48,
    channels: 4,
    background: { r: 255, g: 0, b: 0, alpha: 0.5 }
  }
})
  .png()
  .toBuffer();
```


```
const roundedCorners = Buffer.from(
  '<svg><rect x="0" y="0" width="200" height="200" rx="50" ry="50"/></svg>'
);

const roundedCornerResizer =
  sharp()
    .resize(200, 200)
    .composite([{
      input: roundedCorners,
      blend: 'dest-in'
    }])
    .png();

readableStream
  .pipe(roundedCornerResizer)
  .pipe(writableStream);
```

## Contributing
[](https://www.npmjs.com/package/sharp#contributing)
A [guide for contributors](https://github.com/lovell/sharp/blob/main/.github/CONTRIBUTING.md) covers reporting bugs, requesting features and submitting code changes.
## Licensing
[](https://www.npmjs.com/package/sharp#licensing)
Copyright 2013 Lovell Fuller and others.
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <https://www.apache.org/licenses/LICENSE-2.0>
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
## Readme
### Keywords
  * [jpeg](https://www.npmjs.com/search?q=keywords:jpeg)
  * [png](https://www.npmjs.com/search?q=keywords:png)
  * [webp](https://www.npmjs.com/search?q=keywords:webp)
  * [avif](https://www.npmjs.com/search?q=keywords:avif)
  * [tiff](https://www.npmjs.com/search?q=keywords:tiff)
  * [gif](https://www.npmjs.com/search?q=keywords:gif)
  * [svg](https://www.npmjs.com/search?q=keywords:svg)
  * [jp2](https://www.npmjs.com/search?q=keywords:jp2)
  * [dzi](https://www.npmjs.com/search?q=keywords:dzi)
  * [image](https://www.npmjs.com/search?q=keywords:image)
  * [resize](https://www.npmjs.com/search?q=keywords:resize)
  * [thumbnail](https://www.npmjs.com/search?q=keywords:thumbnail)
  * [crop](https://www.npmjs.com/search?q=keywords:crop)
  * [embed](https://www.npmjs.com/search?q=keywords:embed)
  * [libvips](https://www.npmjs.com/search?q=keywords:libvips)
  * [vips](https://www.npmjs.com/search?q=keywords:vips)


# Provenance
[Share feedback](https://github.com/npm/feedback)
## Package Sidebar
### Install
`npm i sharp`
### Repository
[Gitgithub.com/lovell/sharp](https://github.com/lovell/sharp)
### Homepage
[sharp.pixelplumbing.com](https://sharp.pixelplumbing.com)
[**Fund** this package](https://opencollective.com/libvips)
###  DownloadsWeekly Downloads
79,575,083
### Version
0.35.5
### License
Apache-2.0
### Last publish
a month ago
### Collaborators
  * [![lovell](https://www.npmjs.com/npm-avatar/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXJVUkwiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci85OGE1OTA2NjNlZjNkYzBmMTIxMjEzM2U1ZjVjZDhkOD9zaXplPTEwMCZkZWZhdWx0PXJldHJvIn0.Pi3R3nQTz7rw9usMTmKHzsozSuSoaSrUEPREySgrsA4)](https://www.npmjs.com/~lovell)
lovell


[**Analyze security** with Socket](https://socket.dev/npm/package/sharp)[**Check bundle size**](https://bundlephobia.com/package/sharp)[**View package health**](https://snyk.io/advisor/npm-package/sharp)[**Explore dependencies**](https://npmgraph.js.org/?q=sharp)
[**Report** malware](https://www.npmjs.com/support?inquire=security&security-inquire=malware&package=sharp&version=0.35.5)
## Footer
[](https://github.com/npm)
[](https://github.com)
### Support
  * [Help](https://docs.npmjs.com)
  * [Advisories](https://github.com/advisories)
  * [Status](http://status.npmjs.org/)
  * [Contact npm](https://www.npmjs.com/support)


### Company
  * [About](https://www.npmjs.com/about)
  * [Blog](https://github.blog/tag/npm/)
  * [Press](https://www.npmjs.com/press)


### Terms & Policies
  * [Policies](https://www.npmjs.com/policies/)
  * [Terms of Use](https://www.npmjs.com/policies/terms)
  * [Code of Conduct](https://www.npmjs.com/policies/conduct)
  * [Privacy](https://www.npmjs.com/policies/privacy)


Viewing sharp version 0.35.5

