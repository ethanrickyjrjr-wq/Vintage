# Pages to fetch from the Windows PC (crawl4ai)

Written 2026-11-07 by the sweep-A lanes. The cloud session could not open these hosts (network policy), so every fact drawn from them in the lane reports is snippet-level until fetched. Run from the repo root in Git Bash on the PC:

```bash
grep -oE "^- https?://[^ ]+" research/ebay-photo-studio-2026-11-07/fetch-later.md | cut -c3- | while read -r u; do tools/crawl.sh "$u" "research/ebay-photo-studio-2026-11-07/raw/fetched-on-pc/$(echo "$u" | sed -E 's#https?://##; s#[^A-Za-z0-9.]+#_#g' | cut -c1-80).md"; done
```

Reddit: if the Windows box is walled too, the Fedora box crawl4ai container sits on a residential IP; old.reddit.com URLs with a `.json` suffix are the fallback.

153 URLs, grouped by host. The note after each is the lane that asked for it and why.

## community.ebay.com (21)

- https://community.ebay.com/t5/Selling/Using-a-mannequin-to-display-clothing-for-resale-Dated/td-p/32785890  
  04-ghost-mannequin: eBay seller opinions on mannequin vs flat lay
- https://community.ebay.com/t5/Ask-a-Mentor/a-ghost-mannequin-tool/td-p/32239377  
  04-ghost-mannequin: eBay seller thread on ghost mannequin tools
- https://community.ebay.com/forum/selling-57920/topic/anyone-use-ai-generated-model-photos-for-clothing-464874/  
  05-ai-tryon: seller experience with AI model photos on used clothing
- https://community.ebay.com/t5/Selling/Help-How-do-I-get-ACTUAL-Color-depicted-in-my-photos/td-p/27847415  
  07-enhance: seller colour complaints, quotable
- https://community.ebay.com/t5/Announcements/List-faster-and-easier-with-our-magical-AI-powered-bulk-listing/ba-p/34685758/  
  13-disc-ebay-ai: bulk Magical Listing announcement
- https://community.ebay.com/forum/selling-57920/topic/ai-clothing-model-cover-photo-152705/  
  13-disc-ebay-ai: seller experience with AI model cover photos
- https://community.ebay.com/t5/Selling/Listing-Clothes-How-to-take-proper-pictures/td-p/34490503  
  13-disc-ebay-ai: seller advice on mannequins for clothing
- https://community.ebay.com/t5/Selling/Selling-clothing-Flay-lay-vs-Mannequin/td-p/32565924  
  16-disc-ebay-community: flat lay vs mannequin sell-through
- https://community.ebay.com/t5/Selling/Less-than-6-photos-affect-search-impressions-per-Listing-Quality/td-p/32120944  
  16-disc-ebay-community: photos vs search impressions
- https://community.ebay.com/forum/selling-57920/topic/ebay-forcing-white-background-on-images-looks-terrible-sitewide-111796/  
  16-disc-ebay-community: white panels and 1:1
- https://community.ebay.com/t5/Selling/eBay-Changing-White-Backgrounds-in-Search-MAKING-THEM-GRAY/td-p/33812316  
  16-disc-ebay-community: graying of white backgrounds
- https://community.ebay.com/forum/selling-57920/topic/photo-back-ground-is-white-needed-156571/  
  16-disc-ebay-community: is white required
- https://community.ebay.com/t5/Selling/Ebay-s-Background-Removing-Tool-Greatly-Improved/td-p/33965767  
  16-disc-ebay-community: built-in remover quality
- https://community.ebay.com/t5/Selling/Background-Remover-is-distorting-pictures/td-p/34679136  
  16-disc-ebay-community: remover pitfalls
- https://community.ebay.com/t5/Report-eBay-Technical-Issues/The-new-AI-background-removal-tool-started-this-June-2024-A/td-p/34507676  
  16-disc-ebay-community: remover failure modes
- https://community.ebay.com/t5/Selling/Using-a-background-remover-for-photos/m-p/35334934  
  16-disc-ebay-community: editing policy statement
- https://community.ebay.com/t5/Share-eBay-Technical-Issues/Issues-with-eBay-photo-editor-picture-colors-change-Adds-a-layer/td-p/29533194  
  16-disc-ebay-community: color tint in eBay editor
- https://community.ebay.com/t5/Selling/Best-photo-size-to-avoid-compressed-grainy-images/td-p/33747607  
  16-disc-ebay-community: size and compression claims
