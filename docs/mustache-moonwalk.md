# Mustache moonwalk

**Status (2026-11-07):** the iPhone handoff has been recovered from Google Drive. The first free Wan-Animate-2 transfer produced corrupted green/noisy frames and failed review. A second transfer using the newer modular pipeline is running. No video has passed review yet.

When Ricky says "ready for moonwalk" or "mustache moonwalk", this is the project. Do not ask him to explain it again. The earlier ChatGPT conversation is private, but the complete handoff is available locally in [START_HERE_CODEX.md](../assets/moonwalk/START_HERE_CODEX.md).

## Deliverable and character

Make one smooth, continuous 4–5 second MP4 of the shop mannequin doing an actual backward moonwalk, plus a seamless looping GIF from the video. Check the alternating heel lifts and backward sliding soles, full body including both platform shoes, consistent face, black mustache, black cap, blond wig, purple satin/orange-ruffled blouse and exact patterned white flares. A slideshow, static pose grid or optical-flow treatment of the old rejected GIF is not acceptable.

The three character references and original handoff are saved in `assets/moonwalk/`. The rejected choppy example remains in the original Drive ZIP and is not an input to generation.

- [Original handoff ZIP](https://drive.google.com/file/d/1UjY-oTTxzwx1YkAaVnI4lAr2vL3FESeJ/view)
- [Original ChatGPT conversation](https://chatgpt.com/c/6aef9ce4-9e2c-83ea-9b5c-7477d17fc2d1)

Ricky requested a free GitHub/Hugging Face route. No paid Runway subscription or GPU rental.

## Driving motion and credit

`assets/moonwalk/moonwalk_reference.webm` is RichKaz's **The Best Moonwalk Ever, The Best Michael Jackson performance**, dated 26 June 2011, downloaded from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:The_Best_Moonwalk_Ever,_The_Best_Michael_Jackson_performance.webm). Commons records the source as [RichKaz's video](https://www.youtube.com/watch?v=z-WALbJbLK4), licensed [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Attribution must travel with any derivative or shared motion reference.

`moonwalk-driver.mp4` is a silent 4.5-second derivative starting at 1.25 seconds, cropped to 480 × 480 at x=80, y=0, converted to 24 fps. Changes: trim, crop, transcode. The source already has no audio. Keep the credit above with the finished output.

## Verified free generation route

Checked on 2026-11-07:

- [hugging-apps/wan2-2-animate-2-14b](https://huggingface.co/spaces/hugging-apps/wan2-2-animate-2-14b) is running on ZeroGPU and exposes `/animate` for a reference image plus driving video. The first output failed visual review.
- [hugging-apps/wan2-2-animate](https://huggingface.co/spaces/hugging-apps/wan2-2-animate) uses the newer modular pipeline for the same distilled model. The second attempt uses this Space.
- The handoff's `neksjgg/wan22-animate-character-replace` runs a replacement workflow conditioned on the driver's background. It is less suitable for preserving the neon reference scene.
- The handoff's `techfreakworm/LTX2.3-Studio` accepted an image-to-video call, but returned **Generation failed**, with no output video. Do not count it as a successful generation.
- The first Wan-Animate-2 request (480 square, six steps, 4.5 seconds) failed with `The requested GPU duration (382s) is larger than the maximum allowed`.
- The next request (384 square, four distilled steps, 4.5 seconds, seed 42, guidance 1.0, shift 5.0) completed actual inference: 108 frames at 24 fps, but all sampled frames were corrupted green/noisy images, with no recognizable mannequin. Reject it.

Use `gradio_client.Client(..., token=...)` with the installed 2.7.2 client; `hf_token=` is not accepted. Reuse the locally configured Hugging Face token without printing or committing it. `ffmpeg` and `ffprobe` are installed. This PC has an RTX 4060 Ti with 16 GB VRAM, but no large local video model was installed for this task.

## Finish and verify

1. Inspect the returned video over time for real footwork, identity and outfit consistency, visible shoes, and continuous motion.
2. Preserve the model MP4 before editing. Make the shareable MP4 and a palette-optimized 480 px GIF from continuous frames. Check the loop seam; do not hide a failed moonwalk behind interpolation or a reverse-playback bounce.
3. Record accepted output filenames and any remaining limitations here. Deliver clickable MP4 and GIF links.

