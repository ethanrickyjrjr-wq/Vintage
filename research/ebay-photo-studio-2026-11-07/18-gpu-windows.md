# Lane 18: rembg on the Windows PC (RTX 4060 Ti), GPU recipe and CPU fallback

Status (2026-11-07): fetched, with two limits. Saved under raw/18-gpu-windows/: issue668.md (rendered thread), README.md (rembg main), cuda-ep.md (onnxruntime CUDA execution provider doc, raw from gh-pages), ort-python-readme.md (docs/python/README.rst, no GPU content, nothing useful), PyPI JSON for onnxruntime-gpu, onnxruntime, nvidia-cudnn-cu12, nvidia-cuda-runtime-cu12, nvidia-cublas-cu12, rembg, plus onnxruntime-gpu 1.26.0 metadata, and rembg source src-sessions_base.py.md, src-bg.py.md, src-init.md. Blocked or not done: onnxruntime.ai, NVIDIA driver docs (host blocked), the uv docs page (not needed, uv commands below are ordinary and not source-checked, see open questions). Nothing here was run on Windows: no GPU, no Windows. Every command is untested until Ricky's PC runs it.

## The short answer

Do not run bare `pip install "rembg[gpu]"`. Today it pulls the newest onnxruntime-gpu (1.31.1), and the onnxruntime doc says GPU wheels from 1.27 on are built for CUDA 13.0 by default. Pin onnxruntime-gpu 1.26.0, the last release built on CUDA 12.8 with cuDNN 9, and let pip install the CUDA and cuDNN DLLs as nvidia-*-cu12 wheels. Then call `onnxruntime.preload_dlls()` (rembg does not) or put the pip DLL folders on PATH. If the check does not print CUDAExecutionProvider and a timed run is still CPU speed, stay on CPU.

## Findings

1. Version pairing. VERIFIED_FETCHED, https://raw.githubusercontent.com/microsoft/onnxruntime/gh-pages/docs/execution-providers/CUDA-ExecutionProvider.md. Quote: "Starting with version 1.27, GPU packages published to PyPI (`onnxruntime-gpu`) and NuGet (`Microsoft.ML.OnnxRuntime.Gpu`) are built with **CUDA 13.0** by default. Separate CUDA 12.x GPU packages for these versions are built with **CUDA 12.8** and require CUDA 12.8 or newer. Older GPU package versions are built with **CUDA 12.8** by default." Table rows: "1.30.x-1.27.x | 12.8 | 9.x | CUDA 12.x GPU packages. Requires CUDA 12.8 or newer." and "1.26.x-1.21.x | 12.8 | 9.x | Available in PyPI and NuGet. Default GPU package build before 1.27." and "1.20.x | 12.x | 9.x". Rule quoted: "ONNX Runtime built with CUDA 12.8 require CUDA 12.8 or newer" and "ONNX Runtime built with cuDNN 8.x is not compatible with cuDNN 9.x, and vice versa." So: 1.21 to 1.26 is CUDA 12.8 plus cuDNN 9; 1.27 and later on PyPI is CUDA 13.0 plus cuDNN 9; the CUDA 12 builds of 1.27 and later are "separate" packages and the doc does not say where they are published (not found, open question 1).

2. PyPI state today. VERIFIED_FETCHED, https://pypi.org/pypi/onnxruntime-gpu/json (saved). Latest 1.31.1 uploaded 2026-10-26T19:11:04, requires_python >=3.11. Its `cuda` extra is `nvidia-cuda-nvrtc~=13.0`, `nvidia-cuda-runtime~=13.0`, `nvidia-cufft~=12.0`, `nvidia-curand~=10.0` and its `cudnn` extra is `nvidia-cudnn-cu13~=9.0`, which confirms 1.31.1 is the CUDA 13 build. Version 1.26.0 uploaded 2026-05-08T19:16:33 has file onnxruntime_gpu-1.26.0-cp312-cp312-win_amd64.whl; its extras are `nvidia-cuda-nvrtc-cu12~=12.0`, `nvidia-cuda-runtime-cu12~=12.0`, `nvidia-cufft-cu12~=11.0`, `nvidia-curand-cu12~=10.0` (extra `cuda`) and `nvidia-cudnn-cu12~=9.0` (extra `cudnn`). win_amd64 cp312 wheels exist for 1.25.1 through 1.31.1 (all listed). onnxruntime (CPU) 1.31.1 uploaded 2026-10-26T19:27:12, requires_python >=3.11, cp312 win_amd64 wheel exists, and so for 1.26.0 (2026-05-12).

