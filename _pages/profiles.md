---
layout: page
permalink: /people/
title: People
description: 
nav: false
nav_order: 9
logo: true
display_categories: ["Current PhD Students", "Postdoctoral Researcher", "Current master students", "Graduated PhD students", "Graduated master students"]
images:
  slider: true
students:
  # if you want to include more than one profile, just replicate the following block
  # and create one content file for each profile inside _pages/
  - name: Hanzhi Wang
    image: hanzhi.jpg
    link: https://wanghzccls.github.io/
    more_info: 2024
    category: Graduated PhD students
  - name: Mingguo He
    image: mingguo.jpg
    link: https://ivam-he.github.io/
    more_info: Graph Learning<br>Graph Neural Networks
    category: Current PhD Students
  - name: Yanping Zheng
    image: yanping.jpg
    link: https://zheng-yp.github.io/
    more_info: Graph Neural Networks<br>Dynamic Graph Representation Learning
    category: Postdoctoral Researcher
  - name: Jiajun Li
    image: jiajun.jpg
    link: https://llijiajun.github.io/github-io/
    more_info: 
    category: Current PhD Students
  - name: Yang Zhang
    image: default.svg
    link: https://fengyuewuya.github.io/
    more_info: 
    category: Current PhD Students
  - name: Yuhe Guo
    image: yuhe.jpg
    link: https://yuziguo.github.io/
    more_info: 
    category: Current PhD Students
  - name: Jinjia Feng
    image: default.svg
    link: https://xkxxfyf.github.io/
    more_info: 
    category: Current PhD Students
  - name: Mingji Yang
    image: mingji.jpg
    link: https://kyleyoung-ymj.github.io/
    more_info: Theoretical Computer Science<br>Graph Algorithms<br>Sublinear Algorithms 
    category: Current PhD Students
  - name: Haipeng Ding
    image: haipeng.jpg
    link: 
    more_info: Large-scale Graph Learning<br>LLM4Graph
    category: Current PhD Students
  - name: Lu Yi
    image: lu_yi.jpg
    link: https://luyi256.github.io/
    more_info: Dynamic graph learning<br>Graph unlearning<br>Scalable algorithms
    category: Current PhD Students
  - name: Dongxie Wen
    image: dongxie.jpg
    link: 
    more_info: Sketch4ML<br>Steaming Algorithms<br>Online Learning
    category: Current PhD Students
  - name: Jie Peng
    image: jie_peng.jpg
    link: https://lucas-pj.github.io/
    more_info: Graph Machine Learning<br>Dynamic Graph Learning
    category: Current PhD Students
  - name: Runlin Lei
    image: runlin.jpg
    link: https://leirunlin.github.io/
    more_info: Machine learning on graphs<br>Graph adversarial attack & defense<br>LLM4Graph
    category: Current PhD Students
  - name: Gengmo Zhou
    image: gengmo.jpg
    link: https://zhougengmo.github.io/
    more_info: AI in pharmaceuticals<br>3D molecule modeling
    category: Current PhD Students
  - name: Yuwei Hu
    image: yuwei.jpg
    link: 
    more_info: LLM&Graph
    category: Current PhD Students
  - name:   Yuzhang Fei
    image: yuzhang.jpg
    link: 
    more_info: 
    category: Current PhD Students
  - name: Wenda Wang
    image: wenda.jpg
    link: 
    more_info: Deep learning for bioinformatics
    category: Current PhD Students

  - name: Ruoqi Zhang
    image: default.svg
    link: 
    more_info: 
    category: Current master students
  - name: Xu Liu
    image: default.svg
    link: 
    more_info: 
    category: Current master students
  - name: Guanyu Cui
    image: guanyu.jpg
    link: https://guanyucui.github.io/
    more_info: Graph neural networks<br>Graph algorithms<br>Graph algorithm alignment
    category: Current master students
  - name: Jingyu Chen
    image: default.svg
    link: 
    more_info: 
    category: Current master students
  - name: Jiahong Ma
    image: jiahong.jpg
    link: 
    more_info: Spectral GNN<br>Graph Transformer
    category: Current master students
  - name: Jiarui Ji
    image: jiarui.jpg
    link: 
    more_info: 
    category: Current master students
  - name: Hanyan Yin
    image: hanyan.jpg
    link: https://yinhanyan.github.io/
    more_info: Streaming Algorithms
    category: Current master students

  - name: Yu Liu
    image: yu_liu.jpg
    link: https://faculty.bjtu.edu.cn/9759/
    more_info: 2018, Lecturer of Beijing Jiaotong University (co-supervised with <a href="https://www.cs.helsinki.fi/u/jilu/">Jiaheng Lu</a>)
    category: Graduated PhD students

  - name: Suijun Tong
    image: default.svg
    link: 
    more_info: 2017, IBM
    category: Graduated master students
  - name: Xiaodong He
    image: default.svg
    link: 
    more_info: 2018, 4paradigm
    category: Graduated master students
  - name: Yuan Yin
    image: default.svg
    link: 
    more_info: 2020, ByteDance
    category: Graduated master students
  - name: Chenmiao Yu
    image: default.svg
    link: 
    more_info: 2020, Civil Servant
    category: Graduated master students
  - name: Ming Chen
    image: default.svg
    link: 
    more_info: 2021, Central Enterprise
    category: Graduated master students
  - name: Weirui Kuang
    image: default.svg
    link: https://www.weiruikuang.com/
    more_info: 2021, Alibaba DAMO Academy
    category: Graduated master students
  - name: Tianjing Zeng
    image: default.svg
    link: 
    more_info: 2023, Alibaba DAMO Academy
    category: Graduated master students
  - name: Fangrui Lyu
    image: default.svg
    link: 
    more_info: 2023, China Development Bank
    category: Graduated master students
