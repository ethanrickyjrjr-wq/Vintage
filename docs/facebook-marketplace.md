# Facebook Marketplace setup (2026-11-09)

Ricky asked on 2026-11-08 to get Facebook set up for Holliewood and Vine so the shop can post on Marketplace. He gave the profile URL `https://www.facebook.com/profile.php?id=61596451137563` and signed in to it in Chrome.

**Current status, 2026-11-09:** Hollie's established account is now verified in the browser, the existing shop Page has been found, and item 01 has been recreated as an unpublished draft there. The "Hollie Wood" profile below is a second account for the same person; its earlier draft remains untouched. Retiring that account is Ricky's call. The preparation boundary below supersedes earlier suggestions to change Hollie's profile, friend list or professional mode. See the current inspection results before acting on the historical notes.

## Current preparation boundary (Ricky, later on 2026-11-09)

Ricky reports that Hollie's established Facebook account is now signed in and asks to prepare the shop without changing her regular profile until everyone is ready. This supersedes the earlier instruction to copy the shop bio and work line onto that profile. Keep its name, photos, bio, work, city, professional mode and privacy settings unchanged during preparation. Public listings, posts, friend invitations, group activity, account linking and automatic sharing wait for launch authorization.

Recommended preparation:

1. Inspect which account is active, Marketplace access and any existing Holliewood & Vine Page, without saving changes. Use the profile's View As option to review its existing public appearance when accessible.
2. Prepare the shop Page's bio, logo, cover and opening posts in local files. A business Page is the proposed home for shop branding; check for an existing Page before creating one. Do not assume creating a Page is private, or that an unpublished/deactivated Page is editable. Verify the actual visibility controls before building inside Facebook.
3. Prepare item photos and listing copy locally. Save Marketplace drafts only after confirming the established account and the actual Save draft control. Recreate item 01 there; the previous draft belongs to the second account. Its price, condition and measurements still need confirmation.
4. Review the complete material together before publishing. Profile branding is optional and a separate decision; it is not a prerequisite to prepare listings. Keep the second account untouched pending Ricky's decision.

Marketplace remains connected to the personal seller profile. Meta's [March 2026 announcement](https://about.fb.com/news/2026/03/facebook-marketplace-new-meta-ai-tools-make-selling-faster-and-easier/), re-read in this session, says buyers can see account age, friend count and Marketplace activity. A Page is not a separate identity for ordinary personal Marketplace listings. Do not treat a Hide from friends option as a private staging area; keep listings unpublished during preparation.

## Verified preparation, later on 2026-11-09

**Browser access works through Chrome DevTools MCP.** Ricky added `chrome-devtools` with `npx -y chrome-devtools-mcp@latest --autoConnect`; the server connected to the running Chrome browser. The Windows Computer Use helper still returned `Computer Use native pipe is unavailable: failed to connect native pipe: The system cannot find the file specified. (os error 2)`, but that no longer blocks this task. No credentials were read or entered.

### Account and existing Page

