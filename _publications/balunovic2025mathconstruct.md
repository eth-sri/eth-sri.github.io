---
ref: balunovic2025mathconstruct
title: "MathConstruct: Challenging LLM Reasoning with Constructive Proofs"
authors: Mislav Balunović*, Jasper Dekoninck*, Nikola Jovanović, Ivo Petrov, Martin Vechev
year: 2025
month: 07
venue: ICML
projects: mathllm,llmevals
bibtex: '@article{balunovic2025mathconstruct,
    title={MathConstruct: Challenging LLM Reasoning with Constructive Proofs},
    author={Mislav Balunović and Jasper Dekoninck and Nikola Jovanović and Ivo Petrov and Martin Vechev},
    year={2025},
    journal={{ICML}}
}'
code: https://github.com/eth-sri/mathconstruct
paper: https://arxiv.org/pdf/2502.10197?
---
While Large Language Models (LLMs) demonstrate impressive performance in mathematics, existing math benchmarks come with significant limitations. Many focus on problems with fixed ground-truth answers, and are often saturated due to problem simplicity or the viability of guessing or memorization. Crucially, they capture only a narrow subset of relevant math problems. To address this research gap, we introduce \mc, a new benchmark of 126 challenging problems sourced from various math competitions, which targets constructive proofs, a widely encountered problem type requiring the construction of mathematical objects with specific properties. These proofs are particularly suitable for LLM evaluation, as solution correctness can be easily verified. Our automated verifiers also enable MathConstruct to generate problem variations, used to evaluate robustness. State-of-the-art LLMs solve only 54% of MathConstruct problems, highlighting its complexity and importance for LLM evaluation.




