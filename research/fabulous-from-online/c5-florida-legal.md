# c5: Florida legal guardrails for styling and sourcing

Agent c5, accessed 2026-10-28. Raw captures: `research/fabulous-from-online/raw/c5-*` (statute, rule and FTC text; some PDF text extracted locally).
Method: SearXNG for URLs, crawl4ai for pages (flsenate.gov 2026 statutes ch. 481, 489, 501, s. 212.18; floridarevenue.com; myfloridalicense.com; ecfr.gov; ftc.gov). Two walls were handled with fallbacks: the DOR TAA 02A-014 PDF returned 4 bytes to crawl4ai, so I used the WebFetch fallback, which saved the PDF, and I extracted its text locally (`raw/c5-dor-taa02a014.clean.txt`). Current Rule 12A-1.001 was read on a Cornell mirror, not the flrules page (see section 2). Ch. 538 text comes from the prior capture `research/consignment/raw/b3-fl-ch538-2026.md`; I read it only for the agent-versus-buyer question and did not redo the Florida gate. A curl attempt with a spoofed browser header was blocked by the permission system and I did not retry it.
Tags: `verified` = read on a primary page this session. `mirror` = primary text read on a secondary site. `inferred` = my reading of verified text. `unverified` = not read on a primary page, or a vendor claim.
**This is research, not legal advice.** Take the open questions in the guardrail list to a Florida attorney, a CPA, DOR and DBPR before launch.
Assumes the business is in Lee or Collier County and the clients are individuals decorating homes. Hollie is referred to by name or as they/them.

## TL;DR

1. **Residential styling needs no state interior-design registration, and "interior designer" is a free title.** `verified`. Ch. 481 "shall not apply to" a person doing "interior design services or interior decorator services for any residential application" (481.229(6)(a)). Only "architect," "registered architect" and "registered interior designer" are protected (481.223(1)(b)). The statute is silent on whether non-residential work (events in a rented hall, an office, a restaurant) is barred without registration, but DBPR's FAQ says "Commercial services require registration by the board." Statute verified, DBPR position needs review. Scope the page to homes.
2. **Sales tax splits into two models, and it is the same split as ch. 538.** `verified` (rule on a mirror, TAA from the DOR PDF). If Hollie sells the items to the client (sourcing, resale), the item price, the markup and any design, travel, delivery or rush fee bundled into that sale are taxable. If Hollie only advises and the client buys directly, a separately stated advisory fee is not taxable. DOR's TAA 02A-014 says that if Hollie places the order for the client, even hourly shopping fees become taxable. The drafting that keeps a design fee untaxed is not codified (section 2).
3. **The FTC Cooling-Off Rule covers sales to a buyer who invited the seller in.** `verified`. 16 CFR 429.0(a) reaches sales made "in response to or following an invitation by the buyer," with a $25 threshold at the buyer's residence and $130 elsewhere. A "non-refundable" term cannot waive the 3-business-day cancel right (429.1(d)). Florida's own home solicitation law is narrower on its face (it excludes a sale that "results from a request for specific goods or services by the purchaser"), but if services were performed before a cancellation it says the seller "is entitled to no compensation" (501.045). Guardrail: book and pay online before the visit, and make no on-site upsell without the 429.1 notice forms.
4. **FDUTPA turns FTC rule breaches into Florida violations.** `verified`. 501.203(3)(a) counts "any rules promulgated pursuant to the Federal Trade Commission Act." Penalty is up to $10,000 per willful violation (501.2075), plus actual damages and attorney fees to a harmed buyer (501.211(2), 501.2105). Nothing I read bans a non-refundable fee. The risk is non-disclosure and the in-home cancel right.
5. **The contractor line: placing things is fine, wiring and building are not, and "by others" counts.** 489.105(3) defines a contractor as someone who, for compensation, "does himself or herself or by others" construct, repair, alter, remodel or improve a building. If Hollie hires and pays an electrician or painter for a client, Hollie is contracting. Electrical Part II (489.503) has no $2,500 minor-work exemption, so any hardwiring needs a licensed electrician. The ch. 489 $2,500 exemption (489.103(9)) is lost if Hollie advertises as a contractor. Unlicensed contracting during a declared state of emergency is a third-degree felony (489.127(2)(c)), which matters in SWFL. The client contracts any trade directly; Hollie refers.
6. **Ch. 538 versus rush.** If Hollie buys secondhand goods (lamps, art, glass, antiques) from private sellers in order to resell them to a client, Hollie is a "secondhand dealer" with a 15-day hold (30 days for antique decor and art) during which they may not "sell ... alter ... use, or in any way dispose of" the good (538.06(1)(a)). That defeats a rush service and in-home use of a just-bought piece. The client buying directly, or Hollie buying from a compliant dealer or at an antique show, avoids it. Whether a true agent-buyer model is outside ch. 538 is `unverified`. Ask a Florida attorney.
7. **Insurance norm is general liability plus professional liability, and condo or HOA properties may ask for a certificate with an additional-insured endorsement.** `unverified` (insurer and vendor pages only). Do not print "insured" on the page until a policy is bound.
8. **Words to use:** designer, interior designer, decorator, stylist, e-design, styling, placing, hanging. **Words to avoid:** registered interior designer, architect, licensed or certified designer (unless true), contractor, remodeling or renovation services, installation of fixtures, hardwiring (wording table below).

---

