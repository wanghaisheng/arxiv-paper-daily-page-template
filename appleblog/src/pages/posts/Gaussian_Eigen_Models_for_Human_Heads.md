---
layout: '../../layouts/MarkdownPost.astro'
title: '**Gaussian Eigen Models for Human Heads**'
pubDate: '2024-07-09 06:43:17'
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: '['wearable device']' 
theme: 'light'
featured: true

meta:
 - name: author
   content: Wojciech Zielonka et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.04545v1
## download
[2407.04545v1](http://arxiv.org/abs/2407.04545v1)
## abstracts:
We present personalized Gaussian Eigen Models (GEMs) for human heads, a novel method that compresses dynamic 3D Gaussians into low-dimensional linear spaces. Our approach is inspired by the seminal work of Blanz and Vetter, where a mesh-based 3D morphable model (3DMM) is constructed from registered meshes. Based on dynamic 3D Gaussians, we create a lower-dimensional representation of primitives that applies to most 3DGS head avatars. Specifically, we propose a universal method to distill the appearance of a mesh-controlled UNet Gaussian avatar using an ensemble of linear eigenbasis. We replace heavy CNN-based architectures with a single linear layer improving speed and enabling a range of real-time downstream applications. To create a particular facial expression, one simply needs to perform a dot product between the eigen coefficients and the distilled basis. This efficient method removes the requirement for an input mesh during testing, enhancing simplicity and speed in expression generation. This process is highly efficient and supports real-time rendering on everyday devices, leveraging the effectiveness of standard Gaussian Splatting. In addition, we demonstrate how the GEM can be controlled using a ResNet-based regression architecture. We show and compare self-reenactment and cross-person reenactment to state-of-the-art 3D avatar methods, demonstrating higher quality and better control. A real-time demo showcases the applicability of the GEM representation.
## QA:
coming soon
