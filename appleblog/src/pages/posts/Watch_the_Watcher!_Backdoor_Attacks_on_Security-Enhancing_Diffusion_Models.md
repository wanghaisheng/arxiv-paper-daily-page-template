---
layout: '../../layouts/MarkdownPost.astro'
title: '**Watch the Watcher! Backdoor Attacks on Security-Enhancing Diffusion Models**'
pubDate: '2024-07-09 06:26:26'
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: '['apple', 'apple watch']' 
theme: 'light'
featured: true

meta:
 - name: author
   content: Changjiang Li et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.09669v1
## download
[2406.09669v1](http://arxiv.org/abs/2406.09669v1)
## abstracts:
Thanks to their remarkable denoising capabilities, diffusion models are increasingly being employed as defensive tools to reinforce the security of other models, notably in purifying adversarial examples and certifying adversarial robustness. However, the security risks of these practices themselves remain largely unexplored, which is highly concerning. To bridge this gap, this work investigates the vulnerabilities of security-enhancing diffusion models. Specifically, we demonstrate that these models are highly susceptible to DIFF2, a simple yet effective backdoor attack, which substantially diminishes the security assurance provided by such models. Essentially, DIFF2 achieves this by integrating a malicious diffusion-sampling process into the diffusion model, guiding inputs embedded with specific triggers toward an adversary-defined distribution while preserving the normal functionality for clean inputs. Our case studies on adversarial purification and robustness certification show that DIFF2 can significantly reduce both post-purification and certified accuracy across benchmark datasets and models, highlighting the potential risks of relying on pre-trained diffusion models as defensive tools. We further explore possible countermeasures, suggesting promising avenues for future research.
## QA:
coming soon
