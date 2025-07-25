# 「EZEC-14」众数 I

## 题目描述

给定一个长度为 $n$ 的序列 $a$，我们通过以下方式构造序列 $b$：

- 初始时 $b=a$。
- 依次对 $b$ 进行 $k$ 次操作，每次操作选择任意一个元素并将其**修改**为任意整数。

dXqwq 定义一个序列的**众数**为所有出现次数最大的数。例如 $[1,1,4,5,1,4]$ 的众数为 $1$，而 $[1,14,5,14,19,19,8,10]$ 的众数为 $14,19$。

你需要求出有多少整数可能成为 $b$ 的**众数**。

## 输入格式

第一行输入两个整数 $n,k$。

第二行输入 $n$ 个整数 $a_i$。

## 输出格式

输出一个整数，代表可能成为众数的数的数量。

特别地，如果答案为正无穷，输出 ``pigstd``。

## 提示

**【样例解释】**

对于第一组数据，最终 $1,2,3,4,5$ 可能为区间众数。

对于第二组数据，将第一个数换成 $6,7,8,9,\cdots$ 后它们均会成为区间众数，因此答案为正无穷。

对于第三组数据，$1,2,3$ 可能成为区间众数。

**【提示】**

开 $10^6$ 个 ``std::deque`` 在空间限制为 1024MB 时不一定会 MLE。

**【数据范围】**

**本题采用捆绑测试。**

* Subtask 1（20 pts）：$n\leq 5$。
* Subtask 2（20 pts）：$n\leq 10^3$。
* Subtask 3（20 pts）：$k=0$。
* Subtask 4（20 pts）：$k=1$。
* Subtask 5（20 pts）：无特殊限制。

对于 $100\%$ 的数据，$1\leq n\leq 10^6$，$0\leq k\leq n $，$1\leq a_i\leq n$。

## 时空限制

时间限制: 1000 ms
内存限制: 256 MB
