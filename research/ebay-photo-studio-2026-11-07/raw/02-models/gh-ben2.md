<!-- source: https://github.com/PramaLLC/BEN2, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - PramaLLC/BEN2 · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FPramaLLC%2FBEN2)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FPramaLLC%2FBEN2)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=PramaLLC%2FBEN2)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/PramaLLC/BEN2)

![PramaLLC](https://avatars.githubusercontent.com/u/157913250?s=60&v=4)

**[BEN2](/PramaLLC/BEN2)**

Public

-   [Notifications](/login?return_to=%2FPramaLLC%2FBEN2)You must be signed in to change notification settings
-   [Fork38 (38)](/login?return_to=%2FPramaLLC%2FBEN2)
-   [Star297 (297)](/login?return_to=%2FPramaLLC%2FBEN2)You must be signed in to star a repository

## About

No description, website, or topics provided.

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

[Activity](/PramaLLC/BEN2/activity)

### Stars

**297** stars

### Watchers

**6** watching

### Forks

[**38** forks](/PramaLLC/BEN2/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FPramaLLC%2FBEN2&report=PramaLLC+%28user%29)

[Branches](/PramaLLC/BEN2/branches)[Tags](/PramaLLC/BEN2/tags)

[](/PramaLLC/BEN2/branches)[](/PramaLLC/BEN2/tags)

Open more actions menu

## Latest commit

## History

[29 Commits](/PramaLLC/BEN2/commits/main/)

[](/PramaLLC/BEN2/commits/main/)29 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[BEN2\_demo\_pictures](/PramaLLC/BEN2/tree/main/BEN2_demo_pictures "BEN2_demo_pictures")

[BEN2\_demo\_pictures](/PramaLLC/BEN2/tree/main/BEN2_demo_pictures "BEN2_demo_pictures")

[src/ben2](/PramaLLC/BEN2/tree/main/src/ben2 "This path skips through empty directories")

[src/ben2](/PramaLLC/BEN2/tree/main/src/ben2 "This path skips through empty directories")

[.gitignore](/PramaLLC/BEN2/blob/main/.gitignore ".gitignore")

[.gitignore](/PramaLLC/BEN2/blob/main/.gitignore ".gitignore")

[BEN2.py](/PramaLLC/BEN2/blob/main/BEN2.py "BEN2.py")

[BEN2.py](/PramaLLC/BEN2/blob/main/BEN2.py "BEN2.py")

[LICENSE](/PramaLLC/BEN2/blob/main/LICENSE "LICENSE")

[LICENSE](/PramaLLC/BEN2/blob/main/LICENSE "LICENSE")

[README.md](/PramaLLC/BEN2/blob/main/README.md "README.md")

[README.md](/PramaLLC/BEN2/blob/main/README.md "README.md")

[config.json](/PramaLLC/BEN2/blob/main/config.json "config.json")

[config.json](/PramaLLC/BEN2/blob/main/config.json "config.json")

[gitattributes](/PramaLLC/BEN2/blob/main/gitattributes "gitattributes")

[gitattributes](/PramaLLC/BEN2/blob/main/gitattributes "gitattributes")

[inference.py](/PramaLLC/BEN2/blob/main/inference.py "inference.py")

[inference.py](/PramaLLC/BEN2/blob/main/inference.py "inference.py")

[pyproject.toml](/PramaLLC/BEN2/blob/main/pyproject.toml "pyproject.toml")

[pyproject.toml](/PramaLLC/BEN2/blob/main/pyproject.toml "pyproject.toml")

[requirements.txt](/PramaLLC/BEN2/blob/main/requirements.txt "requirements.txt")

[requirements.txt](/PramaLLC/BEN2/blob/main/requirements.txt "requirements.txt")

[setup.py](/PramaLLC/BEN2/blob/main/setup.py "setup.py")

[setup.py](/PramaLLC/BEN2/blob/main/setup.py "setup.py")

## Repository files navigation

# BEN2: Background Erase Network

[](#ben2-background-erase-network)

[![arXiv](https://camo.githubusercontent.com/ab4b955f396b4c25ec455cd5a193e6198e24a565d7754f3ecd6adfd72452b6be/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d323530312e30363233302d6233316231622e737667)](https://arxiv.org/abs/2501.06230) [![HuggingFace](https://camo.githubusercontent.com/1c2830dc729a00b10d113274b45058406f58f4249c8baf958f28baf6a2212301/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d42454e322d626c7565)](https://huggingface.co/PramaLLC/BEN2) [![Website](https://camo.githubusercontent.com/dead866e29b0ffd8332f64b97f8d29bf7bf86feb54f5061c4e9baaa3aa1eb945/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f576562736974652d6261636b67726f756e6465726173652e6e65742d313034323333)](https://backgrounderase.net)

## Overview

[](#overview)

BEN2 (Background Erase Network) introduces a novel approach to foreground segmentation through its innovative Confidence Guided Matting (CGM) pipeline. The architecture employs a refiner network that targets and processes pixels where the base model exhibits lower confidence levels, resulting in more precise and reliable matting results. This model is built on BEN: [![PWC](https://camo.githubusercontent.com/05aa87696703ee28bfecedf79c8909c7071cc2d0ea73c4a8984f0364220a1d45/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e742e7376673f75726c3d68747470733a2f2f70617065727377697468636f64652e636f6d2f62616467652f62656e2d7573696e672d636f6e666964656e63652d6775696465642d6d617474696e672d666f722f646963686f746f6d6f75732d696d6167652d7365676d656e746174696f6e2d6f6e2d6469732d7664)](https://paperswithcode.com/sota/dichotomous-image-segmentation-on-dis-vd?p=ben-using-confidence-guided-matting-for)

## BEN2 access

[](#ben2-access)

BEN2 was trained on the DIS5k and our 22K proprietary segmentation dataset. Our enhanced model delivers superior performance in hair matting, 4K processing, object segmentation, and edge refinement. Our Base model is open source. To try the full model through our free web demo or integrate BEN2 into your project with our API:

-   🌐 [backgrounderase.com](https://backgrounderase.com)

## Contact us

[](#contact-us)

-   For access to our commercial model email us at [sales@backgrounderase.com](mailto:sales@backgrounderase.com)
-   Our website: [https://backgrounderase.com/](https://backgrounderase.com/)
-   Follow us on X: [https://x.com/PramaResearch/](https://x.com/PramaResearch/)

## Download weights

[](#download-weights)

You can find the weights to BEN2 base from our Huggingface: [https://huggingface.co/PramaLLC/BEN2](https://huggingface.co/PramaLLC/BEN2)

## Using ben2

[](#using-ben2)

```
pip install git+https://github.com/PramaLLC/BEN2.git
```

import torch
from ben2 import AutoModel
from PIL import Image

device \= torch.device('cuda' if torch.cuda.is\_available() else 'cpu')

image \= Image.open("image.jpg") \# your image here 
model \= AutoModel.from\_pretrained("PramaLLC/BEN2") \# repo\_id
model.to(device).eval()
foreground \= model.inference(image)

foreground.save("foreground.png")

## Quick start code (inside cloned repo)

[](#quick-start-code-inside-cloned-repo)

import BEN2
from PIL import Image
import torch

device \= torch.device('cuda' if torch.cuda.is\_available() else 'cpu')

file \= "./image.png" \# input image

model \= BEN2.BEN\_Base().to(device).eval() #init pipeline

model.loadcheckpoints("./BEN2\_Base.pth")
image \= Image.open(file)
foreground \= model.inference(image, refine\_foreground\=False,) #Refine foreground is an extract postprocessing step that increases inference time but can improve matting edges. The default value is False.

foreground.save("./foreground.png")

## Batch image processing

[](#batch-image-processing)

import BEN2
from PIL import Image
import torch

device \= torch.device('cuda' if torch.cuda.is\_available() else 'cpu')

model \= BEN2.BEN\_Base().to(device).eval() #init pipeline

model.loadcheckpoints("./BEN2\_Base.pth")

file1 \= "./image1.png" \# input image1
file2 \= "./image2.png" \# input image2
image1 \= Image.open(file1)
image2 \= Image.open(file2)

foregrounds \= model.inference(\[image1, image2\]) \#  We recommended that batch size not exceed 3 for consumer GPUs as there are minimal inference gains. Due to our custom batch processing for the MVANet decoding steps.
foregrounds\[0\].save("./foreground1.png")
foregrounds\[1\].save("./foreground2.png")

## BEN2 video segmentation

[](#ben2-video-segmentation)

[![BEN2 Demo](https://camo.githubusercontent.com/aeb073b898b54bf9b6f5bbf82a3350b1a45aa25de35ae44eeecfe6ad57ee6b22/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f736b4558694948516379732f302e6a7067)](https://www.youtube.com/watch?v=skEXiIHQcys)

## Video Segmentation

[](#video-segmentation)

sudo apt update
sudo apt install ffmpeg

import BEN2
from PIL import Image
import torch

device \= torch.device('cuda' if torch.cuda.is\_available() else 'cpu')

video\_path \= "/path\_to\_your\_video.mp4"\# input video

model \= BEN2.BEN\_Base().to(device).eval() #init pipeline

model.loadcheckpoints("./BEN2\_Base.pth")

model.segment\_video(
    video\_path\= video\_path,
    output\_path\="./", \# Outputs will be saved as foreground.webm or foreground.mp4. The default value is "./"
    fps\=0, \# If this is set to 0 CV2 will detect the fps in the original video. The default value is 0.
    refine\_foreground\=False,  #refine foreground is an extract postprocessing step that increases inference time but can improve matting edges. The default value is False.
    batch\=1,  \# We recommended that batch size not exceed 3 for consumer GPUs as there are minimal inference gains. The default value is 1.
    print\_frames\_processed\=True,  #Informs you what frame is being processed. The default value is True.
    webm \= False, \# This will output an alpha layer video but this defaults to mp4 when webm is false. The default value is False.
    rgb\_value\= (0, 255, 0) \# If you do not use webm this will be the RGB value of the resulting background only when webm is False. The default value is a green background (0,255,0).
 )

## ONNX support

[](#onnx-support)

You can find the ONNX weights to BEN2 base from our [Huggingface](https://huggingface.co/PramaLLC/BEN2/blob/main/BEN2_Base.onnx) and the inference code [here](https://huggingface.co/PramaLLC/BEN2/blob/main/onnx_run.py).

## BEN2 evaluation

[](#ben2-evaluation)

[![Model Comparison](/PramaLLC/BEN2/raw/main/BEN2_demo_pictures/model_comparison.png)](/PramaLLC/BEN2/blob/main/BEN2_demo_pictures/model_comparison.png)

RMBG 2.0 did not preserve the DIS 5k validation dataset

[![Example 1](/PramaLLC/BEN2/raw/main/BEN2_demo_pictures/grid_example1.png)](/PramaLLC/BEN2/blob/main/BEN2_demo_pictures/grid_example1.png) [![Example 2](/PramaLLC/BEN2/raw/main/BEN2_demo_pictures/grid_example2.png)](/PramaLLC/BEN2/blob/main/BEN2_demo_pictures/grid_example2.png) [![Example 3](/PramaLLC/BEN2/raw/main/BEN2_demo_pictures/grid_example3.png)](/PramaLLC/BEN2/blob/main/BEN2_demo_pictures/grid_example3.png) [![Example 6](/PramaLLC/BEN2/raw/main/BEN2_demo_pictures/grid_example6.png)](/PramaLLC/BEN2/blob/main/BEN2_demo_pictures/grid_example6.png) [![Example 7](/PramaLLC/BEN2/raw/main/BEN2_demo_pictures/grid_example7.png)](/PramaLLC/BEN2/blob/main/BEN2_demo_pictures/grid_example7.png)

## Installation

[](#installation)

1.  Clone Repo
2.  Install requirements.txt

## About

No description, website, or topics provided.

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

[Activity](/PramaLLC/BEN2/activity)

### Stars

**297** stars

### Watchers

**6** watching

### Forks

[**38** forks](/PramaLLC/BEN2/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FPramaLLC%2FBEN2&report=PramaLLC+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.
