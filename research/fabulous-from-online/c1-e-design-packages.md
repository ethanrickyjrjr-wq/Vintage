# c1: e-design packages and pricing

Agent c1, accessed 2026-10-28.

Raw captures: `research/fabulous-from-online/raw/c1-*`.
Method: SearXNG (`tools/search.sh`) for URLs, crawl4ai (`tools/crawl.sh`) for pages, about 30 pages read. WebFetch and WebSearch were used only as fallbacks: WebFetch for one Etsy rush listing (HTTP 403), The Expert FAQ (headings only) and a failed A Vintage Splendor fetch (SSL error); WebSearch for two summary searches on rush fees and The Expert prices. Anything that came from WebSearch is a search-engine summary, not a read page, and is tagged `unverified`. Tags: `verified` = read on a live page this session; `inferred` = my reading or arithmetic; `unverified` = second-hand, snippet-only or unreadable. Prices are US dollars. Shop name throughout: Holliewood & Vine.

## TL;DR

1. **The market has two price floors.** National platforms sell a room for about $199 list (Havenly, Spacejoy) up to $599 to $2,049 (Decorilla, depends on room and designer tier) and make their margin on the shopping. Independent designers charge $450 to $2,100 per room. Micro-services (one question, one shelf, one table) run $75 to $500. Business of Home put it plainly: "You have to figure out whether you make most of your money on the design part or the shopping part. Most major platforms are doing the latter." Hollie sells the goods, so this is Hollie's model too.
2. **The big e-design platforms are fragile; the person is the product.** Modsy stopped offering design services on June 29, 2022 and ceased operations July 6, 2022. Laurel & Wolf and Homepolish shut in 2019 (as reported by TechCrunch). Laurel & Wolf is now an AI photo-restyle subscription ($19 to $99 a month). What survives is a named designer with taste (The Expert, Mix & Match, Black Cat).
3. **Micro-packages are real and priced.** One question: $75 (Insighed, 30 min), $95 (Black Cat, written answer in 2 to 3 business days), $175 (Mix & Match, 30 min), $180 (Safra). Shelf or vignette: $105 to $150 (Black Cat), $425 (Sandringham "Mini Vignettes"), $500 (Black Brick, up to 10 items). Table or seasonal: $295 to $495 (Noeka). These map directly to Hollie's party and event use case.
4. **Intake is always photos, measurements, a questionnaire, inspiration images and a budget.** Nobody asks for a client video walkthrough. Mix & Match (live call plus a recording) and The Expert (show the space on camera) are the closest. A "show me the room on a video call" step is a small differentiator for Hollie, not a standard.
5. **Standard deliverables:** a style or concept board, a floor plan or furniture layout, and a shopping list with links. Revisions are almost always 1 to 3 rounds; extra time is billed hourly ($75 to $200 an hour). Turnaround is 1 to 3 weeks (Design Hub about 1 week, Spacejoy 10 business days, Safra 2 to 3 weeks, Noeka 3 to 4 weeks).
6. **No interior e-design page I read publishes a rush fee.** Treat any rush price as `inferred`. The closest verified signals are Design Hub's "Priority turnaround" on its top tier and Spacejoy's 7 to 10 business days on its top tier versus 10 on the lower ones. In-person is priced as a big step up: Havenly lists $699 in person versus $199 online (about 3.5 times); Annie Wise charges $475 for a 90-minute in-person consult plus $50 beyond 15 miles.
7. **Nobody publishes a priced e-design package built from vintage or secondhand pieces.** ThriftSpace is a matching marketplace with no project prices and unclear traction; Antiques & Interiors and Odloft offer antique sourcing with no published price; Vintage Soul Designs is vintage in name only. That is the open lane for Holliewood & Vine.
8. **Recommended ladder (details at the end):** One Find $95 to $175 · A Corner $195 to $495 · A Room $650 to $1,250 · Whole House quoted by room count with about 10% off rooms two and up. In-person is an upgrade of roughly $250 to $500 per visit; rush is an `inferred` +25% (minimum $75), not a market-proven number.

---

## National services

### 1. Havenly

- Homepage: https://havenly.com/
- Pages read: `/pricing` (raw `c1-havenly-pricing.md`), `/in-person` (`c1-havenly-inperson.md`, thin: the market list did not render), `/faq` (`c1-havenly-faq.md`, navigation only, nothing usable). Accessed 2026-10-28.
- Evidence:
  - Two products, both promo-priced on the day: "Online ~~$199~~ **$89** You save $110" and "In-Person ~~$699~~ **$299** ... 50% OFF", with "Use code **BF26** Ends Tuesday 11/3". `verified`. I read the struck-through numbers as the list prices (`inferred`), so the anchors are $199 online and $699 in person.
  - FAQ on the page: "Online design starts at $89 per room. In-Person design starts at $299. No hidden fees, no surprises." `verified`
  - Included in both: "A real Havenly designer, matched to your style", "A video call to collaborate with your designer", "A finished design plan for your room", "3D renderings, so you see the room before you buy anything", "A custom floor plan, so you know what fits and where", "Revisions until it feels like yours, not just close", "A shopping list made for your room", "Hundreds of brands at members-only prices". `verified`
  - Intake: online is "You share photos", in-person is "We visit your home". Contact: "Video call, chat, or text" versus "In person, at home". `verified`
  - Who buys: online "You shop your list"; in-person "We source and order". `verified`
  - Turnaround: "Online designers typically deliver your first concepts in 3 to 14 days. In-Person timelines are set with your designer based on your project." `verified`
  - Refund: "Love your design, or it's free" and "Happiness guaranteed". `verified`
  - Existing furniture: "Yes. Tell your designer what's staying, whether it's a sofa you love or a hand-me-down, and they'll design around it." `verified`
  - Trade pass-through: "Exclusive discounts on hundreds of brands" (members-only prices, not a stated trade rate). `verified`
  - In-person locations in the footer list Denver, Houston, Austin, Dallas, Chicago, New York plus "View All Locations". Florida is not in the six shown; whether Havenly covers SWFL is `unverified`.
