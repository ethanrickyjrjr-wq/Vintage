// Real disco tracks by Kevin MacLeod (incompetech.com), CC BY 4.0; credited in the footer.
// Nothing loads or plays before a tap. Each start plays the next song; a finished song rolls into the next.
(() => {
  const tracks = [
    ["stringed-disco", "Stringed Disco"],
    ["your-call", "Your Call"],
    ["disco-con-tutti", "Disco con Tutti"],
    ["enter-the-party", "Enter the Party"],
  ];
  let audio = null, playing = false, title = "";
  let next = 0;
  try { next = Number(localStorage.getItem("hnv-track")) || 0; } catch {}

  const announce = () => document.dispatchEvent(new CustomEvent("hnv-track"));

  function play() {
    const [file, name] = tracks[next % tracks.length];
    next = (next + 1) % tracks.length;
    try { localStorage.setItem("hnv-track", next); } catch {}
    title = name;
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
      audio.addEventListener("ended", () => { if (playing) play(); });
      audio.addEventListener("error", () => stop());
    }
    playing = true;
    play();
  }

  function stop() {
    if (!playing) return;
    playing = false;
    title = "";
    audio.pause();
    announce();
  }

  window.HNVDiscoMusic = { start, stop, get playing() { return playing; }, get title() { return title; } };
})();
