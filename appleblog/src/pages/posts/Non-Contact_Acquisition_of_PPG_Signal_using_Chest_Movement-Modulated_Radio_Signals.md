---
layout: '../../layouts/MarkdownPost.astro'
title: 'Non-Contact Acquisition of PPG Signal using Chest Movement-Modulated Radio Signals'
pubDate: 2024-07-09 04:44:10
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['Photoplethysmography', 'PPG'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Israel Jesus Santos Filho et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2402.14565v1
## download
[2402.14565v1](http://arxiv.org/abs/2402.14565v1)
## abstracts:
We present for the first time a novel method that utilizes the chest movement-modulated radio signals for non-contact acquisition of the photoplethysmography (PPG) signal. Under the proposed method, a software-defined radio (SDR) exposes the chest of a subject sitting nearby to an orthogonal frequency division multiplexing signal with 64 sub-carriers at a center frequency 5.24 GHz, while another SDR in the close vicinity collects the modulated radio signal reflected off the chest. This way, we construct a custom dataset by collecting 160 minutes of labeled data (both raw radio data as well as the reference PPG signal) from 16 healthy young subjects. With this, we first utilize principal component analysis for dimensionality reduction of the radio data. Next, we denoise the radio signal and reference PPG signal using wavelet technique, followed by segmentation and Z-score normalization. We then synchronize the radio and PPG segments using cross-correlation method. Finally, we proceed to the waveform translation (regression) task, whereby we first convert the radio and PPG segments into frequency domain using discrete cosine transform (DCT), and then learn the non-linear regression between them. Eventually, we reconstruct the synthetic PPG signal by taking inverse DCT of the output of regression block, with a mean absolute error of 8.1294. The synthetic PPG waveform has a great clinical significance as it could be used for non-contact performance assessment of cardiovascular and respiratory systems of patients suffering from infectious diseases, e.g., covid19.
## QA:
coming soon