- Steal this: the two-product structure (same deliverables, online versus we-come-to-you) with in-person priced at roughly 3.5 times online, and the plain line "Revisions until it feels like yours, not just close". Also the promise to design around a client's keeper pieces.

### 2. Decorilla

- Homepage: https://www.decorilla.com/
- Pages read: `/pricing` (`c1-decorilla-pricing.md`), `/pricing/living-room` (`c1-decorilla-living-room.md`), `/faq/cost-and-fees` (`c1-decorilla-faq-fees.md`). Accessed 2026-10-28.
- Evidence:
  - Prices are a flat rate per room type chosen from a dropdown. The default capture (Hallway/Entry) shows "BRONZE $599 SILVER $859 GOLD $1,099". The Living Room page shows "BRONZE $849 SILVER $1,099 GOLD $2,049". So the "$599" headline is the cheapest room, not a flat price. `verified`
  - A "$120 OFF" promo banner is live (e.g. "$849 ... $120 OFF $729"). `verified`
  - Tier meaning (FAQ): Bronze = "skilled junior designers", Silver = "more seasoned designers", Gold = "top-rated, highly experienced designers". Platinum = "architectural drawings, seamless coordination with contractors ... a dedicated project manager", "Starting from $1,980". `verified`
  - "Choose Multiple Rooms (Save 10%)". `verified`
  - Hourly: "Hourly Interior Design Services ... $119/h - $500/h" and "an hourly rate of just $119 to $500, depending on the experience level of the designer". `verified`
  - Deliverables (FAQ): "every client receives a comprehensive design package that includes two initial design concepts, a finalized design with floor plan, 3D renderings, and a tailored shopping list." Each tier: "2 experienced designers submit concepts for you" (Bronze), "2 greatly experienced designers" (Silver), "2 industry leading designers" (Gold). `verified`
  - Refund and payment: "We don't release the payment until you approve the work" and "100% Satisfaction Guarantee". `verified`
  - Comparison-table rows listed under Decorilla: "Unlimited Communication", "Realistic 3D Model", "Concepts From Multiple Designers", "Trade Discounts on Furniture", "No Markups or Sale Pressure". The check marks did not render in the crawl, so that these are Decorilla claims is `inferred`.
  - Revision count and turnaround are not stated on the pages I read. One testimonial says "I had my design ready in weeks", which is not a policy. `unverified`
- Steal this: pay-on-approval language, and the designer-experience tier names (here the tiers are about who designs, not how much you get). For Hollie, tiers should be about scope, not seniority, since there is one designer.

### 3. Spacejoy

- Homepage: https://www.spacejoy.com/
- Pages read: `/pricing` (`c1-spacejoy-pricing.md`), `/refund-policy` (`c1-spacejoy-refund.md`). Accessed 2026-10-28.
- Evidence:
  - Three plans, priced per room: "delight $199 ~~List price $399~~ / room ... Design per room - 1 concept ... 10 business days to design delivery ... Work 1:1 with a professional designer"; "bliss $399 ~~List price $599~~ ... 2 concepts ... 10 business days ... senior designer" ("Most chosen"); "euphoria $599 ~~List price $799~~ ... 2 concepts ... 7-10 business days ... SENIOR designer". `verified`
  - A banner advertises "Get Exclusive 40%OFF On All Design Packages ... Use code: SPOOKY40". Whether the $199/$399/$599 shown already include that discount is unclear: X verified (banner and prices both on the page), Y need review (the relationship between them).
  - Included: "A real designer and 3D designs of your own room, priced per room. First designs within 10 business days. Furniture is optional." "A Spacejoy designer works with you 1:1 and delivers 3D designs of your room, a floor plan and a shoppable list. Revisions are included in every package; the number depends on the package." `verified`
  - Who buys: "Furniture is optional: buy it with us, elsewhere, or keep what you own." Budget: "you share your furniture budget with your designer, who sources products that match it." `verified`
  - Multi-room: "Every package is priced per room ... If a multi-room discount applies, it is taken off automatically." No percentage given. `verified`
  - Refund: "Full refund within 48 hours of ordering", "A new designer if it's not a fit". Policy text: "Partial refunds will only be considered for those projects that have been delivered within 4 months of the project start date. After 4 months, no design refunds will be issued." "Make sure to send in your feedback with design changes within 30 days of receiving your latest design concept." "You can choose to come back and kickstart your project ... anytime within a year." `verified`
  - The comparison table lists "Video consultation with designer", "Design revisions", "Designer curated shopping list", "Ultra-realistic 3D images", but the per-tier check marks did not render. Per-tier revision counts and which tier gets a video call are unknown. `unverified`
- Steal this: refund tied to when work starts ("a designer is assigned as soon as you place the order") and the 30-day feedback window; both are fair, short and easy to write in Hollie's voice.

### 4. Modsy (shut down)

