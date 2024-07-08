---
layout: '../../layouts/MarkdownPost.astro'
title: "**Position and Altitude of the Nao Camera Head from Two Points on the Soccer Field plus the Gravitational Direction**"
pubDate: "2024-07-09 07:03:46"
description: ''
author: "wanghaisheng"
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: "['camera', 'wearable camera']" 
theme: 'light'
featured: true

meta:
 - name: author
   content: Stijn Oomes et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.03041v1
## download
[2407.03041v1](http://arxiv.org/abs/2407.03041v1)
## abstracts:
To be able to play soccer, a robot needs a good estimate of its current position on the field. Ideally, multiple features are visible that have known locations. By applying trigonometry we can estimate the viewpoint from where this observation was actually made. Given that the Nao robots of the Standard Platform League have quite a limited field of view, a given camera frame typically only allows for one or two points to be recognized.   In this paper we propose a method for determining the (x, y) coordinates on the field and the height h of the camera from the geometry of a simplified tetrahedron. This configuration is formed by two observed points on the ground plane plus the gravitational direction. When the distance between the two points is known, and the directions to the points plus the gravitational direction are measured, all dimensions of the tetrahedron can be determined.   By performing these calculations with rational trigonometry instead of classical trigonometry, the computations turn out to be 28.7% faster, with equal numerical accuracy. The position of the head of the Nao can also be externally measured with the OptiTrack system. The difference between externally measured and internally predicted position from sensor data gives us mean absolute errors in the 3-6 centimeters range, when we estimated the gravitational direction from the vanishing point of the outer edges of the goal posts.
## QA:
coming soon
