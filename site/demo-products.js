// Local /demo only. One approved photo set feeds the collection and room editor.
// Borrowed styling samples do not inherit inventory prices or availability.
(() => {
  const samples = [
    {"id": "A13", "file": "gold-bust-lamp", "cat": "lighting", "title": "Gold Egyptian bust lamp", "sub": "A gilded bust, a generous cream shade and a pale plinth.", "kind": "lamp", "surface": "table"},
    {"id": "A14", "file": "seated-leopard", "cat": "lighting", "title": "Seated ceramic leopard", "sub": "Glossy spotted ceramic, long front legs and a curled tail.", "kind": "decor", "surface": "table"},
    {"id": "A15", "file": "southwestern-armchair", "cat": "lighting", "title": "Southwestern armchair", "sub": "Black wood and rust, cream and black geometric upholstery.", "kind": "floor", "surface": "floor"},
    {"id": "A16", "file": "wood-radio", "cat": "lighting", "title": "Vintage wood tabletop radio", "sub": "Dark cherry wood, a rounded dial and a horizontal speaker grille.", "kind": "media", "surface": "table"},
    {"id": "A17", "file": "brass-oil-lamp", "cat": "lighting", "title": "Brass hurricane lamp", "sub": "Polished brass and a clear glass chimney.", "kind": "lamp", "surface": "table"},
    {"id": "A19", "file": "cowhide", "cat": "lighting", "title": "Brown-and-white cowhide", "sub": "Warm brown patches and the natural outline of a hair-on hide.", "kind": "floor", "surface": "floor"},
    {"id": "A20", "file": "white-paper-chair", "cat": "lighting", "title": "White accordion chair", "sub": "Sculptural white honeycomb folds with a raised back.", "kind": "floor", "surface": "floor"},
    {"id": "A10", "file": "pink-coupes", "cat": "lighting", "title": "Rose champagne coupe", "sub": "Peach-rose glass, a twisted bowl and a decorative stem.", "kind": "decor", "surface": "table"},
    {"id": "A8", "file": "silver-busts", "cat": "art", "title": "Silver mannequin heads", "sub": "A pair of silver head-and-neck busts on small round bases.", "kind": "decor", "surface": "table"},
    {"id": "A9", "file": "film-projector", "cat": "lighting", "title": "Vintage film projector", "sub": "Two reels, a metal housing and a complete lens assembly.", "kind": "media", "surface": "table"},
    {"id": "A1", "file": "lamp-pink-glass-gold-base", "cat": "lighting", "title": "Pink glass urn lamp", "sub": "Pink glass urn table lamp, gold base, gold-champagne cone shade", "kind": "lamp", "surface": "table"},
    {"id": "S117373F4", "file": "lamp-ruby-glass-brass", "cat": "lighting", "title": "Ruby glass table lamp", "sub": "Ruby-red cut glass table lamp, brass fittings, amber pleated shade", "kind": "lamp", "surface": "table"},
    {"id": "A2", "file": "chandelier-brass-frosted-bowls", "cat": "lighting", "title": "Brass and alabaster chandelier", "sub": "Brass pendant chandelier with three frosted alabaster glass bowl shades on a chain", "kind": "ceiling", "surface": "ceiling"},
    {"id": "S921B3611", "file": "gramophone-rose-horn", "cat": "lighting", "title": "Rose-horn gramophone", "sub": "Antique wind-up gramophone with large rose-pink/burgundy flared horn on wooden case", "kind": "media", "surface": "table"},
    {"id": "S696D0374", "file": "rotary-phone-red", "cat": "lighting", "title": "Red rotary telephone", "sub": "Red Bakelite-style rotary desk telephone with cream handset cord", "kind": "decor", "surface": "table"},
    {"id": "S653289D0", "file": "picture-frame-gold-carved", "cat": "art", "title": "Carved gilt frame", "sub": "Square carved gold picture frame with classical flowers and scrolls, empty transparent opening", "kind": "art", "surface": "wall"},
    {"id": "A3", "file": "mirror-gold-oval-rococo", "cat": "art", "title": "Gilded rococo mirror", "sub": "Ornate gold rococo oval wall mirror with shell crest", "kind": "art", "surface": "wall"},
    {"id": "S003F5528", "file": "perfume-atomizer-rose-glass", "cat": "lighting", "title": "Rose glass atomizer", "sub": "Vintage swirled rose/ruby glass perfume atomizer with gold collar, mesh bulb and gold tassel", "kind": "decor", "surface": "table"},
    {"id": "A12", "file": "cut-crystal-goblet", "cat": "lighting", "title": "Cut-crystal goblet", "sub": "Cut-crystal pressed-star goblet on a baluster stem", "kind": "decor", "surface": "table"},
    {"id": "B18", "file": "zebra-print-star-pump", "cat": "fashion", "title": "Zebra-print star pump", "sub": "Zebra-print pointed pump, hot pink lining, star stud and zip trim", "kind": "fashion", "surface": "manual"},
    {"id": "S5C8D0CE0", "file": "spiked-black-platform-pumps", "cat": "fashion", "title": "Spiked black platforms", "sub": "Black suede platform pumps with silver spike toe studs (back view + side view)", "kind": "fashion", "surface": "manual"},
    {"id": "SAADD0092", "file": "neon-pink-patent-platform-pumps", "cat": "fashion", "title": "Neon pink platforms", "sub": "Pair of neon pink patent platform pumps with stiletto heels", "kind": "fashion", "surface": "manual"},
    {"id": "SBFED9B79", "file": "neon-lime-gem-t-strap-sandal", "cat": "fashion", "title": "Lime jewel sandal", "sub": "Tan leather T-strap flat sandal with neon lime gem stones and lime heel", "kind": "fashion", "surface": "manual"},
    {"id": "B6", "file": "feathered-studded-felt-cowboy-hat", "cat": "fashion", "title": "Feathered felt cowboy hat", "sub": "Brown felt cowboy hat, studded leather band, red/blue feather", "kind": "fashion", "surface": "manual"},
    {"id": "SC573BA4B", "file": "red-pleated-leather-jewel-handbag", "cat": "fashion", "title": "Red jewel-clasp handbag", "sub": "Red leather pleated handbag with patent top handle and jewelled flower clasp", "kind": "fashion", "surface": "manual"},
    {"id": "S52495D6C", "file": "magenta-feather-crystal-earrings", "cat": "fashion", "title": "Magenta feather earrings", "sub": "Pair of magenta feather statement earrings with crystal feather studs", "kind": "fashion", "surface": "manual"},
    {"id": "SEF23B100", "file": "gold-braided-chain-necklace", "cat": "fashion", "title": "Braided gold necklace", "sub": "Chunky braided gold necklace set with small diamonds, open clasp", "kind": "fashion", "surface": "manual"},
    {"id": "SEB9EC9E5", "file": "round-wire-pink-lens-sunglasses", "cat": "fashion", "title": "Rose-lens sunglasses", "sub": "Round gold wire-frame sunglasses with pink lenses and clear temple tips (photo)", "kind": "fashion", "surface": "manual"},
    {"id": "B1", "file": "red-orange-shaggy-faux-fur-jacket", "cat": "fashion", "title": "Shaggy sunset jacket", "sub": "Red/orange/yellow shaggy faux fur jacket, ghost mannequin, orange satin lining", "kind": "fashion", "surface": "manual"},
    {"id": "S432B3EF5", "file": "navy-floral-shirt-dress-red-trim", "cat": "fashion", "title": "Red-trim print dress", "sub": "Navy polka-dot and fruit-print shirt dress, red piping and buttons, ghost mannequin", "kind": "fashion", "surface": "manual"},
    {"id": "B10", "file": "safety-pin-star-sequin-mini-dress", "cat": "fashion", "title": "Safety-pin star mini dress", "sub": "Black asymmetric mini dress covered in safety pins, studs and silver stars, ghost mannequin", "kind": "fashion", "surface": "manual"},
    {"id": "S531FE489", "file": "gilded-emerald-velvet-regency-armchair", "cat": "lighting", "title": "Emerald velvet armchair", "sub": "Gilded Regency armchair in emerald velvet", "kind": "floor", "surface": "floor"},
    {"id": "SCB4670A4", "file": "rust-leather-midcentury-sofa", "cat": "lighting", "title": "Rust leather sofa", "sub": "Rust/orange leather mid-century three-seat sofa, tapered wood legs", "kind": "floor", "surface": "floor"},
    {"id": "S7E0E0EA5", "file": "red-swan-sofa-chrome-base", "cat": "lighting", "title": "Red Swan-style sofa", "sub": "Red wool Swan-style sofa on a chrome base", "kind": "floor", "surface": "floor"},
    {"id": "S4B62EB76", "file": "worn-wood-barstool", "cat": "lighting", "title": "Worn wood barstool", "sub": "Worn walnut wooden barstool", "kind": "floor", "surface": "floor"},
    {"id": "S2047BD69", "file": "pink-vinyl-chrome-diner-chair", "cat": "lighting", "title": "Pink chrome diner chair", "sub": "Hot-pink vinyl and chrome 50s diner chair", "kind": "floor", "surface": "floor"},
    {"id": "SB067D22F", "file": "blue-velvet-round-button-pouf-cushion", "cat": "lighting", "title": "Blue velvet button cushion", "sub": "Round teal-blue velvet button cushion/pouf", "kind": "floor", "surface": "floor"},
    {"id": "S4BE9AE76", "file": "black-cream-sheepskin-throw", "cat": "lighting", "title": "Black-and-cream sheepskin", "sub": "Black and cream patched sheepskin throw", "kind": "floor", "surface": "floor"},
    {"id": "SA6FA3177", "file": "rose-flute", "cat": "lighting", "title": "Rose champagne flute", "sub": "Matching vintage rose champagne flute", "kind": "decor", "surface": "table"},
    {"id": "SE8C8CADD", "file": "faceted-pink-coupe", "cat": "lighting", "title": "Faceted pink coupe", "sub": "Fleur de Rose faceted pink coupe", "kind": "decor", "surface": "table"},
    {"id": "SC208AED4", "file": "black-cream-cowhide", "cat": "lighting", "title": "Black-and-cream cowhide", "sub": "Cowhide Rug Texture PNG", "kind": "floor", "surface": "floor"},
    {"id": "S2EA3E335", "file": "yellow-sheepskin-clam-chair", "cat": "lighting", "title": "Mustard sheepskin Clam chair", "sub": "Mustard sheepskin 'Clam' chair with black bentwood arms", "kind": "floor", "surface": "floor"},
    {"id": "S0AA342D4", "file": "burgundy-roll-arm-armchair", "cat": "lighting", "title": "Burgundy roll-arm chair", "sub": "Burgundy linen roll-arm armchair", "kind": "floor", "surface": "floor"},
    {"id": "SAEEEA93E", "file": "brown-mohair-channel-tufted-sofa", "cat": "lighting", "title": "Brown mohair sofa", "sub": "Brown mohair channel-tufted sofa with wood base", "kind": "floor", "surface": "floor"},
    {"id": "S4FDFFCBC", "file": "wood-console-tv-tapered-legs", "cat": "lighting", "title": "Wood console television", "sub": "1960s wood console television on tapered legs", "kind": "floor", "surface": "floor"},
    {"id": "SE2CD77E8", "file": "gold-1950s-portable-tv-rabbit-ears", "cat": "lighting", "title": "Gold portable television", "sub": "Gold-cased 1950s portable TV with rabbit-ear antennas", "kind": "media", "surface": "table"},
    {"id": "SF78FB89E", "file": "rust-red-geometric-kilim-rug", "cat": "lighting", "title": "Rust-red kilim rug", "sub": "Rust-red Scandinavian-style geometric kilim flatweave rug", "kind": "floor", "surface": "floor"},
    {"id": "SCA6C185E", "file": "pink-orange-diamond-kilim-fringed-rug", "cat": "lighting", "title": "Pink diamond kilim rug", "sub": "Pink/orange/cream diamond kilim rug with greek-key border and fringe", "kind": "floor", "surface": "floor"},
    {"id": "S8337BECB", "file": "orange-teal-navy-geometric-kilim-rug", "cat": "lighting", "title": "Orange and teal kilim rug", "sub": "Orange/teal/navy stepped-diamond kilim rug", "kind": "floor", "surface": "floor"},
    {"id": "S27580263", "file": "red-orange-heriz-medallion-rug", "cat": "lighting", "title": "Red Heriz-style rug", "sub": "Rust-red Heriz-style medallion rug", "kind": "floor", "surface": "floor"},
    {"id": "S1FE21145", "file": "aztec-black-tan-rug-perspective", "cat": "lighting", "title": "Black-and-tan Aztec rug", "sub": "Southwestern black/tan/cream Aztec rug photographed in perspective", "kind": "floor", "surface": "floor"},
    {"id": "SB05192FF", "file": "black-velvet-ribbon-cushion", "cat": "lighting", "title": "Ribbon-swirled velvet cushion", "sub": "Black velvet cushion with magenta/orange ribbon swirls", "kind": "decor", "surface": "table"},
  ];
  HNV_ITEMS.splice(0, HNV_ITEMS.length, ...samples.map(sample => ({
    id: sample.id, cat: sample.cat, title: sample.title, sub: sample.sub,
    img: `assets/demo/${sample.file}.webp`, chip: "demo",
  })));
  HNV_ROOM_PRODUCTS.splice(0, HNV_ROOM_PRODUCTS.length, ...samples.map(sample => ({
    id: sample.id, kind: sample.kind, surface: sample.surface,
    overlay: `assets/demo/${sample.file}.webp`,
  })));
  for (const id of Object.keys(HNV_PRICES)) delete HNV_PRICES[id];
  document.querySelector("#sort-select")?.closest("label")?.setAttribute("hidden", "");

  const item = id => HNV_ITEMS.find(item => item.id === id);
  function photo(selector, id) {
    const image = document.querySelector(selector), product = item(id);
    if (!image || !product) return;
    image.removeAttribute("srcset"); image.removeAttribute("sizes");
    image.src = product.img; image.alt = product.title;
  }
  document.body.classList.add("styling-demo");
  const banner = document.createElement("aside");
  banner.className = "styling-demo-banner";
  banner.setAttribute("aria-label", "Private photo preview");
  banner.innerHTML = '<p><strong>A fresh look at the collection.</strong>Polished styling samples, ready to try in your room.</p><a href="#collection">Explore the finds ↗</a>';
  document.body.prepend(banner);

  // Keep the entrance cutouts and the original neon-lit room photograph.
  photo(".department-lighting img", "A1");
  photo(".department-fashion img", "B1");
  photo(".department-art img", "A3");
  photo(".design-detail img", "A10");
  document.querySelector(".department-art p").textContent = "A little character for your walls.";
  document.querySelector(".design-room figcaption").textContent = "The room that started it.";
  document.querySelector("#category-filters [data-category=all] span").textContent = samples.length;
  // Print returns when a full, polished photograph is ready; no rough fallback.
  document.querySelector(".department-print")?.remove();
  document.querySelector("#category-filters [data-category=print]")?.remove();

  // The existing room photograph is the destination for room-tour links.
  for (const control of document.querySelectorAll("[data-open-walkthrough]")) {
    const link = document.createElement("a");
    link.className = control.className; link.href = "#story";
    link.innerHTML = control.innerHTML;
    control.replaceWith(link);
  }
  const tourCaption = document.querySelector(".salon-tour small");
  if (tourCaption) tourCaption.textContent = "The room that started it";
  document.querySelector("#walkthrough-dialog")?.remove();
  const videoDemo = document.querySelector(".room-demo");
  if (videoDemo) videoDemo.hidden = true;

  // Preserve the owner's introduction without the unfinished mirror selfie.
  document.querySelector(".owner-photo")?.remove();
  const ownerAside = document.querySelector(".owner-aside");
  if (ownerAside) ownerAside.textContent = "The wardrobe is another story.";
  const wardrobeLink = document.querySelector(".owner-copy .text-link");
  if (wardrobeLink) wardrobeLink.innerHTML = 'Explore the wardrobe <span aria-hidden="true">↗</span>';
  const notes = document.querySelectorAll(".notes-grid p");
  if (notes[0]) notes[0].textContent = "A curated mix of full product photographs, with the original neon-lit room as our inspiration.";
  if (notes[1]) notes[1].textContent = "These are photographic styling samples. Each find keeps the same image from the collection to your room.";
  if (notes[2]) notes[2].textContent = "A first look at the mix. These samples are for exploring the style; this preview does not take orders or payments.";
  document.querySelector(".price-notes")?.remove();
  const guide = document.querySelector(".collection-bottom > p");
  if (guide) guide.textContent = "Styling samples. Open a find to take a closer look or try it in your room.";

  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("room-use-example").click();
  });
})();
