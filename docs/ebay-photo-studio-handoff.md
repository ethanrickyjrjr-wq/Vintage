# eBay photo studio: the card for the PC

**Status (2026-11-07):** written in the cloud session that researched and built this; nothing here has run on the Windows PC yet. The script ran here on CPU (Linux, 4 cores) on Ricky's four example photos. Every command below is for Windows PowerShell from the repo folder (`C:\Users\ethan\dev\Vintage`). Decisions and the reasons are in `docs/ebay-photo-studio.md`; the research is in `research/ebay-photo-studio-2026-11-07/`. Expect the first session to take about an hour including the model download.

## The simplest route: cut on the phone, frame on the PC

Ricky's call, 2026-11-07: the tap on the phone cuts better than any of this, so use it. The PC only does what the phone cannot: pure white, the square, 1600 px, the file names and the manifest.

1. On the iPhone, cut the item out. Either press and hold the item in Photos until it glows, lift a finger, choose Copy Subject (or Share, then Save to Files), or select several photos, Share, Save to Files, then in Files select them, Quick Actions, Remove Background. Each gives a PNG with a transparent background. (Menu names from third-party guides, not yet checked on your phone; the gesture is the one you already use.)
2. Get the PNGs to the PC: the Drive or iCloud folder the PC syncs. Point the script at that folder.
3. Run the script on the folder (section 3). A transparent PNG is recognised on sight: the model is not loaded, and the photo is only trimmed, centred on pure white, saved at 1600 and 2048, and logged as "cut on the phone, framed here". About one second per photo. Name the PNGs `ITEM-view` as usual if you can; `Background Removed` in the name is fine.
4. Labels and flaw close-ups still go in as plain photos: they are kept as shot.

The model route below is for a stack of photos where tapping each one would take longer. Both can mix in one folder.

## 0. Before you sit down

- Ten or so photos to try on, including the ones already in `assets/examples-2026-11-07/` (the navy dress, its label, the framed print).
- A folder where the phone drops photos (iCloud Photos folder, AirDrop target, or a USB copy). Name it, for example `C:\Users\ethan\Pictures\inbox`.
- Nothing to buy for this part. The shopping list is section 5.

## 1. Install (once, about 15 minutes plus a 1 GB download)

Done on this PC 2026-11-07: `.venv\cutout` is the GPU venv and `.venv\cutout-cpu` the CPU one, both installed and checked; the steps below are for a rebuild. The GPU route is first because, measured here on the same four photos, the RTX 4060 Ti takes 7 to 8 seconds a photo where the 14700KF takes 21 to 35. `nvidia-smi` here reports CUDA 13.4, so the current `onnxruntime-gpu` is used as is: the ONNX Runtime CUDA provider page (read 2026-11-07) says PyPI GPU packages from 1.27 on are built with CUDA 13.0 and need a 13.0 or newer driver, and pip supplies the CUDA 13 and cuDNN 9 DLLs through the `[cuda,cudnn]` extras; no NVIDIA toolkit install. Only on a driver below CUDA 13.0 pin `onnxruntime-gpu[cuda,cudnn]==1.26.0`, the last CUDA 12.8 build, which pulls the `-cu12` DLL set instead.

