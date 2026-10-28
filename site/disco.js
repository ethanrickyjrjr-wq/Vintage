(() => {
  // A spherical mirror grid rotates about its suspension axis. Each facet
  // samples the original photograph's reflected room colors; the lights stay
  // fixed in the room, so highlights pass from mirror to mirror naturally.
  const vertexSource = `#version 300 es
    in vec2 position;
    out vec2 uv;
    void main() {
      uv = position * 0.5 + 0.5;
      gl_Position = vec4(position, 0.0, 1.0);
    }`;
  const fragmentSource = `#version 300 es
    precision highp float;
    in vec2 uv;
    uniform sampler2D room;
    uniform float angle;
    uniform float pixel;
    uniform float energy;
    out vec4 color;
    const float PI = 3.14159265359;
    const float TAU = 6.28318530718;
    float grain(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
    void main() {
      vec2 p = uv * 2.0 - 1.0;
      float radius = dot(p, p);
      if (radius >= 1.0) discard;
      vec3 normal = vec3(p, sqrt(1.0 - radius));
      // A slightly elevated viewpoint shows the top, as in the original photo.
      float c = cos(0.18), s = sin(0.18);
      vec3 local = vec3(normal.x, normal.y*c + normal.z*s, -normal.y*s + normal.z*c);
      float row = (asin(local.y) / PI + 0.5) * 28.0;
      float latitude = ((floor(row) + 0.5) / 28.0 - 0.5) * PI;
      float columns = max(6.0, floor(56.0 * cos(latitude) + 0.5));
      float column = fract((atan(local.x, local.z) - angle) / TAU + 0.5) * columns;
      float longitude = ((floor(column) + 0.5) / columns - 0.5) * TAU + angle;
      float variation = grain(vec2(floor(column), floor(row)));
      longitude += (variation - 0.5) * 0.012;
      vec3 facet = vec3(cos(latitude)*sin(longitude), sin(latitude), cos(latitude)*cos(longitude));
      facet = vec3(facet.x, facet.y*c - facet.z*s, facet.y*s + facet.z*c);
      vec2 reflection = vec2(0.5 + facet.x*0.455, 0.525 - facet.y*0.45);
      vec3 silver = texture(room, reflection).rgb;
      silver = mix(silver, texture(room, reflection + vec2(0.004, 0.003)).rgb, 0.35);
      float grey = dot(silver, vec3(0.299, 0.587, 0.114));
      silver = mix(vec3(grey), silver, 0.72) * (0.88 + variation*0.18);
      // A tile catches the lamp when its normal bisects lamp and camera rays.
      float warm = pow(max(dot(facet, normalize(vec3(-0.42, 0.5, 0.9))), 0.0), 90.0);
      float pink = pow(max(dot(facet, normalize(vec3(0.86, 0.2, 0.5))), 0.0), 50.0);
      silver += vec3(1.0, 0.91, 0.74) * warm * 0.55;
      silver += vec3(0.9, 0.37, 0.48) * pink * 0.26;
      float flash = pow(max(dot(facet, normalize(normalize(vec3(-0.42, 0.5, 0.9)) + vec3(0, 0, 1))), 0.0), 1500.0);
      silver += vec3(1.0, 0.98, 0.91) * flash * (1.15 + energy * 0.2);
      silver *= 0.75 + 0.25*sqrt(normal.z);
      vec2 cell = fract(vec2(column, row));
      vec2 edge = min(cell, 1.0-cell);
      vec2 aa = min(fwidth(vec2(column, row))*0.65, vec2(0.18));
      vec2 seam = smoothstep(vec2(0.018), vec2(0.018)+aa, edge);
      float mirror = seam.x*seam.y;
      vec3 grout = vec3(0.31, 0.27, 0.23) * (0.65 + normal.z*0.35);
      vec3 surface = mix(grout, silver, mirror);
      float alpha = 1.0-smoothstep(1.0-pixel*2.0, 1.0, radius);
      color = vec4(surface*alpha, alpha);
    }`;

  function createRenderer(canvas, image) {
    const gl = canvas.getContext("webgl2", { alpha: true, antialias: false, powerPreference: "low-power" });
    if (!gl) return null;
    function compile(type, source) {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        const message = gl.getShaderInfoLog(shader);
        gl.deleteShader(shader);
        throw new Error(message);
      }
      return shader;
    }
    const program = gl.createProgram();
    const vertex = compile(gl.VERTEX_SHADER, vertexSource);
    const fragment = compile(gl.FRAGMENT_SHADER, fragmentSource);
    gl.attachShader(program, vertex);
    gl.attachShader(program, fragment);
    gl.linkProgram(program);
    gl.deleteShader(vertex);
    gl.deleteShader(fragment);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(program));
    gl.useProgram(program);
    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 1,-1, -1,1, -1,1, 1,-1, 1,1]), gl.STATIC_DRAW);
    const position = gl.getAttribLocation(program, "position");
    gl.enableVertexAttribArray(position);
    gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0);
    const texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);
    // Keep image coordinates top-down to match the photographed ball bounds.
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.uniform1i(gl.getUniformLocation(program, "room"), 0);
    const angleUniform = gl.getUniformLocation(program, "angle");
    const pixelUniform = gl.getUniformLocation(program, "pixel");
    const energyUniform = gl.getUniformLocation(program, "energy");
    let angle = 0;
    function draw(nextAngle = angle, energy = 0) {
      angle = nextAngle;
      gl.uniform1f(angleUniform, angle);
      gl.uniform1f(energyUniform, energy);
      gl.clear(gl.COLOR_BUFFER_BIT);
      gl.drawArrays(gl.TRIANGLES, 0, 6);
    }
    function resize() {
      const size = Math.min(640, Math.max(128, Math.round(canvas.clientWidth * Math.min(devicePixelRatio || 1, 1.5))));
      if (canvas.width !== size || canvas.height !== size) {
        canvas.width = canvas.height = size;
        gl.viewport(0, 0, size, size);
        gl.uniform1f(pixelUniform, 2 / size);
      }
      draw();
    }
    resize();
    return { resize, draw };
  }

  const reduced = matchMedia("(prefers-reduced-motion: reduce)");
  const toggle = document.querySelector(".disco-motion-toggle");
  const sparkleToggle = document.querySelector(".salon-disco");
  const roomToggle = document.querySelector("#room-disco");
  const header = document.querySelector(".site-header");
  let source = sparkleToggle;
  let discoOn = false;
  // The page is a wall behind the ball. Reflect two fixed pinspots from the
  // same spherical tile grid used above, then intersect their rays with it.
  const lightField = document.createElement("div");
  lightField.className = "disco-room-light";
  lightField.setAttribute("aria-hidden", "true");
  const projection = document.createElement("canvas");
  lightField.append(projection);
  document.body.append(lightField);
  const ctx = projection.getContext("2d", { alpha: true, desynchronized: true });
  const TAU = Math.PI * 2;
  const facets = [];
  for (let row = 0; row < 28; row++) {
    const latitude = ((row + .5) / 28 - .5) * Math.PI;
    const columns = Math.max(6, Math.round(56 * Math.cos(latitude)));
    for (let column = 0; column < columns; column++) {
      const variation = Math.sin(column * 127.1 + row * 311.7) * 43758.5453;
      const grain = variation - Math.floor(variation);
      const longitude = ((column + .5) / columns - .5) * TAU + (grain - .5) * .012;
      facets.push({ x: Math.cos(latitude) * Math.sin(longitude), y: Math.sin(latitude), z: Math.cos(latitude) * Math.cos(longitude), grain });
    }
  }
  const lamps = [
    { direction: [.42, -.5, -.9], color: "255,246,224", strength: 1 },
    { direction: [-.86, -.2, -.5], color: "255,199,215", strength: .4 },
  ].map(lamp => {
    const length = Math.hypot(...lamp.direction);
    return { ...lamp, direction: lamp.direction.map(value => value / length) };
  });
  // A photographic diffraction catch has a soft core and tapered rays.
  // It belongs to a projected facet; it never floats independently of the ball.
  const star = document.createElement("canvas");
  star.width = star.height = 64;
  const starCtx = star.getContext("2d");
  if (starCtx) {
    const halo = starCtx.createRadialGradient(32, 32, 0, 32, 32, 30);
    halo.addColorStop(0, "#fffef1b3");
    halo.addColorStop(.15, "#fff4da33");
    halo.addColorStop(1, "#fff4da00");
    starCtx.fillStyle = halo;
    starCtx.fillRect(0, 0, 64, 64);
    starCtx.fillStyle = "#fffdf0b3";
    starCtx.beginPath();
    [[32, 3], [34, 29], [61, 32], [34, 35], [32, 61], [30, 35], [3, 32], [30, 29]].forEach(([x, y], i) => i ? starCtx.lineTo(x, y) : starCtx.moveTo(x, y));
    starCtx.closePath();
    starCtx.fill();
  }
  let width = 0, height = 0, originX = 0, originY = 0, depth = 0;
  let phase = 0, tempo = 120, request = 0, lastPaint = 0, lastGlint = -Infinity, glint = null;
  const glintHistory = new Map();
  function resizeLights() {
    width = innerWidth;
    height = innerHeight;
    const ratio = Math.min(devicePixelRatio || 1, 1.5);
    projection.width = Math.round(width * ratio);
    projection.height = Math.round(height * ratio);
    ctx?.setTransform(ratio, 0, 0, ratio, 0, 0);
    depth = Math.max(width, height) * .55;
    aim();
  }
  // Light comes from whichever ball started the disco. The room's ball keeps its light inside the room photo.
  function aim() {
    const room = source === roomToggle, bounds = source?.getBoundingClientRect();
    originX = bounds ? bounds.left + bounds.width / 2 : width * .53;
    originY = !bounds ? 70 : room ? bounds.top + bounds.height / 2 : Math.max(50, Math.min(height * .22, bounds.top + bounds.height / 2));
    const stage = room ? roomToggle.parentElement.getBoundingClientRect() : null;
    lightField.style.clipPath = stage ? `inset(${Math.max(stage.top, header?.getBoundingClientRect().bottom ?? 0)}px ${width - stage.right}px ${height - stage.bottom}px ${stage.left}px)` : "";
  }
  function drawLights(now, music) {
    if (!ctx) return;
    ctx.clearRect(0, 0, width, height);
    ctx.globalCompositeOperation = "lighter";
    const c = Math.cos(phase), s = Math.sin(phase), tiltC = Math.cos(.18), tiltS = Math.sin(.18);
    let candidate = null;
    const canGlint = music.pulse > .4 && now - lastGlint > 950;
    if (glint && now - glint.born > 420) glint = null;
    if (glint) glint.visible = false;
    lamps.forEach((lamp, lampIndex) => {
      const [dx, dy, dz] = lamp.direction;
      ctx.fillStyle = `rgb(${lamp.color})`;
      facets.forEach((facet, index) => {
        const nx = facet.x * c + facet.z * s;
        const rotatedZ = facet.z * c - facet.x * s;
        const ny = facet.y * tiltC - rotatedZ * tiltS;
        const nz = facet.y * tiltS + rotatedZ * tiltC;
        const incidence = dx * nx + dy * ny + dz * nz;
        if (incidence >= -.02) return;
        const rx = dx - 2 * incidence * nx, ry = dy - 2 * incidence * ny, rz = dz - 2 * incidence * nz;
        if (rz >= -.12) return;
        const x = originX + depth * rx / -rz, y = originY - depth * ry / -rz;
        if (x < -24 || x > width + 24 || y < -24 || y > height + 24) return;
        const radial = Math.hypot(rx, ry);
        const ux = radial > .0001 ? -ry / radial : 1, uy = radial > .0001 ? rx / radial : 0;
        const vx = -rz * uy, vy = rz * ux, vz = rx * uy - ry * ux;
        const spread = .0055 * (.8 + facet.grain * .4);
        const alpha = lamp.strength * (.12 + facet.grain * facet.grain * .52) * Math.min(1, -incidence * 1.6) * (.76 + music.level * .12 + music.pulse * .12);
        ctx.globalAlpha = alpha;
        ctx.beginPath();
        [[-1, -1], [1, -1], [1, 1], [-1, 1]].forEach(([a, b], corner) => {
          const qx = rx + spread * (a * ux + b * vx), qy = ry + spread * (a * uy + b * vy), qz = rz + spread * b * vz;
          const px = originX + depth * qx / -qz, py = originY - depth * qy / -qz;
          if (corner) ctx.lineTo(px, py);
          else ctx.moveTo(px, py);
        });
        ctx.closePath();
        ctx.fill();
        // A restrained second exposure around the brightest tiles adds bloom.
        if (alpha > .5) {
          ctx.globalAlpha = alpha * .09;
          const size = Math.min(38, depth * spread * 7 / -rz);
          ctx.drawImage(star, x - size / 2, y - size / 2, size, size);
        }
        const key = index + lampIndex * facets.length;
        if (glint?.key === key) Object.assign(glint, { x, y, visible: true });
        if (canGlint && lampIndex === 0 && alpha > .5 && now - (glintHistory.get(key) ?? -Infinity) > 2500 && (!candidate || alpha > candidate.alpha)) candidate = { key, x, y, alpha };
      });
    });
    if (candidate) {
      glint = { ...candidate, born: now, visible: true };
      glintHistory.set(candidate.key, now);
      lastGlint = now;
    }
    if (glint?.visible) {
      const age = now - glint.born;
      ctx.globalAlpha = .5 * (age < 70 ? age / 70 : Math.pow(1 - (age - 70) / 350, 2));
      ctx.drawImage(star, glint.x - 12, glint.y - 12, 24, 24);
    }
    ctx.globalAlpha = 1;
  }
  function frame(now) {
    if (now - lastPaint >= 1000 / 30) {
      const delta = Math.min((now - lastPaint) / 1000, .1);
      lastPaint = now;
      const music = window.HNVDiscoMusic?.sample();
      if (music?.playing) {
        tempo += (music.tempo - tempo) * (1 - Math.exp(-delta / 3));
        // One continuous revolution per 64 beats: a real motor has inertia.
        phase = (phase + delta * TAU * tempo / (60 * 64)) % TAU;
        aim();
        drawLights(now, music);
        balls.forEach(ball => ball.draw(phase, music.pulse));
      }
    }
    request = requestAnimationFrame(frame);
  }
  resizeLights();
  window.addEventListener("resize", resizeLights, { passive: true });
  // Names the song that is playing, so Ricky can say which ones stay. Doubles as the on-screen music credit.
  const nowPlaying = document.createElement("p");
  nowPlaying.className = "disco-now";
  nowPlaying.setAttribute("role", "status");
  document.body.append(nowPlaying);
  document.addEventListener("hnv-track", () => {
    const title = window.HNVDiscoMusic?.title;
    nowPlaying.textContent = title ? `♪ ${title} · Kevin MacLeod` : "";
    if (!window.HNVDiscoMusic?.playing && discoOn) {
      discoOn = false;
      syncAll();
    }
  });
  const balls = [...document.querySelectorAll(".disco-ball")].map(element => {
    const canvas = element.querySelector("canvas");
    const image = element.querySelector("img");
    let renderer = null, loading = false, unavailable = false;
    const ball = { element, visible: false, sync, draw(angle, pulse) { if (ball.visible) renderer?.draw(angle, pulse); } };
    async function sync() {
      const active = ball.visible && discoOn && !reduced.matches && !document.hidden;
      if (active && !renderer && !loading && !unavailable) {
        loading = true;
        try {
          await image.decode();
          renderer = createRenderer(canvas, image);
          if (!renderer) unavailable = true;
          else {
            element.classList.add("disco-ready");
          }
        } catch (error) {
          unavailable = true;
          console.warn("Disco motion unavailable; keeping the photograph.", error);
        }
        loading = false;
        sync();
        return;
      }
      const running = active && !!renderer;
      element.dataset.discoState = unavailable ? "unavailable" : running ? "running" : "paused";
    }
    canvas.addEventListener("webglcontextlost", () => {
      unavailable = true;
      renderer = null;
      element.classList.remove("disco-ready");
      element.dataset.discoState = "unavailable";
    });
    if ("ResizeObserver" in window) new ResizeObserver(() => renderer?.resize()).observe(element);
    return ball;
  });
  function syncAll() {
    const running = discoOn && !reduced.matches && !document.hidden;
    lightField.dataset.active = String(running);
    lightField.dataset.running = String(running);
    if (running && !request) {
      lastPaint = performance.now();
      request = requestAnimationFrame(frame);
    } else if (!running) {
      cancelAnimationFrame(request);
      request = 0;
    }
    for (const button of [sparkleToggle, roomToggle]) if (button) {
      button.dataset.motionPaused = String(!discoOn || document.hidden);
      button.dataset.discoSource = String(discoOn && button === source);
      button.setAttribute("aria-pressed", String(discoOn));
      button.setAttribute("aria-label", discoOn ? "Stop the disco: music, spinning and lights" : "Start the disco: music, spinning and lights");
    }
    if (toggle) {
      toggle.setAttribute("aria-pressed", String(discoOn));
      toggle.textContent = discoOn ? "Stop the disco ♪" : "Start the disco ♪";
    }
    balls.forEach(ball => ball.sync());
  }
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        const ball = balls.find(ball => ball.element === entry.target);
        ball.visible = entry.isIntersecting;
        ball.sync();
      });
    });
    balls.forEach(ball => observer.observe(ball.element));
  } else {
    balls.forEach(ball => { ball.visible = true; });
    syncAll();
  }
  function stopDisco() {
    discoOn = false;
    window.HNVDiscoMusic?.stop();
    syncAll();
  }
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) stopDisco();
    else syncAll();
  });
  window.addEventListener("pagehide", stopDisco);
  reduced.addEventListener("change", syncAll);
  function toggleDisco(from = sparkleToggle) {
    discoOn = !discoOn;
    if (discoOn) { source = from; window.HNVDiscoMusic?.start(); }
    else window.HNVDiscoMusic?.stop();
    syncAll();
  }
  sparkleToggle?.addEventListener("click", () => toggleDisco(sparkleToggle));
  roomToggle?.addEventListener("click", () => toggleDisco(roomToggle));
  toggle?.addEventListener("click", () => toggleDisco(sparkleToggle));

  // The room's loading ball uses the same mirrors, with its own silent motor.
  const roomWorking = document.querySelector("#room-working");
  const roomBall = roomWorking?.querySelector(".room-loading-ball");
  if (roomBall) {
    const canvas = roomBall.querySelector("canvas"), image = roomBall.querySelector("img");
    let renderer = null, pending = false, unavailable = false, animation = 0, lastPaint = 0;
    const active = () => !roomWorking.hidden && !document.hidden && !reduced.matches;
    function paint(now) {
      if (now - lastPaint >= 1000 / 30) { renderer.draw(now * TAU / 8000); lastPaint = now; }
      animation = requestAnimationFrame(paint);
    }
    async function syncRoomBall() {
      cancelAnimationFrame(animation); animation = 0;
      if (!active() || unavailable) return;
      if (!renderer) {
        if (pending) return;
        pending = true;
        try {
          await image.decode();
          renderer = createRenderer(canvas, image);
          if (renderer) roomBall.classList.add("disco-ready"); else unavailable = true;
        } catch { unavailable = true; }
        pending = false;
        syncRoomBall(); return;
      }
      renderer.resize();
      animation = requestAnimationFrame(paint);
    }
    canvas.addEventListener("webglcontextlost", () => {
      unavailable = true; cancelAnimationFrame(animation); roomBall.classList.remove("disco-ready");
    });
    document.addEventListener("hnv:room-working", syncRoomBall);
    document.addEventListener("visibilitychange", syncRoomBall);
    reduced.addEventListener("change", syncRoomBall);
    if ("ResizeObserver" in window) new ResizeObserver(() => { if (active()) renderer?.resize(); }).observe(roomBall);
    syncRoomBall();
  }
  syncAll();
})();
