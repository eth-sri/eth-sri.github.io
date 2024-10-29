---
ref: yukhymenko2024synthetic
title: "A Synthetic Dataset for Personal Attribute Inference"
authors: Hanna Yukhymenko, Robin Staab, Mark Vero, Martin Vechev
year: 2024
month: 6
venue: NeurIPS Datasets and Benchmarks
projects: llm
bibtex: "@misc{yukhymenko2024synthetic,
      title={A Synthetic Dataset for Personal Attribute Inference}, 
      author={Hanna Yukhymenko and Robin Staab and Mark Vero and Martin Vechev},
      year={2024},
      eprint={2406.07217},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}"

paper: https://arxiv.org/abs/2406.07217
code: https://github.com/eth-sri/SynthPAI
---

Recently, powerful Large Language Models (LLMs) have become easily accessible to hundreds of millions of users worldwide. However, their strong capabilities and vast world knowledge do not come without associated privacy risks. In this work, we focus on the emerging privacy threat LLMs pose - the ability to accurately infer personal information from online texts. Despite the growing importance of LLM-based author profiling, research in this area has been hampered by a lack of suitable public datasets, largely due to ethical and privacy concerns associated with real personal data. In this work, we take two steps to address this problem: (i) we construct a simulation framework for the popular social media platform Reddit using LLM agents seeded with synthetic personal profiles; (ii) using this framework, we generate SynthPAI, a diverse synthetic dataset of over 7800 comments manually labeled for personal attributes. We validate our dataset with a human study showing that humans barely outperform random guessing on the task of distinguishing our synthetic comments from real ones. Further, we verify that our dataset enables meaningful personal attribute inference research by showing across 18 state-of-the-art LLMs that our synthetic comments allow us to draw the same conclusions as real-world data. Together, this indicates that our dataset and pipeline provide a strong and privacy-preserving basis for future research toward understanding and mitigating the inference-based privacy threats LLMs pose.