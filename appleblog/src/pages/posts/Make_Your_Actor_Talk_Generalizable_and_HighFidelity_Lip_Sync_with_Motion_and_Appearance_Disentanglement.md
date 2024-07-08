---
layout: '../../layouts/MarkdownPost.astro'
title: "**Make Your Actor Talk Generalizable and HighFidelity Lip Sync with Motion and Appearance Disentanglement**"
pubDate: "2024-07-09 07:47:29"
description: ''
author: "wanghaisheng"
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: "['apple watch', 'apple']"
theme: 'light'
featured: true

meta:
 - name: author
   content: Runyi Yu et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.08096v2
## download
[2406.08096v2](http://arxiv.org/abs/2406.08096v2)
## abstracts:
We aim to edit the lip movements in talking video according to the given speech while preserving the personal identity and visual details. The task can be decomposed into two sub-problems: (1) speech-driven lip motion generation and (2) visual appearance synthesis. Current solutions handle the two sub-problems within a single generative model, resulting in a challenging trade-off between lip-sync quality and visual details preservation. Instead, we propose to disentangle the motion and appearance, and then generate them one by one with a speech-to-motion diffusion model and a motion-conditioned appearance generation model. However, there still remain challenges in each stage, such as motion-aware identity preservation in (1) and visual details preservation in (2). Therefore, to preserve personal identity, we adopt landmarks to represent the motion, and further employ a landmark-based identity loss. To capture motion-agnostic visual details, we use separate encoders to encode the lip, non-lip appearance and motion, and then integrate them with a learned fusion module. We train MyTalk on a large-scale and diverse dataset. Experiments show that our method generalizes well to the unknown, even out-of-domain person, in terms of both lip sync and visual detail preservation. We encourage the readers to watch the videos on our project page (https://Ingrid789.github.io/MyTalk/).
## QA:
coming soon
