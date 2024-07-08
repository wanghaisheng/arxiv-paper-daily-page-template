---
layout: '../../layouts/MarkdownPost.astro'
title: 'EEG_GLT-Net: Optimising EEG Graphs for Real-time Motor Imagery Signals Classification'
pubDate: 2024-07-09 05:10:58
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
   content: Htoo Wai Aung et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2404.11075v1
## download
[2404.11075v1](http://arxiv.org/abs/2404.11075v1)
## abstracts:
Brain-Computer Interfaces connect the brain to external control devices, necessitating the accurate translation of brain signals such as from electroencephalography (EEG) into executable commands. Graph Neural Networks (GCN) have been increasingly applied for classifying EEG Motor Imagery signals, primarily because they incorporates the spatial relationships among EEG channels, resulting in improved accuracy over traditional convolutional methods. Recent advances by GCNs-Net in real-time EEG MI signal classification utilised Pearson Coefficient Correlation (PCC) for constructing adjacency matrices, yielding significant results on the PhysioNet dataset. Our paper introduces the EEG Graph Lottery Ticket (EEG_GLT) algorithm, an innovative technique for constructing adjacency matrices for EEG channels. It does not require pre-existing knowledge of inter-channel relationships, and it can be tailored to suit both individual subjects and GCN model architectures. Our findings demonstrated that the PCC method outperformed the Geodesic approach by 9.65% in mean accuracy, while our EEG_GLT matrix consistently exceeded the performance of the PCC method by a mean accuracy of 13.39%. Also, we found that the construction of the adjacency matrix significantly influenced accuracy, to a greater extent than GCN model configurations. A basic GCN configuration utilising our EEG_GLT matrix exceeded the performance of even the most complex GCN setup with a PCC matrix in average accuracy. Our EEG_GLT method also reduced MACs by up to 97% compared to the PCC method, while maintaining or enhancing accuracy. In conclusion, the EEG_GLT algorithm marks a breakthrough in the development of optimal adjacency matrices, effectively boosting both computational accuracy and efficiency, making it well-suited for real-time classification of EEG MI signals that demand intensive computational resources.
## QA:
coming soon
