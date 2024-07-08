---
layout: '../../layouts/MarkdownPost.astro'
title: '**DASS: Distilled Audio State Space Models Are Stronger and More Duration-Scalable Learners**'
pubDate: '2024-07-09 06:20:19'
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: '['smart glass']' 
theme: 'light'
featured: true

meta:
 - name: author
   content: Saurabhchand Bhati et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.04082v1
## download
[2407.04082v1](http://arxiv.org/abs/2407.04082v1)
## abstracts:
State-space models (SSMs) have emerged as an alternative to Transformers for audio modeling due to their high computational efficiency with long inputs. While recent efforts on Audio SSMs have reported encouraging results, two main limitations remain: First, in 10-second short audio tagging tasks, Audio SSMs still underperform compared to Transformer-based models such as Audio Spectrogram Transformer (AST). Second, although Audio SSMs theoretically support long audio inputs, their actual performance with long audio has not been thoroughly evaluated. To address these limitations, in this paper, 1) We applied knowledge distillation in audio space model training, resulting in a model called Knowledge Distilled Audio SSM (DASS). To the best of our knowledge, it is the first SSM that outperforms the Transformers on AudioSet and achieves an mAP of 47.6; and 2) We designed a new test called Audio Needle In A Haystack (Audio NIAH). We find that DASS, trained with only 10-second audio clips, can retrieve sound events in audio recordings up to 2.5 hours long, while the AST model fails when the input is just 50 seconds, demonstrating SSMs are indeed more duration scalable.
## QA:
coming soon
