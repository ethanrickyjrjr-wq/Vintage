# Social research plan and status (parent session notes, 2026-10-29)

Ask (Ricky, 2026-10-29): research Instagram and socials with groups of Sonnets after checking the desk wiki; deliver one step-by-step manual (what/when to post, covers that get clicks, growth, phone video to posted, what vintage/designer people do, mostly autonomous edits/covers/posting/replying with Claude + Codex), all pricing and signup links; GitHub and Hugging Face automation included; write a handoff if needed.

Shared brief: `BRIEF.md` (constraints, tool rules, evidence tags, report shape). Advisor-reviewed plan below.

## Wave 1: strategy (8 lanes, launched 2026-10-29)
- w1a-ig-rules-timing: Instagram's own ranking/rules, policies, timing and frequency; clipfeed on at most 5 Mosseri/Instagram-official videos
- w1b-other-platforms: TikTok, YouTube Shorts, Pinterest, Facebook (Reels, Groups, Marketplace), Threads, Whatnot, Poshmark, Depop; rank for this niche
- w1c-content-hooks: hooks, captions, formats; clipfeed on at most 15 top vintage/decor reels (transcript + engagement)
- w1d-audience-calendar: who buys, trends, 12-month seasonal calendar Nov 2026 to Oct 2027, SWFL angle
- w1e-covers-thumbnails: cover/thumbnail specs and click evidence, H&V cover system
- w1f-dealers-resellers: 15-20 more vintage dealers/resellers (not the d1 12), monetization, growth stories
- w1g-designers-stylists: designers/stylists/stagers/prop people, service funnels (Hire Hollie)
- w1h-capture-ingest: phone gear, shooting recipes, edit apps, phone-to-pipeline ingest options

## Wave 2: automation (7 lanes, after wave 1)
Shared stage taxonomy for finds: ingest > edit > caption > cover > publish > reply > analytics. Each find: stage, stars, last push, license (gh api), CPU or hosted, hosted price.
- w2a-editing: FFmpeg/Remotion/auto-editor vs SaaS (Descript, Opus, Submagic, Captions, CapCut) vs JSON-to-video APIs (Shotstack, Creatomate)
- w2b-cover-automation: HTML-to-PNG (Playwright/Satori), Canva API, Bannerbear/Placid, best-frame pick, A/B testing
- w2c-publish-apis: per platform compare native scheduling vs third-party scheduler (own approved app) vs own API app; TikTok unaudited posts private-only? ; Buffer/Publer/Metricool/Postiz/Ayrshare/Blotato/Upload-Post/n8n/Make/Zapier
- w2d-reply-dm: Meta Graph comments/private replies, ManyChat, CommentSold CommentChat, Meta native automations, policy limits; keyword comment gets link, everything else drafted for approval
- w2e-github-scan: open source social/content pipelines (stage taxonomy; gh budget about 60 calls)
- w2f-hf-scan: Hugging Face models/Spaces CPU-runnable or hosted-with-price
- w2g-runtime: where it runs (Claude routines, GH Actions, Fedora, Windows, Supabase/Vercel), ffmpeg on Fedora (static user ffmpeg vs podman image vs Windows), Claude vs Codex roles, approval UX, monthly cost

## Wave 3: verification and delivery
- Re-read every price and signup link in the finalist stack live; walled Meta pages via Ricky's signed-in Chrome (parent only, not subagents)
- Deliverables: `docs/social-manual.md` (three tiers: native free / one paid scheduler + editor / full Claude+Codex pipeline; steps ordered claim handles > Professional account > link Facebook Page > scheduler > content > automation; each step has link, price, accessed date, source) and `docs/codex-handoff-social-autopilot.md` (build spec)
- Then `/compile`, commit only own paths (`git commit -- paths`), pull --rebase, push

## Open questions for Ricky (surface in the manual)
- Does Hollie approve each post before it goes live, or approve by exception?
- Is `@holliewoodandvine` yours? Is there a legal entity (needed for Meta Business Verification and TikTok developer signup)?
- Apify spend for measured competitor engagement data? Not authorized; clipfeed used instead.
- Hollie on camera or hands only?

## Corrections found by wave 1
- A Facebook Page is NOT a prerequisite for Instagram-only publishing (w1a, Meta developer docs: Unified Login and Instagram Login need no Page; own-account API use is Standard Access with no App Review). Page is still needed for Facebook posting, cross-posting, some ads/shopping tools. Wave 3 step order: claim handles > Business account > scheduler/API > (Page only when Facebook posting starts).
- hire.html line 121 and docs/fabulous-from-online-design.md line 87 carry "10% off each room after the first" (Full Production). Ricky approved the written prices; w1g flags it against the no-discounts rule. Ricky decides; not changed.

## Status log
- 2026-10-29: BRIEF.md and PLAN.md written. Wave 1 launching.
- 2026-10-29: wave 1 reports saved: w1a (saved by parent from inline return), w1b, w1e, w1f, w1g. Still running: w1c (hooks, clipfeed), w1d (calendar), w1h (capture/ingest).
