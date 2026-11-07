# Verify on the PC: lanes 04 (ghost mannequin), 05 (AI try-on) and 11 (dress forms)

Date 2026-11-07. Sonnet subagent report, saved as returned. Brief: check each snippet-level claim in those three lanes against the pages crawled into `raw/fetched-on-pc/` on the PC, quoting licences and prices exactly; read-only, no network.

---

**Header.** Lanes 04, 05, 11. Index rows 30: 26 `page`, 4 `wall`. Opened 26: 23 real pages plus 3 not-found shells over 1 KB (eBay Ask-a-Mentor ghost thread "Page not found"; the eBay user-agreement URL, which lands on `error-404`; Walmart seller 13733 "This page could not be found"). WALLED (4): Etsy creativity-standards, Etsy sellers, eBay Acme sold search, Etsy photo-challenging-items handbook. NOT FETCHED (cited, not in index; earlier VERIFIED_FETCHED/MCP_DATA items not rechecked): 04 snappyit, retouchinglabs, GhostMannequinEngine, HF ghost LoRA and Spaces; 05 Kolors, IDM-VTON, OOTDiffusion, FitDiT, fal/xocialize/ovi054 cards; 11 dritzsewing, Etsy market pages, Subastral, talkofthehouse, markus-hagner, fixanyphoto, vintefy, dresma, wawak, rebeccagracequilting, Walmart `/ip/` pages. Evidence quotes come from the file in `raw/fetched-on-pc/` whose stem starts with the host shown. Vendor-authored: fashn, WearView, pixc, retouch4me, Mannequin Madness (Clipping Magic repost), listingtofreedom (affiliate), Mannequin Mall, Atlas Levy.

### Lane 04 ghost mannequin
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| Two shots: front, then inside-neck (turn form, garment inside out, or foam board) | pixc.com/blog/…photoshop; fashn.ai/blog/ghost-mannequin… | CONFIRMED | pixc: "turn your mannequin around … dress the mannequin again — but this time the garment needs to be inside out" |
| Plain dress form has no removable parts, more masking | retouch4.me/blog/… | CORRECTED (says retail display mannequins; exact sentence absent) | "Standard retail display mannequins create more editing work than they save. Fixed necks, rigid shoulders, and solid joints are difficult to remove cleanly" |
| Photoshop: Pen/Select Subject, warp, check at 100% | fashn | CONFIRMED | "trace the garment with the Pen tool (or start with Select Subject and refine)"; "Zoom to 100 percent" |
| Shadow layer at 35 to 40% | fashn; pixc | CORRECTED | fashn "a Multiply layer at 10 to 20 percent opacity"; pixc "black … opacity of 15%" |
| GIMP: Free Select, Foreground Select, mask, feather | retouchingzone.com/edit-… | PARTLY. Foreground Select and feather NOT ON PAGE | "Use the Free Selection tool or Lasso tool"; "Apply black colors on the layer mask to conceal … white to restore" |
| Time 15–20 / 45–60 min; beginners 2–3x; "40–60" | fashn; retouch4.me | CORRECTED ("40–60" NOT ON PAGE) | fashn "roughly 10 to 30 minutes per image, up to an hour for structured outerwear, and beginners should expect two to three times that"; retouch4me "15 to 30 minutes per item" |
| Outsourced $0.39–0.89 / $1–3 / $5–15 | fashn | CORRECTED | "start under $1 per image for a single neck join … $2 to $12 per image" |
| WearView $29/mo or $49 for 200 credits; from $0.19/image | wearview.co/blog/… | CORRECTED ($0.19 NOT ON PAGE) | "Lite plan at $29/month (50 credits), Pro at $49/month (200 credits), Advanced at $99/month (500 credits)" |
| Pixelz $0.95+$0.50; Photta $14/mo | wearview | CONFIRMED (page also says Photta "$9.95/month") | "From $0.95/image, plus $0.50 invisible mannequin"; "From $14/mo" |
| Pixelcut, Rewarx, Picjam, Claid, Pebblely prices | wearview and other lane-04 pages | NOT ON PAGE | no mention |
| Photoroom `ai.auto`, 1K default | docs.photoroom.com/…ghost-mannequin | CONFIRMED | "set the parameter `ghostMannequin.mode` to `ai.auto`"; "1K (`1024x1024`)"; 2K/4K "for Enterprise plans" |
| Photoroom input types, Android 3:2, pricing | same | NOT ON PAGE | only "meant to be used with images that feature clothing items"; no price |
| peterpeeterspeter: SDXL/ControlNet/Gemini, needs Gemini key | github.com/peterpeeterspeter/… | CONFIRMED | "6-step … using SDXL, ControlNet, and Gemini Vision"; `export GOOGLE_API_KEY="your-gemini-api-key"`. Also MIT, 2 stars, needs `HF_TOKEN` |
| FLUX.2-klein-base-9B "gated, licence other" | huggingface.co/black-forest-labs/…base-9B | CORRECTED | "License: flux-non-commercial-license" |
| eBay seller: flat lays outsold mannequin | community.ebay.com/…Using-a-mannequin… | CONFIRMED (n=1, locked old thread) | "I think if anything, the flat lay items are outselling the ones displayed on a mannequin." |
| Another seller's sales rose with dress form | same; Ask-a-Mentor | NOT ON PAGE; Ask-a-Mentor is a shell | replies: "No both are good."; "Looks better than laying loose." |
| AI "may redraw collars, prints, buttons or seams" | wearview; fashn | CORRECTED | wearview "AI reconstructs hidden garment parts (inner necklines, linings, seams)"; fashn "it can't show a label that isn't in your source photo" |
| Mannequin Madness: pinning and staging | blog.mannequinmadness.com/… | NOT ON PAGE (flat-lay/hanger overview) | "These tools have been falling out of style in recent years, and seem to be most prevalent in the wholesaler space." |

