---
ref: mao24ibp
title: "Understanding Certified Training with Interval Bound Propagation"
authors: Yuhao Mao, Mark Niklas Müller, Marc Fischer, Martin Vechev
year: 2024
month: 05
venue: ICLR
projects: safeai
bibtex: '@inproceedings{mao23taps
			author       = {Yuhao Mao and
							Mark Niklas M{\"{u}}ller and
							Marc Fischer and
							Martin T. Vechev},
			title        = {Understanding Certified Training with Interval Bound Propagation},
			year         = {2024},
			booktitle    = {The Twelfth International Conference on Learning Representations}'
paper: https://arxiv.org/abs/2306.10426
# code: https://github.com/eth-sri/sabr
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
# image: assets/images/taps.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

As robustness verification methods are becoming more precise, training certifiably robust neural networks is becoming ever more relevant. To this end, certified training methods compute and then optimize an upper bound on the worst-case loss over a robustness specification. Curiously, training methods based on the imprecise interval bound propagation (IBP) consistently outperform those leveraging more precise bounding methods. Still, we lack an understanding of the mechanisms making IBP so successful.
In this work, we thoroughly investigate these mechanisms by leveraging a novel metric measuring the tightness of IBP bounds. We first show theoretically that, for deep linear models, tightness decreases with width and depth at initialization, but improves with IBP training, given sufficient network width. We, then, derive sufficient and necessary conditions on weight matrices for IBP bounds to become exact and demonstrate that these impose strong regularization, explaining the empirically observed trade-off between robustness and accuracy in certified training.
Our extensive experimental evaluation validates our theoretical predictions for ReLU networks, including that wider networks improve performance, yielding state-of-the-art results. Interestingly, we observe that while all IBP-based training methods lead to high tightness, this is neither sufficient nor necessary to achieve high certifiable robustness. This hints at the existence of new training methods that do not induce the strong regularization required for tight IBP bounds, leading to improved robustness and standard accuracy.


