---
layout: '../../layouts/MarkdownPost.astro'
title: 'A Bayesian Circadian Hidden Markov Model to Infer Rest-Activity Rhythms Using 24-hour Actigraphy Data'
pubDate: 2024-07-09 04:43:49
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
   content: Jiachen Lu et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2307.03832v1
## download
[2307.03832v1](http://arxiv.org/abs/2307.03832v1)
## abstracts:
24-hour actigraphy data collected by wearable devices offer valuable insights into physical activity types, intensity levels, and rest-activity rhythms (RAR). RARs, or patterns of rest and activity exhibited over a 24-hour period, are regulated by the body's circadian system, synchronizing physiological processes with external cues like the light-dark cycle. Disruptions to these rhythms, such as irregular sleep patterns, daytime drowsiness or shift work, have been linked to adverse health outcomes including metabolic disorders, cardiovascular disease, depression, and even cancer, making RARs a critical area of health research.   In this study, we propose a Bayesian Circadian Hidden Markov Model (BCHMM) that explicitly incorporates 24-hour circadian oscillators mirroring human biological rhythms. The model assumes that observed activity counts are conditional on hidden activity states through Gaussian emission densities, with transition probabilities modeled by state-specific sinusoidal functions. Our comprehensive simulation study reveals that BCHMM outperforms frequentist approaches in identifying the underlying hidden states, particularly when the activity states are difficult to separate. BCHMM also excels with smaller Kullback-Leibler divergence on estimated densities. With the Bayesian framework, we address the label-switching problem inherent to hidden Markov models via a positive constraint on mean parameters. From the proposed BCHMM, we can infer the 24-hour rest-activity profile via time-varying state probabilities, to characterize the person-level RAR. We demonstrate the utility of the proposed BCHMM using 2011-2014 National Health and Nutrition Examination Survey (NHANES) data, where worsened RAR, indicated by lower probabilities in low-activity state during the day and higher probabilities in high-activity state at night, is associated with an increased risk of diabetes.
## QA:
coming soon
