---
ref: horvath2022derand
title: "(De-)Randomized Smoothing for Decision Stump Ensembles"
authors: Miklós Z. Horváth*, Mark Niklas Müller*, Marc Fischer, Martin Vechev
year: 2022
month: 12
venue: NeurIPS
projects: safeai
bibtex: '@inproceedings{horvath2022derandomized,
      	author    = {Miklós Z. Horváth and Mark Niklas M{\"{u}}ller and Marc Fischer and Martin Vechev},
	title     = {(De-)Randomized Smoothing for Decision Stump Ensembles},
	booktitle = {Advances in Neural Information Processing Systems},
	year      = {2022},
	url       = {https://openreview.net/forum?id=IbBHnPyjkco},
	}'
paper: https://arxiv.org/abs/2205.13909
code: https://github.com/eth-sri/drs
#blogpost: smoothens
---

Tree-based models are used in many high-stakes application domains such as finance and medicine, where robustness and interpretability are of utmost importance. Yet, methods for improving and certifying their robustness are severely under-explored, in contrast to those focusing on neural networks. Targeting this important challenge, we propose deterministic smoothing for decision stump ensembles. Whereas most prior work on randomized smoothing focuses on evaluating arbitrary base models approximately under input randomization, the key insight of our work is that decision stump ensembles enable exact yet effiient evaluation via dynamic programming. Importantly, we obtain deterministic robustness certificates, even jointly over numerical and categorical features, a setting ubiquitous in the real world. Further, we derive an MLE-optimal training method for smoothed decision stumps under randomization and propose two boosting approaches to improve their provable robustness. An extensive experimental evaluation on computer vision and tabular data tasks shows that our approach yields signficantly higher certified accuracies than the state-of-the-art for tree-based models. We release all code and trained models at https://github.com/eth-sri/drs.
