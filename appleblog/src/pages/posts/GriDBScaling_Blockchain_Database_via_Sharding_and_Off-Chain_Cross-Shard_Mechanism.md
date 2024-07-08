---
layout: '../../layouts/MarkdownPost.astro'
title: 'GriDB: Scaling Blockchain Database via Sharding and Off-Chain Cross-Shard Mechanism'
pubDate: 2024-07-09 04:44:11
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
   content: Zicong Hong et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.03750v1
## download
[2407.03750v1](http://arxiv.org/abs/2407.03750v1)
## abstracts:
Blockchain databases have attracted widespread attention but suffer from poor scalability due to underlying non-scalable blockchains. While blockchain sharding is necessary for a scalable blockchain database, it poses a new challenge named on-chain cross-shard database services. Each cross-shard database service (e.g., cross-shard queries or inter-shard load balancing) involves massive cross-shard data exchanges, while the existing cross-shard mechanisms need to process each cross-shard data exchange via the consensus of all nodes in the related shards (i.e., on-chain) to resist a Byzantine environment of blockchain, which eliminates sharding benefits. To tackle the challenge, this paper presents GriDB, the first scalable blockchain database, by designing a novel off-chain cross-shard mechanism for efficient cross-shard database services. Borrowing the idea of off-chain payments, GriDB delegates massive cross-shard data exchange to a few nodes, each of which is randomly picked from a different shard. Considering the Byzantine environment, the untrusted delegates cooperate to generate succinct proof for cross-shard data exchanges, while the consensus is only responsible for the low-cost proof verification. However, different from payments, the database services' verification has more requirements (e.g., completeness, correctness, freshness, and availability); thus, we introduce several new authenticated data structures (ADS). Particularly, we utilize consensus to extend the threat model and reduce the complexity of traditional accumulator-based ADS for verifiable cross-shard queries with a rich set of relational operators. Moreover, we study the necessity of inter-shard load balancing for a scalable blockchain database and design an off-chain and live approach for both efficiency and availability during balancing.
## QA:
coming soon
