---
ref: bshouty2017learning
title: Learning Disjunctions of Predicates 
authors: Nader H. Bshouty, Dana Drachsler-Cohen, Martin Vechev, Eran Yahav
year: 2017
venue: COLT
projects: Research Area 1, Research Area 1
awards:
bibtex: '@article{bshouty2017learning,
  title={Learning disjunctions of predicates},
  author={Bshouty, Nader H and Drachsler-Cohen, Dana and Vechev, Martin and Yahav, Eran},
  journal={arXiv preprint arXiv:1706.05070},
  year={2017}}'
paper: ldp-colt17.pdf
talk: 
slides: 
---

Let F be a set of boolean functions. We present an algorithm for learning F∨ := {∨f∈Sf | S ⊆ F} from membership queries. Our algorithm asks at most |F| · OPT(F∨) membership queries where OPT(F∨) is the minimum worst case number of membership queries for learning F∨. When F is a set of halfspaces over a constant dimension space or a set of variable inequalities, our algorithm runs in polynomial time.
The problem we address has practical importance in the field of program synthesis, where the goal is to synthesize a program that meets some requirements. Program synthesis has become popular especially in settings aiming to help end users. In such settings, the requirements are not provided upfront and the synthesizer can only learn them by posing membership queries to the end user. Our work enables such synthesizers to learn the exact requirements while bounding the number of membership queries.