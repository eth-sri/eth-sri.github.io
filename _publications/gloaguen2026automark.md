---
ref: gloaguen2026automark
title: "AutoMark: Enabling Autoresearch to Discover Better LLM Watermarks"
authors: Thibaud Gloaguen, Robin Staab, Martin Vechev
year: 2026
month: 9
day: 29
venue: arXiv
projects: watermarks
bibtex: '@article{gloaguen2026automark,
  title={AutoMark: Enabling Autoresearch to Discover Better LLM Watermarks},
  author={Gloaguen, Thibaud and Staab, Robin and Vechev, Martin},
  journal={arXiv preprint arXiv:2609.37310},
  year={2026},
  url={https://arxiv.org/abs/2609.37310}
}'
paper: https://arxiv.org/abs/2609.37310
code: https://github.com/eth-sri/automark
blogpost: automark
---

With LLM watermarking being deployed commercially and now required by regulations, improving its reliability and effectiveness has become crucial. Yet, recent progress in the field of LLM watermarking has increasingly been driven by improving details of existing methods, an effort fundamentally limited by the pace of human researchers. In this work, we enable for the first time the autonomous discovery of new distortion-free state-of-the-art watermarking schemes.

To enable this, we (i) establish strict criteria to ensure that watermarks are reliable (e.g., they do not have an unexpectedly high false positive rate), (ii) propose rigorous statistical tests to automatically evaluate whether a watermarking scheme satisfies our criteria, and (iii) design an evaluation suite to rank watermarks along three key dimensions: detectability, quality, and robustness.

By running our framework with 3 frontier models (GPT-6 Astra, Opus 5, Gemini-3.8 Flash), we discover over 50 different watermarking schemes, including several that outperform prior works along all key dimensions. We complement this by a manual study of the discovered schemes, distilling the key ideas into smaller components, and individually studying the impact of each component across dimensions (detectability, quality, robustness) to better understand how the proposed schemes operate.

Importantly, we find that the agents, on top of improving existing ideas, also discover fundamentally new ideas (e.g., aligning watermark scores with random per-request direction). Overall, our work establishes the first steps of fully autonomous watermarking research, enabling the discovery of more reliable and effective watermarks.
