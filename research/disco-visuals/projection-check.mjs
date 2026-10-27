// Runnable check for the projection math in REPORT.md. No dependencies: `node research/disco-visuals/projection-check.mjs`
// Model: ball centre B sits `h` px in FRONT of the page (the wall is the plane z=0, viewer on +z).
// Facet grid mirrors site/disco.js shader lines 30-32: 28 rows, columns = max(6, round(56*cos(lat))).
const TAU = Math.PI * 2;
// rows x (cols at equator): the shader uses 28 x 56 (disco.js lines 30-32). Denser grids are tested below.
function makeFacets(rows, eq) {
  const out = [];
  for (let i = 0; i < rows; i++) {
    const lat = ((i + 0.5) / rows - 0.5) * Math.PI;
    const cols = Math.max(6, Math.round(eq * Math.cos(lat)));
    for (let j = 0; j < cols; j++) out.push({ lat, lon: ((j + 0.5) / cols - 0.5) * TAU });
  }
  return out;
}
let facets = makeFacets(28, 56);
const norm = v => { const l = Math.hypot(...v); return v.map(x => x / l); };
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

// One facet -> {n, r, t, hit}. spin rotates the ball about its vertical (y) axis.
function cast(f, spin, d, h) {
  const lon = f.lon + spin;
  const n = [Math.cos(f.lat) * Math.sin(lon), Math.sin(f.lat), Math.cos(f.lat) * Math.cos(lon)]; // unit by construction
  const dn = dot(d, n);
  if (dn >= -0.02) return { n, lit: false };                       // facet faces away from the lamp
  const r = [d[0] - 2 * dn * n[0], d[1] - 2 * dn * n[1], d[2] - 2 * dn * n[2]]; // r = d - 2(d.n)n
  if (r[2] >= -0.05) return { n, r, lit: true, hit: false };       // heads toward the viewer / parallel to the wall
  const t = h / -r[2];                                             // ray B + t*r reaches z=0 when h + t*r.z = 0
  return { n, r, lit: true, hit: true, t, x: h * r[0] / -r[2], y: h * r[1] / -r[2], rz: -r[2] };
}

// 1. identities (the reflection is a mirror: unit length, and r.n = -(d.n))
{
  const d = norm([0.3, -0.7, -0.4]);
  let worst = 0;
  for (const f of facets) {
    const c = cast(f, 0.37, d, 500);
    if (!c.r) continue;
    worst = Math.max(worst, Math.abs(Math.hypot(...c.r) - 1), Math.abs(dot(c.r, c.n) + dot(d, c.n)));
  }
  console.assert(worst < 1e-12, "reflection identities broke", worst);
  // angle doubling: tilt a lit mirror by a about the axis k = d x n (perpendicular to both) and r must turn by exactly 2a
  const cross = (u, v) => [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]];
  const f = facets.map(f => cast(f, 0, d, 500)).find(c => c.hit && dot(d, c.n) < -0.5);
  const k = norm(cross(d, f.n)), a = 0.01;
  const rot = (v) => { const c = Math.cos(a), s = Math.sin(a), kv = cross(k, v), kd = dot(k, v); return v.map((x, i) => x * c + kv[i] * s + k[i] * kd * (1 - c)); };
  const n2 = rot(f.n), dn2 = dot(d, n2), r2 = d.map((x, i) => x - 2 * dn2 * n2[i]);
  const turn = Math.acos(Math.min(1, dot(f.r, r2)));
  console.assert(Math.abs(turn - 2 * a) < 1e-9, "angle doubling broke", turn / a);
  console.log("facets:", facets.length, "| max identity error:", worst.toExponential(1), "| tilt 0.0100 rad -> reflected ray turns", turn.toFixed(4), "rad (2x)");
}

