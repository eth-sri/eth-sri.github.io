---
ref: wang2026secpi
title: "SecPI: Secure Code Generation with Reasoning Models via Security Reasoning Internalization"
authors: Hao Wang, Niels Mündler, Mark Vero, Jingxuan He, Dawn Song, Martin Vechev
year: 2026
month: 4
venue: arXiv
projects: llmsecpriv,codellm
bibtex: "@misc{wang2026secpisecurecodegeneration,
      title={SecPI: Secure Code Generation with Reasoning Models via Security Reasoning Internalization}, 
      author={Hao Wang and Niels Mündler and Mark Vero and Jingxuan He and Dawn Song and Martin Vechev},
      year={2026},
      eprint={2604.03587},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2604.03587}, 
}"

paper: https://arxiv.org/abs/2604.03587
code: https://github.com/moogician/SecPI
---

Reasoning language models (RLMs) are increasingly used in programming. Yet, even state-of-the-art RLMs frequently introduce critical security vulnerabilities in generated code. Prior training-based approaches for secure code generation face a critical limitation that prevents their direct application to RLMs: they rely on costly, manually curated security datasets covering only a limited set of vulnerabilities. At the inference level, generic security reminders consistently degrade functional correctness while triggering only shallow ad-hoc vulnerability analysis. To address these problems, we present SecPI, a fine-tuning pipeline that teaches RLMs to internalize structured security reasoning, producing secure code by default without any security instructions at inference time. SecPI filters existing general-purpose coding datasets for security-relevant tasks using an LLM-based classifier, generates high-quality security reasoning traces with a teacher model guided by a structured prompt that systematically enumerates relevant CWEs and mitigations, and fine-tunes the target model on pairs of inputs with no security prompt and teacher reasoning traces -- as a result, the model learns to reason about security autonomously rather than in response to explicit instructions. An extensive evaluation on security benchmarks with state-of-the-art open-weight reasoning models validates the effectiveness of our approach. For instance, SecPI improves the percentage of functionally correct and secure generations for QwQ 32B from 48.2% to 62.2% (+14.0 points) on CWEval and from 18.2% to 22.0% on BaxBench. Further investigation also reveals strong cross-CWE and cross-language generalization beyond training vulnerabilities. Even when trained only on injection-related CWEs, QwQ 32B generates correct and secure code 9.9% more frequently on held-out memory-safety CWEs. 