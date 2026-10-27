// Served only by dev.mjs at /demo. This file and assets/demo never ship in a build.
// These are style-matched borrowed photographs, not new inventory records.
(() => {
  const samples = [
    { id: "A13", file: "gold-bust-lamp", title: "Gold Egyptian bust lamp", sub: "Gold bust, wide cream rectangular shade and a pale plinth. Similar in spirit to the gilded head lamp by the window." },
    { id: "A14", file: "seated-leopard", title: "Seated spotted ceramic leopard", sub: "Glossy spotted Italian-style leopard, seated upright with long front legs and a curled tail." },
    { id: "A15", file: "southwestern-armchair", title: "Black armchair, Southwestern upholstery", sub: "Low black wood frame with a rust, cream and black geometric star pattern, echoing the original star-cushion armchair." },
    { id: "A16", file: "wood-radio", title: "Vintage wood tabletop radio", sub: "Closed dark cherry cabinet, a near-round radio dial and horizontal speaker grille. A similar silhouette to the original tabletop radio and record player." },
    { id: "A17", file: "brass-oil-lamp", title: "Brass hurricane oil lamp", sub: "Polished brass reservoir, short pedestal and clear glass chimney." },
    { id: "A19", file: "cowhide", title: "Brown-and-white cowhide", sub: "Hair-on hide with warm brown patches and an organic edge, like the hide over the rust sofa." },
    { id: "A20", file: "white-paper-chair", title: "White accordion-paper chair", sub: "Expanded white honeycomb paper with sculptural folds and a raised back. A closer material match than a natural-cardboard Wiggle chair." },
    { id: "A22", file: "source-painted-mannequin", title: "Paint-splattered mannequin torso", sub: "An art mannequin covered in colorful paint drips. This sample is a torso rather than the original full-body form; source photo only, cutout pending.", cutout: false },
    { id: "A10", file: "pink-coupes", title: "Vintage rose champagne coupe", sub: "A peach-rose vintage coupe with a twisted bowl and decorative stem, matching the warm pink stemware on the shelf." },
    { id: "A8", file: "silver-busts", title: "Silver mannequin heads, pair", sub: "Two vintage silver-finish head-and-neck busts on small round bases." },
    { id: "A9", file: "film-projector", title: "Vintage 8mm film projector", sub: "A complete two-reel tabletop projector with period metal housing and lens." },
  ];
  for (const sample of samples) {
    const item = HNV_ITEMS.find(item => item.id === sample.id);
    const product = HNV_ROOM_PRODUCTS.find(product => product.id === sample.id);
    const image = `assets/demo/${sample.file}.webp`;
    Object.assign(item, { title: sample.title, sub: sample.sub, img: image, chip: "demo" });
    Object.assign(product, { ...(sample.cutout === false ? {} : { overlay: image }), ...(sample.surface ? { surface: sample.surface } : {}), ...(sample.kind ? { kind: sample.kind } : {}) });
    // A similar piece must not inherit the actual item's researched selling price.
    delete HNV_PRICES[sample.id];
  }
  // The incomplete Elvis crop is not a whole-object styling layer.
  const incomplete = HNV_ROOM_PRODUCTS.findIndex(product => product.id === "A5");
  if (incomplete !== -1) HNV_ROOM_PRODUCTS.splice(incomplete, 1);
  document.body.classList.add("styling-demo");
  const banner = document.createElement("aside");
  banner.className = "styling-demo-banner";
  banner.setAttribute("aria-label", "Private styling demo");
  banner.innerHTML = '<p><strong>Private styling demo</strong>Similar pieces, clearer photos. Your original lamp, chandelier and artwork stay in the mix.</p><a href="demo-photos.html">Compare the photo matches ↗</a>';
  document.body.prepend(banner);
  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("room-use-example").click();
  });
})();
