---
layout: '../../layouts/MarkdownPost.astro'
title: 'Modeling and LQR Control of Insect Sized Flapping Wing Robot'
pubDate: 2024-07-09 04:44:19
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['apple watch', 'apple'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Daksh Dhingra et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2406.20061v1
## download
[2406.20061v1](http://arxiv.org/abs/2406.20061v1)
## abstracts:
Flying insects can perform rapid, sophisticated maneuvers like backflips, sharp banked turns, and in-flight collision recovery. To emulate these in aerial robots weighing less than a gram, known as flying insect robots (FIRs), a fast and responsive control system is essential. To date, these have largely been, at their core, elaborations of proportional-integral-derivative (PID)-type feedback control. Without exception, their gains have been painstakingly tuned by hand. Aggressive maneuvers have further required task-specific tuning. Optimal control has the potential to mitigate these issues, but has to date only been demonstrated using approxiate models and receding horizon controllers (RHC) that are too computationally demanding to be carried out onboard the robot. Here we used a more accurate stroke-averaged model of forces and torques to implement the first demonstration of optimal control on an FIR that is computationally efficient enough to be performed by a microprocessor carried onboard. We took force and torque measurements from a 150 mg FIR, the UW Robofly, using a custom-built sensitive force-torque sensor, and validated them using motion capture data in free flight. We demonstrated stable hovering (RMS error of about 4 cm) and trajectory tracking maneuvers at translational velocities up to 25 cm/s using an optimal linear quadratic regulator (LQR). These results were enabled by a more accurate model and lay the foundation for future work that uses our improved model and optimal controller in conjunction with recent advances in low-power receding horizon control to perform accurate aggressive maneuvers without iterative, task-specific tuning.
## QA:
coming soon
