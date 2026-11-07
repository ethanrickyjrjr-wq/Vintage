# Lane 09: Reddit discovery, seller wisdom on photographing clothes

Status (2026-11-07): FAILED to reach Reddit. No Reddit thread URL was obtained, so the 25-thread target is NOT met and none were invented.
- Tested with curl: old.reddit.com and www.reddit.com both return "CONNECT tunnel failed, response 403". Nothing fetched, so no file in raw/09-disc-reddit/ (empty folder).
- WebSearch cannot filter to Reddit: allowed_domains ["reddit.com"] returns API 400 "The following domains are not accessible to our user agent". Eleven extended queries (plain, "reddit" keyword, and site:reddit.com/r/<sub> for Flipping, eBaySellers, poshmark, vintageclothing, Depop) returned zero reddit.com URLs. The search tool states it does not seem to index the subreddits.
- Also refused by the proxy (403, tested once each): community.ebay.com, community.etsy.com, forums.tomsguide.com, www.adorama.com, blondesinheaven.com, flowlister.com, www.underpriced.app, www.wearview.co, theecommercemom.com, pages.ebay.com.
- Everything below is SEARCH_SNIPPET (search-tool summaries of non-Reddit pages), not VERIFIED. Treat as leads.

## Substitute seller-wisdom threads (non-Reddit, SEARCH_SNIPPET)

Mannequin vs flat lay vs hanger
- https://community.ebay.com/t5/Selling/Using-a-mannequin-to-display-clothing-for-resale-Dated/td-p/32785890 (and /m-p/32786836): sellers split. One says sales rose after switching from flat lay to a torso form; another says flat-lay items outsold mannequin ones on a small sample; one says a hanger is better; a mannequin suits kimono and drapey pieces. Best thread on the core question.
- https://community.ebay.com/t5/Selling/Clothes-Modeling-Yourself/td-p/27315713 : advice on modeling versus form; new-with-tags items should not be worn for photos (dispute evidence of wear). Also mentions a roughly $100 full-body mannequin.
- https://community.ebay.com/t5/Selling/Listing-Clothes-How-to-take-proper-pictures/m-p/34491021 : general clothing photo how-to.
- https://community.ebay.com/t5/Selling/Item-Photos/td-p/30741936 : general item photos thread.
- https://community.ebay.com/t5/Plus-Size-Divas-Hints-Fashion/Posting-plus-size-clothing-without-a-mannequin/m-p/29129022 : a hanger plus full measurements beats a mannequin that is too small. Relevant to vintage sizing.
- https://community.etsy.com/t5/Etsy-Success/Do-you-prefer-to-see-an-item-being-worn-or-displayed/td-p/49130957 : Etsy sellers; hanger and floor look poor, full-body mannequin recommended for sales.
- https://pages.ebay.com/co/en-us/sellerinformation/growing/CSA.html : eBay seller guidance; snippet says a model, dress form or mannequin shows fit better than hangers or flat lays.

Ghost mannequin
- https://community.ebay.com/t5/Ask-a-Mentor/a-ghost-mannequin-tool/td-p/32239377 : eBay community on ghost mannequin tooling.
- https://www.wearview.co/blog/ghost-mannequin-photography-alternatives : vendor blog; snippet says editing costs $0.39 to $3 per image and eBay allows flat lay and hanger images, so ghost effect is optional. Vendor-biased.
- https://www.wearview.co/blog/ghost-mannequin-photography-without-a-studio : DIY ghost mannequin with window, backdrop, cheap mannequin. Vendor-biased.
- https://graphicxer.com/tips/ghost-mannequin-photography-guide/ : vendor guide.

Vintage, pinning, fit
- https://blondesinheaven.com/blogs/vintage-fashion-guide/how-to-photograph-vintage-clothing : soft indirect daylight (north window), dress form to show drape, front/back/side, light edits only so wear stays visible.
- https://community.etsy.com/t5/Vintage-Fashion-Promotion/VINTAGE-DRESSES/m-p/38151275 (also m-p/38151297, m-p/38152931): Etsy vintage dress thread; a related thread titled "Buyers of Vintage Clothing - models or dress forms?" exists but snippet had no answer.
- https://en.wikipedia.org/wiki/Dress_form : snippet says forms are fragile and pins should not go into them. Check before pinning vintage garments to a good form.

