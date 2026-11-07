# Lane 13: eBay's own photo tooling and photo rules

Status (2026-11-07): ebay.com, pages.ebay.com, community.ebay.com, export.ebay.com, innovation.ebayinc.com, developer.ebay.com, ebayinc.com all returned "CONNECT tunnel failed, response 403" on a curl test. tools/crawl-cloud.sh failed (exit 1, under 1 KB) on ten pages: eBay Seller Center 2024-october tools, eBay community bulk-listing announcement, two innovation.ebayinc.com stories, chainstoreage, valueaddedresource (2 pages), flipsail, nightjar, masonry. The stubs are in raw/13-disc-ebay-ai/ (each holds only the error). techcrunch, shopifreaks, apiway, smallbusinessxchange, 3dsellers and hulkapps are also refused. Five WebSearch (extended) queries ran. Nothing in this run reached VERIFIED_FETCHED. The only VERIFIED_FETCHED facts below are from the 2026-10-30 capture in research/ebay-clothing-photos-2026-10-30/ (fetched by crawl4ai, source URL on line 1), re-read today and quoted from the saved files.

## Already known (2026-10-30 folder, not new)
Up to 24 pictures, main photo face-on and shown in search, 1600 x 1600 recommended, 500 x 500 minimum, 1:1 or 16:9, neutral backdrop with white generally best, no flash, no watermarks, no stock photos for used. See that folder's README. Not repeated below except where it answers this lane.

## New findings

1. eBay's own background tool, exact steps. VERIFIED_FETCHED (2026-10-30 capture, research/ebay-clothing-photos-2026-10-30/photo-tips.md, source https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148). Web: "Select the Background icon to automatically replace the background with a solid white color." App: "Choose White, to change the background to a solid white color. Or, choose from the AI-Generated backgrounds, Studio, Surface, and Outside", with "Edit scene" and "Generate more". This is the only eBay-owned tool statement we hold in full; the page also says "Our photo uploader can take images up to 12MB in size" (new vs. the README, which omitted the 12 MB cap).

