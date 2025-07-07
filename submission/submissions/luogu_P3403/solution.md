# P3403 题解

## 基本思想

通过同余构造某些状态，状态之间的关系类似于两点之间的带权有向边。

那么可以以此建图，将某些问题转化为最短路问题，再使用具有优秀时间复杂度的算法求解。

#### 【例题】[P3403 跳楼机](https://www.luogu.com.cn/problem/P3403)

首先可以将 $h$ 减去 $1$，同时起始楼层设为 $0$。

设 $d_i$ 为能够到达的最低的 $\bmod x = i$ 的楼层。

则有 $i \stackrel{y}{\longrightarrow} (i+y)\bmod x$ 和 $i \stackrel{z}{\longrightarrow} (i+z)\bmod x$。

像这样建图后，$d_i$ 就相当于 $0 \to i$ 的最短路，Dijkstra 即可。

最后统计时，对于 $d_i \le h$，有贡献 $\lfloor\frac{h-d_i}x\rfloor + 1$。

总时间复杂度 $\mathcal O(n \log n)$。

```cpp
const int N = 1e5 + 7;
const ll inf = (1ull << 63) - 1;
ll h, d[N], ans;
int x, y, z, v[N];
vector< pi > e[N];
pq< pair< ll, int > > q; 

int main() {
	rd(h), --h, rd(x), rd(y), rd(z);
	for (int i = 0; i < x; i++) e[i].pb(mp((i + y) % x, y)), e[i].pb(mp((i + z) % x, z)), d[i] = inf;
	d[0] = 0, q.push(mp(0, 0));
	while (q.size()) {
		int x = q.top().se;
		q.pop();
		if (v[x]) continue;
		v[x] = 1;
		for (ui i = 0; i < e[x].size(); i++) {
			int y = e[x][i].fi, z = e[x][i].se;
			if (d[y] > d[x] + z) d[y] = d[x] + z, q.push(mp(-d[y], y));
		}
	}
	for (int i = 0; i < x; i++)
		if (h >= d[i]) ans += (h - d[i]) / x + 1;
	print(ans);
	return 0;
}
```

#### 【例题】[P2371 [国家集训队]墨墨的等式](https://www.luogu.com.cn/problem/P2371)

上一题的扩展。

```cpp
const int N = 5e5 + 7;
const ll inf = 1e18;
ll l, r, d[N], ans;
int n, x, v[N];
vector< pi > e[N];
pq< pair< ll, int > > q; 

int main() {
	rd(n), rd(l), --l, rd(r), rd(x);
	for (int i = 1; i < x; i++) d[i] = inf;
	for (int i = 1, y; i < n; i++) {
		rd(y);
		for (int i = 0; i < x; i++)
			e[i].pb(mp((i + y) % x, y));
	}
	q.push(mp(0, 0));
	while (q.size()) {
		int x = q.top().se;
		q.pop();
		if (v[x]) continue;
		v[x] = 1;
		for (ui i = 0; i < e[x].size(); i++) {
			int y = e[x][i].fi, z = e[x][i].se;
			if (d[y] > d[x] + z) d[y] = d[x] + z, q.push(mp(-d[y], y));
		}
	}
	for (int i = 0; i < x; i++) {
		if (r >= d[i]) ans += (r - d[i]) / x + 1;
		if (l >= d[i]) ans -= (l - d[i]) / x + 1;
	}
	print(ans);
	return 0;
}
```