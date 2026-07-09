---
title: Blog
nav:
  order: 6
  tooltip: News, insights, and research updates from InfoLab
---

{% assign all_posts    = site.posts %}
{% assign post_dates   = all_posts | map: "date" | sort %}
{% assign oldest_yr    = post_dates | first | date: "%Y" %}
{% assign newest_yr    = post_dates | last  | date: "%Y" %}
{% assign latest_post  = all_posts | first %}

<!-- HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">InfoLab</div>
    <h1 class="team-hero-title">Blog</h1>
    <p class="team-hero-sub">Research updates, lab news, and insights from the InfoLab team at SKKU.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">{{ all_posts.size }}</span>
        <span class="team-hstat-lbl">Posts</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ oldest_yr }}&ndash;{{ newest_yr }}</span>
        <span class="team-hstat-lbl">Years</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ latest_post.date | date: "%b %Y" }}</span>
        <span class="team-hstat-lbl">Latest</span>
      </div>
    </div>
  </div>
</div>

{% include section.html %}

{% include search-box.html %}

{%- comment -%}
  Build a list of "padded-count|tagname" strings so a lexical descending sort
  surfaces the most-used tags first. Take the top 10, strip the count prefix,
  pass the resulting tag list to tags.html.
{%- endcomment -%}
{%- capture tagEntries -%}
  {%- for tag_pair in site.tags -%}
    {%- assign tagCount = tag_pair[1].size -%}
    {%- if tagCount < 10 -%}00{{ tagCount }}
    {%- elsif tagCount < 100 -%}0{{ tagCount }}
    {%- else -%}{{ tagCount }}
    {%- endif -%}|{{ tag_pair[0] }},
  {%- endfor -%}
{%- endcapture -%}
{%- assign sortedTags = tagEntries | split: "," | array_filter | sort | reverse -%}
{%- assign topTags    = sortedTags | slice: 0, 10 -%}
{%- assign blogTags   = ""         | split: "," -%}
{%- for tagEntry in topTags -%}
  {%- assign tagName = tagEntry | split: "|" | last -%}
  {%- assign blogTags = blogTags | push: tagName -%}
{%- endfor -%}
{%- assign blogTags = blogTags | sort -%}
{% include tags.html tags=blogTags %}

{% include search-info.html %}

<!-- Featured (latest) post -->
{% assign featured_post = site.posts | first %}
{% if featured_post %}
<div class="blog-featured">
  <div class="blog-featured-badge">
    {% include icon.html icon="fa-solid fa-star" %}
    Latest Post
  </div>
  {% include post-excerpt.html post=featured_post %}
</div>
{% endif %}

<!-- All posts, grouped by year -->
{% assign post_years = site.posts | group_by_exp: "p", "p.date | date: '%Y'" | sort: "name" | reverse %}
{% for year in post_years %}
  {% assign year_posts = year.items | sort: "date" | reverse %}
  {% comment %} skip a year whose only post is the featured one {% endcomment %}
  {% if year_posts.size == 1 and year_posts.first.url == featured_post.url %}
    {% continue %}
  {% endif %}
  <h3 class="blog-year" id="{{ year.name }}">{{ year.name }}</h3>
  <div class="blog-grid">
    {% for post in year_posts %}
      {% if post.url == featured_post.url %}{% continue %}{% endif %}
      {% include post-excerpt.html post=post %}
    {% endfor %}
  </div>
{% endfor %}
