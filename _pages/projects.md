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
