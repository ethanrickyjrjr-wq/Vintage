# Handoff for Claude Code and Codex: the social autopilot

**Status 2026-10-29: designed, nothing built.** Compiled from the lane reports in `research/social-2026-10-29/` (w2a to w2g, w3a, w3b, w3d, w1h); no new research. Tags: `V` verified in the lane, `VC` vendor claim, `I` inferred, "design call" = decided here. Every vendor surface is a hypothesis: crawl the live page before coding it (Vendor First). Companions: `docs/social-manual.md`, `docs/social-manual-appendices.md` (hooks, CTAs, canned replies, cover templates), and the dashboard docs this builds on, `docs/dashboard-design.md` and `docs/dashboard-handoff.md` (T1 to T8).

**Dashboard markers.** **[DASH-T1]** schema and Supabase Pro project, **[DASH-T3]** automatic sold writes, **[DASH-T4]** notify and watchdogs, **[DASH-T6]** PWA shell. The dashboard is also unbuilt; §5.0 gives each fallback.

**Before you start**
- `git status`. Pathspec `git add` only, never `-A`. `site/` belongs to the storefront session (only 5.12 touches it). Each task: `git pull --rebase`, secrets grep, commit, push. Secrets never enter the repo: names only in `.env.example`.
- **Hollie**, with ie, she/her. Never "Hollywood" next to "Vine".
- Ship paused: `social_control.paused = true` until Ricky says otherwise; no product post before real stock.
- Layout (design call): SQL and Edge Functions in `dashboard/supabase/` (one project, one migration history, `0004_social.sql`); runner code, templates, fonts, tests in `social/`; workflow at `.github/workflows/render.yml`.

## 1. Purpose and non-goals

**Purpose.** Run the shop's social posting mostly unattended. Hollie shoots clips and types one line; the pipeline cuts the reel, renders the cover, drafts the caption; Hollie taps Approve (mode A) or only exceptions (mode B); it posts on schedule, answers "LINK" comments with the listing link, drafts all other replies for approval, and logs metrics. One switch stops it all. Stages: `ingest > edit > caption > cover > publish > reply > analytics`. Pattern: photos in, one line in, a draft out, a human taps.

**Non-goals:** selling, holding or claiming by comment or DM; auctions; discounts; AI-generated imagery, voices or music; a second control plane or self-hosted scheduler; ads, extra outbound DMs, customer records; changes to the dashboard's selling flows or to `site/` beyond 5.12. §12 names the specific tools to avoid.

## 2. Fixed shop constraints (BRIEF.md) and the link rule

| Constraint | Enforced by |
|---|---|
| No claims by DM or comment; the only call to action is the listing page. No bidding or claim-to-bid lives (whether that is a regulated auction in Florida is unchecked: flag any such idea for a lawyer). No discounts, codes or offers ("Absolutely no offers"). | fixed reply templates; lint (5.3); "mine/hold/dibs" gets a draft "Pieces can't be held" |
| No showroom language ("visit", "in store", "our doors", "stop by"): the room is not open. Hollie is she/her. "Style", never "interior design" (Florida ch. 481). | lint; never send `location_id` |
| The mirror ball is sometimes a gift, never promised, never every order, never tied to commenting. | lint |
| Sample listings, illustrative prices, checkout "coming soon"; shop accounts do not exist; `@holliewoodandvine` ownership unknown. | `paused` defaults true; `product` posts need an `active` item and a live piece page |
| Real photos of real items only. | manifest clips only; no generated-pixel cutouts on selling covers; no `is_ai_generated`; a VLM never writes material, age, maker, condition or price |
| Burgundy look, Bodoni Moda (never under 20 px), DM Sans, neon pink, white only around product photos; hands-first. | six cover templates; `has_person` flag |
| Approval: "photos in, one line in, a draft out, Ricky taps Publish"; whether Hollie approves each post is open, so both modes are built. | `social_control.mode`; §6 |
| Sold is "Gone" and stays visible. No legal entity confirmed. Budget unset, lead with free. | lint; entity-gated features flagged (Business Verification, Live mode, comment webhooks, TikTok developer signup); §9 |

