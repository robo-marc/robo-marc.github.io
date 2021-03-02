---
layout: page
title: "newslist"
excerpt: "List of all news."
permalink: /newslist/
#image: news.png
# NOTE: don't set permalink, it breaks pagination
---

### NEDO News

<section>
  <ul>
 {% for post in site.posts %}
    <li><a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
</section>



