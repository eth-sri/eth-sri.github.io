---
ref: jovanovic2024watermarkstealing
title: "Watermark Stealing in Large Language Models"
authors: Nikola Jovanović, Robin Staab, Martin Vechev
year: 2024
month: 05
venue: Workshop on Reliable and Responsible Foundation Models -- ICLR
projects: safeai,llm
bibtex: "@article{jovanovic2024watermarkstealing,
  title = {Watermark Stealing in Large Language Models},
  author = {Jovanović, Nikola and Staab, Robin and Vechev, Martin},
  year = {2024},
  eprint={2402.19361},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/jovanovic2024watermarkstealing.pdf
code: https://github.com/eth-sri/watermark-stealing
---

LLM watermarking has attracted attention as a promising way to detect AI-generated content, with some works suggesting that current schemes may already be fit for deployment. In this work we dispute this claim, identifying watermark stealing (WS) as a fundamental vulnerability of these schemes. We show that querying the API of the watermarked LLM to approximately reverse-engineer a watermark enables practical spoofing attacks, as suggested in prior work, but also greatly boosts scrubbing attacks, which was previously unnoticed. We are the first to propose an automated WS algorithm and use it in the first comprehensive study of spoofing and scrubbing in realistic settings. We show that for under $50 an attacker can both spoof and scrub state-of-the-art schemes previously considered safe, with average success rate of over 80%. Our findings challenge common beliefs about LLM watermarking, stressing the need for more robust schemes.