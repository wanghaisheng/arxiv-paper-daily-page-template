---
layout: '../../layouts/MarkdownPost.astro'
title: "**Smart Casual Verification of CCFs Distributed Consensus and Consistency Protocols**"
pubDate: "2024-07-09 07:47:23"
description: ''
author: "wanghaisheng"
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: "['smart watch']"
theme: 'light'
featured: true

meta:
 - name: author
   content: Heidi Howard et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.17455v1
## download
[2406.17455v1](http://arxiv.org/abs/2406.17455v1)
## abstracts:
The Confidential Consortium Framework (CCF) is an open-source platform for developing trustworthy and reliable cloud applications. CCF powers Microsoft's Azure Confidential Ledger service and as such it is vital to build confidence in the correctness of CCF's design and implementation. This paper reports our experiences applying smart casual verification to validate the correctness of CCF's novel distributed protocols, focusing on its unique distributed consensus protocol and its custom client consistency model. We use the term smart casual verification to describe our hybrid approach, which combines the rigor of formal specification and model checking with the pragmatism of automated testing, in our case binding the formal specification in TLA+ to the C++ implementation. While traditional formal methods approaches require substantial buy-in and are often one-off efforts by domain experts, we have integrated our smart casual verification approach into CCF's continuous integration pipeline, allowing contributors to continuously validate CCF as it evolves. We describe the challenges we faced in applying smart casual verification to a complex existing codebase and how we overcame them to find subtle bugs in the design and implementation before they could impact production.
## QA:
coming soon
