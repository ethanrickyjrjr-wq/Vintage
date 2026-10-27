
```
# NeoDisco LLM Reference

NeoDisco is a tiny Canvas 2D disco ball renderer for vanilla JavaScript, React, and Vue.

Website: http://neo-disco.vikingz.me/
Repository: https://github.com/vikingmute/neo-disco
Package import: neodisco

## What It Does

NeoDisco renders an art-directed mirror ball with:
- latitude/longitude mirror tiles projected onto a sphere
- theme palettes: ice, gold, prism, mono
- glow, star flares, wire strokes, shadow, and hanging cord
- deterministic tile layout through seed
- responsive canvas sizing
- framework adapters for React and Vue

It does not use WebGL or Three.js. Rendering happens in Canvas 2D.

## Install

```bash
npm install neodisco
```

## Vanilla Usage

```ts
import { createNeoDisco } from "neodisco";

const instance = createNeoDisco(document.querySelector("#stage")!, {
  theme: "prism",
  tileRows: 28,
  tileColumns: 54,
  sparkle: 0.7,
  glow: 1.1,
  rotationSpeed: 0.18
});

instance.update({ theme: "gold" });
instance.destroy();
```

## React Usage

```tsx
import { NeoDisco } from "neodisco/react";

export function Hero() {
  return <NeoDisco theme="gold" sparkle={0.6} glow={1.05} />;
}
```

## Vue Usage

```vue
<script setup lang="ts">
import { NeoDisco } from "neodisco/vue";
</script>

<template>
  <NeoDisco :options="{ theme: 'prism', tileColumns: 54, sparkle: 0.7 }" />
</template>
```

## Main Options

- theme: "ice" | "gold" | "prism" | "mono"
- palette: partial override for base, mirror, glow, wire, shadow
- size: number | "auto"
- pixelRatio: canvas resolution multiplier
- radius: ball radius relative to canvas size
- tileRows: horizontal mirror bands
- tileColumns: vertical mirror columns
- tileGap: separation between mirror tiles
- rotation: initial rotation
- rotationSpeed: animation speed
- tilt: vertical perspective tilt
- contrast: mirror light/dark intensity
- glow: flare and bloom strength
- sparkle: frequency/intensity of highlight tiles and star flares
- cord: draw hanging cord and cap
- background: true, false, or CSS color
- paused: render one frame without animation
- seed: stable random tile layout
- canvasClassName: class applied to generated canvas
- canvasStyle: inline styles applied to generated canvas

## Design Notes

NeoDisco is art-directed, not physically simulated. Keep effects restrained for premium landing pages: use small sparkle/glow adjustments, moderate tile density, and a slow rotation speed.

```


