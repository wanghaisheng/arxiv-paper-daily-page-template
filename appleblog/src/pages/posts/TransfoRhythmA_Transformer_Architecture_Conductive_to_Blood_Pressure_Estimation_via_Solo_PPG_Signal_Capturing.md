---
layout: '../../layouts/MarkdownPost.astro'
title: 'TransfoRhythm: A Transformer Architecture Conductive to Blood Pressure Estimation via Solo PPG Signal Capturing'
pubDate: 2024-07-09 04:44:06
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['Photoplethysmography', 'PPG'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Amir Arjomand et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.15352v1
## download
[2404.15352v1](http://arxiv.org/abs/2404.15352v1)
## abstracts:
Recent statistics indicate that approximately 1.3 billion individuals worldwide suffer from hypertension, a leading cause of premature death globally. Blood pressure (BP) serves as a critical health indicator for accurate and timely diagnosis and/or treatment of hypertension. Driven by recent advancements in Artificial Intelligence (AI) and Deep Neural Networks (DNNs), there has been a surge of interest in developing data-driven and cuff-less BP estimation solutions. In this context, current literature predominantly focuses on coupling Electrocardiography (ECG) and Photoplethysmography (PPG) sensors, though this approach is constrained by reliance on multiple sensor types. An alternative, utilizing standalone PPG signals, presents challenges due to the absence of auxiliary sensors (ECG), requiring the use of morphological features while addressing motion artifacts and high-frequency noise. To address these issues, the paper introduces the TransfoRhythm framework, a Transformer-based DNN architecture built upon the recently released physiological database, MIMIC-IV. Leveraging Multi-Head Attention (MHA) mechanism, TransfoRhythm identifies dependencies and similarities across data segments, forming a robust framework for cuff-less BP estimation solely using PPG signals. To our knowledge, this paper represents the first study to apply the MIMIC IV dataset for cuff-less BP estimation, and TransfoRhythm is the first MHA-based model trained via MIMIC IV for BP prediction. Performance evaluation through comprehensive experiments demonstrates TransfoRhythm's superiority over its state-of-the-art counterparts. Specifically, TransfoRhythm achieves highly accurate results with Root Mean Square Error (RMSE) of [1.84, 1.42] and Mean Absolute Error (MAE) of [1.50, 1.17] for systolic and diastolic blood pressures, respectively.
## QA:
coming soon
