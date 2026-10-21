---
layout: "blogpost"
category: "other"
title: "Probing the SynthID-text deployment on Gemini APIs"
blogpost-authors: "Thibaud Gloaguen, Robin Staab, Kristian Minchev, Martin Vechev"
date: "2026-10-21"
thumbnail: "probing-synthid-gemini-apis/magnifier.png"
hero: "/assets/blog/probing-synthid-gemini-apis/hero.png"
mathjax_font: "TeX"
usemathjax: true
tldr: "Google DeepMind's SynthID-Text is the first large-scale LLM watermark deployment, yet little is known about how it is actually deployed. Using our work, we, for the first time, identify several key watermark hyperparameters. We find that: (1) <strong>all Gemini models are watermarked with the exact same scheme</strong>, (2) <strong>the context size of the watermark is 4 tokens</strong> (the same as the default from the open-source SynthID release), and (3) <strong>Gemini models also watermark the (hidden) thinking trace</strong>. Our findings allow us to better understand how watermarks are actually deployed in practice and understand the trade-offs made by LLM providers."
excerpt: "Google DeepMind's SynthID-Text is the first large-scale LLM watermark deployment, yet little is known about how it is actually deployed. Using our work, we, for the first time, identify several key watermark hyperparameters. We find that: (1) all Gemini models are watermarked with the exact same scheme, (2) the context size of the watermark is 4 tokens (the same as the default from the open-source SynthID release), and (3) Gemini models also watermark the (hidden) thinking trace. Our findings allow us to better understand how watermarks are actually deployed in practice and understand the trade-offs made by LLM providers."
---

