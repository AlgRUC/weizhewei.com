---
layout: page
permalink: /people/
title: people
description: 
nav: true
nav_order: 9
display_categories: ["Current PhD Students", "Current master students", "Graduated PhD students", "Graduated master students"]
students:
  # if you want to include more than one profile, just replicate the following block
  # and create one content file for each profile inside _pages/
  - name: Hanzhi Wang
    image: whz.png
    link: https://wanghzccls.github.io/
    more_info: Baidu Scholarship, MSRA Fellowship, National Scholarship
    category: Current PhD Students
  - name: Mingguo He
    image: hmg.jpg
    link: https://ivam-he.github.io/
    more_info: 
    category: Current PhD Students
---

{% for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {% assign categorized_projects = page.students | where: "category", category %}
  <div class="row row-cols-1 row-cols-md-4">
  {% for project in categorized_projects %}
    {% assign profile_image_path = project.image | prepend: 'assets/img/students/' %}
    {% assign profile_image_class = 'img-fluid z-depth-1 rounded' %}
    <div class="col">
      <a href="{{ project.link }}" class="no-decoration">
          <div class="card hoverable h-100">
              {% include figure.liquid loading="eager" path=profile_image_path class=profile_image_class %}
              <div class="card-body">
                  <h3 class="card-title">{{ project.name }}</h3>
                  <div class="card-text">{{ project.more_info }}</div>
              </div>
          </div>
      </a>
    </div>
  {% endfor %}
  </div>
{% endfor %}