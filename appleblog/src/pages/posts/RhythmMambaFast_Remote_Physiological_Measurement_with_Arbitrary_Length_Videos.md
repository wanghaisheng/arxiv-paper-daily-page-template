---
layout: '../../layouts/MarkdownPost.astro'
title: 'RhythmMamba: Fast Remote Physiological Measurement with Arbitrary Length Videos'
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
   content: Bochao Zou et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.06483v1
## download
[2404.06483v1](http://arxiv.org/abs/2404.06483v1)
## abstracts:
Remote photoplethysmography (rPPG) is a non-contact method for detecting physiological signals from facial videos, holding great potential in various applications such as healthcare, affective computing, and anti-spoofing. Existing deep learning methods struggle to address two core issues of rPPG simultaneously: extracting weak rPPG signals from video segments with large spatiotemporal redundancy and understanding the periodic patterns of rPPG among long contexts. This represents a trade-off between computational complexity and the ability to capture long-range dependencies, posing a challenge for rPPG that is suitable for deployment on mobile devices. Based on the in-depth exploration of Mamba's comprehension of spatial and temporal information, this paper introduces RhythmMamba, an end-to-end Mamba-based method that employs multi-temporal Mamba to constrain both periodic patterns and short-term trends, coupled with frequency domain feed-forward to enable Mamba to robustly understand the quasi-periodic patterns of rPPG. Extensive experiments show that RhythmMamba achieves state-of-the-art performance with reduced parameters and lower computational complexity. The proposed RhythmMamba can be applied to video segments of any length without performance degradation. The codes are available at https://github.com/zizheng-guo/RhythmMamba.
## QA:
coming soon
