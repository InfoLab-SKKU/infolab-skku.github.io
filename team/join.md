---
title: Join us
description: Fully funded M.S./Ph.D. Combined and Ph.D. research positions at InfoLab, Sungkyunkwan University — full tuition waiver and monthly stipend — in AI security, trustworthy and explainable AI, and biomedical AI.
---

{% assign pub_orcids = site.data.pub-orcids %}
{% assign filtered_pubs = site.data.citations | where_exp: "c", "pub_orcids contains c.orcid" %}
{% assign total_pubs = filtered_pubs.size %}

<!-- ============================ HERO ============================ -->
<div class="team-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">Now Recruiting · Fully Funded</div>
    <h1 class="team-hero-title">Join InfoLab</h1>
    <p class="team-hero-sub">
      <strong>Fully funded M.S./Ph.D. Combined and Ph.D. research positions</strong> at the Information Research Laboratory,
      Sungkyunkwan University (SKKU), led by Prof. Tamer Abuhmed. We work on AI security and adversarial machine learning,
      trustworthy and explainable AI, and biomedical AI. Build rigorous research, publish at strong international venues,
      and grow into an independent researcher.
    </p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">100%</span>
        <span class="team-hstat-lbl">Tuition Covered</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">2</span>
        <span class="team-hstat-lbl">Graduate Programs</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">{{ total_pubs }}</span>
        <span class="team-hstat-lbl">Publications</span>
      </div>
    </div>
  </div>
</div>

{% include team-nav.html %}

{% include section.html %}

<!-- ================= CURRENTLY OPEN GRADUATE PROGRAMS ================= -->
<div class="team-section" id="open-programs">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-graduation-cap"></i></span>
    <h2 class="team-section-title">Currently Open Graduate Programs</h2>
  </div>

  <div class="join-grid">
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-layer-group"></i></span>
      <h3 class="join-card-title">M.S./Ph.D. Combined <span class="join-card-tag">Fully Funded</span></h3>
      <p class="join-card-desc">An integrated route from master's coursework through to the doctorate, without a separate re-application between degrees. Best suited to candidates who already intend to complete a Ph.D. and want to begin research early.</p>
    </div>
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-user-graduate"></i></span>
      <h3 class="join-card-title">Ph.D. <span class="join-card-tag">Fully Funded</span></h3>
      <p class="join-card-desc">For candidates who already hold a master's degree, or equivalent demonstrated research experience, and are ready to take ownership of a research direction and drive it to publication.</p>
    </div>
  </div>

  <div class="join-callout">
    <i class="fa-solid fa-circle-exclamation"></i>
    <p><strong>Standalone M.S. positions are not available at this time.</strong> We are currently recruiting only for the
    <strong>M.S./Ph.D. Combined</strong> and <strong>Ph.D.</strong> programs. If you are seeking a master's-only degree,
    this call is not the right fit — but you may still be a strong candidate for a
    <a href="#other-opportunities">research internship</a>.</p>
  </div>
</div>

{% include section.html %}

<!-- ================= FULLY FUNDED GRADUATE RESEARCH ================= -->
<div class="team-section" id="funding">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-hand-holding-dollar"></i></span>
    <h2 class="team-section-title">Fully Funded Graduate Research</h2>
  </div>
  <p class="team-intro">Graduate researchers admitted to the programs above are funded. You should be able to focus on research
  rather than on financing your degree.</p>
  <ul class="join-list">
    <li><i class="fa-solid fa-check"></i><span><strong>Full tuition fee waiver</strong> — 100% of tuition is covered for the duration of your funded position.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Monthly stipend</strong> — ongoing financial support so that research is your primary work.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Research computing resources</strong> — access to the lab's computing infrastructure for training and large-scale experimentation.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Direct mentorship</strong> from the PI and senior researchers, with regular technical feedback on your work.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Publication-oriented training</strong> — you will be supported in working toward first-author papers at strong international venues.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Active research projects</strong> — funded, ongoing work with real problems rather than invented exercises.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Collaboration</strong> with academic and industrial partners in Korea and internationally.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Conference participation support</strong>, subject to project funding and the stage of your work.</span></li>
  </ul>
</div>

{% include section.html %}

