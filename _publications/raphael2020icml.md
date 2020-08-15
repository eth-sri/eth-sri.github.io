---
ref: raphael2020icml
title:  "Adversarial Attacks on Probabilistic Autoregressive Forecasting Models"
projects: safeai
authors: Raphaël Dang-Nhu, Gagandeep Singh, Pavol Bielik, Martin Vechev
year: 2020
month: 07
bibtex: '@incollection{raphael2020,
  title = {Adversarial Attacks on Probabilistic Autoregressive Forecasting Models},
  author = {Dang-Nhu, Raphaël and Singh, Gagandeep and Bielik, Pavol and Vechev, Martin},
  booktitle = {International Conference on Machine Learning (ICML)},
  year = {2020}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/raphaelicml.pdf
slides: https://files.sri.inf.ethz.ch/website/slides/raphaelicml.pdf
talk: https://icml.cc/virtual/2020/poster/5838
venue: ICML
---
We develop an effective generation of adversarial attacks on neural models that output a sequence of probability distributions rather than a sequence of single values. This setting includes recently
proposed deep probabilistic autoregressive forecasting models that estimate the probability distribution of a time series given its past and achieve state-of-the-art results in a diverse set of application domains. The key technical challenge we address is effectively differentiating through the Monte-Carlo estimation of statistics of the joint distribution of the output sequence. Additionally, we extend prior work on probabilistic forecasting to the Bayesian setting which allows conditioning on future observations, instead of only on past observations. We demonstrate that our approach can successfully generate attacks with small input perturbations in two challenging tasks where robust decision making is crucial – stock market trading and prediction of electricity consumption.
