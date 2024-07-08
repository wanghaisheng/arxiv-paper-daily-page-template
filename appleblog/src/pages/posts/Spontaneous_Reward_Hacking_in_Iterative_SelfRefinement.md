---
layout: '../../layouts/MarkdownPost.astro'
title: '**Spontaneous Reward Hacking in Iterative SelfRefinement**'
pubDate: '2024-07-09 07:52:44'
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: '['heart rate']' 
theme: 'light'
featured: true

meta:
 - name: author
   content: Jane Pan et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.04549v1
## download
[2407.04549v1](http://arxiv.org/abs/2407.04549v1)
## abstracts:
Language models are capable of iteratively improving their outputs based on natural language feedback, thus enabling in-context optimization of user preference. In place of human users, a second language model can be used as an evaluator, providing feedback along with numerical ratings which the generator attempts to optimize. However, because the evaluator is an imperfect proxy of user preference, this optimization can lead to reward hacking, where the evaluator's ratings improve while the generation quality remains stagnant or even decreases as judged by actual user preference. The concern of reward hacking is heightened in iterative self-refinement where the generator and the evaluator use the same underlying language model, in which case the optimization pressure can drive them to exploit shared vulnerabilities. Using an essay editing task, we show that iterative self-refinement leads to deviation between the language model evaluator and human judgment, demonstrating that reward hacking can occur spontaneously in-context with the use of iterative self-refinement. In addition, we study conditions under which reward hacking occurs and observe two factors that affect reward hacking severity: model size and context sharing between the generator and the evaluator.
## QA:
coming soon
