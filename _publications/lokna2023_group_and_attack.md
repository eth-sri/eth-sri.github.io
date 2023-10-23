---
ref: 
title: "Group and Attack: Auditing Differential Privacy"
authors: Johan Lokna, Anouk Paradis, Dimitar I. Dimitrov, Martin Vechev
year: 2023
month: 11
venue: CCS
projects: diff-privacy
bibtex: '@inproceedings{lokna2023group,
  title={Group and Attack: Auditing Differential Privacy},
  author={Lokna, Johan and Paradis, Anouk and Dimitrov, Dimitar I and Vechev, Martin},
  booktitle={Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security},
  year={2023}
}'
code: https://github.com/eth-sri/Delta-Siege
paper: https://files.sri.inf.ethz.ch/website/papers/lokna2023_group_and_attack.pdf
---

Epsilon-delta differential privacy has seen increased adoption recently, especially in private machine learning applications. While this privacy definition allows provably limiting the amount of information leaked by an algorithm, practical implementations of differentially private algorithms often contain subtle vulnerabilities. This motivates the need for effective tools that can audit epsilon-delta differential privacy algorithms before deploying them in the real world. However, existing state-of-the-art-tools for auditing epsilon-delta differential privacy directly extend the tools for epsilon differential privacy by fixing eiter epsilon or delta in the violation search, inherently restricting their ability to efficiently discover violations of epsilon-delta differential privacy. We present a novel method to efficiently discover epsilon-delta differential privacy violations based on the key insight that many epsilon-delta pairs can be grouped as they result in the same algorithm. Crucially, our method is orthogonal to existing approaches and, when combined, results in a faster and more precise violation search. We implemented our approach in a tool called Delta-Siege and demonstrated its effectiveness by discovering vulnerabilities in most of the evaluated frameworks, several of which were previously unknown. Further, in 84% of cases, Delta-Siege outperforms existing state-of-the-art auditing tools. Finally, we show how Delta-Siege outputs can be used to find the precise root cause of vulnerabilities, an option no other differential privacy testing tool currently offers.

