hf:// model-card excerpts read with hf_fs cat on 2026-11-07 (MCP_DATA). Verbatim lines only.

== hf://models/ZhengPeng7/BiRefNet_HR/README.md
> This BiRefNet was trained with images in `2048x2048` for higher resolution inference.
> All tested in FP16 mode.
DIS-VD BiRefNet_HR-general-epoch_130 2048x2048 maxFm .925 wFmeasure .894 MAE .026 Smeasure .927 HCE 811
DIS-VD BiRefNet_HR-general-epoch_130 1024x1024 maxFm .876 wFmeasure .840 MAE .041 HCE 1348
DIS-VD BiRefNet-general-epoch_244 2048x2048 wFmeasure .858 MAE .037 HCE 811
DIS-VD BiRefNet-general-epoch_244 1024x1024 wFmeasure .877 MAE .034 HCE 1128
(So HR must be fed 2048; at 1024 it is worse than the base model.)

== hf://models/ZhengPeng7/BiRefNet-matting/README.md
## This repo holds the official weights of BiRefNet for general matting.
Training sets: P3M-10k (except TE-P3M-500-NP), TR-humans, AM-2k, AIM-500, Human-2k (synthesized with BG-20k), Distinctions-646 (synthesized with BG-20k), HIM2K, PPM-100
Validation: TE-P3M-500-NP. BiRefNet-matting--epoch_100 Smeasure .979 maxFm .996 MSE .003
(Training data is people/animals/objects matting sets; no garment or glass set listed.)

== hf://models/ZhengPeng7/BiRefNet_HR-matting/README.md
> This BiRefNet was trained with images in `2048x2048` for higher resolution image matting with transparency.
> All tested in FP16 mode.
TE-AM-2k BiRefNet_HR-matting 2048x2048 wFmeasure .997 ; BiRefNet-matting at 1024 .996, at 2048 .996 (near-equal scores)

== hf://models/ZhengPeng7/BiRefNet_dynamic/README.md
> An arbitrary shape adaptable BiRefNet for general segmentation.
> This model was trained on arbitrary shapes (256x256 ~ 2304x2304) and shows great robustness on inputs with any shape.
> ... greater than BiRefNet-general and BiRefNet_HR-general on the reserved validation sets (DIS-VD and TE-P3M-500-NP).

== hf://models/ZhengPeng7/BiRefNet_lite/README.md
## How to use (this tiny version)
birefnet = AutoModelForImageSegmentation.from_pretrained('zhengpeng7/BiRefNet_lite', trust_remote_code=True)
"Remember to set the `bb` in `config.py` as `swin_v1_t`" (for GitHub code route). 44.4M params.

== hf://models/ZhengPeng7/BiRefNet-portrait/README.md
## This repo holds the official weights of BiRefNet for general matting.   (card heading; weights are portrait matting)
Training sets: P3M-10k (except TE-P3M-500-P), TR-humans. Validation: TE-P3M-500-P. Acknowledgement: fal GPU support.

== hf://models/PramaLLC/BEN2/README.md  (front matter: license: mit)
BEN2 introduces a novel approach to foreground segmentation through its innovative Confidence Guided Matting (CGM) pipeline.
BEN2 was trained on the DIS5k and our 22K proprietary segmentation dataset. Our enhanced model delivers superior performance in hair matting, 4K processing, object segmentation, and edge refinement. Our Base model is open source.
For access to our commercial model email us at sales@backgrounderase.com
foreground = model.inference(image, refine_foreground=False,)  #Refine foreground is an extract postprocessing step that increases inference time but can improve matting edges.
We recommend that the batch size not exceed 3 for consumer GPUs
Install: pip install -e "git+https://github.com/PramaLLC/BEN2.git#egg=ben2"
(Note: the best "hair/4K" model is the commercial one; the open one is BEN2 Base.)

== hf://models/briaai/RMBG-1.4/README.md
license: other / license_name: bria-rmbg-1.4 ; extra_gated_description: RMBG v1.4 is available as a source-available model for non-commercial use
"Commercial use is subject to a commercial agreement with BRIA."
"BRIA RMBG 1.4 is a saliency segmentation model trained exclusively on a professional-grade dataset."
Training data: over 12,000 images; Objects only 45.11%, People only 17.35%, Photorealistic 87.70%.
"RMBG v1.4 is developed on the IS-Net enhanced with our unique training scheme and proprietary dataset."

== hf://models/briaai/RMBG-2.0/README.md
ERROR HF_FS_ACCESS_DENIED: "Access to model briaai/RMBG-2.0 is restricted and you are not in the authorized list."  Licence taken from hub_repo_details (license: other, Status: Gated) and from the GitHub README (see gh-bria-rmbg2.md).

== hf://models/skytnt/anime-seg/README.md
front matter: license: apache-2.0 ; library: https://github.com/SkyTNT/anime-segmentation (anime characters; not relevant to clothing)
