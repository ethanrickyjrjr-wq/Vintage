# b5: Consign / Sell-to-Us process: intake, agreement, Florida + tax guardrails

**RESEARCH, NOT LEGAL OR TAX ADVICE. Confirm every item with a Florida attorney and a CPA before you build or sign anything.**
**Florida is an ASSUMPTION** (brief says Ricky's other work is Lee County FL; the shop's state is not stated anywhere). If the shop is elsewhere, section 3 and the FL parts of section 4 do not apply as written; sections 1 and 2 still do.
Researched 2026-10-27 by agent b5. Raw fetches: `research/consignment/raw/b5-*`.

## TL;DR

1. In Florida, **consigning is a regulated act by itself**, not just buying: ch. 538 defines "Acquire" as "to obtain by purchase, consignment, or trade" and a "secondhand dealer" as someone "engaged in the business of purchasing, consigning, or trading secondhand goods." Registration with Dept. of Revenue, a government-ID check, thumbprint, photos, a 24-hour report to police, and a 15- or 30-day no-sell hold all attach to consigned goods.
2. **Scope is your biggest lever.** The statute's "secondhand goods" definition excludes clothing, costume jewelry, books, coins, office furniture. So 70s-90s fashion and costume jewelry are likely outside ch. 538; lighting, glassware, art, furniture, fine jewelry, and probably signed memorabilia are inside. (Whether Playboys count as "books" is unclear: attorney question.)
3. **The "items are left at consignor's risk" clause every shop uses may be unenforceable for art in Florida:** s. 686.503(2) says the consignee "shall be responsible for the stated value of the work of art in the event of the loss of or damage to such work of art," and s. 686.502(3) puts sale proceeds "in trust." "Art" there includes prints, photographs, glass and pottery craft work.
4. **Tax:** Florida's consignee (you), not the consignor, collects sales tax (Rule 12A-1.081). The 1099-K $20,000 / 200-transaction threshold is about what Etsy/Shopify report on *you*, and card processors report to you with no threshold. Your 1099-K gross will include the consignors' share. The 1099-NEC/MISC threshold is now $2,000, and the IRS lists "payments for merchandise" as not reportable, which probably covers consignor payouts: CPA to confirm.
5. Blunt opinion: for a one-person online shop, **hard-goods consignment is a compliance machine** (registration, premises inspection, trust accounting, holding periods). Start buy-only plus soft-goods consignment; make hard-goods consignment invite-only after you are registered.

---

## 1. Real examples: intake, agreements, policy pages (7)

None of these exposed a field-level intake form in crawlable text. Evidenced fields are quoted below; the field list in section 6(b) is **synthesized**, not copied.

### 1.1 Arcadian Consignment, Vintage & Antique Co. (State College, PA). Closest match to your stock
- Homepage: https://arcadianconsignment.com . Page read: https://arcadianconsignment.com/consignment-contract/ . Accessed 2026-10-27. Raw: `raw/b5-arcadian-contract.md`.
- Takes: furniture of all eras, rugs, lamps ("Must come with shade"), artwork, pottery, linens, jewelry, barware, dinnerware, vinyl, clocks, vintage toys. Refuses: cribs/high chairs/car seats, mattresses, broken items, torn upholstery, stained fabric, dirty items.
- Commission: "Arcadian Consignment will remit 50% of the selling price to the consignor, less fees for cleaning or repair."
- Term and markdowns: "The consignment term is 90 days... not sold in thirty (30) days will be marked down 10%... sixty (60) days... 20%... ninety (90) days... 30% from original price."
- Pricing control: "The initial selling price for consigned merchandise is established by Arcadian Consignment."
- Early pickup: "Items picked up prior to end of 90-days sales period will be subject to a 25% of initial sales price service fee."
- Unsold: consignor has "five (5) days to remove item"; after that "it/they become(s) the property of Arcadian Consignment and can be sold or donated to charity." "Reminders regarding this timeline will not be sent."
- Payout: checks mailed monthly "within thirty (30) days of the selling date"; "Checks not cashed within ninety (90) days will not be re-issued"; $2 per payout fee; shop credit "at any time."
- Liability: "Arcadian Consignment is not responsible to insure the item(s) against damage or theft while they are in Arcadian Consignment's possession."
- Receipts: consignor "may request a Merchandise Receipt"; shop "cannot be held liable for losses resulting from incomplete or inaccurate information on the Merchandise Receipt."
- Steal: the 30/60/90 = 10/20/30% markdown ladder, the "must come with shade / working battery" acceptance rules, the not-accepted list. Watch out: the lost-cash-forfeiture and abandonment clauses (see risks), and the liability clause vs. s. 686.503(2) for art.

### 1.2 Cloud Nine Designer Consignments (Westport, CT)
- Homepage: https://www.consigncloud9.com . Page read: https://www.consigncloud9.com/pages/consignor-contract (rev. 02/14/24). Accessed 2026-10-27. Raw: `raw/b5-cloudnine-contract.md`.
- Commission: "50/50* split"; "If the items require work... we will do it and pay the consignor 40%."
- Term: "90 day term"; "Call/email to pick up unsold items before 97th day"; after that items are "abandoned" and "become the property of Cloud Nine"; "no payment on items sold after the 97th day."
- Pricing: "Cloud Nine will determine the selling price of each item"; "We reserve the right to take periodic markdowns and run sales at any time without notice."
- Payout: check min $50 less $4 fee; Venmo/PayPal min $25 less $1 fee; store credit no fee; auto-paid quarterly, "available on a daily basis upon request."
- Liability: "Cloud Nine will not be held liable for damages due to any reason such as loss, fire, theft, accident, etc. All items are left at consignor's risk."
- Authenticity: "We guarantee authenticity of every item and when in doubt, it will not be accepted or by mutual agreement, we will have the piece third-party authenticated... minimum being $15" deducted from account; "you are agreeing to not knowingly offer us counterfeit merchandise."
- Steal: the consignor-pays-for-authentication-with-consent mechanism; consignor login to see balance; the short fee schedule at the top of the contract. Watch out: do NOT copy "we guarantee authenticity" for vintage; you cannot back it on one-of-one pieces.

