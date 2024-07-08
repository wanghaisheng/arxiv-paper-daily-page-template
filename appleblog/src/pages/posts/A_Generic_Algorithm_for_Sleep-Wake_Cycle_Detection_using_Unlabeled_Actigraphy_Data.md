---
layout: '../../layouts/MarkdownPost.astro'
title: 'A Generic Algorithm for Sleep-Wake Cycle Detection using Unlabeled Actigraphy Data'
pubDate: 2024-07-09 04:43:53
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
   content: Shanshan Chen et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
1904.05313v1
## download
[1904.05313v1](http://arxiv.org/abs/1904.05313v1)
## abstracts:
One key component when analyzing actigraphy data for sleep studies is sleep-wake cycle detection. Most detection algorithms rely on accurate sleep diary labels to generate supervised classifiers, with parameters optimized for a particular dataset. However, once the actigraphy trackers are deployed in the field, labels for training models and validating detection accuracy are often not available.   In this paper, we propose a generic, training-free algorithm to detect sleep-wake cycles from minute-by-minute actigraphy. Leveraging a robust nonlinear parametric model, our proposed method refines the detection region by searching for a single change point within bounded regions defined by the parametric model. Challenged by the absence of ground truth labels, we also propose an evaluation metric dedicated to this problem. Tested on week-long actigraphy from 112 children, the results show that the proposed algorithm improves on the baseline model consistently and significantly (p<3e-15). Moreover, focusing on the commonality in human circadian rhythm captured by actigraphy, the proposed method is generic to data collected by various actigraphy trackers, circumventing the laborious label collection step in developing customized classifiers for sleep detection.
## QA:
coming soon
