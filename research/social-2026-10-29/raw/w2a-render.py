#!/usr/bin/env python3
"""render.py edl.json [--dry]: edit decision list -> ONE ffmpeg command -> ffprobe asserts. stdlib only
(fontTools optional, only for the text-width lint). Env: FFMPEG, FFPROBE. ponytail: constant speed per clip
(a ramp = split into two clips), silent clips + one music bed; speech clips go through captions, not here."""
import json, os, re, subprocess, sys, shlex
FF, FP = os.environ.get("FFMPEG", "ffmpeg"), os.environ.get("FFPROBE", "ffprobe")
W, H, FPS, BG, CREAM, SCRIM = 1080, 1920, 30, "0x451c2b", "0xf6efdf", "0x321520@0.55"
HDR = ("arib-std-b67", "smpte2084")
TONEMAP = "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:desat=0,zscale=t=bt709:m=bt709:r=tv"

def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)

def width(font, txt, size):  # lint only; kerning ignored
    try: from fontTools.ttLib import TTFont
    except ImportError: return None
    f = TTFont(font); cm, hm, u = f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm
    return sum(hm[cm[ord(c)]][0] for c in txt if ord(c) in cm) * size / u

def texts(edl, work, font, lines, size, y0, t0, t1, lh=1.15):
    out = []
    for i, ln in enumerate(lines):
        w = width(font, ln, size)
        if w and w > 950: sys.exit(f"LINT: '{ln}' is {w:.0f}px wide at {size}px, safe width is 950 (x 65-1015)")
        p = f"{work}/t{abs(hash((ln, y0)))}.txt"; open(p, "w", encoding="utf-8").write(ln)
        out.append(f"drawtext=fontfile={font}:textfile={p}:fontsize={size}:fontcolor={CREAM}:x=(w-text_w)/2:y={int(y0 + i * size * lh)}"
                   f":box=1:boxcolor={SCRIM}:boxborderw=20:enable='between(t,{t0},{t1})'")
    return ",".join(out)

def build(edl, work):
    clips, o, mu = edl["clips"], edl.get("out", {}), edl.get("music")
    F = edl["fonts"]; ins, parts, labels, dur = [], [], [], 0.0
    for i, c in enumerate(clips):
        sp = c.get("speed", 1.0); d = c["out"] - c["in"]; dur += d / sp
        ins += ["-ss", str(c["in"]), "-t", str(d), "-i", c["src"]]
        t = json.loads(run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=color_transfer", "-of", "json", c["src"]]).stdout)["streams"][0]
        sc = (f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H}" if c.get("fit", "cover") == "cover"
              else f"scale={W}:{H}:force_original_aspect_ratio=decrease:flags=lanczos,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:{BG}")
        tm = f",{TONEMAP}" if t.get("color_transfer") in HDR else ""  # scale first, tone-map at 1080p, not 4K float
        parts.append(f"[{i}:v:0]{sc}{tm},format=yuv420p,setsar=1,setpts=(PTS-STARTPTS)/{sp},fps={FPS}[v{i}]"); labels.append(f"[v{i}]")
    hook_end = min(edl["hook"].get("t1", 3.0), dur) if "hook" in edl else 0
    ec = edl.get("end_card")
    if ec:
        e0 = dur; dur += ec["dur"]
        ch = [texts(edl, work, F["bodoni"], ec["lines"], ec.get("size", 150), 560, 0, 99)]
        if ec.get("sub"): ch.append(texts(edl, work, F["dm"], [ec["sub"]], 64, 1000, 0, 99))
        if ec.get("credit"): ch.append(texts(edl, work, F["dm"], ec["credit"], 34, 1120, 0, 99))
        parts.append(f"color=c={BG}:s={W}x{H}:r={FPS}:d={ec['dur']},format=yuv420p,{','.join(ch)}[ve]"); labels.append("[ve]")
    hk = edl.get("hook")
    hd = texts(edl, work, F["bodoni"], hk["lines"], hk.get("size", 104), hk.get("y", 560), 0, hook_end) if hk else "null"
    parts.append(f"{''.join(labels)}concat=n={len(labels)}:v=1:a=0[vc]")
    parts.append(f"[vc]{hd},sidedata=mode=delete,setparams=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv[v]")
    n = len(clips)
    if mu["src"].startswith("tone:"): ins += ["-f", "lavfi", "-i", f"sine=frequency={mu['src'][5:]}:sample_rate=48000"]
    else: ins += ["-stream_loop", "-1", "-ss", str(mu.get("start", 0)), "-i", mu["src"]]
    fi, fo = mu.get("fade_in", 0.5), mu.get("fade_out", 1.5)
    bed = (f"[{n}:a]atrim=0:{dur:.3f},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,"
           f"afade=t=in:st=0:d={fi},afade=t=out:st={dur - fo:.3f}:d={fo},volume={mu.get('gain_db', 0)}dB")
    I, TP = mu.get("lufs", -14), mu.get("tp", -1.5)
    p1 = run([FF, "-nostdin", "-hide_banner", "-v", "info"] + ins + ["-filter_complex", bed + f",loudnorm=I={I}:TP={TP}:LRA=11:print_format=json[x]", "-map", "[x]", "-f", "null", "-"])
    m = json.loads(re.findall(r"\{[^{}]*\}", p1.stderr)[-1])
    ln = (f"loudnorm=I={I}:TP={TP}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000")
    parts.append(f"{bed},{ln}[a]")
    cmd = [FF, "-y", "-hide_banner", "-nostdin"] + ins + ["-filter_complex", ";".join(parts), "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}",
           "-c:v", "libx264", "-preset", o.get("preset", "medium"), "-crf", str(o.get("crf", 18)), "-profile:v", "high", "-level", "4.1", "-pix_fmt", "yuv420p",
           "-maxrate", "12M", "-bufsize", "24M", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-map_metadata", "-1", "-map_chapters", "-1", "-bsf:v", "filter_units=remove_types=6", "-fflags", "+bitexact", "-flags:v", "+bitexact", "-flags:a", "+bitexact",
           "-movflags", "+faststart", edl["output"]]
    return cmd, dur, m

