<!-- source: https://github.com/nihui/waifu2x-ncnn-vulkan, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - nihui/waifu2x-ncnn-vulkan: waifu2x converter ncnn version, runs fast on intel / amd / nvidia / apple-silicon GPU with vulkan · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fnihui%2Fwaifu2x-ncnn-vulkan)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fnihui%2Fwaifu2x-ncnn-vulkan)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=nihui%2Fwaifu2x-ncnn-vulkan)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/nihui/waifu2x-ncnn-vulkan)

![nihui](https://avatars.githubusercontent.com/u/171016?s=60&v=4)

**[waifu2x-ncnn-vulkan](/nihui/waifu2x-ncnn-vulkan)**

Public

-   
-   [Notifications](/login?return_to=%2Fnihui%2Fwaifu2x-ncnn-vulkan)You must be signed in to change notification settings
-   [Fork239 (239)](/login?return_to=%2Fnihui%2Fwaifu2x-ncnn-vulkan)
-   [Star3.5k (3.5k)](/login?return_to=%2Fnihui%2Fwaifu2x-ncnn-vulkan)You must be signed in to star a repository

## About

waifu2x converter ncnn version, runs fast on intel / amd / nvidia / apple-silicon GPU with vulkan

### Topics

[amd](/topics/amd)[gpu](/topics/gpu)[intel](/topics/intel)[linux](/topics/linux)[macos](/topics/macos)[ncnn](/topics/ncnn)[nvidia](/topics/nvidia)[vulkan](/topics/vulkan)[waifu2x](/topics/waifu2x)[windows](/topics/windows)

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

[Activity](/nihui/waifu2x-ncnn-vulkan/activity)

### Stars

**3.5k** stars

### Watchers

**48** watching

### Forks

[**239** forks](/nihui/waifu2x-ncnn-vulkan/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fnihui%2Fwaifu2x-ncnn-vulkan&report=nihui+%28user%29)

[Branches](/nihui/waifu2x-ncnn-vulkan/branches)[Tags](/nihui/waifu2x-ncnn-vulkan/tags)

[](/nihui/waifu2x-ncnn-vulkan/branches)[](/nihui/waifu2x-ncnn-vulkan/tags)

Open more actions menu

## Latest commit

## History

[159 Commits](/nihui/waifu2x-ncnn-vulkan/commits/master/)

[](/nihui/waifu2x-ncnn-vulkan/commits/master/)159 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[.github](/nihui/waifu2x-ncnn-vulkan/tree/master/.github ".github")

[.github](/nihui/waifu2x-ncnn-vulkan/tree/master/.github ".github")

[images](/nihui/waifu2x-ncnn-vulkan/tree/master/images "images")

[images](/nihui/waifu2x-ncnn-vulkan/tree/master/images "images")

[models](/nihui/waifu2x-ncnn-vulkan/tree/master/models "models")

[models](/nihui/waifu2x-ncnn-vulkan/tree/master/models "models")

[src](/nihui/waifu2x-ncnn-vulkan/tree/master/src "src")

[src](/nihui/waifu2x-ncnn-vulkan/tree/master/src "src")

[.gitmodules](/nihui/waifu2x-ncnn-vulkan/blob/master/.gitmodules ".gitmodules")

[.gitmodules](/nihui/waifu2x-ncnn-vulkan/blob/master/.gitmodules ".gitmodules")

[LICENSE](/nihui/waifu2x-ncnn-vulkan/blob/master/LICENSE "LICENSE")

[LICENSE](/nihui/waifu2x-ncnn-vulkan/blob/master/LICENSE "LICENSE")

[README.md](/nihui/waifu2x-ncnn-vulkan/blob/master/README.md "README.md")

[README.md](/nihui/waifu2x-ncnn-vulkan/blob/master/README.md "README.md")

## Repository files navigation

# waifu2x ncnn Vulkan

[](#waifu2x-ncnn-vulkan)

[![CI](https://github.com/nihui/waifu2x-ncnn-vulkan/workflows/CI/badge.svg)](https://github.com/nihui/waifu2x-ncnn-vulkan/workflows/CI/badge.svg) [![download](https://camo.githubusercontent.com/6569b3025d71e2d1a797e3961b61b19dd46e0a92e82e71688d815682a63dad82/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f6e696875692f776169667532782d6e636e6e2d76756c6b616e2f746f74616c2e737667)](https://camo.githubusercontent.com/6569b3025d71e2d1a797e3961b61b19dd46e0a92e82e71688d815682a63dad82/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f6e696875692f776169667532782d6e636e6e2d76756c6b616e2f746f74616c2e737667)

ncnn implementation of waifu2x converter. Runs fast on Intel / AMD / NVIDIA / Apple-Silicon with Vulkan API.

waifu2x-ncnn-vulkan uses [ncnn project](https://github.com/Tencent/ncnn) as the universal neural network inference framework.

## [Download](https://github.com/nihui/waifu2x-ncnn-vulkan/releases)

[](#download)

Download Windows/Linux/macOS Executable for Intel/AMD/NVIDIA/Apple-Silicon GPU

**[https://github.com/nihui/waifu2x-ncnn-vulkan/releases](https://github.com/nihui/waifu2x-ncnn-vulkan/releases)**

This package includes all the binaries and models required. It is portable, so no CUDA or Caffe runtime environment is needed :)

## Usages

[](#usages)

### Example Command

[](#example-command)

waifu2x-ncnn-vulkan.exe -i input.jpg -o output.png -n 2 -s 2

### Full Usages

[](#full-usages)

Usage: waifu2x-ncnn-vulkan -i infile -o outfile \[options\]...

  -h                   show this help
  -v                   verbose output
  -i input-path        input image path (jpg/png/webp) or directory
  -o output-path       output image path (jpg/png/webp) or directory
  -n noise-level       denoise level (-1/0/1/2/3, default=0)
  -s scale             upscale ratio (1/2/4/8/16/32, default=2)
  -t tile-size         tile size (>=32/0=auto, default=0) can be 0,0,0 for multi-gpu
  -m model-path        waifu2x model path (default=models-cunet)
  -g gpu-id            gpu device to use (-1=cpu, default=auto) can be 0,1,2 for multi-gpu
  -j load:proc:save    thread count for load/proc/save (default=1:2:2) can be 1:2,2,2:2 for multi-gpu
  -x                   enable tta mode
  -f format            output image format (jpg/png/webp, default=ext/png)

-   `input-path` and `output-path` accept either file path or directory path
-   `noise-level` = noise level, large value means strong denoise effect, -1 = no effect
-   `scale` = scale level, 1 = no scaling, 2 = upscale 2x
-   `tile-size` = tile size, use smaller value to reduce GPU memory usage, default selects automatically
-   `load:proc:save` = thread count for the three stages (image decoding + waifu2x upscaling + image encoding), using larger values may increase GPU usage and consume more GPU memory. You can tune this configuration with "4:4:4" for many small-size images, and "2:2:2" for large-size images. The default setting usually works fine for most situations. If you find that your GPU is hungry, try increasing thread count to achieve faster processing.
-   `format` = the format of the image to be output, png is better supported, however webp generally yields smaller file sizes, both are losslessly encoded

If you encounter a crash or error, try upgrading your GPU driver:

-   Intel: [https://downloadcenter.intel.com/product/80939/Graphics-Drivers](https://downloadcenter.intel.com/product/80939/Graphics-Drivers)
-   AMD: [https://www.amd.com/en/support](https://www.amd.com/en/support)
-   NVIDIA: [https://www.nvidia.com/Download/index.aspx](https://www.nvidia.com/Download/index.aspx)

## Build from Source

[](#build-from-source)

1.  (macOS only) Download and setup the Vulkan SDK from [https://vulkan.lunarg.com/](https://vulkan.lunarg.com/)
    
2.  Clone this project with all submodules
    

git clone https://github.com/nihui/waifu2x-ncnn-vulkan.git
cd waifu2x-ncnn-vulkan
git submodule update --init --recursive

3.  Build with CMake

-   You can pass -DUSE\_STATIC\_MOLTENVK=ON option to avoid linking the vulkan loader library on macOS

mkdir build
cd build
cmake ../src
cmake --build . -j 4

## Speed Comparison with waifu2x-caffe-cui

[](#speed-comparison-with-waifu2x-caffe-cui)

### Environment

[](#environment)

-   Windows 10 1809
-   AMD R7-1700
-   NVIDIA GTX-1070
-   NVIDIA driver 419.67
-   CUDA 10.1.105
-   cuDNN 10.1

Measure-Command { waifu2x-ncnn-vulkan.exe \-i input.png \-o output.png \-n 2 \-s 2 \-t \[block size\] \-m \[model dir\] }

Measure-Command { waifu2x-caffe-cui.exe \-t 0 \--gpu 0 \-b 1 \-c \[block size\] \-p cudnn \--model\_dir \[model dir\] \-s 2 \-n 2 \-m noise\_scale \-i input.png \-o output.png }

### cunet

[](#cunet)

Image Size

Target Size

Block Size

Total Time(s)

GPU Memory(MB)

waifu2x-ncnn-vulkan

200x200

400x400

400/200/100

0.86/0.86/0.82

638/638/197

waifu2x-caffe-cui

200x200

400x400

400/200/100

2.54/2.39/2.36

3017/936/843

waifu2x-ncnn-vulkan

400x400

800x800

400/200/100

1.17/1.04/1.02

2430/638/197

waifu2x-caffe-cui

400x400

800x800

400/200/100

2.91/2.43/2.7

3202/1389/1178

waifu2x-ncnn-vulkan

1000x1000

2000x2000

400/200/100

2.35/2.26/2.46

2430/638/197

waifu2x-caffe-cui

1000x1000

2000x2000

400/200/100

4.04/3.79/4.35

3258/1582/1175

waifu2x-ncnn-vulkan

2000x2000

4000x4000

400/200/100

6.46/6.59/7.49

2430/686/213

waifu2x-caffe-cui

2000x2000

4000x4000

400/200/100

7.01/7.54/10.11

3258/1499/1200

waifu2x-ncnn-vulkan

4000x4000

8000x8000

400/200/100

22.78/23.78/27.61

2448/654/213

waifu2x-caffe-cui

4000x4000

8000x8000

400/200/100

18.45/21.85/31.82

3325/1652/1236

### upconv\_7\_anime\_style\_art\_rgb

[](#upconv_7_anime_style_art_rgb)

Image Size

Target Size

Block Size

Total Time(s)

GPU Memory(MB)

waifu2x-ncnn-vulkan

200x200

400x400

400/200/100

0.74/0.75/0.72

482/482/142

waifu2x-caffe-cui

200x200

400x400

400/200/100

2.04/1.99/1.99

995/546/459

waifu2x-ncnn-vulkan

400x400

800x800

400/200/100

0.95/0.83/0.81

1762/482/142

waifu2x-caffe-cui

400x400

800x800

400/200/100

2.08/2.12/2.11

995/546/459

waifu2x-ncnn-vulkan

1000x1000

2000x2000

400/200/100

1.52/1.41/1.44

1778/482/142

waifu2x-caffe-cui

1000x1000

2000x2000

400/200/100

2.72/2.60/2.68

1015/570/459

waifu2x-ncnn-vulkan

2000x2000

4000x4000

400/200/100

3.45/3.42/3.63

1778/482/142

waifu2x-caffe-cui

2000x2000

4000x4000

400/200/100

3.90/4.01/4.35

1015/521/462

waifu2x-ncnn-vulkan

4000x4000

8000x8000

400/200/100

11.16/11.29/12.07

1796/498/158

waifu2x-caffe-cui

4000x4000

8000x8000

400/200/100

9.24/9.81/11.16

995/546/436

## Sample Images

[](#sample-images)

### Original Image

[](#original-image)

[![origin](/nihui/waifu2x-ncnn-vulkan/raw/master/images/0.jpg)](/nihui/waifu2x-ncnn-vulkan/blob/master/images/0.jpg)

### Upscale 2x with ImageMagick

[](#upscale-2x-with-imagemagick)

convert origin.jpg -resize 200% output.png

[![browser](/nihui/waifu2x-ncnn-vulkan/raw/master/images/1.png)](/nihui/waifu2x-ncnn-vulkan/blob/master/images/1.png)

### Upscale 2x with ImageMagick Lanczo4 Filter

[](#upscale-2x-with-imagemagick-lanczo4-filter)

convert origin.jpg -filter Lanczos -resize 200% output.png

[![browser](/nihui/waifu2x-ncnn-vulkan/raw/master/images/4.png)](/nihui/waifu2x-ncnn-vulkan/blob/master/images/4.png)

### Upscale 2x with waifu2x noise=2 scale=2

[](#upscale-2x-with-waifu2x-noise2-scale2)

waifu2x-ncnn-vulkan.exe -i origin.jpg -o output.png -n 2 -s 2

[![waifu2x](/nihui/waifu2x-ncnn-vulkan/raw/master/images/2.png)](/nihui/waifu2x-ncnn-vulkan/blob/master/images/2.png)

## Original waifu2x Project

[](#original-waifu2x-project)

-   [https://github.com/nagadomi/waifu2x](https://github.com/nagadomi/waifu2x)
-   [https://github.com/lltcggie/waifu2x-caffe](https://github.com/lltcggie/waifu2x-caffe)

## Other Open-Source Code Used

[](#other-open-source-code-used)

-   [https://github.com/Tencent/ncnn](https://github.com/Tencent/ncnn) for fast neural network inference on ALL PLATFORMS
-   [https://github.com/webmproject/libwebp](https://github.com/webmproject/libwebp) for encoding and decoding Webp images on ALL PLATFORMS
-   [https://github.com/libjpeg-turbo/libjpeg-turbo](https://github.com/libjpeg-turbo/libjpeg-turbo) for encoding and decoding JPEG images on ALL PLATFORMS
-   [https://github.com/pnggroup/libpng](https://github.com/pnggroup/libpng) for encoding and decoding PNG images on ALL PLATFORMS
-   [https://github.com/zlib-ng/zlib-ng](https://github.com/zlib-ng/zlib-ng) for encoding and decoding PNG images on ALL PLATFORMS
-   [https://github.com/tronkko/dirent](https://github.com/tronkko/dirent) for listing files in directory on Windows

## About

waifu2x converter ncnn version, runs fast on intel / amd / nvidia / apple-silicon GPU with vulkan

### Topics

[amd](/topics/amd)[gpu](/topics/gpu)[intel](/topics/intel)[linux](/topics/linux)[macos](/topics/macos)[ncnn](/topics/ncnn)[nvidia](/topics/nvidia)[vulkan](/topics/vulkan)[waifu2x](/topics/waifu2x)[windows](/topics/windows)

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

[Activity](/nihui/waifu2x-ncnn-vulkan/activity)

### Stars

**3.5k** stars

### Watchers

**48** watching

### Forks

[**239** forks](/nihui/waifu2x-ncnn-vulkan/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fnihui%2Fwaifu2x-ncnn-vulkan&report=nihui+%28user%29)

## Releases

## Sponsor this project

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.