## 1. Ch. 481 Part II: interior design (titles, licensing, residential exemption)

Source: https://www.flsenate.gov/Laws/Statutes/2026/Chapter481/All (raw `c5-ch481-all.md`). DBPR: https://www2.myfloridalicense.com/architecture-and-interior-design/faqs/ (raw `c5-dbpr-faqs.md`). `verified`.

**Definitions, 481.203.**
- (9): "“Interior decorator services” includes the selection or assistance in selection of surface materials, window treatments, wallcoverings, paint, floor coverings, surface-mounted lighting, surface-mounted fixtures, and loose furnishings not subject to regulation under applicable building codes."
- (10): "“Interior design” means designs, consultations, studies, drawings, specifications, and administration of design construction contracts relating to nonstructural interior elements of a building or structure. “Interior design” includes, but is not limited to, reflected ceiling plans, space planning, furnishings, and the fabrication of nonstructural elements within and surrounding interior spaces of buildings. “Interior design” specifically excludes the design of or the responsibility for architectural and engineering work, except for specification of fixtures and their location within interior spaces."
- (13): "“Registered interior designer” means a natural person who holds a valid certificate of registration to practice interior design."

**Titles, 481.223(1)(b).** "Use the name or title “architect,” “registered architect,” or “registered interior designer” when the person is not then the holder of a valid license or certificate of registration issued pursuant to this part. This paragraph does not restrict the use of the name or title “interior designer” or “interior design firm.”" Violation is a first-degree misdemeanor (481.223(2)), and an affected person, including anyone "who received services," can sue for an injunction with attorney fees to the prevailing party (481.223(3)). `verified`.
- The words "decorator," "designer," "stylist," "e-design," "design consultant" do not appear in the prohibited list. `verified` (absence from the list I read). Using them is therefore not barred by ch. 481. `inferred`.

**Residential exemption, 481.229(6).** "This part shall not apply to: (a) A person who performs interior design services or interior decorator services for any residential application. For purposes of this paragraph, “residential applications” includes all types of residences, including, but not limited to, residence buildings, single-family homes, multifamily homes, townhouses, apartments, condominiums, and domestic outbuildings appurtenant to one-family or two-family residences." `verified`. (6)(b) separately exempts retail-store employees giving decorator services "provided that such employee does not advertise as, or represent himself or herself as, a registered interior designer."

**Contractor line, 481.229(7).** "Nothing in this part shall be construed as authorizing or permitting an interior designer to engage in the business of, or to act as, a contractor within the meaning of chapter 489, unless registered or certified as a contractor pursuant to chapter 489." `verified`.

**Compensation disclosure, 481.2131(2).** "The interior designer shall have the responsibility of fully disclosing to the client the manner in which all compensation is to be paid. Unless the client knows and agrees, the interior designer shall not accept any form of compensation from a supplier of goods and services in cash or in kind." `verified` text. Because 481.229(6)(a) takes residential work out of "this part," I read this as not binding on Hollie's residential work (`inferred`), but it is a sound FDUTPA-style practice: disclose markups and trade discounts. DOR also treats a trade discount as a taxable "fee" (section 2).

**Commercial work: the discrepancy.**
- 481.223(1) bars practicing *architecture* and using three titles. I also checked 481.213(1) and 481.219; neither says "no one may practice interior design without registration." `verified` (absence in the text I read).
- DBPR FAQ, https://www2.myfloridalicense.com/architecture-and-interior-design/faqs/ : "Do I need a registration to be an Interior Designer? Not for residential interior design services. You must be registered as a registered interior designer to practice commercial interior design. You should contact the local city or county municipality to determine if an occupational license is required." And: "If I am not registered can I call myself an interior designer? Yes. The title “interior designer” is not a protected title and can be used by anyone providing residential interior design services. Commercial services require registration by the board." `verified` (FAQ text).
- Result: statute text verified, DBPR position needs review (ask DBPR). Parties and events held in rented venues, offices or restaurants are the grey zone. Whether temporary event decor counts as "interior design" of "a building" is `unverified`. Keep the page's promises to "your home."
- The statute wording also leaves "studio" ambiguous. A client's home studio is residential; a rented commercial studio is not. Ask which.

