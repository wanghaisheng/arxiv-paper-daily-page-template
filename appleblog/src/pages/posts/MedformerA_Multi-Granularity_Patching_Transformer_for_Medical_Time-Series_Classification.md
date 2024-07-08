---
layout: '../../layouts/MarkdownPost.astro'
title: 'Medformer: A Multi-Granularity Patching Transformer for Medical Time-Series Classification'
pubDate: 2024-07-09 04:44:41
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
   content: Yihe Wang et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2405.19363v1
## download
[2405.19363v1](http://arxiv.org/abs/2405.19363v1)
## abstracts:
Medical time series data, such as Electroencephalography (EEG) and Electrocardiography (ECG), play a crucial role in healthcare, such as diagnosing brain and heart diseases. Existing methods for medical time series classification primarily rely on handcrafted biomarkers extraction and CNN-based models, with limited exploration of transformers tailored for medical time series. In this paper, we introduce Medformer, a multi-granularity patching transformer tailored specifically for medical time series classification. Our method incorporates three novel mechanisms to leverage the unique characteristics of medical time series: cross-channel patching to leverage inter-channel correlations, multi-granularity embedding for capturing features at different scales, and two-stage (intra- and inter-granularity) multi-granularity self-attention for learning features and correlations within and among granularities. We conduct extensive experiments on five public datasets under both subject-dependent and challenging subject-independent setups. Results demonstrate Medformer's superiority over 10 baselines, achieving top averaged ranking across five datasets on all six evaluation metrics. These findings underscore the significant impact of our method on healthcare applications, such as diagnosing Myocardial Infarction, Alzheimer's, and Parkinson's disease. We release the source code at \url{https://github.com/DL4mHealth/Medformer}.
## QA:
coming soon
