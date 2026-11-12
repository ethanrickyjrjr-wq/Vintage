# Shoe photos, 2026-11-12

Source: Drive folder `11/12` (allstatecoop@gmail.com). Six pairs, 45 shoe photos (`IMG_2606` to `IMG_2654`, plus `IMG_7027` added at 22:08). `IMG_7024` and `7025` from the same upload are a print shirt and a grey jacket, not shoes.

| Pair (folder) | Photos | Background |
|---|---|---|
| Michael Kors snake slip-on sneakers (`mk`) | 2606–2611, 2647 | light grey `EDEDED`: white sole and midsole |
| Golden Goose Ballstar, silver (`ggdb`) | 2612, 2614–2616, 2613, 2645 | grey: cream foxing, silver upper |
| Charles by Charles David black block-heel loafers (`charles`) | 2617–2621, 2627, 2646, 7027 | white |
| Antonio Melani knotted mules, caramel, 10M (`melani`) | 2622–2626, 2629, 2653, 2654 | white |
| Zara silver slingback kitten heels (`zara`) | 2631–2635, 2630, 2648 | grey: silver on white loses its edge |
| Johnston & Murphy grey woven slip-ons (`jm`) | 2636–2640, 2641 | grey: cream sole edge |

Rule carried from 2026-11-08: no white-on-white sole, so the whole pair goes on grey wherever a white or cream sole shows (one background per listing). Label close-ups and tape heel-height shots are kept as shot, only turned upright and resized; they are never cut out.

**Done:** the 12 kept-as-shot images are in `assets/ebay-2026-11-12/shoes/<pair>/`.
**Waiting on the Photoroom API key:** the 30 cut-outs. `tools/photoroom-shoes/run.py` sends each one to `image-api.photoroom.com/v2/edit` (background removed, colour per `shots-2026-11-12.csv`, 10% padding, soft AI shadow, 1600×1600 JPEG). Photoroom bills $0.10 a call, about $3 for this set, and a re-run is billed again, so finished files are skipped. Run it from the repo with `PHOTOROOM_API_KEY` set and the folder of HEICs as the argument. This cloud session got HTTP 401 without a key, so nothing was billed.

**Skipped:** 2643 and 2644 (J&M size label, both out of focus) and 2628 (same view as 2629).
**Reshoot if possible:** insole labels 2646 (Charles), 2647 (MK) and 2648 (Zara) are soft; the J&M size is unreadable. Sizes still unread: MK, Golden Goose, Charles (7027 reads 10M, but it is not yet confirmed which pair it belongs to), Zara, J&M.
