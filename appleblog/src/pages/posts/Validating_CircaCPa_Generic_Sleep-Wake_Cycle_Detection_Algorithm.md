---
layout: '../../layouts/MarkdownPost.astro'
title: 'Validating CircaCP: a Generic Sleep-Wake Cycle Detection Algorithm'
pubDate: 2024-07-09 04:43:51
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['actigraphy'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Shanshan Chen et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2111.14960v1
## download
[2111.14960v1](http://arxiv.org/abs/2111.14960v1)
## abstracts:
Sleep-wake cycle detection is a key step when extrapolating sleep patterns from actigraphy data. Numerous supervised detection algorithms have been developed with parameters estimated from and optimized for a particular dataset, yet their generalizability from sensor to sensor or study to study is unknown. In this paper, we propose and validate an unsupervised algorithm -- CircaCP -- to detect sleep-wake cycles from minute-by-minute actigraphy data. It first uses a robust cosinor model to estimate circadian rhythm, then searches for a single change point (CP) within each cycle. We used CircaCP to estimate sleep/wake onset times (S/WOTs) from 2125 indviduals' data in the MESA Sleep study and compared the estimated S/WOTs against self-reported S/WOT event markers. Lastly, we quantified the biases between estimated and self-reported S/WOTs, as well as variation in S/WOTs contributed by the two methods, using linear mixed-effects models and variance component analysis.   On average, SOTs estimated by CircaCP were five minutes behind those reported by event markers, and WOTs estimated by CircaCP were less than one minute behind those reported by markers. These differences accounted for less than 0.2% variability in SOTs and in WOTs, taking into account other sources of between-subject variations. By focusing on the commonality in human circadian rhythms captured by actigraphy, our algorithm transferred seamlessly from hip-worn ActiGraph data collected from children in our previous study to wrist-worn Actiwatch data collected from adults. The large between- and within-subject variability highlights the need for estimating individual-level S/WOTs when conducting actigraphy research. The generalizability of our algorithm also suggests that it could be widely applied to actigraphy data collected by other wearable sensors.
## QA:
coming soon
