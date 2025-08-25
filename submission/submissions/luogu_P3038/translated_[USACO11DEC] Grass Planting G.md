# [USACO11DEC] Grass Planting G (翻译版)

## 题目描述

给出一棵有 $n$ 个节点的树，有 $m$ 个如下所示的操作：

- 将两个节点之间的 **路径上的边** 的权值均加一。

- 查询两个节点之间的 **那一条边** 的权值，保证两个节点直接相连。

初始边权均为 0。

**【输入格式】**

第一行两个整数 $n,m$，含义如上。

接下来 $n-1$ 行，每行两个整数 $u,v$，表示 $u,v$ 之间有一条边。

接下来 $m$ 行，每行格式为 `op u v`，$op=\texttt{P}$ 代表第一个操作，$op=\texttt{Q}$ 代表第二个操作。

**【输出格式】**

若干行。对于每个查询操作，输出一行整数，代表查询的答案。

**【数据范围】**

对于 $100\%$ 的数据，$2\le n\le 10^5$，$1\le m\le 10^5$。

## 输入格式

\* Line 1: Two space-separated integers N and M

\* Lines 2..N: Two space-separated integers describing the endpoints of a road.

\* Lines N+1..N+M: Line i+1 describes step i. The first character of the line is either P or Q, which describes whether or not FJ is planting grass or simply querying. This is followed by two space-separated integers A\_i and B\_i (1 <= A\_i, B\_i <= N) which describe FJ's action or query.


## 输出格式

\* Lines 1..???: Each line has the answer to a query, appearing in the same order as the queries appear in the input.


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
