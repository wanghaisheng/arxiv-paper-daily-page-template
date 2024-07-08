---
layout: '../../layouts/MarkdownPost.astro'
title: 'The Fall of ROME: Understanding the Collapse of LLMs in Model Editing'
pubDate: 2024-07-09 04:44:15
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['huawei', 'huawei watch'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Wanli Yang et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.11263v1
## download
[2406.11263v1](http://arxiv.org/abs/2406.11263v1)
## abstracts:
Despite significant progress in model editing methods, their application in real-world scenarios remains challenging as they often cause large language models (LLMs) to collapse. Among them, ROME is particularly concerning, as it could disrupt LLMs with only a single edit. In this paper, we study the root causes of such collapse. Through extensive analysis, we identify two primary factors that contribute to the collapse: i) inconsistent handling of prefixed and unprefixed keys in the parameter update equation may result in very small denominators, causing excessively large parameter updates; ii) the subject of collapse cases is usually the first token, whose unprefixed key distribution significantly differs from the prefixed key distribution in autoregressive transformers, causing the aforementioned issue to materialize. To validate our analysis, we propose a simple yet effective approach: uniformly using prefixed keys during editing phase and adding prefixes during the testing phase. The experimental results show that the proposed solution can prevent model collapse while maintaining the effectiveness of the edits.
## QA:
coming soon