- https://community.ebay.com/t5/Selling/Do-the-quality-of-photos-really-matter-or-matter-enough-based-on/td-p/34960307  
  16-disc-ebay-community: photo effort vs return for clothing
- https://community.ebay.com/t5/Seller-Tools/Which-apps-or-software-are-good-to-remove-background-for/td-p/32890333  
  16-disc-ebay-community: third-party app opinions
- https://community.ebay.com/t5/Selling/Lighting-for-clothing-photography-how-can-I-improve/td-p/24348100  
  16-disc-ebay-community: lighting and backdrop tips

## www.ebay.com (13)

- https://www.ebay.com/help/policies/listing-policies/picture-policy?id=4370  
  05-ai-tryon: eBay picture policy, stock-photo and accuracy rules
- https://www.ebay.com/help/policies/ebay-user-agreement  
  05-ai-tryon: seller responsibility for generative-AI listing content
- https://www.ebay.com/help/selling/listings/listing-pictures  
  06-pipeline: eBay's own picture rules: min size, 7 MB, background and shadow policy (path from memory, find via help search)
- https://www.ebay.com/help/selling/listings/creating-managing-listings/photo-requirements?id=4113  
  07-enhance: eBay's own image size, zoom and background rules
- https://www.ebay.com/help/selling/listings/adding-pictures-listings?id=4148  
  08-prior-work: Re-check the 1600 px, 24 photo and background-tool wording and the overhead lighting contradiction.
- https://www.ebay.com/sellercenter/listings/photo-tips  
  08-prior-work: Seller Center says use bright overhead lighting; help page says avoid it.
- https://www.ebay.com/sellercenter/selling/selling-clothes  
  08-prior-work: Re-check the light-on-dark backdrop sentence.
- https://www.ebay.com/help/policies/listing-policies/images-videos-text-policy?id=4240  
  08-prior-work: Confirm 'take your own images' and any AI-image rule; the repo has only a paraphrase.
- https://www.ebay.com/sch/i.html?_nkw=acme+adjustable+dress+form+vintage&_sop=12  
  11-disc-mannequins: Acme sold prices (use the Sold filter)
- https://www.ebay.com/help/policies/listing-policies/picture-policy-ebay-pictures-policy?id=4370  
  13-disc-ebay-ai: re-check for AI wording
- https://www.ebay.com/help/policies/member-behavior-policies/user-agreement?id=4259  
  13-disc-ebay-ai: generative-AI responsibility clause
- https://www.ebay.com/help/policies/prohibited-restricted-items/used-clothing-policy?id=4281  
  13-disc-ebay-ai: full used clothing policy text
- https://www.ebay.com/sellercenter/resources/seller-updates/2024-october/tools  
  13-disc-ebay-ai: eBay AI tools list

## huggingface.co (9)

- https://huggingface.co/briaai/RMBG-2.0  
  02-models: Actual licence text and gating terms. hf_fs was denied and the web host is blocked.
- https://huggingface.co/ZhengPeng7/BiRefNet  
  02-models: Full main card usage code and the BiRefNet_lite-2K card
- https://huggingface.co/PramaLLC/BEN2/blob/main/onnx_run.py  
  02-models: BEN2 ONNX inference on Windows
- https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B  
  04-ghost-mannequin: base model license terms for commercial use
- https://huggingface.co/black-forest-labs/FLUX.2-klein-9B  
  05-ai-tryon: gated licence text for the 9B base
- https://huggingface.co/spaces/not-lain/background-removal  
  03-hf-spaces: live status, hardware, limits
- https://huggingface.co/spaces/ZhengPeng7/BiRefNet_demo  
  03-hf-spaces: runtime and hardware, model dropdown
- https://huggingface.co/docs/hub/spaces-zerogpu  
  03-hf-spaces: ZeroGPU quotas and queue rules
- https://huggingface.co/api/spaces/not-lain/background-removal  
  03-hf-spaces: runtime stage and hardware JSON

## www.youtube.com (9)

- https://www.youtube.com/watch?v=p-YpsLSaYas  
  10-disc-youtube: Shoot and edit ghost mannequin: description, chapters, transcript
- https://www.youtube.com/watch?v=YYYoNMDF6iI  
  10-disc-youtube: eBay clothing on bright white background
- https://www.youtube.com/watch?v=9xBRV9UfNBM  
  10-disc-youtube: eBay dresses bright white plus measurements
- https://www.youtube.com/watch?v=EG746TUpw4s  
  10-disc-youtube: Full-time seller photo station tour
