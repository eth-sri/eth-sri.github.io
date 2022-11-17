---
ref: mueller2022certified
title: "Certified Training: Small Boxes are All You Need"
authors: Mark Niklas Müller*, Franziska Eckert*, Marc Fischer, Martin Vechev
year: 2022
month: 12
venue: TSRML@NeurIPS
projects: safeai
bibtex: '@article{mueller2022certified,
	author    = {Mark Niklas M{\"{u}}ller and Franziska Eckert and Marc Fischer and Martin T. Vechev},
	title     = {Certified Training: Small Boxes are All You Need},
	journal   = {CoRR},
	year      = {2022},
	doi       = {10.48550/arXiv.2210.04871},
	}'
paper: https://arxiv.org/abs/2210.04871
#slides: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
image: assets/images/SABR.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

We propose the novel certified training method, SABR, which outperforms existing methods across perturbation magnitudes on MNIST, CIFAR-10, and TinyImageNet, in terms of both standard and certifiable accuracies. The key insight behind SABR is that propagating interval bounds for a small but carefully selected subset of the adversarial input region is sufficient to approximate the worst-case loss over the whole region while significantly reducing approximation errors. SABR does not only establish a new state-of-the-art in all commonly used benchmarks but more importantly, points to a new class of certified training methods promising to overcome the robustness-accuracy trade-off.

