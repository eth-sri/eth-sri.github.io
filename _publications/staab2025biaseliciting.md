---
ref: staab2025bias
title: "Adaptive Generation of Bias-Eliciting Questions for LLMs"
authors: Robin Staab, Jasper Dekoninck, Maximilian Baader, Martin Vechev
year: 2025
month: 10
venue: ArXiv
projects: llmevals
bibtex: "@article{staab2025bias,
      title={Adaptive Generation of Bias-Eliciting Questions for LLMs}, 
      author={Robin Staab and Jasper Dekoninck and Maximilian Baader and Martin Vechev},
      year={2025},
      eprint={2510.12857},
      archivePrefix={arXiv},
      primaryClass={cs.CY},
      url={https://arxiv.org/abs/2510.12857}, 
}"
paper: https://files.sri.inf.ethz.ch/website/papers/staab2025bias.pdf
code: https://github.com/eth-sri/cab
---

Large language models (LLMs) are now widely deployed in user-facing applications, reaching hundreds of millions worldwide. As they become integrated into everyday tasks, growing reliance on their outputs raises significant concerns. In particular, users may unknowingly be exposed to model-inherent biases that systematically disadvantage or stereotype certain groups. However, existing bias benchmarks continue to rely on templated prompts or restrictive multiple-choice questions that are suggestive, simplistic, and fail to capture the complexity of real-world user interactions. In this work, we address this gap by introducing a counterfactual bias evaluation framework that automatically generates realistic, open-ended questions over sensitive attributes such as sex, race, or religion. By iteratively mutating and selecting bias-inducing questions, our approach systematically explores areas where models are most susceptible to biased behavior. Beyond detecting harmful biases, we also capture distinct response dimensions that are increasingly relevant in user interactions, such as asymmetric refusals and explicit acknowledgment of bias. Leveraging our framework, we construct CAB, a human-verified benchmark spanning diverse topics, designed to enable cross-model comparisons. Using CAB, we analyze a range of LLMs across multiple bias dimensions, revealing nuanced insights into how different models manifest bias. For instance, while GPT-5 outperforms other models, it nonetheless exhibits persistent biases in specific scenarios. These findings underscore the need for continual improvements to ensure fair model behavior.