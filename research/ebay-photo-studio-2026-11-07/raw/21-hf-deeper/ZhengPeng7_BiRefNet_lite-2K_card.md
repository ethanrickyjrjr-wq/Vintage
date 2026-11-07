hf://models/ZhengPeng7/BiRefNet_lite-2K/README.md (MCP_DATA 2026-11-07). Header trimmed.
Files: BiRefNet_config.py 298; README.md 5319; birefnet.py 92134; config.json 410; handler.py 4715; model.safetensors 177634392; requirements.txt 149. No .onnx.
license: mit
## This repo holds the official weights of BiRefNet_lite trained in 2K resolution.
### Training Sets: DIS5K (except DIS-VD); HRS10K; UHRSD; P3M-10k (except TE-P3M-500-NP); TR-humans; AM-2k; AIM-500; Human-2k; Distinctions-646; HIM2K; PPM-100
HR samples selection: size_h, size_w = 1440, 2560; ratio = 0.8; h >= size_h and w >= size_w or (h > size_h * ratio and w > size_w * ratio)
### Performance: DIS-VD | BiRefNet_lite-2K-general--epoch_232 | maxFm .867 wFmeasure .831 MAE .045 Smeasure .879 meanEm .919 HCE 952 ...
TE-P3M-500-NP | same | maxFm .993 wFmeasure .986 MAE .009 Smeasure .975 meanEm .986 HCE .000 ...
> Remember to set the resolution of input images to 2K (2560, 1440) for better results when using this model.
