# [USACO06NOV] Roadblocks G

## 题目描述

Bessie has moved to a small farm and sometimes enjoys returning to visit one of her best friends. She does not want to get to her old home too quickly, because she likes the scenery along the way. She has decided to take the second-shortest rather than the shortest path. She knows there must be some second-shortest path.

The countryside consists of R (1 ≤ R ≤ 100,000) bidirectional roads, each linking two of the N (1 ≤ N ≤ 5000) intersections, conveniently numbered 1..N. Bessie starts at intersection 1, and her friend (the destination) is at intersection N.

The second-shortest path may share roads with any of the shortest paths, and it may backtrack i.e., use the same road or intersection more than once. The second-shortest path is the shortest path whose length is longer than the shortest path(s) (i.e., if two or more shortest paths exist, the second-shortest path is the one whose length is longer than those but no longer than any other path).


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
