# Vintage

**Status (2026-10-26):** Day 0. Ricky asked for the folder; he has not yet said what Vintage is.
Do not invent a purpose from the name. Ask him in one line, then record his answer here.

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
- Anything worth keeping past this folder (a decision, a verified vendor fact, a lesson) goes to the
  desk wiki with `/compile <path>`; the wiki lives in `dev/Chief Of Staff/wiki/`.

## Git

Local repo. A GitHub remote is a structure change and needs Ricky's word (`wiki/github-repos.md`).
Once one exists: `git pull --rebase`, secrets grep, commit, push, every time a task lands.
