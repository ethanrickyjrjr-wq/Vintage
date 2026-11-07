# Lane 16: eBay community forum discussions (clothing sellers, mannequins, white backgrounds, photo tools)

Status (2026-11-07): community.ebay.com is BLOCKED. curl returned "CONNECT tunnel failed, response 403" (tested once on the root and once on a thread URL), and tools/crawl-cloud.sh wrote 0 bytes, http 0, same 403. Zero threads were fetched, so nothing here is VERIFIED_FETCHED. Everything below is SEARCH_SNIPPET from 10 WebSearch extended queries (site:community.ebay.com). The search tool paraphrases the snippets; quoted fragments are as the tool returned them and must be re-checked on the real page. Nothing was saved under raw/16-disc-ebay-community/ because there was nothing to save.

## Thread list (all SEARCH_SNIPPET, all to fetch once the host opens)

1. https://community.ebay.com/t5/Selling/Selling-clothing-Flay-lay-vs-Mannequin/td-p/32565924 : seller reports flat-lay items outselling mannequin items ("my sample size is somewhat limited"). Fetch: the closest thing to sell-through evidence on mannequins.
2. https://community.ebay.com/t5/Selling/Using-a-mannequin-to-display-clothing-for-resale-Dated/td-p/32785890 (and /page/2) : "Dated?" debate; form must match the garment's sex and size; a big bust makes buyers think the item is stretched. Fetch: both pages, the main mannequin thread.
3. https://community.ebay.com/t5/Archive-Clothing-Shoes/Mannequins-to-help-photograph-clothes-Inexpensive-Any-good/td-p/17444521 : cheap forms, hanging torsos, headless half-body forms, spray-painted used mannequins. Fetch: sourcing ideas (old, so prices stale).
4. https://community.ebay.com/t5/Selling/Do-the-quality-of-photos-really-matter-or-matter-enough-based-on/td-p/34960307 : clothing seller says many sell on flat lays on gray or off-white carpet with good sell-through; others say photos are the number one thing for clothes. Fetch: counterview on effort vs return.
5. https://community.ebay.com/t5/Selling/Less-than-6-photos-affect-search-impressions-per-Listing-Quality/td-p/32120944 : Listing Quality Report line "listings with the most impressions in eBay search in this category have 6 photos"; replies disagree on whether photo count affects placement. Fetch: the only thread on photos vs search.
6. https://community.ebay.com/t5/Selling/Ebay-Search-Rank-Facts-or-Fiction/td-p/27835269 : Best Match uses "dozens if not hundreds" of factors; no confirmed photo factor. Fetch: for skepticism baseline.
7. https://community.ebay.com/forum/selling-57920/topic/ebay-forcing-white-background-on-images-looks-terrible-sitewide-111796/ : eBay adds white panels to non-square thumbnails; keep photos 1:1 to avoid it. Fetch: matters directly for our square-crop output.
8. https://community.ebay.com/t5/Selling/eBay-Changing-White-Backgrounds-in-Search-MAKING-THEM-GRAY/td-p/33812316 (page 3 seen) : eBay tinting white backgrounds gray in search. Fetch: affects how pure-white cutouts look.
9. https://community.ebay.com/t5/Selling/eBay-please-stop-darkening-photo-backgrounds/td-p/34327934 : same darkening complaint, view-dependent. Fetch: check whether it still happens.
10. https://community.ebay.com/t5/Selling/Photos-being-degraded-by-Ebay-adding-light-gray-overlay/td-p/34351272 : light gray overlay degrading photos. Fetch: same issue, find workarounds.
11. https://community.ebay.com/t5/Selling/Do-we-need-a-white-background-for-Google-No/td-p/33591480 : argues white is not required for Google Shopping. Fetch: policy claim to verify.
12. https://community.ebay.com/forum/selling-57920/topic/photo-back-ground-is-white-needed-156571/ : is white required; replies cite eBay saying uncluttered background, white generally best, dark may suit shiny items. Fetch: most recent look at the question.
13. https://community.ebay.com/t5/Selling/Ebay-s-Background-Removing-Tool-Greatly-Improved/td-p/33965767 : seller says the in-app remover is much better than before, not on all pictures. Fetch: how good is the built-in tool.
14. https://community.ebay.com/t5/Selling/Background-Remover-is-distorting-pictures/td-p/34679136 : app turns very white photos into taller rectangles; excess white space that cannot be cropped. Fetch: pitfalls for white-out workflow.
15. https://community.ebay.com/t5/Report-eBay-Technical-Issues/The-new-AI-background-removal-tool-started-this-June-2024-A/td-p/34507676 : complaints, about 25 percent success, lost eraser and paintbrush, forced black background (jeans vanish). Fetch: failure modes.
16. https://community.ebay.com/t5/Seller-Tools/Which-apps-or-software-are-good-to-remove-background-for/td-p/32890333 : recommendations include PhotoRoom, GIMP, Adobe Express. Fetch: app names with seller opinions.
17. https://community.ebay.com/t5/Selling/Best-app-for-white-background-photos/td-p/34209285 : PhotoRoom free tier suggested; remove.bg mentioned elsewhere. Fetch: same.
18. https://community.ebay.com/t5/Selling/Using-a-background-remover-for-photos/m-p/35334934 (also m-p/32596121, m-p/32592621) : mentors say eBay has no policy against photo editing and has its own editor; PhotoRoom praised. Fetch: the policy statement.
19. https://community.ebay.com/t5/Mobile-Apps/Ai-Background-Photo-Changer/td-p/34602120 : AI background changer needs app version 6.170 or higher. Fetch: check the current feature.
20. https://community.ebay.com/t5/Share-eBay-Technical-Issues/Issues-with-eBay-photo-editor-picture-colors-change-Adds-a-layer/td-p/29533194 : eBay's editor adds a greenish/bluish tint; workaround is edit on a computer and re-upload. Fetch: supports doing edits in our own pipeline.
21. https://community.ebay.com/t5/Selling/Best-photo-size-to-avoid-compressed-grainy-images/td-p/33747607 and https://community.ebay.com/t5/Archive-Selling/Image-Size-recommendations-for-Ebay-image-hosting/td-p/25044421 : zoom needs 800 px longest side, 1600 px recommended, uploader compresses (one says JPEG under 1500 px). Fetch: cross-check against eBay's official help.
22. https://community.ebay.com/t5/Selling/Lighting-for-clothing-photography-how-can-I-improve/td-p/24348100 : plain white bedsheet backdrop makes items pop; black for designer items. Fetch: lighting tips.
23. https://community.ebay.com/t5/Selling/Clothes-Modeling-Yourself/td-p/27315713 , https://community.ebay.com/t5/Ask-a-Mentor/How-to-use-pictures-to-display-clothing-items/td-p/32980093 , https://community.ebay.com/t5/Fashion/Modeling-used-clothing/td-p/31279876 , https://community.ebay.com/t5/New-to-selling-on-eBay/Are-try-on-pictures-okay/td-p/33626083 : alternatives (self-modeling, try-on) and buyer comfort. Fetch: lower priority.

