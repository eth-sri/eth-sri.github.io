---
ref: petrov2025brokenmath
title: "BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs"
authors: Ivo Petrov, Jasper Dekoninck, Martin Vechev
year: 2025
month: 10
venue: ArXiv
projects: mathllm,llmevals
bibtex: "@misc{petrov2025brokenmath,
      title={BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs}, 
      author={Ivo Petrov and Jasper Dekoninck and Martin Vechev},
      year={2025},
      eprint={2510.04721},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2510.04721}, 
}"
paper: https://arxiv.org/pdf/2510.04721
code: https://github.com/insait-institute/broken-math
website: https://www.sycophanticmath.ai/
---
Large language models (LLMs) have recently shown strong performance on mathematical benchmarks. At the same time, they are prone to hallucination and sycophancy, often providing convincing but flawed proofs for incorrect mathematical statements provided by users. This significantly limits the applicability of LLMs in theorem proving, as verification of these flawed proofs must be done manually by expert mathematicians. However, existing benchmarks that measure sycophancy in mathematics are limited: they focus solely on final-answer problems, rely on very simple and often contaminated datasets, and construct benchmark samples using synthetic modifications that create ill-posed questions rather than well-posed questions that are demonstrably false. To address these issues, we introduce BrokenMath, the first benchmark for evaluating sycophantic behavior in LLMs within the context of natural language theorem proving. BrokenMath is built from advanced 2025 competition problems, which are perturbed with an LLM to produce false statements and subsequently refined through expert review. Using an LLM-as-a-judge framework, we evaluate state-of-the-art LLMs and agentic systems and find that sycophancy is widespread, with the best model, GPT-5, producing sycophantic answers 29% of the time. We further investigate several mitigation strategies, including test-time interventions and supervised fine-tuning on curated sycophantic examples. These approaches substantially reduce, but do not eliminate, sycophantic behavior.