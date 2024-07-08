---
layout: '../../layouts/MarkdownPost.astro'
title: 'An LSTM Feature Imitation Network for Hand Movement Recognition from sEMG Signals'
pubDate: 2024-07-09 04:44:31
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
   content: Chuheng Wu et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2405.19356v1
## download
[2405.19356v1](http://arxiv.org/abs/2405.19356v1)
## abstracts:
Surface Electromyography (sEMG) is a non-invasive signal that is used in the recognition of hand movement patterns, the diagnosis of diseases, and the robust control of prostheses. Despite the remarkable success of recent end-to-end Deep Learning approaches, they are still limited by the need for large amounts of labeled data. To alleviate the requirement for big data, researchers utilize Feature Engineering, which involves decomposing the sEMG signal into several spatial, temporal, and frequency features. In this paper, we propose utilizing a feature-imitating network (FIN) for closed-form temporal feature learning over a 300ms signal window on Ninapro DB2, and applying it to the task of 17 hand movement recognition. We implement a lightweight LSTM-FIN network to imitate four standard temporal features (entropy, root mean square, variance, simple square integral). We then explore transfer learning capabilities by applying the pre-trained LSTM-FIN for tuning to a downstream hand movement recognition task. We observed that the LSTM network can achieve up to 99\% R2 accuracy in feature reconstruction and 80\% accuracy in hand movement recognition. Our results also showed that the model can be robustly applied for both within- and cross-subject movement recognition, as well as simulated low-latency environments. Overall, our work demonstrates the potential of the FIN modeling paradigm in data-scarce scenarios for sEMG signal processing.
## QA:
coming soon