- Homepage: https://www.modsy.com/ (not read).
- Pages read: TechCrunch 2022-06-29 (`c1-modsy-techcrunch.md`) and TechCrunch 2022-07-17 (`c1-modsy-techcrunch-jul.md`). Accessed 2026-10-28.
- Evidence:
  - June 29, 2022: Modsy "has ceased to offer design services". `verified`
  - July 17, 2022: "Capital constraints and uncertain market conditions forced the company to cease operations on July 6 and lay off all employees". Assets went to a "new entity" (Pencil, LLC) via an assignment for the benefit of creditors. `verified`
  - So: design services ceased about June 29, 2022; the company ceased operations July 6, 2022. Both `verified`; I did not find a single "shutdown date" that all sources agree on, so quote both.
  - Intake (useful as a benchmark): "Modsy had customers snap photos and take measurements of their rooms and complete a style quiz indicating their preferences, budget and constraints." `verified`
  - Customer harm to avoid: refunds went through "a Google Form" and "five of the seven customers ... either hadn't heard from the company or received boilerplate emails". `verified`
  - Also reported by TechCrunch (citing Business of Home): "Laurel & Wolf and Homepolish shut down in 2019, and Décor Aid, smaller company, shuttered in 2021." `verified` as reported; the underlying Business of Home article was not read in full.
- Steal this: nothing to copy; the lesson is to hold deposits for a short time, state the refund rule up front, and never depend on a platform for the deliverable.

### 5. Laurel & Wolf (now an AI app)

- Homepage: https://laurelandwolf.com/
- Pages read: home (`c1-laurelwolf-home.md`); Business of Home "Laurel & Wolf is back" (`c1-laurelwolf-boh.md`, headline only, I attribute nothing from its body). Accessed 2026-10-28.
- Evidence:
  - Current product is not human e-design: "Upload a photo of your actual room, pick from 13 designer styles, and get a photorealistic redesign back in about two minutes." `verified`
  - Pricing: "Starter $19 /month ... 8 photos every month", "Pro $39 /month ... 20 photos every month", "Studio $99 /month ... 55 photos every month"; "Up to 20 free revisions per photo"; "First photo free". `verified`
  - Aimed first at real estate staging: "Real estate agents started it". `verified`
  - The 2019 shutdown is from TechCrunch (section 4), not from this site. `verified` as reported.
- Steal this: nothing on price. It shows the cheap end of the market is now a $2-per-photo AI tool, which is why Hollie's offer should lean on a human with real objects in hand.

### 6. The Expert (paid video consults with top designers)

- Homepage: https://www.theexpert.com/
- Pages read: `/consultations` (`c1-theexpert.md`), `/consultations/find-an-expert` (`c1-theexpert-find.md`, navigation only), FAQ via WebFetch (question headings only, no answers). Secondary: Teresa Wu Substack review (`c1-expert-review-substack.md`), Decorilla's review of The Expert (`c1-decorilla-expert-review.md`), Business of Home 2021 (`c1-boh-expert-2021.md`). Accessed 2026-10-28.
- Evidence:
  - Live site shows no prices. Steps: "Find an Expert", "Book a Video Consultation: Choose the length of consultation you'd like to book and a time that works for you", "You'll receive a link to your consultation via Zoom so you can meet your Expert face to face". `verified`
  - Teresa Wu (June 22, 2024): "Sessions vary in length from 25 to 115 minutes, with prices ranging from $300 to $3,000+." She "paid $750 for 55 minutes". Intake: "fill out a brief questionnaire and have the option to upload any docs ... screenshare, show your space through your laptop camera". `verified` that the review says this; it does not verify what The Expert charges today.
  - Decorilla (a competitor) says: "prices ranging from $200 to $3,600", "starts at $200 for a 25 minute consultation", sessions "typically ... 55 minutes long, but some designers offer extended sessions of 85 and 115 minutes", and a "No Refund Available" heading. `verified` that the review says this; competitor source.
  - Business of Home, 2021: "Arnold has upped his rate to $1,250 for an hour" and "An hour of Bullard's time will cost customers $1,500". The same article says a rival platform's decor designers charged "$39 per session up to $150". `verified` as reported; 2021, likely stale.
  - The low end disagrees: Decorilla says $200 verified, Wu says $300 verified, and neither is The Expert's own page: X verified, Y need review.
  - The Expert's FAQ lists "What is your consultation refund policy?" and "What happens if I'm dissatisfied ..." as questions, but the answers were not readable. Refund policy is `unverified`.
- Steal this: a session is sold by length (25, 55, 85, 115 minutes). For Hollie, length-based call tiers ($ per 30, 60, 90 minutes) are the cleanest way to sell "describe what you want" and "meet virtually".

---

## Independent designers (e-design package pages)

### 7. Michele Safra Interiors (New York and Miami)

- Homepage: https://michelesafra.net/
- Page read: `/e-design/` (`c1-safra-edesign.md`). The page source carries a 2020-07-11 timestamp and a 2025 copyright line, so prices may be stale (`inferred`).
- Evidence:
  - Tiers: "Jump Start **$450-$1500**" (Basics questionnaire, concept board with furniture inspiration, color palette, key design ideas); "Full Service **$950-$2800**" ("Two revisions", "Floor Plan & Furniture Plan", "Shopping list with links and budget"); "One Question Consult **$180**" ("choosing paint color for one room", "resourcing one item such a rug, sofa etc.", "suggestions for revamping one piece of furniture"). `verified`
  - Price depends on room size: "a flat fee per room which varies depending on the size of the room". `verified`
  - Intake: "Photograph + measure your space and any furniture you wish to keep", "Complete a design questionnaire", "Submit inspirational images that you love". `verified`
  - Turnaround: "within 2-3 weeks via e-mail" as a PDF. `verified`
  - Who buys: client by default; optional "PURCHASING OF PRODUCTS (COST+15%)": "We will extend our full trade discount (that can go up to 50% for some vendors) and will charge you 15% of our net purchasing price (trade price)". `verified`
  - Extras: "FLOOR PLAN ... OR ADDITIONAL PLAN REVISIONS ($75/ hour)", "ADDITIONAL COLOR PALETTE OPTIONS ($150/room)", "HOURLY SKYPE CHAT WITH MICHELE ($450)". `verified`
  - Revisions: "up to two re-selections per design package at no charge". `verified`
  - Stock risk: "What happens if I wait to purchase an item, and then it's no longer available? You can always shop for a similar item if something becomes discontinued." `verified`
