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
  image="images/gallery/2025/WhatsApp Image 2025-04-24 at 7.24.29 PM.jpeg"
  link="team"
  title="Our Team"
  text=text
%}

<p class="home-team-photo">
<img src="../images/gallery/team-itrc.jpeg" alt="Lab team photo at ITRC event" loading="lazy"/>
</p>


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
