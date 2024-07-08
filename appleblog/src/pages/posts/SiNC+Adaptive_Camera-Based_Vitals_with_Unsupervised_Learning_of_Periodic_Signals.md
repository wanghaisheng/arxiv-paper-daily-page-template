---
layout: '../../layouts/MarkdownPost.astro'
title: 'SiNC+: Adaptive Camera-Based Vitals with Unsupervised Learning of Periodic Signals'
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
   content: Jeremy Speth et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.13449v1
## download
[2404.13449v1](http://arxiv.org/abs/2404.13449v1)
## abstracts:
Subtle periodic signals, such as blood volume pulse and respiration, can be extracted from RGB video, enabling noncontact health monitoring at low cost. Advancements in remote pulse estimation -- or remote photoplethysmography (rPPG) -- are currently driven by deep learning solutions. However, modern approaches are trained and evaluated on benchmark datasets with ground truth from contact-PPG sensors. We present the first non-contrastive unsupervised learning framework for signal regression to mitigate the need for labelled video data. With minimal assumptions of periodicity and finite bandwidth, our approach discovers the blood volume pulse directly from unlabelled videos. We find that encouraging sparse power spectra within normal physiological bandlimits and variance over batches of power spectra is sufficient for learning visual features of periodic signals. We perform the first experiments utilizing unlabelled video data not specifically created for rPPG to train robust pulse rate estimators. Given the limited inductive biases, we successfully applied the same approach to camera-based respiration by changing the bandlimits of the target signal. This shows that the approach is general enough for unsupervised learning of bandlimited quasi-periodic signals from different domains. Furthermore, we show that the framework is effective for finetuning models on unlabelled video from a single subject, allowing for personalized and adaptive signal regressors.
## QA:
coming soon
