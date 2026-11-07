<!-- source: https://github.com/franciszzj/Leffa, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - franciszzj/Leffa: \[CVPR 2025\] Learning Flow Fields in Attention for Controllable Person Image Generation · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Ffranciszzj%2FLeffa)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Ffranciszzj%2FLeffa)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=franciszzj%2FLeffa)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/franciszzj/Leffa)

![franciszzj](https://avatars.githubusercontent.com/u/16440889?s=60&v=4)

**[Leffa](/franciszzj/Leffa)**

Public

-   [Notifications](/login?return_to=%2Ffranciszzj%2FLeffa)You must be signed in to change notification settings
-   [Fork185 (185)](/login?return_to=%2Ffranciszzj%2FLeffa)
-   [Star1.7k (1.7k)](/login?return_to=%2Ffranciszzj%2FLeffa)You must be signed in to star a repository

## About

\[CVPR 2025\] Learning Flow Fields in Attention for Controllable Person Image Generation

[huggingface.co/spaces/franciszzj/Leffa](https://huggingface.co/spaces/franciszzj/Leffa)

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

[Activity](/franciszzj/Leffa/activity)

### Stars

**1.7k** stars

### Watchers

**16** watching

### Forks

[**185** forks](/franciszzj/Leffa/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Ffranciszzj%2FLeffa&report=franciszzj+%28user%29)

[Branches](/franciszzj/Leffa/branches)[Tags](/franciszzj/Leffa/tags)

[](/franciszzj/Leffa/branches)[](/franciszzj/Leffa/tags)

Open more actions menu

## Latest commit

## History

[75 Commits](/franciszzj/Leffa/commits/main/)

[](/franciszzj/Leffa/commits/main/)75 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[3rdparty](/franciszzj/Leffa/tree/main/3rdparty "3rdparty")

[3rdparty](/franciszzj/Leffa/tree/main/3rdparty "3rdparty")

[leffa](/franciszzj/Leffa/tree/main/leffa "leffa")

[leffa](/franciszzj/Leffa/tree/main/leffa "leffa")

[leffa\_utils](/franciszzj/Leffa/tree/main/leffa_utils "leffa_utils")

[leffa\_utils](/franciszzj/Leffa/tree/main/leffa_utils "leffa_utils")

[preprocess](/franciszzj/Leffa/tree/main/preprocess "preprocess")

[preprocess](/franciszzj/Leffa/tree/main/preprocess "preprocess")

[.gitignore](/franciszzj/Leffa/blob/main/.gitignore ".gitignore")

[.gitignore](/franciszzj/Leffa/blob/main/.gitignore ".gitignore")

[LICENSE](/franciszzj/Leffa/blob/main/LICENSE "LICENSE")

[LICENSE](/franciszzj/Leffa/blob/main/LICENSE "LICENSE")

[README.md](/franciszzj/Leffa/blob/main/README.md "README.md")

[README.md](/franciszzj/Leffa/blob/main/README.md "README.md")

[SCHP](/franciszzj/Leffa/blob/main/SCHP "SCHP")

[SCHP](/franciszzj/Leffa/blob/main/SCHP "SCHP")

[app.py](/franciszzj/Leffa/blob/main/app.py "app.py")

[app.py](/franciszzj/Leffa/blob/main/app.py "app.py")

[densepose](/franciszzj/Leffa/blob/main/densepose "densepose")

[densepose](/franciszzj/Leffa/blob/main/densepose "densepose")

[detectron2](/franciszzj/Leffa/blob/main/detectron2 "detectron2")

[detectron2](/franciszzj/Leffa/blob/main/detectron2 "detectron2")

[requirements.txt](/franciszzj/Leffa/blob/main/requirements.txt "requirements.txt")

[requirements.txt](/franciszzj/Leffa/blob/main/requirements.txt "requirements.txt")

## Repository files navigation

# _Leffa_: Learning Flow Fields in Attention for Controllable Person Image Generation

[](#leffa-learning-flow-fields-in-attention-for-controllable-person-image-generation)

[📚 Paper](https://arxiv.org/abs/2412.08486) - [🤖 Code](https://github.com/franciszzj/Leffa) - [🔥 Demo](https://huggingface.co/spaces/franciszzj/Leffa) - [🤗 Model](https://huggingface.co/franciszzj/Leffa)

Star ⭐ us if you like it!

## News

[](#news)

-   26/Feb/2025. Leffa is accepted to CVPR 2025.
-   09/Jan/2025. Inference defaults to float16, generating an image in 6 seconds (on A100).
-   02/Jan/2025. Update the mask generator to improve results. Add ref unet acceleration, boosting prediction speed by 30%. Include more controls in Advanced Options to enhance user experience. Enable intermediate result output for easier development. Enjoy using it!
-   18/Dec/2024. Thanks to @[StartHua](https://github.com/StartHua) for integrating Leffa into ComfyUI! Here is the [repo](https://github.com/StartHua/Comfyui_leffa)!
-   16/Dec/2024. The virtual try-on [model](https://huggingface.co/franciszzj/Leffa/blob/main/virtual_tryon_dc.pth) trained on DressCode is released.
-   12/Dec/2024. The HuggingFace [demo](https://huggingface.co/spaces/franciszzj/Leffa) and [models](https://huggingface.co/franciszzj/Leffa) (virtual try-on model trained on VITON-HD and pose transfer model trained on DeepFashion) are released.
-   11/Dec/2024. The [arXiv](https://arxiv.org/abs/2412.08486) version of the paper is released.

_[Leffa](https://en.wiktionary.org/wiki/leffa)_ is a unified framework for controllable person image generation that enables precise manipulation of both appearance (i.e., virtual try-on) and pose (i.e., pose transfer).

[![](https://camo.githubusercontent.com/c01e29f63d95eb5923a44e3788613dce3042b16796086c37fd52e92c41b34025/68747470733a2f2f68756767696e67666163652e636f2f6672616e6369737a7a6a2f4c656666612f7265736f6c76652f6d61696e2f6173736574732f7465617365722e706e67)](https://camo.githubusercontent.com/c01e29f63d95eb5923a44e3788613dce3042b16796086c37fd52e92c41b34025/68747470733a2f2f68756767696e67666163652e636f2f6672616e6369737a7a6a2f4c656666612f7265736f6c76652f6d61696e2f6173736574732f7465617365722e706e67)

## Abstract

[](#abstract)

Controllable person image generation aims to generate a person image conditioned on reference images, allowing precise control over the person’s appearance or pose. However, prior methods often distort fine-grained textural details from the reference image, despite achieving high overall image quality. We attribute these distortions to inadequate attention to corresponding regions in the reference image. To address this, we thereby propose **le**arning **f**low **f**ields in **a**ttention (_**Leffa**_), which explicitly guides the target query to attend to the correct reference key in the attention layer during training. Specifically, it is realized via a regularization loss on top of the attention map within a diffusion-based baseline. Our extensive experiments show that _Leffa_ achieves state-of-the-art performance in controlling appearance (virtual try-on) and pose (pose transfer), significantly reducing fine-grained detail distortion while maintaining high image quality. Additionally, we show that our loss is model-agnostic and can be used to improve the performance of other diffusion models.

## Method

[](#method)

An overview of our _Leffa_ training pipeline for controllable person image generation. The left is our diffusion-based baseline; the right is our _Leffa_ loss. Note that Isrc and Itgt are the same image during training.

[![](https://camo.githubusercontent.com/567cc2c4f8254830708e17124af8384320d8b28bd384192227133619d8c56251/68747470733a2f2f68756767696e67666163652e636f2f6672616e6369737a7a6a2f4c656666612f7265736f6c76652f6d61696e2f6173736574732f6c656666612e706e67)](https://camo.githubusercontent.com/567cc2c4f8254830708e17124af8384320d8b28bd384192227133619d8c56251/68747470733a2f2f68756767696e67666163652e636f2f6672616e6369737a7a6a2f4c656666612f7265736f6c76652f6d61696e2f6173736574732f6c656666612e706e67)

## Visualization

[](#visualization)

Qualitative visual results comparison with other methods. The input person image for the pose transfer is generated using our method in the virtual try-on. The visualization results demonstrate that our method not only generates high-quality images but also greatly reduces the distortion of fine-grained details.

[![](https://camo.githubusercontent.com/829baab78e08deaf975b2bc9980fdcdd9c209a79fb2cd1413788334b5216070b/68747470733a2f2f68756767696e67666163652e636f2f6672616e6369737a7a6a2f4c656666612f7265736f6c76652f6d61696e2f6173736574732f7669735f726573756c742e706e67)](https://camo.githubusercontent.com/829baab78e08deaf975b2bc9980fdcdd9c209a79fb2cd1413788334b5216070b/68747470733a2f2f68756767696e67666163652e636f2f6672616e6369737a7a6a2f4c656666612f7265736f6c76652f6d61696e2f6173736574732f7669735f726573756c742e706e67)

## Installation

[](#installation)

Create a conda environment and install requirements:

conda create -n leffa python==3.10
conda activate leffa
cd Leffa
pip install -r requirements.txt

## Gradio App

[](#gradio-app)

Run locally:

python app.py

## Evaluation

[](#evaluation)

We use this [code](https://github.com/franciszzj/VtonEval) for metric evaluation.

## Star History

[](#star-history)

[![Star History Chart](https://camo.githubusercontent.com/e4ce5b97ed77d07539ccc88b245288210538b65ab3a8bb87f8f89f5ee625719f/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6672616e6369737a7a6a2f4c6566666126747970653d44617465)](https://star-history.com/#franciszzj/Leffa&Date)

## Acknowledgement

[](#acknowledgement)

Our code is based on [Diffusers](https://github.com/huggingface/diffusers) and [Transformers](https://github.com/huggingface/transformers). We use [SCHP](https://github.com/GoGoDuck912/Self-Correction-Human-Parsing/tree/master) and [DensePose](https://github.com/facebookresearch/DensePose) to generate masks and densepose in our [Demo](https://huggingface.co/spaces/franciszzj/Leffa). We also referred to the code of [IDM-VTON](https://github.com/yisol/IDM-VTON) and [CatVTON](https://github.com/Zheng-Chong/CatVTON).

## Citation

[](#citation)

If you find our work helpful or inspiring, please feel free to cite it.

```
@article{zhou2024learning,
  title={Learning Flow Fields in Attention for Controllable Person Image Generation}, 
  author={Zhou, Zijian and Liu, Shikun and Han, Xiao and Liu, Haozhe and Ng, Kam Woh and Xie, Tian and Cong, Yuren and Li, Hang and Xu, Mengmeng and Pérez-Rúa, Juan-Manuel and Patel, Aditya and Xiang, Tao and Shi, Miaojing and He, Sen},
  journal={arXiv preprint arXiv:2412.08486},
  year={2024},
}
```

## About

\[CVPR 2025\] Learning Flow Fields in Attention for Controllable Person Image Generation

[huggingface.co/spaces/franciszzj/Leffa](https://huggingface.co/spaces/franciszzj/Leffa)

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

[Activity](/franciszzj/Leffa/activity)

### Stars

**1.7k** stars

### Watchers

**16** watching

### Forks

[**185** forks](/franciszzj/Leffa/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Ffranciszzj%2FLeffa&report=franciszzj+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.
