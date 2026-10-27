// Real disco tracks by Kevin MacLeod (incompetech.com), CC BY 4.0; credited in the footer.
// Nothing loads or plays before a tap. Each start plays the next song; a finished song rolls into the next.
(() => {
  const tracks = [
    // Tempos from the composer's catalog, retained in research/music-sources/inc-pieces.md.
    ["stringed-disco", "Stringed Disco", 118],
    ["your-call", "Your Call", 120],
    ["disco-con-tutti", "Disco con Tutti", 115],
    ["enter-the-party", "Enter the Party", 120],
  ];
  let audio = null, playing = false, title = "", context = null, analyser = null;
  let spectrum, waveform, lastPosition = 0, lastBeat = -1, bassMean = 0, previousBass = 0, fluxMean = 0;
  const motion = { playing: false, position: 0, tempo: 120, level: 0, pulse: 0 };
  let next = 0;
  try { next = Number(localStorage.getItem("hnv-track")) || 0; } catch {}

  const announce = () => document.dispatchEvent(new CustomEvent("hnv-track"));

  function resetMotion(tempo = 120) {
    lastPosition = bassMean = previousBass = fluxMean = 0;
    lastBeat = -1;
    Object.assign(motion, { playing: false, position: 0, tempo, level: 0, pulse: 0 });
  }

  function connectAnalysis() {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext || context) return;
    try {
      context = new AudioContext();
      analyser = context.createAnalyser();
      analyser.fftSize = 2048;
      analyser.smoothingTimeConstant = .15;
      spectrum = new Uint8Array(analyser.frequencyBinCount);
      waveform = new Float32Array(analyser.fftSize);
      context.createMediaElementSource(audio).connect(analyser);
      analyser.connect(context.destination);
    } catch (error) {
      analyser = null;
      console.warn("Music analysis unavailable; using a steady mirror-ball speed.", error);
    }
  }

  // Read the playing audio, not a timer: bass attacks light the facets. The
  // motor follows the published tempo, so syncopated bass cannot change it.
  function sample() {
    motion.playing = !!(playing && !audio.paused && !audio.ended && audio.readyState >= 2);
    if (!motion.playing) {
      motion.level = motion.pulse = 0;
      return motion;
    }
    const position = audio.currentTime;
    const delta = Math.max(0, Math.min(.1, position - lastPosition));
    lastPosition = motion.position = position;
    motion.pulse *= Math.exp(-delta / .18);
    if (!analyser || context.state !== "running") return motion;
    analyser.getByteFrequencyData(spectrum);
    analyser.getFloatTimeDomainData(waveform);
    const binHz = context.sampleRate / analyser.fftSize;
    const first = Math.max(1, Math.floor(40 / binHz));
    const last = Math.min(spectrum.length - 1, Math.ceil(180 / binHz));
    let bass = 0, power = 0;
    for (let i = first; i <= last; i++) bass += spectrum[i] / 255;
    bass /= last - first + 1;
    for (let i = 0; i < waveform.length; i++) power += waveform[i] * waveform[i];
    motion.level += (Math.min(1, Math.sqrt(power / waveform.length) * 3) - motion.level) * (1 - Math.exp(-delta / .12));
    const flux = Math.max(0, bass - previousBass);
    previousBass = bass;
    bassMean += (bass - bassMean) * (1 - Math.exp(-delta / .8));
    fluxMean += (flux - fluxMean) * (1 - Math.exp(-delta / .7));
    if (position - lastBeat > .29 && bass > bassMean + .025 && flux > Math.max(.012, fluxMean * 1.8)) {
      lastBeat = position;
      motion.pulse = Math.min(1, .45 + flux * 5);
    }
    return motion;
  }

  function play() {
    const [file, name, tempo] = tracks[next % tracks.length];
    next = (next + 1) % tracks.length;
    try { localStorage.setItem("hnv-track", next); } catch {}
    title = name;
    resetMotion(tempo);
    audio.src = `assets/music/${file}.mp3`;
    // A quick off/on aborts the earlier play(); only a real failure should stop the music.
    audio.play().catch(error => { if (error.name !== "AbortError") stop(); });
    announce();
  }

  // The element is created inside the tap so phones allow later src swaps without another gesture.
  function start() {
    if (playing) return;
    if (!audio) {
      audio = new Audio();
      audio.preload = "none";
      audio.volume = .8;
      audio.className = "disco-audio";
      audio.hidden = true;
      document.body.append(audio);
      audio.addEventListener("ended", () => { if (playing) play(); });
      audio.addEventListener("error", () => stop());
    }
    connectAnalysis();
    context?.resume().catch(() => {});
    playing = true;
    play();
  }

  function stop() {
    if (!playing) return;
    playing = false;
    title = "";
    audio.pause();
    context?.suspend().catch(() => {});
    resetMotion();
    announce();
  }

  window.HNVDiscoMusic = { start, stop, sample, get playing() { return playing; }, get title() { return title; } };
})();