- Steal this: the "One Question Consult" named package (and that "resourcing one item" is the example), and the cost-plus purchasing menu. Safra's stock-risk answer is the exact problem Hollie has times ten, because every vintage piece is one of one.

### 8. Stellar Interior Design

- Homepage: https://www.stellarinteriordesign.com/
- Page read: `/design/` (`c1-stellar-edesign.md`). Accessed 2026-10-28. Location not stated on the page I read.
- Evidence:
  - "Room Design Package #1: $475" (inspiration boards, product source list, paint palette and custom fabrics, design notes); "Room Design Package #2: $575" (adds "Floor Plan to scale"); "Paint Color Consultation: $95" (3 paint schemes of 3 colors, 1 week). `verified`
  - À la carte: "Floor Plan ... $200", "Elevation ... $200", "Design Consultation ... $150/HR". `verified`
  - Intake: "You provide us with your room sizes, photos, budget". Turnaround: "Please allow 1-2 weeks for delivery. Concept package priced per room/space". `verified`
  - Revisions and refund terms are behind "FAQs" and "Refund Policy" links I did not open. `unverified`
- Steal this: one room, two prices, and the second adds only the floor plan. Easy to explain and upsell.

### 9. Mix & Match Design Co. (virtual consultations)

- Homepage: https://mixandmatchdesign.com/
- Page read: `/virtual-consultation` (`c1-mixandmatch.md`). Accessed 2026-10-28.
- Evidence:
  - "30 MINUTES The Quick Check $175", "60 MINUTES The Design Consultation $300 (Our most popular and versatile option)", "90 MINUTES The Deep Dive $425". `verified`
  - Included: "Live Google Meet consultation", "Recording", "Links to products/resources discussed". `verified`
  - Intake: "a short questionnaire ... photos, measurements, floor plans, inspiration images, Pinterest boards, product links". `verified`
  - Live sourcing: "we can shop together live and I'll show you what I'd choose and why." `verified`
  - Limits: "Additional sourcing, drawings, mood boards, renderings and ongoing design work aren't included". `verified`
  - Refund: "cancel ... at least 48 hours before ... to receive a full refund. Cancellations made within 48 hours ... and missed appointments are nonrefundable." `verified`
  - "Payment is due at booking." `verified`
- Steal this: the session names (Quick Check, Design Consultation, Deep Dive), the call recording, and shopping live on the call. For Hollie, "shopping live" can mean pulling pieces from stock on camera.

### 10. Dwelling Envy Interiors

- Homepage: https://dwellingenvyinteriors.com/
- Page read: `/e-design/` (`c1-dwellingenvy.md`). Footer reads "2018- 2024", so prices may be a year or two old (`inferred`).
- Evidence:
  - "REVIVE A ROOM starting at $749": "pillows, accent rugs, artwork, lighting, paint or wall coverings, and accent furniture"; includes Custom Online Design Portal, 2D Design Board, Detailed Design Rationale, Shoppable Product Board. "Not Intended for Kitchen or Bathrooms." `verified`
  - "TOTAL ROOM DESIGN starting at $1,499": adds Floor Plan Layout, 3D Conceptual Renderings, "30 Day Post Design Follow-Up". "Open Concept Design is subject to additional charges." `verified`
  - "3D RENDERING SERVICE starting at $500"; "DESIGNER SIDEKICK $125 / HR" (phone, email, Google Meet, Zoom, Facebook Chat). `verified`
  - Intake: a Discovery Call, an online style survey, a photo-and-measure resource guide; then "within 24 - 48 hours, you'll receive your LOA (Letter of Agreement) complete with your Custom Flat Rate Quote". `verified`
  - "All flat-rate services include one round of minor revisions at no additional cost." `verified`
  - Who buys and markup: "you never pay more than retail on any products chosen for your space. You also order on YOUR timeline." "I'm here to answer any follow-up questions for a full 30 days after your purchases are made." `verified`
  - Discrepancies on the same page: the design portal is available "24/7 for 1 year" in one block and "six months" in another; delivery is "two to three weeks" in one place and "as little as 3-4 weeks" for Total Room. X verified (both statements exist), Y need review (which is current).
- Steal this: a "Revive" tier for rooms that are almost there (finishing touches only), and the 30-day post-purchase question window. Also a client-facing page that lasts a year.

### 11. Black Cat Interiors (micro-services, best source for small packages)

