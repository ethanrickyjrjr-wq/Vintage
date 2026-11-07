<!-- source: https://github.com/xinntao/Real-ESRGAN/releases, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                           Releases · xinntao/Real-ESRGAN · GitHub                                                         

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fxinntao%2FReal-ESRGAN%2Freleases)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fxinntao%2FReal-ESRGAN%2Freleases)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Freleases%2Findex&source=header-repo&source_repo=xinntao%2FReal-ESRGAN)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

                  

## Repository navigation

[](/xinntao/Real-ESRGAN)

# Releases

 

Releases · xinntao/Real-ESRGAN

## Real-ESRGAN v0.3.0 Release Note

[Real-ESRGAN v0.3.0 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.3.0) [Latest](/xinntao/Real-ESRGAN/releases/latest)

[Latest](/xinntao/Real-ESRGAN/releases/latest)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4) [github-actions](/apps/github-actions) released this 20 Sep 11:58

[v0.3.0](/xinntao/Real-ESRGAN/tree/v0.3.0)

[`fa4c8a0`](/xinntao/Real-ESRGAN/commit/fa4c8a03ae3dbc9ea6ed471a6ab5da94ac15c2ea)

🚀 Long time no see ☄️

✨ **Highlights**

✅ [add realesr-general-x4v3 and realesr-general-wdn-x4v3](https://github.com/xinntao/Real-ESRGAN/commit/b827be13a1db242ebaea1be8669c62b757bd2796). They are very tiny models for general scenes, and they may more robust. But as they are tiny models, their performance may be limited.  
✅ [support denoise strength for realesr-general-x4v3](https://github.com/xinntao/Real-ESRGAN/commit/576aaddfaf1dec031cdf580924c00f4b29b9b35a). You can use the **\-dn** option to adjust the denising strength. Denoise strength. 0 for weak denoise (keep noise), 1 for strong denoise ability. Only used for the realesr-general-x4v3 model.  
✅ [update inference\_video: support auto download](https://github.com/xinntao/Real-ESRGAN/commit/61e81d3108f9437a9d97b02fd94439e9fc191ed0). You do not need to download models explicitly. If the models are not download, they will be downloaded automatically.

✅ [support ffmpeg stream for inference\_realesrgan\_video](https://github.com/xinntao/Real-ESRGAN/commit/cdc14b74a54e4247581b31c66caf93ea9e0cf159)  
✅ [fix colorspace bug & support multi-gpu and multi-processing](https://github.com/xinntao/Real-ESRGAN/commit/8cb9bd403e0b8206eb69780b97b35cf7aa84bd4e)  
✅ [Added GPU selection feature to python inference](https://github.com/xinntao/Real-ESRGAN/commit/6b15fc693646da1f16ba38ee47cf71a285f08390)  
✅ [deal with flv format](https://github.com/xinntao/Real-ESRGAN/commit/e5e79fbde32cf96720d484511fbae2272144beb6)

📢📢📢

[https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth)

[https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-wdn-x4v3.pth](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-wdn-x4v3.pth)

[![](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/assets/realesrgan_logo.png)](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/assets/realesrgan_logo.png)

Assets 2

Loading

### Uh oh!

There was an error while loading. Please reload this page.

148 people reacted

## Real-ESRGAN V0.2.5.0 Release Note

[Real-ESRGAN V0.2.5.0 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.2.5.0)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 24 Apr 12:09

[v0.2.5.0](/xinntao/Real-ESRGAN/tree/v0.2.5.0)

[`685d429`](/xinntao/Real-ESRGAN/commit/685d429c81888252bdb10f56c7754baededc3823)

[![](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/assets/realesrgan_logo.png)](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/assets/realesrgan_logo.png)

The major update: 🎉

✅ We update the **RealESRGAN AnimeVideo-v3** model, which can achieve better results with a faster inference speed.  
The improvements are:

-   **better naturalness**
-   **Fewer artifacts**
-   **more faithful to the original colors**
-   **better texture restoration**
-   **better background restoration**

You can find more details in [anime video models](https://github.com/xinntao/Real-ESRGAN/blob/master/docs/anime_video_model.md) and [comparisons](https://github.com/xinntao/Real-ESRGAN/blob/master/docs/anime_comparisons.md).

The models can be downloaded from [realesr-animevideov3](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-animevideov3.pth).

✅ We also update the ncnn.  
Portable [Windows](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-windows.zip) / [Linux](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-ubuntu.zip) / [MacOS](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-macos.zip) **executable files for Intel/AMD/Nvidia GPU**.

Assets 8

Loading

### Uh oh!

There was an error while loading. Please reload this page.

90 people reacted

## Real-ESRGAN V0.2.4.0 Release Note

[Real-ESRGAN V0.2.4.0 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.2.4.0)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 15 Feb 16:05

[v0.2.4.0](/xinntao/Real-ESRGAN/tree/v0.2.4.0)

[`f115f40`](/xinntao/Real-ESRGAN/commit/f115f40a775095cc81cd8033005c2df5771651a6)

Have a nice day 😸 and happy everyday 😃

I am happy to add a simple logo to Real-ESRGAN 😋 (designed by myself! and inspired by the [4K logo](https://www.google.com/search?q=4k+logo))  
So I release a new version~

You can see it on [ReadMe](https://github.com/xinntao/Real-ESRGAN)

[![](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/assets/realesrgan_logo.png)](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/assets/realesrgan_logo.png)

Assets 2

Loading

### Uh oh!

There was an error while loading. Please reload this page.

41 people reacted

## Real-ESRGAN V0.2.3.0 Release Note

[Real-ESRGAN V0.2.3.0 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.2.3.0)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 12 Dec 12:26

[v0.2.3.0](/xinntao/Real-ESRGAN/tree/v0.2.3.0)

[`f07aaff`](/xinntao/Real-ESRGAN/commit/f07aaffda04c7e69f11e6bfaf8023a6435471459)

Long long time no see😺

We have added small models for **anime videos**: 🎉

You can find demos and usages in [https://github.com/xinntao/Real-ESRGAN/blob/master/docs/anime\_video\_model.md](https://github.com/xinntao/Real-ESRGAN/blob/master/docs/anime_video_model.md)

✅ We add small models that are optimized for anime videos :-)

Now we have added two models.

Models

Scale

Description

[RealESRGANv2-animevideo-xsx2](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.3.0/RealESRGANv2-animevideo-xsx2.pth)

X2

Anime video model with XS size

[RealESRGANv2-animevideo-xsx4](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.3.0/RealESRGANv2-animevideo-xsx4.pth)

X4

Anime video model with XS size

This release also contains the following files:

-   RealESRGANv2-animevideo-xsx2.pth
-   RealESRGANv2-animevideo-xsx4.pth
-   realesrgan-ncnn-vulkan-20211212-windows.zip
-   realesrgan-ncnn-vulkan-20211212-macos.zip
-   realesrgan-ncnn-vulkan-20211212-ubuntu.zip

Assets 7

Loading

### Uh oh!

There was an error while loading. Please reload this page.

28 people reacted

9 [Join discussion](/xinntao/Real-ESRGAN/discussions/182)

## Real-ESRGAN V0.2.2.4 Release Note

[Real-ESRGAN V0.2.2.4 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.2.2.4)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 31 Aug 16:30

[v0.2.2.4](/xinntao/Real-ESRGAN/tree/v0.2.2.4)

[`f83472d`](/xinntao/Real-ESRGAN/commit/f83472d0113b8af82b5c5dcaa6e5a9dc88e466a7)

See you again 😺

**The major update**: 🎉

-   ✅ We add [_RealESRGAN\_x4plus\_anime\_6B.pth_](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth), which is optimized for **anime** images with much smaller model size. More details and comparisons with [waifu2x](https://github.com/nihui/waifu2x-ncnn-vulkan) are in [**anime\_model.md**](https://github.com/xinntao/Real-ESRGAN/blob/master/docs/anime_model.md)

[![](https://raw.githubusercontent.com/xinntao/public-figures/master/Real-ESRGAN/cmp_realesrgan_anime_1.png)](https://raw.githubusercontent.com/xinntao/public-figures/master/Real-ESRGAN/cmp_realesrgan_anime_1.png)

**Other updates**:

-   ✅ Support finetuning on your own data or paired data (_i.e._, finetuning ESRGAN). See [here](https://github.com/xinntao/Real-ESRGAN/blob/master/Training.md#Finetune-Real-ESRGAN-on-your-own-dataset)
-   ✅ We add [CONTRIBUTING.md](https://github.com/xinntao/Real-ESRGAN/blob/master/CONTRIBUTING.md). Welcome to your contributions 😃

This release also contains the following files:

-   RealESRGAN\_x4plus\_anime\_6B.pth
-   RealESRGAN\_x4plus\_anime\_6B\_netD.pth
-   realesrgan-ncnn-vulkan-20210901-windows.zip
-   realesrgan-ncnn-vulkan-20210901-macos.zip
-   realesrgan-ncnn-vulkan-20210901-ubuntu.zip

Assets 7

Loading

### Uh oh!

There was an error while loading. Please reload this page.

56 people reacted

## Real-ESRGAN V0.2.2.3 Release Note

[Real-ESRGAN V0.2.2.3 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.2.2.3)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 26 Aug 14:31

[v0.2.2.3](/xinntao/Real-ESRGAN/tree/v0.2.2.3)

[`9976a34`](/xinntao/Real-ESRGAN/commit/9976a34454bf5885635cdf5fb4434671098150cd)

-   Add `finetune_realesrgan_x4plus.yml`
-   Add scripts for data preparation:
    -   `generate_multiscale_DF2K.py`
    -   `generate_meta_info.py`

File list:

-   `RealESRGAN_x4plus_netD.pth`
-   `RealESRGAN_x2plus_netD.pth`

Assets 4

Loading

### Uh oh!

There was an error while loading. Please reload this page.

14 people reacted

## Real-ESRGAN V0.2.1 Release Note

[Real-ESRGAN V0.2.1 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.2.1)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 08 Aug 13:35

[v0.2.1](/xinntao/Real-ESRGAN/tree/v0.2.1)

[`64ad194`](/xinntao/Real-ESRGAN/commit/64ad194ddaf9c4d8c4b0d1b98cac6d89d3ea0d11)

-   Support PyPI
-   Support arbitrary scale with `--outscale`
-   Add RealESRGAN\_x2plus.pth model

File list:

-   `RealESRGAN_x2plus.pth`

Assets 3

Loading

### Uh oh!

There was an error while loading. Please reload this page.

23 people reacted

## Real-ESRGAN V0.1.2 Release Note

[Real-ESRGAN V0.1.2 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.1.2)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 31 Jul 18:30

[v0.1.2](/xinntao/Real-ESRGAN/tree/v0.1.2)

[`935993a`](/xinntao/Real-ESRGAN/commit/935993a0406ee43f6fc8899c7a58fd63e2a1a000)

This release is mainly for updating `realesrgan-ncnn-vulkan` executable files.

-   We have added Linux/MacOS executable files
    
-   We add back the `tta` option
    
-   We add the function: when the destination folder does not exist, create it!
    

File list:

-   `realesrgan-ncnn-vulkan-20210801-windows.zip`
-   `realesrgan-ncnn-vulkan-20210801-macos.zip`
-   `realesrgan-ncnn-vulkan-20210801-ubuntu.zip`

Assets 5

Loading

### Uh oh!

There was an error while loading. Please reload this page.

12 people reacted

## Real-ESRGAN V0.1.1 Release Note

[Real-ESRGAN V0.1.1 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.1.1)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 25 Jul 08:06

[v0.1.1](/xinntao/Real-ESRGAN/tree/v0.1.1)

[`2ed9863`](/xinntao/Real-ESRGAN/commit/2ed98632c05fb4185aadfe882db53a756cdbe703)

This release is mainly for storing pre-trained models and executable files.

-   `RealESRGAN-ncnn-vulkan-20210725-windows.zip`
    
-   `RealESRNet_x4plus.pth`
    
-   `ESRGAN_SRx4_DF2KOST_official-ff704c30.pth`
    

Note that: `RealESRGAN_x4plus.pth` can be found in [https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN\_x4plus.pth](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth)

Assets 5

Loading

### Uh oh!

There was an error while loading. Please reload this page.

## Real-ESRGAN V0.1.0 Release Note

[Real-ESRGAN V0.1.0 Release Note](/xinntao/Real-ESRGAN/releases/tag/v0.1.0)

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. Please reload this page.

## No results found

[View all tags](/xinntao/Real-ESRGAN/tags)

![@xinntao](https://avatars.githubusercontent.com/u/17445847?s=40&v=4) [xinntao](/xinntao) released this 22 Jul 19:15

[v0.1.0](/xinntao/Real-ESRGAN/tree/v0.1.0)

[`4c05b20`](/xinntao/Real-ESRGAN/commit/4c05b20cb30aded73ed3731848a9fbbf70c7c0ac)

This release is mainly for storing pre-trained models and executable files.

1.  RealESRGAN-ncnn-vulkan.zip
2.  RealESRGAN\_x4plus.pth

Assets 4

Loading

### Uh oh!

There was an error while loading. Please reload this page.

8 people reacted

You can’t perform that action at this time.
