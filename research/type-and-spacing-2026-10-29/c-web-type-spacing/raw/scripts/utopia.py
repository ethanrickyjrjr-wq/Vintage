MINV,MAXV=360,1500
def clamp(minpx,maxpx,minv=MINV,maxv=MAXV):
    mn,mx=minpx/16,maxpx/16; s=(mx-mn)/((maxv-minv)/16)   # rem per rem of viewport
    inter=mn - s*(minv/16)
    return f"clamp({mn:.4f}rem, {inter:.4f}rem + {s*100:.4f}vw, {mx:.4f}rem)", (lambda v: min(maxpx,max(minpx, (inter*16)+ s*v)))
def row(name,minpx,maxpx):
    c,f=clamp(minpx,maxpx)
    z=2*f(MAXV/2)/f(MAXV)
    print(f"{name:12} {minpx:7.2f}->{maxpx:7.2f}px  {c}   @768={f(768):.1f}px @1024={f(1024):.1f}px  200%-zoom@1500 ratio {z:.2f}x")
b0min,b0max,r1,r2=16,18,1.2,1.25
print("Utopia steps, base 16->18, ratio 1.2->1.25, viewports 360->1500")
for n in range(-2,7):
    row(f"step {n:+d}", b0min*r1**n, b0max*r2**n)
print()
row("hero",56,130); row("hero(86 now)",86,130)
row("label",11,12)
# current site hero for comparison
f=lambda v: min(130,max(86,0.083*v))
print("current hero @360/768/1024/1500:",[round(f(v),1) for v in (360,768,1024,1500)], " 200%-zoom ratio", round(2*f(750)/f(1500),2))
print()
row("hero52",52,130); row("gutter",16,32); row("section",48,96); row("sec-gap",24,48)
# zoom reach: smallest zoom z<=3 (Firefox cap) and <=5 (Chrome) giving >=2x at V=1500
def reach(minpx,maxpx):
    c,f=clamp(minpx,maxpx); out={}
    for z in (2,3,5):
        out[z]=round(z*f(MAXV/z)/f(MAXV),2)
    return out
for nm,a,b in (("body",16,18),("h2",27.65,35.16),("h1",39.81,54.93),("hero52",52,130),("hero80",80,130),("hero86",86,130)):
    print(nm,"zoom 2/3/5x -> on-screen text growth vs 100% at 1500px:",reach(a,b))
