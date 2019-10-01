---
ref: baader2019universal
title: "Universal Approximation with Certified Networks"
authors: Maximilian Baader, Matthew Mirman, Martin Vechev
year: 2019
month: 9
venue: arXiv
projects: safeai
bibtex: '@inproceedings{baader2019universal,
  title={Universal Approximation with Certified Networks},
  author={Maximilian Baader, Matthew Mirman, Martin Vechev},
  journal={arXiv preprint arXiv:1909.13846},
  year={2019}}'
paper: https://arxiv.org/abs/1909.13846
slides:
image: assets/images/baader2019universal.jpg
talk: 
---

Training neural networks to be certifiably robust is a powerful defense against adversarial attacks. However, while promising, state-of-the-art results with certified training are far from satisfactory. Currently, it is very difficult to train a neural network that is both accurate and certified on realistic datasets and specifications (e.g., robustness). Given this difficulty, a pressing existential question is: given a dataset and a specification, is there a network that is both certified and accurate with respect to these? While the evidence suggests "no", we prove that for realistic datasets and specifications, such a network does exist and its certification can be established by propagating lower and upper bounds of each neuron through the network (interval analysis) - the most relaxed yet computationally efficient convex relaxation. Our result can be seen as a Universal Approximation Theorem for interval-certified ReLU networks. To the best of our knowledge, this is the first work to prove the existence of accurate, interval-certified networks. 

