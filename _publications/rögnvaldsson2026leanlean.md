---
ref: rögnvaldsson2026leanlean
title: "LeanLean: Benchmarking Repository-Scale Lean Proof Compression"
authors: Kári Rögnvaldsson, Niels Mündler-Sasahara, Jasper Dekoninck, Martin Vechev
year: 2026
month: 9
projects: mathllm
paper: https://github.com/eth-sri/lean-lean/blob/main/leanlean.pdf
code: https://github.com/eth-sri/lean-lean
website: https://leanleanbench.com/
---

As large language models (LLMs) formalize increasingly advanced mathematics, their proofs can span millions of lines of code. Producing more concise formalizations requires models to discover simpler arguments and extract reusable lemmas across large codebases. To measure this important capability, we introduce LeanLean, a benchmark consisting of 64 large-scale, real-world Lean repositories containing up to 174 thousand lines of code. Within a 12-hour time limit, models are tasked with reducing repository size while preserving the mathematical validity of their main theorems. To achieve maximal compression, models need to optimize at three levels of abstraction: (1) simplifying the underlying mathematical arguments, (2) restructuring proof dependencies by deleting and adding new declarations, and (3) applying syntactic optimizations. The best model, Opus 5, achieves an average compression score of 48.3%, while smaller models such as Gemini 3.8 Flash and GPT-5.6 Luna reach less than 25%. We find that most compression comes from restructuring proof dependencies by making previously used declarations unnecessary, while only Opus 5 and Muse Spark 1.3 achieve substantial gains through syntactic optimizations. LeanLean provides a strong testbed for evaluating models across a combination of capabilities, including long-context handling, mathematical theorem proving, and coding proficiency in Lean.
