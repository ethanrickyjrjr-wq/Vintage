# Ghost Auto: Industrial Autonomous Mannequin Engine

This project automates the process of creating "Ghost Mannequin" (invisible mannequin) product photography. 
It seamlessly fuses an on-hanger product image with an unbuttoned/flat lay back-collar image, completely automatically.

## Core Architecture

1. **Torso Silhouette Locking (Global Translation):**
   - Automatically calculates global `(dx, dy)` shift by aligning the shoulder silhouettes of both images.
2. **SAM 3.1 Neural Masking:**
   - Detects the inner collar cavity and generates a hole-free "Waterfall" mask to ensure no background leakage.
3. **Thin Plate Spline (TPS) Elastomer Warp:**
   - Uses RBF interpolation to perform a 4-corner warp. 
   - Dynamically detects the actual fabric start (ignoring metal hanger hooks via connected components and run-length filtering).
   - Warps the donor back collar up to the lapel seam, while applying a 20% counter-balance to the bottom corners to ensure the brand label has zero distortion.
4. **Closed-Loop QC Bot:**
   - Automatically inspects the final composite for black pixels, hanger leakage, and seam continuity before passing the final image.

## Requirements

Ensure you have `uv` or `pip` installed, then install dependencies:
```bash
pip install -r requirements.txt
```
*(Note: Requires PyTorch, OpenCV, NumPy, SciPy, and SAM 3.1 weights in `weights/sam3.1/`)*

## Usage

```bash
python ghost_auto.py --hanger "input_hanger.tif" --flat "input_flat.tif" --out "output/"
```
