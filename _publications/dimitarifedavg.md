---
ref: dimitrov2022fedavg
title:  "Data Leakage in Federated Averaging"
projects: safeai
authors: Dimitar I. Dimitrov, Mislav Balunović, Nikola Konstantinov, Martin Vechev
year: 2022
month: 6
bibtex: '@misc{https://doi.org/10.48550/arxiv.2206.12395,
  doi = {10.48550/ARXIV.2206.12395},
  url = {https://arxiv.org/abs/2206.12395},
  author = {Dimitrov, Dimitar I. and Balunović, Mislav and Konstantinov, Nikola and Vechev, Martin},
  keywords = {Machine Learning (cs.LG), Cryptography and Security (cs.CR), Distributed, Parallel, and Cluster Computing (cs.DC), FOS: Computer and information sciences, FOS: Computer and information sciences, I.2.11},
  title = {Data Leakage in Federated Averaging},
  publisher = {arXiv},
  year = {2022}, 
  copyright = {Creative Commons Attribution 4.0 International}
}'
paper: https://arxiv.org/abs/2206.12395
venue: arXiv
---
Recent attacks have shown that user data can be recovered from FedSGD updates, thus breaking privacy. However, these attacks are of limited practical relevance as federated learning typically uses the FedAvg algorithm. Compared to FedSGD, recovering data from FedAvg updates is much harder as: (i) the updates are computed at unobserved intermediate network weights, (ii) a large number of batches are used, and (iii) labels and network weights vary simultaneously across client steps. In this work, we propose a new optimization-based attack which successfully attacks FedAvg by addressing the above challenges. First, we solve the optimization problem using automatic differentiation that forces a simulation of the client's update that generates the unobserved parameters for the recovered labels and inputs to match the received client update. Second, we address the large number of batches by relating images from different epochs with a permutation invariant prior. Third, we recover the labels by estimating the parameters of existing FedSGD attacks at every FedAvg step. On the popular FEMNIST dataset, we demonstrate that on average we successfully recover >45% of the client's images from realistic FedAvg updates computed on 10 local epochs of 10 batches each with 5 images, compared to only <10% using the baseline. Our findings show many real-world federated learning implementations based on FedAvg are vulnerable.