---
layout: page
title: Streaming & Sketch4ML
nologo: true
description: Streaming Data Algorithms - Summary, Sketch, Synopsis - and applications in Machine Learning
importance: 3
category: Projects
related_publications: false
related_posts: false
tabs: true
pretty_table: true
mermaid:
  enabled: true
  zoomable: false
---

{% tabs group-name %}

{% tab group-name Background %}

> This project focuses on the <b style="color: blue">streaming data algorithms</b>, which maintain a small data structure in memory, and the applications of these algorithms in machine learning, which are called <b style="color: blue;">Sketch4ML</b>. The streaming algorithms can be used to optimize the machine learning algorithms, which are usually memory-intensive and time-consuming. 
{: .block-tip }

## Streaming algorithm

In computer science, **streaming algorithms** are algorithms for processing data streams in which the input is presented as a sequence of items and can be examined in only a few passes, typically just one. These algorithms are characterized by the following properties:

* Operate with limited computational/storage resources, generally logarithmic in the size of the stream and/or in the maximum value in the stream.
* Have limited processing time per item.
* To reduce computational/storage overhead, a certain error or/and fault probability can be tolerated.

As a result of these constraints, streaming algorithms often produce approximate answers based on a **sketch** of the data stream. 

### Books and Papers

<ul>
  <li>
    <dt><a href="https://www.dimacs.rutgers.edu/~graham/ssbd.html"><i>Small Summaries for Big Data</i></a>, Graham Cormode and Ke Yi, Cambridge University Press, 2020 </dt>
    <dd>This book provides a comprehensive introduction to many classic summary and sketch algorithms for a range of streaming data structures - sets, multisets, ordered data, vector, matrix, graph, and more. This book also offers detailed mathematical analysis of algorithm complexity, approximation error, and statistical properties.</dd>
  </li>
  <li>
    <dt><a href="https://dl.acm.org/doi/10.1561/0400000060"><i>Sketching as a Tool for Numerical Linear Algebra</i></a>, David P. Woodruff, 2014</dt>
    <dd>This survey highlights matrix sketching algorithm for a lot of problems of numerical linear algebra - least squares as well as robust regression problems, low rank approximation, and graph sparsification. </dd>
  </li>
  <li>
    <dt><a href="https://dl.acm.org/doi/10.1145/2487575.2487623"><i>Frequent Directions : Simple and Deterministic Matrix Sketching</i></a>, Edo Liberty, 2013</dt>
    <dd>This paper introduces the Frequent Directions algorithm, which is a simple and deterministic matrix sketching algorithm that can be used to approximate the covariance matrix of a data stream. </dd>
  </li>
</ul>

### Our Work

{% bibliography --query @*[field=Streaming Algorithms]* %}

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

{% endtab %}

{% tab group-name our work:<br>optimal matrix sketch<br>over sliding windows %}

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
  <a href="https://github.com/yinhanyan/DS-FD">
    <img src="https://img.shields.io/badge/yinhanyan%2FDS--FD-white?logo=github&labelColor=black" alt="stars" />
  </a>
  <a href="https://github.com/yinhanyan/DS-FD/stargazers">
    <img src="https://img.shields.io/github/stars/yinhanyan/DS-FD" alt="stars" />
  </a>
</p>

In this work, we proposes the optimal matrix sketch algorithm DS-FD on sliding windows, which achives the lower bound of space complexity for solving the matrix sketching problem over sliding windows. The paper addressed the open question of the lower bounds of space complexity for any deterministic algorithms solving the matrix sketching problem over sliding windows. The answer to this open problem confirms that our DS-FD algorithm is optimal in terms of space complexity.

