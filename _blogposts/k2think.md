---
layout: blogpost
category: other
title: "Debunking the Claims of K2-Think"
blogpost-authors: "Niels Mündler*, Jasper Dekoninck*, Nikola Jovanović*, Ivo Petrov, Martin Vechev" 
date: 2025-09-12
thumbnail: thumbnails/falling_k2.png
image: assets/thumbnails/falling_k2.png
usemathjax: false
tldr: >
    The reported performance of K2-Think is overstated, relying on flawed evaluation marked by contamination, unfair comparisons, and misrepresentation of both its own and competing models’ results. 
excerpt: >
    K2-Think is a recently released LLM that claims performance on par with GPT-OSS 120B and DeepSeek v3.1, despite having fewer parameters. As we discuss below, the reported gains are overstated, relying on flawed evaluation marked by contamination, unfair comparisons, and misrepresentation of both its own and competing models’ results. 
tweet-id: 1966482446276542757
---
<style>
    .blogpost-thumbnail {
        width: 30% !important;
    }
    @media (max-width: 768px) {
    /* styles that apply when viewport is 768px or smaller */
    .blogpost-title {
      font-size: 30px;
    }

    .blogpost-thumbnail {
        width: 60% !important;
    }

    .page-subtitle {
      font-size: 18px
    }

    .tldr {
      padding: 5% 5%;
    }

    .blogpost-col {
      text-align: left;
    }

    .blogpost-col p,
    .blogpost-col h3 {
      padding-left: 10px !important;
      padding-right: 10px !important;
    }
  }
    
</style>
<a href="https://www.k2think.ai/">K2-Think</a> (different from Kimi-K2!) is a reasoning LLM released a few days ago that claims performance on par with GPT-OSS 120B and DeepSeek v3.1, but with fewer parameters, as described in their <a href="https://arxiv.org/abs/2509.07604">paper</a>. It received a significant amount of attention online, with several news articles being published on the topic (<a href="https://www.wired.com/story/uae-releases-a-tiny-but-powerful-reasoning-model/">Wired</a>, <a href="https://www.forbes.com/sites/patrickmoorhead/2025/09/09/the-uae-showcases-its-abilities-in-ai-reasoning-with-k2-think-model/">Forbes</a>, <a href="https://www.cnbc.com/2025/09/09/abu-dhabi-launches-ai-reasoning-model-to-rival-openai-deepseek.html">CNBC</a>, etc.). However, as we discuss below, the reported gains are overstated, relying on flawed evaluation marked by contamination, unfair comparisons, and misrepresentation of both its own and competing models’ results. Instead, K2-Think performs slightly worse than other models of similar size, such as GPT-OSS 20B, Nemotron-32B or Qwen3 30B 2507.

### Evaluation is invalid due to data contamination

We find clear evidence of data contamination. 

For math, both SFT and RL datasets used by K2-Think include the DeepScaleR dataset, which in turn includes Omni-Math problems. As K2-Think uses Omni-Math for its evaluation, this suggests contamination. We confirm this using approximate string matching, finding that at least 87 of the 173 Omni-Math problems that K2-Think uses in evaluation were also included in its training data. Interestingly, there is a large overlap between the creators of the RL dataset, Guru, and the authors of K2-Think, who should have been fully aware of this.

We find a similar issue in the LiveCodeBench evaluation. Around 22% of samples used in K2-Think’s evaluation appear in their SFT dataset. The original authors of the SFT dataset (AM-Team) include a decontamination step, removing problems from Oct 2024 onward. However, K2-Think’s LiveCodeBench evaluation uses all problems from July 2024 onwards, 22% of which were thus also previously seen in training. 

The net effect is that the evaluation results on mathematics and code are <strong>invalid</strong>.

### Unfair comparisons with best-of-n and external model use

The paper’s main results table reports K2-Think’s best-of-3 performance, a <a href="https://aclanthology.org/2024.acl-long.617/">well-known</a> <a href="https://arxiv.org/abs/2501.13007">method</a> to improve model performance. All other models are evaluated using best-of-1, posing them at a significant disadvantage. To make matters worse, the best-of-3 judgment is made by an unspecified “external model”, which could have arbitrary size. This same external model is also used to provide K2-Think with detailed problem-solving plans. The authors define this entire pipeline as “K2-Think,” with the model itself being only one component, undermining the claim that K2-Think relies only on a small 32B parameter model.

Comparing this pipeline to other models without the pipeline, as done in the paper, is invalid. The pipeline itself could be easily applied to other models and would similarly increase their score. Without the external help, K2-Think’s performance is worse than Nemotron 32B, a similarly-sized model trained with a similar methodology on Qwen2.5 32B and released in July.

