from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.boundsPen import BoundsPen
D="C:/Users/ethan/dev/Vintage/site/assets/fonts/"
def bounds(font,ch):
    gs=font.getGlyphSet(); n=font.getBestCmap()[ord(ch)]; bp=BoundsPen(gs); gs[n].draw(bp); return bp.bounds
def rep(name,fn,axes):
    f=TTFont(D+fn)
    g=instancer.instantiateVariableFont(f,axes,inplace=False) if axes else f
    up=g["head"].unitsPerEm
    x=bounds(g,"x"); o=bounds(g,"o"); H=bounds(g,"H")
    print(f"{name} {axes}: x yMax {x[3]/up:.3f}em  (o yMax {o[3]/up:.3f}, overshoot incl)  H yMax {H[3]/up:.3f}em  OS/2 sxHeight {g['OS/2'].sxHeight/up:.3f}")
for op in (9,14,16,24):
    rep("DM Sans","dm-sans-normal-latin.woff2",{"opsz":op,"wght":400})
rep("Space Mono","space-mono-normal-latin.woff2",None)
rep("Bodoni","bodoni-moda-normal-latin.woff2",{"opsz":24,"wght":400})
print("Arial per Capsize: xHeight 1062/2048 =",round(1062/2048,4),"capHeight",round(1467/2048,4))
