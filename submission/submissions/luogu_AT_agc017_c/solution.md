# AT_agc017_c 题解

在博客园食用更佳：[https://www.cnblogs.com/PinkRabbit/p/AGC017.html](https://www.cnblogs.com/PinkRabbit/p/AGC017.html)。

一个很精妙的性质：

- 考虑数轴上的 $N$ 个坐标 $1 \sim N$。每个坐标上都有绳子，一开始长度均为 $0$。
- 对于每个颜色 $A_i = k$ 的 $i$ 号球，在坐标 $k$ 上多挂 $1$ 单位长度的绳子。
- 最后把每个坐标上的绳子向左（负方向）拉直。
- 如果绳子覆盖了 $[0, N]$，则一定可以通过施法让所有球消失。
- 而如果不能让所有球消失，在 $[0, N]$ 中未被覆盖的总长度，就是需要修改颜色的球数，也就是答案。

此结论可以感性理解。

由此我们先开桶统计，然后做后缀和，然后对于每个询问我们可以在桶里查询，修改每个 $[i - 1, i]$ 被覆盖的次数。

每个询问是 $\mathcal O (1)$ 的，可以做到 $\mathcal O (N + Q)$ 的复杂度。

```cpp
#include <cstdio>

const int MN = 200005;

int N, Q, A[MN], C[MN], _S[MN * 2], *S = _S + MN, Ans;

int main() {
	scanf("%d%d", &N, &Q);
	for (int i = 1; i <= N; ++i) scanf("%d", &A[i]), ++C[A[i]];
	for (int i = 1; i <= N; ++i) ++S[i], --S[i - C[i]];
	for (int i = N; i >= -N; --i) S[i] += S[i + 1], Ans += i > 0 && !S[i];
	while (Q--) {
		int p, x;
		scanf("%d%d", &p, &x);
		--C[A[p]];
		if (!--S[A[p] - C[A[p]]]) if (A[p] - C[A[p]] > 0) ++Ans;
		if (!S[x - C[x]]++) if (x - C[x] > 0) --Ans;
		++C[x];
		A[p] = x;
		printf("%d\n", Ans);
	}
	return 0;
}
```