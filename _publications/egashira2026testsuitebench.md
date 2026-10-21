---
ref: egashira2026testsuitebench
title: "TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications"
authors: Kazuki Egashira, Niels Mündler-Sasahara, Mark Niklas Müller, Martin Vechev
year: 2026
month: 10
day: 9
venue: arXiv
projects: codellm,llmevals
bibtex: |
  @misc{egashira2026testsuitebench,
    title={TestSuiteBench: Coding Agents Struggle to Generate Strong Test Suites from Specifications},
    author={Kazuki Egashira and Niels Mündler-Sasahara and Mark Niklas Müller and Martin Vechev},
    year={2026},
    eprint={2610.13065},
    archivePrefix={arXiv},
    primaryClass={cs.SE},
    url={https://arxiv.org/abs/2610.13065}
  }
paper: https://arxiv.org/abs/2610.13065
code: https://github.com/eth-sri/testsuitebench
website: https://testsuitebench.com/
---

Coding agents are increasingly used to create large software projects. While code-generation benchmarks have scaled accordingly to full applications, test-generation benchmarks remain limited to individual functions or bug fixes. In particular, generating complete test suites for complex software from scratch remains unexplored. To address this gap, we introduce TestSuiteBench, a benchmark of 165 open-source applications, each with a structured and detailed specification of intended behavior, a reference implementation, a reference test suite, and on average 74 mutants. Each mutant is generated from a single requirement of the specification and refined to isolate that behavior: 73% are killed by exactly one reference test and, on average, by only 0.2% of the remaining tests. We find that even frontier coding agents struggle to generate strong test suites given our specifications, achieving mutation scores below 60%, despite their suites being largely valid and 88% of their tests passing on the reference implementation. We observe that generated test suites often lack relevant input combinations and are smaller than reference test suites. Meanwhile, implementations generated for the same specifications pass 82% of the reference tests. These results show agents can build software they cannot verify, a gap that directly limits fully autonomous software development.