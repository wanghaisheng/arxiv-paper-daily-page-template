---
layout: '../../layouts/MarkdownPost.astro'
title: 'Co-Morbidity Exploration on Wearables Activity Data Using Unsupervised Pre-training and Multi-Task Learning'
pubDate: 2024-07-09 04:43:54
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['actigraphy'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Karan Aggarwal et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
1712.09527v1
## download
[1712.09527v1](http://arxiv.org/abs/1712.09527v1)
## abstracts:
Physical activity and sleep play a major role in the prevention and management of many chronic conditions. It is not a trivial task to understand their impact on chronic conditions. Currently, data from electronic health records (EHRs), sleep lab studies, and activity/sleep logs are used. The rapid increase in the popularity of wearable health devices provides a significant new data source, making it possible to track the user's lifestyle real-time through web interfaces, both to consumer as well as their healthcare provider, potentially. However, at present there is a gap between lifestyle data (e.g., sleep, physical activity) and clinical outcomes normally captured in EHRs. This is a critical barrier for the use of this new source of signal for healthcare decision making. Applying deep learning to wearables data provides a new opportunity to overcome this barrier.   To address the problem of the unavailability of clinical data from a major fraction of subjects and unrepresentative subject populations, we propose a novel unsupervised (task-agnostic) time-series representation learning technique called act2vec. act2vec learns useful features by taking into account the co-occurrence of activity levels along with periodicity of human activity patterns. The learned representations are then exploited to boost the performance of disorder-specific supervised learning models. Furthermore, since many disorders are often related to each other, a phenomenon referred to as co-morbidity, we use a multi-task learning framework for exploiting the shared structure of disorder inducing life-style choices partially captured in the wearables data. Empirical evaluation using actigraphy data from 4,124 subjects shows that our proposed method performs and generalizes substantially better than the conventional time-series symbolic representational methods and task-specific deep learning models.
## QA:
coming soon