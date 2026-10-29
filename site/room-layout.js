// Deterministic staging from local panoptic masks. Coordinates are photo
// fractions, never inches. Uncertain supports stay empty.
export function semanticGroup(label) {
  const id = Number(/^LABEL_(\d+)$/.exec(label)?.[1]);
  if ([186].includes(id) || /^ceiling/.test(label)) return "ceiling";
  if ([190, 200].includes(id) || /^(floor|rug)/.test(label)) return "floor";
  if ([199].includes(id) || /^wall/.test(label)) return "wall";
  if (label === "couch" || label === "sofa") return "sofa";
  if ([189].includes(id) || /^(dining table|table)/.test(label)) return "table";
  if ([188].includes(id) || /^cabinet/.test(label)) return "cabinet";
  return "obstacle";
}

export function layerBox(layer, photoAspect) {
  const height = layer.w * layer.ratio * photoAspect;
  return { x: layer.x - layer.w / 2, y: layer.y - height / 2, w: layer.w, h: height };
}

export function constrainLayer(layer, photoAspect) {
  layer.w = Math.max(.025, Math.min(layer.w, .85, .94 / (layer.ratio * photoAspect)));
  const { w, h } = layerBox(layer, photoAspect);
  layer.x = Math.max(w / 2, Math.min(1 - w / 2, layer.x));
  layer.y = Math.max(h / 2, Math.min(1 - h / 2, layer.y));
  return layer;
}

function components(mask, width, height) {
  const seen = new Uint8Array(mask.length);
  const regions = [];
  for (let start = 0; start < mask.length; start++) {
    if (!mask[start] || seen[start]) continue;
    const queue = [start];
    seen[start] = 1;
    let left = width, top = height, right = 0, bottom = 0, sumX = 0, sumY = 0;
    const edge = new Array(width).fill(height);
    for (let at = 0; at < queue.length; at++) {
      const index = queue[at], x = index % width, y = Math.floor(index / width);
      sumX += x; sumY += y;
      left = Math.min(left, x); right = Math.max(right, x);
      top = Math.min(top, y); bottom = Math.max(bottom, y); edge[x] = Math.min(edge[x], y);
      for (const next of [x > 0 ? index - 1 : -1, x + 1 < width ? index + 1 : -1, index - width, index + width]) {
        if (next >= 0 && next < mask.length && mask[next] && !seen[next]) { seen[next] = 1; queue.push(next); }
      }
    }
    if (queue.length < width * height * .003) continue;
    const topEdges = edge.slice(left + Math.floor((right - left) * .2), right - Math.floor((right - left) * .2) + 1).filter(y => y < height).sort((a, b) => a - b);
    regions.push({ x: left / width, y: top / height, w: (right - left + 1) / width, h: (bottom - top + 1) / height,
      area: queue.length, centerX: sumX / queue.length / width, centerY: sumY / queue.length / height,
      supportY: (topEdges[Math.floor(topEdges.length / 2)] ?? top) / height });
  }
  return regions.sort((a, b) => b.area - a.area || a.x - b.x);
}

function coverage(mask, grid, box) {
  const { width, height } = grid;
  if (box.x < 0 || box.y < 0 || box.x + box.w > 1.001 || box.y + box.h > 1.001) return 0;
  let count = 0, hits = 0;
  for (let y = Math.max(0, Math.floor(box.y * height)); y < Math.min(height, Math.ceil((box.y + box.h) * height)); y++) {
    for (let x = Math.max(0, Math.floor(box.x * width)); x < Math.min(width, Math.ceil((box.x + box.w) * width)); x++) {
      count++; if (mask[y * width + x]) hits++;
    }
  }
  return count ? hits / count : 0;
}

function overlap(a, b) {
  const area = Math.max(0, Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x)) *
    Math.max(0, Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y));
  return area / Math.min(a.w * a.h, b.w * b.h);
}

