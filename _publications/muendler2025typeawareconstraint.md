---
ref: muendler2025typeawareconstraint
title: "Type-Aware Constraining for Code LLMs"
authors: Niels Mündler, Jingxuan He, Hao Wang, Koushik Sen, Dawn Song, Martin Vechev
year: 2025
month: 3
venue: VerifAI, DL4C @ ICLR
awards: 
projects: safeai,llm
bibtex: "@inproceedings{
mundler2025typeaware,
title={Type-Aware Constraining for Code {LLM}s},
author={Niels M{\"u}ndler and Jingxuan He and Hao Wang and Koushik Sen and Dawn Song and Martin Vechev},
booktitle={ICLR 2025 Third Workshop on Deep Learning for Code},
year={2025},
url={https://openreview.net/forum?id=DNAapYMXkc}
}"
paper: https://openreview.net/forum?id=DNAapYMXkc
---

Large Language Models (LLMs) have achieved notable success in code generation. However, they still frequently produce invalid code, as they do not precisely model formal aspects of programming languages. Constrained decoding is a promising approach to alleviate this issue and has been successfully applied to domain-specific languages and syntactic features, but is not able to enforce more semantic features, such as well-typedness. To address this issue, we introduce type-aware constrained decoding. We develop a novel prefix automata formalism and introduce a sound approach to guarantee existence of a type-safe completion of a partial program based on type inference and a search over inhabitable types. We implement type-aware constraining first for a foundational simply-typed language, then extend it to TypeScript. In our evaluation across state-of-the-art open-weight LLMs of up to 34B parameters and various model families, type-aware constraining reduces compilation errors by on average 70.9% and increases functional correctness by 16.2% in code synthesis, translation, and repair tasks.
