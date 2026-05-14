---
title: Blog
nav:
  order: 7
  tooltip: News, insights, and research updates from InfoLab
---

# {% include icon.html icon="fa-solid fa-rss" %}Blog

Research updates, lab news, and insights from the InfoLab team at SKKU.

{% include section.html %}

{% include search-box.html %}

{% capture _tags_csv %}{% for tag_pair in site.tags %}{{ tag_pair[0] }},{% endfor %}{% endcapture %}
{% assign _blog_tags = _tags_csv | split: "," | uniq | sort %}
{% include tags.html tags=_blog_tags %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}