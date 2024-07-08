---
layout: '../../layouts/MarkdownPost.astro'
title: 'Exploring the limitations of blood pressure estimation using the photoplethysmography signal'
pubDate: 2024-07-09 05:09:57
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['PPG', 'Photoplethysmography'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Felipe M. Dias et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.16049v1
## download
[2404.16049v1](http://arxiv.org/abs/2404.16049v1)
## abstracts:
Hypertension, a leading contributor to cardiovascular morbidity, underscores the need for accurate and continuous blood pressure (BP) monitoring. Photoplethysmography (PPG) presents a promising approach to this end. However, the precision of BP estimates derived from PPG signals has been the subject of ongoing debate, necessitating a comprehensive evaluation of their effectiveness and constraints. We developed a calibration-based Siamese ResNet model for BP estimation, using a signal input paired with a reference BP reading. We compared the use of normalized PPG (N-PPG) against the normalized Invasive Arterial Blood Pressure (N-IABP) signals as input. The N-IABP signals do not directly present systolic and diastolic values but theoretically provide a more accurate BP measure than PPG signals since it is a direct pressure sensor inside the body. Our strategy establishes a critical benchmark for PPG performance, realistically calibrating expectations for PPG's BP estimation capabilities. Nonetheless, we compared the performance of our models using different signal-filtering conditions to evaluate the impact of filtering on the results. We evaluated our method using the AAMI and the BHS standards employing the VitalDB dataset. The N-IABP signals meet with AAMI standards for both Systolic Blood Pressure (SBP) and Diastolic Blood Pressure (DBP), with errors of 1.29+-6.33mmHg for systolic pressure and 1.17+-5.78mmHg for systolic and diastolic pressure respectively for the raw N-IABP signal. In contrast, N-PPG signals, in their best setup, exhibited inferior performance than N-IABP, presenting 1.49+-11.82mmHg and 0.89+-7.27mmHg for systolic and diastolic pressure respectively. Our findings highlight the potential and limitations of employing PPG for BP estimation, showing that these signals contain information correlated to BP but may not be sufficient for predicting it accurately.
## QA:
coming soon
