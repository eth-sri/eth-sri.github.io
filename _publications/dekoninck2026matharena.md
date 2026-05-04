---
ref: dekoninck2026matharena
title: "Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs"
authors: Jasper Dekoninck, Nikola Jovanović, Tim Gehrunger, Kári Rögnvalddson, Ivo Petrov, Chenhao Sun, Martin Vechev
year: 2026
month: 5
venue: ArXiv
projects: mathllm,llmevals
bibtex: '@article{dekoninck2026matharena,
      title={Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs}, 
      author={Jasper Dekoninck and Nikola Jovanović and Tim Gehrunger and Kári Rögnvalddson and Ivo Petrov and Chenhao Sun and Martin Vechev},
      year={2026},
      eprint={2605.00674},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.00674}, 
}'
paper: https://arxiv.org/pdf/2605.00674
code: https://github.com/eth-sri/matharena
website: https://matharena.ai/
---
Large language models (LLMs) are becoming increasingly capable mathematical collaborators, but static benchmarks are no longer sufficient for evaluating progress: they are often narrow in scope, quickly saturated, and rarely updated. This makes it hard to compare models reliably and track progress over time. Instead, we need evaluation platforms: continuously maintained systems that run, aggregate, and analyze evaluations across many benchmarks to give a comprehensive picture of model performance within a broad domain. In this work, we build on the original MathArena benchmark by substantially broadening its scope from final-answer olympiad problems to a continuously maintained evaluation platform for mathematical reasoning with LLMs. MathArena now covers a much wider range of tasks, including proof-based competitions, research-level arXiv problems, and formal proof generation in Lean. Additionally, we maintain a clear evaluation protocol for all models and regularly design new benchmarks as model capabilities improve to ensure that MathArena remains challenging. Notably, the strongest model, GPT-5.5, now reaches 98% on the 2026 USA Math Olympiad and 74% on research-level questions, showing that frontier models can now comfortably solve extremely challenging mathematical problems. This highlights the importance of continuously maintained evaluation platforms like MathArena to track the rapid progress of LLMs in mathematical reasoning.