3. rembg's pin is a floor, so it takes the CUDA 13 build. VERIFIED_FETCHED (https://pypi.org/pypi/rembg/json): rembg 2.0.87, uploaded 2026-11-06T01:19:57, requires_python `<4.0,>=3.11`; extra `gpu` = `onnxruntime-gpu<2.0.0,>=1.23.2; sys_platform != "darwin"`, extra `cpu` = `onnxruntime<2.0.0,>=1.23.2`. Nothing caps it below 1.27. A CUDA 13 build needs, per the doc, CUDA 13.0 or newer; whether Ricky's NVIDIA driver is new enough is unknown. Pinning 1.26.0 avoids the question except for the driver needing to support CUDA 12.8 (driver version number for that: not fetched, UNVERIFIED, nvidia-smi on his PC shows the supported CUDA version top right; it must say 12.8 or higher).

4. Do pip nvidia wheels replace a system CUDA install on Windows? Yes for onnxruntime, per the doc. VERIFIED_FETCHED quotes: "To reduce the need for manual installations of CUDA and cuDNN ... the `onnxruntime-gpu` Python package offers API to load CUDA and cuDNN dynamic link libraries (DLLs) appropriately." "Since version 1.21.0, the `onnxruntime-gpu` package provides the `preload_dlls` function to preload CUDA, cuDNN, and Microsoft Visual C++ (MSVC) runtime DLLs." Search order with `directory=None`: "1. On Windows, the `lib` directory under the PyTorch installation. 2. Python site-packages directories for NVIDIA CUDA or cuDNN libraries (e.g., `nvidia_cuda_runtime_cu12`, `nvidia_cudnn_cu12`)." Install line from the doc: "`pip install onnxruntime-gpu[cuda,cudnn]`" ("install the necessary CUDA and cuDNN runtime DLLs alongside the `onnxruntime-gpu` package using pip"). Debug form: `onnxruntime.preload_dlls(directory="")` "Preload DLLs from NVIDIA site packages and display debug information". Windows site-package path for cuDNN given in the doc: `..\\nvidia\\cudnn\\bin`. The nvidia-cudnn-cu12 9.28.1.4 and nvidia-cuda-runtime-cu12 12.9.79 both ship py3-none-win_amd64 wheels (VERIFIED_FETCHED PyPI JSON), so the DLLs do exist for Windows. The system still needs the NVIDIA display driver (that is not a pip package).

5. Catch: rembg does not call preload_dlls. VERIFIED_FETCHED rembg/sessions/base.py, bg.py and __init__.py on main: no `preload_dlls` in any of the three (grep on the saved files; other files in the repo were not searched, so the claim is "not in the session and entry code I fetched"). Without a preload, Windows may not find DLLs sitting in site-packages\nvidia\...\bin. Whether onnxruntime 1.26 finds them by itself at session creation: not stated in the doc, UNVERIFIED. So the recipe below does the preload explicitly (a tiny wrapper script) and gives a PATH fallback.

6. cublas is a transitive dependency. VERIFIED_FETCHED: nvidia-cudnn-cu12 9.28.1.4 `requires_dist` is `['nvidia-cublas-cu12']`, so installing the `cudnn` extra brings cuBLAS (the missing file in issue 668 was `libcublasLt.so.12`). Watch: the newest nvidia-cublas-cu12, 12.9.3.13, has only Linux wheels on PyPI; 12.9.2.10 and earlier have win_amd64. pip and uv should pick 12.9.2.10 on Windows (inference, UNVERIFIED). If the resolver errors, add `"nvidia-cublas-cu12<12.9.3"`.

7. How rembg picks the provider. VERIFIED_FETCHED rembg/sessions/base.py: if no `providers` list is passed, it checks `ort.get_device() == "GPU"` and `"CUDAExecutionProvider" in ort.get_available_providers()`, then uses `["CUDAExecutionProvider", "CPUExecutionProvider"]`; else ROCm; else OpenVINO if listed; else `["CPUExecutionProvider"]`. New in this version: after creating the session it compares what was asked with `inner_session.get_providers()` and emits a RuntimeWarning: "CUDAExecutionProvider was requested but the session is running on CPU. onnxruntime could not load the provider, usually because the matching CUDA/cuDNN runtime libraries are missing or are a different major version than the onnxruntime-gpu build." The source docstring says `get_available_providers()` lists CUDA "whenever its shim ships with onnxruntime, even if the CUDA/cuDNN libraries it links against are absent", so the providers list alone does not prove the GPU works. This is also why issue 668 users found it silently on CPU: that thread predates the warning (the 2025 reports).

