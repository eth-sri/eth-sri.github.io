---
ref: balunovic2020adversarial
title: "Adversarial Training and Provable Defenses: Bridging the Gap"
authors: Mislav Balunović, Martin Vechev
year: 2020
month: 4
venue: ICLR
awards: Oral
projects: safeai
bibtex: '@inproceedings{balunovic2020adversarial,
  title={Adversarial Training and Provable Defenses: Bridging the Gap},
  author={Mislav Balunović, Martin Vechev},
  journal={International Conference on Learning Representations},
  year={2020}}'
paper: https://files.sri.inf.ethz.ch/website/papers/iclr2020-colt.pdf
slides: https://files.sri.inf.ethz.ch/website/slides/iclr2020-colt.pdf
image: assets/images/colt.png
talk: https://iclr.cc/virtual_2020/poster_SJxSDxrKDr.html
---

We propose a new method to train neural networks based on a novel combination of adversarial training and provable defenses. The key idea is to model training as a procedure which includes both, the verifier and the adversary. In every iteration, the verifier aims to
certify the network using convex relaxation while the adversary tries to find inputs inside that convex relaxation which cause verification to fail. We experimentally show that this training method is promising and achieves the best of both worlds -- it produces a state-of-the-art
neural network with certified robustness of 58.1% and accuracy of 78.8% on the challenging CIFAR-10 dataset with a 2/255 L-inf perturbation. This significantly improves over the currently known best results of 53.9% certified robustness and 68.3% accuracy. 

