---
ref: singh2015making
title: Making Numerical Program Analysis Fast
authors: Gagandeep Singh, Markus Püschel, Martin Vechev        
year: 2015
venue: ACM PLDI
projects: numerical-analysis
awards:
bibtex: '@inproceedings{singh2015making,
  title={Making numerical program analysis fast},
  author={Singh, Gagandeep and P{\"u}schel, Markus and Vechev, Martin},
  booktitle={ACM SIGPLAN Notices},
  volume={50},
  number={6},
  pages={303--313},
  year={2015},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/PLDI15-OptOctagon.pdf
talk: 
slides: http://elina.ethz.ch/slides/pldi2015-fast-octagon.pdf
---

Numerical abstract domains are a fundamental component in modern static program analysis and are used in a wide range of scenarios (e.g. computing array bounds, disjointness, etc). However, analysis with these domains can be very expensive, deeply affecting the scalability and practical applicability of the static analysis.
Hence, it is critical to ensure that these domains are made highly efficient.

In this work, we present a complete approach for optimizing the performance of the Octagon numerical abstract domain, a domain shown to be particularly effective in practice. Our optimization approach is based on two key insights: i) the ability to perform online decomposition of the octagons leading to a massive reduction in operation counts, and ii) leveraging classic performance optimizations from linear algebra such as vectorization, locality of reference, scalar replacement and others, for improving the key bottlenecks of the domain. Applying these ideas, we designed new algorithms for the core Octagon operators with better asymptotic runtime than prior work and combined them with the optimization techniques to achieve high actual performance. We implemented our approach in the Octagon operators exported by the popular APRON C library, thus enabling existing static analyzers using APRON to immediately benefit from our work.

To demonstrate the performance benefits of our approach, we evaluated our framework on four published static analyzers showing massive speedups for the time spent in Octagon analysis (e.g., up to 146x) as well as significant end-to-end program analysis speedups (up to 18.7x). Based on these results, we believe that our framework can serve as a new basis for static analysis with the Octagon numerical domain.
