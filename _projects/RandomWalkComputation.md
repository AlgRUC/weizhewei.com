---
layout: page
title: Random-Walk Computation
nologo: true
description: Theory and Applications of Computing Random-Walk-Based Quantities such as SimRank, PageRank, Personalized PageRank (PPR), and Effective Resistance (ER)
importance: 5
category: Projects
related_publications: false
related_posts: false
tabs: true
pretty_table: true
mermaid:
  enabled: true
  zoomable: false
---

{% tabs random-walk %}

{% tab random-walk Overview %}

> <b style="color: blue">Random-walk probabilities</b> on graphs serve as a cornerstone in **network analysis**, **graph data mining**, and **graph machine learning**. Their further applications span diverse domains, including information retrieval, recommendation systems, chemistry, biology, and neuroscience.
> 
> 
> This project focuses on **efficient computation and approximation** of random-walk probabilities, a subject of both theoretical and practical significance. We mainly concentrate on optimizing algorithms to compute widely-used random-walk-based metrics, such as <b style="color: blue">SimRank</b>, <b style="color: blue">PageRank</b>, <b style="color: blue">Personalized PageRank (PPR)</b>, and <b style="color: blue">Effective Resistance (ER)</b>.
> 
> 
> Our work improves the computational complexity of computing these quantities, and we also conduct empirical evaluations to demonstrate the efficiency and effectiveness of our approaches in real-world applications, including **local graph clustering** and **graph neural networks**.
{: .block-tip }

```mermaid
graph TD
    
    classDef main fill:#FFEBCC,stroke:#FF9900,stroke-width:2px,color:#333,rx:5px,ry:5px;
    classDef secondary fill:#C6F6C6,stroke:#009900,stroke-width:2px,color:#333,rx:5px,ry:5px;
    classDef work fill:#C6E5FF,stroke:#007ACC,stroke-width:2px,color:#333,rx:5px,ry:5px;
    classDef link fill:#FDE2E2,stroke:#E63946,stroke-width:2px,color:#007bFF,font-weight:bold,rx:15px,ry:15px,stroke-dasharray:4,4,text-decoration:underline,font-style:italic;

    A[Our Work on Random-Walk Computation]:::main --> B[for SimRank]:::secondary
    A --> C[for PageRank and PPR]:::secondary
    A --> D[for General Proximity]:::secondary
    A --> E[for ER]:::secondary

    B --> B1[ProbeSim]:::work
    B1 --> B2[PRSim]:::work
    B2 --> B3[ExactSim]:::work
    B --> B4[SimTab]:::work

    C --> C1[...... see below]:::link
    click C1 href "#PPR"

    D --> D1[AGP]:::work

    E --> E1[Single-Pair ER]:::secondary
    E1 --> E2[BiSPER]:::work
```

<a name="PPR" style="position: relative;top: -80px;"></a>

```mermaid
graph TD

    classDef secondary fill:#C6F6C6,stroke:#009900,stroke-width:2px,color:#333,rx:5px,ry:5px;
    classDef work fill:#C6E5FF,stroke:#007ACC,stroke-width:2px,color:#333,rx:5px,ry:5px;
    classDef highlight fill:#66B3FF,stroke:#007ACC,stroke-width:2px,color:#333,rx:5px,ry:5px;
    classDef link fill:#FDE2E2,stroke:#E63946,stroke-width:2px,color:#9B2226,font-weight:bold,rx:5px,ry:5px;

    A[Our Work on PageRank and PPR Computation]:::link

    A --> A1[PPR Survey]:::highlight

    A --> A2[Single-Source PPR]:::secondary
    A2 --> A21[FORA]:::work
    A21 --> A211[SpeedPPR]:::work
    A2 --> A22[EdgePush]:::work
    A2 --> A23["[WWY24]"]:::work

    A --> A3[Single-Target PPR]:::secondary
    A3 --> A31[RBS]:::work
    A3 --> A32["[WWWY24]"]:::work

    A --> A4[Single-Node PageRank]:::secondary
    A4 --> A41[SetPush]:::work
    A4 --> A42["[WWWY24]"]:::work

    A --> A5[TopPPR]:::work
```

