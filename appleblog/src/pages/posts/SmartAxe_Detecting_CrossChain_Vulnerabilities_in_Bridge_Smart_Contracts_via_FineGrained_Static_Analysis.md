---
author: wanghaisheng
cover:
  alt: cover
  square: https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg
  url: https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg
description: ''
featured: true
keywords: key1, key2, key3
layout: ../../layouts/MarkdownPost.astro
meta:
- content: Zeqin Liao et.al.
  name: author
- content: key3, key4
  name: keywords
pubDate: '2024-07-09 08:29:34'
tags:
- smart watch
theme: light
title: SmartAxe Detecting CrossChain Vulnerabilities in Bridge Smart Contracts via
  FineGrained Static Analysis
---

# title: SmartAxe Detecting CrossChain Vulnerabilities in Bridge Smart Contracts via FineGrained Static Analysis 
## publish date: 
**2024-06-23** 
## authors: 
  Zeqin Liao et.al. 
## paper id
2406.15999v1
## download
[2406.15999v1](http://arxiv.org/abs/2406.15999v1)
## abstracts:
With the increasing popularity of blockchain, different blockchain platforms coexist in the ecosystem (e.g., Ethereum, BNB, EOSIO, etc.), which prompts the high demand for cross-chain communication. Cross-chain bridge is a specific type of decentralized application for asset exchange across different blockchain platforms. Securing the smart contracts of cross-chain bridges is in urgent need, as there are a number of recent security incidents with heavy financial losses caused by vulnerabilities in bridge smart contracts, as we call them Cross-Chain Vulnerabilities (CCVs). However, automatically identifying CCVs in smart contracts poses several unique challenges. Particularly, it is non-trivial to (1) identify application-specific access control constraints needed for cross-bridge asset exchange, and (2) identify inconsistent cross-chain semantics between the two sides of the bridge.   In this paper, we propose SmartAxe, a new framework to identify vulnerabilities in cross-chain bridge smart contracts. Particularly, to locate vulnerable functions that have access control incompleteness, SmartAxe models the heterogeneous implementations of access control and finds necessary security checks in smart contracts through probabilistic pattern inference. Besides, SmartAxe constructs cross-chain control-flow graph (xCFG) and data-flow graph (xDFG), which help to find semantic inconsistency during cross-chain data communication. To evaluate SmartAxe, we collect and label a dataset of 88 CCVs from real-attacks cross-chain bridge contracts. Evaluation results show that SmartAxe achieves a precision of 84.95% and a recall of 89.77%. In addition, SmartAxe successfully identifies 232 new/unknown CCVs from 129 real-world cross-chain bridge applications (i.e., from 1,703 smart contracts). These identified CCVs affect a total amount of digital assets worth 1,885,250 USD.
## QA:
coming soon
