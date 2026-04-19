---
title: Contact
nav:
  order: 8
  tooltip: Contact information
---

<!-- HERO -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">InfoLab · SKKU</div>
    <h1 class="team-hero-title">Contact Us</h1>
    <p class="team-hero-sub">We welcome collaboration, student inquiries, and research partnerships.</p>
  </div>
</div>

{% include section.html %}

<!-- MAIN LAYOUT -->
<div class="contact-layout">

  <!-- LEFT: Contact cards + map -->
  <div class="contact-col-main">

    <!-- Info cards -->
    <div class="contact-cards">

      <div class="contact-card">
        <div class="contact-card-icon"><i class="fa-solid fa-envelope"></i></div>
        <div class="contact-card-body">
          <div class="contact-card-label">Email</div>
          <span class="contact-obf" data-u="tamer" data-d="skku.edu" data-t="email"></span>
        </div>
      </div>

      <div class="contact-card">
        <div class="contact-card-icon"><i class="fa-solid fa-phone"></i></div>
        <div class="contact-card-body">
          <div class="contact-card-label">Phone</div>
          <span class="contact-obf" data-p="82312907968" data-s="(+82) 31-290-7968" data-t="phone"></span>
        </div>
      </div>

      <div class="contact-card">
        <div class="contact-card-icon"><i class="fa-solid fa-flask"></i></div>
        <div class="contact-card-body">
          <div class="contact-card-label">Lab Office</div>
          <span class="contact-card-value">Engineering Building 2, Room 27501 (5F)</span>
        </div>
      </div>

      <div class="contact-card">
        <div class="contact-card-icon"><i class="fa-solid fa-door-open"></i></div>
        <div class="contact-card-body">
          <div class="contact-card-label">Professor Office</div>
          <span class="contact-card-value">Research &amp; Business Center, Room 85489 (4F)</span>
        </div>
      </div>

      <div class="contact-card">
        <div class="contact-card-icon"><i class="fa-solid fa-location-dot"></i></div>
        <div class="contact-card-body">
          <div class="contact-card-label">Address</div>
          <span class="contact-card-value">2066 Seobu-Ro, Jangan-Gu, Suwon, Gyeonggi-Do 16419, South Korea</span>
        </div>
      </div>

    </div>

    <!-- Map -->
    <div class="contact-map-wrap">
      <iframe
        title="InfoLab location map"
        width="100%"
        height="380"
        frameborder="0"
        src="https://maps.google.com/maps?q=Hwasan-ro,%20Yulcheon-dong,%20Jangan-gu,%20Suwon-si,%20Gyeonggi-do+(Infolab)&t=&z=16&ie=UTF8&iwloc=B&output=embed"
        allowfullscreen
        loading="lazy"
      ></iframe>
    </div>

    <div class="contact-map-btn">
      {% include button.html icon="fa-solid fa-map" text="View SKKU Campus Map" link="https://www.skku.edu/eng/About/campusinfo/CampusMap.do?campusCd=2&srSearchValue=" %}
    </div>

  </div>

  <!-- RIGHT: Social + Join us -->
  <div class="contact-col-side">

    <div class="contact-side-card">
      <h3 class="contact-side-title"><i class="fa-solid fa-share-nodes"></i> Find Us Online</h3>
      <div class="contact-social-list">
        <a href="https://bsky.app/profile/infolab.bsky.social" target="_blank" rel="noopener" class="contact-social-item">
          <i class="fa-brands fa-bluesky"></i><span>@infolab.bsky.social</span>
        </a>
        <a href="https://x.com/infolabskku" target="_blank" rel="noopener" class="contact-social-item">
          <i class="fa-brands fa-x-twitter"></i><span>@infolabskku</span>
        </a>
        <a href="https://github.com/InfoLab-SKKU" target="_blank" rel="noopener" class="contact-social-item">
          <i class="fa-brands fa-github"></i><span>InfoLab-SKKU</span>
        </a>
        <a href="https://scholar.google.com/citations?user=pLC4l6YAAAAJ" target="_blank" rel="noopener" class="contact-social-item">
          <i class="fa-brands fa-google"></i><span>Google Scholar</span>
        </a>
        <a href="https://www.researchgate.net/lab/SKKU-InfoLab-Information-laboratory-Tamer-Abuhmed" target="_blank" rel="noopener" class="contact-social-item">
          <i class="fa-brands fa-researchgate"></i><span>ResearchGate</span>
        </a>
        <a href="https://orcid.org/0000-0001-9232-4843" target="_blank" rel="noopener" class="contact-social-item">
          <i class="fa-brands fa-orcid"></i><span>ORCID 0000-0001-9232-4843</span>
        </a>
        <a href="https://www.linkedin.com/in/tamerih" target="_blank" rel="noopener" class="contact-social-item">
          <i class="fa-brands fa-linkedin"></i><span>linkedin.com/in/tamerih</span>
        </a>
      </div>
    </div>

    <div class="contact-side-card contact-join-card">
      <h3 class="contact-side-title"><i class="fa-solid fa-user-plus"></i> Join Our Lab</h3>
      <p class="contact-join-text">We are always looking for motivated <strong>Ph.D.</strong>, <strong>M.S.</strong>, and <strong>undergraduate</strong> students passionate about AI security, trustworthy ML, and medical AI.</p>
      <ul class="contact-join-list">
        <li><i class="fa-solid fa-check"></i> Strong background in ML/DL or security</li>
        <li><i class="fa-solid fa-check"></i> Competitive scholarship opportunities</li>
        <li><i class="fa-solid fa-check"></i> International research collaborations</li>
      </ul>
      <span class="contact-obf" data-u="tamer" data-d="skku.edu" data-t="email-btn" data-s="Graduate%20Application%20Inquiry" class="contact-join-btn">
        <i class="fa-solid fa-paper-plane"></i> Send an Inquiry
      </span>
    </div>

  </div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.contact-obf').forEach(function (el) {
    var t = el.dataset.t;
    if (t === 'email') {
      var addr = el.dataset.u + '\x40' + el.dataset.d;
      var a = document.createElement('a');
      a.className = 'contact-card-value';
      a.href = 'mai' + 'lto:' + addr;
      a.textContent = addr;
      el.appendChild(a);
    } else if (t === 'phone') {
      var a = document.createElement('a');
      a.className = 'contact-card-value';
      a.href = 'te' + 'l:+' + el.dataset.p;
      a.textContent = el.dataset.s;
      el.appendChild(a);
    } else if (t === 'email-btn') {
      var addr = el.dataset.u + '\x40' + el.dataset.d;
      el.style.cursor = 'pointer';
      el.classList.add('contact-join-btn');
      el.addEventListener('click', function () {
        window.location.href = 'mai' + 'lto:' + addr + '?subject=' + el.dataset.s;
      });
    }
  });
});
</script>