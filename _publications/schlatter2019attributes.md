---
ref: schlatter2019attributes
title: Learning to Infer User Interface Attributes from Images 
authors: Philippe Schlattner, Pavol Bielik, Martin Vechev 
year: 2019
month: 12
venue: arXiv
projects: plml
awards:
bibtex: '@misc{schlattner2019learning,
             title={Learning to Infer User Interface Attributes from Images},
             author={Philippe Schlattner and Pavol Bielik and Martin Vechev},
             year={2019},
             eprint={1912.13243},
             archivePrefix={arXiv},
             primaryClass={cs.CV}
         }'
paper: https://arxiv.org/pdf/1912.13243.pdf
talk: 
slides: 
---

We explore a new domain of learning to infer user interface attributes that helps developers automate the process of user interface implementation. Concretely, given an input image created by a designer, we learn to infer its implementation which when rendered, looks visually the same as the input image. To achieve this, we take a black box rendering engine and a set of attributes it supports (e.g., colors, border radius, shadow or text properties), use it to generate a suitable synthetic training dataset, and then train specialized neural models to predict each of the attribute values. To improve pixel-level accuracy, we additionally use imitation learning to train a neural policy that refines the predicted attribute values by learning to compute the similarity of the original and rendered images in their attribute space, rather than based on the difference of pixel values. We instantiate our approach to the task of inferring Android Button attribute values and achieve 92.5% accuracy on a dataset consisting of real-world Google Play Store applications.
