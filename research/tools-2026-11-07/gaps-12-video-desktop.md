# Gaps review, lane 12: desktop video, caption, repurposing and design tools (Windows)

Date 2026-11-07. Author: research subagent (completeness critic for lane 12-video-desktop).
Question: What did the lane-12 list miss among Windows desktop and web tools for editing, captioning, repurposing and designing short videos and graphics for a one-person vintage shop, and is anything on the list defunct, acquired or renamed?
Legend: V = vendor page read today (2026-11-07) with the session's headless-Chromium fetcher; U = unverified (page would not load or render, or the fact comes from memory or a snippet).

Method. The shared WebSearch budget for this turn was already used up when this agent started, so no web searches ran and the "appears in two independent 2026 roundups" test could not be run; candidate names came from this agent's knowledge of the category. Every candidate was reached by its own vendor URL (pricing page, homepage, help centre, GitHub repository or Microsoft support page). 75 fetch attempts, about 60 pages loaded; every URL is in section 6. Tools already on the lane-12 list were not re-verified (another agent's job), except where a defunct, acquired or renamed status had to be shown. Prices are quoted as the vendor writes them. Where a page has a monthly/yearly toggle and the text did not say which was showing, that is noted.

## 0. Bottom line

- The biggest miss is Affinity by Canva. Since Canva made it free, it is a full professional vector, photo and layout app on Windows at "$0, free" (V). It replaces the Photopea/GIMP pairing for framed product panels, cutout touch-ups and shop graphics, and exports straight to Canva, which Hollie already uses.
- Two small free utilities the lane lacked will save more time than any editor: LosslessCut (trim iPhone clips in seconds without re-encoding, GPL, Windows) and HandBrake (shrink and convert to MP4 for the Etsy and TikTok size limits, free, Windows 10 and later). Both V.
- Music licensing gap: the lane did not list Meta Sound Collection, which is "Free to use in any videos you create and share on Facebook and Instagram" (V). For other platforms, Incompetech is Creative Commons BY 4.0 (credit the artist or buy a licence) and Coverr's own library is "free for commercial and personal projects" (both V). Bensound free tracks need attribution; its All Access plan is "$9 /month (Billed $119 annually)" (V).
- Captions: Buzz and Vibe are free, open-source Whisper desktop apps for Windows (MIT), simpler than Subtitle Edit for a plain transcript or SRT. Whisper itself is MIT, so commercial use is fine. All V.
- Windows 11 already records the screen: Snipping Tool, "Windows logo key + Shift + R" (V). No install needed for a quick how-to clip. NVIDIA Broadcast (free download, Windows 10/11) removes webcam background and room noise, but only on an RTX 2060 or better GPU (V).
- The clip-and-caption category keeps growing (Vizard, quso.ai, Klap, Munch Studio, Gling, Pictory, InVideo, Lumen5, Repurpose.io, TimeBolt), and every free tier either watermarks, caps at 720p or expires. None fits 15 to 60 second one-of-one product clips. Nothing here beats the lane's existing verdict: skip, trial Veed only if captions become a daily chore.
- Renamed or gone since the roundups were written: Unscreen now redirects to Canva's Video Background Remover "on Canva Pro"; Munch is Munch Studio; vidyo.ai is quso.ai; Screencast-O-Matic is ScreenPal; CapCut Commerce Pro is Pippit AI; Captions' parent company now trades as Mirage (Captions continues as a product); Vegas Pro is sold by Boris FX. HitFilm's site did not load (U). All others V.
- Nothing in this gaps list needs money today. The paid items worth remembering, only once earned: Kittl Pro ($19 monthly or $14 /mo billed annually) for vintage-style typography, ScreenPal Deluxe ($4.00/mo paid annually) if a hosted how-to library is wanted, Lightworks Create ($20.00 monthly) only if 4K export is ever needed.

