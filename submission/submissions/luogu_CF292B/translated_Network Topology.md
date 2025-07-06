# Network Topology (翻译版)

## 题目描述

### 题目大意
给你一个 $n(4 \le n \le 10^5)$ 个点，$m (3 \le m \le 10^5)$ 条边的图，询问它是以下的哪种情况：

1. 总线：一个连接的图，所有节点都与另外两个节点连接，除了作为路径起点和终点的节点；

1. 环：一个连接的图，其中所有节点都与另外两个节点连接；

1. 星型：一个连接的图，其中一个单独的中心节点被选出并与所有其他节点连接。

有关详细信息，请参见图片：

![](https://vj.csgrandeur.cn/a5495a5c4769fff7cad679392410a8f9?v=1701151687)


### 输入

第 $1$ 行两个整数 $n,m$

接下来 $m$ 行，对于第 $i+1$ 行，两个整数 $x_i,y_i(1\le x_i,y_i \le n)$，第 $i$
条边连接的两个点。

### 输出
如果图是总线，则打印 `"bus topology"`（不包括引号），

如果图是环，则打印 `"ring topology"`（不包括引号），

如果图是星型，则打印 `"star topology"`（不包括引号），

如果没有符合的答案，则打印 `"unknown topology"`（不包括引号）。

## 输入格式

The first line contains two space-separated integers $ n $ and $ m $ $ (4<=n<=10^{5}; 3<=m<=10^{5}) $ — the number of nodes and edges in the graph, correspondingly. Next $ m $ lines contain the description of the graph's edges. The $ i $ -th line contains a space-separated pair of integers $ x_{i} $ , $ y_{i} $ $ (1<=x_{i},y_{i}<=n) $ — the numbers of nodes that are connected by the $ i $ -the edge.

It is guaranteed that the given graph is connected. There is at most one edge between any two nodes. No edge connects a node with itself.

## 输出格式

In a single line print the network topology name of the given graph. If the answer is the bus, print "bus topology" (without the quotes), if the answer is the ring, print "ring topology" (without the quotes), if the answer is the star, print "star topology" (without the quotes). If no answer fits, print "unknown topology" (without the quotes).

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
