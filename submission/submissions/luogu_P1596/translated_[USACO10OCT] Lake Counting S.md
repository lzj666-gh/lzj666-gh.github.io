# [USACO10OCT] Lake Counting S (翻译版)

## 题目描述

由于近期的降雨，雨水汇集在农民约翰的田地不同的地方。我们用一个 $N\times M(1\leq N\leq 100, 1\leq M\leq 100)$ 的网格图表示。每个网格中有水（`W`） 或是旱地（`.`）。一个网格与其周围的八个网格相连，而一组相连的网格视为一个水坑。约翰想弄清楚他的田地已经形成了多少水坑。给出约翰田地的示意图，确定当中有多少水坑。

输入第 $1$ 行：两个空格隔开的整数：$N$ 和 $M$。

第 $2$ 行到第 $N+1$ 行：每行 $M$ 个字符，每个字符是 `W` 或 `.`，它们表示网格图中的一排。字符之间没有空格。

输出一行，表示水坑的数量。

## 输入格式

Line 1: Two space-separated integers: N and M \* Lines 2..N+1: M characters per line representing one row of Farmer John's field. Each character is either 'W' or '.'. The characters do not have spaces between them.




## 输出格式

Line 1: The number of ponds in Farmer John's field.



## 提示

OUTPUT DETAILS: There are three ponds: one in the upper left, one in the lower left, and one along the right side.


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
