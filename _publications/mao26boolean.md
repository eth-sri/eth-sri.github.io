---
ref: mao26boolean
title: "Learning Compact Boolean Networks"
authors: Shengpu Wang, Yuhao Mao, Yani Zhang, Martin Vechev
year: 2026
month: 07
venue: arXiv (preprint)
# projects: safeai
bibtex: '@article{wang26boolean,
    title={Learning Compact Boolean Networks},
    author={Wang, Shengpu and Mao, Yuhao and Zhang, Yani and Vechev, Martin},
    journal={arXiv preprint arXiv:2602.05830},
    year={2026}
    }'
paper: https://arxiv.org/abs/2602.05830
# code:
# slides:
#poster:
# image: assets/images/taps.png
#talk:
---

Floating-point neural networks dominate modern machine learning but incur substantial inference cost, motivating interest in Boolean networks for resource-constrained settings. However, learning compact and accurate Boolean networks is challenging due to their combinatorial nature. In this work, we address this challenge from three different angles: learned connections, compact convolutions and adaptive discretization. First, we propose a novel strategy to learn efficient connections with no additional parameters and negligible computational overhead. Second, we introduce a novel convolutional Boolean architecture that exploits locality with fewer Boolean operations than existing methods. Third, we propose an adaptive discretization strategy to reduce the accuracy drop when converting a continuous-valued network into a Boolean one. Extensive results on standard vision benchmarks demonstrate that the Pareto front of accuracy vs. computation of our method significantly outperforms prior state-of-the-art, achieving better accuracy with up to 37x fewer Boolean operations.
