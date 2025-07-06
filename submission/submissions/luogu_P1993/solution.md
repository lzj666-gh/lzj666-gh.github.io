# P1993 题解

[${\color{Orange}My}$ ${\color{Yellow}Blog}$](https://www.luogu.com.cn/blog/Sham-Devour/)

[P1993](https://www.luogu.com.cn/problem/P1993)

[前置知识：差分约束](https://www.luogu.com.cn/blog/Sham-Devour/ci-fen-yue-shu)

题意：给出 $n$ 个数 $a_{i}$ 和 $m$ 条关于 $a_{i}$ 的信息，问有没有一组 $a_{i}$ 满足所有信息，如果有输出 `Yes`，否则输出 `No`。

其中 $m$ 条信息有如下三种形式：

- $a_{i}-a_{j}\ge c$

- $a_{i}-a_{j}\le c$

- $a_{i}=a_{j}$

我们将式子转化为下面的形式：

- $a_{j}\le a_{i}-c$

- $a_{i}\le a_{j}+c$

- $a_{i}\le a_{j}+0$ 和 $a_{j}\le a_{i}+0$

那么我们再来看一下 SPFA 是怎么更新 $dis$ 数组是怎么更新的。

```cpp
for (int i = elast[u]; i != 0; i = e[i].next)
	if (dis[e[i].to] > dis[u] + e[i].len) {
		dis[e[i].to] = dis[u] + e[i].len;
		if (!vis[e[i].to]) {
			q.push(e[i].to);
			vis[e[i].to] = true;
		}
	}
```

也就是 $dis_{i}=\min\left\{dis_{j}+<j,i>\right\}$。

于是在遇到 $a_{i}\le a_{j}+c$ 这样的不等式时，我们可以从 $j$ 到 $i$ 建一条边权为 $b$ 的 **有向边**。

为了避免图不连通的情况，我们需要一个超级源点 $n+1$ ，与点 $i$ 之间连一条边权为 $0$ 的边。

那么怎么判断有没有解呢？

那就是判断 **负环**。

那么又怎么判断负环呢？

只要用一个数组来统计每个点的入队次数，如果某个点的入队次数 $\ge n+1$ 则说明无解，输出 `No`，否则输出 `Yes`。

### Problem Solving！

```cpp
#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

int n, m, cnt, elast[5005], dis[5005], num[5005];
bool vis[5005];

struct edge {
	int to, len, next;
} e[15005];

queue<int> q;

void add (int u, int v, int w) {
	e[++cnt].to = v;
	e[cnt].len = w;
	e[cnt].next = elast[u];
	elast[u] = cnt;
}

bool spfa (int x) {
	dis[x] = 0;
	q.push(x);
	vis[x] = true;
	num[x]++;
	while (!q.empty()) {
		int u = q.front();
		q.pop();
		vis[u] = false;
		for (int i = elast[u]; i != 0; i = e[i].next)
			if (dis[e[i].to] > dis[u] + e[i].len) {
				dis[e[i].to] = dis[u] + e[i].len;
				if (!vis[e[i].to]) {
					q.push(e[i].to);
					vis[e[i].to] = true;
					num[e[i].to]++;
					if (num[e[i].to] == n + 1)
						return false;
				}
			}
	}
	return true;
}

int main () {
	scanf("%d %d", &n, &m);
	memset(dis, 0x3f3f3f3f, sizeof(dis));
	for (int i = 1; i <= m; i++) {
		int opt;
		scanf("%d", &opt);
		switch (opt) {
			case 1: {
				int a, b, c;
				scanf("%d %d %d", &a, &b, &c);
				add(a, b, -c);
				break;
			}
			case 2: {
				int a, b, c;
				scanf("%d %d %d", &a, &b, &c);
				add(b, a, c);
				break;
			}
			case 3: {
				int a, b;
				scanf("%d %d", &a, &b);
				add(a, b, 0);
				add(b, a, 0);
				break;
			}
		}
	}
	for (int i = 1; i <= n; i++)
		add(n + 1, i, 0);
	bool flag = spfa(n + 1);
	if (!flag) {
		printf("No");
		return 0;
	}
	printf("Yes");
	return 0;
}
```