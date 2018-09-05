---
ref: shacham2014verifying
title: Verifying Atomicity via Data Independence 
authors: Ohad Shacham, Eran Yahav, Guy Gueta, Alex Aiken, Nathan Bronson, Mooly Sagiv and Martin Vechev
year: 2014
venue: ISSTA
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{shacham2014verifying,
  title={Verifying atomicity via data independence},
  author={Shacham, Ohad and Yahav, Eran and Gueta, Guy Golan and Aiken, Alex and Bronson, Nathan and Sagiv, Mooly and Vechev, Martin},
  booktitle={Proceedings of the 2014 International Symposium on Software Testing and Analysis},
  pages={26--36},
  year={2014},
  organization={ACM}}'
paper: issta14-atomicity.pdf
talk: 
slides: 
---

We present a technique for automatically verifying atomicity of composed concurrent operations. The main observation behind our approach is that many composed concurrent operations which occur in practice are data-independent. That is, the control-flow of the composed operation does not depend on specific input values. While verifying data-independence is undecidable in the general case, we provide succint sufficient conditions that can be used to establish a composed operation as data-independent. We show that for the common case of concurrent maps, data-independence reduces the hard problem of verifying linearizability to a verification problem that can be solved efficiently with a bounded number of keys and values.

We implemented our approach in a tool called VINE and evaluated it on all composed operations from 57 real-world applications (112 composed operations). We show that many composed operations (49 out of 112) are data-independent, and automatically verify 30 of them as linearizable and the rest 19 as having violations of linearizability that could be repaired and then subsequently automatically verified. Moreover, we show that the remaining 63 operations are not linearizable, thus indicating that data independence does not limit the expressiveness of writing realistic linearizable composed operations.