<div class="table-container">
  <div class="table-wrap" role="region" aria-label="K2-Think performance comparison">
    <table>
      <thead>
        <tr>
          <th scope="col" class="model"><strong>Model</strong></th>
          <th scope="col"><strong>AIME 2024</strong></th>
          <th scope="col"><strong>AIME 2025</strong></th>
          <th scope="col"><strong>HMMT25</strong></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row" class="name">K2-Think</th>
          <td>86.26</td>
          <td>77.72</td>
          <td>66.46</td>
        </tr>
        <tr>
          <th scope="row" class="name">Nemotron 32B</th>
          <td>87.09</td>
          <td>82.71</td>
          <td>67.29</td>
        </tr>
        <tr>
          <th scope="row" class="name"> Qwen3 30B (July)*</th>
          <td>-</td>
          <td>85.00</td>
          <td>71.40</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p class="muted" style="margin-top:10px; text-align: center">
    Table 1: Performance comparison of K2-Think without external help, and Nemotron 32B (both finetunes of Qwen2.5 32B), as well as Qwen3 30B. Results for Qwen3 (*) are taken from their <a href="https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507">model page</a>. All other results are taken from the <a href="https://arxiv.org/pdf/2509.07604">K2-Think paper</a>.
  </p>
</div>

### Misrepresenting results of other models

The report fails to adequately evaluate other models. Most notably, GPT-OSS is only run with medium instead of high reasoning effort, which is the recommended setting for reasoning benchmarks.

Additionally, K2-Think uses outdated versions for many models. For example, even though they evaluate GPT-OSS, which was released in August, the Qwen3 models evaluated in the paper do not appear to be the latest versions of these models, published in July. Specifically, for the three benchmarks that overlap between the releases of Qwen3 and K2-Think (AIME 2025, HMMT 2025, GPQA-Diamond), the results seem to match the older versions, which are significantly (15-20%) below the reported results of the July versions. 

<span id="footnote-source-1">In the table below, we compare the <a href="https://arxiv.org/abs/2505.09388">self-reported results of Qwen3</a> with the numbers reported in the <a href="https://arxiv.org/pdf/2509.07604">K2-Think paper</a>. The scores attributed to Qwen3-30B are far lower than expected, even when compared against the earlier non-July release.<sup><a href="#footnote-1">1</a></sup></span>

