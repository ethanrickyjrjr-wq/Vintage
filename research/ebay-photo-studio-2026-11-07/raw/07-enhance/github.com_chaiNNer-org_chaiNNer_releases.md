<!-- source: https://github.com/chaiNNer-org/chaiNNer/releases, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                           Releases · chaiNNer-org/chaiNNer · GitHub                                                         

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FchaiNNer-org%2FchaiNNer%2Freleases)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FchaiNNer-org%2FchaiNNer%2Freleases)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Freleases%2Findex&source=header-repo&source_repo=chaiNNer-org%2FchaiNNer)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

                  

## Repository navigation

[](/chaiNNer-org/chaiNNer)

# Releases

 

Releases · chaiNNer-org/chaiNNer

## Alpha v0.26.1

[Alpha v0.26.1](/chaiNNer-org/chaiNNer/releases/tag/v0.26.1) [Latest](/chaiNNer-org/chaiNNer/releases/latest)

[Latest](/chaiNNer-org/chaiNNer/releases/latest)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 27 Oct 19:17

[v0.26.1](/chaiNNer-org/chaiNNer/tree/v0.26.1)

[`4c4ca34`](/chaiNNer-org/chaiNNer/commit/4c4ca34ae8a2297a29218e6ff25f3570757d3a97)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.

GPG key ID: B5690EEEBB952194

Verified

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).

## Bug Fixes

