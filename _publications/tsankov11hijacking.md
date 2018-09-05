---
  ref: tsankov11hijacking
  title: 'Execution Hijacking: Improving Dynamic Analysis By Flying Off Course'
  authors: Petar Tsankov, Wei Jin, Alessandro Orso, Saurabh Sinha
  year: 2011
  venue: IEEE ICST  
  projects: 
  awards:
  bibtex:
  paper: https://files.sri.inf.ethz.ch/website/papers/tsankov11hijacking.pdf
  talk:
  slides:
---

Typically, dynamic-analysis techniques operate on a small subset of all possible program behaviors, which limits their effectiveness and the representativeness of the computed results. To address this issue, a new paradigm is emerging: execution hijacking, consisting of techniques that explore a larger set of program behaviors by forcing executions along specific paths. Although hijacked executions are infeasible for the given inputs, they can still produce feasible behaviors that could be observed under other inputs. In such cases, execution hijacking can improve the effectiveness of dynamic analysis without requiring the (expensive) generation of additional
inputs. To evaluate the usefulness of execution hijacking, we defined, implemented, and evaluated several variants of it. Specifically, we performed an empirical study where we assessed whether execution hijacking could improve the effectiveness of a common dynamic analysis: memory error detection. The results of the study show that execution hijacking, if suitably performed, can indeed improve dynamic analysis.
