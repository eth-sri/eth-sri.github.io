---
ref: horvath2022boosting
title: "Boosting Randomized Smoothing with Variance Reduced Classifiers"
authors: Miklós Z. Horváth, Mark Niklas Müller, Marc Fischer, Martin Vechev
year: 2022
month: 4
venue: ICLR (Spotlight)
projects: safeai
paper: https://arxiv.org/abs/2106.06946
code: https://github.com/eth-sri/smoothing-ensembles
blogpost: smoothens
bibtex: '@inproceedings{
	horvath2022boosting,
	title={Boosting Randomized Smoothing with Variance Reduced Classifiers},
      	author={Miklós Z. Horváth and Mark Niklas M{\"{u}}ller and Marc Fischer and Martin Vechev},
	booktitle={International Conference on Learning Representations},
	year={2022}}'
---

Randomized Smoothing (RS) is a promising method for obtaining robustness certiﬁcates by evaluating a base model under noise. In this work, we: (i) theoretically motivate why ensembles are a particularly suitable choice as base models for RS, and (ii) empirically conﬁrm this choice, obtaining state-of-the-art results in multiple settings. The key insight of our work is that the reduced variance of ensembles over the perturbations introduced in RS leads to signiﬁcantly more consistent classiﬁcations for a given input. This, in turn, leads to substantially increased certiﬁable radii for samples close to the decision boundary. Additionally, we introduce key optimizations which enable an up to 55-fold decrease in sample complexity of RS, thus drastically reducing its computational overhead. Experimentally, we show that ensembles of only 3 to 10 classiﬁers consistently improve on their strongest constituting model with respect to their average certiﬁed radius (ACR) by 5% to 21% on both CIFAR10 and ImageNet, achieving a new state-of-the-art ACR of 0.86 and 1.11, respectively. 
