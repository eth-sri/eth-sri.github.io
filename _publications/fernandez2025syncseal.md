---
ref: fernandez2025syncseal
title: "Geometric Image Synchronization with Deep Watermarking"
authors: Pierre Fernandez, Tomáš Souček, Nikola Jovanović, Hady Elsahar, Sylvestre-Alvise Rebuffi, Valeriu Lacatusu, Tuan Tran, Alexandre Mourachko
year: 2026
month: 5
venue: ICASSP
projects: watermarks
bibtex: "@misc{fernandez2025syncseal,
  title={Geometric Image Synchronization with Deep Watermarking},
  author={Pierre Fernandez, Tomáš Souček, Nikola Jovanović, Hady Elsahar, Sylvestre-Alvise Rebuffi, Valeriu Lacatusu, Tuan Tran, Alexandre Mourachko},
  year={2025},
  eprint={2509.15208},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}"
paper: https://arxiv.org/pdf/2509.15208
code: https://github.com/facebookresearch/wmar/tree/main/syncseal
---

Synchronization is the task of estimating and inverting geometric transformations (e.g., crop, rotation) applied to an image. This work introduces SyncSeal, a bespoke watermarking method for robust image synchronization, which can be applied on top of existing watermarking methods to enhance their robustness against geometric transformations. It relies on an embedder network that imperceptibly alters images and an extractor network that predicts the geometric transformation to which the image was subjected. Both networks are end-to-end trained to minimize the error between the predicted and ground-truth parameters of the transformation, combined with a discriminator to maintain high perceptual quality. We experimentally validate our method on a wide variety of geometric and valuemetric transformations, demonstrating its effectiveness in accurately synchronizing images. We further show that our synchronization can effectively upgrade existing watermarking methods to withstand geometric transformations to which they were previously vulnerable.
