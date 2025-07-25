# [ARC160B] Triple Pair (翻译版)

## 题目描述

$T$ 组询问，每次给出一个正整数 $n$。求满足 $x,y,z \in N_{+}$ 且 $xy,xz,yz \leq n$ 有序三元组 $(x,y,z)$ 的个数，并输出答案对 $998244353$ 取模的结果。

有序三元组 $(x_1,y_1,z_1)$ 与 $(x_2,y_2,z_2)$ 不同当且仅当 $x_1 \neq x_2$ 或 $y_1 \neq y_2$ 或 $z_1 \neq z_2$。

## 输入格式

入力は以下の形式で標準入力から与えられる。

ここで、$ \mathrm{case}_i $ とは、$ i $ 番目のテストケースを意味する。

> $ T $ $ \mathrm{case}_1 $ $ \mathrm{case}_2 $ $ \vdots $ $ \mathrm{case}_T $

各テストケースは以下の形式で与えられる。

> $ N $

## 输出格式

$ T $ 行出力せよ。$ i(1\ \le\ i\ \le\ T) $ 行目には、$ i $ 番目のテストケースに対する答えを出力せよ。

## 提示

### 制約

- $ 1\ \le\ T\ \le\ 100 $
- $ 1\ \le\ N\ \le\ 10^9 $
 
### Sample Explanation 1

$ 1 $ 個目のテストケースでは、$ N=1 $ です。条件を満たす $ (x,y,z) $ は $ (1,1,1) $ の $ 1 $ 個です。 $ 2 $ 個目のテストケースでは、$ N=2 $ です。条件を満たす $ (x,y,z) $ は、$ (1,1,1),(2,1,1),(1,2,1),(1,1,2) $ の $ 4 $ 個です。

## 时空限制

时间限制: 2000 ms
内存限制: 1024 MB
