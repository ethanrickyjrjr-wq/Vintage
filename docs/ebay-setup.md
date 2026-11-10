# Holliewood & Vine eBay setup

**Status, November 9, 2026:** Ricky approved dispatch within two business days and 30-day returns, with buyer-paid return postage for a change of mind and seller-paid returns for damage, faults, wrong items or description errors. **Use the free seller profile and templates now; Ricky intends to upgrade soon.** The copy and future Store assets are prepared in [`assets/ebay-shop-kit`](../assets/ebay-shop-kit/README.txt).

**Done on eBay (November 9, Claude Code via Claude in Chrome):** business policies are switched on, the HWV policies exist and four listing templates are saved. With Ricky's go-ahead in chat, **all 6 active listings now carry 30-day buyer-pays returns and 2-business-day handling**, checked from each buyer page. The seventh, the Nancy Glazier print, had already been ended: its page says it was ended Nov 9 at 4:53 AM "by indicating this item is no longer available". Claude did not end it. No messages, offers, subscription or payout settings were touched. Details: [Account state, November 9](#account-state-november-9).

**Browser access:** two Chrome browsers are connected to the account. Browser tools refuse to act until one is chosen. Pick **Browser 1** with `list_connected_browsers`, then `select_browser`. That browser is signed in as `holliewoodandvinellc`, and eBay pages open there with no extra site prompt. Screenshots time out on that window, so read pages through the DOM (`javascript_tool`, `find`, `read_page`). Do not ask for another eBay sign-in. Login details are not part of this kit.

## Account state, November 9

Everything in this section was read back from Seller Hub on November 9.

- **Seller:** `holliewoodandvinellc`, 100% positive on 2 ratings. Member since Sep 8, 2026. 253 listing views and $250.24 in sales over 90 days. There is no Store subscription; Seller Hub shows the subscription upsell page.
- **Monthly limits:** 75,000 items and $750,000. So far 7 items and $1,202 are listed or sold. The 45-item backlog fits. The "about 10 items or $500" figure in `docs/following-2026-11.md` does not apply to this account.
- **Orders:** 2 in total, both delivered, none awaiting shipment. Buyer details stay in eBay.
- **Messages:** the inbox shows 19. None were opened or sent.
- **Shipping preferences:** working days are Monday–Friday with a 2:00 PM Pacific cut-off. Carrier rates are eBay discounted. There are no combined-shipping rules, rate tables or exclusions.
- **International:** none of the policies offer international shipping. No eBay International Shipping enrollment shows on Shipping Preferences or in the policy forms. This was left unchanged.

**Listings as found in the audit.** All seven said "Seller does not accept returns" and had 3-business-day handling. The revisions that followed are listed below this table.

| Item | Format | Shipping today | Location shown |
|---|---|---|---|
| Alice + Olivia Sandals (198769499426) | Auction $26, BIN $40, 0 bids, ends Tue Nov 10, 5:44 PM ET | Calculated, plus free local pickup | Fort Myers, FL |
| Steve Madden satchel (198660368283) | BIN $15, Best Offer | Calculated | Fort Myers, FL |
| Worthington tote (198660374454) | BIN $12, Best Offer | Calculated | Fort Myers, FL |
| GUESS shoulder bag (198660388373) | BIN $15, Best Offer | Calculated | Fort Myers, FL |
| Kay Unger skirt suit (198660722385) | BIN $45, Best Offer | Calculated | Fort Myers, FL |
| Nancy Glazier framed print (198669139180) | BIN $225, Best Offer | Calculated, plus free local pickup | Bonita Springs, FL |
| Bassett coffee table (198693142364) | BIN $850, Best Offer, in a General Promoted Listings campaign | Local pickup only | Bonita Springs, FL |

**Revisions, November 9 (Ricky approved in chat).** Each listing was revised in place; none was ended and relisted. Every buyer page was then read back.

| Item | Shipping policy | Payment policy | Buyer page after revision |
|---|---|---|---|
| Sandals (auction, still 0 bids) | HWV Parcel + pickup | HWV immediate payment | 30-day returns; $5.87 calculated; free local pickup |
| Satchel, tote, GUESS bag | HWV Parcel | HWV immediate payment | 30-day returns; $5.87 calculated |
| Kay Unger suit | HWV Parcel | HWV immediate payment | 30-day returns; $7.04 calculated |
| Bassett table | Local Pickup (unchanged) | eBay Managed Payments: eBay checkout, no money orders | 30-day returns; free local pickup |
| Nancy Glazier print | — | — | Already ended Nov 9, 4:53 AM, "no longer available". Not relisted |

eBay refused immediate payment on the table: "Because you've specified Local Pickup Only for this item, you can't require immediate payment." Ricky had chosen to drop money orders, so the table now uses eBay Managed Payments, which is eBay checkout with no immediate-payment requirement and no offline methods. The same fix went into the Local Pickup template. The descriptions are unchanged; the footer has not been added to any live listing yet.