## Consensus (SEARCH_SNIPPET only, anecdotal, years vary)

- Mannequin vs flat lay: no consensus. One small-sample seller finds flat lays outsell mannequin shots; buyers who like drape prefer a form; choose by garment (silks and draping pieces on a form, basic tees and pants flat or hung). Clear light, measurements and tag close-ups matter more than the method.
- If using a form: it must match the garment's sex and size, plain torso or headless forms keep attention on the garment, and too-large busts or pinched waists draw complaints that the item looks stretched or styled.
- Ghost mannequin: no eBay community thread found for it. The search tool said ghost-mannequin technique appears only on Adobe, Fiverr and app-store pages.
- White backgrounds: commonly advised, not required. eBay's thumbnails add white panels to non-square images (shoot or pad 1:1), and several sellers report eBay graying or darkening white backgrounds in search.
- Built-in eBay background remover: mixed to poor (inconsistent, shadows hurt it, lost manual tools, forced black backgrounds, tint on edits). Sellers move to PhotoRoom, GIMP, Adobe Express and edit on a computer.
- Search effect: no thread establishes that editing photos or whitening backgrounds changes Best Match. Only soft evidence is a Listing Quality Report line about photo count (6 per top listings, category-relative), disputed by replies. No thread found about the photo-quality nudges in the listing flow.
- Size: zoom reportedly needs 800 px longest side, 1600 px recommended, bigger gets scaled down.

## Recommendations for Ricky

1. Output square 1:1 images at 1600x1600 px, JPEG, so eBay adds no white panels and zoom works. Verify against eBay's official help once reachable.
2. Do the whitening on the PC pipeline, not in the eBay app (tint, distortion, lost controls).
3. Use at least 6 photos per listing as a cheap hedge, since that is the only search-adjacent number found.
4. Test one mannequin shot against a flat lay for a few listings; the evidence is too thin to commit. Prefer a plain headless torso or dress form sized to the garment.
5. Expect eBay to gray very pure white; check how a real listing looks in search before chasing perfect 255 white.

## Open questions

- Does eBay still gray white backgrounds in search, and is there a fix? (threads 8 to 10)
- Is there an official eBay statement on photo requirements and on photo quality nudges? (not found in any community thread)
- Does any thread discuss ghost mannequin on eBay specifically? Search found none.

## URLs to fetch once community.ebay.com opens

All URLs in the thread list above, with priority on 1, 2, 5, 7, 8, 12, 13, 14, 15, 18, 20, 21. Reason for each is on its line. Also eBay's official photo requirements help page (not searched here) to confirm size, square and white-background rules.
