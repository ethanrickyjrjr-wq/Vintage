# Hermes and Telegram for Holliewood and Vine

**Status (2026-11-08): ideas and a build order, nothing built.** Written from the live Hermes install on the PC and the Hermes docs fetched the same day (`research/hermes/`). Ricky's ask: "what can we do with hermes and telegram to build this brand and make things more automated?" The sourcing half of that ask is in [`sourcing-2026-11.md`](sourcing-2026-11.md).

Hollie, with ie, she/her. The shop's fixed constraints (no offers or discounts, no claims by DM or comment, no showroom language, real photos only, the model never states material, age, maker, condition or price as fact) apply to every bot message below.

## 1. What exists today (checked on the PC, 2026-11-08)

| Thing | State | How checked |
|---|---|---|
| Hermes Agent on Windows | v0.20.0 (tag 2026.8.3), install `C:\Users\ethan\AppData\Local\hermes`. Newest upstream tag is `v2026.9.24`. The standing decision (desk wiki, agent-fleet) is to test an upgrade on Fedora first; Fedora is unplugged today. | `hermes --version`, `git ls-remote --tags` |
| Telegram gateway | Running (PID 41640), platform state `connected`, one DM chat (Ricky), started at login by `Hermes_Gateway.vbs`. `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS`, `TELEGRAM_HOME_CHANNEL` are set. | `hermes gateway status`, `gateway_state.json`, `.env` names |
| Model | `claude-sonnet-5-5` on provider `anthropic` (changed from gpt-oss:20b after 2026-10-05); fallback `gpt-oss:120b` on Ollama Cloud. No Anthropic API key in Hermes config, so the auth is the `hermes login` OAuth store (`auth.json`, touched 2026-11-06). | `config.yaml`, `hermes config show` |
| Toolsets on | web, browser, terminal, file, code_execution, vision, image_gen, tts, skills, todo, memory, session_search, clarify, delegation, cronjob, computer_use. Off: stt, video, x_search. MCP: `swfl-lake`. | `hermes tools list` |
| Web search backend | none configured (Exa, Firecrawl, Tavily, Parallel all "not set"). SearXNG lives on the Fedora box, which is offline today. What `web_search` does in this profile is unverified. | `hermes config show` |
| Cron | 7 jobs, 6 deliver to Telegram. Five are `--no-agent` scripts (stdout delivered verbatim). `swfl-morning-market-watch` is an agent job and **every one of its 14 retained runs, 2026-10-20 to 2026-11-06, was skipped**: Hermes refuses to run an unpinned job after the global model changed ("config drifted ... pin it explicitly"). Two Telegram deliveries failed on 2026-11-07 at 08:00 and 09:00 with `getaddrinfo failed` (no DNS, so the PC was off the network then). | `hermes cron list` |
| Guardrail | `pre_tool_call` shell hook `hooks/block-send/handler.py`, fail-closed: Hermes cannot send, post or buy anything on its own. | `config.yaml`, hook README |
| Skills | about 60 installed under `~/.hermes/skills/`; none for the shop. | `hermes skills list` |
| Grounding | the desk's `tools/hermes-ground/sync.sh` rewrites the tail of `SOUL.md` hourly with the Chief Of Staff wiki index. The bot knows the desk, not the shop. | Chief Of Staff repo |
| Shop accounts | eBay seller `holliewoodandvinellc` (7 live listings, 2 feedback), Instagram `@holliewoodandvine` (347 followers), empty Depop. No Etsy, Shopify, developer keys or Anthropic API key for the dashboard. | `research/instagram-and-marketplaces-2026-11-08.md` |

## 2. What Hermes and Telegram can do (from the docs, 2026-11-08)

Source pages are in `research/hermes/*-20261108.md`; URLs in section 8. The docs describe the newest release. Features marked **(newer)** are in the docs but not in the installed v0.20.0 CLI help, so they wait for the upgrade.

