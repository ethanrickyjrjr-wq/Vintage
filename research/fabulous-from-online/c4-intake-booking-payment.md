# c4: intake, booking and payment on a static site

Agent c4, accessed 2026-10-28.
Method: SearXNG (`tools/search.sh`) for URLs, crawl4ai (`tools/crawl.sh`) for pages, raw captures in `research/fabulous-from-online/raw/c4-*`. WebSearch and WebFetch were used only to try the Etsy policy pages (WebFetch got HTTP 403) and for one Google Forms check. One live `curl` against the published site. Anything in quotes was read on a live page this session; typographic quotes and apostrophes are normalized to straight ones. Tags: `verified` = read on a live page this session, `inferred` = my reasoning from verified facts, `unverified` = not confirmed. Where sources disagree: "X verified, Y need review." The shop is Holliewood and Vine. Hollie is "Hollie" or they/them throughout.

## TL;DR

1. **Ship (a) today: a `mailto:` link with a prefilled subject and body, plus a photo checklist on the page.** It is how working designers actually do it. Megan Meyers: "Photos and measurements can be sent directly to megan@meganmeyers.com". Of Houses and Trees runs a questionnaire, then asks for photos by email: "Send photos and measurements of your space, plus inspiration photos of spaces you love to larissa(at)ofhousesandtrees.com." Attachments cannot be prefilled: RFC 6068 defines the body as "the first text/plain body part" and the text never uses the word "attach" (count 0). So the body asks for the info and the page carries the checklist. My generated sample href is 1,036 characters (703 for a short version).
2. **The site is not backend-free, but the worker route is the last rung.** Verified: the live site answers `GET /api/room-preview` with `{"available":false,"dailyLimit":3}`, so the Worker is deployed. A form route needs an email vendor key, spam protection (Turnstile), somewhere to read submissions, and a privacy policy. R2 conflict: `hosting.json` has `"r2": null` (no binding today), but the Sites docs list "R2 object storage" for uploads. Photo upload through the worker is possible later, not impossible. Needs review.
3. **Booking: link out, do not embed.** I found no OpenAI documentation on third-party iframes, external scripts or cross-origin form posts on Sites. The live homepage sends no CSP or X-Frame-Options header (verified), so embeds probably load (inferred), untested. A plain link has no such risk. Pick **Cal.com Free**: "Free forever", unlimited event types (one each for video call, in-person, rush), "Accept Stripe & PayPal payments" on the Free list. Calendly Free has "One event type" and payments start on Standard ($10/seat/mo). Google's personal booking page makes your name and photo public and takes no payments. Acuity has no free tier.
4. **Photos: Tally is the only free form with no-login upload** (10 MB per file, unlimited submissions, email notification, redirect on completion). Google Forms uploads require the respondent to sign in to Google (verified). Formspree Free has 0 GB of uploads. Typeform upload is Basic and up. Jotform Starter has 100 MB total. Nobody in my sample asks for uploaded video; video happens live on the call. Free-tier file caps (10 MB, 5 MB) rule video out anyway.
5. **Money: one fixed-price Stripe Payment Link per tier, pasted into Hollie's reply after scoping.** No monthly fee, 2.9% + 30¢ on domestic cards. ChatGPT Sites Terms 2.6 expressly allows third-party payment providers "to sell goods or services". Do not use "customers choose what to pay" for deposits: Stripe positions it for "donations, tipping, or pay-what-you-want".
6. **Marketplaces: keep this service off Etsy.** Etsy Help Center: "In general, services, including rentals, are not allowed to be sold on Etsy. Only services that produce a new tangible item that meets our Seller Policies may be sold on Etsy." The Etsy legal pages themselves were walled, so the policy pages need review. Shopify can sell a service (Help Center documents it), but Shopify Forms is a storefront theme embed and cannot run on the Sites page.
7. **Ladder rank:** (a) mailto + checklist, then (c) booking link, then (d) Stripe link in the reply email, then (b) Tally form link, then (e) embeds, then the worker route. v1 = (a) + (c). v2 adds (b) + paid booking. v3 = worker.

---

## 1. ChatGPT Sites (what the page can do)

- Homepage: https://learn.chatgpt.com/docs/sites
- Pages read: Help Center "Creating and using ChatGPT Sites" (`c4-sites-help.md`), docs "Sites" overview (`c4-sites-learn.md`; developers.openai.com/codex/sites returned byte-identical content, so not counted twice), "Create a site" (`c4-sites-create.md`), "Data and connections" (`c4-sites-data.md`), "Publish and share" (`c4-sites-publish.md`), "Manage a site" (`c4-sites-manage.md`, `c4-sites-manage2.md`), Help Center collection (`c4-sites-collection.md`), "Understanding responsibilities" (`c4-sites-resp.md`), "Preparing a privacy policy" (`c4-sites-privacy.md`), ChatGPT Sites Terms https://openai.com/policies/chatgpt-sites-terms/ (`c4-sites-terms.md`), live response headers (`c4-sites-live-headers.txt`).
- Repo reads: `site/build.mjs` lines 93-101, `site/room-worker.mjs` lines 75-82, `site/.openai/hosting.json`.

**What runs on Sites (coordinator correction folded in)**
- `verified` (repo): `build.mjs` writes `dist/server/index.js` from `room-worker.mjs`, and `dist/server/wrangler.json` with `assets: { directory: "../client", binding: "ASSETS", run_worker_first: ["/api/*"] }` and a D1 binding `DB`. `hosting.json` reads `{"d1":"DB","r2":null}`. The worker returns `env.ASSETS.fetch(request)` for any path other than `/api/room-preview`, and guards POST with `request.headers.get("origin") !== url.origin || request.headers.get("sec-fetch-site") === "cross-site"`. `MAX_BODY` is 4 MB.
- `verified` (live, `curl`, server date 2026-10-29 01:53 UTC = evening of 2026-10-28 in Florida): `GET https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site/api/room-preview` returns `200 {"available":false,"dailyLimit":3}`. The Worker is live. `available` is false because at least one required env var or binding is not set (`ROOM_PREVIEW_ENABLED`, `HF_TOKEN`, `ROOM_RENDERER_URL`, `DB`).
- Docs say: "Sites hosts web experiences in its supported runtime. Some frameworks, private networks, databases, background services, and hosting patterns aren't supported." and "HTTP, HTTPS, and WebSockets are supported. Raw inbound and outbound TCP connections aren't supported." Outbound HTTPS from the Worker is also what `room-worker.mjs` already does to Hugging Face. `verified`.
- Storage table (docs): "D1 database | 10 GB" and "R2 object storage | No fixed storage limit". The data page maps need to feature: "Images, documents, audio, video, or other uploads | R2, object storage for files" and "Uploaded files with searchable metadata | D1 for metadata and R2 for file contents". `verified`.
- **R2: no binding verified here (hosting.json `r2: null`), R2 offered by Sites (docs), enabling it for this project needs review.** I did not find how to add the binding; the docs say to describe the need to Codex/ChatGPT. The coordinator's "there is no R2" is true of the project today, not of the platform.
- The docs even list this pattern: "A request form could collect details through fields, choices, and attachments. You might ask it to check required answers, save submissions for reviewers, and show a confirmation explaining what happens next." `verified`.

