---
ref: balauca2024gsmooth
title: "Overcoming the Paradox of Certified Training with Gaussian Smoothing"
authors: Stefan Balauca, Mark Niklas Müller, Yuhao Mao, Maximilian Baader, Marc Fischer, Martin Vechev
year: 2024
month: 03
venue: arXiv
# awards: Spotlight
projects: safeai
bibtex: '@article{
			balauca2024gsmooth,  
			title={Overcoming the Paradox of Certified Training with Gaussian Smoothing},  
			author={Stefan Balauca and Mark Niklas M{\"{u}}ller and Yuhao Mao and Maximilian Baader and Marc Fischer and Martin T. Vechev},  
		    journal={arXiv preprint arXiv:2403.07095},
		}'
paper: https://arxiv.org/abs/2403.07095
# code: https://github.com/eth-sri/sabr
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
image: assets/images/gsmooth.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Training neural networks with high certified accuracy against adversarial examples remains an open problem despite significant efforts. While certification methods can effectively leverage tight convex relaxations for bound computation, in training, these methods perform worse than looser relaxations. Prior work hypothesized that this is caused by the discontinuity and perturbation sensitivity of the loss surface induced by these tighter relaxations. In this work, we show theoretically that Gaussian Loss Smoothing can alleviate both of these issues. We confirm this empirically by proposing a certified training method combining PGPE, an algorithm computing gradients of a smoothed loss, with different convex relaxations. When using this training method, we observe that tighter bounds indeed lead to strictly better networks that can outperform state-of-the-art methods on the same network. While scaling PGPE-based training remains challenging due to high computational cost, our results clearly demonstrate the promise of Gaussian Loss Smoothing for training certifiably robust neural networks.