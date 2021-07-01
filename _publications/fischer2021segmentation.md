---
ref: fischer2021segmentation 
title: "Scalable Certified Segmentation via Randomized Smoothing"
authors: Marc Fischer, Maximilian Baader,  Martin Vechev
year: 2021
month: 07
venue: ICML
projects: safeai
awards:
bibtex: '@incollection{fischer2021scalable,
         title = {Scalable Certified Segmentation via Randomized Smoothing}, 
         author = { Fischer, Marc and Baader, Maximilian and Vechev, Martin},
         booktitle = {International Conference on Machine Learning (ICML)}, year = {2021} }'
paper: https://files.sri.inf.ethz.ch/website/papers/fischer2021segmentation.pdf
image: assets/images/fischer2021segmentation.png
---

We present a new certification method for image and point cloud segmentation based on randomized smoothing. The method leverages a novel scalable algorithm for prediction and certification that correctly accounts for multiple testing, necessary for ensuring statistical guarantees. The key to our approach is reliance on established multiple-testing correction mechanisms as well as the ability to abstain from classifying single pixels or points while still robustly segmenting the overall input. Our experimental evaluation on synthetic data and challenging datasets, such as Pascal Context, Cityscapes, and ShapeNet, shows that our algorithm can achieve, for the first time, competitive accuracy and certification guarantees on real-world segmentation tasks.
We provide an implementation at [this https URL](https://github.com/eth-sri/segmentation-smoothing).
