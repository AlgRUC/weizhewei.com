---
layout: post
title: Streaming & Sketch4ML
description: Streaming Data Algorithms - Summary, Sketch, Synopsis - and applications in Machine Learning
img: assets/img/optimal2024yin.png
importance: 3
category: works
related_publications: true
related_posts: false
toc:
  beginning: true
---

<!-- <style>
img.badge {
    width: auto;
    height: 20px; /* 设置图片的高度 */
}
</style> -->

<!-- PROJECT LOGO -->
<div align="center">
  <!-- <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h1 align="center">Streaming & Sketch4ML</h1>

  <p align="center">
    Streaming Data Algorithms - Summary, Sketch, Synopsis - and applications in Machine Learning
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br /> -->
    <!-- <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

In many of today’s big data applications, in particular, for highspeed streaming data, the volume and velocity of the data are so high that we cannot afford to store everything. Therefore, streaming algorithms have received a lot of attention in the research community, which uses only sublinear space by sacrificing slightly on accuracy. 

**Streaming algorithms** work by maintaining a small data structure in memory, which is usually called a *sketch, summary, or synopsis*. The streaming algorithms can also be used to optimize the machine learning algorithms, which are called **Sketch4ML**.

This page is a collection of our work on streaming algorithms and Sketch4ML.



## Streaming

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

#### Citation

```bibtex
@article{10.14778/3665844.3665847,
    author = {Yin, Hanyan and Wen, Dongxie and Li, Jiajun and Wei, Zhewei and Zhang, Xiao and Huang, Zengfeng and Li, Feifei},
    title = {Optimal Matrix Sketching over Sliding Windows},
    year = {2024},
    issue_date = {May 2024},
    publisher = {VLDB Endowment},
    volume = {17},
    number = {9},
    issn = {2150-8097},
    url = {https://doi.org/10.14778/3665844.3665847},
    doi = {10.14778/3665844.3665847},
    journal = {Proc. VLDB Endow.},
    month = {aug},
    pages = {2149–2161},
    numpages = {13}
}
```



## Sketch4ML

### Dyadic Block Sketching

TBD



## Roadmap

- [x] Streaming Algorithms
    - [x] Frequent Directions over Sliding Windows
- [ ] Sketch4ML
    - [ ] Dyadic Block Sketching 