### Lane 05 AI try-on
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| Leffa MIT | github.com/franciszzj/Leffa/…LICENSE | CONFIRMED for code; dataset caveat NOT ON PAGE | "MIT License Copyright (c) 2024 Zijian Zhou Permission is hereby granted, free of charge" (grants "the Software" only) |
| fal try-on base FLUX.2-klein-9B: licence "other", unclear | huggingface.co/…FLUX.2-klein-9B | CORRECTED | "This model falls under the FLUX Non-Commercial License."; "Available for non-commercial use." |
| 4B base Apache-2.0 (xocialize) | same | CONFIRMED for base only; LoRA card not fetched | "4B models under an Apache 2.0 license and … 9B models under a non-commercial license" |
| CatVTON Windows problems | github.com/Zheng-Chong/CatVTON/issues/8 | CONFIRMED | "This issue will be kept and update to provide guidance for Win Users."; user error "No module named 'cv2'" (fix `pip install opencv-python`), 8192 MB card |
| eBay does not ban AI photos as a category | ebay.com/help/policies/…picture-policy?id=4370 | NOT ON PAGE (silent on AI) | — |
| Stock photos barred for used goods | same | CONFIRMED | "Stock photos for used, damaged, or defective items"; "Photos that don't accurately represent the item" |
| Seller responsible for generative-AI listing content | ebay.com/help/policies/ebay-user-agreement | SHELL (404). Cross-lane, lane 13 `www.ebay.com_help_policies_member_behavior_policies_user_agreement_id_4259.md` | "You assume full responsibility for the item offered and the accuracy and content of the listing, including … image editing, and generative artificial intelligence tools" |
| Community: AI looked better, NAD risk, real first, label | community.ebay.com/forum/…ai-generated-model-photos… | CONFIRMED (two repliers are vendors: Katalogiq, Sorquil) | "the clothing quality looked a lot better in the AI photos than in the actual photos"; "keep real photos of the item primary and clearly label any generated image" |
| eBay tests AI models without consent | valueaddedresource.net/… | CONFIRMED (Published Apr 14 2026) | "eBay is testing AI generated fashion models, adding altered images to seller listings without warning or explicit consent." |
| Etsy AI disclosure; Oct 2026 unedited photo | etsy.com/legal/… (2) | WALLED | — |

