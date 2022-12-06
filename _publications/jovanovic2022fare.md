---
ref: jovanovic2022fare
title: "FARE: Provably Fair Representation Learning"
authors: Nikola Jovanović, Mislav Balunović, Dimitar I. Dimitrov, Martin Vechev
year: 2022
month: 12
venue: SyntheticData4ML@NeurIPS 2022
projects: safeai
bibtex: '@article{jovanovic2022fare,
  title={FARE: Provably Fair Representation Learning},
  author={Jovanovic, Nikola and Balunovic, Mislav and Dimitrov, Dimitar I and Vechev, Martin},
  journal={arXiv preprint arXiv:2210.07213},
  year={2022}
}'
paper: https://arxiv.org/abs/2210.07213
---

Fair representation learning (FRL) is a popular class of methods aiming to produce fair classifiers via data preprocessing. However, recent work has shown that prior methods achieve worse accuracy-fairness tradeoffs than originally suggested by their results. This dictates the need for FRL methods that provide provable upper bounds on unfairness of any downstream classifier, a challenge yet unsolved. In this work we address this challenge and propose Fairness with Restricted Encoders (FARE), the first FRL method with provable fairness guarantees. Our key insight is that restricting the representation space of the encoder enables us to derive suitable fairness guarantees, while allowing empirical accuracy-fairness tradeoffs comparable to prior work. FARE instantiates this idea with a tree-based encoder, a choice motivated by inherent advantages of decision trees when applied in our setting. Crucially, we develop and apply a practical statistical procedure that computes a high-confidence upper bound on the unfairness of any downstream classifier. In our experimental evaluation on several datasets and settings we demonstrate that FARE produces tight upper bounds, often comparable with empirical results of prior methods, which establishes the practical value of our approach.
