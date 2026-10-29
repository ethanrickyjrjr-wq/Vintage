# Holliewood & Vine Fabulous From Online: the hire-Hollie section

2026-10-28. Ricky's brief: a section where people hire Hollie to find items, or to decorate a corner, a room, or a whole studio or house. Clients meet by video, send photos, or describe what they want by email. Show ideas (parties, events, remodels, spare rooms). Offer in-person and "need it now" upgrades at higher prices. Lay out the page, set it up for Codex, and write "a really good quote".

**Occasion styling update, 2026-10-29.** Ricky requested distinct background colors
and expressive type, and rejected faint burgundy tints. Terra researched vintage
poster art; Sol specified and checked the contrast palette. The 15 occasion links
now use opaque emerald, saffron, coral, violet, rose, oxblood, cobalt, sage, ochre,
lavender, petrol, sea-glass, rust, raspberry and citron grounds. Alternating light
and dark cards sit on the existing burgundy page. The shop's Bodoni Moda, DM Sans
and Space Mono supply invitation italics, bold party lettering and camera/office
labels. Selected cards have invitation rules, camera corners or a record motif.

Visual references: Cooper Hewitt's [Edgardo Giménez poster collection](https://www.cooperhewitt.org/2022/06/22/an-avant-garde-argentine-edgardo-gimenez/)
for bold color and expressive typography, and [E. McKnight Kauffer's poster work](https://www.cooperhewitt.org/2015/04/03/laws-of-attraction/)
for geometric accents and block lettering. These inform the direction; no artwork
is copied. Browser measurements give minimum heading/body contrast of 4.99:1 and
4.92:1. The full fills stay unchanged in both themes and on hover; the gold keyboard
outline contrasts with the surrounding burgundy. All 33 tests, the build, desktop
and 390/320px browser checks passed; Lighthouse accessibility is 100. Both agents
reviewed the rendered design. Screenshots and audit outputs are in ignored
`artifacts/occasion-styling/`.

Evidence comes from six Sonnet reports in `research/fabulous-from-online/c1..c6-*.md`, with raw crawls in `raw/`. This page is the decision layer; the build spec is `docs/codex-handoff-fabulous-from-online.md`. Research, not legal or tax advice.

**What I re-checked myself against captured live pages.**
- Florida ch. 481, 2026 text from flsenate.gov (`raw/c5-ch481-all.md`):
  - 481.223(1)(b) "does not restrict the use of the name or title 'interior designer' or 'interior design firm'"; only "registered interior designer" and "architect" are barred.
  - 481.213(8): no registration is needed for decorator services.
  - 481.229(6)(a): the part "shall not apply to" interior design or decorator services "for any residential application".
- Cal.com pricing: Free is "Free forever" and lists "Accept Stripe & PayPal payments".
- Stripe pricing: "2.9% + 30¢", "No setup fees, monthly fees, or hidden fees".
- Tally: "The free plan supports individual files up to 10 MB".

Everything else is agent-reported from live pages and tagged in the reports.

## The quote

**Headline: "You bring the plot. Hollie dresses the set."** (c6's line.)
- It reads cold as the section's first line.
- It cashes the shop's own "do it for the plot" neon.
- "Set decorator" is a real film job (ScreenSkills: "Set decorators are storytellers"), so the metaphor is earned rather than pasted on.

Supporting lines:
- **"Pan slowly. Hollie has notes."** (c6's #1.) Perfect, but only once you know there's a video call, so it is the Screen Test card's line rather than the headline.
- **"Excellent taste. Now taking rooms."** (Claude's.) It echoes the owner section's "Excellent taste. Absolutely no offers." Use it only if the owner in that section is Hollie. Nothing in the repo says so; Ricky confirms.

Closing epigraph, verified from the primary text (Gutenberg, *The House in Good Taste*, 1913): "There never was a house so bad that it couldn't be made over into something worth while." Elsie de Wolfe.

Verified out: Iris Apfel's "more is more and less is a bore" (QI: nothing found; "less is a bore" is Venturi's), Mae West's "too much of a good thing" (unverified), and Chanel's "remove one accessory" (QI: misattributed).

One flag, for Ricky's eyes only: c6 liked "Not for sale. Very much for hire." as a callback to the owner photo's NOT FOR SALE ticket. It also noted that "for sale or hire" was 1800s wording in ads selling enslaved people. Claude's read: ordinary English, low risk, but not worth it as a headline. It is not in the build.

## Where it lives

**One homepage section, no new page.** Ricky said "section".
- The section sits directly after **Your room** (`#your-room`) and before the disco note.
- The room editor is do-it-yourself; this is the done-for-you answer to it.
- Its anchor is `#hire-hollie`, and a **Hire Hollie** link goes in the header, mobile and footer navs.
- Long parts (photo checklist, fine print) sit in native `<details>`, so the section stays short.
- No new CSS file, no new page, no `build.mjs` change.
- If the owner is Hollie, Ricky may prefer it right after the owner section with the callback eyebrow. That is a one-line move.

## Section layout (top to bottom)

1. **Eyebrow** "Holliewood & Vine Fabulous From Online" (Ricky's name, exactly), **H2** "You bring the plot. *Hollie dresses the set.*", then a one-paragraph lede. Beside it, a framed real photo from the original room (`IMG_6611`: feather hat, lace head, crystal) captioned "From the original room." There is no invented portfolio and no fake testimonials; the room is the portfolio.
2. **Three ways in** (c6 names; c1: no rival asks for a video walkthrough, so this is the differentiator):
   - **Screen Test**: video call. "Pan slowly. Hollie has notes."
   - **Stills**: send photos.
   - **The Logline**: describe it in an email. Free.
3. **The billing**, four tiers (c6 names, c1 prices):

   | Tier | Scope | Starting price | Basis |
   |---|---|---|---|
   | Casting Call | One find: a lamp, a mirror, the right chair | from $95, credited toward the piece | c1 one-question band $75–$180 (Black Cat $95); c2 local floor Vestige $50, Mercer $100, both credited |
   | Close-Up | A corner or section: shelf, bar cart, the spot by the door, a party table | from $295 | c1 Noeka tablescape $295, Sandringham vignettes $425, Black Brick $500 |
   | Leading Role | A room, including a spare room or the one after the remodel | from $750 | c1 independent band $450–$2,800; mid-band, because there is no 3D rendering step |
   | Full Production | A studio or the whole house | quoted by the room, 10% off each room after the first | c1 Decorilla "Save 10%" multi-room, verified |

4. **Two add-ons**:
   - **The Cameo** (in person): $150 an hour, two-hour minimum, or a $1,200 styling day.
     - c3: in-person hour at 1.5x virtual. Morel's $1,250 day is "6 working + 2 office hours".
     - c1: Havenly in-person $699 vs $199 online.
     - c2: BrandWhy $350 vs $175.
   - **Rushes** (need it now): +25% to start within a week, +50% within 48 hours, $75 minimum, on the service fee only, never on item prices.
     - +25% is where c1 and c3 agree. +50% is c3's freelance benchmark.
     - The $75 floor is c1's. c3's $250 floor would be 260% of a $95 Casting Call.
     - No styling vendor publishes a rush fee (c1, c3), so this price is a first guess; revisit after ten bookings.
5. **What's the occasion?** 15 chips. Each opens an email with the occasion in the subject. Pitches are c3's, trimmed to homes:
   - Cocktail hour, Dinner party, The party, Disco night, Bachelorette, Proposal, Photo set
   - After the remodel, Guest room, Spare room, Home office, Snowbird season, Reading nook, Gift a room
   - Something else ("Whatever it is, do it for the plot.")
6. **How it works**, five steps:
   1. The Logline.
   2. The Screen Test: a video call booked online (photos work too).
   3. Pay the billing online, then the board in 7–10 business days, with options labeled *From the collection* or *Sourced for you*, two rounds of changes.
   4. You approve each piece in writing and pay before Hollie buys anything sourced; collection pieces hold 48 hours.
   5. That's a wrap.

   Sources: c1 (revisions, turnaround), c2 (approval flow, Potomac's hold, Design Ink's "No written approval, no order").
7. **"Yes, Hollie sells things too."** The disclosure, drafted by c2 from the ADAA code (IV.B, V.D, V.E) and the BIID conflicts page. Nobody in vintage publishes one, which makes it a trust point.
8. **Photo checklist** (`<details>`, c4 from Havenly and two designers' intake pages):
   - a wide shot from the doorway
   - each corner
   - each wall face-on
   - daylight with lamps off
   - don't tidy
   - no wide-angle lens
   - rough measurements
   - keep / maybe / hard-no lists
   - a budget
9. **The fine print** (`<details>`, c5's terms checklist).
10. **CTAs**: **Email Hollie** (`mailto:` with a prefilled brief), **Book a Screen Test** (Cal.com link), the plain address under them, and the de Wolfe epigraph to close.

## Decisions settled across the reports

- **Homes only in v1.**
  - c5: residential work is exempt under 481.229(6)(a). DBPR's FAQ says commercial work needs registration, while the statute text has no such ban: statute verified, DBPR position needs review.
  - So c3's A-ranked boutique and salon storefronts, venue lounges and film-prop work stay off until an attorney or DBPR answers.
  - Bachelorettes, proposals and parties are at a home.
- **No rentals in v1.** c2 calls renting stock a separate product. c5 says tax on party rentals needs review. c3 has the terms ready (50% retainer, 48-hour period, 10% damage waiver) if Ricky says yes.
- **Book and pay online before any visit; no money changes hands in the client's home.**
  - The FTC Cooling-Off Rule covers buyer-invited home sales of $25+ (16 CFR 429.0(a)), and a "non-refundable" term cannot waive it (429.1(d)). Florida 501.045 is similar (c5).
  - Online booking keeps the upfront fee clean. How the rule treats a sale closed on a video call needs an attorney.
- **Rush only uses pieces already in the collection.**
  - Under 538.06, a secondhand dealer may not sell or *use* privately acquired goods for 15 days, or 30 for antiques, art and jewelry (c5, statute text from the prior capture).
  - A privately sourced lamp cannot be rushed into a client's home. Dealer-to-dealer buys may be exempt (538.03(2)(i)); needs review.
- **Fees are upfront; the Casting Call fee is credited toward the piece.**
  - Five of six shops that state it credit the fee (c2: Vestige, Mercer, Potomac, Zhiva, Coffee and Clothing).
- **If nothing is found, the fee becomes 90-day store credit.**
  - Four of five shops that say keep the fee (c2); only Mercer refunds.
  - This is a values call for Ricky; refunding is the alternative.
- **Sourced pieces carry a 10% sourcing fee on its own line; collection pieces are the listed price.**
  - c2: the verified range is 6.5% (Mercer) to 12% (BrandWhy).
  - c2 also cites the Virginia markup cases on that law-firm blog: secret markups are the lawsuit, so the page, the agreement and the invoice must say the same thing.
- **"Plus applicable sales tax"** on every price until a CPA answers.
  - c5: an advisory fee stated separately is untaxed (TAA 02A-014). Fees bundled with goods Hollie sells are taxed.
  - c2 found a Florida tax firm saying the same about design fees.
- **No disco-ball promise in any tier.** It stays a gift, per CLAUDE.md.

## Words: allowed and banned (c5's table, statute-checked above)

| Allowed | Banned |
|---|---|
| interior designer and interior design (for homes), designer, decorator, stylist, styling, e-design, space planning, placing, arranging, hanging art | "registered interior designer", "architect", "licensed", "certified" (unless true), "insured" (until a policy is bound), "contractor", "remodeling services", "install lighting", "hardwire" |

**In person means** placing furniture, hanging art and mirrors, setting lamps and styling. It excludes:
- electrical work, plumbing, or anything needing a permit
- hiring trades for the client (489.105(3), "by others")

The page says "styling and selections for your remodel", never "we handle your remodel".

## Intake on this stack (c4)

- **v1 (the build):**
  - `mailto:` links with a prefilled brief. RFC 6068 cannot attach files, so the page says to attach photos.
  - A plain Cal.com link for the Screen Test, opening in a new tab. Sites documents nothing about iframes, so no embed.
  - Hollie pastes a fixed-price Stripe Payment Link into the reply. The page itself takes no money.
- **v2:**
  - A Tally form link. It is the only free tool with no-login photo upload (10 MB per file).
  - Turn on Cal.com payments so the Screen Test is paid at booking.
- **v3:** a `/api/hire` route in the existing Sites Worker (`room-worker.mjs`, D1 bound as `DB`). It needs:
  - an email key (Resend or Postmark)
  - Cloudflare Turnstile with server-side verification
  - an R2 binding for photos (`hosting.json` has `"r2": null`)
  - a privacy policy

  Only if v2 proves demand.
- **Not on Etsy.** Etsy's Help Center says services are generally not allowed; the policy pages were walled. Shopify allows selling a service once a store exists.

## Ricky decides (a blank answer takes the default; without an inbox the section ships in demo state)

1. **The inbox address** for Email Hollie. Without it the section ships safely in demo state: the call to action reads "Booking opens soon", like checkout. The test fails only on a half-filled section.
2. **The Cal.com Screen Test link**, or none. With none, the Screen Test card says "Ask for one in your email".
   - **Screen Test price.** Free by default. If paid, turn on Cal.com's Stripe payments for that event and credit the fee toward the billing.
   - **Nav label.** "Hire Hollie" by default, or Ricky's own "Fabulous From Online".
3. **The starting prices** above: confirm or change. They will read as a real offer.
4. **Where Hollie is based and how far The Cameo travels.**
   - The copy assumes Lee and Collier counties included, with travel time billed beyond.
   - c3 suggested "free within 20 miles of base, $300 minimum".
5. **If nothing is found:** store credit (default) or refund.
6. **Rentals for parties:** no (default) or yes, using c3's terms.
7. **Is the owner in the owner section Hollie?** If yes, consider moving the section after it with "Excellent taste. Now taking rooms."
8. **Before money moves, outside the site:**
   - a Florida CPA on sales tax for fees bundled with goods
   - an attorney on the Cooling-Off Rule for video-call sales and on ch. 538 for buying as the client's agent
   - an insurance quote
   - a trademark search for "Fabulous From Online" (USPTO search was JS-walled; no result obtained)