**Third-party scripts, iframes, form posts**
- `unverified`: I searched help.openai.com, learn.chatgpt.com and the Terms for iframe, embed, CSP, external script and cross-origin form post. No page addresses them. Plainly: there is no documentation on this that I could find.
- `verified` (live headers on the homepage): `Server: cloudflare`, `Cache-Control: public, max-age=0, must-revalidate`, and no `Content-Security-Policy`, `X-Frame-Options` or `Permissions-Policy` header. The `/api/room-preview` response sets only `Cache-Control: no-store` and `x-content-type-options: nosniff`.
- `inferred`: with no CSP header, third-party scripts, iframes and form posts probably load. `storefront.html` has no CSP `<meta>` tag (grep for `http-equiv` found none). Sites could still add a policy later. Untested, so links beat embeds.

**Payments and responsibilities**
- Docs overview: "You can sell goods or services and collect payments through a third-party payment processor. Payment-card data must be collected and processed solely by that provider, not by your site or OpenAI. Other financial transactions remain prohibited. You're responsible for the integration, fulfillment, refunds, customer support, and applicable taxes." `verified`.
- Terms 2.6: "You may choose to implement and use third-party payment providers and processors ("Payment Providers") to sell goods or services to or collect payments from End Users". Terms 2.5(e) forbids facilitating financial transactions "except for E-Commerce Activities described in Section 2.6 that are processed by a third-party Payment Provider". `verified`.
- Collecting personal data: "Review features that collect personal information or other visitor content. Decide whether the site should collect, share, or publish that information." and "If visitors can submit or post content, you are responsible for monitoring and moderating that content, including addressing content that is inappropriate or unlawful." Privacy guide: "The easiest and most common way to comply with this requirement is by posting a Privacy Policy on your Site." `verified`.
- Secrets and editors: "Editors can also inspect the live database and publish code that uses the Site's secrets and storage." The owner configures secrets ("owner-only settings, such as secrets and custom domains"). Help: "On Sites that use regional hosting, changes to existing secret values can affect the live Site without publishing again. Adding or removing keys from the Site's configuration still requires publishing." `verified`.
- Sites is a "Beta Service" (Terms 5.3). `verified`.

**Discrepancy for Ricky:** the live URL slug and the wrangler `name` both read `hollywood-and-vine...`. That is a hostname and config string, not copy. The shop is Holliewood and Vine. Rename needs Ricky's word.

---

## 2. Intake patterns on designers' sites

Honest count: **three live field-by-field forms** (Grant Sullivan, Of Houses and Trees, Mod City Mad's sourcing request, the last from a vintage dealer not a designer), **one photo-and-measurement spec** (Megan Meyers), **two sourcing pages with guidelines only** (Brass Armadillo, The Findery Market), **one template list** (Houzz Pro, a vendor article, not a designer's own form), and **four prep guides** (Havenly, Megan Baker, Kellie Burke, Balibest). Paperform, Jotform and Dakota Design Company are vendor templates and are not counted. A Vintage Splendor sourcing page returned 0 bytes (walled).

### 2.1 Grant Sullivan Interiors (full field list, Wix form)
- Homepage: https://www.grantsullivaninteriors.com | read `/client-intake-questionnaire` (`c4-intake-grantsullivan.md`)
- Gating: "This questionnaire is solely used for clients who have purchased a service and scheduled a consultation with our Interior Designer. This questionnaire is required to be completed prior to all consultations." So the form comes after payment and booking. `verified`.
- Fields, verbatim: First Name, Last Name, Email, Street Address (+ Line 2, City, Postal / Zip code, Region/State/Province, Country), "What kind of assistance are you looking for:", "Select Your Purchase", "Have You Worked with An Interior Designer Before?", "Which part of your home (rooms) do you need assistance with?", "What Do You Consider Your Design Style (Check All That Apply)" (Art Deco, Contemporary, Eclectic/Bohemian, Glam, Industrial, Mid-Century Modern, Modern, Traditional, Transitional, Vintage, Other), "What Finishes Do You Prefer" (Gold, Silver, Bronze, Graphite, Black, White), "What Patterns Do You Prefer" (Linen, Leather, Velvet, Cotton), "List your 3 favorite colors.", "List 3 colors you dislike.", "Please list any allergies we should be mindful of?", "Do You Like to Shop for Your Home? How Often and Where?", "What Mood Do You Want to Create Overall", "What Kind of Surroundings Make You Happy?" (A Hotel Getaway Atmosphere / A Simple and Airy Space / A Bright Room with Lots of Color), "What is your preferred color palette?", "What colors you do not want in your color palette?", "What design trend are you dying to try?", "I would absolutely hate it if you included the following in my design", "How did you learn of our services?", "Additional Comments /Questions". No budget field, no photo upload in the form. `verified`.

### 2.2 Of Houses and Trees (e-design, full field list, five-step flow)
- Homepage: https://ofhousesandtrees.com | read `/e-design-questionnaire/` (`c4-intake-ofhouses.md`)
- Flow, verbatim: "Step 2 Within 24 hours of submitting the questionnaire, you'll receive an initial email with payment info and instructions on how to get the process started. (Unless you've already paid!)" then "Step 3 Send photos and measurements of your space, plus inspiration photos of spaces you love to larissa(at)ofhousesandtrees.com." then "Estimated delivery of your initial custom design is 7 to 10 days after I receive your questionnaire answers and photos/measurements." `verified`.
- "Most questions are optional. If you aren't sure of an answer, you can leave it blank and we'll chat about it later."
- Fields, verbatim: Name, Email, "Location (City/Town, Province/State, Country)", "What room(s) do you need help with?", "Do you have a specific timeline in mind for this project or is the completion date flexible?", "Tell me a bit about the space. (What do you currently like and dislike about it? What is your vision of the finished product?)", "Who will be using the space? (i.e.: adults only, children, pets, etc.)", "Do you have any existing furniture or decor items you'd like to incorporate into the space?", "What new furniture and decor items would you like to incorporate into the space?", **budget bands** "Less than $1,500. / Between $1,500-$3,000. / Between $3,000-$4,500. / Between $4,500-$6,000. / Between $6,000 and $7,500. / More than $7,500." with "(Not including the e-design fee.)", style checkboxes (Bohemian, Coastal, Contemporary, Industrial, Farmhouse, Mid-Century Modern, Minimalist, Rustic, Shabby Chic, Traditional, "I don't have a specific style", Other), "Where do you like to shop for furniture and decor?", "Are you open to painting the walls?", color preference (Neutrals / Neutrals with pops of colour / Lots of colour), patterns, metal finishes, wood tones, artwork types, "Are you open to incorporating antique, vintage or secondhand items into your space?", "Are you open to completing DIYs using instructions or videos I send?", "Please include the link to a Pinterest board with images of spaces you love.", discount code, Phone. No file upload in the form; photos come by email. `verified`.

