[Skip to main content](https://pypi.org/project/rembg/#content) Switch to mobile version
Security notice: Upgrade certifi, pip, and uv in response to CA certificate incident [See more](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576)
[ ![PyPI](https://pypi.org/static/images/logo-small.0e0855d0.svg) ](https://pypi.org/)
Search PyPI Search
  * [Docs](https://docs.pypi.org/)
  * [Blog](https://blog.pypi.org)
  * [Log in](https://pypi.org/account/login/?next=https%3A%2F%2Fpypi.org%2Fproject%2Frembg%2F)
  * [Register](https://pypi.org/account/register/)


  * [Docs](https://docs.pypi.org/)
  * [Blog](https://blog.pypi.org)
  * [Log in](https://pypi.org/account/login/?next=https%3A%2F%2Fpypi.org%2Fproject%2Frembg%2F)
  * [Register](https://pypi.org/account/register/)


  * Deutsch 
  * English 
  * español 
  * Esperanto 
  * français 
  * português (Brasil) 
  * Ελληνικά 
  * русский 
  * українська 
  * עברית 
  * 中文 (简体) 
  * 中文 (繁體) 
  * 日本語 
  * 한국어 


Search PyPI Search
# rembg 2.0.86
Remove image background
pip install rembg Copy PIP instructions
  * [ Description  ](https://pypi.org/project/rembg/#description)
  * [ Metadata  ](https://pypi.org/project/rembg/#metadata)
  * [ Release files  ](https://pypi.org/project/rembg/#files)
  * [ Security  ](https://pypi.org/project/rembg/#security)
  * [ Release history  ](https://pypi.org/project/rembg/#history)


![Rembg Logo](https://pypi-camo.freetls.fastly.net/388655114bc901a8aeb49270f41e805988057feb/6c6f676f2e706e67)
Rembg is a tool to remove image backgrounds. It can be used as a CLI, Python library, HTTP server, or Docker container.
[![License](https://pypi-camo.freetls.fastly.net/4150014b4dfdd7b565fa18de88e9bb1b8ccd7c08/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d626c75652e737667)](https://img.shields.io/badge/License-MIT-blue.svg) [![Hugging Face Spaces](https://pypi-camo.freetls.fastly.net/7efead29e9b6a3111a0ad845489d7e673fee252b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652ff09fa49725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/KenjieDec/RemBG) [![Streamlit App](https://pypi-camo.freetls.fastly.net/dae5eb0f4b8328f603ee4c4d276fee65a5db570e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652ff09f8e8825323053747265616d6c6974253230436f6d6d756e6974792d436c6f75642d626c7565)](https://bgremoval.streamlit.app/) [![Open in Colab](https://pypi-camo.freetls.fastly.net/74d996556a82b2f1dd5252d2fd8bead60f9e9d21/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/danielgatis/rembg/blob/main/rembg.ipynb) [![RepoMapr](https://pypi-camo.freetls.fastly.net/9f4ddef5cb8f3987eda45243045c04d747218f10/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5265706f4d6170722d566965775f496e7465726163746976655f4469616772616d2d626c75653f7374796c653d666c6174266c6f676f3d676974687562)](https://repomapr.com/danielgatis/rembg)
  

[ ![danielgatis%2Frembg | Trendshift](https://pypi-camo.freetls.fastly.net/13d5df134adb0fb493a5782aa97dd0c96c23d450/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f32383436) ](https://trendshift.io/repositories/2846)
## Sponsors[](https://pypi.org/project/rembg/#user-content-sponsors)  
|  [ ![PhotoRoom](https://pypi-camo.freetls.fastly.net/938c9f80474175e0d14924f09d88dcdf89c8ef12/68747470733a2f2f7777772e70686f746f726f6f6d2e636f6d2f66617669636f6e732f6170706c652d746f7563682d69636f6e2e706e67) ](https://photoroom.com/api/remove-background?utm_source=rembg&utm_medium=github_webpage&utm_campaign=sponsor)  |  **PhotoRoom Remove Background API**   
[https://photoroom.com/api](https://photoroom.com/api/remove-background?utm_source=rembg&utm_medium=github_webpage&utm_campaign=sponsor)   
Fast and accurate background remover API  
 |  
| --- | --- |  
**If this project has helped you, please consider making a[donation](https://www.buymeacoffee.com/danielgatis).**
## Requirements[](https://pypi.org/project/rembg/#user-content-requirements)

```
python: >=3.11, <3.14

```

## Installation[](https://pypi.org/project/rembg/#user-content-installation)
Choose **one** of the following backends based on your hardware:
### CPU support[](https://pypi.org/project/rembg/#user-content-cpu-support)

```
pip install "rembg[cpu]" # for library
pip install "rembg[cpu,cli]" # for library + cli

```

### GPU support (NVIDIA/CUDA)[](https://pypi.org/project/rembg/#user-content-gpu-support-nvidiacuda)
First, check if your system supports `onnxruntime-gpu` by visiting [onnxruntime.ai](https://onnxruntime.ai/getting-started) and reviewing the installation matrix.
![onnxruntime-installation-matrix](https://pypi-camo.freetls.fastly.net/5eccce339edf9d81118bf6d39de74839bc475e21/2e2f6f6e6e7872756e74696d652d696e7374616c6c6174696f6e2d6d61747269782e706e67)
If your system is compatible, run:

```
pip install "rembg[gpu]" # for library
pip install "rembg[gpu,cli]" # for library + cli

```

> **Note:** NVIDIA GPUs may require `onnxruntime-gpu`, CUDA, and `cudnn-devel`. See [#668](https://github.com/danielgatis/rembg/issues/668#issuecomment-2689830314) for details. If `rembg[gpu]` doesn't work and you can't install CUDA or `cudnn-devel`, use `rembg[cpu]` with `onnxruntime` instead.
### GPU support (AMD/ROCm)[](https://pypi.org/project/rembg/#user-content-gpu-support-amdrocm)
ROCm support requires the `onnxruntime-rocm` package. Install it by following [AMD's documentation](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-onnx.html).
Once `onnxruntime-rocm` is installed and working, install rembg with ROCm support:

```
pip install "rembg[rocm]" # for library
pip install "rembg[rocm,cli]" # for library + cli

```

## Usage as a CLI[](https://pypi.org/project/rembg/#user-content-usage-as-a-cli)
After installation, you can use rembg by typing `rembg` in your terminal.
The `rembg` command has these subcommands:
  * `i` - single files
  * `p` - folders (batch processing)
  * `s` - HTTP server
  * `b` - RGB24 pixel binary stream
  * `d` - download models ahead of time
  * `m` - migrate models from the legacy `~/.u2net` directory


You can get help about the main command using:

```
rembg --help

```

You can also get help for any subcommand:

```
rembg <COMMAND> --help

```

### rembg `i`[](https://pypi.org/project/rembg/#user-content-rembg-i)
Used for processing single files.
**Remove background from a remote image:**

```
curl -s http://input.png | rembg i > output.png

```

**Remove background from a local file:**

```
rembg i path/to/input.png path/to/output.png

```

**Omit the output path** (writes `<input_stem>.out.png` next to the input):

```
rembg i path/to/input.png
# → path/to/input.out.png

```

If `stdout` is redirected (e.g. `rembg i input.png > out.png`), the output is written to `stdout` instead.
**Specify a model:**

```
rembg i -m u2netp path/to/input.png path/to/output.png

```

**Return only the mask:**

```
rembg i -om path/to/input.png path/to/output.png

```

**Apply alpha matting:**

```
rembg i -a path/to/input.png path/to/output.png

```

**Remove color fringing from soft edges:**

```
rembg i -dc path/to/input.png path/to/output.png

```

See [Color decontamination](https://pypi.org/project/rembg/#user-content-color-decontamination) for what this does.
**Pass extra parameters (SAM example):**

```
rembg i -m sam -x '{ "sam_prompt": [{"type": "point", "data": [724, 740], "label": 1}] }' examples/plants-1.jpg examples/plants-1.out.png

```

**Pass extra parameters (custom model):**

```
rembg i -m u2net_custom -x '{"model_path": "~/.u2net/u2net.onnx"}' path/to/input.png path/to/output.png

```

**Use the withoutBG cloud API:**
[Get 50 free credits with signup](https://withoutbg.com/signup?ref=rembg&utm_medium=readme&utm_content=cli). [Sample results](https://withoutbg.com/pro-model-api/results?ref=rembg&utm_medium=readme&utm_content=cli).

```
export WITHOUTBG_API_KEY=sk_...
rembg i -m withoutbg path/to/input.png path/to/output.png

```

**Use the Atlas Cloud API (hosted Midjourney background removal):**

```
export ATLASCLOUD_API_KEY=apikey-...
rembg i -m atlascloud path/to/input.png path/to/output.png

```

The job is asynchronous and can take over a minute per image. Pick another [Atlas Cloud](https://www.atlascloud.ai) model with `ATLASCLOUD_MODEL` or `-x '{"model": "midjourney/v8.1/remove-background"}'`.
Or pass the key via extras:

```
rembg i -m withoutbg -x '{"api_key":"sk_..."}' path/to/input.png path/to/output.png

```

### rembg `p`[](https://pypi.org/project/rembg/#user-content-rembg-p)
Used for batch processing entire folders.
**Process all images in a folder:**

```
rembg p path/to/input path/to/output

```

**Watch mode (process new/changed files automatically):**

```
rembg p -w path/to/input path/to/output

```

### rembg `s`[](https://pypi.org/project/rembg/#user-content-rembg-s)
Used to start an HTTP server.

```
rembg s --host 0.0.0.0 --port 7000 --log_level info

```

For complete API documentation, visit: `http://localhost:7000/api`
**Disable the Gradio UI (reduces idle CPU usage):**

```
rembg s --no-ui

```

**Remove background from an image URL:**

```
curl -s "http://localhost:7000/api/remove?url=http://input.png" -o output.png

```

**Remove background from an uploaded image:**

```
curl -s -F file=@/path/to/input.jpg "http://localhost:7000/api/remove" -o output.png

```

### rembg `b`[](https://pypi.org/project/rembg/#user-content-rembg-b)
Process a sequence of RGB24 images from stdin. This is intended to be used with programs like FFmpeg that output RGB24 pixel data to stdout.

```
rembg b <width> <height> -o <output_specifier>

```

**Arguments:**  
| Argument  | Description  |  
| --- | --- |  
| `width`  | Width of input image(s)  |  
| `height`  | Height of input image(s)  |  
| `output_specifier`  | Printf-style specifier for output filenames (e.g., `output-%03u.png` produces `output-000.png`, `output-001.png`, etc.). Omit to write to stdout.  |  
**Example with FFmpeg:**

```
ffmpeg -i input.mp4 -ss 10 -an -f rawvideo -pix_fmt rgb24 pipe:1 | rembg b 1280 720 -o folder/output-%03u.png

```

> **Note:** The width and height must match FFmpeg's output dimensions. The flags `-an -f rawvideo -pix_fmt rgb24 pipe:1` are required for FFmpeg compatibility.
## Usage as a Library[](https://pypi.org/project/rembg/#user-content-usage-as-a-library)
**Input and output as bytes:**

```
from rembg import remove

with open('input.png', 'rb') as i:
    with open('output.png', 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

```

**Input and output as a PIL image:**

```
from rembg import remove
from PIL import Image

input = Image.open('input.png')
output = remove(input)
output.save('output.png')

```

**Input and output as a NumPy array:**

```
from rembg import remove
import cv2

input = cv2.imread('input.png')
output = remove(input)
cv2.imwrite('output.png', output)

```

**Force output as bytes:**

```
from rembg import remove

with open('input.png', 'rb') as i:
    with open('output.png', 'wb') as o:
        input = i.read()
        output = remove(input, force_return_bytes=True)
        o.write(output)

```

**Batch processing with session reuse (recommended for performance):**

```
from pathlib import Path
from rembg import remove, new_session

session = new_session()

for file in Path('path/to/folder').glob('*.png'):
    input_path = str(file)
    output_path = str(file.parent / (file.stem + ".out.png"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, session=session)
            o.write(output)

```

**withoutBG cloud API:**
[Get 50 free credits with signup](https://withoutbg.com/signup?ref=rembg&utm_medium=readme&utm_content=python). [Sample results](https://withoutbg.com/pro-model-api/results?ref=rembg&utm_medium=readme&utm_content=python).

```
from rembg import remove, new_session

session = new_session("withoutbg", api_key="sk_...")
# or set WITHOUTBG_API_KEY and omit api_key=

with open('input.png', 'rb') as i:
    with open('output.png', 'wb') as o:
        output = remove(i.read(), session=session)
        o.write(output)

```

**Atlas Cloud API:**

```
from rembg import remove, new_session

session = new_session("atlascloud", api_key="apikey-...")
# or set ATLASCLOUD_API_KEY and omit api_key=

with open('input.png', 'rb') as i:
    with open('output.png', 'wb') as o:
        output = remove(i.read(), session=session)
        o.write(output)

```

For more examples, see the [examples](https://pypi.org/project/rembg/USAGE.md) page.
## Choosing an edge mode[](https://pypi.org/project/rembg/#user-content-choosing-an-edge-mode)
Rembg has three ways to turn a mask into a cutout. They differ only in how they treat the _soft_ pixels along an edge — hair, fur, fabric, motion blur.  
| Mode  | Flag  | Fixes edge color  | Refines the mask  | Cost  |  
| --- | --- | --- | --- | --- |  
| Naive  | _(default)_  | No  | No  | Free  |  
| Decontaminate  | `-dc`  | Yes  | No  | Negligible  |  
| Alpha matting  | `-a`  | Yes  | Yes  | Slow  |  
| ViTMatte  | `-vm`  | Yes  | Yes  | Slow, extra download  |  
They are alternatives, not layers — `-a` already decontaminates internally, so passing both changes nothing. Pick one:
**Use the default (naive)** when the subject has hard edges — products, cars, logos, screenshots — or when the background was already close in color to the subject. There is nothing to correct, so the extra work buys nothing.
**Use`-dc`** when the cutout has a colored halo: the subject was shot against a strongly colored background (green grass, blue sky, a painted wall) and that color survives as a rim around hair or fine detail. This is the common case, and it is cheap enough to leave on for a whole batch.
**Use`-a`** when the _shape_ of the mask is wrong, not just its color — the model cut through strands of hair, or left a hard stair-stepped edge where the subject is genuinely soft. It re-estimates coverage with a closed-form solver, and it is much slower than `-dc`. That solver can fail to converge on some images; rembg falls back to a decontaminated cutout when that happens.
**Use`-vm`** for the same problem as `-a`, when you want the fine detail back. ViTMatte predicts the alpha with a network instead of solving for it, so it recovers more of the wispy strands `-a` tends to clip, and it cannot fail to converge. It costs an extra ~110 MB download on first use and runs slower than `-a`. Pick a different checkpoint with `-x '{"vitmatte_model": "base-distinctions-646"}'`:  
| Checkpoint  | Download  | Notes  |  
| --- | --- | --- |  
| `small-distinctions-646`  | ~110 MB  | The default. Best quality per byte.  |  
| `small-composition-1k`  | ~110 MB  | Trained on synthetic composites.  |  
| `base-distinctions-646`  | ~380 MB  | Slightly more detail, ~2.5x the runtime.  |  
| `base-composition-1k`  | ~380 MB  | Larger, synthetic training set.  |  
### Which model to pair it with[](https://pypi.org/project/rembg/#user-content-which-model-to-pair-it-with)
The newer models (`bria-rmbg`, `birefnet-*`, `isnet-general-use`) already produce a soft, well-shaped alpha, so their masks rarely need `-a` — reach for `-dc` first and only try `-a` if the edge shape itself is wrong. `bria-rmbg` is the default, so this is the advice that applies unless you pass `-m`.
The older models (`u2net`, `u2netp`, `silueta`) tend to produce firmer, blockier edges. They benefit most from `-a` on hair-heavy portraits, and are also where its solver is most likely to struggle.
For portraits specifically, `birefnet-portrait` with `-dc` is a good starting point, and `-vm` when the hair detail matters more than the runtime. If you are batch-processing and cannot inspect each result, prefer `-dc` over `-a`: it is faster and cannot fail.
> Note: `-ppm` (post-process mask) thresholds the mask into a fully binary one, which leaves no partially transparent pixels at all. Combining it with `-dc` is pointless — there is nothing left to correct. Use one or the other.
## Color decontamination[](https://pypi.org/project/rembg/#user-content-color-decontamination)
On a soft edge — hair, fur, motion blur — a pixel is not purely foreground or purely background. The camera captured a blend of the two:

```
captured = alpha * foreground + (1 - alpha) * background

```

Making that pixel semi-transparent does not undo the blend, so the background color stays mixed into it and shows up as a colored halo around fine detail. A subject shot against green grass keeps a green rim; against a blue wall, a blue one. This is the same operation Photoshop calls _Decontaminate Colors_ and Nuke calls _decontamination_.
Rembg can estimate the true foreground color and write that instead. This is opt-in:

```
from rembg import remove

output = remove(input, decontaminate=True)

```

```
rembg i -dc path/to/input.png path/to/output.png   # single file
rembg p -dc path/to/input path/to/output           # folder

```

```
curl -s "http://localhost:7000/api/remove?url=...&dc=true" > output.png

```

Notes:
  * It only changes color, never coverage — the alpha channel is untouched.
  * The cost is negligible next to model inference, which dominates runtime.
  * `--alpha-matting` already does this internally, so the flag is ignored there.


## Usage with Docker[](https://pypi.org/project/rembg/#user-content-usage-with-docker)
### CPU Only[](https://pypi.org/project/rembg/#user-content-cpu-only)
Replace the `rembg` command with `docker run danielgatis/rembg`:

```
docker run -v .:/data danielgatis/rembg i /data/input.png /data/output.png

```

### NVIDIA CUDA GPU Acceleration[](https://pypi.org/project/rembg/#user-content-nvidia-cuda-gpu-acceleration)
**Requirements:** Your host must have the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) installed.
CUDA acceleration requires `cudnn-devel`, so you need to build the Docker image yourself. See [#668](https://github.com/danielgatis/rembg/issues/668#issuecomment-2689914205) for details.
**Build the image:**

```
docker build -t rembg-nvidia-cuda-cudnn-gpu -f Dockerfile_nvidia_cuda_cudnn_gpu .

```

> **Note:** This image requires ~11GB of disk space (CPU version is ~1.6GB). Models are not included.
**Run the container:**

```
sudo docker run --rm -it --gpus all -v /dev/dri:/dev/dri -v $PWD:/data rembg-nvidia-cuda-cudnn-gpu i -m birefnet-general /data/input.png /data/output.png

```

**Tips:**
  * You can create your own NVIDIA CUDA image and install `rembg[gpu,cli]` in it.
  * Use `-v /path/to/models/:/root/.rembg` to store model files outside the container, avoiding re-downloads.


## Models[](https://pypi.org/project/rembg/#user-content-models)
Local ONNX models are automatically downloaded on first use and saved under `~/.rembg/models/` (see [Where models are stored](https://pypi.org/project/rembg/#user-content-where-models-are-stored)). The `withoutbg` model is a cloud API backend and does not download a local model.
### Available Models[](https://pypi.org/project/rembg/#user-content-available-models)
Sample results and benchmark scores for each model are hosted by [withoutBG](https://withoutbg.com/?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=disclosure), which supports rembg: signups through these links help fund the project.
  * u2net ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx), [source](https://github.com/xuebinqin/U-2-Net), [sample results](https://withoutbg.com/models/u2net?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=u2net)): A pre-trained model for general use cases.
  * u2netp ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx), [source](https://github.com/xuebinqin/U-2-Net), [sample results](https://withoutbg.com/models/u2netp?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=u2netp)): A lightweight version of u2net model.
  * u2net_human_seg ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_human_seg.onnx), [source](https://github.com/xuebinqin/U-2-Net)): A pre-trained model for human segmentation.
  * u2net_cloth_seg ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_cloth_seg.onnx), [source](https://github.com/levindabhi/cloth-segmentation), [details](https://withoutbg.com/models/u2net_cloth_seg?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=u2net_cloth_seg)): A pre-trained model for Cloths Parsing from human portrait. Here clothes are parsed into 3 category: Upper body, Lower body and Full body.
  * silueta ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/silueta.onnx), [source](https://github.com/xuebinqin/U-2-Net/issues/295), [sample results](https://withoutbg.com/models/silueta?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=silueta)): Same as u2net but the size is reduced to 43Mb.
  * isnet-general-use ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/isnet-general-use.onnx), [source](https://github.com/xuebinqin/DIS), [sample results](https://withoutbg.com/models/isnet-general-use?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=isnet-general-use)): A new pre-trained model for general use cases.
  * isnet-anime ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/isnet-anime.onnx), [source](https://github.com/SkyTNT/anime-segmentation)): A high-accuracy segmentation for anime character.
  * sam ([download encoder](https://github.com/danielgatis/rembg/releases/download/v0.0.0/vit_b-encoder-quant.onnx), [download decoder](https://github.com/danielgatis/rembg/releases/download/v0.0.0/vit_b-decoder-quant.onnx), [source](https://github.com/facebookresearch/segment-anything), [details](https://withoutbg.com/models/sam?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=sam)): A pre-trained model for any use cases.
  * birefnet-general ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-general-epoch_244.onnx), [source](https://github.com/ZhengPeng7/BiRefNet), [sample results](https://withoutbg.com/models/birefnet-general?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=birefnet-general)): A pre-trained model for general use cases.
  * birefnet-general-fp16 ([source](https://github.com/ZhengPeng7/BiRefNet)): birefnet-general converted to float16 on first use (`pip install "rembg[fp16]"`). Roughly 30% faster on CUDA with near-identical masks; it does not reduce VRAM, and on CPU it is usually slower than birefnet-general.
  * birefnet-general-lite ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-general-bb_swin_v1_tiny-epoch_232.onnx), [source](https://github.com/ZhengPeng7/BiRefNet), [sample results](https://withoutbg.com/models/birefnet-general-lite?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=birefnet-general-lite)): A light pre-trained model for general use cases.
  * birefnet-portrait ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-portrait-epoch_150.onnx), [source](https://github.com/ZhengPeng7/BiRefNet), [sample results](https://withoutbg.com/models/birefnet-portrait?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=birefnet-portrait)): A pre-trained model for human portraits.
  * birefnet-dis ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-DIS-epoch_590.onnx), [source](https://github.com/ZhengPeng7/BiRefNet), [sample results](https://withoutbg.com/models/birefnet-dis?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=birefnet-dis)): A pre-trained model for dichotomous image segmentation (DIS).
  * birefnet-hrsod ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-HRSOD_DHU-epoch_115.onnx), [source](https://github.com/ZhengPeng7/BiRefNet), [sample results](https://withoutbg.com/models/birefnet-hrsod?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=birefnet-hrsod)): A pre-trained model for high-resolution salient object detection (HRSOD).
  * birefnet-cod ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-COD-epoch_125.onnx), [source](https://github.com/ZhengPeng7/BiRefNet)): A pre-trained model for concealed object detection (COD).
  * birefnet-massive ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-massive-TR_DIS5K_TR_TEs-epoch_420.onnx), [source](https://github.com/ZhengPeng7/BiRefNet), [sample results](https://withoutbg.com/models/birefnet-massive?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=birefnet-massive)): A pre-trained model with massive dataset.
  * bria-rmbg ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/bria-rmbg-2.0.onnx), [source](https://huggingface.co/briaai/RMBG-2.0), [sample results](https://withoutbg.com/models/bria-rmbg?ref=rembg&utm_medium=readme&utm_campaign=models&utm_content=bria-rmbg)): **The default.** A state-of-the-art background removal model by BRIA AI. At ~1.02 GB it is the largest local model here and runs at 1024x1024, so it is slower than u2net; pass `-m u2net` for a smaller, faster model with blockier edges. Note that RMBG-2.0 is released under a [BRIA license](https://huggingface.co/briaai/RMBG-2.0) that requires a paid agreement for commercial use. Model weights carry their own licenses, independent of rembg's MIT license — check the linked source before using any model commercially.
  * withoutbg ([API](https://withoutbg.com/?ref=rembg&utm_medium=readme&utm_content=models), [sample results](https://withoutbg.com/pro-model-api/results?ref=rembg&utm_medium=readme&utm_content=models)): Cloud API backend. [Get 50 free credits with signup](https://withoutbg.com/signup?ref=rembg&utm_medium=readme&utm_content=models). Pass `api_key` via `-x` / `new_session(...)`, or set `WITHOUTBG_API_KEY`. Images are sent to withoutBG's servers; max upload size is 20 MB.
  * atlascloud ([API](https://www.atlascloud.ai)): Cloud API backend running `midjourney/v8.2/remove-background` by default. Pass `api_key` via `-x` / `new_session(...)`, or set `ATLASCLOUD_API_KEY`; change the model with `model` or `ATLASCLOUD_MODEL`. Requests are asynchronous and can take over a minute. Images are sent to Atlas Cloud's servers; max upload size is 20 MB.


## Environment Variables[](https://pypi.org/project/rembg/#user-content-environment-variables)  
| Variable  | Description  |  
| --- | --- |  
| `REMBG_HOME`  | Path to the directory where models are stored. Defaults to `$XDG_DATA_HOME/rembg` (or `~/.rembg` if `XDG_DATA_HOME` is not set).  |  
| `XDG_DATA_HOME`  | Base data directory used when `REMBG_HOME` is not set.  |  
| `U2NET_HOME`  | Deprecated. Still honored, and still takes precedence over `REMBG_HOME` when set, so existing setups keep working. Prefer `REMBG_HOME`.  |  
| `MODEL_CHECKSUM_DISABLED`  | When set (e.g. `MODEL_CHECKSUM_DISABLED=1`), disables hash verification for downloaded models. This is useful if you want to use your own custom/converted model files without rembg re-downloading the originals.  |  
| `OMP_NUM_THREADS`  | Sets the number of threads used by ONNX Runtime for inference.  |  
| `WITHOUTBG_API_KEY`  | API key for the `withoutbg` cloud session. [Get 50 free credits with signup](https://withoutbg.com/signup?ref=rembg&utm_medium=readme&utm_content=env).  |  
| `ATLASCLOUD_API_KEY`  | API key for the `atlascloud` cloud session.  |  
| `ATLASCLOUD_MODEL`  | Atlas Cloud model used by the `atlascloud` session. Defaults to `midjourney/v8.2/remove-background`.  |  
### Where models are stored[](https://pypi.org/project/rembg/#user-content-where-models-are-stored)
Each model gets its own directory under `~/.rembg/models/`:

```
~/.rembg/models/u2net/u2net.onnx
~/.rembg/models/birefnet-general/birefnet-general.onnx
~/.rembg/models/sam/sam_vit_b_01ec64.encoder.onnx
~/.rembg/models/sam/sam_vit_b_01ec64.decoder.onnx

```

Earlier versions put every model straight into `~/.u2net/`, regardless of its architecture. That directory is still read, so upgrading never re-downloads a model you already have. New downloads go to the layout above.
To move existing downloads across:

```
rembg m --dry-run     # show what would move
rembg m               # copy into the new layout, leaving the originals alone

```

The originals are kept unless you pass `--delete-source`, so a partial run can never lose a multi-gigabyte download. Interrupted downloads leave `tmp*` files behind; `--clean-orphans` removes those.
### Using custom model files[](https://pypi.org/project/rembg/#user-content-using-custom-model-files)
If you need to use a modified version of a model (e.g. converted to a different ONNX IR version for compatibility with an older CUDA toolkit), you can prevent rembg from overwriting it:
  1. Set `MODEL_CHECKSUM_DISABLED=1`
  2. Place your custom `.onnx` file in that model's directory (e.g. `~/.rembg/models/u2net/u2net.onnx`) with the expected filename
  3. Rembg will detect the file exists and use it without re-downloading


Paths passed as `model_path` must sit inside `~/.rembg` or the legacy `~/.u2net`; anything else is rejected.
## FAQ[](https://pypi.org/project/rembg/#user-content-faq)
### When will this library support Python version 3.xx?[](https://pypi.org/project/rembg/#user-content-when-will-this-library-support-python-version-3xx)
This library depends on [onnxruntime](https://pypi.org/project/onnxruntime). Python version support is determined by onnxruntime's compatibility.
## Support[](https://pypi.org/project/rembg/#user-content-support)
If you find this project useful, consider buying me a coffee (or a beer):
[![Buy Me A Coffee](https://pypi-camo.freetls.fastly.net/b0a6d1bd12e9b2c851f743fd08c58e0e7f37be03/68747470733a2f2f626d632d63646e2e6e7963332e6469676974616c6f6365616e7370616365732e636f6d2f424d432d627574746f6e2d696d616765732f637573746f6d5f696d616765732f6f72616e67655f696d672e706e67)](https://www.buymeacoffee.com/danielgatis)
## License[](https://pypi.org/project/rembg/#user-content-license)
Copyright (c) 2020-present [Daniel Gatis](https://github.com/danielgatis)
Licensed under the [MIT License](https://pypi.org/project/rembg/LICENSE.txt).
## Project links
  * [ Homepage](https://github.com/danielgatis/rembg)
  * [ Repository](https://github.com/danielgatis/rembg)


## Key dates
PyPI data
Data sourced directly from PyPI's database.
  * **Released:** Oct 21, 2026

Latest release
##  1 maintainer 
PyPI data
Data sourced directly from PyPI's database.
[ ![Avatar for danielgatis from gravatar.com](https://pypi-camo.freetls.fastly.net/951634ee9e72e4cc0411bfe1254e27a60aba2a61/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f33353830613535616462656432323364613166663633323465323966636566383f73697a653d3335) danielgatis ](https://pypi.org/user/danielgatis/)
## Credits
Data verified by PyPI on Oct 21, 2026
Data provided by the project maintainers, verified at the time the release was uploaded to PyPI. Confirms that the provided email matches a verified, public email address on a PyPI user account associated with the project.
**Author:** Daniel Gatis
## License
MIT License (MIT)
## Requires
**Python** <4.0, >=3.11
## Provides Extra
`cli` `cpu` `dev` `fp16` `gpu` `rocm`
## Tags
`remove` `background` `u2net`
## Classifiers
  * License 
    * [ OSI Approved :: MIT License ](https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License)
  * Programming Language 
    * [ Python ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python)
    * [ Python :: 3 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3)
    * [ Python :: 3 :: Only ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3+%3A%3A+Only)
    * [ Python :: 3.11 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.11)
    * [ Python :: 3.12 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.12)
    * [ Python :: 3.13 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.13)
    * [ Python :: 3.14 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.14)
    * [ Python :: 3.15 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.15)
  * Topic 
    * [ Scientific/Engineering ](https://pypi.org/search/?c=Topic+%3A%3A+Scientific%2FEngineering)
    * [ Scientific/Engineering :: Artificial Intelligence ](https://pypi.org/search/?c=Topic+%3A%3A+Scientific%2FEngineering+%3A%3A+Artificial+Intelligence)
    * [ Scientific/Engineering :: Mathematics ](https://pypi.org/search/?c=Topic+%3A%3A+Scientific%2FEngineering+%3A%3A+Mathematics)
    * [ Software Development ](https://pypi.org/search/?c=Topic+%3A%3A+Software+Development)
    * [ Software Development :: Libraries ](https://pypi.org/search/?c=Topic+%3A%3A+Software+Development+%3A%3A+Libraries)
    * [ Software Development :: Libraries :: Python Modules ](https://pypi.org/search/?c=Topic+%3A%3A+Software+Development+%3A%3A+Libraries+%3A%3A+Python+Modules)


## Metadata
## Project links
  * [ Homepage](https://github.com/danielgatis/rembg)
  * [ Repository](https://github.com/danielgatis/rembg)


## Key dates
PyPI data
Data sourced directly from PyPI's database.
  * **Released:** Oct 21, 2026

Latest release
##  1 maintainer 
PyPI data
Data sourced directly from PyPI's database.
[ ![Avatar for danielgatis from gravatar.com](https://pypi-camo.freetls.fastly.net/951634ee9e72e4cc0411bfe1254e27a60aba2a61/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f33353830613535616462656432323364613166663633323465323966636566383f73697a653d3335) danielgatis ](https://pypi.org/user/danielgatis/)
## Credits
Data verified by PyPI on Oct 21, 2026
Data provided by the project maintainers, verified at the time the release was uploaded to PyPI. Confirms that the provided email matches a verified, public email address on a PyPI user account associated with the project.
**Author:** Daniel Gatis
## License
MIT License (MIT)
## Requires
**Python** <4.0, >=3.11
## Provides Extra
`cli` `cpu` `dev` `fp16` `gpu` `rocm`
## Tags
`remove` `background` `u2net`
## Classifiers
  * License 
    * [ OSI Approved :: MIT License ](https://pypi.org/search/?c=License+%3A%3A+OSI+Approved+%3A%3A+MIT+License)
  * Programming Language 
    * [ Python ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python)
    * [ Python :: 3 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3)
    * [ Python :: 3 :: Only ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3+%3A%3A+Only)
    * [ Python :: 3.11 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.11)
    * [ Python :: 3.12 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.12)
    * [ Python :: 3.13 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.13)
    * [ Python :: 3.14 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.14)
    * [ Python :: 3.15 ](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.15)
  * Topic 
    * [ Scientific/Engineering ](https://pypi.org/search/?c=Topic+%3A%3A+Scientific%2FEngineering)
    * [ Scientific/Engineering :: Artificial Intelligence ](https://pypi.org/search/?c=Topic+%3A%3A+Scientific%2FEngineering+%3A%3A+Artificial+Intelligence)
    * [ Scientific/Engineering :: Mathematics ](https://pypi.org/search/?c=Topic+%3A%3A+Scientific%2FEngineering+%3A%3A+Mathematics)
    * [ Software Development ](https://pypi.org/search/?c=Topic+%3A%3A+Software+Development)
    * [ Software Development :: Libraries ](https://pypi.org/search/?c=Topic+%3A%3A+Software+Development+%3A%3A+Libraries)
    * [ Software Development :: Libraries :: Python Modules ](https://pypi.org/search/?c=Topic+%3A%3A+Software+Development+%3A%3A+Libraries+%3A%3A+Python+Modules)


## Release files for rembg 2.0.86
For a detailed explanation of source distributions (sdists) and built distributions (wheels), please see the [package formats documentation](https://packaging.python.org/en/latest/discussions/package-formats/#package-formats "External link"). 
###  Source distribution (sdist)   
Source distribution for rembg 2.0.86  
| File  | Size  | Uploaded  | Provenance  |   |  
| --- | --- | --- | --- | --- |  
|  [ rembg-2.0.86.tar.gz](https://files.pythonhosted.org/packages/0e/01/cfbd8fe98ba718451c58c35b8687b1ad60623014b50cc32e6a1c0e31f4ed/rembg-2.0.86.tar.gz)  | 52.8 kB  |  Oct 21, 2026  |  Without provenance  |  [Details](https://pypi.org/project/rembg/#rembg-2.0.86.tar.gz)  |  
* * *
###  Built distribution (wheel)   
Table of built distributions (wheels) for rembg 2.0.86  
| File  |  Interpreter   |  ABI   |  Platform   |  [Reset](https://pypi.org/project/rembg/#files)  |  
| --- | --- | --- | --- | --- |  
|  [ rembg-2.0.86-py3-none-any.whl](https://files.pythonhosted.org/packages/0b/68/2f9d97f736ae7a861dbb99e4337dfd8ba02782dca0beb90b5db2f66e7c92/rembg-2.0.86-py3-none-any.whl) 67.8 kB Oct 21, 2026 Without provenance  |  Python 3   |  none   |  any   |  [Details](https://pypi.org/project/rembg/#rembg-2.0.86-py3-none-any.whl)  |  
* * *
**Total release size:** 120.6 kB 
##  [Release files](https://pypi.org/project/rembg/#files) / rembg-2.0.86.tar.gz   
| Download URL  |  [ rembg-2.0.86.tar.gz ](https://files.pythonhosted.org/packages/0e/01/cfbd8fe98ba718451c58c35b8687b1ad60623014b50cc32e6a1c0e31f4ed/rembg-2.0.86.tar.gz)  |  
| --- | --- |  
| Size  | 52.8 kB  |  
| Tags  |  Source  |  
|  SHA-256 checksum   
[How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")  |  `             9c409038acbd52cc2f5e0183c9d0c155aa3798d0707e0f82f71dcdb6937e2dbf                            __                        `  |  
|  BLAKE2b-256 checksum   
[How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")  |  `             0e01cfbd8fe98ba718451c58c35b8687b1ad60623014b50cc32e6a1c0e31f4ed                            __                        `  |  
| Upload date  | Oct 21, 2026  |  
|  Uploaded using Trusted Publishing?   
[What is trusted publishing?](https://docs.pypi.org/trusted-publishers/)  |  No   |  
| Uploaded via  |  `poetry/2.5.1 CPython/3.13.9 Linux/7.0.0-1017-azure`  |  
##  [Release files](https://pypi.org/project/rembg/#files) / rembg-2.0.86-py3-none-any.whl   
| Download URL  |  [ rembg-2.0.86-py3-none-any.whl ](https://files.pythonhosted.org/packages/0b/68/2f9d97f736ae7a861dbb99e4337dfd8ba02782dca0beb90b5db2f66e7c92/rembg-2.0.86-py3-none-any.whl)  |  
| --- | --- |  
| Size  | 67.8 kB  |  
| Tags  |  Python 3  |  
|  SHA-256 checksum   
[How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")  |  `             1db1af3d65fdab16724dbd96b8b0a828dd02ac68efe95a3d8e1010a1517412a6                            __                        `  |  
|  BLAKE2b-256 checksum   
[How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")  |  `             0b682f9d97f736ae7a861dbb99e4337dfd8ba02782dca0beb90b5db2f66e7c92                            __                        `  |  
| Upload date  | Oct 21, 2026  |  
|  Uploaded using Trusted Publishing?   
[What is trusted publishing?](https://docs.pypi.org/trusted-publishers/)  |  No   |  
| Uploaded via  |  `poetry/2.5.1 CPython/3.13.9 Linux/7.0.0-1017-azure`  |  
## Security for rembg 2.0.86
[Report project as malware](https://pypi.org/project/rembg/submit-malware-report/)
### Provenance
**Provenance** describes where a file came from. On PyPI, provenance is shared via **attestations** , which provide a verifiable record of the build or publishing details. [View details, limitations and caveats.](https://docs.pypi.org/using-pypi/package-security/provenance/)
###  No provenance found 
None of the files in this release were uploaded with provenance metadata.
### A note on package security
PyPI is a repository for distributing packages, not a service for auditing them. While third-party security researchers and our staff do their best to detect and remove malicious packages, PyPI cannot guarantee the quality, security or suitability of any given package. 
To learn more about protecting yourself from malicious actors, visit our [package security documentation](https://docs.pypi.org/using-pypi/package-security/introduction/). 
##  Release history [Release notifications](https://docs.pypi.org/api/feeds/#project-releases-feed) | [RSS feed ](https://pypi.org/rss/project/rembg/releases.xml)
This release
![](https://pypi.org/static/images/blue-cube.572a5bfb.svg)
[2.0.86](https://pypi.org/project/rembg/2.0.86/) This release
Oct 21, 2026 [2 release files](https://pypi.org/project/rembg/2.0.86/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.86/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.85](https://pypi.org/project/rembg/2.0.85/)
Sep 20, 2026 [2 release files](https://pypi.org/project/rembg/2.0.85/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.85/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.84](https://pypi.org/project/rembg/2.0.84/)
Sep 7, 2026 [2 release files](https://pypi.org/project/rembg/2.0.84/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.84/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.83](https://pypi.org/project/rembg/2.0.83/)
Sep 2, 2026 [2 release files](https://pypi.org/project/rembg/2.0.83/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.83/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.82](https://pypi.org/project/rembg/2.0.82/)
Sep 2, 2026 [2 release files](https://pypi.org/project/rembg/2.0.82/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.82/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.81](https://pypi.org/project/rembg/2.0.81/)
Aug 18, 2026 [2 release files](https://pypi.org/project/rembg/2.0.81/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.81/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.80](https://pypi.org/project/rembg/2.0.80/)
Aug 17, 2026 [2 release files](https://pypi.org/project/rembg/2.0.80/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.80/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.79](https://pypi.org/project/rembg/2.0.79/)
Aug 16, 2026 [2 release files](https://pypi.org/project/rembg/2.0.79/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.79/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.78](https://pypi.org/project/rembg/2.0.78/)
Aug 6, 2026 [2 release files](https://pypi.org/project/rembg/2.0.78/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.78/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.77](https://pypi.org/project/rembg/2.0.77/)
Jul 18, 2026 [2 release files](https://pypi.org/project/rembg/2.0.77/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.77/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.76](https://pypi.org/project/rembg/2.0.76/)
Jun 3, 2026 [2 release files](https://pypi.org/project/rembg/2.0.76/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.76/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.75](https://pypi.org/project/rembg/2.0.75/)
Apr 8, 2026 [2 release files](https://pypi.org/project/rembg/2.0.75/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.75/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.74](https://pypi.org/project/rembg/2.0.74/)
Mar 24, 2026 [2 release files](https://pypi.org/project/rembg/2.0.74/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.74/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.73](https://pypi.org/project/rembg/2.0.73/)
Mar 15, 2026 [2 release files](https://pypi.org/project/rembg/2.0.73/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.73/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.72](https://pypi.org/project/rembg/2.0.72/)
Jan 3, 2026 [2 release files](https://pypi.org/project/rembg/2.0.72/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.72/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.71](https://pypi.org/project/rembg/2.0.71/)
Jan 3, 2026 [2 release files](https://pypi.org/project/rembg/2.0.71/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.71/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.70](https://pypi.org/project/rembg/2.0.70/)
Jan 3, 2026 [2 release files](https://pypi.org/project/rembg/2.0.70/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.70/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.69](https://pypi.org/project/rembg/2.0.69/)
Dec 4, 2025 [2 release files](https://pypi.org/project/rembg/2.0.69/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.69/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.68](https://pypi.org/project/rembg/2.0.68/)
Nov 17, 2025 [2 release files](https://pypi.org/project/rembg/2.0.68/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.68/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.67](https://pypi.org/project/rembg/2.0.67/)
Jul 5, 2025 [2 release files](https://pypi.org/project/rembg/2.0.67/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.67/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.66](https://pypi.org/project/rembg/2.0.66/)
May 14, 2025 [2 release files](https://pypi.org/project/rembg/2.0.66/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.66/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.65](https://pypi.org/project/rembg/2.0.65/)
Mar 17, 2025 [2 release files](https://pypi.org/project/rembg/2.0.65/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.65/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.64](https://pypi.org/project/rembg/2.0.64/)
Mar 6, 2025 [2 release files](https://pypi.org/project/rembg/2.0.64/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.64/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.63](https://pypi.org/project/rembg/2.0.63/)
Feb 21, 2025 [2 release files](https://pypi.org/project/rembg/2.0.63/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.63/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.62](https://pypi.org/project/rembg/2.0.62/)
Jan 30, 2025 [2 release files](https://pypi.org/project/rembg/2.0.62/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.62/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.61](https://pypi.org/project/rembg/2.0.61/)
Dec 20, 2024 [2 release files](https://pypi.org/project/rembg/2.0.61/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.61/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.60](https://pypi.org/project/rembg/2.0.60/)
Nov 19, 2024 [2 release files](https://pypi.org/project/rembg/2.0.60/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.60/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.59](https://pypi.org/project/rembg/2.0.59/)
Aug 26, 2024 [2 release files](https://pypi.org/project/rembg/2.0.59/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.59/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.58](https://pypi.org/project/rembg/2.0.58/)
Aug 4, 2024 [2 release files](https://pypi.org/project/rembg/2.0.58/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.58/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.57](https://pypi.org/project/rembg/2.0.57/)
May 23, 2024 [2 release files](https://pypi.org/project/rembg/2.0.57/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.57/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.56](https://pypi.org/project/rembg/2.0.56/)
Mar 12, 2024 [2 release files](https://pypi.org/project/rembg/2.0.56/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.56/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.55](https://pypi.org/project/rembg/2.0.55/)
Feb 24, 2024 [2 release files](https://pypi.org/project/rembg/2.0.55/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.55/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.54](https://pypi.org/project/rembg/2.0.54/)
Jan 31, 2024 [2 release files](https://pypi.org/project/rembg/2.0.54/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.54/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.53](https://pypi.org/project/rembg/2.0.53/)
Dec 5, 2023 [2 release files](https://pypi.org/project/rembg/2.0.53/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.53/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.52](https://pypi.org/project/rembg/2.0.52/)
Oct 25, 2023 [2 release files](https://pypi.org/project/rembg/2.0.52/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.52/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.51](https://pypi.org/project/rembg/2.0.51/)
Oct 20, 2023 [2 release files](https://pypi.org/project/rembg/2.0.51/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.51/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.50](https://pypi.org/project/rembg/2.0.50/)
Jul 12, 2023 [2 release files](https://pypi.org/project/rembg/2.0.50/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.50/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.49](https://pypi.org/project/rembg/2.0.49/)
Jun 29, 2023 [2 release files](https://pypi.org/project/rembg/2.0.49/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.49/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.48](https://pypi.org/project/rembg/2.0.48/)
Jun 29, 2023 [2 release files](https://pypi.org/project/rembg/2.0.48/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.48/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.47](https://pypi.org/project/rembg/2.0.47/)
Jun 21, 2023 [2 release files](https://pypi.org/project/rembg/2.0.47/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.47/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.46](https://pypi.org/project/rembg/2.0.46/)
Jun 20, 2023 [2 release files](https://pypi.org/project/rembg/2.0.46/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.46/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.45](https://pypi.org/project/rembg/2.0.45/)
Jun 19, 2023 [2 release files](https://pypi.org/project/rembg/2.0.45/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.45/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.44](https://pypi.org/project/rembg/2.0.44/)
Jun 19, 2023 [2 release files](https://pypi.org/project/rembg/2.0.44/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.44/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.43](https://pypi.org/project/rembg/2.0.43/)
Jun 2, 2023 [2 release files](https://pypi.org/project/rembg/2.0.43/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.43/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.41](https://pypi.org/project/rembg/2.0.41/)
Jun 1, 2023 [2 release files](https://pypi.org/project/rembg/2.0.41/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.41/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.40](https://pypi.org/project/rembg/2.0.40/)
Jun 1, 2023 [2 release files](https://pypi.org/project/rembg/2.0.40/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.40/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.39](https://pypi.org/project/rembg/2.0.39/)
May 30, 2023 [2 release files](https://pypi.org/project/rembg/2.0.39/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.39/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.38](https://pypi.org/project/rembg/2.0.38/)
May 29, 2023 [2 release files](https://pypi.org/project/rembg/2.0.38/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.38/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.37](https://pypi.org/project/rembg/2.0.37/)
May 15, 2023 [2 release files](https://pypi.org/project/rembg/2.0.37/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.37/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.36](https://pypi.org/project/rembg/2.0.36/)
May 9, 2023 [2 release files](https://pypi.org/project/rembg/2.0.36/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.36/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.35](https://pypi.org/project/rembg/2.0.35/)
Apr 27, 2023 [2 release files](https://pypi.org/project/rembg/2.0.35/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.35/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.34](https://pypi.org/project/rembg/2.0.34/)
Apr 24, 2023 [2 release files](https://pypi.org/project/rembg/2.0.34/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.34/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.33](https://pypi.org/project/rembg/2.0.33/)
Apr 23, 2023 [2 release files](https://pypi.org/project/rembg/2.0.33/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.33/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.32](https://pypi.org/project/rembg/2.0.32/)
Mar 31, 2023 [2 release files](https://pypi.org/project/rembg/2.0.32/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.32/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.31](https://pypi.org/project/rembg/2.0.31/)
Mar 28, 2023 [2 release files](https://pypi.org/project/rembg/2.0.31/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.31/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.30](https://pypi.org/project/rembg/2.0.30/)
Dec 20, 2022 [2 release files](https://pypi.org/project/rembg/2.0.30/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.30/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.29](https://pypi.org/project/rembg/2.0.29/)
Nov 27, 2022 [2 release files](https://pypi.org/project/rembg/2.0.29/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.29/#security)
![](https://pypi.org/static/images/white-cube.2351a86c.svg)
[2.0.28](https://pypi.org/project/rembg/2.0.28/)
Nov 24, 2022 [2 release files](https://pypi.org/project/rembg/2.0.28/#files) [ No provenance ](https://pypi.org/project/rembg/2.0.28/#security)
[ ![](https://pypi.org/static/images/white-cube.2351a86c.svg) PyPI ](https://pypi.org/)
Developed and maintained by the [Python Software Foundation](https://www.python.org/psf/ "External link") and Python community, for the Python community.
[Status: all systems operational](https://status.python.org/ "External link")
[Donate today!](https://donate.pypi.org)
## Help
  * [PyPI documentation](https://docs.pypi.org/)
  * [Getting help](https://docs.pypi.org/about/getting-help/)
  * [Installing packages](https://packaging.python.org/tutorials/installing-packages/ "External link")
  * [Uploading packages](https://packaging.python.org/tutorials/packaging-projects/ "External link")
  * [Packaging user guide](https://packaging.python.org/ "External link")


## About PyPI
  * [PyPI blog](https://blog.pypi.org)
  * [Infrastructure dashboard](https://dtdg.co/pypi "External link")
  * [Statistics](https://pypi.org/stats/)
  * [Logos & trademarks](https://pypi.org/trademarks/)
  * [Our sponsors](https://pypi.org/sponsors/)


## Contributing to PyPI
  * [Bugs and feedback](https://docs.pypi.org/about/contributing/#reporting-bugs)
  * [Contribute on GitHub](https://github.com/pypi/warehouse "External link")
  * [Translate PyPI](https://hosted.weblate.org/projects/pypa/warehouse/ "External link")
  * [Sponsor PyPI](https://pypi.org/sponsors/)
  * [Development credits](https://github.com/pypi/warehouse/graphs/contributors "External link")


## Using PyPI
  * [Terms of Service](https://policies.python.org/pypi.org/Terms-of-Service/ "External link")
  * [Report security issue](https://pypi.org/security/)
  * [Code of conduct](https://policies.python.org/python.org/code-of-conduct/ "External link")
  * [Privacy Notice](https://policies.python.org/pypi.org/Privacy-Notice/ "External link")
  * [Acceptable Use Policy](https://policies.python.org/pypi.org/Acceptable-Use-Policy/ "External link")


Switch to desktop version
[ ![](https://pypi-camo.freetls.fastly.net/0e16ff2846ab7bc04f1e52d760b072c987232f52/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f416e7468726f7069635f6c6f676f5f2d5f536c6174652e706e67) Anthropic, PBC Visionary sponsor ](https://www.anthropic.com/) [ ![](https://pypi-camo.freetls.fastly.net/2056e7cc45e271b6b509980e9ff24b8b6346f2f4/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f626c6f6f6d626572672e706e67) Bloomberg Visionary sponsor ](https://www.techatbloomberg.com/) [ ![](https://pypi-camo.freetls.fastly.net/7e24ecafc35532bbd56c7c91521ea6701110c742/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f6872742e706e67) Hudson River Trading Visionary sponsor ](https://www.hudsonrivertrading.com/careers/) [ ![](https://pypi-camo.freetls.fastly.net/6f7cbf25b7d9ee146661528e012e8fa51d6f3337/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f4d6574615f6c6f636b75705f706f7369746976655f7072696d6172795f5247425f636f70795f68546b493532472e706e67) Meta Visionary sponsor ](https://about.facebook.com/meta/) [ ![](https://pypi-camo.freetls.fastly.net/22baa32a7b36b109ce052634015d878f5d029280/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f6e76696469612e706e67) NVIDIA Visionary sponsor ](https://developer.nvidia.com) [ ![](https://pypi-camo.freetls.fastly.net/34ebcaca9a4316e862f2f7641b12534f0cb81bf1/68747470733a2f2f73332e6475616c737461636b2e75732d656173742d322e616d617a6f6e6177732e636f6d2f707974686f6e646f746f72672d6173736574732f6d656469612f73706f6e736f725f7765625f6c6f676f732f6d6963726f736f66742e706e67) Microsoft Sustainability sponsor ](https://aka.ms/python) [ ![](https://pypi-camo.freetls.fastly.net/237c8773674b9f8beff9f894a07424e3b579cd6a/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f6465706f742d636f6c6f722d6c6f676f2d35567a75416e7a6b2e706e67) Depot Continuous Integration ](https://depot.dev) [ ![](https://pypi-camo.freetls.fastly.net/f0e9bd2edb2aa1c533d61b0d4fda0ee761bef88a/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f6177732d636f6c6f722d6c6f676f2d416c6f43525230612e706e67) AWS Cloud computing and Security Sponsor ](https://aws.amazon.com/) [ ![](https://pypi-camo.freetls.fastly.net/530379bec76c3440bd94a24092f49e27323ad0d7/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f64617461646f672d636f6c6f722d6c6f676f2d71616563774a67722e706e67) Datadog Monitoring ](https://www.datadoghq.com/) [ ![](https://pypi-camo.freetls.fastly.net/9706778018adad6f5bf682f55d7bbc226abe551c/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f666173746c792d636f6c6f722d6c6f676f2d766c6d424c33654c2e706e67) Fastly CDN ](https://www.fastly.com/) [ ![](https://pypi-camo.freetls.fastly.net/522342e78db3080c18697369dde99a0ed7925e86/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f676f6f676c652d636f6c6f722d6c6f676f2d32755437496c54702e706e67) Google Download Analytics ](https://careers.google.com/) [ ![](https://pypi-camo.freetls.fastly.net/f2a422796f8e4d51d60d7030b7973aa1651bd096/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f73656e7472792d636f6c6f722d6c6f676f2d346e306a654878502e706e67) Sentry Error logging ](https://sentry.io/for/python/?utm_source=pypi&utm_medium=paid-community&utm_campaign=python-na-evergreen&utm_content=static-ad-pypi-sponsor-learnmore) [ ![](https://pypi-camo.freetls.fastly.net/b0ba0741ac65afcb01ebb4bbf0634c54b8a15827/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f737461747573706167652d636f6c6f722d6c6f676f2d423232436b746e6b2e706e67) StatusPage Status page ](https://statuspage.io)
  * "PyPI", "Python Package Index", and the blocks logos are registered [trademarks](https://pypi.org/trademarks/) of the [Python Software Foundation](https://www.python.org/psf-landing).
  * © 2026 [Python Software Foundation](https://www.python.org/psf-landing/ "External link")
  * [Site map](https://pypi.org/sitemap/)
  * Deployed from [`68dc61b`](https://github.com/pypi/warehouse/commit/68dc61bfbf31633506f3f03c3a93b34220857cfc "External link")



