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
---

In recent years, dynamic graph learning has emerged as a significant research topic, as dynamic graphs provide an accurate abstraction of the ubiquitous dynamic systems in the real world. Dynamic graphs represent entities as nodes and their interactions as timestamped edges. Compared to generic graph learning, dynamic graph learning emphasizes the temporal information to model network dynamics. Our long-term goal is to develop effective dynamic graph models that can accurately capture network dynamics and apply these methods to real-world applications, such as recommendation systems and "Who-To-Follow" features in online social networks.

Existing studies primarily categorize temporal graphs into two types: continuous-time dynamic graphs (CTDGs) and discrete-time dynamic graphs (DTDGs). Our first study on dynamic graphs, [DecoupledGNN](https://dl.acm.org/doi/10.14778/3598581.3598595), proposes a decoupled model for both CTDGs and DTDGs. It leverages a dynamic Personalized PageRank (PPR) propagation technique to efficiently compute node embeddings and utilizes recurrent neural networks (RNNs) to capture the evolving patterns of nodes.

We are also examining existing benchmarks for dynamic graph learning and are in the process of developing a new benchmark. The accompanying paper and code will be released soon!

## Selected publications

{% bibliography --query @*[key=Zheng_2023]* %}

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