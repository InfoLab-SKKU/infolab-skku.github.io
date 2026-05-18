---
title: Home
---

<!-- ============================================================
     HERO SECTION
     ============================================================ -->
<section class="hero-section" aria-labelledby="hero-title">
  <div class="hero-bg" aria-hidden="true">
    {% include hero-svg.html %}
  </div>

  <div class="hero-content">
    <div class="hero-badge">Information Research Laboratory &middot; SKKU</div>
    <h1 id="hero-title" class="hero-title">
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
</section>

<!-- ============================================================
     STATS BAR
     ============================================================ -->
<section class="stats-bar" aria-label="Lab statistics">
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
</section>

<!-- ============================================================
     RESEARCH AREAS
     ============================================================ -->
<section class="ra-section" aria-label="Research areas">
  <div class="ra-grid">
    <a href="/projects/security" class="ra-card ra-card-link" data-area="security">
      <div class="ra-icon-wrap ra-security" aria-hidden="true">
        {% include icon.html icon="fa-solid fa-shield-halved" %}
      </div>
      <h3>Security &amp; Adversarial ML</h3>
      <p>Defending AI systems against adversarial attacks, malware, binary analysis, and exploitation of interpretability mechanisms in high-stakes environments.</p>
    </a>
    <a href="/projects/medical" class="ra-card ra-card-link" data-area="biomedical">
      <div class="ra-icon-wrap ra-biomedical" aria-hidden="true">
        {% include icon.html icon="fa-solid fa-dna" %}
      </div>
      <h3>Biomedical AI</h3>
      <p>Applying deep learning to medical imaging, Alzheimer's detection, multimodal clinical prediction, and biomedical discovery.</p>
    </a>
    <a href="/projects/explainable-ai" class="ra-card ra-card-link" data-area="trustworthy">
      <div class="ra-icon-wrap ra-trustworthy" aria-hidden="true">
        {% include icon.html icon="fa-solid fa-brain" %}
      </div>
      <h3>Trustworthy &amp; Explainable AI</h3>
      <p>Building transparent, interpretable, and robust AI systems for critical domains including healthcare, finance, and security.</p>
    </a>
  </div>
</section>

## {% include icon.html icon="fa-solid fa-flask" %} Our Projects

{% include project-carousel.html %}

<!-- ============================================================
     RECENT NEWS
     ============================================================ -->
<section class="hp-news-section" aria-label="Recent news">
  <div class="hp-news-header">
    <h2>{% include icon.html icon="fa-solid fa-newspaper" %} Recent News</h2>
  </div>
  <div class="hp-news-grid">
    {% assign sorted_news = site.data.news | sort: "date" | reverse %}
    {% for post in sorted_news limit:6 %}
    <article class="hp-news-card">
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
    </article>
    {% endfor %}
  </div>
  <div class="hp-news-more">
    <a href="/news" class="hp-news-all-btn">See All News &rarr;</a>
  </div>
</section>

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

<p class="home-team-photo">
<img src="../images/gallery/team-itrc.jpeg" alt="Lab team photo at ITRC event" loading="lazy"/>
</p>

{%
  include button.html
  icon="fa-solid fa-door-open"
  text="Join us"
  link="/team/join"
%}

### Our funders

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

