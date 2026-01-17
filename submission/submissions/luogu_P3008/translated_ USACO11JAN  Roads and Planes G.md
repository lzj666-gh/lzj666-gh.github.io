# [USACO11JAN] Roads and Planes G (翻译版)

## 题目描述

### 题面描述

Farmer John 正在一个新的销售区域对他的牛奶销售方案进行调查。他想把牛奶送到 $T$ 个城镇 ( $1 \le T \le 25,000$ )，编号为 $1$ 到 $T$ 。这些城镇之间通过 $R$ 条道路 ( $1 \le R \le 50,000$ ，编号为 $1$ 到 $R$ ) 和 $P$ 条航线 ( $1 \le P \le 50,000$ ，编号为 $1$ 到 $P$ ) 连接。每条道路 $i$ 或者航线 $i$ 连接城镇 $A_i$ ( $1 \le A_i \le T$ )到 $B_i$ ( $1 \le B_i \le T$ )，花费为 $C_i$ 。

对于道路 $0 \le C_i \le 10,000$ ;然而航线的花费很神奇，花费 $C_i$ 可能是负数( $-10,000 \le C_i \le 10,000$ )。道路是双向的，可以从 $A_i$ 到 $B_i$，也可以从 $B_i$ 到 $A_i$ ，花费都是 $C_i$ 。然而航线与之不同，只可以从 $A_i$ 到 $B_i$ 。

事实上，由于最近恐怖主义太嚣张，为了社会和谐，出台 了一些政策保证：如果有一条航线可以从 $A_i$ 到  $B_i$，那么保证不可能通过一些道路和航线从 $B_i$ 回到 $A_i$ 。由于 $FJ$ 的奶牛世界公认十分给力，他需要运送奶牛到每一个城镇。他想找到从发送中心城镇 $S$ ( $1 \le S \le T$) 把奶牛送到每个城镇的最便宜的方案，或者知道这是不可能的。

### 输入格式

共 $R+P+1$ 行

第 $1$ 行：四个整数 $T$ , $R$ , $P$ 和 $S$ ，分别表示城镇的数量，道路的数量，航线的数量和中心城镇。

第 $2$ 到 $R+1$ 行：每行三个整数 $A_i$ , $B_i$ 和 $C_i$ ，描述一条道路。

第 $R+2$ 到 $R+P+1$ 行：每行三个整数 $A_i$ , $B_i$ 和 $C_i$ ，描述一条航线。

### 输出格式

共 $T$ 行，第 $i$ 行输出城市 $S$ 到城市 $i$ 的最小花费。如果不能到达，输出`NO PATH`

## 输入格式

\* Line 1: Four space separated integers: T, R, P, and S

\* Lines 2..R+1: Three space separated integers describing a road: A\_i, B\_i and C\_i

\* Lines R+2..R+P+1: Three space separated integers describing a plane: A\_i, B\_i and C\_i


## 输出格式

\* Lines 1..T: The minimum cost to get from town S to town i, or 'NO PATH' if this is not possible


## 提示

6 towns.  There are roads between town 1 and town 2, town 3 and town 4, and town 5 and town 6 with costs 5, 5 and 10; there are planes from town 3 to town 5, from town 4 to town 6, and from town 1 to town 3 with costs -100, - 100 and -10.  FJ is based in town 4.


FJ's cows begin at town 4, and can get to town 3 on the road.  They can get to towns 5 and 6 using planes from towns 3 and 4.  However, there is no way to get to towns 1 and 2, since they cannot go

backwards on the plane from 1 to 3.


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