{% endtab %}

{% tab random-walk SimRank Computation %}

### ProbeSim: Scalable Single-Source and Top-$$k$$ SimRank Computations on Dynamic Graphs [[VLDB 2017](https://dl.acm.org/doi/10.14778/3151113.3151115)]

<p>
  <a href="https://doi.org/10.14778/3151113.3151115">
    <img src="https://img.shields.io/badge/doi-10.14778/3151113.3151115-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="http://arxiv.org/abs/1709.06955">
    <img src="https://img.shields.io/badge/arxiv-1709.06955-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/dokirabbithole/ProbeSim_vldb_pub">
    <img src="https://img.shields.io/badge/dokirabbithole/ProbeSim__vldb__pub-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/dokirabbithole/ProbeSim_vldb_pub/stargazers">
    <img src="https://img.shields.io/github/stars/dokirabbithole/ProbeSim_vldb_pub" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=liu2017probesim]* %}

#### Citation

```bibtex
@article{liu2017probesim,
  author       = {Yu Liu and
                  Bolong Zheng and
                  Xiaodong He and
                  Zhewei Wei and
                  Xiaokui Xiao and
                  Kai Zheng and
                  Jiaheng Lu},
  title        = {ProbeSim: Scalable Single-Source and Top-k SimRank Computations on Dynamic Graphs},
  journal      = {Proceedings of the VLDB Endowment},
  volume       = {11},
  number       = {1},
  pages        = {14--26},
  year         = {2017},
  url          = {http://www.vldb.org/pvldb/vol11/p14-liu.pdf},
  doi          = {10.14778/3151113.3151115}
}
```

---

### PRSim: Sublinear Time SimRank Computation on Large Power-Law Graphs [[SIGMOD 2019](https://dl.acm.org/doi/10.1145/3299869.3319873)]

<p>
  <a href="https://doi.org/10.1145/3299869.3319873">
    <img src="https://img.shields.io/badge/doi-10.1145/3299869.3319873-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="http://arxiv.org/abs/1905.02354">
    <img src="https://img.shields.io/badge/arxiv-1905.02354-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/wzskytop/PRSim-Code">
    <img src="https://img.shields.io/badge/wzskytop/PRSim--Code-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wzskytop/PRSim-Code/stargazers">
    <img src="https://img.shields.io/github/stars/wzskytop/PRSim-Code" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=wei2019prsim]* %}

#### Citation

```bibtex
@inproceedings{wei2019prsim,
  author       = {Zhewei Wei and
                  Xiaodong He and
                  Xiaokui Xiao and
                  Sibo Wang and
                  Yu Liu and
                  Xiaoyong Du and
                  Ji-Rong Wen},
  title        = {PRSim: Sublinear Time SimRank Computation on Large Power-Law Graphs},
  booktitle    = {Proceedings of the 2019 International Conference on Management of
                  Data},
  pages        = {1042--1059},
  year         = {2019},
  url          = {https://doi.org/10.1145/3299869.3319873},
  doi          = {10.1145/3299869.3319873}
}
```

---

### SimTab: Accuracy-Guaranteed SimRank Queries Through Tighter Confidence Bounds and Multi-Armed Bandits [[VLDB 2020](https://doi.org/10.14778/3407790.3407819)]

<p>
  <a href="https://doi.org/10.14778/3407790.3407819">
    <img src="https://img.shields.io/badge/doi-10.14778/3407790.3407819-blue?style=flat&logo=doi
" alt="doi" />
  </a>
</p>

{% bibliography --query @*[key=liu2020simtab]* %}

#### Citation

