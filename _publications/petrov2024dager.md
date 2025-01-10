---
ref: petrov2024dager
title: "DAGER: Exact Gradient Inversion for Large Language Models"
authors: Ivo Petrov, Dimitar I. Dimitrov, Maximilian Baader, Mark Niklas Müller, Martin Vechev
year: 2024
month: 12
venue: NeurIPS
projects: safeai
bibtex: '@inproceedings{
			petrov2024dager,
			title={DAGER: Exact Gradient Inversion for Large Language Models},
			author={Petrov, Ivo and Dimitrov, Dimitar I and Baader, Maximilian and M{\"u}ller, Mark Niklas and Vechev, Martin},
			booktitle = {Advances in Neural Information Processing Systems},
			volume = {37},
			year = {2024}
		}'
paper: https://files.sri.inf.ethz.ch/dager_gradient_leakage/dager.pdf
---
Federated learning works by aggregating locally computed gradients from multiple clients, thus enabling collaborative training without sharing private client data. However, prior work has shown that the data can actually be recovered by the server using so-called gradient inversion attacks. While these attacks perform well when applied on images, they are limited in the text domain and only permit approximate reconstruction of small batches and short input sequences. In this work, we propose DAGER, the first algorithm to recover whole batches of input text exactly. DAGER leverages the low-rank structure of self-attention layer gradients and the discrete nature of token embeddings to efficiently check if a given token sequence is part of the client data. We use this check to exactly recover full batches in the honest-but-curious setting without any prior on the data for both encoder-based and decoder-based architectures using exhaustive heuristic search and a greedy approach, respectively. We provide an efficient GPU implementation of DAGER and show experimentally that it recovers full batches of size up to 128 on large language models (LLMs), beating prior attacks in speed (20x at same batch size), scalability (10x larger batches), and reconstruction quality (ROUGE-1/2 > 0.99).