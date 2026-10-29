# w2a-editing: stage `edit` (trim, speed, text hook, music bed, end card, upload-ready export)

Lane w2a, accessed 2026-10-29. Tags as in BRIEF.md: `verified` (read live or measured this session), `vendor claim`, `practitioner`, `inferred`, `unverified (search)`, "not read". Raw: `raw/w2a-*` (crawls) plus the tested artifacts `raw/w2a-render.py` (103 lines), `raw/w2a-edl-test1.json`, `raw/w2a-edl-test2.json`, `raw/w2a-cmd-test1.txt` (the exact emitted ffmpeg command). Reference load: 16 reels a month, about 15 s each = **4 min of output**, about **8-12 min of raw footage** (`inferred` from w1h's 34 clips per 90-minute shoot). Render APIs bill output minutes; Opus/Vizard bill input minutes.

## TL;DR

- **The Fedora ffmpeg blocker is solved with a user-local static build, no sudo.** BtbN's `linux64-gpl-8.1` build (linked from ffmpeg.org/download.html) decodes H.264 High 4K30 at 3.0-3.7x realtime and HEVC Main10 4K30 at 1.4-1.9x realtime on the box. `verified` (measured).
- **Why the stock build fails:** Fedora's ffmpeg 8.0.1 is configured `--disable-decoder='h264,hevc,vc1,vvc'`; only the `libopenh264` stub remains, and it errored even on the shop walkthrough's Baseline-profile copy. `verified`.
- **A JSON edit list compiles to one ffmpeg command.** A 103-line stdlib Python script took a 3-clip EDL (one clip HDR HLG, one 2x speed) to a 1080x1920, 30 fps, H.264 High, AAC 48 kHz reel with a 3-line Bodoni Moda hook, music bed and end card in 20-31 s wall at CRF 18 (6 s at `veryfast`). `verified`, synthetic input.
- **Output is clean for our code path:** an ffprobe/byte-scan check passes (no GPS, no `com.apple.*`, no C2PA/JUMBF/XMP/DigitalSourceType strings, no side data); a control scan of the raw input finds the GPS and Apple tags. `verified`. Edits, CapCut, Descript and Submagic exports are **not tested** (`gap`).
- **HDR:** `tonemap=hable` darkened a synthetic round trip by 25 luma levels (YAVG 66.6 vs 91.5); `mobius` gave 91.2. Real iPhone HDR is uncalibrated, so keep **HDR Video off** at capture (w1h). `verified` (synthetic).
- **Captions:** faster-whisper `small` int8 took 3.1 s for 8.2 s of speech with word timestamps; burning ASS captions took 5.9 s. The real walkthrough has **no speech** (VAD: 0 segments), so silent clips get hook text only. `verified`.
- **Remotion runs on the box** (install 22 s, headless Chrome shell 99 MB, 3 s render in 36 s) and is free for companies of up to 3 people. `verified`. Use it only for animated typography beyond `drawtext`.
- **Render APIs and AI editors do not beat this at 4 min a month.** Cheapest: Shotstack $10 for 50 min, JSON2Video $49.95 for 120 min (no expiry) (`verified`, vendor pages). The AI editors are speech-first and several sell AI B-roll, avatars or generated images, which the real-items-only rule bans (`vendor claim`).
- **Loudness:** -14 LUFS / -1 dBTP is the most-cited figure; no Meta page gives one (`practitioner`). Two-pass `loudnorm` measured -14.0 LUFS / -1.5 dBTP on a real MacLeod track (`verified`).
- **Recommendation (`inferred`):** the ffmpeg EDL path, tested on Fedora and equally runnable on Windows (w2g picks where); Edits in the phone for month one; Remotion later if wanted.

## 1. The Fedora ffmpeg test (answer for w2g)

| Item | Result |
|---|---|
| Stock `/usr/bin/ffmpeg` | 8.0.1, `--disable-decoder='h264,hevc,vc1,vvc'`, `--disable-encoders` with an allow-list that omits `libx264`/`libx265`. Decoders listed: `libopenh264` only. `verified` |
| Stock errors (verbatim) | H.264 High 4K: `[libopenh264] Unable to create decoder` / `Error while opening decoder` (exit 171). HEVC: `Decoding requested, but no decoder found for: hevc` (exit 234). The Baseline 568x320 walkthrough copy: same `Unable to create decoder` (exit 171) |
| Build source | ffmpeg.org/download.html "Linux Static Builds" points to https://github.com/BtbN/FFmpeg-Builds/releases (page read 2026-10-29; ffmpeg.org lists 9.0.2 as latest stable, released 2026-09-18). johnvansickle.com/ffmpeg as crawled shows "git master built 20240629, release 7.0.2" (stale or cached; not used). BtbN repo: MIT, 11,892 stars, pushed 2026-10-28, not archived |
| Tested build | `ffmpeg-n8.1-latest-linux64-gpl-8.1.tar.xz`, 152,134,292 bytes (matches the GitHub API size), sha256 `201779aed04c3d2b9c9f1362202ad63d3a3e9a16af033f21bdadd6a6c3f0fb23`; downloaded in 16 s, extracted in 1.6 s. Version `n8.1.3-25-g611cec792a-20261028`, gcc 16.2.0; `ffmpeg` 173,067,720 bytes (sha256 `8b779df6...eb02`), `ffprobe` 172,834,184 bytes |
| **Pin to this (reproducible)** | https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2026-10-28-19-47/ffmpeg-n8.1.3-25-g611cec792a-linux64-gpl-8.1.tar.xz , sha256 `8d02a412b0f72051bf30201a9f2c117fe557a4dc44b03c5c99fda2fbd7b00b5d` (152,135,596 bytes). I downloaded it too: its `ffmpeg` and `ffprobe` are **byte-identical** to the tested ones. The rolling `latest` tag is rewritten daily, so never script against it |
| Install | `curl -L -o f.tar.xz <pin URL>; sha256sum f.tar.xz; tar -xJf f.tar.xz --strip-components=1 --wildcards '*/bin/ffmpeg' '*/bin/ffprobe'` then run `./bin/ffmpeg`. No sudo, no PATH change |
| Qualified | native `h264`, `hevc`, `aac` decoders; `libx264`, `libx265`, `aac` encoders; filters `drawtext` (freetype, harfbuzz, fribidi), `subtitles`/`ass` (libass), `zscale`, `tonemap` (zimg), `loudnorm`, `ebur128`, `xfade`, `vidstabdetect`. **Missing:** fontconfig (use `fontfile=` and `fontsdir=`), the ffmpeg 8 `whisper` filter (the Windows gyan 8.1.2 build has `--enable-whisper`; this one does not). "Static" means libs are static; it still links `libm.so.6` from the system glibc. GPL-3 build, used internally, not redistributed |
| Alternatives not run | podman image; pip-packaged static ffmpeg; rpmfusion (needs root, so out). Not needed now |

**Decode timing on the box** (i7-8565U, 8 threads, `ffmpeg -benchmark -f null`, includes the 90-degree autorotate; box load average 0.4 to 3 from other lanes and services, 7.7 during the final encodes). Clips are synthetic, built on Windows from the 24 s walkthrough upscaled to 3840x2160 with noise added at phone-like bitrates, stored landscape with a -90 display matrix, a stereo plus a 4-channel AAC stream and a fake `com.apple.quicktime.location.ISO6709` tag (ffprobe confirmed all present before copying).

| Clip (10 s) | Wall | Realtime factor | User CPU | maxrss |
|---|---|---|---|---|
| H.264 High 4K30, 23.7 Mbps | 2.7-3.3 s | 3.0-3.7x (about 98 fps) | 17.3-19.7 s | 379 MB |
| same, `-threads 1` | 8.8 s | 1.1x | 13.5 s | 165 MB |
| HEVC Main10 HLG 4K30, 18 Mbps | 5.3-7.1 s | 1.4-1.9x | 42.8 s | 730-750 MB |
| Real walkthrough, 24 s, Baseline 568x320 | 0.21 s | 131x | n/a | n/a |

The shop phone's real 1080p30 bitrate is **not measured**; 4K numbers are the worst case.

## 2. End-to-end edit test (JSON EDL to upload-ready reel)

**EDL** (`raw/w2a-edl-test1.json`; the compiler is `raw/w2a-render.py`, stdlib Python, optional fontTools for a text-width lint). Claude writes this; the script does everything else:

```json
{"id":"test-lamp-reel-01","output":"../out/test1.mp4",
 "fonts":{"bodoni":"../fonts/BodoniModa-700-opsz14.ttf","dm":"../fonts/DMSans-500-opsz14.ttf"},
 "clips":[{"src":"A.mov","in":0.5,"out":4.5,"speed":1.0,"fit":"cover"},
          {"src":"B.mov","in":2.0,"out":6.0,"speed":2.0,"fit":"cover"},
          {"src":"Walkthrough_real.mov","in":3.0,"out":6.0,"speed":1.0,"fit":"cover"}],
 "hook":{"lines":["Why does","this lamp click","three times?"],"size":112,"y":520,"t1":3.0},
 "end_card":{"dur":1.5,"lines":["Holliewood","& Vine"],"size":150,"sub":"Link in bio",
             "credit":["Music: Kevin MacLeod (incompetech.com)","CC BY 4.0"]},
 "music":{"src":"tone:220","fade_in":0.5,"fade_out":1.5,"lufs":-14,"tp":-1.5}}
```

**Emitted command** (condensed; the verbatim 3.7 KB line is in `raw/w2a-cmd-test1.txt`; run from the clips folder):

```
ffmpeg -y -nostdin -ss 0.5 -t 4.0 -i A.mov -ss 2.0 -t 4.0 -i B.mov -ss 3.0 -t 3.0 -i Walkthrough_real.mov -f lavfi -i sine=frequency=220:sample_rate=48000 \
 -filter_complex '[0:v:0]scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,format=yuv420p,setsar=1,setpts=(PTS-STARTPTS)/1.0,fps=30[v0];
  [1:v:0]<scale+crop>,zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,setsar=1,setpts=(PTS-STARTPTS)/2.0,fps=30[v1]; [2:v:0]...[v2];
  color=c=0x451c2b:s=1080x1920:r=30:d=1.5,format=yuv420p,drawtext=fontfile=...:textfile=...(x5)[ve];  [v0][v1][v2][ve]concat=n=4:v=1:a=0[vc];
  [vc]drawtext=fontfile=../fonts/BodoniModa-700-opsz14.ttf:textfile=t1.txt:fontsize=112:fontcolor=0xf6efdf:x=(w-text_w)/2:y=520:box=1:boxcolor=0x321520@0.55:boxborderw=20:enable='between(t,0,3.0)'(x3 lines),sidedata=mode=delete,setparams=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv[v];
  [3:a]atrim=0:10.500,asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:st=0:d=0.5,afade=t=out:st=9.000:d=1.5,volume=0dB,loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=-22.59:measured_TP=-21.07:measured_LRA=1.70:measured_thresh=-32.78:offset=0.09:linear=true,aresample=48000[a]' \
 -map '[v]' -map '[a]' -t 10.500 -c:v libx264 -preset medium -crf 18 -profile:v high -level 4.1 -pix_fmt yuv420p -maxrate 12M -bufsize 24M -r 30 -c:a aac -b:a 192k -ar 48000 -ac 2 \
 -map_metadata -1 -map_chapters -1 -bsf:v filter_units=remove_types=6 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact -movflags +faststart ../out/test1.mp4
```

Design points: input-side `-ss/-t` trims; per-clip `setpts` then one `fps=30` (phone video is VFR); `scale` before tone-map so float math runs at 1080p; only the music stream is mapped (both iPhone audio streams dropped); text goes through `textfile=` so LLM text cannot break filter syntax; a lint rejects lines wider than 950 px; two-pass linear `loudnorm` keeps fade shapes.

**Results** (`raw/w2a-render.py` check step; every line PASS on both EDLs):

| Check | Result |
|---|---|
| Runtime | Whole script 20-31 s wall for the 10.5 s reel (two-pass loudnorm, 3 probes, encode, check). Encode command alone: **25.1 s wall**, 702% CPU, 175 s user, **maxrss 1.80 GB**, at box load 7.7; 11,758,092 bytes (9.0 Mbps, inflated by synthetic noise). EDL 2 (real MacLeod MP3, `pad` fit, 0.5x speed, `veryfast` CRF 20, 11.5 s): **6.2 s wall**, 6.4 MB |
| Format | 1080x1920, no rotation, r_frame_rate and avg_frame_rate 30/1, yuv420p, bt709 space/transfer/primaries tagged, h264 High, aac LC 48 kHz stereo, exactly 2 streams, duration within 0.15 s, `moov` before `mdat` (faststart) |
| Loudness (ebur128 on the output) | tone: -13.7 LUFS, -12.5 dBTP (a sine's crest factor). **Real Stringed Disco MP3: -14.0 LUFS, -1.5 dBTP** |
| Metadata | Format tags only the three ftyp brands; stream tags `language=und`, `handler_name`, and `encoder=Lavc libx264` (benign). Byte scan finds none of: `c2pa`, `jumb`, `contentauth`, `DigitalSourceType`, `trainedAlgorithmicMedia`, `<x:xmpmeta`, `ISO6709`, `Apple`, `iPhone`, `com.apple`, `Lavf`, `x264 - core`. **Control:** the raw input still carries `ISO6709` and the Apple make/model tags, so the scan works |
| Two bugs found and fixed | (1) libx264 writes a "x264 - core" SEI string even with `+bitexact` and `-x264-params no-info` is rejected; `-bsf:v filter_units=remove_types=6` removes it. (2) A real iPhone first clip leaked an "Ambient viewing environment" side-data block into the output; `sidedata=mode=delete` removes it |
| Frames read by eye | Legibility and placement only: the hook is legible on busy footage inside the safe zone (y 520-905); end-card and credit lines legible at 34 px. Brightness was measured, not judged by eye: the tone-mapped HLG clip reads YAVG 90.9 against 92.1 for the SDR clip of the same source moment (after switching `hable` to `mobius`) |

**Privacy finding (bigger than C2PA):** iPhone files carry GPS (`com.apple.quicktime.location.ISO6709`) and device tags. `-map_metadata -1` removes them; any other editor's export should be ffprobed for them before posting. In-phone editors may or may not strip them: not tested.

**C2PA/AI-label scope.** Meta's labeling post (about.fb.com, dated Feb 6, 2024, page also shows Apr 1, 2025; read with crawl4ai, `raw/w2a-meta-labeling-post.md`) says it is building detection for "AI generated" information in C2PA and IPTC for images, and: "they haven't started including them in AI tools that generate audio and video at the same scale, so we can't yet detect those signals and label this content from other companies", asking people to disclose photorealistic AI video. `verified` as of that page's dates. Metadata-removal vendors claim real photos edited with generative tools get "AI info" (`unverified (search)`, commercially biased); no source says CapCut exports embed C2PA. Our ffmpeg and Remotion paths write none (Remotion adds `comment=Made with Remotion 4.0.539`, `verified`). For any SaaS or phone editor: export one reel, run `ffprobe -show_format -show_streams` plus the byte scan (`BAD` list in `raw/w2a-render.py`), and post one test before committing.

**HDR round trip (synthetic).** SDR source forward-converted to HLG Main10, then back through `zscale`+`tonemap`; mean luma (YAVG) vs the SDR reference 91.5: raw HLG 66.4, `hable` 66.6, `reinhard` 89.2, `clip` 91.8, **`mobius` 91.2**. The compiler detects `arib-std-b67` or `smpte2084` with ffprobe and applies `mobius`. Real iPhone Dolby Vision/HLG is not tested.

**Captions for clips with speech.** Windows SAPI synthetic voice, 8.2 s, 24 words, faster-whisper `small` int8 CPU with VAD and word timestamps (clipfeed venv, faster-whisper 1.2.1): **3.1 s**, exact transcript ("nineteen fifties" returned as "1950s"). Three words per line into ASS, burned with `ass=...:fontsdir=fonts`: **5.9 s** wall at `veryfast`. Gotcha: the ASS `Fontname` must match the instanced font's family (`DM Sans 9pt`). Noisy-room speech over music is **not tested**.

**Remotion on the box.** Node v26.9.0 is present. `npm install` of remotion 4.0.539 plus cli, bundler, renderer and React 19: 22 s, 254 packages, 262 MB. `npx remotion browser ensure` fetched the 98.9 MB headless Chrome shell in 12.8 s (no sudo, no missing libraries). A 90-frame 1080x1920 render of the 4K H.264 clip with a Bodoni Moda CSS hook: **35.8 s wall** including bundling (load 3.2), 4.6 MB, H.264 High; its bundled compositor decoded the phone-format clip, so it needs no separate ffmpeg. About 12 s per output second against ffmpeg's 2-3 s: motion design, not bulk trims. Memory not measured.

## 3. Options for the edit stage

Prices read 2026-10-29 from the vendor page unless marked. "Billing" matters: annual-billed prices are shown as the page shows them.

### 3a. Code-driven

| Option | Stage | Cost at 16 reels | Runs where | Drivable | Wins when |
|---|---|---|---|---|---|
| **ffmpeg + EDL script** (tested) | edit, caption | $0 | Fedora (static build), Windows (gyan 8.1.2, existing) | Yes (CLI, JSON) | Default: silent hands footage, exact brand type, no invented pixels. No stabilise, crossfade or ramps yet (section 5) |
| Remotion 4.0.539 | edit, caption (animated) | $0 for individuals and companies of up to 3 people ("Free License": all features, unlimited commercial use); 4+ people: $25/month per seat ("Creators") or $0.01 per render, $100/month minimum ("Automators"); https://www.remotion.pro/ (`verified`) | Fedora (tested), Windows | Yes (CLI, React) | Word-by-word animated captions, reusable brand motion. 68,848 stars, pushed 2026-10-29, license field NOASSERTION (custom license) |
| auto-editor | edit | $0 | CPU | Yes (CLI) | Silence and dead-motion cuts on talking footage; little value for silent clips. Unlicense, 5,658 stars, pushed 2026-10-28 |
| MoviePy 2.x | edit | $0 | CPU | Yes (Python) | You prefer Python to filter strings; wraps ffmpeg and gains nothing here. MIT, 15,054 stars, pushed 2026-08-26 |
| Editly | edit | $0 | CPU | Yes (JSON spec) | Closest existing "JSON to video"; MIT, 5,572 stars, last push 2025-05-12 (stale), not run |
| Revideo | edit | $0 | CPU + browser | Yes (TS) | Code-defined motion graphics, overlaps Remotion; MIT, 4,156 stars, pushed 2026-07-15, not run |

### 3b. Render APIs (hosted; raw footage must be uploaded to a URL they can fetch)

| Option | Price (page) | Free tier | At 4 min output a month | JSON template control | Notes |
|---|---|---|---|---|---|
| Shotstack | Pay as you go $10 for 50 min (20 cents a minute, minutes last 12 months); Starter $39/month for 250 min; Pro $99 for 750 | 10 credits on signup, valid 30 days; "free sandbox" (watermark not read) | about $0.80 a month effective on PAYG | Yes, timeline JSON; Make/Zapier/n8n | Includes AI generation (ban). https://shotstack.io/pricing/ |
| JSON2Video | Pre-paid $49.95 for 7,200 credits = 120 min (credits do not expire); $99.95 for 260 min; yearly sub $199.50 ($16.63 a month) for 50 min a month | 600 credits, no card; "watermark removal" is listed under paid plans (so free is probably watermarked, `vendor claim`) | about $1.67 a month amortised (240 credits a month) | Yes, scene JSON | 1 credit = 1 s. https://json2video.com/pricing/ |
| Creatomate | Essential $45/month billed annually ($540); Growth $109 billed annually; monthly price not read | 50-credit trial, no card | $45/month (2,000 credits, far more than needed) | Yes, templates + API | 1 min at 720p about 14 credits; renders hosted 30 days. https://creatomate.com/pricing |
| Plainly | Starter $48/month billed yearly ($579), $69 monthly; 50 min/month | 14-day trial | $48-69/month | After Effects templates | Wrong tool: needs AE |
| Cloudinary | Free 25 credits a month; Plus $99/month ($89 annual) | Free forever | video credit rate not read | URL transformations (text overlay, concat) | A CDN, not an editor |

### 3c. AI editing SaaS (ban the pixel-generating features, not the whole tool: AI B-roll, AI actors/avatars, generated images or video, restyle)

| Tool (source) | Price | Watermark / export | Drivable by Claude/Codex | Flag |
|---|---|---|---|---|
| Descript (https://www.descript.com/pricing, https://www.descript.com/api) | Hobbyist $16/month annual ($24 monthly): 10 media hours, 400 AI credits; Creator $24/$35, 30 hours, 4K | Hobbyist "1080p, watermark-free" | **API + MCP**: "Connect the Descript MCP to Claude" (`vendor claim`) | Transcript editing: good for speech, poor for silent clips |
| Opus Clip (https://www.opus.pro/pricing, https://www.opus.pro/api) | Free 60 credits; Starter $15/month (monthly only, 150 credits); Pro $29 monthly or $14.5 yearly ($174), 300 credits, "Limited API Access" | Free: watermark, 1080p | API + MCP (`vendor claim`) | Long talking video to clips. AI B-Roll on Pro (ban). Credit unit not read |
| Submagic (https://submagic.co/pricing, https://www.submagic.co/api) | Starter $19/month, 15 videos, 2 min max each, 1080p30; Pro $39, 40 videos; Business $69, 100 videos, 4K60 | No watermark on paid | API live; API minutes read as 100 and 10 in two blocks (need review) | **16 reels exceed Starter's 15 videos**, so Pro $39. AI hook titles, AI videos and images exist (ban) |
| Vizard (https://vizard.ai/pricing) | Free 60 credits a month (1 credit = 1 min uploaded); Creator removes watermark, 4K; **paid price not read** | Free watermarked (page structure) | API page exists, not read | Long to short clips |
| VEED (https://www.veed.io/pricing) | **price not read** | not read | Video APIs (subtitles, Fabric avatar): https://www.veed.io/api | Fabric lip-sync avatars: ban |
| Kapwing (https://www.kapwing.com/pricing) | Free: watermark, 4 min exports, 30 min a month; Pro $16 (period not stated), no watermark, 4K, 2 h | as stated | API not read | Browser editor |
| Clipchamp (https://clipchamp.com/en/pricing/) | Free: 1080p, "no watermarks"; 4K with Premium (in Microsoft 365 Personal/Family; price not listed). `unverified (WebFetch summary)` | none | none mentioned | Human editor on Windows |
| CapCut / Captions / InShot / VN | w1h 1.4: CapCut Standard $9.99/month, Pro $19.99; CapCut sounds non-commercial only | free watermark not read | GUI only | Library music not licensed for the shop |

### 3d. In-phone baseline

Instagram **Edits**: free, "4K with no watermark" and auto captions per its App Store listing (w1h `verified`); Hollie's time 10-15 min a reel (`inferred`, w1h), so 16 reels is about 3-4 hours a month. It is the right month-one tool because accounts and stock are unsettled. Export metadata and any "AI info" behaviour are **not tested**.

## 4. Music bed, credit, loudness

- Bed: the four Kevin MacLeod CC BY 4.0 tracks in `docs/music-and-lights-notes.md`. The EDL's `music.start` picks the bar; the script loops short tracks (`-stream_loop`), fades in 0.5 s and out 1.5 s, and writes the credit as two end-card lines. The same credit text goes in the caption (condition: visible credit, per his FAQ as read 2026-10-26). Content ID claims on CC tracks are possible (`inferred`).
- Loudness: two-pass `loudnorm` (measure, then apply linear gain) to -14 LUFS, -1.5 dBTP, verified with `ebur128`. **-14 LUFS / -1 dBTP is a `practitioner` consensus** (several 2026 guides); other guides say -16 or -10 to -12; **no Meta page states a target**. Platforms normalise at playback, so the choice only sets how the reel sits next to others.

## 5. How a Claude-written EDL becomes a render

1. Hollie shoots; ingest (w2g) drops clips in a shoot folder with a manifest (file, what it shows, real-item id).
2. Claude (Haiku for drafts, a stronger model for exceptions) reads the manifest plus Hollie's one line and the w1c hook bank, then writes the EDL: clip in/out/speed/fit, 3-10 word hook as pre-broken lines (drawtext does not wrap), music track and start, end card.
3. `render.py` lints (text width, tone), builds one command, runs it, then asserts the format/metadata/loudness checks above. Non-zero exit means the draft never reaches Hollie.
4. Output today: the mp4 and a console check list. **To build:** a sidecar caption/credit text file and a 6-frame contact sheet (`fps=1/2,scale=360:-1,tile=3x2`) for the approval push.
5. Not built (ponytail ceilings): constant speed per clip (a ramp is two clips; true slow-mo needs 120 fps source); no crossfades (`xfade` is present); no stabilisation (`vidstab` present); no per-clip original audio or ducking (`sidechaincompress` present); `drawtext` still expands `%{...}`, so the lint should reject `%{`; slo-mo files from the phone not tested.

## 6. Recommendation for Holliewood & Vine

| Tier | What | Human still does |
|---|---|---|
| (a) free, native | Edits on the phone, hook from the w1c bank, Sound Collection audio, ffprobe one export for GPS | Everything, every reel; 3-4 h a month |
| (b) one paid tool | If no box: JSON2Video pre-paid $49.95 (no expiry) or Shotstack $10. If speech clips with animated captions: Submagic Pro $39 or Descript Hobbyist $16 (annual). For silent hands footage nothing paid beats free ffmpeg, so this tier buys little | Writes the EDL by hand or with Claude; approves; tests one export for "AI info" |
| (c) full pipeline | ffmpeg EDL (tested on Fedora, equally runnable on Windows; w2g picks the host), optional Remotion for animated captions, faster-whisper for speech clips | Shoots; taps approve; supplies one real iPhone clip so decode and HDR are calibrated |

**Approval modes.** (A) approve everything: every render goes to a phone push with the contact sheet and the check list; Hollie taps. (B) approve by exception: the compiler is mechanical, so a render that passes all checks, uses only manifest clips and a hook from the bank may ship on schedule. Always human: any hook or caption naming price, age, era, material or condition; any frame showing a face or Hollie in a mirror; any clip not in the manifest; music outside the cleared list; ASR text with dates or numbers. Push and tap UX is w2g's lane.

## 7. Decision matrix (reference load)

| Option | Stage | $/month | Setup (h) | Claude/Codex drivable | Ban/ToS risk | Mode fit |
|---|---|---|---|---|---|---|
| Edits (in phone) | edit | 0 | 0.5 | No (GUI) | None; platform's own app | A only |
| ffmpeg EDL, Fedora or Windows | edit, caption | 0 | 4-6 to productise | Yes | None | A and B |
| Remotion, Fedora | edit (animated) | 0 up to 3 people, else $25/seat | 8-12 | Yes | None | A and B |
| Shotstack PAYG | edit | about 1 | 3-5 | Yes (REST) | None; footage leaves the box | A and B |
| JSON2Video pre-paid | edit | about 1.7 | 3-5 | Yes (REST) | None; footage leaves the box | A and B |
| Creatomate | edit | 45 (annual billed) | 3-5 | Yes | None | A and B |
| Submagic Pro | caption, edit | 39 | 1-2 | API | Check AI add-ons off | A |
| Descript Hobbyist | edit, caption | 16 (annual) | 1-2 | API + MCP | None | A |
| Opus Starter | clip, caption | 15 | 1 | API + MCP | AI B-Roll off | A |

Hours are `inferred`.

## 8. Build effort (Claude Code plus Codex, recommended path)

About **8-12 agent hours**: productise `render.py` into the pipeline repo with the manifest and a pinned-ffmpeg bootstrap (2-3 h); add the speech path (ASR to ASS to burn, 2 h); EDL-drafting prompt, hook bank and lint rules (2 h); contact-sheet and check-list push payload (1-2 h); one cron or watcher and the repair loop (w2g). **Ricky still does by hand:** shoot, tap approve, answer comments, send one real iPhone clip at Most Compatible 1080p30 and one HDR clip, decide approval mode and credit placement, run one "AI info" test post if any SaaS editor is adopted.

## 9. X verified, Y need review

- Pinned build `verified`; johnvansickle.com page as crawled shows 2024 builds (stale or cached), `need review`; ffmpeg.org itself points Linux static builds to BtbN.
- Meta says it cannot yet detect other companies' video AI signals: `verified` on the page (crawl4ai) dated Feb 6, 2024 and Apr 1, 2025; whether that still holds in Oct 2026, and whether any editor writes such markers, `need review` (one export test).
- Remotion free for up to 3 people `verified` (remotion.pro); whether Hollie plus Ricky plus any contractor counts toward 3 is Ricky's.
- Tonemap `mobius` verified on a synthetic round trip only; real iPhone HDR `need review`.
- LUFS: -14 widely cited, -16 and -10 to -12 also cited, no Meta figure.
- Submagic: Starter API minutes (100 vs 10) and whether $19 is monthly or annual-billed (the page shows "Billed monthly" and a 41% annual toggle) need review. Creatomate monthly price, Kapwing Pro billing period, Vizard and VEED prices: not resolved. Clipchamp row is a WebFetch summary, `unverified`.

## 10. Questions for Ricky; gaps

1. Which phone shoots, and is HDR Video off? Please send one real Most Compatible 1080p30 clip.
2. Approval mode A or B for the edit stage? Credit wording on the end card, caption only, or both?
3. Hollie on camera: do we add a face check before ship?
4. Remotion for animated captions, or static hook only?

**Gaps.** No real iPhone clip (the walkthrough is a 568x320 Baseline copy; 4K clips are synthetic). No Instagram upload or label test (no accounts). Edits, CapCut, Descript, Submagic exports not tested for metadata. Vizard, VEED, Kapwing API and prices not read. Podman and pip static ffmpeg not tested. `render.py` not run on Windows. No stabilisation, ramps, original-audio ducking or slo-mo files tested. Noisy-room ASR not tested.

## 11. Cleanup state

Verified 2026-10-29 14:17: `~/social-lab/w2a/` (2.3 GB: clips, outputs, both ffmpeg builds and tarballs, fonts, venv, Remotion node_modules) was removed with `rm -rf`; `~/social-lab` is now empty and nothing else was touched. The shared npm (803 MB) and pip (366 MB) caches pre-date this lane and were left. Reinstall of the ffmpeg build is a 16 s download plus `tar`. Evidence kept in `research/social-2026-10-29/raw/w2a-*` (crawls, `w2a-render.py`, the two EDLs, `w2a-cmd-test1.txt`). Nothing was committed (parent handles wave 3 commits).
