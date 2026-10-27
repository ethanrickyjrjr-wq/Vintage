### ObjectDrop: Bootstrapping Counterfactuals for Photorealistic Object Removal and Insertion
Daniel Winter1,2 Matan Cohen1 Shlomi Fruchter1 Yael Pritch1 Alex Rav‑Acha1 Yedid Hoshen1,2
1Google Research 2The Hebrew University of Jerusalem
ECCV 2024
[ PDF ](https://arxiv.org/pdf/2403.18818.pdf)[ Arxiv ](https://arxiv.org/abs/2403.18818)[ New: ObjectMate ](https://object-mate.com)
## ABSTRACT
Diffusion models have revolutionized image editing but often generate images that violate physical laws, particularly the effects of objects on the scene, e.g., occlusions, shadows, and reflections. By analyzing the limitations of self-supervised approaches, we propose a practical solution centered on a "counterfactual" dataset. Our method involves capturing a scene before and after removing a single object, while minimizing other changes. By fine-tuning a diffusion model on this dataset, we are able to not only remove objects but also their effects on the scene. However, we find that applying this approach for photorealistic object insertion requires an impractically large dataset. To tackle this challenge, we propose bootstrap supervision; leveraging our object removal model trained on a small counterfactual dataset, we synthetically expand this dataset considerably. Our approach significantly outperforms prior methods in photorealistic object removal and insertion, particularly at modeling the effects of objects on the scene.
## OBJECT REMOVAL
Our object removal model effectively eliminates objects and their effects on the scene from images. Despite being trained on a relatively small counterfactual dataset captured in controlled environments, the model demonstrates remarkable generalization to diverse scenarios, seamlessly removing large objects.
Click on any image to see results
  * ![](https://objectdrop.github.io/assets/removal_images/inputs/img1.jpg)![](https://objectdrop.github.io/assets/removal_images/masks/img1.jpg)![](https://objectdrop.github.io/assets/removal_images/results/img1.jpg)
  * ![](https://objectdrop.github.io/assets/removal_images/inputs/img2.jpg)![](https://objectdrop.github.io/assets/removal_images/masks/img2.jpg)![](https://objectdrop.github.io/assets/removal_images/results/img2.jpg)
  * ![](https://objectdrop.github.io/assets/removal_images/inputs/img5.jpg)![](https://objectdrop.github.io/assets/removal_images/masks/img5.jpg)![](https://objectdrop.github.io/assets/removal_images/results/img5.jpg)
  * ![](https://objectdrop.github.io/assets/removal_images/inputs/img7.jpg)![](https://objectdrop.github.io/assets/removal_images/masks/img7.jpg)![](https://objectdrop.github.io/assets/removal_images/results/img7.jpg)
  * ![](https://objectdrop.github.io/assets/removal_images/inputs/img8.jpg)![](https://objectdrop.github.io/assets/removal_images/masks/img8.jpg)![](https://objectdrop.github.io/assets/removal_images/results/img8.jpg)
  * ![](https://objectdrop.github.io/assets/removal_images/inputs/img4.jpg)![](https://objectdrop.github.io/assets/removal_images/masks/img4.jpg)![](https://objectdrop.github.io/assets/removal_images/results/img4.jpg)
  * ![](https://objectdrop.github.io/assets/removal_images/inputs/img6.jpg)![](https://objectdrop.github.io/assets/removal_images/masks/img6.jpg)![](https://objectdrop.github.io/assets/removal_images/results/img6.jpg)
  * ![](https://objectdrop.github.io/assets/removal_images/inputs/img3.jpg)![](https://objectdrop.github.io/assets/removal_images/masks/img3.jpg)![](https://objectdrop.github.io/assets/removal_images/results/img3.jpg)


## APPROACH
We collect a counterfactual dataset consisting of photos of scenes before and after removing an object, while keeping everything else fixed. We used this dataset to finetune a diffusion model to remove an object and all its effects from the scene. For the task of object insertion, we bootstrap bigger dataset by removing selected objects from a large unsupervised image dataset, resulting in a vast, synthetic counterfactual dataset. Training on this synthetic dataset and then fine tuning on a smaller, original, supervised dataset yields a high quality object insertion model.
![](https://objectdrop.github.io/assets/overview.png)
## OBJECT INSERTION
By training first on a large synthetic dataset created with the object removal model, and then on a high-quality dataset, our object insertion model can accurately model how an object affects its environment, achieving realistic results.
Click on any image to see results  
|  ![](https://objectdrop.github.io/assets/object_insertion/target/img1.jpg)![](https://objectdrop.github.io/assets/object_insertion/target/img1.jpg)![](https://objectdrop.github.io/assets/object_insertion/result/img1.jpg) ![](https://objectdrop.github.io/assets/object_insertion/target/img2.jpg)![](https://objectdrop.github.io/assets/object_insertion/target/img2.jpg)![](https://objectdrop.github.io/assets/object_insertion/result/img2.jpg) ![](https://objectdrop.github.io/assets/object_insertion/target/img3.jpg)![](https://objectdrop.github.io/assets/object_insertion/target/img3.jpg)![](https://objectdrop.github.io/assets/object_insertion/result/img3.jpg) ![](https://objectdrop.github.io/assets/object_insertion/target/img4.jpg)![](https://objectdrop.github.io/assets/object_insertion/target/img4.jpg)![](https://objectdrop.github.io/assets/object_insertion/result/img4.jpg)  |  
| --- |  
|  ![](https://objectdrop.github.io/assets/object_insertion/references/img1.jpg) ![](https://objectdrop.github.io/assets/object_insertion/references/img2.jpg) ![](https://objectdrop.github.io/assets/object_insertion/references/img3.jpg) ![](https://objectdrop.github.io/assets/object_insertion/references/img4.jpg)  |  
## OBJECT MOVING
Utilizing both our object removal and insertion models, we can seamlessly move objects within an image. This involves removing them from their original position and re-inserting them elsewhere, resulting in realistic transformations.  
|  ![](https://objectdrop.github.io/assets/object_moving/original/img1.jpg)![](https://objectdrop.github.io/assets/object_moving/arrow/img1.jpg)![](https://objectdrop.github.io/assets/object_moving/result/img1.jpg) ![](https://objectdrop.github.io/assets/object_moving/original/img6.jpg)![](https://objectdrop.github.io/assets/object_moving/arrow/img6.jpg)![](https://objectdrop.github.io/assets/object_moving/result/img6.jpg)  |  ![](https://objectdrop.github.io/assets/object_moving/original/img4.jpg)![](https://objectdrop.github.io/assets/object_moving/arrow/img4.jpg)![](https://objectdrop.github.io/assets/object_moving/result/img4.jpg) ![](https://objectdrop.github.io/assets/object_moving/original/img5.jpg)![](https://objectdrop.github.io/assets/object_moving/arrow/img5.jpg)![](https://objectdrop.github.io/assets/object_moving/result/img5.jpg)  |  
| --- | --- |  
|  ![](https://objectdrop.github.io/assets/object_moving/original/img2.jpg)![](https://objectdrop.github.io/assets/object_moving/arrow/img2.jpg)![](https://objectdrop.github.io/assets/object_moving/result/img2.jpg) ![](https://objectdrop.github.io/assets/object_moving/original/img3.jpg)![](https://objectdrop.github.io/assets/object_moving/arrow/img3.jpg)![](https://objectdrop.github.io/assets/object_moving/result/img3.jpg)  |  
Click on any image to see results
## BibTex
@misc{winter2024objectdrop, title={ObjectDrop: Bootstrapping Counterfactuals for Photorealistic Object Removal and Insertion}, author={Daniel Winter and Matan Cohen and Shlomi Fruchter and Yael Pritch and Alex Rav-Acha and Yedid Hoshen}, year={2024}, eprint={2403.18818}, archivePrefix={arXiv}, primaryClass={cs.CV} }
## ACKNOWLEDGMENT
We would like to thank to Gitartha Goswami, Soumyadip Ghosh, Reggie Ballesteros, Srimon Chatterjee, Michael Milne and James Adamson for providing the photographs that made this project possible. We thank Yaron Brodsky, Dana Berman, Amir Hertz, Moab Arar, and Oren Katzir for their invaluable feedback and discussions. We also appreciate the insights provided by Dani Lischinski and Daniel Cohen-Or, which helped improve this work.
We thank owners of images on this site (link for attributions) for sharing their valuable assets.

