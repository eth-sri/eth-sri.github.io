---
ref: mueller2021precise
title: "Synthetiq: Fast and Versatile Quantum Circuit Synthesis"
authors: Anouk Paradis*, Jasper Dekoninck*, Benjamin Bichsel, Martin Vechev
year: 2024
month: 3
venue: OOPSLA
projects: quantum
bibtex: '@misc{paradis2024synthetiq,
      title={Synthetiq: Fast and Versatile Quantum Circuit Synthesis}, 
      author={Anouk Paradis and Jasper Dekoninck and Benjamin Bichsel and Martin Vechev},
      year={2024}'
paper: https://files.sri.inf.ethz.ch/website/papers/paradis2024synthetiq.pdf
---
To implement quantum algorithms on quantum computers it is crucial to decompose their operators into the limited gate set supported by those computers. Unfortunately, existing works automating this essential task are generally slow and only applicable to narrow use cases.

We present Synthetiq, a method to synthesize quantum circuits implementing a given specification over arbitrary finite gate sets, which is faster and more versatile than existing works. Synthetiq utilizes Simulated Annealing instantiated with a novel, domain-specific energy function that allows developers to leverage partial specifications for better efficiency. Synthetiq further couples this synthesis method with a custom simplification pass, to ensure efficiency of the found circuits.

We experimentally demonstrate that Synthetiq can generate better implementations than were previously known for multiple relevant quantum operators including RCCCX, CCT, CCiSWAP, C&radic;<span style="text-decoration: overline">SWAP</span>, and C&radic;<span style="text-decoration: overline">iSWAP</span>.

Our extensive evaluation also demonstrates Synthetiq frequently outperforms a wide variety of more specialized tools in their own domains, including (i) the well-studied task of synthesizing fully specified operators in the Clifford+T gate set, (ii) &epsilon;-approximate synthesis of multi-qubit operators in the same gate set, and (iii) synthesis tasks with custom gate sets. On all those tasks, Synthetiq is typically one to two orders of magnitude faster than previous state-of-the-art and can tackle problems that were previously out of the reach of any synthesis tool.
