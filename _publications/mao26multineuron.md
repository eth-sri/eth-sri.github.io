---
ref: mao26multineuron
title: "Expressiveness of Multi-Neuron Convex Relaxations in Neural Network Certification"
authors: Yuhao Mao*, Yani Zhang*, Martin Vechev
year: 2026
month: 05
venue: ICLR
projects: safeai
bibtex: '@inproceedings{mao26multineuron,
			author       = {Yuhao Mao and
						Yani Zhang and
						Martin T. Vechev},
			title        = {Expressiveness of Multi-Neuron Convex Relaxations in Neural Network Certification},
			year         = {2026},
			booktitle    = {The Fourteenth International Conference on Learning Representations}
            }'
paper: https://arxiv.org/abs/2410.06816
# code: 
# slides: 
#poster: 
# image: 
#talk: 
---

Neural network certification methods heavily rely on convex relaxations to provide robustness guarantees. However, these relaxations are often imprecise: even the most accurate single-neuron relaxation is incomplete for general ReLU networks, a limitation known as the *single-neuron convex barrier*. While multi-neuron relaxations have been heuristically applied to address this issue, two central questions arise: (i) whether they overcome the convex barrier, and if not, (ii) whether they offer theoretical capabilities beyond those of single-neuron relaxations.

In this work, we present the first rigorous analysis of the expressiveness of multi-neuron relaxations. Perhaps surprisingly, we show that they are inherently incomplete, even when allocated sufficient resources to capture finitely many neurons and layers optimally. This result extends the single-neuron barrier to a *universal convex barrier* for neural network certification. 
On the positive side, we show that completeness can be achieved by either (i) augmenting the network with a polynomial number of carefully designed ReLU neurons or (ii) partitioning the input domain into convex sub-polytopes, thereby distinguishing multi-neuron relaxations from single-neuron ones which are unable to realize the former and have worse partition complexity for the latter.
Our findings establish a foundation for multi-neuron relaxations and point to new directions for certified robustness, including training methods tailored to multi-neuron relaxations and verification methods with multi-neuron relaxations as the main subroutine.
