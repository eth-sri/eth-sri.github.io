---
ref: ivanov2020astarix
title: "AStarix: Fast and Optimal Sequence-to-Graph Alignment"
authors: Pesho Ivanov, Benjamin Bichsel, Harun Mustafa, André Kahles, Gunnar Rätsch, Martin Vechev
year: 2020
month: 01
venue: RECOMB
projects: computational-biology
awards:
bibtex: "@article{ivanov2020astarix,
  title={AStarix: Fast and Optimal Sequence-to-Graph Alignment},
  author={Ivanov, Pesho and Bichsel, Benjamin and Mustafa, Harun and Kahles, Andre and R{\"a}tsch, Gunnar and Vechev, Martin},
  journal={RECOMB},
  year={2020},
  publisher={Cold Spring Harbor Laboratory}
}"
paper: https://www.biorxiv.org/content/10.1101/2020.01.22.915496v2.full.pdf
talk: https://www.youtube.com/watch?v=NJ6_zCM3C7Q
slides: 
code: https://github.com/eth-sri/astarix
---

We present an algorithm for the optimal alignment of sequences to genome graphs. It works by phrasing the edit distance minimization task as finding a shortest path on an implicit alignment graph. To find a shortest path, we instantiate the A? paradigm with a novel domain-specific heuristic function that accounts for the upcoming subsequence in the query to be aligned, resulting in a provably optimal alignment algorithm called AStarix. Experimental evaluation of AStarix shows that it is 1–2 orders of magnitude faster than state-of-the-art optimal algorithms on the task of aligning Illumina reads to reference genome graphs. Implementations and evaluations are available at https://github.com/eth-sri/astarix.
