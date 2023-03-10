---
ref: zeqiri2023efficient
title: "Efficient Certified Training and Robustness Verification of Neural ODEs"
authors: Mustafa Zeqiri, Mark Niklas Müller, Marc Fischer, Martin Vechev
year: 2023
month: 05
venue: ICLR
projects: safeai
bibtex: '@inproceedings{
			zeqiri2023efficient,
			title={Efficient Certified Training and Robustness Verification of Neural {ODE}s},
			author={Mustafa Zeqiri and Mark Niklas M{\"{u}}ller and Marc Fischer and Martin Vechev},
			booktitle={The Eleventh International Conference on Learning Representations },
			year={2023},
			url={https://openreview.net/forum?id=KyoVpYvWWnK}
		}'
paper: https://openreview.net/forum?id=hC2_w2d2DY
#slides: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
#image: assets/images/SABR.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Neural Ordinary Differential Equations (NODEs) are a novel neural architecture, built around initial value problems with learned dynamics which are solved during inference. Thought to be inherently more robust against adversarial perturbations, they were recently shown to be vulnerable to strong adversarial attacks, highlighting the need for formal guarantees.  However, despite significant progress in robustness verification for standard feed-forward architectures, the verification of high dimensional NODEs remains an open problem. In this work, we address this challenge and propose GAINS, an analysis framework for NODEs combining three key ideas: (i) a novel class of ODE solvers, based on variable but discrete time steps, (ii) an efficient graph representation of solver trajectories, and (iii) a novel abstraction algorithm operating on this graph representation. Together, these advances enable the efficient analysis and certified training of high-dimensional NODEs, by reducing the runtime from an intractable O(exp(d)+exp(T)) to O(d+T^2 \log^2T) in the dimensionality d and integration time T.  In an extensive evaluation on computer vision (MNIST and F-MNIST) and time-series forecasting (PHYSIO-NET) problems, we demonstrate the effectiveness of both our certified training and verification methods.

