---
ref: bielik2015programming
title: "Programming with Big Code: Lessons, Techniques and Applications" 
authors: Pavol Bielik, Veselin Raychev, Martin Vechev        
year: 2015
venue: SNAPL
projects: plml
awards:
bibtex: '@inproceedings{bielik2015programming,
  title={Programming with" big code": Lessons, techniques and applications},
  author={Bielik, Pavol and Raychev, Veselin and Vechev, Martin},
  booktitle={LIPIcs-Leibniz International Proceedings in Informatics},
  volume={32},
  year={2015},
  organization={Schloss Dagstuhl-Leibniz-Zentrum fuer Informatik}}'
paper: SNAPL15-BigCode.pdf
talk: 
slides: 
---

Programming tools based on probabilistic models of massive codebases (aka “Big Code”) promise to solve important programming tasks that were difficult or practically infeasible to address before. However, building such tools requires solving a number of hard problems at the intersection of programming languages, program analysis and machine learning.

In this paper we summarize some of our experiences and insights obtained by developing several such probabilistic systems over the last few years (some of these systems are regularly used by thousands of developers worldwide). We hope these observations can provide a guideline for others attempting to create such systems.

We also present a prediction approach we find suitable as a starting point for building probabilistic tools, and discuss a practical framework implementing this approach, called Nice2Predict. We release the Nice2Predict framework publicly – the framework can be immediately used as a basis for developing new probabilistic tools. Finally, we present programming applications that we believe will benefit from probabilistic models and should be investigated further.
