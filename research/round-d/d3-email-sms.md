<!-- Saved verbatim by the parent Opus session from agent d3's final message, 2026-10-29 (the harness refuses subagent report writes). -->

# d3: email and SMS for a one-of-one shop

Agent d3, accessed 2026-10-29. Raw captures: `research/round-d/raw/d3-*.md` (55 files; the 4-byte, 37-byte and 191-byte ones are walls, listed below).
Method: SearXNG (`tools/search.sh`) for URLs, crawl4ai (`tools/crawl.sh`) for pages, about 41 pages read in full or grepped for limits, prices and rule text. That is above the 15-25 target because the law lane needed the 2020, 2022, 2023 and 2026 editions of the Florida statute to attribute the 2021 and 2023 amendments. WebFetch was tried twice (kit.com/pricing returned 429; the Justia 11th Circuit page returned 403), so nothing rests on it. WebSearch was used once, for Kit pricing, and was then superseded by Kit's own help page. One call to the Fedora crawl4ai REST endpoint returned `{"detail":"Authentication required"}`. Law text: 16 CFR and 47 CFR from eCFR, Florida from flsenate.gov, Federal Register from federalregister.gov. The US Code (15 USC 7704, 47 USC 227) was read through Cornell LII, which mirrors the Code; it is not govinfo.
Tags: `verified` = read on the live page this session. `inferred` = my reading of what the page implies. `unverified` = not read on a primary page, or a third-party or forum source.

**Walls and dead pages (not retried, no Patchright):**
- kit.com/pricing: 191 bytes, "Vercel Security Checkpoint" (`d3-kit-pricing.md`).
- Kit via the Fedora container: 37 bytes, authentication required.
- Kit help `/collections/2203265-kit-plans-and-pricing`: 404. The Kit Free-plan help article resolved it.
- CTIA Messaging Principles PDF: 4 bytes.
- Etsy `/legal/seller-policy/`: 4 bytes.
- Justia and ca11.uscourts.gov 11th Circuit opinion: 4 bytes each.
- laws.flrules.org ch. 2021-185 and ch. 2023-150: 4 bytes each. The flsenate.gov statute editions answered that question instead.
- Shopify `/promoting-marketing/shopify-email` help page: generic index with no pricing. The shopify.com Email page was used instead.

## TL;DR

1. **Send caps decide the tool, not contact caps.** A weekly drop is one full-list send per week, about 4 to 5 sends per subscriber per month.
   - Klaviyo and Mailchimp free cap sends at 500 per month, so the list is capped near 100 subscribers (500 ÷ 5; my arithmetic).
   - Brevo free caps sends at 300 per day, so a list over 300 cannot get the same-hour alert.
   - Beehiiv free and Kit free have unlimited sends (2,500 and 10,000 subscribers).
   - Shopify Email is free to 10,000 emails per month, about 2,000 subscribers at weekly cadence. `verified`.
2. **Kit Free is the "now" pick; Shopify Email is the "with Shopify" pick.**
   - Kit Free: 10,000 subscribers, unlimited broadcasts, forms and landing pages, tagging and segmentation, API access, per Kit's help page dated Sept 23, 2026.
   - Kit's catch: no visual automations or email sequences on Free, so the welcome email is a manual broadcast until she pays. `verified`.
3. **A hosted link or QR beats an embed.**
   - Kit landing pages "have their own shareable link", and Brevo forms share by "direct link, a QR code, or by embedding".
   - Klaviyo's embed form needs Klaviyo.js installed on the site.
   - Whether ChatGPT Sites accepts third-party scripts is `unverified`.
   - The Worker and D1 already exist, so a plain form posting to D1 is the zero-account fallback and the consent ledger.
4. **Email law is an opt-out regime.** CAN-SPAM needs no prior consent, but it does need:
   - an honest header and subject;
   - a valid postal address (a USPS PO box or a registered private mailbox counts);
   - a working opt-out, honored within 10 business days;
   - penalties up to $53,088 per email. `verified`
5. **Texts are the opposite regime.**
   - Marketing texts need prior express written consent: federally for autodialed telemarketing (47 CFR 64.1200(a)(2)), and in Florida for autodialed sales texts (Fla. Stat. 501.059(8)(a)).
   - Both carry $500 per violation, up to 3x if willful. `verified`
   - Recommendation: no SMS until a lawyer reads the consent wording.
