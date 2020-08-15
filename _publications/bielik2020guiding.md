---
ref: bielik2020guiding
title: Guiding Program Synthesis by Learning to Generate Examples 
authors: Larissa Laich, Pavol Bielik, Martin Vechev 
year: 2020
month: 4
venue: ICLR
projects: plml
awards:
bibtex: '@inproceedings{
         Laich2020Guiding,
         title={Guiding Program Synthesis by Learning to Generate Examples},
         author={Larissa Laich and Pavol Bielik and Martin Vechev},
         booktitle={International Conference on Learning Representations},
         year={2020},
         url={https://openreview.net/forum?id=BJl07ySKvS}
         }'
paper: https://files.sri.inf.ethz.ch/website/papers/laich20guiding.pdf
talk: https://iclr.cc/virtual_2020/poster_BJl07ySKvS.html
slides: 
---

A key challenge of existing program synthesizers is ensuring that the synthesized program generalizes well. This can be difficult to achieve as the specification provided by the end user is often limited, containing as few as one or two input-output examples. In this paper we address this challenge via an iterative approach that finds ambiguities in the provided specification and learns to resolve these by generating additional input-output examples. The main insight is to reduce the problem of selecting which program generalizes well to the simpler task of deciding which output is correct. As a result, to train our probabilistic models, we can take advantage of the large amounts of data in the form of program outputs, which are often much easier to obtain than the corresponding ground-truth programs.
