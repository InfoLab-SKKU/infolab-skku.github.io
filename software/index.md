---
title: Software & Datasets
---

<!-- HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">InfoLab</div>
    <h1 class="team-hero-title">Software &amp; Datasets</h1>
    <p class="team-hero-sub">Open-source tools, datasets, and code releases from InfoLab research.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <a href="https://github.com/InfoLab-SKKU" target="_blank" rel="noopener" style="color:inherit;text-decoration:none;">
          <span class="team-hstat-num"><i class="fa-brands fa-github"></i> InfoLab-SKKU</span>
          <span class="team-hstat-lbl">GitHub Organization</span>
        </a>
      </div>
    </div>
  </div>
</div>

{% include section.html %}

## {% include icon.html icon="fa-solid fa-code" %} Code &amp; Tools

<div class="software-grid">

  <div class="software-card">
    <div class="software-card-header">
      <i class="fa-solid fa-shield software-card-icon software-card-icon--security"></i>
      <div>
        <div class="software-card-title">AdvEdge / AdvEdge+</div>
        <div class="software-card-tag software-card-tag--security">Security · XAI</div>
      </div>
    </div>
    <p class="software-card-desc">Adversarial attack framework targeting explanation-guided deep learning systems. Demonstrates that interpretation models (GradCAM, LIME, SHAP) can be exploited to produce misleading explanations while preserving a model's prediction.</p>
    <div class="software-card-links">
      {%
        include button.html
        icon="fa-brands fa-github"
        text="GitHub"
        link="https://github.com/InfoLab-SKKU"
        style="bare"
      %}
    </div>
  </div>

  <div class="software-card">
    <div class="software-card-header">
      <i class="fa-solid fa-magnifying-glass software-card-icon software-card-icon--security"></i>
      <div>
        <div class="software-card-title">SingleADV</div>
        <div class="software-card-tag software-card-tag--security">Security · Adversarial ML</div>
      </div>
    </div>
    <p class="software-card-desc">Single-model adversarial attack generator for interpretable deep learning. Achieves stealthy, query-efficient perturbations that fool both the classifier and its attached explanation model simultaneously.</p>
    <div class="software-card-links">
      {%
        include button.html
        icon="fa-brands fa-github"
        text="GitHub"
        link="https://github.com/InfoLab-SKKU"
        style="bare"
      %}
    </div>
  </div>

  <div class="software-card">
    <div class="software-card-header">
      <i class="fa-solid fa-brain software-card-icon software-card-icon--xai"></i>
      <div>
        <div class="software-card-title">ExplainableDEP</div>
        <div class="software-card-tag software-card-tag--xai">Biomedical · XAI</div>
      </div>
    </div>
    <p class="software-card-desc">Multi-layer dynamic ensemble framework for depression detection and severity assessment, paired with explanation outputs. Combines clinical time-series, NLP features from screening text, and physiological signals.</p>
    <div class="software-card-links">
      {%
        include button.html
        icon="fa-brands fa-github"
        text="GitHub"
        link="https://github.com/InfoLab-SKKU"
        style="bare"
      %}
    </div>
  </div>

  <div class="software-card">
    <div class="software-card-header">
      <i class="fa-solid fa-fingerprint software-card-icon software-card-icon--security"></i>
      <div>
        <div class="software-card-title">BioAuth Framework</div>
        <div class="software-card-tag software-card-tag--security">Security · Biometrics</div>
      </div>
    </div>
    <p class="software-card-desc">Continuous, sensor-based behavioral biometrics system for smartphone authentication. Collects accelerometer, gyroscope, and touch events; trains adversarially-robust models for session-long identity verification.</p>
    <div class="software-card-links">
      {%
        include button.html
        icon="fa-brands fa-github"
        text="GitHub"
        link="https://github.com/InfoLab-SKKU"
        style="bare"
      %}
    </div>
  </div>

</div>

{% include section.html %}

## {% include icon.html icon="fa-solid fa-database" %} Datasets

<div class="software-grid">

  <div class="software-card">
    <div class="software-card-header">
      <i class="fa-solid fa-mobile-screen software-card-icon software-card-icon--security"></i>
      <div>
        <div class="software-card-title">BioAuth Behavioral Dataset</div>
        <div class="software-card-tag software-card-tag--security">Biometrics · Mobile</div>
      </div>
    </div>
    <p class="software-card-desc">Behavioral sensor recordings (accelerometer, gyroscope, touch events) from participants performing standardized smartphone tasks. Used for continuous authentication model training and adversarial robustness evaluation.</p>
    <div class="software-card-links">
      {%
        include button.html
        icon="fa-brands fa-github"
        text="InfoLab-SKKU GitHub"
        link="https://github.com/InfoLab-SKKU"
        style="bare"
      %}
    </div>
  </div>

  <div class="software-card">
    <div class="software-card-header">
      <i class="fa-solid fa-heart-pulse software-card-icon software-card-icon--bio"></i>
      <div>
        <div class="software-card-title">ICU Clinical Time-Series</div>
        <div class="software-card-tag software-card-tag--bio">Biomedical · ICU</div>
      </div>
    </div>
    <p class="software-card-desc">Preprocessed and feature-engineered subsets of MIMIC-III/IV and eICU used in our mortality and length-of-stay prediction studies. Includes temporal vital signs, labs, medications, and diagnoses with train/test splits.</p>
    <div class="software-card-links">
      {%
        include button.html
        icon="fa-brands fa-github"
        text="InfoLab-SKKU GitHub"
        link="https://github.com/InfoLab-SKKU"
        style="bare"
      %}
    </div>
  </div>

</div>

{% include section.html %}

## {% include icon.html icon="fa-solid fa-circle-info" %} Using Our Work

If you use any InfoLab code or datasets in your research, please cite the corresponding paper. BibTeX entries are available on the [Publications](/pubs/) page via the **Cite** button on each paper card.

For questions, collaborations, or data access requests, [contact us](/contact/).
