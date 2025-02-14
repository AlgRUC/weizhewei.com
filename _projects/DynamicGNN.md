---
layout: page
title: Dynamic Graph Learning
nologo: true
description:  
img: 
importance: 6
category: Projects
related_publications: false
related_posts: false
tabs: true
---

{% tabs dgnn %}

{% tab dgnn Background %}

In recent years, dynamic graph learning has emerged as a significant research topic, as dynamic graphs provide an accurate abstraction of the ubiquitous dynamic systems in the real world. Dynamic graphs represent entities as nodes and their interactions as timestamped edges. Compared to generic graph learning, dynamic graph learning emphasizes the temporal information to model network dynamics. Our long-term goal is to develop effective dynamic graph models that can accurately capture network dynamics and apply these methods to real-world applications, such as recommendation systems and "Who-To-Follow" features in online social networks.

Existing studies primarily categorize temporal graphs into two types: continuous-time dynamic graphs (CTDGs) and discrete-time dynamic graphs (DTDGs). Our first study on dynamic graphs, [DecoupledGNN](https://dl.acm.org/doi/10.14778/3598581.3598595), proposes a decoupled model for both CTDGs and DTDGs. It leverages a dynamic Personalized PageRank (PPR) propagation technique to efficiently compute node embeddings and utilizes recurrent neural networks (RNNs) to capture the evolving patterns of nodes.

We are also examining existing benchmarks for dynamic graph learning and are in the process of developing a new benchmark. The accompanying paper and code will be released soon!

{% endtab %}

{% tab dgnn DecoupledGNN %}

{% bibliography --query @*[key=zheng2023decoupled]* %}

<p>
  <a href="https://arxiv.org/abs/2305.08273">
    <img src="https://img.shields.io/badge/arxiv-2305.08273-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/zheng-yp/DecoupledDGNN">
    <img src="https://img.shields.io/badge/zheng--yp%2FDecoupledDGNN-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/zheng-yp/DecoupledDGNN/stargazers">
    <img src="https://img.shields.io/github/stars/zheng-yp/DecoupledDGNN" alt="stars" />
  </a>
</p>


```bibtex
@article{zheng2023decoupled,
  title={Decoupled Graph Neural Networks for Large Dynamic Graphs},
  author={Zheng, Yanping and Wei, Zhewei and Liu, Jiajun},
  journal={Proceedings of the VLDB Endowment},
  volume={16},
  number={9},
  pages={2239--2247},
  year={2023},
  publisher={VLDB Endowment}
}
```

{% endtab %}

{% tab dgnn DGNNSurvey %}

{% bibliography --query @*[key=zheng2024survey]* %}

<p>
  <a href="https://arxiv.org/abs/2404.18211">
    <img src="https://img.shields.io/badge/arxiv-2404.18211-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
</p>

```bibtex
@article{zheng2024survey,
  author = {Yanping ZHENG, Lu YI, Zhewei WEI},
  title = {A survey of dynamic graph neural networks},
  publisher = {Front. Comput. Sci.},
  year = {2025},
  journal = {Frontiers of Computer Science},
  volume = {19},
  number = {6},
  eid = {196323},
  numpages = {0},
  pages = {196323},
  keywords = {graph neural networks;dynamic graph;temporal modeling;large-scale},
  url = {https://journal.hep.com.cn/fcs/EN/abstract/article_37965.shtml},
  doi = {10.1007/s11704-024-3853-2}
}    
```
{% endtab %}

{% tab dgnn TGB-Seq %}

{% bibliography --query @*[key=yi2025tgb]* %}

<p>
  <a href="https://arxiv.org/abs/2502.02975">
    <img src="https://img.shields.io/badge/arxiv-2502.02975-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/TGB-Seq/TGB-Seq">
    <img src="https://img.shields.io/badge/TGB--Seq-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/TGB-Seq/TGB-Seq/stargazers">
    <img src="https://img.shields.io/github/stars/TGB-Seq/TGB-Seq" alt="stars" />
  </a>
</p>

```bibtex
@inproceedings{yi2025tgb,
  title={TGB-Seq Benchmark: Challenging Temporal GNNs with Complex Sequential Dynamics},
  author={Yi, Lu and Peng, Jie and Zheng, Yanping and Mo, Fengran and Wei, Zhewei and Ye, Yuhang and Zixuan, Yue and Huang, Zengfeng},
  journal={arXiv preprint arXiv:2502.02975},
  year={2025}
}
```

{% endtab %}

{% endtabs %}