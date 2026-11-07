hf://models/ZhengPeng7/BiRefNet-matting/README.md (MCP_DATA 2026-11-07). Header trimmed.
Files: BiRefNet_config.py 298; README.md 4724; birefnet.py 92134; config.json 413; handler.py 4707; model.safetensors 884878856 (lfs); requirements.txt 149. No .onnx.
license: mit
## This repo holds the official weights of BiRefNet for general matting.
### Training Sets: P3M-10k (except TE-P3M-500-NP); TR-humans; AM-2k; AIM-500; Human-2k (synthesized with BG-20k); Distinctions-646 (synthesized with BG-20k); HIM2K; PPM-100
### Validation Sets: TE-P3M-500-NP
### Performance: TE-P3M-500-NP | BiRefNet-matting--epoch_100 | Smeasure .979 maxFm .996 meanEm .988 MSE .003 maxEm .997 meanFm .986 wFmeasure .988 adpEm .864 adpFm .885 HCE .000 mBA .830 maxBIoU .940 meanBIoU .888
"Check the main BiRefNet model repo for more info and how to use it"; no input size stated (HR-matting card table lists it at 1024x1024 and 2048x2048).