export function roomSlots(grid) {
  const { width, height, segments } = grid;
  const masks = Object.fromEntries(["wall", "floor", "ceiling", "sofa", "table", "cabinet", "obstacle"].map(group => [group, new Uint8Array(width * height)]));
  const supports = [];
  for (const segment of segments) {
    if (segment.score != null && segment.score < .5) continue;
    const group = semanticGroup(segment.label);
    for (let index = 0; index < segment.mask.length; index++) if (segment.mask[index]) masks[group][index] = 1;
    if (["table", "cabinet", "sofa"].includes(group)) supports.push(...components(segment.mask, width, height).map(region => ({ ...region, group })));
  }
  const sofas = supports.filter(region => region.group === "sofa").sort((a, b) => b.area - a.area);
  const sofa = sofas[0];
  const slots = [];
  const add = (kind, x, bottom, w, h, extra = {}) => {
    if (w < .035 || h < .035) return;
    slots.push({ id: slots.length, kind, x, bottom, w, h, ...extra });
  };
  for (const seat of sofas.slice(0, 2)) add("art", seat.x + seat.w / 2, seat.y - .025, seat.w * .66, Math.min(.34, seat.y - .05));
  // Cushions rest on a detected sofa seat; no sofa, no cushion slot.
  if (sofa) for (const fraction of [.5, .32, .68]) add("cushion", sofa.x + sofa.w * fraction, sofa.y + sofa.h * .55, sofa.w * .17, sofa.h * .5);
  const walls = components(masks.wall, width, height);
  for (const wall of walls.slice(0, 2)) {
    for (const vertical of [.6, .4, .8]) for (const fraction of [.5, .25, .75]) {
      add("art", wall.x + wall.w * fraction, Math.min(.65, wall.y + wall.h * vertical), Math.min(.22, wall.w * .4), Math.min(.3, wall.h * .5));
    }
  }
  const ceilings = components(masks.ceiling, width, height);
  if (ceilings[0]) {
    const ceiling = ceilings[0];
    // Anchor in the detected ceiling, rather than at an assumed image edge.
    for (const x of [ceiling.centerX, ceiling.x + ceiling.w * .3, ceiling.x + ceiling.w * .7]) {
      add("ceiling", x, ceiling.centerY, Math.min(.2, ceiling.w * .35), .3, { anchorTop: true });
    }
  }
  for (const support of supports.filter(region => region.group !== "sofa")) {
    const center = support.x + support.w / 2;
    const besideSofa = sofa && (center < sofa.x || center > sofa.x + sofa.w) && support.w < sofa.w * .6 &&
      Math.abs(support.supportY - (sofa.y + sofa.h * .3)) < Math.max(.1, sofa.h * .55);
    const console = support.group === "cabinet" && support.w / support.h > 1.2;
    // COCO cannot distinguish coffee tables. Lamps require a positively
    // inferred side table or a broad cabinet; unknown tables get low decor.
    const count = besideSofa ? 1 : 2;
    for (let index = 0; index < count; index++) {
      const x = besideSofa ? center : support.x + support.w * (index ? .75 : .25);
      add(besideSofa || console ? "lamp-or-decor" : "decor", x, support.supportY + .005,
        support.w * (besideSofa ? .48 : .32), Math.min(.36, support.supportY - .03), { support: { ...support } });
    }
    if (console) add("art", center, support.supportY - .025, support.w * .65, Math.min(.3, support.y - .05));
  }
  // Two possible floor positions, only where an actual floor footprint fits.
  for (const floor of components(masks.floor, width, height).slice(0, 2)) {
    const positions = sofa ? [sofa.x - .075, sofa.x + sofa.w + .075] : [floor.x + floor.w * .2, floor.x + floor.w * .8];
    for (const x of positions) add("floor", x, Math.min(.94, floor.y + floor.h * .9), .14, .42);
  }
  return { slots, masks, ...grid };
}

const noSlot = {
  art: "No clear wall space was found.", ceiling: "No clear ceiling position was found.",
  lamp: "No confirmed side table or console has room for this lamp.",
  decor: "No clear tabletop position was found.", media: "No clear tabletop position was found.",
  cushion: "No clear sofa seat was found for this cushion.",
  floor: "No clear floor position was found.",
};

