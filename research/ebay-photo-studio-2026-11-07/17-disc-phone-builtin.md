# Lane 17: built-in phone and Windows background removal (no-software route)

Status, 2026-11-07. Fetched and saved: only two GitHub pages (raw/17-disc-phone-builtin/github_com_adityaarsharma_grabio.md and github_com_topics_background_remove.md). Blocked (proxy 403 on CONNECT, tested once each): support.apple.com, support.microsoft.com, support.google.com, www.ebay.com, routinehub.co. Also 403 or under 1 KB on every third-party page tried: xda-developers, maketecheasier, bgclear.ai, macnative, pureinfotech, bleepingcomputer, innovation.ebayinc.com, valueaddedresource, petapixel, howtogeek, matthewcassinelli.com, blog.routinehub.co. So nearly everything below is SEARCH_SNIPPET (WebSearch summaries, not page text) or UNVERIFIED. No exact quotes from Apple or Microsoft pages could be taken. Treat all steps as "to confirm on the device".

## Findings

1. iPhone lift subject, iOS 16 (SEARCH_SNIPPET). Press and hold the subject in Photos and it lifts out; you can drag it into Messages, Mail, Notes. Works in Photos, Files, Messages, Safari, Quick Look and screenshots. Needs A12 Bionic or later. Source: https://www.xda-developers.com/how-to-remove-backgrounds-photos-ios-ipados-16/ (search summary, page not fetched). Sourced to iOS 16 only; the "Copy Subject" menu wording is UNVERIFIED from memory.
2. Shortcuts action (SEARCH_SNIPPET): a MacNative list names the default media action "Remove Image Background" (removes the background from an image, keeping the subjects), plus "Save to Photos" and "Find Photos". Source: https://macnative.com/list-of-default-media-actions-for-ios-shortcuts/ . Another guide calls it "Remove Background from" (iOS 16 action), so the exact label differs by iOS version.
3. Batch chain for a whole album (SEARCH_SNIPPET, not confirmed by any source as a working recipe): Find Photos (filter Album) or Select Photos, then Repeat with Each, then Remove Image Background, then Save to Photos. An Apple Community thread says a single-image shortcut needs a Repeat with Each block enclosing the remove and save actions. Source: https://discussions.apple.com/thread/254979394 . A RoutineHub single-image shortcut exists: https://blog.routinehub.co/how-to-remove-the-photo-background-with-shortcuts-in-ios-16/ and https://matthewcassinelli.com/shortcuts/remove-background-from-photo/ (both blocked, single image only per the summary).
4. Files app batch (SEARCH_SNIPPET, sources conflict): put the photos in an album, share to Files, select them, Quick Actions, Remove Background; copies are saved beside the originals. One guide says it works on several files at once, another says one by one. Source: https://maketecheasier.com/iphone-batch-edit-photos-videos/ . Test with 5 photos.
5. Output of these is a cutout PNG with transparency (SEARCH_SNIPPET only for Windows; for iPhone UNVERIFIED). For eBay a white background must be added afterward; iPhone Shortcuts has no confirmed "fill white" action in my sources. Grabio (below) lists a "White Background Fill" utility.
6. Grabio (VERIFIED_FETCHED, GitHub page). "An iOS 14+ Apple Shortcut that adds 25+ file utilities to your iPhone share sheet"; includes "AI background remove" and "White background fill" ("Share photo -> White Background Fill"). Sends the file to the author's backend over HTTPS. "The Apple Shortcut itself is closed-source." Free "5 actions/day"; Pro exists. 4 stars. Docs MIT. Source: https://github.com/adityaarsharma/grabio . Privacy cost: Ricky's product photos go to a third-party server. Low trust, low popularity.
7. Other API-recipe shortcut: bgclear.ai "Get Contents of URL + API recipe" (SEARCH_SNIPPET, title only): https://www.bgclear.ai/blog/ios-shortcut-remove-background-api/ . Needs a paid third-party API.
8. iOS 18 Clean Up (SEARCH_SNIPPET). Removes distracting objects, not backgrounds. Apple Intelligence, iOS 18.1 or later, iPhone 15 Pro and Pro Max and iPhone 16 line (one non-Apple source adds iPhone 17). Not available in China mainland. Official page: https://support.apple.com/121429 (blocked). Useful for erasing a stray cord or rack bar, not for whiting out the background.
9. Windows 11 Photos app (SEARCH_SNIPPET): edit view has a Background button; saves a PNG to keep transparency; can replace background; "Background brush tool" refines. An older article says it started with Insiders. Sources: https://pureinfotech.com/remove-replace-image-background-photos-windows-11 , https://www.elevenforum.com/t/remove-background-of-image-in-photos-app-in-windows-11.19741/ . Batch: none found.
10. Windows 11 Paint (SEARCH_SNIPPET): background removal detects the subject automatically, or use Select for part of the image. Source: https://www.bleepingcomputer.com/news/microsoft/microsoft-paint-in-windows-11-gets-a-background-removal-feature/ and https://pureinfotech.com/remove-image-background-paint-windows-11/ . One image at a time. Version added: not established.
11. Snipping Tool: no background removal found in any source (SEARCH_SNIPPET, absence of evidence).
12. Google Photos Magic Editor (SEARCH_SNIPPET): moves, removes, resizes people or objects and changes background (sky presets). Pixel 8 and later, some Samsung via Google Photos. It is scene-editing, not a clean white cutout. https://store.google.com/intl/en_in/ideas/articles/magic-editor . Ricky has an iPhone, so low relevance.
13. Samsung Gallery (SEARCH_SNIPPET): Object Cut Out / Image Clipper in Gallery since One UI 5.1; Object Eraser is separate. Not relevant to an iPhone owner.
14. eBay app background tools (SEARCH_SNIPPET). Mobile app listing flow has a background removal tool and replacement backgrounds (white, studio, AI); "Background Enhancement" AI tool for iOS users in US, UK, Germany first. A trade report (valueaddedresource) says eBay temporarily disabled the background remover in the app and sellers lost eraser and brush refinement tools; status now unknown. Sources: https://innovation.ebayinc.com/stories/background-swap-tool-turns-any-photo-into-a-studio-quality-product-image/ , https://petapixel.com/2024/06/13/ebay-releases-ai-photo-tool-allowing-sellers-to-generate-backgrounds/ , https://www.valueaddedresource.net/ebay-sellers-lose-background-removal-in-app/ , https://www.ebay.com/sellercenter/listings/photo-tips (all blocked). Caution: eBay's own AI backgrounds are generated scenes; for clothing the safe look is plain white, so use the white option only.

