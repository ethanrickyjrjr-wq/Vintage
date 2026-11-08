# eBay listings, batch of 2026-11-08 (seven garments)

Source: 21 iPhone HEICs shot 2026-11-08 against the grey Jeep door (Ricky's Downloads, `IMG_2298` to `IMG_2352`).
Images: `assets/ebay-2026-11-08/ebay/` (1600 x 1600, white, item at 85 percent; upload these). The 2048 masters
(`listing/`) and transparent PNGs (`site/`) are on the PC only (gitignored). `manifest.csv` has one row per photo.

How the images were made: front and back shots were cut by the Photoroom Remove Background API
(`POST https://sdk.photoroom.com/v1/segment`, `format=png`, `size=full`; docs re-read 2026-11-08). The key's
10 free production calls ran out after ten cuts (HTTP 402 on the eleventh), so the four shots marked
`birefnet` in the manifest were cut by the local model in `tools/cutout/cutout.py` instead. The tag photos are
kept exactly as shot and only resized. Pixels were never regenerated; the hanger stays in the shot.

Prices below are my ballpark from memory, not comps. eBay sold listings need the signed-in Chrome tab
(see `vintage-media-fetch` memory); do that pass before publishing or price to move.

**Condition is unassessed.** I saw the photos, not the garments. Check every piece for stains, pulls, pilling,
missing buttons, odour and seam wear before listing, and photograph any flaw in the same light.

## The numbers eBay needs

Every listing needs the label size plus flat measurements in inches. Lay the garment flat, tape it, write the
numbers here, then copy them into the description and the item specifics. None of these can be read from the photos.

| # | Item | Label size | Pit to pit | Shoulder to shoulder | Sleeve (shoulder seam to cuff) | Waist flat | Hip flat | Length | Extra |
|---|------|-----------|------------|----------------------|-------------------------------|------------|----------|--------|-------|
| 1 | Liz Claiborne leopard shirt dress | 8 | | | | | | shoulder seam to hem | |
| 2 | Future Collective slip dress | S | (across top edge) | n/a | strap length | | | top of strap to hem, and top edge to hem | slit length |
| 3 | Ronny Kobo plunge dress | XS | | | | | | shoulder seam to hem, front and back | depth of V from shoulder |
| 4 | Brooks Brothers chino shorts | 10 | n/a | n/a | n/a | | | n/a | front rise, inseam, leg opening |
| 5 | The Limited green blouse | S | | | | n/a | n/a | back collar seam to hem | front length |
| 6 | Starlo vintage dress | not on tag, see below | | | | (relaxed and stretched) | | shoulder seam to hem | |
| 7 | We The Free wide-leg jeans | 29 | n/a | n/a | n/a | | | n/a | front rise, back rise, inseam, leg opening |

Item 6 has no size on the Starlo label. Look for a second tag at the side seam; if none, list by measurements and
"best fits a modern S/M" only after measuring.

## 1. Liz Claiborne leopard print shirt dress

- Photos: `01-liz-claiborne-leopard-shirt-dress-front.jpg`, `-back.jpg`, `-tag.jpg`
- Label: Liz Claiborne Dresses, size 8, 100% polyester, Made in China, RN 52002, CA 16396
- Title (80 max): `Vintage 90s Liz Claiborne Blue Black Leopard Print Double Breasted Midi Shirt Dress 8`
- Item specifics: Brand Liz Claiborne; Department Women; Size 8; Size Type Regular; Type Shirt Dress; Style Shirt Dress; Dress Length Midi; Sleeve Length Short Sleeve; Neckline Collared (notched lapel); Pattern Animal Print (leopard); Color Blue, Black; Material 100% Polyester; Closure Button; Features Elastic Waist, Double Breasted; Vintage Yes; Decade 1990s; Occasion Casual, Work; Country China
- Description: Bright periwinkle blue with a black leopard spot, notched lapel collar, double row of dark buttons down the front, short cuffed sleeves, shirred elastic waist, full midi skirt. Classic 90s Liz Claiborne Dresses label. Lightweight polyester, hangs and travels well, no ironing.
- Ballpark: $32 to $48 (unverified)

## 2. Future Collective floral lace-trim slip dress

- Photos: `02-future-collective-floral-slip-dress-front.jpg`, `-back.jpg`, `-tag.jpg`
- Label: Future Collective (Target), size S, Made in China. Fabric not on the tag photographed; read the care label.
- Title: `Future Collective Pink Cream Mixed Floral Lace Trim Tie Strap Slip Midi Dress Size S`
- Item specifics: Brand Future Collective; Department Women; Size S; Type Slip Dress; Style Slip Dress; Dress Length Midi; Sleeve Length Sleeveless; Neckline Square (lace trimmed); Pattern Floral; Color Pink, Cream, Black; Features Lace Trim, Adjustable Tie Straps, Front Slit; Closure Pullover (confirm: check for a side zip); Occasion Casual, Party
- Description: Two-print slip dress, blush pink sprig print on top meeting a cream ditsy floral on a diagonal seam, eyelash lace at the neckline and hem, tie shoulder straps, front slit. Satin-finish, lined or unlined (confirm). Target's Future Collective line, recent season.
- Ballpark: $14 to $24 (unverified)

## 3. Ronny Kobo rose jacquard plunge dress

- Photos: `03-ronny-kobo-rose-jacquard-plunge-dress-front.jpg`, `-back.jpg`, `-tag.jpg`
- Label: Ronny Kobo, size XS, Made in China. Fabric not on the tag photographed; read the care label (the hand looks like a viscose or silk-blend jacquard).
- Title: `Ronny Kobo Rose Pink Leaf Jacquard Plunge V Neck Long Puff Sleeve Ruched Maxi Dress XS`
- Item specifics: Brand Ronny Kobo; Department Women; Size XS; Type Maxi Dress; Style Bodycon, Wrap-look; Dress Length Long; Sleeve Length Long Sleeve; Sleeve Type Puff; Neckline Plunge V; Pattern Floral jacquard (tone on tone); Color Pink, Rose; Features Ruched front seam, Keyhole back, Padded or gathered shoulders; Closure Button at back neck (confirm zip); Occasion Cocktail, Wedding Guest, Evening
- Description: Dusty rose tone-on-tone palm-leaf jacquard, deep plunge V with draped bodice, gathered puff shoulders, long fitted sleeves, ruched centre seam down the fitted skirt with a fishtail-style hem, keyhole back. Designer piece, retails in the high hundreds. Fitted cut: measurements matter more than the XS here.
- Ballpark: $65 to $120 (unverified)

## 4. Brooks Brothers Advantage Chino shorts

- Photos: `04-brooks-brothers-white-chino-shorts-front.jpg`, `-back.jpg`, `-tag.jpg`
- Label: Brooks Brothers Advantage Chino, size 10, 100% cotton, Made in Malaysia
- Title: `Brooks Brothers Advantage Chino White Cotton Flat Front Walking Shorts Women's Size 10`
- Item specifics: Brand Brooks Brothers; Department Women; Size 10; Type Chino Shorts; Style Walking Shorts; Color White (confirm white vs ivory in daylight); Material 100% Cotton; Rise High (confirm by measuring); Inseam from sheet; Features Belt Loops, Side Slant Pockets, Back Darts, Hem Vents; Closure Zip with hook and bar; Pattern Solid; Occasion Casual, Golf, Resort
- Description: Crisp white cotton twill, flat front, slant pockets, belt loops, small side vents at the hem, darted back. The Advantage Chino is Brooks Brothers' non-iron stretch-free chino cloth. White shorts: look hard for marks before listing.
- Ballpark: $16 to $28 (unverified)

## 5. The Limited green blouse

- Photos: `05-the-limited-green-blouse-front.jpg`, `-back.jpg`, `-tag.jpg`
- Label: The Limited, size S, Made in Indonesia. Fabric not on the tag photographed; almost certainly polyester, read the care label.
- Title: `The Limited Kelly Green Button Front Blouse Roll Tab Long Sleeves Chest Pocket Size S`
- Item specifics: Brand The Limited; Department Women; Size S; Type Blouse; Style Button-Up; Color Green; Sleeve Length Long Sleeve (roll tab); Neckline V-Neck with point collar; Pattern Solid; Features Chest Pocket, Roll Tab Sleeves, Back Yoke Pleat, Shirttail Hem; Closure Button; Occasion Work, Casual
- Description: Saturated kelly green, lightweight crepe, point collar over an open V, single chest pocket, long sleeves with button roll tabs, back yoke with a box pleat, curved shirttail hem. The Limited's work-blouse staple.
- Ballpark: $12 to $20 (unverified)

## 6. Starlo Fashions vintage pleated blouson dress

- Photos: `06-starlo-red-abstract-vintage-dress-front.jpg`, `-back.jpg`, `-tag.jpg`
- Label: Starlo Fashions, Made in U.S.A., RN on the label (the tag photo is in the set; the number reads 48569 but confirm by eye). No size tag photographed.
- Title: `Vintage 80s Starlo Fashions Red Black Abstract Moire Print Pleated Blouson Midi Dress USA`
- Item specifics: Brand Starlo Fashions; Department Women; Size from measurements; Type Blouson Dress; Style Secretary, Blouson; Dress Length Midi; Sleeve Length Long Sleeve; Neckline Round (jewel); Pattern Abstract (moire / woodgrain); Color Red, Black; Material likely polyester, read the care label; Features Elastic Waist, Accordion Pleated Skirt, Keyhole Back, Button Cuffs; Vintage Yes; Decade 1980s; Made in USA
- Description: Bold red-on-black abstract moire print, bloused bodice over an elastic waist, long sleeves with button cuffs, round neck with a button keyhole at the back, fine accordion-pleated skirt. Union-era Made in USA label. Sheer-ish georgette: say whether it is lined.
- Ballpark: $38 to $65 (unverified)

## 7. We The Free wide-leg jeans

- Photos: `07-we-the-free-wide-leg-jeans-front.jpg`, `-back.jpg`, `-tag.jpg`
- Label: We The Free (Free People's denim label), size 29. Fabric content and style name are on the inside waistband or pocket-bag label; photograph it.
- Title: `Free People We The Free Light Wash High Rise Wide Leg Jeans Flap Patch Pockets Size 29`
- Item specifics: Brand Free People; Line We The Free; Department Women; Size 29; Waist Size 29 in (confirm flat x2); Type Jeans; Style Wide Leg; Rise High; Wash Light; Color Blue; Fit Relaxed; Features Flap Patch Front Pockets, Seamed V Back Yoke, Button Fly or Zip (confirm); Inseam from sheet; Material Cotton (confirm stretch)
- Description: Light vintage-blue wash, high rise, full wide leg from the hip, button-flap patch pockets on the front, seamed western-style V yoke across the back, long inseam (measure: these look full length on a tall frame). Free People's We The Free denim.
- Ballpark: $42 to $70 (unverified)

## Shoot notes for next time

- Same light, same hanger works. For the model's sake, hang dark items on the pale hanger and pale items on the black one, and keep the car's chrome handle out of the frame (it sits behind the shorts in shot 2335 and the model has to guess around it).
- Add a measurements-card shot per item (tape visible on pit to pit and length), a fabric close-up, and every flaw. eBay allows 24 photos; aim for eight.
- Shoot the care label as well as the brand label: fabric content was missing for items 2, 3, 5 and 7.
