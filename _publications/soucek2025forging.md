---
ref: soucek2025forging
title: "Transferable Black-Box One-Shot Forging of Watermarks via Image Preference Models"
authors: Tomas Soucek, Sylvestre-Alvise Rebuffi, Pierre Fernandez, Nikola Jovanović, Hady Elsahar, Valeriu Lacatusu, Tuan A. Tran, Alexandre Mourachko
year: 2025
month: 12
venue: NeurIPS
projects: watermarks
bibtex: "@article{soucek2025forging,
  title={Transferable Black-Box One-Shot Forging of Watermarks via Image Preference Models},
  author={Tomas Soucek, Sylvestre-Alvise Rebuffi, Pierre Fernandez, Nikola Jovanović, Hady Elsahar, Valeriu Lacatusu, Tuan A. Tran, Alexandre Mourachko},
	journal = {Advances in Neural Information Processing Systems},
  year={2025}
}"
---

Recent years have seen a surge in interest in digital content watermarking techniques due to the explosion of generative models, as well as increased legal pressure. With an ever-growing percentage of AI-generated content available online, watermarking plays an increasingly important role in ensuring content authenticity and attribution at scale. There have been many works assessing the robustness of watermarking to removal attacks, yet, watermark forging, the scenario when a watermark is stolen from genuine content and applied to malicious content, remains underexplored. In this work, we investigate watermark forging in the context of widely used post-hoc image watermarking. Our contributions are as follows. First, we introduce a preference model to assess whether an image is watermarked. The model is trained using a ranking loss on purely procedurally generated images without any need for real watermarks. Second, we show the capability of this model to remove and forge watermarks by optimizing the input image via backpropagation. This technique requires only a single watermarked image and works without knowledge of the watermarking model, making our attack much simpler and more practical than attacks introduced in related work. Third, we evaluate our proposed method on a variety of post-hoc image watermarking models, demonstrating that our approach can effectively forge watermarks, questioning the security of current watermarking approaches. Our code and further resources will be made publicly available.