### 1.3 Generations Antiques and More (North Royalton, OH). Antiques, closest legal-shape agreement
- Homepage: https://www.generationsantiquesandmore.com . Document read: https://www.generationsantiquesandmore.com/uploads/1/3/6/1/13618050/generations_consignment_agreement.pdf (2 pages; fetched with curl, text extracted with pypdf because crawl4ai returned 4 bytes for the PDF). Accessed 2026-10-27. Raw: `raw/b5-generations-antiques-agreement.pdf` and `.txt`.
- Fields on the form: Consignor name, address, phone, email, "Consignor Identification," "Contract Starts," "Contract Ends," "Last Pick up Date (Mark this date on your calendar)," plus an attached inventory sheet.
- Warranty: consignor "warrants, represents and attests that he/she is at least 18 years of age, is the owner of all goods consigned... and has the legal right to enter into this Consignment Agreement; that the goods are saleable and/or free & clear of liens, loans, legal proceedings or other ownership encumbrances."
- Term: "The consignment period shall be 60 days."
- Two commission options: "Option A 50/50 split... will not allow Generations to accept any offers lower than the asking price"; "Option B 60/40 split... accept offers from buyers that are 80% or greater of the asking price."
- Markdown: "All prices are subject to a 30% reduction on day 45."
- Appraisal disclaimer: "Generations is not a certified appraiser of antiques and/or collectibles."
- Online: "Generations reserves the right to attempt to sell any item through any internet source. Any and all proceeds above the store tag price shall be added to the proceeds of Generations."
- Early removal: fee of "15% of the asking sale price."
- Payout: "on the 10th of each month for the previous month's sales for balances over $25"; pickup in person or store credit; "$1.00 mailing fee"; "Payments not picked up after 3 months will be expired and forfeited."
- Unsold: seven calendar days to pick up, one calendar day's notice required; after that "abandoned and become the sole property of Generations and may be disposed of or donated to any charity."
- Liability: "Generations maintains fire and liability insurance coverage only... items are left at the consignor's risk... not responsible for any loss due to damage, theft, fire, water, casualty or natural disaster."
- Cleaning: "a fee up to $10" deducted from the consignor's share.
- Tracking: sales tracked in a shared Google Doc.
- Steal: the 18+/owner/no-liens warranty block, the Option A / Option B price-flexibility split (a clean way to price "firm" vs. "will negotiate"), the appraisal disclaimer, the inventory sheet attached to the agreement. Watch out: the internet clause as written lets the shop keep the upside above tag; with an agent relationship (s. 686.502(1) makes the consignee "the agent" for art) that is a fiduciary-duty fight waiting to happen.

### 1.4 Season 2 Consign (online, ship-in model; Florida location INFERRED)
- Homepage: https://season2consign.com . Page read: https://season2consign.com/pages/how-to-sell-with-season-2-consign . Accessed 2026-10-27. Raw: `raw/b5-season2-consign.md`.
- Location: page links `.../season-2-consign-west-palm-beach-headquarters`; Florida is **inferred from that URL slug**, not read on a page.
- Intake: "1. Submit Your Item/s. It takes less than 30 seconds to upload photos and details securely through our online portal. 2. Accept Estimate & Ship... provide a fair market value... Accept & ship with our complimentary label. 3. We Work & You Get Paid."
- Commission tiers (verbatim table): $0-$499 = 50%; $500-$1499 = 40%; $1500+ = 30%.
- Payout: "paid electronically on the 10th day of the month after the item sells."
- Unsold: "Items unsold after 90 days may be returned to you upon request. Items are considered abandoned on the 91st day after the initial agreement term is complete."
- Authentication: "Every item undergoes a multi-step verification process... Counterfeits incur a $250 fee."
- Steal: the 3-step online intake (photos + details, estimate, prepaid label) and descending commission tiers. This is the only example that fits a web-first shop. Watch out: for Florida hard goods, a mail-in model collides with the in-person ID/thumbprint record (section 3). Soft goods only, or use the statute's online carve-out, which has strings.

### 1.5 Crossroads Trading (buy/sell/trade, national chain). ID and payout-mix reference
- Homepage: https://crossroadstrading.com . Page read: https://crossroadstrading.com/buy-sell-trade-2-2/ . Accessed 2026-10-27. Raw: `raw/b5-crossroads-bst.md`.
- "Must be 18 (or accompanied by an adult) & present a valid photo ID to sell." The ID-copy rationale appears only inside a link's text-fragment URL to their privacy policy ("we are required to maintain a copy of Your government ID to comply with local and state regulations governing resale businesses"); I did not read the privacy-policy page itself, so treat as secondhand.
- Payouts: "We pay 25-40% based on what we price your items to sell for" in cash; "45% in trade"; consignment "on your high-end designer items, with payouts up to 70% in cash."
- Drop-off: "complete a brief form and be on your way"; payout after "48-72 hours"; "sellers must return to collect their unpurchased items within 3 days or choose to have them donated."
- Mail-in: "Request a bag and we'll send you a roomy one with a pre-paid return shipping label."
- Steal: cash-vs-credit payout spread (credit pays more, keeps money in your shop), the "waitlist/drop-off with brief form" pattern. Watch out: this is a high-volume clothing buyer, not a one-of-one curator.

### 1.6 Hello Vintage ("Sell to Us" page, buy-only)
- Homepage: https://www.hellovintage.com . Page read: https://www.hellovintage.com/pages/sell-to-us . Accessed 2026-10-27. Raw: `raw/b5-hellovintage-sell-to-us.md`.
- Process: "We buy in person by appointment if local, or remotely if you're willing to ship. Send us an e-mail with a brief description of what you are selling, along with any photos you'd like to share."
- Era wish-list by decade (1920s-1990s) with specific garment types.
- Prohibited: "Furs, hats, sports jerseys, nylon stockings, fake or imitation pieces, anything newer than the year 1999, items in poor condition... luggage and suitcases, & anything that contains endangered animal feathers, skin, or fur."
- Steal: the decade-by-decade "What we LOVE" list is cheap, on-brand intake filtering; the explicit "can't take in" list; "not sure when it's from? send a photo, we'll check." Watch out: no price, no payout terms, no ID or paperwork stated on the page: all of that happens off-page, so it does not tell you the legal shape.

