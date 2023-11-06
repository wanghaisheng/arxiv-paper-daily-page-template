---
layout: '../../layouts/MarkdownPost.astro'
title: 'StairNet: Visual Recognition of Stairs for Human-Robot Locomotion'
pubDate: 2023-11-06 21:53:29
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['wearable', 'smart watch'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Andrew Garrett Kurbis et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2310.20666v1
## download
[2310.20666v1](http://arxiv.org/abs/2310.20666v1)
## abstracts:
Human-robot walking with prosthetic legs and exoskeletons, especially over complex terrains such as stairs, remains a significant challenge. Egocentric vision has the unique potential to detect the walking environment prior to physical interactions, which can improve transitions to and from stairs. This motivated us to create the StairNet initiative to support the development of new deep learning models for visual sensing and recognition of stairs, with an emphasis on lightweight and efficient neural networks for onboard real-time inference. In this study, we present an overview of the development of our large-scale dataset with over 515,000 manually labeled images, as well as our development of different deep learning models (e.g., 2D and 3D CNN, hybrid CNN and LSTM, and ViT networks) and training methods (e.g., supervised learning with temporal data and semi-supervised learning with unlabeled images) using our new dataset. We consistently achieved high classification accuracy (i.e., up to 98.8%) with different designs, offering trade-offs between model accuracy and size. When deployed on mobile devices with GPU and NPU accelerators, our deep learning models achieved inference speeds up to 2.8 ms. We also deployed our models on custom-designed CPU-powered smart glasses. However, limitations in the embedded hardware yielded slower inference speeds of 1.5 seconds, presenting a trade-off between human-centered design and performance. Overall, we showed that StairNet can be an effective platform to develop and study new visual perception systems for human-robot locomotion with applications in exoskeleton and prosthetic leg control.
## QA:
None
