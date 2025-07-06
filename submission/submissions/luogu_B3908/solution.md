# B3908 题解

## Source & Knowledge

2023 年 12 月语言月赛，由洛谷网校入门计划/基础计划提供。

## 题目大意

给定 $n$ 个非负整数 $a _ 1, a _ 2, \cdots, a _ n$，确定一个非负整数 $x$，使得 $a _ 1 \oplus a _ 2 \oplus \cdots \oplus a _ n \oplus x$ 最小。

其中 $\oplus$ 代表异或，对于两个非负整数 $x,y$，它们的**异或**是指，将它们作为二进制数，对二进制表示中的每一位进行如下运算得到的结果：
 - $x$ 和 $y$ 的这一位上不同时，结果的这一位为 $1$；
 - $x$ 和 $y$ 的这一位上相同时，结果的这一位为 $0$。
	
## 题目分析

本题考察对循环结构的运用和对题目信息的掌握。

通过题目对异或的定义，我们会发现，如果一个非负整数和自身异或，那么二者的每一位都是相同的，二者最终得到的答案会是 $0000 \cdots 000 = 0$。

所以可以发现，$(a _ 1 \oplus a _ 2 \oplus \cdots \oplus a _ n) \oplus (a _ 1 \oplus a _ 2 \oplus \cdots \oplus a _ n) = 0$。

而显然，对于两个非负整数，一般不可以通过异或得到负数结果，因此 $0$ 是最优的结果。

因此，当 $x$ 取 $(a _ 1 \oplus a _ 2 \oplus \cdots \oplus a _ n)$ 时，答案最优为 $0$。输出 $(a _ 1 \oplus a _ 2 \oplus \cdots \oplus a _ n)$ 和 $0$ 即可。

代码实现上，只需要初始时令 $x = 0$，读入 $a _ i$ 的过程中让 $x \gets x \oplus a _ i$ 即可。

由于 $a _ i \leq 10 ^ {18}$，超过了 `int` 所能容纳的范围（约 $2 \times 10 ^ 9$），因此需要使用 `long long`。

```cpp
int n;
cin >> n;
long long x = 0;
for (int i = 1; i <= n; ++i) {
	long long a;
	cin >> a;
	x = x ^ a;
}
```

## 视频讲解
![](bilibili:BV1Pp4y1f7fm?page=4)
