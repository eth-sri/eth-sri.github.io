---
ref: fischer2019dl2
title: "DL2: Training and Querying Neural Networks with Logic"
authors: Marc Fischer, Mislav Balunovic, Dana Drachsler-Cohen, Timon Gehr, Ce Zhang, Martin Vechev
year: 2019
month: 06
venue: ICML
projects: safeai
bibtex: '@inproceedings{fischer2019dl2,
  title={DL2: Training and Querying Neural Networks with Logic},
  author={Marc Fischer, Mislav Balunovic, Dana Drachsler-Cohen, Timon Gehr, Ce Zhang, Martin Vechev},
  booktitle={International Conference on Machine Learning},
  year={2019}}'
paper: https://files.sri.inf.ethz.ch/website/papers/icml19-dl2.pdf
slides: https://files.sri.inf.ethz.ch/website/papers/icml19-dl2-poster.pdf
---

<meta property="og:image" content="https://www.sri.inf.ethz.ch/assets/images/dl2_poster.png" />

We present DL2, a system for training and querying neural networks with logical constraints. Using DL2, one can declaratively specify domain knowledge to be enforced during training or pose queries on the model with the goal of finding inputs that satisfy a set of constraints. DL2 works by translating logical constraints into a differentiable loss with desirable mathematical properties, then minimized with standard gradient-based methods. We evaluate DL2 by training networks with interesting constraints in unsupervised, semi-supervised and supervised settings. Our experimental evaluation demonstrates that DL2 is both, more expressive than prior approaches combining logic and neural networks, and its resulting loss is better suited for optimization. Further, we show that for a number of queries, DL2 can find the desired inputs within seconds (even for large models such as ResNet-50 on ImageNet).
