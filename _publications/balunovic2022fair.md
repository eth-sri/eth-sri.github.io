---
ref: balunovic2022fair
title: "Fair Normalizing Flows"
authors: Mislav Balunović, Anian Ruoss, Martin Vechev
year: 2022
month: 4
venue: ICLR
projects: safeai
bibtex: '@misc{balunović2021fair,
      title={Fair Normalizing Flows}, 
      author={Mislav Balunović and Anian Ruoss and Martin Vechev},
      year={2021},
      eprint={2106.05937},
      archivePrefix={arXiv},
      primaryClass={cs.LG}}'
paper: https://arxiv.org/abs/2106.05937
blogpost: fnf
talk: 
slides: 
code: https://github.com/eth-sri/fnf
---

Fair representation learning is an attractive approach that promises fairness of downstream predictors by encoding sensitive data. Unfortunately, recent work has shown that strong adversarial predictors can still exhibit unfairness by recovering sensitive attributes from these representations. In this work, we present Fair Normalizing Flows (FNF), a new approach offering more rigorous fairness guarantees for learned representations. Specifically, we consider a practical setting where we can estimate the probability density for sensitive groups. The key idea is to model the encoder as a normalizing flow trained to minimize the statistical distance between the latent representations of different groups. The main advantage of FNF is that its exact likelihood computation allows us to obtain guarantees on the maximum unfairness of any potentially adversarial downstream predictor. We experimentally demonstrate the effectiveness of FNF in enforcing various group fairness notions, as well as other attractive properties such as interpretability and transfer learning, on a variety of challenging real-world datasets. 
