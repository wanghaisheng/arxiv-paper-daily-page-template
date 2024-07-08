---
layout: '../../layouts/MarkdownPost.astro'
title: "**Langevin Dynamics: A Unified Perspective on Optimization via Lyapunov Potentials**"
pubDate: "2024-07-09 07:03:14"
description: ''
author: "wanghaisheng"
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: "['heart rate']" 
theme: 'light'
featured: true

meta:
 - name: author
   content: August Y. Chen et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.04264v1
## download
[2407.04264v1](http://arxiv.org/abs/2407.04264v1)
## abstracts:
We study the problem of non-convex optimization using Stochastic Gradient Langevin Dynamics (SGLD). SGLD is a natural and popular variation of stochastic gradient descent where at each step, appropriately scaled Gaussian noise is added. To our knowledge, the only strategy for showing global convergence of SGLD on the loss function is to show that SGLD can sample from a stationary distribution which assigns larger mass when the function is small (the Gibbs measure), and then to convert these guarantees to optimization results.   We employ a new strategy to analyze the convergence of SGLD to global minima, based on Lyapunov potentials and optimization. We convert the same mild conditions from previous works on SGLD into geometric properties based on Lyapunov potentials. This adapts well to the case with a stochastic gradient oracle, which is natural for machine learning applications where one wants to minimize population loss but only has access to stochastic gradients via minibatch training samples. Here we provide 1) improved rates in the setting of previous works studying SGLD for optimization, 2) the first finite gradient complexity guarantee for SGLD where the function is Lipschitz and the Gibbs measure defined by the function satisfies a Poincar\'e Inequality, and 3) prove if continuous-time Langevin Dynamics succeeds for optimization, then discrete-time SGLD succeeds under mild regularity assumptions.
## QA:
coming soon
