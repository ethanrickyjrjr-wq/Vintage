# Verify on the PC: lane 17 (phone built-in tools)

Date 2026-11-07. Sonnet subagent report, saved as returned. Brief: check each snippet-level claim in `17-disc-phone-builtin.md` against the pages crawled into `raw/fetched-on-pc/` on the PC; read-only, no network. The first pass found that `fetch-later.md` held Apple's guide root pages, not the step articles; four articles were then added to `fetch-later.md` under "Added on the PC 2026-11-07", crawled, and handed back to the same agent. Its addendum follows the first report.

---

## Lane 17 re-verification (phone built-in tools)

**Pages read: 9. Walled: 1 (discussions.apple.com 254979394, 921 bytes). NOT FETCHED: 11 cited URLs (xda, macnative, bgclear, bleepingcomputer, pureinfotech x2, elevenforum, innovation.ebayinc, petapixel, ebay.com sellercenter/photo-tips, blog.routinehub).**

Read-only; I made no network calls and wrote no files.

Four of the nine "page" rows are landing pages, not article pages. The fetch-later list held root URLs, so the crawl got the roots: `support.apple.com/guide/iphone/`, `/guide/shortcuts/`, `support.microsoft.com/` and `routinehub.co/`. None contains step text. **No Apple page with step wording was fetched**, so the brief's premise that "the source is now a fetched Apple page" does not hold for the phone steps. Both Apple guide landing pages render iOS 27: their links carry `/ios/27` and `/10.0/ios/27`.

### Verdict table

All files are in `research/ebay-photo-studio-2026-11-07/raw/fetched-on-pc/`.

| Claim | URL | Verdict | Evidence |
|---|---|---|---|
| Lift subject: press and hold in Photos, iOS 16, needs A12 | xda-developers (how-to-remove-backgrounds-photos-ios-ipados-16) | NOT FETCHED | A12 and iOS 16 appear on no fetched page. |
| Apple's own "Lift a subject" steps | support.apple.com/guide/iphone/ | NOT ON PAGE | Title link only: "Lift a subject from the photo background" (`support.apple.com_guide_iphone_.md`, line 225). |
| "Copy Subject" menu wording | none | NOT ON PAGE | Absent from every fetched file. |
| Shortcuts action "Remove Image Background" / "Remove Background from" | support.apple.com/guide/shortcuts/ ; macnative | NOT ON PAGE (Apple); NOT FETCHED (macnative) | Landing page only: "An action—the building block of a shortcut—is a single step in a task." (`support.apple.com_guide_shortcuts_.md`) |
| Batch chain: Repeat with Each around Remove and Save | discussions.apple.com/thread/254979394 | WALLED | "Security verification in progress. Please wait while we verify your browser" (`discussions.apple.com_thread_254979394.md`) |
| Single-image shortcut exists (Cassinelli) | matthewcassinelli.com/shortcuts/remove-background-from-photo/ | CONFIRMED (exists); "single image only" NOT ON PAGE | "Save the foreground subject of any photo at the image's original size." It does not say whether batch works or what the output format is (`matthewcassinelli.com_shortcuts_remove_background_from_photo_.md`). |
| RoutineHub batch shortcut | routinehub.co | NOT ON PAGE | Homepage listing only. The only "background" hit is an icon maker. blog.routinehub is NOT FETCHED. |
| Files app: Quick Actions, Remove Background, works on several files | maketecheasier.com/iphone-batch-edit-photos-videos/ | CONFIRMED (third-party, published Mar 19 2026; no iOS version named) | "select all the images in your album and tap the Share icon… Save to Files… Select all the images you've copied and press the dot icon at the bottom. Go for Quick Actions → Remove Background. That's it." (`maketecheasier.com_iphone_batch_edit_photos_videos_.md`) |
| Files copies saved beside originals; output is PNG with alpha | same | NOT ON PAGE | No fetched page states the output format or where the copies land. The album step is optional: "you don't necessarily have to do this". |
| Clean Up needs iOS 18.1 and iPhone 15 Pro or 16 line | support.apple.com/121429 | CONFIRMED | "iPhone 16 models, iPhone 15 Pro, and iPhone 15 Pro Max… iOS 18.1, iPadOS 18.1, or macOS Sequoia 15.1" (`support.apple.com_121429.md`) |
| Clean Up: not in China mainland; removes objects only | same | CONFIRMED | "Clean Up will not currently work for devices purchased in China mainland"; "can help remove distracting objects in a photo". |
| Clean Up includes iPhone 17 | same | NOT ON PAGE | The page lists only "iPhone 16 models", although its site navigation sells iPhone 17 and 18 Pro, so the page looks stale. |
| Windows 11 Photos "Background" button; Paint background removal | pureinfotech, elevenforum, bleepingcomputer; support.microsoft.com/ | NOT FETCHED; NOT ON PAGE | The Microsoft file is the support homepage ("What do you need help with today?"), with nothing on Photos or Paint. |
| Snipping Tool has no background removal | none | NOT ON PAGE | An absence claim; nothing to check against. |
| Magic Editor: Pixel 8 and later, some Samsung | store.google.com/intl/en_in/ideas/articles/magic-editor | CORRECTED (capability confirmed, device list not) | "AI-powered tools on Google Pixel let you move, remove, and resize people or objects in an image, and even change the background." No Pixel 8 or Samsung text. |
| eBay in-app remover disabled; eraser and brush lost | valueaddedresource.net/ebay-sellers-lose-background-removal-in-app/ | CONFIRMED, but dated | "Published: Aug 19 2023 Updated: Apr 7 2024". "eBay has temporarily disabled the background remover in the app…" (UPDATE 4-7-2024). The 8-27-23 update says desktop also lost "the paintbrush and eraser functions". |
| eBay Background Enhancement, photo-tips (ebayinc, petapixel, ebay.com) | those three | NOT FETCHED | |
| Grabio: iOS 14+, closed source, 5 actions/day, White Background Fill | github.com/adityaarsharma/grabio | CONFIRMED | Already fetched in the cloud session (`raw/17-disc-phone-builtin/github_com_adityaarsharma_grabio.md`); quotes re-found: "An iOS 14+ Apple Shortcut…", "closed-source", "5 actions/day". |

