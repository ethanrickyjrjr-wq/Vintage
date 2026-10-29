# w1c-content-hooks: what to post (hook, caption and format bank)

Lane w1c, accessed 2026-10-29. Raw: `research/social-2026-10-29/raw/w1c-*` (15 reel transcripts and metadata in `raw/w1c-reels/`, crawls, `w1c-search-results.txt`). Method: SearXNG `site:instagram.com/reel` queries (about 12 search.sh plus about 19 WebSearch, over the 20-query budget) gave about 60 reel URLs; 15 were run through a yt-dlp + faster-whisper `small` (VAD) driver equivalent to clipfeed (one request per reel, no login, public, 12 s apart). First-3-second frames at 0.2, 1.2 and 2.6 s were cut with the Windows ffmpeg and read by eye. Videos stay in the scratchpad, not the repo. None of the 15 is one of d1's 12 accounts.

## TL;DR

- **Hands-first is viable: 9 of 15 reels had no speech** (6 music-only, 2 with no audio stream, 1 meme sound). `observed (n=15 reels, 13 accounts, small)`.
- **11 of 15 put a text hook on screen from frame 0 to 1 s**, median 7 words (range 3-10). Of the 4 without text, 2 open on a hand or light-on reveal inside 3 s (Esthetic Vintage, Ella Grace), which maps onto the shop's "one click" lamp reel. `observed`.
- **The vendor data does not favour Reels for reach.** Socialinsider (Oct 2026, 21.6M Instagram posts, Jan-Sep 2026): Reels lead engagement rate only in the smallest tier measured (1-5K followers, 0.80% vs 0.75%; accounts under 1K are not measured); carousels lead engagement above 5K and lead views at every tier. The case for Reels at launch rests on Instagram's recommendation surfaces (Reels tab, Trial Reels to non-followers, `verified` on the creators page) and practitioner opinion, not on this data. `study (n=21.6M, vendor)`.
- **Caption length: under 60 words for carousels (0.37%), 30-90 words for Reels (0.25% vs 0.20% outside).** The 2023 study said under 30 words. Both are vendor data and disagree by era. `study (vendor)`; need review.
- **Only 4 of 15 used a comment keyword (3 link, 1 claim).** The link keywords came from educators, not dealers. The CTA inflates comments by construction, so no engagement claim follows. `observed`.
- **FIXED-CONSTRAINT CONFLICT, not resolved here: a URL typed into a public Instagram comment is not tappable** (`vendor claim`, Aug 2026). "Reply LINK with the link" only works as a DM or private reply, a Story link sticker, or link-in-bio plus a piece number. See section 3.
- **Reach was not measurable.** No follower counts; `view_count` was None on all 15. Rankings below are by effort plus evidence strength, with reach inferred. `observed`.
- **Avoid** other apps' logos on a reel (Instagram says it does not recommend them; own logo is fine, `verified` via trade press), "comment SOLD to purchase" mechanics, and showroom hours or addresses in captions. `observed` plus `verified`.
- **Gate:** no product-link post until real stock exists (BRIEF). Pre-launch content is room, process and education only.

Tag note: `observed` = measured from this lane's own captures (15 reels, 2026-10-29), equivalent to `study (n=15, own capture)`.

## 1. The 15-reel sample (all `observed`, 2026-10-29)

Likes and comments are as of capture. Follower counts are unknown, so raw likes are not comparable across accounts. "c/l" is comments per 100 likes. Aud: S = speech-led, M = music or sound only, N = no audio stream. URL pattern `instagram.com/reel/<id>/`.

