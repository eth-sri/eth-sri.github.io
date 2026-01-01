---
ref: vonarx2025autobaxbench
title: "AutoBaxBuilder: Bootstrapping Code Security Benchmarking "
authors: Tobias von Arx, Niels Mündler, Mark Vero, Max Baader, Martin Vechev
year: 2025
month: 12
venue: arxiv
awards: 
projects: codellm, llmevals
bibtex: "@article{vonarx2025autobaxbuilderbootstrappingcodesecurity,
      title={AutoBaxBuilder: Bootstrapping Code Security Benchmarking}, 
      author={Tobias von Arx and Niels Mündler and Mark Vero and Maximilian Baader and Martin Vechev},
      year={2025},
      eprint={2512.21132},
      archivePrefix={arXiv},
}",
paper: https://arxiv.org/abs/2512.21132
code: https://github.com/eth-sri/autobaxbuilder
---

As LLMs see wide adoption in software engineering, the reliable assessment of the correctness and security of LLM-generated code is crucial. Notably, prior work has demonstrated that security is often overlooked, exposing that LLMs are prone to generating code with security vulnerabilities. These insights were enabled by specialized benchmarks, crafted through significant manual effort by security experts. However, relying on manually-crafted benchmarks is insufficient in the long term, because benchmarks (i) naturally end up contaminating training data, (ii) must extend to new tasks to provide a more complete picture, and (iii) must increase in difficulty to challenge more capable LLMs. In this work, we address these challenges and present AutoBaxBuilder, a framework that generates tasks and tests for code security benchmarking from scratch. We introduce a robust pipeline with fine-grained plausibility checks, leveraging the code understanding capabilities of LLMs to construct functionality tests and end-to-end security-probing exploits. To confirm the quality of the generated benchmark, we conduct both a qualitative analysis and perform quantitative experiments, comparing it against tasks constructed by human experts. We use AutoBaxBuilder to construct entirely new tasks and release them to the public as AutoBaxBench, together with a thorough evaluation of the security capabilities of LLMs on these tasks. We find that a new task can be generated in under 2 hours, costing less than USD 10. 