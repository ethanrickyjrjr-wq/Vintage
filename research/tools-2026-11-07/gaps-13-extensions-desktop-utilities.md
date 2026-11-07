# Gaps review, lane 13: browser extensions and desktop utilities that save a reseller time

Date 2026-11-07. Author: research subagent (completeness critic for lane 13). Question: What did the lane-13 list miss among Chrome or Edge extensions and small Windows utilities (comps on the fly, listing form fillers, image search, clipboard and text expansion, screenshots and OCR, image resizing, passwords, iPhone photos to a Windows PC), and is anything on the list defunct, acquired or renamed? Legend: V = vendor page read today (2026-11-07); U = unverified (snippet, memory, or the page would not load or render).

Method: the shared WebSearch budget for this turn was already used up when this agent started, so no web searches were run. Every candidate below was reached by its own vendor URL (homepage, pricing page, Chrome Web Store listing, Microsoft Store listing, App Store listing or GitHub repository) and read with the session's headless-Chromium fetcher, with a raw curl of the same vendor page only where the rendered text hid a price or a store link. 66 fetches; all URLs are in section 6. Tools already on the lane-13 list were not re-verified (another agent's job), except where a defunct, acquired or renamed status had to be shown. Candidate names came from the agent's own knowledge of the category, not from roundups, so the "appears in two independent 2026 roundups" test could not be run today; that is stated in section 5.

## 0. Bottom line

- The lane list is solid on Windows built-ins and iPhone transfer. The real gaps are a browser-side text expander (Text Blaze, free tier, 800,000 users), a free private grammar checker that launched after Grammarly's price rise (Harper, open source, Chrome and Edge, updated today), and a one-click multi-engine reverse image search (Search by Image, open source, 300,000 users).
- Passwords: Apple's own iCloud Passwords extension (7,000,000 users) fills Apple Passwords into Chrome and Edge on Windows through iCloud for Windows, which the lane already recommends for photos. If Ricky already keeps passwords on the iPhone, that is zero new vendors. Proton Pass Free (unlimited logins, unlimited devices) and KeePassXC (offline, GPLv3) are the free alternatives the lane lacked; Bitwarden Free still wins on simplicity.
- iPhone photos on Windows: the lane never mentions that Windows needs Microsoft's free HEIF Image Extension to open iPhone HEIC files, and the $0.99 HEVC Video Extensions for iPhone videos. Without them, "full-resolution originals" arrive and will not open. CopyTrans HEIC is the free-for-personal-use alternative; its business tier is quote-only.
- Three tools that still show up in advice for iPhone-to-PC transfer are gone or going: Intel Unison (Intel: stopped June 2025, no longer downloadable), Microsoft Edge Drop (its feature page now redirects to "feature=not-available") and Snapdrop (already flagged by the lane). Send Anywhere still works (free with in-app purchases, "original size to your PC") but its free limits did not render today; LocalSend remains the better free pick.
- Renamed or pivoted: Grammarly's company became Superhuman in October 2025 (the product keeps its name); EtsyHunt is now EHunt (ehunt.ai); Magical, the text-expander extension many roundups list, now markets itself as "AI Agents for Healthcare Operations" and its pricing page is gone, although the extension (200,000 users) was still updated in April 2026. Do not build on Magical.
- Free Windows utilities the lane skipped, all verified today: Greenshot (screenshots, active 2026 builds), NormCap and Text Grab (OCR; Text Grab is $9.99 on the Store but its GitHub build is "100% free"), CopyQ (clipboard), AutoHotkey and Beeftext (text expansion and form filling), Caesium (batch image compression, GPL-3), Squoosh (web, local-only), Windows voice typing (Win+H) and PowerToys Advanced Paste (Win+Shift+V, local OCR, paste as plain text).
- Etsy research extensions beyond eRank and EverBee: Alura's free plan includes its Chrome extension; Sale Samurai ($19.99 monthly, no free plan, 3-day trial) and EHunt (free plan, Basic $7.99 a month billed yearly) bundle extensions too. Lanes 02 and 04 already cover these vendors; eRank Free remains enough for a one-of-one shop.
- Licence gotchas for a business: IrfanView is "FREEWARE (for non-commercial use)" with a US$18 licence for business; XnView: "If you intend to use XnView in a company, you must purchase a license" (29.00 EUR). Both appear in lane 03; neither is free for Hollie as a business.

