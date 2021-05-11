---
ref: he21namer 
title: "Learning Fast and Precise Numerical Analysis"
authors: Jingxuan He, Cheng-Chun Lee, Veselin Raychev, Martin Vechev
year: 2021
month: 06
venue: PLDI
projects: plml
awards:
bibtex:
paper: https://files.sri.inf.ethz.ch/website/papers/pldi21-namer.pdf
---

We introduce a new approach for finding and fixing naming issues in source code. The method is based on a careful combination of unsupervised and supervised procedures: (i) unsupervised mining of patterns from Big Code that express common naming idioms. Program fragments violating such idioms indicates likely naming issues, and (ii) supervised learning of a classifier on a small labeled dataset which filters potential false positives from the violations.

We implemented our method in a system called Namer and evaluated it on a large number of Python and Java programs. We demonstrate that Namer is effective in finding naming mistakes in real world repositories with high precision (~70%). Perhaps surprisingly, we also show that existing deep learning methods are not practically effective and achieve low precision in finding naming issues (up to ~16%).
