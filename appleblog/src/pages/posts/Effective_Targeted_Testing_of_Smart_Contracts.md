---
layout: '../../layouts/MarkdownPost.astro'
title: 'Effective Targeted Testing of Smart Contracts'
pubDate: 2024-07-09 04:44:45
description: ''
author: 'wanghaisheng'
cover:
    url: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    square: 'https://www.apple.com.cn/newsroom/images/product/homepod/standard/Apple-HomePod-hero-230118_big.jpg.large_2x.jpg'
    alt: 'cover'
tags: ['smart glass'] 
theme: 'light'
featured: true

meta:
 - name: author
   content: Mahdi Fooladgar et.al.
 - name: keywords
   content: key3, key4

keywords: key1, key2, key3
---

## paper id
2407.04250v1
## download
[2407.04250v1](http://arxiv.org/abs/2407.04250v1)
## abstracts:
Smart contracts are autonomous and immutable pieces of code that are deployed on blockchain networks and run by miners. They were first introduced by Ethereum in 2014 and have since been used for various applications such as security tokens, voting, gambling, non-fungible tokens, self-sovereign identities, stock taking, decentralized finances, decentralized exchanges, and atomic swaps. Since smart contracts are immutable, their bugs cannot be fixed, which may lead to significant monetary losses. While many researchers have focused on testing smart contracts, our recent work has highlighted a gap between test adequacy and test data generation, despite numerous efforts in both fields. Our framework, Griffin, tackles this deficiency by employing a targeted symbolic execution technique for generating test data. This tool can be used in diverse applications, such as killing the survived mutants in mutation testing, validating static analysis alarms, creating counter-examples for safety conditions, and reaching manually selected lines of code. This paper discusses how smart contracts differ from legacy software in targeted symbolic execution and how these differences can affect the tool structure, leading us to propose an enhanced version of the control-flow graph for Solidity smart contracts called CFG+. We also discuss how Griffin can utilize custom heuristics to explore the program space and find the test data that reaches a target line while considering a safety condition in a reasonable execution time. We conducted experiments involving an extensive set of smart contracts, target lines, and safety conditions based on real-world faults and test suites from related tools. The results of our evaluation demonstrate that Griffin can effectively identify the required test data within a reasonable timeframe.
## QA:
coming soon
