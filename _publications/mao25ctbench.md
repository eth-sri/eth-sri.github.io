---
ref: mao25ctbench
title: "CTBENCH: A Library and Benchmark for Certified Training"
authors: Yuhao Mao, Stefan Balauca, Martin Vechev
year: 2025
month: 05
venue: ICML
projects: safeai
bibtex: '@inproceedings{mao25ctbench
			author       = {Yuhao Mao and
							Stefan Balauca and
							Martin T. Vechev},
			title        = {CTBENCH: A Library and Benchmark for Certified Training},
			year         = {2025},
			booktitle    = {The Forty-Second International Conference on Machine Learning}'
paper: https://arxiv.org/abs/2406.04848
code: https://github.com/eth-sri/CTBench
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
# image: assets/images/taps.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Training certifiably robust neural networks is an important but challenging task. While many algorithms for (deterministic) certified training have been proposed, they are often evaluated on different training schedules, certification methods, and systematically under-tuned hyperparameters, making it difficult to compare their performance. To address this challenge, we introduce CTBench, a unified library and a high-quality benchmark for certified training that evaluates all algorithms under fair settings and systematically tuned hyperparameters. We show that (1) almost all algorithms in CTBench surpass the corresponding reported performance in literature in the magnitude of algorithmic improvements, thus establishing new state-of-the-art, and (2) the claimed advantage of recent algorithms drops significantly when we enhance the outdated baselines with a fair training schedule, a fair certification method and well-tuned hyperparameters. Based on CTBench, we provide new insights into the current state of certified training, including (1) certified models have less fragmented loss surface, (2) certified models share many mistakes, (3) certified models have more sparse activations, (4) reducing regularization cleverly is crucial for certified training especially for large radii and (5) certified training has the potential to improve out-of-distribution generalization. We are confident that CTBench will serve as a benchmark and testbed for future research in certified training.



