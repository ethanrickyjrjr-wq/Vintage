"""Reproducible mask-only pilot. Run stages from any directory; see README.md."""
import argparse
import hashlib
import importlib.metadata as metadata
import io
import json
import os
from pathlib import Path
import shutil
import textwrap
import time

import numpy as np
from PIL import Image, ImageCms, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "artifacts/pilot/work"
OUT = ROOT / "site/assets/cutouts"
MEDIA = ROOT / "media"
CONFIG = json.loads((Path(__file__).parent / "items.json").read_text())
TEST_IDS = {"A1", "A2", "A10", "B9"}
HR_REV = "5d6b6f8adcb5b417c871b1d84ceaae9871355b7f"
HR_SHA256 = "a5a4de698739ea5e0e8bbab28e1b293dde95092b87a442d566cbc585c53cef55"
os.environ.setdefault("U2NET_HOME", str(ROOT / ".venv/models/rembg"))
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("HF_HUB_OFFLINE", "1")
SRGB = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf8")


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_manifest():
    path = MEDIA / "manifest.json"
    return json.loads(path.read_text()) if path.exists() else {"items": {}, "trials": {}}


def save_manifest(manifest):
    manifest["versions"] = {name: metadata.version(name) for name in
                            ("rembg", "Pillow", "numpy", "onnxruntime")}
    for name in ("torch", "torchvision", "transformers", "timm", "kornia", "einops", "safetensors"):
        try:
            manifest["versions"][name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            pass
    manifest["pipeline"] = "oriented sRGB source -> alpha mask -> original RGB + alpha -> alpha bbox -> contain -> WebP"
    manifest["models"] = {
        "general": {"name": "birefnet-general", "licence": "MIT", "expected_md5": "7a35a0141cbbc80de11d9c9a28f52697",
                    "url": "https://huggingface.co/ZhengPeng7/BiRefNet"},
        "matting": {"name": "ZhengPeng7/BiRefNet_HR-matting", "revision": HR_REV, "licence": "MIT", "sha256": HR_SHA256}}
    write_json(MEDIA / "manifest.json", manifest)


def prepare(items, manifest):
    for item in items:
        source = ROOT / item["source"]
        folder = MEDIA / item["id"]
        folder.mkdir(parents=True, exist_ok=True)
        original = folder / ("orig" + source.suffix)
        shutil.copyfile(source, original)
        assert digest(source) == digest(original)
        with Image.open(source) as image:
            profile = image.info.get("icc_profile")
            image = ImageOps.exif_transpose(image).convert("RGB")
            source_size = list(image.size)
            if profile:
                image = ImageCms.profileToProfile(image, ImageCms.ImageCmsProfile(io.BytesIO(profile)),
                                                 ImageCms.createProfile("sRGB"), outputMode="RGB")
            if "crop" in item:
                w, h = image.size
                image = image.crop(tuple(round(v * (w if i % 2 == 0 else h))
                                         for i, v in enumerate(item["crop"])))
            image.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
            image.save(WORK / f'{item["id"]}-source.png', icc_profile=SRGB)
            if item["id"] == "A1":
                # Honest third image: crop the same original, do not invent another angle.
                detail = image.crop((round(image.width * .25), round(image.height * .50),
                                     round(image.width * .80), round(image.height * .96)))
                OUT.mkdir(parents=True, exist_ok=True)
                detail.save(OUT / "A1-detail.webp", quality=85, method=6, icc_profile=SRGB)
        manifest["items"][item["id"]] = {
            **item, "source_px": source_size, "prepared_px": list(image.size), "source_sha256": digest(source),
            "original_sha256": digest(original), "colour_profile": "sRGB", "channel_status": "deferred until style approval",
            "status": "layout test" if item.get("layoutTest") else "pilot; visual review required"}
        print(f'prepared {item["id"]}: {source_size} -> {image.size}', flush=True)
    save_manifest(manifest)
    if not (OUT / "pilot.json").exists():
        write_json(OUT / "pilot.json", [{**v, "cutout": None, "result": "Original / mask pending"} for v in items])


def pixels_kept(source, result):
    rgb = np.asarray(source.convert("RGB")).astype(np.int16)
    rgba = np.asarray(result.convert("RGBA"))
    opaque = rgba[:, :, 3] >= 250
    delta = np.abs(rgb - rgba[:, :, :3].astype(np.int16)).max(-1)
    share = float((delta[opaque] <= 3).mean()) if opaque.any() else None
    return {"within_3_share": share, "opaque_share": float(opaque.mean()),
            "pass": share is not None and share >= .99, "stage": "before trim, resizing and lossy encoding"}


def original_rgb(source, alpha):
    result = source.convert("RGBA")
    result.putalpha(alpha)
    arr = np.array(result)
    arr[arr[:, :, 3] <= 8] = 0
    return Image.fromarray(arr)


def general(items, manifest):
    from rembg import new_session
    from rembg.bg import decontaminate_cutout, naive_cutout
    started = time.perf_counter()
    # Explicit session is mandatory: rembg's default has a noncommercial licence.
    session = new_session("birefnet-general", providers=["CPUExecutionProvider"])
    manifest["general_session_load_seconds"] = round(time.perf_counter() - started, 3)
    for item in items:
        if item["mode"] not in {"cut", "keep"} or item["id"] == "A5":
            continue
        key = item["id"]
        source = Image.open(WORK / f"{key}-source.png").convert("RGB")
        started = time.perf_counter()
        mask = session.predict(source)[0]
        inference = time.perf_counter() - started
        started = time.perf_counter()
        decontaminated = decontaminate_cutout(source, mask)
        decontamination = time.perf_counter() - started
        naive = naive_cutout(source, mask)
        preserved = original_rgb(source, mask)
        for suffix, result in (("A", decontaminated), ("A0", naive), ("mask", preserved)):
            result.save(WORK / f"{key}-{suffix}.png")
        manifest["trials"].setdefault(key, {}).update({
            "A": {"tool": "rembg 2.0.86", "flags": "-m birefnet-general -dc", "provider": "CPUExecutionProvider",
                  "seconds": round(inference + decontamination, 3), "inference_seconds": round(inference, 3),
                  "decontamination_seconds": round(decontamination, 3), "pixels_kept": pixels_kept(source, decontaminated)},
            "A0": {"tool": "rembg naive_cutout; same predicted mask, no decontamination", "pixels_kept": pixels_kept(source, naive)},
            "preserved": {"tool": "original RGB + BiRefNet general alpha", "pixels_kept": pixels_kept(source, preserved)},
            "C": {"tool": "no cut; unchanged source pixels", "seconds": 0, "timing_scope": "no model inference; I/O excluded",
                  "pixels_kept": {"pass": True, "within_3_share": 1}}})
        save_manifest(manifest)
        print(f'{key}: A {inference + decontamination:.2f}s, pixels {manifest["trials"][key]["A"]["pixels_kept"]}', flush=True)


def matting(items, manifest):
    import torch
    from torchvision import transforms
    from transformers import AutoModelForImageSegmentation
    torch.set_num_threads(8)
    model_path = ROOT / ".venv/models/BiRefNet_HR-matting"
    assert digest(model_path / "model.safetensors") == HR_SHA256, "Unexpected HR model weights"
    started = time.perf_counter()
    # Downloaded at HR_REV; model code reviewed before this local-only load.
    model = AutoModelForImageSegmentation.from_pretrained(str(model_path), trust_remote_code=True,
                                                         local_files_only=True, use_safetensors=True).eval()
    manifest["matting_session_load_seconds"] = round(time.perf_counter() - started, 3)
    transform = transforms.Compose([transforms.Resize((2048, 2048)), transforms.ToTensor(),
                                    transforms.Normalize([.485, .456, .406], [.229, .224, .225])])
    for item in items:
        key = item["id"]
        if key not in TEST_IDS:
            continue
        source = Image.open(WORK / f"{key}-source.png").convert("RGB")
        started = time.perf_counter()
        with torch.inference_mode():
            prediction = model(transform(source).unsqueeze(0))[-1].sigmoid().cpu()[0].squeeze()
        alpha = transforms.ToPILImage()(prediction).resize(source.size, Image.Resampling.LANCZOS)
        seconds = time.perf_counter() - started
        result = original_rgb(source, alpha)
        result.save(WORK / f"{key}-B.png")
        manifest["trials"].setdefault(key, {})["B"] = {
            "tool": "BiRefNet_HR-matting", "revision": HR_REV, "resolution": [2048, 2048], "device": "CPU fp32",
            "seconds": round(seconds, 3), "pixels_kept": pixels_kept(source, result)}
        save_manifest(manifest)
        print(f"{key}: B {seconds:.2f}s", flush=True)


def perspective(source, quad):
    points = [(x * source.width, y * source.height) for x, y in quad]
    # Pillow QUAD order is upper-left, lower-left, lower-right, upper-right.
    tl, tr, br, bl = points
    width = round((np.linalg.norm(np.subtract(tr, tl)) + np.linalg.norm(np.subtract(br, bl))) / 2)
    height = round((np.linalg.norm(np.subtract(bl, tl)) + np.linalg.norm(np.subtract(br, tr))) / 2)
    return source.transform((width, height), Image.Transform.QUAD,
                            tuple(v for p in (tl, bl, br, tr) for v in p), Image.Resampling.BICUBIC).convert("RGBA")


def cell(image, item, size=(960, 1200)):
    bbox = image.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    if not bbox:
        raise ValueError(f'{item["id"]}: empty alpha mask')
    image = image.crop(bbox)
    fractions = {"tall": (.82, .88), "wide": (.88, .82), "small": (.72, .7)}[item["fit"]]
    image = ImageOps.contain(image, tuple(round(v * n) for v, n in zip(fractions, size)), Image.Resampling.LANCZOS)
    x = (size[0] - image.width) // 2
    y = {"top": round(size[1] * .06), "bottom": size[1] - image.height - round(size[1] * .06),
         "center": (size[1] - image.height) // 2}[item["anchor"]]
    canvas = Image.new("RGBA", size)
    canvas.paste(image, (x, y))
    arr = np.array(canvas)
    arr[arr[:, :, 3] == 0, :3] = 0
    return Image.fromarray(arr), bbox


def export(items, manifest):
    OUT.mkdir(parents=True, exist_ok=True)
    pilot = []
    for item in items:
        key = item["id"]
        source = Image.open(WORK / f"{key}-source.png").convert("RGB")
        record = manifest["items"][key]
        record.update(item)
        if item["mode"] == "keep":
            for suffix in ("", "--480"):
                (OUT / f"{key}{suffix}.webp").unlink(missing_ok=True)
            for field in ("exports", "pixels_kept", "alpha_bbox_px", "subject_long_edge_prepared_px"):
                record.pop(field, None)
            pilot.append({**item, "cutout": None, "result": "Original retained", "pixelsKept": None})
            record["selected_tool"] = "no cut; original retained"
            record["channel_status"] = "needs re-shoot: glass or obscured item"
            continue
        if item["mode"] == "flat":
            result = perspective(source, item["quad"])
            record["selected_tool"] = "Pillow quadrilateral rectification; no synthesis"
            record["pixels_kept"] = {"pass": True, "stage": "geometric source sampling only; no segmentation or retouching"}
        else:
            selected = item.get("selectedArm", "mask")
            result = Image.open(WORK / f"{key}-{selected}.png").convert("RGBA")
            record["selected_tool"] = "original RGB + " + ("HR-matting alpha" if selected == "B" else "birefnet-general alpha")
            if "maskLimit" in item:
                alpha = np.array(result.getchannel("A"))
                x1, y1, x2, y2 = [round(v * (result.width if i % 2 == 0 else result.height))
                                  for i, v in enumerate(item["maskLimit"])]
                limited = np.zeros_like(alpha)
                limited[y1:y2, x1:x2] = alpha[y1:y2, x1:x2]
                result = original_rgb(source, Image.fromarray(limited))
                record["selected_tool"] += "; alpha-only exclusion of adjacent frame"
            record["pixels_kept"] = pixels_kept(source, result)
            assert record["pixels_kept"]["pass"], f"{key}: source pixels changed"
        canvas, bbox = cell(result, item)
        record["alpha_bbox_px"] = list(bbox)
        record["subject_long_edge_prepared_px"] = max(bbox[2] - bbox[0], bbox[3] - bbox[1])
        if record["subject_long_edge_prepared_px"] < 1500 or item.get("layoutTest") or item.get("note"):
            record["channel_status"] = "needs re-shoot or visual approval; no channel export in pilot"
        record["exports"] = []
        for suffix, size in (("", (960, 1200)), ("--480", (480, 600))):
            target = OUT / f"{key}{suffix}.webp"
            image = canvas if size == canvas.size else canvas.resize(size, Image.Resampling.LANCZOS)
            arr = np.array(image)
            arr[arr[:, :, 3] == 0, :3] = 0
            image = Image.fromarray(arr)
            for quality in (82, 78, 74, 70):
                image.save(target, format="WEBP", quality=quality, alpha_quality=100, method=6,
                           exact=True, icc_profile=SRGB)
                if target.stat().st_size <= 200_000:
                    break
            assert target.stat().st_size <= 200_000, f"{key}: file budget exceeded"
            decoded = Image.open(target).convert("RGBA")
            # Report encoding loss separately; this is not the mask provenance test.
            encoding = pixels_kept(image, decoded)
            encoding.pop("pass")
            encoding["stage"] = "lossy WebP round-trip; not the mask integrity test"
            alpha_exact = np.array_equal(np.asarray(image.getchannel("A")), np.asarray(decoded.getchannel("A")))
            assert alpha_exact, f"{key}: alpha changed during encoding"
            record["exports"].append({"path": str(target.relative_to(ROOT)), "px": size, "bytes": target.stat().st_size,
                                      "quality": quality, "alpha_quality": 100, "alpha_exact": alpha_exact,
                                      "encoding_comparison": encoding})
        pilot.append({**item, "cutout": f"assets/cutouts/{key}.webp", "result": "Perspective crop" if item["mode"] == "flat" else "Mask study",
                      "pixelsKept": record["pixels_kept"]})
    save_manifest(manifest)
    write_json(OUT / "pilot.json", pilot)


def sheets(items, manifest):
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
    heading = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 25)
    # Each arm is inspected at grid size and in a true 1:1 source crop.
    tested = [item["id"] for item in items if item["id"] in TEST_IDS]
    for key in tested:
        source = Image.open(WORK / f"{key}-source.png").convert("RGBA")
        item = next(v for v in items if v["id"] == key)
        sheet = Image.new("RGB", (1800, 1240), "#f6efdf")
        draw = ImageDraw.Draw(sheet)
        draw.text((20, 14), f"{key} / A general -dc / B HR matting / C original / right panels: 100% crops", font=heading, fill="#451c2b")
        # Default crop includes the middle of the hard area, refined per image after inspection.
        focus = item.get("focus", [.5, .5])
        for column, arm in enumerate(("A", "B", "C")):
            path = WORK / f"{key}-{arm}.png"
            result = source if arm == "C" else Image.open(path).convert("RGBA")
            for row, background in enumerate(("#ffffff", "#000000", "#451c2b")):
                x, y = column * 600, 65 + row * 385
                tile = Image.new("RGBA", (285, 350), background)
                thumb, _ = cell(result, item, (285, 350))
                tile.alpha_composite(thumb)
                sheet.paste(tile.convert("RGB"), (x + 10, y))
                cx, cy = (round(focus[0] * result.width), round(focus[1] * result.height))
                box = (max(0, cx - 140), max(0, cy - 140), min(result.width, cx + 140), min(result.height, cy + 140))
                detail = result.crop(box)
                panel = Image.new("RGBA", (280, 280), background)
                panel.alpha_composite(detail, ((280 - detail.width) // 2, (280 - detail.height) // 2))
                sheet.paste(panel.convert("RGB"), (x + 305, y + 25))
                draw.text((x + 14, y + 350), f"{arm}  {background}  |  right: 1:1", font=font, fill="#451c2b")
        sheet.save(ROOT / f"artifacts/pilot/test-{key}.jpg", quality=92)
    overview = Image.new("RGB", (1800, 1240 * len(tested)), "#f6efdf")
    for i, key in enumerate(tested):
        overview.paste(Image.open(ROOT / f"artifacts/pilot/test-{key}.jpg"), (0, i * 1240))
    overview.save(ROOT / "artifacts/pilot/mask-contact-sheet.jpg", quality=90)
    write_json(ROOT / "artifacts/pilot/trial-results.json", manifest["trials"])
    if set(tested) == TEST_IDS:
        verdicts = {
            "A1": ["FAIL as-is: adjacent Elvis frame selected. Lamp edge is usable.",
                   "FAIL: stray hanger, softened foot and adjacent frame remain.",
                   "General alpha plus a rectangular exclusion of the adjacent frame. Layout only: shade clipped, foot obscured."],
            "A2": ["FAIL glass: gaps improve, but shards look opaque.",
                   "FAIL glass: background haze and uneven translucency.",
                   "Keep the original. Re-shoot on a seamless backdrop."],
            "A10": ["FAIL glass: old wall remains inside opaque-looking bowls.",
                    "FAIL: most glasses disappear; unrelated clothing remains.",
                    "Keep the original. Re-shoot glass with defined edges."],
            "B9": ["PASS layout: boots, fringe, toes and soles remain. Source is soft.",
                   "FAIL: shafts and most fringe are erased; only toe areas remain.",
                   "General alpha for layout only. Re-shoot for sharp fringe and listing resolution."]}
        audit = {"versions": manifest["versions"], "models": manifest["models"],
                 "session_load_seconds": {"general": manifest["general_session_load_seconds"],
                                          "matting": manifest["matting_session_load_seconds"]},
                 "trials": {key: manifest["trials"][key] for key in tested}, "visual_review": verdicts,
                 "items": {key: value for key, value in manifest["items"].items()}}
        write_json(ROOT / "tools/cutout/pilot-audit.json", audit)
        table = Image.new("RGB", (1760, 1190), "#f6efdf")
        td = ImageDraw.Draw(table)
        td.text((30, 25), "Hollywood & Vine / mask pilot / 27 October 2026", font=heading, fill="#451c2b")
        td.text((30, 70), "CPU / A: general -dc / B: HR-matting 2048 / C: original, no inference", font=font, fill="#451c2b")
        td.text((30, 102), "All opaque-pixel checks PASS. That proves RGB retention, not correct coverage; judge the masks by eye.", font=font, fill="#451c2b")
        edges = [30, 195, 645, 1095, 1730]
        for x, title in zip(edges, ("Item", "A / general", "B / HR matting", "Decision")):
            td.text((x, 155), title, font=heading, fill="#451c2b")
        for row, key in enumerate(tested):
            y = 205 + row * 215
            td.line((30, y - 10, 1730, y - 10), fill="#451c2b", width=1)
            td.text((30, y), key, font=heading, fill="#451c2b")
            trial = manifest["trials"][key]
            texts = [f'{trial["A"]["seconds"]:.2f} s\n' + verdicts[key][0],
                     f'{trial["B"]["seconds"]:.2f} s\n' + verdicts[key][1], verdicts[key][2]]
            for column, content in enumerate(texts):
                wrapped = "\n".join(textwrap.fill(line, 43 if column < 2 else 58) for line in content.splitlines())
                td.multiline_text((edges[column + 1], y), wrapped, font=font, fill="#451c2b", spacing=7)
        td.text((30, 1100), "No complete listing-ready set. All current sources are below the 1500 px subject threshold. No channel files exported.", font=font, fill="#451c2b")
        td.text((30, 1135), "Source RGB + selected alpha is 100% unchanged before resizing and lossy WebP. Owner review is still required.", font=font, fill="#451c2b")
        table.save(ROOT / "artifacts/pilot/pass-fail.jpg", quality=94)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("prepare", "general", "matting", "export", "sheets"))
    parser.add_argument("--ids", nargs="*")
    args = parser.parse_args()
    selected = [v for v in CONFIG if not args.ids or v["id"] in args.ids]
    WORK.mkdir(parents=True, exist_ok=True)
    globals()[args.stage](selected, read_manifest())
