# P6833 题解

# P6833 题解
## 题意
求从 $(1,a)$ 开始分别到达 $(n,b)$ 和 $(n,c)$ 的路径之和减去其共有路径。（题目中的坐标被作者转化过了）
## 建模
从 $(1,a)$ 到达 $(n,b),(n,c)$ 。这个描述一看就知道是路径问题，于是我们可以想到 $dfs$ ，分别求出 $(1,a) \rightarrow (n,b)$ 和 $(1,a) \rightarrow (n,c)$ 的路径然后减去其共有路径即可。

但是这样做有一个问题：共有路径并不确定。我们在 $dfs$ 的过程中，只保存了最小值，并没有保存路径信息，因此理论上无法快速求出共有路径。所以我们需要把这个问题给规避掉。

我们发现， $(1,a) \rightarrow (n,b),(n,c)$ 的路径中一定有一个转折点 $(i,j)$ ，从 $(1,a)$ 到转折点 $(i,j)$ 后开始分叉分别到达 $(n,b),(n,c)$ 。

但如果我们无脑的从 $(1,a)\ dfs$ 到 $(n,b),(n,c)$ ，就无法确定这个 $(i,j)$ 。那么我们现在就有了一个明确的思路：枚举这个 $(i,j)$ 。

于是路径就被拆成了 $3$ 段：
1. $(1,a) \rightarrow (i,j)$
2. $(i,j) \rightarrow (n,b)$
3. $(i,j) \rightarrow (n,c)$

这三种情况分别求出最短路然后求和即是**转折点为 $(i,j)$ 时的路径** 。  
然后我们每次枚举 $(i,j)$ 的时候分别进行 $dfs$ 即可。复杂度 $\Theta(nmR),R=dfs$ 的复杂度。

## Code
$dfs$ 代码：
```cpp
void dfs(ll x, ll y, ll len) {
	if (len >= min_d[x][y]) return;
	min_d[x][y] = len;
	if (x == tx && y == ty) return;
	for (ll k = 0; k < 4; k ++){
		ll nx = x + dx[k], ny = y + dy[k];
		if (nx >= 1 && nx <= n && ny >= 1 && ny <= m)
			dfs(nx, ny, len + R[nx][ny]);
	}
}
```

## 优化
然而 $dfs$ 并不行，因为单次 $dfs$ 的复杂度过高（~~然而是我写的不好~~）而导致 $\colorbox{#052242}{\color{white}{TLE}}$ 。

于是我们可以把 $dfs$ 改为 $bfs$ 提高算法效率。并通过一开始直接的三次 $bfs$ 统计完所有的路径。

## Code
```cpp
void bfs(ll t, ll tx, ll ty) {
	memset(v, 0, sizeof v);
	priority_queue<node> que;
	que.push((node){tx, ty, min_d[t][tx][ty]});
	while (!que.empty()) {
		node now = que.top(); que.pop();
		if (v[now.x][now.y]) continue;
		v[now.x][now.y] = 1;
		for (int i = 0; i < 4; i ++) {
			ll nx = now.x + dx[i], ny = now.y + dy[i];
			if (nx < 1 || nx > n || ny < 1 || ny > m || v[nx][ny]) continue;
			min_d[t][nx][ny] = min(min_d[t][nx][ny], min_d[t][now.x][now.y] + r[nx][ny]);
			que.push((node){nx, ny, min_d[t][nx][ny]});
		}
	}
}
```
## 后记
算是搜索的半模板题，只要转个弯就能够想到正解。  
~~既然如此你为什么考场上想不到。~~  
最后祝洛谷月赛
### 越办越好
完结撒花，顺便求赞![](https://cdn.jsdelivr.net/gh/xaoxuu/volantis@1.0/img/qq/%E5%8F%AF%E6%80%9C.gif)