## 1. Comparison table: tools missing from the lane-13 list

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Text Blaze | Text expander and form filler inside the browser (snippets, forms, if/then rules) | "Free $0 USD Free forever"; Pro "$2.99 USD per month, billed yearly", "$3.49 when billed monthly"; Business "$6.99 USD per user per month, billed yearly" | "Limited snippets", "Limited snippet sharing" | Chrome ext (800,000 users, 4.8 from 1.9K ratings, v3.3.20, updated Oct 13 2026); works in Edge; Windows and macOS apps listed | High if the boilerplate must live inside the Etsy and eBay listing forms; Espanso already covers the desktop for free | V | https://blaze.today/plans/ |
| Harper (Private Grammar & Spell Checker) | Free, open-source grammar checker that runs locally; no account | "universal access to great grammar checking at a low price ($0)" | Everything | Chrome ext (30,000 users, 4.2 from 136 ratings, v3.1.0, updated Nov 7 2026, "Featured"); Edge Add-ons | High; private, fast, nothing sent to a server; launched after the lane's seeds were written (built at Automattic) | V | https://writewithharper.com/ |
| Search by Image | Right-click reverse image search across "more than 30 search engines" (Google, Bing, Yandex, Baidu, TinEye) | Free, open source (Patreon support) | Everything | Chrome ext (300,000 users, 3.6 from 545 ratings, v8.5.4, updated Jun 16 2026, "Featured"); Edge Add-ons | Medium to high; one menu for Lens, Bing and TinEye when identifying a maker's mark | V | https://chromewebstore.google.com/detail/search-by-image/cnojnbdhbhnkbcieeekonklommdnndci |
| iCloud Passwords (Apple) | Fills passwords from iCloud Keychain into Chrome; saves new ones back to the iPhone | Free | Everything (needs iCloud for Windows) | Chrome ext (7,000,000 users, 2.6 from 2.7K ratings, v3.4.0, updated Sep 29 2026); "Windows versions supported by the iCloud for Windows app" | High if Ricky already uses the iPhone Passwords app; otherwise Bitwarden Free | V | https://chromewebstore.google.com/detail/icloud-passwords/pejdijmoenmkgeppbflobdenhhabjlaj |
| Proton Pass | Password manager, open source, Swiss | Pass Plus and Pass Family amounts did not render in the page text today (U on paid price) | "Proton Free: Unlimited logins, notes and credit cards", "Unlimited devices", "Browser, mobile, and desktop apps", "10 hide-my-email aliases" | Android, iOS, Windows, macOS, Linux, web, Chrome, Edge, Safari, Firefox extensions | Medium; same job as Bitwarden Free | V (free tier), U (paid price) | https://proton.me/pass/pricing |
| KeePassXC | Offline password database, no cloud, no account | Free | Everything | Windows, macOS, Linux; GPLv3; 2.8.0 is the current stable series | Low to medium; no built-in sync to an iPhone | V | https://keepassxc.org/ |
| HEIF Image Extension (Microsoft) | Lets Windows Photos and File Explorer open iPhone HEIC photos | "displayPrice":"Free" (store page structured data) | Everything | Windows 10 and 11, Microsoft Store | High; without it HEIC originals from the iPhone will not open on the PC | V (structured data; visible text did not render) | https://apps.microsoft.com/detail/9pmmsr1cgpwg?hl=en-us&gl=US |
| HEVC Video Extensions (Microsoft) | Plays iPhone HEVC (H.265) video on Windows | "displayPrice":"$0.99" (store page structured data) | None | Windows 10 and 11, Microsoft Store | Medium; needed only for walkthrough videos shot in High Efficiency | V (structured data) | https://apps.microsoft.com/detail/9nmzlz57r3t7?hl=en-us&gl=US |
| CopyTrans HEIC | HEIC viewer, thumbnails and right-click HEIC to JPG converter for Windows | "Personal usage Free Download"; business "Get a quote" | Personal use free | Windows (Explorer plug-in) | Medium; Microsoft's own extension is simpler; a business licence is quote-only | V | https://www.copytrans.net/copytransheic/ |
| CopyTrans Photo | Drag-and-drop iPhone to PC photo transfer "in original quality", HEIC kept or converted | "$ 19.99" (one app) or "7 Pack ... $ 29.99"; "2 years of regular updates" | "Try for free" (trial) | Windows 11, 10, 8.1, 7 | Low to medium; cable plus Windows Photos does the same for free | V | https://www.copytrans.net/store/ |
| iMazing | iPhone manager: photo export, backups, file transfer | "Personal Subscription ... 5 devices, $49.99 per year"; Family "$89.99 20 devices, per year" | Download is free; what the unlicensed mode allows was not stated on the pages read | Windows and Mac | Low; pricier option, listed as such; nothing here that iCloud for Windows or a cable does not do for photos | V | https://imazing.com/store |
| Send Anywhere | Cross-platform file transfer by 6-digit key or link | "Free · In-App Purchases"; Plus adds "Max 50GB file upload size" and no-expiry links | Free with limits (per-transfer limit did not render today, U) | iOS 14.1 or later, Windows app, web | Medium; "Send your photos and videos in original size to your PC"; LocalSend is open source with no server, so prefer it | V (price, platform), U (free limit) | https://apps.apple.com/us/app/send-anywhere-file-transfer/id596642855 |
| Greenshot | Screenshot tool with annotate, obfuscate and export | "free and open source!" | Everything | Windows; "Greenshot 1.3.328 Latest", 1.4 continuous builds, dependency fixes citing 2026 CVEs | Medium; lighter than ShareX, more than Snipping Tool | V | https://getgreenshot.org/ |
| Flameshot | Cross-platform screenshot with built-in annotation | "Free & open source screenshot software" | Everything | Windows, macOS, Linux | Low to medium; duplicates Greenshot and ShareX | V | https://flameshot.org/ |
| NormCap | "OCR-powered screenshot tool to capture text" | Free | Everything | Windows installer or portable (x86_64, ~120 MB), v0.6.0; GPLv3 | Medium; PowerToys Text Extractor already does this | V | https://dynobo.github.io/normcap/ |
| Text Grab | Windows OCR: grab text from any screen region, "Grab Frame", background hotkeys | "Get on Microsoft Store — $9.99"; "the GitHub build is 100% free" | GitHub build free (MIT) | Windows 10 or later; Copilot+ PC adds NPU recognition | Medium; same niche as PowerToys Text Extractor, more modes | V | https://textgrab.net/ |
| CopyQ | Clipboard manager with history, images, tabs and scripting | Free (donations) | Everything | Windows, Linux, macOS 10.15+ | Medium; alternative to Ditto if Win+V's limits bite | V | https://hluk.github.io/CopyQ/ |
| AutoHotkey | "free, open-source scripting language for Windows ... form fillers, auto-clicking, macros" | Free | Everything | Windows; GNU GPLv2 | Medium; the power route for filling repeated listing fields; learning curve | V | https://www.autohotkey.com/ |
| Beeftext | "An open-source text substitution tool for Windows" with a GUI | Free | Everything | Windows; MIT; latest release v16.0 (47 releases) | Medium; point-and-click alternative to Espanso's YAML | V | https://beeftext.org/ |
| Caesium Image Compressor | Batch compress and resize JPG, PNG, WebP, TIFF | "Caesium is a free software" | Everything | Windows 10 (build 1809) or later, installer or portable; GPL-3.0 | Medium; shrinks a whole shoot under marketplace size limits in one pass | V | https://saerasoft.com/caesium/ |
| Squoosh | In-browser image compressor; "does not send your image to a server" | Free | Everything | Web (any browser); Apache-2.0 | Medium; one image at a time; also in lane 03 | V | https://github.com/GoogleChromeLabs/squoosh |
| Windows voice typing (Win+H) | Dictate text into any text box | Free (built in) | Everything | Windows 11 and 10; "you'll need to be connected to the internet" | Medium to high; dictate a condition note or description, then fix with Harper | V | https://support.microsoft.com/en-us/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc |
| PowerToys Advanced Paste (Win+Shift+V) | "paste as plain text, Markdown, JSON ... extract text from images by using local OCR" | Free (part of PowerToys) | Everything; "Paste with AI ... off by default" | Windows 10 and 11 | High; already installed with the PowerToys the lane recommends; the lane did not name it | V | https://learn.microsoft.com/en-us/windows/powertoys/advanced-paste |
| Alura Chrome Extension | Etsy keyword and listing data on Etsy pages | Basic "$95.88 billed yearly, save 33%"; Growth "$179.99 billed yearly, save 50%"; Professional "$359.88 billed yearly, save 57%"; monthly amounts did not render | "Free ... $0 / month ... 5 daily keyword & product searches ... Alura Chrome Extension" | Chrome ext plus web app | Medium; lanes 02 and 04 review Alura; the free extension is the lane-13 gap | V | https://www.alura.io/pricing |
| Sale Samurai | Etsy search volume and competition, "Free Chrome extension included" | "$19.99" monthly; "$16.65/mo Billed as $199.90 yearly" | None; "3-day free trial" | Chrome ext plus web app | Low to medium; paid only; lanes 02 and 04 | V | https://salesamurai.io/pricing/ |
| EHunt (formerly EtsyHunt) | Etsy product research with an "Etsy Extension" | Free "Annual: $0.00/month"; Basic "Annual: $7.99/month" ("$95.88 billed"); Pro "$15.99/month" ("$191.88 billed"); Elite "$29.99/month" ("$359.88 billed") | Free: "Product search 5 times/day", "Listing comparison 1 trial"; Basic "Etsy Extension: Most features" | Chrome ext plus web app | Low to medium; eRank Free already covers tags; lane 02 listed it under the old name | V | https://ehunt.ai/pricing |

