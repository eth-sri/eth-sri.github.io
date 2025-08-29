---
ref: dekoninck2024evading
title: "Evading Data Contamination Detection for Language Models is (too) Easy"
authors: Jasper Dekoninck, Mark Niklas Müller, Maximilian Baader, Marc Fischer, Martin Vechev
year: 2024
month: 02
venue: arXiv 
projects: llmevals
bibtex: "@article{dekoninck2024evading,
      title={Evading Data Contamination Detection for Language Models is (too) Easy}, 
      author={Jasper Dekoninck and Mark Niklas Müller and Maximilian Baader and Marc Fischer and Martin Vechev},
      year={2024},
      eprint={2402.02823},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/dekoninck2024evading.pdf
code: https://github.com/eth-sri/malicious-contamination
---
Large language models (LLMs) are widespread, with their performance on benchmarks frequently guiding user preferences for one model over another. However, the vast amount of data these models are trained on can inadvertently lead to contamination with public benchmarks, thus compromising performance measurements. While recently developed contamination detection methods try to address this issue, they overlook the possibility of deliberate contamination by malicious model providers aiming to evade detection. We argue that this setting is of crucial importance as it casts doubt on the reliability of public benchmarks for LLM evaluation. To more rigorously study this issue, we propose a categorization of both model providers and contamination detection methods. This reveals vulnerabilities in existing methods – we demonstrate how to exploit these with Evasive Augmentation Learning (EAL), a simple yet effective contamination technique that significantly inflates benchmark performance while completely evading current detection methods.