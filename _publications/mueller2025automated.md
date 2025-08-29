---
ref: mueller2025automated
title: "Automated Benchmark Generation for Repository-Level Coding Tasks"
authors: Konstantinos Vergopoulos*, Mark Niklas Müller*, Martin Vechev
year: 2025
month: 05
venue: ICML
# awards: Spotlight
projects: codellm
bibtex: '@inproceedings{
			mueller2025automated,  
			title={Automated Benchmark Generation for Repository-Level Coding Tasks},  
			author={Konstantinos Vergopoulos and Mark Niklas M{\"{u}}ller and Martin T. Vechev},  
			booktitle={The Forty-Second International Conference on Machine Learning},  
			year={2025},  
			url={https://openreview.net/forum?id=qnE2m3pIAb}
		}'
paper: https://openreview.net/forum?id=qnE2m3pIAb
code: https://huggingface.co/datasets/LogicStar/SWA-Bench
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
image: assets/images/SWA_figure.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Code Agent development is an extremely active research area, where a reliable performance metric is critical for tracking progress and guiding new developments. This demand is underscored by the meteoric rise in popularity of SWE-Bench -- a benchmark that challenges code agents to generate patches addressing GitHub issues given the full repository as context. The correctness of generated patches is then evaluated by executing a human-written test suite extracted from the repository after the issue's resolution.

However, constructing benchmarks like SWE-Bench requires substantial manual effort to set up historically accurate execution environments for testing. Crucially, this severely limits the number of considered repositories, e.g., just 12 for SWE-Bench. Considering so few repositories, selected for their popularity runs the risk of leading to a distributional mismatch, i.e., the measured performance may not be representative of real-world scenarios running the riks of misguiding development efforts.

In this work, we address this challenge and introduce SetUpAgent, a fully automated system capable of historically accurate dependency setup, test execution, and result parsing. Using SetUpAgent, we generate two new datasets: (i) SWEE-Bench an extended version of SWE-Bench encompassing hundreds of repositories, and (ii) SWA-Bench a benchmark focusing on applications rather than libraries. Comparing these datasets to SWE-Bench with respect to their characteristics and code agent performance, we find significant distributional differences, including lower issue description quality and detail level, higher fix complexity, and most importantly up to 60% lower agent success rates.
