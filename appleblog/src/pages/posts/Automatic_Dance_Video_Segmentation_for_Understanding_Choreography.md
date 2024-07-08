---
layout: '../../layouts/MarkdownPost.astro'
title: '**Automatic Dance Video Segmentation for Understanding Choreography**'
pubDate: '2024-07-09 06:57:48'
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: '['huawei', 'huawei watch']' 
theme: 'light'
featured: true

meta:
 - name: author
   content: Koki Endo et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2405.19727v1
## download
[2405.19727v1](http://arxiv.org/abs/2405.19727v1)
## abstracts:
Segmenting dance video into short movements is a popular way to easily understand dance choreography. However, it is currently done manually and requires a significant amount of effort by experts. That is, even if many dance videos are available on social media (e.g., TikTok and YouTube), it remains difficult for people, especially novices, to casually watch short video segments to practice dance choreography. In this paper, we propose a method to automatically segment a dance video into each movement. Given a dance video as input, we first extract visual and audio features: the former is computed from the keypoints of the dancer in the video, and the latter is computed from the Mel spectrogram of the music in the video. Next, these features are passed to a Temporal Convolutional Network (TCN), and segmentation points are estimated by picking peaks of the network output. To build our training dataset, we annotate segmentation points to dance videos in the AIST Dance Video Database, which is a shared database containing original street dance videos with copyright-cleared dance music. The evaluation study shows that the proposed method (i.e., combining the visual and audio features) can estimate segmentation points with high accuracy. In addition, we developed an application to help dancers practice choreography using the proposed method.
## QA:
coming soon
