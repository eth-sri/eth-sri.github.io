---
ref: bielik2021adaptiveattacks
title: Automated Discovery of Adaptive Attacks on Adversarial Defenses
authors: Chengyuan Yao, Pavol Bielik, Petar Tsankov, Martin Vechev 
year: 2021
month: 07
venue: AutoML@ICML
projects: safeai
awards: Oral
bibtex: "@inproceedings{
    yao2021automated,
    title={Automated Discovery of Adaptive Attacks on Adversarial Defenses},
    author={Chengyuan Yao and Pavol Bielik and Petar Tsankov and Martin Vechev},
    booktitle={8th ICML Workshop on Automated Machine Learning (AutoML) },
    year={2021},
    url={https://openreview.net/forum?id=M5k-2Pq4pv}   
}"
paper: https://openreview.net/pdf?id=M5k-2Pq4pv
talk: https://icml.cc/virtual/2021/workshop/8371
slides: 
---

Reliable evaluation of adversarial defenses is a challenging task, currently limited to an expert who manually crafts attacks that exploit the defenses inner workings, or to approaches based on ensemble of fixed attacks, none of which may be effective for the specific defense at hand. Our key observation is that custom attacks are composed from a set of reusable building blocks, such as fine-tuning relevant attack parameters, network transformations, and custom loss functions. Based on this observation, we present an extensible tool that defines a search space over these reusable building blocks and automatically discovers an effective attack on a given model with an unknown defense by searching over suitable combinations of these blocks. We evaluated our approach on 23 adversarial defenses and showed it outperforms AutoAttack (Croce and Hein, 2020), the current state-of-the-art tool for reliable evaluation of adversarial defenses: our discovered attacks are either stronger, producing 3.0%-50.8% additional adversarial examples (10 cases), or are typically 2x faster while enjoying similar adversarial robustness (13 cases).
