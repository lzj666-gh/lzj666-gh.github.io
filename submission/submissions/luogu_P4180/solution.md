# P4180 题解

这道题目 是$kruskal$和$LCA$ 算法的合集 题目 不难

但是重在细节

首先 如果是次小生成树 有个性质就是他与最小生成树只有一条边不同 那么就枚举加入哪条边 然后 删去原路径上的一条边 然后删去权值最大（实际上应该是最大的次大的）

一开始 看到这道题 感觉和货车运输比较类似 然后就开始做 每次倍增维护路径上最大值 但是发现样例过不了 交上去有$60pts$

然后开始手搞样例 发现样例他删去的边是路径上的次大边 因为假设加上这条最大边 最小生成树权值和还是原来的和 那么我们考虑维护树上次大和最大值

讲一下维护次大值的思路 就是$max (min(g[u][i - 1], g[f[u][i - 1]][i - 1]), h[u][i - 1], h[f[u][i - 1]][i - 1]))$

然后就是模板了 不过这个模板并没有什么用

```cpp
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;

const ll INF = (1ll << 62);

#define DEBUG(x) std::cerr << #x << " = " << x << std::endl

#define int ll

inline ll read() {
    ll f = 1, x = 0;char ch;
    do {ch = getchar();if (ch == '-')f = -1;} while (ch > '9' || ch < '0');
    do {x = x * 10 + ch - '0';ch = getchar();} while (ch >= '0' && ch <= '9');
    return f * x;
}

const int MAX_N = 100000 + 50;
const int MAX_M = 300000 + 50;
const int MAX_F = 30 + 5;

struct EDGE {
	int to, next, w;
} edge[MAX_M << 1];

int head[MAX_N], cnt;

void addedge (int u, int v, int w) {
	edge[++cnt].to = v;
	edge[cnt].w = w;
	edge[cnt].next = head[u];
	head[u] = cnt;
}

int f[MAX_N][MAX_F], g[MAX_N][MAX_F], h[MAX_N][MAX_F], dep[MAX_N];

inline void ckmax (int &x, int y) {
	x = (x > y ? x : y);
}

inline void dfs (int u, int fa, int w) {
	dep[u] = dep[fa] + 1;
	f[u][0] = fa;
	g[u][0] = w;
	h[u][0] = -INF;
	for (int i = 1; i <= 20; i ++ ) {
		f[u][i] = f[f[u][i - 1]][i - 1];
		g[u][i] = max (g[u][i - 1], g[f[u][i - 1]][i - 1]);
		h[u][i] = max (h[u][i - 1], h[f[u][i - 1]][i - 1]);
		if (g[u][i - 1] > g[f[u][i - 1]][i - 1]) h[u][i] = max (h[u][i], g[f[u][i - 1]][i - 1]);
		else if (g[u][i - 1] < g[f[u][i - 1]][i - 1]) h[u][i] = max (h[u][i], g[u][i - 1]);
	}
	for (int i = head[u]; i; i = edge[i].next ) {
		int v = edge[i].to, w = edge[i].w;
		if (v == fa) continue;
		dfs (v, u, w);
	}
}

inline int LCA (int x, int y) {
	if (dep[x] < dep[y]) swap (x, y);
	for (int i = 20; i >= 0; i -- ) {
		if (dep[f[x][i]] >= dep[y]) x = f[x][i];
	}
	if (x == y) return x;
	for (int i = 20; i >= 0; i -- ) {
		if (f[x][i] != f[y][i]) {
			x = f[x][i];
			y = f[y][i];
		}
	}
	return f[x][0];
}

int n, m, fa[MAX_N], res, sum;

struct Node {
	int u, v, w;
	bool operator < (const Node & rhs ) const  {
		return w < rhs.w;
	}
} a[MAX_M << 1];

inline int find (int x) {
	return x == fa[x] ? x : fa[x] = find (fa[x]);
}

inline void merge (int x, int y) {
	x = find (x); y = find (y);
	if (x == y) return;
	fa[x] = y;
}

bool vis[MAX_M];

inline void kruskal () {
	n = read (); m = read ();
	for (int i = 1; i <= m; i ++ ) {
		a[i].u = read (); a[i].v = read (); a[i].w = read ();
	}
	sort (a + 1, a + m + 1);
	for (int i = 1; i <= n; i ++ ) fa[i] = i;
	res = 0;
	for (int i = 1; i <= m; i ++ ) {
		if (find (a[i].u) != find (a[i].v)) {
			vis[i] = 1;
			res ++ ;
			merge (a[i].u, a[i].v);
			sum += a[i].w;
			addedge (a[i].u, a[i].v, a[i].w);
			addedge (a[i].v, a[i].u, a[i].w);
		}
		if (res == n - 1) break;
	}
	res = 0;
	dfs (1, 0, 0);
}

inline int qmax (int u, int v, int maxx) {
	int ans = -INF;
	for (int i = 18; i >= 0; i -- ) {
		if (dep[f[u][i]] >= dep[v]) {
			if (maxx != g[u][i]) ans = max (ans, g[u][i]);
			else ans = max (ans, h[u][i]);
			u = f[u][i];
		}
	}
	return ans;
}

inline void ckmin (int &x, int y) {
	x = (x < y ? x : y);
}

inline void calc () {
	int ans = INF;
	for (int i = 1; i <= m; i ++ ) {
		if (vis[i]) continue;
		int lca = LCA (a[i].u, a[i].v);
		int max_u = qmax (a[i].u, lca, a[i].w);
		int max_v = qmax (a[i].v, lca, a[i].w);
		ckmin (ans, sum - max (max_u, max_v) + a[i].w);
	}
	printf ("%lld\n", ans);
}

signed main() {
	kruskal ();
	calc ();
	return 0;
}
```