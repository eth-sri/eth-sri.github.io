---
ref: balunovic2025matharena
title: "MathArena: Evaluating LLMs on Uncontaminated Math Competitions"
authors: Mislav Balunović, Jasper Dekoninck, Nikola Jovanović, Ivo Petrov, Martin Vechev
year: 2025
month: 12
venue: NeurIPS Datasets and Benchmarks
projects: mathllm,llmevals
bibtex: "@article{balunovic2025matharena,
	title = {MathArena: Evaluating LLMs on Uncontaminated Math Competitions},
    author = {Mislav Balunović and Jasper Dekoninck and Ivo Petrov and Nikola Jovanović and Martin Vechev},
	journal = {Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmark},
  year={2025}
}"
paper: https://arxiv.org/pdf/2505.23281
code: https://github.com/eth-sri/matharena
website: https://matharena.ai/
---

The rapid advancement of reasoning capabilities in large language models (LLMs) has led to notable improvements on mathematical benchmarks. However, many of the most commonly used evaluation datasets (e.g., AIME 2024) are widely available online, making it difficult to disentangle genuine reasoning from potential memorization. Furthermore, these benchmarks do not evaluate proof-writing capabilities, which are crucial for many mathematical tasks. To address this, we introduce MathArena, a new benchmark based on the following key insight: recurring math competitions provide a stream of high-quality, challenging problems that can be used for real-time evaluation of LLMs. By evaluating models as soon as new problems are released, we effectively eliminate the risk of contamination. Using this framework, we find strong signs of contamination in AIME 2024. Nonetheless, evaluations on harder competitions, such as SMT 2025—published well after model release dates—demonstrate impressive reasoning capabilities in top-performing models. MathArena is also the first benchmark for proof-writing capabilities. On USAMO 2025, even top models score below 25%, far behind their performance on final-answer tasks. So far, we have evaluated 30 models across five competitions, totaling 149 problems. As an evolving benchmark, MathArena will continue to track the progress of LLMs on newly released competitions, ensuring rigorous and up-to-date evaluation of mathematical reasoning.