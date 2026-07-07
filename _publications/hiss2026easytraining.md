---
ref: hiss2026easytraining
title: "Learning from Saturated Data: Signals Beyond Correctness for LLM Training"
authors: Hanno Hiss, Jasper Dekoninck, Martin Vechev
year: 2026
month: 05
venue: AI4Math@ICML
projects: mathllm,llmevals
bibtex: "@misc{hiss2026learningsaturateddatasignals,
      title={Learning from Saturated Data: Signals Beyond Correctness for LLM Training}, 
      author={Hanno Hiss and Jasper Dekoninck and Martin Vechev},
      year={2026},
      eprint={2606.01436},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2606.01436}, 
}"
paper: https://arxiv.org/pdf/2606.01436
code: https://github.com/eth-sri/saturated-learning
---
The growing capabilities of large language models (LLMs) have led to the saturation of many benchmarks and training datasets used to improve them. Motivated by this, we investigate whether questions solved with perfect empirical accuracy can nevertheless be used to improve downstream performance. To do so, we replace binary correctness with two sources of more fine-grained quality signals: (1) pairwise LLM self-judgments, in which the model evaluates the relative quality of its own solutions, and (2) token-level entropy, where token-level uncertainty is used as a proxy for solution quality. We incorporate these signals into several training algorithms and evaluate them on Qwen3-1.7B-Base. When training exclusively on a simple arithmetic task, quality-based signals improve performance by up to 18.6% over the base model, substantially outperforming SFT. On GSM8K, however, gains are more modest and depend strongly on the quality signal. For instance, self-judgments show poor agreement with a stronger external judge and can even degrade performance below the base model. Overall, our results suggest that quality-based training can extract useful signal from saturated questions for base models, but that applying such signals to more complex tasks requires careful calibration and further study.