// An original, browser-synthesized disco loop. No audio loads or plays before a tap.
(() => {
  let session = null;
  const stepLength = 60 / 114 / 4;
  const frequency = note => 440 * 2 ** ((note - 69) / 12);
  const progression = [
    { bass: 38, chord: [62, 65, 69, 72], melody: [81, 79, 77, 76] },
    { bass: 43, chord: [62, 65, 67, 70], melody: [79, 77, 74, 77] },
    { bass: 36, chord: [60, 64, 67, 71], melody: [79, 76, 74, 72] },
    { bass: 33, chord: [61, 64, 67, 69], melody: [76, 73, 71, 73] },
  ];

  function start() {
    if (session) return;
    const Audio = window.AudioContext || window.webkitAudioContext;
    if (!Audio) return;
    let context;
    try { context = new Audio(); } catch { return; }
    const master = context.createGain();
    const compressor = context.createDynamicsCompressor();
    master.gain.value = .48;
    compressor.threshold.value = -18;
    compressor.ratio.value = 4;
    master.connect(compressor).connect(context.destination);
    const noise = context.createBuffer(1, Math.ceil(context.sampleRate * .3), context.sampleRate);
    const samples = noise.getChannelData(0);
    for (let i = 0; i < samples.length; i++) samples[i] = Math.random() * 2 - 1;

    function tone(note, time, duration, volume, type = "sine", cutoff = 1800) {
      const oscillator = context.createOscillator();
      const filter = context.createBiquadFilter();
      const envelope = context.createGain();
      oscillator.type = type;
      oscillator.frequency.value = frequency(note);
      filter.type = "lowpass";
      filter.frequency.setValueAtTime(cutoff, time);
      filter.frequency.exponentialRampToValueAtTime(Math.max(200, cutoff * .35), time + duration);
      envelope.gain.setValueAtTime(0, time);
      envelope.gain.linearRampToValueAtTime(volume, time + .008);
      envelope.gain.exponentialRampToValueAtTime(.0001, time + duration);
      oscillator.connect(filter).connect(envelope).connect(master);
      oscillator.start(time);
      oscillator.stop(time + duration + .02);
      oscillator.onended = () => { oscillator.disconnect(); filter.disconnect(); envelope.disconnect(); };
    }

    function percussion(time, duration, volume, cutoff, highpass = true) {
      const source = context.createBufferSource();
      const filter = context.createBiquadFilter();
      const envelope = context.createGain();
      source.buffer = noise;
      filter.type = highpass ? "highpass" : "bandpass";
      filter.frequency.value = cutoff;
      envelope.gain.setValueAtTime(volume, time);
      envelope.gain.exponentialRampToValueAtTime(.0001, time + duration);
      source.connect(filter).connect(envelope).connect(master);
      source.start(time);
      source.stop(time + duration);
      source.onended = () => { source.disconnect(); filter.disconnect(); envelope.disconnect(); };
    }

    function kick(time) {
      const source = context.createOscillator();
      const envelope = context.createGain();
      source.frequency.setValueAtTime(125, time);
      source.frequency.exponentialRampToValueAtTime(45, time + .13);
      envelope.gain.setValueAtTime(.7, time);
      envelope.gain.exponentialRampToValueAtTime(.0001, time + .23);
      source.connect(envelope).connect(master);
      source.start(time);
      source.stop(time + .25);
      source.onended = () => { source.disconnect(); envelope.disconnect(); };
    }

    function playStep(step, time) {
      const beat = step % 16;
      const bar = Math.floor(step / 16) % progression.length;
      const part = progression[bar];
      if (beat % 4 === 0) kick(time);
      // Offbeat open hats, light sixteenth-note shakers, and a double clap.
      percussion(time, beat % 4 === 2 ? .16 : .035, beat % 2 === 0 ? .12 : .035, 7300);
      if (beat === 4 || beat === 12) {
        percussion(time, .105, .22, 1600, false);
        percussion(time + .018, .085, .14, 2100, false);
        tone(50, time, .07, .1, "triangle");
      }
      const bassPattern = [0, null, 12, null, 0, null, 7, 10, null, 0, 12, null, 7, null, 12, 7];
      if (bassPattern[beat] !== null) {
        tone(part.bass + bassPattern[beat], time, .16, .23, "sawtooth", 650);
        tone(part.bass + bassPattern[beat], time, .18, .16, "sine", 500);
      }
      if ([2, 6, 10, 14].includes(beat)) {
        part.chord.forEach(note => {
          tone(note, time, .3, .07, "triangle", 2400);
          tone(note + 12, time, .12, .016, "sine", 4000);
        });
      }
      // A small answering melody keeps the four-bar groove from feeling like a metronome.
      if ([3, 7, 11, 14].includes(beat)) {
        const note = part.melody[[3, 7, 11, 14].indexOf(beat)];
        tone(note, time, .32, .055, "sine", 3500);
        tone(note, time + .18, .24, .018, "sine", 2500);
      }
    }

    const current = { context, master, timer: 0, step: 0, next: context.currentTime + .04 };
    session = current;
    function schedule() {
      if (session !== current || context.state !== "running") return;
      if (current.next < context.currentTime) current.next = context.currentTime + .02;
      while (current.next < context.currentTime + .12) {
        playStep(current.step++, current.next);
        current.next += stepLength;
      }
    }
    // resume() is called directly inside the click gesture for mobile browsers.
    context.resume().then(schedule).catch(() => {
      if (session === current) stop();
    });
    current.timer = window.setInterval(schedule, 25);
  }

  function stop() {
    if (!session) return;
    const { context, master, timer } = session;
    session = null;
    clearInterval(timer);
    master.gain.cancelScheduledValues(context.currentTime);
    master.gain.setTargetAtTime(0, context.currentTime, .008);
    window.setTimeout(() => context.close().catch(() => {}), 40);
  }

  window.HNVDiscoMusic = { start, stop, get playing() { return session?.context.state === "running"; } };
})();
