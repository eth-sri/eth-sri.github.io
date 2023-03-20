---
ref: balunovic2022bayesian
title: "Bayesian Framework for Gradient Leakage"
authors: Mislav Balunović, Dimitar I. Dimitrov, Robin Staab, Martin Vechev
year: 2022
month: 4
venue: ICLR
projects: safeai
bibtex: '@inproceedings{balunovic2022bayesian,
      title={Bayesian Framework for Gradient Leakage}, 
      author={Mislav Balunović and Dimitar I. Dimitrov and Robin Staab and Martin Vechev},
      booktitle={International Conference on Learning Representations},
      year={2022},
      url={https://openreview.net/forum?id=f2lrIbGx3x7}}'
paper: https://arxiv.org/abs/2111.04706
blogpost: bayesian
talk: 
slides: 
code: https://github.com/eth-sri/bayes-framework-leakage
---

Federated learning is an established method for training machine learning models without sharing training data. However, recent work has shown that it cannot guarantee data privacy as shared gradients can still leak sensitive information. To formalize the problem of gradient leakage, we propose a theoretical framework that enables, for the first time, analysis of the Bayes optimal adversary phrased as an optimization problem. We demonstrate that existing leakage attacks can be seen as approximations of this optimal adversary with different assumptions on the probability distributions of the input data and gradients. Our experiments confirm the effectiveness of the Bayes optimal adversary when it has knowledge of the underlying distribution. Further, our experimental evaluation shows that several existing heuristic defenses are not effective against stronger attacks, especially early in the training process. Thus, our findings indicate that the construction of more effective defenses and their evaluation remains an open problem.
