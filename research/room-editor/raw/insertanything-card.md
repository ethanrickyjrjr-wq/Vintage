[![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face](https://huggingface.co/)
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
[ ![](https://huggingface.co/avatars/3daf4814f206f47a55a55108b5e70aa2.svg) ](https://huggingface.co/WensongSong)
[WensongSong](https://huggingface.co/WensongSong)
/
[Insert-Anything](https://huggingface.co/WensongSong/Insert-Anything)
Like 15
WensongSong/AnyInsertion
[ English ](https://huggingface.co/models?language=en)
arxiv: 2504.15009
License: mit
[ Model card ](https://huggingface.co/WensongSong/Insert-Anything)[ Files Files and versions xet ](https://huggingface.co/WensongSong/Insert-Anything/tree/main)[ Community ](https://huggingface.co/WensongSong/Insert-Anything/discussions)
Copy to bucket
  * [News](https://huggingface.co/WensongSong/Insert-Anything#news "News")
  * [Model Introduction](https://huggingface.co/WensongSong/Insert-Anything#model-introduction "Model Introduction")
  * [Citation](https://huggingface.co/WensongSong/Insert-Anything#citation "Citation")


# Insert Anything
[**Wensong Song**](https://song-wensong.github.io/) · [**Hong Jinag**](https://openreview.net/profile?id=~Hong_Jiang4) · [**Zongxing Yang**](https://z-x-yang.github.io/) · [**Ruijie Quan**](https://scholar.google.com/citations?user=WKLRPsAAAAAJ&hl=en) · [**Yi Yang**](https://scholar.google.com/citations?user=RMSuNFwAAAAJ&hl=en)   
  
[ ![Paper PDF](https://img.shields.io/badge/arXiv-InsertAnything-red?color=%23aa1a1a) ](https://arxiv.org/pdf/2504.15009) [ ![Project Page](https://img.shields.io/badge/Project%20Page-InsertAnything-cyan?logoColor=%23FFD21E&color=%23cbe6f2) ](https://song-wensong.github.io/insert-anything/) [ ![](https://img.shields.io/badge/GitHub-InsertAnything-black?logoColor=23FFD21E&color=%231d2125) ](https://github.com/song-wensong/insert-anything)   
**Zhejiang University | Harvard University | Nanyang Technological University**
##  [ ](https://huggingface.co/WensongSong/Insert-Anything#news) News 
  * **[2025.4.25]** Release **AnyInsertion** dataset on [HuggingFace](https://huggingface.co/datasets/WensongSong/AnyInsertion).
  * **[2025.4.22]** Release inference & demo code on [GitHub](https://github.com/song-wensong/insert-anything), and mask-prompt pretrained checkpoint.


##  [ ](https://huggingface.co/WensongSong/Insert-Anything#model-introduction) Model Introduction 
The currently released checkpoint is 20250321_steps5000_pytorch_lora_weights.safetensors, which is for mask-prompt image insertion. Future versions of the checkpoints will be released as updates.
##  [ ](https://huggingface.co/WensongSong/Insert-Anything#citation) Citation 

```
@article{song2025insert,
  title={Insert Anything: Image Insertion via In-Context Editing in DiT},
  author={Song, Wensong and Jiang, Hong and Yang, Zongxing and Quan, Ruijie and Yang, Yi},
  journal={arXiv preprint arXiv:2504.15009},
  year={2025}
}

```
Downloads last month
    
-     
Downloads are not tracked for this model. [How to track ](https://huggingface.co/docs/hub/models-download-stats)
Inference Providers [NEW](https://huggingface.co/docs/inference-providers)
This model isn't deployed by any Inference Provider. [🙋 Ask for provider support](https://huggingface.co/spaces/huggingface/InferenceSupport/discussions/new?title=WensongSong/Insert-Anything&description=React%20to%20this%20comment%20with%20an%20emoji%20to%20vote%20for%20%5BWensongSong%2FInsert-Anything%5D\(%2FWensongSong%2FInsert-Anything\)%20to%20be%20supported%20by%20Inference%20Providers.%0A%0A\(optional\)%20Which%20providers%20are%20you%20interested%20in%3F%20\(Novita%2C%20Hyperbolic%2C%20Together%E2%80%A6\)%0A)
##  Model tree for WensongSong/Insert-Anything [](https://huggingface.co/docs/hub/model-cards#specifying-a-base-model)
Base model
[black-forest-labs/FLUX.1-Fill-dev](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev)
Finetuned
([34](https://huggingface.co/models?other=base_model:finetune:black-forest-labs/FLUX.1-Fill-dev))
this model
##  Dataset used to train WensongSong/Insert-Anything
#### [WensongSong/AnyInsertion Viewer • Updated May 9, 2025 • 59k • 996 • 9 ](https://huggingface.co/datasets/WensongSong/AnyInsertion)
##  Spaces using WensongSong/Insert-Anything 5
[ ![](https://huggingface.co/avatars/3daf4814f206f47a55a55108b5e70aa2.svg) WensongSong/Insert-Anything ](https://huggingface.co/spaces/WensongSong/Insert-Anything)[🌍 bep40/Insert-Anything ](https://huggingface.co/spaces/bep40/Insert-Anything)[🌍 zeenai2025/Insert-Anything2 ](https://huggingface.co/spaces/zeenai2025/Insert-Anything2)[🌍 luanngo/Insert-Anything ](https://huggingface.co/spaces/luanngo/Insert-Anything)[🌍 LLXX/Insert-Anything ](https://huggingface.co/spaces/LLXX/Insert-Anything)
##  Paper for WensongSong/Insert-Anything
#### [Insert Anything: Image Insertion via In-Context Editing in DiT Paper • 2504.15009 • Published Apr 21, 2025 • 1 ](https://huggingface.co/papers/2504.15009)
System theme
Company
[TOS](https://huggingface.co/terms-of-service) [Privacy](https://huggingface.co/privacy) [About](https://huggingface.co/huggingface) [Careers](https://apply.workable.com/huggingface/) [](https://huggingface.co/)
Website
[Models](https://huggingface.co/models) [Datasets](https://huggingface.co/datasets) [Spaces](https://huggingface.co/spaces) [Pricing](https://huggingface.co/pricing) [Docs](https://huggingface.co/docs)
Inference providers allow you to run inference using different serverless providers.