### HEIC, Visual Look Up, Windows HEIC, phone-to-PC transfer

The lane file `17-disc-phone-builtin.md` makes no claim on any of these topics, and no fetched file in the lane covers them. Their only trace is table-of-contents titles in `support.apple.com_guide_iphone_.md`: "Identify objects in your photos and videos" (Visual Look Up), "Transfer files between devices" and "Connect iPhone and your computer with a cable". The `102108` file belongs to lane 07 (camera lock) and has no HEIC text. Windows HEIC is handled script-side: the README row "pillow-heif 1.8.1 has Windows wheels and opens iPhone HEIC" is marked Corrected, not lane 17.

### The phone steps as Apple writes them

- **(a) Lift a subject and copy or save it:** not on any fetched page. Only the article title exists, and the version is unconfirmed. The landing pages render iOS 27, with a selector from iOS 27 down to 12. Next fetch: `https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iphfe4809658/ios`.
- **(b) Files Quick Action to remove a background:** no Apple wording was fetched. The nearest text is Make Tech Easier's, quoted above. The iPhone guide's "Perform quick actions" entry is a Home Screen feature, not this one.
- **(c) HEIC or JPEG capture and "Most Compatible" transfer:** not on any fetched page. Candidate next fetches are the guide's "Transfer files between devices" (`iph339bafff3`) and "Connect iPhone and your computer with a cable" (`iph42d9b3178`) articles. Shortcuts action list: `https://support.apple.com/guide/shortcuts/navigate-the-action-list-apdc33e4f4da/ios`.

### What changes in the docs

- **Handoff, "The simplest route", step 1.** The sentence "(Menu names from third-party guides, not yet checked on your phone; the gesture is the one you already use.)" should stay as a caveat but be narrowed. Suggested: "(The Files route, Share, Save to Files, then in Files select them, the three-dot button, Quick Actions, Remove Background, matches a Make Tech Easier article of 19 March 2026 that was read on 2026-11-07. The press-and-hold 'Copy Subject' wording and the PNG output are on no page we could read. Apple's 'Lift a subject from the photo background' page is still to be read; confirm on the phone.)"
- **Same step: "Each gives a PNG with a transparent background."** No fetched page says so. Suggested: "Each should give a cut-out with a transparent background (format unconfirmed; the script takes transparent PNG)."
- **Decision doc, section 4, last paragraph.** "produce transparent PNGs" is unsourced. Keep "(unverified on device)", cite the Make Tech Easier article for the Files route, and add: "Do not use Clean Up for backgrounds; Apple says it 'can help remove distracting objects'."
- **Decision doc, section 4 "Do not use", eBay in-app remover.** "(snippet-level)" can be replaced by "Value Added Resource, Aug 2023, updated Apr 2024: the remover was disabled in the app and the eraser and brush were removed". Say it is 2023-24 evidence; the current state is unknown.
- **Decision doc, section 8.** The line "Apple and Microsoft support pages for the phone steps" is still unverified. Reword to: "the pages fetched were landing pages without the steps; the Lift-a-subject and Shortcuts action-list articles need a second fetch." Keep "iPhone model and iOS version" as an open question, because Apple's guide now defaults to iOS 27 and the menu names may differ from older third-party guides.

