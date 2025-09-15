---
ref: balauca2024gsmooth
title: "Gaussian Loss Smoothing Enables Certified Training with Tight Convex Relaxations"
authors: Stefan Balauca, Mark Niklas Müller, Yuhao Mao, Maximilian Baader, Marc Fischer, Martin Vechev
year: 2025
month: 07
venue: TMLR
# awards: Spotlight
projects: safeai
bibtex: '@article{
			balauca2024gsmooth,  
			title={Gaussian Loss Smoothing Enables Certified Training with Tight Convex Relaxations},  
			author={Stefan Balauca and Mark Niklas M{\"{u}}ller and Yuhao Mao and Maximilian Baader and Marc Fischer and Martin T. Vechev},  
		    journal={Transactions on Machine Learning Research 2025/07},
		}'
paper: https://arxiv.org/abs/2403.07095
code: https://github.com/stefanrzv2000/GLS-Cert-Training
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
image: assets/images/gsmooth.png
talk: https://www.youtube.com/watch?v=BMBvFMU1ZeM
---

Training neural networks with high certified accuracy against adversarial examples remains an open challenge despite significant efforts. While certification methods can effectively leverage tight convex relaxations for bound computation, in training, these methods, perhaps surprisingly, can perform worse than looser relaxations. 
Prior works hypothesized that this phenomenon is caused by the discontinuity, non-smoothness, and perturbation sensitivity of the loss surface induced by tighter relaxations. In this work, we theoretically show that Gaussian Loss Smoothing (GLS) can alleviate these issues. We confirm this empirically by instantiating GLS with two variants: a zeroth-order optimization algorithm, called PGPE, which allows training with non-differentiable relaxations, and a first-order optimization algorithm, called RGS, which requires gradients of the relaxation but is much more efficient than PGPE. Extensive experiments show that when combined with tight relaxations, these methods surpass state-of-the-art methods when training on the same network architecture for many settings. Our results clearly demonstrate the promise of Gaussian Loss Smoothing for training certifiably robust neural networks and pave a path towards leveraging tighter relaxations for certified training.