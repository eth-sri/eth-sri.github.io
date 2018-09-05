---
ref: gehr2016psi
title: "PSI: Exact Symbolic Inference for Probabilistic Programs"
authors: Timon Gehr, Sasa Misailovic, Martin Vechev 
year: 2016
venue: CAV
projects: probabilistic-programming
awards:
bibtex: '@inproceedings{gehr2016psi,
  title={Psi: Exact symbolic inference for probabilistic programs},
  author={Gehr, Timon and Misailovic, Sasa and Vechev, Martin},
  booktitle={International Conference on Computer Aided Verification},
  pages={62--83},
  year={2016},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/psi-solver.pdf
talk: 
slides: 
---

Probabilistic inference is a key mechanism for reasoning about probabilistic programs. Since exact inference is theoretically expensive, most probabilistic inference systems today have adopted approximate inference techniques, which trade precision for better performance (but often without guarantees). As a result, while desirable for its ultimate precision, the practical effectiveness of exact inference for probabilistic
programs is mostly unknown.

This paper presents PSI (http://www.psisolver.org), a novel symbolic analysis system for exact inference in probabilistic programs with both continuous and discrete random variables. PSI computes succinct symbolic representations of the joint posterior distribution represented by a given probabilistic program. PSI can compute answers to various posterior distribution, expectation and assertion queries using its own backend
for symbolic reasoning.

Our evaluation shows that PSI is more effective than existing exact inference approaches: (i) it successfully computed a precise result for more programs, and (ii) simplified expressions that existing computer algebra
systems (e.g., Mathematica, Maple) fail to handle.
