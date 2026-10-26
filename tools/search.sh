#!/usr/bin/env bash
# Web search through the Fedora box's SearXNG (free, JSON, no key). Finds URLs; crawl4ai fetches them.
# usage: tools/search.sh "query" [category]      category: general (default) | science | news
[ $# -ge 1 ] || { echo "usage: $0 \"query\" [category]" >&2; exit 2; }
q=$(python -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$1")
cat=${2:-general}
ssh -o BatchMode=yes -o ConnectTimeout=10 fedora \
  "curl -s 'http://127.0.0.1:8888/search?format=json&categories=$cat&q=$q'" \
  | python -c 'import sys,json; d=json.load(sys.stdin); [print(r.get("url",""), "|", r.get("title","").strip(), "|", r.get("engine","")) for r in d.get("results",[])]'
