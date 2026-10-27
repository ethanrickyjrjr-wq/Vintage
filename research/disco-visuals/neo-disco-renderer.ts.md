
```
import { createRandom, clamp, lerp } from "./math";
import { palettes } from "./palette";
import type { DiscoBallInstance, DiscoBallOptions, DiscoBallPalette, DiscoBallTarget } from "./types";

const defaults = {
  size: "auto",
  pixelRatio: 2,
  theme: "ice",
  background: true,
  radius: 0.34,
  tileRows: 24,
  tileColumns: 44,
  tileGap: 0.88,
  rotation: 0,
  rotationSpeed: 0.28,
  tilt: -0.12,
  contrast: 1,
  glow: 0.9,
  sparkle: 0.45,
  cord: true,
  paused: false,
  seed: 7
} satisfies Required<Omit<DiscoBallOptions, "palette" | "canvasClassName" | "canvasStyle">>;

interface ResolvedOptions extends Required<Omit<DiscoBallOptions, "palette" | "canvasClassName" | "canvasStyle">> {
  palette: DiscoBallPalette;
}

interface Tile {
  row: number;
  column: number;
  tone: number;
  flash: number;
  colorIndex: number;
}

interface Point3 {
  x: number;
  y: number;
  z: number;
}

interface FlareCandidate {
  x: number;
  y: number;
  radius: number;
  score: number;
  color: string;
  angle: number;
}

export function createDiscoBall(target: DiscoBallTarget, options: DiscoBallOptions = {}): DiscoBallInstance {
  const canvas = target instanceof HTMLCanvasElement ? target : document.createElement("canvas");
  const context = canvas.getContext("2d");

  if (!context) {
    throw new Error("DiscoBall requires a 2D canvas context.");
  }
  const ctx = context;

  if (!(target instanceof HTMLCanvasElement)) {
    target.appendChild(canvas);
  }

  let opts = resolveOptions(options);
  let frame = 0;
  let raf = 0;
  let width = 0;
  let height = 0;
  let tiles = createTiles(opts);
  const container = target instanceof HTMLCanvasElement ? target.parentElement : target;
  const resizeObserver = typeof ResizeObserver === "undefined" ? undefined : new ResizeObserver(resize);

  canvas.className = options.canvasClassName ?? "";
  Object.assign(canvas.style, {
    display: "block",
    height: opts.size === "auto" ? "100%" : `${opts.size}px`,
    width: opts.size === "auto" ? "100%" : `${opts.size}px`,
    ...options.canvasStyle
  });

  if (container && opts.size === "auto") {
    resizeObserver?.observe(container);
  }

  resize();
  loop();

  return {
    canvas,
    update(nextOptions) {
      const previousSeed = opts.seed;
      const previousRows = opts.tileRows;
      const previousColumns = opts.tileColumns;
      const { palette: _palette, ...baseOptions } = opts;
      opts = resolveOptions({ ...baseOptions, ...nextOptions });
      canvas.className = nextOptions.canvasClassName ?? canvas.className;
      Object.assign(canvas.style, nextOptions.canvasStyle);
      if (previousSeed !== opts.seed || previousRows !== opts.tileRows || previousColumns !== opts.tileColumns) {
        tiles = createTiles(opts);
      }
      resize();
    },
    play() {
      opts.paused = false;
      loop();
    },
    pause() {
      opts.paused = true;
      cancelAnimationFrame(raf);
    },
    destroy() {
      cancelAnimationFrame(raf);
      resizeObserver?.disconnect();
      if (!(target instanceof HTMLCanvasElement)) {
        canvas.remove();
      }
    }
  };

  function loop(time = 0) {
    if (opts.paused) {
      render(time);
      return;
    }

    render(time);
    raf = requestAnimationFrame(loop);
  }

  function resize() {
    const rect = canvas.getBoundingClientRect();
    const cssSize = opts.size === "auto" ? Math.max(1, Math.min(rect.width || 640, rect.height || rect.width || 640)) : opts.size;
    const ratio = clamp(opts.pixelRatio || window.devicePixelRatio || 1, 1, 3);
    width = Math.round(cssSize * ratio);
    height = Math.round(cssSize * ratio);

    if (canvas.width !== width || canvas.height !== height) {
      canvas.width = width;
      canvas.height = height;
    }
  }

  function render(time: number) {
    frame += 1;
    ctx.clearRect(0, 0, width, height);
    drawBackground(ctx, opts, width, height);
    drawCord(ctx, opts, width, height);
    drawBall(ctx, opts, tiles, width, height, time / 1000);
  }
}

function resolveOptions(options: DiscoBallOptions): ResolvedOptions {
  const { palette: paletteOverrides, ...rest } = options;
  const theme = options.theme ?? defaults.theme;
  return {
    ...defaults,
    ...rest,
    theme,
    palette: {
      ...palettes[theme],
      ...paletteOverrides
    }
  };
}

function createTiles(options: ResolvedOptions): Tile[] {
  const random = createRandom(options.seed);
  const tiles: Tile[] = [];

  for (let row = 0; row < options.tileRows; row += 1) {
    for (let column = 0; column < options.tileColumns; column += 1) {
      tiles.push({
        row,
        column,
        tone: random(),
        flash: random(),
        colorIndex: Math.floor(random() * options.palette.mirror.length)
      });
    }
  }

  return tiles;
}

function drawBackground(context: CanvasRenderingContext2D, options: ResolvedOptions, width: number, height: number) {
  if (!options.background) return;

  context.save();
  context.fillStyle = typeof options.background === "string" ? options.background : options.palette.base;
  context.fillRect(0, 0, width, height);

  const gradient = context.createRadialGradient(width * 0.5, height * 0.45, 0, width * 0.5, height * 0.45, width * 0.7);
  gradient.addColorStop(0, `${options.palette.glow}20`);
  gradient.addColorStop(0.52, "rgba(0,0,0,0)");
  gradient.addColorStop(1, "rgba(0,0,0,0.85)");
  context.fillStyle = gradient;
  context.fillRect(0, 0, width, height);
  context.restore();
}

function drawCord(context: CanvasRenderingContext2D, options: ResolvedOptions, width: number, height: number) {
  if (!options.cord) return;

  const centerX = width * 0.5;
  const centerY = height * 0.5;
  const radius = Math.min(width, height) * options.radius;
  context.save();
  context.strokeStyle = options.palette.wire;
  context.lineWidth = Math.max(1, width * 0.002);
  context.beginPath();
  context.moveTo(centerX, 0);
  context.lineTo(centerX, centerY - radius * 0.96);
  context.stroke();
  context.fillStyle = options.palette.glow;
  context.fillRect(centerX - radius * 0.055, centerY - radius * 1.03, radius * 0.11, radius * 0.08);
  context.restore();
}

function drawBall(
  context: CanvasRenderingContext2D,
  options: ResolvedOptions,
  tiles: Tile[],
  width: number,
  height: number,
  seconds: number
) {
  const centerX = width * 0.5;
  const centerY = height * 0.53;
  const radius = Math.min(width, height) * options.radius;
  const rotation = options.rotation + seconds * options.rotationSpeed;
  const light = normalize({
    x: -0.42 + Math.sin(seconds * 0.34) * 0.18,
    y: -0.46 + Math.cos(seconds * 0.21) * 0.1,
    z: 0.86
  });
  const view = normalize({ x: 0, y: 0, z: 1 });
  const flareCandidates: FlareCandidate[] = [];

  context.save();
  context.beginPath();
  context.arc(centerX, centerY, radius, 0, Math.PI * 2);
  context.clip();

  const sortedTiles = tiles
    .map((tile) => ({ tile, depth: tileDepth(tile, options, rotation) }))
    .filter((item) => item.depth > -0.16)
    .sort((a, b) => a.depth - b.depth);

  for (const { tile } of sortedTiles) {
    const quad = tileQuad(tile, options, rotation);
    const projected = quad.map((point) => ({
      x: centerX + point.x * radius,
      y: centerY + point.y * radius
    }));
    const normal = normalize(quad.reduce((acc, point) => ({ x: acc.x + point.x, y: acc.y + point.y, z: acc.z + point.z }), { x: 0, y: 0, z: 0 }));
    const reflection = reflectVector(light, normal);
    const sparkleAmount = clamp(options.sparkle, 0, 1);
    const specular = Math.pow(clamp(dot(reflection, view), 0, 1), lerp(92, 42, sparkleAmount));
    const shimmer = Math.sin(seconds * 0.82 + tile.flash * 9 + tile.column * 0.07) * 0.5 + 0.5;
    const glint = specular * sparkleAmount * lerp(0.72, 1.35, sparkleAmount) * lerp(0.62, 1, shimmer) * lerp(0.72, 1, tile.flash);
    const lightness = clamp(dot(normal, light) * 0.78 + tile.tone * 0.48 + glint * lerp(0.62, 1.15, sparkleAmount), 0, 1);
    const color = options.palette.mirror[tile.colorIndex % options.palette.mirror.length] ?? "#ffffff";
    const firstPoint = projected[0];

    if (!firstPoint) continue;

    context.beginPath();
    context.moveTo(firstPoint.x, firstPoint.y);
    for (const point of projected.slice(1)) context.lineTo(point.x, point.y);
    context.closePath();
    context.fillStyle = colorWithAlpha(color, lerp(0.42, 1, clamp(lightness * options.contrast, 0, 1)));
    context.fill();

    if (glint > lerp(0.42, 0.14, sparkleAmount)) {
      context.fillStyle = colorWithAlpha("#ffffff", clamp(glint * 0.32, 0, 0.32));
      context.fill();
    }

    context.strokeStyle = options.palette.wire;
    context.lineWidth = Math.max(0.45, radius * 0.004 * options.tileGap);
    context.stroke();

    if (glint > lerp(0.42, 0.12, sparkleAmount) && normal.z > 0.18) {
      const flarePoint = projectedCenter(projected);
      flareCandidates.push({
        x: flarePoint.x,
        y: flarePoint.y,
        radius: radius * lerp(0.055, 0.145, sparkleAmount) * lerp(0.88, 1.18, clamp(glint, 0, 1)) * options.glow,
        score: glint * lerp(0.72, 1, normal.z),
        color: glint > lerp(0.38, 0.24, sparkleAmount) ? "#ffffff" : options.palette.glow,
        angle: Math.atan2(normal.y, normal.x) * 0.18
      });
    }
  }

  drawOuterGlow(context, centerX, centerY, radius, options);

  const shadow = context.createRadialGradient(centerX - radius * 0.18, centerY - radius * 0.28, radius * 0.1, centerX, centerY, radius);
  shadow.addColorStop(0, "rgba(255,255,255,0.08)");
  shadow.addColorStop(0.58, "rgba(0,0,0,0)");
  shadow.addColorStop(1, options.palette.shadow);
  context.fillStyle = shadow;
  context.fillRect(centerX - radius, centerY - radius, radius * 2, radius * 2);
  context.restore();

  drawMirrorFlares(context, flareCandidates, radius, options);
}

function tileDepth(tile: Tile, options: ResolvedOptions, rotation: number): number {
  const theta = ((tile.column + 0.5) / options.tileColumns) * Math.PI * 2 + rotation;
  const phi = ((tile.row + 0.5) / options.tileRows - 0.5) * Math.PI;
  return Math.cos(phi) * Math.cos(theta);
}

function tileQuad(tile: Tile, options: ResolvedOptions, rotation: number): Point3[] {
  const rowStart = tile.row / options.tileRows - 0.5;
  const rowEnd = (tile.row + options.tileGap) / options.tileRows - 0.5;
  const columnStart = tile.column / options.tileColumns;
  const columnEnd = (tile.column + options.tileGap) / options.tileColumns;

  return [
    spherePoint(rowStart, columnStart, options.tilt, rotation),
    spherePoint(rowStart, columnEnd, options.tilt, rotation),
    spherePoint(rowEnd, columnEnd, options.tilt, rotation),
    spherePoint(rowEnd, columnStart, options.tilt, rotation)
  ];
}

function spherePoint(row: number, column: number, tilt: number, rotation: number): Point3 {
  const phi = row * Math.PI;
  const theta = column * Math.PI * 2 + rotation;
  const cosPhi = Math.cos(phi);
  const point = {
    x: cosPhi * Math.sin(theta),
    y: Math.sin(phi),
    z: cosPhi * Math.cos(theta)
  };

  return {
    x: point.x,
    y: point.y * Math.cos(tilt) - point.z * Math.sin(tilt),
    z: point.y * Math.sin(tilt) + point.z * Math.cos(tilt)
  };
}

function drawMirrorFlares(context: CanvasRenderingContext2D, candidates: FlareCandidate[], ballRadius: number, options: ResolvedOptions) {
  if (!candidates.length || options.sparkle <= 0) return;

  const selected: FlareCandidate[] = [];
  const sparkleAmount = clamp(options.sparkle, 0, 1);
  const maxCount = Math.max(1, Math.min(3, Math.ceil(sparkleAmount * 3.1)));
  const minDistance = ballRadius * lerp(0.5, 0.3, sparkleAmount);

  for (const candidate of candidates.sort((a, b) => b.score - a.score)) {
    const overlaps = selected.some((flare) => Math.hypot(flare.x - candidate.x, flare.y - candidate.y) < minDistance);
    if (!overlaps) selected.push(candidate);
    if (selected.length >= maxCount) break;
  }

  for (const flare of selected) {
    drawFlare(context, flare);
  }
}

function drawOuterGlow(context: CanvasRenderingContext2D, centerX: number, centerY: number, radius: number, options: ResolvedOptions) {
  if (options.glow <= 0) return;

  context.save();
  context.globalCompositeOperation = "lighter";
  const glowRadius = radius * lerp(1.02, 1.34, clamp(options.glow, 0, 1.8));
  const alpha = clamp(options.glow * 0.12, 0, 0.26);
  const glow = context.createRadialGradient(centerX, centerY, radius * 0.68, centerX, centerY, glowRadius);
  glow.addColorStop(0, "rgba(255,255,255,0)");
  glow.addColorStop(0.58, colorWithAlpha(options.palette.glow, alpha));
  glow.addColorStop(1, "rgba(255,255,255,0)");
  context.fillStyle = glow;
  context.beginPath();
  context.arc(centerX, centerY, glowRadius, 0, Math.PI * 2);
  context.fill();
  context.restore();
}

function drawFlare(context: CanvasRenderingContext2D, flare: FlareCandidate) {
  const { x, y, radius, color, angle, score } = flare;
  context.save();
  context.translate(x, y);
  context.rotate(angle);

  const halo = context.createRadialGradient(0, 0, 0, 0, 0, radius * 1.35);
  halo.addColorStop(0, colorWithAlpha("#ffffff", 0.78));
  halo.addColorStop(0.18, colorWithAlpha(color, 0.38));
  halo.addColorStop(1, "rgba(255,255,255,0)");
  context.fillStyle = halo;
  context.beginPath();
  context.arc(0, 0, radius * 1.35, 0, Math.PI * 2);
  context.fill();

  context.strokeStyle = colorWithAlpha(color, lerp(0.58, 0.92, clamp(score, 0, 1)));
  context.lineWidth = Math.max(0.65, radius * 0.045);
  context.shadowColor = color;
  context.shadowBlur = radius * 0.2;
  context.lineCap = "round";
  context.beginPath();
  context.moveTo(-radius * 1.9, 0);
  context.lineTo(radius * 1.9, 0);
  context.moveTo(0, -radius * 1.15);
  context.lineTo(0, radius * 1.15);
  context.stroke();

  context.globalAlpha = 0.48;
  context.lineWidth = Math.max(0.45, radius * 0.025);
  context.beginPath();
  context.moveTo(-radius * 0.82, -radius * 0.82);
  context.lineTo(radius * 0.82, radius * 0.82);
  context.moveTo(-radius * 0.82, radius * 0.82);
  context.lineTo(radius * 0.82, -radius * 0.82);
  context.stroke();

  context.globalAlpha = 1;
  context.fillStyle = "#ffffff";
  context.beginPath();
  context.arc(0, 0, Math.max(0.75, radius * 0.11), 0, Math.PI * 2);
  context.fill();
  context.restore();
}

function normalize(point: Point3): Point3 {
  const length = Math.hypot(point.x, point.y, point.z) || 1;
  return { x: point.x / length, y: point.y / length, z: point.z / length };
}

function dot(a: Point3, b: Point3): number {
  return a.x * b.x + a.y * b.y + a.z * b.z;
}

function reflectVector(light: Point3, normal: Point3): Point3 {
  const amount = 2 * dot(normal, light);
  return normalize({
    x: amount * normal.x - light.x,
    y: amount * normal.y - light.y,
    z: amount * normal.z - light.z
  });
}

function projectedCenter(points: Array<{ x: number; y: number }>): { x: number; y: number } {
  const total = points.reduce((acc, point) => ({ x: acc.x + point.x, y: acc.y + point.y }), { x: 0, y: 0 });
  const count = Math.max(1, points.length);
  return { x: total.x / count, y: total.y / count };
}

function colorWithAlpha(color: string, alpha: number): string {
  if (!color.startsWith("#")) return color;

  const value = color.slice(1);
  const full = value.length === 3 ? value.split("").map((part) => part + part).join("") : value;
  const number = Number.parseInt(full, 16);
  const red = (number >> 16) & 255;
  const green = (number >> 8) & 255;
  const blue = number & 255;
  return `rgba(${red}, ${green}, ${blue}, ${clamp(alpha, 0, 1)})`;
}

```


