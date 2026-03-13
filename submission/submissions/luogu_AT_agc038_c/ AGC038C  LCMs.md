# [AGC038C] LCMs

## 题目描述

[problemUrl]: https://atcoder.jp/contests/agc038/tasks/agc038_c

長さ $ N $ の整数列 $ A_0,A_1,\cdots,A_{N-1} $ があります。 次式の値を求めてください。

- $ \sum_{i=0}^{N-2}\ \sum_{j=i+1}^{N-1}\ \mathrm{lcm}(A_i,A_j) $

ここで、$ \mathrm{lcm}(x,y) $ は、$ x $ と $ y $ の最小公倍数を意味します。 なお、答えは非常に大きくなることがあるので、$ 998244353 $ で割ったあまりを求めてください。

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
