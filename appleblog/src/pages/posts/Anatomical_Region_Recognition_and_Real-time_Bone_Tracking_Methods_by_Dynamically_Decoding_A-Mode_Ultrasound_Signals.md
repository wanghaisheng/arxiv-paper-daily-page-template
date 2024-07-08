---
layout: '../../layouts/MarkdownPost.astro'
title: 'Anatomical Region Recognition and Real-time Bone Tracking Methods by Dynamically Decoding A-Mode Ultrasound Signals'
pubDate: 2024-07-09 04:44:30
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
   content: Bangyu Lan et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2405.19542v2
## download
[2405.19542v2](http://arxiv.org/abs/2405.19542v2)
## abstracts:
Accurate bone tracking is crucial for kinematic analysis in orthopedic surgery and prosthetic robotics. Traditional methods (e.g., skin markers) are subject to soft tissue artifacts, and the bone pins used in surgery introduce the risk of additional trauma and infection. For electromyography (EMG), its inability to directly measure joint angles requires complex algorithms for kinematic estimation. To address these issues, A-mode ultrasound-based tracking has been proposed as a non-invasive and safe alternative. However, this approach suffers from limited accuracy in peak detection when processing received ultrasound signals. To build a precise and real-time bone tracking approach, this paper introduces a deep learning-based method for anatomical region recognition and bone tracking using A-mode ultrasound signals, specifically focused on the knee joint. The algorithm is capable of simultaneously performing bone tracking and identifying the anatomical region where the A-mode ultrasound transducer is placed. It contains the fully connection between all encoding and decoding layers of the cascaded U-Nets to focus only on the signal region that is most likely to have the bone peak, thus pinpointing the exact location of the peak and classifying the anatomical region of the signal. The experiment showed a 97% accuracy in the classification of the anatomical regions and a precision of around 0.5$\pm$1mm under dynamic tracking conditions for various anatomical areas surrounding the knee joint. In general, this approach shows great potential beyond the traditional method, in terms of the accuracy achieved and the recognition of the anatomical region where the ultrasound has been attached as an additional functionality.
## QA:
coming soon
