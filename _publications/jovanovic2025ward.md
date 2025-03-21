---
ref: jovanovic2025ward
title: "Ward: Provable RAG Dataset Inference via LLM Watermarks"
authors: Nikola Jovanović, Robin Staab, Maximilian Baader, Martin Vechev
year: 2025
month: 04
venue: ICLR
projects: safeai,llm
bibtex: "@article{jovanovic2025ward,
  title = {Ward: Provable RAG Dataset Inference via LLM Watermarks},
  author = {Jovanović, Nikola and Staab, Robin and Baader, Maximilian and Vechev, Martin},
  year = {2025},
  journal = {{ICLR}}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/jovanovic2025ward.pdf
code: https://github.com/eth-sri/ward
---

Retrieval-Augmented Generation (RAG) improves LLMs by enabling them to incorporate external data during generation. This raises concerns for data owners regarding unauthorized use of their content in RAG systems. Despite its importance, the challenge of detecting such unauthorized usage remains underexplored, with existing datasets and methodologies from adjacent fields being ill-suited for its study. In this work, we take several steps to bridge this gap. First, we formalize this problem as (black-box) RAG Dataset Inference (RAG-DI). To facilitate research on this challenge, we further introduce a novel dataset specifically designed for benchmarking RAG-DI methods under realistic conditions, and propose a set of baseline approaches. Building on this foundation, we introduce Ward, a RAG-DI method based on LLM watermarks that enables data owners to obtain rigorous statistical guarantees regarding the usage of their dataset in a RAG system. In our experimental evaluation, we show that Ward consistently outperforms all baselines across many challenging settings, achieving higher accuracy, superior query efficiency and robustness. Our work provides a foundation for future studies of RAG-DI and highlights LLM watermarks as a promising approach to this problem.
