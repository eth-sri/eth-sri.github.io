---
ref: beurerkellner2023lmql_actions
title: "Large Language Models are Zero-Shot Multi-Tool Users"
authors: Luca Beurer-Kellner*,  Marc Fischer*, Martin Vechev
year: 2023
month: 7
venue: Knowlege and Logical Reasoning Workshop -- ICML
projects: cclm
bibtex: "@misc{BeuererkellnerFV2023,
			title     = {Large Language Models are Zero-Shot Multi-Tool Users},
			venue     = {ICML Workshop on Knowledge and Logical Reasoning in the Era of Data-Driven Learning},
			year={2023},
			author    = {Luca Beurer-Kellner and
      		Marc Fischer and
      		Martin Vechev},
			}"
paper: https://files.sri.inf.ethz.ch/website/papers/lmql_actions.pdf
code: https://github.com/eth-sri/lmql
---

% This text will be sanitized and placed into lqa-output/abstract.txt
We introduce LMQL Actions, a framework and programming environment to facilitate the implementation of tool-augmented language models (LMs).
Concretely, we augment LMs with the ability to call actions (arbitrary Python functions), and experiment with different ways of tool discovery and invocation.
We find that, while previous works heavily rely on few-shot prompting to teach tool use, a zero-shot, instruction-only approach is enough to achieve competitive performance. At the same time, LMQL Actions zero-shot approach also offers a much simpler programming interface, not requiring any involved demonstrations. Building on this, we show how LMQL Actions enables LLMs to automatically discover and combine multiple tools to solve complex tasks. Overall, we find that inline tool use as enabled by LMQL Actions, outperforms existing tool augmentation approaches, both in arithmetic reasoning tasks and text-based question answering.