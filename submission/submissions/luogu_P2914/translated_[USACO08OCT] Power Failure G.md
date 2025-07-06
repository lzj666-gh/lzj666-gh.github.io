# [USACO08OCT] Power Failure G (翻译版)

## 题目描述

一场邪恶的暴风雨毁坏了农夫约翰的输电网中的一些电线！农夫约翰有一张包含了所有 $n$（$2\le n\le 1000$）个电能中转点的地图，中转点编号为 $1\ldots n$，第 $i$ 个点的坐标为 $(x_i,y_i)$（$-100000\le x_i\le 100000,-100000\le y_i\le 100000$）。

有 $w$（$1<=w<=10000$）条电线仍然保存着没被暴风雨破坏，每条电线连接着两个电能中转点 $p_i,p_j$（$1\le p_i\le n,1\le p_j\le n$）。

他希望从第一个电能中转点把电导入第 $n$ 个（可能通过一些中间的电能中转点，应当有一组电线连接 $1$ 和 $n$ ）。

给出 $n$ 个电能中转点的坐标和幸存的电线，请确定最少需要架设的电线总长度，但请注意，架设过程中，对于单条电线而言，其长度不应超过$m$（$0.0\le m\le 200000.0$）

给出一个例子，在下面，左边是一个包含 $9$ 个电能中转电和 $3$ 条幸存电线的地图。在这个任务中，规定 $m=2.0$。最佳的架设方案是连接 $6$ 和 $4$，以及 $6$ 和 $9$。

```plain
   After the storm              Optimally reconnected
3  . . . 7 9 . . . . .          3  . . . 7 9 . . . . .
                                          /
2  . . 5 6 . . . . . .          2  . . 5 6 . . . . . .
                                        /
1  2-3-4 . 8 . . . . .          1  2-3-4 . 8 . . . . .
   |                               |
0  1 . . . . . . . . .          0  1 . . . . . . . . .

   0 1 2 3 4 5 6 7 8 9             0 1 2 3 4 5 6 7 8 9
```
总长度是 $1.414213562 + 1.414213562 = 2.828427124$。


## 输入格式

Line $1$: Two space-separated integers: $N$ and $W$.

Line $2$: A single real number: $M$.

Lines $3\ldots N+2$: Each line contains two space-separated integers: $x_i$ and $y_i$.

Lines $N+3\ldots N+2+W$: Two space-separated integers: $P_i$ and $P_j$.


## 输出格式

Line 1: A single integer on a single line. If restoring connection is impossible, output `-1`. Otherwise, output a single integer that is $1000$ times the total minimum cost to restoreelectricity. Do not perform any rounding; truncate the resulting product.


## 提示

Just as in the diagram above.


As above.


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
