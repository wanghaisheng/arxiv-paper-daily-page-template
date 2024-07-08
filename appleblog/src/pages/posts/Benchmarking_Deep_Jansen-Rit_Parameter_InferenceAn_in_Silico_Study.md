---
layout: '../../layouts/MarkdownPost.astro'
title: 'Benchmarking Deep Jansen-Rit Parameter Inference: An in Silico Study'
pubDate: 2024-07-09 04:44:40
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
   content: Deepa Tilwani et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.05002v1
## download
[2406.05002v1](http://arxiv.org/abs/2406.05002v1)
## abstracts:
The study of effective connectivity (EC) is essential in understanding how the brain integrates and responds to various sensory inputs. Model-driven estimation of EC is a powerful approach that requires estimating global and local parameters of a generative model of neural activity. Insights gathered through this process can be used in various applications, such as studying neurodevelopmental disorders. However, accurately determining EC through generative models remains a significant challenge due to the complexity of brain dynamics and the inherent noise in neural recordings, e.g., in electroencephalography (EEG). Current model-driven methods to study EC are computationally complex and cannot scale to all brain regions as required by whole-brain analyses. To facilitate EC assessment, an inference algorithm must exhibit reliable prediction of parameters in the presence of noise. Further, the relationship between the model parameters and the neural recordings must be learnable. To progress toward these objectives, we benchmarked the performance of a Bi-LSTM model for parameter inference from the Jansen-Rit neural mass model (JR-NMM) simulated EEG under various noise conditions. Additionally, our study explores how the JR-NMM reacts to changes in key biological parameters (i.e., sensitivity analysis) like synaptic gains and time constants, a crucial step in understanding the connection between neural mechanisms and observed brain activity. Our results indicate that we can predict the local JR-NMM parameters from EEG, supporting the feasibility of our deep-learning-based inference approach. In future work, we plan to extend this framework to estimate local and global parameters from real EEG in clinically relevant applications.
## QA:
coming soon
