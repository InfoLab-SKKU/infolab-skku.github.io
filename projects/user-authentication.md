---
title: Comprehensive Evaluation of Adversarial Robustness in Deep Learning: Architecture, Diversity, and Defense Analysis
---

{% include breadcrumbs.html %}
# {% include icon.html icon="fa-solid fa-user-shield" %} Behavioral Biometrics for Continuous and Adversarially Robust User Authentication on Smartphones
![Image3](../images/thumbnails/projects/Behavioral Biometrics for Continuous and Adversarially Robust User Authentication on Smartphones 1.jpg)

## Project Description

Traditional authentication methods—such as **passwords, PINs**, and even biometric systems like **fingerprint or facial recognition**—typically secure mobile devices **only at the point of entry**. However, they fail to offer protection **throughout the session**, leaving devices vulnerable to **unauthorized access** when unattended.

To bridge this gap, **InfoLab at Sungkyunkwan University (SKKU)** has conducted a series of studies on **continuous, sensor-based, and adversarially-aware user authentication** for smartphones. This project focuses on designing and evaluating **practical, deep-learning-powered implicit authentication systems** using motion and touch sensor data collected unobtrusively from commodity devices.

It addresses real-world **deployment constraints**, **robustness against adversarial conditions**, and **usability trade-offs** to create trustworthy systems that authenticate users **continuously** based on their behavioral patterns.

---

## Core Contributions and Insights

### 1. MotionID: Toward Practical Behavioral-Based Implicit Authentication

**MotionID** introduces a comprehensive continuous authentication framework that uses touch and motion sensor data:

- Sensors used: **Accelerometer, gyroscope, magnetometer, elevation, gravity**
- **Global Mobile Average** approach to adapt to device-specific sensor variability
- Supports **cross-app and unconstrained usage** scenarios
- Operates on short sample windows of **1–5 seconds** for real-time user identification
- Achieves **F1-scores up to 98.5%**
- Optimized for **low power and memory usage**, making it highly deployable

---

### 2. AUToSen: Deep-Learning-Based Continuous Authentication

**AUToSen** is a high-frequency, **LSTM-based deep learning** authentication system that captures users’ behavioral patterns using built-in sensors:

- Sensors: **Accelerometer, gyroscope, magnetometer**
- Handles **time-series data** for robust modeling
- Achieves:
  - **F1-score ≈ 98%**
  - **Equal Error Rate (EER) as low as 0.09%**
  - **Authentication latency as short as 0.5 seconds**
- Operates effectively with **minimal sensor inputs**, ensuring **lightweight and privacy-preserving** authentication

---

## Research Objectives

- Design and evaluate **real-time, behavioral-based implicit authentication mechanisms** for smartphones.
- Address **device diversity**, **sensor inconsistencies**, and **unconstrained user behavior** in real-world conditions.
- Balance **robustness and usability**, with emphasis on **power efficiency** and **low-latency authentication**.
- Develop methods that remain **resilient against adversarial attempts** to mimic user behavior.
- Offer a **scalable and generalizable framework** for deployment across heterogeneous devices and user populations.

---

## Research Impact

This project represents a **significant advancement in mobile security** by transforming passive sensor data into powerful **behavioral signatures**. The solutions from **InfoLab (SKKU)** enable **continuous, transparent, and secure user authentication**, laying the foundation for:

- **Adversarially robust** mobile security
- **Privacy-preserving** real-time protection
- Practical use in **finance, healthcare, and enterprise systems**

These innovations offer real-world viability for **next-generation authentication systems** that are intelligent, seamless, and secure.