2. Picture policy list of disallowed items. VERIFIED_FETCHED (2026-10-30, picture-policy.md, source https://www.ebay.com/help/policies/listing-policies/picture-policy-ebay-pictures-policy?id=4370): "Photos that don't accurately represent the item", "Placeholder images used to convey messages", "Stock photos for used, damaged, or defective items", "Photos with added borders", "Photos with added text, artwork or marketing material", "Watermarks of any type, including those used for ownership attributions". Also "at least one photo that is 500 pixels on the longest side". The policy text says nothing about AI or editing. Note the phrase "ownership attributions": even a small shop-name mark is out.

3. Stock-photo rule wording. VERIFIED_FETCHED (photo-tips.md, same page as 1): "You can't use a catalog or stock photo if you're listing an item as used."

4. Mannequin statement. VERIFIED_FETCHED (negative): grep of all twelve saved 2026-10-30 pages finds no eBay sentence on mannequins, dress forms or models. The only mannequin evidence is the README's live listing (a Gunne Sax dress on a mannequin, $450, 42 watchers), which is a seller example, not eBay guidance. SEARCH_SNIPPET: a search result summary claims eBay's own tips say to show fit with "a model, dress form, or mannequin" (likely https://export.ebay.com/en/first-steps/manage-listings/photo-tips/ or the Seller Center selling-clothes page). That wording is not in our saved selling-clothes.md or sellercenter-photo-tips.md, so it is UNCONFIRMED until the export.ebay.com page is fetched.

5. App AI scene backgrounds and iOS availability. SEARCH_SNIPPET (source https://innovation.ebayinc.com/stories/background-swap-tool-turns-any-photo-into-a-studio-quality-product-image/ and https://chainstoreage.com/ebay-enables-ai-based-mobile-seller-photo-enhancement): launched 2024, "available to iOS app users in the U.S., U.K., and Germany" with Android to follow. White-background removal "since 2020" is also snippet-level. Ricky has an iPhone, so the AI scenes are in reach. The web tool offers white only (finding 1).

6. Magical Listing (AI listing from photos). SEARCH_SNIPPET (sources https://innovation.ebayinc.com/stories/ebay-reduces-the-time-to-list-on-mobile-with-new-simplified-selling-tool-now-featuring-magical-listing-ai-technology/ , https://community.ebay.com/t5/Announcements/List-faster-and-easier-with-our-magical-AI-powered-bulk-listing/ba-p/34685758/): a single-listing flow in the eBay app and a bulk version in Seller Hub that drafts categories, titles and item specifics from photos, "currently available to US sellers across all categories". Third parties disagree on whether it also drafts price and shipping. TechCrunch (snippet) reports a disclaimer that text may be inaccurate. A February 2026 claim that eBay rebuilt the app flow around AI is from a vendor blog and UNVERIFIED.

7. eBay altering seller images with AI. SEARCH_SNIPPET (sources https://www.valueaddedresource.net/ebay-tests-ai-fashion-models-alters-images/ , https://www.valueaddedresource.net/ebay-images-altered-by-ai-without-knowledge/ , https://www.shopifreaks.com/ebay-is-testing-ai-generated-fashion-model-images-and-inserting-them-into-seller-listings-without-permission/): reports that eBay tested AI fashion model images inserted into listings without seller consent, and one seller found a changed collar. Not seen on a fetched page; dates unknown. Relevant to vintage: check the live listing after publishing.

8. AI-edited photos and disclosure. SEARCH_SNIPPET, vendor blogs that sell AI photo tools (https://nightjar.so/blog/ebay-product-photography-listing-requirements , https://masonry.so/blog/ebay-ai-product-photos-rules): "eBay does not prohibit AI-generated or AI-edited listing photos as a category", no per-photo AI disclosure rule as of August to September 2026, and the User Agreement places accuracy responsibility on the seller. Treat as secondary. Our own fetched policy (finding 2) supports the accuracy angle only.

9. Ghost-mannequin editing. No eBay rule found. My inference (UNVERIFIED): removing the form digitally is a heavy edit that is safest only if the garment shape stays true and the original on-form shot is also included.

10. Used clothing policy exists at https://www.ebay.com/help/policies/prohibited-restricted-items/used-clothing-policy?id=4281 (SEARCH_SNIPPET): about cleanliness and listing language, not photo setup.

11. No Reddit threads on eBay's own tools surfaced; no eBay "photo quality nudge" statement was found in any source. UNVERIFIED that such a nudge exists.

## Recommendations for Ricky
- Shoot the real garment on the real vintage form for every listing; put the on-form, white-background shot first, then back, label, flaws and close-ups. This sits inside every rule we hold in full text.
- Never use AI to change the garment (color, collar, drape, flaws). Whiteout and light cleanup of the backdrop are the safe zone. Do not generate a model wearing it as the main photo.
- Export 1600 x 1600 (square) JPEG under 12 MB, no border, no text, no mark of any kind including a small logo.
- Use eBay's own white-background button as the fallback and benchmark for the local pipeline; compare the two on one dress before trusting either.
- After publishing, open the live listing and confirm the photos are unaltered.

## Open questions
- Does any current eBay page say "model, dress form, or mannequin"? Needs the export.ebay.com page.
- Is the AI scene tool still iOS-first, and does 2026 Seller Hub add photo-quality scoring?
- How strictly does eBay enforce "accurately represent" on edited backgrounds with shadows removed?

## URLs to fetch when the network opens
- https://export.ebay.com/en/first-steps/manage-listings/photo-tips/ and https://export.ebay.com/en/first-steps/manage-listings/the-perfect-clothing-ad/ : confirm or kill the mannequin sentence (finding 4).
- https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148 : re-fetch to catch 2026 changes to the background tool.
- https://www.ebay.com/help/policies/listing-policies/picture-policy-ebay-pictures-policy?id=4370 : re-check for AI wording.
- https://www.ebay.com/help/policies/member-behavior-policies/user-agreement?id=4259 : the generative-AI clause (finding 8).
- https://www.ebay.com/help/policies/prohibited-restricted-items/used-clothing-policy?id=4281 : full text.
- https://innovation.ebayinc.com/stories/background-swap-tool-turns-any-photo-into-a-studio-quality-product-image/ : launch details and availability.
- https://innovation.ebayinc.com/stories/ebay-reduces-the-time-to-list-on-mobile-with-new-simplified-selling-tool-now-featuring-magical-listing-ai-technology/ : Magical Listing scope.
- https://community.ebay.com/t5/Announcements/List-faster-and-easier-with-our-magical-AI-powered-bulk-listing/ba-p/34685758/ : bulk tool.
- https://www.ebay.com/sellercenter/resources/seller-updates/2024-october/tools : eBay's AI tool list.
- https://www.valueaddedresource.net/ebay-tests-ai-fashion-models-alters-images/ and https://www.valueaddedresource.net/ebay-images-altered-by-ai-without-knowledge/ : dates and facts for finding 7.
- https://community.ebay.com/forum/selling-57920/topic/ai-clothing-model-cover-photo-152705/ and https://community.ebay.com/t5/Selling/Listing-Clothes-How-to-take-proper-pictures/td-p/34490503 : seller experience with AI models and mannequins.
