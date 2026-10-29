# w3b: live re-check of automation-tier prices, limits, signup URLs

All facts **accessed 2026-10-29**. Tags: `verified` = read on the live vendor page or vendor source this session; `inferred` = my reading. Raw captures: `raw/w3b-*.md` (35 crawls of 45, 1 search of 8). `curl -sI` and `gh api` covered GitHub, ntfy-source and license items. Nothing downloaded, installed or signed up.

## 1. Anthropic API
Sources: https://platform.claude.com/docs/en/about-claude/pricing · https://platform.claude.com/docs/en/about-claude/models/overview · https://platform.claude.com/docs/en/api/rate-limits · https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers

| Item | Page says | Tag |
|---|---|---|
| Model IDs | `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5` (API ID = alias) | verified |
| Per MTok in / out | Fable 5.1 $10/$50; Opus 5.5 $4/$20; Sonnet 5.5 $2/$10; **Haiku 5.5 $0.10/$0.50 for prompts up to 100,000 tokens, $0.50/$2.50 above** (cache reads and writes count toward the 100K) | verified |
| Cache hits / 5-min writes | Haiku 5.5 $0.01 / $0.125; Sonnet 5.5 $0.10 / $2.50; Opus 5.5 $0.20 / $5 | verified |
| Batch | "50 percent discount on both input and output": Haiku 5.5 $0.05/$0.25, Sonnet 5.5 $1/$5, Opus 5.5 $2/$10 | verified |
| Tokenizer | 4.7 and later models make "approximately 30% more tokens for the same text" | verified |
| Monthly spend limit | Console > Billing (platform.claude.com/settings/billing) > Spend limits > Set/Adjust limit. Cannot exceed tier cap: Start $500, Build $1,000, Scale $200,000 per month. New orgs may start in a lower "Evaluation" tier. No spend limits on the default Workspace | verified |
| On hitting a limit | Your own limit: HTTP 400 `invalid_request_error`. Tier cap: HTTP 429 `enforced_spend_limit_reached`, no `retry-after`, "SDK's automatic retries" fail until 00:00 UTC on the 1st | verified |
| Signup | Console https://platform.claude.com/ (login at /login) | verified |
| Max API credits | Max 5x $100, Max 20x $200 per month; covers API, Agent SDK, Managed Agents; **"Doesn't cover: Claude Code"**; no card needed; no rollover; claim after 7 days. Pro: none | verified |

## 2. Claude plans, scheduled tasks, unattended use
Sources: https://claude.com/pricing · https://code.claude.com/docs/en/routines · https://code.claude.com/docs/en/scheduled-tasks · https://code.claude.com/docs/en/headless · https://code.claude.com/docs/en/authentication · https://code.claude.com/docs/en/legal-and-compliance · https://www.anthropic.com/legal/consumer-terms

| Item | Page says | Tag |
|---|---|---|
| Pro | $17/mo with annual discount ($200 up front); $20 monthly; Claude Code included; "Hand off and schedule tasks" | verified |
| Max | "From $100" per month (5x); 20x price not shown | verified |
| Cloud scheduled tasks (formerly routines) | "research preview"; Pro, Max, Team, Enterprise; claude.ai/code/routines or `/schedule`. Presets hourly/daily/weekly; custom cron, "Expressions that run more often than once per hour are rejected". Limits: 100 scheduled runs/hour per account; Run now/API fires 30/hour per task. Draw down subscription usage; no overage unless usage credits are on. Fresh clone, no local files | verified |
| Faster cadence | Desktop tasks: machine on, 1 minute when Claude sets it, 1 hour in forms. `/loop`: session open, 1 minute, recurring tasks expire after 7 days | verified |
| `/schedule` needs subscription login | Hidden with a Console API key, or if `ANTHROPIC_API_KEY` is set | verified |
| `--bare` | "bare mode doesn't use your subscription login"; "never reads OAuth credentials"; needs `ANTHROPIC_API_KEY`; "will become the default for `-p` in a future release" | verified |
| Subscription headless | `claude setup-token` gives a one-year token for `CLAUDE_CODE_OAUTH_TOKEN`, "For CI pipelines, scripts"; **bare mode does not read it** | verified |
| Legal page | "Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK." OAuth "intended exclusively for purchasers of ... subscription plans ... ordinary use"; developers building products "should use API key authentication" | verified |
| Consumer Terms (eff. Oct 8, 2025) | Forbids automated access "Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it ... through a bot, script, or otherwise" | verified |
| Reading | The docs explicitly offer scripts via `setup-token` and Anthropic-run scheduled tasks, so those are "explicitly permit[ted]". A personal cron on a subscription token is gray; the API key (or Max API credits) is the unambiguous unattended path | inferred |

The two constraints point opposite ways: cloud tasks need the subscription; `--bare` needs the API key.

