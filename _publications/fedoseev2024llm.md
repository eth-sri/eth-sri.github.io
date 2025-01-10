---
ref: fedoseev2024llm
title: "Constraint-Based Synthetic Data Generation for LLM Mathematical Reasoning"
authors: Timofey Fedoseev, Dimitar I. Dimitrov, Timon Gehr, Martin Vechev
year: 2024
month: 12
venue: Workshop on Mathematical Reasoning, NeurIPS
projects: safeai
bibtex: '@inproceedings{
			fedoseev2024llm,
			title={Constraint-Based Synthetic Data Generation for LLM Mathematical Reasoning},
			author={Timofey Fedoseev and Dimitar Iliev Dimitrov and Timon Gehr and Martin Vechev},
			booktitle={The 4th Workshop on Mathematical Reasoning and AI at NeurIPS'24},
			year={2024},
			url={https://openreview.net/forum?id=hR4Hskr4GX}
		}'
paper: https://files.sri.inf.ethz.ch/z3_llm/z3_llm.pdf
poster: https://files.sri.inf.ethz.ch/z3_llm/z3_llm_poster.png
---
Mathematical reasoning with large language models (LLMs) is an emerging research area. A recent breakthrough is the use of off-the-shelf tools LLMs are trained to utilize to offload complex tasks they cannot perform independently. Unfortunately, this approach is limited to popular tools, as many specialized tools lack the data to train these models on. Motivated by our observation that the current tools used with LLMs are insufficient for solving counting problems, in this work, we explore the problem of using Satisfiability Modulo Theories (SMT) solvers with LLMs. Namely, we leverage the SMT grammar to generate synthetic data consisting of problem statements and their solutions represented as Python code interacting with the Z3 API. Our experiments show that fine-tuning LLMs on this dataset substantially enhances their ability to generate accurate Z3 constraint encodings and improves their overall mathematical problem-solving capabilities.