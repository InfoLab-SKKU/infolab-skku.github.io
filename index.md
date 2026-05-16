---
title: Home
---

<!-- ============================================================
     HERO SECTION
     ============================================================ -->
<div class="hero-section" id="main-content" role="banner">
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <div class="hero-bg" aria-hidden="true">
    <svg class="hero-network-svg" viewBox="0 0 1200 200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
      <g opacity="0.16">
        <circle cx="120" cy="80" r="4" fill="white"/>
        <circle cx="360" cy="160" r="3" fill="white"/>
        <circle cx="600" cy="55" r="5" fill="white"/>
        <circle cx="840" cy="130" r="3" fill="white"/>
        <circle cx="1080" cy="75" r="4" fill="white"/>
        <circle cx="210" cy="320" r="3" fill="white"/>
        <circle cx="460" cy="390" r="4" fill="white"/>
        <circle cx="720" cy="290" r="3" fill="white"/>
        <circle cx="960" cy="370" r="4" fill="white"/>
        <circle cx="70"  cy="440" r="3" fill="white"/>
        <circle cx="1140" cy="410" r="3" fill="white"/>
        <circle cx="310" cy="470" r="4" fill="white"/>
        <circle cx="800" cy="460" r="3" fill="white"/>
        <circle cx="500" cy="230" r="3" fill="white"/>
        <circle cx="1000" cy="200" r="4" fill="white"/>
        <line x1="120" y1="80"  x2="360" y2="160"  stroke="white" stroke-width="1"/>
        <line x1="360" y1="160" x2="600" y2="55"   stroke="white" stroke-width="1"/>
        <line x1="600" y1="55"  x2="840" y2="130"  stroke="white" stroke-width="1"/>
        <line x1="840" y1="130" x2="1080" y2="75"  stroke="white" stroke-width="1"/>
        <line x1="120" y1="80"  x2="210" y2="320"  stroke="white" stroke-width="1"/>
        <line x1="360" y1="160" x2="460" y2="390"  stroke="white" stroke-width="1"/>
        <line x1="600" y1="55"  x2="500" y2="230"  stroke="white" stroke-width="1"/>
        <line x1="840" y1="130" x2="960" y2="370"  stroke="white" stroke-width="1"/>
        <line x1="1080" y1="75" x2="1000" y2="200" stroke="white" stroke-width="1"/>
        <line x1="210" y1="320" x2="460" y2="390"  stroke="white" stroke-width="1"/>
        <line x1="460" y1="390" x2="720" y2="290"  stroke="white" stroke-width="1"/>
        <line x1="720" y1="290" x2="960" y2="370"  stroke="white" stroke-width="1"/>
        <line x1="960" y1="370" x2="1140" y2="410" stroke="white" stroke-width="1"/>
        <line x1="70"  y1="440" x2="210" y2="320"  stroke="white" stroke-width="1"/>
        <line x1="70"  y1="440" x2="310" y2="470"  stroke="white" stroke-width="1"/>
        <line x1="800" y1="460" x2="960" y2="370"  stroke="white" stroke-width="1"/>
        <line x1="1000" y1="200" x2="1140" y2="410" stroke="white" stroke-width="1"/>
        <line x1="500" y1="230" x2="720" y2="290"  stroke="white" stroke-width="1"/>
      </g>
    </svg>
  </div>

  <div class="hero-content">
    <div class="hero-badge">Information Research Laboratory &middot; SKKU</div>
    <h1 class="hero-title">
      Advancing <span class="hero-accent">Security</span> &amp;
      <span class="hero-accent">Machine Learning</span>
    </h1>
    <p class="hero-lead">
      Pushing boundaries in bioinformatics, biomedical discovery, and trustworthy AI
      at Sungkyunkwan University, South Korea.
    </p>
    <div class="hero-ctas">
      <a href="/pubs" class="hero-btn-primary">
        {% include icon.html icon="fa-regular fa-newspaper" %}
        View Publications
      </a>
      <a href="/team" class="hero-btn-secondary">
        {% include icon.html icon="fa-solid fa-users" %}
        Meet the Team
      </a>
    </div>
    <p class="hero-affiliation">
      Part of the
      <a href="https://sw.skku.edu/eng_sw/index.do" rel="noopener noreferrer">College of Computing and Informatics</a>
      at
      <a href="https://www.skku.edu/eng/" rel="noopener noreferrer">Sungkyunkwan University</a>.
    </p>
  </div>
</div>

<!-- ============================================================
     STATS BAR
     ============================================================ -->
