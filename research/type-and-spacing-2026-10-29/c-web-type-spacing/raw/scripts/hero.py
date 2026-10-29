from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
D="C:/Users/ethan/dev/Vintage/site/assets/fonts/"
for fn,txt in (("bodoni-moda-normal-latin.woff2","Good taste."),("bodoni-moda-italic-latin.woff2","Bad influence."),("bodoni-moda-italic-latin.woff2","Bad influence.")):
    f=TTFont(D+fn)
    print(fn,[(a.axisTag,a.minValue,a.defaultValue,a.maxValue) for a in f["fvar"].axes])
    g=instancer.instantiateVariableFont(f,{"opsz":96,"wght":500},inplace=False)
    cm=g.getBestCmap(); hm=g["hmtx"]; up=g["head"].unitsPerEm
    w=sum(hm[cm[ord(c)]][0] for c in txt)/up
    n=len(txt)
    for trk in (0,-0.02,-0.055):
        wt=w+trk*n
        print(f"  '{txt}' {w:.3f}em (no kern) ; tracking {trk}: {wt:.3f}em -> fits 320px at {320/wt:.0f}px, 335px at {335/wt:.0f}px")
