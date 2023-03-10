---
ref: mueller2023certified
title: "Certified Training: Small Boxes are All You Need"
authors: Mark Niklas Müller*, Franziska Eckert*, Marc Fischer, Martin Vechev
year: 2023
month: 05
venue: ICLR
projects: safeai
bibtex: '@inproceedings{
			mueller2023certified,  
			title={Certified Training: Small Boxes are All You Need},  
			author={Mark Niklas M{\"{u}}ller and Franziska Eckert and Marc Fischer and Martin T. Vechev},  
			booktitle={The Eleventh International Conference on Learning Representations },  
			year={2023},  
			url={https://openreview.net/forum?id=7oFuxtJtUMH}
		}'
paper: https://openreview.net/forum?id=7oFuxtJtUMH
#slides: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
image: assets/images/SABR.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

To obtain, deterministic guarantees of adversarial robustness, specialized training methods are used. We propose, SABR, a novel such certified training method, based on the key insight that propagating interval bounds for a small but carefully selected subset of the adversarial input region is sufficient to approximate the worst-case loss over the whole region while significantly reducing approximation errors. We show in an extensive empirical evaluation that SABR outperforms existing certified defenses in terms of both standard and certifiable accuracies across perturbation magnitudes and datasets, pointing to a new class of certified training methods promising to alleviate the robustness-accuracy trade-off.

