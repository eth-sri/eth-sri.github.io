---
ref: bakarsky2025spear++
title: "SPEAR++: Scaling Gradient Inversion via Sparsely-Used Dictionary Learning"
authors: Alexander Bakarsky, Dimitar I. Dimitrov, Maximilian Baader, Martin Vechev	
year: 2025
month: 12
venue: Regulatable ML @ NeurIPS
projects: federated
bibtex: '@article{bakarsky2025spear++,
			title={SPEAR++: Scaling Gradient Inversion via Sparsely-Used Dictionary Learning},
			author={Bakarsky, Alexander and Dimitrov, Dimitar I and Baader, Maximilian and Vechev, Martin},
			journal={arXiv preprint arXiv:2510.24200},
			year={2025}
		}'
paper: https://arxiv.org/abs/2510.24200
---

Federated Learning has seen an increased deployment in real-world scenarios recently, as it enables the distributed training of machine learning models without explicit data sharing between individual clients. Yet, the introduction of the so-called gradient inversion attacks has fundamentally challenged its privacy-preserving properties. Unfortunately, as these attacks mostly rely on direct data optimization without any formal guarantees, the vulnerability of real-world systems remains in dispute and requires tedious testing for each new federated deployment. To overcome these issues, recently the SPEAR attack was introduced, which is based on a theoretical analysis of the gradients of linear layers with ReLU activations. While SPEAR is an important theoretical breakthrough, the attack's practicality was severely limited by its exponential runtime in the batch size b. In this work, we fill this gap by applying State-of-the-Art techniques from Sparsely-Used Dictionary Learning to make the problem of gradient inversion on linear layers with ReLU activations tractable. Our experiments demonstrate that our new attack, SPEAR++, retains all desirable properties of SPEAR, such as robustness to DP noise and FedAvg aggregation, while being applicable to 10x bigger batch sizes.