// SKETCH for site/disco.js lines 137-153 (replaces the 96 CSS patches). Plain ES module so it can be exercised in Node:
//   node research/disco-visuals/light-sketch.mjs        -> runs the self-test at the bottom (mock canvas, no browser needed)
// The geometry is checked by projection-check.mjs. The drawing calls have NOT been run in a real browser yet.
const TAU = Math.PI * 2;
const norm = v => { const l = Math.hypot(v[0], v[1], v[2]) || 1e-9; return [v[0] / l, v[1] / l, v[2] / l]; };

// 1. Facets: 56 rows x 112 at the equator (~4000). jx/jy = fixed per-tile tilt (irregularity), gain = per-tile brightness.
export function makeFacets(rows = 56, eq = 112) {
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const out = [];
  for (let i = 0; i < rows; i++) {
    const lat = ((i + .5) / rows - .5) * Math.PI, cols = Math.max(6, Math.round(eq * Math.cos(lat)));
    for (let j = 0; j < cols; j++) out.push({ row: i, col: j, cols, lat, lon: ((j + .5) / cols - .5) * TAU, jx: (rnd() - .5) * .1, jy: (rnd() - .5) * .1, gain: .55 + .45 * rnd() });
  }
  return out;
}

// 2. The same two lamps the ball shader already has (disco.js lines 45-46). d = direction the light TRAVELS = -L.
export const LAMPS = [
  { d: norm([.42, -.5, -.9]), tint: "255,240,205", gain: 1 },   // warm cream
  { d: norm([-.86, -.2, -.5]), tint: "255,150,185", gain: .7 }, // pink gel
];

// 3. Asymmetric twinkle: fast attack (>= 2 frames at 30 fps), exponential decay. t in seconds since the pulse began.
export const pulse = (t, attack = .07, decay = .35) => t < 0 ? 0 : t < attack ? t / attack : Math.exp(-(t - attack) / decay);

// 4. Pre-rendered star: soft core + 4 tapered spikes (+ 4 short diagonals on big sprites). Fixed orientation for ALL stars:
//    diffraction spikes come from the optics (Wikipedia "Diffraction spike"), so they never rotate per star.
export function makeStar(size, tint = "255,246,225", mk = () => document.createElement("canvas")) {
  const c = mk(); c.width = c.height = size;
  const g = c.getContext("2d"), m = size / 2;
  g.globalCompositeOperation = "lighter";
  const core = g.createRadialGradient(m, m, 0, m, m, m * .35);
  core.addColorStop(0, "rgba(255,255,255,1)"); core.addColorStop(.3, `rgba(${tint},.7)`); core.addColorStop(1, `rgba(${tint},0)`);
  g.fillStyle = core; g.fillRect(0, 0, size, size);
  const spikes = (len, half, alpha) => {
    g.save(); g.translate(m, m);
    for (let q = 0; q < 4; q++) {
      g.rotate(Math.PI / 2);
      const lg = g.createLinearGradient(0, 0, len, 0);
      lg.addColorStop(0, `rgba(${tint},${alpha})`); lg.addColorStop(1, `rgba(${tint},0)`);
      g.fillStyle = lg; g.beginPath(); g.moveTo(0, -half); g.lineTo(len, 0); g.lineTo(0, half); g.closePath(); g.fill();
    }
    g.restore();
  };
  spikes(m, Math.max(1, size / 40), .9);
  if (size >= 48) { g.save(); g.translate(m, m); g.rotate(Math.PI / 4); g.translate(-m, -m); spikes(m * .45, Math.max(.7, size / 70), .45); g.restore(); }
  return c;
}