BAD = [b"c2pa", b"jumb", b"contentauth", b"DigitalSourceType", b"trainedAlgorithmicMedia", b"<x:xmpmeta", b"ISO6709", b"Apple", b"iPhone", b"com.apple", b"Lavf", b"x264 - core"]

def loud(p):  # integrated LUFS + true peak of the finished file
    r = run([FF, "-nostdin", "-v", "info", "-i", p, "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr; s = r[r.rfind("Summary:"):]
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", s)[0]), float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", s)[0])

def check(p, dur):  # the one runnable check
    j = json.loads(run([FP, "-v", "error", "-show_streams", "-show_format", "-of", "json", p]).stdout)
    v = [s for s in j["streams"] if s["codec_type"] == "video"]; a = [s for s in j["streams"] if s["codec_type"] == "audio"]
    ok = {"streams v1+a1": len(v) == 1 and len(a) == 1 and len(j["streams"]) == 2, "1080x1920": (v[0]["width"], v[0]["height"]) == (W, H),
          "no side data (display matrix, ambient env)": not v[0].get("side_data_list"), "30/1 fps": v[0]["r_frame_rate"] == "30/1" and v[0]["avg_frame_rate"] == "30/1",
          "yuv420p": v[0]["pix_fmt"] == "yuv420p", "bt709 tags": (v[0].get("color_space"), v[0].get("color_transfer"), v[0].get("color_primaries")) == ("bt709",) * 3,
          "h264 High": (v[0]["codec_name"], v[0]["profile"]) == ("h264", "High"), "aac 48k stereo": (a[0]["codec_name"], a[0]["sample_rate"], a[0]["channels"]) == ("aac", "48000", 2),
          f"duration ~{dur:.2f}s": abs(float(j["format"]["duration"]) - dur) < 0.15, "no format tags beyond ftyp brands": set(j["format"].get("tags", {})) <= {"major_brand", "minor_version", "compatible_brands"}}
    b = open(p, "rb").read(); top, i = [], 0
    while i + 8 <= len(b):
        sz, ty = int.from_bytes(b[i:i + 4], "big"), b[i + 4:i + 8].decode("latin1")
        if sz == 1: sz = int.from_bytes(b[i + 8:i + 16], "big")
        top.append(ty); i += sz or len(b)
    ok["faststart (moov before mdat)"] = top.index("moov") < top.index("mdat")
    li, tp = loud(p); ok[f"loudness {li} LUFS in -14+-1, true peak {tp} dBTP <= -1"] = abs(li + 14) <= 1 and tp <= -1
    hits = [x.decode() for x in BAD if x in b]; ok["no marker strings " + str(hits or "")] = not hits
    return ok, top

if __name__ == "__main__":
    edl = json.load(open(sys.argv[1])); os.chdir(os.path.dirname(os.path.abspath(sys.argv[1])))
    work = edl["output"] + ".work"; os.makedirs(work, exist_ok=True)
    cmd, dur, m = build(edl, work); print("LOUDNORM PASS1:", m); print("CMD:", shlex.join(cmd))
    if "--dry" in sys.argv: sys.exit()
    r = run(cmd); print(r.stderr[-600:] if r.returncode else "ffmpeg ok")
    ok, top = check(edl["output"], dur); print("BOXES:", top)
    for k, v in ok.items(): print("PASS" if v else "FAIL", k)
    sys.exit(0 if all(ok.values()) and not r.returncode else 1)
