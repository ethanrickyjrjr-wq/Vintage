# w2g: where the autopilot runs, how it is orchestrated, how Hollie approves, who builds it (Holliewood & Vine)

Lane w2g-runtime, accessed 2026-10-29. Raw captures: `research/social-2026-10-29/raw/w2g-*.md` (42 kept, 2 walls deleted). Budget used: 44 crawls, 2 WebSearch, 5 `gh` calls. No signups, logins, posts or tests run. **w2a's Fedora ffmpeg result was not in the folder when I finished (only its raw captures exist), so I cite nothing from it; section 4 says what its result would change.**

Tags: `verified` (read live this session), `verified (w2c|w2d|w1x)` (sibling lane's capture of the same date, which I read), `verified 10-26 (dashboard 05)` (carried over from `research/dashboard/05`, three days old), `vendor claim`, `unverified (search)`, `inferred`.

## TL;DR

1. **Two planes.** Control plane (queue, state, approvals, clock, publish calls) = Supabase pg_cron + Edge Functions, the dashboard's pattern. Media plane (ffmpeg, Playwright) cannot run there: 256 MB, 2 s CPU, 150 s Free / 400 s paid wall clock `verified` (https://supabase.com/docs/guides/functions/limits). Meta fetches `video_url` itself, so Edge never touches video bytes `verified (w1a)`.
2. **Media plane = a GitHub Actions ubuntu-24.04 runner started by `repository_dispatch` from Supabase**, not GitHub's own cron (5-minute floor, dropped jobs `verified 10-26`). Repo is private (`gh api`); GitHub Free includes **$12/month = 2,000 Linux minutes at $0.006** `verified`; the load needs about 240 min, $1.44 (`inferred`). The image has Chrome 156, Node 22, Python 3.12 and **no ffmpeg listed**: `apt-get install ffmpeg` `verified`.
3. **Fedora is not the render host unless w2a proves it, and then best-effort only** (box off the network 2026-09-26 to 09-29, desk wiki). Windows is tier 2's manual-assist machine (it sleeps).
4. **Runtime drafting = Claude Haiku 5.5 API, $0.10 in / $0.50 out per MTok:** about $0.0006 a caption, **about $0.27 a month** with a weekly Sonnet plan (`inferred` tokens, `verified` prices). Caching and Batch are irrelevant. API key for unattended runs, subscriptions for building.
5. **Claude vs Codex:** Claude builds pipeline, schema, Edge Functions, PWA tab, tests; **Codex builds the site pages and Ricky publishes them** (ChatGPT Sites publishes only through the Codex/ChatGPT app).
6. **Approval:** Pushover ($4.99 once, the dashboard's choice) pings with the cover and deep-links to a **Posts tab in the PWA**; ntfy `http` buttons (up to 3) give one-tap **Pause all**. Pushover has no action buttons. Edge Functions cannot serve HTML without a custom domain `verified`.
7. **Kill switch:** one row, `social_control.paused` (default true), checked inside the lease SQL; four layers (section 5).
8. **Reply automation may not work without a legal entity.** Comment webhooks need Advanced Access (Business Verification) `verified (w2d)`; polling is the fallback, but whether a Development-mode app returns *customers'* comments is `unverified` (w2d), and w2c keeps the app in Development mode until an entity exists. One throwaway test decides. Publishing is unaffected.
9. **n8n, Make and Zapier replace only the control plane** Supabase already gives; none renders video. n8n self-hosted is $0 and its licence allows internal business use.
10. **Two collisions for Ricky:** the dashboard handoff forbids "any auto-publish path" and "anything on the Fedora box in v1"; B mode and a Fedora render touch both. The dashboard is *designed, not built*; tier 3 stands on its schema, `notify` and PWA.

## 1. Architecture (tier 3)

```
Phone: shoot > share to Drive/PWA upload > Supabase Storage (Pro: no 50 MB cap)
  pg_cron 5 min  > Edge social-ingest   > repository_dispatch (fine-grained token, Contents: write)
  GitHub runner (ubuntu-24.04): apt ffmpeg; render 1080x1920 H.264+AAC faststart; Playwright cover; upload via signed URL;
                                POST job-scoped callback (HMAC) to Edge. No database key on the runner.
  Edge social-draft : Haiku 5.5 (frames + item facts) > lint > risk flags > status needs_review > alerts row
  notify (existing) : Pushover (+cover image, url=PWA /posts/<id>) > ntfy fallback        <-- Hollie's phone
  PWA Posts tab     : preview, edit, Approve / Reject / Pause all                          (RLS: is_owner())
  pg_cron 5 min  > Edge social-publish : lease approved post (skips if paused) > IG container > poll status_code > media_publish
  pg_cron 10 min > Edge social-comments: poll comments < 7 days old > classify > "LINK" template reply | draft for approval
  pg_cron daily  > token watchdog, metrics, digest, Healthchecks pings
```

The Instagram API has no schedule field and containers expire after 24 h, so a cron must create *and* publish at post time. `verified (w2c M1)`. **Caveat:** the comments poll may see only role accounts' comments until a legal entity exists (TL;DR 8); publish does not depend on it.

## 2. Claude side (`verified` 2026-10-29 unless tagged)

| Surface | Limits that matter | Auth and billing | Fit here |
|---|---|---|---|
| **Scheduled tasks** (ex-routines, research preview) https://code.claude.com/docs/en/routines.md. Cloud Claude Code session, Ubuntu 24.04; triggers: schedule, API `/fire` (beta header), GitHub | **Not more often than hourly**; on-the-hour runs start minutes late; 100 scheduled runs/h per account. Default network allowlist (has api.anthropic.com, archive.ubuntu.com); Supabase/Meta need Custom or Full. Auto mode. Env vars visible to environment users: use network secrets | Draws subscription usage; rejected over the limit unless usage credits. Actions "appear as you" | Weekly plan/review only |
| **Headless `claude -p`** https://code.claude.com/docs/en/headless.md | `--max-budget-usd`, `--max-turns`. **`--bare` never uses the subscription login, it needs `ANTHROPIC_API_KEY`** | Login or key | Tier 2 on Windows. Fedora already has Claude Code (v2.1.270, wiki) |
| **GitHub Action** https://github.com/anthropics/claude-code-action (MIT, 9,704 stars, pushed 2026-10-27) | `--max-turns` | `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` (`claude setup-token`) | CI review of pipeline PRs, not rendering |
| **Agent SDK** | n/a | Docs: use API-key auth; no claude.ai login for third parties | Not needed: drafting is one Messages call |
| **Messages API** | Org spend limit editable; at the limit, HTTP 400 "You have reached your specified API usage limits" (https://platform.claude.com/docs/en/api/rate-limits.md) | Console key | The runtime brain |

**Prices** (https://platform.claude.com/docs/en/about-claude/pricing, `verified (w2d capture 13:46)`; caching page `verified`): `claude-haiku-5-5` $0.10 in / $0.50 out per MTok (prompts up to 100k), cache read $0.01, Batch $0.05 / $0.25, minimum cacheable prompt 512 tokens. `claude-sonnet-5-5` $2 / $10 (Batch $1 / $5). The dashboard research's IDs and prices (2026-10-26) still hold.

| Job (reference month: about 48 renders, 130 comments; token counts `inferred`) | In / out | Model | Each | Month |
|---|---|---|---|---|
| Caption draft: system 1,200 + facts 300 + 4 frames at 480x854 (2,232), 2 tries | 3,800 / 450 | Haiku 5.5 | $0.0006 | $0.058 |
| Claims QA pass | 1,500 / 200 | Haiku 5.5 | $0.00025 | $0.012 |
| Comment classify (130) | 700 / 40 | Haiku 5.5 | $0.00009 | $0.012 |
| Draft replies (about 50 non-LINK) | 1,200 / 150 | Haiku 5.5 | $0.0002 | $0.010 |
| Weekly plan (4.33) | 8,000 / 2,500 | Sonnet 5.5 | $0.041 | $0.178 |
| **Total** | | | | **about $0.27; $2.69 at 10x** |

Caching saves about $0.0001 a call and its 5-minute life lapses between posts; Batch halves cents. **Neither is worth the code;** the org spend limit (about $10) plus a daily budget row is the control that matters.

**Subscription vs API.** Pro is $17/month billed yearly ($200 up front) or $20 monthly, Max from $100, Claude Code included (https://claude.com/pricing); Anthropic's legal page says OAuth is for "ordinary use", advertised limits "assume ordinary, individual usage", and products should use API keys (https://code.claude.com/docs/en/legal-and-compliance.md). **Need review whether an unattended shop pipeline counts; I recommend an API key for anything unattended and the subscription for building.**

## 3. Codex side and the three splits

| Surface | Facts (`verified` 2026-10-29, https://learn.chatgpt.com/docs/...) | Fit here |
|---|---|---|
| `codex exec` | Read-only sandbox default; `--sandbox workspace-write`; `--json`, `--output-schema`; auth by saved login or `CODEX_API_KEY` per call; ChatGPT-managed auth in CI is "advanced", not for public repos | Scripted changes, not a runtime |
| `openai/codex-action@v1` (Apache-2.0, 1,285 stars, pushed 2026-10-20) and Codex Cloud | API-key secret; Linux/macOS runners; cloud tasks from GitHub repos | Review gate, build work |
| Scheduled tasks | Desktop: "keep the computer on and the app running"; web tasks have no local folder; CLI has no scheduler | Not the production scheduler |
| Plans | Free $0, Go $8, **Plus $20**, Pro $100/$200/$500; API-key mode is pay-per-token, no cloud features. Plus local messages per 5 h vary by model (GPT-6.1 Sol 15-160); weekly limits may apply | Plus already owned |
| API price | `gpt-6-luna` $0.10 / $0.50 per MTok, **same as Haiku 5.5** (https://developers.openai.com/api/docs/pricing). GPT-5.5 left Codex sign-in on 2026-10-14 (model churn: pin IDs) | Price does not decide the split |
| **Sites** | "describe the changes ... save a version, and deploy it"; has D1, R2, Sign in with ChatGPT. Repo memory (2026-10-26): `git push` does not deploy, Codex CLI 0.164 had no deploy command, Ricky publishes via the Codex app (`inferred` stale: re-check) | Public pages only |

| Split | Who does what | Wins when | Loses when |
|---|---|---|---|
| **Claude only** | Claude builds all and specs the site; Ricky pastes Codex prompts to publish | Fewest parts | Per-piece URLs and link-in-bio cannot go live without Codex/Ricky, so "only" is false |
| **Codex only** | Codex writes Deno/SQL/PWA; drafting on gpt-6-luna | One subscription | Repo, tests and dashboard design are Claude-first; one vendor builds and drafts; Codex tasks need the app open |
| **Named split (recommended)** | **Claude:** migration, lint, Edge Functions, render, workflow, PWA tab, tests, runtime drafting. **Codex:** `site/` pages `/p/<n>` and link-in-bio from a handoff spec; Ricky publishes. **Ricky:** accounts, tokens, shoot, taps | Matches the repo's `docs/codex-handoff-*.md` habit | Two tools; the spec file is the contract |

An approval page on Sites (D1 + Sign in with ChatGPT) is possible but splits state from Supabase, needs a Supabase secret inside Sites (storage of secrets there: not read) and a Ricky publish per change. Rejected.

## 4. Runtimes

| Runtime | Cost at the reference load | Always-on | ffmpeg / Playwright | Secrets | Failure alert | Wins when |
|---|---|---|---|---|---|---|
| **Supabase** pg_cron + Edge + Storage + Vault | **$0 marginal** if the dashboard's Pro project exists; Pro $25 standalone (`verified 10-26`); Free $0 pauses after a week idle, no backups. About 13,000 Edge calls/month (`inferred`) vs 2M included. Storage Free 1 GB, Pro 100 GB then $0.0213/GB-mo `verified`; file cap Free 50 MB, Pro up to 500 GB `verified (w1h)` | Yes; pg_cron seconds to yearly, 8 concurrent jobs of 10 min `verified 10-26` | None (2 s CPU, 256 MB) | Edge secrets (100 max, 48 KiB) + Vault for the rotating Instagram token | `cron.job_run_details`; Healthchecks (free, 20 jobs) | Control plane, always |
| **GitHub Actions** | **$0** inside $12 included (about $1.44 used; 10x = $14.40, $2.40 over). Checkout of Vintage is 132 MB: sparse checkout or a small runner repo | On call. Own cron: 5-min floor, drops, public repos disabled after 60 idle days `verified 10-26` | Chrome 156, Chromium, Node 22, Python 3.12; **ffmpeg not listed**, apt works `verified` | Repo secrets: callback secret only, **never the Supabase secret key** | `if: failure()` posts to ntfy; Supabase flags a job stuck after 15 min | Media plane |
| **Fedora box** | $0 | Off-network 3 days in Sept (wiki); systemd `Persistent=true` catches up missed `OnCalendar=` runs `verified` | **Unknown until w2a**; stub ffmpeg cannot decode phone video (BRIEF) | Mode 600 file | Unit failure to ntfy (`inferred`); a check on the box dies with the box | Optional ingest (`rclone`). If w2a passes: free render host with GitHub as fallback |
| **Windows PC** | $0 | Sleeps; "Wake the computer to run this task" fails when Windows hibernates `unverified (search)` (Microsoft page walled) | Local ffmpeg works (BRIEF) | `.env.local` | None | Tier 2, Ricky at the PC |
| **Cloudflare** Workers/R2/Containers | Workers Paid $5; Containers include 25 GiB-h and 375 vCPU-min, enough for 50 short renders (`inferred`); Workers CPU 10 ms Free, 30 s default Paid; R2 10 GB free (w1h) | Yes | ffmpeg only in a Container: untested, about 15 h to build | Wrangler secrets | Worker logs | GitHub minutes run out, or one vendor wanted |
| **n8n** | Self-hosted $0; licence: "your own internal business purposes" `verified`. Cloud Starter 20 EUR/mo billed yearly (2.5K executions), Pro 50 EUR (10K); a 30-minute comment poll plus 48 posts and 130 replies is about 1,600 executions `inferred` | Cloud yes; self-host = Fedora caveat | No ffmpeg in the cloud | n8n credentials | Error workflow | Visual canvas wanted; a **second** control plane |
| **Vercel / Make / Zapier / Claude scheduled task** | Vercel Hobby is non-commercial and cron is once a day, +-59 min `verified`, Pro $20; Make Core about $9-12 (10,000 credits, sources disagree `unverified (search)`; a poll costs a credit); Zapier from $19.99 (webhooks need Professional; about 800 tasks/month); Claude task $0 marginal | Yes (scheduled task: hourly floor) | None | Vendor stores | Email / run history | None beats Supabase for this job; Claude task for the weekly plan only |

**No-code tools replace only the control plane Supabase already gives for $0; none replaces the media plane.**

## 5. State, queue, kill switch, logging

Extend the dashboard's schema (migration `0004_social.sql`). Reuse `items` (its `status` is `draft|active|sold|withdrawn`), `alerts` (add kinds `post_review`, `post_failed`, `reply_review`, `social_paused` to its CHECK), `integrations`, `is_owner()` and `notify`.

```sql
create table social_control (id int primary key default 1 check (id = 1),
  paused boolean not null default true, mode text not null default 'A' check (mode in ('A','B')),
  max_posts_day int not null default 3, max_replies_day int not null default 40,
  max_usd_day numeric(6,2) not null default 1.00, updated_at timestamptz not null default now());
create table social_assets (id uuid primary key default gen_random_uuid(), item_id uuid references items(id) on delete set null,
  kind text not null check (kind in ('raw_video','raw_photo','render','cover','still')), storage_path text not null,
  sha256 text unique, bytes bigint, duration_s numeric, has_person boolean not null default false, created_at timestamptz default now());
create table social_posts (id uuid primary key default gen_random_uuid(), item_id uuid references items(id),
  kind text not null check (kind in ('product','mood','gone')),         -- product needs an active item
  platform text not null check (platform in ('instagram','facebook','tiktok','pinterest','youtube')),
  format text not null check (format in ('reel','carousel','image','story','pin','short')),
  status text not null default 'idea' check (status in ('idea','drafting','needs_review','approved','publishing','published','failed','cancelled','blocked')),
  caption text, alt_text text, media_ids uuid[] not null default '{}', cover_id uuid references social_assets(id),
  lint jsonb not null default '{}', risk_flags text[] not null default '{}',
  approved_by text check (approved_by in ('human','rule')),
  scheduled_for timestamptz, approved_at timestamptz, approval_hash text,  -- sha256(caption||media_ids): edit after approval voids it
  idempotency_key text not null unique,                                    -- '<post id>:<platform>'
  container_id text, platform_post_id text, permalink text, attempts int not null default 0, last_error text,
  lease_until timestamptz, published_at timestamptz, created_at timestamptz default now(), updated_at timestamptz default now());
create table social_comments (id uuid primary key default gen_random_uuid(), post_id uuid references social_posts(id),
  platform_comment_id text not null unique, handle text, body text, received_at timestamptz,
  class text check (class in ('link_request','question','praise','complaint','spam','other')),
  reply_status text not null default 'none' check (reply_status in ('none','pending_approval','sent','failed','ignored')),
  draft_reply text, replied_at timestamptz);
create table social_runs (id bigint generated always as identity primary key, job text, ok boolean, tokens_in int, tokens_out int,
  usd_est numeric(8,5), detail jsonb, at timestamptz default now());
-- every table: enable RLS; policy owner_all using ((select public.is_owner())); revoke all from anon, authenticated except select/update the PWA needs.
-- Edge Functions use the secret key and bypass RLS. The GitHub runner holds NO database key, only a job-scoped HMAC.
```

**Publish lease** (the handoff's `for update skip locked` pattern; the `paused` check lives *inside* the statement, so a pause beats a race):

```sql
update social_posts set status='publishing', lease_until=now()+interval '10 min', attempts=attempts+1
where id=(select p.id from social_posts p, social_control c
          where c.paused=false and p.status='approved' and p.scheduled_for<=now()
            and (p.kind<>'product' or exists(select 1 from items i where i.id=p.item_id and i.status='active'))
          order by p.scheduled_for limit 1 for update of p skip locked) returning *;
```

**Kill switch, four layers, fail closed:** (1) `social_control.paused`: PWA switch, ntfy `http` button, or SQL. (2) Actions: repository variable `SOCIAL_ENABLED` and `if:` on the workflow, or disable it. (3) Credentials: `cron.unschedule(...)`, delete the Supabase secret, revoke the Instagram token in the Meta App Dashboard. (4) Anthropic org spend limit (drafts then fail with HTTP 400 `verified`). An unreadable control row means no publish.

**Cron jobs:** publish tick 5 min; comments poll 10 min (posts under 7 days old, because a private reply must be within 7 days `verified (w2d)`); sweeper 10 min (stuck `publishing`, expired containers, undelivered alerts); token refresh weekly; metrics and digest daily. **Logging:** `social_runs` per job with tokens and estimated dollars; Supabase function logs (7 days on Pro, 1 on Free `verified 10-26`); Healthchecks per job; a daily digest alert "N published, N failed, $X". Never log tokens or comment bodies beyond the row.

## 6. Approving from a phone

| Option | Cost at reference load | Can it carry Approve / Reject? | Notes |
|---|---|---|---|
| **Pushover to PWA Posts tab (recommended base)** | $4.99 once per platform, 10,000 messages/month free `verified` | Link only: one `url` + `url_title`, an image attachment, priority 2 with retry/expire and a receipt/callback; **no action buttons** `verified` | Same channel the dashboard already specifies. Whether a Pushover link opens Safari or the installed PWA is dashboard smoke test 12 |
| **ntfy action buttons** | Free without sign-up (the topic is the password); Supporter $6 monthly or $5 billed yearly, 2,500 messages/day, 3 reserved topics `verified` | `view`, `http` (POST/GET/PUT), `copy`, Android-only `broadcast`; **up to three actions** `verified`. iOS support of `http` not stated in the text I read: `unverified` | Use for **Pause all** and for B-mode "Looks good". The token in the URL must be single-use, bound to `approval_hash`, 24 h expiry. Free attachments cap at 15 MB with 3-hour life |
| **Telegram bot** | Free | Inline keyboards with callback buttons `verified`; the bot can send a clip for review (upload 50 MB, w1h `verified`) | Needs a webhook endpoint and a second app; downloads are capped at 20 MB, so not an ingest path |
| **Web page** | $0 | Full: video, caption edit, flags | Must live on the PWA host (Cloudflare Pages $0 or Vercel Pro), not in an Edge Function `verified` |

Email (Resend, free 3,000/month) is for the digest only; SMS (Twilio $0.0083 per segment plus carrier fees and A2P registration) is skipped; both `verified 10-26`. Flow: draft lands > `alerts` row > Pushover with cover > Hollie opens `/posts/<id>` > plays the cut, edits the caption, taps **Approve** (sets `approved`, stores `approval_hash`) > publisher posts at `scheduled_for`. Any edit after approval changes the hash and returns the post to `needs_review`.

## 7. Failure modes and guardrails

| Failure | Guardrail |
|---|---|
| **Double post** (crash between `media_publish` and the DB write; the page I read documents no idempotency key) | `idempotency_key` unique; lease; on a stale `publishing` row, **look before re-publishing**: read the container's `status_code` and list recent media for a caption match. Never blind retry. Rate check via `content_publishing_limit` |
| **Expired Meta token** (App Dashboard tokens last 60 days; refresh needs a token at least 24 h old and unexpired; "tokens that have not been refreshed in 60 days will expire and can no longer be refreshed" `verified (w2c)`) | Weekly refresh once the token is 30+ days old, new token written to Vault in the same transaction; `token_expiring` alert at day 50 (the dashboard's watchdog pattern); expiry means Ricky regenerates in the App Dashboard. **The GitHub fine-grained token that sends the dispatch also expires** (its lifetime was not stated on the docs I read): track it in the same watchdog |
| **Rate limits** (Instagram: 50 per 24 h on the endpoint reference, 100 in the guide `verified (w2c)`; private replies 750/h `verified (w2d)`) | Caps in `social_control` far below; honor 429 with backoff; plan for 50 |
| **Runaway token spend** | `max_usd_day` checked from `social_runs`; org spend limit; Haiku with thinking disabled; `--max-budget-usd` and `--max-turns` on any `claude -p` |
| **Bad caption goes out** | Deterministic lint **before** approval, a hard block not a model opinion: banned words (visit, in store, in-store, our doors, stop by, showroom, interior design, discount, % off, offer, bid, auction, first come, DM to claim, comment to claim, "every order"); any `$` or digit-price pattern; claim words (authentic, signed, original, mint, certified, "from the 19xx") force human review; Haiku QA pass lists unsupported claims. First 10 posts run in A mode |
| **Prompt injection through comments** | Comment text is data: classifier output is a JSON enum (structured outputs `verified 10-26`); the LINK reply is a fixed template, never model text; no tool use in the comment path |
| **Sold item still advertised** | Lease requires `items.status='active'`; the dashboard's `sold` trigger (T3) must also cancel `approved` posts for that item and alert; a `gone` post kind is human-only |
| **Stock does not exist yet** (BRIEF constraint) | `paused=true` by default; `kind='product'` blocked until an active item and live listing exist; `mood` posts need no item |
| **Plumbing** (signed URL expired before Meta fetched it; runner or dispatch silently dead; reply loop) | 1-hour signed URL minted at container time; sweeper marks a job stuck after 15 min and alerts; Healthchecks per cron lane; never reply to own account, one reply per comment id (`unique`) |

## 8. Approve-everything (A) vs approve-by-exception (B)

| Stage | A: human taps | B: safe unattended | Always human in both |
|---|---|---|---|
| ingest | Hollie shares clips and sets `has_person` | Same | Anything showing a person |
| edit | Preview in PWA | Deterministic render from a template | Music credit choice |
| caption | Edits and approves | Template + item facts, lint clean, no risk flags | Price, condition, age, maker, provenance, any person, any fixed-constraint word |
| cover | Views | Template cover from the render | New cover styles |
| publish | Taps Approve per post | Posts on schedule only for `mood` kinds and for template product posts that pass lint | Everything with a risk flag; the first 10 posts |
| reply | Approves each | Fixed LINK template after a public reply + private reply (route B in w2d) | Complaints, questions, anything not LINK |
| analytics | n/a | Automatic | Changing the calendar |

B means a lint-clean template post is set to `approved` with `approved_by='rule'` and waits for `scheduled_for` behind a ten-minute veto push ("Posting at 7:07, tap to stop"); A sets `approved_by='human'`. Pause-all is always one tap. **Reply row caveat:** the LINK auto-reply needs a working comment feed, which may need a legal entity (TL;DR 8); until then replies are Hollie's by hand.

## 9. Three tiers

| | **Tier 1: all manual** | **Tier 2: one scheduler + one editor** | **Tier 3: full pipeline** |
|---|---|---|---|
| What runs | Phone: Edits app, native Instagram scheduling (25/day, 30 days ahead) | Buffer Free (API + MCP on every plan; 3 channels, 10 queued posts each `verified (w2c)`) or Publer; Windows ffmpeg script | Section 1 |
| Runtime | None | **Windows PC** on demand + the scheduler's cloud | **Supabase + GitHub Actions + Pushover/PWA**; Fedora optional |
| Claude/Codex | Claude drafts a week of captions in chat; lint script (S1) | Claude Code writes a manifest and calls the scheduler API (subscription) | Haiku API at runtime; Claude builds; Codex builds site pages |
| Approval | Hollie is the poster | Hollie queues and approves captions | A or B |
| Human still | Shoot, edit, post, reply | Shoot, share clips, run the script, approve | A: shoot, tap. B: shoot, tap exceptions, answer non-LINK comments |

| Monthly cost line | Tier 1 | Tier 2 | Tier 3 (dashboard Pro exists) | Tier 3 standalone |
|---|---|---|---|---|
| Anthropic API | 0 | 0 | 0.27 | 0.27 |
| Supabase | 0 | 0 | 0 | 25 (Free possible, pauses) |
| GitHub Actions | 0 | 0 | 0 (1.44 of 12 used) | 0 |
| Push | 0 | 0 | 0 (+$4.99 once, shared) | 0 (+$4.99 once) |
| UI host / Healthchecks | 0 | 0 | 0 | 0 |
| Scheduler | 0 | 0-15 | 0-15, TikTok/Pinterest only (w2c) | 0-15 |
| **Total** | **0** | **0-15** | **about 0.27-15** | **about 25.27-40** |

TikTok stays on a scheduler or native in every tier: the own-API path is dead for public posting (w2c). Meta fees: none.

## 10. Build plan (dependency order)

| # | Piece | Owner | Hours (`inferred`) | Needs |
|---|---|---|---|---|
| S0 | Decisions; Instagram professional account; Meta developer app (Business type, Development mode, App Dashboard token); Anthropic key with about $10 limit; Pushover; GitHub fine-grained token; Supabase Pro `hv-desk` | **Ricky** | 3-4 once | Dashboard handoff section 0 rows 4, 6, 10 |
| S1 | `lint.ts` banned-word, price and claim checks + Deno tests (Edge and the Windows CLI share it) | Claude | 2 | Nothing; serves tier 1 now |
| S2 | Render script: 1080x1920 H.264+AAC 48 kHz, `+faststart`, 23-60 fps, under 25 Mbps (Meta Reel spec `verified (w2c)`), safe-zone crop, cover frame, Playwright cover | Claude | 4 | w2a, w2b |
| S3 | Migration `0004_social.sql`, RLS, control row | Claude | 1 | Dashboard T1 |
| S4 | `render.yml`: dispatch, apt ffmpeg, upload, HMAC callback, failure ping | Claude | 2 | S2, S3 |
| S5 | Edge Functions: ingest, draft, publish, comments, token, approve/control | Claude | 14-18 (w2c budgets 11-13 h for the publisher alone) | S1, S3, Meta token |
| S6 | PWA Posts tab | Claude | 3-4 | Dashboard T6 shell |
| S7 | Site `/p/<n>` pages and link-in-bio (round-d gating fact) from `docs/codex-handoff-social-autopilot.md`; Ricky publishes | **Codex** + Ricky | 3 + a publish | Independent; **before any product post** |
| S8 | Shadow mode (drafts only), then A for 10 posts, then B for template posts | Claude + Ricky | 2 | S4-S6 |
| S9 | Healthchecks, digest, spend report | Claude | 1 | S5 |

## 11. X verified, Y need review

- Instagram publish cap: 50 per 24 h (endpoint reference, verified) vs 100 (guide). Plan for 50.
- GitHub Free compute is now stated as **$12/month** (verified today; equals the 2,000 Linux minutes the dashboard note cited).
- Unattended subscription use: Anthropic's pages verified; whether a one-person shop pipeline is "ordinary individual usage": need review.
- **Comment polling for customers' comments in a Development-mode app: unverified (w2d).** Private reply at Standard Access: contradicted across sources (w2d). Both decide whether reply automation works before an entity exists.
- Make Core price (official page not read; $9-12 from search results); n8n monthly price (not read).
- Windows Task Scheduler wake reliability: community sources only.
- ntfy `http` actions on iOS: not stated in the text I read.
- `video_url` accepting a Supabase signed URL: Meta cURLs a "publicly accessible server"; a signed URL should qualify (`inferred`), one container call decides.
- Safari upload of phone video keeping recorded quality: unverified; w1h's Drive-trip check is also open.

## 12. Questions only Ricky can answer

1. **Is there, or will there be, a legal entity?** It decides whether comment-reply automation works at all (Business Verification, Advanced Access). Without one, replies stay by hand and only publish is automated.
2. **Approve everything, or approve by exception (B)?** B reverses the dashboard's "no auto-publish" rule for social.
3. **May any part touch the Fedora box** (ingest, render)? The dashboard says "not in v1".
4. **May the pipeline live in a small dedicated repo?** The dispatch token needs Contents: write; on the main repo that is write access to the whole shop, and the Vintage checkout is 132 MB. (Structure change: needs your word.)
5. Is a runtime `ANTHROPIC_API_KEY` with a $10 limit approved, with subscriptions kept for building?
6. Is the dashboard (Supabase Pro, Pushover, PWA) going ahead? Tier 3 stands on its T1, T4 and T6.
7. One disclosure line on automated link replies (w2d) vs "nothing else"? GitHub account Free ($12 included) or Pro ($18)?

## 13. Gaps

w2a's Fedora ffmpeg result (not in the folder at finish; if it passes, Fedora becomes the free render host and S4 gains a second target); Live-mode and Business Verification effects beyond w2c/w2d; how ChatGPT Sites stores secrets; Codex CLI deploy support today; lifetime of a fine-grained GitHub token; dispatch latency; Supabase egress allowances; Pushover link behaviour in the installed PWA.

## 14. Decision matrix

| Option | Stage | $/mo at load | Setup h | Claude/Codex-drivable | Ban/ToS risk | Approval fit |
|---|---|---|---|---|---|---|
| Native Instagram scheduling | publish | 0 | 0.5 | No | None | A |
| Buffer Free + Windows ffmpeg (tier 2) | edit/publish | 0-15 | 6-7 | Yes (API/MCP, CLI) | Low (approved app) | A |
| **Supabase + Actions + Haiku + own Meta app (tier 3)** | all | 0.27 (25 standalone) | 30-38 | Yes | Low: Instagram own account, Standard Access | A and B |
| Fedora render/ingest | edit/ingest | 0 | 3+ after w2a | Yes (ssh) | None | A/B, best effort |
| n8n self-hosted | orchestrate | 0 | 8 | JSON workflows | Depends on nodes | A/B |
| n8n Cloud / Make / Zapier | orchestrate | 20 EUR+ / 9-12 / 19.99+ | 5-8 | Partly | Same | A/B, no media plane |
| Claude scheduled task | plan/review | 0 marginal | 2 | Yes | Preview feature | A |
| Cloudflare Workers + Containers | all | 5 | 15 | Yes | Low | A/B |
| Unofficial Instagram libraries | publish | 0 | 4 | Yes | **High: ToS violation, ban risk to the one brand account. Not recommended, not tested** | n/a |

## 15. Build effort

| Tier | Claude Code | Codex | Ricky by hand |
|---|---|---|---|
| 1 | 2 h (S1) | 0 | Shoot, edit in Edits, post, reply |
| 2 | 6-7 h (S1, S2, scheduler wiring) | 0 (S7 optional) | Account setup 1-2 h; shoot, share, run script, approve |
| 3 | 28-35 h (S1-S6, S8, S9; S5 dominates) | 3 h (S7) plus a publish | S0 3-4 h once; weekly shoot; taps; regenerate the Meta token if it lapses; answer non-LINK comments |

All hours `inferred`.
