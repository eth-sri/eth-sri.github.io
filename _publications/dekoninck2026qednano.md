---
ref: dekoninck2025qednano
title: "QED-Nano: Teaching a Tiny Model to Prove Hard Theorems"
authors: LM-Provers, Yuxiao Qu, Amrith Setlur, Jasper Dekoninck, Edward Beeching, Jia Li, Ian Wu, Lewis Tunstall, Aviral Kumar
year: 2026
month: 4
venue: ArXiv
projects: mathllm
bibtex: '@article{lmprovers2026qednano,
      title={QED-Nano: Teaching a Tiny Model to Prove Hard Theorems}, 
      author={LM-Provers and Yuxiao Qu and Amrith Setlur and Jasper Dekoninck and Edward Beeching and Jia Li and Ian Wu and Lewis Tunstall and Aviral Kumar},
      year={2026},
      eprint={2604.04898},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2604.04898}, 
}'
paper: https://arxiv.org/abs/2604.04898
code: https://github.com/CMU-AIRe/QED-Nano
---
Proprietary AI systems have recently demonstrated impressive capabilities on complex proof-based problems, with gold-level performance reported at the 2025 International Mathematical Olympiad (IMO). However, the training pipelines behind these systems remain largely undisclosed, and their reliance on large "internal" models and scaffolds makes them expensive to run, difficult to reproduce, and hard to study or improve upon. This raises a central question: can small, open models also be trained to achieve competitive reasoning performance on difficult Olympiad-level math? In this paper, we answer this question by building QED-Nano, a 4B model post-trained for Olympiad-level proofs. Our training recipe has three stages: (1) supervised fine-tuning to imbue good proof-writing styles by distilling from DeepSeek-Math-V2, (2) reinforcement learning (RL) with rubric-based rewards, and (3) expanding RL with a reasoning cache, which decomposes long proofs into iterative summarize-and-refine cycles and enables stronger test-time reasoning. QED-Nano surpasses the proof-generation performance of much larger open models, including Nomos-1 and GPT-OSS-120B, and approaches the performance of proprietary models like Gemini 3 Pro, at a fraction of the inference cost. To support further research on open mathematical reasoning, we release the full QED-Nano pipeline, including the QED-Nano and QED-Nano-SFT models, the FineProofs-SFT and FineProofs-RL datasets, and the training and evaluation code.