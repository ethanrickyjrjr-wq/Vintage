<!-- Saved verbatim by the parent session from agent w1h's final message, 2026-10-29 (the agent's heredoc write failed on a bash parse error). Raw captures: research/social-2026-10-29/raw/w1h-* -->

Report write failed: bash parse error on the heredoc (not a harness refusal). No file was written (confirmed with ls). Full report below; save it verbatim as `research/social-2026-10-29/w1h-capture-ingest.md`. Raw captures are in `research/social-2026-10-29/raw/w1h-*` (26 files; the empty and landing-shell captures were deleted).

# w1h: capture, gear, edit apps, phone-to-pipeline ingest (accessed 2026-10-29)

Tags: `verified` (read live or measured this session), `vendor claim`, `practitioner`, `unverified (search summary)`, `inferred`. "Not read" means I could not reach the page and did not fill it from memory. Search and WebFetch summaries are tool-written and tagged unverified unless I also crawled the page.

## TL;DR

- **Phone, and what the metadata does and does not prove.** `Downloads/Video.mov` (24.17 s, created 2026-10-26, the shop walkthrough) carries `com.apple.quicktime.model = iPhone 17 Pro`, software 26.5.1. `verified` (ffprobe metadata only). Whether that is the shop phone and who shoots stays Q1. That file is a 568x320, 1.3 Mbps copy, not the original.
- **Size figures come from a different phone.** `IMG_9401.mov` (iPhone 16 Pro Max, 4K30 H.264) runs 25.7 Mbps, about 193 MB/min (46.5 MB for 14.5 s). `verified`, one clip. The shop phone at the recommended 1080p30 is **not measured**, so these are 4K worst cases: Telegram's 20 MB cap about 6 s, Supabase Free's 50 MB about 15 s, Buffer's 300 MB about 93 s.
- **"Most Compatible" (H.264) does not fix the Fedora box.** It cannot decode H.264 either (BRIEF). The real decision is where ffmpeg runs (w2g). Most Compatible only removes the HEVC question on Windows and in third-party apps. `verified` (Apple) / BRIEF.
- **Shoot 30 fps, Auto FPS off, Lock White Balance on, HDR Video off, AE/AF locked on a mid-tone wall, neon exposed down.** The settings exist (`verified`, Apple); the chosen values are `inferred`.
- **Mirrors and the mirror ball will put Hollie or the phone on camera unless you shoot off-axis behind black.** `practitioner`. That recipe is what protects hands-first.
- **One 90-minute shoot, about 34 clips,** covers d1's 20 Instagram posts, 12 TikTok re-cuts and 12 Pin stills. `inferred`.
- **Gear:** Kit A $78.97; Kit B $178.94 on sale prices ($188.94 at regular price; the sale may end), about $209-219 with a turntable. A $149 gimbal busts the $300 cap. `verified` (Neewer US) except the turntable and gimbal.
- **Default editor: Instagram's Edits** (free, 4K, "no watermark", auto captions, per Instagram's own App Store listing). **CapCut's library music is not licensed for a shop's Instagram posts.** `verified` (CapCut Materials License Agreement, updated Jan 22 2026).
- **Workflows:** (a) in-phone about 10-15 min per reel; (b) scheduler queue about 6-10 min; (c) pipeline about 1-3 min of Hollie's time plus a build. All `inferred`, none timed.
- **Ingest, conditional:** the likely winner is share-sheet to the existing Drive folder pulled by `rclone` on the box (`inferred`). Keep it only if one fresh phone clip survives the trip at recorded resolution (see the check under the Drive row). If not, PhotoSync-to-SFTP wins. Telegram needs a self-hosted Bot API server; Syncthing has no official iOS client.

## 1. Findings

### 1.1 Camera settings, the recipe (iPhone)

Apple's guide pages describe the iOS 27 generation (iPhone 18 Pro, "iPhone Duo"); the phone above is on iOS 26.5.1, so menu names may differ. Sources, all accessed 2026-10-29: https://support.apple.com/guide/iphone/change-video-recording-settings-iphc1827d32f/ios , https://support.apple.com/guide/iphone/record-a-video-iph61f49e4bb/ios , https://support.apple.com/guide/iphone/iph3dc593597/ios , https://support.apple.com/en-us/116944 (read via WebFetch; the crawl returned 0 bytes).

