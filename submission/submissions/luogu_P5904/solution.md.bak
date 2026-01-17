# P5904 题解

# 请到博客中查看

先考虑简单版的 $n \le 5 \times 10^3$ 怎么做。

设 $f_{i,j}$ 为满足 $x$ 在 $i$ 的子树中且 $d(x, i) = j$ 的 $x$ 的个数，$g_{i,j}$ 为满足 $x,y$ 在 $i$ 的子树中且 $d(\operatorname{lca}(x, y), x) = d(\operatorname{lca}(x, y), y) = d(\operatorname{lca}(x, y), i) + j$ 的无序数对 $(x,y)$ 的个数。

有转移：

$$
ans \leftarrow g_{i, 0}
$$

$$
ans \leftarrow \sum_{x,y \in \operatorname{son}(i), x \ne y} f_{x,j-1} \times g_{y,j+1}
$$

$$
g_{i,j} \leftarrow \sum_{x,y \in \operatorname{son}(i), x \ne y} f_{x,j-1} \times f_{y,j-1}
$$

$$
g_{i,j} \leftarrow \sum_{x \in \operatorname{son}(i)} g_{x, j+1}
$$

$$
f_{i,j} \leftarrow \sum_{x \in \operatorname{son}(i)} f_{x, j-1}
$$

显然这可以利用前缀和，或者说是所有儿子「向 $i$ 合并」，做到 $\mathcal O(n)$ 转移，总时间复杂度 $\mathcal O(n^2)$。

注意到这里的信息都是以深度为下标的，那么可以利用长链剖分将复杂度降为均摊 $\mathcal O(1)$，总时间复杂度即可降为 $\mathcal O(n)$。

在「直接继承重儿子的信息」时，需要用指针维护，具体见代码。

```cpp
const int N = 1e5 + 7;
int n, d[N], dep[N], son[N];
vi e[N];
ll *f[N], *g[N], p[N<<2], *o = p, ans;

void dfs(int x, int fa) {
	d[x] = d[fa] + 1;
	for (auto y : e[x])
		if (y != fa) {
			dfs(y, x);
			if (dep[y] > dep[son[x]]) son[x] = y;
		}
	dep[x] = dep[son[x]] + 1;
}

void dp(int x, int fa) {
	if (son[x])
		f[son[x]] = f[x] + 1, g[son[x]] = g[x] - 1, dp(son[x], x);
	f[x][0] = 1, ans += g[x][0];
	for (auto y : e[x])
		if (y != fa && y != son[x]) {
			f[y] = o, o += dep[y] << 1, g[y] = o, o += dep[y] << 1;
			dp(y, x);
			for (int i = 0; i < dep[y]; i++) {
				if (i) ans += f[x][i-1] * g[y][i];
				ans += g[x][i+1] * f[y][i];
			}
			for (int i = 0; i < dep[y]; i++) {
				g[x][i+1] += f[x][i+1] * f[y][i];
				if (i) g[x][i-1] += g[y][i];
				f[x][i+1] += f[y][i];
			}
		}
}

int main() {
	rd(n);
	for (int i = 1, x, y; i < n; i++)
		rd(x), rd(y), e[x].pb(y), e[y].pb(x);
	dfs(1, 0), f[1] = o, o += dep[1] << 1, g[1] = o, o += dep[1] << 1;
	dp(1, 0), print(ans);
	return 0;
}
```