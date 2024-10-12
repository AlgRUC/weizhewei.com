---
layout: page
title: Streaming & Sketch4ML
description: Streaming Data Algorithms - Summary, Sketch, Synopsis - and applications in Machine Learning
importance: 3
category: Projects
related_publications: true
related_posts: false
mermaid:
  enabled: true
  zoomable: false
---

> This project focuses on the <b style="color: blue">streaming data algorithms</b>, which maintain a small data structure in memory, and the applications of these algorithms in machine learning, which are called <b style="color: blue;">Sketch4ML</b>. The streaming algorithms can be used to optimize the machine learning algorithms, which are usually memory-intensive and time-consuming. 
{: .block-tip }

## Streaming algorithm

In computer science, **streaming algorithms** are algorithms for processing data streams in which the input is presented as a sequence of items and can be examined in only a few passes, typically just one. These algorithms are characterized by the following properties:

* Operate with limited computational/storage resources, generally logarithmic in the size of the stream and/or in the maximum value in the stream.
* Have limited processing time per item.
* To reduce computational/storage overhead, a certain error or/and fault probability can be tolerated.

As a result of these constraints, streaming algorithms often produce approximate answers based on a **sketch** of the data stream. 

## Sketch for Machine Learning (Sketch4ML)

**Sketch for Machine Learning (Sketch4ML)** is a technique that uses streaming algorithms to optimize machine learning algorithms. For example, matrix sketching has been employed to accelerate **second-order online gradient descent** (SON, [Luo et al., 2016](https://papers.nips.cc/paper_files/paper/2016/hash/15de21c670ae7c3f6f3f1f37029303c9-Abstract.html); RFD-ONS, [Luo et al., 2019](https://www.jmlr.org/papers/v20/17-773.html)), **online kernel learning** ([Calandriello et al., 2017](https://proceedings.neurips.cc/paper/2017/hash/366f0bc7bd1d4bf414073cabbadfdfcd-Abstract.html)), and **linear contextual bandits** (SOFUL, [Kuzborskij et al., 2019](https://proceedings.mlr.press/v89/kuzborskij19a.html); CBSCFD [Chen et al., 2020](https://www.ijcai.org/Proceedings/2020/0588.pdf); DBSLinUCB), as shown in the following figure.

```mermaid
graph LR
    A[Sketch4ML] --> B[Sketched Second-order online gradient descent]
    A --> C[Sketched online kernel learning]
    A --> D[Sketched linear contextual bandits]
    
    B --> B1["Sketched Online Newton (SON)"]
    B --> B2["RFD-ONS"]
    C --> C1["PROS-N-KONS"]
    D --> D1["SOFUL"]
    D --> D2["CBSCFD"]
    D --> D3["DBSLinUCB"]
```

### Optimal Matrix Sketching over Sliding Windows [[VLDB 2024](https://vldb.org/2024/)]

<!-- Badges -->
<p>
  <a href="https://doi.org/10.14778/3665844.3665847">
    <img src="https://img.shields.io/badge/doi-10.14778%2F3665844.3665847-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://arxiv.org/abs/2405.07792">
    <img src="https://img.shields.io/badge/arxiv-2405.07792-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://badge.dimensions.ai/details/id/pub.1174559675">
    <img src="https://badge.dimensions.ai/badge?style=rectangle&count=0" alt="dimensions" />
  </a>
  <a href="https://github.com/yinhanyan/DS-FD">
    <img src="https://img.shields.io/badge/yinhanyan%2FDS--FD-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/yinhanyan/DS-FD/stargazers">
    <img src="https://img.shields.io/github/stars/yinhanyan/DS-FD" alt="stars" />
  </a>
</p>

In this work, we proposes the optimal matrix sketch algorithm DS-FD on sliding windows, which achives the lower bound of space complexity for solving the matrix sketching problem over sliding windows. The paper addressed the open question of the lower bounds of space complexity for any deterministic algorithms solving the matrix sketching problem over sliding windows. The answer to this open problem confirms that our DS-FD algorithm is optimal in terms of space complexity.

<div class="w-75 mx-auto">
  {% include figure.liquid loading="eager" path="assets/img/optimal2024yin.png" title="example image" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
  The space upper bound of DS-FD and lower bound in various senarios.
</div>

The paper {% cite yin2024optimal %} is accepted by VLDB 2024 and nominated for the Best Research Paper. If you are interested in the details, please refer to the [paper](https://doi.org/10.14778/3665844.3665847), [arxiv](https://arxiv.org/abs/2405.07792) or the [code](https://github.com/yinhanyan/DS-FD).


## Sketch4ML

### Dyadic Block Sketching

TBD



## Roadmap

- [x] Streaming Algorithms
    - [x] Frequent Directions over Sliding Windows
- [ ] Sketch4ML
    - [ ] Dyadic Block Sketching 