### Surprises the docs do not mention

- **Clean Up has a hard model limit** (iPhone 15 Pro and later, iOS 18.1). Residents of the EU need iOS 18.4 for Apple Intelligence; the lane missed that. Neither doc mentions Clean Up, and neither mentions any model limit for lift-subject. The A12 limit rests only on the unfetched xda page.
- **No Apple page was read at step level.** The earlier "Apple pages fetched" status overstates what was verified.
- **The Make Tech Easier piece is third-party** and came from the site's archive: "published before Make Tech Easier changed ownership in April 2026".
- **The Shortcuts and Cassinelli pages give no sign of a white-fill action or batch behavior.** The "nothing built in fills white" claim is still an absence claim, not a verified fact.

---

## Addendum: four Apple articles now fetched (lane 17)

**Pages read: 4. Walled: 0. NOT FETCHED: 0.** Read-only, no network, no files written. All four are real article pages, not landing shells. Files are in `research/ebay-photo-studio-2026-11-07/raw/fetched-on-pc/`.

### 1. iOS version each article renders for

| File | Renders | Evidence |
|---|---|---|
| `support.apple.com_guide_iphone_lift_a_subject_from_the_photo_background_iphfe480.md` | iOS 27 | Links end `/27/ios/27`; selector "iOS 27 iOS 26 iOS 18 iOS 17 iOS 16" |
| `support.apple.com_guide_shortcuts_navigate_the_action_list_apdc33e4f4da_ios.md` | iOS 27 | Link `/10.0/ios/27`; selector runs iOS 27 to "Shortcuts 2.0" |
| `support.apple.com_guide_iphone_transfer_files_between_devices_iph339bafff3_ios.md` | iOS 27 | `/27/ios/27`; selector iOS 27 to 16 |
| `support.apple.com_guide_iphone_connect_iphone_and_your_computer_with_a_cable_iph.md` | iOS 27 | `/27/ios/27`; selector iOS 27 to 13 |

None of them states wording differences for earlier iOS versions. The iOS 16 wording is not available from these files.

### 2. Lifting a subject, as Apple writes it (iOS 27 page)

Title: "Lift a subject from the photo or video background on iPhone". The body says:
1. "Open a photo in full screen, or pause a video on any frame."
2. "Touch and hold the subject. When an outline appears around the subject, do one of the following:"
   - "Tap Copy or Copy Subject, then paste the subject into an email, text message, or note."
   - "Continue to hold, then with another finger, open a document in another app and drag the subject into the document."
   - "Tap Look Up to learn more about the subject."
   - "Tap Add Sticker, then save the sticker to use in Markup, Messages, and more."
   - "Tap Share, then choose a sharing option, such as AirDrop or Mail."

The intro says: "You can use this feature in Photos, Safari, Quick Look, and more." The page does not mention Save to Files, the Files app, Quick Actions, any file format, or any iPhone model or chip requirement.

### 3. Shortcuts action list

No background-removal action is named. The article is a how-to on browsing the list, not the list itself. It says "tap Search Actions… Enter a term in the search field", and the only categories it gives as examples are "Media or Web". The words "background", "remove image" and "subject" are absent. The label "Remove Image Background" or "Remove Background" must be found by searching in the editor on the phone.

### 4. HEIF/HEIC, JPEG, "Most Compatible", Windows transfer

