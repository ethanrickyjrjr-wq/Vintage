# c6: copy, the quote, and naming

Agent c6, accessed 2026-10-28. Raw captures: `research/fabulous-from-online/raw/c6-*.md`.
Method: SearXNG (`tools/search.sh`) for URLs, crawl4ai (`tools/crawl.sh`) for pages, WebSearch (fallback tool) for exact-phrase checks because SearXNG ignores quote marks. Tags: `verified` = read on a live page this session; `inferred` = my reasoning or common usage I did not source; `unverified` = not confirmed. Under-1 KB captures are walls or empty pages: `c6-avintagesplendor`, `c6-etsy-rush`, `c6-mcgee-virtual`, `c6-morris-life`, `c6-secretlives`, `c6-venturi-moma`, `c6-venturi-pdf`, `c6-variant-apfel2`, `c6-draper-dl` (401). Not a wall: the QI "Nothing Found" pages (`c6-qi-s-apfel`, `-draper`, `-navy`) and the empty Mae West page 2 mean Quote Investigator has no entry. One mis-fetch (a Gutenberg ID that turned out to be a different book) was deleted and is not cited. I did not run git.

## TL;DR

1. **#1 line: "Pan slowly. Hollie has notes."** It sells the service in five words (show Hollie the space on camera), is vain in the site's way, and uses the site's two-short-sentences pattern. Runners-up: "You bring the plot. Hollie dresses the set." and "The sofa can stay. The beige cannot." Full list of 20 and reasoning in section 6.
2. **The quote gap, stated plainly.** The two most on-brand famous lines fail the QI-or-primary rule: Iris Apfel's "More is more and less is a bore" (`unverified` as a first utterance; "less is a bore" is Robert Venturi, 1966, per secondary sources) and Mae West's "Too much of a good thing can be wonderful" (`unverified`, QI has no entry, a quote-tracing site calls it unsourced). `verified` and usable as an epigraph: Elsie de Wolfe, "There never was a house so bad that it couldn't be made over into something worth while" (primary text, 1913), and Diana Vreeland, "Lots of people have terrible taste, you know, and make a damn good living off of it" (QI). Chanel's "remove one accessory" is a misattributed anonymous adage (QI).
3. **Competitors run on the banned words.** A loose regex for the banned stems hit all 14 captures (2 to 10 hits each; some hits are nav or footer text, so read this as "the words are everywhere", not "every H1 uses them"). The strongest pages (Velvet Jungle, Find Good Studio, Spacejoy) win on personality in microcopy, product names that say what happens ("ONE HOUR VIDEO CHAT"), plain prices, and a low-risk first step. Avoiding the cliché vocabulary is itself the differentiator.
4. **Hollywood & Vine hands over the palette and the metaphor.** Walk of Fame stars are coral-pink terrazzo rimmed with brass (the shop's pink-and-brass), the Walk crosses at Hollywood and Vine (1960), and radio station KFWB was "broadcasting live from Hollywood and Vine" in the 1930s (a ready-made frame for Fabulous From Online). A set decorator is a real job whose official-ish description is "storytellers"; ScreenSkills lists "Stylist (commercials)" as an alternate title.
5. **Naming kit (keeps "Holliewood & Vine Fabulous From Online" exactly).** Tiers: **Casting Call** (one find), **Close-Up** (a corner), **Leading Role** (a room), **Full Production** (house or studio). Rush add-on: **Rushes** (British word for dailies, the footage reviewed the next day). In-person add-on: **The Cameo**. Free first step: **The Logline**. Ways to share the space: **Screen Test** (video call), **Stills** (photos), **The Logline** (email). Main button: "Hire Hollie".
6. **Collision check: no business found using "Fabulous From Online"** (two exact-phrase WebSearch queries plus three SearXNG queries; the only hit is a customer review fragment about a NZ car rental). USPTO TMSearch is a JS app that never ran my query, so there is **no trademark result**. This is not a clearance. No exact-phrase hits for my top 3 lines either (tag `inferred`, not proof of originality).
7. **One flag on honorable mention #4 ("Not for sale. Very much for hire.").** It is the best continuity joke with the owner section (the "NOT FOR SALE" ticket, "$10,000,000 Firm"), but "for sale or hire" is also the formula in 1800s newspaper ads for enslaved people (it surfaced in my search results from the Monticello archive). Probably fine as an inversion; Ricky should make that call knowingly.

---

## 3. Competitor headlines, verbatim

I read 14 service or e-design pages (12 detailed below, 2 more in the last line). Prices are what the page showed on 2026-10-28; several are promo prices.

| # | Business and URL | Headline / tagline / tier names, verbatim | Why it works or doesn't |
|---|---|---|---|
| 1 | **Velvet Jungle Interiors** https://velvetjungleinteriors.com/services/ (raw `c6-velvetjungle.md`, `c6-velvetjungle-home.md`) | "ONE HOUR VIDEO CHAT : During this hour chat, the floor is yours !" / "Show me around the space and let me know what you're working on, where you're stuck, and how I can help !" / home page menu: "1 hour chat 350$", "full consultation 650$", "design one room 1250$", "design multiple rooms 999$*" / "( PSST ... HAVE A BIGGER PROJECT ? )" / CTA "Book a Free Chat!" | Best structural match. The video call is a named, priced product. Tiers are plain nouns with prices. Multiple-rooms discount ("save 250 $ per room"). A free 15-minute chat is the low-risk door. Personality lives in the asides, not the H1. |
| 2 | **Find Good Studio** https://www.findgoodstudio.com/ and /ourservices | "A creative studio for the homeaholics." / "Think of me as your interior bestie. Part designer, part stylist, part vintage treasure hunter." / services "INTERIOR BESTIE CALL", "INTERIOR STYLING", "CUSTOM SOURCING" / "You dream it. I'll go find it." / "Think collected, not cluttered. Styled, not staged." / "Every space has potential . let's find yours." / "NOT SURE WHAT YOU NEED? That's totally fine." / button microcopy "LET'S FIGURE IT OUT TOGETHER", "I'M READY WHEN YOU ARE", "I CAN TRACK IT DOWN" | The closest category twin (advice call, styling, vintage sourcing). The button lines carry the voice. "Collected, not cluttered. Styled, not staged." is the two-short-sentences pattern. The home page also says "curated interiors for feel good living", the cliché Hollie should skip. Do not echo "You dream it. I'll go find it." |
| 3 | **Spacejoy** https://www.spacejoy.com/pricing | "Online Interior Design Pricing" / "A real designer and 3D designs of your own room, priced per room. First designs within 10 business days. Furniture is optional." / tiers "delight $199", "bliss $399 (Most chosen)", "euphoria $599" per room (list prices $399/$599/$799; a 40% Halloween code was running) / "Full refund within 48 hours of ordering" | One-word tier names that sound like outcomes, a "Most chosen" flag, a refund line. The model for tier naming. |
| 4 | **Wand Vintage** https://www.wandvintage.com/services/interior-designers/ | "Bring soul into your scheme." / "A friendly source for the design accents you need to make your scheme sing." / "No fees and no obligation to buy." / "Personal touch. Unique style." (search-result title: "Bespoke sourcing service for interior designers") | Eyebrow line is short and warm. "No fees and no obligation" kills the fear of starting. Business-to-designer, so tone is polite, not glam. |
| 5 | **Home Styling by Alexis** https://homestylingbyalexis.com/virtual-interior-design/ | "I'll meet you virtually in the room you want designed for a flat fee using ZOOM or FACE TIME. The results are THE SAME as if I physically went into your home." / "1 Room $750 excluding the cost of furniture/décor" / "Packages are sold in ten hours increments" | Names the method (Zoom/FaceTime), a flat fee, and what is excluded. No flourish, total clarity. |
| 6 | **Havenly** https://havenly.com/ | "Your dream home starts here." / "We see good design in your future." / "DO IT WITH ME" (Online, ~~$199~~ $89) / "DO IT FOR ME" (In-Person, ~~$699~~ $299) / "The white-glove option. Your designer comes to your home and handles everything from layout to sourcing." | Weak voice, but the two-door structure (online versus in-person) is the same shape as Hollie's base service versus the in-person add-on. Do not echo "DO IT FOR ME". |
| 7 | **Michele Safra Interiors** https://michelesafra.net/e-design/ | "Luxury at the click of a button" / tiers "Jump Start $450-$1500", "Full Service $950-$2800", "One Question Consult" | The tagline is five words with a contrast in it. "One Question Consult" is a nice cheap entry tier. |
| 8 | **A Thing For Styling** https://www.athingforstyling.com/ | "Design Your Home. Live Beautifully Every Day" / "IS THIS YOU?" / "One wrong choice feels expensive. So you pause. Then you get stuck. And the room never feels finished." / "1-Upload", "2. Receive", "3. Shop" / "Send your photos and fill out our quick questionnaire." / "No budget minimum." / "STYLING & DECORATION", "ROOM TRANSFORMATION" | The strongest short-sentence rhythm of the set ("So you pause. Then you get stuck."). Three-verb process. Uses "Transformation" in a tier name, which Hollie should skip. |
| 9 | **The Findery Market, Personal Shopper** https://thefinderymarket.com/pages/personal-shopper | "your exclusive pass to a world of curated vintage treasures tailored just for you" / "Submit your dream item" / "Sit back and relax" / "Happy dance time" / "let The Findery Market be your personal shopper extraordinaire." | Weak copy (exclamatory, templated, two banned words) but the four-step find flow (submit, hunt, notify with photos and price, handle delivery) is exactly the Casting Call flow. |
| 10 | **Studio McGee, Full Service** https://studio-mcgee.com/work-with-us/full-service | "A start-to-finish design process for new builds and large-scale renovations." / "Working on something smaller?" / "collected rather than matched" / process "01 | DISCOVERY, 02 | CONCEPT, 03 | DESIGN AND DOCUMENTATION, 04 | PROCUREMENT & INSTALLATION" | The big-firm template; useful as the "whole house" shape. "Working on something smaller?" is a clean way to route people down a tier. "Collected rather than matched" agrees with the site's "Nothing matches." |
| 11 | **J. Miles Design** https://jmilesdesign.com/ | "Beautiful, Livable Spaces Without the Stress" / "Your Dream Home, Simplified" / "DON'T WANT TO PAY HIGH INTERIOR DESIGNER PRICES?" / packages "new build & renovation package", "full house decor package", "À la carte rooms" | The generic baseline. Shows the cliché "dream home" is the category default. |
| 12 | **Debora Interiors, Single Room** https://deborainteriors.com/services/single-room/ | "Single Room Interior Design" / "Transform any room into your dream space" / "Starting at $600 per room" / "Book Free Consultation" | Same: clear price and a free consult, zero personality. |

Also read, not itemized: Stellar Interior Design (https://www.stellarinteriordesign.com/design/; "Room Design Package #1: $475", "#2: $575", "Paint Color Consultation: $95") and Porche & Co. (https://porcheandco.com/edesign; "Hello, Emily here!", "XOXO, Emily & Team").

**What the strong ones share** (`inferred` from the above):
- The product is named by what the customer does, in plain words ("ONE HOUR VIDEO CHAT", "Send your photos").
- Voice lives in button text and asides, so the offer stays readable.
- A free or low-commitment first step, with "not sure what you need?" as a door.
- Sentences are short and stacked: "So you pause. Then you get stuck." / "Styled, not staged."
- Prices and exclusions are stated. Price anchors seen: 1-hour video consult $350 (Velvet Jungle); one room $600 (Debora), $750 (Alexis), $1,250 (Velvet Jungle), $199 to $599 (Spacejoy, promo-affected); whole-room e-design up to $2,800 (Safra). I found **no rush or expedite add-on** on any page I read. A search-result title shows an Etsy "Rush Design Upgrade" listing, but the page was walled (`unverified`).

---

## 4. Quote verification

Rule applied: Quote Investigator or a primary source only. Goodreads, BrainyQuote, AZQuotes, Quotle, brand blogs, magazine obituaries and House Digest are secondary and can't make a quote `verified`; they are noted as leads.

**Discrepancy report: Morris, de Wolfe (two lines), Vreeland (terrible taste) and the Chanel adage are verified; Apfel, Mae West, Draper's fragment, Baldwin and "pink is the navy blue of India" need review.**

| Quote | Attributed to | Status | Source URL |
|---|---|---|---|
| "Have nothing in your houses that you do not know to be useful, or believe to be beautiful." | William Morris | **verified (primary text)**. The 1882 book text reads "HAVE NOTHING IN YOUR HOUSES THAT YOU DO NOT KNOW TO BE USEFUL OR BELIEVE TO BE BEAUTIFUL." (no comma) in one place and "...WHICH YOU DO NOT KNOW..." in another, so the popular version has a comma and one "that" added by editors. Lecture date not confirmed in my read (`unverified`). Stern; the loophole is "believe to be beautiful". | https://www.marxists.org/archive/morris/works/1882/hopes/chapters/chapter3.htm (*Hopes and Fears for Art*, ch. 3, "The Beauty of Life") |
| "When I am asked to decorate a new house, my first thought is suitability. My next thought is proportion. Always I keep in mind the importance of simplicity." | Elsie de Wolfe | **verified (primary text)** | https://www.gutenberg.org/files/14715/14715-h/14715-h.htm (*The House in Good Taste*, 1913, ch. II) |
| "There never was a house so bad that it couldn't be made over into something worth while." | Elsie de Wolfe | **verified (primary text)**, same book, introduction. Best on-topic epigraph for remodels and spare rooms. | same Gutenberg URL |
| "I am going to make everything around me beautiful" | Elsie de Wolfe | **unverified**. Search-result leads only (Goodreads, AZQuotes); likely from her 1935 memoir, which I did not read. | lead: https://www.goodreads.com/quotes/51441-i-am-going-to-make-everything-around-me-beautiful-- (not accepted) |
| "Lots of people have terrible taste, you know, and make a damn good living off of it." | Diana Vreeland | **verified (QI)**, from her 1980 book *Allure* | https://quoteinvestigator.com/2024/11/09/terrible-taste/ |
| "Elegance is refusal." | Diana Vreeland (often also Chanel) | **verified as Vreeland's usage, not her coinage**: she said "I don't know who it's a quote from... I didn't make it up." QI "found no substantive evidence that Coco Chanel employed this statement." | https://quoteinvestigator.com/2024/11/01/elegance-refusal/ |
| "Pink is the navy blue of India." | Diana Vreeland | **unverified under the rule** (QI search: Nothing Found). Strong lead: a peer-reviewed journal footnote quotes her memoir *D.V.* (1984; 1997 ed., p. 106): "though it's so *vieux jeu* I can hardly bear to repeat it, pink is the navy blue of India", and cites *Time*, 10 May 1963. She herself calls it tired. | lead: https://www.fashionstudies.ca/fashion/photo/film (footnote 8) |
| "The eye has to travel." | Diana Vreeland | **verified only as the title** of the documentary *Diana Vreeland: The Eye Has To Travel*. Where she first said it: **unverified**. | https://www.dianavreeland.com/the-eye-has-to-travel |
| "More is more and less is a bore." | Iris Apfel | **unverified as a first utterance; misattributed if sold as her coinage.** QI: Nothing Found. Vogue's obituary reads it as hers ("as she would have put it"); "less is a bore" is Robert Venturi's retort to Mies's "less is more" in *Complexity and Contradiction in Architecture* (1966) per Metropolis (both secondary; the book itself I could not open). Local collision: The Kitschy Maximalist's hero already says "More is more, more or less." (from a2). | https://www.vogue.com/article/iris-apfel-obituary ; https://metropolismag.com/profiles/robert-venturi-obituary/ |
| "Too much of a good thing can be wonderful." | Mae West | **unverified**. QI's Mae West category lists 8 entries (one page) and this isn't one. Quotle calls it "Unsourced" and says the 1959 memoir *Goodness Had Nothing to Do with It* claim is unconfirmed; it inverts the old proverb. | https://quoteinvestigator.com/category/mae-west/ ; lead: https://quotle.info/who-said/too-much-of-a-good-thing-can-be-wonderful/ |
| "Decorating Is Fun!" | Dorothy Draper | **verified as a book title** (republished with an introduction by Carleton Varney; the 1939 date comes from House Digest, secondary). | https://www.simonandschuster.com/books/Decorating-Is-Fun!/Dorothy-Draper/9780985225629 |
| "If it looks right, it is right." | Dorothy Draper | **unverified**. QI: Nothing Found. House Digest (secondary) says it's from *Decorating Is Fun!*; the archive.org full text returned 401. | lead: https://www.housedigest.com/2229874/quote-of-the-day-dorothy-draper-decorating-meaning/ |
| "First and foremost, furniture must be comfortable. That is the original purpose of it, after all." | Billy Baldwin | **unverified** (a brand-run bio quotes it; primary not read). Same bio: his "pet aversions were jumble and clutter", the wrong team for this shop. | lead: https://billybaldwinstudio.com/billy-baldwin |
| "Before you leave the house, look in the mirror and remove one accessory." | Coco Chanel | **misattributed** (QI): an anonymous adage circulating by 1949, originator unknown; even Chanel biographer Karen Karbo says "She may or may not have said" it. Closest verified Chanel: *Time*, 22 Aug 1960, "One always begins by making dream dresses. Then one has to take away something. Always to take off, never to add." | https://quoteinvestigator.com/2023/02/02/jewelry/ |

**Epigraph recommendation (alternate to an original headline):** de Wolfe's "There never was a house so bad that it couldn't be made over into something worth while." (`verified`, 1913 so almost certainly public domain, `inferred`). Second choice Vreeland's "terrible taste" line (`verified`, credit her and *Allure*, 1980; mildly insulting to clients if misread). Third Morris. If Ricky insists on Apfel or West, it has to be labeled "attributed to".

---

## 5. Hollywood & Vine facts and film vocabulary

### Facts (all `verified` as read on the cited page; Wikipedia is a secondary source, so spot-check before print)

| Fact | Source |
|---|---|
| Hollywood and Vine is the intersection of Hollywood Boulevard and Vine Street in Hollywood, California; it "became known in the 1920s for its concentration of radio and movie-related businesses". | https://en.wikipedia.org/wiki/Hollywood_and_Vine |
| The area was a lemon grove until 1903. | same |
| In the 1930s radio station KFWB spoke of "broadcasting live from Hollywood and Vine", and columnists Hedda Hopper and Jimmie Fidler "regularly touted the intersection's mystique". | same |
| In 1960 the intersection became the crossing point of the t-shaped Hollywood Walk of Fame; the Apollo 11 astronauts' shared markers sit "at all four corners". | same |
| It's often used in songs and films "as a symbol of the area's lure for dreamers and for its decadence and disappointments". | same |
| Corner buildings: Capitol Records Building (1956, "the world's first circular office building"), Hollywood Pantages Theatre (Art Deco, 1930), Taft Building (1923, 12 stories; every studio had offices there), Hollywood Brown Derby (demolished 1994). Named "Bob Hope Square" on 29 May 2003. | same |
| Walk of Fame stars are "five-point, coral-pink terrazzo rimmed with brass" on a charcoal terrazzo square; more than 2,800 stars; six categories (motion pictures, television, recording, radio, live theater/performance, sports entertainment). First stars unveiled 1958, first permanent stars 1960. | https://en.wikipedia.org/wiki/Hollywood_Walk_of_Fame |
| Not found: a sourced origin for the "discovered at the corner of Hollywood and Vine" lore. I did not find a citable version, so treat the story as `unverified` and don't print it. | n/a |

**Wordplay seeds** (`inferred`): the corner/intersection (Hollie styles corners); a pink-and-brass star on the sidewalk is the shop's palette in terrazzo; "broadcasting live" is a video call; "Hollie" plus "-wood" reads as the Hollywood pun the shop name already makes. Keep "Hollywood" for the place and industry and never for the shop.

### Film vocabulary that fits a styling service

| Term | In film | Maps to | Status |
|---|---|---|---|
| Set decorator / set dresser | Set decorator is "the head of the set decoration department" responsible for "the creative vision of the interior design and set elements". ScreenSkills: "Set decorators are storytellers. They create the background of the action, explaining the context, adding mood and visual interest"; "Also known as: Set dec, Set dresser, Stylist (commercials)"; they "buy or hire the items" and dress the set. | Hollie's whole job | verified (https://en.wikipedia.org/wiki/Set_decorator ; https://www.screenskills.com/job-profiles/browse/film-and-tv-drama/craft/set-decorator/). ScreenSkills is UK usage; in the US the decorator heads the department and dressers work under it (`inferred`), so "set decorator" is the safer public term. |
| Art department | "the section of a production's crew concerned with visual artistry... responsible for arranging the overall look of the film" | The studio as a whole | verified (https://en.wikipedia.org/wiki/Art_department) |
| Screen test | "a method of determining the suitability of an actor... to perform on film"; the performer is put in front of a camera; also checks chemistry between two actors | The video call: Hollie sees the room on camera; chemistry check between client and Hollie | verified (https://en.wikipedia.org/wiki/Screen_test) |
| Casting | choosing who plays the part | Finding the one piece for the part | inferred |
| Cameo | "a brief guest appearance of a well-known person" | Hollie turning up in person | verified (https://en.wikipedia.org/wiki/Cameo_appearance) |
| Dailies (rushes) | footage shot the previous day, reviewed the next; glossary index lists "Dailies (rushes)" | The rush add-on, with daily progress updates | verified (https://en.wikipedia.org/wiki/Glossary_of_motion_picture_terms) |
| Call sheet | the schedule telling cast and crew "when and where they should report", listed by call time | The project schedule; "top of the call sheet" for rush | verified (same glossary) |
| Wrap | "That's a wrap" signals the end of filming, in use since the 1920s; followed by a wrap party | The reveal day | verified (https://en.wikipedia.org/wiki/Wrap_(filmmaking)) |
| Location scout | the search for a suitable place outside the studio | An in-person visit, or a sourcing trip | verified (https://en.wikipedia.org/wiki/Location_scouting) |
| Close-up, premiere, leading role, final cut, director's cut | common film terms | corner, party or event reveal, main room, last revision, last revision | inferred (not sourced this session) |

---

## 6. Candidate lines and favorites

Pattern from the site (all `verified` in `site/storefront.html`): "Good taste. Bad influence." / "Nothing matches. Everything belongs." / "Your room. Our kind of character." / "Collector of good things. Excellent taste. Absolutely no offers." Short phrase, then a twist, a little vain. No banned words used below.

### 20 candidates

| # | Line | Plays on |
|---|---|---|
| 1 | Pan slowly. Hollie has notes. | video call |
| 2 | You bring the plot. Hollie dresses the set. | "do it for the plot", set dresser |
| 3 | The sofa can stay. The beige cannot. | works with what you own, "Nothing matches" |
| 4 | Not for sale. Very much for hire. | owner section (see TL;DR 7) |
| 5 | Send the worst corner. Hollie has seen worse. | photos, vanity |
| 6 | Give Hollie a corner. Get back a scene. | corner tier |
| 7 | Hollywood has set decorators. You have Hollie. | Hollie/Hollywood pun |
| 8 | Hollywood has the sign. Holliewood has the sofa. | Hollie/Hollywood pun |
| 9 | Your room has been miscast. Hollie recasts. | casting |
| 10 | Do it for the plot. Hollie does the rest. | neon |
| 11 | You bring the beige. Hollie brings the brass. | palette |
| 12 | Photos in. Glamour out. | photo path |
| 13 | Fabulous From Online. Pants optional. | video call, name (wildcard) |
| 14 | Fabulous From Online: all the taste, none of the commute. | name |
| 15 | Fabulous on screen. Devastating in person. | in-person add-on |
| 16 | Bad lighting? Hollie can see it from here. | video call |
| 17 | Your room is still understudying. Give it the lead. | leading role |
| 18 | A set dresser for your actual life. | set dresser |
| 19 | Lights. Camera. Hollie. | film pun (crowded) |
| 20 | Hire the taste you can't take home. | owner section: "The only thing you can't take home." |

### The 3 favorites

1. **"Pan slowly. Hollie has notes."** Explains the product (show Hollie the room on a video call) without saying "virtual", names Hollie as the authority, and the second sentence is the vanity joke the site already runs ("Absolutely no offers"). It's five words, so it fits a headline and survives mobile. Pronoun-free. Exact-phrase WebSearch: no hits (`inferred` originality).
2. **"You bring the plot. Hollie dresses the set."** Splits the work cleanly (the client has the story and the room; Hollie does the visuals), pays off the "do it for the plot" neon, and uses a real, sourced job title (set decorator, 5.). Possible weak spot: "You bring the ___" is a common sentence frame, so the exact-phrase check with Hollie in it is the one that matters; WebSearch on the fragments found nothing (`inferred`).
3. **"The sofa can stay. The beige cannot."** Says in one breath that Hollie works with what the client already owns and has a point of view, and sets up "Nothing matches. Everything belongs." as the philosophy. It reads like a verdict, which suits the owner's voice. WebSearch: no hits (`inferred`).

Honorable mention, with a flag: **#4 "Not for sale. Very much for hire."** Strongest tie to the page's existing owner gag, if the new section sits near it. See TL;DR 7 on the phrase "for sale or hire".

Not recommended: #19 ("Lights. Camera. Hollie.") because film puns of this shape are everywhere; #13 stays a wildcard only.

---

## 7. Naming proposals

**Overall service.** Keep exactly: **Holliewood & Vine Fabulous From Online**. Alternates only: "Hollie On Call"; "The Remote Set Dresser"; or as a small credit line beneath it, "A Holliewood & Vine Production" (adds the film frame without touching the name). Section eyebrow options: "Now casting: your room." / "Hollie, on call." (site eyebrows are short phrases).

**Tiers** (film-themed, each with a one-line subhead; no prices proposed because none were given):

| Tier | Scope | Subhead |
|---|---|---|
| **Casting Call** | A single find | Tell Hollie the part. Hollie finds the piece to play it. |
| **Close-Up** | A corner or section (a shelf, a wall, a bar cart, the spot by the door) | One corner gets all the attention: the lamp, the art, the attitude. |
| **Leading Role** | A whole room (living room, bedroom, spare room, a remodel) | One room, top billing: layout, color, lighting, the lot. |
| **Full Production** | An entire studio or house | Every room, one vision, no continuity errors. |

Optional fifth, if Hollie wants a paid entry rung like Velvet Jungle's $350 hour or Find Good Studio's "Interior Bestie Call": **Screen Test**, a standalone video call with no project attached. The call is otherwise just the way a client shares the space.

**Ways to share the space** (one phrase each):
- **Screen Test**: a video call; show Hollie the room.
- **Stills**: send photos.
- **The Logline**: describe it in an email.

**Use-case chips** (`inferred`, playful): Parties = Premieres; Events = Opening Night; Remodels = Remakes; Spare rooms = Spin-offs.

**Add-ons:**
- **Rushes** (rush). Subhead: Need it fast? Hollie moves you to the top of the call sheet. Rationale: "rushes" is the British word for dailies (`verified` in the glossary index), the footage turned around overnight; double meaning with "rush job". Tie-in: daily progress updates until wrap.
- **The Cameo** (in person). Subhead: Hollie, in person, for a brief and glamorous appearance. A cameo is a brief appearance of a well-known person (`verified`). Alternate: **On Location**.

**Free first step (email).** **The Logline**. Subhead: Free. Describe the room in a sentence or three, or attach photos, or just rant. Alternates: "Describe It", "The Pitch".

**CTA buttons:**
- Primary: **Hire Hollie** (plain, clear; alternate "Cast Hollie")
- Free email: **Send the Logline**
- Video call: **Book a Screen Test**
- Photos: **Send Stills**
- Add-ons: **Add Rushes**, **Add the Cameo**
- Form submit button: **Do it for the plot**
- Keep the clever labels on secondary buttons, with a plain-words line under each (`inferred` from the competitor pages: the clear words carry the offer, the voice rides in the microcopy).

---

## 8. Collision check results

| Phrase | Method | Result |
|---|---|---|
| "Fabulous From Online" | SearXNG, 3 queries (SearXNG did not honor the quotes: it returned dictionary pages) | no business found |
| "Fabulous From Online" | WebSearch exact phrase, 2 queries (one with interior/styling/vintage terms) | no business, service or trademark found. Near-misses are unrelated: a 2010 Philstar piece about an online clothing shop ("Fabulous finds at your fingertips"), a food-mix maker on Faire, a Snapchat seller. |
| Stray hit | crawled https://www.nzrentacar.co.nz/about-us/ | the "fabulous from online" string is a customer review sentence ("fabulous from online search through to dropping off"), not a brand use. `verified` |
| Related brands | SearXNG hits | "The Fabulous" habit app (https://www.thefabulous.co/) and fabulous.com are different goods; I did not read them. Not a conflict I can judge. |
| USPTO TMSearch (https://tmsearch.uspto.gov) | crawled with the phrase in the URL | **JS-walled.** The page loaded the app shell and showed "0 results for" with a blank query: the URL parameter was not honored and no search ran. **No trademark result obtained.** Recommend Ricky (or a lawyer) run the search by hand; interior design services and retail are the likely classes (`inferred`: 42 and 35). I am not giving legal advice. |
| "Pan slowly. Hollie has notes" | WebSearch exact | no hits (`inferred` originality) |
| "You bring the plot. Hollie dresses the set" | WebSearch, fragments plus "interior stylist" | no hits; the result page was set-decorator job descriptions (`inferred`) |
| "The sofa can stay. The beige cannot" | WebSearch exact | no hits; only beige-sofa shopping pages (`inferred`) |
| "Not for sale. Very much for hire." | WebSearch exact, 2 forms | no hits as a brand line; results are dictionary entries, legal "for hire" text and the 1820 "for sale or hire" newspaper item from Monticello (TL;DR 7) |

Caveat: "no hits" from a search engine proves little. It means I didn't find the phrase, not that it's unused. Any line Hollie prints with the name "Hollie" in it is unlikely to collide verbatim, which is a point for lines that name Hollie.