6. **The Florida amendments, attributed by diffing the statute editions:**
   - Ch. 2021-185 added the written-consent definition and the $500 private right of action. It also changed the 501.616 calling window from 8 a.m.–9 p.m. to 8 a.m.–8 p.m. and added a cap of 3 calls per 24 hours.
   - Ch. 2023-150 narrowed the autodialer test, made a checked box count as a signature, and added a pre-suit "STOP" notice with a 15-day cure. `verified` (diff)
7. **The federal STOP rule changes on Nov 25, 2026.** FCC 26-67 (91 FR 67219, published Oct 26, 2026) makes a STOP to a marketing text revoke all marketing texts from that sender. It lets callers designate reply-STOP as the exclusive revocation method. `verified`
8. **No tool or statute I read covers "it's gone, here's its cousin."** Klaviyo's back-in-stock flow needs an inventory-aware platform, and one-of-ones never restock. Chairish and eBay saved searches are the model for wish-list matches. The "gone/cousin" email is a manual send in v1.

---

## 1. Tools

### 1.1 Klaviyo
- URLs: https://www.klaviyo.com/pricing, https://help.klaviyo.com/hc/en-us/articles/360006897412 (embed forms), https://help.klaviyo.com/hc/en-us/articles/360035056972 (SMS consent), https://help.klaviyo.com/hc/en-us/articles/11644128409371 (SMS disclosure), https://help.klaviyo.com/hc/en-us/articles/115003872251 (back in stock). Raw: `d3-klaviyo-pricing.md`, `-embed-form.md`, `-sms-consent.md`, `-sms-disclosure.md`, `-back-in-stock-flow.md`. Accessed 2026-10-29.
- Limits, verbatim:
  - "Up to 250 profiles / 500 emails/month / $5 of mobile messages/month". `verified`
  - FAQ: "limited to up to 250 active profiles ... and 500 email sends per month." `verified`
  - FAQ: free "allows you to ... build automations, segmentation and reports." `verified`
  - Over the cap: "your account will no longer be able to send additional emails or messages until the next billing cycle or until you upgrade." `verified`
  - Free-tier "Web forms" are listed. `verified`
  - The paid-tier price did not render in the crawl. `unverified`