## Step card for the iPhone today (all steps UNVERIFIED on device; confirm menu names)

A. One photo: open Photos, open the picture, press and hold the garment/mannequin until a glow outline appears, release, choose Copy Subject (or Share/Save as image). Paste into Notes or Files to inspect the edge.
B. Batch via Files: Photos, select the photos, Share, Save to Files. In Files, long-press the selection, Quick Actions, Remove Background. Expect PNG copies with transparent backgrounds beside the originals. Check it handled all, not just one.
C. Batch via Shortcuts: new Shortcut, add Select Photos (Select Multiple on), Repeat with Each, inside it add Remove Background (search "Remove"), then Save to Photo Album or Save File. Run it on 5 photos.
D. White fill: no confirmed built-in. Cutouts go to the PC and the lane pipeline puts them on pure white (255,255,255) there; do not send to unknown servers.
E. Do not use Clean Up for backgrounds. Do not use eBay's AI "generate background"; choose plain white only.

## Quality notes (UNVERIFIED, from general knowledge, to be tested)
Apple's cutout tends to trim thin straps, lace and sheer fabric, and may take the mannequin pole or base as part of the subject or drop the head. A dress form against a burgundy wall is high contrast, which helps. Fur, feathers (the feather hat) and sheer fabric will likely fail. These tools are fine for a first test and for flat shoes, lamps, small glass; the PC-side models should handle fabric edges better.

## Recommendations for Ricky
1. Try step B and C on the same 5 example photos tonight; judge the edge on a white-fill check at 100% zoom.
2. Use the phone route only as a stopgap. The main pipeline on the RTX 4060 Ti should be the real route; this lane gives a no-install fallback.
3. Skip Grabio and API-recipe shortcuts (closed source, uploads photos to a third-party server, daily caps).
4. Do not rely on eBay in-app background removal; reports of it being pulled, and it changes by account.
5. Windows Photos and Paint remove background one image at a time; useless for volume.

## Open questions
- Which iOS version and iPhone model does Ricky have (decides Clean Up, Shortcuts action names)?
- Does the Files Quick Action batch several images in one go?
- Does the Shortcuts "Remove Image Background" action output PNG alpha, and is there a white-fill action (e.g. Combine Images or Overlay) that lets one shortcut finish the job?
- Is the eBay in-app remover currently enabled for Ricky's account?

## URLs to fetch once the network opens
- https://support.apple.com/121429 : Clean Up requirements (official).
- https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iph... (search support.apple.com "Lift a subject from the photo background") : official steps and iOS version.
- https://support.apple.com/guide/shortcuts/ : official Shortcuts action list, confirm "Remove Background" action name and iOS version.
- https://support.microsoft.com/ (search "Photos remove background", "Paint remove background") : Windows versions.
- https://www.ebay.com/sellercenter/listings/photo-tips and the eBay help page for background removal : official policy, current availability. Also eBay's picture policy for white background rules.
- https://www.valueaddedresource.net/ebay-sellers-lose-background-removal-in-app/ , https://maketecheasier.com/iphone-batch-edit-photos-videos/ , https://discussions.apple.com/thread/254979394 : full text for batch behavior.
- https://routinehub.co/ and https://matthewcassinelli.com/shortcuts/remove-background-from-photo/ : shortcut downloads.
- https://store.google.com/intl/en_in/ideas/articles/magic-editor : Magic Editor (low priority).
