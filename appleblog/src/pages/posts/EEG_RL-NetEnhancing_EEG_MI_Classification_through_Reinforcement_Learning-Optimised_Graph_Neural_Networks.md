---
layout: '../../layouts/MarkdownPost.astro'
title: 'EEG_RL-Net: Enhancing EEG MI Classification through Reinforcement Learning-Optimised Graph Neural Networks'
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
2405.00723v1
## download
[2405.00723v1](http://arxiv.org/abs/2405.00723v1)
## abstracts:
Brain-Computer Interfaces (BCIs) rely on accurately decoding electroencephalography (EEG) motor imagery (MI) signals for effective device control. Graph Neural Networks (GNNs) outperform Convolutional Neural Networks (CNNs) in this regard, by leveraging the spatial relationships between EEG electrodes through adjacency matrices. The EEG_GLT-Net framework, featuring the state-of-the-art EEG_GLT adjacency matrix method, has notably enhanced EEG MI signal classification, evidenced by an average accuracy of 83.95% across 20 subjects on the PhysioNet dataset. This significantly exceeds the 76.10% accuracy rate achieved using the Pearson Correlation Coefficient (PCC) method within the same framework.   In this research, we advance the field by applying a Reinforcement Learning (RL) approach to the classification of EEG MI signals. Our innovative method empowers the RL agent, enabling not only the classification of EEG MI data points with higher accuracy, but effective identification of EEG MI data points that are less distinct. We present the EEG_RL-Net, an enhancement of the EEG_GLT-Net framework, which incorporates the trained EEG GCN Block from EEG_GLT-Net at an adjacency matrix density of 13.39% alongside the RL-centric Dueling Deep Q Network (Dueling DQN) block. The EEG_RL-Net model showcases exceptional classification performance, achieving an unprecedented average accuracy of 96.40% across 20 subjects within 25 milliseconds. This model illustrates the transformative effect of the RL in EEG MI time point classification.
## QA:
coming soon
