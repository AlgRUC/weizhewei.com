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

{% tab gnn4science EquiPocket %}

### EquiPocket: an E(3)-Equivariant Geometric Graph Neural Network for Ligand Binding Site Prediction [[ICML 2024](https://icml.cc/Conferences/2024)]

<p>
  <a href="https://openreview.net/forum?id=lmaRfJcDhgY">
    <img src="https://img.shields.io/badge/openreview-EquiPocket-b31b1b?style=flat
" />
  </a>
  <a href="https://github.com/fengyuewuya/equipocket">
    <img src="https://img.shields.io/badge/fengyuewuya%2FEquiPocket-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/fengyuewuya/equipocket/stargazers">
    <img src="https://img.shields.io/github/stars/fengyuewuya/equipocket" alt="stars" />
  </a>
  
</p>

{% bibliography --query @*[key=zhang2024equipocket]* %}

#### Citation

```bibtex
@inproceedings{weiequipocket,
  title={EquiPocket: an E (3)-Equivariant Geometric Graph Neural Network for Ligand Binding Site Prediction},
  author={Wei, Zhewei and Yuan, Ye and Li, Chongxuan and Huang, Wenbing and others},
  booktitle={Forty-first International Conference on Machine Learning}
}
```

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

{% tab gnn4science HierAffinity %}

### HierAffinity: Predicting Protein-Ligand Binding Affinity With Hierarchical Modeling [[DASFAA 2024](https://www.dasfaa2024.org/)]

<p>
  <a href="https://link.springer.com/chapter/10.1007/978-981-97-5575-2_3">
    <img src="https://img.shields.io/badge/springer-HierAffinity-b31b1b?style=flat
" alt="arxiv" />
  </a>
</p>

{% bibliography --query @*[key=zhang2024predicting]* %}

#### Citation

```bibtex
@inproceedings{zhang2024hieraffinity,
  title={HierAffinity: Predicting Protein-Ligand Binding Affinity With Hierarchical Modeling},
  author={Zhang, Yang and Wei, Zhewei and Huang, Wenbing and Li, Chongxuan},
  booktitle={International Conference on Database Systems for Advanced Applications},
  pages={37--52},
  year={2024},
  organization={Springer}
}
```

{% endtab %}

{% tab gnn4science FedHCD %}

### Federated Heterogeneous Contrastive Distillation for Molecular Representation Learning [[CIKM 2024](http://www.cikmconference.org/)]

<!-- Badges -->
<p>
  <a href="https://dl.acm.org/doi/abs/10.1145/3627673.3679725">
    <img src="https://img.shields.io/badge/ACM-FedHCD-b31b1b?style=flat
" />
  </a>
</p>

{% bibliography --query @*[key=feng2024federated]* %}

#### Citation

```bibtex
@inproceedings{feng2024federated,
  title={Federated Heterogeneous Contrastive Distillation for Molecular Representation Learning},
  author={Feng, Jinjia and Wang, Zhen and Wei, Zhewei and Li, Yaliang and Ding, Bolin and Xu, Hongteng},
  booktitle={Proceedings of the 33rd ACM International Conference on Information and Knowledge Management},
  pages={1038--1048},
  year={2024}
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

{% bibliography --query @*[key=zhou2023unimol]* %}

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

{% tab gnn4science MGMAE %}

### MGMAE: Molecular Representation Learning by Reconstructing Heterogeneous Graphs with A High Mask Ratio [[CIKM 2022](http://www.cikmconference.org/)]

<!-- Badges -->
<p>
  <a href="https://dl.acm.org/doi/abs/10.1145/3511808.3557395">
    <img src="https://img.shields.io/badge/ACM-MGMAE-b31b1b?style=flat
" />
  </a>
</p>

{% bibliography --query @*[key=feng2022mgmae]* %}

#### Citation

```bibtex
@inproceedings{feng2022mgmae,
  title={MGMAE: molecular representation learning by reconstructing heterogeneous graphs with A high mask ratio},
  author={Feng, Jinjia and Wang, Zhen and Li, Yaliang and Ding, Bolin and Wei, Zhewei and Xu, Hongteng},
  booktitle={Proceedings of the 31st ACM International Conference on Information \& Knowledge Management},
  pages={509--519},
  year={2022}
}
```

{% endtab %}

{% endtabs %}
