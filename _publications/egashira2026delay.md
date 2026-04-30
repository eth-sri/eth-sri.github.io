---
ref: egashira2026delay
title: "Delay, Plateau, or Collapse: Evaluating the Impact of Systematic Verification Error on RLVR"
authors: Kazuki Egashira, Mark Vero, Jasper Dekoninck, Florian E. Dorner, Robin Staab, Martin Vechev
year: 2026
month: 3
venue: arXiv
projects: llmevals
awards:
bibtex: "@misc{egashiradelay,
  title={Delay, Plateau, or Collapse: Evaluating the Impact of Systematic Verification Error on RLVR},
  author={Egashira, Kazuki and Vero, Mark and Dekoninck, Jasper and Dorner, Florian E and Staab, Robin and Vechev, Martin},
  year         = {2026},
  url          = {https://www.sri.inf.ethz.ch/publications/egashira2026delay}
}"

paper: https://files.sri.inf.ethz.ch/website/papers/egashira2026delay.pdf
code: https://github.com/eth-sri/llm-verifier-noise
website:
---

Reinforcement Learning with Verifiable Rewards (RLVR) has become a powerful approach for improving the reasoning capabilities of large language models (LLMs). While RLVR is designed for tasks with verifiable ground-truth answers, real-world verifiers (e.g., static code checkers) can introduce errors into the reward signal. Prior analyses have largely treated such errors as random and independent across samples, concluding that errors merely slow training with limited effect on final performance. How- ever, practical verifiers tend to exhibit systematic errors. This introduces a risk of models learning unwanted consistent behavior from a structurally incorrect reward signal. In this work, we study the impact of such sys- tematic verification errors on RLVR. Through controlled experiments on arithmetic tasks, we show that systematic false negatives lead to similar effects as random noise. On the other hand, systematic false positives can cause a wide range of behaviors from sub-optimal plateaus to performance collapse. Crucially, these outcomes are not determined by the overall error rate but by the specific pattern of introduced errors, making pre-hoc mitigation difficult. Our results show that, in contrast to prior conclusions, realistic verification errors can critically shape RLVR outcomes and that verifier quality has to be understood beyond its sample-level error rate.