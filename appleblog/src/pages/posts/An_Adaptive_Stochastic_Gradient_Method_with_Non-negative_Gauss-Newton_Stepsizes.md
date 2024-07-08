---
layout: '../../layouts/MarkdownPost.astro'
title: '**An Adaptive Stochastic Gradient Method with Non-negative Gauss-Newton Stepsizes**'
pubDate: '2024-07-09 06:42:04'
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
   content: Antonio Orvieto et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.04358v1
## download
[2407.04358v1](http://arxiv.org/abs/2407.04358v1)
## abstracts:
We consider the problem of minimizing the average of a large number of smooth but possibly non-convex functions. In the context of most machine learning applications, each loss function is non-negative and thus can be expressed as the composition of a square and its real-valued square root. This reformulation allows us to apply the Gauss-Newton method, or the Levenberg-Marquardt method when adding a quadratic regularization. The resulting algorithm, while being computationally as efficient as the vanilla stochastic gradient method, is highly adaptive and can automatically warmup and decay the effective stepsize while tracking the non-negative loss landscape. We provide a tight convergence analysis, leveraging new techniques, in the stochastic convex and non-convex settings. In particular, in the convex case, the method does not require access to the gradient Lipshitz constant for convergence, and is guaranteed to never diverge. The convergence rates and empirical evaluations compare favorably to the classical (stochastic) gradient method as well as to several other adaptive methods.
## QA:
coming soon
