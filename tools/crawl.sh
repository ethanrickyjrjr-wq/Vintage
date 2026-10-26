#!/usr/bin/env bash
# Fetch one URL as markdown with crawl4ai. Works from Git Bash on this machine (and from WSL via its shim).
# usage: tools/crawl.sh "<url>" [out.md]      (default out: research/<host>-<timestamp>.md)
[ $# -ge 1 ] || { echo "usage: $0 \"<url>\" [out.md]" >&2; exit 2; }
url=$1
out=${2:-research/$(echo "$url" | sed -E 's#https?://##; s#[^A-Za-z0-9.]+#_#g' | cut -c1-60)-$(date -u +%Y%m%dT%H%M%SZ).md}
mkdir -p "$(dirname "$out")"
# -bc bypasses crawl4ai's shared cache (cross-call bleed seen at concurrency); env -u undoes the Bash tool's MSYS_NO_PATHCONV
env -u MSYS_NO_PATHCONV crawl4ai "$url" -o md -bc < /dev/null > "$out" 2>/dev/null
bytes=$(wc -c < "$out")
echo "$out ($bytes bytes)"
[ "$bytes" -ge 1024 ] || echo "WARNING: under 1 KB, likely a bot wall, not a page. Try Patchright or the Fedora container." >&2
