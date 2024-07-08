---
layout: '../../layouts/MarkdownPost.astro'
title: 'How Suboptimal is Training rPPG Models with Videos and Targets from Different Body Sites?'
pubDate: 2024-07-09 04:44:09
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
   content: Björn Braun et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2403.10582v1
## download
[2403.10582v1](http://arxiv.org/abs/2403.10582v1)
## abstracts:
Remote camera measurement of the blood volume pulse via photoplethysmography (rPPG) is a compelling technology for scalable, low-cost, and accessible assessment of cardiovascular information. Neural networks currently provide the state-of-the-art for this task and supervised training or fine-tuning is an important step in creating these models. However, most current models are trained on facial videos using contact PPG measurements from the fingertip as targets/ labels. One of the reasons for this is that few public datasets to date have incorporated contact PPG measurements from the face. Yet there is copious evidence that the PPG signals at different sites on the body have very different morphological features. Is training a facial video rPPG model using contact measurements from another site on the body suboptimal? Using a recently released unique dataset with synchronized contact PPG and video measurements from both the hand and face, we can provide precise and quantitative answers to this question. We obtain up to 40 % lower mean squared errors between the waveforms of the predicted and the ground truth PPG signals using state-of-the-art neural models when using PPG signals from the forehead compared to using PPG signals from the fingertip. We also show qualitatively that the neural models learn to predict the morphology of the ground truth PPG signal better when trained on the forehead PPG signals. However, while models trained from the forehead PPG produce a more faithful waveform, models trained from a finger PPG do still learn the dominant frequency (i.e., the heart rate) well.
## QA:
coming soon
