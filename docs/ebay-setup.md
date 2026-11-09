# Holliewood & Vine eBay setup

**Status, November 8, 2026:** Ricky approved dispatch within two business days and 30-day returns, with buyer-paid return postage for a change of mind and seller-paid returns for damage, faults, wrong items or description errors. **Use the free seller profile and templates now; Ricky intends to upgrade soon.** The copy and future Store assets are prepared in [`assets/ebay-shop-kit`](../assets/ebay-shop-kit/README.txt). No eBay account settings, messages, subscriptions or live listings have been changed.

Ricky confirmed that he is signed in. This Codex session has no callable browser-control or computer-use runtime, so it cannot inspect that tab. A public profile request also returned HTTP 403. A TinyFish browser connection was suggested, but is not confirmed connected. Login details are not part of this kit. The existing account evidence is the [earlier November 8 inspection](../research/instagram-and-marketplaces-2026-11-08.md), not a new live audit.

## Start with a dependable shop

Use consistent photographs, clear condition and measurements, predictable dispatch and an easy return process. Carry the website's burgundy and cream through the Store banner, logo and description footer. The item's own details come first; append the footer after condition, dimensions and inclusions.

The approved policy is the starting promise. Internally, aim to dispatch sooner when practical, check messages twice daily and answer within one business day. These are operating targets, not an additional published guarantee.

## Branding now and after the Store upgrade

For the free setup, use the short bio where editable, the reusable description footer, business policies and listing templates. The Store billboard, Store categories and About-tab policies are prepared for the later upgrade; they are not part of the current free-profile implementation.

An eBay Store supports a logo, billboard, About text, Store policies, categories, featured inventory and marketing sections within eBay's layout. It cannot reproduce the website's interactive room experience.

| Kit file | Destination |
|---|---|
| `ebay-logo-300.png` | Store logo, rendered from the website favicon |
| `ebay-billboard-1280x290.png` | Store billboard, using the website colors and Bodoni typography |
| `store-about.txt` | About this Store |
| `profile-bio.txt` | Short seller bio, if the account offers an editable profile |
| `store-shipping.txt`, `store-returns.txt` | Store policy text, after matching policies are applied |
| `listing-footer.txt` | Plain-text description editor or phone copy/paste |
| `listing-footer.html` | HTML description editor, where available |

