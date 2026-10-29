# 3D capture of shop pieces: what the vendors say (2026-10-28)

Question (Ricky): can our own photos match the 11 stand-in models in the 3D showroom?

VERIFIED (pages in this folder):
- RealityScan Mobile (Epic): free, iOS 16+ / Android 7+, no LiDAR needed, cloud processing,
  20 to 250 photos per scan, Object mode removes background, AR coverage guide.
  Downloads: iOS = OBJ, Android = GLB (realityscan-mobile-1-5-docs.md; check the current app before relying on it).
  Object mode defaults to a watertight mesh (closes the base with invented geometry) since 1.9.
- RealityScan desktop: free under $1M annual revenue; Windows needs NVIDIA CUDA GPU (Ricky's RTX 4060 Ti qualifies).
- Apple Reality Composer Object Capture: iPhone 12 Pro or later (LiDAR), outputs USDZ.
- model-viewer `src` takes glTF/GLB; OBJ or USDZ must be converted (Blender).
- `site/build.mjs` ships everything under `site/assets/demo/models/`, so a new GLB plus one entry in `showroom.js` publishes.

NEEDS REVIEW: the mobile EULA's commercial terms. CG Channel says the app is "free, including for commercial use", but the EULA itself was not read.
Not verified: whether the iOS app now exports GLB (the docs above say OBJ).

## Prior work in Chief of Staff (Backwards Blueprints, 2026-09-20 to 09-25)
- Hunyuan3D-2 photo-to-3D, tested: one product render through the public Space `tencent/Hunyuan3D-2` gave a 13.2 MB glb,
  854k faces, 24 s, $0, shape only (`Chief Of Staff/research/backwards-blueprints/2026-09-22/photo-to-3d/test/`).
  Back side is a guess; width came out 0.69x to 1.86x off per part. Licence (fetched 2026-09-20) excludes the EU, UK and
  South Korea, including "display", which is a problem for a public shop site.
- TRELLIS.2 (MIT) README wants a 24 GB GPU; the 16 GB 4060 Ti does not fit. Public Space only. Not tested.
- Mesh shrink script: `Chief Of Staff/plans/backwards-blueprints/guides/pentair-ichlor/shrink.py` (pymeshlab quadric
  decimation to 20k faces). Lesson recorded there: iOS Safari dropped the picture at seven 50k-face meshes (8.2 MB),
  and `fast_simplification` output was junk.
- LiDAR research there was about AR anchoring for repair guides, not object scanning. Nothing reusable here.
- Phone photogrammetry was listed but "not crawled yet" (wiki/tool-discovery.md); this folder is the first verified look.
