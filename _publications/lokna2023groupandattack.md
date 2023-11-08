---
ref: lokna2023groupandattack
title: "Group and Attack: Auditing Differential Privacy"
authors: Johan Lokna, Anouk Paradis, Dimitar I. Dimitrov, Martin Vechev
year: 2023
month: 11
venue: ACM CCS
projects: diff-privacy
awards:
bibtex: '@inproceedings{lokna2023group,
  title={Group and Attack: Auditing Differential Privacy},
  author={Lokna, Johan and Paradis, Anouk and Dimitrov, Dimitar I and Vechev, Martin},
  booktitle={Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security},
  year={2023}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/ccs23-groupattack.pdf
code: https://github.com/eth-sri/Delta-Siege
---

(𝜖, 𝛿) differential privacy has seen increased adoption recently, especially in private machine learning applications. While this privacy definition allows provably limiting the amount of information leaked by an algorithm, practical implementations of differentially private algorithms often contain subtle vulnerabilities. This motivates the need for effective tools that can audit (𝜖, 𝛿) differential privacy algorithms before deploying them in the real world. However, existing state-of-the-art-tools for auditing (𝜖, 𝛿) differential privacy directly extend the tools for 𝜖-differential privacy by fixing either 𝜖 or 𝛿 in the violation search, inherently restricting their ability to efficiently discover violations of (𝜖, 𝛿) differential privacy.

We present a novel method to efficiently discover (𝜖, 𝛿) differential privacy violations based on the key insight that many (𝜖, 𝛿) pairs can be grouped as they result in the same algorithm. Crucially, our method is orthogonal to existing approaches and, when combined, results in a faster and more precise violation search.

We implemented our approach in a tool called Delta-Siege and demonstrated its effectiveness by discovering vulnerabilities in most of the evaluated frameworks, several of which were previously unknown. Further, in 84% of cases, Delta-Siege outperforms existing state-of-the-art auditing tools. Finally, we show how Delta-Siege outputs can be used to find the precise root cause of vulnerabilities, an option no other differential privacy testing tool currently offers.
