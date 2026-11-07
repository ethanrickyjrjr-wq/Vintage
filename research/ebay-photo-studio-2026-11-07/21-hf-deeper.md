# Lane 21: Hugging Face deeper (BiRefNet matting variants, ONNX, BEN2)

Status line: date 2026-11-07. Fetched: all cards, file lists and handler.py below were read through the Hugging Face MCP tools (label MCP_DATA); the four rembg session sources were fetched with tools/crawl-cloud.sh from raw.githubusercontent.com (label VERIFIED_FETCHED). Blocked: huggingface.co web (not needed). Not done: nothing was run, no GPU here, so every speed, VRAM or quality statement is either quoted from a card or marked UNVERIFIED.
Saved evidence: research/ebay-photo-studio-2026-11-07/raw/21-hf-deeper/. Note on the saved cards: the author and badge headers and BibTeX blocks are trimmed; usage code, file lists, licences and quoted sentences are verbatim. The rembg sources are saved whole.

## 1. Variant table (all MCP_DATA unless marked)

| Variant (repo) | Licence | Trained at | Input size to feed | FP16 / VRAM / speed claim | File and size |
|---|---|---|---|---|---|
| ZhengPeng7/BiRefNet_HR-matting | mit | "trained with images in `2048x2048` for higher resolution image matting with transparency" | 2048x2048 (card snippet `image_size = (2048, 2048)`) | Card: "All tested in FP16 mode." No VRAM or seconds figure anywhere in the card | model.safetensors 444,473,596 bytes (about 424 MiB) |
| ZhengPeng7/BiRefNet-matting | mit | Card does not state a size; HR-matting card tests it at 1024x1024 and 2048x2048 | 1024x1024 (the HR card table gives it .973 maxFm at 1024 and .971 at 2048 on TE-AM-2k, so 2048 buys nothing for this one) | none | model.safetensors 884,878,856 bytes (about 844 MiB; twice the HR file, suggesting fp32 weights vs fp16 in HR, UNVERIFIED inference from sizes) |
| ZhengPeng7/BiRefNet_dynamic | mit | "arbitrary shapes (256x256 ~ 2304x2304)" | Any shape in that range; card comments out the Resize ("the resizing is not necessary") | none in text (performance only as images) | model.safetensors 444,473,596 bytes |
| ZhengPeng7/BiRefNet_lite-2K | mit | 2K; card says "Remember to set the resolution of input images to 2K (2560, 1440)" | 2560x1440 (handler.py uses resolution (2560, 1440) for General-Lite-2K) | none | model.safetensors 177,634,392 bytes (about 169 MiB) |
| ZhengPeng7/BiRefNet (general) | mit | 1024 | 1024x1024 | none | model.safetensors 444,473,596 bytes |
| PramaLLC/BEN2 | mit (front matter) | not stated in card | 1024x1024 in its own onnx_run.py (Resize((1024, 1024))); the python API handles sizing itself, card silent | none | model.safetensors 380,577,976; BEN2_Base.pth 1,134,584,206; BEN2_Base.onnx 222,932,053 |

Training data (quoted from cards): BiRefNet-matting lists P3M-10k, TR-humans, AM-2k, AIM-500, Human-2k, Distinctions-646, HIM2K, PPM-100. BiRefNet_lite-2K lists DIS5K, HRS10K, UHRSD plus the same matting sets. The HR-matting card lists no training sets at all (UNCONFIRMED what it was trained on beyond "image matting"; its test sets are TE-AM-2k and TE-P3M-500-NP).

Benchmark numbers on the HR-matting card (FP16, 2048x2048): TE-AM-2k wFmeasure .997, MAE .002; TE-P3M-500-NP wFmeasure .996, MAE .002. The card's column headers are misaligned with its cells, so read these with care. Same card, BiRefNet-matting at 1024x1024 on TE-AM-2k: wFmeasure .996. The honest reading: on these two benchmarks HR-matting and matting are nearly tied; the HR advantage is in boundary metrics (mBA .879 vs .846 at TE-AM-2k, maxBIoU .965 vs .952), which is the fringe/edge area Ricky cares about.

