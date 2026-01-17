# 【CJLOI Ry】T4

## 题目描述

我们称一个长度为 $n$ 的序列 $A$ 是“furry”的，当且仅当 $\forall i\in[1,n),|A_i-A_{i+1}|=1$。

我们称两个长度均为 $t$ 的序列 $A,B$ 是 $k-$“yrruf”的，当且仅当 $A,B$ 都是“furry”的，并且 $\forall i\in[1,t],|A_i-B_i|=k$。

现在给你一个长度为 $n$ 的序列 $A_i=i$，显然这个序列是“furry”的。

拥有操控 $A$ 序列的权限的“furry”控会有如下两种操作：

1. “fnrry”修改。给定两个参数 $l,r$，然后枚举 $i\in[l,r]$。如果 $A_i-A_{i-1}=-1$，那么 $\forall j\in[i,n],A_j+2\to A_j$。反之则 $\forall j\in[i,n],A_j-2\to A_j$。显然经过操作之后序列 $A$ 仍然是“furry”的。
2.  “frury”查询。给定三个参数 $l,r,k$，询问有多少个长度为 $r-l+1$ 序列和 $A$ 的子段 $[l,r]$ 是 $k-$“yrruf” 的。

请对于“furry”控的每一次 $2$ 操作，输出答案。由于答案可能非常大，你需要输出答案对 $19990721$ 取模的结果。

受到急急国王的催促，你必须在线的解决这些问题。

## 输入格式

第一行两个正整数 $n,m$，表示有 $m$ 次操作。

接下来 $m$ 行，每行先输入一个整数 $o\in\{0,1\}$。

如果 $o=0$，则再输入两个整数 $l^\prime,r^\prime$，表示使用参数 $l,r$ 进行一次“fnrry”修改。具体来说，令 $lastans$ 表示上一次查询操作的答案，那么 $l=(l^\prime+lastans)\bmod n+2,r=(r^\prime+lastans)\bmod n+2$。

如果 $o=1$，则再输入三个整数 $l^\prime,r^\prime,k$，表示使用参数 $l,r,k$ 进行一次“frury”查询。具体来说，令 $lastans$ 表示上一次查询操作的答案，那么 $l=(l^\prime+lastans)\bmod n+1,r=(r^\prime+lastans)\bmod n+1$。

对于以上两种操作，初始时 $lastans$ 为 $0$。

## 输出格式

对于每一次“frury”查询，输出答案模 $19990721$ 的值。

## 提示

### 样例解释

第一次询问如图：

![](https://www.helloimg.com/i/2025/10/08/68e66bc51a4db.png)

第二次询问如图：

![](https://www.helloimg.com/i/2025/10/08/68e66bc5b1ced.png)

第三次询问如图：

![](https://www.helloimg.com/i/2025/10/08/68e66bc4d84c1.png)

### 数据范围

对于所有数据，满足 $1\le n\le10^{18},m\le2\times10^5,o\in\{0,1\},0\le l^\prime,r^\prime\le10^{18}$。对于 $o=0$，保证 $1<l\le r\le n$。对于 $o=1$，保证 $1\le l\le r\le n,0\le k\le10^{18}$。具体范围如下：

::cute-table{tuack}


|子任务编号|$n\le$|$m\le$|分值|
|:---:|:----:|:----:|:--------:|
|$1$|$10$|$10$|$10$|
|$2$|$10^3$|$10^3$|$10$|
|$3$|$10^3$|$2\times10^5$|$20$|
|$4$|$10^5$|$2\times10^5$|$30$|
|$5$|$10^{18}$|$2\times10^5$|$30$|

## 时空限制

时间限制: 1500 ms
内存限制: 512 MB
