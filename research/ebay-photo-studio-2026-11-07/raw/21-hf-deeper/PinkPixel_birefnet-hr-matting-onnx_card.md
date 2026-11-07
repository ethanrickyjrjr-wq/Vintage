hf://models/PinkPixel/birefnet-hr-matting-onnx/README.md (MCP_DATA 2026-11-07). Created 7 Sep 2026 per hub search; 0 downloads, 0 likes. Third-party export, not the BiRefNet author's.
Files: LICENSE 1123 (MIT, "Copyright (c) 2024 Peng Zheng and BiRefNet Contributors / Copyright (c) 2026 Pink Pixel"); README.md 7251; infer.py 6864; model.onnx 932150975; model_fp16.onnx 471320622; model_int8.onnx 1055902055; model_q4.onnx 1035677760; model_uint8.onnx 1055076217; requirements.txt 48.
| Input Tensor | `image`: `[1, 3, 2048, 2048]` (Float32, ImageNet normalized RGB) |
| Output Tensor | `alpha`: `[1, 1, 2048, 2048]` (Float32, Sigmoid activated, range `[0.0, 1.0]`) |
| Supported Execution Providers | CPU, CUDA, DirectML, CoreML, WebGPU |
| Available Variants | FP32 (889 MB), FP16 (450 MB), INT8 (1007 MB), UINT8 (1007 MB), Q4 (988 MB) |
| `model_fp16.onnx` | Float16 | 450 MB | CUDA, WebGPU, Apple Silicon, DirectML | Recommended. Halves memory footprint and accelerates 2D convolutions with zero loss in alpha detail |
Quickstart: resized = img.resize((2048, 2048), Image.Resampling.BILINEAR); arr/255; (arr-mean)/std; tensor NCHW float32; session = ort.InferenceSession("model_fp16.onnx", providers=["CUDAExecutionProvider","CPUExecutionProvider"]); alpha_raw = session.run(["alpha"], {"image": tensor})[0]; alpha uint8 resized to original with BILINEAR; cutout.putalpha(alpha_mask); cutout.save("output.png")
infer.py CLI: python infer.py --image photo.jpg --provider cuda ; --dir ./in --output-dir ./out ; --mask-only ; --model default model.onnx next to script.
Benchmarks quoted in the card are copied from the upstream card (not re-measured).
NOT stated: whether the export includes deform_conv2d replacement; how the fp16 file accepts float32 input; any speed or VRAM figure.