<!-- ========================= RESEARCH AREAS ========================= -->
<div class="team-section" id="research-areas">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-diagram-project"></i></span>
    <h2 class="team-section-title">Research Areas</h2>
  </div>
  <p class="team-intro">Read these before applying. The strongest applications name the specific problems the candidate wants to work on.</p>

  <div class="join-grid">
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-shield-halved"></i></span>
      <h3 class="join-card-title">AI Security &amp; Adversarial ML</h3>
      <p class="join-card-desc">Adversarial attacks and defenses, robustness of deep learning and foundation models, attacks against interpretable systems, robust malware detection, federated learning under poisoning, and behavioral biometric authentication.</p>
      <p class="join-card-desc"><a href="/projects/security">Security projects &rarr;</a></p>
    </div>
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-magnifying-glass-chart"></i></span>
      <h3 class="join-card-title">Trustworthy &amp; Explainable AI</h3>
      <p class="join-card-desc">Explainability and interpretability, uncertainty and reliability, robustness and fairness as joint objectives, and dynamic ensemble methods for dependable decision-making. This theme runs through most of what we do rather than sitting beside it.</p>
      <p class="join-card-desc"><a href="/projects/explainable-ai">Explainable AI &rarr;</a></p>
    </div>
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-heart-pulse"></i></span>
      <h3 class="join-card-title">Biomedical &amp; Healthcare AI</h3>
      <p class="join-card-desc">Trustworthy clinical AI, multimodal medical data, disease progression modelling, medical imaging, clinical prediction such as ICU outcomes, and large language models for clinical decision support.</p>
      <p class="join-card-desc"><a href="/projects/medical">Biomedical projects &rarr;</a></p>
    </div>
  </div>

  <p class="team-intro">See all <a href="/projects/">research projects</a> and our <a href="/pubs/">{{ total_pubs }} publications</a>
  to judge research fit for yourself.</p>
</div>

{% include section.html %}

<!-- =========================== WHY INFOLAB =========================== -->
<div class="team-section" id="why-infolab">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-star"></i></span>
    <h2 class="team-section-title">Why InfoLab</h2>
  </div>
  <ul class="join-list">
    <li><i class="fa-solid fa-check"></i><span><strong>Publication-oriented culture.</strong> Recent work has appeared at venues including NDSS, ACM SIGKDD, EMNLP Findings, IEEE Transactions on Information Forensics and Security, IEEE Transactions on Dependable and Secure Computing, and Information Fusion.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Focused mentorship.</strong> A lab deliberately sized so that supervision is direct and individual, not delegated down a long chain.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Interdisciplinary by design.</strong> Security, machine learning, and clinical problems sit in the same group, so methods developed for one area are tested against the others.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>A genuinely international group.</strong> Our researchers come from many countries — see the <a href="/team/">current team</a>. Research and publication are conducted in English.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Development toward independence.</strong> The aim is not that you execute assigned tasks well, but that you leave able to define and defend your own research agenda.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>SKKU and the Korean technology ecosystem.</strong> A research university with strong engineering infrastructure, situated in one of the world's most active technology economies.</span></li>
  </ul>
</div>

{% include section.html %}

<!-- ====================== WHO WE ARE LOOKING FOR ====================== -->
<div class="team-section" id="who-we-want">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-magnifying-glass"></i></span>
    <h2 class="team-section-title">Who We Are Looking For</h2>
  </div>
  <p class="team-intro">We are looking for researchers with the preparation and persistence to do original work. Strong candidates
  typically show several of the following:</p>
  <ul class="join-list">
    <li><i class="fa-solid fa-check"></i><span><strong>Research potential</strong> — evidenced by prior academic research, a thesis, a research assistantship, publications or preprints, or substantial industrial R&amp;D.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Solid foundations</strong> in mathematics and machine learning — linear algebra, probability, optimization, and the ability to reason about why a method works.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Real implementation ability</strong> — Python and a deep-learning framework such as PyTorch; systems or security tooling for security topics.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>The ability to read papers independently</strong> and reconstruct what a method actually does, including its weaknesses.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Evidence you finish things</strong> — a completed thesis, a shipped system, a reproducible open-source project, or a paper carried through to submission.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Clear written communication.</strong> Research is reading, writing, and arguing from evidence at least as much as it is coding.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Independence with collaboration</strong> — able to drive your own work forward while contributing to a shared research group.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Genuine alignment</strong> with the research areas above, rather than a general interest in AI.</span></li>
  </ul>

  <div class="join-callout">
    <i class="fa-solid fa-circle-info"></i>
    <p><strong>You are not expected to satisfy every item on this list.</strong> We evaluate research potential, preparation,
    and fit holistically. Candidates arrive from different starting points, and an applicant who is exceptionally strong in
    one dimension is more interesting to us than one who is uniformly average across all of them.</p>
  </div>
</div>

{% include section.html %}

