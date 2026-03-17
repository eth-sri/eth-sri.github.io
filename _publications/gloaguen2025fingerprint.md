---
ref: gloaguen2025fingerprint
title: "LLM Fingerprinting via Semantically Conditioned Watermarks"
authors: Thibaud Gloaguen, Robin Staab, Nikola Jovanović and Martin Vechev
year: 2026
month: 4
venue: ICLR
projects: watermarks
awards: Oral
bibtex: "@misc{gloaguen2025fingerprint,
    title={LLM Fingerprinting via Semantically Conditioned Watermarks}, 
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

Most LLM fingerprinting methods teach the model to respond to a few fixed queries with predefined atypical responses (keys). This memorization often does not survive common deployment steps such as finetuning or quantization, and such keys can be easily detected and filtered from LLM responses, ultimately breaking the fingerprint. To overcome these limitations we introduce LLM fingerprinting via semantically conditioned watermarks, replacing fixed query sets with a broad semantic domain, and replacing brittle atypical keys with a statistical watermarking signal diffused throughout each response. After teaching the model to watermark its responses only to prompts from a predetermined domain e.g., French language, the model owner can use queries from that domain to reliably detect the fingerprint and verify ownership. As we confirm in our thorough experimental evaluation, our fingerprint is both stealthy and robust to all common deployment scenarios.