## 3. OpenAI Codex
Sources: https://developers.openai.com/codex/pricing · https://developers.openai.com/codex/noninteractive · https://developers.openai.com/codex/app/automations

| Item | Page says | Tag |
|---|---|---|
| Plans | Free $0; Go $8; Plus $20; Pro from $100 ($100/$200/$500); Business $20/user/mo annual ($25 monthly, 2+ users); Enterprise/Edu contact sales; API key at API token prices. "ChatGPT Work and Codex share usage" | verified |
| Where Codex runs | Plus lists web, CLI, IDE, iOS. Free and Go list only the desktop app with GPT-6 Luna "subject to rollout". So `codex exec` needs Plus or an API key | inferred |
| Limits | Plus local messages per 5 hours: GPT-6.1 Sol 15-160, Terra 35-285, Luna 350-3,000, Astra 5-45; "not fixed message limits"; weekly limits may apply; Pro has no 5-hour limit; cloud tasks use more | verified |
| Model churn | GPT-5.5 left Codex ChatGPT sign-in 2026-10-14; API-key sessions unaffected | verified |
| `codex exec` | Read-only sandbox default; "reuses saved CLI authentication by default"; `CODEX_API_KEY` is the CI default; ChatGPT-managed auth in CI is "advanced", "Do not use this workflow for public or open-source repositories" | verified |
| Scheduled tasks | ChatGPT desktop app and web "Scheduled"; custom RRULE; minute intervals inside a chat; Gmail/Slack/GitHub triggers on web/mobile "eligible plans". Local projects: "keep the computer on and the app running". CLI cannot create them. Unattended, `approval_policy = "never"` when allowed | verified |

## 4. Supabase
Sources: https://supabase.com/pricing · https://supabase.com/docs/guides/functions/limits · https://supabase.com/docs/guides/storage/uploads/file-limits · https://supabase.com/docs/guides/cron · https://supabase.com/docs/guides/platform/free-project-pausing

| Item | Page says | Tag |
|---|---|---|
| Free vs Pro | Free $0: 500 MB DB, 1 GB storage, 5 GB egress, 50,000 MAU, 2 active projects. Pro from $25/mo (includes $10 compute credit, 8 GB disk, 100,000 MAU) | verified |
| Storage per file | Free 50 MB ("can't exceed 50 MB"); Pro and Team settable to 500 GB | verified |
| Edge Functions | 256 MB memory; CPU 2 s per request (excludes async I/O); wall clock 150 s Free, 400 s paid; idle timeout 150 s; 500,000 invocations Free, Pro 2M then $2 per million | verified |
| pg_cron | "Supabase Cron" is built on pg_cron; SQL or Dashboard; "every second to once a year"; can call an Edge Function over HTTP; keep at most 8 concurrent jobs, each under 10 minutes. No plan restriction stated | verified; Free availability inferred |
| Pausing | "pauses Free Plan projects that show low activity over a 7-day period"; warning email about a week ahead; paid projects never pause; restore within 1 year (page heading says "90-day window", text says 1 year) | verified |

## 5. GitHub Actions
Sources: https://docs.github.com/en/billing/concepts/product-billing/github-actions · https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows · https://github.com/actions/runner-images

| Item | Page says | Tag |
|---|---|---|
| GitHub Free | Private repos: **$12 included compute per month** (a dollar amount, not minutes), 500 MB artifacts, 10 GB cache. Linux 2-core $0.006/min. Public repos on standard runners: free | verified |
| 2,000 minutes | $12 / $0.006 is my arithmetic; the page gives only "$300 covers 50,000 minutes" | inferred |
| `repository_dispatch` | Custom API trigger; runs on the default branch. No trigger-based billing exemption listed, so it bills as any run | verified; billing inferred |
| ffmpeg | Not in the installed-software lists of Ubuntu 24.04 (image 20261026.354.1) or 26.04 (20261026.180.1). `ubuntu-latest` is 24.04 now and moves to 26.04 in November 2026 | verified (absence) |

