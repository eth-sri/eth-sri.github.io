---
ref: fischer2021shared
title: Shared Certificates for Neural Network Verification 
authors: Marc Fischer*, Christian Sprecher*, Dimitar I. Dimitrov, Gagandeep Singh, Martin Vechev
year: 2022
month: 8
venue: CAV 
projects: safeai
awards:
paper: https://arxiv.org/pdf/2109.00542.pdf 
code: https://github.com/eth-sri/proof-sharing
---

Existing neural network verifiers compute a proof that each input is handled correctly under a given perturbation by propagating a symbolic abstraction of reachable values at each layer. This process is repeated from scratch independently for each input (e.g., image) and perturbation (e.g., rotation), leading to an expensive overall proof effort when handling an entire dataset. In this work we introduce a new method for reducing this verification cost without losing precision based on a key insight that abstractions obtained at intermediate layers for different in- puts and perturbations can overlap or contain each other. Leveraging our insight, we introduce the general concept of shared certificates, enabling proof effort reuse across multiple inputs to reduce overall verification costs. We perform an extensive experimental evaluation to demonstrate the effectiveness of shared certificates in reducing the verification cost on a range of datasets and attack specifications on image classifiers including the popular patch and geometric perturbations.
