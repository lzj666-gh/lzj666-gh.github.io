# [AGC038C] LCMs (翻译版)

## 题目描述

- 给定一个长度为 $N$ 的数列 $A_1, A_2, A_3, \ldots, A_N$。
- 请你求出 $\sum_{i=1}^{N}\sum_{j=i+1}^{N}\mathrm{lcm}(A_i,A_j)$ 的值模 $998244353$ 的结果。
- $1 \leq N \leq 2 \times 10^5$，$1 \leq A_i \leq 10^6$。

## 输入格式

入力は以下の形式で標準入力から与えられる。

> $ N $ $ A_0\ A_1\ \cdots\ A_{N-1} $

## 输出格式

$ \sum_{i=0}^{N-2}\ \sum_{j=i+1}^{N-1}\ \mathrm{lcm}(A_i,A_j) $ の値を $ 998244353 $ で割ったあまりを出力せよ。

## 提示

### 制約

- $ 1\ \leq\ N\ \leq\ 200000 $
- $ 1\ \leq\ A_i\ \leq\ 1000000 $
- 入力される値はすべて整数である。

### Sample Explanation 1

$ \mathrm{lcm}(2,4)+\mathrm{lcm}(2,6)+\mathrm{lcm}(4,6)=4+6+12=22 $ です。

## 时空限制

时间限制: 2000 ms
内存限制: 1024 MB
