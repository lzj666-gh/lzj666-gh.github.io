# new例13.2-2 带负权的最短路计算

## 题目描述

给定一个n个点m条边(n<=1e5,m<=2e5)的有向图，图中可能存在重边和自环，边权绝对值小于$10^4$。数据保证图中不存在负权回路。

请你求出1号点到n号点的最短距离。如果无法从1号点走到n号点，则输出-1。


## 输入格式

第一行包含整数n和m(n<=1e5,m<=2e5)。

接下来m行每行包含三个整数x，y，z，表示存在一条从点x到点y的有向边，边长为z。

## 输出格式

输出一个整数，表示1号点到n号点的最短距离
如果路径不存在，则输出-1。

## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
