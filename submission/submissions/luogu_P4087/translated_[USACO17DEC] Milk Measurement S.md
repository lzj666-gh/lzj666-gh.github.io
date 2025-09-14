# [USACO17DEC] Milk Measurement S (翻译版)

## 题目描述

### 题目描述

Farmer John 的每头奶牛最初每天生产 $G$ 加仑牛奶（$1 \leq G \leq 10^9$）。由于奶牛的产奶量可能会随时间变化，Farmer John 决定定期测量产奶量并将这些记录在日志中。日志中的条目如下所示：

```
35 1234 -2  
14 2345 +3  
```

第一条记录表示在第 35 天，奶牛 #1234 的产奶量比上次测量时减少了 2 加仑。第二条记录表示在第 14 天，奶牛 #2345 的产奶量比上次测量时增加了 3 加仑。Farmer John 每天最多只能进行一次测量。不幸的是，他有点混乱，记录的测量结果不一定按时间顺序排列。

为了激励他的奶牛，Farmer John 自豪地在谷仓的墙上展示当前产奶量最高的奶牛的照片（如果有多头奶牛产奶量并列最高，他会展示所有奶牛的照片）。请确定 Farmer John 需要更改展示的天数。

请注意，Farmer John 的牛群非常庞大，因此尽管日志中记录了一些奶牛产奶量的变化，但总有许多其他奶牛的产奶量保持在 $G$ 加仑不变。

### 输入格式

输入的第一行包含 Farmer John 进行的测量次数 $N$（$1 \leq N \leq 100,000$）和初始产奶量 $G$。接下来的 $N$ 行每行包含一条测量记录，格式如上所述，指定一个天数（范围为 $1 \ldots 10^6$）、奶牛的整数 ID（范围为 $1 \ldots 10^9$）以及自上次测量以来产奶量的变化量（一个非零整数）。每头奶牛的产奶量始终在 $0 \ldots 10^9$ 范围内。

### 输出格式

请输出 Farmer John 需要调整激励展示的天数。

## 输入格式

The first line of input contains the number of measurements $N$ that Farmer John makes ($1 \leq N \leq 100,000$), followed by $G$. Each of the next $N$ lines contains one measurement, in the format above, specifying a day (an integer in the range $1 \ldots 10^6$), the integer ID of a cow (in the range $1 \ldots 10^9$), and the change in her milk output since it was last measured (a nonzero integer). Each cow's milk output will always be in the range $0 \ldots 10^9$.

## 输出格式

Please output the number of days on which Farmer John needs to adjust his motivational display.

## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