8. Expected output of the check. In the issue 668 thread (Linux Docker, onnxruntime-gpu with CUDA) the list printed was `['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']` (VERIFIED_FETCHED, quoted from the thread), even though TensorRT was not installed; TensorRT then logged load errors and ORT fell back: "Falling back to ['CUDAExecutionProvider', 'CPUExecutionProvider'] and retrying." On Windows with the pip wheel the exact list is UNVERIFIED; expect CUDAExecutionProvider and CPUExecutionProvider, probably TensorrtExecutionProvider too. Only a list with no CUDAExecutionProvider (just `['AzureExecutionProvider', 'CPUExecutionProvider']` or `['CPUExecutionProvider']`) means the wrong package is installed (CPU onnxruntime shadowing, or no onnxruntime-gpu). The real test is the second check below, which creates a session and prints `get_providers()`.

9. Do not chase TensorRT. Issue 668 quotes: a commenter calls TensorRT unobtainable without "a complex nvidia developer sign up" (paraphrase of their complaint), and the advice "if you don't really need it, just use `new_session("{model_name}",providers=['CUDAExecutionProvider'])` ... it won't even try to load TensorRT". The TensorRT errors in the log are noise when the CUDA provider then loads. For the CLI there is no flag to pass providers (the `i` and `p` flags in 01-rembg.md have none), so use the Python wrapper below, which passes `providers=["CUDAExecutionProvider","CPUExecutionProvider"]`.

10. Python version. VERIFIED_FETCHED: rembg 2.0.87 PyPI `requires_python <4.0,>=3.11`; rembg README: "This library depends on onnxruntime. Python version support is determined by onnxruntime's compatibility." (01-rembg.md also quotes a README line `>=3.11, <3.14`; not re-checked here). onnxruntime-gpu 1.26.0 has cp311, cp312, cp313 and cp314 Windows wheels (VERIFIED_FETCHED). Python 3.12 is inside every range and has the wheel: use it.

11. Model pre-download. VERIFIED_FETCHED in lane 01 (d_command.py): `rembg d <model names>`, e.g. `rembg d birefnet-general birefnet-general-lite`. README says models are saved under `~/.rembg/models/`; set REMBG_HOME for a known folder (lane 01 finding 13). birefnet-general is a 928 MB file, lite is 214 MB (lane 01 asset list).

12. Timing. CPU: MEASURED_HERE, about 18 to 23 s per photo at 1024 model input on a 4-core cloud box (figure given by the orchestrator; I did not rerun it, and rembg was not run in this lane). Ricky's i7-14700KF has far more cores, so expect faster, number unknown. GPU, ANECDOTE only, issue 668 (one user, Linux Docker, single image, `time rembg i -m birefnet-general realesrgan2x.png ...`, includes model load): "real 0m11.130s" with forced CUDA, "real 0m29.869s" without ("user 1m9.945s"), and 10.730 s on a second CUDA run. That GPU is not named in what I read and the gain was only about 2.7x including load, so on a 4060 Ti expect single digit seconds for the first image and less for later ones in a batch (UNVERIFIED guess; the model loads once per command). README: birefnet-general-fp16 is "roughly 30% faster on CUDA with near-identical masks" and needs `rembg[fp16]`; try it only after the plain GPU path works. Honest read: at the batch sizes of a small resale shop CPU would be acceptable, so GPU is a nice-to-have, not a blocker.

## Copy-paste block (Windows PowerShell, from the project folder)

