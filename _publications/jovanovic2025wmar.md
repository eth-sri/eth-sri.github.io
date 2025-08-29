---
ref: jovanovic2025wmar
title: "Watermarking Autoregressive Image Generation"
authors: Nikola Jovanović, Ismail Labiad, Tomáš Souček, Martin Vechev, Pierre Fernandez
year: 2025
month: 06
venue: arXiv
projects: watermarks
bibtex: "@article{jovanovic2025wmar,
  title={Watermarking Autoregressive Image Generation},
  author={Jovanović, Nikola and Labiad, Ismail and Souček, Tomáš and Vechev, Martin and Fernandez, Pierre},
  journal={arXiv},
  year={2025}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/jovanovic2025wmar.pdf
code: https://github.com/facebookresearch/wmar
---

Watermarking the outputs of generative models has emerged as a promising approach for tracking their provenance. Despite significant interest in autoregressive image generation models and their potential for misuse, no prior work has attempted to watermark their outputs at the token level. In this work, we present the first such approach by adapting language model watermarking techniques to this setting. We identify a key challenge: the lack of reverse cycle-consistency (RCC), wherein re-tokenizing generated image tokens significantly alters the token sequence, effectively erasing the watermark. To address this and to make our method robust to common image transformations, neural compression, and removal attacks, we introduce (i) a custom tokenizer-detokenizer finetuning procedure that improves RCC, and (ii) a complementary watermark synchronization layer. As our experiments demonstrate, our approach enables reliable and robust watermark detection with theoretically grounded p-values.