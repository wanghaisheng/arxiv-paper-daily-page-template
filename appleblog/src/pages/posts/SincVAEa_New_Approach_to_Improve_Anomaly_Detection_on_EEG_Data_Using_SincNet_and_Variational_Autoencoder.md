---
layout: '../../layouts/MarkdownPost.astro'
title: 'SincVAE: a New Approach to Improve Anomaly Detection on EEG Data Using SincNet and Variational Autoencoder'
pubDate: 2024-07-09 05:10:51
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['Electroencephalography'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Andrea Pollastro et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.17537v1
## download
[2406.17537v1](http://arxiv.org/abs/2406.17537v1)
## abstracts:
Over the past few decades, electroencephalography (EEG) monitoring has become a pivotal tool for diagnosing neurological disorders, particularly for detecting seizures. Epilepsy, one of the most prevalent neurological diseases worldwide, affects approximately the 1 \% of the population. These patients face significant risks, underscoring the need for reliable, continuous seizure monitoring in daily life. Most of the techniques discussed in the literature rely on supervised Machine Learning (ML) methods. However, the challenge of accurately labeling variations in epileptic EEG waveforms complicates the use of these approaches. Additionally, the rarity of ictal events introduces an high imbalancing within the data, which could lead to poor prediction performance in supervised learning approaches. Instead, a semi-supervised approach allows to train the model only on data not containing seizures, thus avoiding the issues related to the data imbalancing. This work proposes a semi-supervised approach for detecting epileptic seizures from EEG data, utilizing a novel Deep Learning-based method called SincVAE. This proposal incorporates the learning of an ad-hoc array of bandpass filter as a first layer of a Variational Autoencoder (VAE), potentially eliminating the preprocessing stage where informative band frequencies are identified and isolated. Results indicate that SincVAE improves seizure detection in EEG data and is capable of identifying early seizures during the preictal stage as well as monitoring patients throughout the postictal stage.
## QA:
coming soon