### 1.7 Florida's Antique Mall (Inverness and Sarasota, FL). Booth model, contract UNREAD
- Homepage: https://www.floridasantiquemall.com . Page read: https://www.floridasantiquemall.com/becomeavendor . Accessed 2026-10-27. Raw: `raw/b5-fl-antique-mall-vendor.md`.
- "You rent your booth space, provide and maintain your merchandise, and use our consignment system to easily input your inventory and set your prices... we provide the labels for your items, handle all point-of-sale transactions."
- The vendor contract PDF is linked but **UNREAD**: the connection failed (curl http 000). Rent amounts are not on the page ("Rental pricing varies by location").
- Relevance: a Florida operator that chose rent-a-booth plus consignment software rather than commission-only. A different risk shape (vendor sets price and owns the goods; the mall is a venue). Not a template for you, but a data point that Florida antique operators use it.

### Not usable
- Vida Style Shop's consignment-period post (https://www.vidastyleshop.com) is a generic explainer ("Most shops have a consignment period of 60-90 days"), not a policy; excluded from the matrix. Facebook policy posts surfaced in search and were not fetched.

### Comparison matrix

| Shop | Split | Term | Markdowns | Unsold | Payout | ID | Loss/theft |
|---|---|---|---|---|---|---|---|
| Arcadian (PA) | 50% | 90 d | 10/20/30% at 30/60/90 d | 5 d pickup, then shop owns / donates | monthly, $2 fee; uncashed 90 d not reissued | not stated | not insured, shop not responsible |
| Cloud Nine (CT) | 50% (40% if work) | 90 d (+7) | "any time without notice" | abandoned day 97 | quarterly; $4 check / $1 Venmo | not stated | consignor's risk |
| Generations (OH) | 50% or 60/40 | 60 d | -30% day 45 | 7 d pickup, then shop owns / donates | monthly 10th, over $25; forfeited at 3 mo | "Consignor Identification" field | consignor's risk |
| Season 2 (FL?) | 50/40/30 by price | 90 d | not stated | return on request; abandoned day 91 | monthly, 10th | not stated | not stated |
| Crossroads | cash 25-40%, trade 45%, consign up to 70% | n/a | n/a | 3 d or donate | on the spot / account | photo ID, 18+ | not stated |

---

## 2. What the examples agree on (and where they are weak)

- **Commission:** 50% to the consignor is the floor-case default (Arcadian, Cloud Nine, Generations A). Better terms for the consignor appear when price is higher (Season 2: 40%, then 30% shop cut), firm-price tradeoffs (Generations B 60/40), or high-end (Crossroads "up to 70%").
- **Term:** 60 days (Generations) to 90 days (the rest). Markdown ladders are 10/20/30% (Arcadian) or a single -30% at day 45 (Generations).
- **Unsold:** every one that states it says the consignor must pick up inside 3-7 days after the term, and unclaimed items become the shop's to sell or donate. Nobody sends reminders. **No one offers "extend."** Only Season 2 offers a clean "return on request."
- **Early pickup penalties:** 25% (Arcadian), 15% (Generations).
- **Payout:** monthly (Arcadian, Generations, Season 2) or quarterly (Cloud Nine); minimums ($25-$50); fees on checks. Store credit is the favored option.
- **Liability:** the three physical shops disclaim loss, theft, fire, damage. This is the part Florida's art statute may override (section 4).
- **Weak spots in all of them:** none mentions stolen-goods law, state record-keeping or ID retention, art-consignment statutes, sales tax, or tax reporting. Treat them as retail policy, not compliance.

---

## 3. Florida: ch. 538 (Secondhand Dealers), primary sources

Sources (all accessed 2026-10-27):
- Statute text: The Florida Senate, https://www.flsenate.gov/Laws/Statutes/2025/Chapter538/All (2025 Florida Statutes; raw `raw/b5-fl-ch538-2025-all.md`). Homepage https://www.flsenate.gov .
- Cross-check: Online Sunshine, https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0538/0538.html (page dated "October 27, 2026"; raw `raw/b5-fl-ch538-sunshine-index.md`). Homepage https://www.leg.state.fl.us .
- Agency: Florida Dept. of Revenue, https://floridarevenue.com/taxes/taxesfees/Pages/secondhand_dealers_recyclers.aspx (raw `raw/b5-fdor-secondhand.md`). Homepage https://floridarevenue.com .

**Version check:** I quoted the 2025 flsenate copy, then matched eight key sentences exactly against the 2026-dated Online Sunshine page (Acquire definition; 30-day antique/art/jewelry hold; secondhand-goods exclusion list; actual-physical-possession; thumbprint; the "(n)" no-local-license carve-out; $6 October 1 renewal; the antique-show exemption). The only 2026 session-law cite in the chapter (ch. 2026-68) sits in Part II (secondary metals recyclers) text, not Part I (secondhand dealers). Part I appears unchanged.

### 3.1 Does consignment trigger it? Yes.
- s. 538.03(1)(a): "'Acquire' means to obtain by purchase, consignment, or trade."
- s. 538.03(1)(d): "'Consignment shop' means a shop engaging in the business of accepting for sale, on consignment, secondhand goods which, having once been used or transferred from the manufacturer to the dealer, are then received into the possession of a third party."
- s. 538.03(1)(h): "'Secondhand dealer' means any person, corporation, or other business organization or entity... engaged in the business of purchasing, consigning, or trading secondhand goods."
- s. 538.03(1)(k): "'Transaction' means any purchase, consignment, or trade of secondhand goods by a secondhand dealer."
- FDOR: "Most businesses that sell secondhand goods (for example: household furniture and jewelry) must register as secondhand dealers... All dealers must comply with recordkeeping and holding period requirements of Chapter 538, Florida Statutes."

### 3.2 What counts as "secondhand goods" (your stock sorted). This is the scope lever
s. 538.03(1)(i): "...The term does not include office furniture; pianos; books; clothing; organs; coins; motor vehicles; costume jewelry; gold, silver, platinum, palladium, or rhodium bullion that has been assayed and is properly marked...; cardio and strength training or conditioning equipment designed primarily for indoor use; and secondhand sports equipment that is not permanently labeled with a serial number." It also includes "gift certificates and credit memos as defined in s. 501.95 which are purchased, consigned, or traded."

