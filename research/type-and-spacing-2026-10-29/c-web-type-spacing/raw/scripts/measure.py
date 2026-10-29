import io, sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from PIL import Image, ImageDraw, ImageFont
D="C:/Users/ethan/dev/Vintage/site/assets/fonts/"
FREQ=dict(e=12.70,t=9.06,a=8.17,o=7.51,i=6.97,n=6.75,s=6.33,h=6.09,r=5.99,d=4.25,l=4.03,c=2.78,u=2.76,m=2.41,w=2.36,f=2.23,g=2.02,y=1.97,p=1.93,b=1.49,v=0.98,k=0.77,j=0.15,x=0.15,q=0.10,z=0.07)
def info(name):
    f=TTFont(D+name)
    print("==",name,"UPM",f["head"].unitsPerEm)
    if "fvar" in f: print(" axes:",[(a.axisTag,a.minValue,a.defaultValue,a.maxValue) for a in f["fvar"].axes])
    h=f["hhea"];o=f["OS/2"]
    print(" hhea asc/desc/gap",h.ascent,h.descent,h.lineGap," typo",o.sTypoAscender,o.sTypoDescender,o.sTypoLineGap," win",o.usWinAscent,o.usWinDescent," USE_TYPO",bool(o.fsSelection&128)," xAvgCharWidth",o.xAvgCharWidth," capH",getattr(o,'sCapHeight',None)," xH",getattr(o,'sxHeight',None))
    return f
def avgw(f, space_share=None):
    cmap=f.getBestCmap(); hm=f["hmtx"]; upm=f["head"].unitsPerEm
    tot=sum(FREQ.values()); w=sum(FREQ[c]*hm[cmap[ord(c)]][0] for c in FREQ)/tot
    sp=hm[cmap[32]][0]
    # with space at ~17.5%
    w_sp=(w*(1-0.175)+sp*0.175)
    return w/upm, w_sp/upm
def inst(f, **axes):
    g=TTFont(io.BytesIO(_save(f)))
    return instancer.instantiateVariableFont(g, axes, inplace=False)
def _save(f):
    b=io.BytesIO(); f.flavor=None; f.save(b); return b.getvalue()
def runs(img, axis, idx):
    # return list of ink runs along a line
    w,h=img.size; px=img.load(); out=[]; run=0
    rng = range(h) if axis=="v" else range(w)
    for k in rng:
        v = px[idx,k] if axis=="v" else px[k,idx]
        if v>128: run+=1
        elif run: out.append(run); run=0
    if run: out.append(run)
    return out
def stroke_metrics(font):
    b=io.BytesIO(); font.flavor=None; font.save(b); b.seek(0)
    S=1000
    pf=ImageFont.truetype(b,S)
    res={}
    # 'o': thin = vertical ink run through center column; thick = horizontal run at mid x-height row
    im=Image.new("L",(1400,1800),0); d=ImageDraw.Draw(im); d.text((100,100),"o",font=pf,fill=255)
    bbox=im.getbbox(); x0,y0,x1,y1=bbox; cx=(x0+x1)//2; cy=(y0+y1)//2
    vr=runs(im,"v",cx); hr=runs(im,"h",cy)
    res["o_thin"]=min(vr) if vr else None; res["o_thick"]=max(hr) if hr else None
    # 'H': crossbar vertical run at center column; stem horizontal run at 20% height from bottom
    im=Image.new("L",(1800,1800),0); d=ImageDraw.Draw(im); d.text((100,100),"H",font=pf,fill=255)
    x0,y0,x1,y1=im.getbbox(); cx=(x0+x1)//2; ry=y1-int((y1-y0)*0.15)
    vr=runs(im,"v",cx); hr=runs(im,"h",ry)
    res["H_bar"]=max(vr) if vr else None; res["H_stem"]=max(hr) if hr else None
    return res
if __name__=="__main__":
    bm=info("bodoni-moda-normal-latin.woff2"); dm=info("dm-sans-normal-latin.woff2"); sm=info("space-mono-normal-latin.woff2")
    print("\n-- avg char width (freq-weighted a-z | with ~17.5% space), em")
    print(" Bodoni default:",avgw(bm)); print(" DM Sans default:",avgw(dm)); print(" Space Mono:",avgw(sm))
    print(" Capsize ref: Bodoni 928/2000=%.4f DM Sans 466/1000=%.4f Arial 913/2048=%.4f TNR 832/2048=%.4f Georgia 913/2048=%.4f"%(928/2000,.466,913/2048,832/2048,913/2048))
    print("\n-- Bodoni Moda wght 400: width and stroke vs opsz")
    for opsz in (6,11,14,16,24,36,48,72,96):
        g=instancer.instantiateVariableFont(TTFont(D+"bodoni-moda-normal-latin.woff2"),{"opsz":opsz,"wght":400,"wght":400},inplace=False) if False else None
    rows=[]
    for opsz in (6,11,14,16,24,36,48,72,96):
        f=TTFont(D+"bodoni-moda-normal-latin.woff2")
        g=instancer.instantiateVariableFont(f,{"opsz":opsz,"wght":400},inplace=False)
        a,b=avgw(g); m=stroke_metrics(g)
        print(" opsz %3d  avgW(a-z) %.4f  avgW(+sp) %.4f   o_thin %s/1000em  o_thick %s  contrast %.1f  H_bar %s H_stem %s"%(opsz,a,b,m["o_thin"],m["o_thick"],m["o_thick"]/max(m["o_thin"],1),m["H_bar"],m["H_stem"]))
    print("\n-- DM Sans default+400 and opsz 9/14/40 avg width")
    for opsz in (9,14,24,40):
        f=TTFont(D+"dm-sans-normal-latin.woff2")
        g=instancer.instantiateVariableFont(f,{"opsz":opsz,"wght":400},inplace=False)
        print(" DM Sans opsz",opsz,avgw(g))