**Link rule (w2d §1).** A bare URL in a public comment is not tappable (VC). Routes: **A** link in bio plus "piece No. [n]" on every post (primary, no platform risk; needs 5.12); **B** a "LINK" comment gets one fixed public reply plus one private-reply DM carrying only the listing URL; **C** a Story link sticker by hand on drop days (no sticker field in the API). Every CTA offers A first: "Link in bio, piece No. 14. Or comment LINK and Hollie will message it." B is a convenience, never a gate: never "comment to get/unlock", never gate on a follow. A private reply is one per comment, within 7 days, lands in Requests unless the person follows us, 750 an hour (V). **Not applied silently:** a compliant B adds a public reply and maybe one automated-message line, which may break "nothing else". B stays by hand until Ricky answers (§11 #6).

## 3. Architecture

```
Phone > Drive / PWA / CLI > Supabase Storage (private raw bucket)
 pg_cron 5 min > Edge social-ingest > social-draft(edl: Haiku writes the EDL) > repository_dispatch "render"
 GitHub runner (ubuntu-24.04): pinned ffmpeg, render.py, best-frame sheet; signed URLs; callback; NO database key
 Edge social-draft(caption): Haiku 5.5 on 4 frames > frame pick > lint > flags > dispatch "cover" if a frame cover is needed
 runner: cover.html via Playwright > gate > JPEG > callback      then: needs_review > alerts > notify > Posts tab / Telegram
 Hollie: Approve / Reject / Pause all > Edge social-approve (owner JWT; recompute approval_hash)
 pg_cron 5 min > social-publish: lease (skips if paused) > IG container > poll > media_publish; Buffer for TikTok, Pinterest
 pg_cron 10 min > social-comments: poll > ledger > LINK template | classify > draft       weekly/daily > token, metrics, digest
```

| Plane | Runs on | Why (w2g) |
|---|---|---|
| **Control**: queue, state, approvals, clock, publish calls | Supabase pg_cron + Edge Functions (the dashboard's pattern) | Always on. Instagram has no schedule field and containers expire in 24 h, so a cron creates and publishes at post time (V). Meta fetches `video_url` itself; Edge never handles video |
| **Media**: ffmpeg, Playwright | GitHub Actions ubuntu-24.04, started by `repository_dispatch` from Supabase | Edge cannot render: 256 MB, 2 s CPU, 150 s Free / 400 s paid wall clock (V). GitHub's own cron has a 5-minute floor and drops jobs. Private repo, $12 a month included, about $1.44 used (I). Chrome and Node preinstalled, ffmpeg not |
| Not the host | Fedora, Windows | Fedora was off the network 2026-09-26 to 09-29; w2a proved a user-local ffmpeg works there, so it is an optional best-effort host. Windows sleeps: tier 2 manual assist |

Design calls: the runner gets a single-use callback token per job (in `client_payload`, masked, 30-minute life), never a database key; media moves by 1 h signed URLs; a public bucket `social-public` (render and cover only, never raw) is the fallback if Meta rejects signed URLs (SA-21). Raw files carry GPS and device tags, so the raw bucket is private. Reuse the dashboard's `_shared/` helpers (`hmac.ts`, `pushover.ts`, `ntfy.ts`, `hc.ts`, `db.ts`, `claude.ts`) or write them there for it to adopt. New key names: `ANTHROPIC_API_KEY`, `GITHUB_DISPATCH_TOKEN`, `SOCIAL_HMAC_KEY`, `BUFFER_API_KEY`, `IG_USER_ID`; the Instagram token lives in Vault.

## 4. Data model (`0004_social.sql`) [DASH-T1]

Reuses `items` (`status` `draft|active|sold|withdrawn`), `alerts`, `integrations`, `is_owner()`. Design call, from reading `research/dashboard/06` §1.2: two dashboard CHECKs must be widened or inserts fail, and `alerts.dedupe_key` is NOT NULL unique, so every social alert supplies one (`post_review:<post id>:<hash8>`).

```sql
alter table public.alerts drop constraint alerts_kind_check, add constraint alerts_kind_check check (kind in
 ('sold','buy_match','price_drop','stale_listing','oversell_risk','integration_down','token_expiring','digest',
  'post_review','post_failed','reply_review','social_paused'));
alter table public.integrations drop constraint integrations_channel_check, add constraint integrations_channel_check check (channel in
 ('etsy','ebay','shopify','pushover','fedora','instagram','buffer','github','youtube','pinterest'));  -- confirm names with \d
create sequence items_piece_no_seq;       -- the public "piece No."; seeded SKUs are catalog ids (A1, A2...), so the SKU cannot be the number
alter table items add column piece_no int unique default nextval('items_piece_no_seq');
create table social_control (id int primary key default 1 check (id = 1), paused boolean not null default true,
 mode text not null default 'A' check (mode in ('A','B')), max_posts_day int not null default 3,
 max_replies_day int not null default 40, max_usd_day numeric(6,2) not null default 1.00, updated_at timestamptz default now());
insert into social_control default values;                     -- THE KILL-SWITCH ROW: paused = true
create table social_assets (id uuid primary key default gen_random_uuid(), item_id uuid references items(id) on delete set null,
 kind text not null check (kind in ('raw_video','raw_photo','render','cover','still')), storage_path text not null,
 sha256 text unique, bytes bigint, duration_s numeric, has_person boolean not null default false, created_at timestamptz default now());
create table social_posts (id uuid primary key default gen_random_uuid(), item_id uuid references items(id),
 kind text not null check (kind in ('product','mood','gone')),
 platform text not null check (platform in ('instagram','facebook','tiktok','pinterest','youtube')),
 format text not null check (format in ('reel','carousel','image','story','pin','short')),
 status text not null default 'idea' check (status in ('idea','drafting','needs_review','approved','publishing','published','failed','cancelled','blocked')),
 one_liner text, caption text, alt_text text, media_ids uuid[] not null default '{}', cover_id uuid references social_assets(id),
 lint jsonb not null default '{}', risk_flags text[] not null default '{}',
 approved_by text check (approved_by in ('human','rule')), approved_at timestamptz,
 approval_hash text,   -- sha256(caption||alt_text||media_ids||cover_id): any edit voids approval (w2g's hash plus alt text, cover)
 scheduled_for timestamptz, idempotency_key text not null unique,   -- '<post id>:<platform>'
 container_id text, platform_post_id text, permalink text, attempts int not null default 0, last_error text,
 lease_until timestamptz, published_at timestamptz, created_at timestamptz default now());
create table social_comments (id uuid primary key default gen_random_uuid(), post_id uuid references social_posts(id),
 platform_comment_id text not null unique, media_id text, commenter_id text, handle text, body text, received_at timestamptz,
 class text check (class in ('link_request','availability','price','shipping','piece_question','praise','complaint','claim_attempt','spam','other')),
 reply_status text not null default 'none' check (reply_status in ('none','pending_approval','sent','failed','ignored')),
 draft_reply text, public_reply_id text, dm_sent_at timestamptz, replied_at timestamptz);
create unique index one_link_per_person_per_post on social_comments (commenter_id, media_id) where class = 'link_request';
create table social_metrics (post_id uuid references social_posts(id) on delete cascade, captured_on date,
 reach int, views int, likes int, comments int, saves int, shares int, follows int, primary key (post_id, captured_on));
create table social_runs (id bigint generated always as identity primary key, job text, ok boolean,
 tokens_in int, tokens_out int, usd_est numeric(8,5), detail jsonb, at timestamptz default now());
```


**RLS.** Enable on every table; policy `owner_all` using `((select public.is_owner()))`; revoke from `anon`. The PWA reads through RLS and writes only through `social-approve` (owner JWT), because the hash is computed server-side. Edge Functions use the secret key; the runner has none. **Trigger:** when `items.status` leaves `active`, cancel that item's `product` posts in `idea` to `approved` and insert an alert; it works with manual flips, so T3 is optional. Comment classes are w2d's, replacing w2g's shorter list.

**Publish lease** (the dashboard's `skip locked` pattern; `paused` is checked inside the statement so a pause beats a race; the daily cap completes the row's `max_posts_day`, design call):

```sql
update social_posts set status='publishing', lease_until=now()+interval '10 min', attempts=attempts+1
where id=(select p.id from social_posts p, social_control c
          where c.paused=false and p.status='approved' and p.scheduled_for<=now()
            and (select count(*) from social_posts q where q.published_at > now()-interval '1 day') < c.max_posts_day
            and (p.kind<>'product' or exists(select 1 from items i where i.id=p.item_id and i.status='active'))
          order by p.scheduled_for limit 1 for update of p skip locked) returning *;
```

Cron: ingest 5 min; publish 5 min; comments 10 min (posts under 7 days old); sweeper 10 min (stale `publishing`, expired containers, undelivered alerts, jobs silent over 15 min); token weekly; metrics and digest daily.

## 5. Components, in dependency order

Hours are `I`; lane estimates overlap (w2g's whole build: 28 to 35 Claude hours, 3 Codex hours). The kill switch is built second, not last, because publish reads it.

### 5.0 Prerequisites and the no-dashboard fallback

**Ricky, S0, about 3 to 4 h once.** (1) Handles; Instagram Business account; confirm `@holliewoodandvine` is his. (2) Meta developer registration (code to phone and email, https://developers.facebook.com/async/registration), Business-type app (use case Other, https://developers.facebook.com/apps/creation/), Instagram product, owner as tester, **Generate token** (60 days); two spare Instagram accounts for tests, T (tester) and N (not). (3) Buffer Free (https://login.buffer.com/signup) with TikTok (Business account) and Pinterest (Business, desktop signup) connected; API key at https://publish.buffer.com/settings/api. (4) Anthropic key, spend limit about $10 (https://platform.claude.com/). (5) GitHub fine-grained token on this repo, Contents: write; note its expiry. (6) Supabase Pro `hv-desk`, Pushover $4.99, Healthchecks (dashboard §0 rows 4, 6, 8). (7) One real iPhone clip (Most Compatible 1080p30, HDR Video off) and one HDR clip.

**If the dashboard is not built first**

| Marker | Needs | Fallback |
|---|---|---|
| T1 | Pro project with pg_cron, pg_net, Vault; `is_owner()`, `items`, `alerts`, `integrations` | Create the project (Free pauses after a week idle, no backups: not for a publisher). Apply only 06 §1.2's `set_updated_at`, `is_owner`, `items`, `alerts`, `integrations` as `0001_schema_prereqs.sql`; T1 later skips what exists. Seed `items` by hand |
| T3 | automatic `sold` | flip status in SQL; the trigger still cancels posts |
| T4 | `notify`, Healthchecks, token watchdog | `social-notify` (about 60 lines, ntfy only, free); the token job raises its own alert |
| T6 | PWA, OTP login, Posts tab | Telegram bot (inline keyboard, Edge webhook, free) plus ntfy buttons; PWA upload waits |

### 5.1 Schema and RLS: Claude, 1 h [DASH-T1] (w2g §5)
**In** dashboard 0001/0002 or the prereq subset. **Out** §4 applied, cron rows created disabled, `paused = true`. **Done when** owner and non-owner RLS tests pass; both CHECKs accept the new values; the lease leases nothing while paused, one approved due row once, two concurrent callers two different rows, and no `product` post whose item is not `active`; the trigger cancels posts.

### 5.2 Kill switch: Claude, 1 h (w2g §5)
Four layers, fail closed: (1) `social_control.paused` via PWA switch, ntfy `http` button, Telegram command or SQL; (2) repository variable `SOCIAL_ENABLED` plus an `if:` on the workflow; (3) credentials: `cron.unschedule`, delete the Supabase secret, revoke the Instagram token in the Meta App Dashboard; (4) Anthropic org spend limit (drafts then fail with HTTP 400, V). An unreadable control row means no publish. **Interface** `social-approve` actions `pause|resume` (owner JWT or single-use ntfy token). **Done when** pausing between lease and `media_publish` stops the publish; revoking `select` on the row stops publishing; the workflow skips when `SOCIAL_ENABLED=false`; a tiny spend limit sends a post to `blocked`; the phone button pauses in one tap; the README holds the runbook.

### 5.3 Lint: Claude, 2 h (w2g §7, w2f §2, w2a §5)
**In** any text: caption, alt text, hook, end card, cover text, reply template, VLM output. **Out** `{blocked[], flags[]}`. **Interface** `_shared/lint.ts` (`lint(text, ctx)`), CLI `deno run lint.ts <file>`; `render.py` calls the CLI. A block never leaves `drafting` (status `blocked`); a flag forces human review even in B.

| Hard block | Flag (human review) |
|---|---|
| boutique, interior design/designer, visit, in store, in-store, our doors, stop by, showroom, shop floor, "Hollywood" near "Vine" | authentic, signed, original, mint, certified, "from the 19xx", era, material, maker, condition words |
| sold (suggest "Gone"), discount, "% off", offer(s), code, bid, auction, first come, DM to claim, comment to claim, dibs, "every order", "free" near ball | any `$` or digit price; a person's name or handle; mirror or disco ball; "free shipping" |
| `%{` (ffmpeg `drawtext` expands it); a line wider than 950 px; a product post lacking a "piece No." line | |

**Done when** `deno test` shows each term blocking or flagging and clean captions passing. Known conflict: the hire page's "10% off each room after the first" would block (§11 #12).

### 5.4 Ingest: Claude, 2 to 4 h (w1h §1.6, w2g §1)
**In** clips and photos, item id, Hollie's one line. **Out** private objects `social-raw/<date>/<sha256>.<ext>`; `social_assets` rows with `has_person`; a `social_posts` row (`idea`, `one_liner`); a manifest (file, what it shows, real-item id). **Interface** Edge `social-ingest` (cron secret or owner JWT); CLI `tools/social-ingest.mjs <folder>`. **Paths, in order:** (1) Drive share-sheet to the existing folder, pulled with `rclone` on the PC; Fedora cron only if Ricky allows; **conditional on SA-19**; (2) PhotoSync to SFTP if SA-19 fails ($6.49 yearly, V); (3) PWA upload [DASH-T6] after SA-20 (Supabase Free caps files at 50 MB; Pro needed). **Done when** one real clip arrives at recorded resolution, a duplicate is rejected by `sha256`, no raw object is public, and `has_person` blocks automatic approval.

### 5.5 Edit: Claude, 8 to 12 h (w2a §2, §5, tested)
**In** manifest, one line, hook bank (appendix A.1); Haiku writes an EDL: `id, output, fonts{bodoni,dm}, clips[{src,in,out,speed,fit}], hook{lines,size,y,t1}, end_card{dur,lines,sub,credit[]}, music{src,start,fade_in,fade_out,lufs,tp}`. **Out** `render` asset: 1080x1920, H.264 High, AAC 48 kHz stereo, 30 fps, `+faststart`, about -14 LUFS and -1.5 dBTP; a check list; a 6-frame contact sheet (`fps=1/2,scale=360:-1,tile=3x2`) and a caption/credit sidecar, both still to build. **Interface** `python social/pipeline/render/render.py edl.json [--dry]` (env `FFMPEG`, `FFPROBE`); workflow `render.yml`, type `render`. Start from `research/social-2026-10-29/raw/w2a-render.py` (103 lines, stdlib) and `raw/w2a-edl-test1.json`: one ffmpeg command, text via `textfile=`, two-pass linear `loudnorm`, only the music stream mapped.

**Rules.** Constant speed per clip; hook lines pre-broken. HDR tone-mapped with `mobius` (`hable` darkened 25 luma levels, synthetic); capture with HDR Video off. **Scrub is mandatory:** `-map_metadata -1`, `-bsf:v filter_units=remove_types=6`, `sidedata=mode=delete`, `+bitexact` (iPhone files carry GPS and device tags). Music only from the four Kevin MacLeod CC BY 4.0 tracks in `docs/music-and-lights-notes.md`, credited on the end card and in the caption. Not built, not promised: crossfades, stabilisation, ducking, ramps, slo-mo. Speech captions (faster-whisper) are phase 2. Fonts: one instanced set, `wght` 700, `opsz` 12 per w1e (w2a tested 14; rerun SA-17 after the swap). **Runtime:** pinned ffmpeg only (§10), fetched from our mirror by checksum, not `apt` (design call: `apt` was never tested with this script). **Done when** every `check()` line passes on both test EDLs on the runner; a failed check exits non-zero, the post goes `failed`, and nothing reaches Hollie; a real iPhone clip's output has none of `ISO6709`, `Apple`, `com.apple`, `c2pa`, `jumb`, `DigitalSourceType`, `Lavf`, `x264 - core`.

### 5.6 Best-frame pick: Claude, 1 to 2 h (w2b §4, w2f §1)
**In** a clip, the item title. **Out** top-6 contact sheet; chosen frame (ms) for `thumb_offset` or cover source. **Interface** `pick.py clip.mp4`, then a Haiku 5.5 vision call on the sheet (about $0.0008). Stage 1 (ffmpeg `blurdetect`, `signalstats`, Pillow Laplacian: 48 frames in 0.22 s) only drops blur; the two measures agree at Spearman 0.52. Stage 2 is told "show the whole piece, uncluttered, not clipped". **Never** let qwen3.5:4b vote across frames (picked "Frame 1" in both orders, w2f). For a one-piece reveal a deliberate still beats a frame. **Done when** on the walkthrough t=18.0 s ranks top-2 on both measures and the exposure gate is retuned on one real 4K clip (neon and glass trip the "250+" test). Mode B accepts the pick only inside the sharpness top-3.

### 5.7 Cover render: Claude, Codex reviews, 8 to 12 h (w2b §1, §6, tested)
**In** props `{fmt, head, top, bot, photo, focalBox, template}`. **Out** reel cover 1080x1920 and Pin 1000x1500; **JPEG, 9:16, at most 8 MB** for `cover_url` (design call: Pillow converts the PNG); a grid-crop preview; gate result. **Interface** `node social/pipeline/cover/render.mjs props.json`; `cover.html?fmt=reel|pin&...` with w1e's six templates as CSS blocks. Playwright (`playwright-core` 1.64.1) made both sizes in 1.7 s on Fedora; the runner's Chrome is untested (SA-18). Fonts via fonttools (`wght` 700, `opsz` 12) with each `OFL.txt` beside them.

**Gate, same run** (`getBoundingClientRect`): all text and frames inside the hard-safe square x 90 to 990, y 420 to 1500 and the 3:4 crop y 240 to 1680; no overlaps; w1e minimum font and contrast; photo is a listed real item; lint on every string; legible at 129 px in the Pillow preview. **Rules:** selling covers use the original photograph, framed; editorial cutouts (generated pixels) banned; mask-only cutouts allowed with proof (99% or more pixels kept); glass never cut; a focal box per listing (blind `cover` crop once put a wall switch in the cover); no price, discount, "visit" or claim text; templates 1 and 2 stay unposted until real stock. **Fix first:** w1e template 1's top label (y 330 to 375) sits outside its own safe square. **Done when** SA-18 passes.

### 5.8 Caption drafting: Claude, 3 to 4 h [DASH-T6b shares `claude.ts`; key is dashboard §0 row 10] (w2g §2, w2f §2, w3b §1)
**In** four frames at 480x854, the item row (title, era, condition, `ai_notes`), the one line, hook bank, CTA lines (A.4). **Out** `{caption, alt_text, hook_lines, unsupported_claims[]}`; `lint`, `risk_flags`; status `needs_review` or `blocked`. **Interface** Edge `social-draft` (phases `edl`, `caption`): Messages API, `claude-haiku-5-5`, `thinking: {type:"disabled"}`, structured output, signed Storage URL images (base64 fallback), plus a second pass listing unsupported claims. Alt text is for images and carousel images only. The model states colour, shape, count and what is visible; material, maker, age, condition and price come only from the item row or the one line. **Unattended use is an API key, not the subscription.** Caps: org limit about $10; `max_usd_day` read from `social_runs`. Every caption carries "Link in bio, piece No. N" and the music credit. **Done when** a 20-post bench with deliberately bad inputs leaks nothing past lint; `usage` near 3,800 in and 450 out (about $0.0006); a sold item yields "Gone" or a block. Move to `claude-sonnet-5-5` only if titles prove weak.

### 5.9 Approval UX and notifications: Claude, 4 to 6 h [DASH-T4, T6] (w2g §6, w3b §6)
Draft lands, `alerts` row `post_review`, Pushover with cover and `url=/posts/<id>`, Hollie plays the cut, edits the caption, taps **Approve**; `social-approve` verifies the owner JWT, recomputes the hash, sets `approved`. A later edit changes the hash and returns the post to `needs_review`. The page lives on the PWA host: Edge Functions cannot serve HTML without a custom domain (V).

- **Pushover:** the ping, with cover and deep link. $4.99 once; 10,000 messages free; **no action buttons**; Safari versus installed-PWA link is dashboard smoke 12.
- **ntfy:** **Pause all** and the mode B veto ("Posting at 7:07, tap to stop"). Free; `http` actions, up to three, Apple supported per docs source (w3b); token single-use, bound to `approval_hash`, 24 h.
- **Telegram bot:** the whole approval UI if there is no PWA. Free; inline keyboard; clips to 50 MB; needs an Edge webhook.
- **Resend:** daily digest only (free to 3,000 a month). SMS skipped.

**Done when** a push with the cover lands in under a minute; approve sets the hash; an edit after approval returns the post to review; the veto cancels inside its window; a reused ntfy token is refused.

### 5.10 Token refresh job: Claude, 2 h [DASH-T4 pattern] (w2c §1.2, w3d §2.5)
**In** the Vault secret named by `integrations.token_ref` (`instagram`). **Out** a fresh 60-day token written to Vault in the same transaction as `token_expires_at`. **Interface** Edge `social-token`, weekly: `GET graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=...` only when the token is at least 24 h old and unexpired; refresh once it is 30 days old; keep the returned `expires_in`. `token_expiring` alert at day 50; a token not refreshed in 60 days cannot be refreshed again, so a lapse means Ricky regenerates in the App Dashboard. The same watchdog tracks the GitHub dispatch token, the Buffer key, and any Google or Pinterest token added later (Google consent screen in Testing: refresh tokens die in 7 days). Never log a token. **Done when** SA-15 passes and a forced-expiry drill raises the alert.

### 5.11 Publish adapters: Claude, 11 to 13 h Instagram+Facebook, 3 to 4 h Buffer [DASH-T1] (w2c §1.1, §4, §8; w3a §4; w3d §2.6)
**Interface** `social-publish` leases a post (§4), picks the adapter by `platform`, returns `{platformPostId, permalink}`; `preflight()` returns blockers (paused, item not active, hash changed, cap reached).

| Platform | Default path | Flow and limits |
|---|---|---|
| **Instagram** | Own API: Instagram Login, Business-type app, Standard Access, no App Review, no Facebook Page | `GET /content_publishing_limit`; `POST graph.instagram.com/v26.0/<IG_ID>/media` (`media_type=REELS`, `video_url`, `caption`, `cover_url`, `share_to_feed`, `collaborators` up to 3); poll `status_code` each minute up to 5; `POST /media_publish`. Plan for **50** a day (reference; the guide says 100), 400 containers. Images JPEG with `alt_text` (1,000 chars, not Reels); carousels up to 20; Reels H.264/HEVC + AAC, 23 to 60 fps, 3 s to 15 min, 300 MB. No `location_id`, no `is_ai_generated` on real photos, no Story stickers |
| **Facebook** | IG-to-FB cross-post toggle (free) | API adapter (Page token, `pages_manage_posts`, `publish_video`, `published=false` + `scheduled_publish_time`, 10 min to 30 days) only for FB-specific copy |
| **TikTok, Pinterest** | Buffer Free (3 channels, 10 queued posts each) | GraphQL `https://api.buffer.com`; MCP `https://mcp.buffer.com/mcp`; 150 requests per 15 min, 600 per day. hand-off at post time through the lease, both modes (approval already happened in our Posts tab): `createPost` with `schedulingType: automatic`, `mode: customScheduled`, `dueAt` a few minutes ahead, public HTTPS media. That keeps each queue under Free's 10-post cap. Anything Buffer forces to Notify Me (Story stickers, post music, product tags) stays a human tap. **No custom cover**: `metadata.thumbnailOffset` only; burn the cover into frame 1. Pinterest needs `boardServiceId` and the piece URL per Pin. Public TikTok is a vendor claim until SA-1 |
| YouTube Shorts | native now; own API later | `videos.insert` with `status.publishAt`, 100 calls a day, consent screen In production; Shorts thumbnails need Studio on a computer |

**Do not build** TikTok or Pinterest own-API adapters, or Threads. **Idempotency:** on a stale `publishing` lease, look first: read the container `status_code`, list recent media for the caption; never blind retry. **Done when** SA-3 passes; killing the function between `media_publish` and the write ends with one post; paused creates no container; a sold item cancels the post.

### 5.12 Piece pages and link-in-bio: Codex, then Ricky publishes, 3 h (w2d §1, round-d gating fact)
Route A needs one real URL per piece. Today items are `#item-<id>` hash routes in a dialog and Google indexes the page, not the fragment (`docs/codex-handoff-idea-room.md` §8.3 `idea-own-page.html`, mocked at `/pieces/<slug>`). **In** catalog and `items` (the public piece number is `items.piece_no`). **Out** `/pieces/<slug>` plus a number lookup `/p/<n>`, both HTTP 200 after the piece sells, labeled "Gone"; a link-in-bio page listing pieces by number, Here or Gone. **Done when** a `site/tests/` test (Fabulous-test style) shows every piece resolves and the wording guardrails hold (no "Hollywood", no showroom words, no checkout claim while checkout is "coming soon"), and Ricky has published. **Lands before any `product` post is unpaused.** Gap: `git push` does not deploy, so the site's "Gone" can lag `items.status`; the reply handler reads `items.status`, never the site.

### 5.13 Reply handler: Claude 10 to 16 h, Codex 3 to 4 h review [DASH-T1, T4, T6] (w2d §7, §9; w3d §3)
```
poll GET /<media>/comments, posts under 7 days old (50 per query, top level, no timestamp filter), every 10 min
 -> ledger row BEFORE any send (unique comment id; unique commenter+media for link requests)
 -> whole-word "link" alone: piece No. -> items.status
      active: one fixed public reply + one private reply (POST /<IG_ID>/messages, recipient.comment_id), URL only
      else:   the fixed "Gone" public reply, no DM
 -> otherwise Haiku 5.5 returns a label -> draft in the approval queue | hide (high-confidence spam, logged) | nothing
```
Comment text is data: the classifier returns a label; the LINK reply is a template, never model text; no tools in this path. Non-LINK drafts use Haiku 5.5 by default (about $0.01 a month, w2g); Sonnet 5.5 would add about $0.78 (w2d) and is opt-in for tone. No auto-retry of failed sends; never reply to our own account; do not spend the one private reply on a Gone piece. **Gate (w3d, unresolved):** webhooks need Live mode, Advanced Access and Business Verification (a legal entity); whether polling returns non-role commenters and whether a private reply works at Standard Access are decided only by SA-10 to SA-14. If they fail and there is no entity: Hollie replies by hand (Saved Replies), or a third-party tool holds the approved app for LINK only (InstantDM Legend Pro $9.99 a month billed yearly; ManyChat Essential $14; neither has an approval queue). Pre-launch: "Hollie is still building the shop. The first real drop is announced here first." Do not enable Meta Business Agent (it advertises "Close sales"; if it owns a thread our sends fail). **Done when** the SA-10 to SA-14 outcome is recorded, a redelivered comment sends once, a Gone piece gets no DM, and nothing on §6's Reply row auto-sends.

### 5.14 Analytics sheet: Claude, 3 to 4 h [DASH-T1; digest T4] (w2e Analytics; w2g §5)
Daily rows in `social_metrics` from Instagram insights; a weekly view `social_weekly` (posts, reach, saves, shares, follows, comments, LINK requests) and the digest alert. Metric field names are not in the lane reports: crawl the live insights reference first. UTM tags on piece links; Umami (MIT) is optional and out of v1. Changing the calendar is a human call.

## 6. Approval modes

A: nothing publishes without a tap. B: the pipeline posts on schedule, answers LINK, drafts the rest. `social_control.mode` picks; B only after 10 posts in A. In B a lint-clean template post with no risk flag is set `approved_by='rule'`, waits behind a ten-minute veto push, and Pause all is always one tap.

| Stage | A: human taps | B: automatic | Always human |
|---|---|---|---|
| Ingest | share clips, write the line, set `has_person` | same | any frame with a person, or Hollie in a mirror |
| Edit | preview cut and sheet | render passes every check, manifest clips, bank hook, cleared music | music outside the four tracks; a hook naming price, age, era, material or condition; speech text with dates or numbers |
| Frame, cover | view | template passes the gate; frame pick inside sharpness top-3 | new cover styles; any copy on a cover; Hollie's face |
| Caption | edit, approve | template plus item facts, lint clean, no flags | price, condition, age, maker, provenance, any person, any fixed-constraint word, any ball mention |
| Publish | tap Approve | `mood` and template product posts that pass lint | any flag; first 10 posts; `gone` posts; Story link stickers; collab drops; `is_ai_generated`; going Live on Meta |
| Reply | approve each draft | LINK template for a Here piece; "Gone" public reply; logged spam hides | all else: complaints, refunds, safety or electrical, price talk, condition or provenance beyond the listing, any reply once a person answers a DM, named people, collab or press, low confidence, links or media in a comment |
| Analytics, tokens | n/a | automatic | calendar changes; unpausing; regenerating a token; Meta app changes |

LINK in B also needs SA-10 to SA-14 passed, real stock and Ricky's disclosure answer. B reverses the dashboard's "no auto-publish" rule for social (§11 #7).

## 7. Smoke tests

SA-n, to avoid the dashboard's 1 to 14. Record each in `research/social-2026-10-29/smoke-<date>.md`: call, status, fields, never a token. T and N are the two spare Instagram accounts (T is a tester, N is not). Sources in brackets.

- **SA-1** **TikTok via Buffer Free** [w2c §6]: one public TikTok through a Business account; view logged out; if it fails, repeat via Upload-Post or Zernio. Pass: the scheduler path holds a public TikTok.
- **SA-2** **Buffer cover** [w2c §6]: a Reel via API with `thumbnailOffset`; look for a custom cover in the composer. Pass: decides burned-in cover versus own API.
- **SA-3** **Instagram own API** [w2c §6]: a Reel with `cover_url`, an image with `alt_text`; view logged out (run with SA-9). Pass: Development posts are public, cover works.
- **SA-4** **YouTube** [w2c §6], if built: one unlisted upload from an unverified project. Pass: not private-locked.
- **SA-5** **Pinterest** [w2c §6], if built: time from Trial request to approval.
- **SA-6** **Haiku image URL** [dashboard smoke 14]: a signed Storage URL as image source; log `usage`. Pass: works (else base64); tokens near estimate.

**The one-hour Meta test** [w3d §3], SA-7 to SA-15:

- **SA-7** Create the Business-type app (use case Other), add Instagram, add the owner, accept the invite. Is a mode toggle or Go live shown? Is Business Verification demanded?
- **SA-8** Generate a token; read `content_publishing_limit` (50 or 100).
- **SA-9** Publish a Reel with `cover_url` and `collaborators` via graph.instagram.com, an image with `alt_text`, a Trial Reel (expect refusal under 200 followers); view each logged out from N.
- **SA-10** Subscribe `comments` via `/subscribed_apps`. Comment from T, then N. Compare the dashboard Test button. Which fire?
- **SA-11** Poll `GET /{media}/comments`. Is N's text returned?
- **SA-12** Reply to, hide and delete a comment by API.
- **SA-13** Private-reply T's, then N's comment. Record error codes. Is the link tappable in Requests?
- **SA-14** N sends a DM. Does the messaging webhook fire? Does a reply inside 24 h send?
- **SA-15** Refresh the token under 24 h old (expect refusal), then after.

Decision rule: N works everywhere, no entity needed. Only T works: customer automation needs Live mode and an entity; fall back to polling plus API replies if SA-11 passes, or a third-party tool.

**Build-specific tests**

- **SA-16** **AI-info export test** [w2a, w1a]: export one reel from our render and one from Edits; `ffprobe -show_format -show_streams` plus the byte scan (`BAD` in `w2a-render.py`); post one test reel. Pass: no GPS, device or C2PA marker; no "AI info" label.
- **SA-17** **ffmpeg pin test** [w2a, w3b]: download the pinned URL; `sha256sum` equals `8d02a412b0f72051bf30201a9f2c117fe557a4dc44b03c5c99fda2fbd7b00b5d`; list decoders `h264`, `hevc`, `aac`, encoder `libx264`, filters `drawtext`, `ass`, `zscale`, `tonemap`, `loudnorm`, `ebur128`, `sidedata`; run `render.py` on both EDLs. Repeat on the runner image. Pass: every `check()` line passes on Fedora, Windows and the runner (the build links system `libm`).
- **SA-18** **Cover render test** [w2b §1]: render both formats; zoom "Open." against `raw/w2b-test/zoom-type.png`; run the gate; export JPEG. Pass: under 3 s on the runner (1.7 s on Fedora), hairlines intact, gate passes, JPEG 9:16 and at most 8 MB.
- **SA-19** **Drive-resolution test** [w1h]: share one fresh clip (Most Compatible, 1080p30) to the Drive folder; `rclone` it; `ffprobe`. Pass: size and codec equal the recorded file; else PhotoSync.
- **SA-20** Upload one phone video from Safari through the PWA [DASH-T6] [w2g §11]. Pass: recorded quality kept.
- **SA-21** One container call with a Supabase signed URL as `video_url` [w2g §11]. Pass: Meta accepts it; else `social-public`.

## 8. Failure modes and guardrails

| Failure | Guardrail |
|---|---|
| Double post | unique `idempotency_key`; lease; look before re-publishing; caps well under 50 |
| Token lapse (Instagram; GitHub dispatch token) | 5.10 alert at day 50; a lapse means manual regenerate |
| Bad caption; sold item still advertised; no stock yet | lint before approval; lease needs `active`; trigger cancels; `paused=true`; `gone` human-only; site lag never drives replies |
| Prompt injection, reply loop, spent private reply | label-only classifier; template replies; ledger before send; stock check first |
| Runaway spend | `max_usd_day`; org limit; thinking disabled; `--max-budget-usd` and `--max-turns` on any `claude -p`; alert above $12 runner spend |
| Render drift, dead runner, expired URL | §10 pin; SA-17 on the runner; sweeper alert after 15 min; Healthchecks per lane; `if: failure()` to ntfy; URLs minted late |
| Another automation owns the thread (error 2534037); Buffer 150 requests per 15 min | one automation per account; back off |
| Person on camera; GPS in raw files | `has_person` blocks approval; raw bucket private; output scrubbed |
| "Comment LINK" read as engagement bait | link also always in bio; check Account Status after 30 days (I) |

## 9. Cost at the reference load

One brand; about 22 Instagram/Facebook posts, 13 TikToks, 13 Pins, 48 renders, 130 comments a month. Read 2026-10-29.

| Line | With the dashboard's Pro project | Standalone |
|---|---|---|
| Anthropic API (Haiku 5.5 $0.10 in / $0.50 out per MTok; weekly Sonnet 5.5 plan $2 / $10) | about $0.27 ($2.69 at 10x); w2d's looser guesses reach about $1 | same |
| Supabase | $0 marginal | $25 (Pro) |
| GitHub Actions | $0: about 240 minutes, $1.44 of $12 included ($14.40 at 10x) | $0 |
| Pushover | $4.99 once | $4.99 once |
| ntfy, Healthchecks, Resend, Telegram | $0 | $0 |
| Buffer for TikTok and Pinterest | Free $0; Essentials ($5 per channel yearly, $6 monthly) only for more channels or an unlimited queue | same |
| Reply tool, only if SA-10 to SA-14 fail with no entity | $9.99 or $14 a month, billed yearly | same |
| **Total** | **about $0.27 a month** | **about $25.27** |

Claude Pro ($17 yearly-billed, $20 monthly) and Codex Plus ($20) are for building, already owned.

## 10. Corrections to carry

| Correction | What the build does |
|---|---|
| BtbN's daily tag `autobuild-2026-10-28-19-47` expires about 2026-11-11 | Pin the month-end `autobuild-2026-09-30-13-08` (`ffmpeg-n8.1.3-9-g29e619e767-linux64-gpl-8.1.tar.xz`, 150,360,944 bytes, API digest `sha256:97ce9789...0dbb79`, not yet downloaded) **or mirror the tested tarball (152,135,596 bytes, sha256 `8d02a412...00b5d`) to private Storage and fetch it by checksum**. Never `latest`. GPL build, internal use |
| Haiku 5.5: $0.10 / $0.50 holds to 100K-token prompts ($0.50 / $2.50 above); 4.7 and later models emit about 30% more tokens | Prompts are about 4K; token counts here are `I`, log `usage` |
| `claude --bare -p` refuses the subscription login (and the setup-token); non-bare `-p` with `CLAUDE_CODE_OAUTH_TOKEN` works, but Anthropic says products use API keys | Runtime drafting is a Messages API call with an API key; subscriptions are for building; cloud scheduled tasks run hourly at most |
| HyperFrames telemetry is on by default; Remotion's license counts employees (3), contractors from 5.0 | Neither in v1. If HyperFrames: `hyperframes telemetry disable` or `DO_NOT_TRACK=1` |
| Buffer cannot upload custom covers | Burn the cover into frame 1, or own-API `cover_url` |
| TikTok own-app posting is private-only (`SELF_ONLY`, 5 users per 24 h); its guidelines call an upload utility for your own accounts "not acceptable" | Scheduler or TikTok Studio; never build the adapter |
| Meta webhooks versus Live mode is unresolved ("Live", Business Verification, Advanced Access versus "Business apps do not have app modes"); "own pages need no review" does not cover comment webhooks (wiki to correct) | SA-7 to SA-14, the one-hour test; until then assume customer-triggered automation needs an entity |
| Smaller corrections, applied above | Instagram cap 50 not 100 (5.11); ntfy `http` on Apple (5.9); GitHub states $12, not "2,000 minutes" (§3); Buffer Essentials $6 / $5 per channel, Metricool Starter not flat $20, ManyChat API Advanced only, CommentChat no standalone price (§9, 5.13). **Still open:** `collaborators` "Facebook Login for Business only" (SA-9), Buffer carousel 10 versus 20, Buffer TikTok Business-account rule (SA-1) |

## 11. Open decisions and defaults

| # | Decision | Default | Blocks |
|---|---|---|---|
| 1 | Approve everything (A) or by exception (B)? | **A**; B on Ricky's word after 10 posts | B |
| 2 | Is there, or will there be, a legal entity? | **No.** Live mode and webhooks unavailable; replies by hand | reply automation |
| 3 | `social/` in this repo, or a dedicated private repo (structure change, Ricky's word)? | **This repo**, sparse checkout (132 MB). A dedicated repo shrinks the dispatch token's blast radius | S0 token |
| 4 | May any step run on the Fedora box? The dashboard says "not in v1" | **No**; GitHub runner only | Fedora cron |
| 5 | Runtime Anthropic key with a $10 limit, subscriptions kept for building? | **Yes** | drafting |
| 6 | One automated-message line on private replies versus "nothing else"? | **Route B stays by hand** | LINK automation |
| 7 | B reverses the dashboard's "Do not build": any auto-publish path, anything on Fedora in v1, "Facebook anything". Scope it | Social is separate; the dashboard rule stands for selling | B, Fedora, FB adapter |
| 8 | Is `@holliewoodandvine` Ricky's? | unknown | accounts |
| 9 | Hire page's "10% off each room after the first" versus no discounts | lint blocks copying it; Ricky decides the page | hire posts |
| 10 | Smaller calls | Hollie hands-only with a `has_person` flag; music credit on end card and caption; GitHub Free; both `/pieces/<slug>` and `/p/<n>`; "Gone" stamp `#e5a6b4` | none |

## 12. What not to build

- Unofficial Instagram/TikTok libraries (instagrapi, instagram-private-api, cookie-based TikTok uploaders): ToS violation, ban risk to the one brand account. Not tested, not installed.
- Our own TikTok app; Pinterest or YouTube own-API adapters in v1; Threads.
- Postiz or Mixpost self-host; n8n, Make, Zapier or Chatwoot as a second plane.
- AI video, B-roll, avatars or voices; generative music (MusicGen is non-commercial); super-resolution on listing photos; `briaai/RMBG-2.0` (non-commercial; never run `rembg` without `-m`).
- CommentSold-style claim or auction tools, Meta Business Agent, follow-gating, a bare URL as the only reply, anything tying the mirror ball to engagement.
- qwen3.5:4b as a frame decider; Satori with blurred shadows in Edge; Vercel Hobby for a commercial endpoint; Story link stickers by API; `location_id`; `is_ai_generated` on real photos; Umami, Remotion, HyperFrames in v1.

**Definition of done for v1.** §7 results recorded; one Reel goes from phone clip to public Instagram with the designed cover, in A, kill switch tested; the first 10 posts reviewed in A; `social_control` shipped paused; piece pages published before any product post; `CLAUDE.md` status line updated; smoke-test file and this handoff's outcome `/compile`d into the desk wiki.
