---
layout: '../../layouts/MarkdownPost.astro'
title: 'Ultra-Efficient On-Device Object Detection on AI-Integrated Smart Glasses with TinyissimoYOLO'
pubDate: 2023-11-06 21:53:47
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['wearable', 'smart band'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Julian Moosmann et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2311.01057v2
## download
[2311.01057v2](http://arxiv.org/abs/2311.01057v2)
## abstracts:
Smart glasses are rapidly gaining advanced functionality thanks to cutting-edge computing technologies, accelerated hardware architectures, and tiny AI algorithms. Integrating AI into smart glasses featuring a small form factor and limited battery capacity is still challenging when targeting full-day usage for a satisfactory user experience. This paper illustrates the design and implementation of tiny machine-learning algorithms exploiting novel low-power processors to enable prolonged continuous operation in smart glasses. We explore the energy- and latency-efficient of smart glasses in the case of real-time object detection. To this goal, we designed a smart glasses prototype as a research platform featuring two microcontrollers, including a novel milliwatt-power RISC-V parallel processor with a hardware accelerator for visual AI, and a Bluetooth low-power module for communication. The smart glasses integrate power cycling mechanisms, including image and audio sensing interfaces. Furthermore, we developed a family of novel tiny deep-learning models based on YOLO with sub-million parameters customized for microcontroller-based inference dubbed TinyissimoYOLO v1.3, v5, and v8, aiming at benchmarking object detection with smart glasses for energy and latency. Evaluations on the prototype of the smart glasses demonstrate TinyissimoYOLO's 17ms inference latency and 1.59mJ energy consumption per inference while ensuring acceptable detection accuracy. Further evaluation reveals an end-to-end latency from image capturing to the algorithm's prediction of 56ms or equivalently 18 fps, with a total power consumption of 62.9mW, equivalent to a 9.3 hours of continuous run time on a 154mAh battery. These results outperform MCUNet (TinyNAS+TinyEngine), which runs a simpler task (image classification) at just 7.3 fps per second.
## QA:
None
