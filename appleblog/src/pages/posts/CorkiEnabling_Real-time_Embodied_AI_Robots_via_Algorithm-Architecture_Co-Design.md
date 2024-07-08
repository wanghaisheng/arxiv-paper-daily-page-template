---
layout: '../../layouts/MarkdownPost.astro'
title: '**Corki: Enabling Real-time Embodied AI Robots via Algorithm-Architecture Co-Design**'
pubDate: '2024-07-09 06:42:05'
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
   content: Yiyang Huang et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.04292v1
## download
[2407.04292v1](http://arxiv.org/abs/2407.04292v1)
## abstracts:
Embodied AI robots have the potential to fundamentally improve the way human beings live and manufacture. Continued progress in the burgeoning field of using large language models to control robots depends critically on an efficient computing substrate. In particular, today's computing systems for embodied AI robots are designed purely based on the interest of algorithm developers, where robot actions are divided into a discrete frame-basis. Such an execution pipeline creates high latency and energy consumption. This paper proposes Corki, an algorithm-architecture co-design framework for real-time embodied AI robot control. Our idea is to decouple LLM inference, robotic control and data communication in the embodied AI robots compute pipeline. Instead of predicting action for one single frame, Corki predicts the trajectory for the near future to reduce the frequency of LLM inference. The algorithm is coupled with a hardware that accelerates transforming trajectory into actual torque signals used to control robots and an execution pipeline that parallels data communication with computation. Corki largely reduces LLM inference frequency by up to 8.0x, resulting in up to 3.6x speed up. The success rate improvement can be up to 17.3%. Code is provided for re-implementation. https://github.com/hyy0613/Corki
## QA:
coming soon
