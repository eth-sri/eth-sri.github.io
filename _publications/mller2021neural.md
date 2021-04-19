---
ref: mller2021neural
title:  "Scaling Polyhedral Neural Network Verification on GPUs"
projects: safeai
authors: Christoph Müller*, François Serre*, Gagandeep Singh, Markus Püschel, Martin Vechev
year: 2021
month: 04
talk: https://www.youtube.com/watch?v=rM95uwgFFVw
bibtex: '@InProceedings{gpupoly,
  author    = {Fran{\c c}ois Serre and Christoph M{\"u}ller and Gagandeep Singh and Markus P{\"u}schel and Martin Vechev},
  title     = {Scaling Polyhedral Neural Network Verification on {GPU}s},
  booktitle = {Proc. Machine Learning and Systems (MLSys)},
  year      = {2021}
}'
venue: MLSys
paper: https://files.sri.inf.ethz.ch/website/papers/mller2021neural.pdf
slides: 
---
Certifying the robustness of neural networks against adversarial attacks is critical to their reliable adoption in real-world systems including autonomous driving and medical diagnosis. Unfortunately, state-of-the-art verifiers either do not scale to larger networks or are too imprecise to prove robustness, which limits their practical adoption. In this work, we introduce GPUPoly, a scalable verifier that can prove the robustness of significantly larger deep neural networks than possible with prior work. The key insight behind GPUPoly is the design of custom, sound polyhedra algorithms for neural network verification on a GPU. Our algorithms leverage the available GPU parallelism and the inherent sparsity of the underlying verification task. GPUPoly scales to very large networks: for example, it can prove the robustness of a 1M neuron, 34-layer deep residual network in around 34.5 ms. We believe GPUPoly is a promising step towards the practical verification of large real-world networks.
