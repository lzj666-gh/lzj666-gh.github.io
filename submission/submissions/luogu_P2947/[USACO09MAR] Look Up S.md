# [USACO09MAR] Look Up S

## 题目描述

Farmer John's N (1 <= N <= 100,000) cows, conveniently numbered 1..N, are once again standing in a row. Cow i has height H\_i (1 <= H\_i <= 1,000,000).

Each cow is looking to her left toward those with higher index numbers. We say that cow i 'looks up' to cow j if i < j and H\_i < H\_j. For each cow i, FJ would like to know the index of the first cow in line looked up to by cow i.

Note: about 50% of the test data will have N <= 1,000. 

约翰的 $N(1\le N\le10^5)$ 头奶牛站成一排，奶牛 $i$ 的身高是 $H_i(1\le H_i\le10^6)$。现在，每只奶牛都在向右看齐。对于奶牛 $i$，如果奶牛 $j$ 满足 $i<j$ 且 $H_i<H_j$，我们可以说奶牛 $i$ 可以仰望奶牛 $j$。 求出每只奶牛离她最近的仰望对象。

Input

## 输入格式

1. \* Line 1: A single integer: N

\* Lines 2..N+1: Line i+1 contains the single integer: H\_i

第 $1$ 行输入 $N$，之后每行输入一个身高 $H_i$。


## 输出格式

\* Lines 1..N: Line i contains a single integer representing the smallest index of a cow up to which cow i looks. If no such cow exists, print 0.

共 $N$ 行，按顺序每行输出一只奶牛的最近仰望对象，如果没有仰望对象，输出 $0$。


## 提示

FJ has six cows of heights 3, 2, 6, 1, 1, and 2.


Cows 1 and 2 both look up to cow 3; cows 4 and 5 both look up to cow 6; and cows 3 and 6 do not look up to any cow.

【输入说明】$6$ 头奶牛的身高分别为 3,2,6,1,1,2。

【输出说明】奶牛 #1,#2 仰望奶牛 #3，奶牛 #4,#5 仰望奶牛 #6，奶牛 #3 和 #6 没有仰望对象。

【数据规模】

对于 $20\%$ 的数据：$1\le N\le10$；

对于 $50\%$ 的数据：$1\le N\le10^3$；

对于 $100\%$ 的数据：$1\le N\le10^5,1\le H_i\le10^6$。


## 时空限制

时间限制: 1000 ms
内存限制: 500 MB
