---
ref: petrov2025usamo
title: "Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad"
authors: Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunović, Nikola Jovanović, Martin Vechev
year: 2025
month: 07
venue: AI4Math@ICML
projects: mathllm
bibtex: "@article{petrov2025usamo,
   title={Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad}, 
   author={Ivo Petrov and Jasper Dekoninck and Lyuben Baltadzhiev and Maria Drencheva and Kristian Minchev and Mislav Balunović and Nikola Jovanović and Martin Vechev},
   year={2025},
   archivePrefix={arXiv},
   primaryClass={cs.CL}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/petrov2025usamo.pdf
code: https://github.com/eth-sri/matharena
website: https://matharena.ai/
---
Recent math benchmarks for large language models (LLMs) such as MathArena indicate that state-of-the-art reasoning models achieve impressive performance on mathematical competitions like AIME, with the leading model, O 3- MINI, achieving scores comparable to top human competitors. However, these benchmarks evaluate models solely based on final numerical answers, neglecting rigorous reasoning and proof generation which are essential for real-world mathematical tasks. To address this, we introduce the first comprehensive evaluation of full-solution reasoning for challenging mathematical problems. Using expert human annotators, we evaluated several state-of-the-art reasoning models on the six problems from the 2025 USAMO within hours of their release. Our results reveal that all tested models struggled significantly, achieving less than 5% on average. Through detailed analysis of reasoning traces, we identify the most common failure modes and find several unwanted artifacts arising from the optimization strategies employed during model training. Overall, our results suggest that current LLMs are inadequate for rigorous mathematical reasoning tasks, highlighting the need for substantial improvements in reasoning and proof generation capabilities.