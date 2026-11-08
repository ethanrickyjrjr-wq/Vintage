# Mustache moonwalk

**Status (2026-11-07):** a continuous-motion **draft** MP4 and GIF are saved in `assets/moonwalk/`, and the iPhone handoff is recovered. The newer modular pipeline preserved the neon room and recognizable outfit and transferred the footwork. The mustache is not reliably visible, the opening faces away, the hat sometimes touches the upper edge, and the loop seam jumps. These are reviewable drafts, not accepted final deliverables. Free ZeroGPU quota blocked the prepared refinement.

When Ricky says "ready for moonwalk" or "mustache moonwalk", this is the project. Do not ask him to explain it again. The earlier ChatGPT conversation is private, but the complete handoff is available locally in [START_HERE_CODEX.md](../assets/moonwalk/START_HERE_CODEX.md).

## Deliverable and character

Make one smooth, continuous 4–5 second MP4 of the shop mannequin doing an actual backward moonwalk, plus a seamless looping GIF from the video. Check the alternating heel lifts and backward sliding soles, full body including both platform shoes, consistent face, black mustache, black cap, blond wig, purple satin/orange-ruffled blouse and exact patterned white flares. A slideshow, static pose grid or optical-flow treatment of the old rejected GIF is not acceptable.

The three character references and original handoff are saved in `assets/moonwalk/`. The rejected choppy example remains in the original Drive ZIP and is not an input to generation.

- [Original handoff ZIP](https://drive.google.com/file/d/1UjY-oTTxzwx1YkAaVnI4lAr2vL3FESeJ/view)
- [Original ChatGPT conversation](https://chatgpt.com/c/6aef9ce4-9e2c-83ea-9b5c-7477d17fc2d1)

Ricky requested a free GitHub/Hugging Face route. No paid Runway subscription or GPU rental.

## Saved outputs and next run

- `assets/moonwalk/wan-animate-modular-raw.mp4`: untouched model output from `hugging-apps/wan2-2-animate`, seed 42, 384 square, four steps, 4.5 seconds.
- [mustache-moonwalk-draft.mp4](../assets/moonwalk/mustache-moonwalk-draft.mp4): the same video remuxed with source credit and a draft title. Verified 384 × 384, 24 fps, 108 decoded frames, 108 unique frame hashes, 4.500 seconds.
- [mustache-moonwalk-draft.gif](../assets/moonwalk/mustache-moonwalk-draft.gif): palette-optimized 480 × 480, 68 frames at approximately 15 fps, 4.54 seconds, infinite repeat, approximately 9.9 MB. Repeating is enabled, but the seam is not visually seamless.
- `assets/moonwalk/prompt.txt`: prepared refinement prompt emphasizing the large black mustache, face orientation, exact clothing and full-body framing.
- `assets/moonwalk/moonwalk-driver-side.mp4`: a second driving clip, source seconds 2.0–5.6 slowed by 1.25 to 4.5 seconds at 24 fps, same square crop. This removes the original driver's early back-facing turn. No optical-flow interpolation was used.

After free quota returns, from the repository root run:

```powershell
python tools/moonwalk/generate.py
```

The script uses the already configured Hugging Face login, requests 416 square / six distilled steps / seed 57, and writes a timestamped candidate MP4 and GIF with credits under `assets/moonwalk/candidates/`. It never purchases GPU time, substitutes a paid provider, or marks the candidate approved. The Gradio client and Hugging Face Hub packages are already available in the system Python. Review the result against the checklist below before calling it finished.

## Driving motion and credit

`assets/moonwalk/moonwalk_reference.webm` is RichKaz's **The Best Moonwalk Ever, The Best Michael Jackson performance**, dated 26 June 2011, downloaded from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:The_Best_Moonwalk_Ever,_The_Best_Michael_Jackson_performance.webm). Commons records the source as [RichKaz's video](https://www.youtube.com/watch?v=z-WALbJbLK4), licensed [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Attribution must travel with any derivative or shared motion reference.

`moonwalk-driver.mp4` is a silent 4.5-second derivative starting at 1.25 seconds, cropped to 480 × 480 at x=80, y=0, converted to 24 fps. Changes: trim, crop, transcode. The source already has no audio. Keep the credit above with the finished output.

## Verified free generation route

Checked on 2026-11-07:

- [hugging-apps/wan2-2-animate-2-14b](https://huggingface.co/spaces/hugging-apps/wan2-2-animate-2-14b) is running on ZeroGPU and exposes `/animate` for a reference image plus driving video. The first output failed visual review.
- [hugging-apps/wan2-2-animate](https://huggingface.co/spaces/hugging-apps/wan2-2-animate) uses the newer modular pipeline for the same distilled model. This produced the saved motion draft.
- The handoff's `neksjgg/wan22-animate-character-replace` runs a replacement workflow conditioned on the driver's background. It is less suitable for preserving the neon reference scene.
- The handoff's `techfreakworm/LTX2.3-Studio` accepted an image-to-video call, but returned **Generation failed**, with no output video. Do not count it as a successful generation.
- The first Wan-Animate-2 request (480 square, six steps, 4.5 seconds) failed with `The requested GPU duration (382s) is larger than the maximum allowed`.
- The next request (384 square, four distilled steps, 4.5 seconds, seed 42, guidance 1.0, shift 5.0) completed actual inference: 108 frames at 24 fps, but all sampled frames were corrupted green/noisy images, with no recognizable mannequin. Reject it.
- The newer modular pipeline completed at 384 square / four steps / seed 42 and produced the saved recognizable motion draft.
- The prepared modular refinement (416 square / six steps / seed 57, revised side-view driver and mustache prompt) was refused before inference: `You have exceeded your free ZeroGPU quota (188s requested vs. 15s left). Try again in 23:56:02.` This was reported at approximately 18:57 Eastern on November 7. No refinement output exists.

Use `gradio_client.Client(..., token=...)` with the installed 2.7.2 client; `hf_token=` is not accepted. Reuse the locally configured Hugging Face token without printing or committing it. `ffmpeg` and `ffprobe` are installed. This PC has an RTX 4060 Ti with 16 GB VRAM, but the LTX cache contains configuration files rather than usable model weights, and only about 6.3 GB system RAM was free during the local check. No large local video model or inference stack was installed for this task.

## Finish and verify

1. Inspect the returned video over time for real footwork, identity and outfit consistency, visible shoes, and continuous motion.
2. Preserve the model MP4 before editing. Make the shareable MP4 and a palette-optimized 480 px GIF from continuous frames. Check the loop seam; do not hide a failed moonwalk behind interpolation or a reverse-playback bounce.
3. Record accepted output filenames and any remaining limitations here. Deliver clickable MP4 and GIF links.

