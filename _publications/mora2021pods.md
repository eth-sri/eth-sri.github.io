---
ref: mora2021pods
title: "PODS: Policy Optimization via Differentiable Simulation"
authors: Miguel Angel Zamora Mora, Momchil Peychev, Sehoon Ha, Martin Vechev, Stelian Coros
year: 2021
month: 07
venue: ICML
projects:
bibtex: '@inproceedings{mora2021pods,
  title = {PODS: Policy Optimization via Differentiable Simulation},
  author = {Mora, Miguel Angel Zamora and Peychev, Momchil and Ha, Sehoon and Vechev, Martin and Coros, Stelian},
  booktitle = {Proceedings of the 38th International Conference on Machine Learning},
  pages = {7805--7817},
  year = {2021},
  editor = {Meila, Marina and Zhang, Tong},
  volume = {139},
  series = {Proceedings of Machine Learning Research},
  month = {18--24 Jul},
  publisher = {PMLR},
  pdf = {http://proceedings.mlr.press/v139/mora21a/mora21a.pdf},
  url = {http://proceedings.mlr.press/v139/mora21a.html}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/icml21-pods.pdf
---

Current reinforcement learning (RL) methods use simulation models as simple black-box oracles. In this paper, with the goal of improving the performance exhibited by RL algorithms, we explore a systematic way of leveraging the additional information provided by an emerging class of differentiable simulators. Building on concepts established by Deterministic Policy Gradients (DPG) methods, the neural network policies learned with our approach represent deterministic actions. In a departure from standard methodologies, however, learning these policies does not hinge on approximations of the value function that must be learned concurrently in an actor-critic fashion. Instead, we exploit differentiable simulators to directly compute the analytic gradient of a policy’s value function with respect to the actions it outputs. This, in turn, allows us to efficiently perform locally optimal policy improvement iterations. Compared against other state-of-the-art RL methods, we show that with minimal hyper-parameter tuning our approach consistently leads to better asymptotic behavior across a set of payload manipulation tasks that demand a high degree of accuracy and precision.
