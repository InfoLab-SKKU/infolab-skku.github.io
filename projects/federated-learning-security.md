---
title: "Robust Federated Learning: Defending Distributed AI Against Poisoning Attacks"
---

# {% include icon.html icon="fa-solid fa-network-wired" %} Robust Federated Learning: Defending Distributed AI Against Poisoning Attacks

## Project Description

**Federated Learning (FL)** lets many clients—hospitals, mobile devices, or organizations—collaboratively train a shared model **without ever exchanging their raw data**, making it a natural fit for privacy-sensitive domains such as healthcare and finance. However, this decentralization opens a new attack surface: because the server never sees client data, **malicious or compromised participants can quietly corrupt the global model** through data- and model-poisoning attacks.

At **InfoLab, Sungkyunkwan University (SKKU)**, our research investigates how robust federated learning really is once the convenient assumption of clean, identically distributed client data is removed. We study how poisoning attacks behave under **realistic client data heterogeneity (non-IID settings)** and how defenses must adapt when honest clients already look very different from one another.

## Core Research Themes and Contributions

### 1. Poisoning Attacks Under Client Data Heterogeneity

Most FL robustness studies assume clients hold similar (IID) data, which makes anomalous updates easy to flag. We move to the **harder, more realistic case** where each client's data distribution differs:

- Evaluate **data-poisoning** (label flipping) and **model-poisoning** attacks across varying degrees of non-IID partitioning.
- Show that **data heterogeneity masks malicious updates**, because the natural variance between honest clients shrinks the gap that anomaly-based defenses rely on.
- Quantify how attack success and global-model degradation scale with both the **fraction of malicious clients** and the **severity of distribution skew**.

### 2. Stress-Testing Aggregation and Defense Strategies

We examine how standard robust-aggregation rules hold up under combined pressure from heterogeneity and adversaries, identifying where they fail and what signals remain reliable for detecting compromised participants.

## Project Objectives

- Characterize the **real-world robustness** of federated learning when client data is non-IID and a subset of participants is adversarial.
- Map the relationship between **distribution skew, attacker fraction, and model degradation**.
- Evaluate and harden **robust-aggregation and anomaly-detection defenses** for heterogeneous federations.
- Provide reproducible benchmarks for **trustworthy, attack-resilient collaborative learning**.

## Research Impact

This project extends InfoLab's adversarial-ML expertise from centralized models to **distributed, privacy-preserving training**. By exposing how heterogeneity weakens existing defenses, our work at **InfoLab (SKKU)** helps build federated systems that remain dependable in the conditions they will actually be deployed in—hospitals, edge devices, and cross-organization collaborations—where data is never uniform and not every participant can be trusted.
