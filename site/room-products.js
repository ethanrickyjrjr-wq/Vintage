// Room-friendly inventory only. Overlay assets are editorial styling cutouts;
// A3/A4 use rectified original pixels; lamp/chandelier are existing editorial
// styling assets. Missing cutouts are deliberately unavailable for placement.
const HNV_ROOM_PRODUCTS = [
  { id: "A1", kind: "lamp", surface: "table", overlay: "assets/editorial/urn-lamp.webp" },
  { id: "A2", kind: "ceiling", surface: "ceiling", overlay: "assets/editorial/chandelier.webp" },
  { id: "A3", kind: "art", surface: "wall", overlay: "assets/cutouts/A3.webp", outline: [[.15, 0], [.938, .063], [.975, .97], [.145, .985]] },
  { id: "A4", kind: "art", surface: "wall", overlay: "assets/cutouts/A4.webp", outline: [[.125, .092], [.863, 0], [.88, .95], [.11, .93]] },
  { id: "A5", kind: "art", surface: "wall" },
  { id: "A13", kind: "lamp", surface: "table" },
  { id: "A14", kind: "decor", surface: "table" },
  { id: "A15", kind: "floor", surface: "floor" },
  { id: "A16", kind: "media", surface: "table" },
  { id: "A17", kind: "lamp", surface: "table" },
  { id: "A19", kind: "floor", surface: "sofa or floor" },
  { id: "A20", kind: "floor", surface: "floor" },
  { id: "A22", kind: "floor", surface: "floor" },
  { id: "A10", kind: "decor", surface: "table" },
  { id: "A8", kind: "decor", surface: "table" },
  { id: "A9", kind: "media", surface: "table" },
];
