---
ref: gloaguen2024detectingwatermarks
title: "Black-Box Detection of Language Model Watermarks"
authors: Thibaud Gloaguen, Nikola Jovanović, Robin Staab, Martin Vechev
year: 2025
month: 04
venue: ICLR
projects: safeai,llm
bibtex: "@article{gloaguen2024detectingwatermarks,
  title = {Black-Box Detection of Language Model Watermarks},
  author = {Gloaguen, Thibaud and Jovanović, Nikola and Staab, Robin and Vechev, Martin},
  year = {2024},
  eprint={2405.20777},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/gloaguen2024detectingwatermarks.pdf
---

Watermarking has emerged as a promising way to detect LLM-generated text. To apply a watermark an LLM provider, given a secret key, augments generations with a signal that is later detectable by any party with the same key. Recent work has proposed three main families of watermarking schemes, two of which focus on the property of preserving the LLM distribution. This is motivated by it being a tractable proxy for maintaining LLM capabilities, but also by the idea that concealing a watermark deployment makes it harder for malicious actors to hide misuse by avoiding a certain LLM or attacking its watermark. Yet, despite much discourse around detectability, no prior work has investigated if any of these scheme families are detectable in a realistic black-box setting. We tackle this for the first time, developing rigorous statistical tests to detect the presence of all three most popular watermarking scheme families using only a limited number of black-box queries. We experimentally confirm the effectiveness of our methods on a range of schemes and a diverse set of open-source models. Our findings indicate that current watermarking schemes are more detectable than previously believed, and that obscuring the fact that a watermark was deployed may not be a viable way for providers to protect against adversaries. We further apply our methods to test for watermark presence behind the most popular public APIs: GPT4, Claude 3, Gemini 1.0 Pro, finding no strong evidence of a watermark at this point in time.
