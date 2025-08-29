---
ref: dekoninck2024controlled
title: "ConStat: Performance-Based Contamination Detection in Large Language Models"
authors: Jasper Dekoninck, Mark Niklas Müller, Martin Vechev
year: 2024
month: 12
venue: NeurIPS
projects: llmevals
bibtex: "@article{dekoninck2024constat,
      title={ConStat: Performance-Based Contamination Detection in Large Language Models}, 
      author={Jasper Dekoninck and Mark Niklas Müller and Martin Vechev},
      year={2024},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/dekoninck2024constat.pdf
code: https://github.com/eth-sri/ConStat
website: https://constat.ai
---

Public benchmarks play an essential role in the evaluation of large language models.  However, data contamination can lead to inflated performance, rendering them unreliable for model comparison. It is therefore crucial to detect contamination and estimate its impact on measured performance. Unfortunately, existing detection methods can be easily evaded and fail to quantify contamination. To overcome these limitations, we propose a novel definition of contamination as artificially inflated and non-generalizing benchmark performance instead of the inclusion of benchmark samples in the training data. This perspective enables us to detect any model with inflated performance, i.e., performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task. Based on this insight, we develop ConStat, a statistical method that reliably detects and quantifies contamination by comparing performance between a primary and reference benchmark relative to a set of reference models. We demonstrate the effectiveness of ConStat in an extensive evaluation of diverse model architectures, benchmarks, and contamination scenarios and find high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models.
