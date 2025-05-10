#include<bits/stdc++.h>
using namespace std;
struct Edge {
	int u, v, nxt;
}edge[40000000 + 10];
int head[20000000 + 10], idx;
void add(int u, int v) {
	edge[++idx] = { u,v,head[u] };
	head[u] = idx;
}
int n, m, scc[20000000 + 10], dfn[20000000 + 10], low[20000000 + 10], cnt, idk;
stack<int>stk;
void tarjan(int x) {
	dfn[x] = low[x] = ++idk;
	stk.push(x);
	for (int i = head[x]; i; i = edge[i].nxt) {
		if (!dfn[edge[i].v])
			tarjan(edge[i].v),
			low[x] = min(low[x], low[edge[i].v]);
		else if (!scc[edge[i].v])
			low[x] = min(low[x], dfn[edge[i].v]);
	}
	if (low[x] == dfn[x]) {
		cnt++;
		while (stk.size()) {
			int now = stk.top(); stk.pop();
			scc[now] = cnt;
			if (now == x) break;
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin >> n >> m;
	for (int i = 1, a, b, c, d; i <= m; ++i) {
		cin >> a >> b >> c >> d;
		add(a + b * n, c + (d ^ 1) * n);
		add(c + d * n, a + (b ^ 1) * n);
	}
	for (int i = 1; i <= n + n; ++i) if (!dfn[i]) tarjan(i);
	for (int i = 1; i <= n; ++i) if (scc[i] == scc[i + n]) { cout << "IMPOSSIBLE" << endl; return 0; }
	cout << "POSSIBLE" << endl;
	for (int i = 1; i <= n; ++i)
		cout << (scc[i] < scc[i + n]) << ' ';
	cout << endl;
	return 0;
}
