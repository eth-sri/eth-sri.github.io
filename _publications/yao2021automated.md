---
ref: yao2021automated
title: Automated Discovery of Adaptive Attacks on Adversarial Defenses
authors: Chengyuan Yao, Pavol Bielik, Petar Tsankov, Martin Vechev 
year: 2021
month: 12
venue: NeurIPS
projects: safeai
awards:
bibtex: "@inproceedings{
    yao2021automated,
    title={Automated Discovery of Adaptive Attacks on Adversarial Defenses},
    author={Chengyuan Yao and Pavol Bielik and PETAR TSANKOV and Martin Vechev},
    booktitle={Thirty-Fifth Conference on Neural Information Processing Systems},
    year={2021},
    url={https://openreview.net/forum?id=nWz-Si-uTzt}
}"
paper: https://openreview.net/pdf?id=nWz-Si-uTzt
talk: 
slides: 
---

Reliable evaluation of adversarial defenses is a challenging task, currently limited to an expert who manually crafts attacks that exploit the defense’s inner workings, or to approaches based on ensemble of fixed attacks, none of which may be effective for the specific defense at hand. Our key observation is that adaptive attacks are composed from a set of reusable building blocks that can be formalized in a search space and used to automatically discover attacks for unknown defenses. We evaluated our approach on 24 adversarial defenses and show that it outperforms AutoAttack, the current state-of-the-art tool for reliable evaluation of adversarial defenses: our tool discovered significantly stronger attacks by producing 3.0%-50.8% additional adversarial examples for 10 models, while obtaining attacks with slightly stronger or similar strength for the remaining models.
