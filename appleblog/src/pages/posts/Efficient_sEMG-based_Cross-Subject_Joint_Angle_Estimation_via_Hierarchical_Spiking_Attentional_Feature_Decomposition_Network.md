---
layout: '../../layouts/MarkdownPost.astro'
title: 'Efficient sEMG-based Cross-Subject Joint Angle Estimation via Hierarchical Spiking Attentional Feature Decomposition Network'
pubDate: 2024-07-09 04:44:33
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
   content: Xin Zhou et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.07517v1
## download
[2404.07517v1](http://arxiv.org/abs/2404.07517v1)
## abstracts:
Surface electromyography (sEMG) has demonstrated significant potential in simultaneous and proportional control (SPC). However, existing algorithms for predicting joint angles based on sEMG often suffer from high inference costs or are limited to specific subjects rather than cross-subject scenarios. To address these challenges, we introduced a hierarchical Spiking Attentional Feature Decomposition Network (SAFE-Net). This network initially compresses sEMG signals into neural spiking forms using a Spiking Sparse Attention Encoder (SSAE). Subsequently, the compressed features are decomposed into kinematic and biological features through a Spiking Attentional Feature Decomposition (SAFD) module. Finally, the kinematic and biological features are used to predict joint angles and identify subject identities, respectively. Our validation on two datasets (SIAT-DB1 and SIAT-DB2) and comparison with two existing methods, Informer and Spikformer, demonstrate that SSAE achieves significant power consumption savings of 39.1% and 37.5% respectively over them in terms of inference costs. Furthermore, SAFE-Net surpasses Informer and Spikformer in recognition accuracy on both datasets. This study underscores the potential of SAFE-Net to advance the field of SPC in lower limb rehabilitation exoskeleton robots.
## QA:
coming soon
