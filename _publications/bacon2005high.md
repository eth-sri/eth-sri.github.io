---
ref: bacon2005high
title: High-level Real-time Programming in Java 
authors: David F. Bacon, Perry Cheng, David Grove, Michael Hind, V.T. Rajan, Eran Yahav, M. Hauswirth, C. Kirsch, Daniel Spoonhower, and Martin T. Vechev 
year: 2005
venue: ACM EMSOFT
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{bacon2005high,
  title={High-level real-time programming in Java},
  author={Bacon, David F and Cheng, Perry and Grove, David and Hind, Michael and Rajan, VT and Yahav, Eran and Hauswirth, Matthias and Kirsch, Christoph M and Spoonhower, Daniel and Vechev, Martin T},
  booktitle={Proceedings of the 5th ACM international conference on Embedded software},
  pages={68--78},
  year={2005},
  organization={ACM}}'
paper: emsoft05.pdf
talk: 
slides: 
---

Real-time systems have reached a level of complexity beyond the scaling capability of the low-level or restricted languages traditionally used for real-time programming.

While Metronome garbage collection has made it practical to use Java to implement real-time systems, many challenges remain for the construction of complex real-time systems, some specific to the use of Java and others simply due to the change in scale of such systems.

The goal of our current research is the creation of a comprehensive Java-based programming environment and methodology for the creation of complex real-time systems. Our goals include construction of a provably correct real-time garbage collector capable of providing worst case latencies of 100 μs, capable of scaling from sensor nodes up to large multiprocessors; specialized programming constructs that retain the safety and simplicity of Java, and yet provide sub-microsecond latencies; the extension of Java's "write once, run anywhere" principle from functional correctness to timing behavior; on-line analysis and visualization that aids in the understanding of complex behaviors; and a principled probabilistic analysis methodology for bounding the behavior of the resulting systems.

While much remains to be done, this paper describes the progress we have made towards these goals.