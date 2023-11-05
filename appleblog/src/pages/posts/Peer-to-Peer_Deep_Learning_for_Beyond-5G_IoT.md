---
layout: '../../layouts/MarkdownPost.astro'
title: 'Peer-to-Peer Deep Learning for Beyond-5G IoT'
pubDate: 2023-11-05 23:16:11
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['smart watch', 'wearable'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Srinivasa Pranav et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## abstracts:
We present P2PL, a practical multi-device peer-to-peer deep learning algorithm that, unlike the federated learning paradigm, does not require coordination from edge servers or the cloud. This makes P2PL well-suited for the sheer scale of beyond-5G computing environments like smart cities that otherwise create range, latency, bandwidth, and single point of failure issues for federated approaches.   P2PL introduces max norm synchronization to catalyze training, retains on-device deep model training to preserve privacy, and leverages local inter-device communication to implement distributed consensus. Each device iteratively alternates between two phases: 1) on-device learning and 2) distributed cooperation where they combine model parameters with nearby devices. We empirically show that all participating devices achieve the same test performance attained by federated and centralized training -- even with 100 devices and relaxed singly stochastic consensus weights. We extend these experimental results to settings with diverse network topologies, sparse and intermittent communication, and non-IID data distributions.
