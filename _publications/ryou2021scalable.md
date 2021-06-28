---
ref: ryou2021scalable
title: Scalable Polyhedral Verification of Recurrent Neural Networks
authors: Wonryong Ryou, Jiayu Chen, Mislav Balunovic, Gagandeep Singh, Andrei Dan, Martin Vechev
year: 2021
month: 07
venue: CAV
projects: safeai
awards:
bibtex: '@inproceedings{ryou2021scalable,
  title={Scalable Polyhedral Verification of Recurrent Neural Networks},
  author={Wonryong Ryou and Jiayu Chen and Mislav Balunovic and Gagandeep Singh and Andrei Dan and Martin Vechev},
  booktitle={International Conference on Computer Aided Verification},
  year={2021},
  organization={Springer}}'
paper: https://arxiv.org/abs/2005.13300
---

We present a scalable and precise verifier for recurrent neural networks, called Prover based on two novel ideas: (i) a method to compute a set of polyhedral abstractions for the non-convex and nonlinear recurrent update functions by combining sampling, optimization, and Fermat's theorem, and (ii) a gradient descent based algorithm for abstraction refinement guided by the certification problem that combines multiple abstractions for each neuron. Using Prover, we present the first study of certifying a non-trivial use case of recurrent neural networks, namely speech classification. To achieve this, we additionally develop custom abstractions for the non-linear speech preprocessing pipeline. Our evaluation shows that Prover successfully verifies several challenging recurrent models in computer vision, speech, and motion sensor data classification beyond the reach of prior work. 