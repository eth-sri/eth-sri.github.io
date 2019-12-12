---
ref: singh2019krelu
title:  "Beyond the Single Neuron Convex Barrier for Neural Network Certification"
projects: safeai
authors: Gagandeep Singh, Rupanshu Ganvir, Markus Püschel, Martin Vechev
image: assets/images/singh2019krelu.png
year: 2019
month: 12
bibtex: '@incollection{singh2019krelu,
  title = {Beyond the Single Neuron Convex Barrier for Neural Network Certification},
  author = {Singh, Gagandeep and Ganvir, Rupanshu and Püschel, Markus and Vechev, Martin},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year = {2019}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/neurips19_krelu.pdf
slides: https://files.sri.inf.ethz.ch/website/slides/kPoly.pdf
venue: NeurIPS
---
We propose a new parametric framework, called k-ReLU, for computing precise and scalable convex relaxations used to certify neural networks. The key idea is to approximate the output of multiple ReLUs in a layer jointly instead of separately. This joint relaxation captures dependencies between the inputs to different ReLUs in a layer and thus overcomes the convex barrier imposed by the single neuron
triangle relaxation and its approximations. The framework is parametric in the number of k ReLUs it considers jointly and can be combined with existing verifiers in order to improve their precision. Our experimental results show that k-ReLU enables significantly more precise certification than existing state-of-the-art verifiers while maintaining scalability.
