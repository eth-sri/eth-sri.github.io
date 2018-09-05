---
ref: petrov2012race
title: Race Detection for Web Applications
authors: Boris Petrov, Martin Vechev, Manu Sridharan, Julian Dolby  
year: 2012
venue: ACM PLDI
projects: "EventRacer: Analysis of event-driven applications"
awards:
bibtex: '@inproceedings{petrov2012race,
  title={Race detection for web applications},
  author={Petrov, Boris and Vechev, Martin and Sridharan, Manu and Dolby, Julian},
  booktitle={ACM SIGPLAN Notices},
  volume={47},
  number={6},
  pages={251--262},
  year={2012},
  organization={ACM}}'
paper: pldi12-wr.pdf
talk: 
slides: 
---

Modern web pages are becoming increasingly full-featured, and this additional functionality often requires greater use of asynchrony. Unfortunately, this asynchrony can trigger unexpected concurrency errors, even though web page scripts are executed sequentially.

We present the first formulation of a happens-before relation for common web platform features. Developing this relation was a non-trivial task, due to complex feature interactions and browser differences. We also present a logical memory access model for web applications that abstracts away browser implementation details.

Based on the above, we implemented WebRacer, the first dynamic race detector for web applications. WebRacer is implemented atop the production-quality WebKit engine, enabling testing of full-featured web sites. WebRacer can also simulate certain user actions, exposing more races.

We evaluated WebRacer by testing a large set of Fortune 100 company web sites. We discovered many harmful races, and also gained insights into how developers handle asynchrony in practice.