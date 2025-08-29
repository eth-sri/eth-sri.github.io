---
ref: dan2013predicate
title: Predicate Abstraction for Relaxed Memory Models
authors: Andrei Dan, Yuri Meshman, Martin Vechev, Eran Yahav 
year: 2013
venue: Static Analysis Symposium (SAS)
projects: fender
awards:
bibtex: '@inproceedings{dan2013predicate,
  title={Predicate abstraction for relaxed memory models},
  author={Dan, Andrei Marian and Meshman, Yuri and Vechev, Martin and Yahav, Eran},
  booktitle={International Static Analysis Symposium},
  pages={84--104},
  year={2013},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/sas13-parmm-extended.pdf
talk: 
slides: https://files.sri.inf.ethz.ch/website/slides/sas13-parmm-slides.pdf
---

We present a novel approach for predicate abstraction of programs running on relaxed memory models. Our approach consists of two steps.

First, we reduce the problem of verifying a program P running on a memory model M to the problem of verifying a program PM that captures an abstraction of M as part of the program.

Second, we present a new technique for discovering predicates that enable verification of PM. The core idea is to extrapolate from the predicates used to verify P under sequential consistency. A key new concept is that of cube extrapolation: it successfully avoids exponential state explosion when abstracting PM.

We implemented our approach for the x86 TSO and PSO memory models and showed that predicates discovered via extrapolation are powerful enough to verify several challenging concurrent programs. This is the first time some of these programs have been verified for a model as relaxed as PSO.
