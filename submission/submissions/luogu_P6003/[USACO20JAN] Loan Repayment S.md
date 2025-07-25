# [USACO20JAN] Loan Repayment S

## 题目描述

Farmer John 欠了 Bessie $N$ 加仑牛奶（$1 \leq N \leq 10^{12}$）。他必须在 $K$ 天内将牛奶给 Bessie。但是，他不想将牛奶太早拿出手。另一方面，他不得不在还债上有所进展，所以他必须每天给 Bessie 至少 $M$ 加仑牛奶（$1 \leq M \leq 10^{12}$）。

以下是 Farmer John 决定偿还 Bessie 的方式。首先他选择一个正整数 $X$。然后他每天都重复以下过程：

1. 假设 Farmer John 已经给了 Bessie $G$ 加仑，计算 $\frac{N-G}{X}$ 向下取整。令这个数为 $Y$。
2. 如果 $Y$ 小于 $M$，令 $Y$ 等于 $M$。
3. 给 Bessie $Y$ 加仑牛奶。

求 $X$ 的最大值，使得 Farmer John 按照上述过程能够在 $K$ 天后给 Bessie 至少 $N$ 加仑牛奶 （$1 \leq K \leq 10^{12}$）。

## 输入格式

输入仅有一行，包含三个空格分隔的正整数 $N,K,M$，满足 $K \times M<N$。

## 输出格式

输出最大的正整数 $X$，使得按照上述过程 Farmer John 会给 Bessie 至少 $N$ 加仑牛奶。

## 提示

### 样例解释

在这个测试用例中，当 $X=2$ 时 Farmer John 第一天给 Bessie $5$ 加仑，后两天每天给 Bessie $M=3$ 加仑。

### 子任务

- 测试点 $2 \sim 4$ 满足 $K \leq 10^5$。
- 测试点 $5 \sim 11$ 没有额外限制。

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
