---
ref: boneart2021transformers
title: Fast and Precise Certification of Transformers
authors: Gregory Bonaert, Dimitar I. Dimitrov, Maximilian Baader, Martin Vechev        
year: 2021
month: 6
venue: PLDI
projects: safeai
awards:
bibtex: "@inproceedings{bonaert2021transformers,
	title     = {Fast and precise certification of transformers},
  url       = {https://doi.org/10.1145/3453483.3454056},
  doi       = {10.1145/3453483.3454056},
	booktitle = {{PLDI} '21: 42nd {ACM} {SIGPLAN} International Conference on Programming
               Language Design and Implementation, Virtual Event, Canada, June 20-25,
               2021},
	publisher = {ACM},
	author    = {Gregory Bonaert and
               Dimitar I. Dimitrov and
               Maximilian Baader and
               Martin T. Vechev},
	year = {2021}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/pldi21-transformers.pdf
slides: https://files.sri.inf.ethz.ch/website/slides/pldi21-fast-and-precise-transformer-certification.pdf
code: https://github.com/eth-sri/DeepT
---

We present DeepT, a novel method for certifying Transformer networks based on abstract interpretation. The key idea behind DeepT is our new Multi-norm Zonotope abstract domain, an extension of the classical Zonotope designed to handle l<sup>1</sup> and l<sup>2</sup>-norm bound perturbations. We introduce all Multi-norm Zonotope abstract transformers necessary to handle these complex networks, including the challenging softmax function and dot product. Our evaluation shows that DeepT can certify average robustness radii that are 28x larger than the state-of-the-art, while scaling favorably. Further, for the first time, we certify Transformers against synonym attacks on long sequences of words, where each word can be replaced by any synonym. DeepT achieves a high certification success rate on sequences of words where enumeration-based verification would take 2 to 3 orders of magnitude more time.
