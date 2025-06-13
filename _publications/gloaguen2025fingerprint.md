---
ref: gloaguen2025fingerprint
title: "Robust LLM Fingerprinting via Domain-Specific Watermarks"
authors: Thibaud Gloaguen, Robin Staab, Nikola Jovanović and Martin Vechev
year: 2025
month: 05
venue: arXiv
projects: safeai,llm
bibtex: "@misc{gloaguen2025fingerprint,
    title={Robust LLM Fingerprinting via Domain-Specific Watermarks}, 
    author={Thibaud Gloaguen and Robin Staab and Nikola Jovanović and Martin Vechev},
    year={2025},
    eprint={2505.16723},
    archivePrefix={arXiv},
    primaryClass={cs.CR},
    url={https://arxiv.org/abs/2505.16723}, 
}"
paper: https://arxiv.org/pdf/2505.16723
code: https://github.com/eth-sri/robust-llm-fingerprints
---

As open-source language models (OSMs) grow more capable and are widely shared and finetuned, ensuring model provenance, i.e., identifying the origin of a given model instance, has become an increasingly important issue. At the same time, existing backdoor-based model fingerprinting techniques often fall short of achieving key requirements of real-world model ownership detection. In this work, we build on the observation that while current open-source model watermarks fail to achieve reliable content traceability, they can be effectively adapted to address the challenge of model provenance. To this end, we introduce the concept of domain-specific watermarking for model fingerprinting. Rather than watermarking all generated content, we train the model to embed watermarks only within specified subdomains (e.g., particular languages or topics). This targeted approach ensures detection reliability, while improving watermark durability and quality under a range of real-world deployment settings. Our evaluations show that domain-specific watermarking enables model fingerprinting with strong statistical guarantees, controllable false positive rates, high detection power, and preserved generation quality. Moreover, we find that our fingerprints are inherently stealthy and naturally robust to real-world variability across deployment scenarios. 