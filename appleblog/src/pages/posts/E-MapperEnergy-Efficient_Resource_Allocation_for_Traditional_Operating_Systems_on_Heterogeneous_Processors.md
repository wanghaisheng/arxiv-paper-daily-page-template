---
layout: '../../layouts/MarkdownPost.astro'
title: 'E-Mapper: Energy-Efficient Resource Allocation for Traditional Operating Systems on Heterogeneous Processors'
pubDate: 2024-07-09 04:44:20
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
   content: Till Smejkal et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.18980v1
## download
[2406.18980v1](http://arxiv.org/abs/2406.18980v1)
## abstracts:
Energy efficiency has become a key concern in modern computing. Major processor vendors now offer heterogeneous architectures that combine powerful cores with energy-efficient ones, such as Intel P/E systems, Apple M1 chips, and Samsungs Exyno's CPUs. However, apart from simple cost-based thread allocation strategies, today's OS schedulers do not fully exploit these systems' potential for adaptive energy-efficient computing. This is, in part, due to missing application-level interfaces to pass information about task-level energy consumption and application-level elasticity. This paper presents E-Mapper, a novel resource management approach integrated into Linux for improved execution on heterogeneous processors. In E-Mapper, we base resource allocation decisions on high-level application descriptions that user can attach to programs or that the system can learn automatically at runtime. Our approach supports various programming models including OpenMP, Intel TBB, and TensorFlow. Crucially, E-Mapper leverages this information to extend beyond existing thread-to-core allocation strategies by actively managing application configurations through a novel uniform application-resource manager interface. By doing so, E-Mapper achieves substantial enhancements in both performance and energy efficiency, particularly in multi-application scenarios. On an Intel Raptor Lake and an Arm big.LITTLE system, E-Mapper reduces the application execution on average by 20 % with an average reduction in energy consumption of 34 %. We argue that our solution marks a crucial step toward creating a generic approach for sustainable and efficient computing across different processor architectures.
## QA:
coming soon