<!-- ================= TWO PATHS TO JOINING ================= -->
<div class="team-section" id="two-paths">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-code-branch"></i></span>
    <h2 class="team-section-title">Two Paths to Joining as a Graduate Researcher</h2>
  </div>
  <p class="team-intro">There are two ways into the lab. Neither is superior — they suit different candidates.
  <strong>An InfoLab internship is preferred in some cases, but it is not mandatory.</strong></p>

  <div class="join-grid">
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-flask-vial"></i></span>
      <h3 class="join-card-title">Path A — Research Internship <span class="join-card-tag">Preferred, not required</span></h3>
      <p class="join-card-desc">Join us first as a research intern, then apply to the graduate program. This path suits you if you
      have limited formal research experience, want to demonstrate your potential through actual work, or would rather understand
      our research environment before committing to several years of study.</p>
      <p class="join-card-desc">The internship works as a mutual research-fit evaluation: you see how we work, and we see how you
      think. Many strong candidates choose this route deliberately, even when they could apply directly.</p>
    </div>
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-forward"></i></span>
      <h3 class="join-card-title">Path B — Direct Application <span class="join-card-tag">No internship needed</span></h3>
      <p class="join-card-desc">Apply directly to the M.S./Ph.D. Combined or Ph.D. program without an InfoLab internship. This path
      is open to you if you can demonstrate prior <strong>academic research experience</strong> or relevant
      <strong>industrial research / R&amp;D experience</strong>.</p>
      <p class="join-card-desc">Evidence may include peer-reviewed publications, conference or journal papers, preprints or
      manuscripts under review, an undergraduate or graduate thesis, a university research assistantship, a substantial
      faculty-supervised project, a research internship elsewhere, industrial AI/ML or advanced R&amp;D work, strong technical
      reports, meaningful open-source research contributions, or comparable reproducible research projects.</p>
    </div>
  </div>

  <div class="join-callout">
    <i class="fa-solid fa-circle-info"></i>
    <p><strong>Research potential can be demonstrated in more than one way, and publications are not required.</strong>
    A published paper is strong evidence and is genuinely valued — but a rigorous thesis, a serious industrial R&amp;D record,
    or a well-executed reproducible project can demonstrate the same underlying ability. Tell us what you have done and we will
    assess it on its merits.</p>
  </div>
</div>

{% include section.html %}

<!-- ================= RESEARCH JOURNEY ================= -->
<div class="team-section" id="research-journey">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-route"></i></span>
    <h2 class="team-section-title">Your Research Journey at InfoLab</h2>
  </div>
  <p class="team-intro">Graduate research follows a recognisable arc. Early on you will be guided closely; by the end you should be
  setting the direction yourself. Mentorship is active throughout, but intellectual ownership progressively becomes yours.</p>
  <ol class="join-steps">
    <li class="join-step">
      <span class="join-step-num">1</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Orientation and literature</h3>
        <p>Read deeply into a research area, reproduce key results, and learn to identify what is genuinely unsolved rather than merely unpublished.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">2</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Problem formulation</h3>
        <p>Turn a broad interest into a precise, falsifiable research question with a defensible evaluation plan.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">3</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Methodology and implementation</h3>
        <p>Design an approach, implement it properly, and build experiments that could actually disconfirm your hypothesis.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">4</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Rigorous experimentation</h3>
        <p>Baselines, ablations, statistical care, and honest negative results. This is where most of the real work happens.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">5</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Writing and submission</h3>
        <p>Work toward first-author papers at strong international venues, with detailed feedback on argument and presentation. We support you through submission and rebuttal; no one can promise acceptance.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">6</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Thesis and independence</h3>
        <p>Assemble a coherent body of work into a dissertation, and prepare for the next stage — academic, industrial research, or your own direction.</p>
      </div>
    </li>
  </ol>
</div>

{% include section.html %}

