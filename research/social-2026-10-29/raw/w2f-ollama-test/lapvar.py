import sys, numpy as np
from PIL import Image
def lapvar(p, w=768):
    im = Image.open(p).convert("L"); h = int(im.height * w / im.width); a = np.asarray(im.resize((w, h)), dtype=np.float64)
    L = -4*a[1:-1,1:-1] + a[:-2,1:-1] + a[2:,1:-1] + a[1:-1,:-2] + a[1:-1,2:]
    return L.var()
for p in sys.argv[1:]:
    print(f"{lapvar(p):9.1f}  {p.split('/')[-1]}")