## 2. Notes per tool

- Text Blaze. The old pricing URL (/pricing/) returns 404; plans live at /plans/. The listing page describes itself as a "free text expander" and the plans page says the free plan has "Limited snippets" without a number in the page text. Pro adds images and tables in snippets, if/then rules and Data Blaze. Snippets sync through the Text Blaze account (cloud), unlike Espanso, which is local. For a one-person shop the free tier is likely enough; the test is whether the snippet count limit bites.
- Harper. Runs entirely in the browser: "Every check happens locally. No cloud round-trips, no telemetry, no LLM in the loop." The Chrome listing is marked Featured and was updated today (v3.1.0, Nov 7 2026). The author works at Automattic. It checks English grammar and spelling only; it does not rewrite or paraphrase. Edge Add-ons listing also exists (link found on the vendor site).
- Search by Image. Open source (Armin Sebastian). Right-click any image, pick an engine or search all. Covers Google, Bing, Yandex, Baidu and TinEye in one menu. Rating is 3.6, which is lower than its user count suggests; the listing text gives no complaint detail. For identifying a maker's mark it saves the copy-paste between engines.
- iCloud Passwords. Requires the iCloud for Windows app with iCloud Passwords enabled; the extension cannot work alone. 2.6 rating from 2.7K ratings is low; the listing text does not show the complaints. Also generates verification codes from a QR code. If Ricky's passwords already live in Apple Passwords, this avoids a second vault.
- Proton Pass. Free tier is complete for one person (unlimited logins and devices, all apps). Paid tier prices are rendered client-side and did not appear in the text today, so they are U. Open source, Swiss jurisdiction. No reason to prefer it over Bitwarden Free unless Ricky already uses Proton Mail.
- KeePassXC. Offline database file; syncing to an iPhone needs a third-party iOS KeePass app plus a cloud folder. GPLv3. 2.8.0 is the first version with native ARM64 Windows builds. Fine for a PC-only vault, awkward with an iPhone.
- HEIF Image Extension and HEVC Video Extensions. The Microsoft Store pages would not render as text through the fetcher (curl fallback returned only the title), but the pages' structured data gives "displayPrice":"Free" for HEIF and "displayPrice":"$0.99" with "priceCurrency":"USD" for HEVC. The alternative is to set the iPhone camera to Most Compatible (JPEG and H.264), which avoids both. If Ricky keeps High Efficiency for smaller files, install the free HEIF extension on day one.
- CopyTrans HEIC. "Personal usage Free Download"; the business tier (Citrix, MSI, silent deployment) is "Get a quote". The page claims it also helps IrfanView and FastStone read HEIC. Flag: a resale business is arguably not "personal usage"; the page does not define the term, so stick with Microsoft's own extension.
- CopyTrans Photo. $19.99 single app, $29.99 for the 7-app bundle, "2 years of regular updates". It keeps HEIC or converts on transfer and preserves date and location. The free Windows path (cable plus the Photos app import, or iCloud for Windows) does the same, so this is only for someone who wants a two-pane drag-and-drop view.
- iMazing. Subscription is per device slot, $49.99 a year for 5 devices. The /pricing URL is a 404; prices are on /store. The download page says downloads are free but does not state what the trial allows for photo export, so the free tier is unknown. Pricier option, listed as such.
- Send Anywhere. The App Store page says "Free · In-App Purchases", "No login or registration required" and "Send your photos and videos in original size to your PC". A developer reply mentions Plus features ("Max 50GB file upload size", no-expiry links, password links) with a one-month free trial. The homepage, /plus page and help center rendered without text, so the free per-transfer limit and key expiry are U. A recent review complains that received files on iOS can land inside the app's own Files folder; another reports freezes. Prefer LocalSend.
- Greenshot. Still maintained: the releases page shows 1.3.328 as Latest, 1.4 continuous pre-releases, and a dependency update citing CVE-2026-40021. Free for Windows (the Mac version is a paid App Store item, not relevant here). Simpler than ShareX; no scrolling capture or OCR.
- Flameshot. Free and open source, Windows builds offered. Nothing Greenshot or ShareX lacks; included for completeness.
- NormCap. GPLv3, offline OCR, ~120 MB installer. Overlaps fully with PowerToys Text Extractor; useful only if PowerToys is not installed.
- Text Grab. Two builds of the "Same app either way": the Store build ($9.99) adds Windows AI/NPU recognition, translation and local AI tools and funds development; the GitHub build is MIT and free. All OCR runs on the device. Windows 10 or later. The site also lists a free Chrome and Edge companion extension.
- CopyQ. Free clipboard manager with image support, tabs and scripting; Windows, Linux and macOS. Ditto is already on the list; CopyQ is the choice if Ricky wants cross-platform or scripting.
- AutoHotkey. GPLv2. Scripts can type condition templates, tab through listing fields and fill forms. Steeper than Espanso or Beeftext; worth it only if a repetitive form workflow turns up.
- Beeftext. MIT, Windows-only, GUI for combos (keyword to snippet). The README explains it exists because TextExpander moved to subscriptions in 2016. Latest release v16.0; its date is not shown in the page text (U on freshness). A friendlier Espanso for someone who does not want YAML files.
- Caesium. GPL-3.0, Windows 10 1809 or later, installer and portable. Batch compress and resize with quality control; keeps EXIF optional. PowerToys Image Resizer resizes but does not control JPEG quality; Caesium does both.
- Squoosh. Google Chrome Labs, Apache-2.0, processes locally in the browser. One image at a time, so it suits a hero image, not a shoot. Lane 03 also lists it.
- Windows voice typing. Win+H in any text box; needs the internet and a microphone; language packs installable. Free way to draft descriptions by talking, then clean up with Harper or LanguageTool. Lane 15 mentions it; lane 13 did not.
- PowerToys Advanced Paste. Already part of the PowerToys install the lane recommends. Win+Shift+V pastes as plain text (kills marketplace formatting junk), Markdown or JSON, extracts text from a clipboard image with local OCR, and transcodes media. "Paste with AI" is optional and off by default, and can use a local provider (Ollama, Foundry Local, Phi Silica) instead of an online one.
- Alura, Sale Samurai, EHunt. All three bundle a Chrome extension with a web app. Alura's is included in the free plan; Sale Samurai has no free plan; EHunt's free plan allows 5 product searches a day and the extension's features open at Basic ($7.99 a month billed yearly; monthly billing amounts did not render). Lanes 02 and 04 review the vendors; lane 13 only needed to note the extensions exist. EHunt also sells an "API service" and says "Request a refund within 24 hours of your first purchase". None of these is needed beside eRank Free for a one-of-one shop.
- Licence gotchas (lane 03 tools, verified today because they came up as image utilities): IrfanView "is provided as freeware, but only for private, non-commercial use (that means at home)"; a business licence is "US$ 18.00 or EUR 15,00" per computer, perpetual. XnView: "If you intend to use XnView in a company, you must purchase a license", 1 licence "29.00 €". Caesium, Squoosh and PowerToys have no such clause.

