---
ref: mirman2020generative
title: "Robustness Certification of Generative Models"
authors: Mathew Mirman, Timon Gehr, Martin Vechev 
year: 2020
venue: arXiv
projects: safeai
awards:
bibtex: '@article{mirman2020robustness,
    title={Robustness Certification of Generative Models},
    author={Matthew Mirman and Timon Gehr and Martin Vechev},
    year={2020},
    eprint={2004.14756},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}'
paper: https://arxiv.org/pdf/2004.14756.pdf
talk: 
slides: 
---

Generative neural networks can be used to specify continuous transformations between images via latent-space interpolation. However, certifying that all images captured by the resulting path in the image manifold satisfy a given property can be very challenging. This is because this set is highly non-convex, thwarting existing scalable robustness analysis methods, which are often based on convex relaxations. We present ApproxLine, a scalable certification method that successfully verifies non-trivial specifications involving generative models and classifiers. ApproxLine can provide both sound deterministic and probabilistic guarantees, by capturing either infinite non-convex sets of neural network activation vectors or distributions over such sets. We show that ApproxLine is practically useful and can verify interesting interpolations in the networks latent space.
