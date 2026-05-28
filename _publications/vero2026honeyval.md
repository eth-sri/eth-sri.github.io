---
ref: vero2026honeyval
title: "Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots"
authors: Mark Vero, Fabian Kaczmarczyck, Ivan Petrov, Ilia Shumailov, Jamie Hayes, Niels Heinen, Tianqi Fan, Luca Invernizzi, Martin Vechev
year: 2026
month: 05
venue: preprint
projects: codellm,llmevals
bibtex: "@misc{vero2026honeyval,
  title = {Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots},
  author = {Vero, Mark and Kaczmarczyck, Fabian and Petrov, Ivan and Shumailov, Ilia and Hayes, Jamie and Heinen, Niels and Fan, Tianqi and Invernizzi, Luca and Vechev, Martin},
  year = {2026},
  note = {Preprint}
}"

paper: https://files.sri.inf.ethz.ch/website/papers/honeyval.pdf
code: https://github.com/google-research/honeyval
website: https://honeyval.xyz/
---

Honeypots are decoy systems mimicking real system components designed to defend against cyber attacks. Recently, LLMs increasingly serve as simulation backbones for honeypots. They enable defenders to construct high-interaction honeypots with low system security risks. However, LLM-powered honeypot development lacks a unified evaluation framework. Most evaluations consist of measuring response similarity on fixed commands, manual testing, or real-world deployment. These methods are often not scalable for development, reproducible across evaluations, representative of practical attacks, or adaptable to various attacker and honeypot configurations. In this work, we bridge this gap and propose Honeyval, a comprehensive evaluation framework for LLM-powered HTTP honeypots. We address the limitations of prior evaluations by grounding the honeypots in 16 backend applications, using AI hacking agents as attackers, employing two control tasks to monitor agent and honeypot capabilities across customizations, and defining clear and verifiable exploit goals for the attacker. Using Honeyval, we conduct an extensive evaluation of recent cost-efficient LLMs as HTTP honeypots. Our experiments highlight the promise of LLM-powered honeypots; they lead to substantially longer interactions with the attacker than rule-based baseline honeypots and are far less frequently detected even by frontier models, all while, on average, preserving a running cost advantage against agentic attackers. Further, we experiment with different counter-offensive honeypots configurations, and observe unique trade-offs, such as longer interactions at the cost of increased detection.