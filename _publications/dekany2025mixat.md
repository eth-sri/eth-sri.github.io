---
ref: dekany2025mixat
title: "MixAT: Combining Continuous and Discrete Adversarial Training for LLMs"
authors: Csaba Dékány*, Stefan Balauca*, Robin Staab, Dimitar I. Dimitrov, Martin Vechev
year: 2025
month: 12
venue: NeurIPS
projects: llmsecpriv
bibtex: '@inproceedings{
			dekany2025mixat,
			title={Mix{AT}: Combining Continuous and Discrete Adversarial Training for {LLM}s},
			author={saba Dékány and Stefan Balauca and Dimitar I. Dimitrov and Robin Staab and Martin Vechev},
			booktitle={The Thirty-ninth Annual Conference on Neural Information Processing Systems},
			year={2025},
			url={https://openreview.net/forum?id=NG7kM4wxaN}
		}'
paper: https://arxiv.org/abs/2505.16947
code: https://github.com/insait-institute/MixAT
---

Despite recent efforts in Large Language Model (LLM) safety and alignment, current adversarial attacks on frontier LLMs can still consistently force harmful generations. Although adversarial training has been widely studied and shown to significantly improve the robustness of traditional machine learning models, its strengths and weaknesses in the context of LLMs are less understood. Specifically, while existing discrete adversarial attacks are effective at producing harmful content, training LLMs with concrete adversarial prompts is often computationally expensive, leading to reliance on continuous relaxations. At the same time, despite their effectiveness and generalization capabilities, training with continuous perturbations does not always capture the full spectrum of vulnerabilities exploited by discrete attacks. In this work, we aim to bridge this gap by introducing MixAT, a novel method that combines stronger discrete and faster continuous attacks during training. We rigorously evaluate MixAT across a wide spectrum of state-of-the-art attacks, proposing the At Least One Attack Success Rate (ALO-ASR) metric to capture the worst-case vulnerability of models. We show MixAT achieves substantially better robustness (ALO-ASR < 20%) compared to prior defenses (ALO-ASR > 50%), while maintaining a runtime comparable to methods based on continuous relaxations. We further analyze MixAT in realistic deployment settings, exploring how chat templates, quantization, low-rank adapters, and temperature affect both adversarial training and evaluation, revealing additional blind spots in current methodologies. Our results demonstrate that MixAT's discrete-continuous defense offers a principled and superior robustness-accuracy tradeoff with minimal computational overhead, highlighting its promise for building safer LLMs. We provide our code and models at https://github.com/insait-institute/MixAT.