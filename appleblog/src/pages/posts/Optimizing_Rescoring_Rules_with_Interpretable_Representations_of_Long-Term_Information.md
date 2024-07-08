---
layout: '../../layouts/MarkdownPost.astro'
title: 'Optimizing Rescoring Rules with Interpretable Representations of Long-Term Information'
pubDate: 2024-07-09 04:43:52
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
   content: Aaron Fisher et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2104.14291v1
## download
[2104.14291v1](http://arxiv.org/abs/2104.14291v1)
## abstracts:
Analyzing temporal data (e.g., wearable device data) requires a decision about how to combine information from the recent and distant past. In the context of classifying sleep status from actigraphy, Webster's rescoring rules offer one popular solution based on the long-term patterns in the output of a moving-window model. Unfortunately, the question of how to optimize rescoring rules for any given setting has remained unsolved. To address this problem and expand the possible use cases of rescoring rules, we propose rephrasing these rules in terms of epoch-specific features. Our features take two general forms: (1) the time lag between now and the most recent [or closest upcoming] bout of time spent in a given state, and (2) the length of the most recent [or closest upcoming] bout of time spent in a given state. Given any initial moving window model, these features can be defined recursively, allowing for straightforward optimization of rescoring rules. Joint optimization of the moving window model and the subsequent rescoring rules can also be implemented using gradient-based optimization software, such as Tensorflow. Beyond binary classification problems (e.g., sleep-wake), the same approach can be applied to summarize long-term patterns for multi-state classification problems (e.g., sitting, walking, or stair climbing). We find that optimized rescoring rules improve the performance of sleep-wake classifiers, achieving accuracy comparable to that of certain neural network architectures.
## QA:
coming soon
