---
ref: mueller2021precise
title: "Precise Multi-Neuron Abstractions for Neural Network Certification"
authors: Mark Niklas Müller, Gleb Makarchuk, Gagandeep Singh, Markus Püschel, Martin Vechev
year: 2021
month: 3
venue: arXiv 
projects: safeai
bibtex: '@misc{müller2021precise,
      title={Precise Multi-Neuron Abstractions for Neural Network Certification}, 
      author={Mark Niklas Müller and Gleb Makarchuk and Gagandeep Singh and Markus Püschel and Martin Vechev},
      year={2021},
      eprint={2103.03638},
      archivePrefix={arXiv},
      primaryClass={cs.AI}}'
paper: https://files.sri.inf.ethz.ch/website/papers/mueller2021precise.pdf
#slides: https://files.sri.inf.ethz.ch/website/slides/iclr2020-colt.pdf
#image: assets/images/colt.png
#talk: https://iclr.cc/virtual_2020/poster_SJxSDxrKDr.html
---

Formal verification of neural networks is critical for their safe adoption in real-world applications. However, designing a verifier which can handle realistic networks in a precise manner remains an open and difficult challenge.
In this paper, we take a major step in addressing this challenge and present a new framework, called PRIMA, that computes precise convex approximations of arbitrary non-linear activations. PRIMA is based on novel approximation algorithms that compute the convex hull of polytopes, leveraging concepts from computational geometry. The algorithms have polynomial complexity, yield fewer constraints, and minimize precision loss.
We evaluate the effectiveness of PRIMA on challenging neural networks with ReLU, Sigmoid, and Tanh activations. Our results show that PRIMA is significantly more precise than the state-of-the-art, verifying robustness for up to 16%, 30%, and 34% more images than prior work on ReLU-, Sigmoid-, and Tanh-based networks, respectively
