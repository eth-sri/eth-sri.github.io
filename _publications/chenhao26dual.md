---
ref: chenhao2026dual
title: "Dual Randomized Smoothing: Beyond Global Noise Variance"
authors: Chenhao Sun, Yuhao Mao, Martin Vechev
year: 2026
month: 04
venue: ICLR
projects: safeai
bibtex: '@inproceedings{
			chenhao2026dual,
			title={Dual Randomized Smoothing: Beyond Global Noise Variance},
			author={Sun, Chenhao and Mao, Yuhao and Vechev, Martin},
			booktitle={The Fourteenth International Conference on Learning Representations},
			year={2026},
			url={https://openreview.net/forum?id=syvfsHSqm2}
			}'
paper: https://arxiv.org/abs/2512.01782
# code: https://github.com/eth-sri/acr-weakness
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
# image: assets/images/taps.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Randomized Smoothing (RS) is a prominent technique for certifying the robustness of neural networks against adversarial perturbations. With RS, achieving high accuracy at small radii requires a small noise variance, while achieving high accuracy at large radii requires a large noise variance. However, the global noise variance used in the standard RS formulation leads to a fundamental limitation: there exists no global noise variance that simultaneously achieves strong performance at both small and large radii. To break through the global variance limitation, we propose a dual RS framework which enables input-dependent noise variances. To achieve that, we first prove that RS remains valid with input-dependent noise variances, provided the variance is locally constant around each input. Building on this result, we introduce two components which form our dual RS framework: (i) a variance estimator first predicts an optimal noise variance for each input, (ii) this estimated variance is then used by a standard RS classifier. The variance estimator is independently smoothed via RS to ensure local constancy, enabling flexible design. We also introduce training strategies to iteratively optimize the two components involved in the framework. Extensive experiments on the CIFAR-10 dataset demonstrate that our dual RS method provides strong performance for both small and large radii—unattainable with global noise variance—while incurring only a 60% computational overhead at inference. Moreover, it consistently outperforms prior input-dependent noise approaches across most radii, with particularly large gains at radii 0.5, 0.75, and 1.0, achieving relative improvements of 19.2%, 24.2%, and 20.6%, respectively. On ImageNet, dual RS remains effective across all radii, with roughly 1.5x performance advantages at radii 0.5, 1.0 and 1.5. Additionally, the proposed dual RS framework naturally provides a routing perspective for certified robustness, improving the accuracy-robustness trade-off with off-the-shelf expert RS models.