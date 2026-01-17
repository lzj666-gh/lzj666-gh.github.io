# [USACO09FEB] Revamping Trails G (翻译版)

## 题目描述

约翰一共有 $N$ 个牧场.由 $M$ 条布满尘埃的小径连接。小径可以双向通行。每天早上约翰从牧场 $1$ 出发到牧场 $N$ 去给奶牛检查身体。

通过每条小径都需要消耗一定的时间。约翰打算升级其中 $K$ 条小径，使之成为高速公路。在高速公路上的通行几乎是瞬间完成的，所以高速公路的通行时间为 $0$。

请帮助约翰决定对哪些小径进行升级，使他每天从 $1$ 号牧场到第 $N$ 号牧场所花的时间最短。输出这一最短时间即可。

## 输入格式

\* Line 1: Three space-separated integers: N, M, and K

\* Lines 2..M+1: Line i+1 describes trail i with three space-separated integers: P1\_i, P2\_i, and T\_i


## 输出格式

\* Line 1: The length of the shortest path after revamping no more than K edges


## 提示

K is 1; revamp trail 3->4 to take time 0 instead of 100. The new shortest path is 1->3->4, total traversal time now 1.


## 时空限制

时间限制: 2000 ms
内存限制: 125 MB
