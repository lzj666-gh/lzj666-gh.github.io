# [USACO07DEC] Sightseeing Cows G (翻译版)

## 题目描述

给你一张 $n$ 点 $m$ 边的有向图，第 $i$ 个点点权为 $F_i$，第 $i$ 条边边权为 $T_i$。

找一个环，设环上的点组成的集合为 $S$，环的边组成的集合为 $E$，最大化 $\dfrac{\sum_{u\in S}F_u}{\sum_{e\in E}T_e}$。

数据范围：$1\leq n,F_i,T_i\leq 10^3$，$1\leq m\leq 5\times10^3$。

## 输入格式

\* Line 1: Two space-separated integers: L and P

\* Lines 2..L+1: Line i+1 contains a single one integer: Fi

\* Lines L+2..L+P+1: Line L+i+1 describes cow path i with three space-separated integers: L1i , L2i , and Ti


## 输出格式

\* Line 1: A single number given to two decimal places (do not perform explicit rounding), the maximum possible average fun per unit time, or 0 if the cows cannot plan any trip at all in accordance with the above rules.


## 时空限制

时间限制: 1000 ms
内存限制: 128 MB
