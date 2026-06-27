---
ref: gloaguen2026coding
title: "Coding Agents Don't Know When to Act"
authors: Thibaud Gloaguen, Niels Mündler, Mark Niklas Mueller, Veselin Raychev, Martin Vechev
year: 2026
month: 05
venue: AIWILD @ ICML
projects: codellm
bibtex: |
  @inproceedings{
  gloaguen2026coding,
  title={Coding Agents Don't Know When to Act},
  author={Thibaud Gloaguen and Niels M{\"u}ndler and Mark Niklas Mueller and Veselin Raychev and Martin Vechev},
  booktitle={Second Workshop on Agents in the Wild: Safety, Security, and Beyond},
  year={2026},
  url={https://openreview.net/forum?id=CVg4Honh4Y}
  }
paper: https://arxiv.org/abs/2605.07769
---

Coding agents are increasingly deployed to autonomously maintain software, including to resolve user-reported issues: a bug report comes in and the agent creates a patch to address it. However, in any real-world deployment, they will encounter stale bug reports about issues that have already been resolved. Agents should recognize this and abstain from modifying the code to avoid accumulating technical debt.

To systematically evaluate whether current agents do so, we introduce FixedBench, a code benchmark with 200 human-verified coding tasks in which no code changes are required, testing five recent models across four agent harnesses. We find that even state-of-the-art models fail, proposing undesirable changes (excluding tests and documentation) in 35% to 65% of cases. Explicit instructions to reproduce the issue before patching partially address this issue but introduce a new failure mode: when an issue is partially fixed, they abstain even though a patch would still be needed.

More broadly, our results indicate that LLMs fall prey to an action bias: they choose to act even if inaction would be appropriate. To break this pattern, inaction needs to be explicitly framed as a path to success, which highlights an overreliance on human guidance implicit in current training objectives.