- Homepage: https://www.blackcatinteriors.com/
- Pages read: `/product-category/micro-services/` (`c1-blackcat-micro.md`), `/product/hourly-a-la-carte/` (`c1-blackcat-hourly.md`), `/product/front-door-consultation/` (`c1-blackcat-frontdoor.md`), `/product/shelf-styling/` (`c1-blackcat-shelf.md`). Accessed 2026-10-28.
- Evidence (the full "Micro Services" category lists 7 items):
  - "Designer On Call (Hourly Interior Design Help) $95.00": "A focused, one-question consult"; "Responses are delivered within 2-3 business days." Questions like "Should I buy this, or keep looking?" `verified`
  - "Shelf Styling ~~$150.00~~ $112.00": "Custom Shelf Styling, Up to 6 Shelves"; "to-scale photorealistic styling showing exactly what goes where, using pieces you already own (if preferred) along with new recommendations"; "Shopping lists will be provided as Pinterest boards." `verified`
  - "Custom Gallery Wall Design $105.00"; "Front Door Consultation $75.00" (4 mockups plus 3 additional variations); "Custom Holiday Decorating Design $99.00" ("One realistic visualization ... personalized shopping list with product links ... one round of edits. Delivered in 7-10 business days. ... décor purchased separately"); "Content Creator Backdrop ... $145.00"; "Designer Insider $49.00 / Month" ("Up to 3 hours of personalized support each month"). `verified`
  - Price shown can be a sale price (shelf styling), so the real anchor is $112 to $150. `verified`
- Steal this: a shelf menu of seven tiny, named, priced products, each with a single deliverable. The "Should I buy this, or keep looking?" line is a ready-made hook for "One Find". The monthly "Designer Insider" is a retention idea (not recommended for launch).

### 12. The Black Brick Co. (furniture retailer selling e-design)

- Homepage: https://theblackbrickco.com/
- Page read: product `Shelf Styling & Accessories E-Design Package` (`c1-blackbrick-shelf.md`). Accessed 2026-10-28.
- Evidence:
  - "Regular price $500.00"; "styling open shelves, bookcases, coffee tables, or side tables ... up to 10 handpicked items, which may include decorative objects, frames, wall hangings, art, and pillows." `verified`
  - Process: purchase, designer outreach, "comprehensive design consultation over the phone", client provides "Measurements and photos of your current space" and "2-3 inspiration images". `verified`
  - Deliverables across the e-design line: floor plan, inspiration images, design board, shopping list. It is not clear that every item applies to the $500 shelf package. `unverified` for this product.
  - "This package includes one round of revisions. If additional revisions are required, time will be billed at the rate of $150 an hour." `verified`
- Steal this: pricing a styling job by item count ("up to 10 handpicked items"), a unit that works for one-of-one pieces. Also: a goods retailer using e-design to sell its own catalog, which is the Hollie model.

### 13. Noeka Home (Houston; sells goods and design)

- Homepage: https://noekahome.com/
- Page read: `/pages/virtual-design` (`c1-noeka.md`). Accessed 2026-10-28. Houston is from the page's "Shop Houston" and phone area code (`inferred`); the "Palm Beach Preppy" collection names are a style, not a location.
- Evidence:
  - "Classic Room Design $450 per room" (style board, layout recommendations "not to scale", product links, "Up to three iterations"); "Comprehensive Room Design $650 per room" (adds "Representative renderings"); "Finish Selection Plan $650 per room"; "Renovation Design Plan $950 per room"; "Virtual Tablescape Design $295 per table*" (up to six place settings; "Up to two iterations"); "Seasonal Decorating E-Design $495 per room". `verified`
  - Add-ons: "Renderings starting at $500"; "Optional purchasing support add-on". `verified`
  - Turnaround: "Most e-design projects are completed within 3-4 weeks from your kickoff date"; room packages "3 weeks". A week-by-week timeline is published (kickoff call within 2 to 3 business days, first concept 3 to 4 business days after). `verified`
  - Shop-and-design link: "Clients also enjoy 10-15% off most products offered directly through us. Exclusions apply." `verified`
  - Promo: "DESIGN FEE CREDIT EVENT: Up to 50% Off Design Packages", with codes EDESIGN40/45/50 for 1, 2, or 3+ rooms. This discounts the design fee; it is not a credit toward purchases. `verified`
- Steal this: the table package ($295, six place settings) for parties; a seasonal package; a published week-by-week timeline; 10 to 15% off goods for design clients. This is the closest model to Hollie.

### 14. Sandringham Interiors

- Homepage: https://www.sandringhaminteriors.com/
- Pages read: `/pricing-services` (`c1-sandringham-pricing.md`), `/edesign` (`c1-sandringham.md`). Accessed 2026-10-28. Location not stated on the pages I read.
- Evidence:
  - "Designer on Call Consulting $175 (1 hr min call or In-home visit)": the same price for a call or a home visit. "does NOT include any concept boards, digital renderings or floor plans." `verified`
  - "Accents & Accessories Service - 'Mini Vignettes' $425" (a product board plus "A clickable Shopping List with Vendor Links"). `verified`
  - "Concept E-Design Service (Best Value) $875": one hour call or in-home consultation, one room concept "w/two Concept Board edits", one wall elevation, shopping list. `verified`
  - "Full Service E-Design Service $2100": adds floor plan, final 3-D rendering, installation instructions. "Multi-Room Discount Offers Available." `verified`
  - Process: "Within 4-5 days, we will send over an initial concept board ... Two Revisions are included"; "approximately 10 - 15 days from the date of your completed questionnaire". Intake: "3-4 photos", a measuring guide, a questionnaire, then "a 30-40 minute conference call". `verified`
  - Refund: "Refunds are not available for Design Services upon receipt of final design(s)". Fees "required up front". `verified`
- Steal this: pricing a call and a home visit the same, and the "Mini Vignettes" name. Four prices from $175 to $2,100 is a clean ladder.

### 15. Short entries (read, lower priority)