<div class="table-container">
  <style>
    .table-container {
      --bg: #ffffff;
      --text: #0f172a;
      --muted: #6b7280;
      --border: #e5e7eb;
      --header-bg: #f8fafc;
      font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
      color: var(--text);
    }
    .table-wrap { max-width: 100%; overflow: auto; border-radius: 11px; } table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 11px; line-height: 1.25; }
    thead th {
      background: var(--header-bg);
      border-bottom: 1px solid var(--border);
      padding: 12px 14px;
      text-align: center;
      font-weight: 600;
      white-space: nowrap;
    }
    table th {
        background: var(--header-bg);
    }
    tbody th[scope="row"] {
      text-align: left;
      font-weight: 600;
      white-space: nowrap;
    }
    tbody td {
      text-align: center;
    }
    th, td {
      padding: 12px 14px;
      font-variant-numeric: tabular-nums;
    }
    tbody tr:nth-child(odd) td,
    tbody tr:nth-child(odd) th[scope="row"] {
      background: #fcfcfd;
    }
    /* Rounded corners */
    table thead tr:first-child th:first-child { border-top-left-radius: 12px; }
    table thead tr:first-child th:last-child  { border-top-right-radius: 12px; }
    table tbody tr:last-child th[scope="row"] { border-bottom-left-radius: 12px; }
    table tbody tr:last-child td:last-child   { border-bottom-right-radius: 12px; }
    thead th:nth-child(3),
    tbody td:nth-child(4),
    thead th:nth-child(6),
    tbody td:nth-child(7),
    .model,
    .name  {
      border-right: 2px solid var(--border) !important;
    }
    .muted { color: var(--muted); font-variant-numeric: normal; }
    .na { color: var(--muted); text-align: center; }
    @media (max-width: 768px) {
      .table-wrap > table th,
      .table-wrap > table td {
        white-space: nowrap;
      }
      .table-wrap {
        width: 100%;
        max-width: 100vw;           /* cap at viewport */
        overflow-x: auto !important;
        overflow-y: hidden;
        -webkit-overflow-scrolling: touch;
        scrollbar-gutter: stable both-edges;
      }
      .table-wrap > table {
        display: block;  
        width: max-content;         /* grow to fit columns */
        min-width: 100%;            /* at least fill wrapper */
      }
    }
  </style>

  <div class="table-wrap" role="region" aria-label="Benchmark scores">
    <table>
      <thead>
        <tr>
          <th rowspan="2" scope="col" class="model">Model</th>
          <th colspan="3" scope="colgroup" class="model">AIME 2025</th>
          <th colspan="3" scope="colgroup" class="model">HMMT 2025</th>
          <th colspan="2" scope="colgroup" class="model">GPQA-Diamond</th>
        </tr>
        <tr>
          <th scope="col">Self-Report</th>
          <th scope="col">MathArena</th>
          <th scope="col">K2-Think</th>
          <th scope="col">Self-Report</th>
          <th scope="col">MathArena</th>
          <th scope="col">K2-Think</th>
          <th scope="col">Self-Report</th>
          <th scope="col">K2-Think</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row" class="name">Qwen3-30B (Think)</th>
          <td>70.90</td>
          <td>70.00</td>
          <td>58.14 <span class="muted">(?)</span></td>
          <td>49.80</td>
          <td>50.83</td>
          <td>23.54 <span class="muted">(?)</span></td>
          <td>65.80</td>
          <td>58.91 <span class="muted">(?)</span></td>
        </tr>
        <tr>
          <th scope="row" class="name">Qwen3-30B (Think, July)</th>
          <td>85.00</td>
          <td class="na">&mdash;</td>
          <td class="na">&mdash;</td>
          <td>71.40</td>
          <td class="na">&mdash;</td>
          <td class="na">&mdash;</td>
          <td>73.40</td>
          <td class="na">&mdash;</td>
        </tr>
        <tr>
          <th scope="row" class="name">Qwen3-235B (Think)</th>
          <td>81.50</td>
          <td>80.83</td>
          <td>75.43</td>
          <td>62.50</td>
          <td>62.50</td>
          <td>61.88</td>
          <td>71.10</td>
          <td>65.55</td>
        </tr>
        <tr>
          <th scope="row" class="name">Qwen3-235B (Think, July)</th>
          <td>92.30</td>
          <td class="na">&mdash;</td>
          <td class="na">&mdash;</td>
          <td>83.90</td>
          <td class="na">&mdash;</td>
          <td class="na">&mdash;</td>
          <td>81.10</td>
          <td class="na">&mdash;</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p class="muted" style="margin-top:10px; text-align: center">
    Table 2: Comparing reported scores from <a href="https://arxiv.org/abs/2505.09388">Qwen3 technical report</a> and <a href="https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507">model pages</a>, <a href="https://matharena.ai/">MathArena benchmark</a>, and <a href="https://arxiv.org/pdf/2509.07604">K2-Think paper</a> on AIME 2025, HMMT 2025, and GPQA-Diamond.
  </p>
</div>

### Giving more weight to high-scoring math benchmarks

Finally, K2-Think reports aggregate math scores using a “micro average”, weighing each of the four benchmarks (AIME24, AIME25, HMMT, OmniMath-Hard) by their respective number of tasks, instead of averaging individual benchmark scores equally. While meant to quantify overall math ability of the model, such an average metric is heavily dominated by OmniMath-Hard (~66% of the total score). Not only is this K2-Think’s strongest benchmark, but it is also directly tied to the contamination issues discussed above.


### Our own evaluation

To validate our analysis, we ran K2-Think on our <a href="https://matharena.ai">MathArena benchmark</a> in a fair comparison against other models. We followed the recommended hyperparameters for K2-Think, using temperature 1, p = 0.95, and 64,000 output tokens. <strong>The results show that while K2-Think is a competent model, it falls well short of the performance claimed in the paper and the popular media articles.</strong> In particular, it is far from matching DeepSeek v3.1 or GPT-OSS 120B, despite the authors’ claim to the contrary. In fact, it shows that K2-Think’s math capabilities are not even on par with the smaller GPT-OSS 20B model.

![](/assets/blog/k2think/matharena.png){: .blogpost-img100}

### Conclusion

Overall, we found that the K2-Think model makes wrong claims in several locations: It evaluates on data it was trained on, relies on an external model and additional samples for its claimed performance gains, and artificially reduces the scores of compared models and reweighs its own scores to claim parity or superiority.

Open models are good and we evaluate them all the time. However, flawed evaluations and exaggerated claims are not helpful. We hope the authors fix these issues in the next iteration of K2-Think and correctly present their achievements. 


#### Footnotes


<span id="footnote-1"><a href="#footnote-source-1"><sup>1</sup></a> Since the K2-Think paper does not specify whether the thinking model was used for Qwen3-30B, it is possible that the authors evaluated the instruction-tuned variant instead. However, under that assumption, the reported numbers suddenly become implausibly high, raising further doubts about the validity of these comparisons.</span>