### 2.3 Mod City Mad "Furniture Sourcing" request (closest model for "find me an item")
- Homepage: https://modcitymad.com | read `/pages/sourcing-request` (`c4-intake-modcity.md`)
- Promise: "Tell us what you're looking for. We tap our network of pickers, dealers, auctions and estates to find your piece. Free to ask, no obligation, and we follow up within 48 hours." Steps: "Describe it." / "We search." / "You decide." with "Photos, condition notes and price before you commit." `verified`.
- Fields, verbatim: Your name, Email, "Phone (optional)", Item type (select: Dresser / Chest, Credenza / Buffet, Dining Table, Dining Chairs (Set), Coffee / Side Table, Lounge Chair / Armchair, Sofa / Sectional, Headboard / Bed Frame, Desk, Cabinet / Bar, Nightstands (Pair), Lamp / Lighting, Mirror, Other / Not Sure), "Brand or designer (optional)", "Era (optional)", Condition ("As pictured / Restored / Either"), Timeline ("Flexible, no rush / Within 3 months / Within 6 weeks / As soon as possible"), **Budget** ("Under $500 / $500 to $1,000 / $1,000 to $2,500 / $2,500 to $5,000 / $5,000+ / Flexible"), "What are you looking for?", "Reference link (optional)". Reference is a link, not an upload. Free to ask, no fee. `verified`.

### 2.4 Megan Meyers Interiors (photo and measurement spec)
- Homepage: https://www.meganmeyers.com | read `/e-designquestionnaire` (`c4-intake-megan.md`)
- Verbatim: "Photos and measurements can be sent directly to megan@meganmeyers.com". "I'll need a minimum of 8 photos for each space: An overall photo taken from each of the corners of the room / A photo of each wall face on, try and include parts of the ceiling, floor and adjacent walls if possible / Detail images (close up) of any items you want to include in the final space". Measurements: floor plan sketch, "Mark each wall North, South, East and West", wall elevations, "Measure the overall ceiling height", "provide dimensions for the openings themselves, as well as overall measurements including any casings", and "Please provide dimensions (width, depth, overall height, arm height) of any furniture you would like to keep". `verified`.

### 2.5 Sourcing pages with guidelines only
- Brass Armadillo https://brassarmadillo.com/personal-shopper/ (`c4-intake-brassarmadillo.md`): "Only one item per submission", "You must submit a valid email address (that's how we send you back info)", "Your submission is kept active for three months." `verified`.
- The Findery Market https://thefinderymarket.com/pages/personal-shopper (`c4-intake-findery.md`): "Whether it's a description, a photo, or even just a vague idea, the more details you provide, the better!" then "We'll send you all the juicy details along with photos and pricing". `verified`. (The page footer lists `admin@gmail.com` and a placeholder-looking address; treat the shop as unproven.)
- The Selby House https://theselbyhouse.com/pages/custom-sourcing (`c4-intake-selby.md`): "All-in fixed rate option which covers up to 5 hours of design services and all other costs except shipping." and "Both options are billed at an hourly rate of $120 p/hour." and "Yes, we typically work with a minimum budget of $2,500". Contact form is Name, E-mail, Message only. A price anchor, not a recommendation. `verified`.

### 2.6 Vendor template (not a designer's form)
- Houzz Pro https://pro.houzz.com (`c4-intake-houzz.md`), article "Interior Design Questionnaire for Clients": sections "Contact information" (Name, Address, Email, Phone number, Social media profiles, Preferred method of contact), "Assess the current situation", "Determine intended use of space", "Assess design style"; key questions "What is your ideal budget and timeline/deadline?" and "Do you want your design done in phases or all at once?" `verified` as a template list.
- Dakota Design Company sells the same thing as a $125 Google Form template (`c4-intake-dakota.md`), Paperform and Jotform host free templates (`c4-intake-paperform.md`, `c4-intake-jotform.md`). Not counted.

