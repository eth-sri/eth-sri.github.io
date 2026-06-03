---
ref: zhan2026widening
title: "Widening the Gap: Exploiting LLM Quantization via Outlier Injection"
authors: Xiaohua Zhan, Kazuki Egashira, Robin Staab, Mark Vero, Martin Vechev
year: 2026
month: 5
venue: arXiv
projects: llmsecpriv
bibtex: "@article{zhan2026widening,
  title={Widening the Gap: Exploiting LLM Quantization via Outlier Injection},
  author={Zhan, Xiaohua and Egashira, Kazuki and Staab, Robin and Vero, Mark and Vechev, Martin},
  journal={arXiv preprint arXiv:2605.15152},
  year={2026}
}"

code: https://github.com/eth-sri/aio-quantization-attack
paper: https://arxiv.org/abs/2605.15152
---

LLM quantization has become essential for memory-efficient deployment. Recent work has shown that quantization schemes can pose critical security risks: an adversary may release a model that appears benign in full precision but exhibits malicious behavior once quantized by users. However, existing quantization-conditioned attacks have been limited to relatively simple quantization methods, where the attacker can estimate weight regions that remain invariant under the target quantization. Notably, prior attacks have consistently failed to compromise more popular and sophisticated schemes, limiting their practical impact. In this work, we introduce the first quantization-conditioned attack that consistently induces malicious behavior that can be triggered by a broad range of advanced quantization techniques, including AWQ, GPTQ, and GGUF I-quants. Our attack exploits a simple property shared by many modern quantization methods: large outliers can cause other weights to be rounded to zero. Consequently, by injecting outliers into specific weight blocks, an adversary can therefore induce a targeted, predictable weight collapse in the model. This effect can be used to craft seemingly benign full-precision models that exhibit a wide range of malicious behaviors after quantization. Through extensive evaluation across three attack scenarios and LLMs, we show that our attack achieves high success rates against a broad range of quantization methods on which prior attacks fail. Our results demonstrate, for the first time, that the security risks of quantization are not restricted to simpler schemes but are broadly relevant across complex, widely-used quantization methods.