<!-- ================= APPLICATION MATERIALS ================= -->
<div class="team-section" id="application-materials">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-folder-open"></i></span>
    <h2 class="team-section-title">Application Materials</h2>
  </div>

  <h3>Required</h3>
  <ul class="join-list">
    <li><i class="fa-solid fa-check"></i><span><strong>Curriculum vitae</strong>, including your education, research experience, and technical skills.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Academic transcript</strong> with GPA.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Intended program</strong> — M.S./Ph.D. Combined or Ph.D.</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>Intended admission semester.</strong></span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>A short research-interest statement</strong> (roughly one page — see below).</span></li>
    <li><i class="fa-solid fa-check"></i><span><strong>A concise explanation of why InfoLab specifically</strong>, rather than any lab working on AI.</span></li>
  </ul>

  <h3>What your research statement should cover</h3>
  <ul class="join-list">
    <li><i class="fa-solid fa-check"></i><span>Your previous academic, research, or industrial experience — and what <em>you</em> personally contributed.</span></li>
    <li><i class="fa-solid fa-check"></i><span>The research topics you want to pursue, stated concretely.</span></li>
    <li><i class="fa-solid fa-check"></i><span>Why those topics align with InfoLab's current work.</span></li>
    <li><i class="fa-solid fa-check"></i><span>The technical skills you would bring on day one.</span></li>
    <li><i class="fa-solid fa-check"></i><span>Your evidence of research potential, in whatever form it takes.</span></li>
  </ul>

  <div class="join-callout">
    <i class="fa-solid fa-circle-exclamation"></i>
    <p><strong>Name 1–3 specific InfoLab papers, projects, or research topics</strong> that connect to your interests, and explain
    the connection in a few sentences each. This single requirement is the clearest signal we receive. Applications that could
    have been sent unchanged to fifty other laboratories are unlikely to receive a reply.</p>
  </div>

  <h3>Optional, and strongly recommended where available</h3>
  <ul class="join-list">
    <li><i class="fa-solid fa-check"></i><span>Google Scholar profile, publications, or preprints.</span></li>
    <li><i class="fa-solid fa-check"></i><span>GitHub, open-source contributions, or a technical portfolio.</span></li>
    <li><i class="fa-solid fa-check"></i><span>Personal or research website.</span></li>
    <li><i class="fa-solid fa-check"></i><span>Undergraduate or master's thesis, or substantial research reports.</span></li>
    <li><i class="fa-solid fa-check"></i><span>Evidence of industrial R&amp;D work, where shareable.</span></li>
  </ul>
</div>

{% include section.html %}

<!-- ================= SELECTION PROCESS ================= -->
<div class="team-section" id="selection-process">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-list-check"></i></span>
    <h2 class="team-section-title">Selection Process</h2>
  </div>
  <ol class="join-steps">
    <li class="join-step">
      <span class="join-step-num">1</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Application screening</h3>
        <p>We review your CV, transcript, research statement, and supporting evidence.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">2</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Research-fit evaluation</h3>
        <p>We assess how your interests and preparation map onto active research directions and available supervision capacity.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">3</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Interview</h3>
        <p>A discussion with Prof. Abuhmed, typically online for international applicants, covering your background and research interests.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">4</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Technical or research discussion</h3>
        <p>Where appropriate, a deeper technical conversation or a small research task related to your stated interests.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">5</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Research internship — only when useful</h3>
        <p>For some candidates we may suggest an internship period first, as a mutual evaluation. <strong>This step is optional.</strong> Applicants with demonstrated academic or industrial research experience routinely proceed directly to admission without it.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">6</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Official graduate admission</h3>
        <p>Successful candidates apply through the <a href="https://admission-global.skku.edu/eng/index.html" target="_blank" rel="noopener noreferrer">SKKU Graduate School</a> and must satisfy the university's official admission requirements. Support from the lab does not replace or bypass that process — check the official pages for current requirements, documents, and deadlines.</p>
      </div>
    </li>
  </ol>
</div>

{% include section.html %}

<!-- ================= OTHER OPPORTUNITIES ================= -->
<div class="team-section" id="other-opportunities">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-door-open"></i></span>
    <h2 class="team-section-title">Other Opportunities</h2>
  </div>
  <div class="join-grid">
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-lightbulb"></i></span>
      <h3 class="join-card-title">Research Interns</h3>
      <p class="join-card-desc">Undergraduate and visiting internships for students who want hands-on research experience — whether or not they later apply to our graduate programs. Also the natural route for candidates following Path A above.</p>
    </div>
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-flask"></i></span>
      <h3 class="join-card-title">Postdoctoral Researchers</h3>
      <p class="join-card-desc">Openings depend on active grants. A strong publication record in security, machine learning, or biomedical AI is expected. Enquire with a CV and a short statement of your research direction.</p>
    </div>
    <div class="join-card">
      <span class="join-card-icon"><i class="fa-solid fa-code"></i></span>
      <h3 class="join-card-title">Research Developers</h3>
      <p class="join-card-desc">Engineering-focused roles building the systems, datasets, and tooling behind our research projects.</p>
    </div>
  </div>
</div>

{% include section.html %}

