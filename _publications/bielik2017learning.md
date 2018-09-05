---
ref: bielik2017learning
title: Learning a Static Analyzer from Data 
authors: Pavol Bielik, Veselin Raychev, Martin Vechev
year: 2017
venue: CAV
projects: plml
awards:
bibtex: '@inproceedings{bielik2017learning,
  title={Learning a static analyzer from data},
  author={Bielik, Pavol and Raychev, Veselin and Vechev, Martin},
  booktitle={International Conference on Computer Aided Verification},
  pages={233--253},
  year={2017},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/cav17-pa.pdf
talk: https://www.youtube.com/watch?v=bkieI3jLxVY
slides: https://files.sri.inf.ethz.ch/website/slides/cav17_learning_slides.pdf
---

To be practically useful, modern static analyzers must precisely model the effect of both, statements in the programming language as well as frameworks used by the program under analysis. While important, manually addressing these challenges is difficult for at least two reasons: (i) the effects on the overall analysis can be non-trivial, and (ii) as the size and complexity of modern libraries increase, so is the number
of cases the analysis must handle.

In this paper we present a new, automated approach for creating static analyzers: instead of manually providing the various inference rules of the analyzer, the key idea is to learn these rules from a dataset of programs. Our method consists of two ingredients: (i) a synthesis algorithm capable of learning a candidate analyzer from a given dataset, and (ii) a counter-example guided learning procedure which generates new programs beyond those in the initial dataset, critical for discovering corner cases and ensuring the learned analysis generalizes to unseen programs. We implemented and instantiated our approach to the task of learning JavaScript static analysis rules for a subset of points-to analysis and for allocation sites analysis. These are challenging yet important problems that have received significant research attention. We show that our approach is effective: our system automatically discovered practical and useful inference rules for many cases that are tricky to manually identify and are missed by state-of-the-art, manually tuned analyzers.