- https://www.youtube.com/watch?v=r0lYqGRVj4I  
  10-disc-youtube: Reseller photo studio build
- https://www.youtube.com/watch?v=_EvqC0AN864  
  10-disc-youtube: Batch workflow, 15 items in 15 minutes
- https://www.youtube.com/watch?v=zm7PRDUDlJ0  
  10-disc-youtube: Dress on ghost mannequin
- https://www.youtube.com/watch?v=-WI4b419vmk  
  10-disc-youtube: Blazer on ghost mannequin
- https://www.youtube.com/watch?v=MNnIvZu-PQ0  
  10-disc-youtube: Perfect white background lighting

## github.com (8)

- https://github.com/danielgatis/rembg/blob/main/USAGE.md  
  01-rembg: examples page linked from README
- https://github.com/danielgatis/rembg/pull/846  
  01-rembg: -vm ViTMatte design notes and quality claims
- https://github.com/danielgatis/rembg/pull/843  
  01-rembg: -dc decontamination design notes
- https://github.com/peterpeeterspeter/json-ghost-mannequin-pipeline  
  04-ghost-mannequin: original SDXL/ControlNet/Gemini pipeline, safer than the awekakwe copy
- https://github.com/franciszzj/Leffa/blob/main/LICENSE  
  05-ai-tryon: confirm Leffa MIT text and dataset caveats
- https://github.com/Zheng-Chong/CatVTON/issues/8  
  05-ai-tryon: Windows install problems
- https://github.com/jimmyXiang123/whitebg/tree/main/whitebg  
  06-pipeline: Read crop, pad, shadow, decontamination source to borrow; also its commits page for last-commit date
- https://github.com/ZhengPeng7/BiRefNet  
  03-hf-spaces: local install, model zoo, licences

## www.etsy.com (5)

- https://www.etsy.com/legal/creativity-standards  
  05-ai-tryon: AI disclosure sentence and photo rules
- https://www.etsy.com/legal/sellers  
  05-ai-tryon: listing photo requirements and Oct 2026 change
- https://www.etsy.com/legal/policy/listing-image-requirements/253962679005  
  08-prior-work: Exceptions to the unedited-photo rule; walled earlier.
- https://www.etsy.com/seller-handbook/article/how-to-photograph-challenging-items/146863877358  
  11-disc-mannequins: exact Etsy wording on pins, tape and tissue
- https://www.etsy.com/seller-handbook/article/1347574487014  
  15-disc-competitors: Etsy photo size and count

## old.reddit.com (5)

- https://old.reddit.com/r/Flipping/search?q=mannequin&restrict_sr=1  
  09-disc-reddit: Core Reddit evidence on mannequin vs flat lay; append .json for structure
- https://old.reddit.com/r/eBaySellers/search?q=dress+form&restrict_sr=1  
  09-disc-reddit: eBay seller opinions on dress forms and photos
- https://old.reddit.com/r/poshmark/search?q=dress+form&restrict_sr=1  
  09-disc-reddit: Poshmark seller form/hanger/flat lay experience
- https://old.reddit.com/r/vintageclothing/search?q=photos+selling&restrict_sr=1  
  09-disc-reddit: Vintage-specific photography and pinning advice
- https://old.reddit.com/r/Depop/search?q=mannequin&restrict_sr=1  
  09-disc-reddit: Depop mannequin and flat lay opinions

## www.photoroom.com (5)

- https://www.photoroom.com/api/remove-background  
  08-prior-work: Price, ghostMannequin parameter and API commercial terms.
- https://www.photoroom.com/api/pricing  
  14-disc-hosted: plan minimums and per-image prices
- https://www.photoroom.com/legal/terms-and-conditions  
  14-disc-hosted: exact commercial and API terms
- https://www.photoroom.com/customer-stories/depop  
  14-disc-hosted: confirm Depop integration
- https://www.photoroom.com/blog/sell-fast-on-depop  
  15-disc-competitors: Campervan Vintage quote and Business Insider link

## support.apple.com (4)

- https://support.apple.com/en-us/102108  
  07-enhance: iPhone camera lock behaviour
- https://support.apple.com/121429  
  17-disc-phone-builtin: Official Clean Up requirements
- https://support.apple.com/guide/iphone/  
  17-disc-phone-builtin: Official Lift subject steps and iOS version (search 'Lift a subject from the photo background')
- https://support.apple.com/guide/shortcuts/  
  17-disc-phone-builtin: Official Shortcuts action list; confirm the Remove Background action name and iOS version

## www.valueaddedresource.net (3)

