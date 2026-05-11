---
title: Gallery
nav:
  order: 8
  tooltip: Lab photos and activities
---

{% assign all_photos    = site.data.gallery %}
{% assign sorted_photos = all_photos | sort: "year" | reverse %}
{% assign event_photos  = all_photos | where: "category", "events" %}
{% assign conf_photos   = all_photos | where: "category", "conferences" %}
{% assign out_photos    = all_photos | where: "category", "outings" %}
{% assign mile_photos   = all_photos | where: "category", "milestones" %}
{% assign lab_photos    = all_photos | where: "category", "lab" %}
{% assign unique_cats   = all_photos | map: "category" | uniq %}
{% assign sorted_years  = all_photos | map: "year" | sort | uniq %}
{% assign newest_yr     = sorted_years | last %}

<!-- GALLERY HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">Lab Life</div>
    <h1 class="team-hero-title">Lab Gallery</h1>
    <p class="team-hero-sub">Memorable moments, events, and activities from our lab community.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">{{ all_photos.size }}</span>
        <span class="team-hstat-lbl">Photos</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ unique_cats.size }}</span>
        <span class="team-hstat-lbl">Categories</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">2020&ndash;{{ newest_yr }}</span>
        <span class="team-hstat-lbl">Years</span>
      </div>
    </div>
  </div>
</div>

{% include section.html %}

<!-- FILTER BAR — Category -->
<div class="gallery-filter-bar" id="gallery-cat-bar">
  <button class="gallery-filter-btn active" data-filter="all">
    <i class="fa-solid fa-images"></i> All
    <span class="gallery-filter-count">{{ all_photos.size }}</span>
  </button>
  <button class="gallery-filter-btn" data-filter="events">
    <i class="fa-solid fa-calendar-days"></i> Events
    <span class="gallery-filter-count">{{ event_photos.size }}</span>
  </button>
  <button class="gallery-filter-btn" data-filter="conferences">
    <i class="fa-solid fa-chalkboard-user"></i> Conferences
    <span class="gallery-filter-count">{{ conf_photos.size }}</span>
  </button>
  <button class="gallery-filter-btn" data-filter="outings">
    <i class="fa-solid fa-person-hiking"></i> Outings
    <span class="gallery-filter-count">{{ out_photos.size }}</span>
  </button>
  <button class="gallery-filter-btn" data-filter="milestones">
    <i class="fa-solid fa-trophy"></i> Milestones
    <span class="gallery-filter-count">{{ mile_photos.size }}</span>
  </button>
  <button class="gallery-filter-btn" data-filter="lab">
    <i class="fa-solid fa-flask"></i> Lab Life
    <span class="gallery-filter-count">{{ lab_photos.size }}</span>
  </button>
</div>

<!-- FILTER BAR — Year -->
<div class="gallery-year-bar" id="gallery-year-bar">
  <button class="gallery-year-btn active" data-year="all">
    <i class="fa-solid fa-calendar"></i> All Years
  </button>
  {% assign years_desc = sorted_years | reverse %}
  {% for yr in years_desc %}
  <button class="gallery-year-btn" data-year="{{ yr }}">{{ yr }}</button>
  {% endfor %}
</div>

<!-- MASONRY GRID -->
<div class="gallery-masonry" id="gallery-grid">
  {% for photo in sorted_photos %}
    {% assign encoded_src = photo.image | relative_url %}
    <div class="gallery-item"
      data-category="{{ photo.category }}"
      data-year="{{ photo.year }}"
      data-src="{{ encoded_src }}"
      data-caption="{{ photo.caption | escape }}">
      <div class="gallery-img-wrap">
        <img
          src="{{ encoded_src }}"
          alt="{{ photo.caption | escape }}"
          class="gallery-img"
          loading="lazy"
          {% include fallback.html %}
        >
        {% if photo.caption and photo.caption != "" %}
          <div class="gallery-caption-overlay">{{ photo.caption }}</div>
        {% endif %}
        <div class="gallery-item-year">{{ photo.year }}</div>
      </div>
    </div>
  {% endfor %}
</div>

<p class="gallery-empty" id="gallery-empty">No photos in this category yet.</p>

<!-- LIGHTBOX -->
<div id="gallery-lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer">
  <button id="lb-close" aria-label="Close"><i class="fa-solid fa-xmark"></i></button>
  <button id="lb-prev" aria-label="Previous photo"><i class="fa-solid fa-chevron-left"></i></button>
  <img id="lb-img" src="" alt="Gallery photo">
  <button id="lb-next" aria-label="Next photo"><i class="fa-solid fa-chevron-right"></i></button>
  <p id="lb-caption"></p>
  <p id="lb-counter"></p>
</div>

