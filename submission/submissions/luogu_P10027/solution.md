# P10027 题解

# 题意

求二元组序列 $A_s$ 的数量，满足：

1. $A_1 = (1, 1), A_s = (n, m), \forall A_i = (x, y), 1 \leq x \leq n \land 1 \leq y \leq m \land (x, y) \notin F$；
2. 对于 $A$ 的每相邻两个元素 $A_i(x_0, y_0), A_{i+1}(x_1, y_1)$，要么：
+ $x_0 = x_1, y_0 = y_{1 + 1}$；
+ $y_0 = y_1, x_0 = x_{1 + 1}$；
+ $\exist k, s.t. A_{i+1} = A_{(i+1)-2k}, A_{i} = A_{i-2(k-1)}$（撤销操作，很抽象而且可能有问题，所以需要参考原题面理解）。

并且：所有满足第三步的 $i, i+1$ 对数 $\leq k$。

求合法 $A$ 数量 $\bmod\ p$。

$1 \leq n, m, k \leq 100, 2\leq p \leq 10^9 + 9, 0 \leq \lvert F \rvert \leq n\times m$。

# 思路

一看就是一个类 dp 状物。

dp 从 $(1, 1)$ 走到某个特定的格子感觉很难做，因为后面有很多我们暂时还没有 dp 到的东西！（显然我们需要把撤销操作写进状态。）

于是考虑倒着 dp，令 $f_{i,j,k}$ 表示从 $(i, j)$ 出发使用 $k$ 次撤销操作走到 $(n, m)$ 的方案数，$g_{i,j,k}$ 表示从 $(i, j)$ 出发使用 $k$ 次前进和撤销操作后**恰好回到** $(i, j)$ 的方案数，$h_{i, j, k}$ 表示从 $(i, j)$ 出发使用 $k$ 次前进和撤销操作后**回到** $(i, j)$ 的方案数。计数时调用方式 $f \gets h \gets g$，初始状态 $f_{n,m,0} = g_{n,m,0} = h_{n,m,0} = 1$，特判 $(n, m)$ 有障碍特殊情况。

+ Step 1：计算 $g$

显然根据方格取数的方法，$g_{i,j,k} = h_{i,j+1,k-1}+h_{i+1,j,k-1}$（这里右边不是 $g$！否则你可能只有 $20$ 分）。

+ Step 2：计算 $h$

枚举上一个在这个点出去的 $g$ 是多少，则 $h_{i,j,0} = 1, h_{i,j,k} = \sum\limits_{l=1}^k g_{i,j,l}\times h_{i,j,k-l}$。

+ Step 3：计算 $f$

枚举在这个点往外撤销了多少步，则 $f_{i,j,k} = \sum\limits_{l=0}^k h_{i,j,l} \times (f_{i+1,j,k-l} + f_{i,j+1,k-l})$。

所有不合法状态：$i \gt n, j \gt m, (i, j)$ 处有障碍，这时应将 $f,h,g$ 视为 $0$。

然后求个和就结束了。空间复杂度 $\mathcal O(nmk)$，时间复杂度 $\mathcal O(nmk^2)$。

# 代码

```cpp
#include <bits/stdc++.h>

#define MAXN 105
bool var[MAXN][MAXN];

#define MAXK 101
int f[MAXN][MAXN][MAXK], g[MAXN][MAXN][MAXK], h[MAXN][MAXN][MAXK];

int N, M, K, P, S;
inline void add(int& a, int b) { (a += b) >= P && (a -= P); }
inline int sum(int a, int b) { return (a += b) < P ? a : a - P; }
int main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr), std::cout.tie(nullptr);
	std::cin >> N >> M >> K >> P >> S;
	for (int i = 1, x, y; i <= S; ++i) 
		std::cin >> x >> y, var[x][y] = true;
	for (int i = N; i; --i) for (int j = M; j; --j) {
		if (i == N && j == M) {
			if (var[i][j]) return std::cout << 0, 0;
			f[i][j][0] = g[i][j][0] = h[i][j][0] = 1;
			continue;
		}
		if (var[i][j]) continue;
		h[i][j][0] = g[i][j][0] = 1;
		f[i][j][0] = sum(f[i + 1][j][0], f[i][j + 1][0]);
		for (int k = 1; k <= K; ++k) {
			g[i][j][k] = sum(h[i + 1][j][k - 1], h[i][j + 1][k - 1]);
			for (int l = 1; l <= k; ++l) 
				add(h[i][j][k], 1ll * h[i][j][k - l] * g[i][j][l] % P);
			for (int l = 0; l <= k; ++l) 
				add(f[i][j][k], 1ll * h[i][j][l] * (f[i + 1][j][k - l] + f[i][j + 1][k - l]) % P);
		}
	}
	int ans = 0;
	for (int k = 0; k <= K; ++k) add(ans, f[1][1][k]);
	return std::cout << ans, 0;
}
```