- https://www.valueaddedresource.net/ebay-tests-ai-fashion-models-alters-images/  
  05-ai-tryon: eBay's own AI fashion model test
- https://www.valueaddedresource.net/ebay-images-altered-by-ai-without-knowledge/  
  13-disc-ebay-ai: altered images report
- https://www.valueaddedresource.net/ebay-sellers-lose-background-removal-in-app/  
  17-disc-phone-builtin: Full text on the removed eBay in-app remover

## export.ebay.com (3)

- https://export.ebay.com/en/manage-listings/photo-tips  
  06-pipeline: Confirm 7 MB and 800 to 1600 px statement from eBay's own page
- https://export.ebay.com/en/first-steps/manage-listings/photo-tips/  
  13-disc-ebay-ai: confirm or kill the model/dress form/mannequin sentence
- https://export.ebay.com/en/first-steps/manage-listings/the-perfect-clothing-ad/  
  13-disc-ebay-ai: clothing photo checklist, possible mannequin guidance

## innovation.ebayinc.com (3)

- https://innovation.ebayinc.com/stories/background-swap-tool-turns-any-photo-into-a-studio-quality-product-image/  
  13-disc-ebay-ai: AI background tool launch and availability
- https://innovation.ebayinc.com/stories/ebay-reduces-the-time-to-list-on-mobile-with-new-simplified-selling-tool-now-featuring-magical-listing-ai-technology/  
  13-disc-ebay-ai: Magical Listing scope
- https://innovation.ebayinc.com/stories/ebay-uses-computer-vision-to-enable-sellers-to-create-cleaner-images/  
  14-disc-hosted: current eBay in-app tool

## arxiv.org (2)

- https://arxiv.org/abs/2501.06230  
  02-models: BEN2 paper for architecture and numbers
- https://arxiv.org/abs/2401.03407  
  02-models: BiRefNet paper

## www.reddit.com (2)

- https://www.reddit.com/r/comfyui/  
  02-models: Practitioner threads comparing BiRefNet and BEN2 on garments, glass and lace
- https://www.reddit.com/r/Flipping/  
  12-disc-lighting: reseller threads on white backdrops, mannequins, cut-outs

## onnxruntime.ai (2)

- https://onnxruntime.ai/getting-started  
  01-rembg: CUDA/cuDNN installation matrix the README points to
- https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html  
  06-pipeline: CUDA and cuDNN versions needed for onnxruntime-gpu 1.23.x on Windows

## helpx.adobe.com (2)

- https://helpx.adobe.com/photoshop/using/processing-batch-files.html  
  07-enhance: Photoshop batch and Image Processor details
- https://helpx.adobe.com/express/web/image-creation-and-editing/edit-images/remove-background.html  
  14-disc-hosted: free limits and commercial terms

## pages.ebay.com (2)

- https://pages.ebay.com/co/en-us/sellerinformation/growing/CSA.html  
  09-disc-reddit: eBay's own clothing photo guidance, quote exact sentence
- https://pages.ebay.com/co/en-us/sellerinformation/howtosell/guides/clothes.html  
  12-disc-lighting: eBay backdrop guidance full text

## www.remove.bg (2)

- https://www.remove.bg/pricing  
  08-prior-work: Confirm the 2026-12-01 shutdown and Leonardo.ai API move.
- https://www.remove.bg/faq  
  14-disc-hosted: migration facts and date

## neewer.com (2)

- https://neewer.com/products/lighting-studio-66600013  
  12-disc-lighting: live price, bulb specs, stand height
- https://neewer.com/collections/shooting-tent  
  12-disc-lighting: light tent sizes and prices

## www.bhphotovideo.com (2)

- https://www.bhphotovideo.com/c/product/1739483-REG/godox_sl60iibi_kit_sl60iibi_2_light_kit.html  
  12-disc-lighting: Godox kit contents and price
- https://www.bhphotovideo.com/c/product/45607-REG/Savage_1_1253_Widetone_Seamless_Background_Paper.html  
  12-disc-lighting: paper stock, widths including 107in roll

## withoutbg.com (1)

- https://withoutbg.com/models/birefnet-general  
  02-models: Third-party sample results of rembg models, host not tested

## raw.githubusercontent.com (1)

- https://raw.githubusercontent.com/danielgatis/rembg/main/rembg/sessions/birefnet_general.py  
  01-rembg: preprocessing and whether an HR-matting session exists

## fashn.ai (1)

- https://fashn.ai/blog/ghost-mannequin-photography-complete-guide  
  04-ghost-mannequin: shoot method, Photoshop steps, cost