eBay specifies 300 × 300 pixels for the logo and 1280 × 290 for the billboard, each under 12 MB; About text has a 1,000-character limit. Use **Store → Edit store / Tell Your Story**, preview, then publish. About policy text does not replace native listing policies. [Store customization](https://www.ebay.com/help/selling/ebay-stores/manage-ebay-store?id=4090).

Use **Holliewood & Vine** as the display name, subject to availability. Keep seller username `holliewoodandvinellc`. Add categories as stock supports them: Clothing; Bags & Accessories; Shoes; Art & Wall Decor; Home & Lighting; Furniture & Local Pickup. Avoid empty categories and unsupported location or showroom claims.

### Later Store upgrade

Ricky chose the free seller profile and templates for now and said the shop will upgrade soon. Do not start a paid subscription in this task. When the upgrade is requested, inspect the current subscription and reassess **Starter at $7.95 per month on monthly renewal**. The annual term is $4.95 per month. Basic is $27.95 monthly or $21.95 per month on an annual term. These are US published prices checked November 8, before applicable tax. Show the actual checkout terms before purchasing. [Store plans](https://www.ebay.com/sellercenter/selling/how-to-sell/set-up-your-store).

Starter includes 250 zero-insertion-fee listings, with exclusions and selling limits still applying. Evaluate it as a branding expense; do not assume it pays for itself through lower final value fees. Compare Basic against actual categories, volume and fees before upgrading. [Store selling fees](https://www.ebay.com/help/selling/fees-credits-invoices/store-selling-fees?id=4809).

Templates and business policies can be prepared without purchasing a Store. Marketing tools vary by plan; inspect account availability before planning coupons, newsletters or promoted placements.

## Native business policies

Open [Seller Hub](https://www.ebay.com/sh/ovw) and [Business policies](https://www.ebay.com/bp/manage). Inspect existing policies and linked listings first. Opt in if needed, then create the policies below. An edit can update every compatible linked listing; restricted listings may retain a generated copy. Verify affected listings afterward. Existing policies can also be selected while listing in the mobile app. [Business policies](https://www.ebay.com/help/selling/business-policies/business-policies?id=4212).

| Policy name | Settings | Scope |
|---|---|---|
| HWV \| Returns \| 30 days \| Buyer pays | Domestic returns accepted; 30 days; buyer pays return postage; money-back refund where offered | Standard starting return policy |
| HWV \| Parcel \| Calculated \| 2 business days | Calculated domestic postage; USPS Ground Advantage for eligible parcels; 2 business days; no extra handling charge | Clothes, most bags and small non-fragile items |
| HWV \| Fragile \| Calculated \| 2 business days | Calculated domestic postage; 2 business days; verified service for the packed item, such as UPS Ground or USPS Ground Advantage; no automatic combining | Fragile pieces that can be shipped safely |
| HWV \| Local pickup only | Local pickup; no parcel or international delivery; correct item town/ZIP | Furniture and pieces without a proven shipping method |
| HWV \| eBay checkout \| Immediate payment | eBay checkout; immediate payment for eligible Buy It Now listings | No bank or payout changes; inspect offers and auctions separately |

Only dispatch and returns have been explicitly approved. Carrier selection, combined-shipping settings and the other operating details are implementation recommendations, dependent on actual parcels and account options.

For each parcel listing, enter **packed** weight and outside dimensions, not bare item weight. Confirm the dispatch ZIP, return address and item location privately in eBay; neither Ohio nor Florida should be assumed for all stock. Do not copy private addresses into the repository. Offer faster paid services only when they can be fulfilled. Check destination coverage, including PO boxes, against the selected carrier.

Set working days to Monday–Friday initially. Obtain a carrier acceptance scan within the two-business-day window; creating a label is not dispatch. Use the order's displayed ship-by deadline. Handling time and transit time are separate. [Handling time](https://www.ebay.com/sellercenter/shipping/preparing-your-shipment/handling-time).

### Returns and international orders

Buyer-paid change-of-mind postage does not apply to damage, faults, wrong items or a description mismatch. Those returns require seller-paid return shipping under the applicable eBay protection. Use the return request's address and instructions. [Return shipping](https://www.ebay.com/help/selling/managing-returns-refunds/return-shipping-for-sellers?id=4703).

Recommended choices: no restocking fee, no automatic refund-without-return rule at launch, and human review of exceptions. Check returns daily and follow the displayed response deadline. After a return arrives, review and refund within two business days or use eBay's resolution process. Never condition a refund on a favorable review. [Handling returns](https://www.ebay.com/help/selling/managing-returns-refunds/handling-return-requests?id=4115).

For local pickup, explain that change-of-mind returns require buyer-arranged return transport. Arrange seller-responsible returns through eBay where applicable. Furniture is not automatically exempt from the approved return promise. At handover, verify payment and scan the buyer's QR code or enter the six-digit pickup code in the order. [Local pickup](https://www.ebay.com/help/selling/posting-items/setting-postage-options/local-pickup?id=4181).

Inspect **eBay International Shipping** enrollment before changing international settings. For eligible sales, the seller sends the properly packed item to eBay's domestic hub and eBay handles the international leg and program returns. This differs from self-managed international shipping. Do not combine separate EIS orders; follow each order's instructions. Leave existing enrollment unchanged until inspected. [eBay International Shipping](https://www.ebay.com/sellercenter/shipping/ebay-international-shipping).

### Combined shipping

Start with manual review for mixed vintage stock. Store copy invites buyers to ask before checkout and makes no automatic discount promise.

After verifying a repeatable clothing packing method, consider **HWV | Clothing | Combine weights**, using combined weights without a speculative subtraction. Apply only to compatible clothing listings. Check two actual draft parcels and near/far destination quotes first. Keep fragile pieces and furniture out. eBay requires both a rule in Shipping Preferences and its application to listings; creating it alone is insufficient. [Shipping discounts](https://www.ebay.com/help/ship-track/ship-track-selling/ebay-postage-discounts?id=4168).

## Make listing from the phone straightforward

Create four Seller Hub templates from the kit: Clothing, Accessories, Decor and Local Pickup. Save templates rather than publishing placeholder listings. Use **Listings → Listing templates → Create new template**. [Selling templates](https://www.ebay.com/help/selling/selling-tools/selling-templates?id=4097).

For each unique item:

1. Use its Drive folder under `Holliewood eBay/Items`; photos and `listing.txt` stay together.
2. Inspect the item and fill real measurements, condition, inclusions, label information and flaws. Replace every bracket and blank. Record SKU and storage location.
3. Add the actual item's photos. Keep accurate labels, close-ups and flaws. Reserve branding for the Store and description.
4. Fill native category and item-specific fields. The description does not substitute for size, brand or condition fields.
5. Choose matching policies and enter packed specifications. Quantity is one for a unique piece.
6. Paste the shared footer below the completed item description. On a phone use `listing-footer.txt`, not HTML source.
7. Check price, shipping total, offers, photos and mobile preview. Remove all internal notes before publishing.

The footer is a maintained master, not a global live include. Editing it locally will not update existing listings. If the promise changes, update the master, eBay templates, Store text and applicable live descriptions together. Native policies and description promises must agree.

Some November 8 drafts contain estimated measurements and blanket smoke-free claims. Verify or remove them before publication. This task has not rewritten those drafts or appended the policy to unreviewed listings.

## Messages and customer service

Use `customer-replies.txt` as a copy bank, adapted to the actual conversation. No buyer messages have been sent. Suggested inbox folders: Needs reply, Awaiting buyer, Shipping and Returns. eBay documents up to five custom folders and AI reply suggestions that can be reviewed and edited before sending. Inspect availability; a native saved-reply library has not been configured. [Messages](https://www.ebay.com/help/selling/selling-tools/schedule-time-away?id=4194).

Keep communication on eBay. Check questions each morning and late afternoon. Avoid duplicate shipment notices when eBay already supplies tracking updates. Answer with verified facts, a next step and a date for the next update. Do not claim a refund or dispatch event that has not happened.

When away, configure sales availability and the separate auto-response. Existing obligations continue. Pausing sales does not stop auctions, and some offer and pickup scenarios have special delivery-date behavior. Inspect these before leaving. [Time Away](https://www.ebay.com/help/selling/selling-tools/time-away?id=5137).

## Followers, reviews and pricing

Use the follow invitation and consistent Store identity. Publish small batches of complete listings at a pace the shop can fulfill. Consider offers only after setting an item-specific minimum that preserves margin.

Compare **sold** items with similar condition, size, maker and completeness, using item price plus shipping. Before accepting an offer, allow for acquisition cost, postage, packing, actual eBay fees, ad fees and returns. Do not apply one floor across furniture and inexpensive clothing. The seven historical prices need current comparables and costs before any revision.

Use `thank-you-card.txt` as an optional package insert. Ask for honest feedback without incentives or pressure. eBay prohibits feedback references in listing titles/descriptions and incentives for positive feedback, so the footer contains neither. Keep site URLs, social handles, email and phone details out of listing copy; the supplied link stays on the seller's eBay page. [Feedback policy](https://www.ebay.com/help/policies/feedback-policies/feedback-manipulation-policy?id=4231), [links policy](https://www.ebay.com/help/policies/listing-policies/links-policy?id=4248).

Review weekly: carrier scans by deadline, unanswered questions, returns by reason, damage incidents, net proceeds, followers and sold/listed counts. Include counts alongside percentages for small samples. The target is reliable fulfillment and fewer surprises. This two-day, buyer-paid-returns baseline does **not** by itself qualify listings for Top Rated Plus, which generally requires Top Rated status, same/one-day handling and 30-day free returns. [Top Rated requirements](https://export.ebay.com/en/growth/seller-performance/top-rated-seller/).

## Resume account implementation

With a supported browser connection, continue without repeating the approved-policy question:

- Confirm seller identity, subscription, selling limits, existing policies and international enrollment. Inspect listings and any orders or bids before revisions.
- Verify locations privately in eBay. Establish packed specifications and suitable carrier services.
- Create policies and four templates, update compatible listings with matching descriptions, and verify each changed listing from the buyer view. Record any revisions eBay disallowed.
- Apply the free-profile bio and image where available. Keep the Store banner, About text and categories ready for the later upgrade. Do not purchase a Store subscription during this task.
- Configure selected inbox aids and FAQs where available. Do not send messages or offers merely to test them.

Earlier evidence listed Kay Unger suit, Guess bag, Worthington tote, Steve Madden satchel, Alice + Olivia sandals, Bassett coffee table and Nancy Glazier horse print. Recheck their status. The sandals were an auction; inspect bids and revision restrictions. The table and framed print need special attention to pickup or safe packing. The earlier seven listings and two positive ratings are historical, not a claim about today's live account state.

Completion requires reading back saved settings and buyer-facing pages. This kit is ready for implementation; it is not evidence that eBay has been configured.

## Kit verification

Plain-text and HTML footer wording match. The HTML fragment has no scripts, forms, external images or off-eBay links. The About copy is 595 characters. Both PNGs match eBay's specified dimensions and are under 12 MB. The local preview and standalone footer were checked at a 390-pixel mobile width, and the preview at 1280 pixels: no horizontal overflow or script errors. All twelve copy controls and expandable sections work; if browser clipboard permission is unavailable, the text is selected for manual copying. Native eBay editor rendering and saved account settings remain unverified until implementation.
