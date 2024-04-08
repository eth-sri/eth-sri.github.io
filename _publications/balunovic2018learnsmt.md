---
ref: balunovic2018learnsmt
title: Learning to Solve SMT Formulas
authors: Mislav Balunović, Pavol Bielik, Martin Vechev
year: 2018
month: 12
bibtex: '@incollection{fastSMT,
  title = {Learning to Solve SMT Formulas},
  author = {Balunović, Mislav and Bielik, Pavol and Vechev, Martin},
  booktitle = {Advances in Neural Information Processing Systems 31},
  editor = {S. Bengio and H. Wallach and H. Larochelle and K. Grauman and N. Cesa-Bianchi and R. Garnett},
  pages = {10337--10348},
  year = {2018},
  publisher = {Curran Associates, Inc.},
  url = {http://papers.nips.cc/paper/8233-learning-to-solve-smt-formulas.pdf}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/fastsmt-2018.pdf
venue: NeurIPS
awards: Oral
talk: https://bit.ly/2BbpQtz
slides: https://files.sri.inf.ethz.ch/website/slides/neurips18_fastsmt.pdf
---

We present a new approach for learning to solve SMT formulas. We phrase the challenge of solving SMT formulas as a tree search problem where at each step a transformation is applied to the input formula until the formula is solved. Our approach works in two phases: first, given a dataset of unsolved formulas we learn a policy that for each formula selects a suitable transformation to apply at each step in order to solve the formula, and second, we synthesize a strategy in the form of a loop-free program with branches. This strategy is an interpretable representation of the policy decisions and is used to guide the SMT solver to decide formulas more efficiently, without requiring any modification to the solver itself and without needing to evaluate the learned policy at inference time. We show that our approach is effective in practice - it solves 17% more formulas over a range of benchmarks and achieves up to 100x runtime improvement over a state-of-the-art SMT solver.
