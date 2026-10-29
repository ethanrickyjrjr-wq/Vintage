# w2e: GitHub scan for the social pipeline (2026-10-29)

Lane w2e. Stage taxonomy: `ingest > edit > caption > cover > publish > reply > analytics`. Budget used: 40 of 60 `gh` calls (29 `gh search`, 4 batched GraphQL calls of 10 to 23 repos each, 7 `gh api`), 9 crawls of 45, 0 web searches. Provenance for every star, push date and license below: `raw/w2e-gh-repos.tsv` (all `gh`, read 2026-10-29). Raw crawls: `raw/w2e-postiz-*.md`, `raw/w2e-mixpost-pricing.md`, `raw/w2e-meta-platform-terms.md`. Repos live at `https://github.com/<owner>/<repo>`.

Tags: `verified` (read or ran this session), `vendor claim` (README or pricing page), `inferred`, `unverified`. Columns: Fed = Fedora CPU box, Win = Windows PC, Host = hosted. "Drive" = how Claude or Codex can drive it. Nothing listed in the stage tables is archived or unmaintained for over a year (those are in the Dropped line). Throwaway test results are in the "What I ran" section; synthetic clips are labelled.

## TL;DR

- The Fedora ffmpeg wall is solved with no sudo. A user-local static build decodes H.264 and HEVC and encodes libx264 there: `pip install imageio-ffmpeg` (ffmpeg 7.0.2, libass subtitles, no `drawtext`) or the BtbN build (ffmpeg + ffprobe, libx264, subtitles and drawtext). `verified`, tested on a real 4K iPhone H.264 clip and on synthetic 8-bit H.264/HEVC clips.
- Best open-source scheduler for a Claude/Codex operator: **Postiz** (40,085 stars, AGPL-3.0, pushed 2026-10-28). It ships a CLI, MCP and API, and installs as a Claude Code plugin or skill. `verified`. Use it as **Postiz Cloud** ($29/mo shown, 5 channels, 7-day trial), because the self-hosted edition needs your own Meta, TikTok and YouTube apps and 9 containers. `verified`.
- Self-hosted Postiz has open Instagram connect failures right now (#1578 deprecated scope, #918, #2219, #2299 token refresh after 59 days) and an idle-CPU report (#1570). `verified` (issue list). Do not put it on the shared Fedora box. It was not run.
- **Mixpost Lite is not an option**: free tier posts only to Facebook Pages, Mastodon and X. Instagram, TikTok, Pinterest and YouTube need Pro, $299 one-time. `verified` (mixpost.app/pricing).
- The own-API path for Instagram already exists as an MCP: **mikusnuz/meta-mcp** (31 stars, MIT, v2.2.2 on 2026-10-19; 66 tools: reels, stories, carousels, alt text, comments, DMs, insights). Single maintainer, small user base. `verified` stats, `vendor claim` features.
- Silence-cutting is the wrong default for Hollie's hands-first footage. auto-editor's default cut took the real iPhone clip from 14.4 s to 0.43 s. Use `--edit motion` or `--edit none`, and always pass `-res` and `-c:v libx264`. `verified`.
- **HyperFrames** (heygen-com, 75,323 stars, Apache-2.0) renders HTML to MP4 and PNG stills on the Fedora CPU box: 10 s 1080p in 8.7 s, stills in 2.9 s, once BtbN ffmpeg/ffprobe and a user-local Chrome shell are in place. `verified`. Telemetry is on by default.
- AI video generators (MoneyPrinterTurbo 136k stars, ClipForge and the like) are **avoid** under the "real photos of real items only" rule. They synthesize stock or AI footage from text.
- Unofficial Instagram and TikTok libraries (instagrapi, tiktok-uploader and others) are listed as NOT recommended. Their own READMEs describe private-API or cookie-borrowing methods.
- No official TikTok Content Posting SDK appears among the tiktok org's 30 most recently pushed repos (only Business/Ads, Login Kit, Share Kit). `verified` (partial list).

## Publish

Ranked by "wins when". The Wave-1 facts (IG Standard Access with no review for own accounts, TikTok signup needs a legal entity) come from w1a and the wiki.

| # | Option (stage: publish) | Stars / push / license | Runs | Drive | ToS risk | Evidence | Verdict, wins when |
|---|---|---|---|---|---|---|---|
| 1 | **Postiz Cloud** (gitroomhq/postiz-app, hosted edition) | 40,085 / 2026-10-28 / AGPL-3.0 | Host. $29 Standard, 5 channels, unlimited posts, 7-day trial; Team $39 (10 ch), Pro $49 (30), Ultimate $99 (100). Monthly vs yearly toggle not distinguishable in the crawl: price basis not read | CLI, MCP, API (every plan, page claim) | Low: "official, platform-approved OAuth flows" (vendor claim). Uses Postiz's own approved apps, so no TikTok developer signup | v2.25.3 on 2026-10-24; 130 open issues; issue closed 2026-10-29; 7,600 forks | **use**. Wins when you want Claude/Codex to schedule through one tool and skip app review (TikTok especially) |
| 1a | Postiz API/CLI surface | postiz-agent 557 / 2026-10-22 / AGPL-3.0 per npm package.json (GitHub says NOASSERTION) | CLI ran on Fed (Node 26.9, npm install 2 s, not authenticated) | `postiz posts:create -t draft\|schedule --settings <json>`, `posts:status` (draft to schedule), `upload`, `analytics:post`; API 90 requests/h (100 cloud) on create-post | n/a | Docs: IG settings `post_type` post\|story, `is_trial_reel`, `graduation_strategy`, `collaborators` (native scheduling cannot do collabs, w1a); no cover field in the IG schema as read. TikTok `content_posting_method` DIRECT_POST or UPLOAD (to the TikTok app inbox) | Set `--shortLink false` or check it: default `true` shortens links. UPLOAD is the approve-everything path for TikTok. Whether an unaudited app may DIRECT_POST publicly is w2c's question: need review |
| 2 | **meta-mcp** (mikusnuz) own-API IG + Threads | 31 / 2026-10-19 / MIT | Fed or Win (Node, MCP) | MCP, plus `templates/AGENTS.md` and `CLAUDE.md` | Low if the Meta app is ours (Standard Access, no review, w1a) | 3 releases in recent weeks (v2.2.0 to v2.2.2); 1 open issue; README: reels with `trial_params`, AI-info and paid-partnership labels, alt text, carousels, stories | **study, then use** for path 3. Wins when only Instagram matters and no monthly fee is wanted. No scheduler: needs a cron (the README prompt says "schedule"; Graph API scheduling not confirmed: need review) |
| 3 | **n8n** + `MookieLian/n8n-nodes-instagram` | n8n 209,016 / 2026-10-29 / Sustainable Use License (internal business use OK, not OSI; text read). Node: 30 / 2026-03-17 / MIT | Fed or Win (Node; not tested here) | GUI + webhooks + HTTP; Claude writes workflow JSON (inferred) | Low (Graph API) | n8n v2.45.6 released 2026-10-29. Node v3.4.0: images, reels (trial reels), stories, carousels, comment moderation, private replies, DMs, webhook triggers (README) | **study**. Wins when scheduling, approvals (wait nodes) and replies should live in one visual workflow |
| 4 | **Mixpost** Pro | 3,883 / 2026-03-16 / MIT (Lite repo) | Own PHP host | API, MCP (Pro) | Low | v2.6.0 2026-03-16 (7.5 months quiet). Pro $299 one-time, 1 domain, 1-year updates, engagement inbox, approval flow. Pro source licence not read | **study**. Wins when a one-time $299 beats $29/mo over 10+ months and PHP hosting is fine |
| 5 | YouTube: `anwerj/youtube-uploader-mcp`; official `googleapis/google-api-nodejs-client` | 62 / 2026-09-20 / MIT; 12,278 / 2026-10-22 / Apache-2.0 | Fed or Win | MCP; library | Low | v0.3.0 2026-09-20: upload, scheduled publish, thumbnails under 2 MB, playlists, subtitles | **use** (MCP) if YouTube Shorts is posted outside Postiz |
| 6 | Pinterest: official `pinterest/pinterest-python-sdk`; `clugtu/pinterest-mcp` | 86 / 2026-09-02 / licence not read; 8 / 2026-03-12 / MIT | Fed or Win | Library; MCP (create_pin with link, analytics) | Low | MCPs are tiny (2 to 8 stars, no issues): little evidence | **study**. Wins when Pinterest needs a link-per-pin job outside Postiz |
| 7 | Avoid: `SamurAIGPT/postiz-cheap` (1,370 stars, MIT) | | | | | README: social accounts, uploads, publishing and AI all go through a required MuAPI key | Not self-hosted publishing. **avoid** |
| 8 | Avoid / instructive only: `cogsend/cogsend` (249, MIT) | | | | | Mastodon, Bluesky, LinkedIn, Threads, X only | No Instagram, TikTok or Pinterest. **study** (Cloudflare Workers pattern) |
| 9 | Avoid: `jakemeany523/buffer-mcp` (1 star, no licence); `Seym0n/tiktok-mcp` (208, MIT) | | | | | Buffer MCP is a one-person repo (README says Buffer's REST API is deprecated, GraphQL current: vendor claim). The TikTok MCP only reads videos and subtitles through the TikNeuron third-party service | **avoid** |

## Edit

| # | Option (stage: edit) | Stars / push / license | Runs | Drive | ToS risk | Evidence | Verdict, wins when |
|---|---|---|---|---|---|---|---|
| 1 | **Static ffmpeg + Claude-written scripts**: `BtbN/FFmpeg-Builds`, `imageio/imageio-ffmpeg` | 11,892 / 2026-10-28 / MIT scripts (GPL build); 304 / 2026-10-28 / BSD-2 | Fed (tested), Win (existing ffmpeg 8.1.2 ran here) | CLI | None | Ran both (see "What I ran") | **use**. Wins when edits are deterministic: scale to 1080x1920, trim, burn text, concat intro and outro |
| 2 | **HyperFrames** (heygen-com) | 75,323 / 2026-10-29 / Apache-2.0 | Fed (tested with BtbN + Chrome shell), Win (README section) | CLI; plugin for Claude Code; `npx skills add`; scaffold writes AGENTS.md and CLAUDE.md | None; telemetry on by default, linked to a HeyGen account only if you sign in | v0.8.217 same day; 76 open issues; `doctor`, `lint`, `snapshot`, `render` | **use** for branded overlays, animated text, title cards. Wins when the look is HTML/CSS (burgundy, Bodoni Moda) |
| 3 | **auto-editor** (WyattBlue) | 5,658 / 2026-10-28 / Unlicense | Fed, Win, macOS binaries (assets listed: linux-x86_64 44 MB, windows-x86_64.exe 42 MB) | CLI; README offers `npx skills add WyattBlue/auto-editor` (vendor claim) | None | v31.7.2 on 2026-10-03; 1 open issue; Nim single binary | **use with care**. Wins when footage has speech or dead air; motion mode for hands-only clips |
| 4 | **video-use** (browser-use) | 30,082 / 2026-10-08 / MIT | Fed or Win (Python, ffmpeg, needs an ElevenLabs API key; price not read) | Claude Code and Codex skill (README symlinks into `~/.claude/skills` and `~/.codex/skills`) | None | 34 open issues, last merged PR 2026-10-08; cuts filler words, burns subtitles, 30 ms fades | **study**. Wins only when Hollie talks to camera |
| 5 | **Remotion** (+ `remotion-dev/skills`) | 68,844 / 2026-10-29 / Remotion License (free for individuals and for-profits up to 3 employees; page says terms change in 5.0). Skills: 5,869 / 2026-10-26 / no licence file detected | Fed or Win (headless Chrome) | CLI, official skills | None | v4.0.539 on 2026-10-26 | **study**. Wins when React components are preferred over HyperFrames' plain HTML |
| 6 | Revideo (`midrender/revideo`) | 4,156 / 2026-07-15 / MIT | Node + headless browser | CLI/API | None | PostHog telemetry, opt-out env var | **study**: MIT alternative to Remotion |
| 7 | GUI editors: LosslessCut (45,434 / 2026-10-29 / GPL-2.0, v3.70.2); OpenCut (96,766 / 2026-09-24 / MIT) | | Win | GUI only | None | OpenCut README: being rewritten, MCP server and headless mode are "coming"; the classic repo is the one to use today | **study**: human trimming fallback. Not drivable |
| 8 | Avoid: MoneyPrinterTurbo (136,276 stars, MIT), ClipForge (1,127, AGPL), LocalMiniDrama, Anil-matcha/AI-Youtube-Shorts-Generator (5,650) | | | | | They generate script, stock or AI footage and TTS from a topic, or clip long YouTube videos | **avoid**: breaks "real photos of real items only" (BRIEF.md). MoneyPrinterTurbo does accept local clips, but its design is stock-footage-first |

## Caption

Silent hands-first clips need an on-screen text overlay built from Ricky's one-line input, not transcription. Caption copy is Claude's job (no repo).

| # | Option | Stars / push / license | Runs | Drive | Evidence | Verdict, wins when |
|---|---|---|---|---|---|---|
| 1 | ffmpeg libass `subtitles`/`ass` filter (or `drawtext` on the BtbN build) | in BtbN / imageio | Fed, Win | CLI | 2-line SRT burned on real 4K iPhone clip in 9.1 s, on a 12 s synthetic clip in 2.6 s | **use** for silent clips |
| 2 | HyperFrames text and caption layers | as above | Fed | CLI/skill | Rendered text composition tested; captions skill not run | **use** when captions should be animated or brand-styled |
| 3 | faster-whisper (SYSTRAN, 26,294 / 2026-10-25 / MIT) | already installed on Fed by the desk (clipfeed) | Fed | CLI | v1.2.1 is from 2025-10-31; repo active | **use (no install)** when Hollie narrates |
| 4 | video-use (ElevenLabs Scribe, word-level) | above | Fed/Win | skill | needs ElevenLabs key | **study** if narration plus filler-word cuts matter |
| 5 | whisper.cpp (54,766 / 2026-10-29 / MIT) | | Win; Fed needs a compiler the box lacks (desk, wiki) | CLI | HyperFrames `doctor` also reports whisper-cpp missing | **avoid on Fed**; do not install whisperX either |

## Cover (w2b covers this lane in depth)

| # | Option | Stars / push / license | Runs | Evidence | Verdict, wins when |
|---|---|---|---|---|---|
| 1 | HyperFrames `snapshot` (PNG frames + contact sheet) | above | Fed | 5 PNGs + contact sheet in 2.9 s (placeholder composition; fonts not tested) | **use**. Wins when cover and video share one HTML design |
| 2 | `vercel/satori` (JSX to SVG; PNG needs a rasterizer) | 14,145 / 2026-10-23 / MPL-2.0 | Fed/Win/Vercel | v0.63.2 on 2026-10-20 | **use** when covers are generated in a Deno/Vercel function |
| 3 | `microsoft/playwright` screenshot of an HTML template | 98,813 / 2026-10-29 / Apache-2.0 | Fed/Win | v1.64.1 | **use** for a no-new-dependency path |
| 4 | `lovell/sharp` composite of the real product photo on a template | 32,807 / 2026-10-29 / Apache-2.0 | Fed/Win | v0.35.5 | **use** for the Pinterest 1000x1500 pin |

## Ingest (w1h has the phone side; only repo facts here)

| # | Option | Stars / push / license | Notes | Verdict |
|---|---|---|---|---|
| 1 | `rclone/rclone` | 60,617 / 2026-10-29 / MIT | w1h's likely winner (Drive folder pulled on the box) | **use** |
| 2 | `grammyjs/grammY` Telegram bot | 3,786 / 2026-10-16 / MIT | w1h: bot download cap 20 MB, local Bot API server needs a container | **study** |
| 3 | `syncthing/syncthing` | 89,867 / 2026-10-29 / MPL-2.0 | No official iOS client (w1h) | **avoid** for iPhone |
| 4 | `immich-app/immich` | 117,598 / 2026-10-29 / AGPL-3.0 | Heavy for the 15 GB box (w1h) | **avoid** unless a gallery is wanted |

## Reply

Replies must fit the LINK shape: keyword gets the listing link and nothing else; everything else is a draft. The tools below are neutral; w2d decides the public-reply plus private-reply rule.

| # | Option | Stars / push / license | Runs | Drive | ToS risk | Evidence | Verdict, wins when |
|---|---|---|---|---|---|---|---|
| 1 | Own webhook: Supabase Edge Function (Deno) + Graph API | no repo | Host (Supabase) | Claude/Codex write it | Low (official API, own app) | `flam-ing/instagram-comment-skill` (5 stars, no licence, v1.0.0 2026-08-23) shows the pattern: official Meta webhooks on a Cloudflare Worker, no polling | **study the pattern, then build**. Wins when the keyword rule is simple and a human queue is a table |
| 2 | **n8n + n8n-nodes-instagram** | see Publish | Fed/Win | GUI/JSON | Low | README lists comment moderation, **private replies**, DMs, webhook triggers | **study**. Wins when the private-reply route is chosen |
| 3 | **meta-mcp** | see Publish | Fed/Win | MCP | Low | 7 comment tools (get, post, reply, hide, delete); DM tools; a grep for "private" in the README found none: no private-reply tool listed | **use** for Claude-drafted replies in mode A |
| 4 | **Chatwoot** | 38,554 / 2026-10-29 / MIT (README); `ee` licence not read | Rails + Postgres + Redis: heavy (inferred) | API | Low | v4.19.1 on 2026-10-24; README lists Instagram as a channel; comment handling not read | **study**. Wins as the human approval inbox for DMs |
| 5 | Mixpost Pro Engagement Inbox | see Publish | | | | $299 one-time | **study** |

## Analytics

| # | Option | Stars / push / license | Evidence | Verdict, wins when |
|---|---|---|---|---|
| 1 | Postiz analytics (`analytics:platform`, `analytics:post`) | above | Included on cloud plans (page claim); self-host needs analytics scopes on your own app | **use** if Postiz is the scheduler |
| 2 | meta-mcp insights (`ig_get_account_insights`, post insights) into a Supabase table | above | Tool table read | **use** for the own-API path |
| 3 | `umami-software/umami` | 39,782 / 2026-10-28 / MIT | v3.4.1 on 2026-10-23; tag every listing link with UTM and see which post sent visitors | **use** (wins when the listing page is the only call to action) |
| 4 | Avoid: `pipeboard-co/meta-ads-mcp` (1,341) | | Ads insights only | **avoid** unless paid ads start |

## Claude Code skills, Codex AGENTS.md, awesome lists

- Verified examples that ship agent files: HyperFrames scaffold (`init` wrote AGENTS.md and CLAUDE.md, 7,275 bytes each), meta-mcp (`templates/AGENTS.md`, `templates/CLAUDE.md`), postiz-agent (Claude Code plugin: `/plugin marketplace add gitroomhq/postiz-agent`; skill: `npx skills add gitroomhq/postiz-agent`), video-use (symlink into `~/.claude/skills` or `~/.codex/skills`).
- Libraries of skills: `coreyhaines31/marketingskills` (57,283 / 2026-10-29 / MIT, has `social` and `video` skills) **study**; `anthropics/skills` (184,733, no root licence) **study** the format; `agentsmd/agents.md` (25,210, MIT) is the spec.
- No full "social content pipeline" AGENTS.md or skill with real users turned up: skill and n8n-instagram searches returned only repos with 0 to 5 stars. Code search was not used.
- Awesome lists, `study` only, templates not read: `ComposioHQ/awesome-claude-skills` (78,263, no licence), `enescingoz/awesome-n8n-templates` (26,164, NOASSERTION), `Zie619/n8n-workflows` (57,118, MIT; a release is named "dmca-compliance-2025-08-14").

## NOT recommended: unofficial libraries (do not test, do not install)

| Repo | Stars / push | Why not |
|---|---|---|
| subzeroid/instagrapi | 7,040 / 2026-10-28; licence NOASSERTION | README: "combines public web and private mobile API flows" and says private-API automation is fragile (account trust, proxies, device state, challenges), pointing to hosted HikerAPI |
| instaloader/instaloader | 13,717 / 2026-10-26 | Scraper/downloader, MIT |
| davidteather/TikTok-Api | 6,720 / 2026-08-24 | Scraper |
| wkaisertexas/tiktok-uploader (also haziq-exe/TikTokAutoUploader, 308) | 781 / 2026-02-12 | README: works by duplicating your browser cookies to a remote-controlled browser |
| athcagithub/postiz-leaked | 157 | Claims to be leaked source. Legal risk, and the official repo is open |
| dilame/instagram-private-api | 6,488 / 2024-08-09 | Private API, and stale |

ToS reason, with what was and was not read. TikTok ToS 3.4 (desk wiki, read 2026-10-07): no "scrape, crawl, export or otherwise extract any data or content ... using any automated system or software". Pinterest guidelines (w1b raw): "Don't use any undocumented or unsupported method to access, search, scrape, download or change any part of Pinterest." Instagram's Terms page was a bot wall (4 bytes) and a Wayback attempt failed (111 bytes): the exact Instagram clause is `unverified`. Meta Platform Terms (read 2026-10-29): enforcement "can include suspending or permanently removing your App(s) and account". Ban risk to the one brand account: high (`inferred`).

Dropped (archived, or no push in over a year): fluent-ffmpeg (archived), stable-ts (archived), ShortGPT (2025-02-10), short-video-maker (2025-06-21), editly (2025-05-12), ffmpeg-python (2024-08-04), postiz-n8n (2025-10-07; the npm node `n8n-nodes-postiz` is linked from the Postiz README), instagram-engagement-mcp (2025-04-26). Also not listed: TiagoGrosso/instagram-graph-api-lib (95 stars; last release 2024-08-08), and the 2-star Instagram MCPs (postoncehq, thenavidm, HasData, Insightful-Pipe) with no usage evidence.

## What I ran (Fedora `~/social-lab/w2e/`, user-local; deleted afterwards)

Windows ffmpeg 8.1.2 (read-only use, already installed) made two synthetic 12 s 1080x1920 clips (testsrc2 video, sine audio muted from 4 s to 8 s): H.264+AAC mp4 and HEVC .mov. Real clip: `C:\Users\ethan\Downloads\IMG_9401.mov` (3840x2160 H.264 High yuv420p, 30 fps, 14.5 s, AAC plus an Apple spatial-audio track), copied read-only.

| Test | Command (abridged) | Result |
|---|---|---|
| auto-editor 31.7.2 binary (46 MB, curl from the GitHub release) | `./auto-editor phone_h264.mp4 -o out.mp4` | synthetic: decodes, 12 s to 8.43 s in 2.9 s wall; HEVC in gives HEVC out; `--export premiere` wrote a 4.9 KB XML |
| same, real iPhone clip | default edit; `--edit motion:threshold=0.02 -c:v libx264`; `--edit none -res 1080,608 -c:v libx264` | decodes 4K. Default: 14.4 s to **0.43 s** (1.4 s wall). Motion: full 14.47 s, H.264, 41 s wall, output **2880x1620** (not 4K) unless `-res` is set. Third: 1080x608, 18 s wall |
| imageio-ffmpeg 0.7.0 in a venv | `ffmpeg -i IMG_9401.mov -map 0:v:0 -map 0:a:0 -vf "scale=-2:1080,subtitles=t.srt" -c:v libx264 -preset veryfast` | ffmpeg 7.0.2-static; h264/hevc decoders; `subtitles` and `ass` filters present, **`drawtext` absent**; real clip to 1080p with burned caption in **9.1 s**; synthetic HEVC in 2.6 s |
| BtbN `ffmpeg-master-latest-linux64-gpl.tar.xz` (157 MB, 15 s download) | `-decoders`, `-encoders`, `-filters` | ffmpeg, ffprobe, ffplay; h264/hevc decode; libx264 encode; subtitles, ass, drawtext |
| Postiz CLI 2.0.26 | `npm install postiz`, `--help`, `posts:create --help` | runs on Node 26.9; **server not run, nothing authenticated, nothing posted** |
| HyperFrames 0.8.216 | `npm install hyperframes` (9 s, 108 MB); `doctor`; `browser ensure` (19 s, 261 MB in `~/.cache`); `init`; `render`; `snapshot` | Render with system ffmpeg: "MP4 H.264 encoder unavailable". With imageio ffmpeg: capture and encode worked, then the final probe failed because system ffprobe 8.0.1 cannot decode. With BtbN ffmpeg + ffprobe first on PATH: 10 s 1080p H.264 in **8.7 s**. `snapshot`: 5 PNGs in 2.9 s |

Not run, and why: **Postiz server** (no docker or podman-compose on the box; compose has 9 containers including Elasticsearch 7.17, Temporal and two Postgres; 6 to 11 GB RAM was available; publishing cannot be exercised without app credentials or a login, both forbidden). Not tested: iPhone HEVC/10-bit HDR/Dolby Vision, variable frame rate, rotation metadata, anything on Windows, n8n, Chatwoot. The synthetic clips are 8-bit.

## Recommendation for Holliewood & Vine

| Tier | Stack | Human still does |
|---|---|---|
| (a) free, native | Instagram in-app scheduling (w1a: 25 a day, 30 days), TikTok Studio, Pinterest native. Optional: Windows ffmpeg plus a Claude-written script for resize and burned caption | Everything: shoot, caption, cover, schedule, reply |
| (b) one paid tool | **Postiz Cloud Standard, $29/mo shown** (7-day trial first) driven by Claude Code or Codex through the CLI; static ffmpeg for resize and caption burn; covers via HyperFrames or sharp | Shoot; give the one-line input; connect accounts (OAuth); tap approve (draft to schedule); prices, claims, people, complaints |
| (c) full pipeline | rclone ingest, Fedora with BtbN ffmpeg + HyperFrames for overlays and covers, Claude drafts captions, Postiz Cloud (or meta-mcp on our own IG app plus a cron) publishes, a Supabase webhook plus meta-mcp or n8n handles LINK replies, Postiz or meta-mcp insights plus Umami for analytics | Same approvals; Meta app setup and token refresh (Postiz #2299: 59 days); every non-LINK reply |

Approval modes. Mode A (approve everything): Postiz drafts, `posts:status` flips a draft to scheduled after the tap; TikTok `UPLOAD` lands in the app inbox. Mode B (by exception): safe to automate are resize, caption burn, cover render, scheduled publish of pre-approved templates, and LINK replies. Always human: prices, condition, age or provenance claims, any person, complaints, anything touching the fixed constraints.

## X verified, Y need review

- Postiz-agent licence: npm `package.json` AGPL-3.0 (installed v2.0.26) verified; GitHub licence detector says NOASSERTION. Read its LICENSE before relying on either.
- Postiz Cloud $29/mo verified on the page; monthly vs yearly billing of that figure not read.
- Postiz works for Instagram on the cloud: vendor claim. Self-host Instagram failures are in open issues (verified list); not reproduced.
- meta-mcp "schedule a carousel": README prompt verified; whether Graph API itself schedules Instagram posts is not confirmed. Plan on a cron.
- Chatwoot lists Instagram (README verified); comment replies unread.
- n8n licence text verified (internal business use). Whether Hollie's use counts as "internal business purposes" if the stack is ever resold is a lawyer question, not asked.
- Windows support is asserted by release assets (auto-editor `.exe`) and README sections, not run.
- Remotion licence verified for up to 3 employees; the page warns terms change in 5.0.

## Questions only Ricky can answer

1. Approve every post (mode A) or by exception (mode B)? It decides draft vs scheduled in Postiz.
2. Is a legal entity coming? Without one, TikTok through our own app is blocked, which favours Postiz Cloud.
3. Is $29/mo for Postiz Cloud acceptable after the 7-day trial?
4. May Claude install user-local tools on the Fedora box: BtbN ffmpeg (157 MB), HyperFrames (108 MB) and a Chrome shell (261 MB)? All were deleted after this test.
5. HyperFrames and Revideo send telemetry by default: acceptable, or disable?
6. iPhone capture setting: Most Compatible (H.264) or High Efficiency (HEVC/HDR)? Only H.264 was tested on a real clip.

## Gaps

Instagram terms page unreachable (bot wall and Wayback). Postiz server, Windows runs, real HEVC/HDR, TikTok unaudited-app posting rules (w2c) and the public-reply plus private-reply rule (w2d) are untested or out of lane. Seven multi-term `gh search` queries returned zero rows (for example "n8n instagram workflow", "whisper subtitles burn captions video"); shorter queries worked, so a missing repo may be a search miss. Activepieces' Instagram pieces, Pinterest SDK licence, OpenCut classic and the n8n template quality were not read. Hosted aggregators seen in passing (Ayrshare's Claude plugin repo, bundle.social, Zernio) belong to w2c.

## Decision matrix

| Option | Stage | $/mo at reference load | Setup hours (inferred) | Claude/Codex drivable | Ban/ToS risk | Approval-mode fit |
|---|---|---|---|---|---|---|
| Native app scheduling | publish | 0 | 1 | No | None | A only |
| Postiz Cloud Standard | publish, analytics | 29 (price basis not read) | 3 to 5 | Yes (CLI, MCP, API) | Low | A and B |
| Postiz self-host | publish | 0 + hosting | 12 to 20, plus own platform apps | Yes | Low; TikTok blocked without entity | A and B |
| meta-mcp + cron | publish, reply, analytics | 0 | 8 to 12 | Yes (MCP) | Low (own app) | A and B |
| n8n + IG node (self-host) | publish, reply | 0 + hosting | 8 to 12 | Partly (JSON) | Low | A and B |
| Mixpost Pro | publish, reply | 0 (299 once) | 4 to 6 | Yes (API, MCP) | Low | A and B |
| Static ffmpeg scripts | edit, caption | 0 | 3 to 4 | Yes | None | A and B |
| HyperFrames | edit, cover | 0 | 6 to 8 | Yes | None (telemetry) | A and B |
| auto-editor | edit | 0 | 1 | Yes | None | A and B (motion mode only) |
| Chatwoot | reply inbox | 0 + hosting | 6 to 10 | API | Low | A |
| Umami | analytics | 0 + hosting | 2 to 3 | API | None | n/a |
| Unofficial libs (instagrapi etc.) | any | 0 | n/a | Yes | **High** | **Do not use** |

## Build effort (inferred estimates)

Tier (b): about 8 to 12 hours of Claude Code plus 3 to 4 of Codex (CLI wrapper, static-ffmpeg scripts, approval flip, caption template). Tier (c) adds about 25 to 35 hours: rclone ingest (2), BtbN and Chrome shell on the box (1), HyperFrames cover and overlay templates (6 to 8), Supabase LINK-reply webhook (8 to 12), insights into Supabase and UTM tagging (4 to 5), ntfy or Telegram approval ping (3 to 4). Ricky still does by hand: account creation and OAuth connects, Meta developer app and token refresh if the own-API path is used, shooting, and every approval tap in mode A.
