---
ref: peychev2022latent
title: "Latent Space Smoothing for Individually Fair Representations"
authors: Momchil Peychev, Anian Ruoss, Mislav Balunović, Maximilian Baader, Martin Vechev
year: 2022
month: 10
venue: ECCV
projects: safeai
paper: https://files.sri.inf.ethz.ch/website/papers/peychev2022latent.pdf
code: https://github.com/eth-sri/lassi
---

Fair representation learning transforms user data into a representation that ensures fairness and utility regardless of the downstream application. However, learning individually fair representations, i.e., guaranteeing that similar individuals are treated similarly, remains challenging in high-dimensional settings such as computer vision. In this work, we introduce LASSI, the first representation learning method for certifying individual fairness of high-dimensional data. Our key insight is to leverage recent advances in generative modeling to capture the set of similar individuals in the generative latent space. This enables us to learn individually fair representations that map similar individuals close together by using adversarial training to minimize the distance between their representations. Finally, we employ randomized smoothing to provably map similar individuals close together, in turn ensuring that local robustness verification of the downstream application results in end-to-end fairness certification. Our experimental evaluation on challenging real-world image data demonstrates that our method increases certified individual fairness by up to 90% without significantly affecting task utility.
