# 『STA - R2』Locked

## 题目描述

这把锁从左到右有 $n$ 个数，组成了一个序列 $\{a\}$。

由于 GOD_hj 的记性不好，所以只要将锁设置为输入任意单峰序列即可打开。具体为：
$$ a_1 \le \cdots \le a_i \ge a_{i+1} \ge \cdots \ge a_n\quad (1 \le i \le n) $$

GOD_hj 的锁是拨动式的，即拨一下就能换成临近的一个数（$0$ 和 $9$ 可以互换）。

求最少拨几下可以开锁。

## 输入格式

第一行一个整数，$n$。

第二行 $n$ 个整数，为序列 $\{a\}$。

## 输出格式

一个整数，为最少要拨动几下。

## 提示

**【样例解释】**

样例二：把第四个 $5$ 变为 $6$ 或把第三个 $6$ 变为 $5$。

**【数据范围】**

**本题采用捆绑测试。**

$$
\newcommand{\arraystretch}{1.5}
\begin{array}{c|c|c|c}\hline\hline
\textbf{Subtask} & \bm n\le &\textbf{分值}&\textbf{特殊性质} \\\hline
\textsf{1} & 5 & 5 & \textbf{无} \\\hline
\textsf{2} & 10^3 & 25 & \textbf{无} \\\hline
\textsf{3}  & 5\times 10^5 & 20 & \textbf{无} \\\hline
\textsf{4} & 5\times 10^6 & 10 & a_i\in\{0,1\} \\\hline
\textsf{5} & 5\times 10^6 & 40 & \textbf{无} \\\hline\hline
\end{array}
$$

对于全部数据，$1\le n\le 5\times 10^6$，$0\le a_i<10$。

**Upd on 2023/06/12**：新加 5 组 Hack 数据，放入 Subtask 6，不计分。

## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
