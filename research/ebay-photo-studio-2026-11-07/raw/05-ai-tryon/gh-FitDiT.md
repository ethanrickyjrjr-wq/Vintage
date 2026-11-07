<!-- source: https://github.com/BoyuanJiang/FitDiT, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - BoyuanJiang/FitDiT: Official implementation of "FitDiT: Advancing the Authentic Garment Details for High-fidelity Virtual Try-on" · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FBoyuanJiang%2FFitDiT)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FBoyuanJiang%2FFitDiT)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=BoyuanJiang%2FFitDiT)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/BoyuanJiang/FitDiT)

![BoyuanJiang](https://avatars.githubusercontent.com/u/16739780?s=60&v=4)

**[FitDiT](/BoyuanJiang/FitDiT)**

Public

-   [Notifications](/login?return_to=%2FBoyuanJiang%2FFitDiT)You must be signed in to change notification settings
-   [Fork60 (60)](/login?return_to=%2FBoyuanJiang%2FFitDiT)
-   [Star637 (637)](/login?return_to=%2FBoyuanJiang%2FFitDiT)You must be signed in to star a repository

## About

Official implementation of "FitDiT: Advancing the Authentic Garment Details for High-fidelity Virtual Try-on"

[byjiang.com/FitDiT/](https://byjiang.com/FitDiT/)

### Resources

[Readme](#readme-ov-file)

[License](#License-1-ov-file)

[Activity](/BoyuanJiang/FitDiT/activity)

### Stars

**637** stars

### Watchers

**30** watching

### Forks

[**60** forks](/BoyuanJiang/FitDiT/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FBoyuanJiang%2FFitDiT&report=BoyuanJiang+%28user%29)

[Branches](/BoyuanJiang/FitDiT/branches)[Tags](/BoyuanJiang/FitDiT/tags)

[](/BoyuanJiang/FitDiT/branches)[](/BoyuanJiang/FitDiT/tags)

Open more actions menu

## Latest commit

## History

[18 Commits](/BoyuanJiang/FitDiT/commits/main/)

[](/BoyuanJiang/FitDiT/commits/main/)18 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[examples](/BoyuanJiang/FitDiT/tree/main/examples "examples")

[examples](/BoyuanJiang/FitDiT/tree/main/examples "examples")

[preprocess](/BoyuanJiang/FitDiT/tree/main/preprocess "preprocess")

[preprocess](/BoyuanJiang/FitDiT/tree/main/preprocess "preprocess")

[resource/img](/BoyuanJiang/FitDiT/tree/main/resource/img "This path skips through empty directories")

[resource/img](/BoyuanJiang/FitDiT/tree/main/resource/img "This path skips through empty directories")

[src](/BoyuanJiang/FitDiT/tree/main/src "src")

[src](/BoyuanJiang/FitDiT/tree/main/src "src")

[.gitignore](/BoyuanJiang/FitDiT/blob/main/.gitignore ".gitignore")

[.gitignore](/BoyuanJiang/FitDiT/blob/main/.gitignore ".gitignore")

[LICENSE](/BoyuanJiang/FitDiT/blob/main/LICENSE "LICENSE")

[LICENSE](/BoyuanJiang/FitDiT/blob/main/LICENSE "LICENSE")

[README.md](/BoyuanJiang/FitDiT/blob/main/README.md "README.md")

[README.md](/BoyuanJiang/FitDiT/blob/main/README.md "README.md")

[gradio\_sd3.py](/BoyuanJiang/FitDiT/blob/main/gradio_sd3.py "gradio_sd3.py")

[gradio\_sd3.py](/BoyuanJiang/FitDiT/blob/main/gradio_sd3.py "gradio_sd3.py")

[requirements.txt](/BoyuanJiang/FitDiT/blob/main/requirements.txt "requirements.txt")

[requirements.txt](/BoyuanJiang/FitDiT/blob/main/requirements.txt "requirements.txt")

## Repository files navigation

# FitDiT: Advancing the Authentic Garment Details for High-fidelity Virtual Try-on

[](#fitdit-advancing-the-authentic-garment-details-for-high-fidelity-virtual-try-on)

 [![arxiv](https://camo.githubusercontent.com/b4a464c493de3249a590384f3043f2111592b4204f3adc5efc7d8d9abddb0cd6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d323431312e31303439392d7265643f7374796c653d666c6174266c6f676f3d6172586976266c6f676f436f6c6f723d726564)](https://arxiv.org/abs/2411.10499)[![GitHub](https://camo.githubusercontent.com/cc684b27ce2b960ea5ff80e01f973d8b40b4cb0ecb77b08e42522285d448ec1f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d5265706f2d626c75653f7374796c653d666c6174266c6f676f3d476974487562) ](https://github.com/BoyuanJiang/FitDiT)[![Demo](https://camo.githubusercontent.com/3bd54f66a2c825f679bd0a9314210fc3f31a5402f74fc89d21f1813c5226d2ec/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53706163652d5a65726f4750552d6f72616e67653f7374796c653d666c6174266c6f676f3d47726164696f266c6f676f436f6c6f723d726564) ](https://huggingface.co/spaces/BoyuanJiang/FitDiT)[![Demo](https://camo.githubusercontent.com/da624c750a97fddaee16e45e061891b630cbf346807ab4c2087bd15c236f3bee/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f44656d6f2d47726164696f2d676f6c643f7374796c653d666c6174266c6f676f3d47726164696f266c6f676f436f6c6f723d726564) ](http://demo.fitdit.byjiang.com/)[![huggingface](https://camo.githubusercontent.com/2d200587cf6b90286897a9d247dc684effff73d017ad90a081bb15704ba55011/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48756767696e6720466163652d636b7074732d6f72616e67653f7374796c653d666c6174266c6f676f3d48756767696e6746616365266c6f676f436f6c6f723d6f72616e6765) ](https://huggingface.co/BoyuanJiang/FitDiT)[![webpage](https://camo.githubusercontent.com/066163ce2415b4bec8ad2ced749c07cb2e83c6e271388b84d4bf850592aa3c10/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f576562706167652d50726f6a6563742d73696c7665723f7374796c653d666c6174266c6f676f3d266c6f676f436f6c6f723d6f72616e6765) ](https://byjiang.com/FitDiT/)[![License](https://camo.githubusercontent.com/93e689e5f2adc357a48799ec68139fca17c13847436ad11a03a31dece82c862a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d43432042592d2d4e432d2d53412d2d342e302d6c69676874677265656e3f7374796c653d666c6174266c6f676f3d4c6973656e6365)](https://raw.githubusercontent.com/BoyuanJiang/FitDiT/refs/heads/main/LICENSE)

👋 Join our [QQ Chat Group](/BoyuanJiang/FitDiT/blob/main/resource/img/QQ_group.jpg)

**FitDiT** is designed for high-fidelity virtual try-on using Diffusion Transformers (DiT).

[![](/BoyuanJiang/FitDiT/raw/main/resource/img/teaser.jpg)](/BoyuanJiang/FitDiT/blob/main/resource/img/teaser.jpg)

## Updates

[](#updates)

-   **`2025/1/16`**: We provide the [ComfyUI version of FitDiT](https://github.com/BoyuanJiang/FitDiT/tree/FitDiT-ComfyUI), you can use FitDiT in ComfyUI now.
-   **`2025/1/9`**: We provide a [**Huggingface Space**](https://huggingface.co/spaces/BoyuanJiang/FitDiT) of FitDiT, thanks for Huggingface community GPU grant for providing the GPU resources.
-   **`2024/12/20`**: The FitDiT [**model weight**](https://huggingface.co/BoyuanJiang/FitDiT) is available.
-   **`2024/12/17`**: Inference code is released.
-   **`2024/12/4`**: Our [**Online Demo**](http://demo.fitdit.byjiang.com/) is released.
-   **`2024/11/25`**: Our [**Complex Virtual Dressing Dataset (CVDD)**](https://huggingface.co/datasets/BoyuanJiang/CVDD) is released.
-   **`2024/11/15`**: Our [**FitDiT paper**](https://arxiv.org/abs/2411.10499) is available.

## Gradio Demo

[](#gradio-demo)

Our algorithm is divided into two steps. The first step is to generate the mask of the try-on area, and the second step is to try-on in the mask area.

### Step1: Run Mask

[](#step1-run-mask)

You can simpley get try-on mask by click **Step1: Run Mask** at the right side of gradio demo. If the automatically generated mask are not well covered the area where you want to try-on, you can either adjust the mask by:

1.  Drag the slider of _mask offset top_, _mask offset bottom_, _mask offset left_ or _mask offset right_ and then click **Step1: Run Mask** button, this will re-generate mask.
    
    [![mask_offset](/BoyuanJiang/FitDiT/raw/main/resource/img/mask_offset.jpg)](/BoyuanJiang/FitDiT/blob/main/resource/img/mask_offset.jpg)
    
2.  Using the brush or eraser tool to edit the automatically generated mask
    
    [![manually_adjust](/BoyuanJiang/FitDiT/raw/main/resource/img/manually_adjust.jpg)](/BoyuanJiang/FitDiT/blob/main/resource/img/manually_adjust.jpg)
    

### Step2: Run Try-on

[](#step2-run-try-on)

After generating a suitable mask, you can get the try-on results by click **Step2: Run Try-on**. In the Try-on resolution drop-down box, you can select a suitable processing resolution. In our online demo, the default resolution is 1152x1536, which means that the input model image and garment image will be pad and resized to this resolution before being fed into the model.

## Local Demo

[](#local-demo)

First apply access of FitDiT [model weight](https://huggingface.co/BoyuanJiang/FitDiT), then clone model to _local\_model\_dir_

### Enviroment

[](#enviroment)

We test our model with following enviroment

```
torch==2.4.0
torchvision==0.19.0
diffusers==0.31.0
transformers==4.39.3
gradio==5.8.0
onnxruntime-gpu==1.20.1
```

### Run gradio locally

[](#run-gradio-locally)

```
# Run model with bf16 without any offload, fastest inference and most memory
python gradio_sd3.py --model_path local_model_dir

# Run model with fp16
python gradio_sd3.py --model_path local_model_dir --fp16

# Run model with fp16 and cpu offload, moderate inference and moderate memory
python gradio_sd3.py --model_path local_model_dir --fp16 --offload

# Run model with fp16 and aggressive cpu offload, slowest inference and less memory
python gradio_sd3.py --model_path local_model_dir --fp16 --aggressive_offload
```

## Third-Party Creations

[](#third-party-creations)

We found there've been some 3rd party applications or tutorial based on our FitDiT. Many thanks for their contribution to the community! If you have any related work that you would like to see displayed, please submit it in the [issue](https://github.com/BoyuanJiang/FitDiT/issues/new). These projects have not been verified by us. If you have any questions, please seek help from the original project authors.

### Tutorial

[](#tutorial)

-   A tutorial of using the comfyui version of FitDiT, from `T8star-Aix` at [youtube](https://www.youtube.com/watch?v=qBQtYYa-bvs) or [bilibili](https://www.bilibili.com/video/BV1U4wpe6EkD/)

### Applications

[](#applications)

-   Local one-click integration package of FitDiT, which can be found at [deepface forum](https://deepface.cc/thread-517-1-1.html)

## Star History

[](#star-history)

[![Star History Chart](https://camo.githubusercontent.com/678404f1fae929b517b1af1cc58aeba3ac4c6125ac5cdc8f3d5e266167992f9a/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d426f7975616e4a69616e672f46697444695426747970653d44617465)](https://star-history.com/#BoyuanJiang/FitDiT&Date)

## Contact

[](#contact)

This model can only be used **for non-commercial use**. For commercial use, please visit [Tencent Cloud](https://cloud.tencent.com/document/product/1668/108532) for support.

## Citation

[](#citation)

If you find our work helpful for your research, please consider citing our work.

```
@misc{jiang2024fitditadvancingauthenticgarment,
      title={FitDiT: Advancing the Authentic Garment Details for High-fidelity Virtual Try-on}, 
      author={Boyuan Jiang and Xiaobin Hu and Donghao Luo and Qingdong He and Chengming Xu and Jinlong Peng and Jiangning Zhang and Chengjie Wang and Yunsheng Wu and Yanwei Fu},
      year={2024},
      eprint={2411.10499},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2411.10499}, 
}
```

## About

Official implementation of "FitDiT: Advancing the Authentic Garment Details for High-fidelity Virtual Try-on"

[byjiang.com/FitDiT/](https://byjiang.com/FitDiT/)

### Resources

[Readme](#readme-ov-file)

[License](#License-1-ov-file)

[Activity](/BoyuanJiang/FitDiT/activity)

### Stars

**637** stars

### Watchers

**30** watching

### Forks

[**60** forks](/BoyuanJiang/FitDiT/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FBoyuanJiang%2FFitDiT&report=BoyuanJiang+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.
