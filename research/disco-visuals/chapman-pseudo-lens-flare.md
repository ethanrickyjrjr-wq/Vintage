#  [ john-chapman-graphics ](https://john-chapman-graphics.blogspot.com/)
## Pages
  * [Index](https://john-chapman-graphics.blogspot.com/)


## 22/02/2013
###  Pseudo Lens Flare 
Lens flare is a photographic artefact, caused by various interactions between a lens and the light passing through it. Although it is an artefact, there are a number of motives for simulating lens flare for use in computer graphics:  

  * it increases the perceived brightness and the apparent dynamic range of an image
  * lens flare is ubiquitous in photography, hence its absence in a computer generated images can be conspicuous
  * it can play an important stylistic or dramatic role, or work as part of the gameplay mechanics for video games (think of glare blinding the player)

For real time lens flares, sprite-based techniques have traditionally been the most common approach. Although sprites produce easily controllable and largely realistic results, they have to be placed explicitly and require occlusion data to be displayed correctly. Here I'll describe a simple and relatively cheap screen space process which produces a "pseudo" lens flare from an input colour buffer. It is not physically based, so errs somewhat from photorealism, but can be used as an addition to (or enhancement of) traditional sprite-based effects.   

##  Algorithm
The approach consists of 4 stages:   

  1. Downsample/threshold.
  2. Generate lens flare features.
  3. Blur.
  4. Upscale/blend with original image.


###  1. Downsample/Threshold
Downsampling is key to reducing the cost of subsequent stages. Additionally, we want to select a subset of the brightest pixels in the source image to participate in the lens flare. Using a scale/bias provides a flexible way to achieve this:   


```
   uniform sampler2D uInputTex;

   uniform vec4 uScale;
   uniform vec4 uBias;

   noperspective in vec2 vTexcoord;

   out vec4 fResult;

   void main() {
      fResult = max(vec4(0.0), texture(uInputTex, vTexcoord) + uBias) * uScale;
   }
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRmCNvOiUua0sIjuWUVdQuVw7ypPB3y8jguFQlmpf6gkJT6Q8rYuzQVI1TS4FCOox9EE2IMoyPajfcXPZGJIwzIe64ezXWVLdsKl9DwKvtbCMJteTWCoQmf7rPthU4nYzwCyKuB1Ct5Os/s1600/fig1.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRmCNvOiUua0sIjuWUVdQuVw7ypPB3y8jguFQlmpf6gkJT6Q8rYuzQVI1TS4FCOox9EE2IMoyPajfcXPZGJIwzIe64ezXWVLdsKl9DwKvtbCMJteTWCoQmf7rPthU4nYzwCyKuB1Ct5Os/s1600/fig1.jpg)
Adjusting the scale/bias is the main way to tweak the effect; the best settings will be dependant on the dynamic range of the input as well as how subtle you want the result to look. Because of the approximate nature of this technique, subtle is probably better.  

###  2. Feature Generation
Lens flare features tend to pivot around the image centre. To mimic this, we can just flip the result of the previous stage horizontally/vertically. This is easily done at the feature generation stage by flipping the texture coordinates:   


```
   vec2 texcoord = -vTexcoords + vec2(1.0);
```

Doing this isn't strictly necessary; the rest of the feature generation works perfectly well with or without it. However, the result of flipping the texture coordinates helps to visually separate the lens flare effect from the source image.  
  
**GHOSTS**  
  
"Ghosts" are the repetitious blobs which mirror bright spots in the input, pivoting around the image centre. The approach I've take to generate these is to get a vector from the current pixel to the centre of the screen, then take a number of samples along this vector.   

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGwdmQ2Hf3VcqfDPEnDnbSjzkvzPek64stNWp0xV5kfUC88Nl9PRhVwHT0JA5G1sYlb2yuMbj-NtbdRFt-wV97qLEBK3G8IPe5TNyhf-3P6EalQnb8DzvxsE_tk2W7V5EVMxUw9FujihM/s1600/fig2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGwdmQ2Hf3VcqfDPEnDnbSjzkvzPek64stNWp0xV5kfUC88Nl9PRhVwHT0JA5G1sYlb2yuMbj-NtbdRFt-wV97qLEBK3G8IPe5TNyhf-3P6EalQnb8DzvxsE_tk2W7V5EVMxUw9FujihM/s1600/fig2.jpg)

```
   uniform sampler2D uInputTex;

   uniform int uGhosts; // number of ghost samples
   uniform float uGhostDispersal; // dispersion factor

   noperspective in vec2 vTexcoord;

   out vec4 fResult;

   void main() {
      vec2 texcoord = -vTexcoord + vec2(1.0);
      vec2 texelSize = 1.0 / vec2(textureSize(uInputTex, 0));
 
   // ghost vector to image centre:
      vec2 ghostVec = (vec2(0.5) - texcoord) * uGhostDispersal;
   
   // sample ghosts:  
      vec4 result = vec4(0.0);
      for (int i = 0; i < uGhosts; ++i) { 
         vec2 offset = fract(texcoord + ghostVec * float(i));
  
         result += texture(uInputTex, offset);
      }
 
      fResult = result;
   }
```

Note that I use `fract()` to ensure that the texture coordinates wrap around; you could equally use `GL_REPEAT` as the texture's/sampler's wrap mode.  
  
Here's the result:   

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEeH3jOPUBL2hLkY2Py6YarvqxkG7HMXu3jfqoDc_UMAv7fzN7K4hfYWBPwb2vO9-UifgQ7zTy_eOwbHI40y9H8vTAI9AVfGNivDBwdf2qxIMXUON0rQ20HQjpBpxwHaERUZqiDmJhIWY/s1600/fig3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEeH3jOPUBL2hLkY2Py6YarvqxkG7HMXu3jfqoDc_UMAv7fzN7K4hfYWBPwb2vO9-UifgQ7zTy_eOwbHI40y9H8vTAI9AVfGNivDBwdf2qxIMXUON0rQ20HQjpBpxwHaERUZqiDmJhIWY/s1600/fig3.jpg)
We can improve this by allowing only bright spots from the centre of the source image to generate ghosts. We do this by weighting samples by a falloff from the image centre:  


```
   vec4 result = vec4(0.0);
   for (int i = 0; i < uGhosts; ++i) { 
      vec2 offset = fract(texcoord + ghostVec * float(i));
      
      _float weight = length(vec2(0.5) - offset) / length(vec2(0.5));_
      _weight = pow(1.0 - weight, 10.0);_
  
      result += texture(uInputTex, offset) * weight;
   }

```

The weight function is about as simple as it gets - a linear falloff. The reason we perform the weighting inside the sampling loop is so that bright spots in the centre of the input image can 'cast' ghosts to the edges, but bright spots at the edges can't cast ghosts to the centre.  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEIBExRWlgBjnquHlSQ_yEr7h_t1a1N3khdS1TFaC-KoETWo9KF-GNocw0RlhZaf7RVF6RLzH-cvkT2mq_kym08ln8OXmbTDbYzUuAnO0B76o2cJrDugQ6Cd1GzNzzeV2PAx6tc3mRDn0/s1600/fig4.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEIBExRWlgBjnquHlSQ_yEr7h_t1a1N3khdS1TFaC-KoETWo9KF-GNocw0RlhZaf7RVF6RLzH-cvkT2mq_kym08ln8OXmbTDbYzUuAnO0B76o2cJrDugQ6Cd1GzNzzeV2PAx6tc3mRDn0/s1600/fig4.jpg)
A final improvement can be made by modulating the ghost colour radially according to a 1D texture:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEfmHiu-QZfofA24K8GPXnZjVwyASBSzHXc2a_PJtuGpHbLSU8RUs1X8PpTvEoO0dScSUY5Rc6NC3_KFEeziVH2BENeUnVvNTOzYThglPidDFqsPifR_nR7DHmcwXgKzvnhH4jlB0Z_aU/s1600/fig5.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEfmHiu-QZfofA24K8GPXnZjVwyASBSzHXc2a_PJtuGpHbLSU8RUs1X8PpTvEoO0dScSUY5Rc6NC3_KFEeziVH2BENeUnVvNTOzYThglPidDFqsPifR_nR7DHmcwXgKzvnhH4jlB0Z_aU/s1600/fig5.jpg)
This is applied _after_ the ghost sampling loop so as to affect the final ghost colour:  


```
   result *= texture(uLensColor, length(vec2(0.5) - texcoord) / length(vec2(0.5)));
```

**  
****HALOS**  
**  
**If we take a vector to the centre of the image, as for the ghost sampling, but fix the vector length, we get a different effect: the source image is radially warped:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdzoTXTTqptgfKQBZFo7zuOvKzkAewXTEngb7-o-fMBxcphBdkNQ0ycTq6XlVj1PjkOOftKFaSQo04CFhAZi4khAytqRJSAz9zZ5w4YQSjPpgLU9356YYc3BC6WOKNXzwmhUVdG9MGgVg/s1600/fig6.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdzoTXTTqptgfKQBZFo7zuOvKzkAewXTEngb7-o-fMBxcphBdkNQ0ycTq6XlVj1PjkOOftKFaSQo04CFhAZi4khAytqRJSAz9zZ5w4YQSjPpgLU9356YYc3BC6WOKNXzwmhUVdG9MGgVg/s1600/fig6.jpg)
We can use this to produce a "halo", weighting the sample to to restrict the contribution of the warped image to a ring, the radius of which is controlled by `uHaloWidth`:  


```
   // sample halo:
   vec2 haloVec = normalize(ghostVec) * uHaloWidth;
   float weight = length(vec2(0.5) - fract(texcoord + haloVec)) / length(vec2(0.5));
   weight = pow(1.0 - weight, 5.0);
   result += texture(uInputTex, texcoord + haloVec) * weight;
```

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOA_ALzDt6rv3u-ZTakhdAGlIwhcie1FCugBFgpVHXlI3AOQUPDLXOI0qe3bImg8qOt9wiA82nUyamj7ndFnbWQMy0o6CatSKjgylmqsd2bfECB76_VI5wHWBFm1emSK-Q1oQK94bB8BM/s1600/fig7.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOA_ALzDt6rv3u-ZTakhdAGlIwhcie1FCugBFgpVHXlI3AOQUPDLXOI0qe3bImg8qOt9wiA82nUyamj7ndFnbWQMy0o6CatSKjgylmqsd2bfECB76_VI5wHWBFm1emSK-Q1oQK94bB8BM/s1600/fig7.jpg)
**CHROMATIC DISTORTION**  
**  
**Some lens flares exhibit chromatic distortion, caused by the varying refraction of different wavelengths of light. We can simulate this by creating a texture lookup function which fetches the red, green and blue channels separately at slightly different offsets along the sampling vector:  
  


```
   vec3 textureDistorted(
      in sampler2D tex,
      in vec2 texcoord,
      in vec2 direction, // direction of distortion
      in vec3 distortion // per-channel distortion factor
   ) {
      return vec3(
         texture(tex, texcoord + direction * distortion.r).r,
         texture(tex, texcoord + direction * distortion.g).g,
         texture(tex, texcoord + direction * distortion.b).b
      );
   }
```

This can be used as a direct replacement for the calls to `texture()` in the previous listings. I use the following for the `direction` and `distortion` parameters:  
  


```
   vec2 texelSize = 1.0 / vec2(textureSize(uInputTex, 0));
   vec3 distortion = vec3(-texelSize.x * uDistortion, 0.0, texelSize.x * uDistortion);

   vec3 direction = normalize(ghostVec);
```

Although this is simple it does cost 3x as many texture fetches, although they should all be cache-friendly unless you set `uDistortion` to some huge value.  
  
That's it for feature generation. Here's the result:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGUOWjaXp_rZgpLIsXFAsnzRJ53C42BfRHbiDX8sLZi1RbUCLw3_Sm9cdxT-I_6BeIKyrknqeZ1SHukw8qJPLVh4vRRKsQ0RtbTKjmQopWOGc5EDrR2LjMli4D26Nv5dzeGNvCI-jAKWA/s1600/fig8.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGUOWjaXp_rZgpLIsXFAsnzRJ53C42BfRHbiDX8sLZi1RbUCLw3_Sm9cdxT-I_6BeIKyrknqeZ1SHukw8qJPLVh4vRRKsQ0RtbTKjmQopWOGc5EDrR2LjMli4D26Nv5dzeGNvCI-jAKWA/s1600/fig8.jpg)
###  3. Blur
Without applying a blur, the lens flare features (in particular, the ghosts) tend to retain the appearance of the source image. By applying a blur to the lens flare features we attenuate high frequencies and in doing so reduce the coherence with the input image, which helps to sell the effect.  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiX6tPtn_PLTz1f_yeSOB9ZfxwgMrdNPGxl_xLcGCoyGnhGGh9zVEmQw-uESslGGYJ8K__tw7Sb5O0gchsiBl4O3Ui0N7Q5uc6_SFAPiCSKAjt-_bbBhgTV0xj_fOvHeezYEhBUck-E1XU/s1600/fig9.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiX6tPtn_PLTz1f_yeSOB9ZfxwgMrdNPGxl_xLcGCoyGnhGGh9zVEmQw-uESslGGYJ8K__tw7Sb5O0gchsiBl4O3Ui0N7Q5uc6_SFAPiCSKAjt-_bbBhgTV0xj_fOvHeezYEhBUck-E1XU/s1600/fig9.jpg)
I'll not cover how to achieve the blur here; there are plenty of [resources on the web](http://rastergrid.com/blog/2010/09/efficient-gaussian-blur-with-linear-sampling/).  

###  4. Upscale/Blend
So now we have our lens flare features, nicely blurred. How do we combine this with the original source image? There are a couple of important considerations to make regarding the overall rendering pipeline:  
  

  * Any post process motion blur or depth of field effect must be applied _prior_ to combining the lens flare, so that the lens flare features don't participate in those effects. Technically the lens flare features would exhibit some motion blur, however it's incompatible with post process motion techniques. As a compromise, you could implement the lens flare using an accumulation buffer.
  * The lens flare should be applied before any tonemapping operation. This makes physical sense, as tonemapping simulates the reaction of the film/CMOS to the incoming light, of which the lens flare is a constituent part.


With this in mind, there are a couple of things we can do at this stage to improve the result:
  

**LENS DIRT**
**  
**
The first is to modulate the lens flare features by a full-resolution "dirt" texture (as used [heavily](http://www.sliceofthe.net/wp-content/uploads/2011/10/bf3-2011-09-29-01-14-32-75.jpg) in _Battlefield 3_):
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglY6PScg5yVtK4XUeI5k0jokRUSxiRoXvZ2AZ36O9P7eCBdnq8i6Rahnj8hJKqTbuhISe92RgkEoKq1wj3tplw_HNsUujsSNiHBwIMMEpUejcIysfcgW3KbJv2XgxzbtMM2L66MwHelHc/s1600/fig10.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglY6PScg5yVtK4XUeI5k0jokRUSxiRoXvZ2AZ36O9P7eCBdnq8i6Rahnj8hJKqTbuhISe92RgkEoKq1wj3tplw_HNsUujsSNiHBwIMMEpUejcIysfcgW3KbJv2XgxzbtMM2L66MwHelHc/s1600/fig10.jpg)

```
   uniform sampler2D uInputTex; // source image
   uniform sampler2D uLensFlareTex; // input from the blur stage
   uniform sampler2D uLensDirtTex; // full resolution dirt texture

   noperspective in vec2 vTexcoord;

   out vec4 fResult;

   void main() {
      vec4 lensMod = texture(uLensDirtTex, vTexcoord);
      vec4 lensFlare = texture(uLensFlareTex, vTexcoord) * lensMod;
      fResult = texture(uInputTex, vTexcoord) + lensflare;
   }
```

The key to this is the lens dirt texture itself. If the contrast is low, the shapes of the lens flare features tend to dominate the result. As the contrast increases, the lens flare features are subdued, giving a different aesthetic appearance, as well as hiding a few of the imperfections.
  

**DIFFRACTION STARBURST**  
  
As a further enhancement, we can use a starburst texture in addition to the lens dirt:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipqz7yQwYB4fXQzrNtaAj6xJAYOT0XXp3KR3mxGAhyphenhyphenfxrSX_Y6sftyNivSKu9C5uLGFEgc_Gna7tRxeCWkXXcztmisMHjqNjQgPGbDyFWQNcPyOxq-BcDaltMHm0kAA4CIdaSvjFHXRlA/s1600/fig11.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipqz7yQwYB4fXQzrNtaAj6xJAYOT0XXp3KR3mxGAhyphenhyphenfxrSX_Y6sftyNivSKu9C5uLGFEgc_Gna7tRxeCWkXXcztmisMHjqNjQgPGbDyFWQNcPyOxq-BcDaltMHm0kAA4CIdaSvjFHXRlA/s1600/fig11.jpg)
As a static texture, the starburst doesn't look very good. We can, however, provide a transformation matrix to the shader which allows us to spin/warp it per frame and produce the dynamic effect we want:  
  


```
   uniform sampler2D uInputTex; // source image
   uniform sampler2D uLensFlareTex; // input from the blur stage
   uniform sampler2D uLensDirtTex; // full resolution dirt texture

   _uniform sampler2D uLensStarTex; // diffraction starburst texture_
   _uniform mat3 uLensStarMatrix; // transforms texcoords_

   noperspective in vec2 vTexcoord;

   out vec4 fResult;

   void main() {
      vec4 lensMod = texture(uLensDirtTex, vTexcoord);

      _vec2 lensStarTexcoord = (uLensStarMatrix * vec3(vTexcoord, 1.0)).xy;_
      _lensMod += texture(uLensStarTex, lensStarTexcoord);_

      vec4 lensFlare = texture(uLensFlareTex, vTexcoord) * lensMod;
      fResult = texture(uInputTex, vTexcoord) + lensflare;
   }
```

The transformation matrix `uLensStarMatrix` is based on a value derived from the camera's orientation as follows:  


```
   vec3 camx = cam.getViewMatrix().col(0); // camera x (left) vector
   vec3 camz = cam.getViewMatrix().col(1); // camera z (forward) vector
   float camrot = dot(camx, vec3(0,0,1)) + dot(camz, vec3(0,1,0));
```

There are other ways of obtaining the `camrot` value; it just needs to change continuously as the camera rotates. The matrix itself is constructed as follows:  
  


```
   mat3 scaleBias1 = (
      2.0f,   0.0f,  -1.0f,
      0.0f,   2.0f,  -1.0f,
      0.0f,   0.0f,   1.0f,
   );
   mat3 rotation = (
      cos(camrot), -sin(camrot), 0.0f,
      sin(camrot), cos(camrot),  0.0f,
      0.0f,        0.0f,         1.0f
   );
   mat3 scaleBias2 = (
      0.5f,   0.0f,   0.5f,
      0.0f,   0.5f,   0.5f,
      0.0f,   0.0f,   1.0f,
   );

   mat3 uLensStarMatrix = scaleBias2 * rotation * scaleBias1;
```

The scale and bias matrices are required in order to shift the texture coordinate origin so that we can rotate the starburst around the image centre.  

###  Conclusion
So, that's it! This method demonstrates how a relatively simplistic, image-based post process can produce a decent looking lens flare. It's not quite photorealistic, but when applied subtly can give some lovely results. I've provided a [demo implementation](http://www.john-chapman.net/demos/lensflare.zip).
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyGqLSCAfAdT59iFB1yg-NAmwcPdqPBvduGGoU2uSvP9cjM3LxVF0z4YeOxps5t3goOebl13xb0W-WFh6UZb_cMFSGdLnEyE-pbKhyphenhyphenk_Glb5r5_tk1JMVoWNA7urZH_x8P3ZZTUv6BS4A/s1600/fig12.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyGqLSCAfAdT59iFB1yg-NAmwcPdqPBvduGGoU2uSvP9cjM3LxVF0z4YeOxps5t3goOebl13xb0W-WFh6UZb_cMFSGdLnEyE-pbKhyphenhyphenk_Glb5r5_tk1JMVoWNA7urZH_x8P3ZZTUv6BS4A/s1600/fig12.jpg)
  

[ ![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif) ](https://www.blogger.com/post-edit.g?blogID=1326576410402178223&postID=6595424090675074632&from=pencil "Edit Post")
[Email This](https://www.blogger.com/share-post/1326576410402178223/6595424090675074632?https=true&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post/1326576410402178223/6595424090675074632?https=true&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post/1326576410402178223/6595424090675074632?https=true&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post/1326576410402178223/6595424090675074632?https=true&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post/1326576410402178223/6595424090675074632?https=true&target=pinterest "Share to Pinterest")
#### 23 comments:
  1. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[KingBadger3D](https://www.blogger.com/profile/14620728494317053050)[13 March 2013 at 11:10](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1363173021333#c2879910722874523460)
Great work, Keep it up Mr Chapman. My rendering engine is coming along but im reaching the point where ill need a good bit of help and advice. If i could send you another mail about somethings that would be great, Ill also send a copy of my code over. Your camera movement and materials are awesome. :)
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/2879910722874523460)
[Replies](javascript:;)
[Reply](javascript:;)
  2. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Unknown](https://www.blogger.com/profile/12306202569688675085)[26 June 2013 at 21:34](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1372278895488#c238049692771756756)
First of all excellent article! In the shader that creates the ghosts the MAX_GHOSTS and texelSize are not used. Is something missing from those?
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/238049692771756756)
[Replies](javascript:;)
    1. ![](https://2.bp.blogspot.com/-8Km-B9vQsq8/UOyAKLcDQOI/AAAAAAAAAWE/tP3DcVRo1BY/s35/youtube.jpg)
[John Chapman](https://www.blogger.com/profile/00717956687320127486)[26 June 2013 at 22:14](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1372281255922#c1703352050641060622)
texelSize is used in the chromatic distortion further down, but you're right about MAX_GHOSTS, I've removed it.
[Delete](https://www.blogger.com/comment/delete/1326576410402178223/1703352050641060622)
[Replies](javascript:;)
[Reply](javascript:;)
[Reply](javascript:;)
  3. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Beclamide](https://www.blogger.com/profile/00741297712223325975)[2 August 2013 at 13:44](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1375447499160#c6025072065683043298)
I'd just like to say this is a fantastic blog. All your posts are very interesting and informative. Please keep it up!
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/6025072065683043298)
[Replies](javascript:;)
[Reply](javascript:;)
  4. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgR7cblOFfqjcEIYmcQ8S_ICqDgJSyN50__ltrQhz_1Adt_DWNCE1kOx15XYY8_7lqFkkVKLfVi6nQfqCvV2fzPDHnb4FJIYA2zIgOlaX6tZdjhNQ019-T4OYxKWRiRgVI/s45-c/IMG_3961.JPG)
[Jerome Etienne](https://www.blogger.com/profile/17015325344733065720)[26 August 2013 at 10:04](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1377507882305#c4379743694250476549)
for those interested, i did a three.js implementation for webgl  
  
https://github.com/jeromeetienne/threex.sslensflare
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/4379743694250476549)
[Replies](javascript:;)
[Reply](javascript:;)
  5. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Unknown](https://www.blogger.com/profile/03482428066660307661)[2 September 2013 at 23:40](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1378161644185#c6501177208858582267)
This comment has been removed by the author.
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/6501177208858582267)
[Replies](javascript:;)
[Reply](javascript:;)
  6. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Unknown](https://www.blogger.com/profile/10858820150582738946)[10 March 2014 at 22:50](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1394491804854#c4941951473952428204)
Awesome stuff, I need this for Nuke Pleasse!!!!
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/4941951473952428204)
[Replies](javascript:;)
[Reply](javascript:;)
  7. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Slayer](https://www.blogger.com/profile/06679035430540617992)[23 May 2014 at 03:11](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1400811089691#c6479547379658484900)
Is there any other way to apply radial color to the ghost and the halos? 1D texture doesn't seem to be working for me. Great tutorial btw! Thanks for sharing! 
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/6479547379658484900)
[Replies](javascript:;)
[Reply](javascript:;)
  8. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Unknown](https://www.blogger.com/profile/03506277116984125806)[25 November 2014 at 08:48](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1416905327484#c4819992107502854191)
Hi John! Amazing tutorial :)  
  
How do you prevent just about any little white spot - like specular spots - to cast a flare?  
In your video you have teapot with lots of strong specular spots, yet they don't cast flares.  
  
Great content anyway!
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/4819992107502854191)
[Replies](javascript:;)
[Reply](javascript:;)
  9. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Jr. Williams](https://www.blogger.com/profile/15627387829300054935)[16 April 2016 at 08:42](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1460792573829#c7635435482908656362)
How can I avoid lens flare from head on lights?  
[photography](http://www.lensbender.net/)
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/7635435482908656362)
[Replies](javascript:;)
[Reply](javascript:;)
  10. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Jr. Williams](https://www.blogger.com/profile/15627387829300054935)[16 May 2016 at 15:47](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1463410061619#c1961247714600085989)
Hello, U write some extraordinarily attractive blogs. I always check back here frequently to see if you have updated  
[hawaii aerial photography](https://www.gokenji.com/gallery/)
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/1961247714600085989)
[Replies](javascript:;)
[Reply](javascript:;)
  11. ![](https://resources.blogblog.com/img/blank.gif)
Anonymous[17 July 2016 at 07:08](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1468735680420#c6456684956086804284)
I wasn't quite able to reproduce the full effect, but I was able to convert it to a "glare" effect in minecraft. Only around 70 lines and is very light on my GPU. Here is a screenshot.  
http://imgur.com/ua2XuZl  
One good part about it is that its not only limited to the sun/moon, It appears on bright objects (usually would take messing with lightmaps). Thanks for making this.  

[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/6456684956086804284)
[Replies](javascript:;)
    1. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Unknown](https://www.blogger.com/profile/07376235707258876913)[19 October 2019 at 03:37](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1571452622658#c3103329801339549555)
Can I get a look at your code I might be able to fix it
[Delete](https://www.blogger.com/comment/delete/1326576410402178223/3103329801339549555)
[Replies](javascript:;)
[Reply](javascript:;)
[Reply](javascript:;)
  12. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Fatih Furkan Aydemir](https://www.blogger.com/profile/14398849000753476026)[12 August 2017 at 10:59](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1502531979719#c2166877704765007797)
Thanks a lot for this excellent tutorial! I liked your camera movements so much.Can you give your camera code?
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/2166877704765007797)
[Replies](javascript:;)
[Reply](javascript:;)
  13. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Davinelulin](https://www.blogger.com/profile/01170403909636445225)[28 September 2018 at 09:49](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1538124569452#c8343625145736541006)
Super cool man! I made an implementation into Max/MSP/Jitter:   
https://www.youtube.com/watch?v=VeKkJ6Chduw
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/8343625145736541006)
[Replies](javascript:;)
[Reply](javascript:;)
  14. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Unknown](https://www.blogger.com/profile/07376235707258876913)[19 October 2019 at 03:35](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1571452526802#c3556528184260179678)
Can I get a look at your code I might be able to fix it
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/3556528184260179678)
[Replies](javascript:;)
    1. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Unknown](https://www.blogger.com/profile/07376235707258876913)[19 October 2019 at 03:36](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1571452611440#c6434135907815926382)
Why did it add it here
[Delete](https://www.blogger.com/comment/delete/1326576410402178223/6434135907815926382)
[Replies](javascript:;)
[Reply](javascript:;)
[Reply](javascript:;)
  15. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[michipeka](https://www.blogger.com/profile/01399076753749603341)[20 February 2021 at 15:45](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1613835940544#c7951814192304500116)
Thanks a lot for this, I just implemented the most important parts in my compositing software (Nuke) as a little tool, I cutomized the rest to make it a bit more personal and to my tastes.
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/7951814192304500116)
[Replies](javascript:;)
[Reply](javascript:;)
  16. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1-JcAZN0duFA5HuohaImSA5F5EOjBH5gZwGeGSt_oHSx0SRo18vKm-Ftz2wsAw9gCURftqEvMF1Qa00XbSn4Kf4st9JFiPhwYwxkLn_c574ab90AfrnLhBiSyFqpgXVQ/s45-c/images+%281%29.jpg)
[anekamovie.live and sukacrot.online](https://www.blogger.com/profile/17326573261023172276)[29 July 2021 at 19:12](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1627582362120#c160414251179889581)
NONTON BOKEP GRATIS GUYS  
TANPA PULSA DAN KUOTA > [situs bokep terbaru](https://sukacrot.online/)  
  
[bokep abg indo](https://sukacrot.online/category/bokep-indo/)  
[bokep jepang terbaru](https://sukacrot.online/category/bokep-jepang/)  
[situs bokep barat](https://sukacrot.online/category/bokep-barat/)  
[bokep skandal indo](https://sukacrot.online/category/bokep-asia/)  
[film bokep korea terbaru](https://sukacrot.online/category/bokep-korea/)  
[bokep viral indo](https://sukacrot.online/category/bokep-hentai/)  
  
NONTON FILM TERBARU, TERLENGKAP Dan TERPOPULER  
GRATIS JUGA !!! > [nonton film](https://anekamovie.live/)
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/160414251179889581)
[Replies](javascript:;)
[Reply](javascript:;)
  17. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgM4k4obY640GVSM7WEg5x6C7ZYgTosReeuMeHG01mku2xOuBKO87sLlrE4giQzdXormcMK8APSyiVyk9iExr0_1Z8iGSlla_JYdWAzMqg50yFUYJIAvh0-zocqwuk77g/s45-c/EUXmj5TXkAEKd1S.jpg)
[totosafedb.com](https://www.blogger.com/profile/07024381051844947071)[17 April 2022 at 21:01](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1650225665286#c8555301503274649784)
You were great and everyone received so [먹튀검증](https://www.totosafedb.com "먹튀검증") much from your experience and knowledge. 
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/8555301503274649784)
[Replies](javascript:;)
[Reply](javascript:;)
  18. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[Glebchansky](https://www.blogger.com/profile/01237823308776336572)[21 April 2022 at 18:23](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1650561782272#c5654614485256772443)
Take a look at my SolarSystem 3D project, there are many things implemented there, including lens flare  
https://github.com/GlebchanskyGit/SolarSystem-3D
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/5654614485256772443)
[Replies](javascript:;)
[Reply](javascript:;)
  19. ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipFP0qh7YrSYicn3DjI_UDcRZdTBcvLsrLJdZEPW9ho3junilvAEk4Lw5w9cXmA9J6csu5EC4sMsjUHjweUep7HDu9YIXw5ItS39ta1hx8zYtWaMXFAkAlqowKuS9Sxw/s45-c/ALL+UNIVESITY.jpg)
[Study live zone](https://www.blogger.com/profile/05212998891916974966)[11 January 2024 at 05:48](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1704952122552#c2656080595744234987)
Thanks a lot for giving us such a helpful information. You can also visit our website for [scdl project help  
](javascript:void\(0\);)
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/2656080595744234987)
[Replies](javascript:;)
[Reply](javascript:;)
  20. ![](https://www.blogger.com/img/blogger_logo_round_35.png)
[hennry](https://www.blogger.com/profile/08282184992624101585)[12 August 2025 at 11:20](https://john-chapman-graphics.blogspot.com/2013/02/pseudo-lens-flare.html?showComment=1754994042891#c4271772035868881454)
Your blog is friendly and warm.An [MBA Application Essay](https://www.mbaassignmentexperts.com/mba-application-essay) is a core component of your business school application, serving as your primary opportunity to showcase your personality, motivations, and potential beyond the quantitative data (like GMAT/GRE scores and GPA). Unlike a resume which lists your achievements, the essay allows you to tell the story behind those achievements, articulate your unique perspective, and explain why you are a strong fit for a particular MBA program. 
[Reply](javascript:;)[Delete](https://www.blogger.com/comment/delete/1326576410402178223/4271772035868881454)
[Replies](javascript:;)
[Reply](javascript:;)


[Add comment](javascript:;)
Load more...
[](https://www.blogger.com/comment/frame/1326576410402178223?po=6595424090675074632&hl=en-GB&saa=85391&origin=https%3A%2F%2Fjohn-chapman-graphics.blogspot.com&blogspotRpcToken=786554)
[Older Post](https://john-chapman-graphics.blogspot.com/2013/01/per-object-motion-blur.html "Older Post") [Home](https://john-chapman-graphics.blogspot.com/)
Subscribe to: [Post Comments (Atom)](https://john-chapman-graphics.blogspot.com/feeds/6595424090675074632/comments/default)
## Archive
  * [February 2013](https://john-chapman-graphics.blogspot.com/2013/02/) (1) 
  * [January 2013](https://john-chapman-graphics.blogspot.com/2013/01/) (6) 

  
| 
## About Me
[![My photo](https://2.bp.blogspot.com/-KNubJO_BvTI/UOx_j3AofqI/AAAAAAAAAVg/Pg2ILxwnOsg/s80/youtube.jpg)](https://www.blogger.com/profile/00717956687320127486) 

[ John Chapman ](https://www.blogger.com/profile/00717956687320127486) 
    contact@john-chapman.net [View my complete profile](https://www.blogger.com/profile/00717956687320127486)  |   |  
| --- | --- |  
## Subscribe To
![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif) ![](https://resources.blogblog.com/img/icon_feed12.png) Posts 
[ ![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png) ](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fjohn-chapman-graphics.blogspot.com%2Ffeeds%2Fposts%2Fdefault) [ ![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png) ](https://add.my.yahoo.com/content?url=https%3A%2F%2Fjohn-chapman-graphics.blogspot.com%2Ffeeds%2Fposts%2Fdefault) [ ![](https://resources.blogblog.com/img/icon_feed12.png) Atom ](https://john-chapman-graphics.blogspot.com/feeds/posts/default)
![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif) ![](https://resources.blogblog.com/img/icon_feed12.png) Posts 
![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif) ![](https://resources.blogblog.com/img/icon_feed12.png) Comments 
[ ![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png) ](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fjohn-chapman-graphics.blogspot.com%2Ffeeds%2F6595424090675074632%2Fcomments%2Fdefault) [ ![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png) ](https://add.my.yahoo.com/content?url=https%3A%2F%2Fjohn-chapman-graphics.blogspot.com%2Ffeeds%2F6595424090675074632%2Fcomments%2Fdefault) [ ![](https://resources.blogblog.com/img/icon_feed12.png) Atom ](https://john-chapman-graphics.blogspot.com/feeds/6595424090675074632/comments/default)
![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif) ![](https://resources.blogblog.com/img/icon_feed12.png) Comments   
|   |   |  
| --- | --- |  
Theme images by [Ollustrator](http://www.istockphoto.com/googleimages.php?id=9505737&platform=blogger&langregion=en_GB). Powered by [Blogger](https://www.blogger.com). 