| Holliewood stock | Likely status (my reading, attorney to confirm) |
|---|---|
| 70s-90s clothing, accessories that are clothing | Outside (excluded: "clothing") |
| Costume jewelry | Outside (excluded) |
| Fine jewelry, anything with gold/silver/platinum, gemstones | Inside; 30-day hold ("precious metal, a gemstone, or jewelry") |
| Lighting, glassware, barware, furniture (non-office) | Inside; probably "antique furnishing, fixture, or decorative object" (30-day hold) only if 30+ years old AND of "special value because of its age"; otherwise 15-day hold |
| Art, prints, photographs, pottery, glass craft work | Inside; "an item of art as defined in s. 686.501" = 30-day hold |
| Playboys / magazines / ephemera | UNCLEAR: "books" is excluded; magazines are not named. Attorney question |
| Signed memorabilia | UNCLEAR: no "memorabilia" category; likely inside as general goods (15 d), or "art"/"collectible" depending on item |
| Store credit / gift cards you sell or take in | Inside per the gift-certificate/credit-memo wording |

### 3.3 Records, ID, reporting, stolen goods (s. 538.04)
- "A secondhand dealer shall complete a secondhand dealers transaction form at the time of the actual transaction... maintain a copy... for at least 1 year... However, the secondhand dealer shall maintain a copy of the transaction form for not less than 3 years." Also s. 538.06(5): "maintain transaction records for 3 years."
- **Stolen-goods reporting:** "within 24 hours after acquiring any secondhand goods, deliver to such official a record of the transaction on a form approved by the Department of Law Enforcement." "Appropriate law enforcement official" = the county sheriff, and also the city police chief if located in a municipality (s. 538.03(1)(b)). s. 538.04(6) requires electronic transmission if the agency supplies software.
- The record contains: time/date/place; "A complete and accurate description of the goods... Brand name, Model number, Manufacturer's serial number, Size, Color, Precious metal type, weight, and content if known, Gemstone description... Any other unique identifying marks"; "Digital photographs of the goods"; seller's full name, residential address, workplace, home and work phones; height, weight, DOB, race, gender, hair color, eye color, identifying marks; "The right thumbprint, free of smudges and smears."
- **ID:** "The secondhand dealer shall require verification of the identification by the exhibition of a government-issued photographic identification card such as a driver license or military identification card. The record shall contain the type of identification exhibited, the issuing agency, and the number thereon."
- **Ownership statement:** "The seller shall sign a statement verifying that the seller is the rightful owner of the goods or is entitled to sell, consign, or trade the goods." False verification or false ID while receiving money is a third-degree felony under $300, second-degree at $300 or more.
- Prohibitions (s. 538.15): no knowing transaction with anyone "under the influence of drugs or alcohol," anyone "under the age of 18 years," or "any person using a name other than her or his own name or the registered name of her or his business"; no business "between the hours of 10 p.m. and 8 a.m."; no drive-through transactions; must pay sales tax and "have a sales tax registration number."

### 3.4 Holding period and physical possession (s. 538.06)
- "A secondhand dealer may not sell, barter, exchange, alter, adulterate, use, or in any way dispose of any secondhand good: 1. That is a precious metal, a gemstone, or jewelry; an antique furnishing, fixture, or decorative object; or an item of art as defined in s. 686.501 within 30 calendar days after the date on which the good is acquired. 2. That is not described in subparagraph 1. within 15 calendar days..."
- "'antique' means the item is at least 30 years old and has special value because of its age."
- "A secondhand dealer must maintain actual physical possession of all secondhand goods throughout a transaction."
- s. 538.09(3): the dealer "must hold secondhand goods at the registered location for the period required."
- s. 538.06(3): police may place a "90-day written hold order" on goods on probable cause; "The dealer shall assume all responsibility, civil or criminal, relative to the property."
- s. 538.08: if an owner shows proof and the dealer does not return the goods, a dealer faces a noncriminal fine "of up to $2,500" after a lost replevin action; the dealer "shall hold the property" until the court decides.

### 3.5 Registration (s. 538.09 + FDOR)
- "A secondhand dealer shall not engage in the business of purchasing, consigning, or trading secondhand goods from any location without registering with the Department of Revenue."
- Fees: "$6 per location at the time of registration and an annual renewal fee of $6 per location on October 1"; plus fingerprint-processing cost (dollar amount UNVERIFIED).
- Fingerprints and photo ID; criminal-history check (10-year look-back for theft, dealing in stolen property, fraud, etc. per s. 538.09(5)(f)); "An applicant... must be a natural person who has reached the age of 18 years" (partners all apply; corporations file extra documents).
- FDOR says you need a sales-tax Certificate of Registration (DR-11) "for each county where secondhand goods are purchased, consigned, or traded and at each location where secondhand goods are sold," plus Form DR-1S. Both can be done in the online Florida Business Tax Application (per FDOR).
- Civil fine "up to $10,000 for each violation"; criminal penalty first-degree misdemeanor and fine "not to exceed $10,000" (s. 538.07).
- Premises: "The entire registered premises and required records of each secondhand dealer are subject to inspection during regular business hours by any law enforcement officer having jurisdiction" (s. 538.05).
- Local rules: "Nothing in this chapter shall preclude political subdivisions... from enacting laws more restrictive" (s. 538.17). Lee County / Fort Myers / Cape Coral local requirements for secondhand dealers NOT checked.

