import io, math
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from PIL import Image, ImageDraw, ImageFont
D="C:/Users/ethan/dev/Vintage/site/assets/fonts/"
def runs_line(px,w,h,axis,idx):
    out=[];run=0
    for k in range(h if axis=="v" else w):
        v=px[idx,k] if axis=="v" else px[k,idx]
        if v>128: run+=1
        elif run: out.append(run);run=0
    if run: out.append(run)
    return out
def thin(font,S=4000):
    b=io.BytesIO(); font.flavor=None; font.save(b); b.seek(0)
    pf=ImageFont.truetype(b,S)
    im=Image.new("L",(int(S*1.4),int(S*1.8)),0); ImageDraw.Draw(im).text((100,100),"o",font=pf,fill=255)
    x0,y0,x1,y1=im.getbbox(); cx=(x0+x1)//2; cy=(y0+y1)//2
    w,h=im.size; px=im.load()
    return min(runs_line(px,w,h,"v",cx))/S*1000, max(runs_line(px,w,h,"h",cy))/S*1000   # in 1/1000 em
def inst(opsz,wght):
    return instancer.instantiateVariableFont(TTFont(D+"bodoni-moda-normal-latin.woff2"),{"opsz":opsz,"wght":wght},inplace=False)
print("hairline (thin of 'o', 1/1000 em) and stem (thick) by opsz x wght")
tab={}
for wg in (400,500,600,700):
    for op in (6,11,16,24,36,48,96):
        t,k=thin(inst(op,wg)); tab[(op,wg)]=t
        print(f" wght {wg} opsz {op:>2}: hairline {t:5.1f}  stem {k:5.1f}")
print("\nhairline in CSS px for font-size s: auto (opsz=s, clamped 6..96) vs forced opsz 6, wght 400/500")
def hl(s,mode,wg):
    op = min(96,max(6,s)) if mode=="auto" else 6
    # interpolate from table nearest grid of opsz via linear in log? just measure directly
    return thin(inst(op,wg))[0]*s/1000
for s in (11,12,14,16,18,20,24,32,48,96,130):
    a4=hl(s,"auto",400); a5=hl(s,"auto",500); f4=hl(s,"six",400); f5=hl(s,"six",500)
    print(f" {s:>3}px  auto400 {a4:.2f}px  auto500 {a5:.2f}px | opsz6-forced 400 {f4:.2f}px 500 {f5:.2f}px")
# contrast
def lin(c): c/=255; return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
def lum(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16) for i in (0,2,4)]; return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def cr(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb); return (hi+0.05)/(lo+0.05)
def blend(fg,bg,a):
    f=fg.lstrip('#'); g=bg.lstrip('#')
    return '#%02x%02x%02x'%tuple(round(int(g[i:i+2],16)+(int(f[i:i+2],16)-int(g[i:i+2],16))*a) for i in (0,2,4))
print("\nContrast on --paper #422831 / --wall #652b40:")
for name,c in (("text","#f6efdf"),("muted","#d1bdb8"),("rust","#e5a6b4"),("line","#79545e")):
    print(f" {name} {c}: on paper {cr(c,'#422831'):.2f}  on wall {cr(c,'#652b40'):.2f}")
print(" hairline coverage -> effective colour contrast vs bg (text on paper):")
for a in (0.1,0.2,0.3,0.5,1.0):
    bc=blend('#f6efdf','#422831',a); print(f"  coverage {a:.1f}: {bc} contrast {cr(bc,'#422831'):.2f}")
# fallback math
print("\nFallback overrides (Capsize 4.4.0 metrics):")
def fb(web, fbk):
    wUPM,wasc,wdes,wgap,wavg=web; fUPM,favg=fbk[0],fbk[1]
    sa=(wavg/wUPM)/(favg/fUPM)
    return sa, wasc/(wUPM*sa), abs(wdes)/(wUPM*sa), wgap/(wUPM*sa)
dm=(1000,992,-310,0,466); bm=(2000,2250,-800,0,928)
arial=(2048,913); tnr=(2048,832); geo=(2048,913)
for nm,w,f in (("DM Sans vs Arial",dm,arial),("Bodoni Moda vs Times New Roman",bm,tnr),("Bodoni Moda vs Georgia",bm,geo)):
    sa,a,d,g=fb(w,f); print(f" {nm}: size-adjust {sa*100:.2f}%  ascent {a*100:.2f}%  descent {d*100:.2f}%  line-gap {g*100:.2f}%")
# Space Mono vs Courier New: advance 612 vs 1229/2048
sm=(1000,1120,-361,0,612); cn=(2048,1229)
sa,a,d,g=fb(sm,cn); print(f" Space Mono vs Courier New(adv 1229/2048, [U] value from memory): size-adjust {sa*100:.2f}% ascent {a*100:.2f}% descent {d*100:.2f}%")
# hero word widths
f=inst(96,400); cmap=f.getBestCmap(); hm=f["hmtx"]; up=f["head"].unitsPerEm
for word in ("Holliewood","HOLLIEWOOD","Holliewood & Vine","and Vine","Hollie"):
    w=sum(hm[cmap[ord(c)]][0] for c in word)/up
    print(f" '{word}' advance (no kerning, opsz96 wght400): {w:.3f} em -> max font px in 320px: {320/w:.0f}, in 335px: {335/w:.0f}")