```bibtex
@article{liu2020simtab,
  author       = {Yu Liu and
                  Lei Zou and
                  Qian Ge and
                  Zhewei Wei},
  title        = {SimTab: Accuracy-Guaranteed SimRank Queries through Tighter Confidence
                  Bounds and Multi-Armed Bandits},
  journal      = {Proceedings of the VLDB Endowment},
  volume       = {13},
  number       = {11},
  pages        = {2202--2214},
  year         = {2020},
  url          = {http://www.vldb.org/pvldb/vol13/p2202-liu.pdf},
  doi          = {10.14778/3407790.3407819}
}
```

---

### Exact Single-Source SimRank Computation on Large Graphs [[SIGMOD 2020](https://dl.acm.org/doi/10.1145/3318464.3389781)], ExactSim: Benchmarking Single-Source SimRank Algorithms with High-Precision Ground Truths [[The VLDB Journal 2021](https://link.springer.com/article/10.1007/s00778-021-00672-7)]

<p>
  <a href="https://doi.org/10.1145/3318464.3389781">
    <img src="https://img.shields.io/badge/doi-10.1145/3318464.3389781-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="http://arxiv.org/abs/2004.03493">
    <img src="https://img.shields.io/badge/arxiv-2004.03493-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/wanghzccls/ExactSim">
    <img src="https://img.shields.io/badge/wanghzccls/ExactSim-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wanghzccls/ExactSim/stargazers">
    <img src="https://img.shields.io/github/stars/wanghzccls/ExactSim" alt="stars" />
  </a>
</p>

<p>
  <a href="https://link.springer.com/article/10.1007/s00778-021-00672-7">
    <img src="https://img.shields.io/badge/doi-10.1007/s00778--021--00672--7-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://github.com/wanghzccls/ExactSim">
    <img src="https://img.shields.io/badge/wanghzccls/ExactSim-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wanghzccls/ExactSim/stargazers">
    <img src="https://img.shields.io/github/stars/wanghzccls/ExactSim" alt="stars" />
  </a>
</p>

> We propose <b style="color: blue">ExactSim</b>, the first algorithm that enables <b style="color: blue">probabilistic exact single-source SimRank queries</b> on large graphs. ExactSim can provide the ground truth with a precision up to $$7$$ decimal places for single-source SimRank queries on large graphs within a reasonable query time. With the ground truths computed by ExactSim, we conduct the first experimental study of the accuracy/cost trade-offs of existing approximate SimRank algorithms on large graphs.
{: .block-tip }

{% bibliography --query @*[key=wang2020exact]* %}

{% bibliography --query @*[key=wang2021exactsim]* %}

#### Citations

```bibtex
@inproceedings{wang2020exact,
  author       = {Hanzhi Wang and
                  Zhewei Wei and
                  Ye Yuan and
                  Xiaoyong Du and
                  Ji-Rong Wen},
  title        = {Exact Single-Source SimRank Computation on Large Graphs},
  booktitle    = {Proceedings of the 2020 International Conference on Management of
                  Data},
  pages        = {653--663},
  year         = {2020},
  url          = {https://doi.org/10.1145/3318464.3389781},
  doi          = {10.1145/3318464.3389781}
}

@article{wang2021exactsim,
  author       = {Hanzhi Wang and
                  Zhewei Wei and
                  Yu Liu and
                  Ye Yuan and
                  Xiaoyong Du and
                  Ji-Rong Wen},
  title        = {ExactSim: benchmarking single-source SimRank algorithms with high-precision
                  ground truths},
  journal      = {The VLDB Journal},
  volume       = {30},
  number       = {6},
  pages        = {989--1015},
  year         = {2021},
  url          = {https://doi.org/10.1007/s00778-021-00672-7},
  doi          = {10.1007/S00778-021-00672-7}
}
```

{% endtab %}

{% tab random-walk PPR survey %}

### Efficient Algorithms for Personalized PageRank Computation: A Survey [[TKDE 2024](https://ieeexplore.ieee.org/document/10471277)]

