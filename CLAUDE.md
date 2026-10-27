# Vintage

**Status (2026-10-26):** Vintage is Ricky's vintage resale shop, **Holliewood and Vine**. A physical room already exists
(burgundy walls, racks, lamps, art, a pink "do it for the plot" neon); the job is to put it online on
Etsy and Shopify, probably with its own site later. First pass done 2026-10-26: Drive folder of 10
photos + a 24 s walkthrough video pulled, inventory catalogued in `research/inventory/`, comps priced
by Sonnet subagents into `research/pricing/`, sample storefront built as an artifact. Photos and
video frames live in `assets/` (previews only; originals stay in Ricky's Drive). Next: Ricky re-shoots
the "needs photo" items. Shop name (Ricky, corrected 2026-10-27): **Holliewood and Vine** or
**Holliewood & Vine**. The spelling is **Hollie**, with **ie**.

**Dashboard (2026-10-26):** ops dashboard researched (ten Sonnet reports in `research/dashboard/`) and
designed: `docs/dashboard-design.md` (what and why) and `docs/dashboard-handoff.md` (build order, smoke
tests, schema deltas). Same day, Ricky's call: listing from the phone is in Phase 1 (photos plus one
line in, Claude Haiku drafts, Etsy draft listing, Ricky taps Publish, Crosslist imports from Etsy and
fans out to eBay and Shopify; handoff T6b, smoke tests 13 and 14, an Anthropic key in section 0).
Nothing built. Step 0 is blocked on Ricky creating the eBay, Etsy, Shopify, Supabase Pro and Anthropic
accounts and keys (handoff section 0). The next build session starts at the handoff.

Drive folder (Ricky's second Google account, `u/1`): https://drive.google.com/drive/u/1/folders/1doMLpzt09qxtbSOjWFkBOCYSQQnb3HYD
The Claude Drive connector is on the other account and cannot see it; fetch through the signed-in
Chrome tab (Drive folder menu > Download gives one zip) or ask Ricky to share to the connector account.

**Storefront direction (2026-10-26):** The original room is a reference for the designer's taste and
composition, not a claim of an operating physical store. The site should feel like entering that
world: dimensional lettering, objects in the foreground, varied framed displays and deliberate
overlaps. Disco balls are signature gifts/handouts for buyers (confirmed by Ricky); do not infer an
every-order guarantee. Implemented direction and asset provenance: `docs/storefront-art-direction.md`.

**Photo direction (2026-10-27):** Ricky wants whole, polished product photographs on white framed
panels, including the room decorator, while keeping the entrance cutouts, original neon-lit store
photo and existing mouse movement. The private `/demo` review now uses 52 selected photographs from
the photo-sourcing work; one list supplies both catalog images and room layers. Rough item photos,
stills and the unfinished selfie are omitted from that preview. See `docs/demo-photo-pack.md`.

Global rules (`~/.claude/CLAUDE.md`) apply: Vendor First, Plan Mode First, shell syntax matches the
tool, Claude pushes. Standalone workspace: nothing here touches brain-platform / SWFL Data Gulf.

## crawl4ai (the page fetcher, verified working from this folder 2026-10-26)

One machine-wide install, never reinstalled per project:

- Interpreter: `C:\Users\ethan\crawl4ai-venv\Scripts\python.exe`
- Git Bash shim: `C:\Users\ethan\.local\bin\crawl4ai` · PowerShell shim: `crawl4ai.cmd` beside it
- WSL shim: `~/.local/bin/crawl4ai` (execs the Windows venv; there is NO WSL-native venv)
- Fedora box: podman container `crawl4ai`, REST on `127.0.0.1:11235` (health 200 on 2026-10-26)

Call it:

```bash
tools/crawl.sh "<url>"                 # writes research/<host>-<utc>.md, warns under 1 KB
env -u MSYS_NO_PATHCONV crawl4ai "<url>" -o md -bc < /dev/null > out.md   # the raw form
```

Rules that cost real time before: always `< /dev/null` (it eats stdin in loops); always `env -u
MSYS_NO_PATHCONV` in the Bash tool (else exit 2, zero bytes, looks like a wall); always `-bc` plus a
unique output file when calls run concurrently (cross-call content bleed); under 1 KB is a bot wall,
not a page. Walls and workarounds: `dev/Chief Of Staff/wiki/crawl4ai.md`. Patchright is the
fallback for Cloudflare walls (`wiki/patchright.md`).

## Web search

SearXNG on the Fedora box, free, JSON, no key. `tools/search.sh "query" [general|science|news]`
prints `url | title | engine`. Then crawl the URL. Engines answering as of 2026-10-06: google cse,
bing, yahoo (science: scholar, semantic scholar, arxiv, europepmc). DuckDuckGo and Brave are dead
from that box. Details: `wiki/searxng.md`.

## Fedora box

`ssh fedora` (10.0.0.169, user `stanicky`, key `~/.ssh/fedora_stanicky`, in `~/.ssh/config`).
Always-on second runner on a second residential IP. CPU only (i7-8565U, 15 GB, no GPU), no sudo,
rootless podman, Python 3.14, Claude Code installed. Running there 2026-10-26: `crawl4ai`,
`searxng`, `ollama-agents` (qwen3.5:4b, ~7 tok/s), `beszel-hub`/`beszel-agent`.
Loopback-only services, so tunnel when a local client needs one:
`ssh -L 8888:127.0.0.1:8888 fedora`. Never edit a script a runner is executing; clone per session.
Inventory and gotchas: `wiki/machine-stack.md`, `wiki/shell-and-wsl-gotchas.md`.

## Keys

`.env.local` is a byte copy of the desk key store (`dev/Chief Of Staff/.env`) taken 2026-10-26,
gitignored. `.env.example` has the names only. Load with `set -a; . ./.env.local; set +a` in bash.
A new key goes into the desk `.env` first, then here. Never into brain-platform.

## Layout

- `research/` — fetched pages and notes, dated, with the source URL at the top. Raw layer, never rewritten.
- `tools/` — `crawl.sh`, `search.sh`. Add a script only when a third session would otherwise retype it.
- `docs/` — design and handoff documents (synthesis, decisions). Rewritten as decisions change.
- Anything worth keeping past this folder (a decision, a verified vendor fact, a lesson) goes to the
  desk wiki with `/compile <path>`; the wiki lives in `dev/Chief Of Staff/wiki/`.

## Git

Remote `origin` = github.com/ethanrickyjrjr-wq/Vintage (seen 2026-10-26). Every time a task lands:
`git pull --rebase`, secrets grep, commit, push. Structure changes (rename, delete, visibility) still need Ricky's word.
