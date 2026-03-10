---
title: Home
---

<!-- dark: true; -->
<!-- size: full; -->
<div class="home-hero">
  <div class="home-hero__inner">
    <div class="home-hero__content">
      <div class="home-hero__badge home-hero__animate delay-1">
        <span class="home-hero__badge-dot"></span>
        InfoLab at SKKU
      </div>
      <h1 class="home-hero__title home-hero__animate delay-2">
        Secure, Intelligent Systems for Biomedical Discovery
      </h1>
      <p class="home-hero__lead home-hero__animate delay-3">
        We build trustworthy machine learning and security methods that accelerate bioinformatics and biomedical research.
      </p>
      <p class="home-hero__sub home-hero__animate delay-4">
        Part of the <a href="https://sw.skku.edu/eng_sw/index.do">College of Computing and Informatics</a> at
        <a href="https://www.skku.edu/eng/">Sungkyunkwan University (SKKU)</a>.
      </p>
      <div class="home-hero__actions home-hero__animate delay-5">
        <a class="button home-hero__button" href="#our-projects">Explore Our Work</a>
        <a class="button home-hero__button home-hero__button--ghost" href="/team">Meet the Team</a>
      </div>
      <div class="home-hero__meta home-hero__animate delay-6">
        <span class="home-hero__meta-item">Bioinformatics</span>
        <span class="home-hero__meta-item">Secure ML</span>
        <span class="home-hero__meta-item">Medical AI</span>
      </div>
    </div>
    <div class="home-hero__panel home-hero__animate delay-4">
      <div class="home-hero__panel-title">Research Focus</div>
      <div class="home-hero__panel-grid">
        <div class="home-hero__panel-item">
          <span class="home-hero__panel-icon">
            <i class="fa-solid fa-shield-halved" aria-hidden="true"></i>
          </span>
          <div>
            <strong>Secure Learning</strong>
            <p>Privacy-aware models for sensitive biomedical data.</p>
          </div>
        </div>
        <div class="home-hero__panel-item">
          <span class="home-hero__panel-icon">
            <i class="fa-solid fa-dna" aria-hidden="true"></i>
          </span>
          <div>
            <strong>Bioinformatics Pipelines</strong>
            <p>Computational tools that translate data into discovery.</p>
          </div>
        </div>
        <div class="home-hero__panel-item">
          <span class="home-hero__panel-icon">
            <i class="fa-solid fa-brain" aria-hidden="true"></i>
          </span>
          <div>
            <strong>Robust AI Systems</strong>
            <p>Resilient models that generalize in clinical settings.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>



{% include section.html %}

<div id="our-projects" class="home-anchor"></div>
## Our Projects
{% include project-carousel.html %}

{% include section.html %}

{% capture col1 %}
## Our news

  <div class="home-news">
  {% assign sorted_news = site.data.news | sort: "date" | reverse %}
    {% for post in sorted_news limit:5 %}
    
  <div class="news-card">
    <div class="news-header">
        <span class="news-title">{{ post.title }}</span>
        <span class="news-date">{% include icon.html icon="fa-regular fa-calendar" %} {{ post.date | date: "%B %d, %Y" }} </span>
    </div>
    <div class="news-description">
        {{ post.description }} 
            {% if post.url %}
            <a href="{{ post.url }}" target="_blank">More...</a>
            {% endif %}
    </div>
  </div>

    {% endfor %}  
  </div>
  
{%
  include button.html
  link="news"
  text="Read all news"
  icon="fa-solid fa-arrow-right"
  flip=true
  align=left
%}

{% endcapture %}

{% include cols.html col1=col1 %}

{% include section.html %}

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

Our team includes graduate students, postdoctoral researchers, programmers, and staff, with diverse backgrounds in experimental biology, computer science, and bioinformatics. Come meet the people behind the research!

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

{% include section.html %}

<div class="home-cloud">
  <!-- Generated from https://shiny.rcg.sfu.ca/u/rdmorin/pubmedcloud3/ -->
  <img src="../images/gallery/team-itrc.jpeg" alt="A word cloud of publication titles"/>
</div>
{%
  include button.html
  icon="fa-solid fa-door-open"
  text="Join us"
  link="/team/join"
%}
{% include section.html %}

#### Our funders

{% capture col1 %}
<img src="images/skku-logo.png">
{% endcapture %}

{% capture col2 %}
<img src="images/msit-logo.png">
{% endcapture %}

{% capture col3 %}
<img src="images/nrf-logo2.png">
{% endcapture %}

<div class="home-funders">
  {% include cols.html col1=col1 col2=col2 col3=col3%}
</div>
