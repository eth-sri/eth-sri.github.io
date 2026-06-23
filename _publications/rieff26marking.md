---
ref: rieff26marking
title: "Marking the Wrong Symptoms: Evaluating LLM Watermarks in Medical Texts"
authors: Melanie Rieff, Robin Staab, Thibaud Gloaguen, Stefan Hegselmann, Martin Vechev
year: 2026
month: 05
venue: FM4LS @ ICML, AI4GOOD @ ICML
projects: watermarks
bibtex: "@inproceedings{
rieff2026marking,
title={Marking the Wrong Symptoms: Evaluating LLM Watermarks in Medical Texts},
author={Melanie Rieff and Robin Staab and Thibaud Gloaguen and Stefan Hegselmann and Martin Vechev},
booktitle={ICML 2026 3rd Workshop on Multi-modal Foundation Models and Large Language Models  for Life Sciences},
year={2026},
url={https://openreview.net/forum?id=Nmf9fBxCgq}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/rieff26marking.pdf
---

Large language models (LLMs) are increasingly integrated into clinical workflows, stressing the need for reliable traceability of model-generated output with watermarking. Yet, most watermarks are evaluated on general-purpose benchmarks, leaving domains like medicine, where small token-level perturbations can result in significant semantic changes, under-explored. In this work, we present the first rigorous study of how LLM watermarks affect medical performance, benchmarking 5 watermarking schemes across 11 LLMs and 7 VLMs on various tasks spanning unimodal and multimodal clinical reasoning. Importantly, we complement existing evaluations by introducing a human-expert-validated pipeline for systematically auditing medical reasoning quality, terminological precision, and induced hallucinations. Our results reveal that watermarking can induce substantial degradation across multiple failure modes, including lexical corruption, hallucinated terminology, and amplified misattribution or omission of image findings. Notably, we find that the absence of domain-specific analyses, combined with aggregate metrics that miss failures inherent to clinical text, can systematically obscure practical watermark-induced degradations. Our findings establish domain-specific evaluation as a prerequisite for the safe deployment of watermarked models in medicine, where current benchmarks can otherwise mask clinically consequential failures.