[SynthID-Text](https://www.nature.com/articles/s41586-024-08025-4) is the first major publicized large-scale deployment of an LLM watermarking algorithm, announced in 2024. It was originally deployed in the [Gemini app](https://deepmind.google/blog/watermarking-ai-generated-text-and-video-with-synthid/), and following the requirements of the [EU AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50) is [allegedly](https://discuss.ai.google.dev/t/does-gemini-api-text-output-carry-synthid-watermarking-gemini-2-5-flash-lite-gemini-3-1-flash-lite-eu-ai-act-art-50-2/177241/4) deployed in the API. While Google released an [open-source](https://github.com/google-deepmind/synthid-text) implementation of SynthID-Text, they have not discussed how they deploy their watermark in practice. In this blog post, using our [ICLR 2025 work](https://www.sri.inf.ethz.ch/publications/gloaguen2024detectingwatermarks), we answer the following questions: do all Gemini models share the same watermark? What are the hyperparameters used by the deployed SynthID-Text? Is the (hidden) thinking trace watermarked?

Answering those questions has important practical implications. With the watermark hyperparameters, attackers can then mount more sophisticated [watermark stealing](https://watermark-stealing.org/) attacks that allow them to either remove or spoof the watermark. Furthermore, knowing that lite models use the same watermark as larger models enables attackers to attack the SynthID watermark at a much lower cost. Lastly, knowing whether the thinking trace is watermarked has significant implications for the research community. In particular, recent works ([ReasonMark](https://arxiv.org/abs/2601.05144), [Marking the Wrong Symptoms: Evaluating LLM Watermarks in Medical Texts](https://arxiv.org/html/2607.20462#S4.SS4)) have been discussing whether the thinking trace should be watermarked and how watermarking the thinking trace impacts reasoning accuracy.

### How does text watermarking work?

The idea behind most LLM watermarks, including SynthID-Text, is to change the probabilities of the next tokens to leave a detectable pattern in the generated text. Let’s start with a small example.

![](/assets/blog/probing-synthid-gemini-apis/red-green-context-seeding.png){: .blogpost-img100}


{:.blogpost-caption}
*Illustration of the Red-Green watermarking algorithm. Given a partial sentence, the LLM outputs a probability distribution over the next token. The watermark uses the previously generated token as a seed to partition the vocabulary into red and green tokens. It then increases the probability of green tokens. Thus, a watermarked text has more green tokens than a non-watermarked one.*

The LLM is generating the following text: "ETH is a" and needs to choose the next word. Let's assume that the LLM gives probability 1/2 to "great" and 1/2 to "nice". Without a watermark, the sampling algorithm would simply choose either word with probability 1/2. A simple watermark could increase the probability of "great" to 3/4 (green word) and decrease that of "nice" to 1/4 (red word). Here the color is chosen deterministically by the watermark. Both words are still possible, but "great" is now chosen more often! Repeating this kind of transformation throughout the text leaves a statistical pattern: the generated text contains more of the green words favored by the watermark than we would otherwise expect.

SynthID-Text uses a more complex transformation than this simple probability shift, designed to not alter the quality of the generated text. But the underlying idea remains the same: change the probabilities deterministically so that the text carries a detectable statistical pattern.

How do we decide which tokens to favor? The deterministic choice should look random, but the watermark detector needs to be able to reproduce it. To achieve this, the watermark combines a secret key with a few preceding tokens, called the watermark's context, to compute a seed. This seed determines which tokens are favored: the same key and context give the same choices, while a different context can favor different tokens. A detector with the key can reconstruct these choices from the text and check whether unusually many favored tokens were generated. This reproducibility across queries is also the property our black-box tests exploit.

### Black-Box Detection of Language Model Watermarks

In "[Black-Box Detection of Language Model Watermarks](https://www.sri.inf.ethz.ch/publications/gloaguen2024detectingwatermarks)" we introduced several statistical tests that allow us to detect, from text responses alone, whether an API is watermarked or not. We have now updated our method to be more resilient to modern LLM scenarios (e.g., thinking models).


![](/assets/blog/probing-synthid-gemini-apis/context-size.png){: .blogpost-img100}

{:.blogpost-caption}
*Illustration of context-size probing. Changing a token outside the four-token watermark context preserves the choice probabilities, while changing one inside it changes them.*

In our original work, the idea was to see if, when asking the LLM to choose a random word, we observe a strong dependency based on the context. Specifically, to infer the size of the watermark context, we force the model to generate replies with this specific format: $$t_{1}\dots t_{n} \text{choice}$$. We then, for all $$i$$, vary $$t_{i}$$ while keeping the other ones fixed. If $$i$$ is smaller than the watermark context length, varying $$t_{i}$$ will significantly change the choice (because it changes which tokens are favored by the watermark). If $$i$$ is bigger than the watermark context size, varying $$t_{i}$$ should not change the choice (because the tokens favored by the watermark are the same).



### Autoresearch to update our method

The original method presented above faces several issues when used in practice, e.g., thinking models may decide the choice of the words in their thinking trace without the intended context.

```example
User: Finish the sentence: "I bought 2222" using a word from the list [bananas, strawberries, apples, pears].

Model: <think>I am asked to finish the sentence with a word from the list. I will use the word bananas. Thus my final answer is: 'I bought 2222 bananas'.</think>
I bought 2222 bananas.
```

In this example, the word `bananas` was chosen by the model in the thinking trace: there is no influence due to the context `2222` and thus our test would have failed.

To update our method, we let auto-research agents figure out how to overcome this issue. Specifically, I gave an Opus 5.5 agent access to 3 black-box APIs (from its perspective) with only 1 of them watermarked. The agent was tasked with figuring out which one is watermarked. It also had access to a local GPU for conducting its experiments. After about 24 hours of research, it came up with an improvement to our method!

{: .blogpost-note}
> The three black-box APIs served Qwen3.5-9B, Gemma-4-E4B-it, and Olmo-3-7B-Think, with their identities hidden from the agent. For local experiments, the agent had access to LiquidAI’s LFM2.5-2.6B on an NVIDIA RTX PRO 6000 GPU (96 GB). Downloading any additional model weights, from Hugging Face or elsewhere, was forbidden, preventing direct comparisons between the APIs and local copies of the same models.

The updated method uses the same context-dependency mechanism as our work. It just changes the prompt to:

```
Answer immediately without deliberation. Write a story about a lighthouse keeper in exactly 20 sentences, one sentence per line. Each line must begin with the given code copied exactly (single letters separated by single spaces), then a space, then the sentence. Use these codes in this order, one per line:
r o o g o p d y
j d u d c o p d
e y h u k t v r
[17 more codes]
Output only the 20 lines.
```

Here, each code corresponds to a different sequence $$t_{1},\dots,t_{n}$$ and the choice of words after $$t_{1},\dots,t_{n}$$ is no longer constrained to a specific list, giving more entropy to the model. A typical reply would be

```
<think>I'll start by drafting the sentences. I'll need to create a narrative arc,
building a sense of place and atmosphere.

r o o g o p d y Silas climbed the spiral iron staircase as the sun began to sink below the jagged horizon.
j d u d c o p d The brass lantern housing gleamed under his weathered, calloused hands.
e y h u k t v r Outside, a brisk northern wind howled against the thick granite tower walls.
[...]</think>

r o o g o p d y Silas climbed the spiral iron staircase as the sun began to sink below the jagged horizon.
j d u d c o p d The brass lantern housing gleamed under his weathered, calloused hands.
e y h u k t v r Outside, a brisk northern wind howled against the thick granite tower walls.
[...]
```

In this case, we find that the model consistently generates in its thinking trace the choice of the next word with the context $$t_{1}\dots t_{n}$$.

To detect the watermark, we construct families of codes from a reference code. Each family contains variants that preserve exactly its last 1, 2, 3, 4, or more letters, while changing the earlier letters. We verify that each letter corresponds to one token, so sharing 4 trailing letters means sharing exactly the 4 tokens immediately before the generated word. Each story uses one randomly selected code from each family, and we repeat the experiment across many stories.

For each code, we record the first word of the sentence that follows it. We then build a word-preference profile: which opening words appear unusually often after this code, and which appear unusually rarely?  We compare these profiles as we increase the number of shared trailing letters. If the watermark uses a context of 4 tokens, codes sharing only their last 3 letters generally produce different watermark seeds and therefore different word preferences. Once they share their last 4 letters, their seeds match, and their preferences should become as similar as those observed when repeating the experiment with the same code. We therefore look for a sudden jump in similarity, followed by a plateau: the location of the jump reveals the watermark’s context size!

{: .blogpost-note}
> Precisely, we introduce a similarity metric $$S_m$$ and a global alignment metric $$r$$. We also repeat each query twice independently (query sets $$A$$ and $$B$$) to better calibrate the method.
>
> Let $$N^A_{cw}$$ count how often code $$c$$ is followed by word $$w$$ in query half $$A$$. Under independence between codes and words, its expected count is $$E^A_{cw}=N^A_{c\cdot}N^A_{\cdot w}/N^A_{\cdot\cdot}$$. Define the standardized residual $$R^A_{cw}=(N^A_{cw}-E^A_{cw})/\sqrt{E^A_{cw}}$$, and similarly for the independent half $$B$$. The similarity between codes $$c$$ and $$d$$ is
>
> $$
> G_{cd}=\frac12\sum_w\left(R^A_{cw}R^B_{dw}+R^B_{cw}R^A_{dw}\right).
> $$
>
> We average $$G_{cd}$$ over distinct code pairs sharing exactly $$m$$ trailing tokens within each family, then average equally across families to obtain $$S_m$$. The implementation also averages over multiple random query splits. A larger $$S_m$$ means that these codes reproducibly favor and disfavor the same words.
>
> Let $$S_{0}$$ be the baseline for codes sharing no trailing tokens, and $$S_{\mathrm{same}}$$ the similarity of a code with itself across independent samples. We define $$r \coloneq (S_m-S_0)/(S_{\mathrm{same}}-S_0)$$. When $$r \approx 0$$ this means that $$S_{m} = S_{0}$$ and that sharing $$m$$ trailing tokens has the same biases as sharing $$0$$ tokens. Conversely, with $$r \approx 1$$ this means that $$S_{m} \approx S_{\mathrm{same}}$$ and that sharing $$m$$ trailing tokens has the same biases as sharing the exact same code.

### Applying our method to all Gemini models

We apply our method using stories of 20 sentences, each beginning with a 16-letter code, i.e. $$t_{1},\dots,t_{16}$$. We use the same pool of 220 codes across models and collect 2,000 stories per model. We disable thinking whenever the API allows it.


[![](/assets/blog/probing-synthid-gemini-apis/gemini-context-alignment.png){: .blogpost-img50 .blogpost-plot}](/assets/blog/probing-synthid-gemini-apis/gemini-context-alignment.png)

{:.blogpost-caption}
*Alignment scores for 9 Gemini models depending on the number of shared trailing tokens in each code word. We see that, consistently, the alignment jumps at 4 tokens, indicating that the watermark context size is 4 on each model.*

Our results show that for codes sharing less than 3 trailing tokens (3 included) on all models we see no similar word preferences across codes. However, for codes sharing more than 4 trailing tokens we see on all models that each different code consistently leads to the same word preference. This means that the watermark context size of all evaluated Gemini models is 4 tokens.

[![](/assets/blog/probing-synthid-gemini-apis/gemini-watermark-correlation.png){: .blogpost-img50 .blogpost-plot}](/assets/blog/probing-synthid-gemini-apis/gemini-watermark-correlation.png)

{:.blogpost-caption}
*Correlation between the watermark biases of all Gemini models. We find that all Gemini models share the same context bias, indicating that they are watermarked with the same watermarking key.*

Furthermore, if we look at the word preference across models, we find that for each shared set of trailing tokens, all evaluated models show the same word preference. This means that all models share the exact same watermarking key!

### Detecting that the thinking trace is watermarked

<!-- Citations: add these references at the start of “Detecting that the thinking trace is watermarked”, replacing the citation placeholder. Gloaguen et al., LLM Fingerprinting via Semantically Conditioned Watermarks, Appendix E.1 (opening/closing watermark tokens), discusses selectively watermarking the trace or answer; Liu et al., ReasonMark, Section 2.1, leaves thinking unwatermarked; Rieff et al., Marking the Wrong Symptoms, Section 4.4, compares full and final-answer-only watermarking on medical reasoning tasks. These sources motivate the design question; the Gemini deployment finding comes from our experiments below. -->

A question in the watermark literature is whether model providers should watermark the thinking trace ([ReasonMark](https://arxiv.org/abs/2601.05144), [Marking the Wrong Symptoms: Evaluating LLM Watermarks in Medical Texts](https://arxiv.org/html/2607.20462#S4.SS4)) . With our probing, we find that Google decided to watermark the thinking traces of Gemini.

We realized the thinking trace of Gemini 3.8 Flash is watermarked quite inadvertently. On the Gemini 3.8 Flash API, you can enable/disable the thinking trace. We therefore ran the above experiment with thinking enabled and disabled.

[![](/assets/blog/probing-synthid-gemini-apis/thinking-context-alignment.png){: .blogpost-img50 .blogpost-plot}](/assets/blog/probing-synthid-gemini-apis/thinking-context-alignment.png)

{:.blogpost-caption}
*Alignment scores for Gemini 3.8 Flash without and with thinking depending on the number of shared trailing tokens in each code word. We see that the alignment jumps at 4 tokens without thinking and 3 with thinking.*

As we can see in the figure, the jump in similarity appears at 3 tokens with thinking on (orange curve) whereas it appears at 4 tokens with thinking off (blue curve). This seems to suggest that the watermark context is not the same when thinking is on or off. But is it really?

Because of these unexpected results, we push our investigation further. The Gemini API allows us to obtain thinking summaries of the thinking trace. We therefore decided to look in detail at those summaries.

```text
1.  `g e x q m j h r` High atop the jagged peaks of Mount Ashen, a solitary beast slumbered beneath centuries of frozen mist.
2.  `f r x t k b m o` His crimson scales shimmered like polished rubies caught in the pale morning sun.
3.  `h b x f o d d r` For a thousand years, the dragon had ignored the petty squabbles of the mortal realm below.
```

In most cases, the summary shows verbatim the story the model was about to generate. In particular, in the summary, Gemini always inserted a backtick after the code and before the first word chosen. From this simple observation, we can infer a few things. First, the text we observe outside the thinking trace is almost a copy-paste of the content in the thinking trace. In particular, this means that there is zero entropy for the watermark to be applied. Yet, we observe the watermark with our test: this means the watermark was applied during the thinking.

Furthermore, the backtick explains why with thinking we see the jump at 3 tokens. When we do our test, in practice the context with which the watermark is applied is $$t_{1},\dots,t_{n}\text{`}$$, yet in the visible output we only see $$t_{1}\dots t_{n}$$. Hence, from our method’s perspective it seems the relevant context was $$t_{n-2}t_{n-1}t_{n}$$ whereas in practice it was $$t_{n-2}t_{n-1}t_{n}\text{`}$$. To confirm this hypothesis, we verify that the bias with thinking was the same as the bias without thinking when adding a backtick to every code: this turns out to be true in practice!

### Why watermark the thinking trace?


We now know that Google decided to watermark the thinking trace of their model. In this part, we try to give sensible explanations for why this choice makes sense.

Intuitively, because the thinking trace is hidden anyway, one would think that there is no need for it to be watermarked: end users should never see it anyway. Yet, our tests already give an explanation for why watermarking the thinking trace makes sense. We saw that with our prompt the thinking model first drafted the answer in its trace and then copy-pasted it almost exactly in the visible answer. If the trace were not watermarked, the answer would also not be watermarked. 

We therefore propose a simple “attack” that would generate non-watermarked text with thinking models if their thinking trace is not watermarked. We ask the model to generate a reply with a fixed number of sentences: on all tested models, this forces the model to first explicitly write its reply in the thinking trace to “count” the sentences and then copy-paste them in the visible output.

[![](/assets/blog/probing-synthid-gemini-apis/thinking-watermark-attack.png){: .blogpost-img50 .blogpost-plot}](/assets/blog/probing-synthid-gemini-apis/thinking-watermark-attack.png)


Specifically, we evaluate our attack on Qwen3.8-27B with 1,000 ELI5 prompts and a SynthID watermark with a context of 4 tokens, once with the thinking trace watermarked and once without. We use the following prompt:
```
Answer in 10 sentences exactly this question: {eli5 question}
```

As we can see in the attached figure, when the thinking is watermarked, we can easily detect the watermark even at low FPRs. However, when the thinking is not watermarked, the watermark is almost undetectable (TPR=FPR).