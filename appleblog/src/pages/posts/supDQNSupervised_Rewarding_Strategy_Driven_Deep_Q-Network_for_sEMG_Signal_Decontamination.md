---
layout: '../../layouts/MarkdownPost.astro'
title: 'supDQN: Supervised Rewarding Strategy Driven Deep Q-Network for sEMG Signal Decontamination'
pubDate: 2024-07-09 05:10:01
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
   content: Ashutosh Jena et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2405.05883v1
## download
[2405.05883v1](http://arxiv.org/abs/2405.05883v1)
## abstracts:
The presence of muscles throughout the active parts of the body such as the upper and lower limbs, makes electromyography-based human-machine interaction prevalent. However, muscle signals are stochastic and noisy. These noises can be regular and irregular. Irregular noises due to movements or electrical switching require dynamic filtering. Conventionally, filters are stacked, which trims and delays the signal unnecessarily. This study introduces a decontamination technique involving a supervised rewarding strategy to drive a deep Q-network-based agent (supDQN). It applies one of three filters to decontaminate a 1sec long surface electromyography signal, which is dynamically contaminated. A machine learning agent identifies whether the signal after filtering is clean or noisy. Accordingly, a reward is generated. The identification accuracy is enhanced by using a local interpretable model-agnostic explanation. The deep Q-network is guided by this reward to select filter optimally while decontaminating a signal. The proposed filtering strategy is tested on four noise levels (-5 dB, -1 dB, +1 dB, +5 dB). supDQN filters the signal desirably when the signal-to-noise ratio (SNR) is between -5 dB to +1 dB. It filters less desirably at high SNR (+5 dB). A normalized root mean square (nRMSE) is formulated to depict the difference of filtered signal from ground truth. This is used to compare supDQN and conventional methods including wavelet denoising with debauchies and symlet wavelet, high order low pass filter, notch filter, and high pass filter. The proposed filtering strategy gives an average value nRMSE of 1.1974, which is lower than the conventional filters.
## QA:
coming soon
