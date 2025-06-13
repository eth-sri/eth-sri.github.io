---
ref: gloaguen2024clues
title: "Discovering Spoofing Attempts on Language Model Watermarks"
authors: Thibaud Gloaguen, Nikola Jovanović, Robin Staab, Martin Vechev
year: 2025
month: 07
venue: ICML
projects: safeai,llm
bibtex: "@article{gloaguen2025clues,
  title = {Discovering Spoofing Attempts on Language Model Watermarks},
  author = {Gloaguen, Thibaud and Jovanović, Nikola and Staab, Robin and Vechev, Martin},
  year = {2025},
  journal = {{ICML}}
}"
paper: https://arxiv.org/pdf/2410.02693
code: https://github.com/eth-sri/watermark-spoofing-detection
---

LLM watermarks stand out as a promising way to attribute ownership of LLM-generated text. One threat to watermark credibility comes from spoofing attacks, where an unauthorized third party forges the watermark, enabling it to falsely attribute arbitrary texts to a particular LLM. Despite recent work demonstrating that state-of-the-art schemes are, in fact, vulnerable to spoofing, no prior work has focused on post-hoc methods to discover spoofing attempts. In this work, we for the first time propose a reliable statistical method to distinguish spoofed from genuinely watermarked text, suggesting that current spoofing attacks are less effective than previously thought. In particular, we show that regardless of their underlying approach, all current learning-based spoofing methods consistently leave observable artifacts in spoofed texts, indicative of watermark forgery. We build upon these findings to propose rigorous statistical tests that reliably reveal the presence of such artifacts and thus demonstrate that a watermark has been spoofed. Our experimental evaluation shows high test power across all learning-based spoofing methods, providing insights into their fundamental limitations and suggesting a way to mitigate this threat.
