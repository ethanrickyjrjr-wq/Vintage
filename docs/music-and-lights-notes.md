# Music and disco-light notes (2026-10-26)

Three Sonnet agents researched this with crawl4ai; raw fetched pages are in `research/music-sources/`, `research/music-synth/`, `research/disco-visuals/`. Two agents could not write their own report files, so this is the distilled version. Nothing here was listened to or run on a phone.

## Music: what shipped

Four Kevin MacLeod (incompetech.com) tracks, **CC BY 4.0**, in `site/assets/music/` (re-encoded to 96 kbps, loudness-matched, 2.3 to 2.8 MB each, about 10 MB total): Stringed Disco, Your Call, Disco con Tutti, Enter the Party. Each tap on the ball plays the next one; the title shows in a "now playing" pill; credit text is in the footer (wording from his FAQ). Ricky listens, then says which to cut.

Licence basis: incompetech FAQ and the CC BY 4.0 deed, fetched live. The condition is a visible credit; a credits link is fine per his FAQ. His per-track pages are JS-only, so the licence is the site-wide one.

## Music: other sources, if these four disappoint

| Source | Verdict |
|---|---|
| Incompetech, more tracks | Same licence. Also in range: Funky Chunk (115 BPM), Ether Disco (120), Overcast (120). Disco Medusae and Aurea Carmina fade to silence, so they would need a crossfade. |
| ccMixter CC BY | World Of Sports (120 BPM, 3:37), COME (120, 3:29, has vocals). Credit remixer and sampled source. Thin catalog. |
| Jamendo Licensing, paid, about 29 EUR per track | Only licence text that names background music on a commercial website. Its catalog could not be fetched. |
| Pixabay | Licence bars "standalone" distribution, gray for a public mp3. Most disco tracks carry an "AI generated" badge. |
| Freesound CC0 | Needs a login. Loops, not full songs. |
| Free Music Archive | Disco tracks mostly non-commercial. |
| Bensound free, Uppbeat free, Suno free, ElevenLabs free | Not usable for a commercial site. |
| Unverified | Mixkit, Epidemic Sound, Artlist, Udio. |

## Music: better synth (not used; the owner chose real songs)

If it is ever wanted back: kick ducking (3 lines), synthesized-impulse reverb (about 15), detuned-saw string pad with ensemble delay (about 20), a 32-bar arrangement with a longer chord progression (about 14), stereo buses. About 90 lines, no audio files. No library (Tone.js is 79 KB gzip). The old synth is in git history (`site/disco-music.js` before this change). No cleanly licensed 808 or 909 drum kit was found; CC0 options are VCSL (percussion) and VSCO-2-CE (violin section), both on GitHub.

## Lights and sparkles: implemented 2026-10-27

The owner requested the most realistic treatment and speed that follows the music. `site/disco.js` now projects two fixed pinspots from the same 28-row mirror grid as the rotating sphere, using reflected rays and a wall-plane intersection. Small sharp quadrilaterals stretch at grazing angles, with modest bloom and rare attached diffraction glints. A narrow half-vector specular highlight catches individual tiles on the ball; the artificial hanging sway and CSS patch lanes are removed.

The composer's catalog captured in `research/music-sources/inc-pieces.md` lists Stringed Disco at 118 BPM, Your Call at 120, Disco con Tutti at 115, and Enter the Party at 120. One shared motor clock makes a revolution every 64 beats (about 32 to 33 seconds), smoothing speed changes over three seconds. The published tempos avoid a syncopated bass line confusing a live tempo estimate. Web Audio still measures the actual playing track: bass attacks add small brightness accents and trigger occasional glints. No microphone or additional audio download is used. Reduced motion suppresses the moving light layer and sphere rendering while music remains available.

Validation scripts in ignored `artifacts/` check bass responses against the first 40 seconds of all four committed MP3s, synthetic beats at 100/120/140 BPM, silence, missing Web Audio, pause and song switching. Production projection code is exercised for a minute at 1440×900, 390×844 and 320×740: finite reflected geometry, less than 0.3% maximum alpha-weighted illuminated viewport area, small frame-to-frame changes, and animation suspension for pause, reduced motion and hidden pages. These are implementation checks, not a formal photometric flash certification.

### Original research

Why it reads wrong now: the 96 light patches are 7 to 17 px soft-glowed boxes moving in straight lanes, the 24 stars are plain clip-path polygons, and the ball highlight is broad rather than a tile flashing white.

Recommended build, about 110 lines of Canvas2D replacing the CSS patches:
1. Rotate about 4000 facet normals with the ball spin, reflect the beam (`r = d - 2(d.n)n`), hit the page plane (`t = h / -rz`), draw each as a small hard-edged additive parallelogram (`globalCompositeOperation = "lighter"`) inside the existing screen-blended `.disco-room-light` wrapper. Measured geometry: about 350 warm plus 145 pink spots on a phone viewport.
2. Ball: half-vector flash in the shader (about 10 lines GLSL), later at most 3 JS-chosen "hot tiles" plus a 4-point star sprite.
3. Stars: pre-rendered sprites with a round core and tapering spikes, 70 ms attack and 350 ms decay twinkle, 14 on phones and 24 on desktop.

The implementation resolves the earlier choices with a tempo-based motor, physically projected streaks, no artificial smoke beam, and no moving lights for reduced motion. Glints are limited more conservatively to a single 420 ms catch and at least 950 ms between starts; the same facet cannot repeat within 2.5 seconds. No full-viewport brightness steps are introduced.

`docs/storefront-art-direction.md` and `site/README.md` now describe the implemented light and music behavior.

References: three MIT repos for technique (vikingmute/neo-disco, lowsweet/disco-ball, BonoboJP/threejs-paris-disco-ball); Shadertoy and several physics articles were walled. A runnable geometry check is `research/disco-visuals/projection-check.mjs`.
