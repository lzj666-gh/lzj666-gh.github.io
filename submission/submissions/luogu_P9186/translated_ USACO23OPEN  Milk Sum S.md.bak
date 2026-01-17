# [USACO23OPEN] Milk Sum S (翻译版)

## 题目描述

### 题目描述

**注意：本题的时间限制为 4 秒，是默认时间限制的 2 倍。**

Farmer John 的 $N$ 头奶牛的产奶量为整数 $a_1, \dots, a_N$。也就是说，第 $i$ 头奶牛每分钟产 $a_i$ 单位的牛奶。

每天早上，Farmer John 会将所有 $N$ 头奶牛连接到谷仓的挤奶机上。他需要依次断开连接，将奶牛送去进行日常锻炼。第一头奶牛在挤奶 1 分钟后被断开连接，第二头奶牛在再挤奶 1 分钟后被断开连接，依此类推。由于第一头奶牛（假设是奶牛 $x$）只在挤奶机上停留了 1 分钟，她总共贡献了 $a_x$ 单位的牛奶。第二头奶牛（假设是奶牛 $y$）在挤奶机上停留了总共 2 分钟，因此贡献了 $2a_y$ 单位的牛奶。第三头奶牛（假设是奶牛 $z$）贡献了 $3a_z$ 单位的牛奶，依此类推。设 $T$ 表示 Farmer John 以最优顺序断开奶牛连接时，可以收集到的最大总牛奶量。

Farmer John 很好奇，如果某些奶牛的产奶量发生变化，$T$ 会如何变化。对于每个由两个整数 $i$ 和 $j$ 指定的 $Q$ 个查询，请计算如果将 $a_i$ 设置为 $j$，新的 $T$ 值会是多少。注意，每个查询都是独立的临时变化，即在考虑下一个查询之前，$a_i$ 会恢复为原始值。

### 输入格式

第一行包含 $N$。

第二行包含 $a_1 \dots a_N$。

第三行包含 $Q$。

接下来的 $Q$ 行，每行包含两个用空格分隔的整数 $i$ 和 $j$。

### 输出格式

请为每个查询输出一行，表示对应的 $T$ 值。

### 提示

对于第一个查询，$a$ 将变为 $[1,1,4,2,6]$，此时 $T = 1 \cdot 1 + 2 \cdot 1 + 3 \cdot 2 + 4 \cdot 4 + 5 \cdot 6 = 55$。

对于第二个查询，$a$ 将变为 $[1,8,4,2,6]$，此时 $T = 1 \cdot 1 + 2 \cdot 2 + 3 \cdot 4 + 4 \cdot 6 + 5 \cdot 8 = 81$。

对于第三个查询，$a$ 将变为 $[1,10,4,5,6]$，此时 $T = 1 \cdot 1 + 2 \cdot 4 + 3 \cdot 5 + 4 \cdot 6 + 5 \cdot 10 = 98$。

$1 \leq N \leq 1.5 \cdot 10^5$，$0 \leq a_i \leq 10^8$，$1 \leq Q \leq 1.5 \cdot 10^5$，$0 \leq j \leq 10^8$。

- 输入 2-4：$N, Q \leq 1000$。
- 输入 5-11：没有额外限制。

## 输入格式

The first line contains $N$. 

The second line contains $a_1\dots a_N$.

The third line contains $Q$.

The next $Q$ lines each contain two space-separated integers $i$ and $j$.

## 输出格式

Please print the value of $T$ for each of the $Q$ queries on separate lines.


## 提示

For the first query, $a$ would become $[1,1,4,2,6]$, and
$T =
1 \cdot 1 + 2 \cdot 1 + 3 \cdot 2 + 4 \cdot 4 + 5 \cdot 6 = 55$.

For the second query, $a$ would become $[1,8,4,2,6]$, and
$T =
1 \cdot 1 + 2 \cdot 2 + 3 \cdot 4 + 4 \cdot 6 + 5 \cdot 8 = 81$.

For the third query, $a$ would become $[1,10,4,5,6]$, and
$T =
1 \cdot 1 + 2 \cdot 4 + 3 \cdot 5 + 4 \cdot 6 + 5 \cdot 10 = 98$.

$1\le N\le 1.5\cdot 10^5$, $0 \leq a_i \leq 10^8$,$1\le Q\le 1.5\cdot 10^5$，$0 \leq j \leq 10^8$.

- Inputs 2-4: $N,Q\le 1000$.
- Inputs 5-11: No additional constraints.

## 时空限制

时间限制: 4000 ms
内存限制: 256 MB
