---
ref: sprecher2021shared
title: Shared Certificates for Neural Network Verification 
authors: Christian Sprecher, Marc Fischer, Dimitar I. Dimitrov, Gagandeep Singh, Martin Vechev
year: 2021
month: 9
venue: arXiv 
projects: safeai
awards:
paper: https://arxiv.org/pdf/2109.00542.pdf 
---

Existing neural network verifiers compute a proof that each input is handled correctly under a given perturbation by propagating a convex set of reachable values at each layer. This process is repeated independently for each input (e.g., image) and perturbation (e.g., rotation), leading to an expensive overall proof effort when handling an entire dataset. In this work we introduce a new method for reducing this verification cost based on the key insight that convex sets obtained at intermediate layers can overlap across different inputs and perturbations. Leveraging this insight, we introduce the general concept of shared certificates, enabling proof effort reuse across multiple inputs and driving down overall verification costs. We validate our insight via an extensive experimental evaluation and demonstrate the effectiveness of shared certificates on a range of datasets and attack specifications including geometric, patch and ℓ<sub>∞</sub> input perturbations. 