## 1. Missing tools: comparison table (top 12 by fit)

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| Affinity by Canva | Professional vector, photo editing and page layout in one app; opens PSD, exports to Canva | "$0, free"; "Affinity is free for individuals (seriously)." | Everything, free; needs a Canva account ("sign in with your Canva account (or create one for free)") | Windows, Mac, iPad ("Available on Mac, Windows & iPad") | High: framed product panels, cutout touch-ups, shop graphics, no subscription | V | https://www.affinity.studio/get-affinity ; https://www.affinity.studio/ |
| LosslessCut | Cuts, trims and joins video without re-encoding, so iPhone clips export in seconds | "will always remain free and open source" | All of it; GPL-2.0 | Windows (7zip build; "Windows 7, 8 and 8.1 is no longer supported after v3.50.0"), Mac, Linux | High: trim 40 clips a week in minutes | V | https://github.com/mifi/lossless-cut |
| HandBrake 1.11.2 | Converts and compresses video to MP4/MKV with presets | "It's free!"; "Free and Open Source" | All of it | "For Windows 10 and later"; Mac, Linux | High: shrink to the TikTok 500 MB and Etsy upload limits | V | https://handbrake.fr/ |
| Meta Sound Collection | Free music and sound effects library from Meta | "Free to use in any videos you create and share on Facebook and Instagram." | All tracks, for Facebook and Instagram use | Web (needs a Facebook login) | High for Reels music; not cleared for TikTok, Etsy or YouTube | V | https://www.facebook.com/sound/collection/ |
| Incompetech (Kevin MacLeod) | Royalty-free music library under Creative Commons | "Licensed under Creative Commons: By Attribution 4.0"; "Be sure to credit me or purchase a license." | All tracks with credit; Standard License is paid (price not read) | Web | Medium: works on every platform if the credit line is added | V | https://incompetech.com/music/royalty-free/faq.html |
| Buzz | Offline transcription and subtitles on the PC, powered by Whisper | free (MIT licence) | All of it; "Buzz transcribes and translates audio offline on your personal computer." | Windows ("Get the installation files from the SourceForge. App is not signed"), Mac (Apple silicon only), Linux | Medium: simplest free SRT maker if Subtitle Edit feels heavy | V | https://github.com/chidiwilliams/buzz |
| Windows 11 Snipping Tool (screen recording) | Built-in screenshot and screen video capture | free, part of Windows 11 | All of it | Windows 11 ("Press Windows logo key + Shift + R to open the snipping tool overlay to capture a video clip.") | Medium: zero-install how-to clips | V | https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots |
| NVIDIA Broadcast | AI webcam background removal, noise and echo removal for any app | no price shown on page (free download); "Download the NVIDIA Broadcast App" | All features, if the GPU qualifies | "Windows 10 64-bit, Windows 11 64-bit, Windows 11 on Arm"; needs "NVIDIA GeForce RTX 2060, Quadro RTX 3000, TITAN RTX, RTX Spark, or higher" | Medium, only if Ricky's PC has an RTX card; otherwise skip | V (platform, GPU rule); U (price not stated) | https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-app/ |
| ScreenPal (formerly Screencast-O-Matic) | Screen and webcam recorder with editor, hosting and AI captions | Deluxe "$4.00/mo paid annually"; Max "$10.00/mo paid annually"; Business "$8/user/mo" | "$0/mo free forever": "15 minute recording limit", "10 hosted videos", "Blur webcam background"; watermark status on free not readable | Web, Windows and Mac desktop features ("Video Storyboards & Scripts (Windows & Mac)") | Medium: cheap hosted how-to videos; OBS plus Clipchamp cover the same for free | V | https://screenpal.com/plans ; https://screenpal.com/pricing |
| Streamlabs Desktop | Live streaming and recording built on OBS, with overlays and multistream | Ultra "$27/mo" monthly or "$189/year" | "Free, always": free overlays, 2 destinations; video editor "1 Hour Upload + Watermark" | "Windows 10+", Mac; GPL-3.0 ("only supports OSX 10.14+ and 64-bit Windows") | Medium: easier live-selling setup than bare OBS; same engine | V | https://streamlabs.com/ ; https://github.com/streamlabs/desktop |
| Kittl | Browser design tool for typography, logos and vintage-style graphics | Pro "$19" monthly or "$14 /mo, billed annually"; Expert "$49"/"$39"; Max "$85"/"$65" | "$0 /mo, free forever" with "Full commercial license" | Web | Medium: retro lettering for covers and the neon-sign look; Canva Free covers the rest | V | https://www.kittl.com/pricing |
| Coverr | Free stock video, images and music; premium vertical footage on a plan | Basic "$4.20 / month"; Plus "$6.60 / month"; Pro "$10.80 / month" (shown with "Pay yearly" toggle) | "Everything Coverr publishes is free for commercial and personal projects."; premium items incl. "vertical (9:16) footage" need "Plus plan or higher" | Web | Medium: second b-roll source beside Pexels; read each item's label | V | https://coverr.co/license ; https://coverr.co/pricing |

## 1b. Other candidates checked today (lower fit or duplicates of listed tools)

