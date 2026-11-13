#!/usr/bin/env python3
"""Just-listed reel PoC: title card, 3 stills (slow zoom, crossfades), end card. Needs only ffmpeg 6.x.
usage: python3 make_poc.py [out.mp4]"""
import subprocess, sys, os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
os.chdir(root)
A = "assets/ebay-2026-11-08/ebay/06-starlo-red-abstract-vintage-dress"
F = "assets/brand/fonts"; WM = "assets/brand/holliewood-and-vine-wordmark-cream.png"
BG, CREAM, NEON = "0x451c2b", "0xf6efdf", "0xff2f92"
TITLE, SUB, PRICE = "Vintage 80s Starlo", "red moire pleated midi", "$48"  # PRICE is a placeholder
out = sys.argv[1] if len(sys.argv) > 1 else "research/instagram-video-2026-11-13/poc/just-listed-poc.mp4"
D, X = 2.6, 0.4   # scene seconds, crossfade seconds
BOD = f"{F}/BodoniModa[opsz,wght].ttf"; MONO = f"{F}/SpaceMono-Regular.ttf"; MONOB = f"{F}/SpaceMono-Bold.ttf"
def dt(font, text, color, size, x, y, extra=""):
    return f"drawtext=fontfile='{font}':text='{text}':fontcolor={color}:fontsize={size}:x={x}:y={y}{extra}"
parts = []
# scene 0: title card (inputs: 0..2 photos, 3 wordmark)
parts.append(f"color=c={BG}:s=1080x1920:r=30:d={D}[t0]")
parts.append(f"[3:v]scale=800:-1,format=rgba[wm]")
parts.append(f"[t0][wm]overlay=(W-w)/2:620,{dt(MONOB,'JUST LISTED',NEON,76,'(w-text_w)/2',1000)},{dt(MONO,SUB,CREAM,38,'(w-text_w)/2',1130)},format=yuv420p,setsar=1[s0]")
labels = ["front", "back", "tag close-up"]
for i, lab in enumerate(labels):
    n = D*30
    parts.append(f"[{i}:v]scale=960:1240:force_original_aspect_ratio=decrease,pad=960:1240:(ow-iw)/2:(oh-ih)/2:white,scale=1920:2480,"
                 f"zoompan=z='1+0.10*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=960x1240:fps=30[p{i}]")
    parts.append(f"color=c={BG}:s=1080x1920:r=30:d={D}[b{i}]")
    parts.append(f"[b{i}][p{i}]overlay=60:380:shortest=1,"
                 + dt(BOD, TITLE, CREAM, 84, "(w-text_w)/2", 170) + ","
                 + dt(MONO, SUB, CREAM, 36, "(w-text_w)/2", 290) + ","
                 + dt(MONOB, lab, NEON, 40, "(w-text_w)/2", 1700) + ","
                 + dt(MONOB, PRICE, BG, 64, "w-text_w-90", 1560, f":box=1:boxcolor={CREAM}:boxborderw=22")
                 + f",format=yuv420p,setsar=1[s{i+1}]")
# end card
parts.append(f"color=c={BG}:s=1080x1920:r=30:d={D}[e0]")
parts.append(f"[e0]{dt(BOD,'Piece No. 06',CREAM,90,'(w-text_w)/2',800)},{dt(MONOB,'LINK IN BIO',NEON,72,'(w-text_w)/2',980)},"
             f"{dt(MONO,'@holliewoodandvine',CREAM,38,'(w-text_w)/2',1100)},format=yuv420p,setsar=1[s4]")
# crossfade chain
prev = "s0"; off = D - X
for k in range(1, 5):
    parts.append(f"[{prev}][s{k}]xfade=transition=fade:duration={X}:offset={off:.2f}[x{k}]")
    prev = f"x{k}"; off += D - X
total = 5*D - 4*X
cmd = ["ffmpeg","-y","-hide_banner","-loglevel","error",
       *sum([["-loop","1","-t",str(D+0.1),"-i",f"{A}-{k}.jpg"] for k in ("front","back","tag")],[]),"-loop","1","-t",str(D),"-i",WM,
       "-f","lavfi","-t",f"{total:.2f}","-i","anullsrc=r=48000:cl=stereo",
       "-filter_complex",";".join(parts),"-map",f"[{prev}]","-map","4:a",
       "-c:v","libx264","-profile:v","high","-pix_fmt","yuv420p","-r","30","-crf","20","-preset","medium",
       "-g","60","-bf","2","-movflags","+faststart","-c:a","aac","-b:a","128k","-ar","48000","-ac","2","-t",f"{total:.2f}",out]
subprocess.run(cmd, check=True)
print("wrote", out, f"{total:.1f}s")
