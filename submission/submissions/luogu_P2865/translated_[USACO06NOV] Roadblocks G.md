# [USACO06NOV] Roadblocks G (翻译版)

## 题目描述

贝茜把家搬到了一个小农场，但她常常回到 FJ 的农场去拜访她的朋友。贝茜很喜欢路边的风景，不想那么快地结束她的旅途，于是她每次回农场，都会选择第二短的路径，而不象我们所习惯的那样，选择最短路。  
贝茜所在的乡村有 $R(1\le R \le 10^5)$ 条双向道路，每条路都联结了所有的 $N(1\le N\le 5000)$ 个农场中的某两个。贝茜居住在农场 $1$，她的朋友们居住在农场 $N$（即贝茜每次旅行的目的地）。  
贝茜选择的第二短的路径中，可以包含任何一条在最短路中出现的道路，并且，一条路可以重复走多次。当然咯，第二短路的长度必须严格大于最短路（可能有多条）的长度，但它的长度必须不大于所有除最短路外的路径的长度。

## 输入格式

Line 1: Two space-separated integers: N and R


Lines 2..R+1: Each line contains three space-separated integers: A, B, and D that describe a road that connects intersections A and B and has length D (1 ≤ D ≤ 5000)


## 输出格式

Line 1: The length of the second shortest path between node 1 and node N


## 提示

Two routes: 1 -> 2 -> 4 (length 100+200=300) and 1 -> 2 -> 3 -> 4 (length 100+250+100=450)


## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
