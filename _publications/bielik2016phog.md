---
ref: bielik2016phog
title: "PHOG: Probabilistic Model for Code"
authors: Pavol Bielik, Veselin Raychev, Martin Vechev 
year: 2016
venue: ACM ICML
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{bielik2016phog,
  title={PHOG: probabilistic model for code},
  author={Bielik, Pavol and Raychev, Veselin and Vechev, Martin},
  booktitle={International Conference on Machine Learning},
  pages={2933--2942},
  year={2016}}'
paper: https://files.sri.inf.ethz.ch/website/papers/icml16_phog.pdf
talk: 
slides: https://files.sri.inf.ethz.ch/website/slides/ICML16_PHOG.pdf
---

We introduce a new generative model for code called probabilistic higher order grammar (PHOG). PHOG generalizes probabilistic context free grammars (PCFGs) by allowing conditioning of a production rule beyond the parent non-terminal, thus capturing rich contexts relevant to programs. Even though PHOG is more powerful than a PCFG, it can be learned from data just as efficiently. We trained a PHOG model on a large JavaScript code corpus and show that it is more precise than existing models, while similarly fast. As a result, PHOG can immediately benefit existing programming tools based on probabilistic models of code.