// 5. The projected-light layer. ONE canvas inside the existing .disco-room-light wrapper (which keeps mix-blend-mode: screen).
//    Default alpha:true + clearRect, so if mix-blend-mode ever fails to apply the spots still show over the page instead of a black slab.
//    (alpha:false + black fill is a possible measured optimisation: MDN says it can speed drawing; screen(black) leaves the page untouched.)
export function createLight(canvas, getOrigin, { period = 16, dprCap = 1.5, maxPixels = 1.3e6, size = () => [innerWidth, innerHeight], mk } = {}) {
  const ctx = canvas.getContext("2d");
  const facets = makeFacets();
  const glow = makeStar(32, "255,235,200", mk);          // reused as a halo under the brightest spots (stand-in for a plain radial glow sprite)
  const buckets = [[], [], [], []];                      // quantised brightness -> a handful of fills instead of 1000 fillStyle changes
  let W = 0, H = 0, scale = 1, spin = 0, last = 0, req = 0;

  function resize() {
    const [cw, ch] = size();
    scale = Math.min(globalThis.devicePixelRatio || 1, dprCap, Math.sqrt(maxPixels / (cw * ch)));
    canvas.width = Math.round(cw * scale); canvas.height = Math.round(ch * scale);
    W = cw; H = ch; ctx.setTransform(scale, 0, 0, scale, 0, 0);
  }

  function draw(angle) {
    ctx.globalCompositeOperation = "source-over"; ctx.clearRect(0, 0, W, H);
    ctx.globalCompositeOperation = "lighter";
    const [ox, oy] = getOrigin(W, H);                    // ball centre in viewport px; clamp y >= ~0 so the light keeps reaching the page when the ball scrolls away
    const h = .55 * Math.max(W, H), a = .012;            // h = ball-to-wall distance in px (smaller h = stronger streaks); a = spot half-size in radians
    let glows = 0;
    for (const lamp of LAMPS) {
      buckets.forEach(b => (b.length = 0));
      const d = lamp.d;
      for (const f of facets) {
        const lon = f.lon + angle, cl = Math.cos(f.lat);
        let nx = cl * Math.sin(lon) + f.jx, ny = Math.sin(f.lat) + f.jy, nz = cl * Math.cos(lon);
        const il = 1 / Math.hypot(nx, ny, nz); nx *= il; ny *= il; nz *= il;
        const dn = d[0] * nx + d[1] * ny + d[2] * nz;
        if (dn > -.05) continue;                         // facet faces away from the lamp
        const k = 2 * dn, rx = d[0] - k * nx, ry = d[1] - k * ny, rz = d[2] - k * nz;   // r = d - 2(d.n)n
        if (rz > -.08) continue;                         // heads toward the viewer or along the wall
        const cx = ox + h * rx / -rz, cy = oy - h * ry / -rz;
        if (cx < -40 || cx > W + 40 || cy < -40 || cy > H + 40) continue;
        // footprint = the four rays r +- a*e1 +- a*e2, each intersected with the wall (a real parallelogram, stretched by the geometry)
        const m = Math.hypot(rx, ry) || 1e-6, e1x = ry / m, e1y = -rx / m;                     // e1 (z = 0) is perpendicular to r's xy part
        const e2x = -rz * e1y, e2y = rz * e1x, e2z = rx * e1y - ry * e1x;     // e2 = r x e1
        const pts = [];
        for (const [s1, s2] of [[1, 1], [1, -1], [-1, -1], [-1, 1]]) {
          const qx = rx + a * (s1 * e1x + s2 * e2x), qy = ry + a * (s1 * e1y + s2 * e2y), qz = rz + a * s2 * e2z;
          if (qz > -.05) { pts.length = 0; break; }
          pts.push(ox + h * qx / -qz, oy - h * qy / -qz);
        }
        if (!pts.length) continue;
        const c = -rz, lit = Math.min(1, (-dn - .05) / .3);          // brightness ~ |rz|^3 (flux conserved over a stretched footprint), floored
        const I = Math.max(.12, c * c * c) * f.gain * lamp.gain * lit;
        buckets[Math.min(3, (I * 4) | 0)].push(...pts);
        if (I > .8 && glows < 24) { glows++; ctx.globalAlpha = .3; ctx.drawImage(glow, Math.round(cx - 16), Math.round(cy - 16)); ctx.globalAlpha = 1; }
      }
      buckets.forEach((b, i) => {
        if (!b.length) return;
        ctx.fillStyle = `rgba(${lamp.tint},${(0.25 + i * 0.25).toFixed(2)})`;
        ctx.beginPath();
        for (let j = 0; j < b.length; j += 8) { ctx.moveTo(b[j], b[j + 1]); ctx.lineTo(b[j + 2], b[j + 3]); ctx.lineTo(b[j + 4], b[j + 5]); ctx.lineTo(b[j + 6], b[j + 7]); ctx.closePath(); }
        ctx.fill();
      });
    }
  }

  function frame(now) {                                  // 30 fps cap, same pattern as disco.js lines 117-124; own clock, independent of the ball renderer
    if (now - last >= 1000 / 30) { spin = (spin + Math.min(now - last, 100) / (period * 1000) * TAU) % TAU; last = now; draw(spin); }
    req = requestAnimationFrame(frame);
  }
  resize();
  return {
    resize, draw,
    start() { if (!req) { last = performance.now(); req = requestAnimationFrame(frame); } },
    stop() { cancelAnimationFrame(req); req = 0; },
  };
}