| Tool | What it does | Price (verbatim quote) | Free tier | Platform | Fit for Hollie | V/U | Source URL |
|---|---|---|---|---|---|---|---|
| OpenShot | Open-source timeline editor | free (GPL v3) | "Edit without subscriptions, watermarks, or project limits." | Windows, Mac, Linux | Medium alternative; DaVinci, Shotcut and Kdenlive already listed | V | https://www.openshot.org/ |
| Lightworks | Professional editor with a free tier | Create "$20.00 User / Pay monthly"; Pro "$35.00 User / Pay monthly"; perpetual option | Free "Free forever": "Full HD 1080p Export", "including portrait video for social" | "compatible with Windows, MacOS, and Linux" | Medium alternative; free 1080p vertical export | V | https://lwks.com/pricing ; https://lwks.com/ |
| VSDC Free Video Editor 11.2 | Windows-only free editor with screen recorder and capture | free; Pro price not found (/vsdc-pro 404) | Free version, title says "No watermarks" | "freely available for download to Windows OS-based PCs and laptops" | Medium-low alternative | V (free), U (Pro price) | https://www.videosoftdev.com/ |
| CyberLink PowerDirector | Windows editor with AI tools and a Getty/Meta stock library | subscription and "PowerDirector 2027 one-time purchase" exist; prices did not render | "PowerDirector Essential with no time limits" (free users have limited stock access) | "Windows 11 / 10 and macOS" | Low-medium; paid tiers unpriced today | V (free tier), U (prices) | https://www.cyberlink.com/products/powerdirector-video-editing-software/overview_en_US.html |
| Vegas Pro (Boris FX) | Pro Windows editor | prices did not render as text; "Try for Free" trial | Trial only | Windows | Low; over the need | U (price) | https://www.vegascreativesoftware.com/vegas-pro/plans-pricing/ |
| Camtasia (TechSmith) | Screen recorder and editor suite | Starter "$39.00 per year billed yearly" (Snagit plus "Camtasia Editor (watermarked)"); Essentials "$179.88 per year billed yearly"; Create "$249.00 per year" | Free editor: "exported videos will include a watermark until you upgrade" | "Microsoft Windows 10 (64-bit) 20H2 version or later", macOS | Low; Clipchamp and OBS do this free | V | https://www.techsmith.com/store/camtasia ; https://www.techsmith.com/camtasia/ |
| Vibe | Offline Whisper transcription app | free (MIT) | "Free, open source, and yours to run." | "Optimized for GPU (macOS, Windows, Linux)" | Medium; same job as Buzz | V | https://thewh1teagle.github.io/vibe/ ; https://github.com/thewh1teagle/vibe |
| OpenAI Whisper | Speech-to-text model behind Buzz, Vibe and Subtitle Edit | free | "Whisper's code and model weights are released under the MIT License." | Python, any OS | Reference only: confirms commercial use is allowed | V | https://github.com/openai/whisper |
| Inkscape | Open-source vector editor | free ("licensed under the GPL") | All | Windows, Mac, Linux | Low; Affinity covers it | V | https://inkscape.org/ |
| Krita | Open-source painting and image editor | free ("GNU GPL v3 license"); optional paid Store builds | All | "Windows 8.1 or higher / macOS 10.15 / Linux" | Low | V | https://krita.org/en/download/ |
| Paint.NET | Light Windows image editor | free download; optional paid "Windows Store" copy | All | "PCs that run Windows" | Low-medium for quick crops | V | https://paint.net/ |
| Pixlr | Browser photo editor with AI tools | Plus "$2.49 per month" ("Ad-Free"); Premium "$9.99 per month"; Ultra "$24.99 per month" (toggle default not confirmed) | No free plan shown on the pricing page; ads implied | Web | Low; Photopea and Affinity are free | V | https://pixlr.com/pricing/ |
| Vizard | AI clipper of long videos into shorts | Creator "$29 $14.5 /month", "$174 billed yearly" ("no watermark"); Pro "$39 $19.5" | "$0", "60 credits/month", "Export videos in 720p", "3-day storage" | Web | Low: long-source tool | V | https://vizard.ai/pricing |
| quso.ai (formerly vidyo.ai) | AI clipper and scheduler | Lite "$29/mo Billed monthly", "$348 billed annually"; Essential "$39/mo"; Growth "$49/mo" | "$0/mo", "75 credits / month", "720p with a quso.ai watermark", "7 days data retention" | Web; "Advanced video editor (desktop)" on paid | Low | V | https://quso.ai/pricing |
| Klap | AI clipper | Basic "100 clips/mo $14.50 /mo $174 billed yearly"; Pro "$39.50 /mo" | "Try Klap free on 1 video. No credit card required." | Web | Low | V | https://klap.app/pricing ; https://klap.app/ |
| Munch Studio (formerly Munch) | AI clipper and repurposer | "Essential is $68 a month on a month to month plan or $38 a month billed yearly" | "7-day free trial" only | Web | Low; over budget | V | https://www.munchstudio.com/pricing |
| Gling | Removes silences, bad takes and filler words | Plus "$20/mon"; "$40/mon"; "$100/mon" | "$0": "1 hour of AI edited media per month", "Unlimited video export with watermark" | Web | Low-medium for talking clips | V | https://www.gling.ai/pricing |
| TimeBolt | Desktop silence and filler-word remover, free 4K screen capture | "$17/mo, $97/yr or $347 Lifetime"; "Full power. No limits. No watermark." on paid | "FREE ... exports are watermarked"; "free, local, and watermark-free" (4K screen capture) | "Mac + Windows · Local-first editing · No cloud upload" | Low-medium; only if Hollie records long takes | V | https://www.timebolt.io/pricing ; https://www.timebolt.io/ |
| Pictory | Script or article to video with stock footage | Starter "$25" per month billed annually ("$29" monthly); Professional "$35"/"$59" | "14 days free" trial | Web | Low | V | https://pictory.ai/pricing/ |
| InVideo AI | AI video generator and editor | Starter "$20 $10 per seat/mo, billed annually"; Pro "$60 $30" | A free editor tier is shown; limits not readable | Web | Low | V (prices), U (free limits) | https://invideo.io/pricing/ |
| Lumen5 | Text to video with templates | Basic "$19 USD per month, billed yearly"; Professional "$59 USD" | "$0/forever": "Contains Lumen5 branded outro", "Max 2-minute long videos", "5 videos per month" | Web | Low | V | https://lumen5.com/pricing/ |
| Repurpose.io | Auto-republishes videos across platforms | "$35 billed monthly"; "$79 billed monthly"; "$179 billed monthly" | "Publish 10 videos for FREE - No credit card required" (trial) | Web | Low; Buffer Free and Crosslist cover distribution | V | https://repurpose.io/pricing/ |
| StreamYard | Browser live streaming studio | Essential "$18.99" monthly or "$14.99 /mo" yearly (22% off); Core "$44"/"$35" | Free: "StreamYard logo in your streams", "Local recordings - 2 hours/mo", "For individuals only" | Web | Low-medium; browser live selling without installing OBS | V | https://streamyard.com/pricing |
| Auphonic | One-click audio levelling and noise cleanup | "9 h/m $11" per month ("$132 billed yearly"); "21 h/m $25" | "Auphonic is free for 2 hours of processed audio per month."; "Productions of free users come with a jingle." | Web | Low-medium; the free jingle is a watermark | V | https://auphonic.com/pricing |
| Bensound | Royalty-free music library | All Access "$9 /month (Billed $119 annually)"; "$19 /month (Billed $239 annually)" | "Free License with Attribution" tracks | Web | Medium; cheapest cleared music if credit lines are a bother | V | https://www.bensound.com/pricing ; https://www.bensound.com/faq |
| Free Music Archive | Creative Commons music search | free | Per-track CC licences; "You can use it for commercial purposes." (BY and BY-SA) | Web | Medium; check each track's licence | V | https://freemusicarchive.org/License_Guide/ |
| Storyblocks | Stock video, music and templates subscription | Essentials "$21 per month, billed annually"; Unlimited All Access "$30 per month, billed annually" | Trial FAQ present, answer not expanded | Web, Adobe plugin | Low; Pexels and Coverr are free | V (prices), U (trial) | https://www.storyblocks.com/pricing |
| Suno | AI music generator | prices did not render; "use your songs commercially on any paid plan" | Free Plan: "Best free model (v6-mini)", no commercial rights | Web | Low; AI music needs a paid plan for commercial use | V (licence rule), U (price) | https://suno.com/pricing |
| Luma (Dream Machine) | AI video and image generation | Plus "$30/month" with "Commercial use"; Pro "$90/month" | No free plan shown | Web | Low; same objection as Runway and Pika | V | https://lumalabs.ai/pricing |
| Google Vids | AI video maker tied to Google Slides and Gemini | "available to try at no cost, sign in to your Google account" | Yes; "Advanced features and expanded usage limits are available to business users on Workspace plans" | Web ("Available on desktop at vids.new") | Low; presentation-style videos | V | https://workspace.google.com/products/vids/ |
| Pippit AI (formerly CapCut Commerce Pro) | AI product-marketing video generator, "Powered by CapCut" | "USD101/year"; "USD246/year" (yearly toggle); "Remove watermark" is paid | "Free to use, upgrade anytime."; "Get free daily credits" | Web | Low; generates product ads, which a one-of-one shop does not need | V | https://www.pippit.ai/pricing ; https://www.pippit.ai/ |
| TikTok Studio | TikTok's creator app: analytics, scheduling, limited editing | free | All | "Download TikTok Studio from Google Play or the App Store"; "limited tools ... in the TikTok app and web browser" | Low-medium for scheduling from the PC browser; no Windows app named on this page | V | https://www.tiktok.com/support/faq_detail?id=7581820705491229240&category=web_account |

