---
ref: ruoss2020lcifr
title: Learning Certified Individually Fair Representations
authors: Anian Ruoss, Mislav Balunović, Marc Fischer, Martin Vechev
year: 2020
month: 12
venue: NeurIPS
projects: safeai
awards:
bibtex: '@incollection{ruoss2020learning,
    title = {Learning Certified Individually Fair Representations},
    author = {Ruoss, Anian and Balunović, Mislav and Fischer, Marc and Vechev, Martin},
	booktitle = {Advances in Neural Information Processing Systems 33},
    year = {2020}
}'
paper: https://arxiv.org/pdf/2002.10312
talk: 
slides: https://files.sri.inf.ethz.ch/website/slides/neurips2020-lcifr.pdf
---

To effectively enforce fairness constraints one needs to define an appropriate notion of fairness and employ representation learning in order to impose this notion without compromising downstream utility for the data consumer. A desirable notion is individual fairness as it guarantees similar treatment for similar individuals. In this work, we introduce the first method which generalizes individual fairness to rich similarity notions via logical constraints while also enabling data consumers to obtain fairness certificates for their models. The key idea is to learn a representation that provably maps similar individuals to latent representations at most epsilon apart in l-infinity distance, enabling data consumers to certify individual fairness by proving epsilon-robustness of their classifier. Our experimental evaluation on six real-world datasets and a wide range of fairness constraints demonstrates that our approach is expressive enough to capture similarity notions beyond existing distance metrics while scaling to realistic use cases.

