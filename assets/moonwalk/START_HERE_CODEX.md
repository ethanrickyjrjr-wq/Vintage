# Moonwalking mannequin — handoff for Codex

This project originated in a separate ChatGPT conversation on an iPhone. Codex does **not** inherit the prior conversation. This document and the images in this folder are the necessary context.

## User's exact goal

Create a **genuinely smooth, continuous-motion 4–5 second video** of a funny glamorous shop mannequin doing a convincing Michael Jackson-style **backward moonwalk**, plus a seamless, shareable animated **GIF** made from that video. Avoid a stuttering montage of still poses or crude optical-flow interpolation.

The mannequin needs to retain:

- The original pale mannequin face, short tousled blond wig, **large black fake mustache**, and black baseball cap with pink/aqua text from `mannequin_reference.jpeg`.
- The spectacular white high-waisted flared pants from `pants_reference.jpeg`, with detailed orange branching designs, purple flourishes, orange/dark side stripes, and gold waistband buttons.
- An equally extravagant purple satin disco shirt with bright orange ruffled collar and patterned sleeves, plus white platform shoes. `mannequin_full_body_start.png` is an existing composite showing the intended outfit and neon-purple disco-floor background.

The person is a **mannequin, not a real person**. The tone is absurd, campy, fashion-forward, and funny.

## What went wrong already

Prior attempts generated static pose grids and combined them into `old_choppy_example_DO_NOT_USE.gif`. The user rejected these because they look like a slideshow and *do not actually moonwalk*. Do not spend time making more six-frame slide-show GIFs.

## Best no-subscription workflow

1. Use `mannequin_full_body_start.png` as the character image in a free motion-transfer model, preferably **Wan 2.2 Animate**.
2. Find or obtain a clear 4–5 second full-body reference video of a person doing a recognizable moonwalk, preferably fixed camera and side/three-quarter profile. This is the **driving video**; its leg and heel motion is what the mannequin must follow. Prefer an original or permissively reusable clip, with audio removed.
3. Try this currently identified Hugging Face ZeroGPU Space: https://huggingface.co/spaces/neksjgg/wan22-animate-character-replace . It was shown as **Running on Zero** when checked on 2026-11-07, but availability and free quotas may change. Use the animation / motion-transfer workflow if available. If this particular Space only supports character replacement, check its UI and find an equivalent Wan 2.2 Animate demo that supports animation with a reference image and driving video.
4. The official code/research reference is https://github.com/Wan-Video/Wan2.2 — Wan-Animate takes a reference character image plus driving video and reproduces the driving motion. Running the full model locally can require substantial GPU memory; do **not** assume that a CPU laptop can do so.
5. As a less movement-specific fallback for image-to-video, check this ZeroGPU demo: https://huggingface.co/spaces/techfreakworm/LTX2.3-Studio . Its free queue may be slow, and prompt-only moonwalk accuracy may be less reliable than a motion-driving clip.
6. On a successful output, preserve the original MP4 and make a looping GIF with e.g. `ffmpeg`, resizing to about 480 px wide and choosing a suitable 10–15 fps palette-optimized GIF. The GIF should come from **actual continuous video frames**, not six generated stills.

Do not use a paid Runway subscription: the connected Runway workspace was identified as a Free plan with **no available video models**. The user specifically asked for a free GitHub or Hugging Face route.

## Exact motion directions for video model

> Static full-body 3/4 side view in a neon pink and purple disco studio. The same blond mannequin with an oversized fake black mustache and black baseball cap wears the *exact* white/orange/purple printed flared trousers, an elaborate shiny purple satin blouse with orange ruffles, and white platform shoes. She performs a fluid authentic backward moonwalk. Every cycle: the weight-bearing heel lifts high while the opposite planted flat foot visibly **slides backward** along the floor; then the feet switch weight and repeat. Her torso and head stay almost level and glide backward smoothly, with a small rhythmic shoulder and arm sway. Stable camera, physically plausible ankles and knees, natural foot-floor contact. No jumping, striding forward, kicking, morphing anatomy, added limbs, or outfit changes. One unbroken 5-second shot, designed to loop seamlessly.

## Validation / delivery

- Observe actual heel lifts and backward sliding, as opposed to simply standing or walking.
- Check that the hat, black mustache, shirt, pants pattern and face remain recognizable through the whole clip.
- Keep the full body visible including both shoes.
- Deliver a clickable downloadable MP4 and GIF to the user.
- If the free Space needs user login, queue time, or manual upload, give the user the smallest exact browser action needed. Never claim a video was generated when a queue failed.

The user is frustrated by context loss between ChatGPT and Codex, so **do not ask them to explain this project again**; everything necessary is in this handoff bundle.
