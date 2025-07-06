# 【A】Pair

## 题目描述

我们定义这个函数：

```cpp
int pair_int_int__to_int(pair<int, int>v) {
	return v.first * v.second;
}
```

这时候，我们再给你一个序列 $a$，其长度为 $n$，且其中全部是 unsigned 型数据。

每一次，我们给出两个参数 $l_k,r_k$。

我们需要做的就是求出：

$$\frac{\sum_{i=l_k}^{r_k}\sum_{j=i+1}^{r_k}\operatorname{pair\_int\_int\_\_to\_int}(\operatorname{make\_pair}(a_i,a_j))}{\sum_{i=l_k}^{r_k}\sum_{j=i+1}^{r_k}1}$$

当然，为了避免浮点数精度误差，我们需要输出上面这个分数。而且必须约分至最简分数。

你的输出形式应为 $a/b$。**特别的，如果 $b$ 为 $1$，那么只输出 $a$，如果 $l_i=r_i$，输出 $0$ 即可**。

## 输入格式

第一行两个整数 $n,m$。

第二行 $n$ 个整数。第 $i$ 个整数为 $a_i$。

接下来 $m$ 行，每行两个整数 $l_i,r_i$。

## 输出格式

共 $m$ 行，第 $i$ 行表示 $l_i,r_i$ 对应的上式的值。

## 提示

| Subtask | $n\le$ | $m\le$ | 分值 |
| :----------: | :----------: | :----------: | :----------: |
| 0 | $10^2$ | $10^2$ | 20 |
| 1 | $10^4$ | $10^4$ | 30 |
| 2 | $10^6$ | $10^6$ | 50 |

对于所有数据，保证 $n,m\le10^6,a_i\le10^2$。

本题输入输出量大，提供快读快写模板：

```cpp
inline int read() {
	int r = 0; char c = getchar();
	while (c < '0' || c>'9') c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (c ^ 48), c = getchar();
	return r;
}
inline void write(int x) {
	if (x > 9) write(x / 10);
	putchar(x % 10 ^ 48);
	return;
}
```

## 时空限制

时间限制: 900 ms
内存限制: 512 MB
