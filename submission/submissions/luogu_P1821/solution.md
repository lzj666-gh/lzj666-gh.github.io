# P1821 题解

# 一个巧妙的最短路：


------------

### 题目概括：
求 一个单源最短路 + 一个单终点最短路 的最大值。
### 思路：
- 我们首先想到的是从每个点都求一遍到终点的最短路，这样会加大时间复杂度。
- 所以，我们可以反向建图，直接把单终点最短路转为单源最短路，只需要跑两次最短路算法，显然是稳过的。（可以自己画画图，感受一下）

PS：这里推荐dijkstra算法，不推荐spfa，显然我们可以轻松卡掉spfa，平时练习要养成好的习惯，避免考试时酿成不必要的惨剧。
### 代码如下：
```cpp
#include <bits/stdc++.h>

using namespace std;

typedef long long ll; // 做题的好习惯 

const int maxn = 1005; //点数 
const int maxm = 100005; //边数 

int n, m, s, ans[maxn], sum;

struct Edge{
	int nxt, to, w;
}e[maxm];

int head[maxn], cnt;

void addEdge(int u, int v, int w) {
	e[++cnt].nxt = head[u];
	e[cnt].w = w;
	e[cnt].to = v;
	head[u] = cnt; 
}

int dis[maxn], vis[maxn];

void dijkstra(int s) {
	for (int i = 1; i <= n; i++) dis[i] = 0x3f3f3f3f;  
	priority_queue< pair<int, int> > q;
	q.push(make_pair(0, s));
	dis[s] = 0;
	while (q.size()) {
		int u = q.top().second;
		q.pop();
		if (vis[u]) continue;
		vis[u] = 1;
		for (int i = head[u]; i; i = e[i].nxt) {
			int v = e[i].to;
			if (dis[v] > dis[u] + e[i].w) {
				dis[v] = dis[u] + e[i].w;
				q.push(make_pair(-dis[v], v));
			}
		}
	}
}

int main() {
	int u[maxm], v[maxm], w[maxm];
	cin >> n >> m >> s;
	for (int i = 1; i <= m; i++) {
		cin >> u[i] >> v[i] >> w[i]; //先存下数据，便于以后反向建边 
		addEdge(u[i], v[i], w[i]); //正向建边 
	}
	dijkstra(s);
	for (int i = 1; i <= n; i++) ans[i] = dis[i]; //回家的最短路径  
	cnt = 0;
	memset(dis, 0, sizeof(dis));
	memset(head, 0, sizeof(head));
	memset(vis, 0, sizeof(vis));
	for (int i = 1; i <= m; i++) addEdge(v[i], u[i], w[i]); //反向建边
	dijkstra(s);
	for (int i = 1; i <= n; i++) {
		ans[i] += dis[i]; //回家的最短路+去派对的最短路=全程的最短路 
		sum = max(sum, ans[i]); //求最大值 
	}
	cout << sum;//输出 
	return 0;
}
```


------------
# 感谢！