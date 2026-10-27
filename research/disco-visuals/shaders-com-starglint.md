[![Shaders logo](https://shaders.com/_nuxt/logo.DnY6bMUs.svg)](https://shaders.com/)
[docs](https://shaders.com/docs/guide)[pro](https://shaders.com/pro)[community](https://discord.gg/Mfqmb2jCQT)
[](https://discord.gg/Mfqmb2jCQT "Discord")[5.5K](https://github.com/shader-effects-inc/shaders "GitHub")
sign in[Unlock Pro](https://shaders.com/pro)
Docs/Building with code/[Primitives](https://shaders.com/docs/primitives)/[Light](https://shaders.com/docs/primitives/light)/starGlintSearch the docs`⌘K`
#  starGlint
A four-point star of light: a round core with a thin ray along each axis, like a glint off glitter or a star in a photograph.

```
starGlint(offset: Expr, opts: {
    core: Expr | number
    rayLength: Expr | number
    rayWidth: Expr | number
    rays: Expr | number
    /** Optional: the glint fades to nothing by this distance from its centre (measured along the larger axis). */
    reach?: Expr | number
}): Expr

```

Import `light` from `shaders/std` and use `light.starGlint`.
`offset` is the pixel's position relative to the star's centre, as a `vec2`, in whatever unit you measure the star in (CSS pixels suit small glints). Returns the brightness: 1 at the centre, falling off along the rays and faster everywhere else. `core` is the core's sharpness (larger is a smaller dot). `rayLength` and `rayWidth` are falloff rates along and across each ray (smaller rayLength is a longer ray). `rays` is the rays' brightness relative to the core.
## [Parameters](https://shaders.com/docs/primitives/light/starglint#parameters)  
|  Name  |  Type  |  Notes  |  
| --- | --- | --- |  
|  `offset`  |  `Expr`  |   |  
|  `opts`  |  `{  |   |  

```
core: Expr \| number
rayLength: Expr \| number
rayWidth: Expr \| number
rays: Expr \| number
/** Optional: the glint fades to nothing by this distance from its centre (measured along the larger axis). */
reach?: Expr \| number

```

}` | |
## [Example](https://shaders.com/docs/primitives/light/starglint#example)

```
const glint = starGlint(offset, {core: 0.9, rayLength: 0.45, rayWidth: 1.6, rays: 0.25})

```

> **Tip.** Multiply by a `flashes` blink for a sparkle that comes and goes. Set `reach` to half the cell size when the glints sit on a `scatterPoints` grid, so long rays never hit a cell edge.
## [See also](https://shaders.com/docs/primitives/light/starglint#see-also)
  * [`glowSpot`](https://shaders.com/docs/primitives/light/glowspot) — A soft oval glow over an offset you have already scaled, the core of a bloom or a glare.
  * [`raySpikes`](https://shaders.com/docs/primitives/light/rayspikes) — Thin star spikes with dark gaps between them, like light through a camera aperture.
  * [`flareStarburst`](https://shaders.com/docs/primitives/light/flarestarburst) — The star of thin spikes around the light in a lens flare.


## [Used by](https://shaders.com/docs/primitives/light/starglint#used-by)
[Sparkle](https://shaders.com/docs/components/sparkle)
[ Previous dithered](https://shaders.com/docs/primitives/light/dithered)[ Next Materials & surfaces](https://shaders.com/docs/primitives/materials)
On this page
  * [Parameters](https://shaders.com/docs/primitives/light/starglint#parameters "Parameters")
  * [Example](https://shaders.com/docs/primitives/light/starglint#example "Example")
  * [See also](https://shaders.com/docs/primitives/light/starglint#see-also "See also")
  * [Used by](https://shaders.com/docs/primitives/light/starglint#used-by "Used by")


Actions
  * Copy as Markdown 
  * [Suggest changes ](https://github.com/shader-effects-inc/shaders/blob/main/packages/core/src/std/paint/light.ts#L537)


Open in
  * [ChatGPT](https://chatgpt.com/?q=Read%20this%20documentation%3A%20https%3A%2F%2Fshaders.com%2Fdocs%2Fprimitives%2Flight%2Fstarglint)
  * [Claude](https://claude.ai/new?q=Read%20this%20documentation%3A%20https%3A%2F%2Fshaders.com%2Fdocs%2Fprimitives%2Flight%2Fstarglint)
  * [Cursor](cursor://chat?message=Read%20this%20documentation%3A%20https%3A%2F%2Fshaders.com%2Fdocs%2Fprimitives%2Flight%2Fstarglint)
  * [Grok](https://x.com/i/grok?text=Read%20this%20documentation%3A%20https%3A%2F%2Fshaders.com%2Fdocs%2Fprimitives%2Flight%2Fstarglint)
  * [Perplexity](https://www.perplexity.ai/?q=Read%20this%20documentation%3A%20https%3A%2F%2Fshaders.com%2Fdocs%2Fprimitives%2Flight%2Fstarglint)
  * [![](https://shaders.com/docs/primitives/light/starglint)T3 Chat](https://t3.chat/new?q=Read%20this%20documentation%3A%20https%3A%2F%2Fshaders.com%2Fdocs%2Fprimitives%2Flight%2Fstarglint)


[![Shaders logo](https://shaders.com/_nuxt/logo.DnY6bMUs.svg)](https://shaders.com/)
### Product
  * [Home](https://shaders.com/)
  * [MCP](https://shaders.com/docs/guide/mcp)
  * [CLI](https://shaders.com/docs/guide/cli)
  * [Skill](https://shaders.com/docs/guide/agent-skill)
  * Support


### Frameworks
  * [React](https://shaders.com/react)
  * [Vue](https://shaders.com/vue)
  * [Svelte](https://shaders.com/svelte)
  * [Solid](https://shaders.com/solid)
  * [JavaScript](https://shaders.com/javascript)
  * [Framer](https://www.framer.com/marketplace/plugins/shaders/)


### Pro
  * [Shaders](https://shaders.com/pro#browse)
  * [Sections](https://shaders.com/pro#sections)
  * [Pricing](https://shaders.com/pro#pricing)


### Resources
  * [Documentation](https://shaders.com/docs/guide)
  * [Components](https://shaders.com/docs/components)
  * [System check](https://shaders.com/check)
  * [Changelog](https://github.com/shader-effects-inc/shaders/blob/main/CHANGELOG.md)
  * [Updates](https://shaders.com/updates)


### Legal
  * [Privacy](https://shaders.com/privacy)
  * [Terms](https://shaders.com/terms)
  * [License](https://shaders.com/license)


© 2026 Shader Effects Inc. All rights reserved. 
[X](https://x.com/npm_i_shaders)[Discord](https://discord.gg/Mfqmb2jCQT)[GitHub](https://github.com/shader-effects-inc/shaders)[YouTube](https://www.youtube.com/@npm_i_shaders)[npm](https://www.npmjs.com/package/shaders)
![](https://t.co/1/i/adsct?bci=4&dv=America%2FNew_York%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2628%2624%261080%26600%260%26na%261&eci=3&event=%7B%7D&event_id=9a4e3af5-0817-4f6b-b8bd-81b0a7fbed26&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e0407203-b240-48f2-bf71-f27aa7c0a83f&tw_ch_fvl=Not%2FA\)Brand%2F99.0.0.0%2CChromium%2F148.0.7778.96&tw_document_href=https%3A%2F%2Fshaders.com%2Fdocs%2Fprimitives%2Flight%2Fstarglint&tw_engaged_ms=1&tw_iframe_status=0&tw_pid_src=1&tw_session_count=1&tw_session_id=1793070682358-296183943&tw_session_start=1&twpid=tw.1793070682358.560246568340157111&txn_id=qjupy&type=javascript&version=2.4.12)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FNew_York%26en-US%26Google%20Inc.%26Win32%26255%261080%26600%2628%2624%261080%26600%260%26na%261&eci=3&event=%7B%7D&event_id=9a4e3af5-0817-4f6b-b8bd-81b0a7fbed26&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e0407203-b240-48f2-bf71-f27aa7c0a83f&tw_ch_fvl=Not%2FA\)Brand%2F99.0.0.0%2CChromium%2F148.0.7778.96&tw_document_href=https%3A%2F%2Fshaders.com%2Fdocs%2Fprimitives%2Flight%2Fstarglint&tw_engaged_ms=1&tw_iframe_status=0&tw_pid_src=1&tw_session_count=1&tw_session_id=1793070682358-296183943&tw_session_start=1&twpid=tw.1793070682358.560246568340157111&txn_id=qjupy&type=javascript&version=2.4.12)

