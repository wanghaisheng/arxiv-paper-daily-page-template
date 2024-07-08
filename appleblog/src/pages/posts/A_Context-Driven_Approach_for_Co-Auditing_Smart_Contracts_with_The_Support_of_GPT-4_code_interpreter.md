---
layout: '../../layouts/MarkdownPost.astro'
title: '**A Context-Driven Approach for Co-Auditing Smart Contracts with The Support of GPT-4 code interpreter**'
pubDate: '2024-07-09 06:58:25'
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
   content: Mohamed Salah Bouafif et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.18075v1
## download
[2406.18075v1](http://arxiv.org/abs/2406.18075v1)
## abstracts:
The surge in the adoption of smart contracts necessitates rigorous auditing to ensure their security and reliability. Manual auditing, although comprehensive, is time-consuming and heavily reliant on the auditor's expertise. With the rise of Large Language Models (LLMs), there is growing interest in leveraging them to assist auditors in the auditing process (co-auditing). However, the effectiveness of LLMs in smart contract co-auditing is contingent upon the design of the input prompts, especially in terms of context description and code length. This paper introduces a novel context-driven prompting technique for smart contract co-auditing. Our approach employs three techniques for context scoping and augmentation, encompassing code scoping to chunk long code into self-contained code segments based on code inter-dependencies, assessment scoping to enhance context description based on the target assessment goal, thereby limiting the search space, and reporting scoping to force a specific format for the generated response. Through empirical evaluations on publicly available vulnerable contracts, our method demonstrated a detection rate of 96\% for vulnerable functions, outperforming the native prompting approach, which detected only 53\%. To assess the reliability of our prompting approach, manual analysis of the results was conducted by expert auditors from our partner, Quantstamp, a world-leading smart contract auditing company. The experts' analysis indicates that, in unlabeled datasets, our proposed approach enhances the proficiency of the GPT-4 code interpreter in detecting vulnerabilities.
## QA:
coming soon
