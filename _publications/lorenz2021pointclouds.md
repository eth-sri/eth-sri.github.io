---
ref: lorenz2021pointclouds
title: Robustness Certification for Point Cloud Models
authors: Tobias Lorenz, Anian Ruoss, Mislav Balunovic, Gagandeep Singh, Martin Vechev
year: 2021
month: 10
venue: ICCV
projects: safeai
awards:
bibtex: '@inproceedings{lorenz2021pointclouds,
    title = {Robustness Certification for Point Cloud Models},
    author = {Lorenz, Tobias and Ruoss, Anian and Balunovic, Mislav and Singh, Gagandeep and Vechev, Martin},
	booktitle = {2021 {IEEE/CVF} International Conference on Computer Vision, {ICCV} 2021},
    year = {2021},
    url = {https://arxiv.org/abs/2103.16652}
}'
paper: https://arxiv.org/abs/2103.16652
talk: 
slides:
---

The use of deep 3D point cloud models in safety-critical applications, such as autonomous driving, dictates the need to certify the robustness of these models to semantic transformations. This is technically challenging as it requires a scalable verifier tailored to point cloud models that handles a wide range of semantic 3D transformations. In this work, we address this challenge and introduce 3DCertify, the first verifier able to certify robustness of point cloud models. 3DCertify is based on two key insights: (i) a generic relaxation based on first-order Taylor approximations, applicable to any differentiable transformation, and (ii) a precise relaxation for global feature pooling, which is more complex than pointwise activations (e.g., ReLU or sigmoid) but commonly employed in point cloud models. We demonstrate the effectiveness of 3DCertify by performing an extensive evaluation on a wide range of 3D transformations (e.g., rotation, twisting) for both classification and part segmentation tasks. For example, we can certify robustness against rotations by ±60∘ for 95.7% of point clouds, and our max pool relaxation increases certification by up to 15.6%.
