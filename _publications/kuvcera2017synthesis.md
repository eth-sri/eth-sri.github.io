---
ref: kuvcera2017synthesis
title: Synthesis of Probabilistic Privacy Enforcement 
authors: Martin Kucera, Petar Tsankov, Timon Gehr, Marco Guarnieri, Martin Vechev
year: 2017
venue: ACM CCS
projects: probabilistic-programming
awards:
bibtex: '@inproceedings{kuvcera2017synthesis,
  title={Synthesis of probabilistic privacy enforcement},
  author={Ku{\v{c}}era, Martin and Tsankov, Petar and Gehr, Timon and Guarnieri, Marco and Vechev, Martin},
  booktitle={Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security},
  pages={391--408},
  year={2017},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/spire-ccs17.pdf
talk: https://www.youtube.com/watch?v=_MINtBZwxUM
slides: 
---

Existing probabilistic privacy enforcement approaches permit the execution of a program that processes sensitive data only if the information it leaks is within the bounds specified by a given policy. Thus, to extract any information, users must manually design a program that satisfies the policy.

In this work, we present a novel synthesis approach that automatically transforms a program into one that complies with a given policy. Our approach consists of two ingredients. First, we phrase the problem of determining the amount of leaked information as Bayesian inference, which enables us to leverage existing probabilistic programming engines. Second, we present two synthesis procedures that add uncertainty to the program’s outputs as a way of reducing the amount of leaked information: an optimal one based on SMT solving and a greedy one with quadratic running time.

We implemented and evaluated our approach on 10 representative programs from multiple application domains. We show that our system can successfully synthesize a permissive enforcement mechanism for all examples.
