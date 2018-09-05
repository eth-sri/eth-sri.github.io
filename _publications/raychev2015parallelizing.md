---
ref: raychev2015parallelizing
title: Parallelizing User-Defined Aggregations using Symbolic Execution
authors: Veselin Raychev, Madanlal Musuvathi, Todd Mytkowicz   
year: 2015
venue: ACM SOSP
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{raychev2015parallelizing,
  title={Parallelizing user-defined aggregations using symbolic execution},
  author={Raychev, Veselin and Musuvathi, Madanlal and Mytkowicz, Todd},
  booktitle={Proceedings of the 25th Symposium on Operating Systems Principles},
  pages={153--167},
  year={2015},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/sosp15-symple.pdf
talk: 
slides: 
---

User-defined aggregations (UDAs) are integral to large-scale data-processing systems, such as MapReduce and Hadoop, because they let programmers express application-specific aggregation logic. System-supported associative aggregations, such as counting or finding the maximum, are data-parallel and thus these systems optimize their execution, leading in many cases to orders-of-magnitude performance improvements. These optimizations, however, are not possible on arbitrary UDAs.

This paper presents SYMPLE, a system for performing MapReduce-style groupby-aggregate queries that automatically parallelizes UDAs. Users specify UDAs using stylized C++ code with possible loop-carried dependences. SYMPLE parallelizes these UDAs by breaking dependences using symbolic execution, where unresolved dependences are treated as symbolic values and the SYMPLE runtime partially evaluates the resulting symbolic expressions on concrete input. Programmers write UDAs using SYMPLE’s symbolic data types, which look and behave like standard C++ types. These data types (i) encode specialized decision procedures for efficient symbolic execution and (ii) generate compact symbolic expressions for efficient network transfers. Evaluation on both Amazon’s Elastic cloud and a private 380-node Hadoop cluster housing terabytes of data demonstrates that SYMPLE reduces network communication up to several orders of magnitude and job latency by as much as 5.9x for a representative set of queries.
