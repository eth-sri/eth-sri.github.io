---
ref: dan2017effective
title: Effective Abstractions for Verification under Relaxed Memory Models 
authors: Andrei Dan, Yuri Meshman, Martin Vechev, Eran Yahav         
year: 2015
venue: VMCAI
projects: fender
awards:
bibtex: '@article{dan2017effective,
  title={Effective abstractions for verification under relaxed memory models},
  author={Dan, Andrei and Meshman, Yuri and Vechev, Martin and Yahav, Eran},
  journal={Computer Languages, Systems \& Structures},
  volume={47},
  pages={62--76},
  year={2017},
  publisher={Elsevier}}'
paper: https://files.sri.inf.ethz.ch/website/papers/vmcai15.pdf
talk: 
slides: http://practicalsynthesis.github.io/papers/vmcai15-slides.pdf
---

We present a new abstract interpretation based approach for automatically verifying concurrent programs running on relaxed memory models. Our approach is based on three key insights: (i) behaviors of relaxed models (e.g. TSO and PSO) are naturally captured using explicit encodings of store buffers. Directly using such encodings for program analysis is challenging due to shift operations on buffer contents that result in significant loss of analysis precision. We present a new abstraction of the memory model that eliminates expensive shifting of store buffer contents and significantly improves the precision and scalability of program analysis, (ii) an encoding of store buffer sizes that leverages knowledge of the abstract interpretation domain, further improving analysis precision, and (iii) a source-to-source transformation that realizes the above two techniques: given a program P and a relaxed memory model M, it produces a new program PM where the behaviors of P running on M are over-approximated by the behavior of PM running on sequential consistency (SC). This step makes it possible to directly use state-of-the-art analyzers under SC.

We implemented our approach and evaluated it on a set of finite and infinitestate concurrent algorithms under two memory models: Intel’s x86 TSO and PSO. Experimental results indicate that our technique achieves better precision and efficiency than prior work: we can automatically verify algorithms with fewer fences, faster and with lower memory consumption.
