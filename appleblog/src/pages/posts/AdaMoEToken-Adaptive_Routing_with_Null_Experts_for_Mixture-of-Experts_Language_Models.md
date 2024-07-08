---
layout: '../../layouts/MarkdownPost.astro'
title: 'AdaMoE: Token-Adaptive Routing with Null Experts for Mixture-of-Experts Language Models'
pubDate: 2024-07-09 04:44:23
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
   content: Zihao Zeng et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.13233v1
## download
[2406.13233v1](http://arxiv.org/abs/2406.13233v1)
## abstracts:
Mixture of experts (MoE) has become the standard for constructing production-level large language models (LLMs) due to its promise to boost model capacity without causing significant overheads. Nevertheless, existing MoE methods usually enforce a constant top-k routing for all tokens, which is arguably restrictive because various tokens (e.g., "<EOS>" vs. "apple") may require various numbers of experts for feature abstraction. Lifting such a constraint can help make the most of limited resources and unleash the potential of the model for downstream tasks. In this sense, we introduce AdaMoE to realize token-adaptive routing for MoE, where different tokens are permitted to select a various number of experts. AdaMoE makes minimal modifications to the vanilla MoE with top-k routing -- it simply introduces a fixed number of null experts, which do not consume any FLOPs, to the expert set and increases the value of k. AdaMoE does not force each token to occupy a fixed number of null experts but ensures the average usage of the null experts with a load-balancing loss, leading to an adaptive number of null/true experts used by each token. AdaMoE exhibits a strong resemblance to MoEs with expert choice routing while allowing for trivial auto-regressive modeling. AdaMoE is easy to implement and can be effectively applied to pre-trained (MoE-)LLMs. Extensive studies show that AdaMoE can reduce average expert load (FLOPs) while achieving superior performance. For example, on the ARC-C dataset, applying our method to fine-tuning Mixtral-8x7B can reduce FLOPs by 14.5% while increasing accuracy by 1.69%.
## QA:
coming soon