### 2.7 Prep guides: photos, measurements, video, budget
- Havenly (https://havenly.com/learn/how-to-prepare-for-online-interior-design, `c4-intake-havenly-prep.md`): "have four simple things ready: a few daylight photos of your room, rough measurements, an honest budget number, and a handful of inspiration pictures." Photos: "Shoot in daylight with the lamps off... Stand in the doorway and take a wide shot of the whole room, then one photo of each corner." "Don't tidy for the camera." Keep list: "keeping for sure, open to letting go, and hard no." Budget: "Pick the number you're genuinely comfortable spending, and share that number, not a smaller one you think sounds reasonable." `verified`.
- Megan Baker (https://meganbakerinteriors.com/prepare-for-virtual-design-consultation/, `c4-intake-meganbaker.md`): a 90-minute video session. "Do not be tempted to use a wide angle lens! This distorts the space and makes it appear larger than it is". Supplies: "Laptop or Desktop computer, Tape Measure, Phone, Painters tape, Notepad, Pencil, Sharpie". "Have your phone nearby to quickly Facetime details of the space if needed." `verified`.
- Kellie Burke (https://kellieburke.com/how-virtual-interior-design-works-step-by-step-process/, `c4-intake-kellieburke.md`): "Step 2. Share Photos, Measurements, and a Video Walkthrough" and "Clear photos of every wall, accurate measurements, and a live video walkthrough reveal ceiling heights, window placement, architectural details, and natural light." "A smartphone with a good camera and a stable internet connection is usually enough." The walkthrough is live. `verified`.
- Balibest (https://balibestdesign.com/online-interior-design-consultation-guide/, `c4-intake-balibest.md`): "a 30 to 45 minute call", "Wide shots from each corner, in daylight, clutter and all", "Even a hand sketch with a tape measure works at this stage", "A budget range. Not a fixed number". `verified`.

**What the sample shows**
- `inferred` from the pages read: no one asked clients to upload video. A "video walkthrough" means a live call. Photos go by email or a form; two of three full forms have no upload field at all.
- Style quizzes: I did not read a dedicated quiz page (Havenly mentions "Your session and style quiz"). The check-all-that-apply style, finish and pattern lists in 2.1 and 2.2 are the lite version. `unverified` for standalone quiz mechanics.
- Budget is asked as bands, never as a free number, and "Flexible" is an allowed answer (2.2, 2.3).
- Rush is a timeline option (2.3: "As soon as possible"), not a separate form.

---

## 3. Booking tools

All free-tier and price claims from the vendor's own page, accessed 2026-10-28.

### 3.1 Calendly
- Homepage: https://calendly.com | pages: pricing (`c4-cal-calendly-pricing.md`), invitee questions https://calendly.com/help/how-to-add-or-remove-invitee-questions (`c4-cal-calendly-questions.md`), embed https://help.calendly.com/hc/en-us/articles/223147027-Embed-options-overview (`c4-tool-calendly-embed.md`), payments help (`c4-cal-calendly-collectpay.md`), community thread on attachments (`c4-cal-calendly-community-files.md`).
- Free: "One event type", "One calendar connection", "One-on-one scheduling", "Customizable booking page". `verified`. One event type cannot separate video, in-person and rush offers.
- Payments: Standard, "$10 /seat/mo", billed yearly; under it "Payments: Connect Stripe, PayPal". Also "Collect payments at booking via Stripe and PayPal" and "Custom payment links for one-off services and fees". `verified`. Free has no Payments line.
- Questions: "For each event type, you can add up to 10 custom questions." Answer types: One line, Multiple lines, Radio buttons, Checkboxes, Dropdown, Phone number. `verified`.
- File upload: none in the answer-type list. Calendly staff, 2023-11-07: "At this time there is no way to allow attachments on the booking page." and suggests a redirect to a Google Form. That reply is old; the current list agrees. `verified` (list), `inferred` (still true).
- Embed: "Calendly offers three embed options: Inline embed, Pop-up text, Pop-up widget." plus a plain link. Embed help says "All plans". `verified`. One related help line: "If your plan doesn't support HTML embeds, you can add a link to your Calendly scheduling page instead." (host-dependent).

### 3.2 Cal.com
- Homepage: https://cal.com | pages: pricing (`c4-cal-calcom-pricing.md`), booking questions https://cal.com/help/event-types/booking-questions (`c4-cal-calcom-questions.md`), embed https://cal.com/embed (`c4-cal-calcom-embed.md`), Stripe https://cal.com/features/payments (`c4-cal-calcom-payments.md`), GitHub issue 13887 (`c4-cal-calcom-issue-fileupload.md`).
- Free: "Free forever", "1 user", "Unlimited event types & calendars", "Email & SMS notifications", "Accept Stripe & PayPal payments". Page also says "Start scheduling for free, with no usage limits." `verified`. Teams is $12 per user/month yearly (not needed for one Hollie).
- Questions: "Change booking questions: Customize the questions attendees answer when booking." and the help page: "The booking questions can be either required or optional". Whether every question type is on Free is `inferred` (the compare table lost its column marks in the crawl).
- Prefill: help page says the booking question identifier is used to "prefill the question from the booking link". That lets a mailto/Tally redirect carry answers. `verified`.
- File upload: none in the help page. GitHub issue "Booking questions: Add file upload option #13887" shows "Closed as not planned" (closed May 9, 2024). `verified`; current status unverified beyond that.
- Payments: the Stripe page says "decide which of your bookable events have charges and exactly how much those are." `verified`.
- Embed: "Cal.com currently supports four flexible embedding options: inline embed, floating pop-up button, pop-up via element click, and email embed." plus a plain link. `verified`.
- Redirect after booking: listed as "Redirect on booking". `verified` (feature list).

### 3.3 Google Calendar appointment schedules
- Homepage: https://calendar.google.com | pages: create https://support.google.com/calendar/answer/10729749 (`c4-cal-gcal-appt.md`), premium comparison https://support.google.com/calendar/answer/16287038 (`c4-cal-gcal-premium.md`), payments https://support.google.com/calendar/answer/13762729 (`c4-cal-gcal-payments.md`), share https://support.google.com/calendar/answer/10733297 (`c4-cal-gcal-share.md`).
- Free: "With a personal Google Account or Workspace Business Starter plan, you can create a single booking page to let others schedule appointments on your calendar." `verified`.
- Privacy: "Your booking page is always public. Anyone with the link can view your: Booking page, Profile photo, Account name". That is Ricky's or Hollie's personal Google identity unless a shop account exists. `verified`.
- Payments: "Paid appointment bookings are a premium feature for appointment schedules and available to users with an eligible Google Workspace subscription." Stripe only: "Customers can only select credit card payment, Apple Pay, and Google Pay as payment options." and Google "does not: Process or store any payment info... Charge any platform fees". Premium table: "Accept payments for appointments" is blank under Google One Premium / AI Pro / AI Ultra and checked for Workspace Individual and above. `verified`.
- Intake: booking form has First name, Last name, Email, and "To add more fields, click Add an item." Field types and file upload are not documented on that page. `unverified`.
- **Google disagrees with itself on spam verification:** the create page says "To avoid spam bookings, check the box next to Require email verification", while the premium table lists "Verify emails to prevent spam bookings" blank for the personal tier. Create page is general text; premium table gates it. Y need review.
- Embed: "Button with popup" and "Inline booking page" (HTML snippet), plus a copied link. `verified`.

### 3.4 Square Appointments
- Homepage: https://squareup.com/us/en/appointments | pages: pricing (`c4-cal-square-appt.md`), forms https://squareup.com/help/us/en/article/7104-contracts (`c4-cal-square-forms.md`).
- Free: a Free plan exists ("For solo professionals taking payments and managing schedules", signup token `free`); monthly price figures did not render in the crawl (template placeholders). Plans: Free, Plus ("Best value"), Premium. `verified`.
- Fees: the page's "Online | Applies to card payments made online or through an invoice" row reads `3.3% + 30¢`, `2.9% + 30¢`, `2.9% + 30¢`. The crawl has no column headers, so mapping 3.3% to Free is `inferred` from column order (Free, Plus, Premium). Needs review.
- Payment at booking: "Prepayments and automatic contracts... Require your clients to pay in advance for specific services" and "Appointment deposits: Collect a partial deposit when appointments are scheduled". Which plan gets them: `unverified`.
- Intake: "Square Appointments Plus and Premium subscribers" can send digital forms (Square Contracts), "such as intake forms". So not Free. `verified`. File upload `unverified` (not in the page I read).
- Embed: "Add a Book Now button to your website, create a QR code for a contactless booking option, or embed a booking widget into an existing website." `verified`.

### 3.5 Acuity Scheduling (Squarespace)
- Homepage: https://acuityscheduling.com | pages: pricing (`c4-cal-acuity-pricing.md`), request documents https://help.acuityscheduling.com/hc/en-us/articles/47294195896589 (`c4-cal-acuity-docs.md`), custom forms (`c4-cal-acuity-intake.md`), embed https://help.acuityscheduling.com/hc/en-us/articles/16676884389133 (`c4-cal-acuity-embed.md`).
- Free: none. "Try any plan free for 7 days", "7-day trial, no credit card needed". Starter "$16/ month" (annual) or "$20/ month" (monthly); Standard "$27/ month" / "$34/ month". `verified`.
- Payments: "Payments via Stripe, Square, PayPal, Venmo" listed on Starter, Standard and Premium. `verified`.
- Intake and uploads: "Custom client forms: Use intake forms to collect client details, terms and conditions, and more." And "Add a file upload question so clients can upload images, documents, or other files up to 5 MB." "You need to be logged into your account to access uploaded files." The upload article does not name a plan. `verified` (feature), plan `unverified`. Only tool in this set that takes a file at booking. 5 MB per question stops video and big phone photos.
- Embed: "Embedded scheduler - You can embed Acuity's full online booking experience on your website.", "Booking button", "Booking bar". `verified`.

---

## 4. Payment

### 4.1 Stripe Payment Links
- Homepage: https://stripe.com | pages: pricing https://stripe.com/pricing (`c4-pay-stripe-pricing.md`), overview https://docs.stripe.com/payment-links (`c4-pay-stripe-pl.md`), create (`c4-pay-stripe-create.md`), customize (`c4-pay-stripe-pl-custom.md`), post-payment (`c4-pay-stripe-post.md`), buy button (`c4-pay-stripe-buybutton.md`), share (`c4-pay-stripe-share.md`).
- Fees: "Access a complete payments platform with simple, pay-as-you-go pricing. No setup fees, monthly fees, or hidden fees." "2.9% + 30¢ per successful transaction for domestic cards". Payment Links: "Included at no additional charge for businesses on standard payments pricing". Custom domain on Stripe pages: "$10.00 per month". Illustration (`inferred`): a $150 deposit nets $150 - (4.35 + 0.30) = $145.35 before tax. `verified` for the rates.
- Services: create flow offers "Sell a product or service". `verified`. Fixed price per link. "Customers choose what to pay: Best for donations, tipping, or pay-what-you-want." Use that only if Hollie wants a pay-what-you-want tip. `verified`.
- Custom fields: "Text: Collects freeform text up to 255 characters.", "Numbers only", "Dropdown... up to 10 options" in the Dashboard. "Don't use custom fields to collect personal, protected, or sensitive data, or information restricted by law." Fields appear on the payment details page and in the `checkout.session.completed` webhook. Number of fields allowed: `unverified`. No file upload type. `verified`.
- After payment: "You can also choose to redirect your customers to your website instead of providing a confirmation page." So the link can send the payer to the booking link. `verified`.
- Embeds: the buy button is "a `<script>` tag and a `<stripe-buy-button>` web component" loading `https://js.stripe.com/v3/buy-button.js`. A plain link needs none of that. `verified`.
- Deposit for a service: not named in these docs; it is a fixed-price product called, say, "Fabulous From Online - design consult deposit". `inferred`. The comparison table row "Collect partial payments or set up payment plans" is an Invoicing feature vs Payment Links; the check marks were lost in the crawl, so which column owns it: `unverified`.

### 4.2 Square payment links
- Homepage: https://squareup.com/us/en/payment-links | help https://squareup.com/help/us/en/article/6692-get-started-with-square-checkout-links (`c4-pay-square-checkoutlinks.md`), page (`c4-pay-square-paymentlinks.md`).
- "Optionally toggle on Custom fields and add up to two custom fields to collect additional information from customers." "If Payment links doesn't appear, add it to your menu by... Add-ons > Payment links > Add for free." `verified`. Fee for links: Square's table says online card payments are 3.3% + 30¢ or 2.9% + 30¢ depending on plan (see 3.4, mapping `inferred`). Worse than Stripe on Free, no upside here unless Ricky already uses Square.

### 4.3 PayPal
- Homepage: https://www.paypal.com | fees https://www.paypal.com/us/business/paypal-business-fees (`c4-pay-paypal-fees.md`), links https://www.paypal.com/us/digital-wallet/send-receive-money/paypal-me (`c4-pay-paypalme.md`).
- "PayPal Checkout | 3.49% + fixed fee" and "Send/Receive Money for Goods and Services | 2.99%"; fixed fee for US dollar "0.49 USD". A $150 PayPal Checkout payment costs about $5.73 (`inferred`). `verified`.
- PayPal links: "With a PayPal link, you can send and request money by sharing a unique, one-time payment link directly to your intended recipient via text, email, DMs or other apps." One-time, no custom fields documented. `verified`. Useful only as a fallback for clients who prefer PayPal.

### 4.4 Shopify (service as a non-physical product, Forms)
- Homepage: https://www.shopify.com | pages: https://help.shopify.com/en/manual/products/digital-service-product/selling-services-or-digital-products (`c4-pay-shopify-services.md`), Forms https://help.shopify.com/en/manual/promoting-marketing/create-marketing/forms-app/create (`c4-pay-shopify-forms.md`, `c4-pay-shopify-forms-fields.md`).
- Service: "If you sell a digital download product or a service, then you need to remove shipping for that product." Step: "make sure that the Physical product setting is deactivated." Booking: "To provide a link for your customers to book your service, install an app from the Shopify App Store." `verified`. Deposits: sell a fixed-price service product; no Shopify-native deposit feature read. `unverified`.
- Shopify Forms: marketing-oriented ("Prompt customers to subscribe to your email, SMS, or WhatsApp marketing"; "Approve wholesale retailers using a company account request form"), popup or inline "embedded in a specific section on your theme", "To receive email notifications each time the form is submitted... select Send an email for each submission". Custom fields can be stored as metafields. File upload field: none found in the pages read. `unverified`.
- **Constraint:** "Turn on the Forms app embed for your theme" is a Shopify storefront feature. It cannot run on the static ChatGPT Sites page, and no Shopify store exists yet. `inferred`.

---

## 5. Marketplace policy

### 5.1 Etsy
- Homepage: https://www.etsy.com | read Help Center "What Can I Sell on Etsy?" https://help.etsy.com/hc/en-us/articles/360024112614 (`c4-pol-etsy-whatcanisell.md`) and "reselling" https://help.etsy.com/hc/en-us/articles/23948763872151 (`c4-pol-etsy-reselling.md`).
- **Walled:** https://www.etsy.com/legal/sellers/, /legal/prohibited/, /legal/creativity/, /legal/handmade, /legal/policy/services/242665313101 and the older Seller Policy all returned 4 bytes via crawl4ai (`c4-pol-etsy-seller.md`, `-prohibited.md`, `-creativity.md`, `-handmade.md`, `-services.md`, `-seller-old.md`), and WebFetch returned HTTP 403. The exact text of the Seller Policy, Creativity Standards and the dedicated Services policy was **not read**. Needs review before Ricky relies on it.
- What I did read (Help Center, which summarizes and links those policies): "Everything listed for sale on Etsy must either be made, designed, handpicked or sourced by you." And under Services or rentals: "In general, services, including rentals, are not allowed to be sold on Etsy. Only services that produce a new tangible item that meets our Seller Policies may be sold on Etsy." with a link to the Services policy for "services that may qualify". `verified`.
- Vintage: "Items that fall under 'Handpicked by a seller' include vintage items that are at least 20 years old". `verified`. That covers the shop's goods, not a consultation, a sourcing fee or a decorating fee.
- `inferred`: a design consultation, a sourcing fee or a room-decorating fee does not produce a new tangible item, so it should not be listed on Etsy. Keep Fabulous From Online on the hand-built site and Shopify, and link to it from the Etsy shop About page only if Etsy's policy allows off-platform mentions (`unverified`, needs review of the walled Seller Policy).

### 5.2 Shopify Acceptable Use Policy
- Homepage: https://www.shopify.com/legal/aup (`c4-pol-shopify-aup.md`).
- Text: "You can't use Shopify to do anything that's illegal where you do business." and "certain business activities are not supported by our platform, such as uploading Protected Health Information subject to HIPAA." and "you can't sell products that facilitate intentional self-harm." There is no mention of styling, design or consulting services. `verified` (what it says). `inferred`: a styling service is allowed. The Help Center explicitly documents selling a service (4.4).

---

## 6. File upload from a static page without a backend

All five tools can be a plain link. Only Formspree needs a `<form>` on our page.

| Tool | Free limits (vendor words) | File upload | Respondent sign-in | Spam | Emails the owner | Link vs embed |
|---|---|---|---|---|---|---|
| Tally | "unlimited forms and submissions, completely free, as long as you stay within our fair usage guidelines" | "File uploads are free for all Tally users. The free plan supports individual files up to 10 MB." | "Unlike Google Forms and other tools, your respondents don't need to log in to upload files." | "We support reCAPTHAv2, which is available for free to all Tally users." | "Self email notifications" on the free list | Plain link, plus "Standard, Popup, Full page" embeds, "Embedding forms is a free Tally feature." |
| Formspree | Free: "limited to 50 submissions/mo" | Free 0 GB; Personal 1 GB; Professional 5 GB; Business 10 GB. "each limited to 25MB". "No files will be sent directly by email." | Not required (plain HTML form post, `inferred`) | Formshield ML on all plans, reCAPTCHA one click, "Restrict to domain"; custom honeypot Business only | Yes, links to files in the email | Needs `<form action="https://formspree.io/FORM_ID" enctype="multipart/form-data">` on our page |
| Google Forms | Free | "File upload... To answer this question, responders need to sign in to a Google Account." Files land in the owner's Drive. | **Required** | n/a | Not read this session | Plain link works |
| Jotform | Starter: "5 Forms", "100 Monthly Submissions", "100 MB Available Space" | "Once you reach your account upload limit, your form will show an Over Quota error that'll block users from submitting it." | Not stated | "add a captcha element" (hCAPTCHA default) | Not read | Plain link and embed (embed not read) |
| Typeform | Free: "10 responses/month" | "The File Upload question is a Basic account and higher feature", "maximum file size of 10MB"; Basic is $39/mo monthly, $28/mo yearly, "100 responses/mo" | Not stated | ReCAPTCHA is listed on the Talent plan only | Not read | Plain link and embed (not read) |

Sources: Tally https://tally.so/pricing, https://tally.so/help/file-uploads, https://tally.so/help/embed-your-form, https://tally.so/help/recaptcha (`c4-form-tally-pricing.md`, `-uploads.md`, `-embed.md`, `-recaptcha.md`); Formspree https://formspree.io/plans, https://help.formspree.io/articles/building-your-form/file-uploads (`c4-form-formspree-pricing.md`, `-uploads.md`); Google https://support.google.com/docs/answer/7322334 (`c4-form-gforms-qtype.md`; `-addq.md` and `-upload.md` are context pages); Jotform https://www.jotform.com/pricing/, /help/how-to-free-up-space-in-your-accounts-upload-limit/, /help/how-to-prevent-spam-form-submissions/ (`c4-form-jotform-*.md`); Typeform https://www.typeform.com/pricing/, https://help.typeform.com/hc/en-us/articles/360051567012, /360032972852 (`c4-form-typeform-*.md`). Google Forms: also confirmed by a WebSearch of support.google.com ("a file upload question requires respondents to sign in"). `verified`.

**Disagreements (X verified, Y need review)**
- Tally Pro price: the pricing page shows "$24 per month"; the uploads help page says "Tally Pro removes the 10MB file size limit per file at $29/month". Both verified, which is current needs review. Free tier is unaffected.
- Formspree files per submission: the plans table says "up to 5 files in each form submission (each limited to 25MB)"; the plain-text summary of the same page says "up to 10 files". Both on one URL. Plan gating (Personal and up) is consistent in the help article ("Available on: Personal, Professional, Business plans"). Count needs review.
- Formspree price: monthly $15 / yearly $10 per month for Personal, from the page summary. `verified`.
- Typeform: pricing text says "Available on all plans except Free and Basic" for some feature and the free-plan help says "10 responses/month". The page notes "We sometimes experiment with our pricing plans". Treat Typeform numbers as moving.

**Video:** Tally's free cap is 10 MB per file, Acuity's is 5 MB, Typeform's is 10 MB, Formspree's is 25 MB. A 24-second phone video is already over those (`inferred`). Do the walkthrough live on the call, or add a text field "link to a video (Google Photos, iCloud, Drive)".

---

## 7. The `mailto:` baseline

- Pages: RFC 6068 https://www.rfc-editor.org/rfc/rfc6068.html (`c4-mail-rfc6068.md`), MDN https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Creating_links (`c4-mail-mdn-links.md`) and `a` element (`c4-mail-mdn-anchor.md`), Microsoft mailto protocol (`c4-mail-msft.md`), Wikipedia (`c4-mail-wikipedia.md`), RapidTables (`c4-mail-rapidtables.md`), Microsoft Q&A (`c4-mail-msqa.md`). Stack Overflow's "effective maximum mailto body lengths" was walled (WebFetch: "unable to fetch from stackoverflow.com").
- Prefill works: MDN: "any standard mail header fields can be added to the mailto URL you provide. The most commonly used of these are "subject", "cc", and "body" (which is not a true header field, but allows you to specify a short content message for the new email)." and "The values of each field must be URL-encoded with non-printing characters... and spaces percent-escaped." `verified`.
- Encoding rules (RFC 6068): "line breaks in the body of a message MUST be encoded with "%0D%0A"." and "Within 'mailto' URIs, the characters "?", "=", and "&" are reserved, serving as delimiters. They have to be escaped (as "%3F", "%3D", and "%26", respectively) when not serving as delimiters." So **"Holliewood & Vine" in the subject must be `Holliewood%20%26%20Vine`**, or the query string breaks. `verified`.
- Attachments: RFC 6068 says the "body" value is "the content for the first text/plain body part of the message" and is "primarily intended for the generation of short text messages for automatic processing... not for general MIME bodies". The RFC text contains no occurrence of "attach" (grep count 0), and the client "MAY also choose to create a message with only a subset of the header fields given in the URI." So the standard cannot prefill attachments. `verified`. Any client-specific `attach=` extension: `unverified`, not read, do not rely on it.
- Length: RFC 6068 states no limit. Practical limit: `unverified`. The only figure I found is an AI-written Microsoft Q&A answer about Outlook hyperlinks (2,084 characters historically, 8,192 in newer builds), which is about message-body links, not `mailto:` handlers. I treat about 2,000 characters as the working ceiling (`inferred`, the classic URL length habit). The sample below is 1,036 and the short one is 703.
- Generate the href with Python, not by hand: `urllib.parse.quote(text, safe='')` on the subject and on the body joined with `"\r\n"`. In an HTML attribute write the `&` between `subject=` and `body=` as `&amp;` (`inferred`, standard HTML rule, not read this session).
- No-mail-client visitors: show the plain address next to the button (`inferred`). Hollie can use a shop-only address.
- Photo checklist goes on the page, not into the body. The body is a short brief.

**Sample prefilled mailto (generated by Python, 1,036 characters; `YOURDOMAIN` is a placeholder for Hollie's address, which I do not have)**

```
mailto:hello@YOURDOMAIN.com?subject=Fabulous%20From%20Online%20request%20-%20Holliewood%20%26%20Vine&body=Hi%20Hollie%2C%0D%0A%0D%0AI%20need%20help%20with%20%28pick%20one%29%3A%20find%20an%20item%20%2F%20decorate%20a%20room%20%2F%20a%20corner%20or%20section%20%2F%20a%20whole%20studio%20or%20house%0D%0AWhere%20%28city%2C%20and%20home%20%2F%20studio%20%2F%20rental%29%3A%0D%0ARooms%20or%20areas%3A%0D%0ABudget%20range%3A%0D%0ANeeded%20by%20%28flexible%20%2F%20within%206%20weeks%20%2F%20rush%29%3A%0D%0AHow%20I%27d%20like%20to%20work%20%28video%20call%20%2F%20photos%20%2B%20email%20%2F%20in%20person%29%3A%0D%0AStyle%20words%20or%20things%20I%20love%3A%0D%0AThings%20I%27m%20keeping%3A%0D%0AHard%20no%27s%3A%0D%0AInspiration%20link%20%28Pinterest%20%2F%20Google%20Photos%20%2F%20iCloud%29%3A%0D%0ABest%20days%20and%20times%20for%20a%20call%3A%0D%0AMy%20name%20and%20phone%3A%0D%0A%0D%0AI%27m%20attaching%20photos%20to%20this%20email%3A%20a%20wide%20shot%20of%20each%20space%20plus%20one%20of%20each%20corner%2C%20taken%20in%20daylight.
```

Decoded subject and body (what the visitor sees):

```
Subject: Fabulous From Online request - Holliewood & Vine

Hi Hollie,

I need help with (pick one): find an item / decorate a room / a corner or section / a whole studio or house
Where (city, and home / studio / rental):
Rooms or areas:
Budget range:
Needed by (flexible / within 6 weeks / rush):
How I'd like to work (video call / photos + email / in person):
Style words or things I love:
Things I'm keeping:
Hard no's:
Inspiration link (Pinterest / Google Photos / iCloud):
Best days and times for a call:
My name and phone:

I'm attaching photos to this email: a wide shot of each space plus one of each corner, taken in daylight.
```

The field choices come from the forms in section 2: budget, timeline with a rush option, rooms, keep list, hard no's, inspiration link, how they want to work.

---

## 8. Vendor table

| Tool | Free tier | Payment at booking | Intake questions | File upload | Embed or link | Source URL |
|---|---|---|---|---|---|---|
| Calendly | Free: 1 event type, 1 calendar | Standard $10/seat/mo (yearly): Stripe, PayPal | Up to 10 per event type, 6 answer types | No (staff, 2023: "no way to allow attachments") | Inline, pop-up text, pop-up widget, link | https://calendly.com/pricing |
| Cal.com | "Free forever", unlimited event types and calendars | Free list: "Accept Stripe & PayPal payments" | Yes, required or optional; question identifiers prefillable | No (GitHub request closed "not planned", 2024-05-09) | Inline, floating button, element click, email, link | https://cal.com/pricing |
| Google Calendar appointment schedules | One booking page on a personal account; name and photo public | Workspace Individual or higher, Stripe only (card, Apple Pay, Google Pay); no platform fee | First/last/email plus "Add an item" (types unverified) | Unverified | "Button with popup", "Inline booking page", link | https://support.google.com/calendar/answer/10729749 |
| Square Appointments | Free plan exists; plan price not rendered | Prepayment and deposits listed; plan unverified; online card 3.3% + 30¢ (Free, inferred) | Digital forms need Plus or Premium | Unverified | Book Now button, QR code, booking widget | https://squareup.com/us/en/appointments/pricing |
| Acuity | None; 7-day trial; Starter $16/mo yearly, $20/mo monthly | Stripe, Square, PayPal, Venmo on all plans | "Custom client forms" on Starter | File Upload question, up to 5 MB each, plan unverified | Embedded scheduler, booking button, booking bar, link | https://acuityscheduling.com/pricing |
| Stripe Payment Links | No monthly fee; 2.9% + 30¢ domestic cards | n/a (payment link, can redirect to booking link) | Custom fields: text (255 chars), numbers, dropdown | No | Plain link, `<stripe-buy-button>` script | https://docs.stripe.com/payment-links |
| Square payment links | "Add for free"; up to two custom fields | n/a | Up to two custom fields | No | Link, QR | https://squareup.com/help/us/en/article/6692-get-started-with-square-checkout-links |
| PayPal | 3.49% + 0.49 USD (Checkout); 2.99% (goods and services send) | n/a (one-time link) | None documented | No | Link | https://www.paypal.com/us/business/paypal-business-fees |
| Shopify Forms | Needs a Shopify store (none yet) | Separate (service product, shipping off) | Fields incl. custom metafields | Unverified | Theme embed only | https://help.shopify.com/en/manual/promoting-marketing/create-marketing/forms-app/create |
| Tally | Unlimited forms and submissions | Lists "Collect payments" on the free feature list; processor not read | Unlimited | Yes, 10 MB per file free, no sign-in | Link, standard, popup, full page | https://tally.so/pricing |
| Formspree | 50 submissions/mo, 0 GB uploads | n/a | HTML form fields | Personal+ ($10/mo yearly), 25 MB per file | Form POST from our page | https://formspree.io/plans |
| Google Forms | Free | n/a | Yes | Yes, respondent must sign in to Google | Link | https://support.google.com/docs/answer/7322334 |
| Jotform | 5 forms, 100 submissions/mo, 100 MB | Stripe, PayPal, Square integrations listed | Yes | Yes, 100 MB total on Starter | Link, embed | https://www.jotform.com/pricing/ |
| Typeform | 10 responses/mo | n/a | Yes | Basic+ ($28/mo yearly), 10 MB | Link, embed | https://www.typeform.com/pricing/ |

---

## 9. Ladder ranking

| Rung | What | Verdict | Why |
|---|---|---|---|
| (a) | `mailto:` with subject and body, plus photo checklist on the page | **Do now** | No vendor, no script, no account; matches how Megan Meyers and Of Houses and Trees collect photos; nothing to host or secure |
| (c) | Booking link for the video call | **Do now** (plain link) | Cal.com Free handles tiers (video, in person, rush as separate event types); Sites iframe policy is undocumented, so a link |
| (d) | Payment-link deposit | **Do now, outside the page** | Hollie pastes a fixed-price Stripe link in the scoping reply; Sites Terms 2.6 allows a third-party processor |
| (b) | Hosted form link that takes photos | **v2** | Tally free; the only free tool with no-login upload |
| (e) | Embeds (Cal.com inline, Stripe buy button, Tally inline) | **Skip until proven** | No Sites documentation on iframes or external scripts; no CSP header seen, so likely works, untested; a link has no such risk |
| (f) | Worker route `/api/...` with D1, optional R2, email, Turnstile | **v3, last** | Needs email key, spam protection, review path and a privacy policy |

---

## 10. Recommendation

### v1: ship this week (rungs a + c, plus d by hand)
Page copy and structure:
1. One section, "Holliewood & Vine Fabulous From Online". Four service cards (find an item; a room; a section or corner; a studio or a whole house). Two upgrade lines: "In person" and "Need it done now (rush)", each with "from $___" left for Ricky and Hollie.
2. A photo checklist on the page (taken from Havenly, Megan Meyers and Megan Baker): wide shot from the doorway, one photo of each corner, each wall face-on with ceiling and floor, daylight with lamps off, do not tidy, no wide-angle lens, rough measurements (room length and width, windows, doors), "keeping / maybe / hard no" list, a budget number, an inspiration link.
3. A button "Email Hollie" using the sample `mailto:` above, with the plain address under it and the line "Attach your photos to the email that opens."
4. A button "Book a video call" linking to the Cal.com page (opens in a new tab).
5. A one-line note: "After we talk, Hollie will send a payment link for your deposit." No payment collected on the page.
6. No new npm dependency, no new script. This is two `<a>` tags in `storefront.html`. Note: this file is source for the build, so Hollie or Ricky edits it and publishes through Codex.

Setup Ricky does outside the site:
- **Cal.com** (https://app.cal.com/signup, Free): create one booking link per offer (e.g. "Video call - one room", "Video call - whole space", "Rush call", "In-person visit"), set availability, set meeting location to a video app, then open each link, go to **Booking form**, click **Edit** next to a question and add the intake questions (rooms, budget, needed by, inspiration link). Connect Stripe in the Cal.com app store and set a price on the paid links ("decide which of your bookable events have charges and exactly how much those are"). Copy each link.
- **Stripe** (https://dashboard.stripe.com/payment-links/create): create one Payment Link per tier, selling "a product or service" at a fixed price (design consult deposit, rush fee, in-person visit). Under **After the payment** choose redirect to the Cal.com booking link or a thank-you message. Do not add custom fields for anything sensitive. Keep the links in a notes file; Hollie pastes the right one into the reply.
- **Optional email**: a shop-only address instead of a personal one for the `mailto:`.
- **Privacy**: `mailto:` collects nothing on the site. Sites help still says to review features that collect personal data; v1 collects none.

### v2: add a form and paid booking (rungs b, d wired up)
- **Tally** (https://tally.so/create, Free): build the form with the fields from 2.2 and 2.3 plus a Rush toggle; type `/file` to insert a file upload block, allow multiple files, set allowed types to images. Turn on **Self email notifications**. Set **Redirect on completion** to the Cal.com booking link. Share the form link (do not embed). Put "Send photos here" next to the mailto button; the mailto stays as the fallback.
- Add a text field "Link to a video (Google Photos, iCloud, Drive)". Do not ask for video uploads.
- Turn on Cal.com payments for the video-call links so the deposit is taken at booking, or keep Hollie pasting Stripe links if that suits better.
- Accounts needed: Cal.com, Stripe, Tally. No keys land in the repo.

### v3: the worker route (not before v2 proves demand)
Needs, all `verified` unless marked:
- A new route in `site/room-worker.mjs` beside `/api/room-preview`, reusing its guard (`origin` must equal `url.origin`, reject `sec-fetch-site: cross-site`). `run_worker_first: ["/api/*"]` already routes `/api/*` to the worker.
- Storage: D1 table for submissions (D1 is bound as `DB`). Photos need R2, which is not bound today; the existing `MAX_BODY` is 4 MB of JSON. R2 is documented for Sites; how to add the binding needs review.
- Email notification: an email vendor key stored as a Sites secret. Resend Free: "$0 / mo", "3,000 emails / mo", and in the limits table "Daily limit | 100". Postmark Free: "100 emails/month." (Basic from $15/mo.) Resend sends via `api.resend.com` with an `re_...` key (key format shown in the docs). Needs a verified sender domain for real mail (`unverified`, not read).
- Spam protection: Cloudflare Turnstile Free plan: "Up to 20 widgets", "Unlimited challenges", "10 hostnames per widget". Server side is mandatory: "You must call the Siteverify API to complete your Turnstile implementation. The client-side widget alone does not protect your forms." "Tokens expire. Each token is valid for 300 seconds (5 minutes)." "Tokens are single-use." Needs a Cloudflare account for the site and secret keys. The Sites docs mention nothing about Turnstile. `verified` for Turnstile, the pairing with Sites is `inferred`.
- A way for Ricky to read submissions: the notification email is the main path; D1 can be queried by Site editors ("Editors can also inspect the live database"). A private review page needs an authentication-enabled site (docs: "Public sign-in or an external identity provider | An authentication-enabled site"). `verified`.
- A privacy policy page linked from the form, per the Sites help.
- Publishing goes through Codex like every other change; `git push` does not deploy.

### Rejected or deferred
- Calendly: free tier has one event type and no payments. Fine as a fallback, not as the pick.
- Google booking page: public personal name and photo, no payments on personal accounts.
- Acuity: the only booking tool with an upload question, but no free tier and a 5 MB cap.
- Etsy for the service: against Help Center wording; policy pages need review.
- Formspree: Free has 0 GB uploads and needs a form POST from our page.
- Shopify Forms and Shopify booking apps: useful once a Shopify store exists; not for this page.

---

## 11. Open items for Ricky

1. Hollie's real shop email address for the `mailto:` (I used `hello@YOURDOMAIN.com`).
2. Prices for each tier and the rush and in-person upgrades. I found Selby House at $120/hour with a $2,500 typical minimum budget as one anchor only (2.5).
3. Whether to create an Etsy listing at all for the service (recommend no; Etsy legal pages need a human read through a browser).
4. The `hollywood-and-vine-vintage...chatgpt.site` slug and wrangler `name`: not the shop's spelling.
5. Whether Sites can add the R2 binding (`hosting.json` shows `"r2": null`).

## Raw files by section (`research/fabulous-from-online/raw/`)
- Sites: `c4-sites-*.md`, `c4-sites-live-headers.txt`
- Intake: `c4-intake-*.md` (`c4-intake-vintagesplendor.md` is 0 bytes, walled)
- Booking: `c4-cal-*.md`, `c4-tool-calendly-embed.md`
- Payment and Shopify: `c4-pay-*.md`
- Policy: `c4-pol-*.md` (Etsy legal captures are 4 bytes each, walled; `c4-pol-etsy-whatcanisell.md` and `-reselling.md` are Etsy Help Center pages and were read)
- Forms and APIs: `c4-form-*.md`, `c4-api-*.md`
- mailto: `c4-mail-*.md`
