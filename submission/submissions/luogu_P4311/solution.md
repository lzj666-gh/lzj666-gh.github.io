# P4311 题解

这道题用上下界网络流可能有点大材小用了，其实一个普通的网络流就能解决问题。首先考虑逆向思维，求最少要使用的士兵个数，转化为，初始的时候所有能放士兵的地方都放了士兵的情况下，最多能删掉多少个士兵。

给每一行每一列分别建一个点，对于所有非障碍坐标(x,y)，从x行对应的点 向 y列对应的点连一条容量为1的边，表示这个位置的士兵最多可以删除一次。

源点向每一行对应的点连边，容量为这一行能删除的士兵个数的最大值（即 列数m - 这一行的障碍数 - 这一行需要的士兵数L\[i\]）。

每一列对应的点向汇点连边，容量为这一列能删除的士兵个数的最大值（即 行数n - 这一列的障碍数 - 这一列需要的士兵数C\[i\]）。

这样跑一个最大流，每一个单位的流量表示删除一个士兵，不难证明 任意一种流量状态都与一种合法的士兵删除方案相对应。

特判无解的情况，如果所有能放士兵的地方都放上了士兵，仍然存在行或列不满足限制条件，输出无解即可。

代码如下：

```cpp
#include <queue>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 2*100 + 7, inf = 0x7f7f7f7f;

namespace dinic {
	struct Edge {
		int to, res;
	};
	vector<int> G[maxn];
	vector<Edge> edges;
	inline void addedge(int f, int t, int c) {
		edges.push_back((Edge){t, c});
		edges.push_back((Edge){f, 0});
		int m = edges.size();
		G[f].push_back(m - 2);
		G[t].push_back(m - 1);
	}
	int vis[maxn], d[maxn], cur[maxn], s, t;
	bool bfs() {
		memset(vis, 0x00, sizeof(vis));
		queue<int> q; q.push(s); vis[s] = 1; d[s] = 0;
		while(!q.empty()) {
			int x = q.front(); q.pop();
			for(int i = 0; i < G[x].size(); i ++) {
				Edge& e = edges[G[x][i]];
				if(e.res>0 && !vis[e.to]) {
					vis[e.to] = 1;
					d[e.to] = d[x] + 1;
					q.push(e.to);
				}
			}
		}
		return vis[t];
	}
	int dfs(int x, int a) {
		if(x==t || a==0) return a;
		int flow = 0, f;
		for(int& i = cur[x]; i < G[x].size(); i ++) {
			Edge& e = edges[G[x][i]];
			if(e.res>0 && d[e.to]==d[x]+1 && (f=dfs(e.to,min(a,e.res)))>0) {
				flow += f;
				a -= f;
				edges[G[x][i]^1].res += f;
				e.res -= f;
				if(a == 0) break;
			}
		}
		return flow;
	}
	int maxflow(int S, int T) {
		s=S;t=T; int flow = 0;
		while(bfs()) {
			memset(cur, 0x00, sizeof(cur));
			flow += dfs(s, inf);
		}
		return flow;
	}
}
using dinic::addedge;
using dinic::maxflow;

int m, n, k, L[maxn], C[maxn];
#define LX(x) (x)
#define LY(y) (m+(y))
#define ST    (n+m+1)
#define ED    (n+m+2)

int sol[maxn][maxn], iL[maxn], iC[maxn], acnt;

int main() {
	scanf("%d%d%d", &m, &n, &k); acnt = n*m;
	for(int i = 1; i <= m; i ++) scanf("%d", &L[i]);
	for(int i = 1; i <= n; i ++) scanf("%d", &C[i]);
	for(int i = 1; i <= k; i ++) {
		int x, y; scanf("%d%d", &x, &y);
		sol[x][y] = 1; iL[x] ++; iC[y] ++;
		acnt --;
	}
	for(int i = 1; i <= m; i ++) {
		for(int j = 1; j <= n; j ++)
			if(!sol[i][j]) addedge(LX(i), LY(j), 1);
	}
	for(int i = 1; i <= m; i ++) {
		int c = (n - iL[i]) - L[i];
		if(c < 0) {puts("JIONG!"); return 0;}
		addedge(ST, LX(i), c);
		//printf("[%3d] c = %3d iL = %3d L = %3d\n", i, c, iL[i], L[i]);
	}
	for(int i = 1; i <= n; i ++) {
		int c = (m - iC[i]) - C[i];
		if(c < 0) {puts("JIONG!"); return 0;}
		addedge(LY(i), ED, c);
		//printf("[%3d] c = %3d iC = %3d C = %3d\n", i, c, iC[i], C[i]);
	}
	int ans = acnt - maxflow(ST, ED);
	printf("%d\n", ans);
	return 0;
}
```
