---
title: News
nav:
  order: 1
  tooltip: Lab news and updates
---

{% assign all_news     = site.data.news | sort: "date" | reverse %}
{% assign news_dates   = all_news | map: "date" | sort %}
{% assign oldest_yr    = news_dates | first | date: "%Y" %}
{% assign newest_yr    = news_dates | last  | date: "%Y" %}
{% assign latest_item  = all_news | first %}
{% assign news_by_year = all_news | group_by_exp: "item", "item.date | date: '%Y'" | sort: "name" | reverse %}

<!-- HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">InfoLab</div>
    <h1 class="team-hero-title">News &amp; Updates</h1>
    <p class="team-hero-sub">Latest publications, achievements, and announcements from our lab.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">{{ all_news.size }}</span>
        <span class="team-hstat-lbl">Updates</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ oldest_yr }}&ndash;{{ newest_yr }}</span>
        <span class="team-hstat-lbl">Years</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ latest_item.date | date: "%b %Y" }}</span>
        <span class="team-hstat-lbl">Latest</span>
      </div>
    </div>
  </div>
</div>

{% include section.html %}

<!-- TWO-COLUMN LAYOUT -->
<div class="news-layout">
<div class="news-col-main">

<!-- CATEGORY FILTER -->
<div class="news-filter-bar news-filter-bar--inline" role="group" aria-label="Filter updates by category">
  <button class="news-filter-btn active" data-filter="all" aria-pressed="true">
    <i class="fa-solid fa-layer-group" aria-hidden="true"></i> All
    <span class="news-filter-count"></span>
  </button>
  <button class="news-filter-btn" data-filter="publication" aria-pressed="false">
    <i class="fa-solid fa-file-lines" aria-hidden="true"></i> Publications
    <span class="news-filter-count"></span>
  </button>
  <button class="news-filter-btn" data-filter="member" aria-pressed="false">
    <i class="fa-solid fa-user-plus" aria-hidden="true"></i> Members
    <span class="news-filter-count"></span>
  </button>
  <button class="news-filter-btn" data-filter="patent" aria-pressed="false">
    <i class="fa-solid fa-certificate" aria-hidden="true"></i> Patents
    <span class="news-filter-count"></span>
  </button>
  <button class="news-filter-btn" data-filter="award" aria-pressed="false">
    <i class="fa-solid fa-trophy" aria-hidden="true"></i> Awards
    <span class="news-filter-count"></span>
  </button>
</div>

<!-- NEWS FEED -->
<div id="news-feed">
{% for year_group in news_by_year %}
<div class="news-year-group" data-year="{{ year_group.name }}">
  <div class="news-year-header">
    <span class="news-year-label">{{ year_group.name }}</span>
    <span class="news-year-count">{{ year_group.items.size }} update{% if year_group.items.size != 1 %}s{% endif %}</span>
  </div>
  <div class="news-cards-grid">
    {% for item in year_group.items %}
      {% assign item_year = item.date | date: "%Y" %}
      {% assign t = item.title | downcase %}
      {% assign d = item.description | downcase %}
      {% if t contains "patent" or d contains "patent application" %}
        {% assign item_type = "patent" %}
      {% elsif t contains "welcome" or t contains "new team" or t contains "new lab member" or t contains "new researcher" %}
        {% assign item_type = "member" %}
      {% elsif t contains "award" or t contains "fellowship" or t contains "prize" %}
        {% assign item_type = "award" %}
      {% else %}
        {% assign item_type = "publication" %}
      {% endif %}
      <article class="news-card-item" data-type="{{ item_type }}" data-year="{{ item_year }}">
        <div class="nci-accent nci-{{ item_type }}" aria-hidden="true"></div>
        <div class="nci-body">
          <div class="nci-meta">
            <span class="nci-type-badge nci-badge-{{ item_type }}">
              {% if item_type == "publication" %}<i class="fa-solid fa-file-lines"></i> Publication
              {% elsif item_type == "member" %}<i class="fa-solid fa-user-plus"></i> New Member
              {% elsif item_type == "patent" %}<i class="fa-solid fa-certificate"></i> Patent
              {% elsif item_type == "award" %}<i class="fa-solid fa-trophy"></i> Award
              {% else %}<i class="fa-solid fa-bell"></i> Update
              {% endif %}
            </span>
            <span class="nci-date">
              <i class="fa-regular fa-calendar"></i>
              {{ item.date | date: "%b %d, %Y" }}
            </span>
          </div>
          <h3 class="nci-title">
            {% if item.url %}<a href="{{ item.url }}" target="_blank" rel="noopener">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}
          </h3>
          <p class="nci-desc">{{ item.description }}</p>
          {% if item.url %}
            <a href="{{ item.url }}" class="nci-link" target="_blank" rel="noopener">Read more <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</div>
{% endfor %}
</div>

<p class="news-empty" id="news-empty">No updates found for the selected filter.</p>

</div><!-- /.news-col-main -->

<!-- BLUESKY SIDEBAR -->
<div class="news-col-side">
  <div class="news-social-section news-social-sticky">
    <div class="news-social-header">
      <i class="fa-brands fa-bluesky"></i>
      <span>BlueSky Feed</span>
      <a href="https://bsky.app/profile/infolab.bsky.social" target="_blank" rel="noopener" class="news-social-handle">@infolab.bsky.social</a>
    </div>
    <div class="bluesky-embed-wrap">
      <script type="module" src="https://cdn.jsdelivr.net/npm/bsky-embed/dist/bsky-embed.es.js" async></script>
      <bsky-embed
        username="infolab.bsky.social"
        mode=""
        limit="5"
        link-target="_blank"
        link-image="true"
        load-more="true"
        disable-styles="false"
        custom-styles=".border-slate-300 { border-color: gray; text-align: left}"
        date-format='{"type":"absolute","locale":"en","options":{"weekday":"long","year":"numeric","month":"long","day":"numeric"}}'
      ></bsky-embed>
    </div>
  </div>
</div><!-- /.news-col-side -->

</div><!-- /.news-layout -->
