---
title: Multimodal, Explainable, and Adversarially-Robust Deep Learning for Alzheimer’s Disease Progression Detection
---

{% include breadcrumbs.html %}
# {% include icon.html icon="fa-solid fa-brain" %} Multimodal, Explainable, and Adversarially-Robust Deep Learning for Alzheimer’s Disease Progression Detection

## Project Description

Alzheimer’s disease (AD) is a **progressive neurodegenerative disorder** with no known cure. Accurate early prediction of its progression—from **cognitively normal (CN)** and **mild cognitive impairment (MCI)** to **full AD**—is essential for enabling timely clinical intervention.

Traditional diagnostic models, often reliant on a **single modality** or **snapshot observations**, fall short due to the disease’s **heterogeneous and longitudinal nature**. To address these challenges, **InfoLab at Sungkyunkwan University (SKKU)** launched a research initiative combining:

- **Multimodal data fusion**
- **Deep and time-aware learning**
- **Visual explainability (XAI)**
- **Adversarial robustness evaluation**

The goal is to develop **robust, interpretable, and clinically deployable AI systems** for AD progression detection.

---

## Core Research Contributions

### 1. Multimodal and Cost-Effective Early Detection

We developed **cost-efficient ML models** using non-invasive, longitudinal data sources:

- **Cognitive scores:** MMSE, ADAS, CDRSB, FAQ  
- **Demographics**
- **Medication/comorbidity history** (encoded using **ATC ontology**)

Models trained on time-series records across **2.5 years** achieved strong performance in 4-class classification (CN, sMCI, pMCI, AD), with **Random Forests** outperforming others—even **without neuroimaging data**.

---

### 2. Multimodal Multitask Deep Learning with Temporal Awareness

We proposed hybrid deep learning architectures combining **CNNs + BiLSTMs** to model **spatial-temporal dependencies** in longitudinal health records.

These models jointly:

- **Classify patient stage** (CN, MCI, AD)
- **Regress cognitive scores** (e.g., MMSE) for fine-grained assessment

This **multitask learning strategy** improved accuracy and robustness on the **ADNI dataset**, surpassing single-modality models.

---

### 3. Explainable and Visual Deep Learning for Medical Trust

To improve **clinical trust and transparency**, we implemented a **temporal visual XAI module** using **guided Grad-CAM** over **longitudinal 3D MRI scans**.

Key Features:

- **Voxel-level explanations** highlighting brain region activity over time
- Tracks **structural brain changes** contributing to predictions
- Enhances **clinician validation** of model outcomes

---

### 4. Adversarial Robustness in Predictive Frameworks

Medical AI systems must remain robust under **input distortion** and **adversarial conditions**. We investigated:

- Effects of **data perturbation**, **missing features**, and **input tampering**
- Resilience improvements via **multimodal fusion** and **multitask training**

Our findings showed that fused inputs and shared learning goals help stabilize performance even under **realistic attack scenarios**.

---

## Project Objectives

- Develop **clinically acceptable** deep learning systems for AD progression detection using **multimodal, time-series data**
- Build models that are **interpretable**, **transparent**, and compliant with **regulatory guidelines**
- Ensure **adversarial resilience** and consistent performance under imperfect data conditions
- Optimize for **real-world deployment**, particularly in **resource-constrained** medical settings
- Release datasets, interpretable modules, and evaluation frameworks to **support reproducibility and collaboration**

---

## Research Impact

This project bridges the gap between **cutting-edge AI** and **clinical utility** in the diagnosis of **neurodegenerative diseases**. By integrating:

- **Early fusion of multimodal inputs**
- **Temporal deep learning**
- **Adversarial threat modeling**
- **Visual explanation modules**

The research from **InfoLab (SKKU)** sets a new benchmark for **trustworthy, transparent, and deployable AI systems** in medical diagnostics.