## 2. Notes per tool

Only facts from pages read today. No complaints were read on any page.

**Affinity by Canva.** The get-affinity page states "$0, free" and that you "sign in with your Canva account (or create one for free)". "Available on Mac, Windows & iPad". Homepage: "Affinity runs fast even on mid-range machines, but loves a dedicated GPU." Imports "PSD, AI, IDML, DWG" with layers kept and exports to Canva. Canva premium plan holders get extra AI features. FAQ headings on the page include "Is Affinity really free?" and "Will Affinity by Canva get free updates and new features?" (answers not expanded in the text). Enterprise SSO is the paid angle. For Hollie: this is the one install that upgrades the whole graphics side, free.

**LosslessCut.** GPL-2.0. "LosslessCut is maintained by me alone and will always remain free and open source." Windows download is a 7zip archive; "APPX (Windows) and PKG (macOS) do not work" for the store builds. Lossless means no quality loss and no render wait. Best first step on every iPhone clip before DaVinci or Clipchamp.

**HandBrake.** Version 1.11.2, "For Windows 10 and later". Converts "from nearly any format" to modern codecs. Use the built-in presets to hit size caps before upload.

**Meta Sound Collection.** Page text: "Thousands of high-quality audio tracks and sound effects", "Free to use in any videos you create and share on Facebook and Instagram." Needs a Facebook login to download. It does not cover TikTok, YouTube, Etsy listing videos or the Shopify site. The Meta Business Help URL this agent guessed returned 404.

