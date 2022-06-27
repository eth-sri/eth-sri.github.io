---
ref: horvath2022robust
title: "Robust and Accurate - Compositional Architectures for Randomized Smoothing"
authors: Miklós Z. Horváth, Mark Niklas Müller, Marc Fischer, Martin Vechev
year: 2022
month: 4
venue: SRML@ICLR
projects: safeai
bibtex: |
      @inproceedings{horvath2022robust,
      title={Robust and Accurate - Compositional Architectures for Randomized Smoothing}, 
      author={Miklós Z. Horváth and Mark Niklas M{\"{u}}ller and Marc Fischer and Martin Vechev},
      booktitle={ICLR 2022 Workshop on Socially Responsible Machine Learning},
      year={2022}
      }
paper: https://arxiv.org/pdf/2204.00487.pdf
code: https://github.com/eth-sri/aces)
---
Randomized Smoothing (RS) is considered the state-of-the-art approach to obtain certifiably robust models for challenging tasks. However, current RS approaches drastically decrease standard accuracy on unperturbed data, severely limiting their real-world utility. To address this limitation, we propose a compositional architecture, ACES, which certifiably decides on a per-sample basis whether to use a smoothed model yielding predictions with guarantees or a more accurate standard model without guarantees. This, in contrast to prior approaches, enables both high standard accuracies and significant provable robustness. On challenging tasks such as ImageNet, we obtain, e.g., 80.0% natural accuracy and 28.2% certifiable accuracy against l2 perturbations with r = 1.0. We release our code and models at [https://github.com/eth-sri/aces](https://github.com/eth-sri/aces).

