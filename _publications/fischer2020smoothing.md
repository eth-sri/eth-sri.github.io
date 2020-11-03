---
ref: fischer2020smoothing
title: Certified Defense to Image Transformations via Randomized Smoothing
authors: Marc Fischer, Maximilian Baader,  Martin Vechev
year: 2020
month: 12
venue: NeurIPS
projects: safeai
image: assets/images/fischer2020smoothing.png
awards:
bibtex: '@incollection{fischer2020transformationsmoothing,
    title = {Certified Defense to Image Transformations via Randomized Smoothing},
    author = { Fischer, Marc and Baader, Maximilian and Vechev, Martin},
	booktitle = {Advances in Neural Information Processing Systems 33},
    year = {2020}
}'
paper: https://arxiv.org/pdf/2002.12463.pdf
talk: 
slides: 
---

We extend randomized smoothing to cover parameterized transformations (e.g., rotations, translations) and certify robustness in the parameter space (e.g., rotation angle). This is particularly challenging as interpolation and rounding effects mean that image transformations do not compose, in turn preventing direct certification of the perturbed image (unlike certification with lp-norms). We address this challenge by introducing three different defenses, each with a different guarantee (heuristic, distributional and individual) stemming from the method used to bound the interpolation error. Importantly, in the individual case, we show how to efficiently compute the inverse of an image transformation, enabling us to provide individual guarantees in the online setting. We provide an implementation of all methods at [this https URL](https://github.com/eth-sri/transformation-smoothing). 
