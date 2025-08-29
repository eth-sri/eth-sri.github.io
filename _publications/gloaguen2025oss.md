---
ref: gloaguen2025oss
title: "Towards Watermarking of Open-Source LLMs"
authors: Thibaud Gloaguen, Nikola Jovanović, Robin Staab, Martin Vechev
year: 2025
month: 04
venue: WMARK @ ICLR
projects: watermarks
bibtex: "@article{gloaguen2025oss,
  title = {Towards Watermarking of Open-Source LLMs},
  author = {Gloaguen, Thibaud and Jovanović, Nikola and Staab, Robin and Vechev, Martin},
  year = {2025},
  eprint={2502.10525},
  archivePrefix={arXiv},
  primaryClass={cs.CR}
}"
paper: https://arxiv.org/pdf/2502.10525
code: https://github.com/eth-sri/durability-oss-watermarks
---

While watermarks for closed LLMs have matured and have been included in largescale deployments, these methods are not applicable to open-source models, which allow users full control over the decoding process. This setting is understudied yet critical, given the rising performance of open-source models. In this work, we lay the foundation for systematic study of open-source LLM watermarking. For the first time, we explicitly formulate key requirements, including durability against common model modifications such as model merging, quantization, or finetuning, and propose a concrete evaluation setup. Given the prevalence of these modifications, durability is crucial for an open-source watermark to be effective. We survey and evaluate existing methods, showing that they are not durable. We also discuss potential ways to improve their durability and highlight remaining challenges. We hope our work enables future progress on this important problem.