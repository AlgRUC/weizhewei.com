---
layout: page
title: Spectral GNN
nologo: true
description: Spectral Graph Neural Networks
importance: 1
category: works
related_publications: false
related_posts: false
tabs: true
---


{% tabs spectralgnn %}

{% tab spectralgnn Background %}

> Spectral Graph Neural Networks (**Spectral GNNs**) are a class of neural networks designed to operate on graph-structured data, leveraging spectral methods to analyze the properties of graphs. They employ the graph Laplacian matrix, which encapsulates the structure of the graph, and use its eigenvalues and eigenvectors to process signals on the graph's nodes and edges. By transforming graph data into the spectral domain, Spectral GNNs can efficiently capture global and local graph patterns. This page is a collection of our work on SpectralGNNs.
{: .block-tip }

<div class="mx-auto">
  {% include figure.liquid loading="eager" path="assets/img/publication_preview/Spectral.svg" title="Spectral GNNs" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
  Evolution of Spectral Graph Neural Networks
</div>

Spectral GNNs often involve computationally expensive operations like eigen-decomposition, which limits scalability to large graphs. However, recent advancements have focused on improving efficiency by approximating these operations, making Spectral GNNs applicable to real-world tasks such as node classification, link prediction, and graph clustering. These models are particularly effective in applications where the structural information of the graph plays a critical role, including social networks, recommendation systems, and bioinformatics.

{% endtab %}

{% tab spectralgnn PSHGCN %}

### Spectral Heterogeneous Graph Convolutions via Positive Noncommutative Polynomials {% cite He_2024 %} [[WWW 2024](https://www2024.thewebconf.org/)]

<p>
  <a href="https://arxiv.org/abs/2305.19872">
    <img src="https://img.shields.io/badge/arxiv-2305.19872-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/ivam-he/PSHGCN">
    <img src="https://img.shields.io/badge/ivam--he%2FPSHGCN-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/ivam-he/PSHGCN/stargazers">
    <img src="https://img.shields.io/github/stars/ivam-he/PSHGCN" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=He_2024]* %}

#### Citation

```bibtex
@inproceedings{DBLP:conf/www/HeWFHLSY24,
  author       = {Mingguo He and
                  Zhewei Wei and
                  Shikun Feng and
                  Zhengjie Huang and
                  Weibin Li and
                  Yu Sun and
                  Dianhai Yu},
  editor       = {Tat{-}Seng Chua and
                  Chong{-}Wah Ngo and
                  Ravi Kumar and
                  Hady W. Lauw and
                  Roy Ka{-}Wei Lee},
  title        = {Spectral Heterogeneous Graph Convolutions via Positive Noncommutative
                  Polynomials},
  booktitle    = {Proceedings of the {ACM} on Web Conference 2024, {WWW} 2024, Singapore,
                  May 13-17, 2024},
  pages        = {685--696},
  publisher    = {{ACM}},
  year         = {2024},
  url          = {https://doi.org/10.1145/3589334.3645515},
  doi          = {10.1145/3589334.3645515},
}
```

{% endtab %}
{% tab spectralgnn FarOptBasis %}

### Graph Neural Networks with Learnable and Optimal Polynomial Bases {% cite guo2023graph %} [[ICML 2023](https://icml.cc/Conferences/2023)]

<!-- Badges -->
<p>
  <a href="https://arxiv.org/abs/2302.12432">
    <img src="https://img.shields.io/badge/arxiv-2302.12432-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/yuziGuo/FarOptBasis">
    <img src="https://img.shields.io/badge/yuziGuo%2FFarOptBasis-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/yuziGuo/FarOptBasis/stargazers">
    <img src="https://img.shields.io/github/stars/yuziGuo/FarOptBasis" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=guo2023graph]* %}

#### Citation

```bibtex
@inproceedings{DBLP:conf/icml/GuoW23,
  author       = {Yuhe Guo and
                  Zhewei Wei},
  editor       = {Andreas Krause and
                  Emma Brunskill and
                  Kyunghyun Cho and
                  Barbara Engelhardt and
                  Sivan Sabato and
                  Jonathan Scarlett},
  title        = {Graph Neural Networks with Learnable and Optimal Polynomial Bases},
  booktitle    = {International Conference on Machine Learning, {ICML} 2023, 23-29 July
                  2023, Honolulu, Hawaii, {USA}},
  series       = {Proceedings of Machine Learning Research},
  volume       = {202},
  pages        = {12077--12097},
  publisher    = {{PMLR}},
  year         = {2023},
  url          = {https://proceedings.mlr.press/v202/guo23i.html},
}
```

{% endtab %}
{% tab spectralgnn ClenshawGNN %}

