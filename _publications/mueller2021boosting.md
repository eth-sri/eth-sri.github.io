---
ref: mueller2021boosting
title: "Certify or Predict: Boosting Certified Robustness with Compositional Architectures"
authors: Mark Niklas Müller, Mislav Balunovic, Martin Vechev
year: 2021
month: 5
venue: ICLR 
projects: safeai
bibtex: '@inproceedings{
	mueller2021boosting,
	title={Boosting Certified Robustness of Deep Networks via a Compositional Architecture},
	author={Mark Niklas Mueller and Mislav Balunovic and Martin Vechev},
	booktitle={International Conference on Learning Representations},
	year={2021}}'
paper: https://files.sri.inf.ethz.ch/website/papers/mueller2021boosting.pdf
#slides: https://files.sri.inf.ethz.ch/website/slides/iclr2020-colt.pdf
#image: assets/images/colt.png
#talk: https://iclr.cc/virtual_2020/poster_SJxSDxrKDr.html
---

A core challenge with existing certified defense mechanisms is that while they improve certified robustness, they also tend to drastically decrease natural accuracy, making it difficult to use these methods in practice. In this work, we propose a new architecture which addresses this challenge and enables one to boost the certified robustness of any state-of-the-art deep network, while controlling the overall accuracy loss, without requiring retraining. The key idea is to combine this model with a (smaller) certified network where at inference time, an adaptive selection mechanism decides on the network to process the input sample. The approach is compositional: one can combine any pair of state-of-the-art (e.g., EfficientNet or ResNet) and certified networks, without restriction. The resulting architecture enables much higher natural accuracy than previously possible with certified defenses alone, while substantially boosting the certified robustness of deep networks. We demonstrate the effectiveness of this adaptive approach on a variety of datasets and architectures.
For instance, on CIFAR-10 with an L-inf perturbation of 2/255, we are the first to obtain a high natural accuracy (90.1%) with non-trivial certified robustness (27.5%). Notably, prior state-of-the-art methods incur a substantial drop in accuracy for a similar certified robustness.