### Lane 11 forms
| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| VFG: wide shoulders limit fit; removable arms; Wolf pop-in shoulders | forums.vintagefashionguild.org/… | CONFIRMED (Dec 25, 2017, 3 posts). "Vintage adjustables adjust worse", wire forms NOT ON PAGE | "you will be better off with a mannequin with removable arms"; "Wolf forms where the shoulders push in and then pop out (once dressed)" |
| Etsy handbook: pins, tape, tissue | etsy.com/seller-handbook/… | WALLED. Nearest: lane 10 botika file | botika: "Pin at the back and pad the shoulders and sleeves with tissue." |
| Binder clips, bra, black cloth, dress forms need more retouching | mannequinmadness | NOT ON PAGE (tissue there is for flat lays); fixanyphoto NOT FETCHED | — |
| Dritz My Double Medium $155; bust 39.5–45.5 | atlaslevy.com/…p_49.html | CONFIRMED (stock ambiguous) | "Your Price: $155.00"; "Bust/Chest: 39½" - 45½""; "Waist: 31½" - 38""; "Hips:41" - 47""; "Availability: In Stock" beside waitlist text |
| Fabulous Fit sizing; price | theshopcompany.com/…fabulous-fit | CONFIRMED sizing; "$85.00" is the default variant only (FF-S, Small, Half Body); "add 1 to 3 inches" and "never down" NOT ON PAGE | "Medium | Female 6 - 10 and Male 34 -36" (final size after padding) |
| Mannequin Mall French $183–$305; white linen $349.99; MM-B5W-NF | mannequinmall.com/collections/female-dress-forms | CORRECTED: second number is regular price. Linen $349.99 and MM-B5W-NF NOT ON PAGE (7 products, "Page 1 of 1") | "Female French Dress Form With Round Base MM-FFDRB from $182.99 $305.00"; "Female Pinnable Dress Form with Movable Arms MM-BFWH-1WM $212.99 $305.00" |
| Antique linen form $375 | fadedfragments.com/… | CONFIRMED price, but unavailable | "$375.00"; "Default Title - Sold Out"; "antique canvas linen mannequin with a spindle base" |
| Roxy Display prices | walmart.com/seller/13733 | SHELL (unverified) | "This page could not be found." |
| No full-size pinnable form under $60 | amazon.com/pinnable-dress-form/s | CORRECTED. Page is "Delivering to Fort Myers 33908", many rows Sponsored | "Bonnlo Female Dress Form Pinnable Mannequin Body Torso with Wooden Tripod Base Stand (Beige, 10-12)" `$49.99`, then "$19.99 delivery"; (White, 6) $36.00; (White, 2-4) $29.99; all plus $19.99 delivery |
| Budget list: Dritz Sew You, SINGER, PDM, Bonnlo 51–66 in | amazon; listingtofreedom.com/… | CONFIRMED, now priced (new; the second figure is used/new offers) | Sew You Small/Medium US 4-12 $129.99; SINGER Small/Medium 4-10 $174.99; PDM Size 6-14 $139.99; Bonnlo "Height is adjustable (51″-66″)" |
| Acme sold prices | ebay.com/sch/… | WALLED | — |