**Incompetech.** "Licensed under Creative Commons: By Attribution 4.0". The FAQ says to "replace the word Title with the Actual Title of the piece" in the credit and that where credits are impossible you should "obtain a Standard License" (price not read). Works on every platform if the credit line goes in the caption or end card.

**Coverr.** Licence page: "Everything Coverr publishes is free for commercial and personal projects." Caveats: "Logos and trademarks in the footage aren't licensed to you"; "Premium" items, "including vertical (9:16) footage", need "Plus plan or higher" and "watermarked previews can't be used"; sponsored Shutterstock, iStock and PremiumBeat items "follow their own licenses"; AI generations come "as is" with no indemnity. Attribution "Not required for anything you download from Coverr". Pricing page shows Basic "$4.20 / month", Plus "$6.60 / month" under a "Pay yearly" heading.

**Bensound.** Pricing: "$9 /month (Billed $119 annually)", "$19 /month (Billed $239 annually)", "$39 /month (Billed $479 annually)", plus pay-per-track. FAQ: "To share videos on social media, our Individual License (Pay-per-track or All Access Subscription plan) has you covered." Free tracks use a "Free License with Attribution" and the FAQ describes YouTube copyright claims when the attribution text is missing. Licences "are valid worldwide and forever".

**Free Music Archive.** A search index of Creative Commons tracks; each track carries its own licence. BY and BY-SA allow commercial use with credit; BY-SA also requires the same licence on the video. Some CC licences on the site are non-commercial, so read the tag on each track.

**Buzz and Vibe.** Both are MIT-licensed desktop front ends for Whisper, transcribing on the PC with nothing uploaded. Buzz Windows installer is on SourceForge and "is not signed, you will get a warning when you install it." Vibe lists "macOS, Windows, Linux" and a "Stable timestamps mode for subtitle/movie-grade timing". Either produces SRT files that Clipchamp, DaVinci and CapCut can burn in. Whisper's "code and model weights are released under the MIT License", so commercial use is fine.

**Windows 11 Snipping Tool.** "Press Windows logo key + Shift + R to open the snipping tool overlay to capture a video clip." Some features ("Perfect screenshot", "Color picker") are "only available on a Windows 11 AI + PC". Enough for a packing or room-styling screen clip without installing OBS.

**NVIDIA Broadcast.** Requires "NVIDIA GeForce RTX 2060, Quadro RTX 3000, TITAN RTX, RTX Spark, or higher" and "Windows 10 64-bit, Windows 11 64-bit, Windows 11 on Arm". The page shows a "Download Now" button and no price; it is a free download, but no price statement was read (U on price). If Ricky's PC has an RTX card it gives clean webcam cutouts and noise removal in OBS, Clipchamp or any browser; otherwise skip.

**ScreenPal.** Branding reads "Screenpal formerly Screencast-O-Matic". Free: "15 minute recording limit", "10 hosted videos", "Easy video editing", "Blur webcam background". Deluxe "$4.00/mo paid annually" adds "Unlimited recorder", "Full video editor", "AI speech-to-text captions". Max "$10.00/mo paid annually" adds "Auto-captions & transcriptions" and "AI text-to-speech narration". The plan table has a "No watermark" row but which plans tick it was not readable in text. The "Do you offer monthly plans?" FAQ was collapsed.

**Streamlabs Desktop.** "Windows 10+", "Free, feature-packed broadcasting software. Open source on GitHub." The GitHub repo is GPL-3.0 and says "This application currently only supports OSX 10.14+ and 64-bit Windows." Ultra is "$27/mo" or "$189/year". The free tier's video editor shows "1 Hour Upload + Watermark" and "Create Custom Videos with Watermark"; the streaming side has "2 destinations" free. Same engine as OBS with a friendlier setup.

