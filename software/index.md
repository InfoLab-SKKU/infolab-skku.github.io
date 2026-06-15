---
title: Software & Datasets
nav:
  order: 6
  tooltip: Open-source code and datasets from InfoLab
---

<!-- HERO -->
<div class="team-hero sw-hero">
  <div class="team-hero-content">
    <div class="team-hero-badge">Open Source</div>
    <h1 class="team-hero-title">Software &amp; Datasets</h1>
    <p class="team-hero-sub">Open-source tools, libraries, and datasets from InfoLab research — freely available for the research community.</p>
    <div class="team-hero-stats">
      <div class="team-hstat">
        <span class="team-hstat-num">21</span>
        <span class="team-hstat-lbl">Repositories</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">2</span>
        <span class="team-hstat-lbl">pip Libraries</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <span class="team-hstat-num">5</span>
        <span class="team-hstat-lbl">Research Areas</span>
      </div>
      <div class="team-hstat-sep"></div>
      <div class="team-hstat">
        <a href="https://github.com/InfoLab-SKKU" target="_blank" rel="noopener noreferrer" class="team-hstat-link">
          <span class="team-hstat-num"><i class="fa-brands fa-github"></i></span>
          <span class="team-hstat-lbl">InfoLab-SKKU</span>
        </a>
      </div>
    </div>
  </div>
</div>

{% include section.html %}

<!-- CATEGORY FILTER -->
<div class="sw-filter-bar">
  <button class="sw-filter-btn active" data-cat="all">
    <i class="fa-solid fa-layer-group"></i> All
    <span class="sw-filter-count">21</span>
  </button>
  <button class="sw-filter-btn" data-cat="security">
    <i class="fa-solid fa-shield-halved"></i> Security &amp; Adversarial ML
    <span class="sw-filter-count">6</span>
  </button>
  <button class="sw-filter-btn" data-cat="federated">
    <i class="fa-solid fa-network-wired"></i> Federated Learning
    <span class="sw-filter-count">2</span>
  </button>
  <button class="sw-filter-btn" data-cat="biomedical">
    <i class="fa-solid fa-heart-pulse"></i> Biomedical AI
    <span class="sw-filter-count">8</span>
  </button>
  <button class="sw-filter-btn" data-cat="library">
    <i class="fa-solid fa-cube"></i> XAI &amp; Libraries
    <span class="sw-filter-count">3</span>
  </button>
  <button class="sw-filter-btn" data-cat="vision">
    <i class="fa-solid fa-camera"></i> Human Activity
    <span class="sw-filter-count">2</span>
  </button>
</div>

