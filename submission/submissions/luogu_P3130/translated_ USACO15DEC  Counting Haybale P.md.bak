# [USACO15DEC] Counting Haybale P (翻译版)

## 题目描述

### 题目描述

Farmer John 正在尝试雇佣承包商来帮助他重新安排农场，但到目前为止，所有承包商在看到 FJ 希望他们遵循的复杂指令序列后都辞职了。FJ 不得不自己完成这个项目，他意识到自己可能把项目搞得比必要的还要复杂。请帮助他按照指令完成农场的升级。

FJ 的农场由一排 $N$ 个田地组成，编号为 $1 \ldots N$。每个田地里可以有任意数量的干草堆。Farmer John 的指令包含三种类型的条目：

1) 给定一个连续的田地区间，向每个田地添加一个新的干草堆。

2) 给定一个连续的田地区间，确定该区间内田地中干草堆的最小数量。

3) 给定一个连续的田地区间，计算该区间内干草堆的总数。

### 输入格式

第一行包含两个正整数，$N$（$1 \leq N \leq 200,000$）和 $Q$（$1 \leq Q \leq 100,000$）。

第二行包含 $N$ 个非负整数，每个整数最多为 $100,000$，表示每个田地中初始的干草堆数量。

接下来的 $Q$ 行每行包含一个大写字母，可能是 M、P 或 S，后跟两个正整数 $A$ 和 $B$（$1 \leq A \leq B \leq N$），或者三个正整数 $A$、$B$ 和 $C$（$1 \leq A \leq B \leq N$；$1 \leq C \leq 100,000$）。只有当大写字母是 P 时，才会有三个正整数。

如果字母是 M，输出从 $A \ldots B$ 的田地区间内干草堆的最小数量。

如果字母是 P，向从 $A \ldots B$ 的田地区间内的每个田地添加 $C$ 个新的干草堆。

如果字母是 S，输出从 $A \ldots B$ 的田地区间内干草堆的总数。

### 输出格式

对于 FJ 指令中的每一个 'M' 或 'S' 条目，输出一行相应的结果。

## 输入格式

The first line contains two positive integers, $N$ ($1 \leq N \leq 200,000$) and $Q$ ($1 \leq Q \leq 100,000$).

The next line contains $N$ nonnegative integers, each at most 100,000, indicating how many haybales are initially in each field.

Each of the next $Q$ lines contains a single uppercase letter, either M, P or S, followed by either two positive integers $A$ and $B$ ($1 \leq A \leq B \leq N$), or three positive integers $A$, $B$, and $C$ ($1 \leq A \leq B \leq N$; $1 \leq C \leq 100,000$).  There will be three positive integers if and only if the uppercase letter is P.

If the letter is M, print the minimum number of haybales in the interval of fields from $A \ldots B$.

If the letter is P, put $C$ new haybales in each field in the interval of fields from $A \ldots B$.

If the letter is S, print the total number of haybales found within interval of fields from $A \ldots B$.

## 输出格式

A line in the output should appear in response to every 'M' or 'S' entry in FJ's instructions.

## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
