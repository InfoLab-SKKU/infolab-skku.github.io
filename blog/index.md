---
title: Blog
nav:
  order: 7
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

{% capture _tags_csv %}{% for tag_pair in site.tags %}{{ tag_pair[0] }},{% endfor %}{% endcapture %}
{% assign _blog_tags = _tags_csv | split: "," | uniq | sort %}
{% include tags.html tags=_blog_tags %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}