- Form on a static site: "For embed forms to work, you'll need: Onsite tracking (Klaviyo.js) installed on your site ... The form's embed code placed where you want it to display." `verified`. Works only if the host lets her paste a script. No hosted-link form was found on that page. `unverified`
- Back in stock: the feature is for "Shopify, BigCommerce, Magento 2, PrestaShop, SFCC, or Shopware ... or ... an inventory-aware catalog synced via custom catalog feed or API." `verified`. It does not exist for a static site. Flow guidance: "Keep the flow between 1 to 3 messages." `verified`
- SMS rules (Klaviyo's own, which they flag as not legal advice):
  - "Someone must agree to receive SMS messages."
  - "SMS consent also must be collected separately from any other marketing channel."
  - "It's illegal to force someone to sign up for SMS in order to make a purchase."
  - "No. Having consent for email does not mean you have consent for SMS."
  - Disclosure checklist: service name, message frequency, "Text HELP for help. Text STOP ... to opt out", links to terms and privacy policy, "Message and data rates may apply", "Consent is not a condition of purchase", and the autodialer statement. `verified`
- Steal this: (a) the separate-checkbox rule for texts; (b) the disclosure checklist as the skeleton for the draft in section 6; (c) "1 to 3 messages" per flow.

### 1.2 Mailchimp
- URLs: https://mailchimp.com/pricing/marketing/, https://mailchimp.com/help/share-your-signup-form/. Raw: `d3-mailchimp-pricing.md`, `d3-mailchimp-share-form.md`. Accessed 2026-10-29.
- Free column (the compare table's last column):
  - "Limit of 250 contacts $0 /month".
  - "Monthly Email Sends ... Max of 500/mo or 250/day".
  - "Marketing Automation Flows ... Not included".
  - "Email Scheduling ... Not included".
  - "Remove Mailchimp Branding ... Not included".
  - "Sending will be paused if contact or email send limit is exceeded."
  - SMS: "Not included" on Free; an add-on on paid plans. `verified`
- Form: "The built-in sharing options send potential subscribers to the Basic subscribe form" (hosted); "Each signup form URL is randomly generated ... and can't be customized"; embeddable HTML for sites hosted elsewhere. `verified`
- Verdict: worst fit for a drop shop. No automation, no scheduling and a 500-send cap on Free. Hosted link works.
- Steal this: nothing structural. Skip it.

### 1.3 Brevo
- URLs: https://www.brevo.com/pricing/, https://help.brevo.com/hc/en-us/articles/208580669 (Free limits), https://help.brevo.com/hc/en-us/articles/208771869 (sign-up form). Raw: `d3-brevo-pricing.md`, `d3-brevo-free-limits.md`, `d3-brevo-signup-form.md`. Accessed 2026-10-29.
- Limits, verbatim:
  - "The Free plan includes 300 email sends per day."
  - "The Free plan allows you to store up to 100,000 contacts."
  - "if you send a campaign to more than 300 recipients, only 300 contacts will receive it on the scheduled day. To reach the remaining contacts, you need to manually resend."
  - "Emails sent from the Free plan always include the Sent with Brevo sticker."
  - "up to 2,000 unique contacts can enter your active automations."
  - Not on Free: A/B testing, landing pages, popups. `verified`
  - The Starter price did not render in the crawl. `unverified`
- Form: "You can now share your sign-up form through a direct link, a QR code, or by embedding it on your website." Double confirmation is "[Recommended]" and the form builder supports a CAPTCHA. `verified`
- Verdict: a hosted link and a QR code work, and the contact cap is generous. The 300-per-day cap kills the same-hour alert once the list passes 300.
- Steal this: the QR-code-for-the-box-card idea.

### 1.4 Kit
- URLs: https://help.kit.com/en/articles/16627071-the-kit-free-plan, https://help.kit.com/en/articles/2502632-the-difference-between-forms-and-landing-pages-faq. Raw: `d3-kit-free-plan-help.md`, `d3-kit-forms-landing.md`. Accessed 2026-10-29. The pricing page itself was walled.
- Free plan, verbatim (help article dated Sept 23, 2026):
  - "Kit's Free plan gives you up to 10,000 email subscribers, unlimited forms and landing pages, and unlimited email broadcasts at no cost."
  - Also included: "Audience tagging and segmentation", "A/B testing on your broadcasts", "API access".
  - Needs a paid plan: "Visual automations and the automation template library", "Email sequences", "Rules and RSS campaigns". `verified`
- Form: "A landing page is a standalone opt-in that works with or without a website. ... Each landing page has its own shareable link ... Kit hosts it for you." Forms, by contrast: "a form doesn't have a specific share link, since it lives on your site." `verified`
- Not verified this session: Creator and Pro prices. Only third-party blogs ($39 per month at 1,000 subscribers) surfaced, so `unverified`.
- Steal this: a hosted landing page link as the signup door, and tags as the wish-list ("hunting: lamp", "hunting: mirror").

### 1.5 Beehiiv
- URLs: https://www.beehiiv.com/pricing, https://www.beehiiv.com/support/article/12977090590487-creating-an-embedded-subscribe-form. Raw: `d3-beehiiv-pricing.md`, `d3-beehiiv-embed-form.md`. Accessed 2026-10-29.
- Free: "Unlimited email sends", "Landing pages"; "Subscribers, Free, Up to 2,500". Lite is "$49 /mo, Yearly billing", and Automations appear only from Lite up. "No. Every plan includes unlimited email sends." `verified`
- Form: "Embedded subscribe forms ... let you add a beehiiv newsletter signup to any external website you own", and "Embedded subscribe forms are for external sites only." A script embed. `verified`
- Verdict: fine sends, but a newsletter product. No free automation, and the list cap is 2,500. Kit beats it for this use.
- Steal this: nothing structural.

### 1.6 Shopify Email, Forms and SMS (the "with Shopify" stack)
- URLs: https://www.shopify.com/email, https://www.shopify.com/forms, https://help.shopify.com/en/manual/promoting-marketing/create-marketing/shopify-messaging/sms/pricing. Raw: `d3-shopify-email.md`, `d3-shopify-forms.md`, `d3-shopify-sms-pricing.md`. Accessed 2026-10-29.
- Email: "Every month, you can send up to 10,000 manual or automated emails for free. After that, only pay for what you use at $1 USD per 1,000 additional emails." `verified`
- Automations: "Choose from ready-to-use automations like welcome, winback, and upsell emails." `verified`
- Forms: "Shopify Forms, a free lead capture solution"; they "decide where and when each form shows up on your store"; a form can offer "early access to future sales or new product drops." `verified`. It is tied to a store: "Don't have a Shopify store? Get started with a 3-day free trial." `verified`
- SMS: US "$0.012 USD" per message; "A $2.15 USD monthly charge applies to each approved toll-free number used for SMS marketing in the United States and Canada." Also billed per message: subscriber confirmations, double opt-in messages, and replies to HELP or INFO. `verified`
- Steal this: "early access to ... new product drops" is Shopify's own wording for the drop-alert incentive.

### Same-day-send test (my arithmetic on verified caps, assuming one full-list send per week, 5 weeks in a bad month)

| Tool | Free ceiling for weekly drops |
|---|---|
| Klaviyo | 500 sends ÷ 5 = about 100 subscribers (also capped at 250 profiles) |
| Mailchimp | same 500/month, plus no automation flows |
| Brevo | 300/day, so same-hour delivery works only to a list of 300 or fewer |
| Beehiiv | unlimited sends to 2,500 subscribers; no free automations |
| Kit | unlimited broadcasts to 10,000 subscribers; no free automations |
| Shopify Email | 10,000 ÷ 5 = about 2,000 subscribers before any fee |

---

## 2. Comparators for the flows

- **Chairish "Follow This Search"** (https://support.chairish.com/hc/en-us/articles/44253725332753-My-Saved-Searches, raw `d3-chairish-saved-searches.md`). "We will notify you by email when a new item in your saved search becomes available or goes on sale. You can update your Email Settings to manage how frequently you receive saved search emails." `verified`. **Steal this:** the wish-list match is a saved search; give the subscriber a frequency control.
- **eBay saved searches** (https://www.ebay.com/help/buying/search-tips/saved-searches?id=4051, raw `d3-ebay-saved-searches.md`). "We'll send you email alerts when new items matching your search are listed." Unsubscribing from saved-search emails has its own help section. `verified`. **Steal this:** the match email is about the search the person defined, not the shop's schedule.
- **r/Emailmarketing, "back in stock ... then the item sells out ... let them know they missed out"** (https://www.reddit.com/r/Emailmarketing/comments/1o19g27/, raw `d3-reddit-back-in-stock-oneofkind.md`). The poster asks for "a way of letting people know they've missed out this time ... here are some similar products" and says Googling and "Klaviyo's AI support ... implied this isn't a thing marketers do." The archived capture shows no answer. `unverified` (one poster). **Steal this:** it names the "gone, here's its cousin" flow; nobody has a template for it, so Hollie writes her own.
- **Wild & Worn by Hannah, Facebook post, Oct 2** (https://www.facebook.com/61577196659952/posts/..., raw `d3-wildworn-fb-drop-email.md`). "want first dibs on new drops? join the wild & worn email list for early access and exclusive discounts, sent straight to your inbox." `verified` as a post, `unverified` as to how it performs. It is a shirt shop, not vintage home. **Steal this:** the pitch is "first dibs", not "newsletter". The shop's version drops the discounts ("Absolutely no offers").

---

## 3. Law (primary text)

### 3.1 CAN-SPAM: 16 CFR 316, 15 USC 7704, FTC guide
- URLs: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-316, https://www.law.cornell.edu/uscode/text/15/7704, https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business. Raw: `d3-ecfr-16cfr316.md`, `d3-usc-15-7704.md`, `d3-ftc-canspam-guide.md`. Accessed 2026-10-29.
- FTC list, verbatim:
  - "Don't use false or misleading header information."
  - "Don't use deceptive subject lines."
  - "Tell recipients where you're located. ... valid physical postal address."
  - "Honor opt-out requests promptly. ... You must honor a recipient's opt-out request within 10 business days."
  - The opt-out mechanism "must be able to process opt-out requests for at least 30 days after you send your message."
  - "Each separate email in violation of the CAN-SPAM Act is subject to penalties of up to $53,088." `verified`
- Postal address, 16 CFR 316.2(p): "the sender's current street address, a Post Office box the sender has accurately registered with the United States Postal Service, or a private mailbox the sender has accurately registered with a commercial mail receiving agency." `verified`
- Opt-out must be free and simple, 316.5: no sender may require that a recipient "pay any fee, provide any information other than the recipient's electronic mail address and opt-out preferences, or take any other steps except sending a reply electronic mail message or visiting a single Internet Web page." `verified`
- Ad label: 15 USC 7704(a)(5)(A)(i) requires "clear and conspicuous identification that the message is an advertisement or solicitation." The next paragraph says it "does not apply ... if the recipient has given prior affirmative consent to receipt of the message." `verified`. See the disagreement in section 4.
- Mixed messages: the FTC's Message A (account info first, short ad last) is most likely transactional; Message B (ad first) is commercial. 316.3 turns on whether transactional content appears "at the beginning of the body." `verified`. Practical rule: keep the care and shipping email promotion-free, and send "find me another" as a separate marketing email.
- **Steal this:** (a) the postal-address plus one-click-unsubscribe footer; (b) a separate marketing email for "find me another".

### 3.2 Gmail sender rules
- URL: https://support.google.com/a/answer/81126. Raw: `d3-google-sender-reqs.md`. Accessed 2026-10-29.
- "All senders: SPF or DKIM. Bulk senders: SPF, DKIM, and DMARC." Over 5,000 messages per day to Gmail adds one-click unsubscribe and a spam rate "below 0.30%". "Don't impersonate Gmail From: headers." `verified`
- Implication (`inferred`): she needs a sending domain she controls, not a gmail.com From address through an ESP. She is far below 5,000 per day, but SPF/DKIM still apply.

### 3.3 Federal text rules: 47 USC 227 and 47 CFR 64.1200
- URLs: https://www.law.cornell.edu/uscode/text/47/227, https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200 (eCFR "up to date as of 10/27/2026"), https://www.federalregister.gov/citation/91-FR-67219, https://docs.fcc.gov/public/attachments/DA-26-12A1.txt. Raw: `d3-usc-47-227.md`, `d3-ecfr-47cfr64-1200.md`, `d3-fedreg-91fr67219.md`, `d3-fcc-da-26-12-text.md`, `d3-fcc-revocation-delay.md`. Accessed 2026-10-29.
- Consent for marketing texts, 64.1200(a)(2): no autodialed or prerecorded call that "includes or introduces an advertisement or constitutes telemarketing" to a cell number "other than a call made with the prior express written consent of the called party." (f)(9) defines it as "an agreement, in writing, bearing the signature of the person called" with a disclosure that (A) the person authorizes autodialed telemarketing and (B) "is not required to sign ... as a condition of purchasing any property, goods, or services." A "signature" includes an electronic one recognized under federal law. (e) applies the telephone-solicitation rules to "text messages to wireless telephone numbers" per FCC 03-153. `verified`
- Remedy, 47 USC 227(b)(3): "$500 in damages for each such violation, whichever is greater," trebled if "willfully or knowingly." `verified`
- Hours, 64.1200(c)(1): no telephone solicitation to a residential subscriber "before the hour of 8 a.m. or after 9 p.m. (local time at the called party's location)." But (f)(15) says a "telephone solicitation" does not include a message "to any person with that person's prior express invitation or permission", or to someone with an established business relationship (a purchase within 18 months or an inquiry within 3 months). `verified`. So these hours technically attach to unsolicited texts, and I recommend following them anyway.
- Revocation, current eCFR text, (a)(10): words "stop," "quit," "end," "revoke," "opt out," "cancel," or "unsubscribe" are a per se valid revocation, honored "not to exceed ten business days"; callers "may not designate an exclusive means." (a)(12): one confirmation text is allowed if sent within five minutes and contains no marketing. `verified`
- **New rule, FCC 26-67, 91 FR 67219, published Oct 26, 2026, "Effective November 25, 2026."** Text, verbatim:
  - "Callers may designate any of the following methods as the exclusive means to revoke consent: ... replying to an incoming text message with any one of the following standardized words."
  - "Text senders that designate a reply text message as the exclusive means ... can satisfy the disclosure obligation by including at least one of the standardized words ... in each text message."
  - "Revocation requests made in response to calls or text messages that contain an advertisement or constitute telemarketing revoke consent to all future calls or text messages containing an advertisement or constitute telemarketing from that caller."
  - Ten business days stays. `verified`
- The prior waiver, DA 26-12 (Jan 6, 2026), delayed (a)(10) only "to the extent the rule requires callers to treat a request to revoke consent made ... in response to one type of informational message as applicable to all future robocalls and robotexts ... on unrelated matters" until Jan 31, 2027. FCC 26-67 supersedes that delay on Nov 25, 2026. `verified`. For one marketing program it makes no practical difference: STOP ends every marketing text.
- One-to-one consent rule: Wiley's alert says the 11th Circuit vacated it on Jan 24, 2025 (*Insurance Marketing Coalition v. FCC*). `verified` as a law-firm report; the opinion itself was walled, so `unverified` as primary text. Mostly a lead-generator rule, marginal here.
- **Steal this:** (a) put "Reply STOP to opt out" in every marketing text, which also satisfies the new designated-method disclosure; (b) send one confirmation text only, within five minutes, no marketing.

### 3.4 Florida: Fla. Stat. 501.059, and 501.616
- URLs: https://www.flsenate.gov/Laws/Statutes/2020/501.059, `/2022/501.059`, `/2023/501.059`, `/2026/501.059`, and `/2020/501.616`, `/2025/501.616`, `/2026/501.616`, plus `/2025/501.603` and `/2025/501.604`. Raw: `d3-fl-501-059-2020.md`, `d3-fl-501-059-2022.md`, `d3-fl-501-059.md` (the 2023 edition), `d3-fl-501-059-2026.md`, `d3-fl-501-616-2020.md`, `d3-fl-501-616.md`, `d3-fl-501-616-2026.md`, `d3-fl-501-603.md`, `d3-fl-501-604.md`. Accessed 2026-10-29. The 2023 and 2026 editions differ only in "fees"/"fee" wording; history ends at ch. 2023-150 in both.
- A "telephonic sales call" is "a telephone call, text message, or voicemail transmission ... for the purpose of soliciting a sale of any consumer goods or services." An "unsolicited telephonic sales call" excludes calls "In response to an express request of the person called" and calls "To a person with whom the telephone solicitor has a prior or existing business relationship." `verified`
- **What ch. 2021-185 changed (diff of the 2020 edition against the 2022 edition):** `verified`
  - Added "Prior express written consent" (defined as a signed written agreement with a "clear and conspicuous disclosure" that it is not a condition of purchase), "Called party" and "Signature."
  - Turned (8)(a) from a flat ban on automated calls into a ban "without the prior express written consent of the called party." The 2020 exceptions for calls about goods "previously ordered or purchased" disappeared from the text.
  - Added the private right of action: "Recover actual damages or $500, whichever is greater," up to three times for a willful or knowing violation.
  - Amended 501.616(6) (its history note cites s. 2, ch. 2021-185): the 2020 text barred calls "before 8 a.m. or after 9 p.m."; the current text bars "before 8 a.m. or after 8 p.m. local time in the called person's time zone" and "More than three ... calls from any number to a person over a 24-hour period on the same subject matter."
- **What ch. 2023-150 changed (diff of the 2022 edition against the 2023 edition):** `verified`
  - "selection or dialing" became "selection and dialing" in the autodialer language, in (1)(g) and (8)(a).
  - (8)(a) now reaches only an "unsolicited" telephonic sales call.
  - "Signature" now includes "An act that demonstrates express consent, including, but not limited to, checking a box indicating consent or responding affirmatively to receiving text messages."
  - New (10)(c): "Before the commencement of any action for damages ... for text message solicitations, the called party must notify the telephone solicitor ... by replying 'STOP'. Within 15 days after receipt of such notice, the telephone solicitor shall cease sending text message solicitations." It is a pre-suit condition, not a replacement for the federal ten-business-day rule.
  - The note under the history says the 2023 amendments "apply to any suit filed on or after the effective date."
- Scope caveat for 501.616: it binds a "commercial telephone seller", whose definition excludes people exempted by 501.604. Exemption (21) covers prior customers "if the solicitor is operating under the same exact business name." Exemption (22) covers a business that has operated a retail establishment for at least a year and does most of its business there. Holliewood & Vine has no public showroom, so (22) likely fails. `inferred`. The statute speaks of "phone calls", and I cannot tell from the text whether texts to consenting subscribers are covered. Lawyer question.
- **Steal this:** (a) a web checkbox is a Florida "signature", so a checkbox plus a stored wording version is a defensible consent record; (b) honor STOP at once and keep the confirmation text out of the 15-day argument; (c) schedule texts inside 8 a.m.–8 p.m. recipient time. My arithmetic: texting only between 11:00 a.m. and 8:00 p.m. Eastern keeps you inside 8-to-8 in every lower-48 time zone (`inferred`).

---

## 4. Where sources disagree

- **Ad label under CAN-SPAM.** The FTC summary says "you must disclose clearly and conspicuously that your message is an advertisement." The statute (7704(a)(5)(B)) lifts that duty for recipients who gave prior affirmative consent. Both `verified`. **Treat as: statute verified, FTC summary incomplete.** Keep a light label anyway until a consent ledger exists.
- **Is adding Etsy buyers to a list illegal?** One r/Etsy commenter says CAN-SPAM requires opt-in. Another replies that "CAN-SPAM compliance does not require specific opt-in consent" and that adding without consent is "against the terms of most ESPs." The statute I read is opt-out. The Etsy policy page was walled, so Etsy's own rule is `unverified`. **Treat as: law verified opt-out; Etsy and ESP terms need review.** Safe plan: invite buyers through a box-card QR, never auto-add them.
- **Quiet hours.** Federal: 8 a.m.–9 p.m. (64.1200(c)(1)), for unsolicited telephone solicitations. Florida 501.616(6)(a): 8 a.m.–8 p.m., for "commercial telephone sellers." **Federal verified, Florida verified, whether Florida's reaches texts to consenting subscribers needs review.** Follow the stricter one.
- **Brevo automations on Free.** The help center says Free allows automations with a 2,000-contact entry cap. The pricing page lists "Marketing automation" under Standard. **Free-plan limit verified, whether Free's automation is a reduced version needs review.**
- **Kit free-tier size.** Kit's help page says 10,000 subscribers. A third-party search summary said one older pricing calculator still shows 1,000. **10,000 verified on Kit's own page (Sept 23, 2026); Kit's paid prices need review (pricing page walled).**
- **FCC revocation timing.** The Jan 2026 waiver delayed only the "revoke all" scope to Jan 31, 2027. The Oct 26, 2026 final rule supersedes it on Nov 25, 2026. **Both verified; the later rule governs from Nov 25.** The eCFR page I captured is dated 10/27/2026 and still shows the pre-amendment text.

---

## 5. Recommendation for Holliewood & Vine

### 5.1 What to do now (no accounts needed)
1. **Make D1 the consent ledger.** Add a `/api/subscribe` route in the existing Worker (the shop already has `/api/hire` and D1). Store: email, optional hunt tags, the wording-version id the person saw, timestamp, source page, and source type (site or box card). Export a CSV into whatever tool goes live. This is new drafting for the site's builder; I did not touch `site/`.
2. **Do not collect phone numbers yet.** Texts wait for the lawyer review in 5.2.
3. **Lock the drop clock.** Pick a drop time where the one-hour-early email lands at a sane hour. For a later SMS alert, 11 a.m. alert and noon public drop sit inside every window.
4. **Write the footer, the signup microcopy and the five flows (section 6).** The footer needs: the shop's legal name, a postal address, and an unsubscribe link.
5. **Treat Etsy and Shopify buyers as strangers to the list.** Invite them with a box card (a QR to the hosted signup page) rather than adding them.
6. **Tool plan, decided on three checks: (a) a same-day send to the whole list, (b) a hosted-link form, (c) a welcome email at no cost.** Kit passes (a) and (b); (c) fails, but her first list will be small enough to send the welcome as a one-off broadcast. Klaviyo and Mailchimp pass (b) or (c) but fail (a) beyond about 100 subscribers. Brevo fails (a) beyond 300.

### 5.2 What needs an account, a fee or a lawyer
- **Account, free:** Kit Free. Use a landing page as the signup door and tags for hunts. Kit's API access is on Free, so a later Worker job can push D1 rows into Kit.
- **Fee:** a domain she controls with SPF and DKIM set up (Gmail rules, 3.2). Price not researched.
- **Fee:** a USPS PO box or commercial mail receiving agency mailbox, so the unsubscribe-footer address is not her home (316.2(p)). Price not researched.
- **Fee, later:** Kit Creator or Pro if she wants automations before Shopify (price `unverified`).
- **With Shopify (later):**
  - Use Shopify Email, Forms and the welcome-email automation. They are free to 10,000 emails per month (about 2,000 subscribers at weekly cadence).
  - Add SMS through Shopify Messaging at $0.012 per US message plus $2.15 per month for the toll-free number, and only after the lawyer step.
  - Keep Klaviyo as the escalation path if wish-list matching needs real event logic. Its back-in-stock flow works only with an inventory-aware platform, and one-of-ones never restock, so do not buy Klaviyo for that.
  - Import the Kit list into Shopify with its consent record from D1. Whether Shopify's import accepts consent fields is `unverified`.
- **Lawyer:**
  - The SMS consent wording in section 6.
  - Whether 501.616 reaches texts to consenting subscribers.
  - Whether platform-sent texts count as an "automated system for the selection and dialing of telephone numbers."
  - Whether a past buyer counts as having a "prior or existing business relationship" for 501.059.
  - Whether to keep the CAN-SPAM ad label.
  - Etsy's rule on using buyer contact information (policy page walled).

---

## 6. The flows in Hollie's voice

Placeholders in {braces}; no invented items, prices or customers. No discounts. No promised gift. "Design" wording is avoided per the decided ch. 481 rule. All five are new drafting. The brief names three flows but lists five, so all five are written.

**Footer on every marketing email (new drafting):**
"Holliewood & Vine, {postal address}. You're here because you signed up at {url} on {date}. One of one, always. Unsubscribe in one click, no hard feelings: {unsubscribe_link}."

**Signup microcopy (new drafting):** "Get the door an hour early. One email a week. Leave any time."

**1. Welcome** (trigger: signup)
Subject: You're on the list. Naturally.
- Hollie here. Collector of good things. Excellent taste. Absolutely no offers.
- Everything I sell is one of one, so when it's gone, it's gone. On drop day ({drop_day}) you get the door an hour early, at {early_time}.
- Tell me what you're hunting by replying, and I'll write when something fits. Not for you? The unsubscribe link is below, and I'll take it with grace.

**2. Drop alert** (trigger: weekly, one hour before public open, to the list)
Subject: The door opens at {public_time}. You're in at {early_time}.
- {count} new pieces, every one of them one of one. First look: {lead_piece}.
- The public walks in at {public_time}. You're already inside.
- Once it's gone, it's gone: {shop_link}.

**3. Wish-list match** (trigger: a new piece matches a saved hunt)
Subject: I found your {wish_word}.
- You told me you were hunting {wish_text}. {piece} just came in, and it's {matching_trait}.
- It's one of one, so you hear it from me first: {piece_link}.
- Close but not right? Reply and tell me what's off. I'll keep looking.

**4. It's gone, here's its cousin** (trigger: a piece sells; send manually in v1 to people who saved, viewed or hunted it)
Subject: {piece} found a home. Here's its cousin.
- Someone with excellent taste got {piece} first. It happens to the best ones.
- Here's a relative: {cousin_piece}, same {shared_trait}, different story: {cousin_link}.
- Want the next one before it's listed? Reply with what you loved about {piece}.

**5a. After purchase, care** (the order-update email; keep promotion out so it stays transactional)
Subject: {piece} is on its way. Care notes inside.
- {piece} ships {ship_date}. Tracking: {tracking_link}.
- Care for this piece: {care_line_from_condition_card}.
- Sometimes a little something shiny rides along in the box. No promises.

**5b. After purchase, find me another** (marketing; send 7 to 10 days after delivery, only to buyers who opted in through the box card or the signup page)
Subject: Now that it's home: want me to find another?
- {piece} should be settling in. Reply and tell me how it's looking.
- Missing something? Tell me what the room still needs and I'll hunt for it: one piece, one corner, one very specific lamp.
- Want the early-hour list too? {signup_link}

**SMS drop alert (later, after legal review; new drafting):**
"Holliewood & Vine: you're in an hour early. New pieces: {short_link} Msg&data rates may apply. Reply STOP to opt out."

**SMS consent checkbox (later; separate from email, unchecked, phone field labeled optional; new drafting for lawyer review):**
"[ ] Text me the hour-early alert. I agree to receive recurring automated marketing text messages (new-piece alerts and wish-list matches) from Holliewood & Vine at the mobile number I entered. Consent is not a condition of any purchase. Message frequency varies, up to {N} per week. Message and data rates may apply. Reply STOP to cancel, HELP for help. Terms: {link}. Privacy: {link}."
Built from Klaviyo's disclosure checklist (1.1), 64.1200(f)(9)(i)(A)/(B) and Fla. Stat. 501.059(1)(g)4.a/b.

---

## 7. Ideas for Hollie

1. Sell the list as "first dibs", not a newsletter: "The door opens an hour early for the list." (Wild & Worn post; Kit unlimited broadcasts)
2. Make the signup a hunt form ("what are you after?") so every address arrives with a tag that powers the wish-list match. (Chairish saved searches; Kit tagging)
3. Print a QR card for the box that goes to the hosted signup page, so buyers opt in instead of being added. (Brevo QR code; Reddit Etsy thread)
4. Send "found a home, here's its cousin" by hand for every sale, and link the sold archive. (r/Emailmarketing capture; sold archive already decided)
5. Let people set how often wish-list matches arrive, the way Chairish does. (Chairish email settings)
6. Keep texts for one job only: the hour-early alert, with its own checkbox. (Klaviyo SMS consent; Shopify SMS pricing)
7. Choose the drop hour backward from the legal window: an 11 a.m. alert and a noon drop. (47 CFR 64.1200(c)(1); Fla. Stat. 501.616(6)(a))
8. Write the unsubscribe line in her voice, and make it work in one click: "Leaving? The door stays open." (16 CFR 316.5; FTC guide)
9. Store the exact consent wording version beside every signup, so any complaint has a one-row answer. (Fla. Stat. 501.059(1)(h)2; 64.1200(f)(9))
10. Put the care line on the condition card and pull it into the order email, so the care message needs no extra writing. (CAN-SPAM transactional rule; her condition-grade idea)