### 3.6 Does an online-only seller escape it? Probably not, and the carve-outs have strings
- s. 538.03(2)(n) exempts "Any person offering his or her own personal property for sale... via an Internet website, or a person or entity offering the personal property of others for sale, purchase, consignment, or trade via an Internet website, **when that person or entity does not have, and is not required to have, a local occupational or business license for this purpose.**"
- Lee County Tax Collector (https://leetc.com/businesses/business-tax-guide-and-applications/, accessed 2026-10-27; raw `raw/b5-leetc-business-tax.md`; homepage https://leetc.com): "Individuals or business entities choosing to start a business... will need to obtain a Business Tax Account... prior to doing business in Lee County." Reading both together: a shop that needs a county/city business tax receipt likely **cannot use (n)**. Attorney to confirm (home-occupation exemptions, etc.).
- s. 538.03(2)(m) is a second online carve-out but needs *all* of: a "shop, store, or other business premises"; goods viewable free on the website; records kept 2 years including serial numbers; searchable by state/zip; business name given to law enforcement; premises inspectable at any time; **payments "made by check or via a money services business licensed under part II of chapter 560"**; and a serial-number check against the FDLE stolen-article database 48 hours after contracting (or a 24-hour electronic report to police with the consignor's name, address, phone, and driver license number). Note the payment line: Zelle/Venmo/PayPal payouts to consignors may not satisfy it. UNVERIFIED whether any of those are "licensed under part II of chapter 560."
- Other exemptions relevant to you: (g) "Any person at antique, coin, or collectible shows or sales" (pop-ups); (k) licensed auction businesses; (a) nonprofits; (f) garage-sale operators holding sales "less than 10 weekends per year"; (i) buying from another registered dealer. Note (f) and (n) say the chapter "does not apply to" the garage-sale operator and the online seller; they do not say a dealer's purchase from that person is exempt. Whether these seller-side exemptions also cover the dealer's purchase is unclear: attorney question (open question 1 in 6(d); risk 12 in 6(c)).

### 3.7 Inference: what it means for the intake flow
The statutory record is created "at the time of the actual transaction," requires a physical ID, a thumbprint, and "actual physical possession." So: the web form can only be a **pre-screen** for hard goods. The real intake is an in-person (or approved alternate) step. Mail-in consignment of covered goods cannot produce a thumbprint. This is my inference from the text, not an agency statement.

---

## 4. Florida: the art consignment act (ss. 686.501-686.506)

Sources (accessed 2026-10-27): https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&Search_String=&URL=0600-0699/0686/Sections/0686.501.html and `.../0686.502.html` (raw `raw/b5-fl-686-501.md`, `raw/b5-fl-686-502.md`); s. 686.503 via https://www.flsenate.gov/Laws/Statutes/2025/686.503 (2025 text; raw `raw/b5-fl-686-503.md`). Secondary commentary: Akiba Law, https://www.akibalaw.com/blog/2026/04/consigning-art-in-florida-why-written-agreements-notices-and-statutory-formalities-matter/ (raw `raw/b5-akiba-fl-art-consign.md`; a law-firm blog, not authority).

- **Definition is broad:** "'Art' means a painting, sculpture, drawing, work of graphic art, pottery, weaving, batik, macrame, quilt, print, photograph, or craft work executed in materials including... clay, textile, paper, fiber, wood, tile, metal, plastic, or glass," plus "a map 80 years old or older" and rare prints/documents. "'Art dealer' means... a person who is a consignee of a work of art."
- s. 686.502(1): delivery for sale "on a commission, fee, or other basis of compensation... is deemed to be 'on consignment'; and... such consignee shall thereafter be deemed to be the agent of such consignor."
- s. 686.502(2): consignor must tag the work, or the consignee must "post a clear and conspicuous sign in the consignee's place of business giving notice that some works of art are being sold subject to a contract of consignment."
- s. 686.502(3): "The proceeds of sale of a work of art shall be held in trust by the consignee for the benefit of the consignor."
- s. 686.502(4): "Any provision of a contract or agreement whereby the consignor waives any of the provisions of this section is void."
- s. 686.503: a written contract is required and must include: proceeds delivered "at a schedule agreed upon"; "(2) The consignee shall be responsible for the stated value of the work of art in the event of the loss of or damage to such work of art while it is in the possession of such consignee"; "(3) The work of art shall only be sold by the consignee for an amount at least equal to the amount agreed upon by the consignor in writing"; "(4) The work of art may be used or displayed by the consignee or others only with the prior written consent of the consignor and only if the artist is acknowledged." Subsection (5) gives *an artist* priority over the dealer's creditors.
- **Open scope question:** the quoted text uses "consignor" without a statutory definition and (5) is expressly artist-specific; I did not find text limiting (1)-(4) to artists. Whether an estate seller consigning a print is covered is an attorney question. If it is, three things in the examples are non-compliant for art: "all items are left at consignor's risk"; shop-chosen price with no consignor-agreed minimum; and using photos/display without written consent (your site and Etsy listings are "display").

---

## 5. Tax

### 5.1 Form 1099-K (what Etsy/Shopify/card processors report about YOU)
- IRS, https://www.irs.gov/businesses/understanding-your-form-1099-k (homepage https://www.irs.gov ; page shows "Page Last Reviewed or Updated: 28-Jun-2026"; accessed 2026-10-27; raw `raw/b5-irs-1099k.md`).
- "Third party settlement organizations (TPSOs) (payment apps and online marketplaces) are required to report payments on Form 1099-K when the total amount of payments you receive for goods or services through the platform exceeds $20,000 in more than 200 transactions. You may receive a Form 1099-K even when total payments or transactions are less than the reporting threshold."
- Cards are different: "If your customers or clients pay you directly by credit, debit or gift card, you'll get a Form 1099-K from your payment card processor no matter how many payments you got or how much they were for."
- "Whether or not you receive a Form 1099-K, you must still report any income on your tax return. This includes payments for any goods you sell (including personal items such as clothing or furniture sold at a gain)."
- Consequence for consignment: the gross on your 1099-K includes the consignor's share. Your books need a consignor-payable line so you can show only your commission as income. (Accounting inference, CPA to confirm.)
- Consignors: it is also their obligation to report gains; your agreement should say you give no tax advice.

### 5.2 Forms 1099-NEC / 1099-MISC (what YOU might have to file for consignor payouts)
- IRS, https://www.irs.gov/instructions/i1099mec ("Instructions for Forms 1099-MISC and 1099-NEC," December 2026 revision per the page's own anchors; accessed 2026-10-27; raw `raw/b5-irs-i1099mec.md`).
- "For tax years beginning after 2025, the minimum threshold amount for reporting certain payments... increased to $2,000 and may be adjusted for inflation beginning in calendar year 2027."
- 1099-NEC: "for each person in the course of your business during the year to whom you have paid at least $2,000 in: Services performed by someone who is not your employee... or Payments to an attorney."
- Exception list: "Some payments do not have to be reported on Form 1099-MISC, although they may be taxable to the recipient... Payments for merchandise, telegrams, telephone, freight, storage, and similar items." (The same line appears in the 1099-NEC exceptions.)
- "Payments made with a credit card or payment card and certain other types of payments, including third-party network transactions, must be reported on Form 1099-K by the payment settlement entity... and are not subject to reporting on Form 1099-MISC or Form 1099-NEC."
- There is a "direct sales" box for "sales by you totaling $5,000 or more of consumer products to a person on a buy-sell, deposit-commission, or other commission basis for resale... anywhere other than in a permanent retail establishment." That reads as a seller-to-reseller rule, not payouts to consignors, but the phrase "deposit-commission" is close enough to consignment that the CPA should explicitly rule it out.
- My read (not advice): consignor payouts for goods sold are "payments for merchandise," so no 1099-NEC/MISC. If you ever pay a consignor for **services** (styling, repair, photography) the $2,000 NEC threshold applies. Payments you make by card or payment app may fall under 1099-K reporting instead.
- Discrepancy note: third-party blogs found in search results discuss the 1099-K threshold history; I used only IRS pages. IRS pages verified $20,000/200 (TPSO) and $2,000 (NEC/MISC, tax years after 2025). Anything about prior-year thresholds is not needed here and was not verified.

### 5.3 Florida sales tax on consigned goods
- Rule 12A-1.081, Florida Administrative Code, "Consignment Sales": "Where merchandise is delivered to a dealer on a consignment basis, the tax shall be collected and remitted by the consignee, not the consignor." Effective 6/16/1972 per the official page.
- Sources: official rule page https://www.flrules.org/gateway/ruleNo.asp?id=12A-1.081 (homepage https://www.flrules.org ; shows title, effective date, history; the rule text itself is an attached .doc I did not open; raw `raw/b5-fac-12a-1-081-flrules.md`); text read from the mirror https://flrules.elaws.us/fac/12a-1.081 ("Florida Administrative Code (Last Updated: March 7, 2026)"; homepage https://www.elaws.us ; raw `raw/b5-fac-12a-1-081-elaws.md`).
- **Discrepancy:** operative sentence verified on the elaws mirror only. The two pages list different rulemaking-authority cites (flrules: 212.18(2), 213.06(1); Law Implemented 212.05(1). elaws adds 212.17(6) and 212.02(15)). Operative text verified, citation history needs review.
- FDOR: "Retail sales of secondhand goods, precious metals, and secondary metals are subject to Florida's sales and use tax and discretionary sales surtax."
- Net effect: tax applies to the whole sale price (not just your commission) and you remit it. UNVERIFIED (not fetched): whether Etsy collects/remits Florida tax as marketplace facilitator on Etsy orders, how that interacts with your own filing, and the current Lee County discretionary surtax rate.

---

## 6. Deliverables

### (a) Consignment agreement outline (one page). DRAFT, NOT LEGAL ADVICE. Have a Florida attorney finalize

1. **Parties and ID.** Shop legal name and registered location; consignor name, address, phone, email; consignor ID type, issuing agency, number (copy kept; statutory record in s. 538.04). Agreement date; start date; end date; last pickup date (Generations pattern).
2. **Items.** Attached inventory sheet: per item photo, description, brand/maker, size, serial number if any, condition notes, agreed asking price, and **minimum acceptable price in writing** (s. 686.503(3) for art). Shop may refuse any item.
3. **Ownership warranty.** Consignor is 18+, sole owner or authorized to sell, goods not stolen and free of liens (Generations wording); signs the statutory "rightful owner" statement (s. 538.04(3)); acknowledges false statements may be a felony; consents to ID copy, photos, and reports to law enforcement.
4. **Hold period.** Shop cannot sell until the statutory hold ends (15 or 30 days from acquisition); term clock and markdown clock start after that. The law does not lock the consignor in: s. 538.06(1)(a) says the holding periods "are not applicable when the person known by the secondhand dealer to be the person from whom the goods were acquired desires to redeem, repurchase, or recover the goods, provided the dealer can produce the record of the original transaction with verification that the customer is the person from whom the goods were originally acquired." So the verified consignor may reclaim their item during the hold; any contractual lock-in is Ricky's business choice, not a legal requirement.
5. **Term.** 60 or 90 days (examples). Pick one; say what starts the clock.
6. **Pricing and markdowns.** Shop sets list price after consulting consignor, never below the written floor; markdown ladder (Arcadian 10/20/30% at 30/60/90 d, or Generations -30% at day 45). State whether offers below ask are accepted (Generations A/B).
7. **Commission.** Flat (50%) or tiered (Season 2: 50/40/30% by price); "firm price" vs. "negotiable" variants (Generations A/B). Fees that come off the consignor share must be listed with caps (cleaning, authentication with consent, shipping materials).
8. **Channels.** In-person, own site, Etsy, Shopify; state who gets proceeds above list price if sold online (decide deliberately: Generations keeps it; consider not copying) and that the item is exclusive to you during the term.
9. **Payout.** Schedule (monthly on the 10th is the common pattern), minimum balance, method (check/ACH/store credit; no forfeiture without written notice), statement of each sale; reversal rule if the buyer returns the item or a payment is charged back; proceeds held in a separate account (and in trust for art).
10. **Unsold items.** Written notice by email at 14 days before term end; options: pick up, extend one term at lower split, donate on written consent, or shop buys at an agreed price. Pickup window with notice. State what happens if unclaimed, with a final written notice before disposal.
11. **Early withdrawal.** Allowed with fee (examples: 15% Generations, 25% Arcadian). A fee during the statutory hold is a business choice; the statute lets the verified consignor recover the goods then (see item 4).
12. **Risk of loss.** Shop carries inventory/bailee coverage (confirm with insurer). For art: shop responsible for stated value of loss or damage (s. 686.503(2)). For other goods: either same or a stated cap; do not copy blanket "consignor's risk" wording without attorney review.
13. **Condition and authenticity.** Shop describes items from consignor information and its own inspection; no appraisal; no guarantee of authenticity or provenance beyond the listing text; consignor warrants authenticity of any signed/branded item and indemnifies for counterfeits (Season 2 and Cloud Nine charge a fee; consider a refund-of-proceeds clause instead).
14. **Prohibited items.** Stolen or unverifiable property, weapons/firearms, recalled or unsafe items (cribs, car seats: Arcadian), fur/endangered-animal material (Hello Vintage), electrical items that are unsafe unrewired (decision for you), mattresses, mold/odor/pest-infested items, counterfeits.
15. **Taxes.** Shop collects and remits Florida sales tax on the full price. Consignor is responsible for own income taxes; shop gives no tax advice; shop issues no 1099 for merchandise payouts unless the law requires (CPA to confirm).
16. **Records and privacy.** Shop keeps ID copy, photos, and the transaction record at least 3 years; how data is protected; who can see it.
17. **Default, notices, governing law.** Written notice by email; Florida law; venue; entire agreement; copy to consignor; both sign and date.
For art: add the public notice/tag language of s. 686.502(2) at the shop and on listings.

### (b) Intake-form field list (ready to build). Synthesized; source tags: [S] = from Fla. Stat. ch. 538, [Ex] = seen in an example above, [H] = my suggestion

**Tier 1: web pre-screen (no ID, no promise)**
- Seller name, email, phone [Ex] ; city/state [H]
- Path: "sell to us" vs "consign" [Ex: Crossroads, Hello Vintage] ; preferred payout: cash/check/store credit [Ex]
- Per item (repeat): category [H]; title/short description [Ex Hello Vintage]; maker/brand/era [S: 538.04(1)(b)]; size and dimensions [S: size] ; color [S]; materials; serial number or maker's mark if any [S]; condition (select: mint/good/fair/flaws) + free text on flaws [H]; works/doesn't work (lamps: wired? bulb socket?) [Ex Arcadian "must have working battery", "must come with shade"]; provenance (where/how you got it) [H, supports 538.04(3) later]; seller's asking price or "open to offers" [Ex: Generations A/B]; minimum price (hard floor) [S for art: 686.503(3)]; photos (required, see below)
- Photo requirements (shop practice; statute requires the shop to take its own "digital photographs" at intake): 1) overall, 2) mark/label/signature/serial close-up, 3) flaws, 4) scale shot, 5) base/underside/back. Let seller upload 5-10 per item [H]. Do NOT collect ID images on the web form.
- Declarations: age 18+ checkbox [S: 538.15(1)(b); Ex Generations]; "I own this and it is not stolen" checkbox [S/Ex]; "I understand intake is by appointment and ID is required" [S]
- Anti-spam: honeypot + rate limit [H]; show prohibited-items list before submit [Ex Hello Vintage, Arcadian]

