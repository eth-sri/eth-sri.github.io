---
ref: vero2022data
title: "TabLeak: Tabular Data Leakage in Federated Learning"
authors: Mark Vero, Mislav Balunović, Dimitar I. Dimitrov, Martin Vechev
year: 2023
month: 7
venue: ICML
projects: federated
bibtex: "@InProceedings{pmlr-v202-vero23a,
  title = 	 {TabLeak: Tabular Data Leakage in Federated Learning},
  author =       {Vero, Mark and Balunovic, Mislav and Dimitrov, Dimitar Iliev and Vechev, Martin},
  booktitle = 	 {Proceedings of the 40th International Conference on Machine Learning},
  year = 	 {2023},
  series = 	 {Proceedings of Machine Learning Research},
  publisher =    {PMLR}
 }"

paper: https://arxiv.org/abs/2210.01785
code: https://github.com/eth-sri/tableak
---

While federated learning (FL) promises to preserve privacy, recent works in the image and text domains have shown that training updates leak private client data. However, most high-stakes applications of FL (e.g., in healthcare and finance) use tabular data, where the risk of data leakage has not yet been explored. A successful attack for tabular data must address two key challenges unique to the domain: (i) obtaining a solution to a high-variance mixed discrete-continuous optimization problem, and (ii) enabling human assessment of the reconstruction as unlike for image and text data, direct human inspection is not possible. In this work we address these challenges and propose TabLeak, the first comprehensive reconstruction attack on tabular data. TabLeak is based on two key contributions: (i) a method which leverages a softmax relaxation and pooled ensembling to solve the optimization problem, and (ii) an entropy-based uncertainty quantification scheme to enable human assessment. We evaluate TabLeak on four tabular datasets for both FedSGD and FedAvg training protocols, and show that it successfully breaks several settings previously deemed safe. For instance, we extract large subsets of private data at >90% accuracy even at the large batch size of 128. Our findings demonstrate that current high-stakes tabular FL is excessively vulnerable to leakage attacks. 