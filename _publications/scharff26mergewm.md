---
ref: scharff26mergewm
title: "Making Open-Source Text LLM Watermarks Durable Against Merging"
authors: Luisa Scharff, Thibaud Gloaguen, Robin Staab, Martin Vechev
year: 2026
month: 05
venue: AI4GOOD @ ICML
projects: watermarks
bibtex: "@inproceedings{
scharff26mergewm,
title={Making Open-Source Text {LLM} Watermarks Durable Against Merging},
author={Luisa Scharff and Thibaud Gloaguen and Robin Staab and Martin Vechev},
booktitle={Trustworthy AI for Good (AI4GOOD) Workshop @ ICML 2026},
year={2026},
url={https://openreview.net/forum?id=84maDBcTYn}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/mergewm.pdf
---

Open-source LLMs (OSMs) are reaching near state-of-the-art performance, prompting prior works to trace the text they generate by embedding text watermarking algorithms directly into their weights. Yet, OSMs are subject to post-training modifications, which has been shown to remove the watermark. Model merging in particular, a prominent method used for combining expert knowledge and preventing catastrophic forgetting, strongly removes such OSMs watermarks. A key question is how to enable OSM watermarks that survive subsequent merging. In this work, we show for the first time how to design an OSM watermark that is durable against model merging. We propose Merge-Adversarial Training, an adversarial training algorithm to distill text watermarks into model weights while being robust to subsequent model merging. Our approach consistently outperforms all baselines (e.g. with SLERP up to +51 percentage points (pp) TPR@1%FPR with +25 pp on average) while preserving downstream capabilities. We also for the first time evaluate OSM watermarks against realistic merge scenarios, representing common use-cases such as combining expert capabilities or preventing catastrophic forgetting, and with 3 prominent merging algorithms. More broadly, our findings suggest that adversarial training is a reliable approach for increasing OSM watermark durability against post-training modifications.