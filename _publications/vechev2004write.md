---
ref: vechev2004write
title: Write Barrier Elision for Concurrent Garbage Collectors
authors: Martin Vechev and David F. Bacon
year: 2004
venue: ACM ISMM
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{vechev2004write,
  title={Write barrier elision for concurrent garbage collectors},
  author={Vechev, Martin T and Bacon, David F},
  booktitle={Proceedings of the 4th international symposium on Memory management},
  pages={13--24},
  year={2004},
  organization={ACM}}'
paper: Vechev04Barriers.pdf
talk: 
slides: 
---

Concurrent garbage collectors require write barriers to preserve consistency, but these barriers impose significant direct and indirect costs. While there has been a lot of work on optimizing write barriers, we present the first study of their elision in a concurrent collector. We show conditions under which write barriers are redundant, and describe how these conditions can be applied to both incremental update or snapshot-at-the-beginning barriers. We then evaluate the potential for write barrier elimination with a trace-based limit study, which shows that a significant percentage of write barriers are redundant. On average, 54% of incremental barriers and 83% of snapshot barriers are unnecessary.