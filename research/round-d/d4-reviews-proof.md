<!-- Saved verbatim by the parent Opus session from agent d4's final message, 2026-10-29 (the harness refuses subagent report writes). -->

# d4: reviews and social proof for a one-of-one shop

Agent d4, accessed 2026-10-29. Raw captures: `research/round-d/raw/d4-*.md` (saved; the parent writes this report to `research/round-d/d4-reviews-proof.md`).
Method: SearXNG (`tools/search.sh`) for URLs, crawl4ai (`tools/crawl.sh`) for pages, about 45 pages read live this session. Two WebSearch calls (Etsy vintage-shop results) were used for orientation only, so anything resting on them is `unverified`. WebFetch was tried on Etsy shop and Etsy handbook pages and got HTTP 403. No Patchright. Primary text came from ecfr.gov, flsenate.gov and copyright.gov.
Tags: `verified` = read live on the page this session. `inferred` = my reading of what the page implies. `unverified` = not read on a primary page.

Walls and dead pages (not retried): Etsy `/legal/prohibited`, `/legal/community`, `/legal/terms`, `/legal/policy/shilling`, `/legal/sellers` (all 4 bytes); Etsy seller-handbook "5 ways to get great reviews" (0 bytes, WebFetch 403); Etsy shop pages LampGoods, SugarRunHome (4 bytes; WebFetch 403); Instagram help and terms (4 bytes); copyright.gov Circular 1 PDF (4 bytes); Virginia Vintage (4 bytes); Ruby Lane (4 bytes); 1stDibs dealers (32 bytes); Google Maps policy 7400114 (404, though Google's prohibited-content page on the same policy was read); lostandloved.com (0 bytes; the .co.uk site was read). Trustpilot pages returned navigation only, so Trustpilot fees and rules are `unverified` and left out of the plan.

## TL;DR

1. **For a shop where nothing repeats, proof lives at shop level, because product reviews die with the listing.** Judge.me's Etsy Sync does not bring over "Reviews from inactive, sold-out, draft, or expired Etsy listings". For one-of-one vintage that skips almost everything. The manual JSON import works, but it assigns each review to a product and "won't be verified in Judge.me". Etsy's own shop rating is shop-wide. Judge.me store reviews are built for "eligible orders with unavailable products". Shopify's Shop-app reviews are product-level and are a poor fit. `verified`.
2. **Most small vintage shops show no review widget at all.** In 8 shops read (section 10), proof is carried by place, tenure, curation or authentication: "Since 2014 / 250+ sales", "WALK-INS WELCOME", "personally sourced, authenticated", "ONE OF ONE". Only Scandiwegians (a spare-bedroom lamp shop) and Chairish run visible review proof. So Holliewood & Vine can open with proof that is not stars. `verified` (homepages only).
3. **The FTC rule (16 CFR Part 465, effective 2024-10-21) allows what a new shop needs: invite every buyer, the same way, to post an honest review.** It bans fake reviews, buying reviews of a "particular sentiment", insider reviews without disclosure, and misrepresenting that the reviews shown are all or most when you hide bad ones. `verified`.
4. **Platforms are stricter than the FTC, so the plan follows the strictest source: no incentives, no insider reviews, no happy-customers-only asks, newest-first sort.** Google, the Shopify Shop app and Judge.me's own policy-driven setting all go further than Part 465. See "Where sources disagree".
5. **The "in its new home" photo program needs four things in one line:** the buyer owns the photo, anyone recognizable said yes (Florida s. 540.08), the shop says exactly where it will appear, and nobody was paid. If you announce in advance that photos "might be featured", the FTC wants that disclosed next to the photos. Drafted below.
6. **Google Business Profile is closed to an online-only shop.** Google lists "Brands, organizations, artists, and other online-only businesses" as ineligible. A service-area profile may open once the in-person Cameo service is live. That is `inferred` and needs Ricky's call.
7. **Day 90 lines up with Etsy's Star Seller clock.** Eligibility starts 90 days after the first sale and needs 5 orders and $300 in 3 months, a 4.8+ average, 95% first-reply in 24 hours and 95% on-time shipping. It is a milestone, not a promise.
8. **Honest ceiling on "10 reviews in 90 days":** you cannot get 10 reviewers from fewer than 10 buyers or clients. I found no verified review-response rate, so the plan is keyed to asks per order and platform timings, not a predicted yield.

---

## 1. FTC rule text: 16 CFR Part 465 (primary)

- URL: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465 — raw `d4-ecfr-465.md`. Page states: "Displaying title 16, up to date as of 10/27/2026." Source note: "89 FR 68077, Aug. 22, 2024".
- Evidence, verbatim:
  - Buying: "It is an unfair or deceptive act or practice and a violation of this part for a business to provide compensation or other incentives in exchange for, or conditioned expressly or by implication on, the writing or creation of consumer reviews expressing a particular sentiment, whether positive or negative" (465.4). `verified`
  - Definition of buying: "Purchase a consumer review means to provide something of value, such as money, gift certificates, products, services, discounts, coupons, contest entries, or another review, in exchange for a consumer review." (465.1(m)). `verified`
  - Safe harbor for broad asks: 465.2(d)(1) exempts "Reviews or testimonials that resulted from a business making generalized solicitations to purchasers to post reviews or testimonials about their experiences with the product, service, or business". `verified`
  - Insiders: an officer or manager's review "fails to have a clear and conspicuous disclosure of the officer's or manager's material relationship to the business" is a violation (465.5(a)). `verified`
  - Suppression: "to materially misrepresent... that the consumer reviews... represent most or all the reviews submitted... when reviews are being suppressed (i.e., not displayable) based upon their ratings or their negative sentiment" (465.7(b)). Allowed filters must be applied "equally to all reviews submitted without regard to sentiment", e.g. reviews with defamatory content, another individual's personal information or likeness, content "clearly false or misleading", or "wholly unrelated" content. `verified`
  - Threats: unfounded legal threats, physical threats, intimidation or knowingly false public accusations to stop or remove a review are banned (465.7(a)). `verified`
- Penalty: 16 CFR 1.98, eCFR current to 10/27/2026, lists "Section 5(m)(1)(A) of the FTC Act... —$53,088" and says the amounts "apply only to penalties assessed after January 17, 2025". Raw `d4-ecfr-1-98.md`. `verified` for the figure. That Part 465 penalties run through 5(m)(1)(A) is `inferred`; the FTC says only that the rule allows "civil penalties against knowing violators" (`d4-ftc-press.md`, `verified`). A newer annual adjustment may exist.
- **Steal this:** the generalized-solicitation safe harbor is the whole plan: one ask, same words, to every buyer. Write the shop's moderation rule as an equal-treatment rule before the first review lands.

## 2. FTC staff Q&A on the rule

- URL: https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers — raw `d4-ftc-qa.md`. Also the press release https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials, raw `d4-ftc-press.md`.
- Evidence, verbatim:
  - "went into effect on October 21, 2024... The rule authorizes courts to impose civil penalties for knowing violations". `verified`
  - Caveat on the Q&A itself: "Our staff guidance isn't definitive or comprehensive, and it doesn't provide a safe harbor from potential liability." `verified`
  - "The rule does not prohibit giving incentives for reviews, as long as there isn't an express or implied requirement that the reviews have to express a particular sentiment. But remember that failing to disclose incentives could be a violation of the FTC Act." `verified`
  - Wording that steers: "Tell us how much you loved your visit to John's Steakhouse and get a $5 coupon" is given as implying the review must be positive. `verified`
  - Family: "I own a small business. Can I ask my family members to write consumer reviews of my business? Yes, but ask them to clearly and conspicuously disclose their relationship to your business." `verified`
  - Happy-only asks: "Can my business ask for reviews only from customers whom we think are happy with our services? The rule does not contain a specific prohibition against such conduct. But this practice could violate the FTC Act." `verified`
  - Unhappy customers: the rule does not prohibit "contacting customers who post negative reviews to resolve the reported issues" or "simply asking satisfied customers to update their reviews". `verified`
  - Public replies: "Yes, you can respond publicly to the review, and yes, you should watch what you say." `verified`
  - Sort order: "Organizing reviews is not suppressing reviews under the rule." and for rating-first default: "the rule does not cover that situation. However, organizing reviews in a way that makes it difficult for consumers to know about or find negative reviews could be an unfair or deceptive act". `verified`
  - Cherry-picking in marketing: the suppression provision applies only to a review section, "However, the use of non-representative consumer reviews in marketing could be deceptive in violation of Section 5". `verified`
  - An incentivized review is also a testimonial: "if a business pays for or gives incentives for consumer reviews... those incentivized reviews would also be considered consumer testimonials under the rule." `verified`
- **Steal this:** the Steakhouse example is the voice test. Hollie's vain, witty tone will drift into "tell us how much you adored it". Strip every adjective about the buyer's feelings from the ask.

## 3. FTC Endorsement Guides and the Guides Q&A

- URLs: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255 (raw `d4-ecfr-255.md`); https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking (raw `d4-ftc-endorse-qa.md`, duplicate `d4-ftc-endorse-qa2.md`).
- Evidence, verbatim:
  - Quotes: "An advertisement need not present an endorser's message in the exact words of the endorser unless the advertisement represents that it is presenting the endorser's exact words, such as through the use of quotation marks. However, the endorsement may not be presented out of context or reworded so as to distort in any way the endorser's opinion or experience" (255.1(b)). `verified`
  - Press excerpts count: "A film critic's review of a movie is excerpted in an advertisement placed by the film's producer. The critic's review is not an endorsement, but when the excerpt from the review is used in the producer's advertisement, the excerpt becomes an endorsement." (255.0 Example 1). `verified`
  - Handling reviews: "In procuring, suppressing, boosting, organizing, publishing, upvoting, downvoting, reporting, or editing consumer reviews of their products, advertisers should not take actions that have the effect of distorting or otherwise misrepresenting what consumers think of their products" (255.2(d)). `verified`
  - Material connections include "the provision of free or discounted products... regardless of whether the advertiser requires an endorsement in return" and "the possibility of being paid, of winning a prize, or of appearing on television or in other media promotions" (255.5(a)). `verified`
  - The new-shop scenario: "I'm starting a new online business and I don't have money for advertising... it's okay to invite all of your customers to post honest reviews, positive or negative, after they've actually used your products or services." Same answer: you can't condition a discount on a positive review, and "(Note, however, that many platforms prohibit such incentives.)" `verified`
  - Asking only some people: "Only asking for reviews from customers who you think are more likely to be happy with your product would be misleading if it substantially skews the favorability of the reviews." `verified`
  - Featuring customers: "if customers are told in advance that their comments might be used in advertising, they might expect to receive a payment for a positive review... even if you tell your customers you aren't going to pay them but they might be featured in your advertising, that opportunity might be seen as having a value. So the fact that they knew this when they gave the review should be disclosed (e.g., 'Customers were told in advance they might be featured in an ad.')." `verified`
  - Delay: "you should delay posting all reviews, positive and negative, for the same, reasonable period of time." `verified`
  - Fixing a bad review: you may "ask them if they'll add updates to their reviews. However, asking them to change or delete their initial negative reviews could mislead readers." `verified`
  - Default sort: five-stars-first "could get a misleading picture... This is true even if you give consumers the option to re-sort the reviews". `verified`
- **Steal this:** the "told in advance they might be featured" line is a ready-made disclosure for the photo gallery. Ask for review and photo as two separate steps, or announce featuring and add that line.

## 4. Etsy: what the review system gives a one-of-one shop

- URLs: https://help.etsy.com/hc/en-us/articles/360000572708-How-the-Review-System-Works-for-Sellers (raw `d4-etsy-review-system.md`); https://help.etsy.com/hc/en-us/articles/115013197687 (`d4-etsy-when-can-buyer-review.md`); https://help.etsy.com/hc/en-us/articles/115015808588 (`d4-etsy-negative-review.md`); https://help.etsy.com/hc/en-us/articles/4403058372503 (`d4-etsy-star-seller.md`).
- Evidence, verbatim:
  - "Buyers have 100 days to review an order, beginning on the delivery date or estimated delivery date." `verified`
  - "Reviews can only be left for items sold through Etsy." (an in-person Square sale cannot be reviewed on Etsy). `verified`
  - "If a buyer includes a photograph or video in their review, this will be visible to anyone who looks at your reviews." `verified`
  - Buyers can rate "Item Quality, Shipping, and Seller Customer Service" as well as overall (`d4-etsy-when-can-buyer-review.md`). `verified`
  - Removal: "Etsy Support cannot remove a review at a seller's request." A compliant negative review stays. A buyer "is able to edit their review within 100 days of the estimated delivery date... if you haven't responded to the review." Reviews that "Include shilling or otherwise falsely inflate a shop's review score" violate Etsy policy. `verified`
  - Star Seller: "You're eligible to become a Star Seller starting 90 days after your first sale... received at least 5 orders and $300 in sales over the past 3 months." Plus "reply to 95% of first messages in a thread within 24 hours", "95% of orders ship on time", "Average review ratings: 4.8+". Reviewed on the 1st of every month. "Star Seller badges do not directly impact your search ranking." `verified`
  - Etsy may disqualify a shop it has "reason to believe you attempted to falsely inflate your Star Seller stats". `verified`
- Not read (walled): Etsy's seller policy on asking for reviews or offering incentives, and Etsy's terms on who may reuse buyers' review photos. Both `unverified`.
- **X verified, Y need review:** Etsy's seller page says the score "is a recency-weighted average of all the star ratings... the weight it carries in the average calculation decreases by half each year." The buyer page says "A shop's rating is the average of the reviews they've received in the past 12 months." Two Etsy pages describe the shop score two ways. Need review before Hollie quotes a number.
- **Steal this:** Etsy is the one surface where the review is tied to a real order, which makes it the strongest proof you cannot be accused of faking. Count the 100-day window and the 90-day Star Seller line in the plan, and answer 95% of messages within 24 hours from day 1.

## 5. Judge.me (free tier) and what it does with sold-out stock

- URLs: https://judge.me/pricing (`d4-judgeme-pricing.md`); https://judge.me/app/store-reviews (`d4-judgeme-store-reviews.md`); https://judge.me/help/en/articles/10713924-syndicate-reviews-from-etsy-to-judge-me-on-shopify (`d4-judgeme-etsy-sync.md`); https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file (`d4-judgeme-etsy-import.md`); https://judge.me/help/en/articles/8379747-offering-judge-me-generated-coupon-codes-for-reviews (`d4-judgeme-coupons.md`). Also read: `d4-judgeme-trust-manifesto.md`, `d4-judgeme-visual-reviews.md` (little usable detail).
- Evidence, verbatim:
  - Free, $0 per month: "Unlimited product & store reviews", "Unlimited photo & video reviews", "Google Rich Snippets". Awesome, $15 per month: adds "AI (snippets, summary, responses)", "Referrals & coupons". "$15 per month is the most you can ever pay us." `verified`
  - Install path: every call to action on the pricing page links to `apps.shopify.com/judgeme`. Whether Judge.me runs on a static ChatGPT Sites page was not shown. `unverified`
  - Store reviews: "A store review is a customer's feedback on the experience of buying from your business: the service, delivery, packaging and checkout." "Included in the Free plan." "For eligible orders with unavailable products or custom items, request a store review so the shopping experience can still be shared." `verified`
  - Etsy Sync is "Available on the Free plan", but "The following reviews are not synced from Etsy: Reviews from inactive, sold-out, draft, or expired Etsy listings". Synced reviews are "marked as verified"; the manual option can sync a listing's reviews "as store reviews". Synced Etsy reviews are not in the Google Shopping product ratings feed. `verified`
  - JSON import: "Etsy's JSON file doesn't include any Shopify product identifiers... You'll need to manually assign each review to a product", and "Reviews imported from Etsy won't be verified in Judge.me". The steps say "select the product for each review"; no store-review option is mentioned (silence, not a confirmed gap). `verified`
  - Coupons are Awesome-only: "Incentivized reviews are automatically tagged with the `<is_incentivized_review>` attribute in the Product Ratings feed for Google Shopping." And: "To comply with Shopify's Product Review Policy, the option to generate coupons based on review ratings... was removed." `verified`
- Not captured: which plan includes "Automatic Reminders" (listed under Collect Reviews on the pricing page without plan marks). Do not assume it is free. `unverified`
- **Steal this:** use the store-review prompt, not product reviews, on a one-of-one shop. Do not rely on Etsy Sync; budget for manual import. Leave coupons off: they are the one feature on the page that creates an incentive.

## 6. Shopify's own options

- URLs: https://community.shopify.com/t/whats-going-on-with-the-product-reviews-app-its-no-longer-available/249489 (`d4-shopify-community-reviews.md`); https://thornthwaitedesign.com/sunsetting-shopify-product-reviews/ (`d4-shopify-sunset-blog.md`); https://help.shopify.com/en/manual/online-sales-channels/shop/product-reviews (`d4-shopify-shop-product-reviews.md`), `/merchant-guidelines` (`d4-shopify-review-guidelines.md`), `/manage` (`d4-shopify-shop-reviews-manage.md`).
- Evidence, verbatim:
  - Retirement: a Shopify community reply (author "Elias", group "retired") says "the Product Reviews app has been sunset and delisted as of Sept 05, 2023", pointing to third-party apps. A web-agency blog repeats it and lists Judge.me, Loox, Okendo, Stamped.io and Yotpo as the migration partners. I read no Shopify Help Center page on the retirement, so this is `verified` as a staff reply plus one agency blog, not as official documentation.
  - Today's native option: "After a customer purchases a product through the Shop app or your online store, they can leave a product review in the Shop app... Only Shop customers that have purchased a product from you are allowed to submit a review." Reviews "are displayed on the product details page in the Shop app". "You can't opt out of receiving product reviews if you sell products on Shop." Review requests go out "between 1 to 180 days after delivery". `verified`
  - Guidelines for reviews on Shop: "If you encourage your customers to leave a review, then you need to do so in a neutral manner." "You shouldn't offer compensation in exchange for reviews. This includes money, discounts, free products, or refunds." You shouldn't "incentivize the customer to change or remove that review." A store owner's "employees, family members, or friends shouldn't review your products". `verified`
  - Whether those Shop guidelines bind reviews shown on your own storefront is not stated. `unverified`
- **Steal this:** Shop-app reviews attach to a product that will be sold out, and they show in the Shop app, not on the site. Treat them as a bonus, not the base.

## 7. Google: Business Profile reviews

- URLs: https://support.google.com/business/answer/13763036 (`d4-gbp-eligibility.md`); https://support.google.com/business/answer/2622994 (`d4-gbp-ask-reviews.md`); https://support.google.com/business/answer/3038177 (`d4-gbp-guidelines.md`).
- Evidence, verbatim:
  - "To qualify for a Business Profile, a business must make in-person contact with customers during its stated hours." Ineligible examples include "Brands, organizations, artists, and other online-only businesses." `verified`
  - Service-area businesses: "If your business doesn't have a storefront with clear signage but travels to customers at their physical locations, you're allowed one service-area Business Profile." "If you're a service-area business, you should hide your business address from customers." A "virtual office" that is "rented" and not operated from "isn't eligible". `verified`
  - Reviews policy: "We do not allow merchants to: Offer incentives – such as payment, discounts, free goods and/or services - in exchange for posting any review or revision or removal of a negative review. Discourage or prohibit negative reviews, or selectively solicit positive reviews from customers." Also no requests "that specific content be included" and no conflicts of interest, which Google says may include "familial relationships". Allowed: "Solicit or encourage the posting of content that does represent a genuine experience, without offering incentives to do so or attempting to influence the rating or the contents of the review." `verified`
- `inferred`: the online shop is ineligible; a service-area profile for the in-person styling service (the Cameo, which places furniture and hangs art in clients' homes per `docs/fabulous-from-online-design.md`) might qualify once it exists. Google was not asked. It would also hold service reviews, not product reviews.
- **Steal this:** Google's list is the cleanest statement of a neutral ask: invite everyone, no reward, no script.

## 8. Photo consent: law and the vendor flow

- Florida right of publicity: https://www.flsenate.gov/Laws/Statutes/2025/540.08 (`d4-fl-540-08.md`). "No person shall publish, print, display or otherwise publicly use for purposes of trade or for any commercial or advertising purpose the name, portrait, photograph, or other likeness of any natural person without the express written or oral consent to such use given by: (a) Such person; or..." Remedies include injunction, damages "including an amount which would have been a reasonable royalty, and punitive or exemplary damages". Consent for a minor "shall be given on behalf of a minor by the guardian of her or his person or by either parent". Exception for "any photograph of a person solely as a member of the public and where such person is not named or otherwise identified". `verified`. Written is not required by the statute (oral is listed); written is better evidence (`inferred`).
- Copyright: https://www.copyright.gov/what-is-copyright/ (`d4-copyright-what-is.md`). "Once you create an original work and fix it, like taking a photograph, writing a poem or blog, or recording a new song, you are the author and the owner." Owners have the right to "authorize others" to reproduce and display. `verified`. (Circular 1 PDF walled.) Consequence, `inferred`: a buyer's photo is the buyer's; the shop needs a license.
- Vendor flow: https://docs.emplifi.io/platform/latest/home/permission-and-message-best-practices (`d4-emplifi-permission.md`). "Before using collected user-generated content (UGC) on your website, social, or other marketing channels, you'll first need to ask permission from the original poster of the content." Ask "the user to explicitly give their consent", "Explain exactly where you plan to feature the content", "Avoid language that sounds too legal." For YouTube/TikTok, once granted "mark the content as permissioned and attach the proof for future reference." Example request ends with a reply of `#yesbrand`. `verified` (vendor guidance, not law).
- Not read: Instagram's own terms on reposting (walled) and Etsy's terms on reusing review photos (walled). `unverified`.
- **Steal this:** keep the "yes" as a saved message, name the places, and keep the sentence short enough to read on a phone.

## 9. Press and feature mentions as proof

- Chairish "As Seen In...": https://support.chairish.com/hc/en-us/articles/44244117139857-Press (`d4-chairish-press.md`). Each item is a one-paragraph description of the mention plus a link out, e.g. "shares alternatives to pricey built in cabinetry... Shop our collection on Chairish, and read the full article here" and "Featured alongside iconic picks". `verified`. It describes how the company appeared (quoted, featured alongside, rounded up) rather than implying an endorsement.
- HARO: https://www.helpareporter.com/about (`d4-haro-about.md`). "In April 2025, HARO was acquired by Featured.com." It is "a free, straightforward email newsletter", "Registered sources receive up to three email digests per day, Monday through Friday". "2024: Cision rebrands HARO as 'Connectively,' then permanently shuts the platform down in December." `verified` (the vendor's own history). The page says sources get credit "often with a link back to their website"; payment is described as "at no cost".
- Local magazine: https://gulfshorelife.com/contact-us (`d4-gulfshore-contact.md`). Gulfshore Life, Fort Myers; menu sections include "Local Designers" and "Shopping" under Home + Design; the page lists an editor in chief and a publisher with email addresses. `verified` for the sections and contacts. Whether it covers an online-only shop is `unverified`.
- Rules: an excerpt from coverage becomes an endorsement (255.0 Ex. 1), and quotation marks mean exact words (255.1(b)). No FTC page on "as seen in" logos was found; logo-use permission varies by outlet (`unverified`).
- **Steal this:** write each mention the way Chairish does, say exactly what happened, link the article, and quote only exact words. Do not display an "As seen in" row before there is coverage.

## 10. How small vintage shops display proof today (8 examples, homepages read this session)

1. **Scandiwegians** (vintage Danish lamps, "a micro business operating out of our spare bedroom in Reigate, Surrey"). https://scandiwegians.com/pages/reviews (`d4-scandiwegians-reviews.md`): links Trustpilot, says "We've been on Etsy for more than 7 years and have over 700 5 star reviews - you can see some of them below" and shows eight review screenshots. https://scandiwegians.com/pages/what-our-customers-say (`d4-scandiwegians-customers-say.md`): testimonials credited "Jane from Texas, USA", "Amy, from the South of France", with purchase photos labelled "added a photo of their purchase". `verified` for what is on the page; the "700" claim and whether buyers consented to reuse are `unverified`. One flaw: the "Lucy, from Hertfordshire, UK" entry has the same text as "Lori, from California USA", including "survived the long trip to California". It looks like a paste error. **Steal this:** first name plus place, and borrowed Etsy proof. **Do not steal this:** cropping 5-star screenshots with no link to the full list, and any testimonial that cannot be matched to its source. Keep the log.
2. **Chairish seller Modern Retro Finds** (Jersey City, NJ). https://www.chairish.com/shop/modernretrofinds (`d4-chairish-seller-modernretro.md`): "Since 2014", "250+ sales", a star row linking to a Reviews tab. `verified`. **Steal this:** tenure and sales band as proof, only when true.
3. **Chairish seller Fig + Stone** (Los Angeles). https://www.chairish.com/shop/figandstone (`d4-chairish-seller-figandstone.md`): "All items in this shop have sold" plus "founded by One Kings Lane design alum". `verified`. **Steal this:** a sold shop as proof and a credential line.
4. **Chairish itself.** https://www.chairish.com/pages/reviews (`d4-chairish-reviews.md`): seller testimonials such as "Listing is a snap!" credited "Ariel of Fig + Stone" with a link to her shop, and a third-party widget "4.41 avg. from 33168 Verified Reviews". `verified`.
5. **Vestige Vintage** (Punta Gorda, FL). https://www.vestigevintage.com/ (`d4-shop-vestige-home.md`): "By Appointment... private shopping appointment" and a Book An Appointment link; no review widget on the homepage as crawled. `verified`.
6. **Sunbeam Vintage** (Highland Park, LA). https://sunbeamvintage.com/ (`d4-shop-sunbeam.md`): banner "HIGHLAND PARK OPEN DAILY 10–6 • WALK-INS WELCOME • NEW VINTAGE ARRIVING DAILY"; no review section on the homepage. `verified`.
7. **Mercer Vintage** (Houston). https://mercervintage.com/ (`d4-shop-mercer-home.md`): "Every piece is personally sourced, authenticated, and chosen for lasting style" and "Follow @shop_mercer for first access." No reviews on the homepage. `verified`.
8. **George's Vintage** (UK clothing). https://georgesvintage.com/ (`d4-shop-georges.md`): "CURATED SECOND-HAND / ONE OF ONE / NEW FINDS REGULARLY"; no review section on the homepage. `verified`. Also read with no review proof on the homepage: Rescued and Reimagined Relics (studio "open by appointment"), Pop Sick Vintage, Lost and Loved UK.
- Pattern: a homepage-only read can miss reviews placed deeper in a site; Scandiwegians hides theirs under a nav menu. X verified (the homepages above), Y need review (any deeper page).

---

## Where sources disagree (X verified, Y need review)

1. **Incentives.** The FTC rule and Q&A allow incentives not tied to sentiment, with an Endorsement Guides disclosure (verified). Google says merchants may not "Offer incentives – such as payment, discounts, free goods and/or services - in exchange for posting any review" (verified). Shopify's Shop guidelines say "You shouldn't offer compensation in exchange for reviews. This includes money, discounts, free products, or refunds" (verified). Judge.me sells coupons for reviews but removed rating-based coupons for Shopify's policy (verified). Etsy's own policy page was walled, so Etsy is `unverified`. Plan follows the strictest: **no incentives of any kind.**
2. **Insider and family reviews.** FTC allows them with a clear and conspicuous disclosure (verified). Google lists "familial relationships" as a conflict of interest and Shopify's Shop rules ban friends and family (verified). Plan: **none from Hollie, Ricky, relatives or friends, on any platform.**
3. **Asking only happy customers.** Rule text is silent; the Guides Q&A says it "would be misleading if it substantially skews the favorability"; Google bans selective solicitation (all verified). Plan: **same ask to every order.**
4. **Default sort by rating.** Rule Q&A: "the rule does not cover that situation". Guides Q&A: five-stars-first is deceptive organizing even with a re-sort option (verified). Plan: **newest first** on any review section the site builds.
5. **Etsy shop score** formula: two Etsy pages differ (section 4). Need review.
6. **Penalty figure.** $53,088 per violation is the 45(m)(1)(A) cap in 16 CFR 1.98 (verified). That it applies to Part 465 is `inferred`; amounts are adjusted annually.
7. **Judge.me "verified".** Synced Etsy reviews are marked verified; JSON-imported ones are not (verified). Both are excluded from Google Shopping feeds (verified).

---

## 90-day plan: first 10 genuine reviews, inside the FTC rule

"Genuine" here means: from a real buyer or client, unpaid, unrewarded, not from Hollie, Ricky, relatives or friends, posted where the buyer chose, quoted unedited. Day 0 = first sale, not launch, because Etsy's windows run from delivery. Floor: 10 reviews needs at least 10 buyers or clients. I found no verified response rate, so measure your own ask-to-review ratio from the first 5 orders and size the plan from that.

**Before day 0 (no accounts needed)**
1. Write a one-page Review Rules sheet: ask every buyer in the same words at the same time; no discount, gift, entry or favor for a review or photo; no reviews from insiders; never ask anyone to change or delete a review (asking them to add an update is fine); public replies stay calm, no threats; any hide or withhold rule applies equally to all reviews (465.7(b) list: defamatory, another person's personal info, clearly false, unrelated).
2. Start the testimonial log (spreadsheet, or a D1 table later): date, platform, reviewer's displayed name, order or service, relationship to shop, link or screenshot, photo-consent status, and the saved "yes".
3. Draft the neutral ask for the box card (the box card is already decided): *"However it went, you're welcome to tell other people, good or bad, where you bought it. We read all of it."* Voice test before every edit: would a buyer feel nudged toward five stars? If yes, cut the line (this is the Steakhouse example in 465).
4. Keep the mirror-ball gift unconditional. It rides in the box before any review exists. Never write "thanks for the ball, now review us", and never send a gift after a review: Google bans "free goods... in exchange for posting any review". Name this for the lawyer pass (low risk, `inferred`).
5. Build the zero-review proof stack from what is already decided: condition grades, lamp spec block, packing photos, the returns line, Hollie's name and face, and the sold archive with a count that is only ever true (Chairish models: "Since 2014", "250+ sales", "All items in this shop have sold").

**Days 0 to 14**
6. Open Etsy when ready. Ship on time with tracking and reply to every first message within 24 hours: these are Star Seller thresholds (95% each).
7. Delivery day D: Etsy's 100-day review window opens by itself. Box card in the box.

**Days 14 to 45**
8. D+7 to D+10: one personal follow-up to every buyer: "did it arrive in one piece?" plus the same one-line invitation to review where they bought. One reminder at most. If something is wrong, fix it, then you may invite an update; never ask for a deletion.
9. D+21: a separate photo ask (below) to every buyer. Photo ask and review ask are two messages so the review is not conditioned on featuring.
10. Confirm Etsy's own text on asking buyers for reviews before sending (walled to me), and choose the channel accordingly.

**Days 45 to 75**
11. Day 45 check: orders, reviews, photo consents, complaints. If reviews are low per order, look at delivery experience first, not the ask wording.
12. Add a "Kind words" block on the site only once there are 3 or more genuine reviews, and only with exact quotes (quotation marks mean exact words), source and date, newest first, plus a link to the full list on Etsy. If you ever show a curated set, label it "Selected" and link the full list (255.2(b) non-representative warning).
13. Fabulous From Online: ask each client after the work, with the same neutral line. Tag any testimonial from a free Screen Test "Booked a free Screen Test" (free service is a material connection; `inferred`). No discount on a next booking in exchange.
14. If a Shopify account exists: install Judge.me Free, turn on the store-review prompt, leave coupons and referrals off, and import Etsy reviews by hand (assign each to a product; not verified). Do not count on Etsy Sync for sold pieces.

**Days 75 to 90**
15. Day 90: first Star Seller evaluation is possible only if first sale was 90+ days ago, with 5 orders and $300 in sales in the last 3 months, 4.8+ average, and the two 95% rates. Count genuine reviews. Orders delivered in the last weeks can still be reviewed up to 100 days after delivery, so the count lags.
16. If under 10 at day 90: keep asking every order. Do not recruit friends. Do not add an incentive.

## Photo-consent line (draft for lawyer review)

The ask (separate from the review ask):
> If you'd like to show us where [piece] ended up, send a photo. It's optional, nothing comes with it, and it's yours. Please keep faces, house numbers and mail out of frame unless you want them in.

The consent line (a checkbox or a reply the buyer types):
> Yes. Holliewood & Vine may show my photo of [piece] on its website, Etsy shop, Instagram and emails, credited as [first name, city]. I took the photo or have the right to share it, and anyone recognizable in it said yes. I wasn't paid or promised anything, and no review was required. I keep my photo; you may crop and resize it. I can ask for it to be taken down by emailing [address], and it will stop being used from then on.

The public line, near the gallery (the FTC example wording, adapted):
> Photos from buyers who were invited to send one and told we might feature it. Nobody was paid.

Notes: no children in photos (a parent's consent is required under 540.08(6)); save the buyer's reply as the record; if a buyer's words go with the photo, quote them exactly. The "stops being used from then on" revocation language is `inferred`, and the whole release should get a Florida attorney's review before volume use. Not legal advice.

---

## Recommendation for Holliewood & Vine

**What to do now (no accounts needed)**
- Adopt the Review Rules sheet and the testimonial log. They cost nothing and make every later claim defensible.
- Write the box card line and the follow-up messages; run the voice test.
- Build the zero-review proof stack so the site is not asking visitors to trust stars that do not exist yet. Do not show "0 reviews".
- If the D1 site ever adds a review area: sort newest first, apply moderation equally, delay nothing selectively, quote exactly.
- Draft the photo ask, consent line and gallery disclosure above.
- Decide with Ricky whether the Cameo makes a Google service-area profile worth setting up.

**What needs an account, a fee or a lawyer**
- Etsy shop (account): the strongest proof, because reviews are tied to real orders. Fees were not researched in this lane.
- Shopify and Judge.me Free (accounts): store reviews and photo reviews at $0 for Judge.me; the Shopify plan cost is another lane. Skip the $15 plan unless the AI features are wanted; skip its coupons on purpose.
- Google Business Profile (account, verification): only for the in-person service, with the address hidden.
- Lawyer: the photo release wording and revocation, whether a gift in the box and a free Screen Test need disclosure on testimonials, and any ch. 481 wording on client testimonials for the styling service (not researched here).
- Etsy's walled policy pages: someone with a seller login should read the review and shilling sections before the first ask goes out.

## Ideas for Hollie

1. A "Rehomed" counter on the site, a running count of pieces sold taken from the sold archive, shown only when true. (Chairish "250+ sales"; Fig + Stone "All items in this shop have sold".)
2. A "Where it landed" page: buyer photos credited first name plus city, each with a logged "yes". (Scandiwegians "Jane from Texas, USA"; Emplifi permission flow.)
3. A "Checked by Hollie" line on lamps: what was tested (cord, socket, harp), only if true. (Mercer "personally sourced, authenticated".)
4. Link out to the full Etsy reviews instead of copying screenshots. (Scandiwegians crop-risk; FTC Q&A on non-representative reviews.)
5. A press page that says exactly how each mention happened, quoted or featured alongside, with links, once there is coverage. (Chairish "As Seen In..."; 255.1(b).)
6. Pitch Gulfshore Life's Local Designers or Shopping sections when the Cameo is live and there is something to see. (Gulfshore contact page; HARO as the free route to local-press questions.)
7. A public reply policy: Hollie answers every review, including the cranky ones, calmly and in her voice. (Etsy negative-review page; FTC Q&A "you can respond publicly".)
8. A signed "before and after" case page for each styling job, with the client's release and a Screen Test tag if free. (FTC soliciting-endorsements Q&A; Florida s. 540.08.)
9. A neutral Hollie-voiced ask that survives the steering test: "Good, bad or somewhere in the middle, tell people where you found it." (FTC Steakhouse example; Shop "neutral manner".)
10. A box-card line for the photo ask that doubles as the disclosure: "Send a photo of it at home. We might feature it. Nobody gets paid." (FTC "told in advance" example.)