- **Vintage Soul Designs** (Frederick County, Maryland) https://www.vintagesouldesigns.com/ , `/e-design-packages` (`c1-vintagesoul.md`): "The Basic Package ... Prices start at $350" (mood board, no shopping links); "The Essentials package ... start at $500" (two or three furniture pieces with direct links, "up to 2 revision"); "Full Design Package ... between $700-$1000" (floor plan, "up to three revisions"). `verified`. The page says nothing about vintage or secondhand sourcing, so the name does not make it a vintage service. `verified` that it is silent.
- **Insighed Designs** (Madison, WI) https://insigheddesigns.com/ , product page (`c1-insighed-30.md`): "Virtual Interior Design Consultation $75.00 ... Schedule your 30-minute virtual consultation". `verified`
- **Design Hub Home** https://designhubhome.com/ , `/virtual-design` (`c1-designhub.md`): three flat-fee tiers, price "quoted when you book" (no number published). Room Refresh = "Shoppable list, 8 to 12 pieces", "1 revision round", "about 1 week"; Full Room Design = "15 to 25 pieces", "2 revision rounds", "30 minute video call with your designer"; Whole Space = "Up to 3 connected rooms ... Priority turnaround". "Your shoppable list is yours" but showroom items carry member pricing. `verified`. This is the only page where "priority turnaround" is a tier feature.
- **Annie Wise Design** https://www.anniewise.com/ , `/product-page/90-minute-consult` (`c1-anniewise-90.md`): "90 Minute Design Consult" in person, $475; "A $50 additional charge incurred for projects outside a 15 mile radius"; "additional time will be charged at $200 per hour, in 15 minute increments"; deliverable "a Google Slide Presentation"; "Design fees are refundable (less processing fees) prior to date of Consult." `verified`
- **E-Design Interiors** https://e-design-interiors.com/ , `/e-design-faq/` (`c1-edesigninteriors-faq.md`): a 20-minute intro Zoom and 20-minute wrap-up; "additional zoom consultations at a rate of $75.00 per 30 mins"; "up to three re-selections at no charge"; "a reselection option for $75.00 for 4 replacement pieces". `verified`
- **Pages read but not used:** Tanna By Design `/interior-design/virtual-interior-design` (`c1-tanna.md`): packages exist but no prices on the page. Wellbuilt Florida `interior-design-consultation-cost` (`c1-wellbuilt-fl.md`): reads like generated filler ("SEER and tonnage do not apply here" on a design page); low credibility, not used for any number.

---

## Local anchor (assumption: Lee and Collier counties)

### 16. Pure Design of Naples (Naples, FL)

- Homepage: https://puredesignofnaples.com/
- Page read: `/interior-designer-cost-naples-fl/` (`c1-puredesign-naples.md`). This is a firm's own marketing page for full-service work, so it shows local full-service prices, not e-design prices. Accessed 2026-10-28.
- Evidence:
  - "An interior design consultation in Naples, FL runs $150 to $500 for a paid in-home session. Many studios, Pure Design of Naples included, open with a free discovery call instead." "... many Naples firms credit that fee toward your project." `verified` that the page says it; the figures are the firm's claim.
  - "Hourly rates in Naples run $100 to $250." "Single-room design in Naples runs $2,500 to $6,000. Whole-home work starts near $15,000 and climbs past $50,000." `verified` as the firm's claim.
  - Seasonal clients: "Remote or seasonal project. One fee, with a set number of video reviews. Uncapped hourly gets expensive when you approve choices from Michigan." `verified`. Seasonal residents approving choices from far away is a natural fit for the "meet virtually" option.
- Steal this: a paid in-home visit that is credited toward the project, and a fixed number of video reviews per project instead of unlimited hourly.

---

## The vintage lane (what exists, what does not)

### 17. ThriftSpace, Antiques & Interiors llc, Odloft

- ThriftSpace: https://thrift-space.com/ (`c1-thriftspace.md`, `c1-thriftspace-pricing.md`). "Connect with talented design students and professionals who create stunning spaces using curated second-hand finds." Pricing page: client "$0.99/month", designer "$9.99/month"; no per-project prices. © 2025. `verified` that the page says this; whether it has real designers or clients is `unverified`.
- Antiques & Interiors llc: http://antiquesandinteriorsllc.com/ (`c1-antiques-interiors.md`). "We offer full-time interior design, decoration, and consultations, and curate exceptional antiques, vintage furnishings, and objet d'art". No prices. `verified`
- Odloft: https://odloft.com/ , `/pages/trade-interior-design` (`c1-odloft-trade.md`). "Our sourcing service can help you find distinctive antique and vintage pieces beyond our current collection ... we'll use our network of dealers, auctions and private sources". Trade-focused, "Trade Accounts Coming Soon", no price. `verified`
- Result: no priced e-design package that builds the shopping list from vintage or secondhand pieces turned up in this session. I checked designer sites and general search; I could not open Etsy listings (blocked) or A Vintage Splendor, so Etsy-only sellers may exist. `unverified` that none exist.
- Steal this: Hollie can be the first to publish a price and a deliverable for "a room from pieces that already exist."

---

## Comparison table

"not stated" = not on the page I read. Promo prices are noted.

