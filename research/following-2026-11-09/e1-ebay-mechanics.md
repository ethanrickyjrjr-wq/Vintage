<!-- Saved verbatim by the parent Opus session from Sonnet lane e1's final message, 2026-11-09 (the harness refuses subagent report writes). -->

# e1: eBay's own mechanics for followers and repeat buyers (verified on eBay pages, 2026-11-09)

Raw crawls are saved in `research/following-2026-11-09/raw/e1-*.md`. Tags: **verified** means read live this session with the URL given. **search snippet** means unverified. **inferred** means my reading, not eBay's text.

## 1. TL;DR

- **The follow mechanic is called "Save" and it is one-way.** The button on our public profile reads "Save" (verified, https://www.ebay.com/usr/holliewoodandvinellc). A saver sees our listings in their feed (verified, https://pages.ebay.com/make-the-most-of-ebay/). I found no page saying the saved seller is notified, and sellers can't see who follows them (community consensus, search snippet). So following other sellers does nothing for us. Nothing reciprocal exists except Live "Raids" (see section 3d).
- **Every audience-marketing tool needs a Store.** Newsletters, coded coupons, Discounts Manager (sale events, volume, order and shipping discounts), buyer groups and rule-based auto offers all say "Store subscribers". I found no Starter carve-out on any US page, but also no page that says Starter has everything. Write it as "verified for Store subscribers; no US tier carve-out found; confirm in the account before buying Starter." Third-party sources conflict.
- **Free-tier levers that work today:**
  - Sending offers to watchers and cart-holders (manual, bulk or per-listing auto, valid 96 hours).
  - Best Offer.
  - The free profile About field (1,000 characters, empty now). `profile-bio.txt` can go live today.
  - The "Follower" tag on buyers in Seller Hub orders.
  - The Share button.
- **The 2 feedback ratings are eBay automated feedback, not buyer-written.** The profile reads "eBay automated feedback... Order delivered on time with no issues". Automated feedback exists only for tracked, on-time orders with no issue (verified, https://www.ebay.com/sellercenter/news/2025-august/seller-protection). Tracking on every order is the cheapest way to grow the score. The account was created Sep 8, 2026 and passes the 90-day rule on about Dec 7. Top Rated also needs 100 transactions and $1,000 in US sales over 12 months, so it is a long way off.
- **Promoted Listings (General) is likely a bad fit for one-of-a-kind vintage right now.** Eligibility is "Above Standard or Top Rated sellers with enough account activity" (verified). That is undefined for a 2-sale account. The fee triggers if ANY buyer clicked the ad in the prior 30 days, a click includes "add to watchlist", and it applies to accepted Best Offers too. External placements are on by default.
- **Kit audit: no file breaks a stated eBay rule.** Cautions:
  - Keep the disco-ball gift and the feedback request apart (section 5).
  - Reply 11 says "privately" about the pickup address. Change it to "in eBay Messages after the buyer has paid".
  - The footer says "Follow" while the button says "Save". This is cosmetic.
- **Red lines.** No Instagram handle, URL, email or phone anywhere eBay shows: listings, listing images, profile, Store, messages, feedback. No off-eBay discount on a package insert. A coded coupon printed on the insert is the eBay-sanctioned route, but it needs a Store.
- **Live is reachable but gated.** It needs a business account plus Business Policies and approval, and may waitlist. No giveaways, no off-eBay pointers. Live sales are excluded from seller level from Oct 15, 2026.

## 2. Feature matrix

"No gate stated" means the eBay page names no Store requirement.

| Feature | Free | Starter | Basic | What it does for followers and repeat buyers | Source |
|---|---|---|---|---|---|
| Save seller button, Saved sellers list, feed | Yes | Yes | Yes | Saver sees our new items in their feed. Per-listing email or push alerts are not verified. | make-the-most-of-ebay; /help/account/using-ebay/using-ebay?id=5185 |
| Profile "About" (1,000 characters) | Yes | Yes | Yes | Free-account bio. Placeholder reads "Give people more reasons to follow you! 1/1000". | Our public profile |
| Store logo, billboard, Store About, categories, inventory strips | No | Yes | Yes | Branding. Store logo shows on listing pages. | /help/selling/ebay-stores/manage-ebay-store?id=4090 |
| Store newsletter | No | Yes (no carve-out found) | Yes | Email to recent buyers, 31-365 day buyers, "your followers (saved you as a seller)", or all subscribers. | /help/selling/selling-tools/email-marketing-sellers?id=4654 |
| Coded coupons, sale events, volume, order and shipping discounts | No | Yes (no carve-out found) | Yes | Repeat-purchase tools. Coded coupons can be printed in the package or posted publicly. | /sellercenter/growth/seller-hub-promotions; /help/selling/selling-tools/discounts-manager?id=4094 |
| Buyer groups, rule-based automatic offers | No | Yes (no carve-out found) | Yes | Target past buyers or followers. Max one coupon per buyer per 14 days. | /sellercenter/growth/seller-hub-promotions/buyer-groups/ |
| Send offers to watchers or cart (manual, bulk, per-listing auto) | Yes (no gate stated) | Yes | Yes | Converts interest. 30 most recent interested buyers. Offer must be at least 5% off. Cart item must be there at least 2 days. | /help/selling/listings/adding-best-offer-listing-using-reply-offer?id=4144 |
| "Send offer" in reply to a buyer's question | Yes | Yes | Yes | Up to 3 offers, 96 hours. | same page |
| Seller Hub buyer details ("Follower", "Repeat buyer" tags) | Yes (no gate stated) | Yes | Yes | Shows which buyers also follow. | /sellercenter/resources/seller-updates/2025-january/buyer-details |
| Promoted Listings General (cost per sale) | No Store gate; level gate | same | same | Ads. Needs Above Standard or Top Rated "with enough account activity". | /help/selling/listings/promoted-listings-overview/promoted-listings-standard?id=4164 |
| Promoted Listings Priority (cost per click) | No Store gate; level gate | same | same | $3 minimum daily budget. Same level gate. | /help/selling/ebay-advertising/promoted-listings/priority-campaign-strategy?id=5299 |
| Promoted Offsite (Google etc.) | No Store gate stated | same | same | Fixed price only. Pay per click, monthly cap. | /help/selling/ebay-advertising/promoted-offsite?id=5471 |
| eBay Live | No Store gate stated | same | same | Business account plus Business Policies, approval or waitlist. | /ebaylive/seller |
| eBay Partner Network (affiliate) | Yes | Yes | Yes | Links only OFF eBay. | /sellercenter/growth/ebay-partner-network |

## 3. Findings by question

### 3a. Following (verified unless tagged)

- **Label.** The profile shows "Save", the listing page shows "Save this seller", and My eBay lists "Saved Sellers". eBay's text: "Simply click the Save this seller link from an item or store page... you'll start seeing what they're selling in your feed" (https://pages.ebay.com/make-the-most-of-ebay/).
- **Where the saver finds us.** Under Saved Sellers (https://www.ebay.com/help/account/using-ebay/using-ebay?id=5185).
- **Notifications.**
  - Email or push alerts for new listings from a saved seller: not verified. The same page ties alerts to saved searches.
  - Saved sellers are alerted when a seller goes live. The eBay Live FAQ says "Followed Sellers – Notifies you when a seller you saved goes live" (https://pages.ebay.com/ebaylive-faq).
- **Follower count on the profile.** None on our public profile crawl. Community posts say sellers can see a count but not names (search snippet, https://community.ebay.com/t5/Selling/How-to-view-my-followers/m-p/34284992). Whether a count is shown publicly stays a gap.
- **Names.** Sellers cannot see a follower list. "You can see if a buyer that purchases from you is a follower" is confirmed by the Jan 2025 Seller Center update: "visible Follower and Repeat buyer tags".
- **Newsletter link.** "When customers save you as their favorite Store, they can subscribe to your newsletter" (https://www.ebay.com/sellercenter/selling/how-to-sell/set-up-your-store). Saves collected now should become the newsletter audience after an upgrade (inferred from the audience option "Your followers (saved you as a seller)").
- **Following others.** Verified that it only adds to our own feed and list. No page says it notifies them or earns anything (inferred: not reciprocal). Using extra accounts to follow or inflate would hit the multiple-accounts and feedback rules (https://www.ebay.com/help/policies/feedback-policies/feedback-manipulation-policy?id=4231, "Registering multiple accounts or working with others to exchange feedback...").

### 3b. Marketing to followers

- **Store newsletters exist in 2026 and need a Store** (verified, https://www.ebay.com/help/selling/selling-tools/email-marketing-sellers?id=4654).
  - Six templates.
  - Promotional ones need an active discount: "an active discount (coupon, volume pricing, or sale event) is needed".
  - A buyer gets at most one email from us per 14 days.
  - Can't include: "Offers to sell items outside of eBay; Phone numbers or email addresses; Links or image references to items not located on an eBay site; HTML tags, JavaScript or other active scripting."
- **Coded coupons** (Store; https://www.ebay.com/sellercenter/growth/seller-hub-promotions/coded-coupons/).
  - Can go "Publicly on eBay" or "Privately off eBay".
  - Verbatim: "Send a printed coupon code note in your orders to encourage repeat purchases."
  - Coupons can be shared "on social media". Off-eBay sharing must show the terms and link the Buyer Terms.
  - Buyer groups also send coupons by email and app notification. One coupon per buyer per 14 days.
- **Naming drift.** The Seller Center calls the tools "Seller Hub Discounts" ("Free for Store subscribers"). The help page still says "Discounts Manager". "Promotions Manager" is the older name.
- **Free tier: send offers to interested buyers.**
  - Verbatim: "If a buyer shows interest in your item (watching your item or adding it to their cart, for example), you can send them special offers individually or in bulk."
  - Limits: at least 5% below Buy It Now, 30 most recent interested buyers, 96-hour validity, cart items need at least 2 days.
  - Per-listing automated offers need no Store. Rule-based automatic offers via Buyer Groups are "Store subscribers" only.
  - If a General Promoted Listings ad was clicked, an accepted offer still pays the ad fee.
- **Starter vs Basic.** The only US differences I found are fees and listing allowances:
  - Starter: 250 zero-insertion-fee listings, then $0.30 each; "Most categories" final value fee 13.6% up to $7,500 (https://www.ebay.com/help/selling/fees-credits-invoices/store-selling-fees?id=4809).
  - Prices re-verified: Starter $7.95/$4.95, Basic $27.95/$21.95 (https://www.ebay.com/sellercenter/selling/how-to-sell/set-up-your-store).
  - No page lists marketing-tool differences by tier. A third-party search found "some benefits are not available with Starter" without naming them (search snippet).

### 3c. Promoted Listings

Terms verified at /help/selling/listings/promoted-listings-overview/promoted-listings-standard?id=4164 and /help/selling/ebay-advertising/promoted-listings-overview?id=5295. eBay now calls the types General and Priority.

- **General.**
  - Ad rate 2% to 100% of the total sale amount (item, shipping, tax and fees).
  - Verbatim: "General fees are charged when a buyer purchases the promoted item from a general ad that any buyer clicked on in the most recent 30 days."
  - A click includes "add to watchlist, add to cart, quick view".
  - Dynamic or fixed rate, with an optional cap. App "Easy boost" promotes everything at one rate.
  - "By default, all listings in general campaigns are eligible to appear in external sponsored placements." Opting out takes a form and 7 days.
  - A sale after a click is still charged, even if the buyer arrived organically.
- **Priority.** Pay per click, second-price auction, "There is a $3 minimum" target daily budget, monthly spend at most 30.4 times the daily budget. Not for auctions or the "Everything Else" category. A click is charged even with no sale.
- **Offsite.** Fixed price only. Pay per click. Monthly cap is 30.4 times the daily budget, and a day can spend up to 2x. No rate table. Seller-level gate not stated on the page.
- **Eligibility for us.** "Above Standard or Top Rated sellers with enough account activity can promote fixed price listings for most categories." "Enough" is undefined. This is not verifiable without opening the Advertising tab.
- **Suggested rates for vintage clothing or home decor.** eBay publishes none (https://www.ebay.com/help/selling/ebay-advertising/promoted-listings/suggested-ad-rates?id=5839). The rate is computed per listing, daily, from competition, price, listing quality and past performance. Third-party "2% to 5%" starting points are rules of thumb, not eBay figures.
- **Fit.** Inferred: because a single watch-click triggers the fee for 30 days, General is a poor match for unique items that mostly sell by Best Offer. Test only with fixed-price pieces after the account has sales history.

### 3d. eBay Live

- **Eligibility, verbatim.** "eBay Live is available to eligible professional sellers, including registered businesses and sole proprietors. To sell on eBay Live, you'll need an eBay business account and Business Policies for shipping, returns, and payments... If you don't currently meet eligibility requirements, you may be placed on the waitlist." (https://www.ebay.com/ebaylive/seller)
- **How to apply.** New sellers apply on that page. Existing sellers with Business Policies "can automatically receive access... through the Live Studio link in Seller Hub" (https://www.ebay.com/help/selling/ebay-live/livestream-selling-ebay-live?id=5762).
- **Categories.** Fashion, apparel, handbags, home and garden and more are named as supported or featured. "Category availability may vary by market seller eligibility requirements."
- **Fees.** 6% commission capped at $100, plus 2.9% + $0.30 processing, no insertion fee. A promotion through Dec 31, 2026 puts a $0.10 per order fee on items of $10 or less (https://www.ebay.com/ebaylive/seller-pricing).
- **Followers inside Live.** The bell gives a push when the event starts. The heart "follow[s] your eBay store and receive[s] alerts for all of your eBay Live events" (help guide above). Buyers get "Followed Sellers" notifications (FAQ).
- **Raids.** The guide says "Raids can help support your fellow trusted sellers... and introduce your audience to new sellers". This is the one verified cross-seller audience mechanism, and it is relevant to e2.
- **Stale source.** The old FAQ still says "currently in beta with select sellers". Newer pages contradict it (X verified, Y need review). Treat the FAQ as stale.
- **Rules.**
  - Seller levels: "As of October 15, 2026, eBay Live transactions are no longer counted in your seller standards or service metrics calculations" (https://www.ebay.com/help/policies/selling-policies/seller-standards-policy?id=4347).
  - Giveaways: "Sellers may not conduct promotions, giveaways, competitions, or similar activities unless explicitly approved by eBay in advance" (https://www.ebay.com/help/policies/member-behavior-policies/ebay-live-policy?id=5478). Disco-ball gifts are therefore off the table on air without pre-approval.
  - Spam: "Directing users to external websites or off-platform channels" counts as spam.
  - Feedback: using Live for incentivized feedback is banned.
- **Unknown.** Whether our account is a business account.

### 3e. Selling limits, seller levels, feedback

- **Limits** (https://www.ebay.com/help/selling/listings/selling-limits?id=4107).
  - Verbatim: "We'll review your account every month and adjust the limits automatically based on your sales volume and the feedback you've received from buyers. Remember, your active and sold listings count toward your monthly limit."
  - Our numbers are in Seller Hub, Overview, "Monthly limits". The help page publishes none. A common third-party figure for new sellers is about 10 items and $500 a month (search snippet, unverified). With 7 live and about 45 prepared, check this before batching.
  - Listings above the limit may be ended.
  - Increases: request via the message or button, or link an older account. New-category limits are lifted automatically after a good record.
  - "A Store doesn't raise limits" comes only from the India export page (search snippet, not verified for the US).
- **Levels** (https://www.ebay.com/help/policies/selling-policies/seller-standards-policy?id=4347). Evaluated on the 20th of each month. With fewer than 400 transactions in 3 months, it counts 12 months.
  - Below Standard needs more than 2 cases closed without resolution, or defects above 2% tied to more than 4 different buyers. A tiny account is mostly protected.
  - Below Standard blocks Promoted Listings and lowers search placement and limits.
  - Top Rated (all must hold):
    - Account active at least 90 days.
    - At least 100 transactions and $1,000 in US sales over 12 months.
    - Defects at most 0.5% across no more than 3 buyers.
    - Late shipments at most 5 (or 3%).
    - At least 95% of orders with validated tracking.
  - Top Rated Plus needs same or next-day handling and 30-day free returns. Our approved policy does not qualify.
- **Feedback.** The 2026-11-09 profile shows 2 positive, both automated. Automated feedback began Sept 3, 2025: "If a buyer decides to leave feedback, we'll replace our automated message with their message. If the buyer returns the item or reports an issue, we'll remove our automated feedback."

### 3f. Off-eBay sharing tools

- **Share button.** Present on our profile (verified). Targets not enumerated in the US pages I could read.
- **Social sharing FVF credit.** https://pages.ebay.com/social/sharing/terms.html exists but looks legacy: it mentions PayPal fees and the quick listing tool, and has no date. Currency unverified, so don't build a tactic on it.
- **EPN.** Verified: "up to 4% of the item sale price". Verbatim: "eBay Partner Network links can only be posted outside of eBay, never on eBay property. This means that partners who are eBay sellers can't include affiliate links within their eBay listings, eBay store or eBay Messages." The Seller Center page I crawled shows no 100% credit text. The Value Added Resource report (https://www.valueaddedresource.net/ebay-kills-epn-affiliate-fvf-seller-incentive/) says the US seller incentive was removed effective Aug 1, 2025 (X verified, Y need review: no eBay announcement found). Own-listing links still work for tracking (/help/selling/selling/ebay-partner-network?id=4662).
- **Collections.** Our public profile shows only Shop, About and Feedback. The My eBay menu has "My Collection" (collectors' hub). A Jan 2026 community snippet suggests profile Collections still exist, with a display cap. Unresolved.
- **Store naming.** "We don't allow store names to be a web address or include (for example) '.com'" (links policy).

## 4. Policy red lines (verbatim, with URLs)

**Links.** https://www.ebay.com/help/policies/listing-policies/links-policy?id=4248
- "listings or item descriptions can't contain links that direct customers to any other site."
- "Links in a description are only allowed for the following: Other eBay pages (eBay Messages, other eBay items, Stores pages, Follow Seller or Add to my Favorite Sellers)... Links that we allow must use secure HTTPS."

**Contact information.** https://www.ebay.com/help/policies/member-behavior-policies/contact-information-sharing-policy?id=4373
- Banned: "Social media ID", "External website addresses (URLs)", name, address, phone, email.
- Public areas named: "Listings, Images in a listing, eBay Live..., Profile pages, Storefront pages... Feedback content, Ask a question."

**Offsite sales.** https://www.ebay.com/help/policies/payment-policies/offering-buy-sell-outside-ebay-policy?id=4272
- "Share or request direct contact information prior to completing a sale. This includes: Name, Addresses, Phone number, Email address, Social media ID...".
- "In any communications with another eBay member, refer to or promote external websites that facilitate sales outside of eBay".
- "Use contact information obtained through an eBay transaction to offer to buy or sell an item outside of eBay".
- "List an item and then mention or link to additional identical or related items for sale outside of eBay".
- "Offer catalogs or other items that are used to order items directly outside of eBay".
- Recommended instead: Best Offer, Seller Initiated Offer, Private Offer.

**Member-to-member contact.** https://www.ebay.com/help/policies/member-behavior-policies/membertomember-contact-policy?id=4262
- Bans "Sending irrelevant or unrelated promotional messages to buyers" and "Adding members to mailing lists or sending marketing communications without their permission".
- Allows "Messages reasonably necessary to complete an eBay transaction... provided they aren't excessive or used for unrelated promotional purposes."
- Bans "physical addresses" within eBay messaging, with no "after payment" qualifier (see the reply 11 note below).

**Feedback manipulation.** https://www.ebay.com/help/policies/feedback-policies/feedback-manipulation-policy?id=4231
- "Referencing eBay feedback in a listing title or description".
- "Offering discounts, free items, or any other form of compensation, benefit, or incentive in exchange for positive feedback."
- Feedback policy (https://www.ebay.com/help/policies/feedback-policies/feedback-policy?id=4208): "Creating, soliciting, or using fake, misleading, or manipulated feedback is not allowed."

**Package inserts.**
- I found no eBay policy page on inserts. A volunteer Community Mentor says "there is no rule concerning package inserts", with the same limit (nothing in listings or eBay messages). This is hearsay, not eBay text (https://community.ebay.com/t5/Ask-a-Mentor/Ads-in-Packages/td-p/33839575).
- **Gray:** an insert with an Instagram handle and nothing for sale.
- **Risky (inferred from 4272):** an insert that points to another shop, a catalog, or an off-eBay discount. That includes a Fabulous From Online hire flyer.
- **Safe:** an insert that only points to eBay. A printed coded coupon is the eBay-sanctioned discount, and it needs a Store.

**Discrepancies (X verified, Y need review):**
- **Feedback mentions.** The feedback policy bans referencing feedback in a description. The endorsements policy (https://www.ebay.com/help/policies/listing-policies/thirdparty-endorsements-policy?id=4249) allows "Buy with confidence! I have over 1,000 positive feedback ratings." The kit follows the stricter rule; keep it.
- **Pickup address in Messages.** The contact policy bars physical addresses in eBay messaging. eBay's local-pickup page says "only share the exact pickup location once the buyer has paid... through Messages" (https://www.ebay.com/help/selling/posting-items/setting-postage-options/local-pickup?id=4181). Follow the pickup page, which is the more specific instruction.

## 5. Kit audit, file by file (`assets/ebay-shop-kit/`)

- **README.txt:** clean.
- **listing-footer.txt:** clean. No handle, URL or contact detail. The closing line, "Follow Holliewood & Vine on eBay", matches the allowed "Follow Seller" language. Cosmetic: the buyer-facing control is labeled "Save". Returns text must match the native policy, because buyers contract on the listing's stated terms (eBay selling practices, search snippet).
- **listing-footer.html:** clean.
  - Its one link, `https://www.ebay.com/usr/holliewoodandvinellc`, is an allowed "Other eBay page" over HTTPS.
  - `target="_blank"` is covered by the JavaScript policy exception for links that open "in a new window when clicked on" (https://www.ebay.com/help/policies/listing-policies/javascript-policy?id=4247).
  - It has no script, form or iframe.
  - Run eBay's active content checker (https://www.ebay.com/sh/lst/active/active-content) once in the account.
- **store-about.txt:** clean (595 characters). Store only. Free accounts use the profile About.
- **profile-bio.txt:** clean. No handle, URL or "buy elsewhere" text. Fits the free profile About field.
- **store-shipping.txt, store-returns.txt:** clean. Store-only text.
- **thank-you-card.txt:** clean on links, handles and contact details. It points only to eBay, which is the safe class. One caution: the card says "Your honest feedback on eBay helps future shoppers know what to expect." An honest-feedback request with no incentive is not on the banned list. But the disco-ball gift is "free items" and the policy bans "any other form of compensation, benefit, or incentive in exchange for positive feedback". Never put the gift and the feedback line on the same card or in the same sentence. The safer option is to drop the feedback line when a gift is in the package.
- **customer-replies.txt:** clean except reply 11 (see below).
  - Reply 10 follows eBay's own advice ("I'll use eBay's offer option").
  - Replies 4, 5 and 6 stay on eBay.
  - Reply 11: change "Agree the address privately through the order conversation" to "in eBay Messages after the buyer has paid". "Privately" can be misread as off-platform.
- **listing-template-clothing / accessories / decor:** clean. Seller-check blocks are labeled "REMOVE BEFORE PUBLISHING". The risk is leaving them in, not policy.
- **listing-template-pickup:** mostly clean. "Arrange collection through eBay Messages" is correct. The exact-address caveat is the same as reply 11.
- Not audited: `preview.html`, `setup-guide.html`, `branding.html`, `font-license.txt` (internal files).

## 6. Gaps

- Whether a public follower count shows, and whether saved sellers get email or push alerts for new listings. Only Live push is verified.
- Promoted Listings eligibility at 2 sales ("enough account activity" is undefined). No published suggested ad rates for vintage or home decor.
- Tier carve-outs for Starter. Confirm in the Seller Hub Store comparison at checkout.
- Our actual monthly selling limit (Seller Hub, Overview).
- Whether the account is a business account (gates Live).
- Package-insert rules: no official text found.
- The 60-day window for buyers to replace automated feedback (search snippet only).
- Collections on profiles.
- Whether the old social-sharing FVF credit still runs.
- The Jan 13, 2026 General fee change and a top-slot restriction: search snippets only, not on the pages I crawled.

Sources read live (all under https://www.ebay.com unless stated): the links, contact-information, offsite, member-to-member, feedback manipulation, feedback, endorsements, JavaScript, images/text and eBay Live policies; seller standards; selling limits; the Promoted Listings overview, General, Priority, Offsite and suggested-rate pages; email marketing, Discounts Manager, coded coupons, buyer groups and Best Offer/send offers; Store fees, set-up-store and manage-store; eBay Live seller page, pricing and guide; EPN help and Seller Center; the Seller Center Jan 2025 buyer-details page and Aug 2025 seller-protection page; our public profile; pages.ebay.com (make-the-most-of-ebay, ebaylive-faq, social/sharing/terms).
