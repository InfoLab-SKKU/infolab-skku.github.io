---
title: Home
---

<!-- ============================================================
     HOMEPAGE BENTO FRAMEWORK
     hero (animated neural canvas) · live stats · research pillars ·
     featured publication · news activity stream · join CTA
     ============================================================ -->
{% include hero-bento.html %}

<!-- ============================================================
     EDITORIAL FEATURES
     ============================================================ -->
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
  image="images/gallery/2025/itrc2025_team_03.jpeg"
  link="team"
  title="Our Team"
  text=text
%}

<p class="home-team-photo">
<img src="{{ 'images/gallery/team-itrc.jpeg' | relative_url }}" alt="Lab team photo at ITRC event" loading="lazy"/>
</p>


## Supported By

<div class="funders-band">
  <a href="https://www.skku.edu/eng/" target="_blank" rel="noopener noreferrer" data-tooltip="Sungkyunkwan University">
    <img src="{{ 'images/skku-logo.png' | relative_url }}" alt="Sungkyunkwan University (SKKU)" loading="lazy">
  </a>
  <a href="https://www.msit.go.kr/eng/" target="_blank" rel="noopener noreferrer" data-tooltip="Ministry of Science and ICT">
    <img src="{{ 'images/msit-logo.png' | relative_url }}" alt="Ministry of Science and ICT (MSIT)" loading="lazy">
  </a>
  <a href="https://www.nrf.re.kr/eng/main" target="_blank" rel="noopener noreferrer" data-tooltip="National Research Foundation of Korea">
    <img src="{{ 'images/nrf-logo2.png' | relative_url }}" alt="National Research Foundation of Korea (NRF)" loading="lazy">
  </a>
  <a href="https://www.iitp.kr/en/main.it" target="_blank" rel="noopener noreferrer" data-tooltip="Institute for ICT Planning & Evaluation">
    <img src="{{ 'images/iitp-logo.jpg' | relative_url }}" alt="Institute for Information & Communications Technology Planning & Evaluation (IITP)" loading="lazy">
  </a>
</div>