### Clenshaw Graph Neural Networks {% cite Guo_2023 %} [[KDD 2023](https://kdd.org/kdd2023/index.html#)]

<!-- Badges -->
<p>
  <a href="https://arxiv.org/abs/2210.16508">
    <img src="https://img.shields.io/badge/arxiv-2210.16508-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/yuziGuo/ClenshawGNN">
    <img src="https://img.shields.io/badge/yuziGuo%2FClenshawGNN-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/yuziGuo/ClenshawGNN/stargazers">
    <img src="https://img.shields.io/github/stars/yuziGuo/ClenshawGNN" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=Guo_2023]* %}

#### Citation

```bibtex
@inproceedings{DBLP:conf/kdd/GuoW23,
  author       = {Yuhe Guo and
                  Zhewei Wei},
  editor       = {Ambuj K. Singh and
                  Yizhou Sun and
                  Leman Akoglu and
                  Dimitrios Gunopulos and
                  Xifeng Yan and
                  Ravi Kumar and
                  Fatma Ozcan and
                  Jieping Ye},
  title        = {Clenshaw Graph Neural Networks},
  booktitle    = {Proceedings of the 29th {ACM} {SIGKDD} Conference on Knowledge Discovery
                  and Data Mining, {KDD} 2023, Long Beach, CA, USA, August 6-10, 2023},
  pages        = {614--625},
  publisher    = {{ACM}},
  year         = {2023},
  url          = {https://doi.org/10.1145/3580305.3599275},
  doi          = {10.1145/3580305.3599275},
}
```

{% endtab %}
{% tab spectralgnn EvenNet %}

### EvenNet: Ignoring Odd-Hop Neighbors Improves Robustness of Graph Neural Networks {% cite lei2022evennet %} [[NeurIPS 2022](https://nips.cc/Conferences/2022)]

<!-- Badges -->
<p>
  <a href="https://arxiv.org/abs/2205.13892">
    <img src="https://img.shields.io/badge/arxiv-2205.13892-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/Leirunlin/EvenNet">
    <img src="https://img.shields.io/badge/Leirunlin%2FEvenNet-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/Leirunlin/EvenNet/stargazers">
    <img src="https://img.shields.io/github/stars/Leirunlin/EvenNet" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=lei2022evennet]* %}

#### Citation

```bibtex
@inproceedings{Lei2022evennet,
  title={EvenNet: Ignoring Odd-Hop Neighbors Improves Robustness of Graph Neural Networks},
  author={Lei, Runlin and Wang, Zhen and Li, Yaliang and Ding, Bolin and Wei, Zhewei},
  booktitle={NeurIPS},
  year={2022}
}
```

{% endtab %}
{% tab spectralgnn ChebNetII %}

### ChebNetII: Learning Arbitrary Graph Spectral Filters via Bernstein Approximation {% cite he2022convolutional %} [[NeurIPS 2022](https://nips.cc/Conferences/2022)]

<!-- Badges -->
<p>
  <a href="https://arxiv.org/abs/2202.03580">
    <img src="https://img.shields.io/badge/arxiv-2202.03580-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/ivam-he/ChebNetII">
    <img src="https://img.shields.io/badge/ivam--he%2FChebNetII-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/ivam-he/ChebNetII/stargazers">
    <img src="https://img.shields.io/github/stars/ivam-he/ChebNetII" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=he2022convolutional]* %}

#### Citation

```bibtex
@inproceedings{he2022chebnetii,
  title={Convolutional Neural Networks on Graphs with Chebyshev Approximation, Revisited},
  author={He, Mingguo and Wei, Zhewei and Wen, Ji-Rong},
  booktitle={NeurIPS},
  year={2022}
}
```

{% endtab %}
{% tab spectralgnn BernNet %}

### BernNet: Learning Arbitrary Graph Spectral Filters via Bernstein Approximation {% cite he2021bernnet %} [[NeurIPS 2021](https://nips.cc/Conferences/2021)]

<!-- Badges -->
<p>
  <a href="https://arxiv.org/abs/2106.10994">
    <img src="https://img.shields.io/badge/arxiv-2106.10994-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/ivam-he/BernNet">
    <img src="https://img.shields.io/badge/ivam--he%2FBernNet-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/ivam-he/BernNet/stargazers">
    <img src="https://img.shields.io/github/stars/ivam-he/BernNet" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=he2021bernnet]* %}

#### Citation

```bibtex
@inproceedings{he2021bernnet,
  title={BernNet: Learning Arbitrary Graph Spectral Filters via Bernstein Approximation},
  author={He, Mingguo and Wei, Zhewei and Huang, Zengfeng and Xu, Hongteng},
  booktitle={NeurIPS},
  year={2021}
}
```

{% endtab %}
{% endtabs %}