import urllib.request, urllib.parse, http.cookiejar, json, sys, time, collections, datetime
cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"),("Accept-Language","en-US,en;q=0.9")]
def get(url):
    r = op.open(url, timeout=30)
    return r.read().decode("utf-8","replace")
def series(kw, geo="US", t="today 5-y"):
    req = {"comparisonItem":[{"keyword":kw,"geo":geo,"time":t}],"category":0,"property":""}
    u = "https://trends.google.com/trends/api/explore?hl=en-US&tz=300&req="+urllib.parse.quote(json.dumps(req,separators=(",",":")))
    txt = get(u)
    d = json.loads(txt[txt.index("{"):])
    w = [x for x in d["widgets"] if x["id"]=="TIMESERIES"][0]
    u2 = "https://trends.google.com/trends/api/widgetdata/multiline?hl=en-US&tz=300&req="+urllib.parse.quote(json.dumps(w["request"],separators=(",",":")))+"&token="+w["token"]
    txt2 = get(u2)
    d2 = json.loads(txt2[txt2.index("{"):])
    return [(int(p["time"]), p["value"][0]) for p in d2["default"]["timelineData"]]
try:
    get("https://trends.google.com/trends/explore?geo=US&hl=en-US")
except Exception as e:
    print("cookie fetch:", e)
out = {}
for kw in sys.argv[1:]:
    try:
        s = series(kw)
        out[kw] = s
        json.dump(s, open('gt_'+kw.replace(' ','_')+'.json','w'))
        bym = collections.defaultdict(list)
        for ts,v in s:
            m = datetime.datetime.fromtimestamp(ts, datetime.UTC).month
            bym[m].append(v)
        import statistics
        row = " ".join(f"{m:02d}:{statistics.median(bym[m]):4.0f}" for m in range(1,13))
        print(f"{kw!r:28} n={len(s)} last={datetime.datetime.fromtimestamp(s[-1][0], datetime.UTC).date()}  {row}")
    except Exception as e:
        print(kw, "ERR", repr(e)[:200])
    time.sleep(25)

