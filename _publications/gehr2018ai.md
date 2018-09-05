---
ref: gehr2018ai
title: "AI2: Safety and Robustness Certification of Neural Networks with Abstract Interpretation"
authors: Timon Gehr, Matthew Mirman, Dana Drachsler-Cohen, Petar Tsankov, Swarat Chaudhuri, Martin Vechev
year: 2018
month: 05
venue: IEEE S&P
projects: safeai
awards:
bibtex: '@inproceedings{gehr2018ai,
  title={Ai 2: Safety and robustness certification of neural networks with abstract interpretation},
  author={Gehr, Timon and Mirman, Matthew and Drachsler-Cohen, Dana and Tsankov, Petar and Chaudhuri, Swarat and Vechev, Martin},
  booktitle={Security and Privacy (SP), 2018 IEEE Symposium on},
  year={2018}}'
paper: https://files.sri.inf.ethz.ch/website/papers/sp2018.pdf
talk: https://www.youtube.com/watch?v=LJnjCMV8KzA
slides: http://safeai.ethz.ch/files/FLOC18-AI2.pdf
---

We present AI2, the first sound and scalable analyzer for deep neural networks. Based on overapproximation, AI2 can automatically prove safety properties (e.g., robustness) of realistic neural networks (e.g., convolutional neural networks).

The key insight behind AI2 is to phrase reasoning about safety and robustness of neural networks in terms of classic abstract interpretation, enabling us to leverage decades of advances in that area. Concretely, we introduce abstract transformers that capture the behavior of fully connected and convolutional neural network layers with rectified linear unit activations (ReLU), as well as max pooling layers. This allows us to handle real-world neural networks, which are often built out of those types of layers.

We present a complete implementation of AI2 together with an extensive evaluation on 20 neural networks. Our results demonstrate that: (i) AI2 is precise enough to prove useful specifications (e.g., robustness), (ii) AI2 can be used to certify the effectiveness of state-of-the-art defenses for neural networks, (iii) AI2 is significantly faster than existing analyzers based on symbolic analysis, which often take hours to verify simple fully connected networks, and (iv) AI2 can handle deep convolutional networks, which are beyond the reach of existing methods.
