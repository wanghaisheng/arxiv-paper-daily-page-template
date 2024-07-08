---
layout: '../../layouts/MarkdownPost.astro'
title: '**ConvoCache: Smart Re-Use of Chatbot Responses**'
pubDate: '2024-07-09 06:58:24'
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: '['smart watch']' 
theme: 'light'
featured: true

meta:
 - name: author
   content: Conor Atkins et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.18133v1
## download
[2406.18133v1](http://arxiv.org/abs/2406.18133v1)
## abstracts:
We present ConvoCache, a conversational caching system that solves the problem of slow and expensive generative AI models in spoken chatbots. ConvoCache finds a semantically similar prompt in the past and reuses the response. In this paper we evaluate ConvoCache on the DailyDialog dataset. We find that ConvoCache can apply a UniEval coherence threshold of 90% and respond to 89% of prompts using the cache with an average latency of 214ms, replacing LLM and voice synthesis that can take over 1s. To further reduce latency we test prefetching and find limited usefulness. Prefetching with 80% of a request leads to a 63% hit rate, and a drop in overall coherence. ConvoCache can be used with any chatbot to reduce costs by reducing usage of generative AI by up to 89%.
## QA:
coming soon
