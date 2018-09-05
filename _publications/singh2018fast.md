---
ref: singh2018fast
title: Fast Numerical Program Analysis with Reinforcement Learning
authors: Gagandeep Singh, Markus Püschel, Martin Vechev
year: 2018
month: 07
venue: CAV
projects: numerical-analysis
awards:
bibtex: '@inproceedings{singh2018fast,
  title={Fast Numerical Program Analysis with Reinforcement Learning},
  author={Singh, Gagandeep and P{\"u}schel, Markus and Vechev, Martin},
  booktitle={International Conference on Computer Aided Verification},
  pages={211--229},
  year={2018},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/CAV18-RLPOLY_Paper.pdf
talk: 
slides: https://files.sri.inf.ethz.ch/website/slides/CAV18-RLPOLY_Slides.pdf
---

We show how to leverage reinforcement learning (RL) in order to speed up static program analysis. The key insight is to establish a correspondence between concepts in RL and those in analysis: a state in RL maps to an abstract program state in analysis, an action maps to an abstract transformer, and at every state, we have a set of sound transformers (actions) that represent different trade-offs between precision and performance. At each iteration, the agent (analysis) uses a policy learned offline by RL to decide on the transformer which minimizes loss of precision at fixpoint while improving analysis performance. Our approach leverages the idea of online decomposition (applicable to popular numerical abstract domains) to define a space of new approximate transformers with varying degrees of precision and performance. Using a suitably designed set of features that capture key properties of abstract program states and available actions, we then apply Q-learning with linear function approximation to compute an optimized context-sensitive policy that chooses transformers during analysis. We implemented our approach for the notoriously expensive Polyhedra domain and evaluated it on a set of Linux device drivers that are expensive to analyze. The results show that our approach can yield massive speedups of up to two orders of magnitude while maintaining precision at fixpoint.