### What changes in docs/ebay-photo-studio.md
- §4 Do not use. Current: "AI virtual try-on (IDM-VTON, CatVTON, OOTDiffusion, FitDiT): CC BY-NC or gated non-commercial licences…". Those four were not re-fetched. Add: "Also anything on FLUX.2-klein-9B (the fal try-on LoRA, the ghost-mannequin LoRA): 'This model falls under the FLUX Non-Commercial License.' Leffa's MIT covers 'the Software' only; dataset terms unchecked. Apache-clean base is FLUX.2-klein-4B."
- §4 Paid fallback. Current: "Its single-photo ghost mannequin mode exists but regenerates pixels…". Add: "default output '1K (1024x1024)', 2K/4K Enterprise only, below the 1600 px listing size; the page shows no price; the optional `ghostMannequin.prompt` 'guide[s] the generation style'."
- §3 (outside your list). Current: "eBay's current page on AI-edited photos could not be opened from here". The User Agreement is now fetched (lane 13): sellers carry responsibility for "generative artificial intelligence tools". The picture policy is still silent on AI.
- §5 Form. Current: "One adjustable, pinnable dress form with an adjustable pole…". Add "with removable or collapsible arms/shoulders" (VFG; Mannequin Mall: "Collapsible shoulders and/or arms are offered for sellers who need to clothe their mannequins with finished clothing articles").
- §5 Prices. Current: "Dritz My Double about $155 … Mannequin Mall French forms $183 to $305 … antique linen spindle-base form $375. No full-size pinnable form under $60 was confirmed." Replace: "Opened 2026-11-07: Dritz My Double Medium $155.00 (bust 39½"–45½", too big for a 6–8; stock unclear); Mannequin Mall French from $182.99 (regular $305.00); antique spindle form $375.00 but Sold Out. Amazon pinnable tripod forms: Bonnlo $29.99 (2-4), $36.00 (6), $49.99 (10-12), each plus $19.99 delivery. Etsy $125, Roxy and Acme prices still unverified."
- §5 Padding. Current: "buy the smaller form and pad up with batting". Add Fabulous Fit "Medium | Female 6 - 10"; the $85.00 shown is Small/Half Body.
- §5 Pinning kit. Clips, pins and tissue now have a source (botika, lane 10). Black cloth and padded bra remain unsourced; listingtofreedom adds painter's tape and "a clip or two".
- §5 Lighting. Current: "the form five or six feet in front of the backdrop". pixc: "at least five feet away from the backdrop". fashn's "five or six feet" is softbox-to-form distance. "Two softboxes at 45 degrees" is confirmed (fashn, retouch4me).
- §6. Current: "20 to 45 minutes a piece by hand (vendor figures, snippet-level)". Replace: "10 to 30 minutes skilled, up to an hour for structured outerwear, two to three times that for a beginner (fashn; retouch4me says 15 to 30)". Change "a FLUX LoRA that regenerates the garment" to "…on a non-commercial 9B base". Add: purpose-built ghost torsos "start around $300" (fashn), and fashn says a standard mannequin "works too, but you'll spend longer in Photoshop".

### Forms and mannequins
- Shape: "you will be better off with a mannequin with removable arms" (forums.vintagefashionguild…, 2017); a basic wide-shoulder form passed "only clothing with large waists".
- Cheap: pinnable foam torsos exist under $60 new, e.g. Bonnlo $49.99 + "$19.99 delivery" (amazon file). Mid-range adjustables run $129.99 to $174.99 (Dritz Sew You, SINGER).
- Vintage-look: "Female French Dress Form With Round Base MM-FFDRB from $182.99 $305.00"; "Female Professional Dress Form with Collapsible Shoulders MM-PFDCS from $427.99 $570.00" (mannequinmall file).
- Where sellers say it matters (cross-lane): chapeau-noir, "If I'm selling draping items, kimono, lagenlook, silks, etc., I use a mannequin because they display better" (`community.ebay.com_t5_Selling_Do_the_quality…`, lane 16); "Flat-lay photography can hide drape problems, fit issues, or shoulder distortion" (blondesinheaven, lane 09).
- Counter-evidence: the eBay OP above, and "falling out of style … wholesaler space" (mannequinmadness).

### Surprising, not in the decision doc
- VAR (Apr 14 2026): "sellers have no way to opt out of having these AI tests and features applied to their listings". A no-AI policy cannot keep eBay's AI model images off Ricky's listings. The thread's example: "AI 'filled in' sleeve details … The collar is different".
- The ghost vendors sell interior invention. WearView: "AI reconstructs hidden garment parts". A reconstructed label or neck is made up for a one-off used garment, which backs the §6 caution.
- The eBay "Flay lay vs Mannequin" thread (lane 16) is also a 404 shell. The only mannequin-versus-flat-lay thread with content is the locked one.
- Atlas Levy lists Dritz Petite at $214.95, above the Medium's $155.00.