Backgrounds and lighting on a budget
- https://community.ebay.com/t5/Ask-a-Mentor/How-to-use-the-photo-background/m-p/33752076 : eBay background removal in the app; plain white or solid bedsheet works, patterned cloth makes removal harder.
- https://community.ebay.com/t5/Selling/Posting-professional-pictures/m-p/33293207 and https://community.ebay.com/t5/Seller-Tools/Background/m-p/32479101 : backgrounds and pro-looking pictures.
- https://community.ebay.com/t5/Selling/Which-one-to-Choose-White-or-Colored-Ummm-Confused-Help/td-p/35087591 : white versus colored; white does not suit every product.
- https://community.etsy.com/t5/Etsy-Success/White-background-in-photos/td-p/46803790 and https://community.etsy.com/t5/Etsy-Success/white-background-photos/td-p/71891983 : white shows true colors; light garments may read better on a slightly darker ground.
- https://community.ebay.com/t5/Selling/Photography/m-p/28236739 : two fluorescent tubes, one each side.
- https://forums.tomsguide.com/threads/help-me-pick-a-camera-for-ebay-forum-sales.354578/post-1541110 : older Nikon Coolpix P510 sells fine; white foam board on a table outdoors.
- https://theecommercemom.com/how-to-sell-on-ebay-series-the-easy-way-to-take-great-photos/ : roughly $40 kit (poster board, phone tripod); any recent phone is enough; window light, flash off.
- https://flowlister.com/blog/how-to-take-photos-for-ebay/ : light gray or cream for light items; item fills 80 to 90 percent of frame.
- https://www.adorama.com/alc/wp-json/wp/v2/posts/90078 : mannequin recommended, about 50mm focal length for garments.

Photo count and first photo
- https://www.underpriced.app/blog/photograph-thrift-clothes-for-ebay-guide-2026 , https://flowlister.com/blog/how-to-take-photos-for-ebay/ , https://nightjar.so/blog/ebay-product-photography-listing-requirements , https://www.zikanalytics.com/blog/ebay-image-requirements/ : up to 24 photos, first photo is the search thumbnail and should be the full front of the garment; 8 to 12 purposeful photos reported to beat 20 plus. The "20 to 40 percent" and "30 percent CTR" figures come from one seller-tool blog with no data; unverified.

Depop, Poshmark, Vinted
- https://sellers.depop.com/Depop_Seller_Photography_Guide.pdf : Depop's own (2020) guide; modeled and flat-lay named as top styles; advises against dark backgrounds, bedsheets and floors for flat lays.
- https://www.vestiai.com.br/en/blog/depop-poshmark-vinted-photo-tips-that-sell and https://designerbox.ai/blog/depop-shop-photos/ : platform photo tips; a wood floor with foliage may beat white studio on Depop (platform aesthetic, not eBay).
- https://hannahmosman.substack.com/p/an-in-depth-poshmark-guide-from-a : Poshmark guide from a clothing designer.

Cheap dress forms (shopping pages, prices are snippet-level only)
- https://www.walmart.com/c/kp/dress-forms : snippet shows a 63 inch adjustable form from $39.96 and a tripod form at $26.59.
- https://www.ebay.com/b/Dress-Forms/111935/bn_7702420 and https://www.ebay.com/p/20032787836 : Dritz Sew You form listed around $165.75; used Global Model Form listed at $600 (https://www.ebay.com/itm/324496690266). Prices drift; recheck.

## Recommendations for Ricky
1. Do not rely on this lane for Reddit evidence; there is none. The honest finding is that the conflicting anecdotes (form versus flat lay) are real, and no source offered sold-listing data.
2. For vintage, the leads agree on: soft window light, front/back/side plus detail and flaw shots, a first photo of the full garment, measurements in the listing, light editing only. Test form versus flat lay yourself on a few similar pieces and track sell-through.
3. Check the Wikipedia point before pinning clothes to a good vintage form; use clips or pins on a cheap sacrificial form.

## Open questions
- Does a hanger plus measurements beat a form for oversize or odd-sized vintage?
- Is there any sold-listing comparison anywhere? None surfaced.

## URLs to fetch once the network opens (and why)
- Reddit search pages, once reddit is allowed: https://old.reddit.com/r/Flipping/search?q=mannequin&restrict_sr=1 , .../r/eBaySellers/search?q=dress+form&restrict_sr=1 , .../r/poshmark/search?q=dress+form&restrict_sr=1 , .../r/vintageclothing/search?q=photos+selling&restrict_sr=1 , .../r/Depop/search?q=mannequin&restrict_sr=1 , .../r/Mercari, r/reseller, r/vinted, r/VintageFashion, r/ThriftStoreHauls (each with ?q=ghost+mannequin, lighting, white+background, how+many+photos). Reason: the requested Reddit evidence. Append .json for structured output.
- Every community.ebay.com, community.etsy.com and vendor URL above, to turn leads into VERIFIED_FETCHED.
