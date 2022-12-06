---
ref: jovanovic2022paradox
title: "On the Paradox of Certified Training"
authors: Nikola Jovanović*, Mislav Balunović*, Maximilian Baader, Martin Vechev
year: 2022
month: 10
venue: TMLR
projects: safeai
bibtex: '@article{jovanovic2022on,
    title={On the Paradox of Certified Training},
    author={Nikola Jovanović and Mislav Balunović and Maximilian Baader and Martin Vechev},
    journal={Transactions on Machine Learning Research},
    year={2022},
    url={https://openreview.net/forum?id=atJHLVyBi8},
    note={}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/jovanovic2022paradox.pdf
code: https://github.com/eth-sri/paradox
---

Certified defenses based on convex relaxations are an established technique for training provably robust models. The key component is the choice of relaxation, varying from simple intervals to tight polyhedra. Counterintuitively, loose interval-based training often leads to higher certified robustness than what can be achieved with tighter relaxations, which is a well-known but poorly understood paradox. While recent works introduced various improvements aiming to circumvent this issue in practice, the fundamental problem of training models with high certified robustness remains unsolved. In this work, we investigate the underlying reasons behind the paradox and identify two key properties of relaxations, beyond tightness, that impact certified training dynamics: continuity and sensitivity. Our extensive experimental evaluation with a number of popular convex relaxations provides strong evidence that these factors can explain the drop in certified robustness observed for tighter relaxations. We also systematically explore modifications of existing relaxations and discover that improving unfavorable properties is challenging, as such attempts often harm other properties, revealing a complex tradeoff. Our findings represent an important first step towards understanding the intricate optimization challenges involved in certified training.
