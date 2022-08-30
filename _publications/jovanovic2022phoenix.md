---
ref: jovanovic2022phoenix
title: Private and Reliable Neural Network Inference
authors: Nikola Jovanović, Marc Fischer, Samuel Steffen, Martin Vechev
year: 2022
month: 11
venue: ACM CCS
projects: safeai
awards:
bibtex: '@inproceedings{jovanovic2022phoenix,
    author = {Jovanović, Nikola and Fischer, Marc and Steffen, Samuel Vechev, Martin},
    title = {Private and Reliable Neural Network Inference},
    year = {2022},
    publisher = {Association for Computing Machinery},
    booktitle = {Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security},
    location = {Los Angeles, U.S.A.},
    series = {CCS ’22}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/ccs22-phoenix.pdf
code: https://github.com/eth-sri/phoenix
---

Reliable neural networks (NNs) provide important inference-time reliability guarantees such as fairness and robustness. Complementarily, privacy-preserving NN inference protects the privacy of client data. So far these two emerging areas have been largely disconnected, yet their combination will be increasingly important.

In this work, we present the first system which enables privacy-preserving inference on reliable NNs. Our key idea is to design efficient fully homomorphic encryption (FHE) counterparts for the core algorithmic building blocks of randomized smoothing, a state-of-the-art technique for obtaining reliable models. The lack of required control flow in FHE makes this a demanding task, as naïve solutions lead to unacceptable runtime.

We employ these building blocks to enable privacy-preserving NN inference with robustness and fairness guarantees in a system called Phoenix. Experimentally, we demonstrate that Phoenix achieves its goals without incurring prohibitive latencies.

To our knowledge, this is the first work which bridges the areas of client data privacy and reliability guarantees for NNs.