**StreamYard.** Free tier carries the "StreamYard logo in your streams" and "Local recordings - 2 hours/mo". Essential is "$18.99" monthly or "$14.99 /mo" on the yearly toggle with a "7-day free trial". "Essential, Core and Advanced plans are for individual use only" per its usage policy. Browser only, no install.

**Camtasia.** "You can download and use the full Camtasia Editor for free ... exported videos will include a watermark until you upgrade". Store: Starter "$39.00 per year" (Snagit plus watermarked editor), Essentials "$179.88 per year billed yearly", Create "$249.00 per year", Pro "$599.00". "Camtasia individual plans are non-transferable"; "Each Camtasia license is valid for use on two devices by the same user." Windows 10 20H2 or later.

**Kittl.** Free: "$0 /mo, free forever" and "Full commercial license" appears in every tier including Free. Pro "$19" monthly or "$14 /mo, billed annually". Good at retro lettering and distressed badge looks that match a vintage brand. Web only.

**Clipper and repurposing tools (Vizard, quso.ai, Klap, Munch Studio, Gling, Pictory, InVideo, Lumen5, Repurpose.io, TimeBolt).** Every free tier watermarks, caps resolution, expires, or is a trial: Vizard "60 credits/month", 720p, "3-day storage"; quso.ai "720p with a quso.ai watermark", "7 days data retention"; Klap free on "1 video"; Munch Studio "7-day free trial" then "$68 a month" or "$38 a month billed yearly"; Gling "Unlimited video export with watermark"; Pictory "14 days free"; Lumen5 "Contains Lumen5 branded outro", "Max 2-minute long videos"; TimeBolt "exports are watermarked" on free; Repurpose.io "Publish 10 videos for FREE" then "$35 billed monthly". These tools look for highlights in long recordings; a 40-second lamp clip has none. TimeBolt is the one that runs locally on Windows and would help only if Hollie records long talking takes.

**Auphonic.** "free for 2 hours of processed audio per month", but "Productions of free users come with a jingle." That is an audio watermark; Audacity (already listed) does the job without one. Paid starts at "$11" per month for 9 hours ("$132 billed yearly").

**Lightworks, OpenShot, VSDC, PowerDirector Essential.** All free on Windows without a watermark claim (Lightworks "Free forever" with "Full HD 1080p Export, including portrait video for social"; OpenShot "without subscriptions, watermarks, or project limits"; VSDC title "No watermarks"; PowerDirector "100% free version: PowerDirector Essential with no time limits"). The lane already has DaVinci, Shotcut and Kdenlive, so these are alternatives, not gaps that change the recommendation. PowerDirector's stock library is "Getty Images and Meta Sound Collection" with limited access for free users; its paid prices did not render.

**Pixlr.** No free plan listed on the pricing page today; Plus "$2.49 per month" is labelled "Ad-Free", implying the free editor has ads. Photopea and Affinity make it unnecessary.

**AI generators (Luma, Suno, Google Vids, Pippit AI, InVideo).** Luma Plus "$30/month" includes "Commercial use"; no free plan shown. Suno: commercial rights only "on any paid plan". Google Vids is "available to try at no cost" with a Google account and runs "on desktop at vids.new". Pippit AI (formerly CapCut Commerce Pro) is "Free to use" with "Remove watermark" paid. Same verdict as the lane: a one-of-one listing must show the real object, and TikTok and Meta label synthetic media.

**TikTok Studio.** The support page describes a phone app ("Download TikTok Studio from Google Play or the App Store") with "limited tools for creators in the TikTok app and web browser". No Windows desktop app is named on this page. www.tiktok.com/studio returned a 404.

## 3. Defunct, acquired or renamed (evidence read today)

