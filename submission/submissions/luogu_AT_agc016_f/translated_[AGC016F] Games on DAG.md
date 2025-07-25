# [AGC016F] Games on DAG (翻译版)

## 题目描述

给定一个 $n$ 个点 $m$ 条边的 DAG，对于每条边 $(u,v)$ 都满足 $u<v$，$1,2$ 号点各一个石头，每次可以沿 DAG 上的边移动一颗石头，不能移动则输，求所有 $2^{m}$ 个边的子集中，只保留这个子集先手必胜的方案个数。

注意：两个石头可以重合。

## 输入格式

入力は以下の形式で標準入力から与えられる。

> $ N $ $ M $ $ x_1 $ $ y_1 $ $ x_2 $ $ y_2 $ $ : $ $ x_M $ $ y_M $

## 输出格式

高橋君が勝つような $ G' $ は何通りか？ $ 10^9+7 $ で割った余りを出力せよ。

## 提示

### 制約

- $ 2\ <\ =\ N\ <\ =\ 15 $
- $ 1\ <\ =\ M\ <\ =\ N(N-1)/2 $
- $ 1\ <\ =\ x_i $
- $ (x_i,\ y_i) $ はすべて相異なる。

### Sample Explanation 1

$ G' $ は次図の $ 2 $ 通りです。 高橋君が勝つ場合は ○ で、負ける場合は × で表しています。 !\[b250f23c38d0f5ec2204bd714e7c1516.png\](https://atcoder.jp/img/agc016/b250f23c38d0f5ec2204bd714e7c1516.png)

### Sample Explanation 2

$ G' $ は次図の $ 8 $ 通りです。 !\[8192fd32f894f708c5e4a60dcdea9d35.png\](https://atcoder.jp/img/agc016/8192fd32f894f708c5e4a60dcdea9d35.png)

## 时空限制

时间限制: 5000 ms
内存限制: 256 MB
