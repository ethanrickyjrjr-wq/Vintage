hf://models/ZhengPeng7/BiRefNet_HR-matting/handler.py (MCP_DATA, 2026-11-07). This is where refine_foreground lives (the model cards themselves do not mention it).
# These HF deployment codes refer to https://huggingface.co/not-lain/BiRefNet/raw/main/handler.py.
import cv2, numpy as np, torch
from PIL import Image
from torchvision import transforms
from transformers import AutoModelForImageSegmentation
torch.set_float32_matmul_precision(["high", "highest"][0])
device = "cuda" if torch.cuda.is_available() else "cpu"

def refine_foreground(image, mask, r=90):
    if mask.size != image.size:
        mask = mask.resize(image.size)
    image = np.array(image) / 255.0
    mask = np.array(mask) / 255.0
    estimated_foreground = FB_blur_fusion_foreground_estimator_2(image, mask, r=r)
    image_masked = Image.fromarray((estimated_foreground * 255.0).astype(np.uint8))
    return image_masked

def FB_blur_fusion_foreground_estimator_2(image, alpha, r=90):
    # Thanks to the source: https://github.com/Photoroom/fast-foreground-estimation
    alpha = alpha[:, :, None]
    F, blur_B = FB_blur_fusion_foreground_estimator(image, image, image, alpha, r)
    return FB_blur_fusion_foreground_estimator(image, F, blur_B, alpha, r=6)[0]

def FB_blur_fusion_foreground_estimator(image, F, B, alpha, r=90):
    if isinstance(image, Image.Image):
        image = np.array(image) / 255.0
    blurred_alpha = cv2.blur(alpha, (r, r))[:, :, None]
    blurred_FA = cv2.blur(F * alpha, (r, r))
    blurred_F = blurred_FA / (blurred_alpha + 1e-5)
    blurred_B1A = cv2.blur(B * (1 - alpha), (r, r))
    blurred_B = blurred_B1A / ((1 - blurred_alpha) + 1e-5)
    F = blurred_F + alpha * (image - alpha * blurred_F - (1 - alpha) * blurred_B)
    F = np.clip(F, 0, 1)
    return F, blurred_B

usage_to_weights_file = {'General':'BiRefNet','General-HR':'BiRefNet_HR','General-Lite':'BiRefNet_lite','General-Lite-2K':'BiRefNet_lite-2K','General-reso_512':'BiRefNet-reso_512','Matting':'BiRefNet-matting','Matting-HR':'BiRefNet_HR-Matting','Portrait':'BiRefNet-portrait','DIS':'BiRefNet-DIS5K','HRSOD':'BiRefNet-HRSOD','COD':'BiRefNet-COD','DIS-TR_TEs':'BiRefNet-DIS5K-TR_TEs','General-legacy':'BiRefNet-legacy'}
# resolution: General-Lite-2K -> (2560,1440); General-reso_512 -> (512,512); General-HR, Matting-HR -> (2048,2048); else (1024,1024)
half_precision = True
# load: AutoModelForImageSegmentation.from_pretrained('/'.join(('zhengpeng7', usage_to_weights_file[usage])), trust_remote_code=True); .to(device); .eval(); .half()
# call:
#   image = image_ori.convert('RGB'); image_proc = Resize(resolution)+ToTensor+Normalize(ImageNet)(image).unsqueeze(0)
#   preds = self.birefnet(image_proc.to(device).half())[-1].sigmoid().cpu(); pred = preds[0].squeeze()
#   pred_pil = transforms.ToPILImage()(pred)
#   image_masked = refine_foreground(image, pred_pil)
#   image_masked.putalpha(pred_pil.resize(image.size)); return image_masked
(Condensed copy of the handler: functions verbatim, class body paraphrased in comments.)