| service | price | unit | deliverables | revisions | turnaround | who buys |
|---|---|---|---|---|---|---|
| Havenly Online | $199 list ($89 promo to 11/3) | per room | video call, floor plan, 3D renders, shopping list | "until it feels like yours" | first concepts 3 to 14 days | client |
| Havenly In-Person | $699 list ($299 promo) | per room | same, designer visits home | same | set with designer | designer sources and orders |
| Decorilla Bronze/Silver/Gold | $599/$859/$1,099 (hall/entry); $849/$1,099/$2,049 (living room) | per room, by room type | 2 concepts, floor plan, 3D, shopping list | not stated | not stated | client (trade discounts listed) |
| Decorilla hourly / Platinum | $119 to $500 per hour / from $1,980 | hour / project | advice / project management | n/a | n/a | client |
| Spacejoy delight/bliss/euphoria | $199/$399/$599 (list $399/$599/$799) | per room | 1 or 2 concepts, 3D, floor plan, shoppable list | in every package, number varies | 10 / 10 / 7 to 10 business days | client (optional via Spacejoy) |
| Laurel & Wolf (AI) | $19/$39/$99 per month | subscription | AI restyle of a photo | up to 20 per photo | about 2 minutes | n/a |
| The Expert | $300 to $3,000+ (Wu); $200 to $3,600 (Decorilla); unverified on site | per session, 25 to 115 min | live advice on Zoom | none (book again) | book a slot | client |
| Safra Jump Start | $450 to $1,500 | per room (by size) | concept board, palette | not stated | 2 to 3 weeks | client |
| Safra Full Service | $950 to $2,800 | per room | board, floor plan, shopping list with budget | 2 re-selections | 2 to 3 weeks | client, or Safra at cost + 15% |
| Safra One Question | $180 | per consult | paint, one item, one piece | n/a | not stated | client |
| Stellar #1 / #2 / paint | $475 / $575 / $95 | per room | boards, source list, palette (#2 adds floor plan) | not read | 1 to 2 weeks | client |
| Mix & Match | $175 / $300 / $425 | 30 / 60 / 90 min | live call, recording, product links | none | book a slot | client |
| Dwelling Envy Revive / Total | from $749 / from $1,499 | per room | 2D board, shoppable board (Total adds floor plan, 3D) | 1 minor round | 2 to 4 weeks (page conflicts) | client, no markup |
| Dwelling Envy Sidekick | $125 | per hour | advice | n/a | n/a | client |
| Black Cat On Call | $95 | per question | written answer | n/a | 2 to 3 business days | client |
| Black Cat Shelf Styling | $112 (list $150) | up to 6 shelves | to-scale styling image, shopping list | not stated | not stated | client |
| Black Cat Gallery Wall / Holiday | $105 / $99 | per wall / per space | layout / one visualization plus list | 1 round (holiday) | 7 to 10 business days (holiday) | client |
| Black Brick Shelf Styling | $500 | up to 10 items | phone consult, handpicked items | 1 round, then $150/hr | not stated | client |
| Noeka Classic / Comprehensive | $450 / $650 | per room | style board, links (renders in Comprehensive) | up to 3 | about 3 weeks | client, 10 to 15% off via Noeka |
| Noeka Tablescape / Seasonal | $295 / $495 | per table / per room | board, layout, links | up to 2 / up to 3 | 3 to 4 weeks | client |
| Sandringham On Call | $175 | per hour | advice, call or home visit | n/a | n/a | client |
| Sandringham Mini Vignettes | $425 | per room | accessory board, link list | not stated | 10 to 15 days | client |
| Sandringham Concept / Full | $875 / $2,100 | per room | concept, elevation / adds floor plan, 3D, install guide | 2 edits | 10 to 15 days | client |
| Vintage Soul Basic/Essentials/Full | from $350 / from $500 / $700 to $1,000 | per room | mood board / plus 2 to 3 pieces with links / plus floor plan, full list | up to 2 / up to 3 | not stated | client |
| Insighed 30 min | $75 | per call | advice | n/a | book a slot | client |
| Design Hub Refresh/Full/Whole | quoted (not published) | per room / up to 3 rooms | 8 to 12 pieces / 15 to 25 pieces plus layout | 1 / 2 | about 1 week; priority on Whole | client, member pricing optional |
| Annie Wise in-person | $475 (+$50 beyond 15 miles) | 90 min | Google Slides summary | none | on the day | client |
| Pure Design Naples in-home | $150 to $500 (firm's claim) | per visit | advice | n/a | on the day | n/a |

---

## Discrepancies and open items

- Havenly: $199 and $699 list versus $89 and $299 promo. X verified (both numbers are on the page), Y need review (how often the promo is not running).
- Decorilla: "$599" is the cheapest room type; Living Room starts at $849. X verified, Y need review for the other room types.
- Spacejoy: banner says 40% off with code SPOOKY40; list prices are shown struck through. X verified, Y need review (whether displayed prices already include it).
- The Expert: low end $200 (Decorilla) versus $300 (Wu) versus Arnold at $1,250 an hour (BOH 2021). None is The Expert's own page. X verified as reported, Y need review.
- Modsy: "ceased to offer design services" (June 29, 2022) versus "cease operations on July 6" (CEO, via TechCrunch July 17). Both verified; they are different events.
- Dwelling Envy: portal 1 year versus six months; delivery 2 to 3 weeks versus 3 to 4 weeks. X verified, Y need review.
- Safra's page may be stale (2020 timestamp). `inferred`
- Not read or failed: Etsy shelf-styling and 60-minute-consult listings (crawl returned 4 bytes), Etsy rush listing (WebFetch HTTP 403), A Vintage Splendor `/vintage-sourcing/` (0 bytes; WebFetch SSL error), Redesign Livings (0 bytes), designerfeecalculator.com (0 bytes), DesignedByDijae rush-fee page (Shopify store closed, not a wall), Ville Otis e-design mini (404), Findery personal-shopper page (`c1-findery-shopper.md`, 0 bytes, crawl did not return). The Findery capture belongs to agent c2's lane (`c2-findery.md`); I did not use it.
- Rush fee (WebSearch only, `unverified`): one non-interior design studio is said to charge $75 for 48 to 72 hours and $150 for same day or 24 hours. I could not open the page.
- Local anchor is a single vendor page; I did not find an independent SWFL price survey.

---

## Recommendation for Holliewood & Vine

Assumptions to confirm with Ricky: the business is in Southwest Florida (Lee and Collier), in person means Hollie goes to the client, and there is no public showroom. Refer to Hollie by name or as they/them.

Core idea: charge for Hollie's taste and sourcing time, and let the design fee flow into a purchase from Hollie's stock. Business of Home says platforms make the money on shopping; Hollie already has the shop. Offer a design fee credit toward pieces bought from Holliewood & Vine (`inferred`, supported by "many Naples firms credit that fee toward your project" and Noeka's 10 to 15% off for design clients). Because every piece is one of one, add a short hold on named pieces (for example 72 hours, `inferred`) and a reselection price like E-Design Interiors' "$75 for 4 replacement pieces", since Safra's FAQ shows the stock problem even with new goods.

### Tier ladder

| tier | what it is | price range | sources for the range | suggested start |
|---|---|---|---|---|
| 1. One Find | Client sends a photo, size and budget (or books a 30-minute call). Hollie returns 3 options for one thing: a lamp, mirror, chair, bar cart. | $95 to $175 | Insighed $75 (30-min call); Black Cat $95 (one written question, 2 to 3 business days); Mix & Match $175 (30 min); Safra $180 (includes "resourcing one item"); Sandringham $175 per hour | $125, credited toward the piece |
| 2. A Corner | One vignette: a shelf, bar cart, bookcase, entry table, party table, one wall. Board of 6 to 10 pieces from stock and sourced, placement notes, 1 to 2 edits. | $195 to $495 | Black Cat shelf $112 to $150 and gallery wall $105; Noeka tablescape $295 and seasonal $495; Sandringham Mini Vignettes $425; Black Brick shelf $500 for up to 10 items | $295 |
| 3. A Room | A room, a section, or a studio zone. Intake call (video that shows the space), board, floor plan sketch, shopping list with links, Hollie's pieces first, 2 revision rounds, 7 to 10 business days. | $650 to $1,250 | Noeka $450 to $650; Stellar $475 to $575; Vintage Soul $350 to $1,000; Dwelling Envy $749 to $1,499; Sandringham $875 to $2,100; Safra $950 to $2,800. National platforms sit below ($199 list at Havenly and Spacejoy) or at the top ($849 to $2,049 Decorilla living room) | $750 |
| 4. Whole House or Studio | Several rooms or a whole home, quoted by room count. | Room rate x rooms, about 10% off rooms two and up. Example: 3 rooms at $750 less 10% = $2,025; 5 rooms at $1,000 less 10% = $4,500 | Decorilla "Save 10%" multi-room (verified); Spacejoy and Sandringham say a multi-room discount exists but give no number; Design Hub "Whole Space" up to 3 rooms (unpriced) | Quote after intake call |

Why the Room band sits in the middle: vintage sourcing is bespoke labor (hunting one-of-ones), so it should not match the $199 platform tier, and Hollie has no 3D rendering step, which is what pushes the independents above $1,500. If Hollie wants renderings, Dwelling Envy and Noeka price them as a $500 add-on.

### Intake and hours

- Intake (matches every source): photos, measurements, a short questionnaire, inspiration images, budget. Add the video call that walks the space (`inferred` differentiator; no source requires it). Offer three ways in, as Hollie described: virtual call, send photos, or describe it by email.
- Extra time: bill hourly at about $95 to $150 for add-ons and extra revisions, in the middle of Safra $75, Dwelling Envy $125, Stellar $150, Black Brick $150, Sandringham and Annie Wise $175 to $200 (`inferred`).

### Upgrades

- **In person (Hollie comes to the client):** add $250 to $500 per visit, plus a $50 fee beyond a set radius (Lee and Collier is wide; Annie Wise uses 15 miles). Evidence: Havenly in-person is $699 versus $199 online (about +$500); Annie Wise in-person 90-minute consult $475 plus $50 beyond 15 miles; Sandringham prices a home visit the same as a call ($175); a Naples firm says paid in-home sessions run $150 to $500 and are often credited to the project. Price range is `inferred` from those numbers.
- **Rush ("need it done now"):** `inferred`, no verified e-design rush price exists. Start at +25% of the package with a $75 minimum, and offer it only when the pieces are already in hand. The closest verified signals are Design Hub's "Priority turnaround" and Spacejoy's faster top tier. Treat the number as an experiment and revisit after ten bookings.

### Policy choices the evidence supports

- Revisions: 2 rounds included (Sandringham 2, Safra 2, Design Hub 1 to 2, Noeka 2 to 3); extra at the hourly rate.
- Refunds: full refund within 48 hours or before work starts (Spacejoy), pay on approval of the board (Decorilla), call cancellations 48 hours ahead (Mix & Match). No refund after final delivery (Sandringham). Write it short, in Hollie's voice.
- Who buys: the client buys; the shopping list links to Holliewood & Vine first, then outside sources. Optional "Hollie buys and delivers" at cost plus a fee, like Safra's cost + 15% (`inferred` as a premium option).
- Deliverable format: a clickable list plus a short deck or page the client keeps (Annie Wise Google Slides; Dwelling Envy a page kept for a year; Mix & Match a recording).
- Party and event use case: price a table or room as a standalone package (Noeka tablescape $295 and seasonal $495 are the closest model), with rush available.
