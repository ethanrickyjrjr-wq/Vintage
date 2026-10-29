# Wave 2 addendum: automation lanes (read BRIEF.md first, then this)

BRIEF.md is still binding (constraints, tool rules, evidence tags, report shape). This adds what wave 1 learned and the rules for the automation lanes. Written 2026-10-29.

## Goal of wave 2

Ricky wants edits, covers, posting and replying **mostly autonomous** with Claude Code and Codex, human in the loop only where it matters. Wave 2 finds the real options for each stage, compares them honestly, and costs them. The parent builds nothing yet; wave 3 verifies the finalists and writes `docs/social-manual.md` and `docs/codex-handoff-social-autopilot.md`.

## Stage taxonomy (every find, in every lane, is tagged with one)

`ingest > edit > caption > cover > publish > reply > analytics`

Every tool, repo or model you list carries: stage; for GitHub repos stars, last push, license (from `gh api repos/OWNER/REPO --jq '{stars:.stargazers_count,pushed:.pushed_at,license:.license.spdx_id,archived:.archived}'`); runs on CPU on the Fedora box, runs on the Windows PC, or hosted (and its price); whether Claude or Codex can drive it (API, CLI, MCP, or only a GUI); and the ban/ToS risk if it touches Instagram, TikTok or Meta.

## Three paths per platform (publishing and replying lanes)

For each platform compare: (1) **native** scheduling in the platform's own app; (2) a **third-party scheduler running under its own approved platform app**; (3) **our own API app**. For each give: setup steps, gates (legal entity, app review, audit, business verification), what it can and cannot post (Reels, carousels, Stories, covers, alt text, collabs, scheduled limits), monthly cost for the reference load below, and whether it is safe for the main account.

**Reference load** for all pricing: one brand, 5 Instagram/Facebook posts a week, 3 TikTok videos a week, 3 Pins a week, replies to about 30 comments a week.

## Facts wave 1 already verified (use them, do not re-derive; read the reports for sources)

- `w1a-ig-rules-timing.md` sections 2 and 4: Instagram API publishing works through Unified Login or Instagram Login with **no Facebook Page**; own-account use is **Standard Access, no App Review**; Advanced Access (other people's accounts) needs App Review plus Business Verification; in-app scheduling is 25 a day, 30 days ahead, any public account, but **no collab posts or product tags on scheduled posts**; the developer doc says 100 API posts per 24 h in one place and 50 in another (plan for 50); Trial Reels need a professional account with 200+ followers and have an API parameter; alt text is an API field; the AI-generated-profile label covers AI people only, but C2PA/AI-info metadata from some AI tools may label real photos (test before committing); watermarks and re-uploads cost reach; music: licensed library is non-commercial and may be missing on business accounts, Sound Collection is commercial-safe.
- `w1b-other-platforms.md`: ranking beyond Instagram is Pinterest, YouTube Shorts, a Facebook Page by native cross-post, TikTok deferred. Pinterest needs a real URL per piece.
- `w1e-covers-thumbnails.md`: one 1080x1920 master with a hard-safe square at x 90-990, y 420-1500; Pinterest wants its own 1000x1500; six cover templates with coordinates; Shorts custom thumbnails need Studio on a computer.
- `w1h-capture-ingest.md` (if present when you start): phone gear, editing apps, ingest options. Read it before costing ingest/edit.
- `C:\Users\ethan\dev\Chief Of Staff\wiki\social-comment-ai.md`: Meta/TikTok approval gates. TikTok developer signup needs a company-domain email and a legal entity.

## Approval modes (design for both; do not choose)

(A) **Approve everything:** nothing publishes without a human tap (the "photos in, one line in, a draft out, Ricky taps Publish" pattern). (B) **Approve by exception:** the pipeline posts on schedule, replies to keyword comments with the listing link, and drafts everything else for approval. For each stage say what is safe in B and what must always be human (prices, claims about condition/age/provenance, anything about a person, replies to complaints, anything touching the fixed constraints). Include how a human gets pinged and approves from a phone (push, email, Telegram, Slack, a web page), with cost.

## Reply policy shape

A comment containing a keyword (LINK) gets the listing-page link and nothing else. Everything else becomes a draft for approval. No claims, no DM selling, no discounts. Check each tool against that shape and against the platform's rules on automated replies and DMs (messaging windows, private reply limits, disclosure).

**Wave 1 conflict you must resolve (w1c, unresolved there):** a URL typed in a public Instagram comment is not tappable (vendor claims; CommentSold and InstantDM-style tools deliver the link by DM or private reply instead). So "reply LINK with the link" works only through one of: (1) a public reply ("sent, check your DMs") plus a **DM or private reply carrying the listing link** (the comment-to-DM tools' pattern); (2) a Story link sticker; (3) link-in-bio plus a piece number that the listing page answers. Compare all three for the reply lane: platform rules and limits for private replies (once per comment? time window?), whether a link-only DM still satisfies "no DM selling / no claims" (it sends the buyer to the listing page, it does not take the claim), engagement-bait risk (w1a: unresolved whether "comment LINK" counts), cost, and which of the three the own-API path can do without App Review on our own account. State what Ricky must decide.

## Unofficial APIs

List them (for example reverse-engineered Instagram libraries) because Ricky will see them recommended online, but mark them clearly: ToS violation, ban risk to the one brand account, not recommended. Do not test them.

## Throwaway tests (allowed in wave 2, nowhere else)

You may run small tests on the Fedora box in `~/social-lab/<LANE>/` (user-local installs only: no sudo, no system changes, delete when done) and use the Windows PC's existing ffmpeg for read-only experiments. Never install on Windows, never sign up, never post, never DM, never log in, no paid APIs. Record exactly what you ran and the result. The Fedora ffmpeg has only the `libopenh264` stub (cannot decode phone H.264/HEVC); a lane that needs real ffmpeg on Fedora must test a user-local static build or a container and report whether it works there.

## Budgets

Searches at most 20, crawls at most 45, and **stay inside them** (wave 1 lanes overran by 2x). GitHub: only lane w2e may use more than 10 `gh` calls (its cap is 60); sleep 2 seconds between `gh search` calls. Reports at most about 3,500 words. Remember the heredoc fails on large reports: write the report with the Write tool in one call, or in several appended chunks, then `ls -l`.

## Output additions

Besides BRIEF.md's report shape, end with: **decision matrix** (option, stage, cost per month at the reference load, setup effort in hours, Claude/Codex-drivable yes/no, ban/ToS risk, approval-mode fit), and **build effort** (rough hours for Claude Code plus Codex to wire the recommended path, and what Ricky still does by hand).