// 6. Choreographed hot tiles on the BALL (shader grid 28 x 56, view tilt 0.18 = disco.js lines 28-38). JS picks <= K tiles whose
//    normal is closest to the mirror half-vector H = normalize(L + V); the shader whitens exactly those (row, col) via `uniform vec3 hot[3]`,
//    and the page canvas draws a star sprite at the same tile. One decision, two renderers, hard cap on simultaneous flashes.
export const BALL = makeFacets(28, 56).map((f, i, all) => ({ ...f, id: i }));
export function pickHotTiles(angle, K = 3, power = 150, minSep = .25) {
  const L = norm([-.42, .5, .9]), H = norm([L[0], L[1], L[2] + 1]);
  const c = Math.cos(.18), s = Math.sin(.18), cand = [];
  for (const t of BALL) {
    const lon = t.lon + angle, cl = Math.cos(t.lat);
    let nx = cl * Math.sin(lon), ny = Math.sin(t.lat), nz = cl * Math.cos(lon);
    [ny, nz] = [ny * c - nz * s, ny * s + nz * c];              // back to view space (shader line 38)
    if (nz < .15) continue;                                     // far side or rim
    const q = norm([nx + t.jx, ny + t.jy, nz]);
    const sc = Math.pow(Math.max(0, q[0] * H[0] + q[1] * H[1] + q[2] * H[2]), power);
    if (sc > .04) cand.push({ id: t.id, row: t.row, col: t.col, x: nx, y: ny, sc });    // x,y = tile centre on the unit disc (screen = centre + (x*R, -y*R))
  }
  cand.sort((a, b) => b.sc - a.sc);
  const out = [];
  for (const t of cand) if (out.length < K && out.every(o => Math.hypot(o.x - t.x, o.y - t.y) > minSep)) out.push(t);
  return out;
}

// ---- self-test (Node): geometry runs, bucketed fills happen, nothing throws, envelope behaves ----
if (import.meta.url === `file://${process.argv[1].replace(/\\/g, "/").replace(/^([A-Za-z]):/, "/$1:")}` || process.argv[1]?.endsWith("light-sketch.mjs")) {
  const calls = {};
  const mkCtx = () => { const o = {}; const p = new Proxy(o, { get: (t, k) => (k in t ? t[k] : (...args) => { calls[k] = (calls[k] || 0) + 1; return p; }), set: (t, k, v) => (t[k] = v, true) }); return p; };
  const mk = () => ({ width: 0, height: 0, getContext: () => mkCtx() });
  const canvas = { width: 0, height: 0, getContext: () => mkCtx() };
  globalThis.devicePixelRatio = 3;
  const light = createLight(canvas, () => [188, 53], { size: () => [390, 844], mk });
  console.assert(canvas.width === 585 && canvas.height === 1266, "dpr should cap at 1.5", canvas.width, canvas.height);
  light.draw(0.7);
  console.log("moveTo calls (one per drawn spot):", calls.moveTo, "| fills:", calls.fill, "| glow sprites:", calls.drawImage);
  console.assert(calls.moveTo > 300 && calls.moveTo < 1500, "expected hundreds of spots on a 390x844 phone viewport");
  console.assert(calls.fill >= 4 && calls.fill < 40, "fills should be bucketed");
  console.assert(pulse(0.07) === 1 && pulse(0.5) < 0.6 && pulse(-1) === 0, "envelope");
  const star = makeStar(96, undefined, mk); console.assert(star.width === 96);
  let tot = 0, mx = 0, cnt = 0; for (let k = 0; k < 128; k++) { const hot = pickHotTiles((k / 128) * TAU); tot += hot.length; cnt += hot.filter(t => t.sc > .5).length; mx = Math.max(mx, hot.length); }
  console.log("ball (power 150, minSep .25): mean tiles picked", (tot / 128).toFixed(2), "| mean >50% lit", (cnt / 128).toFixed(2), "| max picked at once:", mx);
  console.assert(mx <= 3, "cap on simultaneous flashes");
  // the shader consumes (row, col): check what the picker returns is a valid tile index in the shader's grid (28 rows, cols = max(6, round(56*cos(lat))))
  for (let k = 0; k < 64; k++) for (const t of pickHotTiles((k / 64) * TAU, 3, 150)) {
    const lat = ((t.row + .5) / 28 - .5) * Math.PI, cols = Math.max(6, Math.round(56 * Math.cos(lat)));
    console.assert(Number.isInteger(t.row) && t.row >= 0 && t.row < 28 && Number.isInteger(t.col) && t.col >= 0 && t.col < cols, "bad tile index", t);
  }
  // measured by hand: minSep .45 never returns more than 1 tile at any power; minSep .25 with power 60-150 reaches 3.
  console.log("self-test ok");
}
