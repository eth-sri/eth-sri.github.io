---
ref: paletov2018inferring
title: Inferring Crypto API Rules from Code Changes
authors: Rumen Paletov, Petar Tsankov, Veselin Raychev, Martin Vechev
year: 2018
month: 06
venue: PLDI
projects: plml
awards:
bibtex: '@inproceedings{paletov2018inferring,
  title={Inferring crypto API rules from code changes},
  author={Paletov, Rumen and Tsankov, Petar and Raychev, Veselin and Vechev, Martin},
  booktitle={Proceedings of the 39th ACM SIGPLAN Conference on Programming Language Design and Implementation},
  pages={450--464},
  year={2018},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/diffcode-pldi2018.pdf
talk: https://www.youtube.com/watch?v=vl-w5KFO0II
slides: 
---

Creating and maintaining an up-to-date set of security rules that match misuses of crypto APIs is challenging, as crypto APIs constantly evolve over time with new cryptographic primitives and settings, making existing ones obsolete.

To address this challenge, we present a new approach to extract security fixes from thousands of code changes. Our approach consists of: (i) identifying code changes, which often capture security fixes, (ii) an abstraction that filters irrelevant code changes (such as refactorings), and (iii) a clustering analysis that reveals commonalities between semantic code changes and helps in eliciting security rules.

We applied our approach to the Java Crypto API and showed that it is effective: (i) our abstraction effectively filters non-semantic code changes (over 99% of all changes) without removing security fixes, and (ii) over 80% of the code changes are security fixes identifying security rules. Based on our results, we identified 13 rules, including new ones not supported by existing security checkers.