**Business policies.** Opting in is reversible: eBay's help page says "You can opt out any time", active listings are unaffected, and opting out deletes your policies ([Business policies](https://www.ebay.com/help/selling/business-policies/business-policies?id=4212), read November 9). At opt-in, eBay generated policies from the listings and named them itself. Do not edit those generated policies. Editing a policy pushes the change to every linked listing.

| Policy | Settings (read back) | Made by |
|---|---|---|
| HWV \| Returns \| 30 days \| Buyer pays | Domestic returns, 30 days, buyer pays return postage, money back. No international returns | Claude |
| HWV \| eBay checkout \| Immediate payment | Immediate payment for Buy It Now. No offline methods | Claude |
| HWV \| Parcel \| Calculated \| 2 business days | Calculated USPS Ground Advantage, 2-business-day handling, no handling charge. No pickup, no international | Claude (copied from eBay's generated policy, with only the handling time and name changed) |
| HWV \| Parcel + pickup \| Calculated \| 2 business days | Same as above, plus free local pickup | Claude (copy) |
| Calculated: USPSParcel, 3 business days (two copies, with and without pickup) | Current setup of the shipped listings | eBay |
| Local Pickup | No shipping, local pickup only | eBay |
| No Return Accepted | No returns | eBay |
| eBay Managed Payments; eBay Managed Payments - MOCC | No immediate payment. MOCC also accepts money orders (the table's setup) | eBay |

Not created: **Fragile** and **Clothing combine weights**. They depend on tested packing methods. The approval covered dispatch and returns, not carrier changes.

**Listing templates** (Seller Hub, at `bulkedit.ebay.com/ManageTemplates`). All four use Buy It Now, quantity 1, HWV immediate payment and the HWV 30-day return policy. Each description holds the template's bracketed skeleton followed by the HTML footer. The "SELLER CHECK" notes are left out; they stay in the kit files.

| Template | Shipping policy | Category |
|---|---|---|
| HWV \| Clothing \| 2 day \| 30 day | HWV Parcel | **Antiques > Other Antiques: change it on every listing.** Women's Vintage Clothing would not save on a template because eBay then requires a title and a condition |
| HWV \| Accessories \| 2 day \| 30 day | HWV Parcel | Women's Bags & Handbags |
| HWV \| Decor \| 2 day \| 30 day | HWV Parcel + pickup (no Fragile policy yet) | Home Décor > Other Home Décor |
| HWV \| Local pickup \| 30 day | Local Pickup (eBay's generated policy), with payment set to eBay Managed Payments because pickup-only listings cannot require immediate payment | Furniture > Tables |

**Not done, and why:**
- **Profile About text.** The field is empty, with a 1,000-character limit. Typing `profile-bio.txt` and pressing Save twice did not persist after a reload. Paste it by hand at `ebay.com/usr/holliewoodandvinellc?_tab=about`.
- **Clothing template category:** see the template table above.

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

**Unmeasured clothes go in as eBay drafts, not live listings** (checked 2026-11-09). Seller Hub keeps a draft 75 days after its last edit, up to 5,000 drafts ([Seller Center, Winter 2024](https://www.ebay.com/sellercenter/resources/seller-updates/2024-winter/business)). Do not publish first and add measurements later. Once an offer is sent or received, eBay blocks edits to the existing description and item specifics ([Revise a listing](https://www.ebay.com/help/selling/listings/revising-listing?id=4356)). The `[about NN]` figures in `listing.txt` are estimates from photos, so they never go into a listing. Weigh each packed item at the same time as measuring, because HWV Parcel uses calculated postage.

### Clothing drafts, November 9

All 20 clothing items are saved as Seller Hub drafts (**Listings → Drafts**). None is live; Active still shows only the six earlier listings. The custom label (SKU) `HWV-NN` matches the Drive folder number. Drafts expire 75 days after the last edit, so these go on **January 23, 2027**; any edit restarts the count.

Every draft was read back from eBay after saving, and each one has:
- a title of 80 characters or fewer. eBay's limit is 80, and every `listing.txt` title except item 45 was 84 to 92 characters, so each one was shortened by hand;
- a category, Pre-owned – Good, quantity 1 and Buy It Now;
- the item specifics from `listing.txt`, plus any eBay filled in from the title (checked);
- the Drive photos, front first;
- the description, with every measurement, size and condition gap left as `____`, then the shop footer;
- the policies HWV eBay checkout immediate payment, HWV Parcel and HWV Returns 30 days.

The photo estimates (`[about NN]`) and the unverified "smoke-free" line were removed. eBay pre-fills its own suggested price (it put $18 on item 01), so the price was cleared on every draft. It also switches Best Offer on by default. Best Offer was turned off on all 20 because offers wait for a per-item minimum, and an offer locks the description. Promoted Listings (General and Priority) are off on all 20, even though the General campaign's 13% rate shows as pre-filled.

**Before each draft can go live, with the piece in hand:**
1. Search the description for `____` and fill each gap: measurements, condition, and size where the label has none.
2. Change Pre-owned – Good if the inspection says otherwise.
3. Weigh the packed item and enter its weight and box size. HWV Parcel uses calculated postage.
4. Set the price, then Preview and List it.

| NN | Category | Photos | Notes |
|---|---|---|---|
| 01 Liz Claiborne shirt dress | Women > Dresses | 3 | Count the ten buttons |
| 02 Future Collective slip dress | Women > Dresses | 3 | |
| 03 Ronny Kobo maxi | Women > Dresses | 3 | |
| 04 Brooks Brothers shorts | Women > Shorts | 3 | |
| 05 The Limited blouse | Women > Tops | 3 | |
| 06 Starlo dress | Women > Dresses | 3 | No label size: set Size from the measurements |
| 07 We The Free jeans | Women > Jeans | 4 | Waist Size and Inseam specifics come from the tape |
| 08 Free People blouse | Women > Tops | 3 | |
| 10 Lew Magram maxi | Women > Dresses | 3 | Check the satin collar for yellowing |
| 11 adidas sample jacket | Women > Activewear Jackets | 4 | Confirm the shell material on the care label |
| 12 Connie Rizza dress | Women > Dresses | 3 | No label size |
| 13 Jones New York blouse | Women > Tops | 3 | |
| 14 Ghost London dress | Women > Dresses | 3 | |
| 15 coral-print trousers | Women > Pants | 2 | No brand or size yet. Adding a brand means shortening the title again |
| 16 Denim & Flower bomber | Men > Coats, Jackets & Vests | 5 | Includes both flaw photos |
| 17 Neiman Marcus silk dress | Women > Dresses | 3 | |
| 18 Zara jumpsuit | Women > Jumpsuits & Rompers | 3 | eBay added "Set Includes: Shorts"; it was removed |
| 19 Columbia PFG shirt | Men > Casual Button-Down Shirts | 3 | |
| 20 Bonnie & Norma skirt | Women > Skirts | 3 | |
| 45 halter tuxedo vest | Wedding & Formal > Men's Tuxedo & Formal Vests | 1 | One photo only, and no size yet |

eBay will require a Size before 06, 12, 15 and 45 can list. Item 16's description says "Priced accordingly"; check that line when setting its price. Do not re-run `tools/ebay-drafts/` on these drafts. The item specifics for 04, 05, 07, 11, 15, 16, 18, 19, 20 and 45 were adjusted in eBay to fit each category, and the generator would put the old values back. Dresses went into Women > Dresses with Vintage: Yes, not into Specialty > Vintage. The photo plan calls for 8 to 12 photos (label, fabric, closures, every flaw, a measurement card), and these drafts have 1 to 5. Add shots during the measuring pass where possible.

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

The audit, policies and templates are done (see [Account state, November 9](#account-state-november-9)). What is left:

1. **Done:** the 6 active listings were revised and checked from the buyer view (see the revisions table). Find out from Ricky why the print was ended at 4:53 AM. Then decide whether it comes back, as a relist under the new policies, or stays off.
2. **eBay revise limits, for later edits:** the sandals auction ends Tue Nov 10 at 5:44 PM ET. eBay's [Revise a listing](https://www.ebay.com/help/selling/listings/revising-listing?id=4356) page (read Nov 9) sets out what can still change in an auction with no bids and under 12 hours left, and policy edits are not on that list. So finish any further change to it before about 5:44 AM ET on Nov 10.
3. **Add the footer last.** The policies now match on all 6 active listings, so the footer can go on. First scan each existing description for "no returns", smoke-free claims and similar wording.
4. **Paste the profile About text by hand** (it would not save from automation). The profile image stays as it is until Ricky picks one.
5. **When nothing links to them any more,** delete the generated "Calculated: USPSParcel, 3 business days" and "No Return Accepted" policies (or use Delete inactive policies). Ask Ricky before deleting.
6. **Inbox aids:** inspect folders and AI reply suggestions. Do not send messages or offers just to test them.

Do not purchase a Store subscription during this task. Completion still requires reading back the buyer-facing listing pages.

## Kit verification

Plain-text and HTML footer wording match. The HTML fragment has no scripts, forms, external images or off-eBay links. The About copy is 595 characters. Both PNGs match eBay's specified dimensions and are under 12 MB. The local preview and standalone footer were checked at a 390-pixel mobile width, and the preview at 1280 pixels: no horizontal overflow or script errors. All twelve copy controls and expandable sections work; if browser clipboard permission is unavailable, the text is selected for manual copying. Native eBay editor rendering and saved account settings remain unverified until implementation.