<p>
  <a href="https://arxiv.org/abs/2403.05198">
    <img src="https://img.shields.io/badge/arxiv-2403.05198-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
</p>

> This <b style="color: blue">survey paper</b> provides a systematic and comprehensive review of several <b style="color: blue">basic techniques</b> and <b style="color: blue">recent algorithms</b> for PPR computation **from an algorithmic perspective**.
{: .block-tip }

{% bibliography --query @*[key=yang2024efficient]* %}

#### Citation

```bibtex
@article{yang2024efficient,
  author       = {Mingji Yang and
                  Hanzhi Wang and
                  Zhewei Wei and
                  Sibo Wang and
                  Ji-Rong Wen},
  title        = {Efficient Algorithms for Personalized PageRank Computation: A Survey},
  journal      = {IEEE Transactions on Knowledge and Data Engineering},
  volume       = {36},
  number       = {9},
  pages        = {4582--4602},
  year         = {2024},
  doi          = {10.1109/TKDE.2024.3376000}
}
```

{% endtab %}

{% tab random-walk FORA %}

### FORA: Simple and Effective Approximate Single-Source Personalized PageRank [[KDD 2017](https://dl.acm.org/doi/10.1145/3097983.3098072)], Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries [[TODS 2019](https://dl.acm.org/doi/10.1145/3360902)]

<p>
  <a href="https://doi.org/10.1145/3097983.3098072">
    <img src="https://img.shields.io/badge/doi-10.1145/3097983.3098072-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://github.com/wangsibovictor/fora">
    <img src="https://img.shields.io/badge/wangsibovictor/fora-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wangsibovictor/fora/stargazers">
    <img src="https://img.shields.io/github/stars/wangsibovictor/fora" alt="stars" />
  </a>
</p>


<p>
  <a href="https://doi.org/10.1145/3360902">
    <img src="https://img.shields.io/badge/doi-10.1145/3360902-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://arxiv.org/abs/1908.10583">
    <img src="https://img.shields.io/badge/arxiv-1908.10583-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/wangsibovictor/fora">
    <img src="https://img.shields.io/badge/wangsibovictor/fora-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wangsibovictor/fora/stargazers">
    <img src="https://img.shields.io/github/stars/wangsibovictor/fora" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=wang2017fora]* %}

{% bibliography --query @*[key=wang2019efficient]* %}

#### Citations

```bibtex
@inproceedings{wang2017fora,
  author       = {Sibo Wang and
                  Renchi Yang and
                  Xiaokui Xiao and
                  Zhewei Wei and
                  Yin Yang},
  title        = {FORA: Simple and Effective Approximate Single-Source Personalized PageRank},
  booktitle    = {Proceedings of the 23rd ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages        = {505--514},
  year         = {2017},
  url          = {https://doi.org/10.1145/3097983.3098072},
  doi          = {10.1145/3097983.3098072}
}

@article{wang2019efficient,
  author       = {Sibo Wang and
                  Renchi Yang and
                  Runhui Wang and
                  Xiaokui Xiao and
                  Zhewei Wei and
                  Wenqing Lin and
                  Yin Yang and
                  Nan Tang},
  title        = {Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries},
  journal      = {ACM Transactions on Database Systems},
  volume       = {44},
  number       = {4},
  pages        = {18:1--18:37},
  year         = {2019},
  url          = {https://doi.org/10.1145/3360902},
  doi          = {10.1145/3360902}
}
```

{% endtab %}

{% tab random-walk EdgePush %}

### Edge-based Local Push for Personalized PageRank [[VLDB 2022](https://dl.acm.org/doi/10.14778/3523210.3523216)]

<p>
  <a href="https://doi.org/10.14778/3523210.3523216">
    <img src="https://img.shields.io/badge/doi-10.14778/3523210.3523216-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://arxiv.org/abs/2203.07937">
    <img src="https://img.shields.io/badge/arxiv-2203.07937-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/wanghzccls/EdgePush">
    <img src="https://img.shields.io/badge/wanghzccls/EdgePush-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wanghzccls/EdgePush/stargazers">
    <img src="https://img.shields.io/github/stars/wanghzccls/EdgePush" alt="stars" />
  </a>
