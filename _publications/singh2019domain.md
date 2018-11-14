---
ref: singh2019domain
title: An Abstract Domain for Certifying Neural Networks
authors: Gagandeep Singh, Timon Gehr, Markus Püschel, Martin Vechev
year: 2019
month: 01
venue: ACM POPL
projects: numerical-analysis
awards:
bibtex:
paper: https://files.sri.inf.ethz.ch/website/papers/DeepPoly.pdf
talk: 
slides: 
---

We present a novel method for scalable and precise certification of deep neural networks. The key technical insight behind our approach is a new abstract domain which combines floating point polyhedra with intervals and is equipped with abstract transformers specifically tailored to the setting of neural networks. Concretely, we introduce new transformers for affine transforms, the rectified linear unit (ReLU), sigmoid, tanh, and maxpool functions.

We implemented our method in a system called DeepPoly and evaluated it extensively on a range of datasets, neural architectures (including defended networks), and specifications. Our experimental results indicate that DeepPoly is more precise than prior work while scaling to large networks. We also show how to combine DeepPoly with abstraction refinement in order to prove, for the first time, robustness of the given input (e.g., an image) to complex perturbations such as rotations that employ linear interpolation.
