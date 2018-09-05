---
ref: drachsler2017synthesis
title: Synthesis with Abstract Examples
authors: Dana Drachsler-Cohen, Sharon Shoham, and Eran Yahav
year: 2017
venue: CAV
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{DBLP:conf/cav/Drachsler-Cohen17,
  author    = {Dana Drachsler{-}Cohen and
               Sharon Shoham and
               Eran Yahav},
  title     = {Synthesis with Abstract Examples},
  booktitle = {Computer Aided Verification - 29th International Conference, {CAV}
               2017, Heidelberg, Germany, July 24-28, 2017, Proceedings, Part {I}},
  pages     = {254--278},
  year      = {2017},
  crossref  = {DBLP:conf/cav/2017-1},
  url       = {https://doi.org/10.1007/978-3-319-63387-9\_13},
  doi       = {10.1007/978-3-319-63387-9\_13},
  timestamp = {Fri, 14 Jul 2017 12:55:54 +0200},
  biburl    = {https://dblp.org/rec/bib/conf/cav/Drachsler-Cohen17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}'
paper: http://ddana.cswp.cs.technion.ac.il/wp-content/uploads/sites/19/2017/06/Synthesis_with_abstract_examples_CAV17.pdf
talk: 
slides: 
---

Interactive program synthesizers enable a user to communicate his/her intent via input-output examples. Unfortunately, such synthesizers only guarantee that the synthesized program is correct on the provided examples. A user that wishes to guarantee correctness for all possible inputs has to manually inspect the synthesized program, an error-prone and challenging task.

We present a novel synthesis framework that communicates only through (abstract) examples and guarantees that the synthesized program is correct on all inputs. The main idea is to use abstract examples—a new form of examples that represent a potentially unbounded set of concrete examples. An abstract example captures how part of the input space is mapped to corresponding outputs by the synthesized program. Our framework uses a generalization algorithm to compute abstract examples which are then presented to the user. The user can accept an abstract example, or provide a counterexample in which case the synthesizer will explore a different program. When the user accepts a set of abstract examples that covers the entire input space, the synthesis process is completed.

We have implemented our approach and we experimentally show that our synthesizer communicates with the user effectively by presenting on average 3 abstract examples until the user rejects false candidate programs. Further, we show that a synthesizer that prunes the program space based on the abstract examples reduces the overall number of required concrete examples in up to 96% of the cases.