HEIF, HEIC, JPEG, "Most Compatible" and "Transfer to Mac or PC" are absent from all four files. Windows wording is as follows.
- Cable article: "You can use a cable to directly connect your iPhone to a Mac with OS X 10.9 or later, or to a Windows device with Windows 7 or later." It also says "If an alert appears on your iPhone asking whether to trust this computer, select Trust."
- Transfer article: "Transfer files to your Windows device (Windows 10 or later): Use Apple Devices for Windows." Windows 7 or earlier uses iTunes.
- Transfer article, AirDrop: "To quickly share a photo, file, or other item from your iPhone to a nearby Apple device, you can use AirDrop." That is Apple devices only, so it does not reach the PC.
- Transfer article, iCloud: "OS X 10.10 (or later) or Windows 7 (or later) are required. You must be signed in to the same Apple Account on both your iPhone and your computer".
- Transfer article, cable caveat: "Only files from iPhone apps that support file sharing can be transferred." This is under the Finder / Apple Devices file-transfer list. The page does not describe Windows photo import.

### 5. Updated verdicts

| Claim | Verdict | Evidence |
|---|---|---|
| Lift subject by touch and hold in Photos | CONFIRMED (Apple, iOS 27) | "Touch and hold the subject. When an outline appears around the subject" (lift file) |
| "Copy Subject" wording | CONFIRMED | "Tap Copy or Copy Subject, then paste the subject into an email, text message, or note." The label varies; Apple names both. |
| "until it glows" (handoff wording) | CORRECTED | Apple says "an outline appears", not "glows". |
| "Share, then Save to Files" for a lifted subject | NOT ON PAGE | The page says only "Tap Share, then choose a sharing option, such as AirDrop or Mail." |
| Lifted subject is a transparent PNG | NOT ON PAGE | No format named anywhere in the lift file. |
| Needs A12 or later | NOT ON PAGE | No model limit on the article; the only source remains xda, NOT FETCHED. |
| Shortcuts "Remove Image Background" action | NOT ON PAGE | `...apdc33e4f4da_ios.md` has no action names. The label stays third-party only (macnative NOT FETCHED). |
| Files Quick Action "Remove Background" | Still third-party | Not on any Apple file. Make Tech Easier (19 Mar 2026) remains the only source. |
| HEIC vs JPEG, "Most Compatible" | NOT ON PAGE | Zero hits in all four files. |
| Phone-to-PC route via iCloud or cable | CONFIRMED (Apple) | Quotes in section 4. |

### 6. Replacement wording

**Handoff, "The simplest route", step 1.** Replace the current sentence and its parenthetical with:

"On the iPhone, cut the item out. Apple's iPhone User Guide (iOS 27 page, read 2026-11-07) says: open the photo in full screen, touch and hold the item, and when an outline appears tap Copy or Copy Subject, then paste it; or tap Share and choose a sharing option such as AirDrop or Mail. Apple does not say what file type that produces. For a stack of photos, the Files route (select the photos, Share, Save to Files, then in Files select them, the three-dot button, Quick Actions, Remove Background) is described only by a March 2026 Make Tech Easier article, not by Apple. Confirm on your phone that you end up with a transparent PNG; the script takes transparent PNG."

**Decision doc, section 4, "Phone-only stopgap".** Replace with:

"**Phone-only stopgap (lift steps from Apple, iOS 27 page; Files batch third-party; unverified on device):** Photos lift-subject (touch and hold the subject, then Copy, Add Sticker or Share) is documented by Apple. Apple's page names no file format and no model limit. The Files Quick Action 'Remove Background' is described only by a March 2026 third-party article. Apple's Shortcuts action-list article names no background-removal action, so 'nothing built in fills white' is still an absence claim. Clean Up removes objects, not backgrounds, and needs an iPhone 15 Pro or later. The PC pipeline stays the real route. Skip third-party shortcuts that upload photos to someone's server."

Also edit the section 8 line "Apple and Microsoft support pages for the phone steps". Apple's lift-subject, Shortcuts, transfer and cable articles are now read. Still open: file format of the lifted subject, the Files Quick Action on an Apple page, HEIC vs JPEG capture and "Most Compatible", and the Microsoft pages (low priority).

### Surprises

- The page's title is now "photo or video background", and it lifts from a paused video frame. That is newer than the iOS 16-era third-party guides, so menu wording may differ on Ricky's iOS.
- The Apple pages say nothing about HEIC vs JPEG or a Windows photo-import path. The handoff's step 2 (a folder the PC syncs) rests on the iCloud sentence above (Windows 7 or later, same Apple Account), not on Windows Photos import.
- Do not rely on AirDrop for the PC: the transfer article scopes it to Apple devices.
