---
ref: dan2017finding
title: Finding Fix Locations for CFL-Reachability Analyses via Minimum Cuts 
authors: Andrei Dan, Manu Sridharan, Satish Chandra, Jean-Baptiste Jeannin, Martin Vechev
year: 2017
venue: CAV
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{dan2017finding,
  title={Finding Fix Locations for CFL-Reachability Analyses via Minimum Cuts},
  author={Dan, Andrei Marian and Sridharan, Manu and Chandra, Satish and Jeannin, Jean-Baptiste and Vechev, Martin},
  booktitle={International Conference on Computer Aided Verification},
  pages={521--541},
  year={2017},
  organization={Springer}}'
paper: cav17-mincut.pdf
talk: 
slides: 
---

Static analysis tools are increasingly important for ensuring code quality. Ideally, all warnings from a static analysis would be addressed, but the volume of warnings and false positives usually makes this effort prohibitive. We present techniques for finding fix locations, a small set of program locations where fixes can be applied to address all static analysis warnings. We focus on analyses expressible as context-freelanguage reachability, where a set of fix locations is naturally expressed as a min-cut of the CFL graph. We show, surprisingly, that computing such a CFL min-cut is NP-hard. We then phrase the problem of finding CFL min-cuts as an optimization problem which allows us to trade-off the size of the cut vs. the preservation of computed information. We then show how to solve the optimization problem via a MaxSAT encoding. Our evaluation shows that we compute fix location sets that are significantly smaller than both the number of warnings and, in the case of a true CFL min-cut, the fix location sets from a normal min-cut.