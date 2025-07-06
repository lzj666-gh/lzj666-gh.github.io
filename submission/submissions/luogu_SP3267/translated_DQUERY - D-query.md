# DQUERY - D-query (翻译版)

## 题目描述

给出一个长度为n 的数列，$a_{1}$​ ,$a_{2}$​ ,...,$a_{n}$ ，有q 个询问，每个询问给出数对$(i,j)$，需要你给出$a_{i}$​ ，$a_{i+1}$​ ，...，$a_{j}$​ 这一段中有多少不同的数字

## 输入格式

- Line 1: n (1 ≤ n ≤ 30000).
- Line 2: n numbers a $ _{1} $ , a $ _{2} $ , ..., a $ _{n} $ (1 ≤ a $ _{i} $ ≤ 10 $ ^{6} $ ).
- Line 3: q (1 ≤ q ≤ 200000), the number of d-queries.
- In the next q lines, each line contains 2 numbers i, j representing a d-query (1 ≤ i ≤ j ≤ n).

## 输出格式

- For each d-query (i, j), print the number of distinct elements in the subsequence a $ _{i} $ , a $ _{i+1} $ , ..., a $ _{j} $ in a single line.

## 时空限制

时间限制: 227 ms
内存限制: 1500 MB
