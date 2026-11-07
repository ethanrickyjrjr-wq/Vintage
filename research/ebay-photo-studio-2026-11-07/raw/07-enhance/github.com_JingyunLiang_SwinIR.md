<!-- source: https://github.com/JingyunLiang/SwinIR, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - JingyunLiang/SwinIR: SwinIR: Image Restoration Using Swin Transformer (official repository) · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FJingyunLiang%2FSwinIR)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FJingyunLiang%2FSwinIR)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=JingyunLiang%2FSwinIR)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/JingyunLiang/SwinIR)

![JingyunLiang](https://avatars.githubusercontent.com/u/17873150?s=60&v=4)

**[SwinIR](/JingyunLiang/SwinIR)**

Public

-   [Notifications](/login?return_to=%2FJingyunLiang%2FSwinIR)You must be signed in to change notification settings
-   [Fork668 (668)](/login?return_to=%2FJingyunLiang%2FSwinIR)
-   [Star5.6k (5.6k)](/login?return_to=%2FJingyunLiang%2FSwinIR)You must be signed in to star a repository

## About

SwinIR: Image Restoration Using Swin Transformer (official repository)

[arxiv.org/abs/2108.10257](https://arxiv.org/abs/2108.10257)

### Topics

[compression-artifact-reduction](/topics/compression-artifact-reduction)[deblocking](/topics/deblocking)[decompression](/topics/decompression)[denoising](/topics/denoising)[image-deblocking](/topics/image-deblocking)[image-denoising](/topics/image-denoising)[image-restoration](/topics/image-restoration)[image-sr](/topics/image-sr)[image-super-resolution](/topics/image-super-resolution)[lightweight-image-super-resolution](/topics/lightweight-image-super-resolution)[low-level-vision](/topics/low-level-vision)[real-world-image-super-resolution](/topics/real-world-image-super-resolution)[restoration](/topics/restoration)[super-resolution](/topics/super-resolution)[transformer](/topics/transformer)[vision-transformer](/topics/vision-transformer)

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

[Activity](/JingyunLiang/SwinIR/activity)

### Stars

**5.6k** stars

### Watchers

**49** watching

### Forks

[**668** forks](/JingyunLiang/SwinIR/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FJingyunLiang%2FSwinIR&report=JingyunLiang+%28user%29)

[Branches](/JingyunLiang/SwinIR/branches)[Tags](/JingyunLiang/SwinIR/tags)

[](/JingyunLiang/SwinIR/branches)[](/JingyunLiang/SwinIR/tags)

Open more actions menu

## Latest commit

## History

[66 Commits](/JingyunLiang/SwinIR/commits/main/)

[](/JingyunLiang/SwinIR/commits/main/)66 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[figs](/JingyunLiang/SwinIR/tree/main/figs "figs")

[figs](/JingyunLiang/SwinIR/tree/main/figs "figs")

[model\_zoo](/JingyunLiang/SwinIR/tree/main/model_zoo "model_zoo")

[model\_zoo](/JingyunLiang/SwinIR/tree/main/model_zoo "model_zoo")

[models](/JingyunLiang/SwinIR/tree/main/models "models")

[models](/JingyunLiang/SwinIR/tree/main/models "models")

[testsets](/JingyunLiang/SwinIR/tree/main/testsets "testsets")

[testsets](/JingyunLiang/SwinIR/tree/main/testsets "testsets")

[utils](/JingyunLiang/SwinIR/tree/main/utils "utils")

[utils](/JingyunLiang/SwinIR/tree/main/utils "utils")

[LICENSE](/JingyunLiang/SwinIR/blob/main/LICENSE "LICENSE")

[LICENSE](/JingyunLiang/SwinIR/blob/main/LICENSE "LICENSE")

[README.md](/JingyunLiang/SwinIR/blob/main/README.md "README.md")

[README.md](/JingyunLiang/SwinIR/blob/main/README.md "README.md")

[cog.yaml](/JingyunLiang/SwinIR/blob/main/cog.yaml "cog.yaml")

[cog.yaml](/JingyunLiang/SwinIR/blob/main/cog.yaml "cog.yaml")

[download-weights.sh](/JingyunLiang/SwinIR/blob/main/download-weights.sh "download-weights.sh")

[download-weights.sh](/JingyunLiang/SwinIR/blob/main/download-weights.sh "download-weights.sh")

[main\_test\_swinir.py](/JingyunLiang/SwinIR/blob/main/main_test_swinir.py "main_test_swinir.py")

[main\_test\_swinir.py](/JingyunLiang/SwinIR/blob/main/main_test_swinir.py "main_test_swinir.py")

[predict.py](/JingyunLiang/SwinIR/blob/main/predict.py "predict.py")

[predict.py](/JingyunLiang/SwinIR/blob/main/predict.py "predict.py")

## Repository files navigation

# SwinIR: Image Restoration Using Swin Transformer

[](#swinir-image-restoration-using-swin-transformer)

[Jingyun Liang](https://jingyunliang.github.io), [Jiezhang Cao](https://www.jiezhangcao.com/), [Guolei Sun](https://vision.ee.ethz.ch/people-details.MjYzMjMw.TGlzdC8zMjg5LC0xOTcxNDY1MTc4.html), [Kai Zhang](https://cszn.github.io/), [Luc Van Gool](https://scholar.google.com/citations?user=TwMib_QAAAAJ&hl=en), [Radu Timofte](http://people.ee.ethz.ch/~timofter/)

Computer Vision Lab, ETH Zurich

* * *

[![arXiv](https://camo.githubusercontent.com/846127fd337037ea62290eae21b82f23e5a64070df2f3252d6b86ead440326de/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d50617065722d253343434f4c4f522533452e737667)](https://arxiv.org/abs/2108.10257) [![GitHub Stars](https://camo.githubusercontent.com/e125a7e2b5f009d187134c6b36970b15764519405d082bac02b0e5821148f933/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4a696e6779756e4c69616e672f5377696e49523f7374796c653d736f6369616c)](https://github.com/JingyunLiang/SwinIR) [![download](https://camo.githubusercontent.com/27e6834ffee6a57b1d10d0d574781b912324d86cc5e4004ff333419599093fad/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f4a696e6779756e4c69616e672f5377696e49522f746f74616c2e737667)](https://github.com/JingyunLiang/SwinIR/releases) [![visitors](https://camo.githubusercontent.com/1ca830ca0e8dabbef1e4664fcdf4a0f326419105d27a15eab9bca65c6efb4ee0/68747470733a2f2f76697369746f722d62616467652e676c697463682e6d652f62616467653f706167655f69643d6a696e6779756e6c69616e672f5377696e4952)](https://camo.githubusercontent.com/1ca830ca0e8dabbef1e4664fcdf4a0f326419105d27a15eab9bca65c6efb4ee0/68747470733a2f2f76697369746f722d62616467652e676c697463682e6d652f62616467653f706167655f69643d6a696e6779756e6c69616e672f5377696e4952) [](https://colab.research.google.com/gist/JingyunLiang/a5e3e54bc9ef8d7bf594f6fee8208533/swinir-demo-on-real-world-image-sr.ipynb)[![google colab logo](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/gist/JingyunLiang/a5e3e54bc9ef8d7bf594f6fee8208533/swinir-demo-on-real-world-image-sr.ipynb) [![](https://camo.githubusercontent.com/251a3f751b955610d6cd609abc89ca55d9460d4a4a850991aacb55a1c70cc6d4/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d5265706c6963617465266d6573736167653d44656d6f20616e6420446f636b657220496d61676526636f6c6f723d626c7565)](https://replicate.ai/jingyunliang/swinir) [![PlayTorch Demo](https://github.com/facebookresearch/playtorch/raw/main/website/static/assets/playtorch_badge.svg)](https://playtorch.dev/snack/@playtorch/swinir/) [Gradio Web Demo](https://huggingface.co/spaces/akhaliq/SwinIR)

This repository is the official PyTorch implementation of SwinIR: Image Restoration Using Shifted Window Transformer ([arxiv](https://arxiv.org/pdf/2108.10257.pdf), [supp](https://github.com/JingyunLiang/SwinIR/releases), [pretrained models](https://github.com/JingyunLiang/SwinIR/releases), [visual results](https://github.com/JingyunLiang/SwinIR/releases)). SwinIR achieves **state-of-the-art performance** in

-   bicubic/lighweight/real-world image SR
-   grayscale/color image denoising
-   grayscale/color JPEG compression artifact reduction

  

🚀 🚀 🚀 **News**:

-   **Aug. 16, 2022**: Add PlayTorch Demo on running the real-world image SR model on mobile devices [![PlayTorch Demo](https://github.com/facebookresearch/playtorch/raw/main/website/static/assets/playtorch_badge.svg)](https://playtorch.dev/snack/@playtorch/swinir/).
-   **Aug. 01, 2022**: Add pretrained models and results on JPEG compression artifact reduction for color images.
-   **Jun. 10, 2022**: See our work on video restoration 🔥🔥🔥 [VRT: A Video Restoration Transformer](https://github.com/JingyunLiang/VRT) [![GitHub Stars](https://camo.githubusercontent.com/b990b62b5cdcd14e8d94ef61d0d94fcef8e79bb2e8e8334167ead5c9e416d587/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4a696e6779756e4c69616e672f5652543f7374796c653d736f6369616c)](https://github.com/JingyunLiang/VRT) [![download](https://camo.githubusercontent.com/4622370d21995903854cc03bb94d5b29d3f59b39c22a3595d467636b7f0bfffa/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f4a696e6779756e4c69616e672f5652542f746f74616c2e737667)](https://github.com/JingyunLiang/VRT/releases) and [RVRT: Recurrent Video Restoration Transformer](https://github.com/JingyunLiang/RVRT) [![GitHub Stars](https://camo.githubusercontent.com/13380c72c35d7a08c7ca5f910662ff56398ca0b3df9bb1e0b15f0531c91b72fc/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4a696e6779756e4c69616e672f525652543f7374796c653d736f6369616c)](https://github.com/JingyunLiang/RVRT) [![download](https://camo.githubusercontent.com/2a6a920e7392296d68a54523b84cdb977b3e1cf44ef29046bc4ded426a091e72/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f4a696e6779756e4c69616e672f525652542f746f74616c2e737667)](https://github.com/JingyunLiang/RVRT/releases) for video SR, video deblurring, video denoising, video frame interpolation and space-time video SR.
-   **Sep. 07, 2021**: We provide an interactive online Colab demo for real-world image SR [![google colab logo](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/gist/JingyunLiang/a5e3e54bc9ef8d7bf594f6fee8208533/swinir-demo-on-real-world-image-sr.ipynb)🔥 for comparison with [the first practical degradation model BSRGAN (ICCV2021) ![GitHub Stars](https://camo.githubusercontent.com/29b9ef3ea1128e1936c90030b7a479b750f992797bd51bcf9d449bc791bbab74/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f63737a6e2f42535247414e3f7374796c653d736f6369616c)](https://github.com/cszn/BSRGAN) and a recent model RealESRGAN. Try to super-resolve your own images on Colab!

Real-World Image (x4)

[BSRGAN, ICCV2021](https://github.com/cszn/BSRGAN)

[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

SwinIR (ours)

SwinIR-Large (ours)

[![](/JingyunLiang/SwinIR/raw/main/figs/ETH_LR.png)](/JingyunLiang/SwinIR/blob/main/figs/ETH_LR.png)

[![](/JingyunLiang/SwinIR/raw/main/figs/ETH_BSRGAN.png)](/JingyunLiang/SwinIR/blob/main/figs/ETH_BSRGAN.png)

[![](/JingyunLiang/SwinIR/raw/main/figs/ETH_realESRGAN.jpg)](/JingyunLiang/SwinIR/blob/main/figs/ETH_realESRGAN.jpg)

[![](/JingyunLiang/SwinIR/raw/main/figs/ETH_SwinIR.png)](/JingyunLiang/SwinIR/blob/main/figs/ETH_SwinIR.png)

[![](/JingyunLiang/SwinIR/raw/main/figs/ETH_SwinIR-L.png)](/JingyunLiang/SwinIR/blob/main/figs/ETH_SwinIR-L.png)

[![](/JingyunLiang/SwinIR/raw/main/figs/OST_009_crop_LR.png)](/JingyunLiang/SwinIR/blob/main/figs/OST_009_crop_LR.png)

[![](/JingyunLiang/SwinIR/raw/main/figs/OST_009_crop_BSRGAN.png)](/JingyunLiang/SwinIR/blob/main/figs/OST_009_crop_BSRGAN.png)

[![](/JingyunLiang/SwinIR/raw/main/figs/OST_009_crop_realESRGAN.png)](/JingyunLiang/SwinIR/blob/main/figs/OST_009_crop_realESRGAN.png)

[![](/JingyunLiang/SwinIR/raw/main/figs/OST_009_crop_SwinIR.png)](/JingyunLiang/SwinIR/blob/main/figs/OST_009_crop_SwinIR.png)

[![](/JingyunLiang/SwinIR/raw/main/figs/OST_009_crop_SwinIR-L.png)](/JingyunLiang/SwinIR/blob/main/figs/OST_009_crop_SwinIR-L.png)

-   _**Aug. 26, 2021**: See our recent work on [real-world image SR: a pratical degrdation model BSRGAN, ICCV2021](https://github.com/cszn/BSRGAN) [![GitHub Stars](https://camo.githubusercontent.com/29b9ef3ea1128e1936c90030b7a479b750f992797bd51bcf9d449bc791bbab74/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f63737a6e2f42535247414e3f7374796c653d736f6369616c)](https://github.com/cszn/BSRGAN)_ 
-   _**Aug. 26, 2021**: See our recent work on [generative modelling of image SR and image rescaling: normalizing-flow-based HCFlow, ICCV2021](https://github.com/JingyunLiang/HCFlow) [![GitHub Stars](https://camo.githubusercontent.com/0f9ce6b9263d327cc6c5cd8c21c2a2aa69b936c45513e7f33ad4d01fa45af1a8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4a696e6779756e4c69616e672f4843466c6f773f7374796c653d736f6369616c)](https://github.com/JingyunLiang/HCFlow) [](https://colab.research.google.com/gist/JingyunLiang/cdb3fef89ebd174eaa43794accb6f59d/hcflow-demo-on-x8-face-image-sr.ipynb)[![google colab logo](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/gist/JingyunLiang/cdb3fef89ebd174eaa43794accb6f59d/hcflow-demo-on-x8-face-image-sr.ipynb)_  
-   _**Aug. 26, 2021**: See our recent work on [blind SR: spatially variant kernel estimation (MANet, ICCV2021)](https://github.com/JingyunLiang/MANet) [![GitHub Stars](https://camo.githubusercontent.com/13796ae8d9a14565c0e23d90197e0690676c242d9ad4890212163f071c92a559/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4a696e6779756e4c69616e672f4d414e65743f7374796c653d736f6369616c)](https://github.com/JingyunLiang/MANet) [](https://colab.research.google.com/gist/JingyunLiang/4ed2524d6e08343710ee408a4d997e1c/manet-demo-on-spatially-variant-kernel-estimation.ipynb)[![google colab logo](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/gist/JingyunLiang/4ed2524d6e08343710ee408a4d997e1c/manet-demo-on-spatially-variant-kernel-estimation.ipynb) and [unsupervised kernel estimation (FKP, CVPR2021)](https://github.com/JingyunLiang/FKP) [![GitHub Stars](https://camo.githubusercontent.com/5726b7235b7f17997147ee3446c220efa878f80fb16c017c9463898c28acdf95/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f4a696e6779756e4c69616e672f464b503f7374796c653d736f6369616c)](https://github.com/JingyunLiang/FKP)_ 

* * *

> Image restoration is a long-standing low-level vision problem that aims to restore high-quality images from low-quality images (e.g., downscaled, noisy and compressed images). While state-of-the-art image restoration methods are based on convolutional neural networks, few attempts have been made with Transformers which show impressive performance on high-level vision tasks. In this paper, we propose a strong baseline model SwinIR for image restoration based on the Swin Transformer. SwinIR consists of three parts: shallow feature extraction, deep feature extraction and high-quality image reconstruction. In particular, the deep feature extraction module is composed of several residual Swin Transformer blocks (RSTB), each of which has several Swin Transformer layers together with a residual connection. We conduct experiments on three representative tasks: image super-resolution (including classical, lightweight and real-world image super-resolution), image denoising (including grayscale and color image denoising) and JPEG compression artifact reduction. Experimental results demonstrate that SwinIR outperforms state-of-the-art methods on different tasks by up to 0.14~0.45dB, while the total number of parameters can be reduced by up to 67%.

[![](/JingyunLiang/SwinIR/raw/main/figs/SwinIR_archi.png)](/JingyunLiang/SwinIR/blob/main/figs/SwinIR_archi.png)

#### Contents

[](#contents)

1.  [Training](#Training)
2.  [Testing](#Testing)
3.  [Results](#Results)
4.  [Citation](#Citation)
5.  [License and Acknowledgement](#License-and-Acknowledgement)

### Training

[](#training)

Used training and testing sets can be downloaded as follows:

Task

Training Set

Testing Set

Visual Results

classical/lightweight image SR

[DIV2K](https://cv.snu.ac.kr/research/EDSR/DIV2K.tar) (800 training images) or DIV2K +[Flickr2K](https://cv.snu.ac.kr/research/EDSR/Flickr2K.tar) (2650 images)

Set5 + Set14 + BSD100 + Urban100 + Manga109 [download all](https://drive.google.com/drive/folders/1B3DJGQKB6eNdwuQIhdskA64qUuVKLZ9u)

[here](https://github.com/JingyunLiang/SwinIR/releases)

real-world image SR

SwinIR-M (middle size): [DIV2K](https://cv.snu.ac.kr/research/EDSR/DIV2K.tar) (800 training images) +[Flickr2K](https://cv.snu.ac.kr/research/EDSR/Flickr2K.tar) (2650 images) + [OST](https://openmmlab.oss-cn-hangzhou.aliyuncs.com/datasets/OST_dataset.zip) ([alternative link](https://drive.google.com/drive/folders/1iZfzAxAwOpeutz27HC56_y5RNqnsPPKr), 10324 images for sky,water,grass,mountain,building,plant,animal)  
SwinIR-L (large size): DIV2K + Flickr2K + OST + [WED](http://ivc.uwaterloo.ca/database/WaterlooExploration/exploration_database_and_code.rar)(4744 images) + [FFHQ](https://drive.google.com/drive/folders/1tZUcXDBeOibC6jcMCtgRRz67pzrAHeHL) (first 2000 images, face) + Manga109 (manga) + [SCUT-CTW1500](https://universityofadelaide.box.com/shared/static/py5uwlfyyytbb2pxzq9czvu6fuqbjdh8.zip) (first 100 training images, texts)  
  
\***We use the pionnerring practical degradation model from [BSRGAN, ICCV2021 ![GitHub Stars](https://camo.githubusercontent.com/29b9ef3ea1128e1936c90030b7a479b750f992797bd51bcf9d449bc791bbab74/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f63737a6e2f42535247414e3f7374796c653d736f6369616c)](https://github.com/cszn/BSRGAN)** 

[RealSRSet+5images](https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/RealSRSet+5images.zip)

[here](https://github.com/JingyunLiang/SwinIR/releases)

color/grayscale image denoising

[DIV2K](https://cv.snu.ac.kr/research/EDSR/DIV2K.tar) (800 training images) + [Flickr2K](https://cv.snu.ac.kr/research/EDSR/Flickr2K.tar) (2650 images) + [BSD500](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz) (400 training&testing images) + [WED](http://ivc.uwaterloo.ca/database/WaterlooExploration/exploration_database_and_code.rar)(4744 images)  
  
\*BSD68/BSD100 images are not used in training.

grayscale: Set12 + BSD68 + Urban100  
color: CBSD68 + Kodak24 + McMaster + Urban100 [download all](https://github.com/cszn/FFDNet/tree/master/testsets)

[here](https://github.com/JingyunLiang/SwinIR/releases)

grayscale/color JPEG compression artifact reduction

[DIV2K](https://cv.snu.ac.kr/research/EDSR/DIV2K.tar) (800 training images) + [Flickr2K](https://cv.snu.ac.kr/research/EDSR/Flickr2K.tar) (2650 images) + [BSD500](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz) (400 training&testing images) + [WED](http://ivc.uwaterloo.ca/database/WaterlooExploration/exploration_database_and_code.rar)(4744 images)

grayscale: Classic5 +LIVE1 [download all](https://github.com/cszn/DnCNN/tree/master/testsets)

[here](https://github.com/JingyunLiang/SwinIR/releases)

The training code is at [KAIR](https://github.com/cszn/KAIR/blob/master/docs/README_SwinIR.md).

## Testing (without preparing datasets)

[](#testing-without-preparing-datasets)

For your convience, we provide some example datasets (~20Mb) in `/testsets`. If you just want codes, downloading `models/network_swinir.py`, `utils/util_calculate_psnr_ssim.py` and `main_test_swinir.py` is enough. Following commands will download [pretrained models](https://github.com/JingyunLiang/SwinIR/releases) **automatically** and put them in `model_zoo/swinir`. **[All visual results of SwinIR can be downloaded here](https://github.com/JingyunLiang/SwinIR/releases)**.

We also provide an [online Colab demo for real-world image SR](https://colab.research.google.com/gist/JingyunLiang/a5e3e54bc9ef8d7bf594f6fee8208533/swinir-demo-on-real-world-image-sr.ipynb) [![google colab logo](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/gist/JingyunLiang/a5e3e54bc9ef8d7bf594f6fee8208533/swinir-demo-on-real-world-image-sr.ipynb) for comparison with [the first practical degradation model BSRGAN (ICCV2021) ![GitHub Stars](https://camo.githubusercontent.com/29b9ef3ea1128e1936c90030b7a479b750f992797bd51bcf9d449bc791bbab74/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f63737a6e2f42535247414e3f7374796c653d736f6369616c)](https://github.com/cszn/BSRGAN) and a recent model [RealESRGAN](https://github.com/xinntao/Real-ESRGAN). Try to test your own images on Colab!

We provide a PlayTorch demo [![PlayTorch Demo](https://github.com/facebookresearch/playtorch/raw/main/website/static/assets/playtorch_badge.svg)](https://playtorch.dev/snack/@playtorch/swinir/) for real-world image SR to showcase how to run the SwinIR model in mobile application built with React Native.

# 001 Classical Image Super-Resolution (middle size)
# Note that --training\_patch\_size is just used to differentiate two different settings in Table 2 of the paper. Images are NOT tested patch by patch.
# (setting1: when model is trained on DIV2K and with training\_patch\_size=48)
python main\_test\_swinir.py --task classical\_sr --scale 2 --training\_patch\_size 48 --model\_path model\_zoo/swinir/001\_classicalSR\_DIV2K\_s48w8\_SwinIR-M\_x2.pth --folder\_lq testsets/Set5/LR\_bicubic/X2 --folder\_gt testsets/Set5/HR
python main\_test\_swinir.py --task classical\_sr --scale 3 --training\_patch\_size 48 --model\_path model\_zoo/swinir/001\_classicalSR\_DIV2K\_s48w8\_SwinIR-M\_x3.pth --folder\_lq testsets/Set5/LR\_bicubic/X3 --folder\_gt testsets/Set5/HR
python main\_test\_swinir.py --task classical\_sr --scale 4 --training\_patch\_size 48 --model\_path model\_zoo/swinir/001\_classicalSR\_DIV2K\_s48w8\_SwinIR-M\_x4.pth --folder\_lq testsets/Set5/LR\_bicubic/X4 --folder\_gt testsets/Set5/HR
python main\_test\_swinir.py --task classical\_sr --scale 8 --training\_patch\_size 48 --model\_path model\_zoo/swinir/001\_classicalSR\_DIV2K\_s48w8\_SwinIR-M\_x8.pth --folder\_lq testsets/Set5/LR\_bicubic/X8 --folder\_gt testsets/Set5/HR

# (setting2: when model is trained on DIV2K+Flickr2K and with training\_patch\_size=64)
python main\_test\_swinir.py --task classical\_sr --scale 2 --training\_patch\_size 64 --model\_path model\_zoo/swinir/001\_classicalSR\_DF2K\_s64w8\_SwinIR-M\_x2.pth --folder\_lq testsets/Set5/LR\_bicubic/X2 --folder\_gt testsets/Set5/HR
python main\_test\_swinir.py --task classical\_sr --scale 3 --training\_patch\_size 64 --model\_path model\_zoo/swinir/001\_classicalSR\_DF2K\_s64w8\_SwinIR-M\_x3.pth --folder\_lq testsets/Set5/LR\_bicubic/X3 --folder\_gt testsets/Set5/HR
python main\_test\_swinir.py --task classical\_sr --scale 4 --training\_patch\_size 64 --model\_path model\_zoo/swinir/001\_classicalSR\_DF2K\_s64w8\_SwinIR-M\_x4.pth --folder\_lq testsets/Set5/LR\_bicubic/X4 --folder\_gt testsets/Set5/HR
python main\_test\_swinir.py --task classical\_sr --scale 8 --training\_patch\_size 64 --model\_path model\_zoo/swinir/001\_classicalSR\_DF2K\_s64w8\_SwinIR-M\_x8.pth --folder\_lq testsets/Set5/LR\_bicubic/X8 --folder\_gt testsets/Set5/HR

# 002 Lightweight Image Super-Resolution (small size)
python main\_test\_swinir.py --task lightweight\_sr --scale 2 --model\_path model\_zoo/swinir/002\_lightweightSR\_DIV2K\_s64w8\_SwinIR-S\_x2.pth --folder\_lq testsets/Set5/LR\_bicubic/X2 --folder\_gt testsets/Set5/HR
python main\_test\_swinir.py --task lightweight\_sr --scale 3 --model\_path model\_zoo/swinir/002\_lightweightSR\_DIV2K\_s64w8\_SwinIR-S\_x3.pth --folder\_lq testsets/Set5/LR\_bicubic/X3 --folder\_gt testsets/Set5/HR
python main\_test\_swinir.py --task lightweight\_sr --scale 4 --model\_path model\_zoo/swinir/002\_lightweightSR\_DIV2K\_s64w8\_SwinIR-S\_x4.pth --folder\_lq testsets/Set5/LR\_bicubic/X4 --folder\_gt testsets/Set5/HR

# 003 Real-World Image Super-Resolution (use --tile 400 if you run out-of-memory)
# (middle size)
python main\_test\_swinir.py --task real\_sr --scale 4 --model\_path model\_zoo/swinir/003\_realSR\_BSRGAN\_DFO\_s64w8\_SwinIR-M\_x4\_GAN.pth --folder\_lq testsets/RealSRSet+5images --tile

# (larger size + trained on more datasets)
python main\_test\_swinir.py --task real\_sr --scale 4 --large\_model --model\_path model\_zoo/swinir/003\_realSR\_BSRGAN\_DFOWMFC\_s64w8\_SwinIR-L\_x4\_GAN.pth --folder\_lq testsets/RealSRSet+5images

# 004 Grayscale Image Deoising (middle size)
python main\_test\_swinir.py --task gray\_dn --noise 15 --model\_path model\_zoo/swinir/004\_grayDN\_DFWB\_s128w8\_SwinIR-M\_noise15.pth --folder\_gt testsets/Set12
python main\_test\_swinir.py --task gray\_dn --noise 25 --model\_path model\_zoo/swinir/004\_grayDN\_DFWB\_s128w8\_SwinIR-M\_noise25.pth --folder\_gt testsets/Set12
python main\_test\_swinir.py --task gray\_dn --noise 50 --model\_path model\_zoo/swinir/004\_grayDN\_DFWB\_s128w8\_SwinIR-M\_noise50.pth --folder\_gt testsets/Set12

# 005 Color Image Deoising (middle size)
python main\_test\_swinir.py --task color\_dn --noise 15 --model\_path model\_zoo/swinir/005\_colorDN\_DFWB\_s128w8\_SwinIR-M\_noise15.pth --folder\_gt testsets/McMaster
python main\_test\_swinir.py --task color\_dn --noise 25 --model\_path model\_zoo/swinir/005\_colorDN\_DFWB\_s128w8\_SwinIR-M\_noise25.pth --folder\_gt testsets/McMaster
python main\_test\_swinir.py --task color\_dn --noise 50 --model\_path model\_zoo/swinir/005\_colorDN\_DFWB\_s128w8\_SwinIR-M\_noise50.pth --folder\_gt testsets/McMaster

# 006 JPEG Compression Artifact Reduction (middle size, using window\_size=7 because JPEG encoding uses 8x8 blocks)
# grayscale
python main\_test\_swinir.py --task jpeg\_car --jpeg 10 --model\_path model\_zoo/swinir/006\_CAR\_DFWB\_s126w7\_SwinIR-M\_jpeg10.pth --folder\_gt testsets/classic5
python main\_test\_swinir.py --task jpeg\_car --jpeg 20 --model\_path model\_zoo/swinir/006\_CAR\_DFWB\_s126w7\_SwinIR-M\_jpeg20.pth --folder\_gt testsets/classic5
python main\_test\_swinir.py --task jpeg\_car --jpeg 30 --model\_path model\_zoo/swinir/006\_CAR\_DFWB\_s126w7\_SwinIR-M\_jpeg30.pth --folder\_gt testsets/classic5
python main\_test\_swinir.py --task jpeg\_car --jpeg 40 --model\_path model\_zoo/swinir/006\_CAR\_DFWB\_s126w7\_SwinIR-M\_jpeg40.pth --folder\_gt testsets/classic5

# color
python main\_test\_swinir.py --task color\_jpeg\_car --jpeg 10 --model\_path model\_zoo/swinir/006\_colorCAR\_DFWB\_s126w7\_SwinIR-M\_jpeg10.pth --folder\_gt testsets/LIVE1
python main\_test\_swinir.py --task color\_jpeg\_car --jpeg 20 --model\_path model\_zoo/swinir/006\_colorCAR\_DFWB\_s126w7\_SwinIR-M\_jpeg20.pth --folder\_gt testsets/LIVE1
python main\_test\_swinir.py --task color\_jpeg\_car --jpeg 30 --model\_path model\_zoo/swinir/006\_colorCAR\_DFWB\_s126w7\_SwinIR-M\_jpeg30.pth --folder\_gt testsets/LIVE1
python main\_test\_swinir.py --task color\_jpeg\_car --jpeg 40 --model\_path model\_zoo/swinir/006\_colorCAR\_DFWB\_s126w7\_SwinIR-M\_jpeg40.pth --folder\_gt testsets/LIVE1

* * *

## Results

[](#results)

We achieved state-of-the-art performance on classical/lightweight/real-world image SR, grayscale/color image denoising and JPEG compression artifact reduction. Detailed results can be found in the [paper](https://arxiv.org/abs/2108.10257). All visual results of SwinIR can be downloaded [here](https://github.com/JingyunLiang/SwinIR/releases).

Classical Image Super-Resolution (click me)

[![](/JingyunLiang/SwinIR/raw/main/figs/classic_image_sr.png)](/JingyunLiang/SwinIR/blob/main/figs/classic_image_sr.png) [![](/JingyunLiang/SwinIR/raw/main/figs/classic_image_sr_visual.png)](/JingyunLiang/SwinIR/blob/main/figs/classic_image_sr_visual.png)

-   More detailed comparison between SwinIR and a representative CNN-based model RCAN (classical image SR, X4)

Method

Training Set

Training time  
(8GeForceRTX2080Ti  
batch=32, iter=500k)

Y-PSNR/Y-SSIM  
on Manga109

Run time  
(1GeForceRTX2080Ti,  
on 256x256 LR image)\*

#Params

#FLOPs

Testing memory

RCAN

DIV2K

1.6 days

31.22/0.9173

0.180s

15.6M

850.6G

593.1M

SwinIR

DIV2K

1.8 days

31.67/0.9226

0.539s

11.9M

788.6G

986.8M

\* We re-test the runtime when the GPU is idle. We refer to the evluation code [here](https://github.com/cszn/KAIR/blob/master/main_challenge_sr.py).

-   Results on DIV2K-validation (100 images)

Training Set

scale factor

PSNR (RGB)

PSNR (Y)

SSIM (RGB)

SSIM (Y)

DIV2K (800 images)

2

35.25

36.77

0.9423

0.9500

DIV2K+Flickr2K (2650 images)

2

35.34

36.86

0.9430

0.9507

DIV2K (800 images)

3

31.50

32.97

0.8832

0.8965

DIV2K+Flickr2K (2650 images)

3

31.63

33.10

0.8854

0.8985

DIV2K (800 images)

4

29.48

30.94

0.8311

0.8492

DIV2K+Flickr2K (2650 images)

4

29.63

31.08

0.8347

0.8523

Lightweight Image Super-Resolution

[![](/JingyunLiang/SwinIR/raw/main/figs/lightweight_image_sr.png)](/JingyunLiang/SwinIR/blob/main/figs/lightweight_image_sr.png)

Real-World Image Super-Resolution

[![](/JingyunLiang/SwinIR/raw/main/figs/real_world_image_sr.png)](/JingyunLiang/SwinIR/blob/main/figs/real_world_image_sr.png)

Grayscale Image Deoising

[![](/JingyunLiang/SwinIR/raw/main/figs/gray_image_denoising.png)](/JingyunLiang/SwinIR/blob/main/figs/gray_image_denoising.png)

Color Image Deoising

[![](/JingyunLiang/SwinIR/raw/main/figs/color_image_denoising.png)](/JingyunLiang/SwinIR/blob/main/figs/color_image_denoising.png)

JPEG Compression Artifact Reduction

on grayscale images

[![](/JingyunLiang/SwinIR/raw/main/figs/jepg_compress_artfact_reduction.png)](/JingyunLiang/SwinIR/blob/main/figs/jepg_compress_artfact_reduction.png)

on color images

Training Set

quality factor

PSNR (RGB)

PSNR-B (RGB)

SSIM (RGB)

LIVE1

10

28.06

27.76

0.8089

LIVE1

20

30.45

29.97

0.8741

LIVE1

30

31.82

31.24

0.9018

LIVE1

40

32.75

32.12

0.9174

## Citation

[](#citation)

```
@article{liang2021swinir,
  title={SwinIR: Image Restoration Using Swin Transformer},
  author={Liang, Jingyun and Cao, Jiezhang and Sun, Guolei and Zhang, Kai and Van Gool, Luc and Timofte, Radu},
  journal={arXiv preprint arXiv:2108.10257},
  year={2021}
}
```

## License and Acknowledgement

[](#license-and-acknowledgement)

This project is released under the Apache 2.0 license. The codes are based on [Swin Transformer](https://github.com/microsoft/Swin-Transformer) and [KAIR](https://github.com/cszn/KAIR). Please also follow their licenses. Thanks for their awesome works.

## About

SwinIR: Image Restoration Using Swin Transformer (official repository)

[arxiv.org/abs/2108.10257](https://arxiv.org/abs/2108.10257)

### Topics

[compression-artifact-reduction](/topics/compression-artifact-reduction)[deblocking](/topics/deblocking)[decompression](/topics/decompression)[denoising](/topics/denoising)[image-deblocking](/topics/image-deblocking)[image-denoising](/topics/image-denoising)[image-restoration](/topics/image-restoration)[image-sr](/topics/image-sr)[image-super-resolution](/topics/image-super-resolution)[lightweight-image-super-resolution](/topics/lightweight-image-super-resolution)[low-level-vision](/topics/low-level-vision)[real-world-image-super-resolution](/topics/real-world-image-super-resolution)[restoration](/topics/restoration)[super-resolution](/topics/super-resolution)[transformer](/topics/transformer)[vision-transformer](/topics/vision-transformer)

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

[Activity](/JingyunLiang/SwinIR/activity)

### Stars

**5.6k** stars

### Watchers

**49** watching

### Forks

[**668** forks](/JingyunLiang/SwinIR/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FJingyunLiang%2FSwinIR&report=JingyunLiang+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.
