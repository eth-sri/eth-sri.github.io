---
ref: baader2019universal
title: "Universal Approximation with Certified Networks"
authors: Maximilian Baader, Matthew Mirman, Martin Vechev
year: 2020
month: 4
venue: ICLR
projects: safeai
bibtex: '@inproceedings{baader2020universal,
  title={Universal Approximation with Certified Networks},
  author={Maximilian Baader, Matthew Mirman, Martin Vechev},
  journal={ICLR},
  year={2020}}'
paper: https://files.sri.inf.ethz.ch/website/papers/iclr2020-universal.pdf
slides: https://files.sri.inf.ethz.ch/website/papers/iclr2020-slides.pdf
image: assets/images/baader2019universal2.jpg
talk: 
---

Training neural networks to be certifiably robust is critical to ensure their safety against adversarial attacks. However, it is currently very difficult to train a neural network that is both accurate and certifiably robust. In this work we take a step towards addressing this challenge. We prove that for every continuous function f, there exists a network n such that: (i) n approximates f arbitrarily close, and (ii) simple interval bound propagation of a region B through n yields a result that is arbitrarily close to the optimal output of f on B. Our result can be seen as a Universal Approximation Theorem for interval-certified ReLU networks. To the best of our knowledge, this is the first work to prove the existence of accurate, interval-certified networks.

