---
title: Research Impact
nav:
  order: 4
  tooltip: Citation metrics and research impact
---

{% assign current_year = 'now' | date: "%Y" %}
{% assign total_pubs = site.data.citations | size %}

<!-- HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">InfoLab</div>
    <h1 class="team-hero-title">Research Impact</h1>
    <p class="team-hero-sub">Bibliometric overview of InfoLab's scholarly output and influence.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">6,200+</span>
        <span class="team-hstat-lbl">Citations</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">35+</span>
        <span class="team-hstat-lbl">h-index</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">65+</span>
        <span class="team-hstat-lbl">i10-index</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ total_pubs }}</span>
        <span class="team-hstat-lbl">Publications</span>
      </div>
    </div>
  </div>
</div>

{% include section.html %}

## {% include icon.html icon="fa-solid fa-chart-line" %} Bibliometric Overview

<div class="impact-metrics-grid">
  <div class="impact-metric-card impact-metric-card--primary">
    <div class="impact-metric-icon"><i class="fa-solid fa-quote-left"></i></div>
    <div class="impact-metric-num">6,200+</div>
    <div class="impact-metric-lbl">Total Citations</div>
    <div class="impact-metric-note">Google Scholar · All time</div>
  </div>
  <div class="impact-metric-card">
    <div class="impact-metric-icon"><i class="fa-solid fa-ranking-star"></i></div>
    <div class="impact-metric-num">35+</div>
    <div class="impact-metric-lbl">h-index</div>
    <div class="impact-metric-note">At least 35 papers with ≥35 citations each</div>
  </div>
  <div class="impact-metric-card">
    <div class="impact-metric-icon"><i class="fa-solid fa-layer-group"></i></div>
    <div class="impact-metric-num">65+</div>
    <div class="impact-metric-lbl">i10-index</div>
    <div class="impact-metric-note">Papers with at least 10 citations</div>
  </div>
  <div class="impact-metric-card">
    <div class="impact-metric-icon"><i class="fa-regular fa-newspaper"></i></div>
    <div class="impact-metric-num">76+</div>
    <div class="impact-metric-lbl">Journal Articles</div>
    <div class="impact-metric-note">Peer-reviewed journal publications</div>
  </div>
  <div class="impact-metric-card">
    <div class="impact-metric-icon"><i class="fa-solid fa-person-chalkboard"></i></div>
    <div class="impact-metric-num">25+</div>
    <div class="impact-metric-lbl">Conference Papers</div>
    <div class="impact-metric-note">IEEE, ACM, USENIX, Springer venues</div>
  </div>
  <div class="impact-metric-card">
    <div class="impact-metric-icon"><i class="fa-solid fa-calendar-days"></i></div>
    <div class="impact-metric-num">2009–{{ current_year }}</div>
    <div class="impact-metric-lbl">Active Since</div>
    <div class="impact-metric-note">Continuous publication record</div>
  </div>
</div>

<div class="impact-scholar-link">
  {%
    include button.html
    icon="fa-brands fa-google"
    text="View full profile on Google Scholar"
    link="https://scholar.google.com/citations?user=pLC4l6YAAAAJ"
    style="button"
  %}
  {%
    include button.html
    icon="fa-brands fa-orcid"
    text="ORCID Profile"
    link="https://orcid.org/0000-0001-9232-4843"
    style="button"
  %}
</div>

{% include section.html %}

## {% include icon.html icon="fa-solid fa-trophy" %} Top Publication Venues

<div class="impact-venues-grid">
  <div class="impact-venue-card">
    <div class="impact-venue-badge impact-venue-badge--ieee">IEEE</div>
    <div class="impact-venue-name">IEEE Transactions on Dependable and Secure Computing</div>
    <div class="impact-venue-note">TDSC · Q1</div>
  </div>
  <div class="impact-venue-card">
    <div class="impact-venue-badge impact-venue-badge--ieee">IEEE</div>
    <div class="impact-venue-name">IEEE Transactions on Information Forensics &amp; Security</div>
    <div class="impact-venue-note">TIFS · Q1</div>
  </div>
  <div class="impact-venue-card">
    <div class="impact-venue-badge impact-venue-badge--ieee">IEEE</div>
    <div class="impact-venue-name">IEEE Access</div>
    <div class="impact-venue-note">Open Access · Q1</div>
  </div>
  <div class="impact-venue-card">
    <div class="impact-venue-badge impact-venue-badge--elsevier">Elsevier</div>
    <div class="impact-venue-name">Information Fusion</div>
    <div class="impact-venue-note">IF > 14 · Q1</div>
  </div>
  <div class="impact-venue-card">
    <div class="impact-venue-badge impact-venue-badge--elsevier">Elsevier</div>
    <div class="impact-venue-name">Knowledge-Based Systems</div>
    <div class="impact-venue-note">KBS · Q1</div>
  </div>
  <div class="impact-venue-card">
    <div class="impact-venue-badge impact-venue-badge--nature">Nature</div>
    <div class="impact-venue-name">Scientific Reports</div>
    <div class="impact-venue-note">Open Access · Q1</div>
  </div>
  <div class="impact-venue-card">
    <div class="impact-venue-badge impact-venue-badge--acm">ACM</div>
    <div class="impact-venue-name">ACM CCS</div>
    <div class="impact-venue-note">Conference · Top-4 Security</div>
  </div>
  <div class="impact-venue-card">
    <div class="impact-venue-badge impact-venue-badge--usenix">USENIX</div>
    <div class="impact-venue-name">NDSS Symposium</div>
    <div class="impact-venue-note">Conference · Top-4 Security</div>
  </div>
</div>

{% include section.html %}

## {% include icon.html icon="fa-solid fa-coins" %} Research Funding

<div class="impact-funding-grid">
  <div class="impact-funding-card">
    <div class="impact-funding-agency">NRF</div>
    <div class="impact-funding-title">Alzheimer's Disease Clinical Decision Support</div>
    <div class="impact-funding-meta">National Research Foundation of Korea · 2021–2024</div>
  </div>
  <div class="impact-funding-card">
    <div class="impact-funding-agency">IITP</div>
    <div class="impact-funding-title">SW-Oriented University Supporting Program</div>
    <div class="impact-funding-meta">Institute for Information &amp; Communications Technology Planning &amp; Evaluation · 2021–2026</div>
  </div>
</div>

{% include section.html %}

## {% include icon.html icon="fa-solid fa-globe" %} Research Areas

<div class="impact-areas-grid">
  <div class="impact-area-card impact-area-card--security">
    <i class="fa-solid fa-shield impact-area-icon"></i>
    <div class="impact-area-name">Security &amp; Adversarial ML</div>
    <div class="impact-area-desc">Adversarial attacks, malware detection, intrusion detection, deepfake detection, federated learning security, continuous authentication</div>
  </div>
  <div class="impact-area-card impact-area-card--bio">
    <i class="fa-solid fa-heart-pulse impact-area-icon"></i>
    <div class="impact-area-name">Biomedical AI</div>
    <div class="impact-area-desc">Alzheimer's progression detection, ICU mortality prediction, clinical decision support, multimodal medical data fusion</div>
  </div>
  <div class="impact-area-card impact-area-card--xai">
    <i class="fa-solid fa-brain impact-area-icon"></i>
    <div class="impact-area-name">Trustworthy &amp; Explainable AI</div>
    <div class="impact-area-desc">XAI for high-stakes decisions, dynamic ensemble learning, interpretable deep learning, agentic AI systems</div>
  </div>
</div>