## retouch4.me (1)

- https://retouch4.me/blog/how-to-create-the-ghost-mannequin-effect-for-ecommerce-product-photography  
  04-ghost-mannequin: step-by-step guide

## pixc.com (1)

- https://pixc.com/blog/how-to-create-a-ghost-mannequin-effect-photoshop/  
  04-ghost-mannequin: Photoshop steps

## www.retouchingzone.com (1)

- https://www.retouchingzone.com/edit-ghost-mannequin-photography-in-gimp/  
  04-ghost-mannequin: GIMP steps

## docs.photoroom.com (1)

- https://docs.photoroom.com/image-editing-api-plus-plan/ghost-mannequin  
  04-ghost-mannequin: official Photoroom ghost spec and pricing

## www.wearview.co (1)

- https://www.wearview.co/blog/best-ai-ghost-mannequin-tools  
  04-ghost-mannequin: tool comparison and pricing

## blog.mannequinmadness.com (1)

- https://blog.mannequinmadness.com/2019/05/a-crash-course-in-staging-your-clothing-to-photograph-to-sell-online/  
  04-ghost-mannequin: pinning and staging clothes on forms

## pillow.readthedocs.io (1)

- https://pillow.readthedocs.io/en/stable/reference/ImageCms.html  
  06-pipeline: Confirm sRGB profile conversion API

## imagemagick.org (1)

- https://imagemagick.org/script/command-line-options.php  
  07-enhance: exact flags for resize, unsharp, auto-level, distort, strip

## www.xnview.com (1)

- https://www.xnview.com/en/xnconvert/  
  07-enhance: XnConvert licence and batch features

## www.irfanview.com (1)

- https://www.irfanview.com  
  07-enhance: IrfanView batch conversion and licence

## www.topazlabs.com (1)

- https://www.topazlabs.com/topaz-photo-ai  
  07-enhance: Topaz Photo AI price, version, specs

## www.shopify.com (1)

- https://www.shopify.com/blog/115603781-how-to-color-correct-product-images-in-adobe-lightroom-and-minimize-returns  
  07-enhance: colour correction and returns

## en.wikipedia.org (1)

- https://en.wikipedia.org/wiki/Gray_card  
  07-enhance: grey card reference quote

## www.alanranger.com (1)

- https://www.alanranger.com/blog-on-photography/how-to-take-product-photos-with-iphone  
  07-enhance: iPhone AE/AF lock steps

## pixelcut.ai (1)

- https://pixelcut.ai  
  07-enhance: upscaler pricing

## blondesinheaven.com (1)

- https://blondesinheaven.com/blogs/vintage-fashion-guide/how-to-photograph-vintage-clothing  
  09-disc-reddit: Vintage photography guide

## sellers.depop.com (1)

- https://sellers.depop.com/Depop_Seller_Photography_Guide.pdf  
  09-disc-reddit: Depop official photography guide

## pypi.org (1)

- https://pypi.org/pypi/rembg/json  
  08-prior-work: Confirm the current rembg version and Python range (reachable; lane 01 already did).

## botika.com (1)

- https://botika.com/resources/thethread/how-to-photograph-clothing-on-a-mannequin  
  10-disc-youtube: Written pinning and styling guidance; host not tested

## www.photorobot.com (1)

- https://www.photorobot.com/tutorials/fashion-photography-styling-tools  
  10-disc-youtube: Styling tools, clips and pins; host not tested

## forums.vintagefashionguild.org (1)

- https://forums.vintagefashionguild.org/threads/using-a-dress-form-with-vintage-clothing.64881/  
  11-disc-mannequins: first-hand vintage seller form advice

## atlaslevy.com (1)

- https://atlaslevy.com/Dritz-My-Double-Medium-Adjustable-Dress-Form_p_49.html  
  11-disc-mannequins: live Dritz price and size chart

## www.amazon.com (1)

- https://www.amazon.com/pinnable-dress-form/s?k=pinnable+dress+form  
  11-disc-mannequins: live prices for forms under $60

## mannequinmall.com (1)

- https://mannequinmall.com/collections/female-dress-forms  
  11-disc-mannequins: vintage-look linen tier prices

## www.walmart.com (1)

- https://www.walmart.com/seller/13733  
  11-disc-mannequins: Roxy Display prices

## theshopcompany.com (1)

- https://theshopcompany.com/products/the-ultimate-dress-form-fitting-pad-system-by-fabulous-fit  
  11-disc-mannequins: padding system price and size table

