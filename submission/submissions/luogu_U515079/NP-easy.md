# NP-easy

## 题目描述

一个序列，有 $n$ 个数。

你要选择它的一个子序列 $b$，使 $b$ 中的 $\sum b_{2i}-\sum b_{2i+1}$ 最大。

但邪恶的 JCY crab 要求 LBY 带修，然后 LBY ~~依旧会做~~不会做了。

请你来 solve it。

## 输入格式

给你两个数 $n$，$m$，表示序列长度与操作个数。

接下来 $1$ 行，$n$ 个数，表示那个序列 $a$。

接下来 $m$ 行，每次两个数 $x$，$y$，表示一个操作，将 $a_x$ 赋值为 $y$。

## 输出格式

每次操作之后，输出答案

## 提示

对于 $100\%$ 的数据，$1\le n,m\le 10^5$，$1\le a_i \le 10^9$。

## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
