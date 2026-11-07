"""Cut one photo with one rembg model, then try two mask repairs. Mask only; pixels come from the photo."""
import sys, time
import numpy as np, cv2
from PIL import Image, ImageOps
from scipy import ndimage
from rembg import new_session, remove

photo_path, model, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
img = ImageOps.exif_transpose(Image.open(photo_path)).convert('RGB')
img.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
rgb = np.asarray(img)
t = time.time()
rgba = np.array(remove(img, session=new_session(model), decontaminate=True))
secs = time.time() - t
alpha = rgba[..., 3]

def largest_component(mask):
    lab, n = ndimage.label(mask)
    if n == 0: return mask
    sizes = ndimage.sum(mask, lab, range(1, n + 1))
    return lab == (1 + int(np.argmax(sizes)))

def on_white(a):
    a3 = (a.astype(np.float32) / 255.0)[..., None]
    return Image.fromarray((rgb * a3 + 255 * (1 - a3)).astype(np.uint8))

mask = alpha > 127
main = largest_component(mask)
filled = ndimage.binary_fill_holes(main)
# closing: fills notches narrower than ~2*r without moving the outline much
r = max(8, int(0.015 * max(np.ptp(np.where(main)[0]), np.ptp(np.where(main)[1]))))
k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))
closed = cv2.morphologyEx(filled.astype(np.uint8), cv2.MORPH_CLOSE, k).astype(bool)
# convex hull: right for frames, mirrors, boxes, anything with no inward corners
cnts, _ = cv2.findContours(filled.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hull = np.zeros_like(filled, dtype=np.uint8)
if cnts:
    cv2.fillConvexPoly(hull, cv2.convexHull(max(cnts, key=cv2.contourArea)), 1)
hull = hull.astype(bool)

def merge(a, m):  # keep the soft original alpha, force 255 where the repair added pixels
    out = a.copy(); out[m & (a < 255)] = 255; return out

for name, a in (('raw', alpha), ('closed', merge(alpha, closed)), ('hull', merge(alpha, hull))):
    on_white(a).save(f'{out_dir}/{model}-{name}.jpg', quality=90)
added_closed = int((closed & ~mask).sum()); added_hull = int((hull & ~mask).sum())
print(f'{model}: {secs:.1f}s  object px {int(mask.sum())}  closing added {added_closed}  hull added {added_hull}')
