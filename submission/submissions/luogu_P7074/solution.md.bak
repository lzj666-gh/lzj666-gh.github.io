# P7074 题解

upd 2022.08.08：修正方向，感谢@[Zlc晨鑫](https://www.luogu.com.cn/user/297555)、@[wzkdh](https://www.luogu.com.cn/user/235121)、@[hyt666](https://www.luogu.com.cn/user/280999) 三位同学的贡献。

## Description
给定一个 $n\cdot m$ 矩阵，找一条从 $(1,1)$ 到 $(n,m)$ 权值和最大的路径，每次只准向上、下、右三个方向走。

## $\text{Solution\ 1}$：暴力$\text{dfs}$
概述：这种算法比较简单，不需要动头脑，直接三方向深搜即可。

时间复杂度：$\mathcal{O}(3^{nm})$

期望得分：$20$ 分

## $\text{Solution\ 2}$：最优性剪枝
概述：考场上我只想到了这种方法（~~太菜了~~。我们设 $F_{i,j,0}$ 表示从一个格子上方走到该格子的路径最大和，$F_{i,j,1}$ 表示从一个格子右方走到该格子的路径最大和，$F_{i,j,2}$ 表示从一个格子下方走到该格子的路径最大和。如果搜到相同的状态则判断是否比原 $F$ 值更大，如果更优则更新答案，否则退出该状态。

时间复杂度：视具体数据而定，当格子权值差值较大时能拿到较多分数。

期望得分：$40$ 分

### 考场 $\text{code}$
```cpp
#include <stdio.h>
const int dx[] = {1, 0, -1}, dy[] = {0, 1, 0};
typedef long long LL;
int n, m; bool vis[1005][1005];
LL w[1005][1005], f[1005][1005][3], ans = -20000000000;
inline LL mx(LL p, LL q) {return p > q ? p : q;}
inline void dfs(int x, int y, int from, LL now) {
	if (x == n && y == m) {
		ans = mx(now, ans);
		return;
	}
	if (f[x][y][from] > now) return;
	else f[x][y][from] = now;
	for (int i = 0, xx, yy; i < 3; ++i) {
		xx = x + dx[i]; yy = y + dy[i];
		if (xx >= 1 && xx <= n && yy >= 1 && yy <= m && !vis[xx][yy]) {
			vis[xx][yy] = true;
			dfs(xx, yy, i, now + w[xx][yy]);
			vis[xx][yy] = false;
		}
	}
}
int main(void) {
//	freopen("number.in", "r", stdin); freopen("number.out", "w", stdout);
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) {
			scanf("%lld", &w[i][j]);
			f[i][j][0] = f[i][j][1] = f[i][j][2] = -20000000000;
		}
	vis[1][1] = true;
	dfs(1, 1, 0, w[1][1]);
	printf("%lld\n", ans);
	return 0;
}
```

## $\text{Solution\ 3}$：记忆化搜索
概述：这才是正解。我们设 $F_{i,j,0}$ 表示从一个格子**下方**走到该格子的路径最大和，$F_{i,j,1}$ 表示从一个格子**上方**走到该格子的路径最大和。如果搜到以前搜过的状态则直接返回搜过的最大和（也就是 $F$ 中的值），否则继续搜索到达该格时的最大和。

时间复杂度：$\mathcal{O}(nm)$

期望得分：$100$ 分

### $\text{ac\ code}$
```cpp
#include <stdio.h>
typedef long long LL;
const LL min_ll = -1e18;
int n, m; LL w[1005][1005], f[1005][1005][2];
inline LL mx(LL p, LL q, LL r) {return p > q ? (p > r ? p : r) : (q > r ? q : r);}
inline LL dfs(int x, int y, int from) {
    if (x < 1 || x > n || y < 1 || y > m) return min_ll;
    if (f[x][y][from] != min_ll) return f[x][y][from];
    if (from == 0) f[x][y][from] = mx(dfs(x + 1, y, 0), dfs(x, y - 1, 0), dfs(x, y - 1, 1)) + w[x][y];
    else f[x][y][from] = mx(dfs(x - 1, y, 1), dfs(x, y - 1, 0), dfs(x, y - 1, 1)) + w[x][y];
    return f[x][y][from];
}
int main(void) {
//	freopen("number.in", "r", stdin); freopen("number.out", "w", stdout);
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) {
			scanf("%lld", &w[i][j]);
			f[i][j][0] = f[i][j][1] = min_ll;
		}
    f[1][1][0] = f[1][1][1] = w[1][1];
	printf("%lld\n", dfs(n, m, 1));
	return 0;
}
```

## The end. Thanks.
记得点赞（qwq