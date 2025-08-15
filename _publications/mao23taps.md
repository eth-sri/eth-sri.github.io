---
ref: mao23taps
title: "Connecting Certified and Adversarial Training"
authors: Yuhao Mao, Mark Niklas Müller, Marc Fischer, Martin Vechev
year: 2023
month: 12
venue: NeuIPS
projects: safeai
bibtex: '@article{mao23taps,
			author       = {Yuhao Mao and
							Mark Niklas M{\"{u}}ller and
							Marc Fischer and
							Martin T. Vechev},
			title        = {{TAPS:} Connecting Certified and Adversarial Training},
			year         = {2023},
			doi          = {10.48550/arXiv.2305.04574},
			eprinttype    = {arXiv},
			eprint       = {2305.04574}}'
paper: https://arxiv.org/abs/2305.04574
code: https://github.com/eth-sri/taps
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
image: assets/images/taps.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Training certifiably robust neural networks remains a notoriously hard problem. 
While adversarial training optimizes under-approximations of the worst-case loss, which leads to insufficient regularization for certification, sound certified training methods, optimize loose over-approximations, leading to over-regularization and poor (standard) accuracy. 
In this work, we propose TAPS, an (unsound) certified training method that combines IBP and PGD training to optimize more precise, although not necessarily sound, worst-case loss approximations, reducing over-regularization and increasing certified and standard accuracies. 
Empirically, TAPS achieves a new state-of-the-art in many settings, e.g., reaching a certified accuracy of 22% on TinyImageNet for L-inf-perturbations with radius eps=1/255.