- The signed-in account menu and Marketplace composer identify **Hollie Lippmeier**, the established account. Its personal name, photographs, bio, work details and settings were not changed.
- **[Holliewood and Vine already exists](https://www.facebook.com/61589196235186/)**, Page ID `61589196235186`, with **186 followers** observed. It appears in Hollie's account switcher and shortcuts. No duplicate Page was created.
- The Page was also readable in a new tab that showed Facebook's logged-out interface. Treat it as public, not a hidden staging Page. No Page visibility settings were changed; unpublishing controls were not investigated.
- Its current Intro describes a **Loveland, Ohio showroom and studio rental**. Ricky confirmed in this session that the prepared replacement copy should describe **Southwest Florida vintage and resale sales, with no showroom or rentals**. Exact address and contact details still need review before any live update. No Page edits or posts were saved.
- The seller dashboard already had **two active listings**: the Bassett wood/glass coffee table at **$850** and Turkish pillow covers at **$10**. Both remain unchanged.

### Item 01 saved as a draft

[Open the saved Liz Claiborne draft](https://www.facebook.com/marketplace/edit/?listing_id=1761191728799823). Its draft ID is `1761191728799823`.

The composer exposed an explicit **Save draft** button under Hollie's established seller identity. The draft was saved, appeared under the **Drafts** heading, then was reopened to verify:

- Title: `Liz Claiborne Blue Leopard Print Midi Shirt Dress — Size 8`.
- Three existing photographs in front/back/label order; front and back are Photoroom exports.
- The factual description from [`marketplace-01.txt`](../assets/facebook-shop-kit/marketplace-01.txt), without unconfirmed condition, exact decade, measurements, smoke-free or no-ironing claims.
- Material `100% Polyester` and private SKU `HV-01`.
- Women's clothing & shoes selected during creation; reopening displays the parent category Clothing, Shoes & Accessories.
- **Condition is blank. Price was left blank, but Facebook saved it as `$0` and shows `FREE` in the draft list. This is not an approved price. Replace it before publishing.**
- The preview defaults to **Loveland**. Confirm the actual listing location and pickup/shipping arrangements before publication. The approved regional Page copy does not establish an exact pickup location.

After saving, **Your listings** still showed **2 active**. No Next or Publish action was taken. Neither of the existing active listings, the existing Page, nor either personal profile was edited.

### Local review pack

Open [`preview.html`](../assets/facebook-shop-kit/preview.html) for the proposed bio, About text, three posts, existing brand artwork and first item. Plain-text files in the same folder are ready for review and copying. Existing artwork is reused unchanged; the eBay-sized banner is a cover reference and still needs a Facebook crop review before upload.

The Page copy uses Ricky's confirmed Southwest Florida direction. The item still needs availability, price, condition, tape measurements and delivery/location confirmation. Publication and any shop link or work line on Hollie's personal profile remain separate decisions.

### Browser notes for continuing

- Reuse the already signed-in Facebook tab. In this inspection, newly created tabs used a different browser context and showed a logged-out interface; no new login was necessary in the original tab.
- Prefer DOM text and accessibility snapshots. A live-browser screenshot timed out; the local preview was rendered separately with headless Chrome.
- The MCP form-fill tool did not persist the description textarea through React rerenders. Clicking the textarea and entering it with `type_text` did; its full contents were verified after reopening the saved draft.
- A `Public` label and "Listed a few seconds ago" appear in the composer preview even before publication. The actual saved status was verified under the **Drafts** heading, with the active-listing count unchanged. Hide from friends was not used as a privacy substitute.

## Earlier observed state: the second account

- **Account.** The account is a personal profile named "Hollie Wood", signed in to Ricky's Chrome. It is new: no profile photo, no cover photo and 0 friends. Login details are not kept here.
- **Marketplace access is open.** Both `facebook.com/marketplace/create/item` and the seller dashboard load. No restriction notice appeared.
- **Set on 2026-11-09 with Ricky's approval:**
  - Bio: "Holliewood & Vine. Curated vintage clothes, lamps, art and decor. IG @holliewoodandvine".
  - Work line: Owner at Holliewood & Vine, Bonita Springs, Florida. This is a plain-text entry and is not linked to any of the "Hollywood & Vine" Pages Facebook suggested.
  - Current city: Bonita Springs, Florida. "Share on Feed" was declined, so no posts were created.
- **One draft listing, not public.** Item 01 (Liz Claiborne leopard shirt dress) has:
  - 3 Photoroom photos, the title, and the description with its blanks left in;
  - category Women's clothing & shoes, material 100% Polyester, and private SKU `HV-01`.
  - Price and condition are blank, so the draft shows as $0.
  - To finish it: Marketplace > Selling > Continue.
- **Not done:** profile photo, cover photo, friends, payouts and shipping.

## What Meta's own pages say (read 2026-11-08/09)

| Fact | Source |
|---|---|
| A Page cannot create a Marketplace listing. List from the personal profile. | https://www.facebook.com/help/1557451221155310 |
| Marketplace is meant for consumer-to-consumer sales. Business sellers face restrictions only in the EEA, the Philippines and India, so the US is fine. | https://www.facebook.com/policies_center/commerce |
| Prohibited items that matter for vintage: used cosmetics or cosmetics not in original packaging, animals or animal parts, recalled products, counterfeits, alcohol, adult products. | same |
| Meta may restrict Marketplace for a "new or inactive account" or an "additional Facebook profile instead of your main profile". | https://www.facebook.com/help/1968285150185577 |
| Buyers see an AI summary of the seller that includes how long they have been on Facebook and their number of friends (March 2026). | https://about.fb.com/news/2026/03/facebook-marketplace-new-meta-ai-tools-make-selling-faster-and-easier/ |
| Your name should be the one friends use and should appear on an ID. "Profiles are for individual use only. You can create a Page for a business." | https://www.facebook.com/help/112146705538576 |
| Shipping and checkout reach buyers in the continental US. "Some shipping features are not available to all eligible sellers." | https://www.facebook.com/help/796066857221106 |
| You must ship within 7 calendar days or the order may be cancelled. Seller Protection requires Meta prepaid labels and onsite checkout. The maximum list price for shipped items is $500. The chargeback fee is $20. | https://www.facebook.com/legal/merchant_policies |
| Selling fee: 10% per transaction, minimum $0.80, charged on the whole amount including shipping and tax. | same |
| Payouts go to a bank or PayPal account. If sales pass a limit with no tax ID on file, transfers are held. Facebook collects tax only in marketplace-facilitator states. | https://www.facebook.com/help/449101635835192 |

**Discrepancy:** the 10% fee above is verified from Meta's Seller Protection Policy. A search summary of Meta's marketing page (https://www.facebook.com/marketplace/sell-with-shipping/) quotes 5%. That page was not opened in this session and needs review. Plan on 10%.

## What it means for the shop

- **Account risk.** If "Hollie Wood" is not the name on Hollie's ID, Meta can lock the profile behind an ID check. All Marketplace listings would go with it. The repo does not say whether it is her real name; Ricky has to confirm it.
- **Trust.** A blank profile with 0 friends shows that to every buyer. Hollie should add her own photo from her phone and friend the people she actually knows before the first listings go live.
- **Pace.** Start with a few listings and add more as the account ages. Meta publishes no number, so this is a recommendation, not a rule.
- **Price cap for shipping.** Pieces over $500 cannot ship through Marketplace. The $850 Bassett coffee table is local pickup only here.
- **Dispatch time.** The eBay promise of two-business-day dispatch fits inside Meta's 7-day limit.

## Earlier handoff for the second account (paused)

These steps predate the decision to use Hollie's established account and the preparation boundary above. Do not execute them against either account without reconciling that boundary.

1. Hollie adds a profile photo from her phone. Untick "share to feed" if she does not want a post. A cover photo is optional.
2. Add real friends.
3. Set up payouts with a bank account or PayPal, plus the tax ID when asked. Claude does not enter bank or tax details. The click path was not verified in this session. Facebook should prompt for payouts the first time a listing is set to shipping (finish the draft, then Next > delivery options). Meta's help page above covers updating the payout account.
4. Finish the item 01 draft: measurements, condition, price. Then publish from the phone.
