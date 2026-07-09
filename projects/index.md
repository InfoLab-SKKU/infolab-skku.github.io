---
title: Projects
nav:
  order: 1
  tooltip: Projects in the lab
---

<!-- ============================================================
     CATEGORY HERO CARDS
     ============================================================ -->
{% assign security_count = site.data.projects | where: "group", "security" | size %}
{% assign medical_count  = site.data.projects | where: "group", "medical"  | size %}

<div class="proj-categories">
  <a href="/projects/security" class="proj-cat-card proj-cat-security">
    <div class="proj-cat-icon" aria-hidden="true">
      {% include icon.html icon="fa-solid fa-shield-halved" %}
    </div>
    <div class="proj-cat-body">
      <h2>Security &amp; Adversarial ML</h2>
      <p>Defending AI systems against adversarial attacks, malware, binary analysis, and behavioral authentication.</p>
      <span class="proj-cat-count">{{ security_count }} Projects</span>
    </div>
    <span class="proj-cat-arrow" aria-hidden="true">→</span>
  </a>

  <a href="/projects/medical" class="proj-cat-card proj-cat-medical">
    <div class="proj-cat-icon" aria-hidden="true">
      {% include icon.html icon="fa-solid fa-dna" %}
    </div>
    <div class="proj-cat-body">
      <h2>Biomedical AI</h2>
      <p>Applying deep learning to medical imaging, disease detection, and multimodal clinical decision support.</p>
      <span class="proj-cat-count">{{ medical_count }} Projects</span>
    </div>
    <span class="proj-cat-arrow" aria-hidden="true">→</span>
  </a>
</div>

<!-- ============================================================
     FILTER TABS + ALL PROJECTS GRID
     ============================================================ -->
<div class="proj-section">
  <div class="proj-filter-bar" role="group" aria-label="Filter projects by research area">
    <button class="proj-filter-btn active" data-filter="all" aria-pressed="true">All Projects</button>
    <button class="proj-filter-btn" data-filter="security" aria-pressed="false">Security &amp; Adversarial ML</button>
    <button class="proj-filter-btn" data-filter="medical" aria-pressed="false">Biomedical AI</button>
  </div>

  <div class="proj-grid">
    {% for project in site.data.projects %}
    <a href="/{{ project.link }}" class="proj-card" data-group="{{ project.group }}">
      <div class="proj-card-img">
        {% if project.image contains "://" %}
          <img src="{{ project.image }}" alt="{{ project.title }}" width="400" height="180" loading="lazy" data-fallback-hide>
        {% else %}
          <img src="/{{ project.image }}" alt="{{ project.title }}" width="400" height="180" loading="lazy" data-fallback-hide>
        {% endif %}
      </div>
      <div class="proj-card-body">
        {% if project.group == "security" %}
          <span class="proj-tag proj-tag-security">Security</span>
        {% elsif project.group == "medical" %}
          <span class="proj-tag proj-tag-medical">Biomedical AI</span>
        {% endif %}
        <h3>{{ project.title }}</h3>
        <p>{{ project.description | truncate: 130 }}</p>
      </div>
    </a>
    {% endfor %}
  </div>
</div>

<!-- ============================================================
     FUNDING SECTION
     ============================================================ -->
<div class="proj-funding-section">
  <h2>{% include icon.html icon="fa-solid fa-hand-holding-dollar" %} Funding &amp; Support</h2>

  <div class="proj-funding-list">

    <a href="https://www.nrf.re.kr/eng/main" class="proj-funding-card" target="_blank" rel="noopener noreferrer">
      <img src="/images/nrf-logo.png" alt="NRF Logo" class="proj-funding-logo">
      <div class="proj-funding-info">
        <strong>Intelligent and Robust Clinical Decision Support System for Alzheimer Disease</strong>
        <span>Mid-Career Researcher Program · National Research Foundation (NRF) · MSIP</span>
        <span class="proj-funding-date">March 2021 – Feb. 2024</span>
      </div>
    </a>

    <a href="https://www.iitp.kr/en/main.it" class="proj-funding-card" target="_blank" rel="noopener noreferrer">
      <img src="/images/iitp-logo.jpg" alt="IITP Logo" class="proj-funding-logo">
      <div class="proj-funding-info">
        <strong>SW-oriented College, Sungkyunkwan University</strong>
        <span>SW-oriented University Supporting Program (SW중심대학지원) · IITP</span>
        <span class="proj-funding-date">April 2021 – Dec. 2026</span>
      </div>
    </a>

    <a href="https://iitp.kr/kr/1/business/menuZDADXpage.it" class="proj-funding-card" target="_blank" rel="noopener noreferrer">
      <img src="/images/iitp-logo.jpg" alt="IITP Logo" class="proj-funding-logo">
      <div class="proj-funding-info">
        <strong>Towards Super Sapiens: Superintelligence for Future Human Innovations</strong>
        <span>ICT Creative Consilience Program (ICT명품인재) · IITP</span>
        <span class="proj-funding-date">Sep. 2021 – Dec. 2027</span>
      </div>
    </a>

    <a href="https://www.iitp.kr/en/main.it" class="proj-funding-card" target="_blank" rel="noopener noreferrer">
      <img src="/images/iitp-logo.jpg" alt="IITP Logo" class="proj-funding-logo">
      <div class="proj-funding-info">
        <strong>Development of a Policy-Adaptive AI Platform for Personal Information Protection Compliance</strong>
        <span>Institute for Information &amp; Communications Technology Planning &amp; Evaluation · IITP</span>
        <span class="proj-funding-date">Feb. 2022 – Dec. 2027</span>
      </div>
    </a>

  </div>
</div>

