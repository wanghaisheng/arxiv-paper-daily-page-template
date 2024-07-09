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
title: SmartState Detecting StateReverting Vulnerabilities in Smart Contracts via
  FineGrained StateDependency Analysis
---

# title: SmartState Detecting StateReverting Vulnerabilities in Smart Contracts via FineGrained StateDependency Analysis 
## publish date: 
**2024-06-23** 
## authors: 
  Zeqin Liao et.al. 
## paper id
2406.15988v1
## download
[2406.15988v1](http://arxiv.org/abs/2406.15988v1)
## abstracts:
Smart contracts written in Solidity are widely used in different blockchain platforms such as Ethereum, TRON and BNB Chain. One of the unique designs in Solidity smart contracts is its state-reverting mechanism for error handling and access control. Unfortunately, a number of recent security incidents showed that adversaries also utilize this mechanism to manipulate critical states of smart contracts, and hence, bring security consequences such as illegal profit-gain and Deny-of-Service (DoS). In this paper, we call such vulnerabilities as the State-reverting Vulnerability (SRV). Automatically identifying SRVs poses unique challenges, as it requires an in-depth analysis and understanding of the state-dependency relations in smart contracts.   This paper presents SmartState, a new framework for detecting state-reverting vulnerability in Solidity smart contracts via fine-grained state-dependency analysis. SmartState integrates a set of novel mechanisms to ensure its effectiveness. Particularly, Smart-State extracts state dependencies from both contract bytecode and historical transactions. Both of them are critical for inferring dependencies related to SRVs. Further, SmartState models the generic patterns of SRVs (i.e., profit-gain and DoS) as SRV indicators, and hence effectively identify SRVs based on the constructed state-dependency graph. To evaluate SmartState, we manually annotated a ground-truth dataset which contains 91 SRVs in the real world. Evaluation results showed that SmartState achieves a precision of 87.23% and a recall of 89.13%. In addition, SmartState successfully identifies 406 new SRVs from 47,351 real-world smart contracts. 11 of these SRVs are from popular smart contracts with high transaction amounts (i.e., top 2000). In total, our reported SRVs affect a total amount of digital assets worth 428,600 USD.
## QA:
coming soon
