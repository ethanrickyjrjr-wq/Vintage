import json,sys
sys.stdout.reconfigure(encoding="utf-8")
d=json.load(open(sys.argv[1],encoding="utf-8"))
out=[]
def walk(n):
    if isinstance(n,dict):
        if n.get("type")=="text" and "text" in n: out.append(n["text"])
        elif n.get("type") in ("codeVoice",) and "code" in n: out.append(n["code"])
        for k,v in n.items():
            if k in("text","type","code") and n.get("type") in("text","codeVoice"): continue
            walk(v)
        if n.get("type") in ("paragraph","heading","listItem","tableRow","row"): out.append("\n")
    elif isinstance(n,list):
        for x in n: walk(x)
walk(d.get("primaryContentSections",[]))
print("".join(out))
