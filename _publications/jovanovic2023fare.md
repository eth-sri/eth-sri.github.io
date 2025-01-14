---
ref: jovanovic2023fare
title: "FARE: Provably Fair Representation Learning with Practical Certificates"
authors: Nikola Jovanović, Mislav Balunović, Dimitar I. Dimitrov, Martin Vechev
year: 2023
month: 7
venue: ICML
projects: safeai
bibtex: '@article{jovanovic2023fare,
  title={FARE: Provably Fair Representation Learning with Practical Certificates},
  author={Jovanović, Nikola and Balunović, Mislav and Dimitrov, Dimitar I and Vechev, Martin},
  year = {2023},
  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
  publisher = {PMLR}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/jovanovic2023fare.pdf
code: https://github.com/eth-sri/fare
---

Fair representation learning (FRL) is a popular class of methods aiming to produce fair classifiers via data preprocessing. Recent regulatory directives stress the need for FRL methods that provide practical certificates, i.e., provable upper bounds on the unfairness of any downstream classifier trained on preprocessed data, which directly provides assurance in a practical scenario. Creating such FRL methods is an important challenge that remains unsolved. In this work, we address that challenge and introduce FARE (Fairness with Restricted Encoders), the first FRL method with practical fairness certificates. FARE is based on our key insight that restricting the representation space of the encoder enables the derivation of practical guarantees, while still permitting favorable accuracy-fairness tradeoffs for suitable instantiations, such as one we propose based on fair trees. To produce a practical certificate, we develop and apply a statistical procedure that computes a finite sample high-confidence upper bound on the unfairness of any downstream classifier trained on FARE embeddings. In our comprehensive experimental evaluation we demonstrate that FARE produces practical certificates that are tight and often even comparable with purely empirical results obtained by prior methods, which establishes the practical value of our approach. 
