---
ref: mueller2021precise
title: "PRIMA: General and Precise Neural Network Certification via Scalable Convex Hull Approximations"
authors: Mark Niklas Müller*, Gleb Makarchuk*, Gagandeep Singh, Markus Püschel, Martin Vechev
year: 2022
month: 1
venue: POPL
projects: safeai
bibtex: '@misc{müller2021precise,
      title={PRIMA: Precise and General Neural Network Certification via Multi-Neuron Convex Relaxations}, 
      author={Mark Niklas Müller and Gleb Makarchuk and Gagandeep Singh and Markus Püschel and Martin Vechev},
      year={2021},
      eprint={2103.03638},
      archivePrefix={arXiv},
      primaryClass={cs.AI}}'
<!--blogpost: prima-->
paper: https://files.sri.inf.ethz.ch/website/papers/mueller2021precise.pdf
slides: https://files.sri.inf.ethz.ch/website/slides/POPL2022_prima.pdf
image: assets/images/SBLM_full.png
talk: https://www.youtube.com/watch?v=YUysJvxLrK8
---

Formal verification of neural networks is critical for their safe adoption in real-world applications. However, designing a precise and scalable verifier which can handle different activation functions, realistic network architectures and relevant specifications remains an open and difficult challenge.

In this paper, we take a major step forward in addressing this challenge and present a new verification framework, called PRIMA. PRIMA is both (i) general: it handles any non-linear activation function, and (ii) precise: it computes precise convex abstractions involving multiple neurons via novel convex hull approximation algorithms that leverage concepts from computational geometry. The algorithms have polynomial complexity, yield fewer constraints, and minimize precision loss.

We evaluate the effectiveness of PRIMA on a variety of challenging tasks from prior work. Our results show that PRIMA is significantly more precise than the state-of-the-art, verifying robustness to input perturbations for up to 20%, 30%, and 34% more images than existing work on ReLU-, Sigmoid-, and Tanh-based networks, respectively. Further, PRIMA enables, for the first time, the precise verification of a realistic neural network for autonomous driving within a few minutes.