| # | Account, id | Date | Sec | Likes | Cmts | c/l | Aud | First 3 s, spoken | First 3 s, on screen | Hook type | Cap words / tags | CTA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | @arvinolano C2IJpjZpuHV | 2024-01-15 | 89 | 4,984 | 501 | 10.1 | S | "Here's how you can find the best lamps on Etsy. It's all about the keywords" | "How to find the best vintage lamps on Etsy" | how-to promise | 24 / 0 | link keyword "LINKS" |
| 2 | @alexandra__harper DTZC-Isjy2Q | 2026-01-12 | 174 | 16,087 | 445 | 2.8 | S | "Pottery Barn or Home Goods part 33. I'm Alexandra and every week I take one of your spaces..." | "Pottery Barn or Home Goods" animating in | named series (Pt 33) | 108 / 5 | link keyword "SHELVES" |
| 3 | @redeux_style DU4T4UejheP | 2026-02-18 | 249 | 1,198 | 63 | 5.3 | S | "I get asked a lot about vintage glass and how I know what I can use in my home" | "Do I ever worry about using vintage glass!" | question + FAQ | 15 / 5 | spoken link keyword (at end) |
| 4 | @emmanuel.uddenberg DfDYPbQS2Sz | 2026-10-28 | 25 | 984 | 54 | 5.5 | S | "I have a thing for lamps and this one might be the coolest vintage 1970s chrome cylinder lamp" | "VINTAGE LAMP PICKUP" | format label | 19 / 5 | none |
| 5 | @vladslickbartender DVy8iwTknbI | 2026-03-12 | 50 | 522 | 13 | 2.5 | S | "How do I get expensive glassware for about $1 a piece?" | none (pour) | spoken question | 8 / 0 | none |
| 6 | @more.than.a.fad DOcDNMpktAg | 2025-09-10 | 17 | 63 | 1 | 1.6 | S | starts mid-demo: "it's french glass but it's newer glass..." | quote "How do you know it's not Depression glass?" plus burned captions | question | 76 / 0 | "drop questions below" |
| 7 | @estheticvintage DXzGXxyR6zY | 2026-05-01 | 11 | 494 | 6 | 1.2 | M | none | none; hand reaches the switch, light on at about 2.5 s | hand reveal | 65 / 0 | "Message for info" |
| 8 | @ellagracemarketplace DRnquaSgXx7 | 2025-11-29 | 22 | 414 | 10 | 2.4 | N | none | none; unlit to lit at about 2.6 s | light-on reveal | 77 / 17 | "screenshot and give us a call", plus hours and address |
| 9 | @hannaehenderson DUUG2ztkT4y | 2026-02-03 | 56 | 399 | 15 | 3.8 | M | none | "$8 LAMP THRIFT FLIP" | format label | 124 / 5 plus keyword line | none |
| 10 | @arvinolano DWj-Nq_SJBb | 2026-03-31 | 13 | 1,234 | 9 | 0.7 | M | none (music) | "Some girls want designer bags and some want vintage lamps" | meme on audio | 9 / 0 | none |
| 11 | @craftedhiveculture Ddpv545z5Et | 2026-09-24 | 114 | 123 | 20 | 16.3 | N | none | "Another estate sale haul \| Part 1" | series label | 102 / 5 plus keyword line | question "what would you have grabbed first?" |
| 12 | @arvinolano DboGVZjAMiz | 2026-08-04 | 13 | 129 | 1 | 0.8 | M | meme clip "He said..." at 11.7 s | "When he asks what I bring to the table" | meme on audio | 8 / 0 | none |
| 13 | @bcmodernmke DUZgrlpjhFg | 2026-02-06 | 60 | 74 | 4 | 5.4 | M | none | "Packing Vintage Pyrex Bowls for Shipping *ASMR" (face in frame) | format label | 31 / 3 | none |
| 14 | @ahundred.stories DSJ8l9lCG6V | 2025-12-12 | 13 | 31 | 2 | 6.5 | M | none | "FANCY SOME HOLLYWOOD GLAMOUR?" | question over object | 43 / 9 | "Available online now" |
| 15 | @littlewingantiques DWigDV9EoPn | 2026-03-31 | 40 | 22 | 2 | 9.1 | M | none | none (static lamp) | none | 63 / 0 | "Comment sold to purchase" (claim) |

Caution on audio: Whisper's VAD drops non-speech, so "M" cannot tell music from ASMR sound.

**Patterns that survive (n=15, 13 accounts; read as hypotheses):**

