---
ref: wicker2025certification
title: "Certification for Differentially Private Prediction in Gradient-Based Training"
authors: Matthew Robert Wicker, Philip Sosnin, Igor Shilov, Adrianna Janik, Mark Niklas Müller, Yves-Alexandre de Montjoye, Adrian Weller, Calvin Tsay
year: 2025
month: 05
venue: ICLM
# awards: Spotlight
projects: safeai
bibtex: '@inproceedings{
			wicker2025certification,  
			title={Certification for Differentially Private Prediction in Gradient-Based Training},  
			author={Matthew Robert Wicker and Philip Sosnin and Igor Shilov and Adrianna Janik and Mark Niklas Müller and Yves-Alexandre de Montjoye and Adrian Weller and Calvin Tsay},  
			booktitle={The Forty-Second International Conference on Machine Learning},  
			year={2025},  
			url={https://openreview.net/forum?id=viXwXCkA7N}
		}'
paper: https://openreview.net/forum?id=viXwXCkA7N
# code: https://huggingface.co/datasets/LogicStar/SWA-Bench
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
image: assets/images/cert_train_fig.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

We study private prediction where differential privacy is achieved by adding noise to the outputs of a non-private model. Existing methods rely on noise proportional to the global sensitivity of the model, often resulting in sub-optimal privacy-utility trade-offs compared to private training. We introduce a novel approach for computing dataset-specific upper bounds on prediction sensitivity by leveraging convex relaxation and bound propagation techniques. By combining these bounds with the smooth sensitivity mechanism, we significantly improve the privacy analysis of private prediction compared to global sensitivity-based approaches. Experimental results across real-world datasets in medical image classification and natural language processing demonstrate that our sensitivity bounds are can be orders of magnitude tighter than global sensitivity. Our approach provides a strong basis for the development of novel privacy preserving technologies.
