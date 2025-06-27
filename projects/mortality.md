---
title: Explainable and Dynamic Ensemble Models for ICU Mortality and Length-of-Stay Prediction
---

{% include breadcrumbs.html %}
# {% include icon.html icon="fa-solid fa-heart-pulse" %} Explainable and Dynamic Ensemble Models for ICU Mortality and Length-of-Stay Prediction

## Project Description

Predicting outcomes in **Intensive Care Units (ICUs)**—such as **mortality risk** and **length of stay (LOS)**—is crucial for improving care quality, reducing hospital strain, and optimizing resource use. Traditional scoring methods and classical ML approaches often struggle with the complexity, high dimensionality, and heterogeneity of ICU data.

To address these gaps, **InfoLab at Sungkyunkwan University (SKKU)** launched a project focused on **explainable** and **adaptive ensemble models** using **multivariate time-series data** from early ICU admission. The models are tailored for both **adult and neonatal ICU** settings and emphasize clinical relevance and transparency.

---

## Core Contributions

### 1. Patient-Specific Stacking Ensemble for Adult ICU Mortality Prediction

- Developed a **stacking ensemble** using base learners trained on **modality-specific features** curated by domain experts.
- Features extracted at **6, 12, and 24 hours** post-admission, enabling temporal prediction.
- **MIMIC-III dataset (10,000+ patients):**  
  Achieved **94.4% accuracy**, surpassing traditional scores (e.g., APACHE, SOFA) and standard ML baselines.
- Built a **clinically interpretable pipeline** integrating **temporal feature slices** and **modality fusion**.

---

### 2. Multilayer Dynamic Ensemble for Neonatal ICU Mortality and LOS

- Introduced a **two-layer ensemble system**:
  - **Layer 1:** Predicts **mortality**
  - **Layer 2:** Estimates **length of stay** via regression
- Employed **Dynamic Ensemble Selection (DES)** to adapt to the **local feature space**, boosting reliability under high uncertainty.
- Integrated **XAI tools**:
  - **SHAP values**
  - **Decision tree visualizations**
  - **Rule-based logic**
- Dataset: Refined **NICU cohort of 3,133 neonates (MIMIC-III)**
- Built a **web-based clinical interface** for **real-time ICU monitoring** and **practitioner feedback**

---

## Project Objectives

- Build **robust, generalizable** models for **early mortality** and **LOS prediction** in adult and neonatal ICUs.
- Leverage **stacking and dynamic ensemble techniques** to improve accuracy and model diversity.
- Incorporate **transparent explainability tools** to support clinician trust.
- Tackle challenges such as **missing data**, **irregular timestamps**, and **heterogeneous sources** using domain-informed preprocessing.

---

## Research Impact

By fusing **clinical expertise** with **modern AI**, this project introduces **trustworthy, explainable ensemble models** to the ICU:

- **Enhances patient safety** through early risk detection  
- **Improves hospital resource allocation** with LOS forecasting  
- **Supports medical staff** via actionable insights from **interpretable models**

Together, these efforts offer a practical foundation for next-generation **critical care AI**, shaping a future where **real-time, data-driven decisions** improve ICU outcomes and efficiency.
