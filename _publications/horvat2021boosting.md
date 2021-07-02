---
ref: horvat2021boosting
title: "Boosting Randomized Smoothing with Variance Reduced Classifiers"
authors: Miklós Z. Horváth, Mark Niklas Müller, Marc Fischer, Martin Vechev
year: 2021
month: 6
venue: arXiv
projects: safeai
bibtex: '@misc{horváth2021boosting,
      title={Boosting Randomized Smoothing with Variance Reduced Classifiers}, 
      author={Miklós Z. Horváth and Mark Niklas Müller and Marc Fischer and Martin Vechev},
      year={2021},
      eprint={2106.06946},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
      }'
paper: https://arxiv.org/abs/2106.06946
---

Randomized Smoothing (RS) is a promising method for obtaining robustness certificates by evaluating a base model under noise. In this work we: (i) theoretically motivate why ensembles are a particularly suitable choice as base models for RS, and (ii) empirically confirm this choice, obtaining state of the art results in multiple settings. The key insight of our work is that the reduced variance of ensembles over the perturbations introduced in RS leads to significantly more consistent classifications for a given input, in turn leading to substantially increased certifiable radii for difficult samples. We also introduce key optimizations which enable an up to 50-fold decrease in sample complexity of RS, thus drastically reducing its computational overhead. Experimentally, we show that ensembles of only 3 to 10 classifiers consistently improve on the strongest single model with respect to their average certified radius (ACR) by 5% to 21% on both CIFAR-10 and ImageNet. On the latter, we achieve a state-of-the-art ACR of 1.11. We release all code and models required to reproduce our results upon publication. 
