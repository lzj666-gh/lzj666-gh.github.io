# [NEERC 2015] Adjustment Office (翻译版)

## 题目描述

有一个大小为 $n\times n$ 的矩阵，每个位置的值为该位置的行数+列数。

接下来有 $q$ 次操作：

- $R\ m$：输出第 $m$ 行的总和并整行消去。
- $C\ m$：输出第 $m$ 列的总和并整列消去。

$1\leqslant n\leqslant 10^6$，$1\leqslant q\leqslant 10^5$，$1\leqslant m\leqslant n$。

Translated by Eason_AC  
2020.11.19

## 输入格式

The first line of the input contains two integers $n$ and $q$ $(1\leq n\leq10^6$, $1\leq q\leq10^5$) — the size of the square and the number of queries.

Each of the next $q$ lines contains the description of the query. Each query is either “R $r$” $(1\leq r\leq n$) or “C $c$” $(1\leq c\leq n$).

## 输出格式

The output file shall contain $q$ lines. The $i$ - th line shall contain one integer — the result of the $i$ - th query. 

## 提示

Time limit: 1 s, Memory limit: 256 MB. 



## 时空限制

时间限制: 1000 ms
内存限制: 256 MB
