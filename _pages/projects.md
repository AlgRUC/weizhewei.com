---
layout: page
title: Projects
permalink: /projects/
description: The collections of projects of our group.
nav: false
nav_order: 3
display_categories: [works]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects pt-3">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}"> </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <ul>
  {% for project in sorted_projects %}
    {% include projects_horizontal.liquid %}
  {% endfor %}
  </ul>
  {% else %}
  <ul>
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </ul>
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