---
ref: dimitrov2024spear
title: "SPEAR: Exact Gradient Inversion of Batches in Federated Learning"
authors: Dimitar I. Dimitrov, Maximilian Baader, Mark Niklas Müller, Martin Vechev
year: 2024
month: 12
venue: NeurIPS
projects: safeai
bibtex: '@inproceedings{
			dimitrov2024spear,
			title={SPEAR: Exact Gradient Inversion of Batches in Federated Learning},
			author={Dimitrov, Dimitar I and Baader, Maximilian and M{\"u}ller, Mark Niklas and Vechev, Martin},
			booktitle = {Advances in Neural Information Processing Systems},
			volume = {37},
			year = {2024}
		}'
paper: https://files.sri.inf.ethz.ch/spear/spear.pdf
poster: https://files.sri.inf.ethz.ch/spear/spear_poster.png
slides: https://files.sri.inf.ethz.ch/spear/spear_slides.pdf
---
Federated learning is a framework for collaborative machine learning where clients only share gradient updates and not their private data with a server. However, it was recently shown that gradient inversion attacks can reconstruct this data from the shared gradients. In the important honest-but-curious setting, existing attacks enable exact reconstruction only for batch size of b = 1, with larger batches permitting only approximate reconstruction. In this work, we propose SPEAR, the first algorithm reconstructing whole batches with b > 1 exactly. SPEAR combines insights into the explicit low-rank structure of gradients with a sampling-based algorithm. Crucially, we leverage ReLU-induced gradient sparsity to precisely filter out large numbers of incorrect samples, making a final reconstruction step tractable. We provide an efficient GPU implementation for fully connected networks and show that it recovers high-dimensional ImageNet inputs in batches of up to b < 25 exactly while scaling to large networks. Finally, we show theoretically that much larger batches can be reconstructed with high probability given exponential time.
