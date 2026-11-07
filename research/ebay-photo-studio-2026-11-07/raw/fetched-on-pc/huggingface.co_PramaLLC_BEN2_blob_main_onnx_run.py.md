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
[ ![](https://cdn-avatars.huggingface.co/v1/production/uploads/65ad3d4cdf46651406f2535a/g186fbqoplfoGY7hpcnMl.png) ](https://huggingface.co/PramaLLC)
[PramaLLC](https://huggingface.co/PramaLLC)
/
[BEN2](https://huggingface.co/PramaLLC/BEN2)
Like 253
Follow
![](https://cdn-avatars.huggingface.co/v1/production/uploads/65ad3d4cdf46651406f2535a/g186fbqoplfoGY7hpcnMl.png) BackgroundErase 74
[ Image Segmentation ](https://huggingface.co/models?pipeline_tag=image-segmentation)[ BEN2 ](https://huggingface.co/models?library=ben2)[ ONNX ](https://huggingface.co/models?library=onnx)[ Safetensors ](https://huggingface.co/models?library=safetensors)[ PyTorch ](https://huggingface.co/models?library=pytorch)[ BEN2 ](https://huggingface.co/models?other=BEN2)[ background-remove ](https://huggingface.co/models?other=background-remove)[ mask-generation ](https://huggingface.co/models?other=mask-generation)[ Dichotomous image segmentation ](https://huggingface.co/models?other=Dichotomous+image+segmentation)[ background remove ](https://huggingface.co/models?other=background+remove)[ foreground ](https://huggingface.co/models?other=foreground)[ background ](https://huggingface.co/models?other=background)[ remove background ](https://huggingface.co/models?other=remove+background)[ model_hub_mixin ](https://huggingface.co/models?other=model_hub_mixin)[ pytorch_model_hub_mixin ](https://huggingface.co/models?other=pytorch_model_hub_mixin)[ background removal ](https://huggingface.co/models?other=background+removal)[ background-removal ](https://huggingface.co/models?other=background-removal)
arxiv: 2501.06230
License: mit
[ Model card ](https://huggingface.co/PramaLLC/BEN2)[ Files Files and versions xet ](https://huggingface.co/PramaLLC/BEN2/tree/main)[ Community 7 ](https://huggingface.co/PramaLLC/BEN2/discussions)
Deploy
Copy to bucket
Use this model
### Instructions to use PramaLLC/BEN2 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  * [ BEN2](https://huggingface.co/PramaLLC/BEN2?library=ben2)
How to use PramaLLC/BEN2 with BEN2:

```
import requests
from PIL import Image
from ben2 import AutoModel

url = "https://huggingface.co/datasets/mishig/sample_images/resolve/main/teapot.jpg"
image = Image.open(requests.get(url, stream=True).raw)

model = AutoModel.from_pretrained("PramaLLC/BEN2")
model.to("cuda").eval()
foreground = model.inference(image)

```

  * Notebooks
  * [ Google Colab](https://huggingface.co/PramaLLC/BEN2/colab)
  * [ Kaggle](https://huggingface.co/PramaLLC/BEN2/kaggle)


main
[BEN2](https://huggingface.co/PramaLLC/BEN2/tree/main) / onnx_run.py
![MaxwellMeyer's picture](https://cdn-avatars.huggingface.co/v1/production/uploads/65ad3d4cdf46651406f2535a/ewgFdPFlAJjC-HI1nUdc6.png)
[MaxwellMeyer](https://huggingface.co/MaxwellMeyer)
[Update onnx_run.py](https://huggingface.co/PramaLLC/BEN2/commit/d66d54ef23eedc4b4406e5fb42bc022957cb160f)
[d66d54e](https://huggingface.co/PramaLLC/BEN2/commit/d66d54ef23eedc4b4406e5fb42bc022957cb160f) verified over 1 year ago
Download
### Download onnx_run.py from PramaLLC/BEN2: direct link, hf CLI and curl.
  * Browser
  * [ Download file 1.68 kB](https://huggingface.co/PramaLLC/BEN2/resolve/main/onnx_run.py?download=true)
  * Copy download link 
```
https://huggingface.co/PramaLLC/BEN2/resolve/main/onnx_run.py
```

  * Command line
  * Copy hf CLI command 
```
hf download hf://PramaLLC/BEN2/onnx_run.py
```

  * Copy curl command 
```
curl -L -o onnx_run.py https://huggingface.co/PramaLLC/BEN2/resolve/main/onnx_run.py
```



[ Raw ](https://huggingface.co/PramaLLC/BEN2/raw/main/onnx_run.py)[ History ](https://huggingface.co/PramaLLC/BEN2/commits/main/onnx_run.py)[ Blame ](https://huggingface.co/PramaLLC/BEN2/blame/main/onnx_run.py)[ Contribute ](https://huggingface.co/PramaLLC/BEN2/edit/main/onnx_run.py)[ Delete ](https://huggingface.co/PramaLLC/BEN2/delete/main/onnx_run.py)
Safe
1.68 kB  
|   |  import onnxruntime  |  
| --- | --- |  
|   |  import numpy as np  |  
|   |  from PIL import Image  |  
|   |  import torchvision.transforms as transforms  |  
|   |  import torch  |  
|   |  import torch.nn.functional as F  |  
|   |   |  
|   |   |  
|   |  session = onnxruntime.InferenceSession("./BEN2_Base.onnx", providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])  |  
|   |   |  
|   |  def postprocess_image(result_np: np.ndarray, im_size: list) -> np.ndarray:  |  
|   |   |  
|   |  result = torch.from_numpy(result_np)  |  
|   |   |  
|   |   |  
|   |  if len(result.shape) == 3:  |  
|   |  result = result.unsqueeze(0)  |  
|   |   |  
|   |   |  
|   |  result = torch.squeeze(F.interpolate(result, size=im_size, mode='bilinear'), 0)  |  
|   |   |  
|   |   |  
|   |  ma = torch.max(result)  |  
|   |  mi = torch.min(result)  |  
|   |  result = (result - mi) / (ma - mi)  |  
|   |   |  
|   |  im_array = (result * 255).permute(1, 2, 0).cpu().data.numpy().astype(np.uint8)  |  
|   |  im_array = np.squeeze(im_array)  |  
|   |  return im_array  |  
|   |   |  
|   |  def preprocess_image(image):  |  
|   |  original_size = image.size  |  
|   |  transform = transforms.Compose([  |  
|   |  transforms.Resize((1024, 1024)),  |  
|   |  transforms.ToTensor(),  |  
|   |  ])  |  
|   |  img_tensor = transform(image)  |  
|   |   |  
|   |  img_tensor = img_tensor.unsqueeze(0)  |  
|   |  return img_tensor.numpy(), image, original_size  |  
|   |   |  
|   |  def run_inference(image):  |  
|   |   |  
|   |  input_data, original_image, (w, h) = preprocess_image(image)  |  
|   |   |  
|   |  input_name = session.get_inputs()[0].name  |  
|   |   |  
|   |  outputs = session.run(None, {input_name: input_data})  |  
|   |   |  
|   |   |  
|   |  alpha = postprocess_image(outputs[0], im_size=[w, h])  |  
|   |   |  
|   |   |  
|   |  mask = Image.fromarray(alpha)  |  
|   |  mask = mask.resize((w, h))  |  
|   |   |  
|   |   |  
|   |  original_image.putalpha(mask)  |  
|   |  return original_image  |  
|   |   |  
|   |  # Example usage  |  
|   |  image_path = "image.png"  |  
|   |  output_path = "output.png"  |  
|   |   |  
|   |   |  
|   |  image = Image.open(image_path)  |  
|   |   |  
|   |  result_image = run_inference(image)  |  
|   |  result_image.save(output_path)  |  
|   |   |  
Wrap lines

