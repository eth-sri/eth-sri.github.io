---
ref: bichsel2018fine
title: Fine-grained Semantics for Probabilistic Programs
authors: Benjamin Bichsel, Timon Gehr, Martin Vechev
year: 2018
month: 04
venue: ESOP
projects: probabilistic-programming
awards:
bibtex: '@inproceedings{bichsel2018fine,
  title={Fine-grained Semantics for Probabilistic Programs},
  author={Bichsel, Benjamin and Gehr, Timon and Vechev, Martin},
  booktitle={European Symposium on Programming},
  pages={145--185},
  year={2018},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/Fine-grained_Semantics_for_Probabilistic_Programs_full.pdf
talk: 
slides: https://files.sri.inf.ethz.ch/website/slides/esop18-fine-grained-semantics-main.pdf
---

Probabilistic programming is an emerging technique for modeling processes involving uncertainty. Thus, it is important to ensure these programs are assigned precise formal semantics that also cleanly handle typical exceptions such as non-termination or division by zero. However, existing semantics of probabilistic programs do not fully accommodate different exceptions and their interaction, often ignoring some or conflating multiple ones into a single exception state, making it impossible to distinguish exceptions or to study their interaction.
