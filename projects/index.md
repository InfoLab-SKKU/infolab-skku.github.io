---
title: Projects
nav:
  order: 2
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
    <button class="proj-filter-btn active" data-filter="all">All Projects</button>
    <button class="proj-filter-btn" data-filter="security">Security &amp; Adversarial ML</button>
    <button class="proj-filter-btn" data-filter="medical">Biomedical AI</button>
  </div>

  <div class="proj-grid">
    {% for project in site.data.projects %}
    <a href="/{{ project.link }}" class="proj-card" data-group="{{ project.group }}">
      <div class="proj-card-img">
        {% if project.image contains "://" %}
          <img src="{{ project.image }}" alt="{{ project.title }}" loading="lazy" onerror="this.closest('.proj-card-img').style.display='none'">
        {% else %}
          <img src="/{{ project.image }}" alt="{{ project.title }}" loading="lazy" onerror="this.closest('.proj-card-img').style.display='none'">
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
        <span>ICT Creative Consilience program (ICT명품인재) · IITP</span>
        <span class="proj-funding-date">Sep. 2021 – Dec. 2022</span>
      </div>
    </a>

    <a href="https://www.chowis.com/" class="proj-funding-card" target="_blank" rel="noopener noreferrer">
      <img src="https://static.wixstatic.com/media/a716c2_9c42e1548c9b43078135f37ff87b2190~mv2.png/v1/fill/w_127,h_31,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/chowislogo.png" alt="Chowis Logo" class="proj-funding-logo">
      <div class="proj-funding-info">
        <strong>Artificial Intelligent-based Skin Analysis Algorithms</strong>
        <span>Industry collaboration · Chowis Co., Ltd</span>
        <span class="proj-funding-date">Oct. 2020 – April 2021</span>
      </div>
    </a>

    <a href="https://www.nrf.re.kr/eng/main" class="proj-funding-card" target="_blank" rel="noopener noreferrer">
      <img src="/images/nrf-logo.png" alt="NRF Logo" class="proj-funding-logo">
      <div class="proj-funding-info">
        <strong>Software Authorship Identification Based on Deep Learning</strong>
        <span>Young Researcher Program · National Research Foundation (NRF) · MSIP</span>
        <span class="proj-funding-date">Nov. 2016 – Nov. 2019</span>
      </div>
    </a>

  </div>
</div>