<!-- REPO GRID -->
<div class="sw-repo-grid">

  <!-- SECURITY & ADVERSARIAL ML -->

  <div class="sw-repo-card" data-cat="security">
    <div class="sw-card-accent sw-accent--security"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--security"><i class="fa-solid fa-eye-slash"></i></div>
        <div>
          <div class="sw-card-name">AdvEdge / AdvEdge+</div>
          <div class="sw-card-repo">InfoLab-SKKU/AdvEdge-Attack</div>
        </div>
      </div>
      <p class="sw-card-desc">Introduces two white-box adversarial attacks that simultaneously fool a DNN classifier <em>and</em> its coupled interpretation model (GradCAM, LIME, SHAP). Demonstrates that interpretable deep learning systems are vulnerable to adversarial inputs designed to produce misleading yet visually plausible explanations.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Adversarial Attack</span>
        <span class="sw-tag">XAI</span>
        <span class="sw-tag">ImageNet</span>
        <span class="sw-tag">PyTorch</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE TDSC 2024</span>
        <a href="https://github.com/InfoLab-SKKU/AdvEdge-Attack" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="library">
    <div class="sw-card-accent sw-accent--library"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--library"><i class="fa-solid fa-star"></i></div>
        <div>
          <div class="sw-card-name">Awesome Dynamic Ensemble Learning</div>
          <div class="sw-card-repo">InfoLab-SKKU/awesome-dynamic-ensemble-learning</div>
        </div>
      </div>
      <p class="sw-card-desc">A curated list of resources, libraries, and papers about Dynamic Ensemble Selection (DES), Dynamic Ensemble Learning, and related explainable ensemble methods. Includes implementations, benchmarks, and reading lists to help researchers and practitioners explore the field.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Awesome List</span>
        <span class="sw-tag">Dynamic Ensemble</span>
        <span class="sw-tag">Survey</span>
        <span class="sw-tag">Resources</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/awesome-dynamic-ensemble-learning" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="vision">
    <div class="sw-card-accent sw-accent--vision"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--vision"><i class="fa-solid fa-eye"></i></div>
        <div>
          <div class="sw-card-name">VisionDES</div>
          <div class="sw-card-repo">InfoLab-SKKU/VisionDES</div>
        </div>
      </div>
      <p class="sw-card-desc">VisionDES provides dynamic ensemble selection methods tailored for computer vision tasks. Includes training and evaluation scripts, pretrained models, and integration examples for image classification benchmarks using dynamic ensemble strategies.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Dynamic Ensemble</span>
        <span class="sw-tag">Vision</span>
        <span class="sw-tag">PyTorch</span>
        <span class="sw-tag">ImageNet</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/VisionDES" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="security">
    <div class="sw-card-accent sw-accent--security"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--security"><i class="fa-solid fa-crosshairs"></i></div>
        <div>
          <div class="sw-card-name">SingleADV</div>
          <div class="sw-card-repo">InfoLab-SKKU/SingleClassADV</div>
        </div>
      </div>
      <p class="sw-card-desc">SingleADV generates a universal perturbation targeting an entire category of objects, fooling both the DNN prediction model and its interpretation model simultaneously in white-box and black-box settings. Limits unintended cross-class fooling for targeted stealth.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Universal Perturbation</span>
        <span class="sw-tag">Black-box</span>
        <span class="sw-tag">ImageNet</span>
        <span class="sw-tag">CAM</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE TIFS 2024</span>
        <a href="https://github.com/InfoLab-SKKU/SingleClassADV" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="security">
    <div class="sw-card-accent sw-accent--security"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--security"><i class="fa-solid fa-robot"></i></div>
        <div>
          <div class="sw-card-name">AdViT</div>
          <div class="sw-card-repo">InfoLab-SKKU/AdViT</div>
        </div>
      </div>
      <p class="sw-card-desc">Adversarial attack framework targeting interpretable Vision Transformers. Attacks the Transformer Interpreter explanation model, generating adversarial samples whose attribution maps closely resemble those of benign examples. Supports DeiT-B as source model and ViT-B as target.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Vision Transformer</span>
        <span class="sw-tag">ViT Attack</span>
        <span class="sw-tag">DeiT</span>
        <span class="sw-tag">XAI</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/AdViT" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="security">
    <div class="sw-card-accent sw-accent--security"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--security"><i class="fa-solid fa-magnifying-glass-chart"></i></div>
        <div>
          <div class="sw-card-name">QuScore</div>
          <div class="sw-card-repo">InfoLab-SKKU/QuScore</div>
        </div>
      </div>
      <p class="sw-card-desc">A stealthy, query-efficient score-based black-box attack against interpretable deep learning systems using a microbial genetic algorithm. Achieves 95&ndash;100% attack success rate on Inception, ResNet, VGG, and DenseNet across ImageNet and CIFAR with minimal queries. Resilient against JPEG, bit-depth reduction, and median smoothing defenses.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Black-box Attack</span>
        <span class="sw-tag">Query-Efficient</span>
        <span class="sw-tag">Genetic Algorithm</span>
        <span class="sw-tag">ImageNet</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE Trans. Reliability 2025</span>
        <a href="https://github.com/InfoLab-SKKU/QuScore" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="security">
    <div class="sw-card-accent sw-accent--security"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--security"><i class="fa-solid fa-flask"></i></div>
        <div>
          <div class="sw-card-name">Black-Box Attacks Analysis</div>
          <div class="sw-card-repo">InfoLab-SKKU/black-box-attacks</div>
        </div>
      </div>
      <p class="sw-card-desc">Empirical study of three black-box attacks — SimBA, HopSkipJump, BoundaryAttack — across CNN architectures (ResNet, VGG, DenseNet) on ImageNet and CIFAR-100. Investigates model complexity vs. robustness, model diversity, cross-dataset transferability, and preprocessing-based defenses (JPEG, median smoothing, bit squeezing).</p>
      <div class="sw-card-tags">
        <span class="sw-tag">SimBA</span>
        <span class="sw-tag">HopSkipJump</span>
        <span class="sw-tag">BoundaryAttack</span>
        <span class="sw-tag">Defense</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE SVCC 2024</span>
        <a href="https://github.com/InfoLab-SKKU/black-box-attacks" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="security">
    <div class="sw-card-accent sw-accent--security"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--security"><i class="fa-solid fa-chart-bar"></i></div>
        <div>
          <div class="sw-card-name">Adversarial Attacks Analysis</div>
          <div class="sw-card-repo">InfoLab-SKKU/Adversarial-Attacks-Analysis</div>
        </div>
      </div>
      <p class="sw-card-desc">Multi-dimensional study of DNN robustness examining model complexity vs. adversarial robustness, diversity effects of heterogeneous model ensembles, cross-dataset attack transferability (ImageNet, CIFAR-100), and effectiveness of preprocessing-based defenses across diverse architectures.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Robustness</span>
        <span class="sw-tag">Model Diversity</span>
        <span class="sw-tag">Transferability</span>
        <span class="sw-tag">Defense</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE SVCC 2024</span>
        <a href="https://github.com/InfoLab-SKKU/Adversarial-Attacks-Analysis" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <!-- FEDERATED LEARNING -->

  <div class="sw-repo-card" data-cat="federated">
    <div class="sw-card-accent sw-accent--federated"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--federated"><i class="fa-solid fa-server"></i></div>
        <div>
          <div class="sw-card-name">HARFed</div>
          <div class="sw-card-repo">InfoLab-SKKU/harfed</div>
        </div>
      </div>
      <p class="sw-card-desc">A Streamlit-based simulator for federated learning experiments focused on heterogeneity, attacks, and robustness. Supports Dirichlet and IID partitioning, FedAvg/FedMedian/FedProx strategies, configurable adversarial clients, local differential privacy, and real-time GPU monitoring with accuracy and attack success rate plots exportable as PNG/PDF.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Federated Learning</span>
        <span class="sw-tag">Streamlit</span>
        <span class="sw-tag">FedAvg</span>
        <span class="sw-tag">Differential Privacy</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/harfed" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="federated">
    <div class="sw-card-accent sw-accent--federated"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--federated"><i class="fa-solid fa-shield-virus"></i></div>
        <div>
          <div class="sw-card-name">SecurityAnalysisFL</div>
          <div class="sw-card-repo">InfoLab-SKKU/SecurityAnalysisFL</div>
        </div>
      </div>
      <p class="sw-card-desc">Investigates data-poisoning attacks against federated learning under heterogeneous client data distributions. Uses PyTorch and the Flower framework to simulate distributed MobileNetV2 training. Evaluates attack robustness with local differential privacy and studies the interplay between data heterogeneity and model vulnerability.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Poisoning Attacks</span>
        <span class="sw-tag">Flower</span>
        <span class="sw-tag">MobileNetV2</span>
        <span class="sw-tag">LDP</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE IMCOM 2025</span>
        <a href="https://github.com/InfoLab-SKKU/SecurityAnalysisFL" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <!-- BIOMEDICAL AI -->

  <div class="sw-repo-card" data-cat="biomedical">
    <div class="sw-card-accent sw-accent--biomedical"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--biomedical"><i class="fa-solid fa-brain"></i></div>
        <div>
          <div class="sw-card-name">4DfCF &mdash; 4D fMRI CrossFormer</div>
          <div class="sw-card-repo">InfoLab-SKKU/4DfCF</div>
        </div>
      </div>
      <p class="sw-card-desc">Novel vision transformer with cross-scale embeddings and hierarchical 4D short/long-distance attention for spatiotemporal brain disorder classification from 4D fMRI. Evaluated on ADHD-200, ADNI (Alzheimer&apos;s), and ABIDE (Autism), consistently outperforming 3D-CNN and SwiFT baselines. Integrated Gradients XAI maps highlight disorder-relevant brain regions.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">4D fMRI</span>
        <span class="sw-tag">Vision Transformer</span>
        <span class="sw-tag">ADHD-200 &bull; ADNI &bull; ABIDE</span>
        <span class="sw-tag">XAI</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE JBHI 2025</span>
        <a href="https://github.com/InfoLab-SKKU/4DfCF" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="biomedical">
    <div class="sw-card-accent sw-accent--biomedical"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--biomedical"><i class="fa-solid fa-timeline"></i></div>
        <div>
          <div class="sw-card-name">5DfCF &mdash; 5D fMRI CrossFormer</div>
          <div class="sw-card-repo">InfoLab-SKKU/5DfCF</div>
        </div>
      </div>
      <p class="sw-card-desc">Extends spatiotemporal fMRI modeling to longitudinal (multi-session) data with a Period CrossFormer Block that fuses intra-session 4D attention with inter-session dynamics using period-aware positional embeddings. Achieves <strong>94.3% accuracy</strong> and <strong>94.1% AUC</strong> on ADNI MCI-to-dementia conversion, outperforming all baselines by 3&ndash;10 points.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Longitudinal fMRI</span>
        <span class="sw-tag">Alzheimer&apos;s Progression</span>
        <span class="sw-tag">MCI Conversion</span>
        <span class="sw-tag">ADNI</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/5DfCF" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="biomedical">
    <div class="sw-card-accent sw-accent--biomedical"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--biomedical"><i class="fa-solid fa-cubes"></i></div>
        <div>
          <div class="sw-card-name">MML-3DCrossFormer</div>
          <div class="sw-card-repo">InfoLab-SKKU/MML-3DCrossFormer</div>
        </div>
      </div>
      <p class="sw-card-desc">3D MRI CrossFormer with multimodal intermediate fusion of volumetric MRI embeddings (via 3D-LDA/SDA dual-range attention) and structured clinical data (MMSE, CDR-SB, ADAS13). Achieves <strong>99.3% accuracy</strong> and <strong>99.7% AUC</strong> on ADNI Alzheimer&apos;s diagnosis. Guided Grad-CAM highlights the hippocampus, entorhinal cortex, and medial temporal lobe.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">3D MRI</span>
        <span class="sw-tag">Multimodal Fusion</span>
        <span class="sw-tag">Alzheimer&apos;s</span>
        <span class="sw-tag">Grad-CAM</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/MML-3DCrossFormer" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="biomedical">
    <div class="sw-card-accent sw-accent--biomedical"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--biomedical"><i class="fa-solid fa-child-reaching"></i></div>
        <div>
          <div class="sw-card-name">4DViTADHD</div>
          <div class="sw-card-repo">InfoLab-SKKU/4DViTADHD</div>
        </div>
      </div>
      <p class="sw-card-desc">Multimodal framework combining a 4D Vision Transformer for high-dimensional fMRI with an MLP for clinical and demographic tabular data (age, gender, IQ, behavioral scores) for ADHD diagnosis on ADHD-200. Compares intermediate and decision fusion strategies. SHAP and Integrated Gradients provide interpretability across both modalities.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">ADHD</span>
        <span class="sw-tag">fMRI + Tabular</span>
        <span class="sw-tag">Multimodal Fusion</span>
        <span class="sw-tag">SHAP</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/4DViTADHD" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="biomedical">
    <div class="sw-card-accent sw-accent--biomedical"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--biomedical"><i class="fa-solid fa-layer-group"></i></div>
        <div>
          <div class="sw-card-name">MPMS MRI Progression</div>
          <div class="sw-card-repo">InfoLab-SKKU/mpms-mri-progression</div>
        </div>
      </div>
      <p class="sw-card-desc">Multi-plane, multi-slice longitudinal MRI deep ensemble for Alzheimer&apos;s progression detection. Keras-based with pluggable CNN backbones (EfficientNet, ResNet, ConvNext, DenseNet, XceptionNet), optional CBAM attention, and Bayesian-optimized classification heads (MLP, LSTM, multi-head self-attention). Run via command-line with flexible configuration flags.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Longitudinal MRI</span>
        <span class="sw-tag">Keras</span>
        <span class="sw-tag">CBAM</span>
        <span class="sw-tag">Bayesian Optimization</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/mpms-mri-progression" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="biomedical">
    <div class="sw-card-accent sw-accent--biomedical"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--biomedical"><i class="fa-solid fa-wave-square"></i></div>
        <div>
          <div class="sw-card-name">AD Progression Detection (MRI)</div>
          <div class="sw-card-repo">InfoLab-SKKU/AD-progression-detection-MRI</div>
        </div>
      </div>
      <p class="sw-card-desc">3D-CNN-BRNN framework for Alzheimer&apos;s progression from multi-timestep longitudinal MRI. A 3D-CNN extracts deep volumetric features; a Bidirectional RNN models temporal dynamics across visits. Visual XAI highlights spatiotemporal brain regions most predictive of progression. Tested at baseline, 6-month, and 12-month ADNI timepoints.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">3D-CNN</span>
        <span class="sw-tag">Bidirectional RNN</span>
        <span class="sw-tag">Longitudinal MRI</span>
        <span class="sw-tag">XAI</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--elsevier">Information Fusion 2023</span>
        <a href="https://github.com/InfoLab-SKKU/AD-progression-detection-MRI" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="biomedical">
    <div class="sw-card-accent sw-accent--biomedical"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--biomedical"><i class="fa-solid fa-face-sad-tear"></i></div>
        <div>
          <div class="sw-card-name">DES4Depression</div>
          <div class="sw-card-repo">InfoLab-SKKU/DES4Depression</div>
        </div>
      </div>
      <p class="sw-card-desc">Two-stage dynamic ensemble framework for depression detection and severity prediction using NSHAP data. Stage 1 detects depression (FIRE-KNOP DES: <strong>88.33% accuracy</strong>); Stage 2 predicts severity among depressed patients (<strong>83.68%</strong>). SHAP and feature network diagrams provide clinical explainability for older-adult populations.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Depression</span>
        <span class="sw-tag">Dynamic Ensemble</span>
        <span class="sw-tag">NSHAP</span>
        <span class="sw-tag">SHAP</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--mdpi">Diagnostics 2024</span>
        <a href="https://github.com/InfoLab-SKKU/DES4Depression" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="biomedical">
    <div class="sw-card-accent sw-accent--biomedical"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--biomedical"><i class="fa-solid fa-syringe"></i></div>
        <div>
          <div class="sw-card-name">Explainable Ensemble Hypoglycemia</div>
          <div class="sw-card-repo">InfoLab-SKKU/Explainable-Ensemble-Hypoglycemia</div>
        </div>
      </div>
      <p class="sw-card-desc">Predicts severe hypoglycemic episodes in Type-1 Diabetes using multimodal data (clinical, psychological, cognitive features) with early and late fusion strategies. Benchmarks classical ML, static ensembles, and Dynamic Ensemble Selection. Best results: <strong>AUC-ROC 0.877</strong> (late fusion) and <strong>accuracy 0.798</strong> (early fusion). Dataset from Jaeb Center for Health Research.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Type-1 Diabetes</span>
        <span class="sw-tag">Hypoglycemia</span>
        <span class="sw-tag">Multimodal Fusion</span>
        <span class="sw-tag">DES</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/Explainable-Ensemble-Hypoglycemia" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <!-- XAI & LIBRARIES -->

  <div class="sw-repo-card" data-cat="library">
    <div class="sw-card-accent sw-accent--library"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--library"><i class="fa-solid fa-box-open"></i></div>
        <div>
          <div class="sw-card-name">Infodeslib</div>
          <div class="sw-card-repo">InfoLab-SKKU/infodeslib</div>
        </div>
      </div>
      <div class="sw-pip-badge"><i class="fa-brands fa-python"></i> pip install infodeslib</div>
      <p class="sw-card-desc">Open-source Python library for Dynamic Ensemble Selection with late fusion of multimodal data and integrated SHAP-based explainability. Implements 4 dynamic classifier selection and 7 DES techniques. Each model in the pool can train on different feature sets (modalities), and the <code>predict()</code> call handles competence estimation, selection, and explanation in one step.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Python Library</span>
        <span class="sw-tag">Dynamic Ensemble</span>
        <span class="sw-tag">Late Fusion</span>
        <span class="sw-tag">SHAP</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--acm">KDD KiL Workshop 2024</span>
        <a href="https://github.com/InfoLab-SKKU/infodeslib" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="library">
    <div class="sw-card-accent sw-accent--library"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--library"><i class="fa-solid fa-chart-line"></i></div>
        <div>
          <div class="sw-card-name">XAI-DESReg</div>
          <div class="sw-card-repo">InfoLab-SKKU/xaidesreg</div>
        </div>
      </div>
      <div class="sw-pip-badge"><i class="fa-brands fa-python"></i> pip install xaidesreg</div>
      <p class="sw-card-desc">Dynamic Ensemble Selection for regression with built-in explainability. Selects the most competent regressors per query using k-NN region-of-competence modeling. The <code>predict_xai()</code> method returns per-model predictions, competence scores, and the neighbor samples in the region of competence &mdash; making ensemble decisions fully transparent. Compatible with any scikit-learn regressor.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Python Library</span>
        <span class="sw-tag">Regression</span>
        <span class="sw-tag">Dynamic Ensemble</span>
        <span class="sw-tag">XAI</span>
      </div>
      <div class="sw-card-footer">
        <a href="https://github.com/InfoLab-SKKU/xaidesreg" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="library">
    <div class="sw-card-accent sw-accent--library"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--library"><i class="fa-solid fa-diagram-project"></i></div>
        <div>
          <div class="sw-card-name">MM-DES</div>
          <div class="sw-card-repo">InfoLab-SKKU/mm-des</div>
        </div>
      </div>
      <p class="sw-card-desc">Multimodal clinical prediction framework combining joint contrastive embeddings across image, clinical text, and tabular modalities with Dynamic Ensemble Selection. Region-of-Competence modeling adapts ensemble composition per query. Built-in XAI explains which modality and which classifiers contributed to each decision. Robust to noisy and heterogeneous clinical datasets.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Multimodal</span>
        <span class="sw-tag">Contrastive Learning</span>
        <span class="sw-tag">Dynamic Ensemble</span>
        <span class="sw-tag">Clinical AI</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--springer">ICPR 2026</span>
        <a href="https://github.com/InfoLab-SKKU/mm-des" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <!-- HUMAN ACTIVITY -->

  <div class="sw-repo-card" data-cat="vision">
    <div class="sw-card-accent sw-accent--vision"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--vision"><i class="fa-solid fa-person-walking"></i></div>
        <div>
          <div class="sw-card-name">Low-Cost Human Activity Detection</div>
          <div class="sw-card-repo">InfoLab-SKKU/Low-Cost-Human-Activity-Detection</div>
        </div>
      </div>
      <p class="sw-card-desc">Real-time human detection and activity recognition using the MLX90640 low-resolution infrared sensor (32&times;24 pixels). Demonstrates that reliable activity detection is achievable with accessible, low-cost thermal hardware without high-resolution cameras. Includes the thermal image dataset repository for replication and benchmarking.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Thermal Imaging</span>
        <span class="sw-tag">MLX90640</span>
        <span class="sw-tag">Real-time</span>
        <span class="sw-tag">Activity Recognition</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE IMCOM 2023</span>
        <a href="https://github.com/InfoLab-SKKU/Low-Cost-Human-Activity-Detection" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

  <div class="sw-repo-card" data-cat="vision">
    <div class="sw-card-accent sw-accent--vision"></div>
    <div class="sw-card-body">
      <div class="sw-card-top">
        <div class="sw-card-icon sw-icon--vision"><i class="fa-solid fa-database"></i></div>
        <div>
          <div class="sw-card-name">Thermal Human Detection Dataset</div>
          <div class="sw-card-repo">InfoLab-SKKU/Thermal-Human-Detection</div>
        </div>
      </div>
      <div class="sw-dataset-badge"><i class="fa-solid fa-table"></i> Dataset</div>
      <p class="sw-card-desc">Low-resolution infrared thermal image dataset collected with the MLX90640 sensor (32&times;24 IR resolution). Captures human presence and activity patterns across standardized scenarios. Accompanies the low-cost human activity detection paper and provides a benchmark for embedded thermal imaging and edge-deployed detection systems.</p>
      <div class="sw-card-tags">
        <span class="sw-tag">Dataset</span>
        <span class="sw-tag">Thermal IR</span>
        <span class="sw-tag">32&times;24 px</span>
        <span class="sw-tag">Human Detection</span>
      </div>
      <div class="sw-card-footer">
        <span class="sw-paper-badge sw-badge--ieee">IEEE IMCOM 2023</span>
        <a href="https://github.com/InfoLab-SKKU/Thermal-Human-Detection" target="_blank" rel="noopener" class="sw-gh-btn"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>
  </div>

</div>

{% include section.html %}

## {% include icon.html icon="fa-solid fa-circle-info" %} Using Our Work

If you use any InfoLab code or datasets in your research, please cite the corresponding paper. BibTeX entries are available on the [Publications](/pubs/) page via the **Cite** button on each paper card.

For questions, collaborations, or data access requests, [contact us](/contact/).