# 【模板】AC 自动机

## 题目描述

给你一个文本串 $S$ 和 $n$ 个模式串 $T_{1 \sim n}$，请你分别求出每个模式串 $T_i$ 在 $S$ 中出现的次数。

## 输入格式

第一行包含一个正整数 $n$ 表示模式串的个数。

接下来 $n$ 行，第 $i$ 行包含一个由小写英文字母构成的非空字符串 $T_i$。

最后一行包含一个由小写英文字母构成的非空字符串 $S$。

**数据不保证任意两个模式串不相同**。

## 输出格式

输出包含 $n$ 行，其中第 $i$ 行包含一个非负整数表示 $T_i$ 在 $S$ 中出现的次数。

## 提示

对于 $100 \%$ 的数据，$1 \le n \le 2 \times {10}^5$，$T_{1 \sim n}$ 的长度总和不超过 $2 \times {10}^5$，$S$ 的长度不超过 $2 \times {10}^6$。

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