<!-- ============================== FAQ ============================== -->
<div class="team-section" id="faq">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-circle-question"></i></span>
    <h2 class="team-section-title">Frequently Asked Questions</h2>
  </div>

  <h3>Are M.S.-only positions available?</h3>
  <p>No. Standalone M.S. positions are not available at this time. We are recruiting for the M.S./Ph.D. Combined and Ph.D. programs only.</p>

  <h3>Which graduate programs are currently recruiting?</h3>
  <p><strong>M.S./Ph.D. Combined</strong> and <strong>Ph.D.</strong></p>

  <h3>Are the positions funded?</h3>
  <p>Yes. Graduate researchers in these programs receive a <strong>full tuition fee waiver</strong> and a <strong>monthly stipend</strong>, together with research computing resources, mentorship, and support for publication-oriented work.</p>

  <h3>Is an InfoLab internship mandatory?</h3>
  <p>No. An internship is <strong>preferred in some cases but not required</strong>. It is most useful for candidates with limited formal research experience, or for anyone who wants to evaluate research fit before committing.</p>

  <h3>Can I apply directly without an InfoLab internship?</h3>
  <p>Yes — particularly if you can demonstrate prior academic research experience or relevant industrial research and development experience. See <a href="#two-paths">Path B</a> above.</p>

  <h3>Do I need publications to apply?</h3>
  <p>No. Publications are strong evidence of research ability and are genuinely valued, but they are not the only way to demonstrate research potential. A thesis, a research assistantship, industrial R&amp;D work, technical reports, or serious reproducible open-source research can all serve as evidence.</p>

  <h3>Can international students apply?</h3>
  <p>Yes. InfoLab is an international research group and international applicants are explicitly welcome — our current researchers come from many countries. Applications are handled through SKKU's international graduate admissions.</p>

  <h3>Do I need to speak Korean?</h3>
  <p>Research and publication in the lab are conducted in English, and Korean proficiency is not required to do research with us. Formal language requirements for admission are set by the university, not the lab — check the <a href="https://admission-global.skku.edu/eng/index.html" target="_blank" rel="noopener noreferrer">SKKU Graduate School admissions</a> pages for the requirements that apply to your program and nationality.</p>

  <h3>When should I apply?</h3>
  <p>Contact the lab well in advance of the SKKU Graduate School application deadline for your intended semester — several months ahead is sensible, since research-fit evaluation and any interview take time. Official deadlines and document requirements are published by the university, so check the admissions pages for current dates.</p>

  <h3>Can undergraduate students apply for internships?</h3>
  <p>Yes. Research internships are open to undergraduate and visiting students, and are a separate track from graduate recruitment. An internship is not an admission decision, and admission does not require one — but for some candidates it is a useful step toward it.</p>

  <h3>What if my background is unconventional?</h3>
  <p>Tell us about it. We care about demonstrated research ability and fit with our research directions. Candidates from industry, from adjacent disciplines, or with non-linear academic histories are assessed on the same basis as anyone else.</p>
</div>

{% include section.html %}

<!-- ========================= CALL TO ACTION ========================= -->
<div class="team-section" id="how-to-apply">
  <div class="team-section-header">
    <span class="team-section-icon"><i class="fa-solid fa-paper-plane"></i></span>
    <h2 class="team-section-title">Apply</h2>
  </div>

  <p class="team-intro">If you have read this far and the research areas genuinely match what you want to work on, we would like to
  hear from you.</p>

  <ol class="join-steps">
    <li class="join-step">
      <span class="join-step-num">1</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Read our research first</h3>
        <p>Go through our <a href="/projects/">projects</a> and <a href="/pubs/">publications</a>, and pick the 1–3 papers or topics closest to your interests.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">2</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Prepare your materials</h3>
        <p>CV, transcript, research-interest statement, intended program and semester, and any evidence of research or R&amp;D experience — as listed under <a href="#application-materials">Application Materials</a>.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">3</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Email Prof. Tamer Abuhmed</h3>
        <p>Send everything in a single email, with the subject line:</p>
        <p><strong>[Graduate Application] Ph.D. — Your Name</strong><br>
        or <strong>[Graduate Application] MS/PhD Combined — Your Name</strong></p>
        <p>For internships, use <strong>[Internship Application] — Your Name</strong>. A clear subject line means your message is
        read as an application rather than filtered as an enquiry.</p>
      </div>
    </li>
    <li class="join-step">
      <span class="join-step-num">4</span>
      <div class="join-step-body">
        <h3 class="join-step-title">Apply to the Graduate School</h3>
        <p>Successful candidates then apply through <a href="https://admission-global.skku.edu/eng/index.html" target="_blank" rel="noopener noreferrer">SKKU Graduate School admissions</a>, naming InfoLab and Prof. Abuhmed in the application.</p>
      </div>
    </li>
  </ol>

  {% include button.html type="email" link="tamer@skku.edu" text="Email Prof. Abuhmed" %}
  {% include button.html icon="fa-solid fa-address-book" text="Contact Page" link="/contact" style="bare" %}
</div>
