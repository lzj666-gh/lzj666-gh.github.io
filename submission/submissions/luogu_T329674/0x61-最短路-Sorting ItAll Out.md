# 0x61-最短路-Sorting ItAll Out

## 题目描述

一个不同的值的升序排序数列指的是一个从左到右元素依次增大的序列，例如，一个有序的数列 $A,B,C,D$ 表示$A<B,B<C,C<D$。在这道题中，我们将给你一系列形如 $A<B$ 的关系，并要求你判断是否能够根据这些关系确定这个数列的顺序。

## 输入格式

第一行有两个正整数 $n,m$，$n$ 表示需要排序的元素数量，$2\leq n\leq 26$，第 $1$ 到 $n$ 个元素将用大写的 $A,B,C,D\dots$ 表示。$m$ 表示将给出的形如 $A<B$ 的关系的数量。

接下来有 $m$ 行，每行有 $3$ 个字符，分别为一个大写字母，一个 `<` 符号，一个大写字母，表示两个元素之间的关系。


## 输出格式

若根据前 $x$ 个关系即可确定这 $n$ 个元素的顺序 `yyy..y`（如 `ABC`），输出

`Sorted sequence determined after xxx relations: yyy...y.`

若根据前 $x$ 个关系即发现存在矛盾（如 $A<B,B<C,C<A$），输出

`Inconsistency found after x relations.`

若根据这 $m$ 个关系无法确定这 $n$ 个元素的顺序，输出

`Sorted sequence cannot be determined.`

（提示：确定 $n$ 个元素的顺序后即可结束程序，可以不用考虑确定顺序之后出现矛盾的情况）


## 提示

$2 \leq n \leq 26,1 \leq m \leq 600$。

## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
