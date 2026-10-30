---
ref: paina2026probe
title: "PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix"
authors: Marco Paina, Mark Niklas Müller, Niels Mündler-Sasahara, Martin Vechev
year: 2026
month: 10
venue: arXiv
projects: codellm,llmevals
paper: https://arxiv.org/abs/2610.35987
website: https://probebench.com/
bibtex: "@misc{paina2026probe,
  title = {PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix},
  author = {Marco Paina and Mark Niklas Müller and Niels Mündler-Sasahara and Martin Vechev},
  year = {2026},
  eprint = {2610.35987},
  archivePrefix = {arXiv},
  primaryClass = {cs.SE},
  url = {https://arxiv.org/abs/2610.35987}
}"
---

Proactive bug discovery is an important software-engineering problem. Even though coding agents are already widely deployed in this domain, their capabilities remain understudied. In particular, the challenging task of finding all bugs that human maintainers would repair across an entire repository has not been studied yet. To close this gap, we introduce PROBE, a benchmark consisting of all 2,457 bugs fixed over the course of 18 months across 20 diverse GitHub repositories, together with a method for matching candidate findings to this partial reference set. We evaluate coding agents across frontier models and find they all achieve a recall of below 21% and a precision of less than 9% with respect to the reference set. While stronger models increase recall substantially from 8% to 17%, they do not improve precision. Surprisingly, despite the low precision, LLM and human evaluators still judge 85% of findings valid. Crucially, we find that found bug distributions are similar across agents but differ substantially from those of bugs fixed by maintainers. The practical relevance of bug discovery and the low recall of frontier models make this benchmark a valuable resource for both model users and developers.
