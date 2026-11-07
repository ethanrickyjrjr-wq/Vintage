hf://models/emrikol/birefnet-matting-onnx/README.md (MCP_DATA 2026-11-07). Created 30 Jun 2026, 0 downloads. Files: birefnet-matting.onnx 940840787; README.md 1802.
license: mit; base_model: ZhengPeng7/BiRefNet-matting. "This repo contains **only a format conversion** (PyTorch -> ONNX)".
"BiRefNet uses `torchvision::deform_conv2d` (deformable convolution), which neither the legacy nor the dynamo ONNX exporter supports. This export replaces that op with a mathematically equivalent implementation built from `grid_sample` (validated numerically against `torchvision.ops.deform_conv2d` to < 1e-3), so the model runs in ONNX Runtime / Core ML EP."
| Input | `input_image`, `float32`, shape `[1, 3, 1024, 1024]`, NCHW |
| Normalization | ImageNet |
| Output | `output_image`, `[1, 1, 1024, 1024]` **logits** - apply sigmoid for the alpha matte |
| Precision | fp32 (~897 MB) - opset 16 |
