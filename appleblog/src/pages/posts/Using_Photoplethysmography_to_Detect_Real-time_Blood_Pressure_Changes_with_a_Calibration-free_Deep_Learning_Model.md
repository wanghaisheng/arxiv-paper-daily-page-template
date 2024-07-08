---
layout: '../../layouts/MarkdownPost.astro'
title: 'Using Photoplethysmography to Detect Real-time Blood Pressure Changes with a Calibration-free Deep Learning Model'
pubDate: 2024-07-09 05:09:51
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
   content: Jingyuan Hong et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.03274v1
## download
[2407.03274v1](http://arxiv.org/abs/2407.03274v1)
## abstracts:
Blood pressure (BP) changes are linked to individual health status in both clinical and non-clinical settings. This study developed a deep learning model to classify systolic (SBP), diastolic (DBP), and mean (MBP) BP changes using photoplethysmography (PPG) waveforms. Data from the Vital Signs Database (VitalDB) comprising 1,005 ICU patients with synchronized PPG and BP recordings was used. BP changes were categorized into three labels: Spike (increase above a threshold), Stable (change within a plus or minus threshold), and Dip (decrease below a threshold). Four time-series classification models were studied: multi-layer perceptron, convolutional neural network, residual network, and Encoder. A subset of 500 patients was randomly selected for training and validation, ensuring a uniform distribution across BP change labels. Two test datasets were compiled: Test-I (n=500) with a uniform distribution selection process, and Test-II (n=5) without. The study also explored the impact of including second-deviation PPG (sdPPG) waveforms as additional input information. The Encoder model with a Softmax weighting process using both PPG and sdPPG waveforms achieved the highest detection accuracy--exceeding 71.3% and 85.4% in Test-I and Test-II, respectively, with thresholds of 30 mmHg for SBP, 15 mmHg for DBP, and 20 mmHg for MBP. Corresponding F1-scores were over 71.8% and 88.5%. These findings confirm that PPG waveforms are effective for real-time monitoring of BP changes in ICU settings and suggest potential for broader applications.
## QA:
coming soon