```powershell
# 0. Check the driver first. Top right of the nvidia-smi table must show CUDA Version 12.8 or higher.
nvidia-smi

# 1. uv and the venv (Python 3.12)
uv venv .venv/cutout --python 3.12
.\.venv\cutout\Scripts\Activate.ps1

# 2. GPU install: rembg 2.0.87 with the CUDA 12.8 build of onnxruntime-gpu and pip-supplied CUDA 12 and cuDNN 9 DLLs
uv pip install "rembg[gpu,cli]==2.0.87" "onnxruntime-gpu[cuda,cudnn]==1.26.0"
# if the resolver complains about nvidia-cublas-cu12, add: "nvidia-cublas-cu12<12.9.3"

# 3. Check 1: which providers does the package list?
python -c "import onnxruntime as ort; ort.preload_dlls(directory=''); print(ort.__version__); print(ort.get_available_providers())"
#   expect: 1.26.0 and a list that contains 'CUDAExecutionProvider' (the thread showed
#   ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider'] on Linux).
#   preload_dlls(directory='') prints which DLLs it loaded from site-packages\nvidia. Read that output.

# 4. Download the models once (the default bria-rmbg is banned for commercial use, never download it)
$env:REMBG_HOME = "$PWD\models\rembg"
rembg d birefnet-general birefnet-general-lite

# 5. Check 2 (the real test): build a session and print what it actually got, with timing
@'
import time, onnxruntime as ort
ort.preload_dlls(directory="")
from rembg import new_session, remove
from PIL import Image
import sys
s = new_session("birefnet-general", providers=["CUDAExecutionProvider", "CPUExecutionProvider"])
print("session providers:", s.inner_session.get_providers())
img = Image.open(sys.argv[1])
for i in range(2):
    t = time.time(); remove(img, session=s); print(f"run {i+1}: {time.time()-t:.1f} s")
'@ | Set-Content gpucheck.py
python gpucheck.py .\example.jpg
#   good: session providers starts with 'CUDAExecutionProvider' and run 2 is a few seconds or less.
#   bad: ['CPUExecutionProvider'] only, or a RuntimeWarning "was requested but the session is running on CPU".
```

If check 2 fails to load the CUDA provider, try the PATH route once (the doc names the cuDNN folder `nvidia\cudnn\bin`; the other folder names are UNVERIFIED, so list them with Get-ChildItem):

```powershell
$sp = python -c "import site; print(site.getsitepackages()[-1])"
Get-ChildItem "$sp\nvidia" -Directory | ForEach-Object { $_.FullName + "\bin" }
$env:PATH = (Get-ChildItem "$sp\nvidia" -Directory | ForEach-Object { "$($_.FullName)\bin" }) -join ";" + ";" + $env:PATH
python gpucheck.py .\example.jpg
```

## CPU fallback (also the safe default for first tests)

```powershell
deactivate
uv venv .venv/cutout-cpu --python 3.12
.\.venv\cutout-cpu\Scripts\Activate.ps1
uv pip install "rembg[cpu,cli]==2.0.87"
$env:REMBG_HOME = "$PWD\models\rembg"
rembg d birefnet-general birefnet-general-lite
rembg p -m birefnet-general -dc INBOX OUTBOX
```

Never put onnxruntime and onnxruntime-gpu in one venv (known foot-gun; UNVERIFIED from memory, so use two separate venvs as above). Expect on the order of 18 to 23 s per photo on a 4-core machine (MEASURED_HERE); the 14700KF should do better, to be measured. If CUDAExecutionProvider is missing or the session says CPU after the PATH attempt, stay on CPU. Do not install TensorRT, do not build onnxruntime, do not install a system CUDA toolkit; rembg's own README says: "If `rembg[gpu]` doesn't work and you can't install CUDA or `cudnn-devel`, use `rembg[cpu]` with `onnxruntime` instead."

## Recommendations

1. Pin onnxruntime-gpu 1.26.0 with extras `[cuda,cudnn]` (CUDA 12.8, cuDNN 9), rembg 2.0.87, Python 3.12. Do not let rembg[gpu] float to 1.27 and later on a PC whose driver may not support CUDA 13.
2. Always verify with check 2, not the providers list alone: the rembg source itself says the list is not proof.
3. Time-box the GPU attempt: one pass through the block, one PATH retry, then CPU. Batch with `rembg p` or one Python session so the model loads once.
4. Fix the handoff: add the pin and the preload step, and replace "confirm the arguments" for `rembg d` with `rembg d birefnet-general birefnet-general-lite`.

## Open questions

1. Where are the CUDA 12 builds of onnxruntime-gpu 1.27 and later published? The doc says "Separate CUDA 12.x GPU packages ... require CUDA 12.8 or newer" but the install location was not fetched (onnxruntime.ai blocked). Not needed if 1.26.0 is pinned.
2. What NVIDIA driver version does CUDA 12.8 need on Windows, and what does Ricky's PC have? Run nvidia-smi.
3. Does onnxruntime 1.26 on Windows find the site-packages DLLs without preload_dlls or PATH? The doc is silent; the block works around it.
4. Does the pip resolver skip nvidia-cublas-cu12 12.9.3.13 (no Windows wheel) cleanly? Inference only.
5. Real GPU seconds per image for birefnet-general on the 4060 Ti, and CPU seconds on the 14700KF: need his PC. Also whether the `uv venv` / `uv pip install` syntax is exactly right on his uv version (not source-checked this run).
6. Are the nvidia\cublas\bin and nvidia\cuda_runtime\bin folder names right on Windows? Only nvidia\cudnn\bin is in the doc.