| Pattern | Count | Note |
|---|---|---|
| Text hook on screen by about 1 s | 11 of 15 | median 7 words; format labels 5, questions 3, memes 2, how-to 1. The 4 without text: 2 hand or light reveals, 1 spoken question, 1 static |
| Not speech-led | 9 of 15 | the speech-led reels were the educators and the pickup reel |
| Length | 7 at 25 s or less; 5 at 40-90 s; 3 over 110 s | dealer product reels 11-40 s; process 50-60 s; education and series 89-249 s |
| Caption words (hashtags excluded) | median 43; 6 at 30 or less, 6 at 31-90, 3 over 90 | dealers write spec blocks of 63-77 words; creators write 8-25 |
| Hashtags | 0 in 7; 3-5 in 6; over 5 in 2 | both over-5 posts predate 2025-12-19 (Ella Grace's 17 tags still display, so any cap did not strip old posts). Of the 11 later posts, 5 use none and 5 of the 6 that use tags sit at exactly 5 (one at 3); two add an unhashed keyword line. Consistent with the reported five-tag cap (`inferred`; the cap itself is `unverified (search snippet)`, trade press Dec 2025) |
| CTA | link keyword 3, claim 1, message or call 2, question 2, "online now" 1, none 6 | 5 of d1's 12 accounts use comment or DM claims (d1 snippets), so claim mechanics are common in the niche |
| Series naming | 3 (Pt 33, Part 1, ASMR) | the biggest raw-likes reel (16K) is a numbered weekly series |
| Comments per 100 likes by CTA | no CTA median 3.1; link keyword 2.8, 5.3, 10.1; question 1.6 and 16.3 | a CTA inflates comments by construction; no engagement conclusion |

**Small-n limits:** 15 reels from a search-index sample, not a performance sample. Arvin Olano is 3 of 15 (count him once: 13 accounts). The 4 biggest raw-like reels are personality or education creators with unknown audiences. One reel from 2024; 14 from Sep 2025 on. No carousel could be sampled (yt-dlp reaches video posts; the carousel query returned no `/p/` URLs). One timepoint (likes still grow). Three stills per reel for the hook.

**Second sample, snippet only (`unverified (search snippet)`, title text, not watched):** DNyLWLL2Gat "SOLD!!!! Incredible 1930s Art Deco brass floor lamp..." (claim style); DZ11V9TO1ZF "Some of my favourite lamps we have for sale! Drop me a message if..." (DM CTA); DYPisl7opbv "Set of Vintage Green Hollywood Regency-style table lamps"; DTyh9nFDSUo "Now available in my booth" (showroom wording); Dbk_XEFvtDJ "I found this rare 1993 martini lamp on Facebook Marketplace in the..." (found-story hook); DX4bO0WoJd3 "Let's pack the first 10 orders together - ASMR edition"; DeZgyBSO909 "behind the scenes for a little packing ASMR"; DVhZkW3DJ4S "comment SHOP for a link" (styling); DUl3pqRDvGC "What I thrifted VS. How I DIY'd it"; DZCx7tqRpuB "Buy the ugly lamp... the perfect way to start your thrift flip". Titles truncate captions, so CTAs cannot be counted from them.

## 2. Platform and practitioner evidence

| Claim | Source, date | Tag, bias |
|---|---|---|
| Instagram engagement by tier, Jan-Sep 2026: 1-5K Reels 0.80, carousel 0.75, image 0.45; 5-10K 0.65/0.70/0.35; 10-50K 0.55/0.60/0.33. Carousels top views at every tier. ER = (likes+comments)/followers | https://www.socialinsider.io/blog/what-to-post-on-social-media/ (Oct 15 2026; read live) | `study (n=21.6M IG posts of 62.7M, vendor)` |
| All-size ER Q3 2026: Reels 0.48, carousels 0.50, images 0.35; carousels earn the most saves | https://www.socialinsider.io/instagram-benchmarks (read live) | `study (35M posts for 2025, vendor)` |
| Captions: Instagram under 60 words best; carousels 0.37% under 60 words, 0.28% at 60-90, 0.20% over 90; Reels 0.25% at 30-90 vs 0.20% outside; 90+ worst everywhere | https://www.socialinsider.io/blog/social-media-caption-length-best-practices/ (Oct 27 2026) | `study (multi-million posts, Jan-Sep 2026, vendor)` |
| Older study: under 30 words best; n=9,117,401 posts, 82,952 pages, Jan-Jul 2023 | https://www.socialinsider.io/blog/instagram-caption-length/ (updated Oct 19 2026) | `study (vendor)` |
| A carousel not swiped can be re-served starting at slide 2, so slide 2 is a backup hook | Socialinsider page above (quotes a Dentsu strategist); the Mosseri origin was not read | `vendor claim` |
| Educating carousel: "Turn a product shoot into a carousel that educates"; Socialinsider says carousels win saves and "service content" | https://journalofantiques.com/columns/instagram-strategy-for-vintage-sellers-why-most-shops-are-using-it-wrong/ (Jan 7 2026, via d1); Socialinsider | two sources, both sell analytics or agency services: `vendor claim` |
| Reels up to 3 min eligible for non-follower recommendation (US); "post original content consistently"; audio on photos and carousels may reach the Reels tab; Trial Reels show a reel to non-followers first | https://creators.instagram.com/blog/the-latest-with-instagram (Jan 21 2025; read live) | `verified` (official) |
| "Own logo is fine; we try not to recommend Reels with logos from other apps" (Mosseri) | https://www.socialmediatoday.com/news/instagram-clarifies-including-your-own-logo-on-a-reel-is-ok/730852/ (Oct 23 2024; the reel itself not read) | `verified` as quoted by trade press |
| Signals to watch: average watch time, likes per reach, sends per reach; "open with a strong hook in the first three seconds" | https://blog.hootsuite.com/instagram-algorithm/ (read live) | `vendor claim` (attributes to Mosseri 2025); no Mosseri 3-second statement found |
| Sound off: "most video ads in mobile feed are viewed without sound"; captions +12% view time; "65% who watch 3 s watch 10 s" | https://www.facebook.com/business/news/updated-features-for-video-ads (undated, ads, names retired tools) | `vendor claim`, old, ads only |
| Counter figure: "80%+ of Reels viewed with sound on", attributed to Meta | WebSearch summary of trade press | `unverified (search snippet)` |
| Text overlay: express the message visually so it works muted (same ads page, e.g. a question as the opening text, then 1-2-3 steps on screen); this sample's on-screen hooks run a median 7 words (3-10), 11 of 15 reels | same Meta ads page; own capture | `vendor claim` (old, ads only) plus `observed` |
| Business accounts often cannot use trending licensed audio; use the "Original Audio" filter, or copy the trend with different audio; do not switch to Personal to get it | https://www.planoly.com/blog/commercially-licensed-vs-trending-sounds-what-can-brands-use (read live; Planoly sells a scheduler) | `vendor claim` |
| Caption links are not clickable except a Meta Verified test (reported Mar 16 2026, 10 links a month) | https://petapixel.com/2026/03/16/instagram-begins-testing-clickable-links-in-post-captions/ (read live; cites Engadget, not read) | `verified` as press report |
| Comment URLs show as plain text, not tappable; a keyword comment then DM converts at 15-30% | https://instantdm.com/blog/instagram-comment-links-2026-guide (Aug 24 2026) | `vendor claim` (sells DM automation); no official page read |
| CommentSold's CommentChat sends a public reply plus a DM with "the product link you specify" (links travel by DM) | https://try.commentsold.com/sell-everywhere/instagram/ (read live by d1, 2026-10-29) | `vendor claim` (second source, d1) |
| Comment-to-DM conversion 12-30% (InstantDM, SmartReply, ManyChat); no independent study; denominators undefined | WebSearch summaries | `unverified (search snippet)`, vendor bias |
| 50 hook templates, product-centric ("Watch how we pack a [product] order") | https://insense.pro/blog/instagram-reel-hooks (Oct 23 2026) | `vendor claim`, no data |

## 3. Decisions (options)

| Decision | Option | Price | Effort | Risk | Wins when |
|---|---|---|---|---|---|
| Format mix | A Reels-led | free | 10-40 min a post | no vendor data says Reels win reach | the Reels tab and Trial Reels (verified) are the launch lever |
| | B carousel-led | free | 20 min a post | slower discovery by non-followers | saves and education matter most; carousels lead views and engagement above 5K (vendor) |
| | C 3 Reels plus 2 carousels a week | free | about 90 min of shooting a week | spread thin | default: Reels for reach attempts, carousels for saves. `inferred`; reach not measured |
| On camera | A hands-only | free | lowest | no personality hook | default; fits the room and hands brand |
| | B hands plus Hollie voiceover | free | plus 10 min a script | voice quality | a spoken fact helps (education reels led raw likes, confounded) |
| | C Hollie on camera | free | highest | Hollie's comfort | Hollie's own call |
| Audio | A native ASMR or room sound | free | none | none known | first choice |
| | B Instagram commercial library | free | 5 min to pick | contents unverified | a music bed is wanted |
| | C paid licensed library | price not read | 5 min | cost, licence terms | defer to w2a |
| Link delivery (the constraint conflict) | A link in bio plus "piece No. [n]" | free | 0 | one extra tap for the viewer | every post |
| | B comment LINK, then a DM or private reply with the page, by hand | free | minutes a day | slow replies; one vendor flags keyword-comment wording as engagement bait (need review) | "LINK" comments arrive |
| | C the same, automated | paid, price not read (w2d) | setup hours | account-approval gates (see `social-comment-ai.md`) | volume justifies it |
| | D Story link sticker | free | 3 min a Story | Stories only; vendor claim | a drop-day Story |

## 4. 30 hook templates (text on screen at frame 0; hands-first; `inferred` from the sample, sources in brackets)

Rules: 3-10 words; "Gone", never "sold"; no "visit", "in store", "come by"; "style", never "interior design"; no safety, electrical or price claims.

| # | Hook line | Shot |
|---|---|---|
| 1 | One click. | Hand turns the lamp on; glow by second 3 [Esthetic Vintage, Ella Grace] |
| 2 | Wait for the glow. | Dim room, switch, light up |
| 3 | The ring test. | Hand flicks a glass; sound on [Redeux Style] |
| 4 | Hollie's hands. A [decade] [object]. | Hands lift and turn it |
| 5 | Turn it over. | Hand flips the piece to show base and mark |
| 6 | Weigh it. | Hand lifts brass or cut glass, no talking |
| 7 | Fancy some [Hollywood glamour]? | Object, slow push-in [A Hundred Stories] |
| 8 | Real or reproduction? Check the seam. | Two pieces, hand finds the seam [More Than a Fad] |
| 9 | Why does this lamp click three times? | Hand cycles the switch [Esthetic Vintage caption] |
| 10 | How do you know it's [cut glass]? | Question text, hand test |
| 11 | What is this? | Odd object, hands only, answer in the caption |
| 12 | Buy the ugly lamp. | Before shot, hands [snippet DZCx7tqRpuB] |
| 13 | I found this [rare thing] in [unlikely place]. | Found-story label card [snippet Dbk_XEFvtDJ] |
| 14 | How to read a vintage lamp in 20 seconds. | Reel or carousel: base, socket, cord, shade, drop |
| 15 | Words that find good [lamps]. | Text-only how-to [Arvin Olano, 4,984 likes] |
| 16 | What "good condition" means here. | Close-up of one honest flaw |
| 17 | Three things on a shelf: the triangle. | Hands build a group of three [Alexandra England] |
| 18 | How it leaves. | Hands wrap pink glass; ASMR [BC Modern] |
| 19 | Wrapping [pink glass]. No talking. | Packing, original sound |
| 20 | Unboxing the find. Part 1. | Box, hands, items out [Candese and Kelly] |
| 21 | New shade, same lamp. | Before and after, only if the piece is restyled [Hanna Henderson] |
| 22 | [Object] No. [n] of the week. | Fixed title, one object [Palm Beach Regency "Top Six", via d1] |
| 23 | Hollie's Top Three. | Three objects, fast cuts |
| 24 | Part 1 of [n]. | Series label over the first object |
| 25 | Act [n]: [theme]. | A drop named like a set (d1) |
| 26 | Same corner. More plot. | Bare corner, then dressed (d1 skeleton) |
| 27 | Some want designer bags. Hollie wants a lamp. | Text on a lamp; original audio [Arvin Olano, 1,234 likes] |
| 28 | POV: the room agrees. | Light on, room reacts |
| 29 | One lamp, three corners. | Same piece moved three ways |
| 30 | Gone. Someone has taste. | Day-after still with a neon-pink GONE stamp (d1) |

## 5. 12 repeatable formats, ranked by effort (minutes per post)

Reach is not measured, so rank = effort, with evidence strength beside it. Faceless = no face needed.

| Rank | Format | Length | Shot list | Who does what | Min | Faceless | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | "Gone." stamp | 6 s | Real listing photo plus stamp | Claude or Codex templates the photo; Hollie approves | 3 | yes | d1 snippets only; weak |
| 2 | Teaser "Tomorrow: [object]" | 6-8 s | One close-up, no price | Hollie shoots; Claude writes caption | 5 | yes | d1, 4 accounts (snippet) |
| 3 | Drop-day carousel, "Here" tags | 3-5 slides | Photos already shot | Claude drafts; Hollie approves | 5 | yes | d1; needs real stock |
| 4 | "One click" lamp reveal | 8-12 s | Locked phone, hand, switch, light at 2-3 s | Hollie films 5 lamps in 30 min | 10 | yes | 2 of 15 reels open on a hand or light reveal; moderate |
| 5 | Text-meme on original sound | 12 s | Object plus about 8-word text | Claude writes text; Hollie films | 10 | yes | Arvin Olano 1,234 vs 129 likes, same account; mixed |
| 6 | Packing ASMR "How it leaves" | 30-60 s | Tissue, tape, note card, box | Hollie films a real order; blur labels | 15 | yes (hands) | 1 reel, 74 likes; weak |
| 7 | "Read the lamp" education carousel | 6-8 slides | Close-ups of base, socket, cord, shade | Hollie shoots; Claude lays out | 20 | yes | vendor study: carousels lead saves and views; moderate |
| 8 | Haul or unboxing, Part 1 and 2 | 60-110 s | Boxes, items, text labels | Hollie films; sound off is fine | 25 | yes | 1 reel, 16 comments per 100 likes; weak |
| 9 | Voiceover fact, hands on object | 20-60 s | Hand demo plus recorded voice | Hollie records a line; Claude writes the script | 30 | voice only | education reels led raw likes; confounded |
| 10 | Restyle process (new shade, new cord) | 30-60 s | Before, steps, after | Hollie; no safety claims | 40 | yes | 1 reel, 399 likes; only if the shop restyles |
| 11 | "Same corner. More plot." | 15 s | Bare, then dressed | Hollie moves pieces | 45 | yes | d1 skeleton; no sample evidence |
| 12 | "Hollie has notes" series | 120-170 s | A reader sends a space; Hollie styles it | Hollie on camera or voice | 60+ | no | 16K likes (Alexandra England), a different niche; wait for Hire Hollie |

Cross-use (note only): formats 1-8 re-export clean for Facebook and TikTok; keep the Instagram logo out.

## 6. Captions

Open with a searchable phrase (Hootsuite and Socialinsider both say Instagram search leans on caption keywords; `vendor claim`). At most 5 hashtags.

| Length | Formula | Example |
|---|---|---|
| Short, 8-30 words | [Keyword phrase]. [One feeling line]. Piece [No.], link in bio. | Brass tulip lamp, 1980s. The room agrees. Piece 14, link in bio. |
| Medium, 31-60 words (Reels, carousels) | [Keyword hook]. [Era, material, size]. [One honest flaw]. [Where the page is]. | Pink pressed-glass bowl, 1950s. About 9 inches across. One small rim chip, shown in slide 3. Everything is on the listing page, link in bio, piece 22. |
| Long, 60-90 words (education, story) | [Question]. [3 short facts]. [Hollie's rule]. [Save line]. [Page]. | How do you spot cut glass? It rings when flicked. It is heavier than it looks. The edges are sharp. Hollie's rule: test it in your hand, not by the photo. Save this. The piece list is in the link in bio. |
| Gone edit | Gone. [Piece]. [One provenance line]. [Next drop day]. | Gone. Pink pressed-glass bowl, 1950s. Found in [town]. Next drop [DROP DAY]. |

## 7. 10 CTA lines that survive the constraints

1. Piece [No.] is on the listing page. Link in bio.
2. Full photos and honest condition: link in bio, piece [No.].
3. Comment LINK and Hollie sends the page by message. (Delivery by DM; see section 3.)
4. Save this for the day you stand in front of a [lamp].
5. Send this to the friend with a [pink glass] list.
6. Tomorrow: [object]. Follow to see it first.
7. The page shows what is Here and what is Gone.
8. Tell Hollie what you are hunting. Name the object.
9. Which corner next? Comment 1, 2 or 3.
10. Same piece, more angles: link in bio.

**Reply wording (one canned line each):**
- Live, "is this available?": "The listing page is the only truth. If it says Here, it is here. If it says Gone, it is Gone. Pieces can't be held. Link in bio, piece [No.]."
- Live, "price?": "Price, condition and measurements are on the listing page. Prices are fixed. Link in bio, piece [No.]."
- Pre-launch (use until real stock exists): "Hollie is still building the shop. The first real drop is announced here first."
- "LINK": a DM or private reply with the page URL only.

## 8. What to avoid

| Avoid | Why |
|---|---|
| Another app's logo or watermark on a reel | Instagram says it does not recommend Reels with other apps' logos (Mosseri quote, `verified` via trade press); own logo is fine. Check each editor's export for its own logo (w2a, w1h) |
| Trending audio the account cannot use | Vendor claim: business accounts lose licensed trends. Do not switch to a Personal account to get them (loses insights and contact buttons, per Planoly). Copy the format, change the sound |
| "Comment SOLD / CLAIM to purchase" | Little Wing Antiques' mechanic; a commitment-to-buy comment is the claim system the shop rejects |
| Showroom wording | Ella Grace's caption has hours, an address and "give us a call"; a snippet reel says "now available in my booth" |
| Safety or health advice | The glass reel advises on lead and food use; skip it or take it to a lawyer |
| Electrical claims | "Rewired", "safe", "works well" are claims; state cord condition only |
| Discount or "deal" framing | "$8 flip" and "$1 glass" frame cheap sourcing; the shop has no offers or codes |
| Customer labels in packing videos | Blur names and addresses |
| Product-link posts before real stock | BRIEF gate |

## 9. Recommendation for Holliewood & Vine

- **(a) Free and native:** Hollie films formats 1-4 and 7 on a phone in one weekly session (about 90 minutes for 5 pieces); captions from the section 6 formulas; link in bio plus piece number; "LINK" replies by hand via DM; a free scheduler within d1's caps. Human: everything, every post.
- **(b) One paid tool:** only a DM automation for "LINK" (price not read, w2d) once comment volume is real. Nothing else here needs money.
- **(c) Claude + Codex pipeline:** Claude drafts hook, caption and CTA from photos plus one line; Codex or ffmpeg builds "Gone" stamps and carousel layouts from the real photos. Approve-by-exception fits formats 1-3 (templated); formats 9 and 12 need Hollie's eyes every time. Human: stock truth, "Gone" status, any voice or face.

## 10. X verified, Y need review

- Caption length: 2023 study verified (under 30 words); Oct 2026 study verified (carousels under 60, Reels 30-90); both vendor; which applies to a new account needs review.
- Reel length: Jan 2025 official page verified (3 min eligible); the sample has a 249 s reel; current cap need review (w1a).
- Reels vs carousels: the leader flips with account size (Reels under 5K, carousels above); the engagement formula excludes views and saves.
- Sound: the ads page (undated) says most feed video is watched muted; trade press says 80%+ of Reels are watched with sound on (unverified). Design for both: text on screen plus native sound.
- Hashtag cap of five: trade press only; the sample is consistent.
- Comment URLs not tappable: vendor claims only, no official page read; caption links verified as a press report (Meta Verified test).
- Comment-DM conversion 12-30%: vendors disagree; no study.

## 11. Questions for Ricky, and gaps

1. Business or Creator account? It changes music access (Planoly claim only). Cross-ref w1a.
2. Does a DM carrying the listing link satisfy "reply LINK with the link, nothing else"? A public reply cannot be tapped.
3. Hollie: hands only, voiceover, or on camera? Formats 9 and 12 need a voice.
4. Pick DROP DAY; the teaser and "Gone" formats key off it.
5. Does Hollie approve every post, or by exception?

**Gaps:** no carousel or TikTok sample (carousel posts not reachable by yt-dlp or the search index); no follower counts or views, so no rates; Instagram help pages are walled, so no official page for comment-link behaviour or the hashtag cap; Meta Sound Collection and Business-account music rules unread; Ella Grace and Esthetic Vintage numbers cannot be tied to sales; the Vintage Seekers reel-ideas article is members-only (its URL now 404s).
