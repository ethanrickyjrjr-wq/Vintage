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