</p>

> The state-of-the-art algorithm, LocalPush, for Personalized PageRank computation can be rather inefficient on <b style="color: blue">weighted graphs</b>. In this paper, we propose an <b style="color: blue">Edge-based Push Method (EdgePush)</b>, which decomposes the push operation of LocalPush into separate edge-based push operations and achieves superior query efficiency over LocalPush on weighted graphs.
{: .block-tip }

{% bibliography --query @*[key=wang2022edgebased]* %}

#### Citation

```bibtex
@article{wang2022edgebased,
  author       = {Hanzhi Wang and
                  Zhewei Wei and
                  Junhao Gan and
                  Ye Yuan and
                  Xiaoyong Du and
                  Ji-Rong Wen},
  title        = {Edge-based Local Push for Personalized PageRank},
  journal      = {Proceedings of the VLDB Endowment},
  volume       = {15},
  number       = {7},
  pages        = {1376--1389},
  year         = {2022},
  url          = {https://www.vldb.org/pvldb/vol15/p1376-wang.pdf},
  doi          = {10.14778/3523210.3523216}
}
```

{% endtab %}

{% tab random-walk [WWY24] %}

### Approximating Single-Source Personalized PageRank with Absolute Error Guarantees [[ICDT 2024](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2024.9)]

<p>
  <a href="https://doi.org/10.4230/LIPIcs.ICDT.2024.9">
    <img src="https://img.shields.io/badge/doi-10.4230/LIPIcs.ICDT.2024.9-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://arxiv.org/abs/2401.01019">
    <img src="https://img.shields.io/badge/arxiv-2401.01019-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
</p>

> This paper proposes new algorithms to improve the upper bounds for <b style="color: blue">approximating Single-Source Personalized PageRank</b> with <b style="color: blue">(degree-normalized) absolute error guarantees</b> on various graphs.
{: .block-tip }

{% bibliography --query @*[key=wei2024approximating]* %}

#### Citation

```bibtex
@inproceedings{wei2024approximating,
  author       = {Zhewei Wei and
                  Ji-Rong Wen and
                  Mingji Yang},
  title        = {Approximating Single-Source Personalized PageRank with Absolute Error
                  Guarantees},
  booktitle    = {Proceedings of the 27th International Conference on Database Theory},
  volume       = {290},
  pages        = {9:1--9:19},
  year         = {2024},
  url          = {https://doi.org/10.4230/LIPIcs.ICDT.2024.9},
  doi          = {10.4230/LIPICS.ICDT.2024.9}
}
```

{% endtab %}

{% tab random-walk RBS %}

### Personalized PageRank to a Target Node, Revisited [[KDD 2020](https://dl.acm.org/doi/10.1145/3394486.3403108)]

<p>
  <a href="https://doi.org/10.1145/3394486.3403108">
    <img src="https://img.shields.io/badge/doi-10.1145/3394486.3403108-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://arxiv.org/abs/2006.11876">
    <img src="https://img.shields.io/badge/arxiv-2006.11876-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/wanghzccls/RBS">
    <img src="https://img.shields.io/badge/wanghzccls/RBS-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wanghzccls/RBS/stargazers">
    <img src="https://img.shields.io/github/stars/wanghzccls/RBS" alt="stars" />
  </a>
</p>

> We propose <b style="color: blue">Randomized Backward Search (RBS)</b>, a novel algorithm that answers <b style="color: blue">approximate single-target personalized PageRank queries</b> (a.k.a. PageRank contribution queries) with **nearly optimal time complexity**.
{: .block-tip }

{% bibliography --query @*[key=wang2020personalized]* %}

#### Citation

