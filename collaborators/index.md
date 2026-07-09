---
title: Collaborators
nav:
  order: 4
  tooltip: Our collaborators
---

{% assign collaborators = site.members | where: "group", "collab" %}

<!-- COLLABORATORS HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">Global Network</div>
    <h1 class="team-hero-title">Collaborators</h1>
    <p class="team-hero-sub">We work with outstanding researchers and faculty around the world, spanning cybersecurity, AI, and data science.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">{{ collaborators.size }}</span>
        <span class="team-hstat-lbl">Collaborators</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">6+</span>
        <span class="team-hstat-lbl">Countries</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">10+</span>
        <span class="team-hstat-lbl">Institutions</span>
      </div>
    </div>
  </div>
</div>

{% include team-nav.html %}

{% include collab-map.html %}

<div class="team-section">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-handshake"></i></span>
    <h2 class="team-section-title">Research Collaborators</h2>
  </div>
  <div class="team-member-grid collab-grid">
    {% for member in collaborators %}
      {% assign mtype = site.data.types[member.role] %}
      <div class="mem-card">
        <a href="{{ member.url | relative_url }}" class="mem-card-photo-link" aria-label="{{ member.name }}">
          <img src="{{ member.image | relative_url }}" alt="{{ member.name }}" class="mem-card-photo" loading="lazy" {% include fallback.html %}>
        </a>
        <div class="mem-card-body">
          <span class="mem-role-pill">{{ mtype.description | default: member.role }}</span>
          <h3 class="mem-card-name">
            <a href="{{ member.url | relative_url }}">{{ member.name }}</a>
          </h3>
          <p class="mem-card-bio">{{ member.content | strip_html | strip | truncatewords: 18 }}</p>
          <div class="mem-card-links">
            {% for link in member.links %}
              {% assign lkey = link[0] %}
              {% assign lval = link[1] | strip %}
              {% if lval != "" %}
                {% assign ltype = site.data.types[lkey] %}
                {% if ltype %}
                  {% if lkey == "email" %}
                    {% comment %} spam protection: address split into data attrs, assembled by email-protect.js {% endcomment %}
                    {% assign e_parts = lval | split: "@" %}
                    <a href="#" class="mem-link mem-link-email email-protected" data-eu="{{ e_parts[0] }}" data-ed="{{ e_parts[1] }}" title="{{ ltype.tooltip | default: lkey }}">
                      {% include icon.html icon=ltype.icon %}
                    </a>
                  {% else %}
                    {% if ltype.link %}
                      {% assign lhref = ltype.link | replace: "$VALUE", lval %}
                    {% else %}
                      {% assign lhref = lval %}
                    {% endif %}
                    <a href="{{ lhref }}" class="mem-link mem-link-{{ lkey }}" title="{{ ltype.tooltip | default: lkey }}" target="_blank" rel="noopener noreferrer">
                      {% include icon.html icon=ltype.icon %}
                    </a>
                  {% endif %}
                {% elsif lkey == "home-page" %}
                  <a href="{{ lval }}" class="mem-link mem-link-home" title="Website" target="_blank" rel="noopener noreferrer">
                    <i class="fa-solid fa-globe"></i>
                  </a>
                {% endif %}
              {% endif %}
            {% endfor %}
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>
