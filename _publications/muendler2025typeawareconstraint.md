---
ref: muendler2025typeawareconstraint
title: "Type-Constrained Code Generation with Language Models"
authors: Niels Mündler<sup>†</sup>, Jingxuan He<sup>†</sup>, Hao Wang, Koushik Sen, Dawn Song, Martin Vechev
year: 2025
month: 4
venue: VerifAI, DL4C @ ICLR
awards: 
projects: safeai,llm
bibtex: "@inproceedings{
mundler2025typeaware,
title={Type-Constrained Code Generation with Language Models},
author={Niels M{\"u}ndler and Jingxuan He and Hao Wang and Koushik Sen and Dawn Song and Martin Vechev},
booktitle={ICLR 2025 Third Workshop on Deep Learning for Code},
year={2025},
url={https://arxiv.org/abs/2504.09246}
}"
paper: https://arxiv.org/abs/2504.09246
code: https://github.com/eth-sri/type-constrained-code-generation
---

Large language models (LLMs) have achieved notable success in code generation.  However, they still frequently produce uncompilable output because their next-token inference procedure does not model formal aspects of code.  Although constrained decoding is a promising approach to alleviate this issue, it has only been applied to handle either domain-specific languages or syntactic language features.  This leaves typing errors, which are beyond the domain of syntax and generally hard to adequately constrain.  To address this challenge, we introduce a type-constrained decoding approach that leverages type systems to guide code generation.  We develop novel prefix automata for this purpose and introduce a sound approach to enforce well-typedness based on type inference and a search over inhabitable types.  We formalize our approach on a simply-typed language and extend it to TypeScript to demonstrate practicality.  Our evaluation on HumanEval shows that our approach reduces compilation errors by more than half and increases functional correctness in code synthesis, translation, and repair tasks across LLMs of various sizes and model families, including SOTA open-weight models with more than 30B parameters. 