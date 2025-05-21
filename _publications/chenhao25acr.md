---
ref: chenhao25acr
title: "Average Certified Radius is a Poor Metric for Randomized Smoothing"
authors: Chenhao Sun*, Yuhao Mao*, Mark Niklas Müller, Martin Vechev
year: 2025
month: 07
venue: ICML
projects: safeai
bibtex: '@inproceedings{chenhao25acr
			author       = {Chenhao Sun and
                            Yuhao Mao and
							Mark Niklas M{\"{u}}ller  and
							Martin T. Vechev},
			title        = {Average Certified Radius is a Poor Metric for Randomized Smoothing},
			year         = {2025},
			booktitle    = {The Forty-Second International Conference on Machine Learning}'
paper: https://arxiv.org/abs/2410.06895
# code: https://github.com/eth-sri/CTBench
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
# image: assets/images/taps.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Randomized smoothing is a popular approach for providing certified robustness guarantees against adversarial attacks, and has become an active area of research. Over the past years, the average certified radius (ACR) has emerged as the most important metric for comparing methods and tracking progress in the field. However, in this work, for the first time we show that ACR is a poor metric for evaluating robustness guarantees provided by randomized smoothing. We theoretically prove not only that a trivial classifier can have arbitrarily large ACR, but also that ACR is much more sensitive to improvements on easy samples than on hard ones. Empirically, we confirm that existing training strategies, though improving ACR with different approaches, reduce the model's robustness on hard samples consistently. To strengthen our conclusion, we propose strategies, including explicitly discarding hard samples, reweighting the dataset with approximate certified radius, and extreme optimization for easy samples, to achieve state-of-the-art ACR, without training for robustness on the full data distribution. Overall, our results suggest that ACR has introduced a strong undesired bias to the field, and its application should be discontinued when evaluating randomized smoothing.