---

<swiper-container keyboard="true" navigation="true" pagination="true" pagination-clickable="true" pagination-dynamic-bullets="true" rewind="true" autoplay-delay="3000" autoplay-disable-on-interaction="false">
  <swiper-slide>{% include figure.liquid loading="eager" path="assets/img/albums/1.jpg" class="img-fluid rounded z-depth-1" caption="2024.07.01 get together" %}</swiper-slide>
  <swiper-slide>{% include figure.liquid loading="eager" path="assets/img/albums/2.jpg" class="img-fluid rounded z-depth-1" caption="2023.09.21 get together" %}</swiper-slide>
</swiper-container>

{% for category in page.display_categories %}
  {% if category == "Current PhD Students" or category == "Current master students" or catogory == "Postdoctoral Researcher" %}
  <h2 class="category mt-3">{{ category }}</h2>
  {% assign categorized_projects = page.students | where: "category", category %}
  <div class="row row-cols-2 row-cols-md-4">
  {% for project in categorized_projects %}
    {% assign profile_image_path = project.image | prepend: 'assets/img/students/' %}
    {% assign profile_image_class = 'img-fluid z-depth-1 rounded' %}
    <div class="col my-1 px-1">
      <div class="card hoverable h-100">
        <div class="col">
          <a href="{{ project.link }}" class="no-decoration">
            <img
              src="{{ profile_image_path | prepend: site.baseurl }}"
              class="img-fluid rounded-start"
              loading="lazy"
            />
          </a>
        </div>
        <div class="col">
          <div class="card-body p-3">
              <h4 class="card-title text-center"><a href="{{ project.link }}">{{ project.name }}</a></h4>
              <div class="card-text text-center">{{ project.more_info }}</div>
          </div>
        </div>
      </div>
    </div>
  {% endfor %}
  </div>
  {% endif %}
{% endfor %}

{% for category in page.display_categories %}
  {% if category ==  "Graduated PhD students" or category == "Graduated master students"%}
  <h2 class="category mt-3">{{ category }}</h2>
  {% assign categorized_projects = page.students | where: "category", category %}
  <ul>
  {% for project in categorized_projects %}
      <li><a href="{{ project.link }}">{{ project.name }}</a>, {{ project.more_info }}. </li>
  {% endfor %}
  </ul>
  {% endif %}
{% endfor %}