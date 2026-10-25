---
ref: zhan2026allinone
title: "All-in-One: A Composable Attack on LLM Transformations"
authors: Xiaohua Zhan, Kazuki Egashira, Robin Staab, Mark Vero, Martin Vechev
year: 2026
month: 10
venue: Preprint
projects: llmsecpriv
bibtex: "@misc{zhan2026allinone,
  title={{All-in-One}: A Composable Attack on {LLM} Transformations},
  author={Zhan, Xiaohua and Egashira, Kazuki and Staab, Robin and Vero, Mark and Vechev, Martin},
  year={2026},
  url={https://files.sri.inf.ethz.ch/website/papers/zhan2026allinone.pdf}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/zhan2026allinone.pdf
code: https://github.com/eth-sri/aio-attack
---

Quantization, pruning, and model merging are popular transformations applied to deployment-ready LLMs to improve efficiency and downstream performance. Recent work has shown that these transformations can introduce a security threat: an adversary can train a model that passes safety checks in its pre-transformed state, only turning malicious once it is transformed for deployment. However, prior attacks target one specific transformation (e.g., quantization) and generally rely on transformation-specific techniques, making them difficult to combine in practice. In this work, we introduce a simple, composable attack framework that targets multiple transformations simultaneously and triggers when any one of them is applied by a user. Our key insight is that the effect of each transformation can be approximated as a perturbation to the model weights, allowing us to jointly train the model with a benign loss on the original model and a malicious loss on each simulated transformed model. These perturbations are simple enough to simulate at every training iteration across diverse transformations, making them practically combinable within a single training objective, enabling a unified attack. Through extensive experiments across attack scenarios, model families, and a wide range of deployment-time model transformations, we show that our attack achieves high success rates. This demonstrates that model transformations may be utilized to trigger significantly different behavior from the original model and reinforces the associated security concerns by demonstrating that a single attack can jointly target diverse transformations.
