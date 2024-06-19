---
ref: pouget2024frleval
title: "Back to the Drawing Board for Fair Representation Learning"
authors: Angéline Pouget, Nikola Jovanović, Mark Vero, Robin Staab, Martin Vechev
year: 2024
month: 05
venue: arXiv
projects: safeai
bibtex: "@article{pouget2024frleval,
  title = {Back to the Drawing Board for Fair Representation Learning},
  author = {Angéline Pouget, Nikola Jovanović, Mark Vero, Robin Staab, Martin Vechev},
  year = {2024},
  eprint={2405.18161},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/pouget2024frleval.pdf
---

The goal of Fair Representation Learning (FRL) is to mitigate biases in machine learning models by learning data representations that enable high accuracy on downstream tasks while minimizing discrimination based on sensitive attributes. The evaluation of FRL methods in many recent works primarily focuses on the tradeoff between downstream fairness and accuracy with respect to a single task that was used to approximate the utility of representations during training (proxy task). This incentivizes retaining only features relevant to the proxy task while discarding all other information. In extreme cases, this can cause the learned representations to collapse to a trivial, binary value, rendering them unusable in transfer settings. In this work, we argue that this approach is fundamentally mismatched with the original motivation of FRL, which arises from settings with many downstream tasks unknown at training time (transfer tasks). To remedy this, we propose to refocus the evaluation protocol of FRL methods primarily around the performance on transfer tasks. A key challenge when conducting such an evaluation is the lack of adequate benchmarks. We address this by formulating four criteria that a suitable evaluation procedure should fulfill. Based on these, we propose TransFair, a benchmark that satisfies these criteria, consisting of novel variations of popular FRL datasets with carefully calibrated transfer tasks. In this setting, we reevaluate state-of-the-art FRL methods, observing that they often overfit to the proxy task, which causes them to underperform on certain transfer tasks. We further highlight the importance of task-agnostic learning signals for FRL methods, as they can lead to more transferrable representations.