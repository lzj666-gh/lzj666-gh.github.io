# [USACO18FEB] Rest Stops S (翻译版)

## 题目描述

### 题目描述

Farmer John 和他的私人教练 Bessie 正在攀登温哥华山。为了他们的目的（以及你的目的），这座山可以表示为一条长度为 $L$ 米的长直步道（$1 \leq L \leq 10^6$）。Farmer John 将以每米 $r_F$ 秒的恒定速度徒步（$1 \leq r_F \leq 10^6$）。由于他正在锻炼耐力，他不会在途中休息。

然而，Bessie 被允许在休息站休息，她可能会在那里找到一些美味的草。当然，她不能随便停下来！步道上有 $N$ 个休息站（$1 \leq N \leq 10^5$）；第 $i$ 个休息站距离步道起点 $x_i$ 米（$0 < x_i < L$），并且有一个美味值 $c_i$（$1 \leq c_i \leq 10^6$）。如果 Bessie 在第 $i$ 个休息站休息 $t$ 秒，她会获得 $c_i \cdot t$ 的美味单位。

当不在休息站时，Bessie 将以每米 $r_B$ 秒的固定速度徒步（$1 \leq r_B \leq 10^6$）。由于 Bessie 年轻且健康，$r_B$ 严格小于 $r_F$。

Bessie 希望最大化她摄入的美味草量。但她担心 Farmer John；她认为如果在徒步的任何时刻她在步道上落后于 Farmer John，他可能会失去继续前进的动力！

请帮助 Bessie 找到在确保 Farmer John 完成徒步的情况下，她能获得的最大总美味单位。

### 输入格式

输入的第一行包含四个整数：$L$、$N$、$r_F$ 和 $r_B$。接下来的 $N$ 行描述了休息站。对于每个 $i$ 从 $1$ 到 $N$，第 $i+1$ 行包含两个整数 $x_i$ 和 $c_i$，分别描述第 $i$ 个休息站的位置和草的美味值。
保证 $r_F > r_B$，且 $0 < x_1 < \dots < x_N < L$。**注意，$r_F$ 和 $r_B$ 的单位是秒每米！**

### 输出格式

输出一个整数：Bessie 能获得的最大总美味单位。


### 提示

在这个例子中，Bessie 最优的策略是在 $x=7$ 的休息站休息 $7$ 秒（获得 $14$ 个美味单位），然后在 $x=8$ 的休息站再休息 $1$ 秒（获得 $1$ 个美味单位，总共 $15$ 个美味单位）。

## 输入格式

The first line of input contains four integers: $L$, $N$, $r_F$, and $r_B$. The next $N$ lines describe the rest stops. For each $i$ between $1$ and $N$, the $i+1$-st line contains two integers $x_i$ and $c_i$, describing the position of the $i$-th rest stop and the tastiness of the grass there.
It is guaranteed that $r_F > r_B$, and $0 < x_1 < \dots < x_N < L $. **Note that $r_F$ and $r_B$ are given in seconds per meter!**

## 输出格式

A single integer: the maximum total tastiness units Bessie can obtain.

## 提示

In this example, it is optimal for Bessie to stop for $7$ seconds at the $x=7$ rest stop (acquiring $14$ tastiness units) and then stop for an additional $1$ second at the $x=8$ rest stop (acquiring $1$ more tastiness unit, for a total of $15$ tastiness units).

Problem credits: Dhruv Rohatgi

## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
