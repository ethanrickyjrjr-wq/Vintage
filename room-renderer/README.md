---
title: Holliewood and Vine Room Preview
emoji: 🛋️
colorFrom: yellow
colorTo: red
sdk: gradio
sdk_version: 6.30.0
app_file: app.py
python_version: "3.12"
short_description: Private room styling renderer for Holliewood and Vine
license: apache-2.0
startup_duration_timeout: 1h
---

Private image-editing backend for the Holliewood and Vine storefront. Runs the
Apache-2.0 **black-forest-labs/FLUX.2-klein-4B** model on free ZeroGPU hardware.
The storefront authenticates server-side. No visitor needs a Hugging Face login.
Room photos and results pass as JSON in memory; this app does not write them to
files, galleries, datasets, or logs. GPU availability and daily quotas still apply.

The original Spark demo is retained at revision
`6054219a10550a6d0f90cfc26d6181fe3ab87e55`, with its archived branch recorded in
the project handoff. Keep this Space private.

Model: https://huggingface.co/black-forest-labs/FLUX.2-klein-4B

API endpoint: `/render_room`. Inputs and output are JSON; use the storefront's
validated server handler rather than exposing its Hugging Face token to visitors.
