---
layout: '../../layouts/MarkdownPost.astro'
title: 'CaFNet: A Confidence-Driven Framework for Radar Camera Depth Estimation'
pubDate: 2024-07-09 04:44:11
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['huawei', 'huawei watch'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Huawei Sun et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.00697v1
## download
[2407.00697v1](http://arxiv.org/abs/2407.00697v1)
## abstracts:
Depth estimation is critical in autonomous driving for interpreting 3D scenes accurately. Recently, radar-camera depth estimation has become of sufficient interest due to the robustness and low-cost properties of radar. Thus, this paper introduces a two-stage, end-to-end trainable Confidence-aware Fusion Net (CaFNet) for dense depth estimation, combining RGB imagery with sparse and noisy radar point cloud data. The first stage addresses radar-specific challenges, such as ambiguous elevation and noisy measurements, by predicting a radar confidence map and a preliminary coarse depth map. A novel approach is presented for generating the ground truth for the confidence map, which involves associating each radar point with its corresponding object to identify potential projection surfaces. These maps, together with the initial radar input, are processed by a second encoder. For the final depth estimation, we innovate a confidence-aware gated fusion mechanism to integrate radar and image features effectively, thereby enhancing the reliability of the depth map by filtering out radar noise. Our methodology, evaluated on the nuScenes dataset, demonstrates superior performance, improving upon the current leading model by 3.2% in Mean Absolute Error (MAE) and 2.7% in Root Mean Square Error (RMSE).
## QA:
coming soon
