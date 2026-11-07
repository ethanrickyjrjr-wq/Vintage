<!-- source: https://github.com/levihsu/OOTDiffusion, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - levihsu/OOTDiffusion: \[AAAI 2025\] Official implementation of "OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on" · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Flevihsu%2FOOTDiffusion)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Flevihsu%2FOOTDiffusion)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=levihsu%2FOOTDiffusion)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/levihsu/OOTDiffusion)

![levihsu](https://avatars.githubusercontent.com/u/33045876?s=60&v=4)

**[OOTDiffusion](/levihsu/OOTDiffusion)**

Public

-   [Notifications](/login?return_to=%2Flevihsu%2FOOTDiffusion)You must be signed in to change notification settings
-   [Fork952 (952)](/login?return_to=%2Flevihsu%2FOOTDiffusion)
-   [Star6.6k (6.6k)](/login?return_to=%2Flevihsu%2FOOTDiffusion)You must be signed in to star a repository

## About

\[AAAI 2025\] Official implementation of "OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on"

### Resources

[Readme](#readme-ov-file)

[License](#License-1-ov-file)

[Activity](/levihsu/OOTDiffusion/activity)

### Stars

**6.6k** stars

### Watchers

**78** watching

### Forks

[**952** forks](/levihsu/OOTDiffusion/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Flevihsu%2FOOTDiffusion&report=levihsu+%28user%29)

[Branches](/levihsu/OOTDiffusion/branches)[Tags](/levihsu/OOTDiffusion/tags)

[](/levihsu/OOTDiffusion/branches)[](/levihsu/OOTDiffusion/tags)

Open more actions menu

## Latest commit

## History

[20 Commits](/levihsu/OOTDiffusion/commits/main/)

[](/levihsu/OOTDiffusion/commits/main/)20 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[checkpoints](/levihsu/OOTDiffusion/tree/main/checkpoints "checkpoints")

[checkpoints](/levihsu/OOTDiffusion/tree/main/checkpoints "checkpoints")

[images](/levihsu/OOTDiffusion/tree/main/images "images")

[images](/levihsu/OOTDiffusion/tree/main/images "images")

[ootd](/levihsu/OOTDiffusion/tree/main/ootd "ootd")

[ootd](/levihsu/OOTDiffusion/tree/main/ootd "ootd")

[preprocess](/levihsu/OOTDiffusion/tree/main/preprocess "preprocess")

[preprocess](/levihsu/OOTDiffusion/tree/main/preprocess "preprocess")

[run](/levihsu/OOTDiffusion/tree/main/run "run")

[run](/levihsu/OOTDiffusion/tree/main/run "run")

[.gitignore](/levihsu/OOTDiffusion/blob/main/.gitignore ".gitignore")

[.gitignore](/levihsu/OOTDiffusion/blob/main/.gitignore ".gitignore")

[LICENSE](/levihsu/OOTDiffusion/blob/main/LICENSE "LICENSE")

[LICENSE](/levihsu/OOTDiffusion/blob/main/LICENSE "LICENSE")

[README.md](/levihsu/OOTDiffusion/blob/main/README.md "README.md")

[README.md](/levihsu/OOTDiffusion/blob/main/README.md "README.md")

[requirements.txt](/levihsu/OOTDiffusion/blob/main/requirements.txt "requirements.txt")

[requirements.txt](/levihsu/OOTDiffusion/blob/main/requirements.txt "requirements.txt")

## Repository files navigation

# OOTDiffusion

[](#ootdiffusion)

This repository is the official implementation of OOTDiffusion

🤗 [Try out OOTDiffusion](https://huggingface.co/spaces/levihsu/OOTDiffusion)

(Thanks to [ZeroGPU](https://huggingface.co/zero-gpu-explorers) for providing A100 GPUs)

> **OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on** \[[arXiv paper](https://arxiv.org/abs/2403.01779)\]  
> [Yuhao Xu](http://levihsu.github.io/), [Tao Gu](https://github.com/T-Gu), [Weifeng Chen](https://github.com/ShineChen1024), [Chengcai Chen](https://www.researchgate.net/profile/Chengcai-Chen)  
> Xiao-i Research

Our model checkpoints trained on [VITON-HD](https://github.com/shadow2496/VITON-HD) (half-body) and [Dress Code](https://github.com/aimagelab/dress-code) (full-body) have been released

-   🤗 [Hugging Face link](https://huggingface.co/levihsu/OOTDiffusion) for _**checkpoints**_ (ootd, humanparsing, and openpose)
-   📢📢 We support ONNX for [humanparsing](https://github.com/GoGoDuck912/Self-Correction-Human-Parsing) now. Most environmental issues should have been addressed : )
-   Please also download [clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) into _**checkpoints**_ folder
-   We've only tested our code and models on Linux (Ubuntu 22.04)

[![demo](/levihsu/OOTDiffusion/raw/main/images/demo.png)](/levihsu/OOTDiffusion/blob/main/images/demo.png)  [![workflow](/levihsu/OOTDiffusion/raw/main/images/workflow.png)](/levihsu/OOTDiffusion/blob/main/images/workflow.png) 

## Installation

[](#installation)

1.  Clone the repository

git clone https://github.com/levihsu/OOTDiffusion

2.  Create a conda environment and install the required packages

conda create -n ootd python==3.10
conda activate ootd
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
pip install -r requirements.txt

## Inference

[](#inference)

1.  Half-body model

cd OOTDiffusion/run
python run\_ootd.py --model\_path <model-image-path\> --cloth\_path <cloth-image-path\> --scale 2.0 --sample 4

2.  Full-body model

> Garment category must be paired: 0 = upperbody; 1 = lowerbody; 2 = dress

cd OOTDiffusion/run
python run\_ootd.py --model\_path <model-image-path\> --cloth\_path <cloth-image-path\> --model\_type dc --category 2 --scale 2.0 --sample 4

## Citation

[](#citation)

```
@article{xu2024ootdiffusion,
  title={OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on},
  author={Xu, Yuhao and Gu, Tao and Chen, Weifeng and Chen, Chengcai},
  journal={arXiv preprint arXiv:2403.01779},
  year={2024}
}
```

## Star History

[](#star-history)

[![Star History Chart](https://camo.githubusercontent.com/263afa97fcd3eb0167a5586774e15cca05ff1ba6a2eae372fcdb9b27c9e24326/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6c6576696873752f4f4f54446966667573696f6e26747970653d44617465)](https://star-history.com/#levihsu/OOTDiffusion&Date)

## TODO List

[](#todo-list)

-    Paper
-    Gradio demo
-    Inference code
-    Model weights
-    Training code

## About

\[AAAI 2025\] Official implementation of "OOTDiffusion: Outfitting Fusion based Latent Diffusion for Controllable Virtual Try-on"

### Resources

[Readme](#readme-ov-file)

[License](#License-1-ov-file)

[Activity](/levihsu/OOTDiffusion/activity)

### Stars

**6.6k** stars

### Watchers

**78** watching

### Forks

[**952** forks](/levihsu/OOTDiffusion/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Flevihsu%2FOOTDiffusion&report=levihsu+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.