## 2. Windows Python snippet (transformers route)

Only what the cards and handler.py show. Flagged items follow the code.

```python
# pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128   (FLAG 1)
# pip install -r https://raw.githubusercontent.com/ZhengPeng7/BiRefNet/main/requirements.txt   (card, step 0)
# pip install opencv-python   (handler.py imports cv2 for refine_foreground; requirements.txt not read, FLAG 2)
import sys
from pathlib import Path
import numpy as np, cv2, torch
from PIL import Image
from torchvision import transforms
from transformers import AutoModelForImageSegmentation

torch.set_float32_matmul_precision("high")          # card
birefnet = AutoModelForImageSegmentation.from_pretrained(
    "ZhengPeng7/BiRefNet_HR-matting", trust_remote_code=True)   # card
birefnet.to("cuda").eval().half()                    # card: .to('cuda'), .eval(), .half()

tf = transforms.Compose([
    transforms.Resize((2048, 2048)),                 # card, HR-matting
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

def refine_foreground(image, mask, r=90):            # verbatim logic from handler.py
    mask = mask.resize(image.size) if mask.size != image.size else mask
    img = np.array(image) / 255.0
    a = (np.array(mask) / 255.0)[:, :, None]
    def est(I, F, B, alpha, r):
        ba = cv2.blur(alpha, (r, r))[:, :, None]
        bF = cv2.blur(F * alpha, (r, r)) / (ba + 1e-5)
        bB = cv2.blur(B * (1 - alpha), (r, r)) / ((1 - ba) + 1e-5)
        Fn = np.clip(bF + alpha * (I - alpha * bF - (1 - alpha) * bB), 0, 1)
        return Fn, bB
    F, bB = est(img, img, img, a, r)
    F = est(img, F, bB, a, 6)[0]
    return Image.fromarray((F * 255.0).astype(np.uint8))

def cutout(src: Path, dst: Path, refine=True):
    image = Image.open(src).convert("RGB")
    x = tf(image).unsqueeze(0).to("cuda").half()
    with torch.no_grad():
        pred = birefnet(x)[-1].sigmoid().cpu()[0].squeeze()
    mask = transforms.ToPILImage()(pred).resize(image.size)
    out = refine_foreground(image, mask) if refine else image.copy()
    out.putalpha(mask)                               # RGBA
    out.save(dst)                                    # PNG

if __name__ == "__main__":
    cutout(Path(sys.argv[1]), Path(sys.argv[2]))
```

Flags (what I could not confirm):
1. The PyTorch CUDA wheel line is not on any card. I did not verify the right wheel tag for the RTX 4060 Ti; the cards say nothing about CUDA versions or Windows. UNVERIFIED.
2. I did not read requirements.txt for any repo (149 bytes each), so I cannot say which transformers, timm, kornia or einops versions are pinned. The card step 0 installs them. Custom code (birefnet.py, 92 KB) loads with trust_remote_code=True, which runs repo code on Ricky's PC; it is MIT and the author's own repo, but it is still remote code.
3. The cards' own snippet does not call refine_foreground; handler.py does (`image_masked = refine_foreground(image, pred_pil)` then `putalpha(pred_pil.resize(image.size))`). My snippet follows handler.py. Whether refine_foreground helps on white-backdrop photos is untested. It replaces the colour of edge pixels with an estimated foreground colour, which is what removes backdrop-coloured fringe, so it matters most on lace and feathers. With r=90 on a 12 MP phone image the cv2.blur calls will be slow on CPU (UNVERIFIED, not timed).
4. VRAM and seconds per image at 2048 are not stated anywhere. The 16 GB card has a decent chance of fitting FP16 at 2048 but that is a guess; measure it with torch.cuda.max_memory_allocated().
5. The card's snippet does not call convert("RGB") before the transform; mine does (handler.py does), because iPhone HEIC/PNG with alpha would otherwise break the 3-channel normalize.
6. Downloading weights needs huggingface.co from Ricky's PC; it is blocked only in this sandbox.

## 3. Is there an ONNX that rembg could run for HR-matting?

Short answer: an ONNX file exists, but rembg cannot use it properly.

