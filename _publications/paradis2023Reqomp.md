---
ref: paradis2023Reqomp
title: "Reqomp: Space-constrained Uncomputation for Quantum Circuits"
authors: Anouk Paradis, Benjamin Bichsel, Martin Vechev
year: 2022
month: 12
venue: arXiv
projects: quantum
paper: https://arxiv.org/abs/2212.10395
code: https://github.com/eth-sri/Reqomp
---

Quantum circuits must run on quantum computers with tight limits on qubit and gate counts. To generate circuits respecting both limits, a promising opportunity is exploiting uncomputation to trade qubits for gates. We present Reqomp, a method to automatically synthesize correct and efficient uncomputation of ancillae while respecting hardware constraints. For a given circuit, Reqomp can offer a wide range of trade-offs between tightly constraining qubit count or gate count. Our evaluation demonstrates that Reqomp can significantly reduce the number of required ancilla qubits by up to 96%. On 80% of our benchmarks, the ancilla qubits required can be reduced by at least 25% while never incurring a gate count increase beyond 28%. 

