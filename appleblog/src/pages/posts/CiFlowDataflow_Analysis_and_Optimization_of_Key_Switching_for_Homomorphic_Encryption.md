---
layout: '../../layouts/MarkdownPost.astro'
title: 'CiFlow: Dataflow Analysis and Optimization of Key Switching for Homomorphic Encryption'
pubDate: 2023-11-06 21:53:37
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['wearable', 'smart ring'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Negar Neda et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2311.01598v1
## download
[2311.01598v1](http://arxiv.org/abs/2311.01598v1)
## abstracts:
Homomorphic encryption (HE) is a privacy-preserving computation technique that enables computation on encrypted data. Today, the potential of HE remains largely unrealized as it is impractically slow, preventing it from being used in real applications. A major computational bottleneck in HE is the key-switching operation, accounting for approximately 70% of the overall HE execution time and involving a large amount of data for inputs, intermediates, and keys. Prior research has focused on hardware accelerators to improve HE performance, typically featuring large on-chip SRAMs and high off-chip bandwidth to deal with large scale data. In this paper, we present a novel approach to improve key-switching performance by rigorously analyzing its dataflow. Our primary goal is to optimize data reuse with limited on-chip memory to minimize off-chip data movement. We introduce three distinct dataflows: Max-Parallel (MP), Digit-Centric (DC), and Output-Centric (OC), each with unique scheduling approaches for key-switching computations. Through our analysis, we show how our proposed Output-Centric technique can effectively reuse data by significantly lowering the intermediate key-switching working set and alleviating the need for massive off-chip bandwidth. We thoroughly evaluate the three dataflows using the RPU, a recently published vector processor tailored for ring processing algorithms, which includes HE. This evaluation considers sweeps of bandwidth and computational throughput, and whether keys are buffered on-chip or streamed. With OC, we demonstrate up to 4.16x speedup over the MP dataflow and show how OC can save 16x on-chip SRAM by streaming keys for minimal performance penalty.
## QA:
None