What exists (MCP_DATA):
- ZhengPeng7 repos: no .onnx anywhere (every ls shows only safetensors). The author does not publish ONNX.
- PinkPixel/birefnet-hr-matting-onnx (third party, created 7 Sep 2026, 0 downloads, MIT with the author's copyright retained): model.onnx 932,150,975; model_fp16.onnx 471,320,622; also int8, uint8, q4. Input `image` [1,3,2048,2048] float32, ImageNet normalised; output `alpha` [1,1,2048,2048] already sigmoid-activated. Its card says "self-contained ONNX export of BiRefNet_HR-matting".
- emrikol/birefnet-matting-onnx (BiRefNet-matting, 1024, fp32 940,840,787 bytes, outputs logits). Its card explains why BiRefNet ONNX is hard: "BiRefNet uses `torchvision::deform_conv2d` (deformable convolution), which neither the legacy nor the dynamo ONNX exporter supports."
- onnx-community/BiRefNet_dynamic-1024x1024-ONNX (model.onnx 972,495,971; model_fp16.onnx 489,811,221; transformers.js usage, logits output) plus a -CUDA sibling.

Why rembg cannot run the HR file (VERIFIED_FETCHED from rembg main on 2026-11-07, saved raw/21-hf-deeper/rembg-*.py.md):
- The README says `rembg i -m u2net_custom -x '{"model_path": "~/.u2net/u2net.onnx"}' in.png out.png` (raw/01-rembg/README.md line 178), and "Paths passed as `model_path` must sit inside `~/.rembg` or the legacy `~/.u2net`; anything else is rejected." So the flag is confirmed, with the path restriction.
- But the u2net_custom session hard-codes the size: `self.normalize(img, (0.485, 0.456, 0.406), (0.229, 0.224, 0.225), (320, 320))`. It also takes ort_outs[0] without sigmoid and min-max rescales. That is a 320 px U2Net recipe; fed a 2048-shaped ONNX it fails on the shape.
- dis_custom and ben_custom hard-code `(0.5, 0.5, 0.5), (1.0, 1.0, 1.0), (1024, 1024)`: wrong mean/std for BiRefNet (ImageNet) and wrong size for HR.
- birefnet_general (the built-in) uses ImageNet mean/std, `(1024, 1024)` and applies `self.sigmoid(...)`. A 1024 BiRefNet ONNX with logits output (emrikol matting, or onnx-community dynamic) would fit that session if placed as ~/.rembg/models/birefnet-general/birefnet-general.onnx with MODEL_CHECKSUM_DISABLED=1 (README lines 561 and 593 to 601 describe this replace-in-place trick). That would be the 1024 matting model, not HR. UNTESTED.
- rembg's normalize also divides by the image's max pixel rather than 255 (rembg-base.py.md line 94), a small deviation from the cards' preprocessing.
- The PinkPixel input shape is fixed at 2048 in its card, and rembg's size is fixed in code, so no rembg flag reaches it. Running that ONNX needs the 20-line onnxruntime script on its card (or the included infer.py, which has --provider cuda, --dir, --output-dir, --mask-only). That route needs no PyTorch or trust_remote_code, which is its one real advantage, but its fp16 file taking float32 input is stated only by implication (the quickstart feeds float32 to model_fp16.onnx); not confirmed. Also, nobody has verified this export numerically against the PyTorch model: 0 downloads, no stated validation.

## 4. BEN2

Install (card, verbatim): `pip install -e "git+https://github.com/PramaLLC/BEN2.git#egg=ben2"`

Inference (card, verbatim):
```python
from ben2 import BEN_Base
from PIL import Image
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
file = "./image.png" # input image
model = BEN_Base.from_pretrained("PramaLLC/BEN2")
model.to(device).eval()
image = Image.open(file)
foreground = model.inference(image, refine_foreground=False,) #Refine foreground is an extract postprocessing step that increases inference time but can improve matting edges. The default value is False.
foreground.save("./foreground.png")
```
Batch: `foregrounds = model.inference([image1, image2])` with the note "We recommend that the batch size not exceed 3 for consumer GPUs". requirements.txt lists numpy, torch, einops, Pillow, timm>=1.0.10, torchvision, onnxruntime.

Licence: front matter `license: mit`. The card contains no separate licence text; the repo file list has no LICENSE file (ls showed none). So the only licence statement is the MIT tag.

The commercial caveat, quoted: "BEN2 was trained on the DIS5k and our 22K proprietary segmentation dataset. Our enhanced model delivers superior performance in hair matting, 4K processing, object segmentation, and edge refinement. Our Base model is open source." and "For access to our commercial model email us at sales@backgrounderase.com". Reading: the open weights are the Base model; the model that is advertised as better at hair matting and 4K is the paid one, so the open BEN2 should not be expected to beat BiRefNet HR on fine fringe. The card's comparison images are not readable here and quote no numbers, so no head-to-head claim is supported. Also the card notes "RMBG 2.0 did not preserve the DIS 5k validation dataset", a note about its own comparison fairness. BEN2 also ships its own ONNX (BEN2_Base.onnx, 222,932,053 bytes, 1024 input per onnx_run.py) but rembg's ben_custom hard-codes mean 0.5/std 1.0/1024 while onnx_run.py uses plain ToTensor with no normalisation; whether those match is UNVERIFIED (ben_custom's normalize also divides by max pixel).

## 5. Which to try first on lace, fringe and feathers

Try first: ZhengPeng7/BiRefNet_HR-matting at 2048 with refine_foreground (the snippet above). Reasons, labelled:
- It is the only variant whose card says it is for "higher resolution image matting with transparency" (MCP_DATA), and the only one with a 2048 training size. Lace, fringe and feathers are sub-pixel structures at 1024; with 12 MP iPhone photos, 2048 keeps more of them (reasoning, UNVERIFIED on Ricky's photos).
- Its boundary metrics in the card (mBA .879 vs .846, maxBIoU .965 vs .952 against BiRefNet-matting at 1024 on TE-AM-2k) favour it at edges, while the headline F-measures are tied.
- AM-2k (animal matting, fur and feathers) is a test set for it and a training set for BiRefNet-matting (MCP_DATA); that is the nearest public benchmark to feathers. It says nothing about lace over a dress form.
Second: BiRefNet-matting at 1024 (smaller input, faster; the card shows 2048 gives it no gain). Third: BiRefNet_dynamic at native photo size capped near 2304 (card claims it beats BiRefNet general and HR-general on DIS-VD and TE-P3M-500-NP, with images only). BiRefNet_lite-2K is the fast option (169 MiB) at 2560x1440 but is a general model, not a matting one, and the card's own scores on DIS-VD are lower (maxFm .867). Treat BEN2 as a curiosity: its better model is paid.
Caveat for the whole group: matting models trained on people, animals and DIS objects give soft alpha, which is what lace needs, but all of them can leave the dress form's neck or base in the cutout, and dark lace on a white backdrop can punch holes; those are test-on-Ricky's-photos questions, no card answers them.

## Recommendations
1. Run the transformers snippet on 5 hard photos (lace, fringe, feathers, sequins, a dark piece) for HR-matting at 2048, matting at 1024, dynamic at native size; save the masks side by side. Measure peak VRAM and seconds.
2. Do not spend time on rembg u2net_custom, dis_custom or ben_custom for HR: their size and normalisation are hard-coded wrong. If a rembg-compatible route is wanted, it is the 1024 matting ONNX dropped in as birefnet-general.onnx, untested.
3. Treat PinkPixel's HR ONNX as an optional PyTorch-free path, to be validated against the PyTorch output on the same photos before trust; it is a 0-download third-party export.
4. Evaluate refine_foreground on and off; it is the piece that fixes coloured fringe.

## Open questions
- Does HR-matting at 2048 FP16 fit comfortably in 16 GB and how many seconds per photo? Nobody states it.
- What was HR-matting trained on? The card lists no training sets.
- Which transformers/timm versions does requirements.txt pin, and does it install cleanly on Windows with the 4060 Ti's CUDA build?
- Is PinkPixel's ONNX numerically equal to the PyTorch model (deform_conv2d handling)?
- Does BEN2 open Base match BiRefNet on fine fringe? The card gives only images.