- **Telegram in:** text, photos, files, voice memos (auto-transcribed by the configured STT provider: `local` faster-whisper needs no key). Photos reach the agent as images for the `vision_analyze` tool. The public Bot API caps file downloads at 20 MB.
- **Telegram out:** any agent reply; `MEDIA:<path>` in a reply ships a file as a native attachment (jpg, png, pdf, csv, md, docx, xlsx and more). A bare image path is sent as a photo (Telegram recompresses to about 1280 px); `[[as_document]]` sends it as a file at full quality.
- **`hermes send`:** a CLI that posts text or `MEDIA:` files to Telegram from any script, "no LLM, no agent loop, no running gateway required". Targets: `telegram` (home channel), `telegram:<chat_id>`, `telegram:<chat_id>:<thread_id>`. Exit codes 0/1/2.
- **Cron:** schedules in `30m`, `every 2h`, cron expressions or natural language; `--deliver telegram`; `--no-agent --script x.py` runs a script and delivers its stdout (empty stdout = silent); `--monitor-url <url>` fetches a page each tick and only wakes the agent when the bytes change; `--skill` attaches a skill; `--model/--provider` pins the model (the drift guard above is why every job must be pinned); `[SILENT]` in a reply suppresses delivery; `context_from` chains jobs. **(newer)**: `--pin`, `--paused`, `--timezone`, `--grace-minutes`, `hermes cron cancel`, delivery `UNVERIFIED` tracking, `hermes cron doctor`.
- **Skills:** a folder under `~/.hermes/skills/<name>/SKILL.md` with YAML front matter (`name`, `description`, optional `platforms`, `requires_toolsets`, `config`) and sections When to Use / Procedure / Pitfalls / Verification. Every skill is a `/<name>` slash command in Telegram and can be attached to a cron job. `/learn` **(newer)** writes one from a walkthrough.
- **Groups and channels:** the bot works in groups (privacy mode or admin), can observe without replying, `require_mention`; cron can deliver to a specific chat or forum topic. One bot token per running profile.
- **Profiles:** a separate Hermes home per agent (own config, `.env`, SOUL.md, memory, skills, cron). "Never point two agent processes at the same profile." A second bot needs a second BotFather token.
- **Hooks:** shell `pre_tool_call` hooks can block tool calls (the block-send guard); gateway hooks cannot.

## 3. The ideas, ranked

Ranked by time saved per hour of setup, with the lazy version first. Costs use Anthropic list prices as of 2026-10-06 (Haiku 5.5 $0.10 in / $0.50 out per million tokens; Sonnet 5.5 $2 / $10); a Telegram photo is about 1,600 input tokens.

| # | Idea | Ricky does | Hermes does | LLM | Setup | Ceiling |
|---|---|---|---|---|---|---|
| 1 | **Cut-outs back to the phone** | shoots on the iPhone into Drive, as today | a watcher on the PC runs `cutout.py --watch` on the Drive inbox and `hermes send`s each finished white 1600 px JPEG to Ricky's Telegram | none | 1 hour | PC must be awake and on the network |
| 2 | **`/list` from the phone** | sends 3 to 6 photos plus one line (cost, flaws, measurements, maker mark) to the bot | the `hv-lister` skill drafts the eBay title, description in the house template, item specifics, the blanks still missing, and a price *range* flagged "comps not checked"; appends a row to the inventory sheet; returns the draft as text and as a `.md` file | Haiku first, under a cent a draft | half a day | the model guesses era and maker; every guess stays marked; Ricky pastes into the eBay app himself |
| 3 | **Estate-sale digest** | nothing | 07:00 Thu to Sat, a cron job reads this weekend's SWFL estate sales and auctions and sends the five worth driving to, with the keyword hits (brass, Pyrex, Blenko, Lilly, lamps) | Haiku, cents a day | 2 hours once the sourcing lane names the feeds | depends on which sites expose a feed or a plain-GET page |
| 4 | **Keyword lot watch** | nothing | `--monitor-url` on saved ShopGoodwill and HiBid searches; the agent wakes only when the page changes and reports new lots under the buy ceiling | Haiku, only on change | 1 hour per keyword set | only for pages that render without JavaScript (check per site) |
| 5 | **Buy-ceiling check** | types `/ceiling 45 ebay 2lb` at the sale | a script (not the model) returns the most to pay: half the net at the low end of the sold range after fees and postage, the rule in `sourcing-2026-11.md` section 2 | none | 1 hour | the fee table has to be kept current |
| 6 | **"New Finds" Telegram channel** | taps Publish on eBay | after each publish, `hermes send` posts the cut-out photo, one line and the listing link to a public channel linked from the Instagram bio and the site | none | 1 hour | Telegram is a small US audience; this is a VIP list, not the main feed |
| 7 | **Caption drafts** | sends a photo and `/caption` | drafts the Instagram caption and hashtags in the social-manual voice; Ricky posts | Haiku or Sonnet | 2 hours | interim until the social autopilot is built |
| 8 | **Buyer-question drafts** | forwards a buyer's question as text | drafts the reply in Hollie's voice using the listing's measurements; Ricky pastes it | Haiku | 1 hour | eBay and Etsy messages cannot be read by code, so it is paste in, paste out |
| 9 | **Sunday scoreboard** | nothing | a no-agent script reads the inventory sheet and sends listed / sold / cash in / cash out for the week | none | 1 hour | only as good as the sheet |
| 10 | **Comps on demand** | sends `comps Stiffel brass lamp` | *does not work from the PC*: eBay sold pages wall crawlers and headless browsers (memory, 2026-10-26). Ricky's eBay app, Sold filter, is 30 seconds. | | | skip |

