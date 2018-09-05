---
ref: bacon2005syncopation
title: "Syncopation: Generational Real-time Garbage Collection in the Metronome"
authors: David F. Bacon, Perry Cheng, David Grove, Martin Vechev 
year: 2005
venue: ACM LCTES
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{bacon2005syncopation,
  title={Syncopation: generational real-time garbage collection in the metronome},
  author={Bacon, David F and Cheng, Perry and Grove, David and Vechev, Martin T},
  booktitle={ACM SIGPLAN Notices},
  volume={40},
  number={7},
  pages={183--192},
  year={2005},
  organization={ACM}}'
paper: syncopation.pdf
talk: 
slides: 
---

Real-time garbage collection has been shown to be feasible, but for programs with high allocation rates, the utilization achievable is not sufficient for some systems.Since a high allocation rate is often correlated with a more high-level, abstract programming style, the ability to provide good real-time performance for such programs will help continue to raise the level of abstraction at which real-time systems can be programmed.We have developed techniques that allow generational collection to be used despite the problems caused by variance in program behavior over the short time scales in which a nursery can be collected. Syncopation allows such behavior to be detected by the scheduler in time for allocation to by-pass the nursery and allow real-time bounds to be met.We have provided an analysis of the costs of both generational and non-generational techniques, which allow the trade-offs to be evaluated quantitatively. We have also provided measurements of application behavior which show that while syncopation is necessary, the need for it is rare enough that generational collection can provide major improvements in real-time utilization. An additional technique, arraylet pre-tenuring, often significantly improves generational behavior.