The paper is accepted by VLDB 2024 and nominated for the Best Research Paper. If you are interested in the details, please refer to the [paper](https://doi.org/10.14778/3665844.3665847), [arxiv](https://arxiv.org/abs/2405.07792) or the [code](https://github.com/yinhanyan/DS-FD).

{% bibliography --query @*[key=yin2024optimal]* %}

### Problem Definition

(**Optimal Matrix Sketching over Sliding Windows**) Suppose we have a data stream where each item is in the set $$\mathbb{R}^{d}$$. Given the error parameter $$\varepsilon$$ and window size $$N$$, the goal is to maintain a matrix sketch $$\kappa$$ such that, at the current time $$T$$, $$\kappa$$ can return an approximation $$\boldsymbol{B}_W$$ for the matrix $$\boldsymbol{A}_W=\boldsymbol{A}_{T-N,T} \in \mathbb{R}^{N\times d}$$, stacked by the recent $$N$$ items. The approximation quality is measured by the *covariance error*, such that:

 $$ 
    \mathbf{cova-error}(\boldsymbol{A}_W, \boldsymbol{B}_W) = \lVert \boldsymbol{A}^\top_W\boldsymbol{A}_W - \boldsymbol{B}^\top_W\boldsymbol{B}_W\rVert_2 \le \varepsilon \lVert\boldsymbol{A}_W\rVert_F^2,
  $$

where $$N$$ bounds the maximum size of window $$W$$.

### Method

We propose the DS-FD algorithm, which is optimal in terms of space complexity for solving the matrix sketching problem over sliding windows. 

#### DS-FD Algorithm for *Normalized Sequence-based* Sliding Windows

First, we take a step back and consider a simplified scenario where the norm of each row is constantly 1, and each update occupies one timestamp. The window length is set to $$N$$. We refer to this as the *sequence-based* and *normalized* sliding window model. To handle this model, we maintain a sketch matrix $$\boldsymbol{C}$$ and a queue $$\mathcal{S}$$. When a row vector $$\boldsymbol{a}$$ arrives, we 

Step 1: First remove any outdated elements from the queue $$\mathcal{S}$$. Next, we concatenate the matrix $$\boldsymbol{C}$$ with the new vector $$\boldsymbol{a}$$.

<div class="w-75 mx-auto">
  {% include video.liquid path="assets/video/swfd-1.mp4" class="img-fluid rounded z-depth-1" controls=true %}
</div>

Step 2: If the rank of $$\boldsymbol{C}$$ is more than $$\ell$$, we perform Singular Value Decomposition (SVD) on the concatenated matrix $$\boldsymbol{C}$$ and get $$\mathtt{svd}(\boldsymbol{C})=(\boldsymbol{U},\boldsymbol{\Sigma},\boldsymbol{V}^\top)$$.

If the top singular value $$\sigma_1^2>\varepsilon N$$, we drop the top singular value $$\sigma_1$$ from $$\boldsymbol{\Sigma}$$ and the corresponding right singular vector $$\boldsymbol{v}_1$$ ffrom $$\boldsymbol{V}$$, and save the $$\sigma_1 \cdot \boldsymbol{v}_1^\top$$ with the current timestamp $$t$$ to the queue $$\mathcal{S}$$. (The saved timestamp is used to delete outdated elements in step 1 later.) We refer to this as **dump operation**. The new sketch matrix $$\boldsymbol{C}=\boldsymbol{\Sigma}[2:,\:]\boldsymbol{V}[2:,\:]^\top$$. 

<div class="w-75 mx-auto">
  {% include video.liquid path="assets/video/swfd-2.mp4" class="img-fluid rounded z-depth-1" controls=true %}
</div>

Otherwise ($$\sigma_1^2\le\varepsilon N$$), we update the sketch matrix $$\boldsymbol{C}$$ using the **FD reduce operation** as in [[1]](#ref1). That is, $$\boldsymbol{C}=\sqrt{\boldsymbol{\Sigma}^2-\sigma^2_{\ell+1}\boldsymbol{I}_{\ell+1}}\boldsymbol{V}^\top$$.

<div class="w-75 mx-auto">
  {% include video.liquid path="assets/video/swfd-3.mp4" class="img-fluid rounded z-depth-1" controls=true %}
</div>

#### Generalization to *Unnormalized* and *Time-based* Sliding Windows

We then extend DS-FD to handle more general scenarios when the rows are *unnormalized*, where the norm of each row vector lies within the range of $$1$$ to $$R$$ ($$\lVert \boldsymbol{a}_i\rVert \in [1,R]$$), or in a *time-based* window model, where each timestamp may contain zero updates ($$\lVert \boldsymbol{a}_i\rVert \in {0} \cup [1,R]$$). In these scenarios, we can first normalize the vectors and treat the update as $$\lVert \boldsymbol{a}_i\rVert$$ time updates of the normalized vector $$\boldsymbol{a}_i$$ ($$\lVert \boldsymbol{a}_i\rVert \times \frac{\boldsymbol{a}_i}{\lVert \boldsymbol{a}_i\rVert}$$). This converts the problem into the *normalized sequence-based* model, but with a *variable window length*. The minimum window length is $$N$$, and the maximum is $$NR$$.

To manage this, we initialize $$\log ⁡R$$ parallel DS-FD data structures, each with an exponentially increasing threshold to trigger the **dump operation**. The queue at each level stores no more than $${1\over\varepsilon}$$ snapshots. As a result, there will always be one DS-FD level that returns a qualified sketch at any time, and the space complexity naturally increases by a logarithm factor.

<div class="w-75 mx-auto">
  {% include figure.liquid loading="eager" path="assets/img/publication_preview/seq-dsfd.svg" title="example image" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
  DS-FD algorithm for *unnormalized* and *time-based* sliding windows model
</div>

### Results

#### Optimal Space Complexity

Furthermore, we were surprised to discover that the space lower bound for the matrix sketching problem in the sliding window model is of the same order as the space complexity of DS-FD. This indicates that our DS-FD algorithm is optimal in terms of space overhead for solving the problem.

| sketch $$\kappa$$ | Sequence-based<br>(normalized) | Sequence-based<br>(unnormalized) | Time-based<br>(normalized) | Time-based<br>(unnormalized) |
|-----------------|----------------------------|-------------------------------|-------------------------|----------------------------|
| Sampling | $$O\left(\frac{d}{\varepsilon^2} \log N\right)$$ * | $$O\left(\frac{d}{\varepsilon^2} \log NR\right)$$ * | $$O\left(\frac{d}{\varepsilon^2} \log N\right)$$ * | $$O\left(\frac{d}{\varepsilon^2} \log NR\right)$$ * |
| LM-FD[[2]](#ref2) | $$O\left(\frac{d}{\varepsilon^2}\right)$$ | $$O\left(\frac{d}{\varepsilon^2} \log R\right)$$ | $$O\left(\frac{d}{\varepsilon^2} \log \varepsilon N\right)$$ | $$O\left(\frac{d}{\varepsilon^2} \log \varepsilon NR\right)$$ |
| DI-FD[[2]](#ref2) | $$O\left(\frac{d}{\varepsilon} \log \frac{1}{\varepsilon}\right)$$ | $$O\left(\frac{Rd}{\varepsilon} \log \frac{R}{\varepsilon}\right)$$ | - | - |
| **DS-FD<br>(This work)** | $$O\left(\frac{d}{\varepsilon}\right)$$ | $$O\left(\frac{d}{\varepsilon} \log R\right)$$ | $$O\left(\frac{d}{\varepsilon} \log \varepsilon N\right)$$ | $$O\left(\frac{d}{\varepsilon} \log \varepsilon NR\right)$$ |
| **Lower bound<br>(This work)** | $$\Omega\left(\frac{d}{\varepsilon}\right)$$ | $$\Omega\left(\frac{d}{\varepsilon} \log R\right)$$ | $$\Omega\left(\frac{d}{\varepsilon} \log \varepsilon N\right)$$ | $$\Omega\left(\frac{d}{\varepsilon} \log \varepsilon NR\right)$$ |

<div class="caption">
  Given the dimension d of each row vector, the upper bound of relative covariance error 𝜀, and the size of the sliding window N, this table presents an overview of space complexities for algorithms addressing matrix sketching over sliding windows. An asterisk (*) indicates that the space complexity is the expected value when it is a random variable. 
</div>

In our proof of the lower bound, we carefully constructed challenging adversarial inputs against the algorithms. Our approach incorporates techniques used in the proof of the lower bound in the streaming model, as outlined in the paper on Frequent Directions[[1]](#ref1).

#### Experiments

We implemented all the algorithms across various data streams, both synthetic and real-world. We recorded the maximum error, average error, and the corresponding maximum space cost under different parameter settings. Our observations show that DS-FD achieves the best trade-off between error and space cost, as well as between update time and query time. These results confirm the theoretical analysis and the efficiency of our algorithm.

<div class="w-75 mx-auto">
  {% include figure.liquid loading="eager" path="assets/img/publication_preview/swfd-experiments.png" title="example image" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
  Maximum error and maximum space cost of different algorithms under different data streams.
</div>

#### References

<ol>
<li><a name="ref1"></a>Edo Liberty. 2013. <a href="https://dl.acm.org/doi/10.1145/2487575.2487623">Simple and deterministic matrix sketching</a>. In <cite>Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining (KDD '13)</cite>. Association for Computing Machinery, New York, NY, USA, 581–588. https://doi.org/10.1145/2487575.2487623</li>
<li><a name="ref2"></a>Zhewei Wei, Xuancheng Liu, Feifei Li, Shuo Shang, Xiaoyong Du, and Ji-Rong Wen. 2016. <a href="https://dl.acm.org/doi/10.1145/2882903.2915228">Matrix Sketching Over Sliding Windows</a>. In <cite>Proceedings of the 2016 International Conference on Management of Data (SIGMOD '16)</cite>. Association for Computing Machinery, New York, NY, USA, 1465–1480. https://doi.org/10.1145/2882903.2915228</li>
</ol>

{% endtab %}

{% tab group-name our work:<br>Dyadic Sketched Bandit %}

TBD

{% endtab %}

{% endtabs %}