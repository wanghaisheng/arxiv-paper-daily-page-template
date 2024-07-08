---
layout: '../../layouts/MarkdownPost.astro'
title: 'Towards Robust and Interpretable EMG-based Hand Gesture Recognition using Deep Metric Meta Learning'
pubDate: 2024-07-09 05:10:02
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
   content: Simon Tam et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.15360v1
## download
[2404.15360v1](http://arxiv.org/abs/2404.15360v1)
## abstracts:
Current electromyography (EMG) pattern recognition (PR) models have been shown to generalize poorly in unconstrained environments, setting back their adoption in applications such as hand gesture control. This problem is often due to limited training data, exacerbated by the use of supervised classification frameworks that are known to be suboptimal in such settings. In this work, we propose a shift to deep metric-based meta-learning in EMG PR to supervise the creation of meaningful and interpretable representations. We use a Siamese Deep Convolutional Neural Network (SDCNN) and contrastive triplet loss to learn an EMG feature embedding space that captures the distribution of the different classes. A nearest-centroid approach is subsequently employed for inference, relying on how closely a test sample aligns with the established data distributions. We derive a robust class proximity-based confidence estimator that leads to a better rejection of incorrect decisions, i.e. false positives, especially when operating beyond the training data domain. We show our approach's efficacy by testing the trained SDCNN's predictions and confidence estimations on unseen data, both in and out of the training domain. The evaluation metrics include the accuracy-rejection curve and the Kullback-Leibler divergence between the confidence distributions of accurate and inaccurate predictions. Outperforming comparable models on both metrics, our results demonstrate that the proposed meta-learning approach improves the classifier's precision in active decisions (after rejection), thus leading to better generalization and applicability.
## QA:
coming soon
