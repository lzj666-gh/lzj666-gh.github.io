# [USACO12FEB] Nearby Cows G

## 题目描述

Farmer John has noticed that his cows often move between nearby fields. Taking this into account, he wants to plant enough grass in each of his fields not only for the cows situated initially in that field, but also for cows visiting from nearby fields.

Specifically, FJ's farm consists of N fields (1 <= N <= 100,000), where some pairs of fields are connected with bi-directional trails (N-1 of them in total).  FJ has designed the farm so that between any two fields i and j, there is a unique path made up of trails connecting between i and j. Field i is home to C(i) cows, although cows sometimes move to a different field by crossing up to K trails (1 <= K <= 20).

FJ wants to plant enough grass in each field i to feed the maximum number of cows, M(i), that could possibly end up in that field -- that is, the number of cows that can potentially reach field i by following at most K trails.  Given the structure of FJ's farm and the value of C(i) for each field i, please help FJ compute M(i) for every field i.

给你一棵 $n$ 个点的树，点带权，对于每个节点求出距离它不超过 $k$ 的所有节点权值和 $m_i$。

## 输入格式

\* Line 1: Two space-separated integers, N and K.

\* Lines 2..N: Each line contains two space-separated integers, i and j (1 <= i,j <= N) indicating that fields i and j are directly connected by a trail.

\* Lines N+1..2N: Line N+i contains the integer C(i). (0 <= C(i) <= 1000)

第一行两个正整数 $n,k$。   
接下来 $n-1$ 行，每行两个正整数 $u,v$，表示 $u,v$ 之间有一条边。  
最后 $n$ 行，每行一个非负整数 $c_i$，表示点权。


## 输出格式

\* Lines 1..N: Line i should contain the value of M(i). 

输出 $n$ 行，第 $i$ 行一个整数表示 $m_i$。

## 提示

There are 6 fields, with trails connecting (5,1), (3,6), (2,4), (2,1), and (3,2).  Field i has C(i) = i cows.


Field 1 has M(1) = 15 cows within a distance of 2 trails, etc.

【数据范围】  
对于 $100\%$ 的数据：$1 \le n \le 10^5$，$1 \le k \le 20$，$0 \le c_i \le 1000$

## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