// 2. how many facets throw a spot INSIDE the viewport? (average over one revolution)
function run(label, W, H, ball, lamp, hMul, aRad = 0.03) {
  const d = norm(lamp), h = hMul * Math.max(W, H);
  let counts = [], minC = 1e9, maxC = 0, elong = [], sizes = [], area = 0;
  for (let s = 0; s < 32; s++) {
    let c = 0;
    for (const f of facets) {
      const k = cast(f, (s / 32) * TAU, d, h);
      if (!k.hit) continue;
      const px = ball[0] + k.x, py = ball[1] - k.y;
      if (px < -20 || px > W + 20 || py < -20 || py > H + 20) continue;
      c++;
      elong.push(1 / k.rz);                                          // radial/tangential stretch of a spot = 1/|r.z|
      sizes.push(h * aRad / (k.rz * k.rz));                          // radial length of an aRad spot
      area += (h * aRad / (k.rz * k.rz)) * (h * aRad / k.rz);        // radial x tangential footprint, px^2
    }
    counts.push(c); minC = Math.min(minC, c); maxC = Math.max(maxC, c);
  }
  const mean = counts.reduce((a, b) => a + b) / counts.length;
  elong.sort((a, b) => a - b); sizes.sort((a, b) => a - b);
  const q = (arr, p) => arr[Math.floor(arr.length * p)]?.toFixed(1);
  console.log(`${label.padEnd(34)} h=${h.toFixed(0)}px lamp=[${lamp}]  spots in view: mean ${mean.toFixed(0)} (min ${minC}, max ${maxC})  elongation p50/p90 ${q(elong, .5)}/${q(elong, .9)}  radial length px p50/p90 ${q(sizes, .5)}/${q(sizes, .9)}  coverage ${(100 * area / 32 / (W * H)).toFixed(0)}%`);
}
const phone = [390, 844], desk = [1440, 900];
// The two lamps already in the shader (disco.js lines 45-46: warm L=(-.42,.5,.9), pink L=(.86,.2,.5)); beam direction d = -L.
const warm = norm([0.42, -0.5, -0.9]), pink = norm([-0.86, -0.2, -0.5]);
for (const [rows, eq] of [[28, 56], [42, 84], [56, 112]]) {
  facets = makeFacets(rows, eq);
  console.log(`\n--- facet grid ${rows} x ${eq} = ${facets.length} facets ---`);
  for (const hMul of [0.5, 0.9]) {
    for (const [name, lamp] of [["warm", warm], ["pink", pink]]) {
      run(`phone ${name} h=${hMul}`, ...phone, [188, 53], lamp, hMul);
      run(`desk  ${name} h=${hMul}`, ...desk, [760, 70], lamp, hMul);
    }
  }
}

// 3. recommended starting point: 56 x 112 light grid, h = 0.55 * max(W,H), warm + pink lamps, spot half-size 0.012 rad
facets = makeFacets(56, 112);
console.log("\n--- recommended: 56 x 112 =", facets.length, "facets, h=0.55, aRad=0.012 ---");
for (const [name, lamp] of [["warm", warm], ["pink", pink]]) {
  run(`phone ${name}`, ...phone, [188, 53], lamp, 0.55, 0.012);
  run(`desk  ${name}`, ...desk, [760, 70], lamp, 0.55, 0.012);
}

// 4. h sweep: smaller h (ball closer to the wall) = more grazing rays on screen = stronger streaks and more spots
console.log("\n--- h sweep, warm lamp, 56 x 112, aRad=0.012 ---");
for (const hMul of [0.2, 0.3, 0.55]) {
  run(`phone h=${hMul}`, ...phone, [188, 53], warm, hMul, 0.012);
  run(`desk  h=${hMul}`, ...desk, [760, 70], warm, hMul, 0.012);
}

