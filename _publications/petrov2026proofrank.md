---
ref: petrov2026proofrank
title: "Not All Proofs Are Equal: Evaluating LLM Proof Quality Beyond Correctness"
authors: Ivo Petrov, Jasper Dekoninck, Dimitar I. Dimitrov, Martin Vechev
year: 2026
month: 05
venue: AI4Math@ICML
projects: mathllm,llmevals
bibtex: "@misc{petrov2026proofsequalevaluatingllm,
      title={Not All Proofs Are Equal: Evaluating LLM Proof Quality Beyond Correctness}, 
      author={Ivo Petrov and Jasper Dekoninck and Dimitar I. Dimitrov and Martin Vechev},
      year={2026},
      eprint={2605.10379},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.10379}, 
}"
paper: https://arxiv.org/pdf/2605.10379
code: https://github.com/insait-institute/proofrank
---
Large language models (LLMs) have become capable mathematical problem-solvers, often producing correct proofs for challenging problems. However, correctness alone is not sufficient: mathematical proofs should also be clear, concise, insightful, and transferable to other problems. While this proof quality is subjective and depends on the reader and context, many of its components are concrete and broadly valued. In this work, we identify such components and introduce ProofRank, a benchmark curated from challenging mathematical competitions. ProofRank evaluates several scalable proxies of proof quality: (i) conciseness, measuring whether proofs avoid unnecessary steps; (ii) computational ease, measuring the extent to which a proof relies on tedious calculations; (iii) cognitive simplicity, measuring how accessible the used proof techniques are; (iv) diversity, measuring how varied a model's proofs for a single problem are; and (v) adaptivity, measuring whether a model can follow a specified proof technique. Across models, we find substantial differences in proof quality that are not captured by correctness-only benchmarks. We also observe significant trade-offs between proof-quality metrics and correctness, suggesting that future evaluations of mathematical reasoning should measure how useful LLM-generated proofs are.