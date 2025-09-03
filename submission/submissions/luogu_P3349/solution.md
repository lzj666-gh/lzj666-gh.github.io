# P3349 题解

将问题抽象化：

一个$n$个节点的树，和一个$n$个节点的图，要求给树上的每个节点编号，使得编号是一个$1$到$n$的排列，并且要满足树上任意一条边$(u,v)$，图中一定要有边$(x_u,x_v)$（$x_u$表示点$u$的编号），求方案数。

暴力的做法是定义状态$f[i][j][S]$表示节点$i$编号为$j$，$i$的子树内的编号集合为$S$的方案数。

但是这样的瓶颈在于枚举子集，复杂度是$O(n^3\times 3^n)$的，显然TLE。

Q：为什么要记录$S$这一维？

A：要求中有「编号是一个$1$到$n$的排列」。

尝试把「编号是一个$1$到$n$的排列」这一条件去掉，就不用记录$S$了。

这样只需要定义$f[i][j]$为在$i$的子树内，点$i$的编号为$j$的方案数。

而这时候会出现重复编号，怎么办呢？

容斥！

先$2^n$枚举$\{1,2,...,n\}$的一个子集$S$，强制规定树上每个点的编号必须是$S$的子集，然后每次$O(n^3)$一次DP，总方案数为：

$(|S|=n$的方案数$)-(|S|=n-1$的方案数$)+(|S|=n-2$的方案数$)-...$

复杂度降到$O(n^3\times 2^n)$，在UOJ上需要进行一定的常数优化。

代码：

```cpp
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
inline int read() {
	int res = 0; bool bo = 0; char c;
	while (((c = getchar()) < '0' || c > '9') && c != '-');
	if (c == '-') bo = 1; else res = c - 48;
	while ((c = getchar()) >= '0' && c <= '9')
		res = (res << 3) + (res << 1) + (c - 48);
	return bo ? ~res + 1 : res;
}
typedef long long ll;
const int N = 20, M = 40;
int n, m, ecnt, nxt[M], adj[N], go[M], tot, whi[N];
bool g[N][N], vis[N]; ll f[N][N], ans;
inline void add_edge(const int &u, const int &v) {
	nxt[++ecnt] = adj[u]; adj[u] = ecnt; go[ecnt] = v;
	nxt[++ecnt] = adj[v]; adj[v] = ecnt; go[ecnt] = u;
}
inline void dfs(const int &u, const int &fu) {
	int i, j; for (int e = adj[u], v; e; e = nxt[e]) {
		if ((v = go[e]) == fu) continue; dfs(v, u);
	}
	for (i = 1; i <= tot; i++) {
		int x = whi[i]; f[u][x] = 1;
		for (int e = adj[u], v; e; e = nxt[e]) {
			if ((v = go[e]) == fu) continue; ll sum = 0;
			for (j = 1; j <= tot; j++) {
				int y = whi[j]; if (!g[x][y]) continue; sum += f[v][y];
			}
			f[u][x] *= sum;
		}
	}
}
inline void solve() {
	int i; tot = 0; for (i = 1; i <= n; i++) if (vis[i]) whi[++tot] = i;
	dfs(1, 0); for (i = 1; i <= tot; i++)
		if (n - tot & 1) ans -= f[1][whi[i]]; else ans += f[1][whi[i]];
}
inline void Dfs(const int &dep) {
	if (dep == n + 1) return solve();
	vis[dep] = 0; Dfs(dep + 1);
	vis[dep] = 1; Dfs(dep + 1);
}
int main() {
	int i, x, y; n = read(); m = read();
	for (i = 1; i <= m; i++) x = read(), y = read(), g[x][y] = g[y][x] = 1;
	for (i = 1; i < n; i++) x = read(), y = read(), add_edge(x, y);
	Dfs(1); cout << ans << endl; return 0;
}
```