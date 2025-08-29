---
ref: drencheva2025grain
title: "GRAIN: Exact Graph Reconstruction from Gradients"
authors: Maria Drencheva, Ivo Petrov, Maximilian Baader, Dimitar I. Dimitrov, Martin Vechev
year: 2025
month: 4
venue: ICLR
projects: federated
bibtex: '@inproceedings{
		drencheva2025grain,
		title={{GRAIN}: Exact Graph Reconstruction from Gradients},
		author={Maria Drencheva and Ivo Petrov and Maximilian Baader and Dimitar Iliev Dimitrov and Martin Vechev},
		booktitle={The Thirteenth International Conference on Learning Representations},
		year={2025},
		url={https://openreview.net/forum?id=7bAjVh3CG3}
}'
paper: https://files.sri.inf.ethz.ch/grain/grain.pdf
---
Federated learning claims to enable collaborative model training among multiple clients with data privacy by transmitting gradient updates instead of the actual client data. However, recent studies have shown the client privacy is still at risk due to the, so called, gradient inversion attacks which can precisely reconstruct clients' text and image data from the shared gradient updates. While these attacks demonstrate severe privacy risks for certain domains and architectures, the vulnerability of other commonly-used data types, such as graph-structured data, remain under-explored. To bridge this gap, we present GRAIN, the first exact gradient inversion attack on graph data in the honest-but-curious setting that recovers both the structure of the graph and the associated node features. Concretely, we focus on Graph Convolutional Networks (GCN) and Graph Attention Networks (GAT) --- two of the most widely used frameworks for learning on graphs. Our method first utilizes the low-rank structure of GNN gradients to efficiently reconstruct and filter the client subgraphs which are then joined to complete the input graph. We evaluate our approach on molecular, citation, and social network datasets using our novel metric. We show that GRAIN reconstructs up to 80% of all graphs exactly, significantly outperforming the baseline, which achieves up to 20% correctly positioned nodes.
