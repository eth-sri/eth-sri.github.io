---
ref: gloaguen2025diffusionwatermark
title: "Watermarking Diffusion Language Models"
authors: Thibaud Gloaguen, Robin Staab, Nikola Jovanović, Martin Vechev
year: 2025
month: 09
venue: GenProCC @ NeurIPS 2025
projects: watermarks
bibtex: "@article{gloaguen2025watermarkingdiffusionlanguagemodels,
    title={Watermarking Diffusion Language Models}, 
    author={Thibaud Gloaguen and Robin Staab and Nikola Jovanović and Martin Vechev},
    year={2025},
    eprint={2509.24368},
    archivePrefix={arXiv},
    primaryClass={cs.LG},
    url={https://arxiv.org/abs/2509.24368}, 
}"
paper: https://arxiv.org/abs/2509.24368
code: https://github.com/eth-sri/diffusion-lm-watermark
website: https://diffusionlm-watermark.ing
---

We introduce the first watermark tailored for diffusion language models (DLMs), an emergent LLM paradigm able to generate tokens in arbitrary order, in contrast to standard autoregressive language models (ARLMs) which generate tokens sequentially. While there has been much work in ARLM watermarking, a key challenge when attempting to apply these schemes directly to the DLM setting is that they rely on previously generated tokens, which are not always available with DLM generation. In this work we address this challenge by: (i) applying the watermark in expectation over the context even when some context tokens are yet to be determined, and (ii) promoting tokens which increase the watermark strength when used as context for other tokens. This is accomplished while keeping the watermark detector unchanged. Our experimental evaluation demonstrates that the DLM watermark leads to a >99\% true positive rate with minimal quality impact and achieves similar robustness to existing ARLM watermarks, enabling for the first time reliable DLM watermarking.