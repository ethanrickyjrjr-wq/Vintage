Source: https://huggingface.co/zhengchong/CatVTON (fetched 2026-11-13 with crawl4ai)

[![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)
Search models, datasets, users... `Ctrl K`
  * [ Models](https://huggingface.co/models)
  * [ Datasets](https://huggingface.co/datasets)
  * [ Spaces](https://huggingface.co/spaces)
  * [ Buckets](https://huggingface.co/storage)
  * [ Docs](https://huggingface.co/docs)
  * [ Enterprise](https://huggingface.co/enterprise)
  * [Pricing](https://huggingface.co/pricing)
  *     * Website
      * [ Tasks](https://huggingface.co/tasks)
      * [ HuggingChat](https://huggingface.co/chat)
      * [ Collections](https://huggingface.co/collections)
      * [ Languages](https://huggingface.co/languages)
      * [ Organizations](https://huggingface.co/organizations)
    * Community
      * [ Blog](https://huggingface.co/blog)
      * [ Posts](https://huggingface.co/posts)
      * [ Daily Papers](https://huggingface.co/papers)
      * [ Hardware](https://huggingface.co/hardware)
      * [ Learn](https://huggingface.co/learn)
      * [ Discord](https://huggingface.co/join/discord)
      * [ Forum](https://discuss.huggingface.co/)
      * [ GitHub](https://github.com/huggingface)
    * Solutions
      * [ Team & Enterprise](https://huggingface.co/enterprise)
      * [ Hugging Face PRO](https://huggingface.co/pro)
      * [ Enterprise Support](https://huggingface.co/support)
      * [ Inference Providers](https://huggingface.co/inference/models)
      * [ Inference Endpoints](https://huggingface.co/inference-endpoints)
      * [ Storage Buckets](https://huggingface.co/storage)
  * * * *
  * [Log In](https://huggingface.co/login)
  * [Sign Up](https://huggingface.co/join)


# 
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/646446517572c66a8e652e94/A4LIdECGW03ixc0HfIhfo.png) ](https://huggingface.co/zhengchong)
[zhengchong](https://huggingface.co/zhengchong)
/
[CatVTON](https://huggingface.co/zhengchong/CatVTON)
Like 87
[ Transformers ](https://huggingface.co/models?library=transformers)[ Safetensors ](https://huggingface.co/models?library=safetensors)
arxiv: 2407.15886
License: cc-by-nc-sa-4.0
[ Model card ](https://huggingface.co/zhengchong/CatVTON)[ Files Files and versions xet ](https://huggingface.co/zhengchong/CatVTON/tree/main)[ Community 6 ](https://huggingface.co/zhengchong/CatVTON/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use zhengchong/CatVTON with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ Transformers](https://huggingface.co/zhengchong/CatVTON?library=transformers)
How to use zhengchong/CatVTON with Transformers:

```
# pip install -U transformers accelerate
# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("zhengchong/CatVTON", device_map="auto")
```

  * Notebooks
  * [ Google Colab](https://huggingface.co/zhengchong/CatVTON/colab)
  * [ Kaggle](https://huggingface.co/zhengchong/CatVTON/kaggle)


**Configuration Parsing Warning:** Invalid JSON for config file config.json
  * [🐈 CatVTON: Concatenation Is All You Need for Virtual Try-On with Diffusion Models](https://huggingface.co/zhengchong/CatVTON#%F0%9F%90%88-catvton-concatenation-is-all-you-need-for-virtual-try-on-with-diffusion-models "🐈 CatVTON: Concatenation Is All You Need for Virtual Try-On with Diffusion Models")
    * [Updates](https://huggingface.co/zhengchong/CatVTON#updates "Updates")
    * [Installation](https://huggingface.co/zhengchong/CatVTON#installation "Installation")
    * [Deployment](https://huggingface.co/zhengchong/CatVTON#deployment "Deployment")
      * [ComfyUI Workflow](https://huggingface.co/zhengchong/CatVTON#comfyui-workflow "ComfyUI Workflow")
      * [Gradio App](https://huggingface.co/zhengchong/CatVTON#gradio-app "Gradio App")
    * [Inference](https://huggingface.co/zhengchong/CatVTON#inference "Inference")
      * [1. Data Preparation](https://huggingface.co/zhengchong/CatVTON#1-data-preparation "1. Data Preparation")
      * [2. Inference on VTIONHD/DressCode](https://huggingface.co/zhengchong/CatVTON#2-inference-on-vtionhddresscode "2. Inference on VTIONHD/DressCode")
      * [3. Calculate Metrics](https://huggingface.co/zhengchong/CatVTON#3-calculate-metrics "3. Calculate Metrics")
    * [Acknowledgement](https://huggingface.co/zhengchong/CatVTON#acknowledgement "Acknowledgement")
    * [License](https://huggingface.co/zhengchong/CatVTON#license "License")
    * [Citation](https://huggingface.co/zhengchong/CatVTON#citation "Citation")


#  [ ](https://huggingface.co/zhengchong/CatVTON#%F0%9F%90%88-catvton-concatenation-is-all-you-need-for-virtual-try-on-with-diffusion-models) 🐈 CatVTON: Concatenation Is All You Need for Virtual Try-On with Diffusion Models 
[ ![arxiv](https://img.shields.io/badge/arXiv-2407.15886-red?style=flat&logo=arXiv&logoColor=red) ](http://arxiv.org/abs/2407.15886) [ ![huggingface](https://img.shields.io/badge/Hugging%20Face-ckpts-orange?style=flat&logo=HuggingFace&logoColor=orange) ](https://huggingface.co/zhengchong/CatVTON) [ ![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat&logo=GitHub) ](https://github.com/Zheng-Chong/CatVTON) [ ![Demo](https://img.shields.io/badge/Demo-Gradio-gold?style=flat&logo=Gradio&logoColor=red) ](http://120.76.142.206:8888) [ ![Demo](https://img.shields.io/badge/Space-ZeroGPU-orange?style=flat&logo=Gradio&logoColor=red) ](https://huggingface.co/spaces/zhengchong/CatVTON) [ ![webpage](https://img.shields.io/badge/Webpage-Project-silver?style=flat&logo=&logoColor=orange) ](https://zheng-chong.github.io/CatVTON/) [ ![License](https://img.shields.io/badge/License-CC%20BY--NC--SA--4.0-lightgreen?style=flat&logo=Lisence) ](https://github.com/Zheng-Chong/CatVTON/LICENCE)
**CatVTON** is a simple and efficient virtual try-on diffusion model with _**1) Lightweight Network (899.06M parameters totally)**_ , _**2) Parameter-Efficient Training (49.57M parameters trainable)**_ and _**3) Simplified Inference ( < 8G VRAM for 1024X768 resolution)**_.
##  [ ](https://huggingface.co/zhengchong/CatVTON#updates) Updates 
  * **`2024/10/17`**:[**Mask-free version**](https://huggingface.co/zhengchong/CatVTON-MaskFree)🤗 of CatVTON is release and please try it in our [**Online Demo**](http://120.76.142.206:8888). 
  * **`2024/10/13`**: We have built a repo[**Awesome-Try-On-Models**](https://github.com/Zheng-Chong/Awesome-Try-On-Models) that focuses on image, video, and 3D-based try-on models published after 2023, aiming to provide insights into the latest technological trends. If you're interested, feel free to contribute or give it a 🌟 star!
  * **`2024/08/13`**: We localize DensePose & SCHP to avoid certain environment issues.
  * **`2024/08/10`**: Our 🤗[**HuggingFace Space**](https://huggingface.co/spaces/zhengchong/CatVTON) is available now! Thanks for the grant from [**ZeroGPU**](https://huggingface.co/zero-gpu-explorers)！
  * **`2024/08/09`**:[**Evaluation code**](https://github.com/Zheng-Chong/CatVTON?tab=readme-ov-file#3-calculate-metrics) is provided to calculate metrics 📚.
  * **`2024/07/27`**: We provide code and workflow for deploying CatVTON on[**ComfyUI**](https://github.com/Zheng-Chong/CatVTON?tab=readme-ov-file#comfyui-workflow) 💥.
  * **`2024/07/24`**: Our[**Paper on ArXiv**](http://arxiv.org/abs/2407.15886) is available 🥳!
  * **`2024/07/22`**: Our[**App Code**](https://github.com/Zheng-Chong/CatVTON/blob/main/app.py) is released, deploy and enjoy CatVTON on your mechine 🎉!
  * **`2024/07/21`**: Our[**Inference Code**](https://github.com/Zheng-Chong/CatVTON/blob/main/inference.py) and [**Weights** 🤗](https://huggingface.co/zhengchong/CatVTON) are released.
  * **`2024/07/11`**: Our[**Online Demo**](http://120.76.142.206:8888) is released 😁.


##  [ ](https://huggingface.co/zhengchong/CatVTON#installation) Installation 
Create a conda environment & Install requirments

```
conda create -n catvton python==3.9.0
conda activate catvton
cd CatVTON-main  # or your path to CatVTON project dir
pip install -r requirements.txt

```

##  [ ](https://huggingface.co/zhengchong/CatVTON#deployment) Deployment 
###  [ ](https://huggingface.co/zhengchong/CatVTON#comfyui-workflow) ComfyUI Workflow 
We have modified the main code to enable easy deployment of CatVTON on [ComfyUI](https://github.com/comfyanonymous/ComfyUI). Due to the incompatibility of the code structure, we have released this part in the [Releases](https://github.com/Zheng-Chong/CatVTON/releases/tag/ComfyUI), which includes the code placed under `custom_nodes` of ComfyUI and our workflow JSON files.
To deploy CatVTON to your ComfyUI, follow these steps:
  1. Install all the requirements for both CatVTON and ComfyUI, refer to [Installation Guide for CatVTON](https://github.com/Zheng-Chong/CatVTON/blob/main/INSTALL.md) and [Installation Guide for ComfyUI](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#installing).
  2. Download [`ComfyUI-CatVTON.zip`](https://github.com/Zheng-Chong/CatVTON/releases/download/ComfyUI/ComfyUI-CatVTON.zip) and unzip it in the `custom_nodes` folder under your ComfyUI project (clone from [ComfyUI](https://github.com/comfyanonymous/ComfyUI)).
  3. Run the ComfyUI.
  4. Download [`catvton_workflow.json`](https://github.com/Zheng-Chong/CatVTON/releases/download/ComfyUI/catvton_workflow.json) and drag it into you ComfyUI webpage and enjoy 😆!


> Problems under Windows OS, please refer to [issue#8](https://github.com/Zheng-Chong/CatVTON/issues/8).
When you run the CatVTON workflow for the first time, the weight files will be automatically downloaded, usually taking dozens of minutes.
![](https://huggingface.co/zhengchong/CatVTON/resolve/main/resource/img/comfyui-1.png)
###  [ ](https://huggingface.co/zhengchong/CatVTON#gradio-app) Gradio App 
To deploy the Gradio App for CatVTON on your machine, run the following command, and checkpoints will be automatically downloaded from HuggingFace.

```
CUDA_VISIBLE_DEVICES=0 python app.py \
--output_dir="resource/demo/output" \
--mixed_precision="bf16" \
--allow_tf32 

```

When using `bf16` precision, generating results with a resolution of `1024x768` only requires about `8G` VRAM.
##  [ ](https://huggingface.co/zhengchong/CatVTON#inference) Inference 
###  [ ](https://huggingface.co/zhengchong/CatVTON#1-data-preparation) 1. Data Preparation 
Before inference, you need to download the [VITON-HD](https://github.com/shadow2496/VITON-HD) or [DressCode](https://github.com/aimagelab/dress-code) dataset. Once the datasets are downloaded, the folder structures should look like these:

```
├── VITON-HD
|   ├── test_pairs_unpaired.txt
│   ├── test
|   |   ├── image
│   │   │   ├── [000006_00.jpg | 000008_00.jpg | ...]
│   │   ├── cloth
│   │   │   ├── [000006_00.jpg | 000008_00.jpg | ...]
│   │   ├── agnostic-mask
│   │   │   ├── [000006_00_mask.png | 000008_00.png | ...]
...

```

```
├── DressCode
|   ├── test_pairs_paired.txt
|   ├── test_pairs_unpaired.txt
│   ├── [dresses | lower_body | upper_body]
|   |   ├── test_pairs_paired.txt
|   |   ├── test_pairs_unpaired.txt
│   │   ├── images
│   │   │   ├── [013563_0.jpg | 013563_1.jpg | 013564_0.jpg | 013564_1.jpg | ...]
│   │   ├── agnostic_masks
│   │   │   ├── [013563_0.png| 013564_0.png | ...]
...

```

For the DressCode dataset, we provide script to preprocessed agnostic masks, run the following command:

```
CUDA_VISIBLE_DEVICES=0 python preprocess_agnostic_mask.py \
--data_root_path <your_path_to_DressCode> 

```

###  [ ](https://huggingface.co/zhengchong/CatVTON#2-inference-on-vtionhddresscode) 2. Inference on VTIONHD/DressCode 
To run the inference on the DressCode or VITON-HD dataset, run the following command, checkpoints will be automatically downloaded from HuggingFace.

```
CUDA_VISIBLE_DEVICES=0 python inference.py \
--dataset [dresscode | vitonhd] \
--data_root_path <path> \
--output_dir <path> 
--dataloader_num_workers 8 \
--batch_size 8 \
--seed 555 \
--mixed_precision [no | fp16 | bf16] \
--allow_tf32 \
--repaint \
--eval_pair  

```

###  [ ](https://huggingface.co/zhengchong/CatVTON#3-calculate-metrics) 3. Calculate Metrics 
After obtaining the inference results, calculate the metrics using the following command: 

```
CUDA_VISIBLE_DEVICES=0 python eval.py \
--gt_folder <your_path_to_gt_image_folder> \
--pred_folder <your_path_to_predicted_image_folder> \
--paired \
--batch_size=16 \
--num_workers=16 

```

  * `--gt_folder` and `--pred_folder` should be folders that contain **only images**.
  * To evaluate the results in a paired setting, use `--paired`; for an unpaired setting, simply omit it.
  * `--batch_size` and `--num_workers` should be adjusted based on your machine.


##  [ ](https://huggingface.co/zhengchong/CatVTON#acknowledgement) Acknowledgement 
Our code is modified based on [Diffusers](https://github.com/huggingface/diffusers). We adopt [Stable Diffusion v1.5 inpainting](https://huggingface.co/runwayml/stable-diffusion-inpainting) as the base model. We use [SCHP](https://github.com/GoGoDuck912/Self-Correction-Human-Parsing/tree/master) and [DensePose](https://github.com/facebookresearch/DensePose) to automatically generate masks in our [Gradio](https://github.com/gradio-app/gradio) App and [ComfyUI](https://github.com/comfyanonymous/ComfyUI) workflow. Thanks to all the contributors!
##  [ ](https://huggingface.co/zhengchong/CatVTON#license) License 
All the materials, including code, checkpoints, and demo, are made available under the [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license. You are free to copy, redistribute, remix, transform, and build upon the project for non-commercial purposes, as long as you give appropriate credit and distribute your contributions under the same license.
##  [ ](https://huggingface.co/zhengchong/CatVTON#citation) Citation 

```
@misc{chong2024catvtonconcatenationneedvirtual,
 title={CatVTON: Concatenation Is All You Need for Virtual Try-On with Diffusion Models}, 
 author={Zheng Chong and Xiao Dong and Haoxiang Li and Shiyue Zhang and Wenqing Zhang and Xujie Zhang and Hanqing Zhao and Xiaodan Liang},
 year={2024},
 eprint={2407.15886},
 archivePrefix={arXiv},
 primaryClass={cs.CV},
 url={https://arxiv.org/abs/2407.15886}, 
}

```


Downloads last month
    3,734
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
This model isn't deployed by any Inference Provider. [🙋 2 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/5793)
##  Model tree for zhengchong/CatVTON [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Finetunes
[1 model](https://huggingface.co/models?other=base_model:finetune:zhengchong/CatVTON)
##  Spaces using zhengchong/CatVTON 100
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/646446517572c66a8e652e94/A4LIdECGW03ixc0HfIhfo.png) zhengchong/CatVTON ](https://huggingface.co/spaces/zhengchong/CatVTON)[🐈 multimodalart/CatVTON-zerogpu ](https://huggingface.co/spaces/multimodalart/CatVTON-zerogpu)[👗 burhanbhatti/tryon-vton-api ](https://huggingface.co/spaces/burhanbhatti/tryon-vton-api)[🐈 2716omar/my-catvton ](https://huggingface.co/spaces/2716omar/my-catvton)[👗 aroooba-amjad/ata-virtual-try-on ](https://huggingface.co/spaces/aroooba-amjad/ata-virtual-try-on)[👕 jh2629/vcloset-tryon ](https://huggingface.co/spaces/jh2629/vcloset-tryon)[👕 melikfiratai/seetudio-catvton ](https://huggingface.co/spaces/melikfiratai/seetudio-catvton)[🐈 VIDraft/Fashion-Fit ](https://huggingface.co/spaces/VIDraft/Fashion-Fit) + 95 Spaces + 92 Spaces
##  Paper for zhengchong/CatVTON
#### [CatVTON: Concatenation Is All You Need for Virtual Try-On with Diffusion Models Paper • 2407.15886 • Published Jul 21, 2024 • 3 ](https://huggingface.co/papers/2407.15886)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)

