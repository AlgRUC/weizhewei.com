---
layout: page
title: GNN4Science
nologo: true
description: Graph Neural Networks for Science
img: 
importance: 7
category: works
related_publications: false
related_posts: false
tabs: true
---

{% tabs gnn4science %}

{% tab gnn4science Background %}

> **GNN4Science** applies Graph Neural Networks (GNNs) to solve complex problems in fields like chemistry, biology, material science, and physics. By representing scientific data as graphs, where entities such as atoms, molecules, or biological components are nodes and their interactions are edges, GNN4Science enables accurate predictions and uncovers hidden patterns in large-scale datasets. It is particularly effective for tasks like molecular property prediction, protein folding, material design, and physics simulations, providing powerful tools to accelerate scientific discovery and deepen our understanding of the natural world. This page is a collection of our work on GNN4Science.
{: .block-tip }

<h3 style="text-align: center;">From <span style="color: red;">Representation Models</span> to <span style="color: red;">Downstream Tasks</span></h3>
<h4 style="text-align: center;">Key Inductive Bias: <span style="color: red;">Equivariance</span></h4>

<div class="mx-auto">
  {% include figure.liquid loading="lazy" path="assets/img/publication_preview/gnn4science1.svg" title="From Representation Models to Downstream Tasks" class="img-fluid rounded z-depth-1" %}
</div>

<br>

<h3 style="text-align: center;">Generative Models</h3>

<div class="mx-auto">
  {% include figure.liquid loading="lazy" path="assets/img/publication_preview/gnn4science2.svg" title="Generative Models" class="img-fluid rounded z-depth-1" %}
</div>

<br>

The goal of GNN4Science is to bridge the gap between cutting-edge machine learning techniques and scientific research, particularly in fields such as chemistry, biology, material science, and physics. One area of particular focus is geometric GNNs based on structural modeling, which have shown exceptional performance in these tasks. A key challenge in this area is how to encode structural information while maintaining the crucial inductive bias of equivariance — the property that ensures the model’s predictions remain consistent under transformations, such as rotations or translations, which is essential for many scientific applications.

{% endtab %}

{% tab gnn4science S-MolSearch %}

### S-MolSearch: 3D Semi-supervised Contrastive Learning for Bioactive Molecule Search [[NeurIPS 2024](https://nips.cc/Conferences/2024)]

<p>
  <a href="https://arxiv.org/abs/2409.07462">
    <img src="https://img.shields.io/badge/arxiv-2409.07462-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
    <a href="https://bohrium.dp.tech/apps/s-molsearch">
    <img src="https://img.shields.io/badge/Bohrium_Apps-S--MolSearch-blue
" />
  </a>
  
</p>

{% bibliography --query @*[key=zhou2024smolsearch]* %}

#### Citation

```bibtex
@inproceedings{
  zhou2024smolsearch,
  title={S-MolSearch: 3D Semi-supervised Contrastive Learning for Bioactive Molecule Search},
  author={Gengmo Zhou and Zhen Wang and Feng Yu and Guolin Ke and Zhewei Wei and Zhifeng Gao},
  booktitle={The Thirty-eighth Annual Conference on Neural Information Processing Systems},
  year={2024},
  url={https://openreview.net/forum?id=wJAF8TGVUG}
}
```

{% endtab %}

{% tab gnn4science Uni-Mol %}

### Uni-Mol: A Universal 3D Molecular Representation Learning Framework [[ICLR 2023](https://iclr.cc/Conferences/2023)]

<!-- Badges -->
<p>
  <a href="https://chemrxiv.org/engage/chemrxiv/article-details/6402990d37e01856dc1d1581">
    <img src="https://img.shields.io/badge/chemrxiv-Uni--Mol-b31b1b?style=flat
" />
  </a>
  <a href="https://github.com/deepmodeling/Uni-Mol">
    <img src="https://img.shields.io/badge/deepmodeling%2FUni--Mol-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/deepmodeling/Uni-Mol/stargazers">
    <img src="https://img.shields.io/github/stars/deepmodeling/Uni-Mol" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=zhou2023uni]* %}

#### Citation

```bibtex
@inproceedings{
  zhou2023unimol,
  title={Uni-Mol: A Universal 3D Molecular Representation Learning Framework},
  author={Gengmo Zhou and Zhifeng Gao and Qiankun Ding and Hang Zheng and Hongteng Xu and Zhewei Wei and Linfeng Zhang and Guolin Ke},
  booktitle={The Eleventh International Conference on Learning Representations },
  year={2023},
  url={https://openreview.net/forum?id=6K2RM6wVqKu}
}
```

{% endtab %}

{% endtabs %}
