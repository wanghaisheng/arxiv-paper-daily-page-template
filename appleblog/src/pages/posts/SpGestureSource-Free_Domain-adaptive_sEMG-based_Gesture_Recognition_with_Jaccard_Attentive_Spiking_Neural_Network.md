---
layout: '../../layouts/MarkdownPost.astro'
title: 'SpGesture: Source-Free Domain-adaptive sEMG-based Gesture Recognition with Jaccard Attentive Spiking Neural Network'
pubDate: 2024-07-09 04:44:31
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['Electromyography'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Weiyu Guo et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2405.14398v1
## download
[2405.14398v1](http://arxiv.org/abs/2405.14398v1)
## abstracts:
Surface electromyography (sEMG) based gesture recognition offers a natural and intuitive interaction modality for wearable devices. Despite significant advancements in sEMG-based gesture-recognition models, existing methods often suffer from high computational latency and increased energy consumption. Additionally, the inherent instability of sEMG signals, combined with their sensitivity to distribution shifts in real-world settings, compromises model robustness.   To tackle these challenges, we propose a novel SpGesture framework based on Spiking Neural Networks, which possesses several unique merits compared with existing methods: (1) Robustness: By utilizing membrane potential as a memory list, we pioneer the introduction of Source-Free Domain Adaptation into SNN for the first time. This enables SpGesture to mitigate the accuracy degradation caused by distribution shifts. (2) High Accuracy: With a novel Spiking Jaccard Attention, SpGesture enhances the SNNs' ability to represent sEMG features, leading to a notable rise in system accuracy. To validate SpGesture's performance, we collected a new sEMG gesture dataset which has different forearm postures, where SpGesture achieved the highest accuracy among the baselines ($89.26\%$). Moreover, the actual deployment on the CPU demonstrated a system latency below 100ms, well within real-time requirements. This impressive performance showcases SpGesture's potential to enhance the applicability of sEMG in real-world scenarios. The code is available at https://anonymous.4open.science/r/SpGesture.
## QA:
coming soon
