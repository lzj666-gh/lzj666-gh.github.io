# 【模板】扩展 BSGS/exBSGS

## 题目描述

给定 $a,p,b$，求满足 $a^x≡b \pmod p$ 的最小自然数 $x$ 。


## 输入格式

每个测试文件中包含若干组测试数据，保证 $\sum \sqrt p\le 5\times 10^6$。

每组数据中，每行包含 $3$ 个正整数 $a,p,b$ 。

当 $a=p=b=0$ 时，表示测试数据读入完全。


## 输出格式

对于每组数据，输出一行。

如果无解，输出 `No Solution`，否则输出最小自然数解。


## 提示

对于 $100\%$ 的数据，$1\le a,p,b≤10^9$ 或 $a=p=b=0$。

2021/5/14 加强 by [SSerxhs](https://www.luogu.com.cn/user/29826)。  
2021/7/1 新添加[一组 Hack 数据](https://www.luogu.com.cn/discuss/391666)。

## 时空限制

时间限制: 3000 ms
内存限制: 128 MB
