---
layout: '../../layouts/MarkdownPost.astro'
title: 'Biometric Authentication Based on Enhanced Remote Photoplethysmography Signal Morphology'
pubDate: 2024-07-09 05:09:51
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
   content: Zhaodong Sun et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.04127v1
## download
[2407.04127v1](http://arxiv.org/abs/2407.04127v1)
## abstracts:
Remote photoplethysmography (rPPG) is a non-contact method for measuring cardiac signals from facial videos, offering a convenient alternative to contact photoplethysmography (cPPG) obtained from contact sensors. Recent studies have shown that each individual possesses a unique cPPG signal morphology that can be utilized as a biometric identifier, which has inspired us to utilize the morphology of rPPG signals extracted from facial videos for person authentication. Since the facial appearance and rPPG are mixed in the facial videos, we first de-identify facial videos to remove facial appearance while preserving the rPPG information, which protects facial privacy and guarantees that only rPPG is used for authentication. The de-identified videos are fed into an rPPG model to get the rPPG signal morphology for authentication. In the first training stage, unsupervised rPPG training is performed to get coarse rPPG signals. In the second training stage, an rPPG-cPPG hybrid training is performed by incorporating external cPPG datasets to achieve rPPG biometric authentication and enhance rPPG signal morphology. Our approach needs only de-identified facial videos with subject IDs to train rPPG authentication models. The experimental results demonstrate that rPPG signal morphology hidden in facial videos can be used for biometric authentication. The code is available at https://github.com/zhaodongsun/rppg_biometrics.
## QA:
coming soon