### Idea 1: cut-outs back to the phone

`tools/cutout/cutout.py` already has `--watch` (process each photo as it lands, stop with `stop.txt`) and writes a manifest. Missing piece: after each photo, `hermes send --to telegram "MEDIA:<out>/<name>-ebay.jpg"`. Lazy version: a 15-line wrapper that tails the manifest and sends new rows, started by the same Windows login item that starts the gateway. Drive for desktop streams at `G:\My Drive`, so the inbox is a Drive folder Ricky drops into from the phone. Ricky then lists from the eBay app on the phone with white-background photos he never touched on the PC.

Check before trusting it: `hermes send` from Git Bash with a Windows path (the docs' Docker note says the path must be readable by the gateway process; here both run on the PC).

### Idea 2: `/list` from the phone (the skill)

This is the dashboard handoff's T6b ("photos plus one line in, Claude Haiku drafts") without the dashboard, Supabase, Etsy keys or the Anthropic console key, none of which exist yet. The skill replaces the Edge Function; Ricky's paste into the eBay app replaces the Etsy draft listing.

SKILL.md (`~/.hermes/skills/hv-lister/`), in outline:
- **When to use:** `/list`, or photos arriving with a line that looks like an item note.
- **Procedure:** describe each photo with `vision_analyze`; write the Title (80 characters, the house order: Vintage, decade, brand, colour, pattern, type, size), the Description in the template already used in `assets/ebay-2026-11-08/listings-copy.md` (condition line, measurements taken flat with `____` for anything not given, "Ships from Southwest Florida, smoke-free"), the Item specifics list, a "Still missing" list of the blanks, and a price range only if Ricky gave comps or the sourcing doc's category table covers it, otherwise "price: yours". Append one row (date, title, cost, status `draft`) to the inventory CSV. Reply with the text and `MEDIA:` the `.md`.
- **Pitfalls (the rules):** never state maker, era, material or condition as fact from a photo; write "appears", "unverified" and keep the guess visible; never invent a measurement; no price without a comp; Hollie with ie; no offers, no showroom words.
- **Verification:** the reply ends with the "Still missing" list even when empty.

Why Telegram photos are fine here: Telegram recompresses photos to about 1280 px, which is enough to read a label and draft text, and the listing photos themselves come through Drive and idea 1 at full size.

Model: start on Haiku 5.5 (`--model claude-haiku-5-5 --provider anthropic` if run as a job; in chat the profile's model applies, so this needs the profile split in section 4 or a `/model` switch). The dashboard handoff's own fallback stands: if a 20-item side-by-side shows weak titles, move to Sonnet 5.5.

### Idea 3: estate-sale digest

The job: `hermes cron create "0 7 * * 4-6" --name hv-estate-digest --deliver telegram --provider anthropic --model claude-haiku-5-5 --skill hv-sourcing "<prompt>"`. The prompt follows the pattern that already works in `swfl-morning-market-watch`: fetch named URLs, quote only what the page says, bracketed blanks on failure, a fixed output shape, max 200 words. Which URLs, and whether they are feeds or pages, is the sourcing lane's job (`sourcing-2026-11.md` section on local venues). If a site needs JavaScript, the job uses the `browser` toolset at a cost of a few more cents, or that site is dropped.

### Idea 4: keyword lot watch

`hermes cron create "every 6h" --monitor-url "<search url>" --deliver telegram --provider anthropic --model claude-haiku-5-5 --name hv-watch-blenko "The page is a search result. List only lots that are new since the last run, with price and end time. If nothing is new reply [SILENT]."` The monitor hash suppresses the model run while the page is unchanged. One job per keyword set; keep it to five.

### Idea 6: the "New Finds" channel

Make a public Telegram channel, add the bot as admin, note the channel id. After each publish, `hermes send --to telegram:<channel_id> "MEDIA:<cutout.jpg>"` then the one-liner and the eBay link. Later, when the dashboard's `channel_listings` exists, the webhook does it. Constraint check: a channel that only ever posts a photo, one line and the listing link makes no offers and takes no claims, so it is within the shop's rules. Position it as "first look, one hour before Instagram" and put the `t.me` link in the Instagram bio in place of the empty Depop link (`research/instagram-and-marketplaces-2026-11-08.md`).

## 4. Prerequisites and fixes, in order

1. **Pin every cron job's model.** The drift guard has skipped `swfl-morning-market-watch` on every retained run since 2026-10-20 (`hermes cron runs 4b639fe053a5`). Either pin it (`hermes cron edit 4b639fe053a5 --provider anthropic --model claude-haiku-5-5`) or remove it; SWFL is a dead revenue lane per the desk kill list, so removing is the lazier choice and Ricky's call. Every new shop job is created with `--provider` and `--model`.
2. **Prove one agent cron job on the Anthropic auth.** No agent job has run since the provider changed. Create a one-shot (`hermes cron create "in 5m" --deliver telegram --provider anthropic --model claude-haiku-5-5 "Reply with the word ready."`) and watch it land. If OAuth refresh fails unattended, an Anthropic API key in Hermes `.env` is the fix (the dashboard handoff wants that key anyway).
3. **Keep the PC on the network when jobs fire.** The 2026-11-07 deliveries failed on DNS. Windows power plan: never sleep while plugged in; or schedule deliveries for hours the PC is known to be up. Fedora is the better host for always-on jobs once it is plugged back in.
4. **Decide the profile.** Lazy first week: one skill on the `default` profile, which already has Ricky's DM, cron and the block-send guard. When `/list` is daily, split: `hermes profile create hv`, a second BotFather token, its own SOUL.md grounded on the shop constraints with a copy of the desk's `sync.sh` pointed at this repo's docs, its own skills and cron. The docs' rule: one profile per agent, one token per running gateway.
5. **Turn on STT** if voice memos are wanted (idea 2 with a spoken item note): the `stt` toolset is off and no STT provider is configured; `local` faster-whisper needs no key.
6. **Pick a web search backend** for the digest if any source needs search rather than fixed URLs: SearXNG on Fedora when it is back, else Exa or Firecrawl keys. Fixed URLs need none.
7. **Upgrade** only after the Fedora test (standing decision). Nothing in the first six ideas needs a feature newer than v0.20.0; `--pin`, `--paused`, `--grace-minutes` and `hermes cron cancel` are conveniences.

## 5. What not to build

- Anything that sends, posts, bids or buys on its own. The block-send hook stays fail-closed; `hermes send` is called by scripts Ricky starts, and the agent itself never sends.
- A bot that talks to buyers. eBay and Etsy messages cannot be read by code (Etsy's API has no messages endpoint; eBay's path needs the developer keys that do not exist), and the shop rule is no claims by DM.
- Comps by bot (idea 10). eBay sold pages are walled to this machine; the eBay app is faster.
- A Telegram-first audience. The buyers are on Instagram and eBay; Telegram is Ricky's remote control and a small VIP list.
- Image generation for listings. Real photos only is a fixed constraint.

## 6. Spend, roughly

| Job | Tokens a run | Haiku 5.5 | Sonnet 5.5 |
|---|---|---|---|
| `/list` draft, 6 photos plus template | about 12k in, 1.5k out | about $0.002 | about $0.04 |
| Estate digest, three pages | about 20k in, 0.5k out | about $0.002 | about $0.045 |
| Lot watch, when the page changed | about 8k in, 0.3k out | about $0.001 | about $0.02 |

A month of daily use is cents on Haiku and a few dollars on Sonnet. The Ollama Cloud fallback (`gpt-oss:120b`) is free-tier and catches provider outages.

## 7. Build order and the first test

1. Fixes 1 and 2 (ten minutes, no code).
2. Idea 1 (the wrapper plus `hermes send`): first test is one photo dropped in the Drive inbox from the phone, the white JPEG back on the phone within a minute.
3. Idea 2 (the skill): first test is the seven live eBay listings re-drafted from their photos and compared with `assets/ebay-2026-11-08/listings-copy.md`.
4. Idea 3 once `sourcing-2026-11.md` names the feeds; idea 6 once Ricky creates the channel.

## 8. Sources

Hermes docs, fetched 2026-11-08 with crawl4ai into `research/hermes/`:
- https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram
- https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/tools
- https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode

Local state: `hermes --version`, `hermes cron list`, `hermes tools list`, `hermes skills list`, `hermes send --help`, `hermes cron create --help`, `hermes config show`, `config.yaml` and `.env` key names, all on 2026-11-08. Prior desk research: `dev/Chief Of Staff/wiki/agent-fleet.md`, `research/agent-fleet/2026-09-16/`. Anthropic prices: the `claude-api` skill table cached 2026-10-06.