- **Unscreen (video background remover) is folded into Canva.** https://www.unscreen.com/pricing redirected to https://www.canva.com/features/video-background-remover/, whose text says "the Video Background Remover on Canva Pro". The standalone Unscreen site no longer answers at that URL. V. (remove.bg, its sister product, was already reported to end 2026-12-01.)
- **Munch is now Munch Studio.** https://www.getmunch.com/pricing redirected to https://www.munchstudio.com/pricing ("Pricing - Munch Studio"). V.
- **vidyo.ai is now quso.ai.** quso.ai/pricing: "Coming from Vidyo.ai? Your plan and pricing are unchanged." V.
- **Screencast-O-Matic is now ScreenPal.** screenpal.com/pricing carries the "Screenpal formerly Screencast-O-Matic logo". V.
- **CapCut Commerce Pro is now Pippit AI.** https://commercepro.capcut.com/ redirected to https://www.pippit.ai/ ("Powered by CapCut, Pippit AI supercharges your content creation."). V.
- **Captions (on the lane list) now belongs to a company trading as Mirage.** mirage.app footer: "© 2026 NOCAP, Inc. d/b/a Mirage." The site still says "Explore Captions" and links "Captions on Web Terms", so the Captions product continues; the parent brand changed. V. The lane's pricing facts stand.
- **Vegas Pro is sold by Boris FX.** Plans page footer "© 2026 Boris FX. All rights reserved." and "sign in with your Boris FX account". The earlier owner (MAGIX) is from memory. V (Boris FX), U (history).
- **HitFilm (FXhome): status unknown.** https://fxhome.com/ failed (tunnel error) and https://artlist.io/hitfilm returned an empty page. U. Do not recommend until a vendor page loads.
- **Camtasia's pricing URL moved.** techsmith.com/camtasia/pricing/ is a 404; prices live at techsmith.com/store/camtasia. V.
- **Adobe Premiere Rush and OpenAI Sora** were already marked gone by the lane; nothing read today changes that.
- **Not defunct, checked:** TikTok Studio exists but as a phone app with a limited web mode (V). Loom (on the lane list) is sold through Atlassian: its pricing page, read today by lane 12, asks "What's the difference between buying Loom on Loom.com versus Atlassian.com?" and lists "Atlassian Guard Standard (SSO, SCIM)". V. Pricing facts on the lane stand.

## 4. Recommendation for Hollie

Install or sign up today (free, verified today):
1. Affinity by Canva (free, Windows). Sign in with the Canva account. Use it for framed product panels, cutout touch-ups after rembg, and any PSD work. It replaces the need for Photopea and GIMP side by side.
2. LosslessCut (free). Trim every iPhone clip here first; no render wait, no quality loss.
3. HandBrake (free). Compress finished videos to MP4 under the TikTok 500 MB and Etsy limits.
4. Meta Sound Collection (free, Facebook login) for Reels and Facebook music. For TikTok, YouTube and the site, use Incompetech with the credit line, or Coverr's free tracks. Keep the lane's rule: no CapCut library music until its terms are read.
5. Buzz (free) if Subtitle Edit feels heavy; both are offline Whisper, both make SRT files.
6. Snipping Tool (already in Windows 11): Win + Shift + R for a quick screen clip.
7. NVIDIA Broadcast only if the PC has an RTX 2060 or newer; it cleans the webcam and room noise for OBS and browser recordings.

Pay only once it earns it:
- Kittl Pro ("$14 /mo, billed annually" or "$19" monthly) if the free tier's templates run out and the vintage lettering is selling the brand.
- ScreenPal Deluxe ("$4.00/mo paid annually") if Hollie wants a hosted library of how-to videos for buyers (care, styling, packing) with captions, instead of YouTube.
- Bensound All Access ("$9 /month (Billed $119 annually)") only if credit lines on free music become a chore across platforms.

Skip and why:
- Every AI clipper and repurposer (Vizard, quso.ai, Klap, Munch Studio, Gling, Pictory, InVideo, Lumen5, Repurpose.io): wrong shape for short product clips; free tiers watermark or expire.
- Camtasia, Streamlabs Ultra, StreamYard paid: OBS and Clipchamp already do this free; Streamlabs Desktop free is fine if OBS feels bare.
- Auphonic free: adds a jingle to the audio. Audacity instead.
- Luma, Suno, Google Vids, Pippit AI: generated product content; the buyer needs the real object.
- Pixlr, Inkscape, Krita, Paint.NET: redundant once Affinity is installed.

## 5. Gaps and pages that would not load

- screenpal.com/pricing loaded but the price cards were not in the text; screenpal.com/plans had them. Free-tier watermark status not readable.
- techsmith.com/camtasia/pricing/ returned 404; techsmith.com/store/camtasia loaded.
- tiktok.com/studio returned 404; the TikTok support FAQ loaded instead. No Windows desktop app named.
- facebook.com/business/help/249451493651831 (guessed id) 404; the Sound Collection landing page loaded with the licence sentence.
- bensound.com/licensing "Information Page Not Found"; bensound.com/pricing and /faq loaded.
- soundstripe.com/pricing: bot wall (117 chars). U, not listed.
- create.vista.com/pricing/ and /pricing: 404 twice. VistaCreate (formerly Crello) is U, not listed.
- support.microsoft.com guessed article id failed; the real Snipping Tool page loaded.
- fxhome.com: tunnel failed; artlist.io/hitfilm: empty page. HitFilm status U.
- app.klingai.com membership page: bot wall (35 chars). Kling not listed.
- podcast.adobe.com/en/enhance: empty page (Adobe walls, consistent with the lane). Adobe Podcast Enhance not listed.
- ads.tiktok.com Creative Center music library: HTTP 500. TikTok Commercial Music Library is U; the rule that business accounts must use it is from memory and not stated here.
- videosoftdev.com/vsdc-pro: 404; VSDC Pro price unknown.
- cyberlink.com compare page redirected to the overview; PowerDirector 365 and 2027 prices not shown.
- vegascreativesoftware.com plans-pricing loaded but prices did not render as text.
- suno.com/pricing loaded without dollar amounts.
- lumalabs.ai/pricing shows no free plan; pixlr.com/pricing shows no free plan; invideo.io free-tier limits and storyblocks.com trial answer were collapsed.
- nvidia.com Broadcast page states requirements but no price.
- WebSearch was exhausted for this turn, so no roundup, Product Hunt, Chrome Web Store or Shopify App Store category pages were used for discovery; candidates came from this agent's knowledge of the category. The "two independent 2026 roundups" test was not run.
- Etsy's AI-content and video policies were not re-attempted (walled for the lane; another agent's job).