**Tier 2: in-person intake record (this is the statutory transaction record for covered goods; exact FDLE form is set by law enforcement)**
- Time, date, place of transaction [S 538.04(1)(a)]
- Per item: brand, model, serial number, size, color, precious metal type/weight/content if known, gemstone description, other marks [S 538.04(1)(b)]; shop-taken digital photos of the identifying marks [S 538.04(1)(c)]
- Seller: full legal name, current residential address, workplace, home and work phone [S 538.04(1)(d)1]; height, weight, DOB, race, gender, hair color, eye color, identifying marks [S (d)2]; right thumbprint [S (d)3]
- ID: type, issuing agency, number, plus a copy/scan [S 538.04(2)]
- Signed rightful-owner statement [S 538.04(3)]
- Check: name matches ID (no alias use) [S 538.15(1)(c)]; sober; 18+ [S 538.15(1)(a)(b)]; transaction between 8 a.m. and 10 p.m. [S 538.15(2)]
- Hold-until date [S 538.06] computed: 15 or 30 days from acquisition date; "antique" flag if 30+ years old, "art" flag
- Law-enforcement report sent within 24 hours: date/time sent, confirmation [S 538.04(1)]
- Agreement signed + inventory sheet attached; consignor copy given [Ex Generations]

**Tier 3: internal (not shown to consignor)**
- Item ID / SKU, intake date, term end date, markdown dates, list price history, listing URLs by channel, sale date, sale price, buyer-return flag, commission calc, sales tax collected, payout due and paid (date, method), unclaimed notice dates, disposition (returned/donated/extended) with dated email.

