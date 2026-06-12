---
title: Team
nav:
  order: 4
  tooltip: Meet the team
---

{% assign active_members = site.members | where: "group", "active" %}
{% assign pi_member = active_members | where: "role", "pi" | first %}
{% assign senior_members = active_members | where: "role", "senior" %}
{% assign phd_members = active_members | where: "role", "phd" %}
{% assign combined_members = active_members | where: "role", "combined" %}
{% assign master_members = active_members | where: "role", "master" %}
{% assign intern_members = active_members | where: "role", "intern" %}
{% assign researcher_count = senior_members.size | plus: phd_members.size | plus: combined_members.size | plus: master_members.size %}

<!-- TEAM HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">Our People</div>
    <h1 class="team-hero-title">Meet the Team</h1>
    <p class="team-hero-sub">A diverse, international group united by a shared mission — advancing AI for security, health, and society.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">{{ active_members.size }}</span>
        <span class="team-hstat-lbl">Active Members</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ researcher_count }}</span>
        <span class="team-hstat-lbl">Researchers</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ intern_members.size }}</span>
        <span class="team-hstat-lbl">Interns</span>
      </div>
    </div>
  </div>
</div>

{% include team-nav.html %}

{% include section.html %}

<!-- PI SECTION -->
<div id="pi" class="team-section">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-user-secret"></i></span>
    <h2 class="team-section-title">Principal Investigator</h2>
  </div>

  {% if pi_member %}
  <div class="pi-card">
    <a href="{{ pi_member.url | relative_url }}" class="pi-card-photo-wrap" aria-label="{{ pi_member.name }}">
      <img src="{{ pi_member.image | relative_url }}" alt="{{ pi_member.name }}" class="pi-card-photo" width="180" height="180" loading="lazy">
    </a>
    <div class="pi-card-body">
      <span class="pi-role-pill">Professor &amp; Lab Director</span>
      <h2 class="pi-card-name">
        <a href="{{ pi_member.url | relative_url }}">{{ pi_member.name }}</a>
      </h2>
      <p class="pi-card-affil">Associate Professor &middot; College of Computing and Informatics &middot; SKKU</p>
      <p class="pi-card-bio">{{ pi_member.content | strip_html | strip | truncatewords: 55 }}</p>
      <div class="pi-card-links">
        {% for link in pi_member.links %}
          {% assign lkey = link[0] %}
          {% assign lval = link[1] | strip %}
          {% if lval != "" %}
            {% assign ltype = site.data.types[lkey] %}
            {% if ltype %}
              {% if lkey == "email" %}
                {% comment %} spam protection: address split into data attrs, assembled by email-protect.js {% endcomment %}
                {% assign e_parts = lval | split: "@" %}
                <a href="#" class="pi-link pi-link-email email-protected" data-eu="{{ e_parts[0] }}" data-ed="{{ e_parts[1] }}" title="{{ ltype.tooltip | default: lkey }}">
                  {% include icon.html icon=ltype.icon %}
                </a>
              {% else %}
                {% if ltype.link %}
                  {% assign lhref = ltype.link | replace: "$VALUE", lval %}
                {% else %}
                  {% assign lhref = lval %}
                {% endif %}
                <a href="{{ lhref }}" class="pi-link pi-link-{{ lkey }}" title="{{ ltype.tooltip | default: lkey }}" target="_blank" rel="noopener noreferrer">
                  {% include icon.html icon=ltype.icon %}
                </a>
              {% endif %}
            {% endif %}
          {% endif %}
        {% endfor %}
      </div>
    </div>
  </div>
  {% endif %}
</div>

{% include section.html %}

<!-- RESEARCHERS SECTION -->
<div id="researchers" class="team-section">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-users"></i></span>
    <h2 class="team-section-title">Researchers</h2>
  </div>

  {% if senior_members.size > 0 %}
  <div class="team-role-group">
    <h3 class="team-role-label">Senior Researchers</h3>
    <div class="team-member-grid">
      {% for member in senior_members %}
        {% include team-member-card.html member=member %}
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if phd_members.size > 0 %}
  <div class="team-role-group">
    <h3 class="team-role-label">PhD Students</h3>
    <div class="team-member-grid">
      {% for member in phd_members %}
        {% include team-member-card.html member=member %}
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if combined_members.size > 0 %}
  <div class="team-role-group">
    <h3 class="team-role-label">Combined MS/PhD Students</h3>
    <div class="team-member-grid">
      {% for member in combined_members %}
        {% include team-member-card.html member=member %}
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if master_members.size > 0 %}
  <div class="team-role-group">
    <h3 class="team-role-label">Master's Students</h3>
    <div class="team-member-grid">
      {% for member in master_members %}
        {% include team-member-card.html member=member %}
      {% endfor %}
    </div>
  </div>
  {% endif %}
</div>

{% include section.html %}

<!-- INTERNS SECTION -->
{% if intern_members.size > 0 %}
<div id="interns" class="team-section">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-school"></i></span>
    <h2 class="team-section-title">Interns</h2>
  </div>
  <div class="team-member-grid">
    {% for member in intern_members %}
      {% include team-member-card.html member=member %}
    {% endfor %}
  </div>
</div>
{% endif %}
