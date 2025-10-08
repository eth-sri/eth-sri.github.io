---
ref: venev2025qblaze
title: "qblaze: An Efficient and Scalable Sparse Quantum Simulator"
authors: Hristo Venev, Thien Udomsrirungruang, Dimitar Dimitrov, Timon Gehr, Martin Vechev
year: 2025
month: 10
venue: ACM OOPSLA
projects: quantum
awards:
bibtex: '@inproceedings{venev2025qblaze,
  title={qblaze: An Efficient and Scalable Sparse Quantum Simulator},
  author={Hristo Venev and Thien Udomsrirungruang and Dimitar Dimitrov and Timon Gehr and Martin Vechev},
  booktitle={ACM SIGPLAN Notices},
  year={2025},
  organization={ACM}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/oopsla25-qblaze.pdf
---

Classical simulation of quantum circuits is critical for the development of implementations of quantum
algorithms: it does not require access to specialized hardware, facilitates debugging by allowing direct access
to the quantum state, and is the only way to test on inputs that are too big for current NISQ computers.
Many quantum algorithms rely on invariants that result in sparsity in the state vector. A sparse state vector
simulator only computes with non-zero amplitudes. For important classes of algorithms, this results in an
asymptotic improvement in simulation time. While promising prior work has investigated ways to exploit
sparsity, it is still unclear what is the best way to scale sparse simulation to modern multi-core architectures.
In this work, we address this challenge and present qblaze, a highly optimized sparse state vector simulator
based on (i) a compact sorted array representation, and (ii) new, easily parallelizable and highly-scalable
algorithms for all quantum operations. Our extensive experimental evaluation shows that qblaze is often
orders-of-magnitude more efficient than prior sparse state vector simulators even on a single thread, and also
that qblaze scales well to a large number of CPU cores.
Overall, our work enables testing quantum algorithms on input sizes that were previously out of reach.
