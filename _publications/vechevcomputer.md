---
ref: vechevcomputer
title: "Position Paper: Computer-Assisted Construction of Efficient Concurrent Algorithms"
authors: Martin Vechev, Eran Yahav, Maged Michael, Hagit Attiya, Greta Yorsh
year: 2008
venue: "EC2: Exploiting Concurrency Efficiently and Correctly -- CAV Workshop"
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@article{vechevcomputer,
  title={Computer-Assisted Construction of Efficient Concurrent Algorithms},
  author={Vechev, Martin and Yahav, Eran and Michael, Maged and Attiya, Hagit and Yorsh, Greta}}'
paper: https://files.sri.inf.ethz.ch/website/papers/ec2-2008.pdf
talk: 
slides: 
---

Practical and efficient concurrent systems are notoriously hard to design, implement, and verify. As concurrent
systems become a larger part of society’s mission-critical infrastructure, it is imperative that we raise the
level of confidence in the correctness of these systems, and that we understand the trade-offs inherent in our
algorithmic choice.

Current practices for developing concurrent systems are rather limited. Directly using low-level concurrency
constructs is the realm of experts, and is extremely error-prone. Generic higher-level constructs (e.g., transactional memory) are currently limited, and are not clearly easier to use. Analytic techniques (e.g., race detection) only address a fraction of the problems, and can only be applied after the code is written and is potentially broken in a fundamental manner. This motivates us to explore a methodology and a tool that assist an algorithm designer during the construction process. Our hope is that at least for specific domains it would be possible to generate efficient provably correct concurrent systems from higher-level specifications.
