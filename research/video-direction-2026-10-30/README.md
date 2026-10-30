# Video direction research, 2026-10-30

Raw layer for `docs/video-direction.md`. Ask (Ricky, 2026-10-30): what the shots and videos should look and feel like (trying on, showing off, talking about pieces) in a small space; how everyday creators do it; how to shoot and how to speak.

## What was captured

Eight long-form YouTube videos from small vintage and thrift creators (try-on hauls, "how I style vintage", a Depop seller's week). Only the **first 75 seconds** of each was downloaded (`yt-dlp --download-sections "*0-75"`, 480p or lower) and transcribed. One frame per video was cut at 40 s for a contact sheet. Videos and frames stay in the session scratchpad and are not committed (other people's likenesses). Transcripts are in `raw/<video id>.txt`.

| Video id | Channel | Title (truncated) | Length | Views on 2026-10-30 | Type |
|---|---|---|---|---|---|
| `y-Ors35p5ic` | Lillian Kay | HUGE WHIMSYGOTH THRIFT HAUL + try on | 12:44 | 7,100 | try-on haul |
| `Uy__pjeBoSc` | Carrie Dayton | a huuuge collective thrift haul (& try on), 90s vintage & Y2K | 20:55 | 52,828 | try-on haul |
| `bbTNS4jHeG0` | Emma Rosa Katharina | Vintage Clothing Thrift Haul, 1960s & 1970s Style | 22:58 | 9,294 | show and tell |
| `liun5XcbFfc` | Jessica Grace | *TRY ON* THRIFT HAUL (unexpected vintage clothing) | 20:15 | 2,656 | try-on haul |
| `Eiu7bu1_GPk` | Vintage Weekends | 10 VINTAGE STAPLES You Can Actually Wear | 17:32 | 10,119 | everyday styling |
| `-aHsCHtouCk` | A Classic Approach | From Heirloom to Everyday, Modern Styling for Vintage | 9:52 | 185 | everyday styling |
| `rd-iMslxU2g` | Kesha The Stylist | How I Style My Favorite Vintage Pieces | 14:37 | 257 | styling, with a website drop |
| `eMH1fAgv594` | bella | depop top seller! week in my life | 19:36 | 60,354 | seller's week |

URL pattern: `https://www.youtube.com/watch?v=<id>`. Found with `yt-dlp "ytsearch14:<query>"` (flat metadata), filtered to under 300K views.

## Method and limits

- Transcripts: faster-whisper `base.en`, VAD on, CPU. Machine transcripts, so names and some words are wrong (video 1's first line reads "I am from your sugar"). Read them for structure, not wording.
- This is **long-form YouTube, not Reels**. It shows how people talk and set up a shot; it does not show a 3-second short-form hook. Every opening ran 30 to 60 seconds of channel intro before the first piece.
- n = 8 videos, 75 s each, one frame each. No performance data beyond public view counts.
- Earlier sample, not repeated here: 15 decor and lamp reels with transcripts in `research/social-2026-10-29/raw/w1c-reels/`.
- Not reached: Instagram and TikTok (walled to these tools), any short-form try-on reel, Instagram's own insight data.

## Tooling notes (commands that worked)

1. **Find:** `uvx yt-dlp --flat-playlist --print "%(id)s|%(duration)s|%(view_count)s|%(channel)s|%(title).70s" "ytsearch14:<query>"`. Short-form queries (`#shorts` plus a niche phrase) returned mostly keyword spam; long-form try-on and styling queries returned usable creators.
2. **Download the first 75 s:** `uvx yt-dlp -f "bv*[height<=480]+ba/b[height<=480]" --merge-output-format mp4 --download-sections "*0-75" -o "<dir>/%(id)s.%(ext)s" <url>` (needs ffmpeg; YouTube serves split video and audio).
3. **Transcribe:** decode with the system ffmpeg to 16 kHz mono float32 (`-f f32le -ac 1 -ar 16000 -`) and pass the numpy array to faster-whisper `model.transcribe`, run through `uv run --with faster-whisper python -I`. Its own PyAV decoder errors under `uv run`.
4. **Contact sheet:** Windows ffmpeg takes explicit input files, not globs; stack with `hstack` and `vstack`.

## Web sources read this session (2026-10-30)

- https://www.engadget.com/social-media/instagram-chief-ai-is-so-ubiquitous-it-will-be-more-practical-to-fingerprint-real-media-than-fake-media-202620080.html (Dec 31 2025; press account of Mosseri's year-ahead post)
- https://www.threads.com/@mosseri/post/DS76UiklIDf/media (primary post; only one sentence came through: "authenticity is becoming infinitely reproducible")
- https://www.thevintageseeker.ca/magazine/icp-member-reel-talk-how-resellers-can-navigate-instagram-reels-1290343007 (Dec 9 2022, from an Oct 2022 Later webinar; members-gated; format ideas only)
- https://www.ulanzi.com/blogs/guides/small-apartment-video-setup (accessory vendor; small-room setup)
- https://creatorflow.so/blog/instagram-outfit-posts-link-requests/ (vendor; the "3 to 5x link requests" claim, not read in full)
- https://www.nokillmag.com/articles/tag/3days3ways/ (a "3 days, 3 ways" styling series, editorial)
- Search summaries only, unread pages: Marie Claire UK vintage-on-Instagram piece (fetch returned the headline only), Popsugar AU citing the Depop Seller Handbook ("model shots +60%"), Meta and Toluna Reels sound study (via ppc.land).
