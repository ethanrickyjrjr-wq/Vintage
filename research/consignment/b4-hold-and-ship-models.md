# b4: Hold-and-ship consignment models (owner keeps the item, ships only when it sells)

Agent b4, Group B (consignment and buying). Researched and fetched 2026-10-27. Raw pages are in `research/consignment/raw/b4-*.md`.

**Research, not legal advice. Every tax, legal, and contract point below needs a CPA / Florida attorney before Holliewood and Vine relies on it.**
**Florida assumption:** I assumed Holliewood and Vine is a Florida-based seller (Ricky's repo and Fedora box context; nobody confirmed the legal entity or state of formation). Out-of-state sales-tax nexus on own-site sales was NOT researched.

## TL;DR

1. Yes, the model exists: the owner keeps the item and ships direct to the buyer. It is the default on peer marketplaces (Chairish seller-managed shipping, Poshmark, Vestiaire Direct Shipping). It is NOT how consignment shops or eBay's own consignment service work. Those are ship-to-them.
2. There are two clean versions. (a) The owner lists on their own account and is the seller; H&V is a paid helper, with no title, no tax, no merchant-of-record role. (b) H&V's own site sells the item and the owner ships it. Then H&V is the merchant of record and a Florida "marketplace provider," and carries refunds, chargebacks, and tax even though it never touches the box.
3. Etsy is the problem platform. Its help text bans drop shipping (exception: craft/party supplies only), and an owner shipping straight to the buyer reads as drop shipping. I could not read Etsy's Seller Policy or Creativity Standards (walled). On Etsy, ship-to-us works and hold-and-ship is high risk.
4. The core operational risk: when an item is damaged in transit, the carrier wants photos of the packaging and label (Chairish's claims page says so). H&V cannot produce those for an item it never handled.
5. Skip Stripe Connect and Shopify multi-vendor apps for now. For a one-person shop with a handful of consignors they are overkill. Hold-and-ship via a flat-fee listing service or one-off exceptions for big or fragile pieces is the sane version.

---

## 1. What changes when title and possession stay with the consignor

| Question | Ship-to-us (shop holds it) | Hold-and-ship, H&V sells on its own site | Hold-and-ship, owner is seller on their own platform account |
|---|---|---|---|
| Who the customer buys from (merchant of record) | H&V | H&V (Shopify TOS: "You are the seller or merchant of record for all sales through the Services"; Stripe: the entity the customer understands they are buying from) | The owner (inference; no page I read uses the phrase "seller of record") |
| Florida sales tax | H&V as consignee (FL Rule 12A-1.081) | H&V, almost certainly (see section 5) | The platform collects and remits (Etsy, eBay, Whatnot, Depop pages); the owner does not |
| Returns / chargebacks | H&V, and it has the item back | H&V, but the item is at the consignor's house and the money may already be paid out | The owner, under the platform's buyer protection |
| Damaged in transit | H&V packs it, H&V documents it | Consignor packs it, H&V cannot document it | The owner |
| Payment split | H&V keeps its cut, pays the consignor later | Same, but you must hold the payout until the return window closes | Platform pays the owner; H&V is paid separately by the owner (flat fee or %) |
| Platform terms | Listing a held item is the normal case | Etsy: high risk. eBay: not addressed. Shopify: OK if H&V is the seller (see section 4) | Fine, but H&V needs delegated access the platform allows (eBay: Multi-User Account Access, not shared logins) |

---

## 2. Platforms where the item stays with the owner until sold

None of the pages I fetched use the literal phrase "seller of record." "Merchant of record" appears only in Shopify's and Stripe's docs. Everywhere else I describe who the platform treats as the seller from its own wording.

### Chairish (owner keeps the item; the best fit for big and fragile pieces)
- Homepage: https://www.chairish.com/
- Pages read: https://support.chairish.com/hc/en-us/articles/44169858180497-Who-Pays-for-Shipping, https://support.chairish.com/hc/en-us/articles/45510187289105-Seller-Payment-Processing, https://support.chairish.com/hc/en-us/articles/46175167712529-Lost-or-Damaged-Order-Claims (accessed 2026-10-27)
- Hold-and-ship is the default. Quote: "If you elect to manage your own shipping (Seller-Managed Shipping), you must add the shipping costs to the listing form." Or Chairish-managed: "Parcel Delivery: You will receive a pre-paid shipping label from Chairish. However, you are responsible for packing and any costs associated with packing." Large items go to "In-home Shipping: Chairish manages the selection, booking, and payment to the shipper."
- Payment holding, which is the pattern to copy: "Chairish collects payments from buyers at the time of sale and holds the proceeds until confirmation that the item has been picked up (local pickup) or delivered safely." "Sales are considered final after the 48-hour return period elapsed." "Payment typically appears in your account approximately 6 days after the sale is closed."
- Tax: "Taxes paid by the buyer will not be passed to the seller, as they are collected and remitted by Chairish."
- Damage: "If an item suffers irreparable damage in transit, we may close the order, issue a full refund to the buyer, and release your payment after the claim is resolved." Claim evidence: "Claims cannot be filed without packaging and label photos."
- Steal this: the payout-hold timeline (delivery confirmed + 48 h + ~6 days) and the "photos of box, label, and damage or no claim" rule.
- Not read here: Chairish's own consign/pickup program and commission (sibling agent b2 covers those).

### eBay
- Homepage: https://www.ebay.com/
- Pages read: https://www.ebay.com/help/policies/selling-policies/drop-shipping-policy?id=4176 ; https://www.ebay.com/help/policies/member-behaviour-policies/user-agreement?id=4259 ; https://www.ebay.com/sellercenter/resources/tax-information (accessed 2026-10-27)
- Drop shipping page: "Dropshipping... is when you buy stock from a supplier and work with them to send items directly to your buyers without ever handling them yourself." It is allowed, but "you're still responsible for the safe delivery of the item." And: "listing an item on eBay and then purchasing the item from another retailer or marketplace that ships directly to your customer is not allowed."
- Read carefully: that page covers wholesale suppliers (allowed) and retail arbitrage (banned). An owner holding their own vintage item and shipping it for you is neither, so the page does not address consignor-held inventory. Any claim that "eBay allows/bans it" is unsupported.
- User Agreement: "The eBay Payment Entities will collect the transaction amount on behalf of the seller." On access: "If you require that authorized third parties (employees, agents, etc.) have access to your account we offer a Multi-User Account Access... program for that purpose." So if H&V ever lists on an owner's eBay account, use that program, not shared passwords.
- Tax page: "In such cases, eBay collects and remits Internet Sales Tax on your behalf." Florida appears in the page's state list. The page also says "You are responsible for paying all fees and taxes associated with using eBay as an eBay seller" (income taxes stay with the seller).
- Watch out: the buyer's recourse is against the listing seller. If H&V's account is the seller, H&V answers for a shipment it does not control.

### Etsy (highest risk for hold-and-ship)
- Homepage: https://www.etsy.com/
- Pages read: https://help.etsy.com/hc/en-us/articles/360024112614-What-Can-I-Sell-on-Etsy ; https://help.etsy.com/hc/en-us/articles/23948763872151-Does-Etsy-Allow-Drop-Shipping-or-Reselling ; https://help.etsy.com/hc/en-us/articles/360000343968-How-US-State-Sales-Tax-and-Fees-Applies-to-Etsy-Orders (accessed 2026-10-27)
- WALLED (4 bytes, not read): https://www.etsy.com/legal/sellers/ (Seller Policy) and https://www.etsy.com/legal/handmade (Creativity Standards). I did not check any explicit consignment clause there, so I cannot say Etsy "bans consignment."
- What the help text says: "Everything listed for sale on Etsy must either be made, designed, handpicked or sourced by you." Vintage is allowed: "Vintage items: Breathe new life into unique, handpicked items that are over 20 years old." (90s fashion clears the 20-year bar.)
- The trap: "Drop shipping is not allowed on Etsy, with the limited exception of Craft and Party Supplies." Defined as "selling ready-made products that are shipped directly from a third-party supplier to the customer." Vintage is exempt from the reselling ban, not from the drop-shipping ban. An owner shipping straight to the buyer fits that definition on a plain reading.
- Verdict: ship-to-us (H&V holds and curates the item) fits "handpicked by you." Hold-and-ship under H&V's Etsy shop is high risk. Option (a), where the owner lists their own vintage on their own Etsy shop, is outside H&V's shop entirely.
- Tax: "Etsy automatically calculates, collects, and remits US sales tax on behalf of sellers." "Sellers can't opt out of Etsy automatically collecting sales tax." The state list includes "Florida, as of 07/01/2021".

### Poshmark
- Homepage: https://poshmark.com/
- Page read: https://poshmark.com/posh_guide/how_to_ship (accessed 2026-10-27)
- Seller holds the item and ships it: "The email will include instructions and your pre-paid, pre-addressed shipping label."
- UNVERIFIED: Poshmark's terms fetch returned 0 bytes, so I have no first-party page for its tax handling, seller-of-record language, or any "must own/possess the item" rule. Do not assume.

### Depop
- Homepage: https://www.depop.com/
- Page read: https://depophelp.zendesk.com/hc/en-gb/articles/360012516318-State-Sales-Tax-in-the-US (accessed 2026-10-27)
- "Depop automatically calculates, collects, and remits US sales tax on behalf of sellers... when an order is sent to a recipient in the US." Florida appears in the page's state table.
- Not found: any rule on selling items you do not possess.

### Mercari
- Homepage: https://www.mercari.com/
- Page read: https://www.mercari.com/us/help_center/article/467/ (accessed 2026-10-27)
- "Mercari calculates, collects, reports, and remits applicable sales tax on behalf of our third-party sellers under Mercari's registered sales tax identification numbers." "Sellers cannot opt-out."
- Discrepancy: Florida is NOT named on this page, while Etsy, eBay, Whatnot, and Depop pages name it. Mercari/Florida: need review.
- Not found: any possession rule.

### Whatnot
- Homepage: https://www.whatnot.com/
- Pages read: https://help.whatnot.com/hc/en-us/articles/360061196012-U-S-Sales-Tax-Collection-on-Whatnot ; https://help.whatnot.com/hc/en-us/sections/4417226792333-Seller-Policies (accessed 2026-10-27)
- "Where required in the states and territories of the U.S., Whatnot collects sales taxes on behalf of sellers... sellers on Whatnot are not required to collect or remit sales tax on their transactions." Florida is in the list.
- The Seller Policies index is a list of category policies (supplements, coins, wholesale, food, knives, cards, and so on). I did not find a rule about owning or possessing the item. Not checked in the individual policy pages.
- Fit: live-selling wants an item in hand on camera. Hold-and-ship does not fit Whatnot.

---

## 3. "We list it, you ship it": real services and what their published terms say

| Service | Who ships to whom | Evidence | Status |
|---|---|---|---|
| eBay Consignment (2023 launch, luxury) | Owner ships to eBay's consignment partner (Linda's Stuff) | eBay press release, Sep 12, 2023: "users direct access to expert sellers who will list and sell their luxury items on their behalf"; "the customer will be provided with a prepaid, insured shipping label." URL: https://www.prnewswire.com/news-releases/ebay-launches-luxury-consignment-301924083.html | Ship-to-them, not hold-and-ship. The "20-40%" commission appears only in Offload's blog (third party, discloses its own bias); the press release does not state it. Need review. |
| eBay Trading Assistants (older program) | Owner drops items off | eBay page: "Trading Assistants can sell items on eBay for others. Trading Assistants operate independently as eBay sellers, and are not employees, agents or partners of eBay." "You and the Trading Assistant are responsible for negotiating all terms." URL: https://pages.ebay.com.my/tradingassistants/questions.html | The page is on eBay's Malaysia domain and is still served. Offload says eBay "retired its Trading Assistant program... years ago." Page live vs claimed retired: need review. Useful precedent: eBay itself accepted "seller sells for others, owner is not eBay's problem." |
| Offload (AI selling agent) | Owner keeps the item; "You ship when it sells." | https://offload.market/blog/hire-someone-to-sell-on-ebay : "One photo; the AI agent writes, prices, lists, and negotiates, with a floor price you control... Subscription + marketplace fees." | A real hold-and-ship listing service, subscription priced. Vendor blog, so treat as marketing. I did not read its terms. |
| Human consignment / tasker on eBay | Varies | Offload claims "30-50 percent after eBay fees" and price minimums | Single biased source. Unverified. |
| Vestiaire Collective Direct Shipping | Seller ships straight to buyer | https://faq.vestiairecollective.com/hc/en-us/articles/360006739537-Seller-Direct-Shipping : "the buyer receives their item directly from you, the seller, rather than having their items physically checked." Only US-to-US (also Australia, Switzerland), items "less than $1000 USD"; the seller "cannot opt out." | Platform feature, not a shop-for-hire. Shows the model is normal at the marketplace level, capped by price. |
| Chairish seller-managed shipping | Owner ships | see section 2 | Same note. |
| Shopify Collective | Supplier ships, revenue splits | Shopify blog: "allows a store to sell another Shopify business's products directly from its storefront. Orders are routed to the supplier for fulfillment and revenue splitting. It's free for eligible stores." URL: https://www.shopify.com/blog/multi-vendor-marketplace | Needs the other party to be a Shopify business. A private owner clearing out a closet is not. Doesn't fit (inference). |

Blunt read: I found no retail "we list it, you ship it" shop with published consignor terms. The real examples are marketplaces (owner is the seller), an AI service (Offload), and eBay's own consignment (ship-to-them). Hold-and-ship for a branded shop is something you would be inventing, not copying.

---

## 4. Software that supports commission splits and consignor-held inventory

### Shopify multi-vendor apps
- Homepage: https://www.shopify.com/ ; page read: https://www.shopify.com/blog/multi-vendor-marketplace (accessed 2026-10-27)
- Blog: "A multivendor marketplace is an ecommerce website where multiple independent sellers list and sell products... The marketplace platform owner doesn't handle inventory management or order fulfillment for the sellers." Apps "generally handle... individual vendor dashboards, automated order routing and splitting... commission calculation, and vendor payouts." Named examples: Webkul's Multi Vendor Marketplace, Shipturtle.
- CollabPay (https://apps.shopify.com/collabpay): "Calculate and distribute commissions easily, with payouts via PayPal, Stripe, or bank"; the listing mentions consignment. Pricing was not captured (UNVERIFIED).
- **Discrepancy: Shopify promotes multivendor apps, but the Shopify Payments Terms (https://www.shopify.com/legal/terms-shopify-payments, section 16 "Restricted Use") say you shall not "(ii) submit any Transaction that does not arise from your sale of goods or service to a customer; (iii) act as a payment intermediary or aggregator or otherwise resell the Payments Services on behalf of any third party."** Consignment where H&V is the seller (H&V sells, later pays the owner from its own bank) is verified as compatible with the plain wording. A vendor-as-seller marketplace running through Shopify Payments needs Shopify's written confirmation. Do not auto-route consignor money through Shopify Payments.
- Shopify TOS (https://www.shopify.com/legal/terms): "any contract of sale made through the Services is directly and only between you and the customer. You are the seller or merchant of record for all sales through the Services. You are responsible for... the goods and services that you may sell... This includes... determining and collecting taxes, refunds, returns, fulfilling any sales or customer service, fraudulent transactions." So on Shopify, H&V is the merchant of record for everything, even if the owner ships. I keyword-searched the TOS and found no clause about listing another person's goods; I did not read the whole document.

### Stripe Connect (verified on Stripe's own docs)
- Homepage: https://stripe.com/ ; pages read: https://docs.stripe.com/connect/charges ; https://docs.stripe.com/connect/merchant-of-record ; https://docs.stripe.com/connect/disputes ; https://docs.stripe.com/connect/risk-management ; https://docs.stripe.com/connect/identity-verification ; https://stripe.com/connect/pricing (accessed 2026-10-27)
- Charge types. Destination charges: "Customers transact with your platform for products or services provided by your connected accounts... Refunds and chargebacks reduce your platform's balance." Direct charges: customers "are often unaware of your platform's existence... Refunds and chargebacks reduce the connected account's balance." Separate charges and transfers: "split funds between multiple connected accounts, or hold them"; "You can create a charge before being able to transfer the funds." That last one matches "hold payout until the return window closes."
- Platform fees: with direct charges "You can specify an application fee"; with destination charges "The portion of the funds that remains in your platform balance represents the fee you charge your connected account."
- Merchant of record: "The MoR is the entity that the customer understands they're buying from. It's also the business that's responsible for the transaction and for providing customer recourse in scenarios such as refunds and disputes... Don't base it on the charge type or payment configuration." On an H&V-branded site, H&V is the MoR no matter who ships.
- Disputes: for indirect charges the "Balance debited for the disputed amount" is the "Platform's balance." Risk page: "Your platform is always responsible for its own negative balances."
- KYC for sellers: "Collecting information about the individual or company receiving funds; Verifying information to establish that we know who our customers are." A US company might need business name, address, tax ID, the account opener's name and date of birth, and beneficial owners. "Stripe temporarily pauses charges or payouts if the information isn't provided or verified." Also: "Don't rely on Stripe's verification to meet any independent legal KYC or verification requirements." Each consignor would have to complete Stripe onboarding.
- Pricing: under "You handle pricing for your users": "$2 per monthly active account" (active = payouts sent that month) plus "0.25% + 25¢ per payout sent." Under "Stripe handles pricing for your users": "No fees for your platform." I did not fetch Stripe's base card pricing, so the card-processing rate is not quoted here.
- Verdict: gimmick at this scale. Every consignor needs KYC onboarding, H&V still eats refunds and chargebacks, and the build is custom (the H&V site is hand-coded). A monthly Zelle/ACH/check payout from H&V's own bank is the sane version until volume proves otherwise.

### ConsignCloud
- Homepage: https://consigncloud.com/ ; pages read: https://consigncloud.com/pricing ; https://consigncloud.com/features/sell-online ; https://help.consigncloud.com/en/articles/3212864-integrating-consigncloud-with-shopify (accessed 2026-10-27)
- Real product. "Shops that sell items for consignors, paying them a split once the item sells." Store-type tile "Online-Only: Web-based stores that sell through Shopify or Square."
- Online: "Sync your inventory to Shopify or Square... let ConsignCloud keep every item, split, and balance up to date." Shopify sync: "If an item is sold in Shopify, it will be marked as sold in ConsignCloud and the consignor's balance history will be updated." Built for one-offs: "built primarily for consignment stores, which most often deal with unique items with a quantity of '1'."
- Price: Basic $139/month (unlimited items, "Shopify & Square Integrations", "ACH Payouts ($2.50/payout)"); Pro $189/month per location (adds "Consignor Portal"). The help page says "Shopify itself costs $29/mo"; that figure is secondhand (ConsignCloud's page, not Shopify's), so verify at Shopify.
- Does it support consignor-held inventory? Not documented. The only "different fulfillment location" item is about Shopify multi-location Shelves, not inventory at a consignor's home. It is built around in-store intake. Etsy sync not shown on the pages I read.

### Ricochet
- Homepage: https://www.ricoconsign.com/ ; pages read: https://www.ricoconsign.com/pricing ; https://www.ricoconsign.com/integrations (accessed 2026-10-27)
- Real product. Plans: Core $99/month (RicochetPay "3.29% + 10¢"), Reach $149/month ("eCommerce add-on included"; 2.99% + 10¢), Lead $199/month (adds "Vendor/Consignor support"; 2.69% + 10¢). Keeping another card processor means "a monthly non processing fee of $100" on Lead or Custom.
- Its Consignor Portal blurb is aimed at booth/vendor shops ("Give vendors access to add their own inventory, automate rent payments, and streamline payouts"). It documents vendors entering inventory, not consignor-held shipping. I did not read the eCommerce ("Ricochet Web") detail pages, so whether it syncs to Shopify or Etsy is UNVERIFIED.

**Neither ConsignCloud nor Ricochet documents consignor-held inventory; both assume the shop takes the goods in.** For H&V they are ledger tools (items, splits, consignor balances, payout reports), not hold-and-ship enablers. At $99-$189/month, wait until there are enough consignors that a spreadsheet hurts.

---

## 5. Florida sales tax (assumption: H&V is Florida-based; research, not legal advice; confirm with a CPA)

Sources: Florida Statutes 212.05965 and 212.0596 on the official Online Sunshine site (http://leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0200-0299/0212/Sections/0212.05965.html and ...0212.0596.html); Florida Administrative Code rules 12A-1.103 and 12A-1.081 (Department of Revenue rules, read via the eLaws mirror https://flrules.elaws.us/fac/12a-1.103 and .../12a-1.081, "Last Updated: March 7, 2026"). Florida DOR homepage: https://floridarevenue.com/. DOR's own explainer (https://www.floridarevenue.com/taxes/Documents/dr1mp.pdf) was walled (4 bytes), so the rule text came through a third-party mirror. All accessed 2026-10-27.

- Definition: F.S. 212.05965(1)(b): a "marketplace provider" is "a person who facilitates a retail sale by a marketplace seller by listing or advertising for sale by the marketplace seller tangible personal property in a marketplace and who directly, or indirectly through agreements or arrangements with third parties, collects payment from the customer and transmits all or part of the payment to the marketplace seller, regardless of whether the marketplace provider receives compensation." The definition excludes "a payment processor business" (so Stripe or Shopify Payments do not take on the duty). It reads literally on an H&V site that lists an owner's item, takes the buyer's payment, and forwards part to the owner.
- Dealer status: subsection (2): a marketplace provider "that has a physical presence in this state or who is making or facilitating... a substantial number of remote sales... is a dealer." Subsection (4)(b)1: a marketplace seller with a physical presence in Florida "shall register and shall collect and remit the tax... on all taxable retail sales made outside of the marketplace." The $100,000 threshold (212.0596(1)(b)) applies to remote sellers; do not treat it as a safe harbor for a Florida-based shop.
- Consignment rule: 12A-1.081: "Where merchandise is delivered to a dealer on a consignment basis, the tax shall be collected and remitted by the consignee, not the consignor." This rule dates from 1972 and speaks to merchandise delivered to the dealer. In hold-and-ship nothing is delivered to H&V, so this rule does not squarely decide it. The marketplace-provider text from 2021 is the better fit for the own-site case.
- Practical read: on an H&V-owned checkout (Shopify or the custom site), plan on H&V collecting and remitting Florida tax on every sale, including consigned items the owner ships. On Etsy, eBay, Whatnot, and Depop, the platform collects and remits "on behalf of sellers," so the tax question disappears for sales made there.
- Not researched: 1099 reporting on consignor payouts (sibling agent b5 has IRS 1099-K and Florida secondhand material), local surtaxes, resale certificates, and the legal status of the consignment agreement itself.

---

## 6. The two legitimate hold-and-ship setups, and what the consignor agreement must say

### Setup (a): "listing service," the owner stays the seller
- The owner's name is on the Chairish / eBay / Etsy account. H&V does photos, copy, and pricing, and is paid a flat fee or percent by the owner, outside the platform.
- Wins: no title, no merchant-of-record role, no sales-tax duty, buyer protection and tax handled by the platform. H&V carries almost no inventory risk.
- Watch out: on eBay use Multi-User Account Access (User Agreement), not shared logins. Whether the platforms accept an off-platform percentage arrangement is UNVERIFIED (I found nothing either way). Etsy is fine only because the owner lists their own vintage.

### Setup (b): H&V's own site sells, the owner ships
- H&V is the merchant of record (Shopify TOS, Stripe MoR doc) and, on the statute's wording, a Florida marketplace provider. The buyer's recourse is against H&V.
- The consignor agreement should cover (all need an attorney):
  1. Ship-by window (for example 2 business days) using a prepaid label bought by H&V.
  2. A packing standard, plus photos of the box, label, and item before sealing. This is the Chairish evidence rule: "Claims cannot be filed without packaging and label photos."
  3. Who bears loss when packing fails. Default: consignor, deducted from the payout.
  4. Payout held until the return window closes. Chairish: delivery confirmed, 48 h, then about 6 days.
  5. Chargeback and refund clawback if the consignor was already paid. UNVERIFIED how Stripe transfer reversals work (not read).
  6. Item-condition and authenticity warranty, and the owner's confirmation that they own the item free of liens.
  7. A kill-switch: H&V can pull the listing at any time, and a no-ship penalty.
- The operational problem, bluntly: H&V can't photograph the packing, can't inspect condition before the buyer sees it, and can't fix a bad box. For $20 ephemera that doesn't matter. For a $600 lamp it matters a lot.

---

## 7. Decision table (ratings are my judgment, not sourced figures)

| | Ship-to-us (consign) | Hold-and-ship | Buy outright |
|---|---|---|---|
| Effort for H&V | Med: intake, storage, photos, ledger | Med-High: chasing owners, packing disputes, payout holds | Low per item once bought: you own it and control photos and shipping |
| Risk | Med: inventory sits unsold, consignor disputes | High: merchant of record without possession; damage and condition unknowns | Med: you eat unsold stock, but you control everything |
| Cash needed | Low (no purchase) | Lowest (no purchase, no storage) | High (you pay before it sells) |
| Speed to list | Slow: wait for shipment and photos | Fast to list, slower to deliver (ship-by window) | Fast: you have it in hand |
| Platform fit | Works on Etsy ("handpicked by you"), eBay, own site | Etsy high risk; eBay not addressed; own site OK if H&V is MoR; Chairish OK with owner as seller | Works everywhere |
| Best item types | Small high-value pieces: signed ephemera, Playboys, jewelry and accessories, small glass and barware, anything where H&V controls photos and authentication | Large or fragile pieces where freight is the cost: furniture, big lighting, framed art. Best on Chairish (owner sells, Chairish-managed shipping) or via a listing-service fee | Sure-thing pieces with clear comps and fast turn: well-known 70s-90s fashion, brass and glass lamps with known demand |

---

## 8. Ranked recommendations for Holliewood and Vine

1. **Default to ship-to-us for anything under a couple hundred dollars.** It is the only version that fits Etsy's text and keeps photos, authentication, and packing under H&V's control. The Florida consignment rule (12A-1.081) then applies directly.
2. **Buy outright the sure things.** Cash-heavy but the cleanest legally; no consignor, no payout clock, no title question.
3. **Treat hold-and-ship as an exception for big or fragile items,** and prefer setup (a): the owner lists on Chairish with Chairish-managed shipping and pays H&V a listing fee. Chairish handles tax, payment holding, and damage claims. H&V never becomes the merchant of record.
4. **If you do setup (b), do it only on H&V's own site,** not Etsy. Use the clauses in section 6, hold payouts until the return window closes, and have a CPA confirm that H&V collects Florida tax.
5. **Skip Stripe Connect and Shopify multi-vendor apps for now.** Per-consignor KYC, chargeback exposure that stays with H&V, and the Shopify Payments Terms intermediary clause all make it a bad trade at this scale.
6. **Don't buy ConsignCloud ($139/mo) or Ricochet ($99/mo) yet.** A spreadsheet with item ID, consignor, split, status, and payout date covers the first dozen consignors. Revisit when payouts become a monthly chore. ConsignCloud's Shopify sync is the better fit for H&V's stack.
7. **Ask in writing before relying on any platform gray area:** Etsy support on consigned vintage and owner-shipped orders; eBay on listing a consignor's item; Shopify on Payments Terms section 16 with a consignment payout flow.

---

## 9. Blocked, unverified, and "need review" list

- WALLED (not read): Etsy Seller Policy (https://www.etsy.com/legal/sellers/) and Etsy Creativity Standards (https://www.etsy.com/legal/handmade); Florida DOR's dr1mp.pdf; Poshmark terms (0 bytes, background fetch hung).
- UNVERIFIED: Poshmark tax and possession rules; Whatnot "must own the item" rule (only the policy index was read); Depop and Mercari possession rules; CollabPay pricing; Ricochet eCommerce / Shopify sync; transfer-reversal mechanics on Stripe; Stripe base card rates (stripe.com/pricing not fetched); whether platforms accept an off-platform percentage fee to an agent; 1099 reporting on consignor payouts (see sibling b5); out-of-state sales-tax nexus on own-site sales.
- NEED REVIEW (sources disagree or conflict):
  - Shopify blog promotes multivendor apps vs Shopify Payments Terms section 16(iii): consignment with H&V as seller is verified as compatible; vendor-as-seller on Shopify Payments needs Shopify's confirmation.
  - eBay Trading Assistants: the Malaysia-domain FAQ is still live; Offload says the program was retired. Needs review.
  - eBay Consignment commission "20-40%" appears only in Offload's blog; eBay's press release gives no number.
  - Mercari's sales-tax page does not name Florida; the other platform pages do.
  - FL Rule 12A-1.081 (1972, goods "delivered to a dealer") vs F.S. 212.05965 (2021, marketplace provider) on goods that never reach H&V: needs a CPA's read.
  - The $29/month Shopify price came from ConsignCloud's help page, not Shopify.
- Visuals: this report cites text only; I did not view any rendered page.

## 10. Source files (raw, in `research/consignment/raw/`)
`b4-chairish-who-pays-shipping.md`, `b4-chairish-seller-payment.md`, `b4-chairish-lost-damaged.md`, `b4-ebay-dropshipping-policy.md`, `b4-ebay-user-agreement.md`, `b4-ebay-tax-info.md`, `b4-ebay-luxury-consignment-pr.md`, `b4-ebay-trading-assistants-faq.md`, `b4-etsy-what-can-i-sell.md`, `b4-etsy-dropship-reselling.md`, `b4-etsy-sales-tax.md`, `b4-poshmark-how-to-ship.md`, `b4-depop-sales-tax.md`, `b4-mercari-sales-tax.md`, `b4-whatnot-sales-tax.md`, `b4-whatnot-seller-policies.md`, `b4-vestiaire-direct-shipping.md`, `b4-offload-hire-ebay.md`, `b4-shopify-multivendor-blog.md`, `b4-shopify-collabpay.md`, `b4-shopify-payments-terms.md`, `b4-shopify-tos.md`, `b4-stripe-connect-charges.md`, `b4-stripe-connect-mor.md`, `b4-stripe-connect-disputes.md`, `b4-stripe-connect-risk.md`, `b4-stripe-connect-identity.md`, `b4-stripe-connect-pricing.md`, `b4-consigncloud-home.md`, `b4-consigncloud-pricing.md`, `b4-consigncloud-sell-online.md`, `b4-consigncloud-shopify-help.md`, `b4-ricochet-home.md`, `b4-ricochet-pricing.md`, `b4-ricochet-integrations.md`, `b4-fl-stat-212-0596.md`, `b4-fl-stat-212-05965.md`, `b4-fl-rule-12a-1-103.md`, `b4-fl-rule-12a-1-081-consignment.md`. Empty/walled files: `b4-etsy-seller-policy.md`, `b4-etsy-creativity-standards.md`, `b4-fl-dor-dr1mp.md`, `b4-poshmark-terms.md`.