```powershell
# 0. Driver check. Top right of the table must say CUDA Version 12.8 or higher.
nvidia-smi

# 1. A fresh venv on Python 3.12 (never reuse crawl4ai-venv)
cd C:\Users\ethan\dev\Vintage
uv venv .venv\cutout --python 3.12
.\.venv\cutout\Scripts\Activate.ps1

# 2. rembg with onnxruntime-gpu 1.31.1 (CUDA 13.0 build) and the pip-supplied CUDA 13 and cuDNN 9 DLLs, plus the script's helpers. About 5 minutes of downloads here.
uv pip install "rembg[gpu,cli]==2.0.87" "onnxruntime-gpu[cuda,cudnn]==1.31.1" "pillow-heif==1.8.1" opencv-python-headless scipy
# driver below CUDA 13.0 only: ==1.26.0 instead (it pulls the -cu12 DLL set)

# 3. Check 1: does the package see the GPU?
python -c "import onnxruntime as ort; ort.preload_dlls(directory=''); print(ort.__version__); print(ort.get_available_providers())"
#    good (seen here 2026-11-07): 1.31.1 and ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
#    bad:  only CPUExecutionProvider (or AzureExecutionProvider and CPU): wrong package, go to the CPU route

# 4. The model, once (about 1 GB). Never download bria-rmbg: non-commercial licence.
#    Already on this PC in C:\Users\ethan\.rembg\models\birefnet-general (rembg's default folder, REMBG_HOME unset): skip.
rembg d birefnet-general

# 5. Check 2, the real test: a session that says which provider it got, with timing
python tools\cutout\cutout.py assets\examples-2026-11-07 $env:TEMP\cutout-check
#    first line should read: model birefnet-general on CUDAExecutionProvider
#    a WARNING line saying the session runs on CPU means the DLLs were not found: try section 1b once, then the CPU route
```

