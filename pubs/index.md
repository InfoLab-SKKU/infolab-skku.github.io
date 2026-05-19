---
title: Publications
nav:
  order: 3
  tooltip: Published works
---

<!-- Stats bar -->
{% assign pub_orcids = "0000-0001-9232-4843,0000-0002-0086-8155,0009-0002-4648-9289" | split: "," %}
{% assign filtered_pubs = site.data.citations | where_exp: "c", "pub_orcids contains c.orcid" %}
{% assign total_pubs = filtered_pubs.size %}
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
    <button class="pubs-filter-btn active" data-filter="all" aria-pressed="true">All <span class="pubs-filter-count" id="count-all"></span></button>
    <button class="pubs-filter-btn" data-filter="security" aria-pressed="false">Security &amp; Adversarial ML <span class="pubs-filter-count" id="count-security"></span></button>
    <button class="pubs-filter-btn" data-filter="biomedical" aria-pressed="false">Biomedical AI <span class="pubs-filter-count" id="count-biomedical"></span></button>
    <button class="pubs-filter-btn" data-filter="explainable" aria-pressed="false">Explainable AI <span class="pubs-filter-count" id="count-explainable"></span></button>
    <button class="pubs-filter-btn pubs-filter-btn--type" data-filter="journal" aria-pressed="false"><i class="fa-regular fa-newspaper" aria-hidden="true"></i> Journals <span class="pubs-filter-count" id="count-journal"></span></button>
    <button class="pubs-filter-btn pubs-filter-btn--type" data-filter="conference" aria-pressed="false"><i class="fa-solid fa-person-chalkboard" aria-hidden="true"></i> Conferences <span class="pubs-filter-count" id="count-conference"></span></button>
  </div>
  <div class="pubs-controls">
    <select class="pubs-sort-select" id="pubs-sort" aria-label="Sort publications">
      <option value="newest">Newest First</option>
      <option value="oldest">Oldest First</option>
    </select>
    <div class="pubs-view-toggle" role="group" aria-label="View mode">
      <button class="pubs-view-btn" data-view="rich" title="Rich view" aria-pressed="false">
        <i class="fa-solid fa-grip" aria-hidden="true"></i>
      </button>
      <button class="pubs-view-btn active" data-view="compact" title="Compact view" aria-pressed="true">
        <i class="fa-solid fa-list" aria-hidden="true"></i>
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
{% include list.html data_array=filtered_pubs component="citation" style="rich" %}
</div>
