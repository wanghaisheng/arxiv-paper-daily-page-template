---
layout: '../../layouts/MarkdownPost.astro'
title: 'Improving full-waveform inversion based on sparse regularisation for geophysical data'
pubDate: 2023-11-06 21:53:42
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
   content: Jiahang Li et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2311.01688v1
## download
[2311.01688v1](http://arxiv.org/abs/2311.01688v1)
## abstracts:
Full Waveform Inversion (FWI) is an advanced geophysical inversion technique. In fields such as oil exploration and geology, FWI is used for providing images of subsurface structures with higher resolution. The conventional algorithm minimises the misfit error by calculating the least squares of the wavefield solutions between observed data and simulated data, followed by gradient direction and model update increment. Since the gradient is calculated by forward and backward wavefields, the high-accuracy model update relies on accurate forward and backward wavefield modelling. However, the quality of wavefield solutions obtained in practical situations could be poor and does not meet the requirements of high-resolution FWI. Specifically, the low-frequency wavefield is easily affected by noise and downsampling, which influences data quality, while the high-frequency wavefield is susceptible to spatial aliasing effects that produce imaging artefacts. Therefore, we propose using an algorithm called Sparse Relaxation Regularised Regression to optimise the wavefield solution in frequency domain FWI, which is the forward and backward wavefield obtained from the Helmholtz equation, and thus improve the accuracy of the FWI. The sparse relaxed regularised regression algorithm combines sparsity and regularisation, allowing the broadband FWI to reduce the effects of noise and outliers, which can provide data supplementation in the low-frequency band and anti-aliasing in the high-frequency band. Our numerical examples demonstrate the wavefield optimization effect of the sparse relaxed regularised regression-based algorithm in various cases. The accuracy and stability of the improved algorithm are verified in comparison to the Tikhonov regularisation algorithm.
## QA:
None
