<!-- source: https://github.com/danielgatis/rembg/issues/668, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                          FAIL : Failed to load library libonnxruntime\_providers\_cuda.so with error: libcublasLt.so.12: cannot open shared object file: No such file or directory · Issue #668 · danielgatis/rembg · GitHub                                             

[Skip to content](#start-of-content)            

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fdanielgatis%2Frembg%2Fissues%2F668)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fdanielgatis%2Frembg%2Fissues%2F668)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fvoltron%2Fissues_fragments%2Fissue_layout&source=header-repo&source_repo=danielgatis%2Frembg)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

                 

## Repository navigation

                                                                                                                    [](/danielgatis/rembg)

# FAIL : Failed to load library libonnxruntime\_providers\_cuda.so with error: libcublasLt.so.12: cannot open shared object file: No such file or directory #668

[New issue](/login?return_to=https://github.com/danielgatis/rembg/issues/668)

Copy link

[New issue](/login?return_to=https://github.com/danielgatis/rembg/issues/668)

Copy link

Closed as not planned

Closed as not planned

[FAIL : Failed to load library libonnxruntime\_providers\_cuda.so with error: libcublasLt.so.12: cannot open shared object file: No such file or directory](/danielgatis/rembg/issues/668#top)#668

Copy link

Labels

[bugSomething isn't working](https://github.com/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working[stale](https://github.com/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)

## Description

[![@JianfeiMa](https://avatars.githubusercontent.com/u/20241982?u=8980f20660dedfe2184dc0115315d1578972e642&v=4&size=48)](https://github.com/JianfeiMa)

[JianfeiMa](https://github.com/JianfeiMa)

opened [on Sep 7, 2024](https://github.com/danielgatis/rembg/issues/668#issue-2511498773)

Issue body actions

2024-09-07 14:23:35.189200391 \[E:onnxruntime:Default, provider\_bridge\_ort.cc:1978 TryGetProviderInfo\_TensorRT\] /onnxruntime\_src/onnxruntime/core/session/provider\_bridge\_ort.cc:1637 onnxruntime::Provider& onnxruntime::ProviderLibrary::Get() \[ONNXRuntimeError\] : 1 : FAIL : Failed to load library libonnxruntime\_providers\_tensorrt.so with error: libcublas.so.12: cannot open shared object file: No such file or directory

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* EP Error \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
EP Error /onnxruntime\_src/onnxruntime/python/onnxruntime\_pybind\_state.cc:490 void onnxruntime::python::RegisterTensorRTPluginsAsCustomOps(PySessionOptions&, const onnxruntime::ProviderOptions&) Please install TensorRT libraries as mentioned in the GPU requirements page, make sure they're in the PATH or LD\_LIBRARY\_PATH, and that your GPU is supported.  
when using \['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider'\]  
Falling back to \['CUDAExecutionProvider', 'CPUExecutionProvider'\] and retrying.

* * *

2024-09-07 14:23:35.282705908 \[E:onnxruntime:Default, provider\_bridge\_ort.cc:1992 TryGetProviderInfo\_CUDA\] /onnxruntime\_src/onnxruntime/core/session/provider\_bridge\_ort.cc:1637 onnxruntime::Provider& onnxruntime::ProviderLibrary::Get() \[ONNXRuntimeError\] : 1 : FAIL : Failed to load library libonnxruntime\_providers\_cuda.so with error: libcublasLt.so.12: cannot open shared object file: No such file or directory

## Activity

1.  [![](https://avatars.githubusercontent.com/u/20241982?s=64&u=8980f20660dedfe2184dc0115315d1578972e642&v=4)JianfeiMa](/JianfeiMa)
    
    added
    
    [bugSomething isn't working](/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working
    
    [on Sep 7, 2024](https://github.com/danielgatis/rembg/issues/668#event-14168593682)
    
2.  ### github-actions commented on Oct 8, 2024
    
    [![@github-actions](https://avatars.githubusercontent.com/in/15368?v=4&size=48)](/apps/github-actions)
    
    [github-actions](/apps/github-actions)Bot
    
    [on Oct 8, 2024](https://github.com/danielgatis/rembg/issues/668#issuecomment-2398487000) – with [GitHub Actions](https://help.github.com/en/actions)
    
    More actions
    
    This issue is stale because it has been open for 30 days with no activity.
    
3.  [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)
    
    added
    
    [stale](/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)
    
    [on Oct 8, 2024](https://github.com/danielgatis/rembg/issues/668#event-14548943582)
    
4.  ### evan00144 commented on Oct 18, 2024
    
    [![@evan00144](https://avatars.githubusercontent.com/u/88994216?v=4&size=48)](/evan00144)
    
    [evan00144](/evan00144)
    
    [on Oct 18, 2024](https://github.com/danielgatis/rembg/issues/668#issuecomment-2422172828)
    
    More actions
    
    any updataes onm this?
    
    Reacted by Andrew Smalley and Karsten Larson
    
5.  [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)
    
    removed
    
    [stale](/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)
    
    [on Oct 19, 2024](https://github.com/danielgatis/rembg/issues/668#event-14728791918)
    
6.  ### github-actions commented on Nov 18, 2024
    
    [![@github-actions](https://avatars.githubusercontent.com/in/15368?v=4&size=48)](/apps/github-actions)
    
    [github-actions](/apps/github-actions)Bot
    
    [on Nov 18, 2024](https://github.com/danielgatis/rembg/issues/668#issuecomment-2481777829) – with [GitHub Actions](https://help.github.com/en/actions)
    
    More actions
    
    This issue is stale because it has been open for 30 days with no activity.
    
7.  [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)
    
    added
    
    [stale](/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)
    
    [on Nov 18, 2024](https://github.com/danielgatis/rembg/issues/668#event-15327325447)
    
8.  ### Karsten-Larson commented on Nov 20, 2024
    
    [![@Karsten-Larson](https://avatars.githubusercontent.com/u/45808840?v=4&size=48)](/Karsten-Larson)
    
    [Karsten-Larson](/Karsten-Larson)
    
    [on Nov 20, 2024](https://github.com/danielgatis/rembg/issues/668#issuecomment-2488904406)
    
    More actions
    
    I am experiencing the same issue
    
9.  [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)
    
    removed
    
    [stale](/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)
    
    [on Nov 21, 2024](https://github.com/danielgatis/rembg/issues/668#event-15374831934)
    
10.  ### Grizemc commented on Nov 26, 2024
    
    [![@Grizemc](https://avatars.githubusercontent.com/u/152372912?u=118c0e34dd638752892c71175f814934e6251529&v=4&size=48)](/Grizemc)
    
    [Grizemc](/Grizemc)
    
    [on Nov 26, 2024](https://github.com/danielgatis/rembg/issues/668#issuecomment-2500060652)
    
    More actions
    
    Maybe onnxtime has download problem
    
11.  ### github-actions commented on Dec 27, 2024
    
    [![@github-actions](https://avatars.githubusercontent.com/in/15368?v=4&size=48)](/apps/github-actions)
    
    [github-actions](/apps/github-actions)Bot
    
    [on Dec 27, 2024](https://github.com/danielgatis/rembg/issues/668#issuecomment-2563232090) – with [GitHub Actions](https://help.github.com/en/actions)
    
    More actions
    
    This issue is stale because it has been open for 30 days with no activity.
    
12.  [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)
    
    added
    
    [stale](/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)
    
    [on Dec 27, 2024](https://github.com/danielgatis/rembg/issues/668#event-15769113635)
    
13.  ### Quantuman134 commented on Jan 6, 2025
    
    [![@Quantuman134](https://avatars.githubusercontent.com/u/68807149?v=4&size=48)](/Quantuman134)
    
    [Quantuman134](/Quantuman134)
    
    [on Jan 6, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2572917281)
    
    More actions
    
    I install a previous version released in 2023, and worked out
    
14.  [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)
    
    removed
    
    [stale](/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)
    
    [on Jan 7, 2025](https://github.com/danielgatis/rembg/issues/668#event-15832717900)
    
15.  ### AD1PRAJAPATI commented on Jan 30, 2025
    
    [![@AD1PRAJAPATI](https://avatars.githubusercontent.com/u/98583957?v=4&size=48)](/AD1PRAJAPATI)
    
    [AD1PRAJAPATI](/AD1PRAJAPATI)
    
    [on Jan 30, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2623552795)
    
    More actions
    
    try below steps
    
    \-> onnxruntime-gpu version ==1.19.2  
    \-> torch version ==2.4.1  
    \-> CUDA VERSION > 12(based on the error you would be having greater than 12 )  
    \-> cuDNN VERISON > 9(just check this if you have cuDNN version 8.9 then you would be requiring  
    torch version 2.3.1 and onnxruntime-gpu version 1.18.0  
    )
    
    \-> after installing this you would get error like FAILED to find `libcudnn_cnn.so.9` so for that youll need to export lib path of that and run the command like this
    
    `LD_LIBRARY_PATH=$LD_LIBRARY_PATH: /miniconda3/envs/{your_enviroment}/lib/python3.11/site-packages/nvidia/cudnn/lib CUDA_VISIBLE_DEVICES=7 python {your_pythonscript}.py`
    
    \-> also before running the above just pass the provider in the session eg: `session = new_session("{model_name}",providers=['CUDAExecutionProvider'])` (you can check what providers you have using `import onnxruntime as ort`  
    `print(ort.get_available_providers())`)
    
    \-> The above steps worked for me , Thank you
    
16.  ### catscarlet commented on Feb 20, 2025
    
    [![@catscarlet](https://avatars.githubusercontent.com/u/10594035?u=4a758860ebfec3c1e5e95a59621dcdfb3f6cd9f1&v=4&size=48)](/catscarlet)
    
    [catscarlet](/catscarlet)
    
    [on Feb 20, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2670558679)
    
    Contributor
    
    More actions
    
    Here is the final result what I tried for months.
    
    part of my dockerfile
    
    ```
    FROM nvidia/cuda:12.2.2-devel-ubuntu22.04
    
    RUN apt update
    RUN apt install -y --no-install-recommends python3-pip
    RUN pip install onnxruntime-gpu --break-system-packages
    RUN pip install "rembg[gpu,cli]" --break-system-packages
    ```
    
    I use cuda:12.2 because my host only support cuda:12.2 right now.
    
    And when I ran rembg, this happened:
    
    ```
    2025-02-20 13:39:39.615359815 [E:onnxruntime:Default, provider_bridge_ort.cc:1848 TryGetProviderInfo_TensorRT] /onnxruntime_src/onnxruntime/core/session/provider_bridge_ort.cc:1539 onnxruntime::Provider& onnxruntime::ProviderLibrary::Get() [ONNXRuntimeError] : 1 : FAIL : Failed to load library libonnxruntime_providers_tensorrt.so with error: libnvinfer.so.10: cannot open shared object file: No such file or directory
    
    *************** EP Error ***************
    EP Error /onnxruntime_src/onnxruntime/python/onnxruntime_pybind_state.cc:507 void onnxruntime::python::RegisterTensorRTPluginsAsCustomOps(PySessionOptions&, const onnxruntime::ProviderOptions&) Please install TensorRT libraries as mentioned in the GPU requirements page, make sure they're in the PATH or LD_LIBRARY_PATH, and that your GPU is supported.
     when using ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
    Falling back to ['CUDAExecutionProvider', 'CPUExecutionProvider'] and retrying.
    ****************************************
    2025-02-20 13:39:39.740567077 [E:onnxruntime:Default, provider_bridge_ort.cc:1862 TryGetProviderInfo_CUDA] /onnxruntime_src/onnxruntime/core/session/provider_bridge_ort.cc:1539 onnxruntime::Provider& onnxruntime::ProviderLibrary::Get() [ONNXRuntimeError] : 1 : FAIL : Failed to load library libonnxruntime_providers_cuda.so with error: libcudnn.so.9: cannot open shared object file: No such file or directory
    ```
    
    I think most of the issues, in this repository are related to the **onnxruntime can't find cuda and tensorrt** issue, which wasn't there before. The inactive auto-closed just hide them like they were solved.  
    (The default Dockerfile is repository even has `RUN python -m pip install ".[cpu,cli]"` which are already funny)
    
    I also tried to use different onnxruntime version and whatever. I don't remember which was the last one that worked.  
    The requirement of **the whole thing of cuda** is already hilarious, and it also require **TensorRT**, which you can't even install it without **a complex nvidia developer sign up**, which I couldn't get one.
    
    I say Microsoft fucks up all onnxruntime users.
    
    It's dead. All open source onnx remove backgournd tools are dead. There are only commercial image editors with rembg features.  
    Just suffer with CPU when using it.
    
17.  ### AD1PRAJAPATI commented on Feb 20, 2025
    
    [![@AD1PRAJAPATI](https://avatars.githubusercontent.com/u/98583957?v=4&size=48)](/AD1PRAJAPATI)
    
    [AD1PRAJAPATI](/AD1PRAJAPATI)
    
    [on Feb 20, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2670592151)
    
    More actions
    
    I totally get it—this whole ONNXRuntime + CUDA + TensorRT setup is a mess. You're definitely not the only one dealing with this headache.
    
    From what you’ve shared, it’s still failing because TensorRT `(libnvinfer.so.10)` isn’t installed and cuDNN `(libcudnn.so.9)` isn’t being found. I actually mentioned the LD\_LIBRARY\_PATH fix in my last response, so you might wanna try that.
    
    For TensorRT, if you don’t really need it, just use `new_session("{model_name}",providers=['CUDAExecutionProvider'])` when setting up the session. That way, it won’t even try to load TensorRT and fail.
    
    Honestly, the way ONNXRuntime handles dependencies is kinda trash, but it’s not completely dead yet. If you still wanna troubleshoot, I’m happy to try!
    
    Reacted by sus71
    
    Reacted by sus71
    
18.  ### catscarlet commented on Feb 20, 2025
    
    [![@catscarlet](https://avatars.githubusercontent.com/u/10594035?u=4a758860ebfec3c1e5e95a59621dcdfb3f6cd9f1&v=4&size=48)](/catscarlet)
    
    [catscarlet](/catscarlet)
    
    [on Feb 20, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2670630843)
    
    Contributor
    
    More actions
    
    [@AD1PRAJAPATI](https://github.com/AD1PRAJAPATI) Thanks for your reply.
    
    > From what you’ve shared, it’s still failing because TensorRT `(libnvinfer.so.10)` isn’t installed and cuDNN `(libcudnn.so.9)` isn’t being found. I actually mentioned the LD\_LIBRARY\_PATH fix in my last response, so you might wanna try that.
    
    Well funny things:
    
    -   **nvidia/cuda:12.2.2-devel-ubuntu22.04** doesn't include file **libcudnn.so.9**, nor any **libcudnn** files.
    -   As my search on dockerhub, **cuda:12.2** version only has **12.2.2-cudnn8**, which includes **libcudnn.so.8**, not **libcudnn.so.9**
    
    My host right now is using ubuntu 20.04 based system so it only has old driver which only supports cuda 12.2. (yes i know it's coming eol. i just don't have time to upgrade it).
    
    Well. I think this is the best I can do.
    
19.  ### AD1PRAJAPATI commented on Feb 20, 2025
    
    [![@AD1PRAJAPATI](https://avatars.githubusercontent.com/u/98583957?v=4&size=48)](/AD1PRAJAPATI)
    
    [AD1PRAJAPATI](/AD1PRAJAPATI)
    
    [on Feb 20, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2670978136)
    
    More actions
    
    Yo, real quick—what versions of torch and torchvision are you running? Just wanna see if they line up with your CUDA/cuDNN setup, ‘cause that might be causing some of this chaos. Wouldn't be surprised if a mismatch is messing things up.
    
20.  ### catscarlet commented on Feb 22, 2025
    
    [![@catscarlet](https://avatars.githubusercontent.com/u/10594035?u=4a758860ebfec3c1e5e95a59621dcdfb3f6cd9f1&v=4&size=48)](/catscarlet)
    
    [catscarlet](/catscarlet)
    
    [on Feb 22, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2676189977)
    
    Contributor
    
    More actions
    
    > Yo, real quick—what versions of torch and torchvision are you running? Just wanna see if they line up with your CUDA/cuDNN setup, ‘cause that might be causing some of this chaos. Wouldn't be surprised if a mismatch is messing things up.
    
    Funny thing: I didn't manually install pytorch. I think there is no pytorch in my docker image.
    
21.  ### catscarlet commented on Feb 28, 2025
    
    [![@catscarlet](https://avatars.githubusercontent.com/u/10594035?u=4a758860ebfec3c1e5e95a59621dcdfb3f6cd9f1&v=4&size=48)](/catscarlet)
    
    [catscarlet](/catscarlet)
    
    [on Feb 28, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2689830314)
    
    Contributor
    
    More actions
    
    So I made a **Great Breakthrough**
    
    Here is the core of the Dockerfile I build for testing
    
    ```
    FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
    
    RUN apt update
    RUN apt install -y --no-install-recommends python3-pip
    RUN pip install onnxruntime-gpu --break-system-packages
    RUN pip install "rembg[gpu,cli]" --break-system-packages
    ```
    
    Command I used for running docker:  
    `docker run --gpus all -v /dev/dri:/dev/dri -v /mystorage2/libs/u2net:/root/.u2net -v $PWD:/rembg rembg-docker-gpu-test`
    
    Yea I upgrade my computer to Linux Mint 22.1 (based on Ubuntu24.04) so now my driver is 550.120 with CUDA 12.4
    
    The onnxruntime-gpu version in this test is confirmed **1.20.1** by `print(onnxruntime.__version__)`
    
    ```
    :~$ nvidia-smi
    Fri Feb 28 13:41:44 2025       
    +-----------------------------------------------------------------------------------------+
    | NVIDIA-SMI 550.120                Driver Version: 550.120        CUDA Version: 12.4     |
    ```
    
    After the docker image build finish. I test and it doesn't have the lib missing issue anymore, **BUT it still use ONLY CPU** .
    
    Then I run some debug and here is the big deal.
    
    In rembg/sessions/base.py, i add both `print(ort.get_device())` and `print(ort.get_available_providers())` in _**init**_ and it gives this everytime I run it.
    
    ```
    GPU
    ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
    ```
    
    So now I'm sure two thing,
    
    -   onnxruntime-gpu was successfully installed and it can detect GPU
    -   It says TensorrtExecutionProvider is one of the available provider, which was totally wrong because I didn't install any of Tensorrt shit.
    
    I continued my testing and this made a great progress:
    
    ```
    def __init__(self, model_name: str, sess_opts: ort.SessionOptions, providers=['CUDAExecutionProvider'], *args, **kwargs):
            """Initialize an instance of the BaseSession class."""
            self.model_name = model_name
            #providers = ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']     //Ignore this.
            providers = ['CUDAExecutionProvider']       //This
            self.inner_session = ort.InferenceSession(
                str(self.__class__.download_models(*args, **kwargs)),
                sess_options=sess_opts,
                providers=providers,                                   //And this
            )
    ```
    
    Now I'm forcing onnxruntime to using CUDAExecutionProvider, and it worked. I can hear the fan of Graphic Card instead of CPU's
    
    The speed difference between with and with out `providers = ['CUDAExecutionProvider']` when running `time rembg i -m birefnet-general realesrgan2x.png realesrgan2x_rembg.png`
    
    With `providers = ['CUDAExecutionProvider']`
    
    ```
    
    GPU
    ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
    
    real	0m11.130s
    user	0m10.317s
    sys	0m1.438s
    ```
    
    Without `providers = ['CUDAExecutionProvider']`
    
    ```
    root@003e1933d74c:/rembg# time rembg i -m birefnet-general realesrgan2x.png realesrgan2x_rembg.png 
    GPU
    ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
    
    real	0m29.869s
    user	1m9.945s
    sys	0m3.733s
    
    ```
    
    Now I'm sure **this is a terrible onnxruntime bug** . In common sense, it usually goes like this:
    
    -   Use an onnxruntime.get\_available\_providers() order like `['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']`
    -   Try using GPU, if fail, try CPU as failsafe. (it's actually as same as the above one)
    
    Turns out by default onnxruntime/onnxruntime-gpu use CPU at first with no reason. WTF!  
    Yeah if I try `providers = ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']`, which the TensorrtExecutionProvider would break, it still go like this:
    
    ```
    2025-02-28 13:58:36.158909947 [E:onnxruntime:Default, provider_bridge_ort.cc:1848 TryGetProviderInfo_TensorRT] /onnxruntime_src/onnxruntime/core/session/provider_bridge_ort.cc:1539 onnxruntime::Provider& onnxruntime::ProviderLibrary::Get() [ONNXRuntimeError] : 1 : FAIL : Failed to load library libonnxruntime_providers_tensorrt.so with error: libnvinfer.so.10: cannot open shared object file: No such file or directory
    
    *************** EP Error ***************
    EP Error /onnxruntime_src/onnxruntime/python/onnxruntime_pybind_state.cc:507 void onnxruntime::python::RegisterTensorRTPluginsAsCustomOps(PySessionOptions&, const onnxruntime::ProviderOptions&) Please install TensorRT libraries as mentioned in the GPU requirements page, make sure they're in the PATH or LD_LIBRARY_PATH, and that your GPU is supported.
     when using ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
    Falling back to ['CUDAExecutionProvider', 'CPUExecutionProvider'] and retrying.
    ****************************************
    GPU
    ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
    
    real	0m10.730s
    user	0m10.174s
    sys	0m1.472s
    ```
    
    Yeah after TensorRT fail, it goes CUDA for accurately.
    
    So I think this one is related to many issues like: [#682](https://github.com/danielgatis/rembg/issues/682) [#664](https://github.com/danielgatis/rembg/issues/664) [#707](https://github.com/danielgatis/rembg/issues/707) [#439](https://github.com/danielgatis/rembg/issues/439) [#696](https://github.com/danielgatis/rembg/issues/696)
    
    Conclusion:  
    Onnxruntime messed us up. Onnxruntime requires terrible cuda and cudnn compatibility. Provider must be provided to onnxruntime or it will use CPU first even we install onnxruntime-gpu.
    
    Fix:  
    I'm still now very sure. The official dockerfile declared `FROM python:3.10-slim` and `RUN python -m pip install ".[cpu,cli]"`. I don't know if we can run rembg\[gpu\] without cuda nor cuddn nor onnxruntime-gpu.  
    Maybe more tests is needed.
    
22.  ### catscarlet commented on Feb 28, 2025
    
    [![@catscarlet](https://avatars.githubusercontent.com/u/10594035?u=4a758860ebfec3c1e5e95a59621dcdfb3f6cd9f1&v=4&size=48)](/catscarlet)
    
    [catscarlet](/catscarlet)
    
    [on Feb 28, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2689853768)
    
    Contributor
    
    More actions
    
    > I'm still now very sure. The official dockerfile declared `FROM python:3.10-slim` and `RUN python -m pip install ".[cpu,cli]"`. I don't know if we can run rembg\[gpu\] without cuda nor cuddn nor onnxruntime-gpu.  
    > Maybe more tests is needed.
    
    OK CUDA is still needed. onnxruntime is installed by `setup.py`.
    
23.  ### AD1PRAJAPATI commented on Feb 28, 2025
    
    [![@AD1PRAJAPATI](https://avatars.githubusercontent.com/u/98583957?v=4&size=48)](/AD1PRAJAPATI)
    
    [AD1PRAJAPATI](/AD1PRAJAPATI)
    
    [on Feb 28, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2689856249)
    
    More actions
    
    Damn, that’s wild. So ONNXRuntime really just defaulting to CPU even when GPU is available? That’s actually insane. Makes no sense why it wouldn’t prioritize CUDAExecutionProvider automatically.
    
    The whole TensorrtExecutionProvider thing is hilarious too—like, bro, I didn’t even install TensorRT, why are you acting like it’s there? 😂
    
    Lowkey feels like ONNXRuntime just doesn’t know what to do unless you explicitly tell it to use CUDA. Also, the fact that it still falls back properly after TensorRT fails but won’t just go straight to CUDA first?? Yeah, that’s sus.
    
    Appreciate you digging into this though, ‘cause this might be the reason so many people are struggling with ONNX and GPUs. I’m guessing the only real fix (for now) is to force CUDAExecutionProvider in the code. But man, ONNXRuntime gotta get it together.
    
    Reacted by Cat Scarlet, Ricardo G. Sousa and 𝘿𝙚𝙘𝙞𝙢𝙖𝙩𝙞𝙤𝙣
    
24.  ### catscarlet commented on Feb 28, 2025
    
    [![@catscarlet](https://avatars.githubusercontent.com/u/10594035?u=4a758860ebfec3c1e5e95a59621dcdfb3f6cd9f1&v=4&size=48)](/catscarlet)
    
    [catscarlet](/catscarlet)
    
    [on Feb 28, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2689914205)
    
    Contributor
    
    More actions
    
    > The whole TensorrtExecutionProvider thing is hilarious too—like, bro, I didn’t even install TensorRT, why are you acting like it’s there?
    
    I got funnier one. I tried **nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04** to replace **nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04** so to save disk space, but cudnn-runtime gives me this:
    
    ```
    root@1ab131f73295:/rembg# rembg i -m birefnet-general 20250224182548.png 20250224182548_rembg2.png 
    Segmentation fault (core dumped)
    ```
    
    So **cudnn-devel** is required.  
    I also tried plain cuda but libcudnn is required and cuda doesn't offer libcudnn
    
    ```
    root@7cec443ec049:/rembg# rembg i -m birefnet-general 20250224182548.png 20250224182548_rembg.png 
    2025-02-28 14:56:30.568092315 [E:onnxruntime:Default, provider_bridge_ort.cc:1862 TryGetProviderInfo_CUDA] /onnxruntime_src/onnxruntime/core/session/provider_bridge_ort.cc:1539 onnxruntime::Provider& onnxruntime::ProviderLibrary::Get() [ONNXRuntimeError] : 1 : FAIL : Failed to load library libonnxruntime_providers_cuda.so with error: libcudnn.so.9: cannot open shared object file: No such file or directory
    
    root@7cec443ec049:/rembg# find / -name libcudnn*
    root@7cec443ec049:/rembg# 
    ```
    
    What a shitty show.
    
25.  ### github-actions commented on Mar 31, 2025
    
    [![@github-actions](https://avatars.githubusercontent.com/in/15368?v=4&size=48)](/apps/github-actions)
    
    [github-actions](/apps/github-actions)Bot
    
    [on Mar 31, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2764926543) – with [GitHub Actions](https://help.github.com/en/actions)
    
    More actions
    
    This issue is stale because it has been open for 30 days with no activity.
    
26.  [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)
    
    added
    
    [stale](/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)
    
    [on Mar 31, 2025](https://github.com/danielgatis/rembg/issues/668#event-17050089306)
    
27.  ### github-actions commented on Apr 14, 2025
    
    [![@github-actions](https://avatars.githubusercontent.com/in/15368?v=4&size=48)](/apps/github-actions)
    
    [github-actions](/apps/github-actions)Bot
    
    [on Apr 14, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2800298042) – with [GitHub Actions](https://help.github.com/en/actions)
    
    More actions
    
    This issue was closed because it has been inactive for 14 days since being marked as stale.
    
28.  [![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](/apps/github-actions)
    
    closed this as [not planned](/danielgatis/rembg/issues?q=is%3Aissue%20state%3Aclosed%20archived%3Afalse%20reason%3Anot-planned)[on Apr 14, 2025](https://github.com/danielgatis/rembg/issues/668#event-17240705469)
    
29.  ### kzhang2 commented on May 6, 2025
    
    [![@kzhang2](https://avatars.githubusercontent.com/u/12497065?u=10e6da73929c95494f45cfaf90b6509666cec162&v=4&size=48)](/kzhang2)
    
    [kzhang2](/kzhang2)
    
    [on May 6, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-2855069107)
    
    More actions
    
    To fix this issue, I believe we can use my solution posted in a different thread to properly enable `Tensorrt` support for `rembg`: [#707 (comment)](https://github.com/danielgatis/rembg/issues/707#issuecomment-2855062603). I'd also like to point out to [@catscarlet](https://github.com/catscarlet) that the `Tensorrt` libraries can be installed through `pip` without registering for an NVIDIA developer account, and my comment shows how to do so.
    
30.  ### thomaskleiven commented on Jul 3, 2025
    
    [![@thomaskleiven](https://avatars.githubusercontent.com/u/17145074?u=769adf93d3bb50ecbc021d99af736746daf27875&v=4&size=48)](/thomaskleiven)
    
    [thomaskleiven](/thomaskleiven)
    
    [on Jul 3, 2025](https://github.com/danielgatis/rembg/issues/668#issuecomment-3031118016)
    
    Contributor
    
    More actions
    
    I also found it annoying that `print(ort.get_device())` and `print(ort.get_available_providers())` might give wrong execution providers. I put up a PR where we can use custom logic to determine which execution providers to use: [#768](https://github.com/danielgatis/rembg/pull/768)
    

[Sign up for free](/signup?return_to=https://github.com/danielgatis/rembg/issues/668) **to join this conversation on GitHub.** Already have an account? [Sign in to comment](/login?return_to=https://github.com/danielgatis/rembg/issues/668)

## Metadata

## Metadata

### Assignees

No one assigned

### Labels

[bugSomething isn't working](https://github.com/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22bug%22)Something isn't working[stale](https://github.com/danielgatis/rembg/issues?q=state%3Aopen%20label%3A%22stale%22)

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

No branches or pull requests

## Issue actions

-

You can’t perform that action at this time.