The models live in `C:\Users\ethan\.rembg\models` (rembg's default; `REMBG_HOME` is unset here). Set `REMBG_HOME` only to move them; the repo's `models/` folder is gitignored for that case.

**1b. If check 2 says CPU: one PATH attempt, then stop chasing it.**

```powershell
$sp = python -c "import site; print(site.getsitepackages()[-1])"
Get-ChildItem "$sp\nvidia" -Directory | ForEach-Object { $_.FullName + "\bin" }
$env:PATH = ((Get-ChildItem "$sp\nvidia" -Directory | ForEach-Object { "$($_.FullName)\bin" }) -join ";") + ";" + $env:PATH
python tools\cutout\cutout.py assets\examples-2026-11-07 $env:TEMP\cutout-check --force
```

**1c. CPU route (also fine; the 14700KF will beat this cloud box's 20 seconds a photo).** Use a second venv so the CPU and GPU onnxruntime never share one.

```powershell
deactivate
uv venv .venv\cutout-cpu --python 3.12
.\.venv\cutout-cpu\Scripts\Activate.ps1
uv pip install "rembg[cpu,cli]==2.0.87" "pillow-heif==1.8.1" opencv-python-headless scipy
rembg d birefnet-general birefnet-general-lite
python tools\cutout\cutout.py assets\examples-2026-11-07 $env:TEMP\cutout-check
```

Do not install TensorRT, a CUDA toolkit or cuDNN by hand, and do not build anything. rembg's own README: "If `rembg[gpu]` doesn't work and you can't install CUDA or `cudnn-devel`, use `rembg[cpu]` with `onnxruntime` instead."

## 2. First run: what good looks like

If the folder holds only phone cut-outs and close-ups, the run takes seconds and prints no model line at all. The lines below are for the model route.

The check in step 5 writes `%TEMP%\cutout-check\ebay`, `listing`, `site` and `manifest.csv`. Report lines from this PC on the GPU, 2026-11-07 (the cloud box printed the same percentages at 18 to 22 seconds a photo):

```
model birefnet-general on CUDAExecutionProvider
nm-dress-back.jpg: 7.4s  pixels kept 99.9%  solid 98%  item small in frame, shoot closer
nm-dress-front.jpg: 7.1s  pixels kept 99.9%  solid 98%  item small in frame, shoot closer
nm-dress-label.jpg: 0.0s  kept as shot (close-up), resized only
shisa-print.jpg: 8.3s  pixels kept 100.0%  solid 91%  item small in frame, shoot closer     (plain cut; see the note below)
```

Open `ebay\nm-dress-front.jpg`: the dress on pure white with the hanger, nothing else. Open `ebay\shisa-print.jpg`: the frame will show a notch at the top, because this test file is not named with a rectangle word. Rename it `A9-framed-print.jpg` (or run the folder with `--rect`) and run again with `--force`: the whole black frame, no notch and no scar along the top edge even at full zoom, and the report line says `rect repair filled 3.1%`. Add `--check` to get `check\A9-framed-print.jpg`, the cut on green with the patched gaps in magenta. `--straighten` and `--reframe` exist but are not the plan. Measured here: 7 to 8 seconds a photo on the GPU for a 12 MP phone photo, 6.5 seconds to load the model, 47 seconds for the four-photo folder. The CPU venv on the same folder: 21 to 35 seconds a photo, 80 seconds in all. The masks are identical on both routes.

## 3. The daily flow

1. Shoot per the shot list in `docs/ebay-photo-studio.md` section 5, and name the files `ITEM-view`: `B12-front.heic`, `B12-back.heic`, `B12-room.heic`, `B12-label.heic`, `B12-fabric.heic`, `B12-flaw1.heic`, `B12-measure.heic`. The view word decides the treatment: `front`, `back`, `side` and anything unlisted are cut out onto white; `label`, `tag`, `flaw`, `detail`, `close`, `inside`, `measure`, `fabric`, `hem`, `button`, `zipper` are kept exactly as shot; `frame`, `framed`, `art`, `mirror`, `painting`, `poster`, `box`, `book`, `sign`, `tray`, `record`, `album` get the rectangle repair (not `print` or `canvas`: a print dress and a canvas tote are clothes). The in-room shot (`room`) will be cut too, so give the unedited original to Etsy from the phone, or name it `B12-room-detail.heic` to keep it as shot.
2. Start the watcher before shooting, in the venv window:
   ```powershell
   python tools\cutout\cutout.py C:\Users\ethan\Pictures\inbox C:\Users\ethan\Pictures\inbox\cutouts --watch
   ```
   It processes what is already there, then each new photo two seconds after it stops growing. Stop with Ctrl+C or by creating `stop.txt` in the inbox.
3. Upload `cutouts\ebay\*.jpg` to eBay (1600 square, under 12 MB, no text or marks). The crosslister carries them on. `listing\` is the 2048 master for Shopify; `site\*.png` is for our storefront only and never goes to a marketplace.
4. Read `manifest.csv` or the console: `PIXELS CHANGED` means check that photo by eye; `mostly see-through` means glass, list the original sweep shot; `item small in frame` means reshoot closer; `no item found` means reshoot on the white sweep.
5. Framed art: run its folder with `--reframe` when the frame is undamaged; the frame comes out as a clean rectangle built from its own bar, and the mat and picture stay as shot. Reflections in the glass are in the photo, so shoot framed pieces with the window light from the side and black boards just outside the frame.
6. Objects that stand on a surface (lamps, shoes, hats, bags) can take a soft contact shadow: run their folder with `--shadow`. Hanging or framed things can take `--shadow drop`. Clothes on the form: no shadow.

## 4. Options

| Flag | What it does |
|---|---|
| `--watch` | keep running, process new photos as they land, `stop.txt` ends it |
| `--shadow` or `--shadow drop` | contact shadow under standing objects, or a faint drop shadow behind hanging ones; never on the PNG |
| `--rect` | rectangle repair on every photo in the folder (frames, mirrors, boxes), otherwise by file name |
| `--straighten` | with the rectangle repair, square up a frame shot at an angle (four corners to a true rectangle); compare with the plain output, proportions are estimated |
| `--check` | frames: also write `check\NAME.jpg`, the cut on green with the filled gaps in magenta, to see what was patched |
| `--reframe` | framed art with an undamaged frame: rebuild the frame from its own bar around the untouched mat and picture, mitred corners, straightened first. Never for a chipped or worn frame |
| `--model birefnet-general-lite` | the 224 MB model, for a laptop or a quick preview; `birefnet-general` is the default |
| `--force` | redo photos that already have outputs |

Lace, fringe, feathers and fur: the general model is the starting point; if edges disappoint, lane 21 (`research/ebay-photo-studio-2026-11-07/21-hf-deeper.md`) has the BiRefNet HR-matting route at 2048 px for the GPU. That is a later step, not part of the daily flow.

## 5. Shopping list

Prices are asking prices seen in search results on 2026-11-07; the pages themselves could not be opened from the cloud session, so check live before ordering (`fetch-later.md` has every URL).

**Form and pinning**

- One adjustable, pinnable dress form with an adjustable pole, sized at or under the smallest size Hollie sells, padded up with batting for larger sizes. Dritz My Double about $155; Roxy linen forms $136 to $188; used Acme adjustable $50 to $250 on Marketplace and estate sales.
- The cream linen vintage-look form as the room piece that also appears in photos: Mannequin Mall French forms $183 to $305, Etsy linen forms from $125, antique linen on a spindle base $375.
- Pinning kit, under $60 total: binder clips, spring clamps, dressmaker pins, tissue, transparent tape, quilt batting, a black cloth for sheers.

**Light and backdrop, cheapest tier that works (about $165 to $230)**

- Two Neewer 24-inch softbox kits with stands, $80 to $120.
- A 10 by 7 foot backdrop stand with clamps, $30 to $46.
- Savage 53-inch pure white seamless paper roll, about $45 (check whether coats and the feather hat need the 107-inch roll).
- A phone tripod with a Bluetooth remote, $7 to $20.
- Same bulbs in every light, 5500 to 5700 K, CRI 90 or better. Add a third light on the backdrop only if the white reads grey.

Already on hand per the earlier docs: foam boards, a lazy Susan, a steamer, hangers, a rack, tape, a lint roller.

## 6. Fetch the pages the cloud could not

The cloud session's network blocked eBay, Reddit, YouTube, Hugging Face's website, Amazon and the vendor sites, so every price above and several seller claims are snippet-level. From Git Bash on the PC, one loop fetches all 153 pages with crawl4ai into `research/ebay-photo-studio-2026-11-07/raw/fetched-on-pc/`:

```bash
grep -oE "^- https?://[^ ]+" research/ebay-photo-studio-2026-11-07/fetch-later.md | cut -c3- | while read -r u; do tools/crawl.sh "$u" "research/ebay-photo-studio-2026-11-07/raw/fetched-on-pc/$(echo "$u" | sed -E 's#https?://##; s#[^A-Za-z0-9.]+#_#g' | cut -c1-80).md"; done
```

Then ask Claude to re-run the verification against the fetched pages and update `docs/ebay-photo-studio.md`. Reddit may still wall the Windows box; the Fedora container is the fallback (`old.reddit.com` URLs with a `.json` suffix).

## 7. Questions to answer while you are there

- Which forms are on hand, and does any have a removable neck or arms?
- iPhone model and iOS version; HEIC or JPEG capture.
- Room depth: can the form stand five or six feet from the backdrop?

## 8. If something goes wrong

- `No module named cv2` or `scipy`: the venv is missing the helpers; rerun the install line in section 1.
- `bria-rmbg weights are licensed for non-commercial use only`: the script refusing `--model bria-rmbg`, as intended.
- A photo fails with a memory error on CPU: the script already turns off onnxruntime's CPU memory arena (with it on, the second photo in a run was killed here at a 16 GB limit; off, three photos ran flat at about 8 GB). If it still happens, close other programs or run with `--model birefnet-general-lite`. The GPU route uses far less system memory.
- HEIC files skipped or unreadable: `pillow-heif` missing; rerun the install line.
- Edges with a thin coloured halo: already handled by rembg's decontamination; if it persists on one photo, shoot that item against a backdrop of the opposite tone (eBay's clothing page: dark clothes on light, light clothes on dark).
- A notch or missing piece on a frame or box: the file name needs a rectangle word (`frame`, `box`, `mirror`), or run the folder with `--rect`.