<div class="stats-bar" aria-label="Lab statistics">
  <div class="stats-inner">
    <div class="stat-item">
      {% assign pub_orcids = "0000-0001-9232-4843,0000-0002-0086-8155,0009-0002-4648-9289" | split: "," %}
      {% assign pub_count = 0 %}
      {% for citation in site.data.citations %}
        {% if pub_orcids contains citation.orcid %}
          {% assign pub_count = pub_count | plus: 1 %}
        {% endif %}
      {% endfor %}
      {% assign pub_tens = pub_count | divided_by: 10 | times: 10 %}
      <span class="stat-num">{{ pub_tens }}+</span>
      <span class="stat-lbl">Publications</span>
    </div>
    <div class="stat-sep" aria-hidden="true"></div>
    <div class="stat-item">
      {% assign active_members = site.members | where: "group", "active" %}
      <span class="stat-num">{{ active_members.size }}</span>
      <span class="stat-lbl">Lab Members</span>
    </div>
    <div class="stat-sep" aria-hidden="true"></div>
    <div class="stat-item">
      {% assign project_count = site.data.projects | size %}
      <span class="stat-num">{{ project_count }}</span>
      <span class="stat-lbl">Research Projects</span>
    </div>
    <div class="stat-sep" aria-hidden="true"></div>
    <div class="stat-item">
      {% assign years_active = 'now' | date: "%Y" | minus: 2019 %}
      <span class="stat-num">{{ years_active }}+</span>
      <span class="stat-lbl">Years Active</span>
    </div>
  </div>
</div>

<!-- ============================================================
     RESEARCH AREAS
     ============================================================ -->
<div class="ra-section">
  <div class="ra-grid">
    <a href="/projects/security" class="ra-card ra-card-link">
      <div class="ra-icon-wrap ra-security" aria-hidden="true">
        {% include icon.html icon="fa-solid fa-shield-halved" %}
      </div>
      <h3>Security &amp; Adversarial ML</h3>
      <p>Defending AI systems against adversarial attacks, malware, binary analysis, and exploitation of interpretability mechanisms in high-stakes environments.</p>
    </a>
    <a href="/projects/medical" class="ra-card ra-card-link">
      <div class="ra-icon-wrap ra-biomedical" aria-hidden="true">
        {% include icon.html icon="fa-solid fa-dna" %}
      </div>
      <h3>Biomedical AI</h3>
      <p>Applying deep learning to medical imaging, Alzheimer's detection, multimodal clinical prediction, and biomedical discovery.</p>
    </a>
    <a href="/projects/explinable-ai" class="ra-card ra-card-link">
      <div class="ra-icon-wrap ra-trustworthy" aria-hidden="true">
        {% include icon.html icon="fa-solid fa-brain" %}
      </div>
      <h3>Trustworthy &amp; Explainable AI</h3>
      <p>Building transparent, interpretable, and robust AI systems for critical domains including healthcare, finance, and security.</p>
    </a>
  </div>
</div>

## {% include icon.html icon="fa-solid fa-flask" %} Our Projects

{% include project-carousel.html %}

<!-- ============================================================
     RECENT NEWS
     ============================================================ -->
<div class="hp-news-section">
  <div class="hp-news-header">
    <h2>{% include icon.html icon="fa-solid fa-newspaper" %} Recent News</h2>
  </div>
  <div class="hp-news-grid">
    {% assign sorted_news = site.data.news | sort: "date" | reverse %}
    {% for post in sorted_news limit:6 %}
    <div class="hp-news-card">
      <div class="hp-news-date">{{ post.date | date: "%b %d, %Y" }}</div>
      <div class="hp-news-title">{{ post.title }}</div>
      {% if post.description %}
        <div class="hp-news-desc">{{ post.description | truncate: 320 }}</div>
        {% if post.description.size > 320 or post.url %}
          {% if post.url %}
            <a href="{{ post.url }}" target="_blank" rel="noopener noreferrer" class="hp-news-link">Read more &rarr;</a>
          {% else %}
            <a href="/news" class="hp-news-link">Read more &rarr;</a>
          {% endif %}
        {% endif %}
      {% endif %}
    </div>
    {% endfor %}
  </div>
  <div class="hp-news-more">
    <a href="/news" class="hp-news-all-btn">See All News &rarr;</a>
  </div>
</div>

{% capture text %}
A great way to explore our work is through our publications. Browse or search our full list of research outputs to learn more about what we do.

{%
  include button.html
  link="pubs"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}
{%
  include feature.html
  image="images/gallery/AR402001.jpg"
  link="pubs"
  title="Our Publications"
  flip=true
  text=text
%}

{% capture text %}
Our team includes graduate students, postdoctoral researchers, and researchers, with diverse backgrounds in computer science, AI, cybersecurity, and biomedical informatics. Come meet the people behind the research!

{%
  include button.html
  link="team"
  text="Meet the team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}
{%
  include feature.html
  image="images/gallery/2025/WhatsApp Image 2025-04-24 at 7.24.29 PM.jpeg"
  link="team"
  title="Our Team"
  text=text
%}

<center>
<img src="../images/gallery/team-itrc.jpeg" alt="Lab team photo at ITRC event" style="width:100%"/>
</center>

{%
  include button.html
  icon="fa-solid fa-door-open"
  text="Join us"
  link="/team/join"
%}

#### Our funders

{% capture col1 %}
<img src="images/skku-logo.png" alt="SKKU Logo">
{% endcapture %}

{% capture col2 %}
<img src="images/msit-logo.png" alt="MSIT Logo">
{% endcapture %}

{% capture col3 %}
<img src="images/nrf-logo2.png" alt="NRF Logo">
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

