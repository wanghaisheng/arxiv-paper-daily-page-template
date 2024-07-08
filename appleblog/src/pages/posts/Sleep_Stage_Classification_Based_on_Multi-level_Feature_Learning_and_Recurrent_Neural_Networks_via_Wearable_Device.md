---
layout: '../../layouts/MarkdownPost.astro'
title: 'Sleep Stage Classification Based on Multi-level Feature Learning and Recurrent Neural Networks via Wearable Device'
pubDate: 2024-07-09 05:10:25
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
   content: Xin Zhang et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
1711.00629v1
## download
[1711.00629v1](http://arxiv.org/abs/1711.00629v1)
## abstracts:
This paper proposes a practical approach for automatic sleep stage classification based on a multi-level feature learning framework and Recurrent Neural Network (RNN) classifier using heart rate and wrist actigraphy derived from a wearable device. The feature learning framework is designed to extract low- and mid-level features. Low-level features capture temporal and frequency domain properties and mid-level features learn compositions and structural information of signals. Since sleep staging is a sequential problem with long-term dependencies, we take advantage of RNNs with Bidirectional Long Short-Term Memory (BLSTM) architectures for sequence data learning. To simulate the actual situation of daily sleep, experiments are conducted with a resting group in which sleep is recorded in resting state, and a comprehensive group in which both resting sleep and non-resting sleep are included.We evaluate the algorithm based on an eight-fold cross validation to classify five sleep stages (W, N1, N2, N3, and REM). The proposed algorithm achieves weighted precision, recall and F1 score of 58.0%, 60.3%, and 58.2% in the resting group and 58.5%, 61.1%, and 58.5% in the comprehensive group, respectively. Various comparison experiments demonstrate the effectiveness of feature learning and BLSTM. We further explore the influence of depth and width of RNNs on performance. Our method is specially proposed for wearable devices and is expected to be applicable for long-term sleep monitoring at home. Without using too much prior domain knowledge, our method has the potential to generalize sleep disorder detection.
## QA:
coming soon
