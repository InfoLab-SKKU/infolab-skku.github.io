---
title: "New Paper: Federated Learning Under Data Heterogeneity"
author: Abdenour Soubih
tags:
  - federated learning
  - security
  - machine learning
image: images/thumbnails/FLIMCOM25.png
---

We are excited to share our latest paper accepted at **IMCOM 2025**: *Towards Robust Federated Learning: Investigating Poisoning Attacks Under Clients Data Heterogeneity*.

Federated learning enables collaborative model training across distributed clients without sharing raw data — but it remains vulnerable to **poisoning attacks**, especially when client data distributions are heterogeneous.

<!-- more -->

Our work systematically evaluates state-of-the-art poisoning attack strategies under realistic non-IID data settings. We analyze how data heterogeneity affects attack success rates and propose defenses tailored to this challenging scenario.

**Key contributions:**
- Comprehensive evaluation of poisoning attacks under varying degrees of data heterogeneity
- Analysis of why standard defenses (FedAvg + median/trimmed-mean aggregation) fail in non-IID settings
- Lightweight mitigation strategy that degrades attack success without sacrificing model accuracy

The full paper is available on our [publications page](/pubs/).