## 6. Sources

Loaded today (2026-11-07):
- https://www.affinity.studio/
- https://www.affinity.studio/get-affinity (from https://www.affinity.studio/get-affinity/)
- https://www.affinity.studio/help/ (nav only)
- https://github.com/mifi/lossless-cut
- https://handbrake.fr/
- https://www.openshot.org/
- https://github.com/chidiwilliams/buzz
- https://thewh1teagle.github.io/vibe/
- https://github.com/thewh1teagle/vibe
- https://github.com/openai/whisper
- https://screenpal.com/pricing (no prices in text)
- https://screenpal.com/plans
- https://vizard.ai/pricing
- https://quso.ai/pricing
- https://klap.app/pricing
- https://klap.app/
- https://www.munchstudio.com/pricing (from https://www.getmunch.com/pricing)
- https://streamlabs.com/
- https://github.com/streamlabs/desktop
- https://streamyard.com/pricing
- https://www.techsmith.com/camtasia/ (from https://www.techsmith.com/camtasia.html)
- https://www.techsmith.com/store/camtasia
- https://www.tiktok.com/support/faq_detail?id=7581820705491229240&category=web_account (from https://support.tiktok.com/en/using-tiktok/creating-videos/tiktok-studio)
- https://www.facebook.com/sound/collection/
- https://www.bensound.com/pricing
- https://www.bensound.com/faq
- https://incompetech.com/music/royalty-free/faq.html
- https://freemusicarchive.org/License_Guide/
- https://www.canva.com/features/video-background-remover/ (from https://www.unscreen.com/pricing)
- https://www.gling.ai/pricing
- https://www.timebolt.io/
- https://www.timebolt.io/pricing
- https://pictory.ai/pricing/
- https://inkscape.org/
- https://krita.org/en/download/
- https://paint.net/ (from https://www.getpaint.net/)
- https://pixlr.com/pricing/
- https://www.kittl.com/pricing
- https://www.storyblocks.com/pricing
- https://coverr.co/license
- https://coverr.co/pricing
- https://invideo.io/pricing/
- https://lumen5.com/pricing/
- https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-app/
- https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots
- https://mirage.app/
- https://lumalabs.ai/pricing
- https://auphonic.com/pricing
- https://www.vegascreativesoftware.com/vegas-pro/
- https://www.vegascreativesoftware.com/vegas-pro/plans-pricing/ (prices did not render)
- https://www.cyberlink.com/products/powerdirector-video-editing-software/features_en_US.html
- https://www.cyberlink.com/products/powerdirector-video-editing-software/overview_en_US.html (also reached from the compare URL)
- https://suno.com/pricing (no prices in text)
- https://lwks.com/
- https://lwks.com/pricing
- https://www.videosoftdev.com/
- https://repurpose.io/pricing/
- https://workspace.google.com/products/vids/
- https://www.pippit.ai/ (from https://commercepro.capcut.com/)
- https://www.pippit.ai/pricing

Failed or empty today:
- https://www.techsmith.com/camtasia/pricing/ (404)
- https://www.tiktok.com/studio (404)
- https://www.facebook.com/business/help/249451493651831 (404)
- https://www.bensound.com/licensing (not found)
- https://www.soundstripe.com/pricing (bot wall)
- https://create.vista.com/pricing/ and https://create.vista.com/pricing (404)
- https://support.microsoft.com/en-us/windows/record-your-screen-in-snipping-tool-c51e3d5f-4d8a-4f0b-b5b8-4f4b2e3f7f0a (wrong id)
- https://fxhome.com/ (tunnel failed)
- https://artlist.io/hitfilm (empty)
- https://app.klingai.com/global/membership/membership-plan (bot wall)
- https://podcast.adobe.com/en/enhance (empty)
- https://ads.tiktok.com/business/creativecenter/music/pc/en (HTTP 500)
- https://www.videosoftdev.com/vsdc-pro (404)