| Setting | Do this | Why | Tag |
|---|---|---|---|
| Format | Settings > Camera > Formats > Most Compatible for month one | Apple: "All new photos and videos will now use JPEG or H.264 format." Meta's Reels ad spec also names "H.264 compression" (https://www.facebook.com/business/ads-guide/update/video/instagram-reels) | verified |
| Resolution / fps | 1080p30 default; 4K30 for hero clips you may crop | Apple: "Faster frame rates and higher resolutions result in larger video files." Instagram's help page reportedly wants 30 fps minimum (https://help.instagram.com/1038071743007909, walled) | verified / unverified (search summary) |
| Avoid PAL | Never "HD (PAL)" or 25 fps | US mains are 60 Hz; 25 fps against LEDs bands (forum consensus) | verified (option exists) / practitioner |
| Auto FPS | Off in this dark room | Apple: "automatically reducing the frame rate to 24 fps" in low light | verified; value inferred |
| Lock White Balance | On (Settings > Camera > Record Video) | Apple documents it; keeps burgundy from drifting past neon, brass, lamps | verified; use inferred |
| HDR Video | Off, explicitly | Apple: other devices "receive an SDR version". I did not verify that Most Compatible turns it off | verified (option) / inferred |
| Exposure | Touch and hold a mid-tone wall until "AE/AF Lock"; slide exposure down until neon tubes keep colour | Apple (photo section): "touch and hold the focus area until you see AE/AF Lock"; same in Video per https://primalvideo.com/video-creation/shooting/filming-videos-with-iphone-fix-lighting-and-exposure-changes-with-auto-exposure-lock | verified / practitioner |
| Neon | Dim the sign to its lowest setting if it has a dimmer | YellowPop (a neon seller): "use the dimmer to put it on the lowest brightness setting... adjust and lock exposure settings" (https://www.yellowpop.com/blogs/news/how-to-take-good-pictures-of-your-neon-sign) | vendor claim |
| Slow-mo | 120 fps for ball and glass, under the room's lamps rather than cheap LED panels | Ulanzi (sells panels, dated Sep 15 2026): panels use PWM and can band at 120/240 fps; "test your exact camera and light" (https://www.ulanzi.com/blogs/knowledges/why-led-panels-flicker-120fps-240fps) | vendor claim |
| Stabilisation | Action mode or a tripod | Apple: Action mode "works best in bright light" | verified |
| Audio | Record normally, strip in the edit | Apple: iPhone 16+ record Spatial Audio by default; both probed clips carry a 4-channel second audio stream | verified |

**Capture-format options**

| Option | Cost | Wins when |
|---|---|---|
| Most Compatible, 1080p30 | Smallest H.264 files that every Windows tool opens (bitrate unmeasured) | Default for month one; ingest caps matter |
| Most Compatible, 4K30 for hero clips only | About 193 MB/min at 4K30 H.264 (other phone); hits 20 MB and 50 MB caps first | You will crop in for a vertical re-frame or pull 4K Pin stills |
| High Efficiency (HEVC) 4K | Smaller files (Apple: better compression), but HEVC needs conversion for the Fedora box and some editors | You only edit in Edits/Photos and never ingest to the box |

**Safe-zone framing.** Meta's Reels ad guide: leave "at least 14% of the top, 35% of the bottom, and 6% on each side" free of text and key elements; 9:16; MP4/MOV; AAC 128 kbps+ (same URL). That is ad guidance applied to organic posts: `inferred`. Practical box: subject inside the middle 88% wide, between 14% and 65% of the height. w1e owns the grid crop and covers.

**Reflections (mirrors, glass, mirror ball).** All `practitioner` (forum and Q&A consensus via a search summary; the UniquePhoto page was walled): (1) camera off the mirror's centre line, farther back, 2x/3x not 0.5x; (2) black foam board with a lens hole, or black cloth where the reflection falls (the photo checklist already lists a black foam board); (3) dark clothing, no white shirt; (4) light the frame and the reflected surface separately, keep the camera side dark; (5) polarizer evidence conflicts. **Flag:** a mirror shot can show Hollie's face by accident; on-camera or not is Ricky's/Hollie's call, and this recipe keeps hands-first intact.

**Colour temperature.** Warm lamps and brass read right near 3200K. The Neewer NL-36AI offers 3200K / 4100K / 5600K and CRI 97+ (`verified`, product page). Set 3200K (`inferred`).

### 1.2 One 90-minute shoot to four weeks

Ordered by light state to minimise resets. Post numbers are d1's (`research/round-d/d1-social-video.md`). Clips 8-15 s unless noted, vertical.

| Min | Block | Clips | Feeds |
|---|---|---|---|
| 0-5 | Test | One 5 s clip per light; check banding and colour on the phone | all |
| 5-35 | **Lights on** | Slow pan along the burgundy wall past lamps and art, 3 passes (3). Hands wrap pink glass in tissue, tape, write the note card (3). Hand reads a lamp: base, socket, cord, wattage tag (3 x 6 s). Bare corner locked off, then dressed (2). Hands on a video call, post only after booking exists (1) | #2, #7, #11, #12, #16, #17 |
| 35-60 | **Lamps and glass, mood light** | Hand clicks a lamp, the room warms (2). Teaser close-up, no price (1). Hand runs along brass (1). Backlit cut glass on a lazy Susan, hand turns it (2). Light through facets, 120 fps (1). One honest flaw close-up (1) | #6, #8, #13, #14 |
| 60-75 | **Neon** | Hand flips the pink "do it for the plot" neon on (2, 120 fps once). Slow push-in, exposure locked (1). Neon off-axis in a mirror (1). Neon behind a brass lamp (1) | #1 |
| 75-90 | **Mirror ball** | Ball turning in one narrow beam, 15 s (2). Light spots sweeping the wall (1). Facet close-up (1). 120 fps hand spin (1) | #4 |

About 34 clips: 20 Instagram posts, 12 TikTok re-cuts (3 a week, same clips), 12 Pins from 4K frame grabs plus the photo-checklist stills. `inferred`; I did not time a shoot. Per the BRIEF gate, drop-day posts wait for real stock. Keep on-screen text free of "visit", "in store", "our doors".

**Audio.** Silent hands clips plus room-mood music. Business-account music limits are w1a's; the implication here is that CapCut's library is off the table (1.4). The already-chosen option is the four Kevin MacLeod CC BY 4.0 tracks in `docs/music-and-lights-notes.md` (condition: visible credit, per his FAQ read 2026-10-26), mixed into the file and credited in the caption. Content ID claims on CC tracks are possible (`inferred`).

### 1.3 Gear (Neewer US store JSON and product pages, 2026-10-29; tax and shipping excluded)

Neewer's page: "prices vary by location" (tariffs, logistics); free shipping over $50 shown on the page. The room has its own lamps and neon; add small fill, do not flatten the mood.

| Kit | Items | Sum | Wins when |
|---|---|---|---|
| **A, under $100** | DS034 desk mount, C-clamp, phone holder $29.99 (https://neewer.com/products/neewer-basics-ds034-camera-desk-mount-stand-with-c-clamp-phone-holder-66610105); TP34 flexible phone tripod $25.99 (https://neewer.com/products/neewer-tp34-flexible-phone-tripod-66610307); NL-36AI bi-colour light $22.99 (https://neewer.com/products/neewer-nl-36ai-camera-soft-light-66600903). Black foam board and lazy Susan already in the kit/kitchen | **$78.97** | First month; you only need a steady phone and one fill |
| **B, under $300** | DS026 overhead phone stand $44.99 (https://neewer.com/products/neewer-ds026-overhead-phone-tripod-stand-66609390); TP34 $25.99; ST180B 180 cm light stand $34.99 (https://neewer.com/products/neewer-basics-st180b-180cm-photography-light-stand-66609099); 2x RGB61 RGB light, **sale** $24.99 each, regular $29.99 (https://neewer.com/products/neewer-rgb61-cri-97-rgb-video-light-360-full-color-led-camera-light-with-3-cold-shoe-66600609); NL-36AI $22.99 | **$178.94** (sale), $188.94 (regular) | Backlit glass and weekly batches; you want a pink or amber rim light |
| B + turntable | Generic 20 cm motorised USB turntable about $28-31 (`unverified (search snippet)`) | about $209-219 | A no-hands object loop is wanted |
| B + gimbal | DJI Osmo Mobile 8 reportedly $149 (Canon Rumors, via search summary). DJI's own page was not reached: **price not read** | about $358, over cap | Walkthrough pans; Action mode plus tripod is the free alternative |

Turntable references: Foldio360 Smart Turntable $139 (https://www.orangemonkie.com/products/foldio360-turntable, `verified`, store JSON); B&H Angler motorised $98 (`unverified`, snapshot reportedly about 9 months old). Hollie's hand on a lazy Susan fits hands-first. Mic: not needed (silent clips). **Skip:** ring lights (round catchlights in glass), softboxes, polarizers for mirrors, shotgun mics, any gimbal before month two (`inferred`).

### 1.4 Editing and posting apps (App Store listings, US, 2026-10-29, unless stated)

| App | Price | Watermark / export | Captions, templates | Commercial-use music | Wins when |
|---|---|---|---|---|---|
| **Instagram Edits** (id6738967378) | Free. Listing says "In-App Purchases" but lists none: **price not read** | "Export your videos in 4K with no watermark"; capture "up to 10 minutes" (listing; https://edits.instagram.com/) | "Generate captions automatically"; templates (v447 notes); weekly updates (v453.1, Oct 27) | Instagram's audio; rules are w1a's (help page walled) | Default. Reviews report crashes and battery drain (users) |
| **CapCut** (id1500855883) | App Store IAP: Standard Monthly $9.99, Pro Monthly $19.99, Yearly $89.99. capcut.com/pricing: Pro $19.99/mo or $179.99/yr, Ultra $79/mo, "reference only" | Free-tier watermark not on the pricing page: **need review** | Auto captions, templates, speed 0.1-100x | **Sounds are non-commercial only**; Commercial Sounds may be shared "within CapCut, TikTok and TikTok for Business" (https://www.capcut.com/clause/material-license-agreement) | You want the deepest templates. Export silent, no CapCut music |
| **InShot** (id997362197) | Pro Monthly $4.99, Yearly $19.99, Lifetime $49.99, Remove ads $3.99 | Ads implied; watermark not read | Auto captions, AI Cut, speed 0.1-100x | Not read | Cheapest one-time upgrade |
| **VN** (id1343581380) | Free; VN Pro $7.99 and $69.99 (periods not stated) | Subtitle: "Free with No Watermark" | Auto captions, templates, LUT import | Not read | Multi-track timeline, no subscription |
| **Splice** (id409838725) | IAP entries $9.99 including "Weekly With Free Trial"; periods unclear | Not read | Not listed | "6,000+ royalty-free tracks from Artlist and Shutterstock" (vendor claim) | Skip: weekly pricing |
| **Captions** (id1541407007) | Basic weekly $5.99, monthly $9.99, yearly $64.99; Max $24.99 | Not read | AI edit, AI avatars (age 18+) | Not read | Talking-head only; not this shop |
| **Photos / iMovie** (id377298193) | Free | None | iMovie: storyboards, trailers; no auto captions listed. **Conflict:** listing requires iOS 27, the phone is on 26.5.1 | Apple's | Quick trim and slow-mo. Apple's own Clips did not appear in a US App Store search: **need review** |
| **Meta Business Suite / Instagram editor** | Free | None | Native | Meta Sound Collection (w1a) | Last-minute fixes |

**Constraint flag:** Edits' AI animation/Restyle, CapCut's Seedance / Nano Banana generation and Captions' AI Twin/Actors/B-roll are off-limits on product footage under "real photos of real items only". Captions, cuts, colour and speed are fine.

### 1.5 Three workflows, ranked by effort

| | (a) All in the phone | (b) Phone to a scheduler queue | (c) Phone to ingest, Claude/Codex, approval push |
|---|---|---|---|
| Steps | Camera, Edits, post from Instagram | Edits export, Buffer/Publer mobile, queue a week | Share to ingest; box converts, cuts, drafts; push; tap Approve; publish |
| Hollie's time per video | 10-15 min (`inferred`) | 6-10 min plus weekly queue (`inferred`) | 1-3 min plus unattended machine time; setup is a build (wave 2) (`inferred`) |
| Cost | $0 | $0 (free caps: 10 queued per channel, d1 `verified`) | Ingest $0-7/yr plus runtime (w2g) |
| Limits | Manual, no queue | Professional account needed to auto-publish. Buffer Reel: 4:5-9:16, up to 1920 px wide, 3 s-15 min, 300 MB; no custom cover upload; personal accounts get a notification only (https://support.buffer.com/article/657-scheduling-instagram-posts-and-reels, `verified`) | Caps in 1.6; the box cannot decode video until ffmpeg is fixed (w2g) |
| Wins when | Week 1, accounts and stock unsettled | The weekly batch rhythm is set (d1) | Volume, or approve-by-exception, is wanted |

### 1.6 Ingest options for (c), assuming iPhone

| Option | Phone effort | Price | Reliability and limits | Box can watch? | Arrives as | Wins when |
|---|---|---|---|---|---|---|
| **Drive share-sheet to the u/1 folder + `rclone` on the box** | 3-4 taps from Photos; folder exists | Drive price not read. rclone MIT, 60,617 stars, pushed 2026-10-29 (`verified`, gh) | rclone docs: "Shared with me" and `root_folder_id`; 750 GiB/day upload cap (https://rclone.org/drive/). Token made once on the PC and copied to the box: `inferred` (remote-setup docs not read). **Check first:** the only clip I saw that came through Drive is 568x320, and I cannot tell if Drive or the download shrank it. Share one fresh clip, pull with rclone, ffprobe it | Yes, polling | Recorded format (H.264 under Most Compatible) | The check passes; Hollie already uses Drive |
| **PhotoSync to SFTP on the box** | Install once; auto-transfer; pick an album | Premium yearly $6.49, monthly $0.99, lifetime $14.99 / $24.99 (App Store, `verified`) | Vendor: iOS auto-transfer supports only "Location-Based Transfer" and "When Charging" (https://www.photosync-app.com/, iOS 13 note) | Yes, files over SSH | Original or converted: not read | The Drive check fails, or Hollie wants zero taps |
| **Telegram bot** | Share to the bot chat | Free | Bots download "up to 20 MB", upload 50 MB (https://core.telegram.org/bots/faq). Local Bot API server: "Download files without a size limit", "Upload files up to 2000 MB" (https://core.telegram.org/bots/api). The box has no compiler, so that needs a podman image: **unverified** | Yes | Video-vs-file recompression not read | You want approve buttons in the same chat (`inferred`) |
| **Shortcut: share-sheet PUT to R2 or Supabase** | One tap; no Photos "new video" trigger found in Apple's trigger docs (list not read, `unverified`) | R2: 10 GB-month, 1M Class A, 10M Class B, egress free, $0.015/GB-month after (https://developers.cloudflare.com/r2/pricing/, Oct 26 2026). Supabase Free: **50 MB** per file; Pro up to 500 GB (https://supabase.com/docs/guides/storage/uploads/file-limits) | Good once built; you write the presign function | Yes, S3 API or webhook | As shared | You want it in your own stack (Deno/Supabase) |
| **iCloud Photos + `icloudpd`** | None after setup | iCloud tiers not read. icloudpd MIT, 12,352 stars, pushed today, banner "Looking for MAINTAINER" | Unofficial; needs "Access iCloud Data on the Web" on and Advanced Data Protection off (README); Apple ID plus 2FA on a box | Yes, `--watch-with-interval` | Originals (Apple: iCloud Photos keeps "original format, resolution, and frame rate") | Zero taps and ADP is off |
| **iCloud Shared Album** | Add clips | Counts to owner's storage | No API found. https://support.apple.com/en-us/148868 : albums made on iOS 27+ keep "original formats at full resolution", no item limit; iOS 26 or earlier: 15 min, 720p, 5,000 items | **No** (gap) | Original (iOS 27+) | Sharing with people, not ingest |
| **USB cable to PC** | Plug in | Free | Apple: import may convert to "JPEG or H.264" unless Photos > Keep Originals | No | H.264 or original | A one-off bulk pull |
| **Dropbox Camera Uploads** | Automatic | Basic free 2 GB; Plus $9.99/mo 2 TB (https://www.dropbox.com/plans; billing toggle not read) | Camera Uploads help 404'd: **not read**; 2 GB fills fast | Yes (API/rclone) | Not read | Hollie already has Dropbox |
| **Immich on the box** | Choose one album | Free; AGPL-3.0, 117,595 stars; app v3.3.5 | Docs: "select which album(s) you want to back up" (https://docs.immich.app/features/mobile-app/); iOS background reliability not read; heavy for 15 GB | Yes | Original | You also want a gallery |
| **Syncthing** | n/a | Free | **No official iOS client**; syncthing.net lists third-party Möbius Sync for iOS as a sponsor | Yes | n/a | Android or Windows only |
| **Tailscale + SMB** | Files app, manual | Tailscale Personal $0, "Up to 6 users", unlimited devices (https://tailscale.com/pricing) | Manual, not automatic | Needs Samba (`inferred`) | Original | You are away from home Wi-Fi and want a private link |
| **AirDrop; OneDrive; email-to-folder / Mail Drop** | - | **Not read** | AirDrop-to-Windows, OneDrive, email caps and Mail Drop: not read | - | - | - |

**Approval push.** ntfy publishes with "simple HTTP PUT or POST" and has an iOS App Store app (https://docs.ntfy.sh/, `verified`; action buttons and pricing not read). Telegram buttons are the alternative; Pushover not read.

**Android.** Edits links to Google Play (`verified`). Drive/Google Photos backup and Telegram work as above; Syncthing's current Android app status is not read. Google's Photos Library API now reaches only app-created content (search summary, `unverified`), so do not plan on reading a Google Photos library.

## 2. Recommendation for Holliewood & Vine

- **(a) Free and native:** Camera on the settings above, Kit A or nothing, Edits, post from Instagram. Human does everything.
- **(b) One paid tool:** Kit B plus a free Buffer or Publer queue (professional Instagram account for auto-publish); optionally PhotoSync Premium ($6.49/yr). Human shoots, approves captions, answers replies.
- **(c) Full pipeline:** Hollie shoots and shares to Drive (or PhotoSync); `rclone` pulls to the box; a converted copy feeds the w2 cut/caption steps; ntfy or Telegram sends the approval tap. Approve-everything: she taps every post. Approve-by-exception: she taps only posts with a price, a claim or a face. In both she shoots and answers non-"LINK" comments.

## 3. X verified, Y need review

- Phone: iPhone 17 Pro verified from the walkthrough's metadata; that it is the shop phone, and whose the 16 Pro Max clip is, need review.
- CapCut yearly: $89.99 (App Store) vs $179.99 (capcut.com, "reference only").
- Tailscale free tier reads 6 users, unlimited devices (verified); older figures differ.
- Shared Albums limits depend on the iOS version the album was created on (verified); no API either way.
- Reel minimum length: Buffer's main article says 3 s; another Buffer table reportedly says 5 s (search summary).
- Meta's safe-zone numbers are ad guidance (verified), applied to organic by inference.
- Edits "Only for iPhone" on the listing means no iPad; the Edits site links Google Play (not a conflict).

## 4. Questions only Ricky can answer

1. Is the iPhone 17 Pro the shop phone, and is Hollie the one shooting?
2. Does Hollie approve every post or only exceptions?
3. Does Hollie appear on camera when a mirror catches her?
4. May the box run a user-space ffmpeg and a Telegram/ntfy listener (w2g)?
5. Is a $79 or $179 gear spend approved?

## 5. Gaps

Not read: Instagram help pages (walled), DJI price, OneDrive, email caps and Mail Drop, Dropbox Camera Uploads, AirDrop-to-Windows, Telegram video-vs-file recompression, Shortcuts "Encode Media" and any Photos trigger (Apple's pages returned landing shells), CapCut watermark, InShot/VN/Splice music terms, ntfy action buttons, Pushover, iCloud paid tiers, Drive price. Not measured: 1080p bitrate on the shop phone, and whether a fresh clip survives the Drive trip at recorded resolution (the check in the Drive row).
