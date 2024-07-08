---
layout: '../../layouts/MarkdownPost.astro'
title: 'SQUWA: Signal Quality Aware DNN Architecture for Enhanced Accuracy in Atrial Fibrillation Detection from Noisy PPG Signals'
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
   content: Runze Yan et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.15353v1
## download
[2404.15353v1](http://arxiv.org/abs/2404.15353v1)
## abstracts:
Atrial fibrillation (AF), a common cardiac arrhythmia, significantly increases the risk of stroke, heart disease, and mortality. Photoplethysmography (PPG) offers a promising solution for continuous AF monitoring, due to its cost efficiency and integration into wearable devices. Nonetheless, PPG signals are susceptible to corruption from motion artifacts and other factors often encountered in ambulatory settings. Conventional approaches typically discard corrupted segments or attempt to reconstruct original signals, allowing for the use of standard machine learning techniques. However, this reduces dataset size and introduces biases, compromising prediction accuracy and the effectiveness of continuous monitoring. We propose a novel deep learning model, Signal Quality Weighted Fusion of Attentional Convolution and Recurrent Neural Network (SQUWA), designed to learn how to retain accurate predictions from partially corrupted PPG. Specifically, SQUWA innovatively integrates an attention mechanism that directly considers signal quality during the learning process, dynamically adjusting the weights of time series segments based on their quality. This approach enhances the influence of higher-quality segments while reducing that of lower-quality ones, effectively utilizing partially corrupted segments. This approach represents a departure from the conventional methods that exclude such segments, enabling the utilization of a broader range of data, which has great implications for less disruption when monitoring of AF risks and more accurate estimation of AF burdens. Our extensive experiments show that SQUWA outperform existing PPG-based models, achieving the highest AUCPR of 0.89 with label noise mitigation. This also exceeds the 0.86 AUCPR of models trained with using both electrocardiogram (ECG) and PPG data.
## QA:
coming soon
