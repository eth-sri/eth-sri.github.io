---
ref: ivanov2022seeds
title: "Fast and Optimal Sequence-to-Graph Alignment Guided by Seeds"
authors: Pesho Ivanov, Benjamin Bichsel, Martin Vechev
year: 2022
month: 5
venue: RECOMB
projects: computational-biology
awards:
bibtex: 
paper: https://www.biorxiv.org/content/10.1101/2021.11.05.467453
talk: 
slides:
code: https://github.com/eth-sri/astarix
---

We present a novel A* seed heuristic enabling fast and optimal sequence-to-graph
alignment, guaranteed to minimize the edit distance of the alignment assuming
non-negative edit costs. We phrase optimal alignment as a shortest path problem
and solve it by instantiating the A* algorithm with our novel seed heuristic.
The key idea of the seed heuristic is to extract seeds from the read, locate
them in the reference, mark preceding reference positions by crumbs, and use the
crumbs to direct the A* search. We prove admissibility of the seed heuristic,
thus guaranteeing alignment optimality. Our implementation extends the free and
open source AStarix aligner and demonstrates that the seed heuristic outperforms
all state-of-the-art optimal aligners including GraphAligner, Vargas, PaSGAL,
and the prefix heuristic previously employed by AStarix. Specifically, we
achieve a consistent speedup of >60x on both short Illumina reads and long HiFi
reads (up to 25kbp), on both the E. coli linear reference genome (1Mbp) and the
MHC variant graph (5Mbp). Our speedup is enabled by the seed heuristic
consistently skipping >99.99% of the table cells that optimal aligners based on
dynamic programming compute.