```bibtex
@inproceedings{wang2020personalized,
  author       = {Hanzhi Wang and
                  Zhewei Wei and
                  Junhao Gan and
                  Sibo Wang and
                  Zengfeng Huang},
  title        = {Personalized PageRank to a Target Node, Revisited},
  booktitle    = {Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages        = {657--667},
  year         = {2020},
  url          = {https://doi.org/10.1145/3394486.3403108},
  doi          = {10.1145/3394486.3403108}
}
```

{% endtab %}

{% tab random-walk [WWWY24] %}

### Revisiting Local Computation of PageRank: Simple and Optimal [[STOC 2024](https://dl.acm.org/doi/10.1145/3618260.3649661))]

<p>
  <a href="https://doi.org/10.1145/3618260.3649661">
    <img src="https://img.shields.io/badge/doi-10.1145/3618260.3649661-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://arxiv.org/abs/2403.12648">
    <img src="https://img.shields.io/badge/arxiv-2403.12648-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
</p>

> We use **simple techniques and analyses** to give <b style="color: blue">matching upper and lower bounds</b> for <b style="color: blue">estimating PageRank contributions and single-node PageRank</b>. Our results for the upper bounds are derived by revisiting the known algorithms of **ApproxContributions** (a.k.a. Backward Push) and **BiPPR**.
{: .block-tip }

{% bibliography --query @*[key=wang2024revisiting]* %}

#### Citation

```bibtex
@inproceedings{wang2024revisiting,
  author       = {Hanzhi Wang and
                  Zhewei Wei and
                  Ji-Rong Wen and
                  Mingji Yang},
  title        = {Revisiting Local Computation of PageRank: Simple and Optimal},
  booktitle    = {Proceedings of the 56th Annual ACM Symposium on Theory of Computing},
  pages        = {911--922},
  year         = {2024},
  url          = {https://doi.org/10.1145/3618260.3649661},
  doi          = {10.1145/3618260.3649661}
}
```

{% endtab %}

{% tab random-walk SetPush %}

### Estimating Single-Node PageRank in $$\tilde{O}\left(\min\big\{d_t,\sqrt{m}\big\}\right)$$ Time [[VLDB 2023](https://dl.acm.org/doi/10.14778/3611479.3611500)]

<p>
  <a href="https://doi.org/10.14778/3611479.3611500">
    <img src="https://img.shields.io/badge/doi-10.14778/3611479.3611500-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://arxiv.org/abs/2307.13162">
    <img src="https://img.shields.io/badge/arxiv-2307.13162-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/wanghzccls/SetPush-code">
    <img src="https://img.shields.io/badge/wanghzccls/SetPush--code-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wanghzccls/SetPush-code/stargazers">
    <img src="https://img.shields.io/github/stars/wanghzccls/SetPush-code" alt="stars" />
  </a>
</p>

> For the problem of estimating a <b style="color: blue">single node's PageRank</b> score in an <b style="color: blue">undirected graph</b>, we tighten the upper bound for query time complexity from $$O\left((nd_t)^{1/2}\right)$$ to $$\textcolor{blue}{O\left(\min\left(d_t, m^{1/2}\right)\right)}$$ (omitting logarithmic factors). Here $$n$$ and $$m$$ denote the number of nodes and edges in the given graph, respectively. $$d_t$$ denotes the degree of the given target node $$t$$.
{: .block-tip }

{% bibliography --query @*[key=wang2023estimating]* %}

#### Citation

```bibtex
@article{wang2023estimating,
  author       = {Hanzhi Wang and
                  Zhewei Wei},
  title        = {Estimating Single-Node PageRank in $\tilde{O}\left(\min\big\{d_t,\sqrt{m}\big\}\right)$ Time},
  journal      = {Proceedings of the VLDB Endowment},
  volume       = {16},
  number       = {11},
  pages        = {2949--2961},
  year         = {2023},
  url          = {https://dl.acm.org/doi/10.14778/3611479.3611500},
  doi          = {10.14778/3611479.3611500}
}
```