// 5. mirror-flash density on the BALL: a flat tile flashes toward the viewer when its normal ~ H = normalize(L + V).
//    How many of the visible tiles are > 50% lit at once, for several exponents? (view-space normals, shader tilt 0.18, 28 x 56 grid)
{
  const g = makeFacets(28, 56), c = Math.cos(0.18), s = Math.sin(0.18);
  const L = norm([-0.42, 0.5, 0.9]), V = [0, 0, 1], H = norm([L[0] + V[0], L[1] + V[1], L[2] + V[2]]);
  let seed = 1; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647) - 0.5;
  const jit = g.map(() => [rnd(), rnd()]);                                   // per-tile tilt, both axes (the shader today jitters longitude by +-0.006 only)
  console.log("\n--- ball flash: tiles >50% lit at once (mean over 64 spin angles), visible tiles ~", g.filter(f => Math.cos(f.lat) * Math.cos(f.lon) > 0).length);
  for (const jitter of [0.006, 0.1]) {
    for (const p of [90, 300, 700, 1500]) {
      let total = 0;
      for (let a = 0; a < 64; a++) {
        const spin = (a / 64) * TAU;
        g.forEach((f, i) => {
          const lon = f.lon + spin;
          let n = [Math.cos(f.lat) * Math.sin(lon), Math.sin(f.lat), Math.cos(f.lat) * Math.cos(lon)];
          n = [n[0], n[1] * c - n[2] * s, n[1] * s + n[2] * c];            // back to view space, as shader line 38
          if (n[2] <= 0) return;                                           // far side
          n = norm([n[0] + jit[i][0] * 2 * jitter, n[1] + jit[i][1] * 2 * jitter, n[2]]);
          if (Math.pow(Math.max(dot(n, H), 0), p) > 0.5) total++;
        });
      }
      console.log(`  tilt jitter +-${jitter} rad, exponent ${String(p).padStart(4)}: ${(total / 64).toFixed(2)} tiles lit at once (half-width of one tile's flash ${(Math.acos(0.5 ** (1 / p)) * 180 / Math.PI).toFixed(1)} deg)`);
    }
  }
}

// 6. CPU cost of the geometry only (desktop Node/V8, NOT a phone): 3998 facets x 2 lamps, 4 corner rays per lit visible facet.
{
  facets = makeFacets(56, 112);
  const lampsB = [warm, pink], t0 = performance.now(), FR = 200;
  let sink = 0;
  for (let fr = 0; fr < FR; fr++) {
    const spin = (fr / 60) * 0.39;
    for (const d of lampsB) for (const f of facets) {
      const k = cast(f, spin, d, 464);
      if (!k.hit) continue;
      const e1 = norm([k.r[1], -k.r[0], 0]), e2 = [k.r[1] * e1[2] - k.r[2] * e1[1], k.r[2] * e1[0] - k.r[0] * e1[2], k.r[0] * e1[1] - k.r[1] * e1[0]];
      for (const [sx, sy] of [[1, 1], [1, -1], [-1, -1], [-1, 1]]) {
        const q = norm([k.r[0] + 0.012 * (sx * e1[0] + sy * e2[0]), k.r[1] + 0.012 * (sx * e1[1] + sy * e2[1]), k.r[2] + 0.012 * (sx * e1[2] + sy * e2[2])]);
        if (q[2] < -0.05) sink += 464 * q[0] / -q[2];
      }
    }
  }
  console.log(`\n--- geometry cost: ${((performance.now() - t0) / FR).toFixed(2)} ms/frame on this desktop CPU (sink ${Math.round(sink) % 7}); a phone will be slower, not measured`);
}

// 7. inverse mapping used by the "single fragment shader" option: from a wall point back to the mirror normal that lights it.
//    n = normalize(r - d)  (because r - d = -2(d.n)n = 2|d.n| n for a lit facet)
{
  const d = warm, h = 464; let worst = 0, tested = 0;
  for (const f of makeFacets(28, 56)) {
    const k = cast(f, 0.9, d, h);
    if (!k.hit) continue;
    const r = norm([k.x, k.y, -h]);                                   // ray from the ball to the wall point (x, y), as a shader would build it per pixel
    const n = norm([r[0] - d[0], r[1] - d[1], r[2] - d[2]]);
    worst = Math.max(worst, Math.hypot(n[0] - k.n[0], n[1] - k.n[1], n[2] - k.n[2])); tested++;
  }
  console.assert(worst < 1e-9, "inverse mapping broke", worst);
  console.log(`\n--- inverse mapping n = normalize(r - d): ${tested} facets, max error ${worst.toExponential(1)}`);
}
