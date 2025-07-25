# [POI 2008] BLO-Blockade (翻译版)

## 题目描述

B 城有 $n$ 个城镇（从 $1$ 到 $n$ 标号）和 $m$ 条双向道路。

每条道路连结两个不同的城镇，没有重复的道路，所有城镇连通。


把城镇看作节点，把道路看作边，容易发现，整个城市构成了一个无向图。

请你对于每个节点 $i$ 求出，把与节点 $i$ 关联的所有边去掉以后（不去掉节点 $i$ 本身），无向图有多少个有序点 $(x,y)$，满足 $x$ 和 $y$ 不连通。

**【输入格式】**

第一行包含两个整数 $n$ 和 $m$。

接下来 $m$ 行，每行包含两个整数 $a$ 和 $b$，表示城镇 $a$ 和 $b$ 之间存在一条道路。

**【输出格式】**

输出共 $n$ 行，每行输出一个整数。

第 $i$ 行输出的整数表示把与节点 $i$ 关联的所有边去掉以后（不去掉节点 $i$ 本身），无向图有多少个有序点 $(x,y)$，满足 $x$ 和 $y$ 不连通。

**【数据范围】**

$n\le 100000$，$m\le500000$。

## 输入格式

In the first line of the standard input there are two positive    integers: $n$ and $m$ ($1\le n\le 100\ 000$, $1\le m\le 500\ 000$) denoting the number of towns and roads, respectively.

The towns are numbered from 1 to $n$.

The following $m$ lines contain descriptions of the roads.

Each line contains two integers $a$ and $b$ ($1\le a<b\le n$) and    denotes a direct road between towns numbered $a$ and $b$.


## 输出格式

Your programme should write out exactly $n$ integers to the standard    output, one number per line. The $i^{th}$ line should contain the number    of visits that could not take place if the programmers blocked the town    no. $i$.


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