{% endtab %}

{% tab random-walk TopPPR %}

### TopPPR: Top-$$k$$ Personalized PageRank Queries with Precision Guarantees on Large Graphs [[SIGMOD 2018](https://doi.org/10.1145/3183713.3196920)]

<p>
  <a href="https://doi.org/10.1145/3183713.3196920">
    <img src="https://img.shields.io/badge/doi-10.1145/3183713.3196920-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://github.com/wzskytop/TopPPR">
    <img src="https://img.shields.io/badge/wzskytop/TopPPR-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wzskytop/TopPPR/stargazers">
    <img src="https://img.shields.io/github/stars/wzskytop/TopPPR" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=wei2018topppr]* %}

#### Citation

```bibtex
@inproceedings{wei2018topppr,
  author       = {Zhewei Wei and
                  Xiaodong He and
                  Xiaokui Xiao and
                  Sibo Wang and
                  Shuo Shang and
                  Ji-Rong Wen},
  title        = {TopPPR: Top-k Personalized PageRank Queries with Precision Guarantees on Large Graphs},
  booktitle    = {Proceedings of 2018 ACM Conference on Management of Data},
  pages        = {441--456},
  year         = {2018},
  url          = {https://doi.org/10.1145/3183713.3196920},
  doi          = {10.1145/3183713.3196920}
}
```

{% endtab %}

{% tab random-walk AGP %}

### Approximate Graph Propagation [[KDD 2021](https://dl.acm.org/doi/10.1145/3447548.3467243)]

<p>
  <a href="https://doi.org/10.1145/3447548.3467243">
    <img src="https://img.shields.io/badge/doi-10.1145/3447548.3467243-blue?style=flat&logo=doi
" alt="doi" />
  </a>
  <a href="https://arxiv.org/abs/2106.03058">
    <img src="https://img.shields.io/badge/arxiv-2106.03058-b31b1b?style=flat&logo=arxiv
" alt="arxiv" />
  </a>
  <a href="https://github.com/wanghzccls/AGP-Approximate_Graph_Propagation">
    <img src="https://img.shields.io/badge/wanghzccls/AGP--Approximate__Graph__Propagation-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/wanghzccls/AGP-Approximate_Graph_Propagation/stargazers">
    <img src="https://img.shields.io/github/stars/wanghzccls/AGP-Approximate_Graph_Propagation" alt="stars" />
  </a>
</p>

> We propose <b style="color: blue">Approximate Graph Propagation (AGP)</b>, a unified randomized algorithm that computes <b style="color: blue">various proximity queries</b> and <b style="color: blue">GNN feature propagation</b> with **almost optimal time complexity**.
{: .block-tip }

{% bibliography --query @*[key=wang2021approximate]* %}

#### Citation

```bibtex
@inproceedings{wang2021approximate,
  author       = {Hanzhi Wang and
                  Mingguo He and
                  Zhewei Wei and
                  Sibo Wang and
                  Ye Yuan and
                  Xiaoyong Du and
                  Ji-Rong Wen},
  title        = {Approximate Graph Propagation},
  booktitle    = {Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages        = {1686--1696},
  year         = {2021},
  url          = {https://doi.org/10.1145/3447548.3467243},
  doi          = {10.1145/3447548.3467243}
}
```

{% endtab %}

{% tab random-walk BiSPER %}

### Mixing Time Matters: Accelerating Effective Resistance Estimation via Bidirectional Method [KDD 2025]

<p>
  <a href="https://github.com/GuanyuCui/BiSPER">
    <img src="https://img.shields.io/badge/GuanyuCui/BiSPER-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/GuanyuCui/BiSPER/stargazers">
    <img src="https://img.shields.io/github/stars/GuanyuCui/BiSPER" alt="stars" />
  </a>
</p>

{% bibliography --query @*[key=cui2025mixing]* %}

{% endtab %}

{% endtabs %}
