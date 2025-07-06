# [USACO10DEC] Apple Delivery S (翻译版)

## 题目描述

贝西有两个又香又脆的红苹果要送给她的两个朋友。当然她可以走的 $C(1 \le C \le 200000)$ 条“牛路”都被包含在一种常用的图中。这张图同时包含了$P(1 \le P \le 100000)$ 个牧场，分别被标为 $1 \cdots P$。没有“牛路”会从一个牧场又走回它自己。“牛路”是双向的，每条牛路都会被标上一个距离。最重要的是，每个牧场都可以通向另一个牧场。每条牛路都连接着两个不同的牧场 $P1\_i$和$P2\_i$（$1 \le P1\_i,P2\_i \le P$)，距离为$D\_i$。所有“牛路”的距离之和不大于 $2000000000$。

现在，贝西要从牧场 $PB$ 开始给 $PA\_1$ 和 $PA\_2$ 牧场各送一个苹果（$PA\_1$ 和 $PA\_2$ 顺序可以调换），那么最短的距离是多少呢？当然，$PB$、$PA\_1$ 和 $PA\_2$ 各不相同。


## 输入格式

\* Line 1: Line 1 contains five space-separated integers: C, P, PB, PA1, and PA2

\* Lines 2..C+1: Line i+1 describes cowpath i by naming two pastures it connects and the distance between them: P1\_i, P2\_i, D\_i


## 输出格式

\* Line 1: The shortest distance Bessie must travel to deliver both apples


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
