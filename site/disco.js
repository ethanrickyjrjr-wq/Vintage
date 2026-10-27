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
      // Broad warm illumination, and small specular catches confined to tiles.
      float warm = pow(max(dot(facet, normalize(vec3(-0.42, 0.5, 0.9))), 0.0), 90.0);
      float pink = pow(max(dot(facet, normalize(vec3(0.86, 0.2, 0.5))), 0.0), 50.0);
      silver += vec3(1.0, 0.91, 0.74) * warm * 0.55;
      silver += vec3(0.9, 0.37, 0.48) * pink * 0.26;
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

  function createRenderer(canvas, image, seconds) {
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
    let angle = 0, request = 0, lastPaint = 0;
    function draw() {
      gl.uniform1f(angleUniform, angle);
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
    function frame(now) {
      if (now - lastPaint >= 1000 / 30) {
        angle = (angle + Math.min(now-lastPaint, 100) / (seconds*1000) * Math.PI*2) % (Math.PI*2);
        lastPaint = now;
        draw();
      }
      request = requestAnimationFrame(frame);
    }
    resize();
    return {
      resize,
      start() { if (!request) { lastPaint = performance.now(); request = requestAnimationFrame(frame); } },
      stop() { cancelAnimationFrame(request); request = 0; },
    };
  }

  const reduced = matchMedia("(prefers-reduced-motion: reduce)");
  const toggle = document.querySelector(".disco-motion-toggle");
  const sparkleToggle = document.querySelector(".salon-disco");
  let discoOn = false;
  // Projected light is a page layer, so it also reaches the collection while
  // the ball is outside the viewport. CSS animates only transforms and opacity.
  const lightField = document.createElement("div");
  lightField.className = "disco-room-light";
  lightField.setAttribute("aria-hidden", "true");
  // Mirror facets project curved rows of light that travel together as the ball turns.
  for (let i = 0; i < 96; i++) {
    const row = Math.floor(i / 12), column = i % 12;
    const patch = document.createElement("span");
    patch.className = "disco-light-patch";
    patch.style.setProperty("--light-y", `${5 + row * 12.5}%`);
    patch.style.setProperty("--light-size", `${7 + (i * 7 % 11)}px`);
    patch.style.setProperty("--light-delay", `${-column * 2 - row * .28}s`);
    patch.style.setProperty("--glint-delay", `${-i * .37}s`);
    lightField.append(patch);
  }
  document.body.append(lightField);
  const balls = [...document.querySelectorAll(".disco-ball")].map((element, index) => {
    const canvas = element.querySelector("canvas");
    const image = element.querySelector("img");
    let renderer = null, loading = false, unavailable = false;
    const ball = { element, visible: false, sync };
    async function sync() {
      const active = ball.visible && discoOn && !reduced.matches && !document.hidden;
      if (active && !renderer && !loading && !unavailable) {
        loading = true;
        try {
          await image.decode();
          renderer = createRenderer(canvas, image, index ? 20 : 16);
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
      if (running) renderer.start();
      else renderer?.stop();
    }
    canvas.addEventListener("webglcontextlost", () => {
      unavailable = true;
      renderer?.stop();
      renderer = null;
      element.classList.remove("disco-ready");
      element.dataset.discoState = "unavailable";
    });
    if ("ResizeObserver" in window) new ResizeObserver(() => renderer?.resize()).observe(element);
    return ball;
  });
  function syncAll() {
    lightField.dataset.active = String(discoOn && !document.hidden);
    lightField.dataset.running = String(discoOn && !reduced.matches && !document.hidden);
    if (sparkleToggle) {
      sparkleToggle.dataset.motionPaused = String(!discoOn || document.hidden);
      sparkleToggle.setAttribute("aria-pressed", String(discoOn));
      sparkleToggle.setAttribute("aria-label", discoOn ? "Stop the disco: music, spinning and lights" : "Start the disco: music, spinning and lights");
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
  function toggleDisco() {
    discoOn = !discoOn;
    if (discoOn) window.HNVDiscoMusic?.start();
    else window.HNVDiscoMusic?.stop();
    syncAll();
  }
  sparkleToggle?.addEventListener("click", toggleDisco);
  toggle?.addEventListener("click", toggleDisco);
  syncAll();
})();
