"""Run Wan-Animate-2 attention without compilation, with its KV cache on CPU.

The SDPA substitution follows the Apache-2.0 Hugging Face demo:
https://huggingface.co/spaces/hugging-apps/wan2-2-animate/blob/main/app.py
CPU cache placement preserves the reference tensors; it does not interpolate video.
"""

import torch
import torch.nn.functional as F
import torch.nn.attention.flex_attention as flex
import diffusers.models.attention_dispatch as dispatch
import diffusers.models.transformers.transformer_wan_animate_2 as wan


def configure():
    original_mask = flex.create_block_mask

    def eager_mask(*args, **kwargs):
        kwargs["_compile"] = False
        return original_mask(*args, **kwargs)

    wan.create_block_mask = eager_mask
    masks = {}

    def sdpa(query, key, value, attn_mask=None, is_causal=False, scale=None,
             enable_gqa=False, return_lse=False, _parallel_config=None):
        mask = attn_mask
        if isinstance(mask, flex.BlockMask):
            cache_key = (id(mask), query.shape[1], key.shape[1])
            if cache_key not in masks:
                zero = torch.zeros((), dtype=torch.long, device=query.device)
                cols = torch.arange(key.shape[1], device=query.device)[None, :]
                dense = torch.empty(query.shape[1], key.shape[1],
                                    dtype=torch.bool, device=query.device)
                for start in range(0, query.shape[1], 256):
                    rows = torch.arange(start, min(start + 256, query.shape[1]),
                                        device=query.device)[:, None]
                    dense[start:start + len(rows)] = mask.mask_mod(zero, zero, rows, cols)
                # Hold the mask too, so Python cannot reuse its id for another mask.
                masks.clear()
                masks[cache_key] = (mask, dense[None, None])
            mask = masks[cache_key][1]
        result = F.scaled_dot_product_attention(
            query.transpose(1, 2), key.transpose(1, 2), value.transpose(1, 2),
            attn_mask=mask, is_causal=is_causal, scale=scale, enable_gqa=enable_gqa,
        ).transpose(1, 2)
        return (result, None) if return_lse else result

    dispatch._AttentionBackendRegistry._backends[dispatch.AttentionBackendName.FLEX] = sdpa

    def store(cache, key, value):
        cache.device = key.device
        cache.key = key.to("cpu")
        cache.value = value.to("cpu")

    def get(cache):
        if cache.key is None:
            raise RuntimeError("Reference cache is empty")
        return cache.key.to(cache.device), cache.value.to(cache.device)

    wan.WanAnimate2KVLayerCache.store = store
    wan.WanAnimate2KVLayerCache.get = get
