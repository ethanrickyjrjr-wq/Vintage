#!/usr/bin/env bash
# usage: f.sh url name
R=/c/Users/ethan/dev/Vintage/research/type-and-spacing-2026-10-29/c-web-type-spacing/raw
PY=/c/Users/ethan/crawl4ai-venv/Scripts/python.exe
H=/c/Users/ethan/AppData/Local/Temp/claude/C--Users-ethan-dev-Vintage/a1eacbbb-39fd-497c-8e29-6513242fb666/scratchpad/h2t.py
{ echo "<!-- SOURCE: $1 (fetched $(date -u +%FT%TZ) via curl + html->text) -->"; echo; curl -sL --compressed --max-time 60 -A "Mozilla/5.0" "$1" | "$PY" -I "$H"; } > "$R/$2.md"
echo "$2 $(wc -c < $R/$2.md)"
