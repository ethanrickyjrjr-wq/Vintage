#!/usr/bin/env bash
# Cloud-session stand-in for crawl.sh (crawl4ai lives on the Windows box and the Fedora box only).
# Same contract: one URL in, one markdown file out with the source URL on the first line, warning under 1 KB.
# usage: tools/crawl-cloud.sh "<url>" [out.md] [--browser]      (default out: research/<host>-<utc>.md)
[ $# -ge 1 ] || { echo "usage: $0 \"<url>\" [out.md] [--browser]" >&2; exit 2; }
url=$1
out=${2:-research/$(echo "$url" | sed -E 's#https?://##; s#[^A-Za-z0-9.]+#_#g' | cut -c1-60)-$(date -u +%Y%m%dT%H%M%SZ).md}
mkdir -p "$(dirname "$out")"
NODE_PATH="${NODE_PATH:-$(npm root -g)}" node "$(dirname "$0")/fetchpage.cjs" "$url" "$out" "${3:-}"
