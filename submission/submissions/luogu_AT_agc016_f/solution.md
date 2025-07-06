# AT_agc016_f 题解

在博客园食用更佳：[https://www.cnblogs.com/PinkRabbit/p/AGC016.html](https://www.cnblogs.com/PinkRabbit/p/AGC016.html)。

也就是要问有多少种情况满足 $1, 2$ 的 SG 值相等，用 $2^M$ 减去后就是最终答案。

我们考虑一下先钦点 SG 值序列：$\{x_1, x_2, \ldots , x_N\}$。

则对于 $x_i = v$ 的那些点，必须满足：

1. 对于每个 $k < v$，必须要向至少一个 $x_i = k$ 的点 $i$ 连一条边。
2. 它们之间互相都不能连边。
3. 对于 $k > v$，它们向 $x_i = k$ 的点的连边无所谓。

这样还是不太好分析。此时有一个关键的想法：

- 先把那些 $x_i = 0$ 的点枚举出来。

这些点之间互不能连边，剩下的点中每个点都必须至少要向这些点连一条边，而这些点对剩下的点的连边是任意的。

以上是与这些点有关的边的状态，对于无关的边，把剩下的点的 $x_i$ 全部减少 $1$，正好对应仅考虑剩下的点的导出子图的情况。

于是容易写出 DP：令 $\mathrm{f}[S]$ 表示仅考虑 $S$（必须保证 $1, 2 \in S$）中的点的导出子图时，满足 $1, 2$ 的 SG 值相等的连边方案数。

转移时我们枚举 $T$ 为 $S$ 的一个子集，表示 $S \setminus T$ 为 SG 值全 $0$ 的子集，然后从 $\mathrm{f}[T]$ 转移。

当然，上面仅是 $1, 2 \in T$ 的情况，对于 $1, 2 \in S \setminus T$ 的情况，也就是 $1, 2$ 的 SG 值均为 $0$，则 $T$ 中的连边就不重要了，随便连。

适当地预处理一些辅助数组，可以得到 $\mathcal O (3^N N)$ 的时间复杂度。

```cpp
#include <cstdio>

typedef long long LL;
const int Mod = 1000000007;
const int MN = 15;

int N, M, A[MN][MN];
int w[MN * MN];
int c[1 << MN][MN], f[1 << MN];

int main() {
	scanf("%d%d", &N, &M), w[0] = 1;
	for (int i = 1; i <= M; ++i) w[i] = 2 * w[i - 1] % Mod;
	for (int i = 1, x, y; i <= M; ++i) scanf("%d%d", &x, &y), A[--x][--y] = 1;
	for (int S = 1; S < 1 << N; ++S) {
		int j = 0;
		while (~S >> j & 1) ++j;
		for (int u = 0; u < N; ++u)
			c[S][u] = c[S ^ 1 << j][u] + A[u][j];
	}
	for (int S = 0; S < 1 << N; ++S) if ((S & 3) == 3) {
		f[S] = 1;
		for (int T = S & (S - 1); T; --T &= S) if ((T & 1) == (T >> 1 & 1)) {
			if (T & 1) {
				int Coef = 1;
				for (int i = 0; i < N; ++i) if (S >> i & 1) {
					if (T >> i & 1) Coef = (LL)Coef * (w[c[S ^ T][i]] - 1) % Mod;
					else Coef = (LL)Coef * w[c[T][i]] % Mod;
				}
				f[S] = (f[S] + (LL)Coef * f[T]) % Mod;
			} else {
				int Coef = 1;
				for (int i = 0; i < N; ++i) if (S >> i & 1) {
					if (T >> i & 1) Coef = (LL)Coef * (w[c[S ^ T][i]] - 1) % Mod * w[c[T][i]] % Mod;
					else Coef = (LL)Coef * w[c[T][i]] % Mod;
				}
				f[S] = (f[S] + Coef) % Mod;
			}
		}
	}
	printf("%d\n", (w[M] - f[(1 << N) - 1] + Mod) % Mod);
	return 0;
}
```