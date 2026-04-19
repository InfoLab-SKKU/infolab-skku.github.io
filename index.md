---
title: Home
---

<div class="hero-with-news">
  <div class="hero-content-wrapper">
    <!-- LEFT COLUMN: Welcome -->
    <div class="hero-welcome">
      <div class="container" style="position: relative; z-index: 1; display: flex; flex-direction: column; justify-content: flex-start; align-items: flex-start; text-align: left; color: #fff; height: 100%; padding: 40px 40px 10px 20px; margin: 0;">
        <h1 style="font-size: 2.8rem; margin: 0 0 15px 0; font-weight: 700; line-height: 1.2;">Welcome to InfoLab</h1>
        <p class="lead" style="font-size: 1.05rem; margin: 0 0 15px 0; max-width: 100%;">
          Pushing the boundaries of <strong>security</strong> and <strong>machine learning</strong>, 
          especially in <strong>bioinformatics</strong> and <strong>biomedical discovery</strong>.
        </p>
        <p style="font-size: 0.9rem; margin: 0; opacity: 0.95;">
          Part of the 
          <a href="https://sw.skku.edu/eng_sw/index.do" style="color: #fff; text-decoration: underline;">College of Computing and Informatics</a> at 
          <a href="https://www.skku.edu/eng/" style="color: #fff; text-decoration: underline;">Sungkyunkwan University</a>.
        </p>
        <a href="#explore" class="button primary" style="background-color: transparent; color: white; border: 2px solid white; padding: 10px 28px; text-decoration: none; font-weight: bold; border-radius: 5px; transition: all 0.3s; width: fit-content; margin: 20px 0 0 0;" onmouseover="this.style.backgroundColor='rgba(255,255,255,0.1)'" onmouseout="this.style.backgroundColor='transparent'">
          Explore Our Work
        </a>
      </div>
    </div>

    <!-- RIGHT COLUMN: Recent News -->
    <div class="hero-news">
      <div style="position: relative; z-index: 1; padding: 40px 40px 0 40px; height: 100%; display: flex; flex-direction: column; justify-content: flex-start; width: 100%;">
        <h3 style="color: white; font-size: 1.1rem; margin-bottom: 0px; font-weight: 600; display: flex; align-items: center; gap: 8px;">
          {% include icon.html icon="fa-solid fa-newspaper" %} Recent News
        </h3>
        
        {% assign sorted_news = site.data.news | sort: "date" | reverse %}
        {% for post in sorted_news limit:3 %}
          <div class="hero-news-item">
            <div class="hero-news-date">{{ post.date | date: "%b %d" }}</div>
            <div class="hero-news-title">{{ post.title }}</div>
            {% if post.url %}
              <a href="{{ post.url }}" target="_blank" class="hero-news-link">Read →</a>
            {% endif %}
          </div>
        {% endfor %}
        
        <a href="/news" class="hero-news-btn" style="background-color: transparent; color: white; border: 2px solid white; padding: 10px 28px; text-decoration: none; font-weight: bold; border-radius: 5px; transition: all 0.3s; width: fit-content; display: inline-block; margin-top: 20px; font-size: 0.9rem;" onmouseover="this.style.backgroundColor='rgba(255,255,255,0.1)'" onmouseout="this.style.backgroundColor='transparent'">
          {% include icon.html icon="fa-solid fa-arrow-right" %} More News
        </a>
      </div>
    </div>
  </div>
</div>

<style>
  .hero-with-news {
    position: relative;
    width: 100vw;
    height: 58vh;
    margin: -60px calc(-50vw + 50%) 0 calc(-50vw + 50%);
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: stretch;
    background-color: #07377b;
  }

  .hero-content-wrapper {
    position: relative;
    width: 100%;
    max-width: 900px;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    z-index: 1;
    background-color: #07377b;
  }

  .hero-welcome {
    display: flex;
    align-items: center;
  }

  .hero-news {
    background-color: transparent;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
  }

  .hero-news-item {
    padding: 12px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: left;
    width: 100%;
  }

  .hero-news-item:last-of-type {
    border-bottom: none;
  }

  .hero-news-item:hover {
    padding-left: 8px;
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 4px;
  }

  .hero-news-date {
    font-size: 0.75rem;
    color: rgba(255, 255, 255, 0.6);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
    text-align: left;
  }

  .hero-news-title {
    font-size: 0.9rem;
    color: white;
    font-weight: 600;
    margin: 6px 0;
    line-height: 1.3;
    text-align: left;
  }

  .hero-news-link {
    font-size: 0.8rem;
    color: #7fc3ff;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
    text-align: left;
  }

  .hero-news-link:hover {
    color: white;
    text-decoration: underline;
  }

  .hero-news-all:hover {
    opacity: 1;
    text-decoration: underline;
  }

  @media (max-width: 1024px) {
    .hero-content-wrapper {
      grid-template-columns: 1fr;
    }

    .hero-news {
      border-left: none;
      border-top: 2px solid rgba(255, 255, 255, 0.2);
      padding: 20px;
    }

    .hero-with-news {
      height: auto;
    }
  }

  @media (max-width: 768px) {
    .hero-content-wrapper {
      grid-template-columns: 1fr;
    }

    .hero-welcome .container {
      padding: 30px 20px;
    }

    .hero-welcome h1 {
      font-size: 2rem;
    }
  }
</style>
## {% include icon.html icon="fa-solid fa-flask" %} Our Projects
{% include project-carousel.html %}
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
<center>
<!-- Generated from https://shiny.rcg.sfu.ca/u/rdmorin/pubmedcloud3/ -->
<img src="../images/gallery/team-itrc.jpeg" alt="A word cloud of publication titles" style="width:100%"/>
</center>
{%
  include button.html
  icon="fa-solid fa-door-open"
  text="Join us"
  link="/team/join"
%}
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


{% include cols.html col1=col1 col2=col2 col3=col3%}
