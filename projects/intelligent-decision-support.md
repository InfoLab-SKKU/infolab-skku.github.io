---
title: xplainable Dynamic Ensemble Learning with Late Fusion of Multimodal Data for Intelligent Decision
---

{% include breadcrumbs.html %}

# {% include icon.html icon="fa-solid fa-layer-group" %} Explainable Dynamic Ensemble Learning with Late Fusion of Multimodal Data for Intelligent Decision Support

## Project Description

In domains like **healthcare**, **finance**, and **cybersecurity**, data often comes from **multiple modalities**—images, sensors, clinical records, and text reports. However, this heterogeneity presents major challenges:

- **Missing modalities**
- **Imbalanced feature sets**
- **Prediction uncertainty**

While **dynamic ensemble selection (DES)** offers a flexible way to choose the best models per instance, traditional systems mostly rely on **early fusion**, limiting their performance and explainability.

To overcome these limitations, **InfoLab at Sungkyunkwan University (SKKU)** has developed a novel **explainable DES framework** using **late fusion**. This project introduces new algorithms, validated applications, and an open-source Python library, **Infodeslib**, for real-world use.

---

## Key Contributions

### 1. Infodeslib: Python Library for Dynamic Late Fusion

An open-source Python package that implements:

- **4 DCS** and **7 DES** techniques adapted for **late fusion**
- Modular assignment of classifiers to specific modalities
- Improved **generalization** and **modal robustness**

Built-in **explainability tools** include:

- **Case-Based Reasoning (CBR):** Highlights similar past cases
- **Classifier Contribution Visuals:** Shows how each model influenced the final decision
- **Local Feature Importance (SHAP):** Displays feature impact on predictions

---

### 2. Dynamic Late Fusion Framework with Clinical Validation

We extended traditional DES methods like **KNORA-U** to support **late fusion** using **region-of-competence selection**.

**Evaluation Results:**

- **MIT-GOSSIS Dataset (6,600 hospital patients):**  
  Achieved **90.16% accuracy**, outperforming early fusion and static ensembles
- **Additional Benchmarks:**  
  ADNI, NACC, PPMI, Credit Card Clients, and Samarkand Neonatal ICU Dataset
- Demonstrated strong performance in **handling missing data** and **enhancing diversity**

---

## Project Objectives

- Build an **adaptive, late-fusion ensemble framework** that dynamically selects models across modalities
- Integrate **explainable AI tools** to support **transparent decision-making**
- Test the framework across **healthcare, financial, and critical system datasets**
- Release a **user-friendly, open-source library** to foster adoption and reproducibility

---

## Research Impact

This project pioneers a **next-gen intelligent decision support system** by uniting:

- **Dynamic ensemble learning**
- **Multimodal late fusion**
- **Embedded explainability**

The result is a robust, interpretable solution for high-stakes AI applications. By releasing **Infodeslib**, InfoLab (SKKU) empowers researchers and practitioners to build trustworthy and high-performance systems across a range of multimodal data environments.
