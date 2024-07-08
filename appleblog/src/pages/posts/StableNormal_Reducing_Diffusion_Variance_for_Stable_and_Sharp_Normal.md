---
layout: '../../layouts/MarkdownPost.astro'
title: '**StableNormal Reducing Diffusion Variance for Stable and Sharp Normal**'
pubDate: '2024-07-09 07:52:24'
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: '['smart watch']' 
theme: 'light'
featured: true

meta:
 - name: author
   content: Chongjie Ye et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.16864v1
## download
[2406.16864v1](http://arxiv.org/abs/2406.16864v1)
## abstracts:
This work addresses the challenge of high-quality surface normal estimation from monocular colored inputs (i.e., images and videos), a field which has recently been revolutionized by repurposing diffusion priors. However, previous attempts still struggle with stochastic inference, conflicting with the deterministic nature of the Image2Normal task, and costly ensembling step, which slows down the estimation process. Our method, StableNormal, mitigates the stochasticity of the diffusion process by reducing inference variance, thus producing "Stable-and-Sharp" normal estimates without any additional ensembling process. StableNormal works robustly under challenging imaging conditions, such as extreme lighting, blurring, and low quality. It is also robust against transparent and reflective surfaces, as well as cluttered scenes with numerous objects. Specifically, StableNormal employs a coarse-to-fine strategy, which starts with a one-step normal estimator (YOSO) to derive an initial normal guess, that is relatively coarse but reliable, then followed by a semantic-guided refinement process (SG-DRN) that refines the normals to recover geometric details. The effectiveness of StableNormal is demonstrated through competitive performance in standard datasets such as DIODE-indoor, iBims, ScannetV2 and NYUv2, and also in various downstream tasks, such as surface reconstruction and normal enhancement. These results evidence that StableNormal retains both the "stability" and "sharpness" for accurate normal estimation. StableNormal represents a baby attempt to repurpose diffusion priors for deterministic estimation. To democratize this, code and models have been publicly available in hf.co/Stable-X
## QA:
coming soon
