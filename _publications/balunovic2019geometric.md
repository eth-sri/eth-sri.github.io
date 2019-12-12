---
ref: balunovic2019geometric
title: Certifying Geometric Robustness of Neural Networks
projects: safeai
authors: Mislav Balunovic, Maximilian Baader, Gagandeep Singh, Timon Gehr, Martin Vechev
year: 2019
month: 12
venue: NeurIPS
projects: safeai
paper: https://files.sri.inf.ethz.ch/website/papers/neurips19-deepg.pdf
slides: https://files.sri.inf.ethz.ch/website/papers/neurips19-deepg-poster.pdf
image: assets/images/balunovic2019geometric.png
bibtex: '@incollection{balunovic2019geometric,
  title = {Certifying Geometric Robustness of Neural Networks},
  author = {Balunovic, Mislav and Baader, Maximilian and Singh, Gagandeep and Gehr, Timon and Vechev, Martin},
  booktitle = {Advances in Neural Information Processing Systems 32},
  year = {2019}
}'
---

The use of neural networks in safety-critical computer vision systems calls for their
robustness certification against natural geometric transformations (e.g., rotation,
scaling). However, current certification methods target mostly norm-based pixel
perturbations and cannot certify robustness against geometric transformations. In
this work, we propose a new method to compute sound and asymptotically optimal
linear relaxations for any composition of transformations. Our method is based on
a novel combination of sampling and optimization. We implemented the method
in a system called DeepG and demonstrated that it certifies significantly more
complex geometric transformations than existing methods on both defended and
undefended networks while scaling to large architectures.