## 6. Hosting, storage, notifications, transfer
| Item | Page says | Tag |
|---|---|---|
| Vercel (https://vercel.com/pricing, /docs/plans/hobby) | Hobby $0, "restricts users to non-commercial, personal use only". Pro $20/mo with $20 usage credit | verified |
| Cloudflare R2 (https://developers.cloudflare.com/r2/pricing/) | Free per month: 10 GB-month, 1M Class A, 10M Class B, free egress, Standard storage only. After: $0.015/GB-mo, $4.50/M Class A, $0.36/M Class B | verified |
| Pushover (https://pushover.net/pricing, /api) | $4.99 one-time per platform, 30-day trial, 10,000 free messages/month sent. Teams $5/user/mo. **No action buttons**: API has `url`/`url_title` and an emergency-priority acknowledge callback only | verified (absence) |
| ntfy (https://ntfy.sh/, https://docs.ntfy.sh/publish/) | Free without sign-up (ntfy.sh: 250 daily messages, 2 MB attachments). Supporter $5/mo annual ($6 monthly) 2,500/day; Pro $10 ($12) 20k/day; Business $20 ($25) 50k/day. iOS app on App Store. Action buttons `view`, `http`, `copy`, `broadcast`; docs source marks `http` "Supported on: Android, Apple, Firefox"; `broadcast` Android only. Self-hosting free | verified |
| PhotoSync (https://apps.apple.com/us/app/photosync-transfer-photos/id415850124) | Free app + in-app purchases: Premium Yearly $6.49, Monthly $0.99, Premium Lifetime $24.99 (list also shows a $14.99 Lifetime and Pro Lifetime $5.99). Premium Autotransfer is iOS only | verified; current SKU needs review |
| rclone (https://rclone.org/) | Free, MIT, v1.75.2 | verified |

## 7. ffmpeg pin, Remotion, HyperFrames
| Item | Page says | Tag |
|---|---|---|
| BtbN asset resolves | `curl -sI` on `.../releases/download/autobuild-2026-10-28-19-47/ffmpeg-n8.1.3-25-g611cec792a-linux64-gpl-8.1.tar.xz`: 302, then 200, Content-Length 152135596, Last-Modified 2026-10-28 19:48:07 GMT | verified |
| Checksum | `checksums.sha256` and the release API digest agree: `8d02a412b0f72051bf30201a9f2c117fe557a4dc44b03c5c99fda2fbd7b00b5d` | verified |
| Retention | README: "The last build of each month is kept for two years. The last 14 daily builds are kept." Today's release list: exactly 14 dailies (10-15 to 10-28) plus month-end tags back to 2024-11-30 | verified |
| Pin expiry | The 10-28 tag is not a month-end, so it drops after about 14 further builds, near 2026-11-11 | inferred |
| Safer pin | Month-end `autobuild-2026-09-30-13-08`, `ffmpeg-n8.1.3-9-g29e619e767-linux64-gpl-8.1.tar.xz`, 150,360,944 bytes, API digest `sha256:97ce978979194b5cf7e06a5e68020dbdaa7a4f3294c5452b6a1bc347100dbb79`; or mirror the tarball to our own storage and pin by checksum | verified (digest); advice inferred |
| Remotion (LICENSE.md, https://www.remotion.pro/license) | Free if "an individual", "a for-profit organization with up to 3 employees", non-profit, or evaluating. 4+ people: Creators $25/mo per seat, Automators $0.01/render with $100/mo minimum, Enterprise from $500/mo. Repo license field NOASSERTION | verified |
| Remotion 5.0 | Open PR #3750: new license "apply for anyone using Remotion 5.0 or later"; "Contractors also count towards team size" | verified |
| HyperFrames (https://github.com/heygen-com/hyperframes) | Apache-2.0 (API and README). Telemetry **on by default** (`DEFAULT_CONFIG telemetryEnabled: true`, `packages/cli/src/telemetry/config.ts`); off via `hyperframes telemetry disable`, `HYPERFRAMES_NO_TELEMETRY` or `DO_NOT_TRACK`. README does not mention telemetry | verified |

## Corrections (page differs from or qualifies the earlier report)
1. **Haiku 5.5 $0.10/$0.50** holds only for prompts up to 100K tokens; above that $0.50/$2.50. Sonnet 5.5 $2/$10 confirmed.
2. **"Hourly at most"** is true for cloud scheduled tasks only. Desktop tasks and `/loop` run every minute but need the machine on.
3. **`claude --bare -p`** confirmed to refuse subscription login, and it also ignores the `setup-token` token. Non-bare `claude -p` with `CLAUDE_CODE_OAUTH_TOKEN` is the documented subscription path. `--bare` is slated to become the `-p` default.
4. **Remotion "up to 3 people"**: LICENSE.md says "3 employees" (the pricing page says "people"). Remotion 5.0 will count contractors.
5. **BtbN pin `autobuild-2026-10-28-19-47` resolves today but is a daily tag** and will be pruned within about two weeks.
6. **GitHub "2,000 Linux min"** is arithmetic; GitHub states $12.
7. **Max credits** ($100/$200) do not cover Claude Code.

All other bracketed values matched.

## Could not verify
- Max 20x monthly price (page says only "From $100").
- Which ChatGPT plans get scheduled tasks ("eligible plans").
- Whether a pg_cron job counts as Free-plan activity; pg_cron on Free is inferred.
- Current PhotoSync SKU (App Store lists duplicates); price outside the US store.
- HyperFrames "linked to a HeyGen account only if you sign in": `telemetryIdentity.ts` keys on a signed-in user's username or email, but I did not trace the anonymous path.
- Whether Anthropic treats a personal cron on a `setup-token` as permitted; only Anthropic can say.
- Sept month-end tarball: API digest only, not downloaded.
