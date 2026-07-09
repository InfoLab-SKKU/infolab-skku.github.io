---
title: Lab Alumni
---

{% assign alum_members = site.members | where: "group", "alum" %}
{% assign alum_phd = alum_members | where: "role", "phd" %}
{% assign alum_master = alum_members | where: "role", "master" %}
{% assign alum_combined = alum_members | where: "role", "combined" %}
{% assign alum_grads = alum_phd | concat: alum_master | concat: alum_combined %}
{% assign alum_interns = alum_members | where: "role", "intern" %}

<!-- ALUMNI HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">Alumni</div>
    <h1 class="team-hero-title">Lab Alumni</h1>
    <p class="team-hero-sub">We have been lucky to have a fantastic group of individuals come through the lab — many have gone on to even bigger and better things.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">{{ alum_members.size }}</span>
        <span class="team-hstat-lbl">Total Alumni</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ alum_grads.size }}</span>
        <span class="team-hstat-lbl">Graduates</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ alum_interns.size }}</span>
        <span class="team-hstat-lbl">Interns</span>
      </div>
    </div>
  </div>
</div>

{% include team-nav.html %}

{% include section.html %}

<!-- GRADUATE ALUMNI -->
{% if alum_grads.size > 0 %}
<div class="team-section">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-graduation-cap"></i></span>
    <h2 class="team-section-title">Graduate Students</h2>
  </div>
  <div class="team-member-grid">
    {% for member in alum_grads %}
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
          {% if member.years_worked %}
            <p class="mem-card-years"><i class="fa-solid fa-calendar-alt"></i> {{ member.years_worked }}</p>
          {% endif %}
          {% if member.placement %}
            <p class="mem-card-now"><i class="fa-solid fa-briefcase"></i> {{ member.placement }}</p>
          {% endif %}
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
{% endif %}

{% include section.html %}

<!-- INTERN ALUMNI -->
{% if alum_interns.size > 0 %}
<div class="team-section">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-school"></i></span>
    <h2 class="team-section-title">Interns</h2>
  </div>
  <div class="team-member-grid">
    {% for member in alum_interns %}
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
          {% if member.years_worked %}
            <p class="mem-card-years"><i class="fa-solid fa-calendar-alt"></i> {{ member.years_worked }}</p>
          {% endif %}
          {% if member.placement %}
            <p class="mem-card-now"><i class="fa-solid fa-briefcase"></i> {{ member.placement }}</p>
          {% endif %}
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
{% endif %}
