---
ref: raychev2013effective
title: Effective Race Detection for Event-Driven Programs
authors: Veselin Raychev, Martin Vechev, Manu Sridharan 
year: 2013
venue: ACM OOPSLA
projects: "EventRacer: Analysis of event-driven applications"
awards:
bibtex: '@inproceedings{raychev2013effective,
  title={Effective race detection for event-driven programs},
  author={Raychev, Veselin and Vechev, Martin and Sridharan, Manu},
  booktitle={ACM SIGPLAN Notices},
  volume={48},
  number={10},
  pages={151--166},
  year={2013},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/oopsla13-web.pdf
talk: 
slides: https://docs.google.com/presentation/d/1-eKof4xLvDJYyWigujUNtf0kdEnAB3Kx3l2sbyDiyOY/edit?usp=sharing
---

Like shared-memory multi-threaded programs, event-driven programs such as client-side web applications are susceptible to data races that are hard to reproduce and debug. Race detection for such programs is hampered by their pervasive use of ad hoc synchronization, which can lead to a prohibitive number of false positives. Race detection also faces a scalability challenge, as a large number of shortrunning event handlers can quickly overwhelm standard vector-clock-based techniques.

This paper presents several novel contributions that address both of these challenges. First, we introduce race coverage, a systematic method for exposing ad hoc synchronization and other (potentially harmful) races to the user, significantly reducing false positives. Second, we present an efficient connectivity algorithm for computing race coverage. The algorithm is based on chain decomposition and leverages the structure of event-driven programs to dramatically decrease the overhead of vector clocks.

We implemented our techniques in a tool called EVENTRACER and evaluated it on a number of public web sites. The results indicate substantial performance and precision improvements of our approach over the state-of-the-art. Using EVENTRACER, we found many harmful races, most of which are beyond the reach of current techniques.