## 3. Defunct, acquired, renamed or moved (with evidence)

- Grammarly (on the lane list). Company renamed: "In October, our company became Superhuman. The new name unites all three products under one brand and one mission. Grammarly remains at the core" (grammarly.com/about, V). The product keeps the Grammarly name; the lane only saw the "2026 © Superhuman Platform" footer. No price impact found today.
- EtsyHunt (a lane-02 lead). Renamed EHunt: etsyhunt.com/pricing redirects to ehunt.ai/pricing, headline "Meet the new EHunt AI! All-in-one AI tools for Etsy product research" (V).
- Magical (text-expander extension common in 2024 roundups; not on the lane list). The company site now reads "Magical | AI Agents for Healthcare Operations" and getmagical.com/pricing redirects to that homepage with no consumer plan (V). The Chrome listing "Magical: Text Expander & Autofill" still exists (200,000 users, 3.1 from 3.5K ratings, v3.119.1, updated Apr 4 2026) and still says "Join 950,000 users" (V). Treat as a product no longer sold to individuals; do not adopt.
- Intel Unison (a 2023 to 2024 iPhone-to-PC recommendation; not on the list). Intel: "As of June 2025, Intel has stopped manufacturing Intel Unison products" and "The Intel Unison Product and drivers are no longer available for download" (intel.com article 000102120, V). The Microsoft Store listing (9pp9gzm2gn26) still answers with a title only.
- Microsoft Edge Drop (Edge's phone-to-PC file and note sharing; not on the list). The feature page microsoft.com/en-us/edge/features/drop now redirects to explore.microsoft.com/en-us/edge/features?feature=not-available (V on the redirect). The Edge Stable release-notes page text read today did not mention Drop, so the formal deprecation note is U. Do not recommend it for iPhone photos.
- Snapdrop (on the list). The lane already found snapdrop.net uploads to LimeWire; not re-checked.
- Photoroom Chrome extension (on the list, U). The listing ID lokegfgcnpdiambfeddkhgjhpbafbgnh returned only the store's empty shell again today (313 characters). Treat as removed or re-published under another ID until proven otherwise (U).
- Microsoft Phone Link for iPhone (on the list, U). The requirements page says Phone Link connects "your Android or iPhone" and lets you "view recent photos from your mobile device", but the only requirements section that rendered lists photos for Android ("view recent photos from your Android device"); the iOS tab content did not render and the Store listing's description could not be extracted. iPhone photo sync stays U; the lane's "low for photos" stands.
- Moved pages, not defunct: Text Blaze pricing is at blaze.today/plans/ (the /pricing/ URL is a 404); iMazing prices are at imazing.com/store (/pricing is a 404).

## 4. Recommendation for Hollie

- Install today, all free: HEIF Image Extension from the Microsoft Store (or set the iPhone camera to Most Compatible); Harper in Chrome or Edge (keep LanguageTool if Ricky prefers it; do not run both); Search by Image for one-click Lens, Bing and TinEye on a maker's mark; PowerToys Advanced Paste is already in the PowerToys install, so turn on Win+Shift+V and use paste-as-plain-text for every listing description.
- Passwords: if Ricky already uses the iPhone Passwords app, add the iCloud Passwords extension on the PC (it rides on the iCloud for Windows install the lane already recommends for photos). Otherwise Bitwarden Free stays the pick. Skip Proton Pass and KeePassXC unless Ricky asks for them.
- Text expansion: Espanso stays the desktop pick. Add Text Blaze Free only if snippets must work inside the Etsy or eBay listing form with fill-in fields; pay for Pro ($2.99 a month billed yearly) only after the free snippet limit is hit. Beeftext is the GUI fallback if Espanso's YAML is a wall. AutoHotkey only for a specific repetitive form that nothing else handles.
- Photos: cable plus Windows Photos, or iCloud for Windows, remain the paths. Add Caesium for batch compression before upload. Buy the $0.99 HEVC extension only when an iPhone video will not play. Skip iMazing ($49.99 a year), CopyTrans Photo ($19.99), Send Anywhere (free limits unverified, server in the middle), Intel Unison (discontinued) and Edge Drop (withdrawn).
- Screenshots and OCR: Snipping Tool plus PowerToys covers it; Greenshot if ShareX feels heavy; Text Grab's GitHub build or NormCap only if PowerToys Text Extractor misses text on a label.
- Dictation: try Win+H voice typing for first drafts of descriptions.
- Skip for now: Magical (pivoted to healthcare), Sale Samurai (paid only), EHunt and Alura paid tiers (eRank Free does the Etsy tag job), IrfanView and XnView unless a business licence is bought, PhraseExpress (pricing page would not render; licence terms unverified).

## 5. Gaps and pages that would not load

- No web searches were possible (the turn's shared WebSearch budget was exhausted before this agent ran), so the "appears in two independent 2026 roundups or category pages" test was not run. Candidates came from category knowledge and were each verified on the vendor's own page. A follow-up with search budget should sweep the Chrome Web Store "Workflow & Planning" and "Tools" categories and Product Hunt for 2026 launches in this lane.
- blaze.today/pricing and /pricing/ return 404 (plans are at /plans/). imazing.com/pricing 404 (prices at /store).
- apps.microsoft.com listings (HEIF, HEVC, Intel Unison, Phone Link) render as a JavaScript shell; prices came from the pages' structured data via a raw fetch, and the Phone Link description could not be extracted.
- proton.me/pass/pricing: paid plan amounts did not appear in the page text (client-rendered).
- send-anywhere.com, send-anywhere.com/plus and the help center rendered without body text; free limits U.
- phraseexpress.com/pricing/ and /buy/ fell back to curl with no price text; PhraseExpress is therefore not in the table.
- apps.apple.com Link to Windows listing: FETCH FAILED.
- grammarly.com/blog/company/superhuman-launch/ 404; the About page carried the rename statement instead.
- Chrome Web Store ID lokegfgcnpdiambfeddkhgjhpbafbgnh (Photoroom): store shell only.
- Alura monthly amounts and EHunt monthly-billing amounts did not render; yearly totals are quoted instead.
- Beeftext's latest release date is not in the page text.
- Not attempted today: Edge Visual Search documentation, WorthPoint (covered in lanes 04, 05 and 06), Bing visual search, OneTab and other tab managers, Google Drive for desktop as a photo path.

## 6. Sources (every URL fetched today)

https://blaze.today/pricing/
https://blaze.today/pricing
https://blaze.today/
https://blaze.today/plans/
https://blaze.today/business/
https://chromewebstore.google.com/detail/text-blaze-templates-and/idgadaccgipmpannjkmfddolnnhmeklj
https://www.getmagical.com/pricing
https://www.getmagical.com/
https://chromewebstore.google.com/detail/magical-text-expander-aut/iibninhmiggehlcdolcilmhacighjamp
https://writewithharper.com/
https://chromewebstore.google.com/detail/private-grammar-spell-che/lodbfhdipoipcjmlebjbgmmgekckhpfb
https://proton.me/pass/pricing
https://keepassxc.org/
https://chromewebstore.google.com/detail/icloud-passwords/pejdijmoenmkgeppbflobdenhhabjlaj
https://www.microsoft.com/en-us/edge/features/drop
https://explore.microsoft.com/en-us/edge/features?feature=not-available&form=MT0160
https://support.microsoft.com/en-us/windows/apps/phonelink/phone-link-requirements-and-setup
https://apps.microsoft.com/detail/9pmmsr1cgpwg?hl=en-us&gl=US
https://apps.microsoft.com/detail/9nmzlz57r3t7?hl=en-us&gl=US
https://apps.microsoft.com/detail/9pp9gzm2gn26?hl=en-us&gl=US
https://apps.microsoft.com/detail/9nmpj99vjbwv?hl=en-us&gl=US
https://www.intel.com/content/www/us/en/support/products/230575/software/intel-unison-app.html
https://www.intel.com/content/www/us/en/products/docs/unison/overview.html
https://www.intel.com/content/www/us/en/support/articles/000102120/software.html
https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel
https://imazing.com/pricing
https://imazing.com/store
https://imazing.com/download
https://send-anywhere.com/
https://send-anywhere.com/plus
https://apps.apple.com/us/app/send-anywhere-file-transfer/id596642855
https://help.send-anywhere.com/hc/en-us
https://support.send-anywhere.com/hc/en-us
https://www.copytrans.net/copytransheic/
https://www.copytrans.net/copytransphoto/
https://www.copytrans.net/store/
https://getgreenshot.org/
https://github.com/greenshot/greenshot/releases
https://flameshot.org/
https://dynobo.github.io/normcap/
https://github.com/TheJoeFin/Text-Grab
https://textgrab.net/
https://hluk.github.io/CopyQ/
https://chromewebstore.google.com/detail/search-by-image/cnojnbdhbhnkbcieeekonklommdnndci
https://raw.githubusercontent.com/dessant/search-by-image/master/README.md
https://chromewebstore.google.com/detail/lokegfgcnpdiambfeddkhgjhpbafbgnh
https://flipwise.app/pricing
https://www.alura.io/pricing
https://salesamurai.io/pricing/
https://etsyhunt.com/pricing
https://ehunt.ai/pricing
https://www.autohotkey.com/
https://beeftext.org/
https://github.com/xmichelo/Beeftext
https://github.com/xmichelo/Beeftext/releases
https://www.phraseexpress.com/pricing/
https://www.phraseexpress.com/buy/
https://squoosh.app/
https://github.com/GoogleChromeLabs/squoosh
https://saerasoft.com/caesium/
https://github.com/Lymphatus/caesium-image-compressor
https://www.irfanview.com/main_what_is_engl.htm
https://www.xnview.com/en/xnviewmp/
https://www.xnview.com/en/xnview/
https://www.grammarly.com/blog/company/superhuman-launch/
https://superhuman.com/
https://www.grammarly.com/
https://www.grammarly.com/about
https://support.microsoft.com/en-us/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc-fec94565-c4bd-329d-e59a-af033fa5689f
https://support.microsoft.com/en-us/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc
https://learn.microsoft.com/en-us/windows/powertoys/advanced-paste
https://apps.apple.com/us/app/link-to-windows/id1623727783