-   Fixed the window going blank when using the light theme. ([#3352](https://github.com/chaiNNer-org/chaiNNer/issues/3352), [#3353](https://github.com/chaiNNer-org/chaiNNer/pull/3353))
-   Fixed the window not appearing on Linux Wayland desktops, such as KDE Plasma on Nobara and CachyOS. ([#3348](https://github.com/chaiNNer-org/chaiNNer/issues/3348), [#3351](https://github.com/chaiNNer-org/chaiNNer/pull/3351))
-   Fixed an "UNKNOWN: unknown error, watch" error dialog on Windows. File watch errors are now logged instead. ([#3357](https://github.com/chaiNNer-org/chaiNNer/issues/3357), [#3358](https://github.com/chaiNNer-org/chaiNNer/pull/3358))

**Full Changelog**: [v0.26.0...v0.26.1](https://github.com/chaiNNer-org/chaiNNer/compare/v0.26.0...v0.26.1)

Assets 8

Loading

### Uh oh!

There was an error while loading. Please reload this page.

3 people reacted

## Alpha v0.26.0

[Alpha v0.26.0](/chaiNNer-org/chaiNNer/releases/tag/v0.26.0)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 18 Oct 21:45

[v0.26.0](/chaiNNer-org/chaiNNer/tree/v0.26.0)

[`ad1ccb0`](/chaiNNer-org/chaiNNer/commit/ad1ccb0bd97b05ecd8ed174a4fce7ae222b2bca3)

This is a long overdue release. I had implemented a bunch of things earlier this year and then subsequently forgot to release them after they had been tested out by people, so this update is releasing all that to stable.

Part of why I hadn't released these changes is because I have been privately working on a Rust rewrite of chaiNNer's backend. I've been working on and off on that since around March. I will discuss that more soon, so stay tuned for updates and announcements on that. If you don't know what that entails, basically that just means everything will be significantly faster, and some things (like dependency management) a bit less jank.

This is the last release (minus any patches for necessary bug fixes) with the Python backend. It is also the last release that will be marked Alpha, and going forward I will use true semantic versioning starting from v27.0.0.

# Major Changes

-   TensorRT upscaling and engine conversion, with BF16 support. Requires an RTX 20xx / GTX 16xx GPU or newer. ([#3247](https://github.com/chaiNNer-org/chaiNNer/pull/3247), [#3265](https://github.com/chaiNNer-org/chaiNNer/pull/3265), [#3254](https://github.com/chaiNNer-org/chaiNNer/pull/3254), [#3255](https://github.com/chaiNNer-org/chaiNNer/pull/3255))
-   Language switching: the interface is now available in English, German, Spanish, French, Hindi, Italian, Japanese, Korean, Dutch, Polish, Portuguese (Brazil), Russian, Turkish and Chinese (Simplified). Change it in Settings → Appearance ([#3171](https://github.com/chaiNNer-org/chaiNNer/pull/3171), [#3180](https://github.com/chaiNNer-org/chaiNNer/pull/3180), [#3341](https://github.com/chaiNNer-org/chaiNNer/pull/3341))
    -   Node names, descriptions and inputs, the app menu, some dialogs and messages, and type descriptions are still in English
    -   The translations are machine-made and machine-reviewed. Corrections from native speakers are welcome.

# New nodes and node features

-   New _Math Expression_ node: write a formula with variable inputs ([#3187](https://github.com/chaiNNer-org/chaiNNer/pull/3187), [#3191](https://github.com/chaiNNer-org/chaiNNer/pull/3191))
-   New _Is Grayscale_ node: checks whether an image is grayscale ([#3222](https://github.com/chaiNNer-org/chaiNNer/pull/3222))
-   _Regex Find_ has a new "Found" output, so a chain no longer fails when nothing matches ([#3140](https://github.com/chaiNNer-org/chaiNNer/pull/3140))
-   Channel nodes are renamed to consistent "Split" and "Combine" names ([#3135](https://github.com/chaiNNer-org/chaiNNer/pull/3135))

# Minor Changes

-   Upscale nodes show their own progress bar while processing tiles, for PyTorch, ONNX, NCNN and TensorRT ([#3252](https://github.com/chaiNNer-org/chaiNNer/pull/3252))
-   Lower CPU usage from progress updates during long runs ([#3250](https://github.com/chaiNNer-org/chaiNNer/pull/3250))
-   PyTorch auto split takes the model's size requirements into account ([#3167](https://github.com/chaiNNer-org/chaiNNer/pull/3167))
-   Installation progress shows on the taskbar ([#3169](https://github.com/chaiNNer-org/chaiNNer/pull/3169))
-   Installing no longer hangs silently when the disk runs out of space ([#3131](https://github.com/chaiNNer-org/chaiNNer/pull/3131))
-   Python 3.8 and 3.9 are no longer supported, because both have reached end of life. If you use your own system Python, it must be 3.10 or newer ([#3207](https://github.com/chaiNNer-org/chaiNNer/pull/3207))
-   The backend now writes independent log files, which helps with bug reports. If submitting a bug, please send all three log files: main.log, host.log and worker.log ([#3137](https://github.com/chaiNNer-org/chaiNNer/pull/3137))
-   Updated dependencies

# Bug Fixes

-   Fixed VRAM usage growing every time the PyTorch inpaint node ran ([#3194](https://github.com/chaiNNer-org/chaiNNer/pull/3194))
-   Fixed cached node results never being freed ([#3199](https://github.com/chaiNNer-org/chaiNNer/pull/3199))

**Full Changelog**: [v0.26.0...v0.26.0](https://github.com/chaiNNer-org/chaiNNer/compare/v0.26.0...v0.26.0)

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

8 people reacted

## Alpha v0.25.1

[Alpha v0.25.1](/chaiNNer-org/chaiNNer/releases/tag/v0.25.1)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 23 Oct 00:07

[v0.25.1](/chaiNNer-org/chaiNNer/tree/v0.25.1)

[`2f340e1`](/chaiNNer-org/chaiNNer/commit/2f340e1e8b5fc1951eab1ecec5e9c35482aa6294)

This is a small update to address a few issues that have been resolved since the last release. If the current version of chaiNNer is working fine for you, you can ignore this update.

If you have an older (1000 series or lower) Nvidia GPU, please reinstall PyTorch from the dependency manager.

## What's Changed

-   Fix GTX 1000 series GPU compatibility with PyTorch ([#3161](https://github.com/chaiNNer-org/chaiNNer/pull/3161))
-   Fix conditional input validation bug causing NOT logic operation to require hidden input B ([#3154](https://github.com/chaiNNer-org/chaiNNer/pull/3154))
-   Fix audio not saving in save video node ([#3174](https://github.com/chaiNNer-org/chaiNNer/pull/3174))
-   Fix dependency resolution to prevent using global Python site-packages ([#3134](https://github.com/chaiNNer-org/chaiNNer/pull/3134))
-   Fix TensorRT engine cache persistence across application restarts ([#3139](https://github.com/chaiNNer-org/chaiNNer/pull/3139))
-   Fix grammar and capitalization in Python setup error messages ([#3133](https://github.com/chaiNNer-org/chaiNNer/pull/3133))
-   Hide "install all packages button", due to its functionality being broken ([#3179](https://github.com/chaiNNer-org/chaiNNer/pull/3179))

NOTE: I had to disable code signing for MacOS due to it causing build issues. I do not know how exactly that will manifest when trying to install this update, but just a heads up that you might get some kind of warning now that you did not used to.

**Full Changelog**: [v0.25.0...v0.25.1](https://github.com/chaiNNer-org/chaiNNer/compare/v0.25.0...v0.25.1)

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

16 people reacted

## Alpha v0.25.0

[Alpha v0.25.0](/chaiNNer-org/chaiNNer/releases/tag/v0.25.0)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 19 Oct 22:07

[v0.25.0](/chaiNNer-org/chaiNNer/tree/v0.25.0)

[`99c49e8`](/chaiNNer-org/chaiNNer/commit/99c49e84965c14f6cfd16aefae3feba64910ceaf)

After more than a year without a stable release, chaiNNer development has resumed at reduced capacity. This release brings the features from the nightly version to stable (with many of the reported bugs from the nightly version fixed).

The main new feature is support for using multiple iterators of equal length together. Nested or combined iteration is still not supported. UX for this feature remains limited but stable based on user feedback.

Users with RTX 5000-series GPUs should install this update and update PyTorch through the dependency manager.

# Changelog:

## Major Changes:

-   Add support for combined iterator lineage by [@joeyballentine](https://github.com/joeyballentine) and [@RunDevelopment](https://github.com/RunDevelopment) in [#2949](https://github.com/chaiNNer-org/chaiNNer/pull/2949), [#2960](https://github.com/chaiNNer-org/chaiNNer/pull/2960), [#2973](https://github.com/chaiNNer-org/chaiNNer/pull/2973), [#2975](https://github.com/chaiNNer-org/chaiNNer/pull/2975), [#2971](https://github.com/chaiNNer-org/chaiNNer/pull/2971), [#3141](https://github.com/chaiNNer-org/chaiNNer/pull/3141)
    -   This allows mixing and matching of same-length iterators.
-   Allow more nodes to be "starting nodes" by [@joeyballentine](https://github.com/joeyballentine) in [#2944](https://github.com/chaiNNer-org/chaiNNer/pull/2944)
    -   This allows the ability to pass a path into Load Image, for example
-   Update Torch & Torchvision to support RTX 50 series by [@LlamaEnjoyer](https://github.com/LlamaEnjoyer) in [#3103](https://github.com/chaiNNer-org/chaiNNer/pull/3103)

## Minor Changes:

-   Add padding input to PyTorch Upscale node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2966](https://github.com/chaiNNer-org/chaiNNer/pull/2966)
-   Add support for 3 TIFF compression modes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2970](https://github.com/chaiNNer-org/chaiNNer/pull/2970)
-   Add ONNX size requirements and more robust shape detection by [@RunDevelopment](https://github.com/RunDevelopment) in [#2978](https://github.com/chaiNNer-org/chaiNNer/pull/2978), [#2979](https://github.com/chaiNNer-org/chaiNNer/pull/2979)
-   Add support for new SR architectures as supported by Spandrel version 0.4.1 by the-database in [#3038](https://github.com/chaiNNer-org/chaiNNer/pull/3038), [#3082](https://github.com/chaiNNer-org/chaiNNer/pull/3082)
-   Add support for subtle noise generation in "Add Noise" node by [@Arcitec](https://github.com/Arcitec) in [#3055](https://github.com/chaiNNer-org/chaiNNer/pull/3055)
-   Updates to "Align Image to Reference" node by [@pifroggi](https://github.com/pifroggi) in [#3091](https://github.com/chaiNNer-org/chaiNNer/pull/3091)
-   Rename "Model Scale" node to "Get Model Info" node by [@tumuyan](https://github.com/tumuyan) in [#3090](https://github.com/chaiNNer-org/chaiNNer/pull/3090)

## New Nodes:

-   Add "Balance Normals" node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2964](https://github.com/chaiNNer-org/chaiNNer/pull/2964)
-   Add "Logic Operation" node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2990](https://github.com/chaiNNer-org/chaiNNer/pull/2990)

## Bug Fixes:

-   Fix undo history containing select state by [@joeyballentine](https://github.com/joeyballentine) in [#2961](https://github.com/chaiNNer-org/chaiNNer/pull/2961)
-   Fix label for != in Compare node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2991](https://github.com/chaiNNer-org/chaiNNer/pull/2991)
-   Clarify "Load Model" SafeTensors documentation by [@JeremyRand](https://github.com/JeremyRand) in [#3028](https://github.com/chaiNNer-org/chaiNNer/pull/3028)
-   (A1111/SD) Fix SwinIR 4X being referenced with wrong name by [@PereViader](https://github.com/PereViader) in [#2998](https://github.com/chaiNNer-org/chaiNNer/pull/2998)
-   Fix "Install All Packages" hanging indefinitely in Dependency Manager by @copilot in [#3127](https://github.com/chaiNNer-org/chaiNNer/pull/3127)

## Known Issues:

-   "Logic Operation" currently has an issue with the NOT operation that is being looked into
-   DML support for ONNX was added by [@FNsi](https://github.com/FNsi) but is currently broken

## New Contributors

-   [@PereViader](https://github.com/PereViader) made their first contribution in [#2998](https://github.com/chaiNNer-org/chaiNNer/pull/2998)
-   [@FNsi](https://github.com/FNsi) made their first contribution in [#3072](https://github.com/chaiNNer-org/chaiNNer/pull/3072)
-   [@Arcitec](https://github.com/Arcitec) made their first contribution in [#3055](https://github.com/chaiNNer-org/chaiNNer/pull/3055)
-   [@styler00dollar](https://github.com/styler00dollar) made their first contribution in [#3067](https://github.com/chaiNNer-org/chaiNNer/pull/3067)
-   [@tumuyan](https://github.com/tumuyan) made their first contribution in [#3090](https://github.com/chaiNNer-org/chaiNNer/pull/3090)
-   [@LlamaEnjoyer](https://github.com/LlamaEnjoyer) made their first contribution in [#3103](https://github.com/chaiNNer-org/chaiNNer/pull/3103)
-   [@oumad](https://github.com/oumad) made their first contribution in [#3069](https://github.com/chaiNNer-org/chaiNNer/pull/3069)

**Full Changelog**: [v0.24.1...v0.25.0](https://github.com/chaiNNer-org/chaiNNer/compare/v0.24.1...v0.25.0)

### Contributors

-   [![@JeremyRand](https://avatars.githubusercontent.com/u/244188?s=64&v=4)](https://github.com/JeremyRand)
-   [![@pifroggi](https://avatars.githubusercontent.com/u/1202907?s=64&v=4)](https://github.com/pifroggi)
-   [![@tumuyan](https://avatars.githubusercontent.com/u/3126801?s=64&v=4)](https://github.com/tumuyan)
-   [![@oumad](https://avatars.githubusercontent.com/u/17836943?s=64&v=4)](https://github.com/oumad)
-   [![@RunDevelopment](https://avatars.githubusercontent.com/u/20878432?s=64&v=4)](https://github.com/RunDevelopment)
-   [![@PereViader](https://avatars.githubusercontent.com/u/32639021?s=64&v=4)](https://github.com/PereViader)
-   [![@joeyballentine](https://avatars.githubusercontent.com/u/34788790?s=64&v=4)](https://github.com/joeyballentine)
-   [![@Arcitec](https://avatars.githubusercontent.com/u/38923130?s=64&v=4)](https://github.com/Arcitec)
-   [![@styler00dollar](https://avatars.githubusercontent.com/u/51405565?s=64&v=4)](https://github.com/styler00dollar)
-   [![@LlamaEnjoyer](https://avatars.githubusercontent.com/u/108919017?s=64&v=4)](https://github.com/LlamaEnjoyer)
-   [![@FNsi](https://avatars.githubusercontent.com/u/125447286?s=64&v=4)](https://github.com/FNsi)

JeremyRand, pifroggi, and 9 other contributors

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

5 people reacted

## Alpha v0.24.1

[Alpha v0.24.1](/chaiNNer-org/chaiNNer/releases/tag/v0.24.1)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 07 Jun 21:36

[v0.24.1](/chaiNNer-org/chaiNNer/tree/v0.24.1)

[`76e230d`](/chaiNNer-org/chaiNNer/commit/76e230d7abdc1688d520e2c7a23cf1bfc72d0464)

This update contains a few bug fixes and some QOL improvements.

## What's Changed

-   Add UI for anchor/position dropdowns by [@RunDevelopment](https://github.com/RunDevelopment) in [#2940](https://github.com/chaiNNer-org/chaiNNer/pull/2940)
-   Add "Install All" button to dependency manager by [@RunDevelopment](https://github.com/RunDevelopment) in [#2931](https://github.com/chaiNNer-org/chaiNNer/pull/2931)
-   Make node widths slightly more consistent when dealing with handles by [@RunDevelopment](https://github.com/RunDevelopment) in [#2938](https://github.com/chaiNNer-org/chaiNNer/pull/2938)
-   (PyTorch) Add a setting for clearing CUDA cache after each inference by [@joeyballentine](https://github.com/joeyballentine) in [#2930](https://github.com/chaiNNer-org/chaiNNer/pull/2930)
-   (PyTorch) Never auto update PyTorch to allow custom versions to remain installed by [@joeyballentine](https://github.com/joeyballentine) in [#2943](https://github.com/chaiNNer-org/chaiNNer/pull/2943)

## Bug Fixes

-   (PyTorch) Fix incorrect tile size estimations after upscaling optimizations by [@joeyballentine](https://github.com/joeyballentine) in [#2929](https://github.com/chaiNNer-org/chaiNNer/pull/2929)
-   Fix output types for the Resolutions node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2937](https://github.com/chaiNNer-org/chaiNNer/pull/2937)

**Full Changelog**: [v0.24.0...v0.24.1](https://github.com/chaiNNer-org/chaiNNer/compare/v0.24.0...v0.24.1)

### Contributors

-   [![@RunDevelopment](https://avatars.githubusercontent.com/u/20878432?s=64&v=4)](https://github.com/RunDevelopment)
-   [![@joeyballentine](https://avatars.githubusercontent.com/u/34788790?s=64&v=4)](https://github.com/joeyballentine)

RunDevelopment and joeyballentine

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

18 people reacted

## Alpha v0.24.0

[Alpha v0.24.0](/chaiNNer-org/chaiNNer/releases/tag/v0.24.0)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 01 Jun 19:50

[v0.24.0](/chaiNNer-org/chaiNNer/tree/v0.24.0)

[`171cc66`](/chaiNNer-org/chaiNNer/commit/171cc66a93f507e85d69745813e5bb5b3265293d)

This update brings many new major features to chaiNNer, including but not limited to conditional branching (via two new nodes: Conditional and Compare), node passthrough/skipping, new themes, PyTorch optimizations, and many more fixes and quality of life improvements all around.

The conditional and compare nodes bring a long-awaited feature: branching support. Well, mostly. These nodes allow you to switch between inputs based on a condition created by comparing two values in various ways. This means users can finally set up chains that do one thing under a certain condition and another thing under a different one (e.g. if an image is over a certain size vs under a certain size). The thing to keep in mind is how you have to set this up might be opposite of what's intuitive. Since you're switching between values, it's what comes _before_ the condition that is decided between, not what comes after.

The disable toggle has also been replaced with a button that allows you to swap between three states: "enabled", "disabled", and "skipped". In skipped mode, the node will not be run, but it also will not disable downstream nodes like disabling it would. This is another heavily-requested feature that we are happy is finally in chaiNNer.

New themes can be selected in settings. This is semi-experimental as we plan on adding support for fully custom themes in the future, as well as improving the existing default selection. The current selection is mainly just a proof of concept to show that we _can_ support themes of some kind, and also to give users some options for customization. We'd love to hear feedback on the current selection and if you have any suggestions on themes to add.

PyTorch upscaling has been heavily optimized. I was able to using a visual profiling tool (called VizTracer, which I highly recommend for anyone wanting to optimize a python project) to see what was slowing down upscaling. Upscaling has been optimized to a point where it's roughly 1.25x faster than it was before (though YMMV depending on what model you use, as well as other factors). While not perfect, it's still a large improvement and should help your PyTorch upscaling chains run faster.

## Major Changes

-   Support passthrough/skipping nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2805](https://github.com/chaiNNer-org/chaiNNer/pull/2805), [#2864](https://github.com/chaiNNer-org/chaiNNer/pull/2864), [#2887](https://github.com/chaiNNer-org/chaiNNer/pull/2887)
-   Add new themes by [@joeyballentine](https://github.com/joeyballentine) in [#2833](https://github.com/chaiNNer-org/chaiNNer/pull/2833), [#2847](https://github.com/chaiNNer-org/chaiNNer/pull/2847), [#2874](https://github.com/chaiNNer-org/chaiNNer/pull/2874), [#2921](https://github.com/chaiNNer-org/chaiNNer/pull/2921)
-   Various optimizations to PyTorch upscaling by [@joeyballentine](https://github.com/joeyballentine) in [#2853](https://github.com/chaiNNer-org/chaiNNer/pull/2853), [#2852](https://github.com/chaiNNer-org/chaiNNer/pull/2852), [#2861](https://github.com/chaiNNer-org/chaiNNer/pull/2861), [#2859](https://github.com/chaiNNer-org/chaiNNer/pull/2859), [#2858](https://github.com/chaiNNer-org/chaiNNer/pull/2858), [#2860](https://github.com/chaiNNer-org/chaiNNer/pull/2860), [#2862](https://github.com/chaiNNer-org/chaiNNer/pull/2862), [#2869](https://github.com/chaiNNer-org/chaiNNer/pull/2869), [#2884](https://github.com/chaiNNer-org/chaiNNer/pull/2884), [#2886](https://github.com/chaiNNer-org/chaiNNer/pull/2886)

## Minor Changes

-   Add avif support by [@the-database](https://github.com/the-database) in [#2820](https://github.com/chaiNNer-org/chaiNNer/pull/2820)
-   Add convolve usage example by [@BigBoyBarney](https://github.com/BigBoyBarney) in [#2827](https://github.com/chaiNNer-org/chaiNNer/pull/2827)
-   (PyTorch) Add custom tiling option by [@the-database](https://github.com/the-database) in [#2828](https://github.com/chaiNNer-org/chaiNNer/pull/2828), [#2870](https://github.com/chaiNNer-org/chaiNNer/pull/2870), [#2880](https://github.com/chaiNNer-org/chaiNNer/pull/2880)
-   (PyTorch) Update spandrel (adds support for PLKSR, RealPLKSR, IPT, SAFMN\_BCIE, DRCT) by [@RunDevelopment](https://github.com/RunDevelopment) in [#2837](https://github.com/chaiNNer-org/chaiNNer/pull/2837), [#2846](https://github.com/chaiNNer-org/chaiNNer/pull/2846)
-   Default chain file saving to documents folder by [@joeyballentine](https://github.com/joeyballentine) in [#2836](https://github.com/chaiNNer-org/chaiNNer/pull/2836)
-   Rename parameters of numeric inputs and clean up parameters by [@RunDevelopment](https://github.com/RunDevelopment) in [#2863](https://github.com/chaiNNer-org/chaiNNer/pull/2863)
-   Increase font size for type tags by [@RunDevelopment](https://github.com/RunDevelopment) in [#2865](https://github.com/chaiNNer-org/chaiNNer/pull/2865)
-   Make all Switch inputs optional by [@RunDevelopment](https://github.com/RunDevelopment) in [#2867](https://github.com/chaiNNer-org/chaiNNer/pull/2867)
-   Slightly redesign the Math node by [@RunDevelopment](https://github.com/RunDevelopment), [@joeyballentine](https://github.com/joeyballentine) in [#2868](https://github.com/chaiNNer-org/chaiNNer/pull/2868), [#2873](https://github.com/chaiNNer-org/chaiNNer/pull/2873)
-   Better type errors for text nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2871](https://github.com/chaiNNer-org/chaiNNer/pull/2871)
-   Add "order" dropdown for both spritesheet nodes by [@joeyballentine](https://github.com/joeyballentine) in [#2878](https://github.com/chaiNNer-org/chaiNNer/pull/2878)
-   Improve style of multiline text area by [@RunDevelopment](https://github.com/RunDevelopment) in [#2885](https://github.com/chaiNNer-org/chaiNNer/pull/2885)
-   Add a "simple" mode for saving video by [@joeyballentine](https://github.com/joeyballentine) in [#2879](https://github.com/chaiNNer-org/chaiNNer/pull/2879)
-   Slightly more space for text in dropdowns by [@RunDevelopment](https://github.com/RunDevelopment) in [#2892](https://github.com/chaiNNer-org/chaiNNer/pull/2892)
-   Slightly more compact Save Video node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2893](https://github.com/chaiNNer-org/chaiNNer/pull/2893)
-   Optimize away Passthrough nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2896](https://github.com/chaiNNer-org/chaiNNer/pull/2896)
-   Add type color for Booleans by [@joeyballentine](https://github.com/joeyballentine) in [#2891](https://github.com/chaiNNer-org/chaiNNer/pull/2891)
-   Add type color for Colors by [@joeyballentine](https://github.com/joeyballentine) in [#2898](https://github.com/chaiNNer-org/chaiNNer/pull/2898), [#2904](https://github.com/chaiNNer-org/chaiNNer/pull/2904)
-   Stricter condition for type assignability by [@RunDevelopment](https://github.com/RunDevelopment) in [#2902](https://github.com/chaiNNer-org/chaiNNer/pull/2902)
-   Select best-matching node based on search query by [@RunDevelopment](https://github.com/RunDevelopment) in [#2903](https://github.com/chaiNNer-org/chaiNNer/pull/2903)
-   Support connected handles with multiple colors by [@RunDevelopment](https://github.com/RunDevelopment) in [#2906](https://github.com/chaiNNer-org/chaiNNer/pull/2906)
-   Better type error message for division by zero by [@RunDevelopment](https://github.com/RunDevelopment) in [#2907](https://github.com/chaiNNer-org/chaiNNer/pull/2907)
-   Fix assignability for outputs with errors by [@RunDevelopment](https://github.com/RunDevelopment) in [#2909](https://github.com/chaiNNer-org/chaiNNer/pull/2909)
-   Add special suggestion for Math and Compare nodes in node selector by [@RunDevelopment](https://github.com/RunDevelopment) in [#2908](https://github.com/chaiNNer-org/chaiNNer/pull/2908)
-   Mention node names in error messages by [@RunDevelopment](https://github.com/RunDevelopment) in [#2920](https://github.com/chaiNNer-org/chaiNNer/pull/2920)
-   Add similarity check to ONNX model conversions by [@RunDevelopment](https://github.com/RunDevelopment) in [#2915](https://github.com/chaiNNer-org/chaiNNer/pull/2915)
-   Add support for ONNX type and tag broadcasting by [@RunDevelopment](https://github.com/RunDevelopment) in [#2919](https://github.com/chaiNNer-org/chaiNNer/pull/2919)
-   Improve types for model conversion nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2925](https://github.com/chaiNNer-org/chaiNNer/pull/2925)

## New Nodes

-   Add "Compare" & "Conditional" nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2866](https://github.com/chaiNNer-org/chaiNNer/pull/2866), [#2895](https://github.com/chaiNNer-org/chaiNNer/pull/2895)
-   Add "Image Align with Rife" and "Wavelet Color Fix" Nodes by [@pifroggi](https://github.com/pifroggi), [@RunDevelopment](https://github.com/RunDevelopment) in [#2714](https://github.com/chaiNNer-org/chaiNNer/pull/2714), [#2888](https://github.com/chaiNNer-org/chaiNNer/pull/2888), [#2889](https://github.com/chaiNNer-org/chaiNNer/pull/2889)
-   Add "Regex Find" node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2855](https://github.com/chaiNNer-org/chaiNNer/pull/2855)
-   Add "Separate Color" node by [@joeyballentine](https://github.com/joeyballentine), @RunDevelopmentg in [#2897](https://github.com/chaiNNer-org/chaiNNer/pull/2897), [#2910](https://github.com/chaiNNer-org/chaiNNer/pull/2910)

## Bug Fixes

-   Fixed input gathering for collectors by [@RunDevelopment](https://github.com/RunDevelopment) in [#2818](https://github.com/chaiNNer-org/chaiNNer/pull/2818)
-   Use `atexit` to always kill worker by [@RunDevelopment](https://github.com/RunDevelopment) in [#2822](https://github.com/chaiNNer-org/chaiNNer/pull/2822)
-   Rework GPU API to fix issues with older GPUs by [@RunDevelopment](https://github.com/RunDevelopment) in [#2821](https://github.com/chaiNNer-org/chaiNNer/pull/2821)
-   Avoid RGB contamination by transparent pixels in "Color Transfer" node by [@Splendide-Imaginarius](https://github.com/Splendide-Imaginarius) in [#2389](https://github.com/chaiNNer-org/chaiNNer/pull/2389)
-   Prevent chain files from being saved in install directory by [@joeyballentine](https://github.com/joeyballentine) in [#2835](https://github.com/chaiNNer-org/chaiNNer/pull/2835)
-   Fix that empty string was not allowed as the default value by [@RunDevelopment](https://github.com/RunDevelopment) in [#2856](https://github.com/chaiNNer-org/chaiNNer/pull/2856)
-   Fix converting indexed PIL images to NumPy by [@RunDevelopment](https://github.com/RunDevelopment) in [#2881](https://github.com/chaiNNer-org/chaiNNer/pull/2881)
-   Fix node documentation modal opening on reload by [@joeyballentine](https://github.com/joeyballentine) in [#2883](https://github.com/chaiNNer-org/chaiNNer/pull/2883)
-   Fix timing issue for lazy inputs by [@RunDevelopment](https://github.com/RunDevelopment) in [#2890](https://github.com/chaiNNer-org/chaiNNer/pull/2890)
-   Prevent log spam by not logging useless stack traces by [@RunDevelopment](https://github.com/RunDevelopment) in [#2900](https://github.com/chaiNNer-org/chaiNNer/pull/2900)\\
-   Fix image pairs length validation when using limit by [@joeyballentine](https://github.com/joeyballentine) in [#2917](https://github.com/chaiNNer-org/chaiNNer/pull/2917)
-   (ONNX) Fix size requirement padding by [@RunDevelopment](https://github.com/RunDevelopment) in [#2918](https://github.com/chaiNNer-org/chaiNNer/pull/2918)
-   Add status API to get executor status to prevent stale/stuck status by [@RunDevelopment](https://github.com/RunDevelopment) in [#2928](https://github.com/chaiNNer-org/chaiNNer/pull/2928)

## New Contributors

-   [@the-database](https://github.com/the-database) made their first contribution in [#2820](https://github.com/chaiNNer-org/chaiNNer/pull/2820)
-   [@pifroggi](https://github.com/pifroggi) made their first contribution in [#2714](https://github.com/chaiNNer-org/chaiNNer/pull/2714)

**Full Changelog**: [v0.23.2...v0.24.0](https://github.com/chaiNNer-org/chaiNNer/compare/v0.23.2...v0.24.0)

### Contributors

-   [![@pifroggi](https://avatars.githubusercontent.com/u/1202907?s=64&v=4)](https://github.com/pifroggi)
-   [![@RunDevelopment](https://avatars.githubusercontent.com/u/20878432?s=64&v=4)](https://github.com/RunDevelopment)
-   [![@the-database](https://avatars.githubusercontent.com/u/25811902?s=64&v=4)](https://github.com/the-database)
-   [![@joeyballentine](https://avatars.githubusercontent.com/u/34788790?s=64&v=4)](https://github.com/joeyballentine)
-   [![@BigBoyBarney](https://avatars.githubusercontent.com/u/86712892?s=64&v=4)](https://github.com/BigBoyBarney)
-   [![@Splendide-Imaginarius](https://avatars.githubusercontent.com/u/119545140?s=64&v=4)](https://github.com/Splendide-Imaginarius)

pifroggi, RunDevelopment, and 4 other contributors

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

8 people reacted

## Alpha v0.23.3

[Alpha v0.23.3](/chaiNNer-org/chaiNNer/releases/tag/v0.23.3)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 24 Apr 18:19

[v0.23.3](/chaiNNer-org/chaiNNer/tree/v0.23.3)

[`79b80df`](/chaiNNer-org/chaiNNer/commit/79b80df577b4ce2df3a4ac8f13b5ab5a3c98ecc0)

This is a hotfix release to fix a regression introduced in the v0.23.2 which caused iterators to error when running. Apologies to anyone who was affected by this issue.

## Bug Fixes

-   Fixed input gathering for collectors by [@RunDevelopment](https://github.com/RunDevelopment) in [#2818](https://github.com/chaiNNer-org/chaiNNer/pull/2818)

### Contributors

-   [![@RunDevelopment](https://avatars.githubusercontent.com/u/20878432?s=64&v=4)](https://github.com/RunDevelopment)

RunDevelopment

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

5 people reacted

## Alpha v0.23.2

[Alpha v0.23.2](/chaiNNer-org/chaiNNer/releases/tag/v0.23.2)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 23 Apr 23:34

[v0.23.2](/chaiNNer-org/chaiNNer/tree/v0.23.2)

[`c071afd`](/chaiNNer-org/chaiNNer/commit/c071afd588ff2c7246aa81751b16e83d129111ed)

This update fixes a few bugs and adds some new features.

Please note: If you install or update chaiNNer and get a critical error upon setup completion, please attempt restarting chaiNNer before reporting.

## What's Changed

-   Optimized Box Blur for different x-y radii by [@RunDevelopment](https://github.com/RunDevelopment) in [#2795](https://github.com/chaiNNer-org/chaiNNer/pull/2795)
-   Move FFMPEG download to the backend by [@RunDevelopment](https://github.com/RunDevelopment) in [#2799](https://github.com/chaiNNer-org/chaiNNer/pull/2799)
-   Improved validation for `goIntoDirectory` by [@RunDevelopment](https://github.com/RunDevelopment) in [#2801](https://github.com/chaiNNer-org/chaiNNer/pull/2801)
-   Support multi-en/disabling nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2800](https://github.com/chaiNNer-org/chaiNNer/pull/2800)
-   Validate all relative paths by [@RunDevelopment](https://github.com/RunDevelopment) in [#2809](https://github.com/chaiNNer-org/chaiNNer/pull/2809)
-   Add Skip existing files option for Save Image by [@RunDevelopment](https://github.com/RunDevelopment) in [#2808](https://github.com/chaiNNer-org/chaiNNer/pull/2808)
-   Add softness for Threshold anti-aliasing by [@RunDevelopment](https://github.com/RunDevelopment) in [#2812](https://github.com/chaiNNer-org/chaiNNer/pull/2812)

## New Nodes

-   Add "Crop Border" node to remove border/frame with constant color by [@RunDevelopment](https://github.com/RunDevelopment) in [#2794](https://github.com/chaiNNer-org/chaiNNer/pull/2794)

## Bug Fixes

-   Fix startup crash when using a system language other than English on Windows by [@joeyballentine](https://github.com/joeyballentine) in [#2815](https://github.com/chaiNNer-org/chaiNNer/pull/2815)
-   Prevent middle-mouse and right-click from triggering tab clicks by [@RaySit](https://github.com/RaySit) in [#2792](https://github.com/chaiNNer-org/chaiNNer/pull/2792)
-   Fixed 'Copy File Name' option for file inputs by [@RunDevelopment](https://github.com/RunDevelopment) in [#2793](https://github.com/chaiNNer-org/chaiNNer/pull/2793)
-   Don't allow ONNX conversion for Craft models by [@RunDevelopment](https://github.com/RunDevelopment) in [#2797](https://github.com/chaiNNer-org/chaiNNer/pull/2797)
-   Fixed SSE request not getting canceled and getting SSE stuck by [@RunDevelopment](https://github.com/RunDevelopment) in [#2806](https://github.com/chaiNNer-org/chaiNNer/pull/2806)

## New Contributors

-   [@RaySit](https://github.com/RaySit) made their first contribution in [#2792](https://github.com/chaiNNer-org/chaiNNer/pull/2792)

**Full Changelog**: [v0.23.1...v0.23.2](https://github.com/chaiNNer-org/chaiNNer/compare/v0.23.1...v0.23.2)

### Contributors

-   [![@RunDevelopment](https://avatars.githubusercontent.com/u/20878432?s=64&v=4)](https://github.com/RunDevelopment)
-   [![@joeyballentine](https://avatars.githubusercontent.com/u/34788790?s=64&v=4)](https://github.com/joeyballentine)
-   [![@RaySit](https://avatars.githubusercontent.com/u/77477538?s=64&v=4)](https://github.com/RaySit)

RunDevelopment, joeyballentine, and RaySit

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

4 people reacted

## Alpha v0.23.1

[Alpha v0.23.1](/chaiNNer-org/chaiNNer/releases/tag/v0.23.1)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 12 Apr 14:30

[v0.23.1](/chaiNNer-org/chaiNNer/tree/v0.23.1)

[`7fbc997`](/chaiNNer-org/chaiNNer/commit/7fbc9972ad318149f017d64e1ffb2528aa3a0411)

## What's Changed

-   Optimize Clamp node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2785](https://github.com/chaiNNer-org/chaiNNer/pull/2785)
-   Rename Fast NL means node to Denoise by [@RunDevelopment](https://github.com/RunDevelopment) in [#2786](https://github.com/chaiNNer-org/chaiNNer/pull/2786)

## Bug Fixes

-   Fix nodes not refreshing after changing dependencies by [@joeyballentine](https://github.com/joeyballentine) in [#2787](https://github.com/chaiNNer-org/chaiNNer/pull/2787)

**Full Changelog**: [v0.23.0...v0.23.1](https://github.com/chaiNNer-org/chaiNNer/compare/v0.23.0...v0.23.1)

### Contributors

-   [![@RunDevelopment](https://avatars.githubusercontent.com/u/20878432?s=64&v=4)](https://github.com/RunDevelopment)
-   [![@joeyballentine](https://avatars.githubusercontent.com/u/34788790?s=64&v=4)](https://github.com/joeyballentine)

RunDevelopment and joeyballentine

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

6 people reacted

## Alpha v0.23.0

[Alpha v0.23.0](/chaiNNer-org/chaiNNer/releases/tag/v0.23.0)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/chaiNNer-org/chaiNNer/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 11 Apr 03:08

[v0.23.0](/chaiNNer-org/chaiNNer/tree/v0.23.0)

[`e5dadc3`](/chaiNNer-org/chaiNNer/commit/e5dadc357d586439803f292bd6cee36020508cc7)

This biggest part of this release was a bunch of internal changes we made that aren't super easily reflected to users. However, you will (hopefully) notice a bit more stability in certain areas.

There are a bunch of new features, changes, bug fixes, and all the rest of the usual stuff included as well.

As always, please report any new issues that pop up in this release.

## Major Changes

-   Major internal refactors by [@joeyballentine](https://github.com/joeyballentine), [@RunDevelopment](https://github.com/RunDevelopment) in [#2597](https://github.com/chaiNNer-org/chaiNNer/pull/2597), [#2647](https://github.com/chaiNNer-org/chaiNNer/pull/2647), [#2649](https://github.com/chaiNNer-org/chaiNNer/pull/2649), [#2651](https://github.com/chaiNNer-org/chaiNNer/pull/2651), [#2650](https://github.com/chaiNNer-org/chaiNNer/pull/2650), [#2659](https://github.com/chaiNNer-org/chaiNNer/pull/2659), [#2675](https://github.com/chaiNNer-org/chaiNNer/pull/2675), [#2677](https://github.com/chaiNNer-org/chaiNNer/pull/2677), [#2683](https://github.com/chaiNNer-org/chaiNNer/pull/2683), [#2718](https://github.com/chaiNNer-org/chaiNNer/pull/2718), [#2719](https://github.com/chaiNNer-org/chaiNNer/pull/2719), [#2726](https://github.com/chaiNNer-org/chaiNNer/pull/2726), [#2738](https://github.com/chaiNNer-org/chaiNNer/pull/2738), [#2745](https://github.com/chaiNNer-org/chaiNNer/pull/2745), [#2748](https://github.com/chaiNNer-org/chaiNNer/pull/2748), [#2754](https://github.com/chaiNNer-org/chaiNNer/pull/2754), [#2755](https://github.com/chaiNNer-org/chaiNNer/pull/2755), [#2767](https://github.com/chaiNNer-org/chaiNNer/pull/2767), [#2769](https://github.com/chaiNNer-org/chaiNNer/pull/2769)
    -   Improves the reliability of stopping execution
    -   Improves the reliability of installing dependencies from the dependency manager
    -   Allows the UI to handle dependency installation even when using a remote host (note: remote hosts are still not fully supported)
-   Add ability to rename nodes by double clicking on the node's name by [@joeyballentine](https://github.com/joeyballentine) in [#2749](https://github.com/chaiNNer-org/chaiNNer/pull/2749)
-   Remove the splash screen, chaiNNer now starts directly to its main window by [@joeyballentine](https://github.com/joeyballentine) in [#2731](https://github.com/chaiNNer-org/chaiNNer/pull/2731), [#2758](https://github.com/chaiNNer-org/chaiNNer/pull/2758)
-   Add key information to collapsed nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2656](https://github.com/chaiNNer-org/chaiNNer/pull/2656), [#2657](https://github.com/chaiNNer-org/chaiNNer/pull/2657)
-   (PyTorch) Make PyTorch upscaling pauseable by [@RunDevelopment](https://github.com/RunDevelopment) in [#2705](https://github.com/chaiNNer-org/chaiNNer/pull/2705), [#2732](https://github.com/chaiNNer-org/chaiNNer/pull/2732)
-   Improve Python setup process by [@RunDevelopment](https://github.com/RunDevelopment) in [#2768](https://github.com/chaiNNer-org/chaiNNer/pull/2768)
-   Improve iterator ETA by [@RunDevelopment](https://github.com/RunDevelopment) in [#2775](https://github.com/chaiNNer-org/chaiNNer/pull/2775)
-   Allow math expressions in number inputs by [@RunDevelopment](https://github.com/RunDevelopment) in [#2697](https://github.com/chaiNNer-org/chaiNNer/pull/2697)

## Dependency Updates

-   (PyTorch) Update Spandrel for improved model support by [@RunDevelopment](https://github.com/RunDevelopment), [@joeyballentine](https://github.com/joeyballentine) in [#2655](https://github.com/chaiNNer-org/chaiNNer/pull/2655), [#2710](https://github.com/chaiNNer-org/chaiNNer/pull/2710), [#2661](https://github.com/chaiNNer-org/chaiNNer/pull/2661), [#2646](https://github.com/chaiNNer-org/chaiNNer/pull/2646)
    -   Adds support for RGT, Restormer, FFTformer, M3SNet, DCTLSA, APISR, MixDehazeNet, ATD, AdaCode, MPRNet, MIRNet2, DnCNN, FDnCNN, and DRUNet
    -   Removes SPSR support
-   (ONNX) Update ONNX & ONNX Runtime which fixes execution issues [@joeyballentine](https://github.com/joeyballentine) in [#2717](https://github.com/chaiNNer-org/chaiNNer/pull/2717)

## New Nodes

-   Add Directory Go Up and Directory to Text nodes [@RunDevelopment](https://github.com/RunDevelopment) in [#2695](https://github.com/chaiNNer-org/chaiNNer/pull/2695)
-   Add Directory Go Into node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2702](https://github.com/chaiNNer-org/chaiNNer/pull/2702)

## Minor Changes

-   Use a single settings file and refactor settings by [@RunDevelopment](https://github.com/RunDevelopment) in [#2640](https://github.com/chaiNNer-org/chaiNNer/pull/2640), [#2735](https://github.com/chaiNNer-org/chaiNNer/pull/2735)
-   Make the "Random Seed" button non-draggable by [@RunDevelopment](https://github.com/RunDevelopment) in [#2653](https://github.com/chaiNNer-org/chaiNNer/pull/2653)
-   Add setting to hide minimap by [@RunDevelopment](https://github.com/RunDevelopment) in [#2652](https://github.com/chaiNNer-org/chaiNNer/pull/2652)
-   Use package display name in dependency manager by [@RunDevelopment](https://github.com/RunDevelopment) in [#2672](https://github.com/chaiNNer-org/chaiNNer/pull/2672)
-   Improve error reporting by [@RunDevelopment](https://github.com/RunDevelopment) in [#2685](https://github.com/chaiNNer-org/chaiNNer/pull/2685)
-   Automatically remove unused nodes with side effects by [@RunDevelopment](https://github.com/RunDevelopment) in [#2690](https://github.com/chaiNNer-org/chaiNNer/pull/2690)
-   Automatically create directory for Save X nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2691](https://github.com/chaiNNer-org/chaiNNer/pull/2691)
-   Move important nodes up in Image category by [@RunDevelopment](https://github.com/RunDevelopment) in [#2692](https://github.com/chaiNNer-org/chaiNNer/pull/2692)
-   Automatically set value after clicking on steppers by [@RunDevelopment](https://github.com/RunDevelopment) in [#2698](https://github.com/chaiNNer-org/chaiNNer/pull/2698)
-   Ignore error types in docs by [@RunDevelopment](https://github.com/RunDevelopment) in [#2704](https://github.com/chaiNNer-org/chaiNNer/pull/2704)
-   Improve missing module error logging by [@RunDevelopment](https://github.com/RunDevelopment) in [#2737](https://github.com/chaiNNer-org/chaiNNer/pull/2737)
-   Improve UI for dependency manager by [@RunDevelopment](https://github.com/RunDevelopment) in [#2742](https://github.com/chaiNNer-org/chaiNNer/pull/2742), [#2743](https://github.com/chaiNNer-org/chaiNNer/pull/2743)
-   Clean up files on uninstall (windows only) by [@RunDevelopment](https://github.com/RunDevelopment) in [#2746](https://github.com/chaiNNer-org/chaiNNer/pull/2746)
-   Stop progress bar from moving logo by [@RunDevelopment](https://github.com/RunDevelopment) in [#2756](https://github.com/chaiNNer-org/chaiNNer/pull/2756)
-   Hide minimap by default by [@RunDevelopment](https://github.com/RunDevelopment) in [#2757](https://github.com/chaiNNer-org/chaiNNer/pull/2757)
-   Add "Clear" options for file and directory inputs by [@RunDevelopment](https://github.com/RunDevelopment) in [#2760](https://github.com/chaiNNer-org/chaiNNer/pull/2760)
-   Optimize Brightness and Contrast node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2773](https://github.com/chaiNNer-org/chaiNNer/pull/2773)
-   Optimize Hue & Saturation node by [@RunDevelopment](https://github.com/RunDevelopment) in [#2774](https://github.com/chaiNNer-org/chaiNNer/pull/2774)
-   Organize adjustments category by [@RunDevelopment](https://github.com/RunDevelopment) in [#2776](https://github.com/chaiNNer-org/chaiNNer/pull/2776)

## Bug Fixes

-   Fix default values not being added correctly on load by [@RunDevelopment](https://github.com/RunDevelopment) in [#2658](https://github.com/chaiNNer-org/chaiNNer/pull/2658)
-   Fix vivid light blend mode implementation by [@BigBoyBarney](https://github.com/BigBoyBarney) in [#2664](https://github.com/chaiNNer-org/chaiNNer/pull/2664)
-   Fix connection error tooltip getting stuck by [@RunDevelopment](https://github.com/RunDevelopment) in [#2676](https://github.com/chaiNNer-org/chaiNNer/pull/2676)
-   Fix glob negation by [@joeyballentine](https://github.com/joeyballentine) in [#2678](https://github.com/chaiNNer-org/chaiNNer/pull/2678)
-   Fix division by zero in progress calculation by [@RunDevelopment](https://github.com/RunDevelopment) in [#2686](https://github.com/chaiNNer-org/chaiNNer/pull/2686)
-   Fix F5 (and others) from inside number and text inputs by [@RunDevelopment](https://github.com/RunDevelopment) in [#2696](https://github.com/chaiNNer-org/chaiNNer/pull/2696)\\
-   Fix FLT\_MAX ONNX -> NCNN error by [@joeyballentine](https://github.com/joeyballentine) in [#2684](https://github.com/chaiNNer-org/chaiNNer/pull/2684)
-   Fix padding on number inputs by [@RunDevelopment](https://github.com/RunDevelopment) in [#2699](https://github.com/chaiNNer-org/chaiNNer/pull/2699)
-   Fix unused side-effect node optimization for Copy To Clipboard by [@RunDevelopment](https://github.com/RunDevelopment) in [#2700](https://github.com/chaiNNer-org/chaiNNer/pull/2700)
-   Fix symbols in path type tags by [@RunDevelopment](https://github.com/RunDevelopment) in [#2701](https://github.com/chaiNNer-org/chaiNNer/pull/2701), [#2706](https://github.com/chaiNNer-org/chaiNNer/pull/2706)
-   Fix search bar in node documentation being below nodes by [@RunDevelopment](https://github.com/RunDevelopment) in [#2703](https://github.com/chaiNNer-org/chaiNNer/pull/2703)
-   Fix context selector pane moving body by [@RunDevelopment](https://github.com/RunDevelopment) in [#2733](https://github.com/chaiNNer-org/chaiNNer/pull/2733)
-   Don't re-log empty messages by [@RunDevelopment](https://github.com/RunDevelopment) in [#2736](https://github.com/chaiNNer-org/chaiNNer/pull/2736)
-   Disallow converting SPAN models to NCNN by [@RunDevelopment](https://github.com/RunDevelopment) in [#2763](https://github.com/chaiNNer-org/chaiNNer/pull/2763)
-   Fix Execution Number node not working when collapsed by [@RunDevelopment](https://github.com/RunDevelopment) in [#2766](https://github.com/chaiNNer-org/chaiNNer/pull/2766)
-   Proper capitalization for TensorRT in ONNX settings by [@RunDevelopment](https://github.com/RunDevelopment) in [#2764](https://github.com/chaiNNer-org/chaiNNer/pull/2764)
-   Fix saving images with non-ASCII characters by [@RunDevelopment](https://github.com/RunDevelopment) in [#2772](https://github.com/chaiNNer-org/chaiNNer/pull/2772)

**Full Changelog**: [v0.22.2...v0.23.0](https://github.com/chaiNNer-org/chaiNNer/compare/v0.22.2...v0.23.0)

### Contributors

-   [![@RunDevelopment](https://avatars.githubusercontent.com/u/20878432?s=64&v=4)](https://github.com/RunDevelopment)
-   [![@joeyballentine](https://avatars.githubusercontent.com/u/34788790?s=64&v=4)](https://github.com/joeyballentine)
-   [![@BigBoyBarney](https://avatars.githubusercontent.com/u/86712892?s=64&v=4)](https://github.com/BigBoyBarney)

RunDevelopment, joeyballentine, and BigBoyBarney

Assets 9

Loading

### Uh oh!

There was an error while loading. Please reload this page.

4 people reacted

Previous [1](/chaiNNer-org/chaiNNer/releases?page=1) [2](/chaiNNer-org/chaiNNer/releases?page=2) [3](/chaiNNer-org/chaiNNer/releases?page=3) [4](/chaiNNer-org/chaiNNer/releases?page=4) [5](/chaiNNer-org/chaiNNer/releases?page=5) … [9](/chaiNNer-org/chaiNNer/releases?page=9) [10](/chaiNNer-org/chaiNNer/releases?page=10) [Next](/chaiNNer-org/chaiNNer/releases?page=2)

Previous [Next](/chaiNNer-org/chaiNNer/releases?page=2)

You can’t perform that action at this time.
