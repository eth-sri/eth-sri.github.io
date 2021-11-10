---
ref: balunovic2021bayesian
title: "Bayesian Framework for Gradient Leakage"
authors: Mislav Balunovic, Dimitar I. Dimitrov, Robin Staab, Martin Vechev
year: 2021
month: 11
venue: NeurIPS Workshop on New Frontiers in Federated Learning
projects: safeai
bibtex: '@misc{balunovic2021bayesian,
      title={Bayesian Framework for Gradient Leakage}, 
      author={Mislav Balunović and Dimitar I. Dimitrov and Robin Staab and Martin Vechev},
      year={2021},
      eprint={2111.04706},
      archivePrefix={arXiv},
      primaryClass={cs.LG}}'
paper: https://arxiv.org/abs/2111.04706
---

Federated learning is an established method for training machine learning models without sharing training data. However, recent work has shown that it cannot guarantee data privacy as shared gradients can still leak sensitive information. To formalize the problem of gradient leakage, we propose a theoretical framework that enables, for the first time, analysis of the Bayes optimal adversary phrased as an optimization problem. We demonstrate that existing leakage attacks can be seen as approximations of this optimal adversary with different assumptions on the probability distributions of the input data and gradients. Our experiments confirm the effectiveness of the Bayes optimal adversary when it has knowledge of the underlying distribution. Further, our experimental evaluation shows that several existing heuristic defenses are not effective against stronger attacks, especially early in the training process. Thus, our findings indicate that the construction of more effective defenses and their evaluation remains an open problem.