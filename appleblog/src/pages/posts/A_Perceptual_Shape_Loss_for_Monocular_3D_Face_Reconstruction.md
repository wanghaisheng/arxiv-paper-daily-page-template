---
layout: '../../layouts/MarkdownPost.astro'
title: 'A Perceptual Shape Loss for Monocular 3D Face Reconstruction'
pubDate: 2023-11-06 21:53:32
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['wearable', 'smart watch'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Christopher Otto et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2310.19580v1
## download
[2310.19580v1](http://arxiv.org/abs/2310.19580v1)
## abstracts:
Monocular 3D face reconstruction is a wide-spread topic, and existing approaches tackle the problem either through fast neural network inference or offline iterative reconstruction of face geometry. In either case carefully-designed energy functions are minimized, commonly including loss terms like a photometric loss, a landmark reprojection loss, and others. In this work we propose a new loss function for monocular face capture, inspired by how humans would perceive the quality of a 3D face reconstruction given a particular image. It is widely known that shading provides a strong indicator for 3D shape in the human visual system. As such, our new 'perceptual' shape loss aims to judge the quality of a 3D face estimate using only shading cues. Our loss is implemented as a discriminator-style neural network that takes an input face image and a shaded render of the geometry estimate, and then predicts a score that perceptually evaluates how well the shaded render matches the given image. This 'critic' network operates on the RGB image and geometry render alone, without requiring an estimate of the albedo or illumination in the scene. Furthermore, our loss operates entirely in image space and is thus agnostic to mesh topology. We show how our new perceptual shape loss can be combined with traditional energy terms for monocular 3D face optimization and deep neural network regression, improving upon current state-of-the-art results.
## QA:
None
