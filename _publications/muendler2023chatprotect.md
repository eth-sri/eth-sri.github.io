---
ref: muendler2023chatprotect
title: "Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation"
authors: Niels Mündler, Jingxuan He, Slobodan Jenko, Martin Vechev
year: 2024
month: 05
venue: ICLR
awards: 
projects: cclm
bibtex: "@inproceedings{muendler2023chatprotect,
			title     = {Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation},
			year         = {2024},
			booktitle    = {The Twelfth International Conference on Learning Representations}'
			author    = {Mündler, Niels and He, Jingxuan and Jenko, Slobodan and Vechev, Martin},
			}"
paper: https://arxiv.org/abs/2305.15852
code: https://github.com/eth-sri/ChatProtect
website: https://chatprotect.ai
---

Large language models (large LMs) are susceptible to producing text that contains hallucinated content. An important instance of this problem is self-contradiction, where the LM generates two contradictory sentences within the same context. In this work, we present a comprehensive investigation into self-contradiction for various instruction-tuned LMs, covering evaluation, detection, and mitigation. Our primary evaluation task is open-domain text generation, but we also demonstrate the applicability of our approach to shorter question answering. Our analysis reveals the prevalence of self-contradictions, e.g., in 17.7% of all sentences produced by ChatGPT. Self-contradiction also complements retrieval-based methods, as a large portion of them (e.g., 35.2% for ChatGPT) cannot be verified using online text. We then propose a novel prompting-based framework designed to effectively detect and mitigate self-contradictions. Our detector achieves high accuracy, e.g., around 80% F1 score when prompting ChatGPT. The mitigation algorithm iteratively refines the generated text to remove contradictory information while preserving text fluency and informativeness. Importantly, our entire framework is applicable to black-box LMs and does not require external databases. Our approach is practically effective and has been released as a push-button tool to benefit the public at [chatprotect.ai](https://chatprotect.ai/).