**Amendments 2020 to 2026.** `verified` for the history lines; effect `inferred`.
- HB 1193 (2020) became ch. 2020-160, effective 7/1/2020. The bill page (https://www.flsenate.gov/Session/Bill/2020/1193, raw `c5-hb1193-2020.md`) lists 481.203, 481.209, 481.213, 481.2131, 481.223, 481.229 and others as amended. I read the bill page index, not the bill text.
- In the 2026 statute the History lines end at ch. 2020-160 for 481.2131, 481.223 and 481.229, and at ch. 2021-51 for 481.203. I saw no 2022 to 2026 amendment to those sections. I did not search for 2026-session bills beyond the 2026 statute text.
- The 2026 text bars "registered interior designer" and leaves "interior designer" free. I did not read the pre-2020 text; the DBPR FAQ's "not a protected title" matches the current statute.

---

## 2. Sales tax

### 2a. Buying for clients and the Annual Resale Certificate

Source: https://floridarevenue.com/taxes/taxesfees/Pages/annual_resale_certificate_sut.aspx (raw `c5-dor-resale-cert.md`); https://www.flsenate.gov/Laws/Statutes/2026/212.18 (raw `c5-fs-212-18.md`). `verified`.
- 212.18(3)(a)–(b): a person who wants to "engage in or conduct business in this state as a dealer" must apply for a certificate of registration "before" engaging in the business, and "may not engage in business as a dealer ... without a valid certificate." Failure to register is a first-degree misdemeanor (212.18(3)(d)1).
- 212.18(3)(e): "the department shall provide each active dealer with an annual resale certificate."
- DOR page: "The certificate allows business owners, or their representatives, to buy or rent property or services tax free when the property or service is resold or re-rented." It "may not" be used for property "used: But not resold or rented, Before selling or renting the goods, or By your business or for personal purposes, such as furniture, office equipment, computers, or supplies." And: "If you purchase an item tax exempt intending to resell it, but then use the item in your business or for personal use, you must report and pay use tax on the item." "There are criminal and civil penalties for the fraudulent use of a resale certificate."
- Consequence for Hollie: items bought for a specific client for resale can be bought tax-free with the certificate. Props, staging stock and shop pieces that Hollie *uses* in installs *before selling* are a use-tax issue. `inferred`.
- Renting vintage pieces for parties would be a separate rental transaction. Whether and how rentals are taxed was not read. `unverified`.
- TAA 02A-014 answer 9 (below): purchases "on behalf of its clients qualify for resale exemption, as long as Taxpayer does not purchase the items to consume itself in real property improvement."
- County surtax rates were not looked up. `unverified`.

### 2b. Are design, decorating and consulting fees taxable?

Sources:
- Rule 12A-1.001(2) "Service transactions," read on a mirror: https://www.law.cornell.edu/regulations/florida/Fla-Admin-Code-Ann-R-12A-1-001 (raw `c5-fac-12a-1-001-cornell.md`). `mirror`. The official flrules page (https://www.flrules.org/gateway/ruleNo.asp?id=12A-1.001, raw `c5-fac-12a-1-001.md`) gave metadata only, with an effective date of 12/29/2025 and a .doc link. The Cornell history ends at 1/1/2024, so the mirror may be one revision behind. Re-check the official text.
- DOR Technical Assistance Advisement 02A-014, 3/18/2002, "Sales Tax - Interior Design Contract": https://floridarevenue.com/TaxLaw/Documents/TAA%2002A-014.pdf (raw `c5-dor-taa02a014.pdf` and `.clean.txt`). `verified` (DOR PDF, text extracted locally).
- TAA 19A-006 "Interior Decorating": primary DOR PDF not retrieved (guessed URL 404). I read only a law-firm republication: https://www.floridasalestax.com/taas/taa-19a-006-interior-decorating/ (raw `c5-taa19a006-mirror.md`). `mirror`; Q&A text only, without the facts.
- DOR brochure GT-800052 "Sales and Use Tax for Interior Decorators and Interior Designers" now 404s on floridarevenue.com. Not read.

**Current rule text (mirror), 12A-1.001(2)(a):**
1. "An interior decorator's so-called fee is taxable as a part of the selling price under Section 212.02(16), F.S., or as a part of the cost price under Section 212.02(4), F.S., and cannot be exempted as a professional or personal service charge when the transaction involves the sale of tangible personal property. This is true when the so-called fee is paid in the form of a trade discount ... The decorator fee is also taxable when it appears as an amount added to the decorator's cost when billed to the client for tangible personal property on a cost plus basis."
2. "If the decorator's fee is solely for designing the interior and exterior decorative scheme or for advising his clients and recommending colors, paints, wallpaper, fabrics, brands, sources of supply, etc., and there is no sale of tangible personal property involved, then such fee would be exempt as a professional or personal service transaction."
3. "In some instances, the decorator may receive a fixed sum, which is not in any way contingent upon the sale of tangible personal property, as a so-called decorator fee. Then, in other completely unrelated transactions, he may sell tangible personal property to the same client. In such cases the decorator's fee cannot be considered as a part of the selling price of the property sold because there is no connection between the transactions."

**TAA 02A-014 (DOR's reading of those rules), verbatim from the PDF:**
- Summary: "Fees charged by designers in conjunction with the sales of tangible personal property are a part of the total charge for the tangible personal property and are subject to tax, even when separately itemized and charged to their clients on a cost plus basis. Fees charged by an interior decorator or designer solely for consultation or designing services when no sale of tangible personal property occurs in conjunction with those services are not subject to tax."
- Answer 5: "If the design fee is part of the sale of the furniture, the entire $16,500 is subject to tax, because the design fee is part of the taxable sales price of the tangible personal property. This kind of absurd result is easily avoided where the agreement is drafted to avoid such a result." (The example was a $15,000 design fee plus $1,500 of furniture.)
- Answer 15, the conditions DOR names for a design fee to stay untaxed: "No tax is due on the Phase II services as long as the following requirements are met: design fees are separately stated; they are allocated in the contract to design only; the amount of the design fee is not contingent on the purchase of tangible personal property; the design agreement does not require the purchase of tangible personal property; and the contract provides for separate pricing of tangible personal property."
- Answer 17 (the agent versus buyer line): hourly fees for taking a client shopping "are not taxable as long as the billing for these services is clear and unless the Taxpayer and not the Taxpayer's client orders the tangible personal property. If the Taxpayer is making the purchases for its client, then the hourly fees are taxable as services that are part of the sale."
- Answer 14: where the client buys directly from a retail store, the designer "should not impute a sales tax amount" and the accompanying fee is "a nontaxable service as long as such fees are separately described and billed."
- Answer 10: "Taxpayer must collect Florida sales tax on freight, insurance, and delivery charges that are charged to clients ... because they are part of the cost of the item."
- Answer 18: the designer "is not permitted to remove its travel costs from the taxable sales price of the tangible personal property by treating them as separately reimbursed costs."
- Answer 13: cancellation charges (a purchasing fee and a restocking fee) "are solely for services, do not meet the definition of a taxable sale ... and are not subject to Florida sales tax, as long as such fees are separately described and billed."
- Answer 7 (deposits): "Tax is not imposed at the time that the deposits or down payments are made. However, the amount of tax applicable to the down payment or deposit will be due upon the delivery of the tangible personal property. The entire amount of the design fee is taxable at the time of the first sale of tangible personal property, the sales price of which includes that service."
- Discussion, third-party installers: "If Taxpayer sells tangible personal property and pays a third party to install it, and it remains tangible personal property after installation, it is likely that the labor charges will be taxable unless the installer can prove that no tangible personal property was used in the installation."
- Discussion, fixtures that become part of the building: the designer "should neither charge its clients tax for real property improvements nor should it give resale certificates to its vendors for materials and supplies used in its real property improvements" unless a specific exception applies (Rule 12A-1.051). This is another reason to stay away from hardwired fixtures.
- Binding scope: "This response constitutes a Technical Assistance Advisement under Article 213.22, F.S., which is binding on the Department only under the facts and circumstances described in the request." It is dated 2002 and warns that later rule or statute changes "may subject similar future transactions to a different treatment."

**Discrepancy to surface.** The conditions in answer 15 also appear in the TAA as *proposed* rule language for 12A-1.001, a longer seven-part list that includes "the client is not obligated to purchase tangible personal property from the decorator or designer" and "the amount of the consultation fee is not contingent upon whether the client purchases any tangible personal property." The current rule text I read (mirror) still has the old four paragraphs. So the seven-part test is `verified` as DOR's 2002 position and as proposed language, and `unverified` as codified law. Ask DOR or a CPA whether it was ever adopted.

**What this means for Hollie's two models.** `inferred` from the above.
- *Advisory (client buys direct from vendors, or buys from Hollie's shop through normal checkout):* a design or consult fee is untaxed only if it is solely for design, separately stated, not contingent on any purchase, and the client is not required to buy from Hollie. The weak spot is Hollie's own shop: if clients buy shop pieces from Hollie while paying a design fee, DOR can say the fee is "in conjunction with" the sale. Draft the agreement to hit every condition in answer 15.
- *Sourcing (Hollie buys, then resells):* tax the item, the markup, delivery and any bundled design, in-person, travel or rush fee. Charging "rush" on a sourced item is part of the sales price.
- *In-person fee:* untaxed only in the advisory model and billed clearly as a service. If Hollie then places a purchase order for the client, the hourly fee turns taxable (answer 17).
- Cancellation or restocking fees are service fees if separately described and billed (answer 13).
- TAA 19A-006, read on a mirror: "The mark-up fees and charges for reimbursable expenses are part of the sales price of tangible personal property and are subject to tax under sections 212.02(16) and 212.06(1)(a), F.S." and charges for storage and handling "that are marked up and passed on to the Client are part of the sales price subject to sales tax." `mirror`.

---

## 3. Deposits, non-refundable fees and cancellations

### 3a. FTC Cooling-Off Rule, 16 CFR Part 429

Source: https://www.ecfr.gov/current/title-16/part-429 (captured via the eCFR renderer API, raw `c5-ecfr-16cfr429-api.md`; a Cornell copy is `c5-cfr429-cornell.md`). FTC plain-language page: https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help (raw `c5-ftc-consumer-cooloff.md`). `verified`.

- 429.0(a): "Door-to-Door Sale—A sale, lease, or rental of consumer goods or services in which the seller or his representative personally solicits the sale, *including those in response to or following an invitation by the buyer*, and the buyer's agreement or offer to purchase is made at a place other than the place of business of the seller (e.g., sales at the buyer's residence or at facilities rented on a temporary or short-term basis, such as hotel or motel rooms, convention centers, fairgrounds and restaurants ...), and which has a purchase price of $25 or more if the sale is made at the buyer's residence or a purchase price of $130 or more if the sale is made at locations other than the buyer's residence, whether under single or multiple contracts."
- Excluded transactions, 429.0(a):
  - (1) "Made pursuant to prior negotiations in the course of a visit by the buyer to a retail business establishment having a fixed permanent location where the goods are exhibited or the services are offered for sale on a continuing basis."
  - (4) "Conducted and consummated entirely by mail or telephone; and without any other contact between the buyer and the seller or its representative prior to delivery of the goods or performance of the services."
  - (5) buyer-initiated visit "for the purpose of repairing or performing maintenance upon the buyer's personal property," and extras sold on that visit are not excluded.
- 429.0(b): "Consumer Goods or Services—Goods or services purchased, leased, or rented primarily for personal, family, or household purposes."
- 429.1(d): it is an unfair and deceptive practice to "Include in any door-to-door contract or receipt any confession of judgment or any waiver of any of the rights to which the buyer is entitled under this section including specifically the buyer's right to cancel the sale."
- 429.1(b) notice text (required): "You may CANCEL this transaction, without any Penalty or Obligation, within THREE BUSINESS DAYS from the above date. If you cancel, any property traded in, any payments made by you under the contract or sale, and any negotiable instrument executed by you will be returned within TEN BUSINESS DAYS following receipt by the seller of your cancellation notice."
- 429.1(e): the seller must also tell the buyer *orally*, when the buyer signs, of the right to cancel.
- 429.1(g): refund all payments within 10 business days of a valid cancellation.
- FTC consumer page: "The Rule also applies when you invite a salesperson to make a presentation in your home." It lists as not covered sales "made entirely online, by mail, or telephone."

**Wording discrepancy.** The regulation says "entirely by mail or telephone" and "without any other contact ... prior to delivery." The FTC consumer page says "entirely online, by mail, or telephone." So a sale closed on a website checkout before any visit being outside the rule is `inferred`, supported by the consumer page and by the rule's requirement that the seller "personally solicits." A *video-call* pitch followed by an e-signature is not clearly "mail or telephone." `unverified`. Needs attorney review.

**Application to the service.** `inferred`.
- *Covered:* a consumer (household) client invites Hollie to the home, Hollie proposes an in-person package or an upgrade there, and the client signs or agrees on the spot for $25 or more. Also covered: a sale pitched at a rented venue for $130 or more.
- *Likely not covered:* a virtual package booked and paid through the website before any visit. A corporate or business client (not "primarily for personal, family, or household purposes"). A sale closed after the client visited the shop's fixed location, if the shop counts as the "place of business" and the room is open on a continuing basis (exclusion (1)). The repair-visit exclusion (5) does not fit decorating.
- If an in-home sale is covered, the contract needs the 429.1 notice forms and the oral notice, and a "non-refundable" deposit cannot be kept after a timely cancel.

### 3b. Florida home solicitation sale law, 501.021–501.055

Source: https://www.flsenate.gov/Laws/Statutes/2026/Chapter501/All (raw `c5-ch501-all.md`). `verified`.
- 501.021(1): a "home solicitation sale" is a sale "of consumer goods or services with a purchase price in excess of $25" in which "(a) The seller or a person acting for him or her engages in a personal solicitation of the sale ... at a place other than the seller's fixed location business establishment ... and (b) The buyer's agreement or offer to purchase is given to the seller and the sale ... is consummated at a place other than at the seller's fixed location business establishment." It "does not include ... a sale, lease, or rental that results from a request for specific goods or services by the purchaser."
- 501.022(1)(b)2: the seller permit does not apply to "Solicitors, salespersons, or agents making a call or business visit upon the express invitation, oral or written, of an inhabitant of the premises or her or his agent." Also excluded: sales "by sample, catalog, or brochure for future delivery" (b)4.
- 501.025: "the buyer has the right to cancel a home solicitation sale until midnight of the third business day after the day on which the buyer signs an agreement or offer to purchase."
- 501.031: the agreement needs a conspicuous caption "BUYER'S RIGHT TO CANCEL" and a statutory paragraph ending "If you cancel this agreement, the seller may not keep all or part of any cash down payment."
- 501.041: the seller must tender payments back "Within 10 days."
- 501.045: "If the seller has performed any services pursuant to a home solicitation sale prior to its cancellation, the seller is entitled to no compensation for such services."
- 501.047(4): no one may "Allege or imply that the agreement ... is noncancelable when such is not a fact." 501.055: violation of ss. 501.025–501.047 is a first-degree misdemeanor.
- Reading: because a client who invites Hollie for requested design services is arguably outside 501.021(1) (a "request for specific goods or services") and outside the permit rule, the FTC rule is the safer one to build to. Florida's law may still reach an on-site upsell that the client did not request. `inferred`. Whether it reaches Hollie's invited visits at all is `unverified`; ask an attorney. Under 429.2(b) the FTC rule does not displace state law, so both can apply.

### 3c. FDUTPA, ch. 501 Part II

Source: same chapter capture. `verified`.
- 501.204(1): "Unfair methods of competition, unconscionable acts or practices, and unfair or deceptive acts or practices in the conduct of any trade or commerce are hereby declared unlawful." 501.204(2): "great weight" goes to FTC interpretations.
- 501.203(3): a "violation of this part" may be based on "(a) Any rules promulgated pursuant to the Federal Trade Commission Act ... (b) The standards of unfairness and deception set forth and interpreted by the Federal Trade Commission or the federal courts; or (c) Any law, statute, rule, regulation, or ordinance which proscribes unfair methods of competition, or unfair, deceptive, or unconscionable acts or practices."
- 501.2075: willful violations carry "a civil penalty of not more than $10,000 for each such violation." 501.211(2): a person who has "suffered a loss" may recover "actual damages, plus attorney's fees and court costs." 501.2105: prevailing party may get attorney fees.
- Relevance to "non-refundable": I read nothing in 501 Part II that bans a non-refundable fee. A fee buried in fine print, a fee that contradicts a cancel right the law gives, or credentials the business does not hold (a "licensed" or "certified" claim, "insured") fit "deceptive." `inferred`. Whether a court would enforce a non-refundable booking fee as liquidated damages rather than a penalty is contract law I did not research. `unverified`.

---

## 4. In-person installs: insurance and the contractor line

### 4a. Insurance norms

All `unverified` (insurer and agency pages, vendor claims; no Florida statute requires GL for a residential decorator that I read).
- Insureon, https://www.insureon.com/design-business-insurance/interior-designers (raw `c5-ins-insureon-interior.md`): general liability "covers basic third-party risks of interior design, such as accidental damage to a client's home. It's often required for a commercial lease." Also lists professional liability, a business owner's policy ("commercial general liability coverage and commercial property insurance together") and workers' comp ("required in almost every state for interior design firms that have employees"). Florida's employee thresholds were not read.
- The Hartford (home staging), https://www.thehartford.com/business-insurance/home-staging-insurance (raw `c5-ins-hartford-staging.md`): GL for claims "that it caused bodily injury or property damage to others," for example "accidentally damaging a client's luxury flooring"; commercial property for "owned or rented storage and studio space" and inventory. Its stated average cost for stand-alone GL is $678 a year. Vendor figure, not a Florida rate.
- Prestige Insurance, https://www.prestigeinsurance.com/blog/hoa-vendor-insurance-requirements-in-florida/ (raw `c5-ins-hoa-vendor-fl.md`): "a certificate listing the association as certificate holder does not make the association an additional insured." Where additional-insured status matters, "ask for the endorsement itself." Relevant to condo and HOA work in Lee and Collier. I found no per-occurrence limit figure on the pages, so I make no claim about a standard limit.
- Practical list (`inferred`): general liability; professional liability for design advice; coverage for shop inventory and client goods in transit or storage; an additional-insured endorsement on request. Ask an agent about what a policy treats as a "contractor" exclusion.

### 4b. The contractor line (ch. 489)

Source: https://www.flsenate.gov/Laws/Statutes/2026/Chapter489/All (raw `c5-ch489-all.md`). `verified` text unless noted.
- 489.105(3): "“Contractor” means the person who is qualified for, and is only responsible for, the project contracted for and means, except as exempted in this part, the person who, for compensation, undertakes to, submits a bid to, or does himself or herself or by others construct, repair, alter, remodel, add to, demolish, subtract from, or improve any building or structure, including related improvements to real estate, for others or for resale to others; and whose job scope is substantially similar to the job scope described in one of the paragraphs of this subsection."
- 489.127(1)(f): no person shall "Engage in the business or act in the capacity of a contractor or advertise himself or herself or a business organization as available to engage in the business or act in the capacity of a contractor without being duly registered or certified." (2)(a): first-degree misdemeanor; (2)(c): "during the existence of a state of emergency declared by executive order of the Governor commits a felony of the third degree." Also (1)(h): no one may "Commence or perform work for which a building permit is required ... without such building permit being in effect." And: "A business tax receipt issued under the authority of chapter 205 is not a license for purposes of this part."
- 489.128: a contract with an unlicensed contractor is "unenforceable in law or in equity by the unlicensed contractor," but "if a state license is not required for the scope of work to be performed under the contract, the individual performing that work is not considered unlicensed."
- **No general handyman exemption.** The text has no "handyman" exemption. The closest are: 489.103(9), "Any work or operation of a casual, minor, or inconsequential nature in which the aggregate contract price for labor, materials, and all other items is less than $2,500, but this exemption does not apply: (a) If the construction ... is a part of a larger or major operation ... or in which a division of the operation is made in contracts of amounts less than $2,500 for the purpose of evading this part ... (b) To a person who advertises that he or she is a contractor or otherwise represents that he or she is qualified to engage in contracting."
- 489.103(6): the chapter does not apply to "The sale or installation of any finished products, materials, or articles of merchandise that are not fabricated into and do not become a permanent fixed part of the structure, such as awnings."
- 489.117(4)(a)1: a person whose job scope "does not substantially correspond" to a listed contractor category "is not required to register with the board," and a local government may not require a license for such scopes, naming "handyman services" and "interior remodeling when the scope of the project does not include a task for which a state license is required." So general placement work is not a state-licensed category. `inferred` for Hollie's tasks.
- **Electrical, Part II (489.503 and 489.505).** 489.505(12): an "Electrical contractor" is one who has "the experience, knowledge, and skill to install, repair, alter, add to, or design ... electrical wiring, fixtures, appliances, apparatus, raceways, conduit," including anyone who "undertakes, offers to undertake, purports to have the capacity to undertake" electrical contracting. 489.503(5) exempts "The sale or installation of any finished products, materials, or articles of merchandise which are not actually fabricated into, and do not become a permanent fixed part of, the structure." I read all 24 exemptions in 489.503; none is a dollar-based minor-work exemption (the $2,500 item exists only in 489.103(9) for Part I). `verified` (absence).

**Where the line falls.** `inferred`; ask DBPR or a Lee or Collier building department to confirm.
- Likely no license needed: placing plug-in lamps, arranging furniture, laying rugs, styling shelves, hanging art and mirrors with hooks or anchors, hanging curtains, positioning pieces. These are finished articles that do not become "a permanent fixed part of the structure," and the work does not match a contractor category.
- Licensed trade or a permit needed: hardwiring a chandelier, sconce or fan; moving electrical boxes; plumbing fixtures; anything that needs a building permit; anything structural. Mounting a very heavy item into framing is a grey area. Keep the terms to picture hooks and standard wall anchors, and refer anything heavier.
- **Hire-through risk.** Because 489.105(3) says "by others," Hollie hiring and invoicing an electrician, painter or carpenter for a client is contracting. The client should hire the trade directly; Hollie recommends and coordinates only. Do not call it "project management" of a remodel.
- **Local.** DBPR's FAQ says an occupational license from the city or county may be needed (Lee County Tax Collector: https://leetc.com/businesses/ business tax receipts, raw `c5-lee-tc-business.md`; Collier's contractor licensing page, https://www.collier.gov/Business-Resources/Contractor-Licensing, raw `c5-collier-contractor-licensing.md`, repeats the felony-in-emergency warning). A business tax receipt is not a state license.

---

## 5. Ch. 538 and buying secondhand goods on behalf of a client

Prior work: `docs/site-ideas-and-consignment-synthesis.md`, "Florida gate." I did not redo it. Text below is from the prior capture of https://www.flsenate.gov/Laws/Statutes/2026/Chapter538/All (`research/consignment/raw/b3-fl-ch538-2026.md`). `verified` text; application `inferred` or `unverified` as marked.

- 538.03(1)(h): a secondhand dealer is one "engaged in the business of purchasing, consigning, or trading secondhand goods." (k): "“Transaction” means any purchase, consignment, or trade of secondhand goods by a secondhand dealer." (i): goods exclude "office furniture; pianos; books; clothing; organs; coins; motor vehicles; costume jewelry ..." so lamps, glass, art and decor are in.
- 538.06(1)(a): a dealer "may not sell, barter, exchange, alter, adulterate, use, or in any way dispose of any secondhand good: 1. That is a precious metal, a gemstone, or jewelry; an antique furnishing, fixture, or decorative object; or an item of art as defined in s. 686.501 within 30 calendar days after the date on which the good is acquired. 2. That is not described in subparagraph 1. within 15 calendar days after the date on which the good is acquired." (b): "antique" means "at least 30 years old and has special value because of its age."
- 538.06(2): a dealer "must maintain actual physical possession of all secondhand goods throughout a transaction."

**The agent versus buyer question.**
- *Hollie as principal (buys privately, then resells to the client):* Hollie is "purchasing ... secondhand goods" as a business, so each private-party purchase of a regulated item starts the 15 or 30 day clock. Because the hold bars "use," Hollie could not even stage the piece in a client's home inside the window. This is why "rush" cannot promise privately sourced secondhand pieces. `inferred`.
- *Exemptions that may take a purchase out of the chapter* (538.03(2)): (i) dealer to dealer when the selling dealer complied; (g) "Any person at antique, coin, or collectible shows or sales"; (k) an auction business; (f) a garage-sale operator holding fewer than 10 weekend sales a year. Whether the buyer on the other side of (f) or (k) is covered is `unverified`. Exemptions (l) to (n) (the antique-dealer-at-residence and website carve-outs) are discussed in the prior synthesis and still undecided.
- *Hollie as agent (the client is the buyer; title passes from the seller to the client; Hollie neither takes title nor resells):* the statute regulates "purchasing, consigning, or trading" by a dealer in the business. I found no sentence that exempts or covers an agent-buyer. The only agent language is 538.03(2)(h), which covers selling "as an agent for the property owner ... at that person's residence." Whether a purchasing agent falls outside the chapter is `unverified`. Ask a Florida attorney, DOR (which administers registration) and the Lee or Collier Sheriff's office.
- *Items from Hollie's own existing stock, held past the period:* a normal sale. The hold has already run. `inferred`.
- Agent mode also changes the tax picture (section 2): if Hollie places the order, the TAA treats it as a sale.
- Etsy or Shopify sales of the same stock are unchanged from the prior synthesis.

---

## Guardrail list (X verified, Y needs review)

1. Residential interior design and decorating need no state registration (481.229(6)(a)) **verified**; non-residential and event work in rented venues **needs review (ask DBPR)**. Statute verified, DBPR FAQ position needs review.
2. "Interior designer" is a free title (481.223(1)(b), DBPR FAQ) **verified**; "registered interior designer" and "architect" are barred **verified**. Whether "licensed" or "certified" claims are false depends on facts, so keep them off the page **(FDUTPA, inferred)**.
3. A pure advisory fee is untaxed and a bundled fee is taxed (12A-1.001(2)(a) on a mirror; TAA 02A-014 from the DOR PDF) **verified**; the exact drafting that keeps a design fee untaxed when clients also buy from Hollie, and whether the seven-part test was adopted, **needs review (ask DOR or a CPA)**.
4. The Annual Resale Certificate process and its limits (DOR page, 212.18) **verified**; use tax on props used before sale, and tax on party rentals, **needs review (ask DOR or a CPA)**.
5. The Cooling-Off Rule reaches buyer-invited at-home sales of $25+ (16 CFR 429.0(a)) **verified**; how it treats a video-call sale closed by e-signature **needs review (ask an attorney)**.
6. A non-refundable term cannot waive the cancel right on an in-home sale (429.1(d)) **verified**; whether a non-refundable booking fee on an online-signed contract is enforceable **needs review (ask an attorney)**.
7. Florida's home solicitation law text and its no-pay-for-services-performed rule (501.045) **verified**; whether it reaches Hollie's invited visits **needs review (ask an attorney)**.
8. Hardwiring needs a licensed electrician, and Part II has no $2,500 exemption (489.503) **verified**; "hanging art and placing lamps is fine" **inferred, needs review (ask DBPR or the county building department)**.
9. A contractor includes someone who acts "by others" (489.105(3)) **verified**; whether coordinating a client's own contractors crosses the line **needs review (ask an attorney)**.
10. Ch. 538 holding periods and the "use" bar (538.06) **verified**; whether a purchasing agent is outside the chapter **needs review (ask an attorney, DOR and the Sheriff's office)**.
11. Insurance norms **unverified** (vendor pages); ask a Florida independent agent for quotes and for any "contractor" exclusion language.
12. Local business tax receipt in Lee or Collier: DBPR FAQ says one may be needed **verified**; the county and city specifics **were not read**.

---

## Wording table

| Word or phrase | OK? | Why |
|---|---|---|
| interior designer, interior design, interior design firm | OK for homes | 481.223(1)(b): the paragraph "does not restrict the use of the name or title “interior designer” or “interior design firm.”" DBPR FAQ: not a protected title. Commercial services: see guardrail 1. |
| designer, design consultant, decorator, interior decorating | OK | Not on the 481.223(1)(b) list. 481.203(9) defines "interior decorator services"; 481.229(6)(a) exempts them for residential work. |
| stylist, styling, e-design, virtual design, room refresh | OK | Not on the prohibited list (absence verified). |
| space planning, furniture layout | OK for homes | Part of "interior design" (481.203(10), (15)); exempt for residential (481.229(6)(a)). |
| placing, arranging, hanging art, placing lamps, curtains | OK | Finished articles not fixed into the structure (489.103(6), 489.503(5)); not a contractor category (489.117(4)(a)1). `inferred` |
| registered interior designer, RID | NO | 481.223(1)(b); first-degree misdemeanor, 481.223(2). |
| architect, architectural plans or drawings | NO | 481.223(1)(a)–(b); "interior design" excludes architectural work (481.203(10)). |
| licensed designer, state-licensed, certified designer, NCIDQ | NO unless true | A false credential is "deceptive," 501.204(1). `inferred` |
| insured, fully insured | NO until a policy is bound | Deceptive if untrue, 501.204(1). `inferred` |
| contractor, builder, general contractor | NO | 489.127(1)(f) bars advertising as available to act as a contractor; also forfeits the 489.103(9) exemption, (9)(b). |
| remodeling or renovation services, "we handle your remodel," project management of a build | NO | 489.105(3) ("by others"); 489.127(1)(f). Use "styling and selections for your remodel." |
| install lighting or fixtures, hardwire, electrical, plumbing | NO | 489.505(12) ("fixtures"); 489.503; 489.127(1)(h) (permit work). |
| handyman | AVOID | 489.117(4)(a)1 names it as an unlicensed local-government scope, but advertising it invites the contracting question. `inferred` |
| office, restaurant or commercial interior design | REVIEW | DBPR FAQ requires registration for commercial services; statute silent (section 1). |
| non-refundable | OK only if conspicuous, defined, and kept off in-home-signed agreements | 429.1(d); 501.204(1); 501.025/501.045. |
| "Fabulous From Online" (service name) | OK | Not a regulated term. Business-name registration was not researched. `unverified` |

---

## Terms checklist (the service terms must state)

- **Deposit:** the amount, what it covers, whether it is credited to items or fees, and when it becomes non-refundable. State it plainly, in the same language as the sales conversation. Book and take the deposit online before any visit.
- **Cancellation:** the client's cancel window and what is kept after work starts. If a covered in-home sale is possible, add the FTC notice of cancellation (429.1) and Florida's "BUYER'S RIGHT TO CANCEL" paragraph (501.031), and say that the deposit is returned within 10 days of a valid cancel.
- **Who owns purchased items:** title and risk of loss under each model. *Sourcing:* Hollie buys and resells, so title passes to the client at delivery or payment, and risk of loss is stated. *Advisory:* the client buys directly from the seller and owns the item from that moment.
- **Returns on sourced items:** vintage pieces are one of one. State final sale versus a defined return window, who pays shipping, and a condition-disclosure promise. Cancellation or restocking fees should be separately described and billed (TAA answer 13).
- **Rush:** rush does not apply to privately bought secondhand pieces (15 or 30 day hold). It applies to Hollie's own held stock, new goods, or compliant-dealer sources. `inferred`
- **Sales tax:** show each fee line and say whether it carries tax. Show markup or disclose that sourced items carry a markup. Disclose any trade discount Hollie keeps (DOR treats it as a taxable fee).
- **What in-person work excludes:** hardwiring or any electrical connection, plumbing, anything needing a permit, structural mounting beyond picture hooks and standard wall anchors (`inferred`), moving very heavy items, work at heights, and hiring trades on the client's behalf. The client contracts any trade directly.
- **Access and property:** the client confirms the right to authorize work (a renter or condo owner may need association approval and a certificate of insurance), pets and pre-existing damage are photographed, and a limit-of-liability clause is in place. Keep the insurance line off the page until bound.
- **Scope:** residential only unless an attorney clears event or commercial work. Define "room," "corner" and "entire house" as the priced tiers.

---

## Not retrieved or walled

- DOR brochure GT-800052: 404 (page no longer exists). 455.228: 35 bytes (wall). TAA 19A-006 primary PDF: guessed URL 404; mirror only. Rule 12A-1.001 on flrules: metadata only; Cornell mirror used.
- Not researched: Florida fictitious-name registration, local business tax receipt specifics for Lee or Collier, county discretionary sales surtax rates, the taxability of party rentals, Florida workers' comp thresholds, liquidated damages case law, photo or copyright releases.
