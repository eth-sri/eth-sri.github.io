---
ref: vero2022data
title: "Data Leakage in Tabular Federated Learning"
authors: Mark Vero, Mislav Balunović, Dimitar I. Dimitrov, Martin Vechev
year: 2022
month: 10
venue: arXiv
projects: safeai
bibtex: '@article{vero2022data,
  title={Data Leakage in Tabular Federated Learning},
  author={Vero, Mark and Balunovi{\'c}, Mislav and Dimitrov, Dimitar I and Vechev, Martin},
  journal={arXiv preprint arXiv:2210.01785},
  year={2022}}'
paper: https://arxiv.org/abs/2210.01785
---

While federated learning (FL) promises to preserve privacy in distributed training of deep learning models, recent work in the image and NLP domains showed that training updates leak private data of participating clients. At the same time, most high-stakes applications of FL (e.g., legal and financial) use tabular data. Compared to the NLP and image domains, reconstruction of tabular data poses several unique challenges: (i) categorical features introduce a significantly more difficult mixed discrete-continuous optimization problem, (ii) the mix of categorical and continuous features causes high variance in the final reconstructions, and (iii) structured data makes it difficult for the adversary to judge reconstruction quality. In this work, we tackle these challenges and propose the first comprehensive reconstruction attack on tabular data, called TabLeak. TabLeak is based on three key ingredients: (i) a softmax structural prior, implicitly converting the mixed discrete-continuous optimization problem into an easier fully continuous one, (ii) a way to reduce the variance of our reconstructions through a pooled ensembling scheme exploiting the structure of tabular data, and (iii) an entropy measure which can successfully assess reconstruction quality. Our experimental evaluation demonstrates the effectiveness of TabLeak, reaching a state-of-the-art on four popular tabular datasets. For instance, on the Adult dataset, we improve attack accuracy by 10% compared to the baseline on the practically relevant batch size of 32 and further obtain non-trivial reconstructions for batch sizes as large as 128. Our findings are important as they show that performing FL on tabular data, which often poses high privacy risks, is highly vulnerable.
