---
ref: cusumano2018incremental
title: Incremental Inference for Probabilistic Programs
authors: Marco Cusumano-Towner, Benjamin Bichsel, Timon Gehr, Martin Vechev, Vikash K. Mansinghka
year: 2018
month: 06
venue: PLDI
projects: probabilistic-programming
awards:
bibtex: '@inproceedings{cusumano2018incremental,
  title={Incremental inference for probabilistic programs},
  author={Cusumano-Towner, Marco and Bichsel, Benjamin and Gehr, Timon and Vechev, Martin and Mansinghka, Vikash K},
  booktitle={Proceedings of the 39th ACM SIGPLAN Conference on Programming Language Design and Implementation},
  pages={571--585},
  year={2018},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/pldi18_interemental_inference_for_probabilistic_programs.pdf
talk: 
slides: 
---

We present a novel approach for approximate sampling in probabilistic programs based on incremental inference. The key idea is to adapt the samples for a program P into samples for a program Q, thereby avoiding the expensive sampling computation for program Q. To enable incremental inference in probabilistic programming, our work: (i) introduces the concept of a trace translator which adapts samples from P into samples of Q, (ii) phrases this translation approach in the context of sequential Monte Carlo (SMC), which gives theoretical guarantees that the adapted samples converge to the distribution induced by Q, and (iii) shows how to obtain a concrete trace translator by establishing a correspondence between the random choices of the two probabilistic programs. We implemented our approach in two different probabilistic programming systems and showed that, compared to methods that sample the program Q from scratch, incremental inference can lead to orders of magnitude increase in efficiency, depending on how closely related P and Q are.
