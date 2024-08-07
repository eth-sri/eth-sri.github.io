---
ref: mirman2021pldi
title: "Robustness Certification with Generative Models"
authors: Matthew Mirman, Alexander Hägele, Timon Gehr, Pavol Bielik, Martin Vechev
year: 2021
month: 04
venue: PLDI
projects: safeai, plml
awards:
bibtex: '@inproceedings{mirman2021pldi,
  title={Robustness Certification with Generative Models},
  author={Mirman, Matthew and H\"agele, Alexander and Gehr, Timon and Bielik, Pavol and Vechev, Martin},
  booktitle={Proceedings of the 42nd ACM SIGPLAN Conference on Programming Language Design and Implementation},
  year={2021},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/mirman2021pldi.pdf
slides: 
---

Generative neural networks are powerful models capable of learning a wide range of rich semantic image transformations such as altering person's age, head orientation, adding mustache, changing the hair color and many more. At a high level, a generative model effectively produces new and previously unseen images with the desired properties, which can then be used to improve the accuracy of existing models. In this work, we advance the state-of-the-art in verification by bridging the gap between (i) the well studied but limited norm-based and geometric transformations, and (ii) the rich set of semantic transformations used in practice. This problem is especially hard since the images are generated from a highly non-convex image manifold, preventing the use of most existing verifiers, which often rely on convex relaxations. We present a new verifier, called GenProve, which is capable of certifying the rich set of semantic transformations of generative models. GenProve can provide both sound deterministic and probabilistic guarantees, by capturing infinite non-convex sets of activation vectors and distributions over them, while scaling to realistic networks.