export function arrangeRoom(products, grid, photoAspect) {
  const scene = grid.slots ? grid : roomSlots(grid);
  const layers = [], unplaced = [], used = new Set();
  const rank = { ceiling: 0, art: 1, lamp: 2, floor: 3, cushion: 4, media: 5, decor: 6 };
  const ordered = [...products].sort((a, b) => (rank[a.kind] ?? 9) - (rank[b.kind] ?? 9) || a.id.localeCompare(b.id, "en", { numeric: true }));
  for (const product of ordered) {
    if (!product.overlay || !product.ratio) { unplaced.push({ id: product.id, reason: "A clear product cutout is needed. You can still save this find." }); continue; }
    let placed = false, tooBig = false;
    for (const slot of scene.slots) {
      if (used.has(slot.id)) continue;
      const legal = product.kind === "lamp" ? slot.kind === "lamp-or-decor" :
        ["decor", "media"].includes(product.kind) ? ["decor", "lamp-or-decor"].includes(slot.kind) : slot.kind === product.kind;
      if (!legal || product.kind === "art" && layers.filter(layer => layer.kind === "art").length >= 2 || product.kind === "floor" && layers.filter(layer => layer.kind === "floor").length >= 2) continue;
      // Real size: a find with a size in cm, in a slot with a scale, is drawn at that size,
      // capped to the slot and never enlarged. Under 70% of real size, the slot cannot hold it.
      const fit = Math.min(slot.w, slot.h / (product.ratio * photoAspect));
      const real = product.cm && slot.ppm ? product.cm / 100 / Math.max(1, product.ratio) * slot.ppm : Infinity;
      if (real < Infinity && fit < real * .7) { tooBig = true; continue; }
      for (const scale of [1, .85, .7]) {
        const w = Math.min(fit, real) * scale;
        if (w < Math.min(.035, real * .7)) continue;
        const h = w * product.ratio * photoAspect;
        const layer = { id: product.id, kind: product.kind, x: slot.x, y: slot.bottom + (slot.anchorTop ? h / 2 : -h / 2), w, ratio: product.ratio, flip: false };
        const box = layerBox(layer, photoAspect);
        if (box.x < .01 || box.y < .01 || box.x + box.w > .99 || box.y + box.h > .99) continue;
        // Uploaded rooms need mask checks. The shipped sample has reviewed
        // empty bounds instead; both paths retain size, capacity and overlap checks.
        if (scene.masks) {
          if (product.kind === "art" && coverage(scene.masks.wall, grid, box) < .88) continue;
          if (product.kind === "ceiling" && coverage(scene.masks.ceiling, grid, { x: layer.x - .01, y: box.y, w: .02, h: .01 }) < .6) continue;
          if (product.kind === "floor" && coverage(scene.masks.floor, grid, { x: box.x, y: box.y + box.h - .015, w: box.w, h: .015 }) < .8) continue;
          if (coverage(scene.masks.obstacle, grid, box) > .03) continue;
          // A cushion must sit on the sofa; everything else must stay off it.
          if (product.kind === "cushion" && coverage(scene.masks.sofa, grid, box) < .75) continue;
          if ((product.kind === "cushion" ? ["table", "cabinet"] : ["sofa", "table", "cabinet"]).some(group => coverage(scene.masks[group], grid, { ...box, h: Math.max(.001, box.h - .012) }) > .05)) continue;
        }
        // Tabletop finds stand in front of the sofa (and draw after cushions), so they may cover part of one.
        if (layers.some(other => !(other.kind === "cushion" && ["decor", "media"].includes(product.kind)) && overlap(box, layerBox(other, photoAspect)) > .05)) continue;
        layers.push(layer); used.add(slot.id); placed = true; break;
      }
      if (placed) break;
    }
    if (!placed) unplaced.push({ id: product.id, reason: tooBig ? "Too big for the open space in this room." : noSlot[product.kind] || "No suitable position was found." });
  }
  return { layers, unplaced, slotCount: scene.slots.length };
}
