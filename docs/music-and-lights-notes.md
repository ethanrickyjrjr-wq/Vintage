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

## Lights and sparkles: researched, not built

Why it reads wrong now: the 96 light patches are 7 to 17 px soft-glowed boxes moving in straight lanes, the 24 stars are plain clip-path polygons, and the ball highlight is broad rather than a tile flashing white.

Recommended build, about 110 lines of Canvas2D replacing the CSS patches:
1. Rotate about 4000 facet normals with the ball spin, reflect the beam (`r = d - 2(d.n)n`), hit the page plane (`t = h / -rz`), draw each as a small hard-edged additive parallelogram (`globalCompositeOperation = "lighter"`) inside the existing screen-blended `.disco-room-light` wrapper. Measured geometry: about 350 warm plus 145 pink spots on a phone viewport.
2. Ball: half-vector flash in the shader (about 10 lines GLSL), later at most 3 JS-chosen "hot tiles" plus a 4-point star sprite.
3. Stars: pre-rendered sprites with a round core and tapering spikes, 70 ms attack and 350 ms decay twinkle, 14 on phones and 24 on desktop.

Owner decisions before building: speed (16 s vs 24 to 30 s per turn), how streaky, whether to add a faint beam haze, still frame vs nothing for reduced motion. Safety rules to keep: at most 3 simultaneous glints, no repeat of one star faster than every 2.5 s, no full-viewport brightness steps. Run a flash-safety check on the final build.

`docs/storefront-art-direction.md` lines 17 to 18 are out of step with the code (it says 64 stars and eight light reflections; the code has 96 patches and 24 stars). Fix when the lights are rebuilt.

References: three MIT repos for technique (vikingmute/neo-disco, lowsweet/disco-ball, BonoboJP/threejs-paris-disco-ball); Shadertoy and several physics articles were walled. A runnable geometry check is `research/disco-visuals/projection-check.mjs`.
