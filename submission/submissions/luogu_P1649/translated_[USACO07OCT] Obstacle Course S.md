# [USACO07OCT] Obstacle Course S (翻译版)

## 题目描述

$N\times N\ (1\le N\le 100)$ 方格中，$\verb!x!$ 表示不能行走的格子，$\verb!.!$ 表示可以行走的格子。卡门很胖，故而不好转弯。现在要从 $A$ 点走到 $B$ 点，请问最少要转 $90$ 度弯多少次？

## 输入格式

Line 1: A single integer: N

Lines 2..N + 1: Line i+1 represents row i of the field with N characters as above (i.e., '.', 'x', 'A', and 'B'); no spaces are present on a line


## 输出格式

Line 1: A single integer, the minimum number of turns the cow must make in a traversal

## 提示

只可以上下左右四个方向行走，并且不能走出这些格子之外。开始和结束时的方向可以任意。

### 数据范围及约定

对于全部数据，保证 $2\le N\le 100$。


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
