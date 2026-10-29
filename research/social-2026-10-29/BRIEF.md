# Social media research: shared brief (read this first, every lane)

Written 2026-10-29 by the parent Opus session. Working directory: `C:\Users\ethan\dev\Vintage` (Git Bash).

## Mission

Ricky Cooper owns **Holliewood and Vine** (also written **Holliewood & Vine**; spelled Hollie, with ie), a vintage resale shop and styling service going online. Hollie is the persona and the decider, she/her. Ricky wants one step-by-step manual for social media growth that answers: what to post, when to post, how to make covers and thumbnails that get clicks, the best way to grow, the easiest way to take a phone video and get it posted, what other vintage sellers and designer-type people do, and how to make the whole thing **mostly autonomous** (edits, covers, posting, replying) using **Claude Code and Codex (OpenAI)**. Prices and signup links for every tool. Do not find one tool and call it the way: compare real options and say which wins under which condition.

Your lane is one slice of that. The parent writes the manual from all lanes.

## Already done: do NOT redo it

Read these first, in this order, then build on them:
1. `research/round-d/d1-social-video.md`. 12 vintage Instagram accounts already studied (Palm Beach Regency, Vintage Regency, Brass Lotus, Gaby's Old Treasures, Sunday Morning Salvage, Curated by Lucy, Ca Marche, Mill Street, Select Vintage NYC, Barfly Vintage, Vincent Collective, Vestige). Platform rules for TikTok Shop, Meta Shops, Pinterest are read. Free scheduler caps are read (Buffer, Publer, Metricool, Planoly, Pinterest native, TikTok Studio). Its 4-week content skeleton exists. Do not re-study those accounts or re-fetch those pages unless you need one fact from them.
2. `C:\Users\ethan\dev\Chief Of Staff\wiki\social-comment-ai.md`. Meta and TikTok API approval gates, read live 2026-10-12: Meta Business Verification needs a registered legal entity (up to 14 business days); App Review is only for permissions on other people's accounts, **our own pages need no review**; the TikTok consumer developer platform has no comment scope and TikTok developer signup needs a company-domain email and a legal entity.
3. `C:\Users\ethan\dev\Chief Of Staff\wiki\clipfeed.md` and `video-to-markdown.md` (how video links become text and frames on the Fedora box).
4. `docs/round-d-synthesis.md` (decisions Ricky already made) and `docs/storefront-art-direction.md` (the brand look).

## Fixed constraints (the shop's rules; never recommend against them, flag conflicts instead)

- **No claims by DM or comment.** The shop sells one-of-one pieces; a comment/DM claim risks selling one object twice. The only call to action is the listing page (reply "LINK" with the link, nothing else).
- **No bidding, no claim-to-bid lives.** Whether that is a regulated auction in Florida is unchecked. Whatnot-style auctions are out unless flagged for a lawyer.
- **No discounts, no discount codes, "Absolutely no offers."**
- **No showroom language.** Never "visit", "in store", "our doors", "stop by". There is a room (burgundy walls, racks, lamps, art, a pink "do it for the plot" neon) that inspires the brand; it is not an open store. Samples on the site are illustrative.
- **Hollie is she/her. Say "style", never "interior design"** (Florida ch. 481 wording rule).
- **The mirror ball is "sometimes" a gift, never promised, never every order.**
- **The site's listings are sample listings with illustrative prices; checkout is "coming soon".** No product-link post should go out until real stock exists. Etsy, Shopify, Instagram, TikTok, Pinterest, and Facebook accounts for the shop do not exist yet. Whether `@holliewoodandvine` on Instagram is Ricky's is **unknown**.
- **Real photos of real items only.** Never recommend AI-generated product imagery. AI for captions, cuts, covers around real photos is fine.
- Brand look: burgundy atmosphere, Bodoni Moda (headlines, never under 20px) and DM Sans, neon pink accent, white framing only around product photos. Hands-first filming (Hollie's hands, the room, the objects) is the default; Hollie on camera is optional and Ricky's/Hollie's call.
- Sold pieces are marked "Gone" and stay visible.
- No legal entity is confirmed. Anything that needs a registered company (Meta Business Verification, TikTok developer signup) must be flagged as such.
- Budget is not set. Price everything. Lead with free, show the first paid step and what it buys.
- Ricky's pattern for approval is "photos in, one line in, a draft out, Ricky taps Publish". Whether Hollie approves each post before it goes live is Ricky's open question: design for both modes (approve-everything and approve-by-exception) and say which parts need a human in each.

## Operator facts

- Tools Ricky has: Claude Code (this) and Codex (OpenAI) subscriptions; Windows 11 PC (Git Bash + PowerShell, local ffmpeg works); an always-on Fedora box (`ssh fedora`, CPU-only i7-8565U, 15 GB, no sudo, rootless podman; its ffmpeg has only the `libopenh264` stub, so it cannot decode phone H.264/HEVC video as-is); a phone, probably an iPhone (the Apple ID is a private-relay address; unconfirmed). Stack: TypeScript, Deno, Supabase, Vercel, React. Site hosted via ChatGPT Sites, published by Codex.
- `ssh fedora` also runs SearXNG, crawl4ai (REST) and Ollama (qwen3.5:4b, about 7 tok/s). CPU only. Any Hugging Face/GitHub pick must be CPU-runnable there, or hosted with a stated price.
- Claude Code skills installed on this machine that touch social/video (note them, don't assume they work): ecc:social-publisher (SocialClaw), ecc:crosspost, ecc:content-engine, ecc:video-editing, ecc:remotion-video-creation, ecc:videodb, ecc:fal-ai-media, ecc:brand-voice.

## Rules of evidence (Vendor First)

- Today is **2026-10-29**. What you remember from training about 2025-2026 platform features is a hypothesis. Verify against the live vendor page in this session and date every fact.
- Order of trust: (1) the platform's or vendor's own page, docs or official account; (2) big-sample studies with stated n, method and date; (3) practitioners (label their commercial bias: agencies and tool vendors sell this advice); (4) search snippets. "Best time to post" studies from scheduler vendors are **marketing**; tag them so.
- Tag every fact: `verified` (read on the live page this session), `vendor claim`, `study (n=..., date)`, `unverified (search snippet)`, `inferred` (your reading). Never write a number without its tag and source URL.
- When sources disagree, write "X verified, Y need review" and show both.
- Prices: plan name, price, billing period (monthly vs annual-billed), limits, source URL, accessed date. If the page is walled, write "price not read".
- Signup links: give the real URL where Ricky creates the account or reads the docs.

## Tool rules (these cost real time before)

- Fetch a page: `env -u MSYS_NO_PATHCONV crawl4ai "<url>" -o md -bc < /dev/null > research/social-2026-10-29/raw/<LANE>-<slug>.md` (always `< /dev/null`, always `-bc`, always a lane-prefixed unique output file, never a shared one). Check the size: **under 1 KB is a bot wall, not a page**. `tools/crawl.sh "<url>" <out.md>` does the same.
- **Instagram, TikTok and most Meta/Facebook help pages are bot walls.** Do not burn crawls retrying them. Reach the same facts through: the shop's own website, Linktree, press articles, platform blogs and newsrooms, creator.* portals, transcripts, search snippets (tag them), and clipfeed (below). No Patchright (Ricky denied it, do not retry). Do not use Chrome. Do not log in anywhere.
- Search: `tools/search.sh "query" [general|science|news]` prints `url | title | engine` (SearXNG on the Fedora box; it returns junk when hammered). Budget **at most 20 searches**; pace them. Prefer the **WebSearch tool in standard mode** for discovery (load it with ToolSearch `select:WebSearch` if it is deferred), and keep `search.sh` for raw URL lists. Budget about 40 crawls.
- GitHub: `gh search repos ...` and `gh api repos/OWNER/REPO --jq '{stars:.stargazers_count,pushed:.pushed_at,license:.license.spdx_id}'` work (authenticated). `gh search` is limited to 30 requests a minute on one shared token; sleep 2 seconds between search calls and keep to the budget in your lane prompt.
- Watching a public Instagram/TikTok/YouTube video: `ssh fedora '~/clipfeed/venv/bin/python ~/clipfeed/clipfeed.py "<url>"'` prints a timestamped transcript (YouTube captions first, else Whisper small). For engagement numbers and caption: `ssh fedora '~/clipfeed/venv/bin/python -m yt_dlp --skip-download --dump-json --no-playlist "<url>"'` and read `like_count`, `comment_count`, `view_count` (often missing on Instagram), `duration`, `timestamp`, `uploader`, `description`. No cookies, no login, public items only. Keep it small and spaced (the Fedora box's IP can be rate-limited): follow the per-lane cap. Fedora's ffmpeg cannot decode phone video, so frame grabs need the file copied down and cut with the Windows ffmpeg (`fps=1/5,scale=420:-1,tile=3x3`).
- Concurrency: other lanes run at the same time. Never write outside `research/social-2026-10-29/`. Never edit existing repo files.

## What you must NOT do

No signups, no purchases, no logins, no posting, no DMs, no comments, no Apify or other paid-API spend, no installs on the Windows machine. (Wave 2 lanes may run small throwaway tests on the Fedora box in their own temp dir if their prompt says so.) Do not create files elsewhere in the repo.

## Output (the parent saves nothing for you unless you cannot)

1. Raw captures: `research/social-2026-10-29/raw/<LANE>-*.md` (the crawl outputs above; delete any under-1 KB wall captures).
2. Your report: **try once** to write the full report to `research/social-2026-10-29/<LANE>.md` with a Bash heredoc (`cat > file <<'EOF'`). The harness has refused subagent report writes before. If it refuses, do not retry or fight it: **return the full report as your final message** and say so on the first line. If the write works, your final message is only a digest (at most 350 words: top 8 findings, decisions for Ricky, gaps, the file path) and you must confirm with `ls -l` that the file exists.
3. Report shape, at most about 3,500 words, tables over prose:
   - **TL;DR** (at most 10 bullets, each with its tag).
   - **Findings**, each with source URL, accessed date, tag.
   - **Options table** for every decision in your lane: at least three real options, price, effort, risk, and "wins when ...".
   - **Recommendation for Holliewood & Vine**, in three tiers where it makes sense: (a) free and native only, (b) one paid tool, (c) the full Claude + Codex pipeline. State what a human must still do in each.
   - **X verified, Y need review** list.
   - **Questions only Ricky can answer** and **gaps** (what you could not reach and why).
   - Where a finding changes a fixed constraint above, say so plainly and do not apply it silently.
