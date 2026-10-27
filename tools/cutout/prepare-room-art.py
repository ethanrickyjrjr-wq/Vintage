"""Rectify photographed artwork for the browser room editor; never redraw pixels.

Run with an existing Python environment containing Pillow and numpy:
    python tools/cutout/prepare-room-art.py

The quadrilaterals are the existing room-products.js outlines, in clockwise
top-left order. Rectification resamples the source, retaining glare, condition
and the small photographed obstruction on A3. This is not a channel export.
"""

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'site/assets/cutouts'
AUDIT = ROOT / 'artifacts/cutouts'
ART = {
    'A3': ('IMG_6609.webp', [[.15, 0], [.938, .063], [.975, .97], [.145, .985]]),
    'A4': ('IMG_6613.webp', [[.125, .092], [.863, 0], [.88, .95], [.11, .93]]),
}


def inverse_perspective(destination, source):
    """Solve output-to-input homography coefficients for Pillow PERSPECTIVE."""
    rows, values = [], []
    for (x, y), (u, v) in zip(destination, source):
        rows.extend([
            [x, y, 1, 0, 0, 0, -u * x, -u * y],
            [0, 0, 0, x, y, 1, -v * x, -v * y],
        ])
        values.extend([u, v])
    return np.linalg.solve(np.asarray(rows), np.asarray(values))


def prepare(item_id, filename, outline):
    path = ROOT / 'site/assets/photos' / filename
    image = ImageOps.exif_transpose(Image.open(path)).convert('RGB')
    # These storefront exports are already converted to sRGB and have no ICC.
    if image.info.get('icc_profile'):
        raise ValueError('Convert the source profile explicitly before rectifying')
    points = np.asarray(outline) * np.asarray(image.size)
    edge_width = (np.linalg.norm(points[1] - points[0])
                  + np.linalg.norm(points[2] - points[3])) / 2
    edge_height = (np.linalg.norm(points[3] - points[0])
                   + np.linalg.norm(points[2] - points[1])) / 2
    height = 1200
    width = round(height * edge_width / edge_height)
    destination = [(0, 0), (width, 0), (width, height), (0, height)]
    coefficients = inverse_perspective(destination, points)
    rectified = image.transform(
        (width, height), Image.Transform.PERSPECTIVE, coefficients,
        resample=Image.Resampling.BICUBIC,
    ).convert('RGBA')
    # Keep a lossless audit copy to distinguish geometry from WebP compression.
    audit_path = AUDIT / f'{item_id}-rectified.png'
    rectified.save(audit_path)
    audit_pixels = np.asarray(Image.open(audit_path))
    assert np.array_equal(audit_pixels, np.asarray(rectified))

    for suffix, texture in [('', rectified), ('--480', rectified.resize(
            (480, round(height * 480 / width)), Image.Resampling.LANCZOS))]:
        texture.save(OUTPUT / f'{item_id}{suffix}.webp', quality=82,
                     alpha_quality=100, method=6, exact=True)

    output_path = OUTPUT / f'{item_id}.webp'
    exported = Image.open(output_path).convert('RGBA')
    assert exported.size == rectified.size
    assert exported.getchannel('A').getextrema() == (255, 255)
    return {
        'id': item_id,
        'source': str(path.relative_to(ROOT)).replace('\\', '/'),
        'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'source_px': list(image.size),
        'outline_normalized': outline,
        'operation': 'deterministic inverse perspective, bicubic; no inpainting',
        'size': [width, height],
        'ratio': width / height,
        'content_bbox': [0, 0, width, height],
        'pre_encoding_pixels_kept': 1.0,
        'pre_encoding_comparison': 'exact equality to deterministic source warp',
        'encoding': 'lossy WebP quality 82, lossless opaque alpha',
        'bytes': output_path.stat().st_size,
        'output_sha256': hashlib.sha256(output_path.read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    OUTPUT.mkdir(parents=True, exist_ok=True)
    AUDIT.mkdir(parents=True, exist_ok=True)
    results = [prepare(item_id, *config) for item_id, config in ART.items()]
    (OUTPUT / 'room-art-provenance.json').write_text(
        json.dumps(results, indent=2) + '\n', encoding='utf-8',
    )
    print(json.dumps(results, indent=2))
