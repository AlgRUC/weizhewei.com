---
layout: page
title: Projects
permalink: /projects/
description: The collections of projects of our group.
nav: false
nav_order: 3
display_categories: [works]
horizontal: false
logo: true
---

<!-- pages/projects.md -->
<div class="projects pt-3">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <div class="social-header float-right">
    <div style="font-size: 0.8rem" align="center">Follow our works via:</div>
    <div class="contact-icons">{% include social.liquid %}</div>
  </div>
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category mt-3">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>

<br>

<small>Some cover picture(s) are created by Dunk from [flickr](https://www.flickr.com/photos/dullhunk/4520018121).  </small>

## Projects and Grants

*   2022.12 - 2025.11, "Rapid Streaming Computation under Restricted Resources", National Science and Technology Major Project (2022ZD0114802, 1,700,000 RMB), PI.
*   2023.01 - 2026.12, "Native Distributed Graph Storage and Computation for Graph Learning Tasks", NSFC Grant (No.U2241212, Major Program, 2,550,000 RMB), PI.
*   2022.01 - 2024.12, "Heterogeneous Graph Representation Learning For Modern Urban Transportation Networks", Beijing Natural Science Foundation (No.4222028, General Program, 200,000 RMB), PI.
*   2020.01 - 2024.12, "Big Graph Complexity and Efficient Computing", NSFC Grant (No.61932001, Major Program, 3,000,000 RMB), co-PI (3 co-PI's in total).
*   2020.01 - 2023.12, "Proximities on Large Graphs: Computation and Applications", NSFC Grant (No.61972401, General Program, 600,000 RMB), PI.
*   2019.01 - 2023.12, "Real-time Interactive Analysis on Cross-Modal Big Data", NSFC Grant (No.61832017, Major Program, 3,000,000 RMB), primary participant.
*   2016.01 - 2018.12, "Multi-Dimensional and Dynamic Indexing for Summary Queries", NSFC Grant (No.61502503, Youth Program, 240,000 RMB), PI.
*   2023.01 - 2023.12, "Implementations and Applications of Efficient Samplers in Database Systems", Alibaba DAMO Academy Air Project (500,000 RMB), PI.
*   2023.01 - 2023.12, "Computation and Applications of Large-Scale Heterogeneous Graphs", Huawei-Renmin University joint program on Information Retrieval (580,000 RMB), PI.
*   2022.01 - 2022.12, "Ten-Billion-Level Graph Machine Learning Model", Huawei-Renmin University joint program on Information Retrieval (300,000 RMB), PI.
*   2022.01 - 2022.12, "Optimize Data Storage Efficiency based on Machine Learning Algorithms", Alibaba air (500,000 RMB), PI.
*   2021.08 - 2022.08, "Scalable Graph Neural Networks", CCF-Baidu OPEN Fund (150,000 RMB), PI.
*   2021.01 - 2021.12, "Sampling Operator and AQP Algorithm Supporting Real-time Data Analysis", Alibaba air (500,000 RMB), PI.
*   2020.01 - 2021.12, "Efficient Sampling Operator and Application in Database", Alibaba air (500,000 RMB), PI.