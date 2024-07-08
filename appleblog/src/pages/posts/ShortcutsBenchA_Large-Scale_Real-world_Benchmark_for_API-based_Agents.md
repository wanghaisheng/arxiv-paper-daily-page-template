---
layout: '../../layouts/MarkdownPost.astro'
title: 'ShortcutsBench: A Large-Scale Real-world Benchmark for API-based Agents'
pubDate: 2024-07-09 05:10:28
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['apple watch', 'apple'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Haiyang Shen et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.00132v1
## download
[2407.00132v1](http://arxiv.org/abs/2407.00132v1)
## abstracts:
Recent advancements in integrating large language models (LLMs) with application programming interfaces (APIs) have gained significant interest in both academia and industry. These API-based agents, leveraging the strong autonomy and planning capabilities of LLMs, can efficiently solve problems requiring multi-step actions. However, their ability to handle multi-dimensional difficulty levels, diverse task types, and real-world demands through APIs remains unknown. In this paper, we introduce \textsc{ShortcutsBench}, a large-scale benchmark for the comprehensive evaluation of API-based agents in solving tasks with varying levels of difficulty, diverse task types, and real-world demands. \textsc{ShortcutsBench} includes a wealth of real APIs from Apple Inc.'s operating systems, refined user queries from shortcuts, human-annotated high-quality action sequences from shortcut developers, and accurate parameter filling values about primitive parameter types, enum parameter types, outputs from previous actions, and parameters that need to request necessary information from the system or user. Our extensive evaluation of agents built with $5$ leading open-source (size >= 57B) and $4$ closed-source LLMs (e.g. Gemini-1.5-Pro and GPT-3.5) reveals significant limitations in handling complex queries related to API selection, parameter filling, and requesting necessary information from systems and users. These findings highlight the challenges that API-based agents face in effectively fulfilling real and complex user queries. All datasets, code, and experimental results will be available at \url{https://github.com/eachsheep/shortcutsbench}.
## QA:
coming soon
