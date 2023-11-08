---
ref: baader2023expressivity
title: "Expressivity of ReLU-Networks under Convex Relaxations"
authors: Maximilian Baader*, Mark Niklas Müller*, Yuhao Mao, Martin Vechev
year: 2023
month: 11
venue: arXiv
projects: safeai
bibtex: '@misc{
			BaaderMMV2023,  
			title={Expressivity of ReLU-Networks under Convex Relaxations},  
			author={Maximilian Baader and Mark Niklas M{\"{u}}ller and Yuhao Mao and Martin Vechev},  
      		eprint={2311.04015},
			archivePrefix={arXiv},
			year={2023},
		}'
paper: https://arxiv.org/abs/2311.04015
# code: https://github.com/eth-sri/sabr
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
image: assets/images/Expressivity_img.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Convex relaxations are a key component of training and certifying provably safe neural networks. However, despite substantial progress, a wide and poorly understood accuracy gap to standard networks remains, raising the question of whether this is due to fundamental limitations of convex relaxations. Initial work investigating this question focused on the simple and widely used IBP relaxation. It revealed that some univariate, convex, continuous piecewise linear (CPWL) functions cannot be encoded by any ReLU network such that its IBP-analysis is precise. To explore whether this limitation is shared by more advanced convex relaxations, we conduct the first in-depth study on the expressive power of ReLU networks across all commonly used convex relaxations. We show that: (i) more advanced relaxations allow a larger class of univariate functions to be expressed as precisely analyzable ReLU networks, (ii) more precise relaxations can allow exponentially larger solution spaces of ReLU networks encoding the same functions, and (iii) even using the most precise single-neuron relaxations, it is impossible to construct precisely analyzable ReLU networks that express multivariate, convex, monotone CPWL functions.
