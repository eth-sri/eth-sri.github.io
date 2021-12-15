---
ref: mirman2021impossibility
title: "The Fundamental Limits of Interval Arithmetic for Neural Networks"
authors: Matthew Mirman, Maximilian Baader, Martin Vechev
year: 2021
month: 12
venue: arXiv
projects: safeai
bibtex: '@misc{mirman2021impossibility,
  title={The Fundamental Limits of Interval Arithmetic for Neural Networks},
  author={Matthew Mirman, Maximilian Baader, Martin Vechev},
  eprint={2112.05235}, 
  archivePrefix={arXiv}, primaryClass={cs.LG},
  year={2021}}'
paper: https://files.sri.inf.ethz.ch/website/papers/mirman2021fundamental.pdf
image: assets/images/mirman2021impossibility.png
---


Interval analysis (or interval bound propagation, IBP) is a popular technique for verifying and training provably robust deep neural networks, a fundamental challenge in the area of reliable machine learning. However, despite substantial efforts, progress on addressing this key challenge has stagnated, calling into question whether interval arithmetic is a viable path forward.

In this paper we present two fundamental results on the limitations of interval arithmetic for analyzing neural networks. Our main impossibility theorem states that for any neural network classifying just three points, there is a valid specification over these points that interval analysis can not prove. Further, in the restricted case of one-hidden-layer neural networks we show a stronger impossibility result: given any radius $\alpha < 1$, there is a set of $O(\alpha^{-1})$ points with robust radius $\alpha$, separated by distance $2$, that no one-hidden-layer network can be proven to classify robustly via interval analysis.