### (c) Risks nobody warns you about
1. **Consignment alone makes you a regulated dealer** in Florida (definition (h)), not just buying. FDOR says registration also needs a sales-tax registration per county where goods are "purchased, consigned, or traded."
2. **The hold period applies to consigned goods too** ("acquire" includes consignment): 15 days for most, **30 for antique furnishings/fixtures/decorative objects (30+ years old), art, and jewelry.** The antique line requires 30+ years old *and* that the item "has special value because of its age," so age alone does not decide it (attorney question #2); anything made in 1996 or earlier clears only the age half today. "Consign Saturday, list Sunday, sell Monday" is illegal for covered goods. The statute also bars "alter... use" during the hold, which may include cleaning or rewiring a lamp. Attorney question.
3. **Police can walk into your registered premises** during business hours and inspect inventory and records (s. 538.05). A spare room at home is your "registered location."
4. **You become a store of ID data and thumbprints** you must keep 3 years. That is PII under your Supabase/host controls: encryption, access rules, retention, breach response. The statute requires the data; it does not tell you how to protect it.
5. **Stolen-goods exposure:** the dealer "shall assume all responsibility, civil or criminal" for held goods (s. 538.06(3)); an owner with proof can replevin the item from you; the thief's restitution happens only after a conviction. Refunding a buyer for an item that turns out stolen comes out of your pocket.
6. **"Consignor's risk" may be void for art** (s. 686.503(2), s. 686.502(4)); you may owe the stated value of lost or damaged art, and proceeds must be kept in trust. Two sets of books.
7. **1099-K gross inflation:** Etsy/Shopify/card processors will report gross sales including consignors' shares. If you do not track consignor payable, you pay income tax on money you owe other people. Cards trigger 1099-K at any amount.
8. **Sales tax is yours on the full price** of consigned goods (12A-1.081), including any you sell on your own site; marketplace-facilitator handling on Etsy UNVERIFIED.
9. **Forfeiture and "abandoned" clauses may not be safe to copy.** Arcadian ("Checks not cashed within ninety (90) days will not be re-issued"), Generations ("Payments not picked up after 3 months will be expired and forfeited"). Florida unclaimed-property rules for uncashed payouts and store credit NOT checked; do not copy until an attorney confirms.
10. **Authenticity cuts both ways.** Cloud Nine "guarantees authenticity"; you can't on vintage signed items or Playboys with signatures. Use a consignor warranty plus a refund-of-proceeds clause.
11. **Ghost listings.** The same one-of-one item can be on your site, Etsy, and the consignor's Facebook Marketplace. Exclusivity clause, plus delisting speed, or you'll oversell.
12. **Sourcing, not just consigning:** buying from individuals (door, DMs, Facebook Marketplace) is a "transaction." The statute exempts yard-sale operators under 10 weekends a year, nonprofits, auctions, and other registered dealers, but not obviously every online seller you buy from. Ask the attorney how your own sourcing is treated.
13. **Mail-in consignment doesn't fit hard goods** (thumbprint, physical-possession, same-day transaction record). A "ship it to us" Season 2-style flow works for clothing/costume jewelry only.
14. **Payout rails.** If you rely on the online-seller carve-out (m), payouts must go by check or a licensed money-services business. Venmo/Zelle may not qualify. UNVERIFIED.
15. **Time-of-day rule.** s. 538.15(2) says no business "between the hours of 10 p.m. and 8 a.m." Unknown whether it reaches a 24/7 website taking consignment requests; keep the web form pre-screen-only and promise nothing.
16. **UCC / creditors.** Per Akiba's summary of *Rayfield v. Kreps* (4th DCA 2010), a consignor who didn't tag goods or file lost to the gallery's lender. Low risk with no lender; matters if you ever borrow against inventory. (Law-firm blog summary, not the opinion.)

### (d) Open questions Ricky must settle with a professional

**Attorney (Florida):**
1. Does ch. 538 apply to an online-first shop with a home address and a Lee County business tax receipt? Is (n) unavailable because a license is required? Can (m) be met, including payouts?
2. Classification of each stock type: Playboys (books?), signed memorabilia, glass/barware, vintage lighting (antique "fixture"? 30-day or 15-day hold; is 30+ years old enough, or must the item also have "special value because of its age"?), prints, fine vs. costume jewelry (rhinestone and gold-plated).
3. Do ss. 686.501-686.506 apply to non-artist consignors? Can art loss risk be limited by contract? Trust account mechanics and signage on listings.
4. Can items be listed during the hold (not sold)? Does "alter" cover cleaning/rewiring?
5. Which law-enforcement agency and form does Lee County use (Sheriff, plus city police chief if inside Fort Myers/Cape Coral/etc.)? What electronic reporting system must you use (s. 538.04(6))? Any local rules stricter than state law (s. 538.17)?
6. Entity choice: an LLC? Registration needs natural-person applicants; do owners get fingerprinted?
7. Unclaimed property / abandonment rules for uncashed payouts, store credit, and unclaimed goods; is "abandoned after N days" enforceable in Florida?
8. Whether you may keep merchandise at home as the "registered premises"; zoning / home-occupation.
9. Indemnity and counterfeit clauses; limits on early-withdrawal fees; enforceability of attorney-fee clauses (Arcadian has one).

**CPA:**
10. Treatment of consignor payable vs. commission income; reconciling 1099-K gross to net.
11. Confirm no 1099-NEC/MISC for merchandise payouts, rule out the "direct sales / deposit-commission" box, and any 1099-K treatment if you pay consignors through a payment app.
12. Sales tax: collecting on consigned sales on Etsy vs. own site; marketplace-facilitator treatment; Lee County discretionary surtax rate; DR-11 per county.
13. Store credit and gift card liability and tax timing.

**Insurance agent:**
14. Does your policy cover other people's property in your care (bailee coverage)? Theft, fire, and flood for consigned inventory? Generations says it carries "fire and liability insurance coverage only." Ask what yours excludes.

---

## 7. Ranked recommendations for Holliewood and Vine

1. **Do not launch hard-goods consignment day one.** Register as a secondhand dealer and get the paperwork rhythm working on goods you buy outright. Great idea: it's the lowest-risk path to learning the 24-hour reporting loop. Cost: a registration and a few weeks.
2. **Launch soft goods first.** Clothing and costume jewelry are likely outside ch. 538 (s. 538.03(1)(i)), so a Season 2-style web intake (photos + details, quote, prepaid label) is plausible for fashion. Confirm with the attorney before you build it.
3. **Make hard-goods consignment invite-only and in person.** Appointment, ID, thumbprint, 24-hour report, hold date tracked, written agreement. Good for pieces where your cut justifies the work; gimmick for $20 glassware. (My opinion: set a minimum item value; the examples don't give one.)
4. **Use a tiered commission,** not a flat 50: Season 2's 50/40/30 by price band is the only structure in the examples that rewards high-value pieces. Offer a "firm price / negotiable" option like Generations A/B.
5. **Rewrite the liability and abandonment clauses** before copying anything. Do not copy "left at consignor's risk," forfeiture of uncashed payouts, or authenticity guarantees.
6. **Track money properly from day one:** consignor payable ledger, separate account for consigned proceeds, sales tax on the full price, match to the 1099-K gross.
7. **Hello Vintage-style "what we love / can't take in" page** is the cheapest on-brand intake filter. Great for your voice; add era wish-lists for lamps, barware, art.
8. **Skip** the "we guarantee authenticity" claim and any "we ship it back for free" promise.

---

## 8. Provenance, discrepancies, and UNVERIFIED list

**Discrepancies**
- Rule 12A-1.081: operative text verified on mirror (elaws) only; official flrules page shows metadata and a linked .doc that I did not open; rulemaking-authority cites differ between them. **Verified (text), need review (citation history).**
- Ch. 538: 2025 flsenate copy used for quotes; spot-matched 8 sentences against the 2026-dated Online Sunshine page; the one 2026 session-law cite in the chapter is in Part II. **Part I verified identical on those sentences; the remaining Part I text was not diffed line-by-line.**
- FDOR "$6 for each location and for each license type" vs. statute "$6 per location... plus fingerprint cost": compatible, but the fingerprint fee amount is not stated in either fetched source. **UNVERIFIED.**
- Hello Vintage's Etsy/Shopify tax and legal state: not stated on the page.

**UNVERIFIED / not fetched**
- Season 2's Florida location (inferred from a URL slug).
- Florida's Antique Mall vendor contract (PDF fetch failed, http 000).
- Crossroads ID-retention rationale (seen only in a link's URL fragment).
- Etsy marketplace-facilitator sales-tax handling; Lee County discretionary surtax rate.
- City-level business licenses and local secondhand-dealer rules (Lee County, Fort Myers, Cape Coral); Lee County Tax Collector page only confirms a business tax account is needed "prior to doing business in Lee County," renewals expire Sept 30.
- Florida unclaimed-property rules; FDLE form details; which payout rails count as "licensed under part II of chapter 560."
- The FDOR brochure GT-800036 (download returned HTML, not the PDF).

**Access dates:** all pages 2026-10-27. Raw files are in `C:\Users\ethan\dev\Vintage\research\consignment\raw\` (prefix `b5-`).
