---
layout: '../../layouts/MarkdownPost.astro'
title: 'Resolve Domain Conflicts for Generalizable Remote Physiological Measurement'
pubDate: 2024-07-09 05:09:56
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
   content: Weiyu Sun et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.07855v1
## download
[2404.07855v1](http://arxiv.org/abs/2404.07855v1)
## abstracts:
Remote photoplethysmography (rPPG) technology has become increasingly popular due to its non-invasive monitoring of various physiological indicators, making it widely applicable in multimedia interaction, healthcare, and emotion analysis. Existing rPPG methods utilize multiple datasets for training to enhance the generalizability of models. However, they often overlook the underlying conflict issues across different datasets, such as (1) label conflict resulting from different phase delays between physiological signal labels and face videos at the instance level, and (2) attribute conflict stemming from distribution shifts caused by head movements, illumination changes, skin types, etc. To address this, we introduce the DOmain-HArmonious framework (DOHA). Specifically, we first propose a harmonious phase strategy to eliminate uncertain phase delays and preserve the temporal variation of physiological signals. Next, we design a harmonious hyperplane optimization that reduces irrelevant attribute shifts and encourages the model's optimization towards a global solution that fits more valid scenarios. Our experiments demonstrate that DOHA significantly improves the performance of existing methods under multiple protocols. Our code is available at https://github.com/SWY666/rPPG-DOHA.
## QA:
coming soon