## www.fadedfragments.com (1)

- https://www.fadedfragments.com/products/mannequin-antique-dress-form-with-antique-wood-base  
  11-disc-mannequins: antique linen form listing

## listingtofreedom.com (1)

- https://listingtofreedom.com/best-mannequin-for-photography/  
  11-disc-mannequins: reseller-oriented form pick

## help.photoroom.com (1)

- https://help.photoroom.com/en/articles/14182832-create-ghost-mannequin-images-for-a-batch-web-app  
  14-disc-hosted: batch limits

## www.pixelcut.ai (1)

- https://www.pixelcut.ai/api/background-remover  
  14-disc-hosted: verify $0.05 and terms

## www.canva.com (1)

- https://www.canva.com/help/background-remover/  
  14-disc-hosted: Canva remover plan and bulk

## pixian.ai (1)

- https://pixian.ai/pricing  
  14-disc-hosted: dollar per credit, HEIC, terms

## claid.ai (1)

- https://claid.ai/api-pricing  
  14-disc-hosted: API credit prices, terms

## ar5iv.labs.arxiv.org (1)

- https://ar5iv.labs.arxiv.org/html/1406.3561  
  15-disc-competitors: Confirm the eBay paper's flat, mannequin and person numbers and its sample

## help.etsy.com (1)

- https://help.etsy.com/hc/en-us/articles/115015628707-Listing-a-Physical-Item  
  15-disc-competitors: Etsy official 20 photos and video limit

## productscene.com (1)

- https://productscene.com/product-photography/clothing-product-photos-for-etsy  
  15-disc-competitors: Etsy clothing photo advice and conversion claim source

## www.underpriced.app (1)

- https://www.underpriced.app/blog/photograph-thrift-clothes-for-ebay-guide-2026  
  15-disc-competitors: eBay clothing photo guide with mannequin vs flat lay discussion

## www.scavengerlife.com (1)

- https://www.scavengerlife.com/forums/topic/using-a-mannequin-or-posing-clothes-for-ebay-listings-which-is-better/  
  15-disc-competitors: Seller forum thread on mannequin vs posing

## www.thevintageseeker.ca (1)

- https://www.thevintageseeker.ca/magazine/listing-tips-from-a-seller-simplify-your-listings-process-with-this-advice-from-lemons-loot  
  15-disc-competitors: A working vintage seller's listing process

## www.emerald.com (1)

- https://www.emerald.com/jrim/article-abstract/17/3/470/250559/Can-you-imagine-yourself-wearing-this-product  
  15-disc-competitors: Mannequin vs human model study abstract

## support.microsoft.com (1)

- https://support.microsoft.com/  
  17-disc-phone-builtin: Windows Photos and Paint background removal: versions and exact steps

## maketecheasier.com (1)

- https://maketecheasier.com/iphone-batch-edit-photos-videos/  
  17-disc-phone-builtin: Files Quick Action batch behaviour

## discussions.apple.com (1)

- https://discussions.apple.com/thread/254979394  
  17-disc-phone-builtin: Repeat with Each pattern for batch Remove Background

## matthewcassinelli.com (1)

- https://matthewcassinelli.com/shortcuts/remove-background-from-photo/  
  17-disc-phone-builtin: Downloadable single-image shortcut

## routinehub.co (1)

- https://routinehub.co/  
  17-disc-phone-builtin: Search for batch remove-background shortcuts

## store.google.com (1)

- https://store.google.com/intl/en_in/ideas/articles/magic-editor  
  17-disc-phone-builtin: Magic Editor details (low priority; Ricky has an iPhone)

## Added on the PC 2026-11-07 (lane 17's re-check found the list held Apple guide roots, not the step articles)

- https://support.apple.com/guide/iphone/lift-a-subject-from-the-photo-background-iphfe4809658/ios  
  17-disc-phone-builtin: Apple's own steps for lifting a subject and the menu wording (Copy Subject, Share)
- https://support.apple.com/guide/shortcuts/navigate-the-action-list-apdc33e4f4da/ios  
  17-disc-phone-builtin: the Shortcuts action list, to see whether a Remove Background action exists
- https://support.apple.com/guide/iphone/transfer-files-between-devices-iph339bafff3/ios  
  17-disc-phone-builtin: how photos move from the phone to the PC
- https://support.apple.com/guide/iphone/connect-iphone-and-your-computer-with-a-cable-iph42d9b3178/ios  
  17-disc-phone-builtin: cable transfer and the Most Compatible setting
