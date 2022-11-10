---
ref: zeqiri2022efficient
title: "Efficient Robustness Verification of Neural Ordinary Differential Equations"
authors: Mustafa Zeqiri, Mark Niklas Müller, Marc Fischer, Martin Vechev
year: 2022
month: 12
venue: DLDE@NeurIPS
projects: safeai
bibtex: '@inproceedings{
	zeqiri2022efficient,
	title={Efficient Robustness Verification of Neural Ordinary Differential Equations},
	author={Mustafa Zeqiri and Mark Niklas Mueller and Marc Fischer and Martin Vechev},
	booktitle={The Symbiosis of Deep Learning and Differential Equations II},
	year={2022},
	url={https://openreview.net/forum?id=hC2_w2d2DY}
	}'
paper: https://openreview.net/forum?id=hC2_w2d2DY
#slides: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
#image: assets/images/SABR.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Neural Ordinary Differential Equations (NODEs) are a novel neural architecture, built around initial value problems with learned dynamics. Thought to be inherently more robust against adversarial perturbations, they were recently shown to be vulnerable to strong adversarial attacks, highlighting the need for formal guarantees. In this work, we tackle this challenge and propose GAINS, an analysis framework for NODEs based on three key ideas: (i) a novel class of ODE solvers, based on variable but discrete time steps, (ii) an efficient graph representation of solver trajectories, and (iii) a bound propagation algorithm operating on this graph representation. Together, these advances enable the efficient analysis and certified training of high-dimensional NODEs, which we demonstrate in an extensive evaluation on computer vision and time-series forecasting problems.

