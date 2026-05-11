---
title: Publications
nav:
  order: 3
  tooltip: Published works
---

<!-- Stats bar -->
{% assign pub_orcids = "0000-0001-9232-4843,0000-0002-0086-8155,0009-0002-4648-9289" | split: "," %}
{% assign total_pubs = 0 %}
{% for citation in site.data.citations %}
  {% if pub_orcids contains citation.orcid %}
    {% assign total_pubs = total_pubs | plus: 1 %}
  {% endif %}
{% endfor %}
{% assign current_year = 'now' | date: "%Y" %}

<div class="pubs-stats-bar">
  <div class="pubs-stat">
    <span class="pubs-stat-num" id="pubs-showing-count">{{ total_pubs }}</span>
    <span class="pubs-stat-lbl">Publications</span>
  </div>
  <div class="pubs-stat-sep"></div>
  <div class="pubs-stat">
    <span class="pubs-stat-num">2009–{{ current_year }}</span>
    <span class="pubs-stat-lbl">Year Range</span>
  </div>
  <div class="pubs-stat-sep"></div>
  <div class="pubs-stat">
    <span class="pubs-stat-num" id="pubs-filter-label">All Topics</span>
    <span class="pubs-stat-lbl">Active Filter</span>
  </div>
</div>

<!-- Filter bar + controls -->
<div class="pubs-header-bar">
  <div class="pubs-filter-btns" role="group" aria-label="Filter publications by topic">
    <button class="pubs-filter-btn active" data-filter="all">All <span class="pubs-filter-count" id="count-all"></span></button>
    <button class="pubs-filter-btn" data-filter="security">Security &amp; Adversarial ML <span class="pubs-filter-count" id="count-security"></span></button>
    <button class="pubs-filter-btn" data-filter="biomedical">Biomedical AI <span class="pubs-filter-count" id="count-biomedical"></span></button>
    <button class="pubs-filter-btn" data-filter="explainable">Explainable AI <span class="pubs-filter-count" id="count-explainable"></span></button>
    <button class="pubs-filter-btn pubs-filter-btn--type" data-filter="journal"><i class="fa-regular fa-newspaper"></i> Journals <span class="pubs-filter-count" id="count-journal"></span></button>
    <button class="pubs-filter-btn pubs-filter-btn--type" data-filter="conference"><i class="fa-solid fa-person-chalkboard"></i> Conferences <span class="pubs-filter-count" id="count-conference"></span></button>
  </div>
  <div class="pubs-controls">
    <select class="pubs-sort-select" id="pubs-sort" aria-label="Sort publications">
      <option value="newest">Newest First</option>
      <option value="oldest">Oldest First</option>
    </select>
    <div class="pubs-view-toggle" role="group" aria-label="View mode">
      <button class="pubs-view-btn" data-view="rich" title="Rich view">
        <i class="fa-solid fa-grip"></i>
      </button>
      <button class="pubs-view-btn active" data-view="compact" title="Compact view">
        <i class="fa-solid fa-list"></i>
      </button>
    </div>
    {%
      include button.html
      icon="fa-solid fa-calendar-alt"
      text="Upcoming Venues"
      link="pubs/upcoming"
      style="bare"
    %}
  </div>
</div>

# {% include icon.html icon="fa-regular fa-newspaper" %} Featured Publications

{% include search-box.html %}

{% include search-info.html %}

<div id="pubs-list-wrapper">
{% include list.html data="citations" component="citation" style="rich" filters="orcid: 0000-0001-9232-4843|0000-0002-0086-8155|0009-0002-4648-9289"%}
</div>
