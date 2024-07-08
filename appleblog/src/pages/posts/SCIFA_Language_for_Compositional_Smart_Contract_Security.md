---
layout: '../../layouts/MarkdownPost.astro'
title: '**SCIF: A Language for Compositional Smart Contract Security**'
pubDate: '2024-07-09 06:30:53'
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
   content: Siqiu Yao et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.01204v1
## download
[2407.01204v1](http://arxiv.org/abs/2407.01204v1)
## abstracts:
Securing smart contracts remains a fundamental challenge. At its core, it is about building software that is secure in composition with untrusted code, a challenge that extends far beyond blockchains. We introduce SCIF, a language for building smart contracts that are compositionally secure. SCIF is based on the fundamentally compositional principle of secure information flow, but extends this core mechanism to include protection against reentrancy attacks, confused deputy attacks, and improper error handling, even in the presence of malicious contracts that do not follow SCIF's rules. SCIF supports a rich ecosystem of interacting principals with partial trust through its mechanisms for dynamic trust management. SCIF has been implemented as a compiler to Solidity. We describe the SCIF language, including its static checking rules and runtime. Finally, we implement several applications with intricate security reasoning, showing how SCIF supports building complex smart contracts securely and gives programmer accurate diagnostics about potential security bugs.
## QA:
coming soon
