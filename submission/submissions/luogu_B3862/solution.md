# B3862 题解

~~蒟蒻第一次发题解，望审核通过~~

## [题目](https://www.luogu.com.cn/problem/B3862)

给出 $N$ 个点，$M$ 条边的有向图，对于每个点 $v$，求从点 $v$ 出发，能到达的编号最大的点。


这是一道图的遍历考察的是如何使用 DFS 遍历图（~~废话~~）。

## 思路

我们可以来这样思考，我们按节点编号大小从大到小依此遍历每一个数所能到达的节点，这一个操作可以用 DFS。

再来详细的说如何 DFS。

我们可以**反向建边**，这样如果一个点 $x$ 能被另一个点 $y$ 访问到，那么 $x$ 也一定能访问 $y$。

DFS 的过程就是：如果我遍历到一个点 $x$ 就来看这个点是否被比我编号更大的点访问过。

简单点说就是看 $x$ 是否被标记过。我们是按节点编号大小从大到小依此遍历，如果 $x$ 被标记过就是说明 $x$ 被比我编号更大的点访问过。

如果没有那么就表明我是 $x$ 可以访问到的编号最大的点（这样就可以知道 $x$ 多能到达最大的节点的编号了）。

然后再依次 DFS 自己的子节点就好惹！

# 代码！
~~注释较少，别打我...~~
```cpp
#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

#define TRACE 1
#define tcout TRACE && cout

#define fst ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

#define int long long

#ifdef int
const int INF = 0x3f3f3f3f3f3f3f3f; 
#else
const int INF = 0x3f3f3f3f;
#endif

const int P = 998244353; 
const int N = 1e5 + 10, M = 1e5 + 10; 

int n, m;
vector<int> g[N];

bool vis[N];

int a[N];

void dfs(int u, int i)
{
	if(vis[u])
	{
		//如果这个点被别的点到达过, 则不能再走了
		return;
	}
	vis[u] = 1;
	a[u] = i;
	for(auto v: g[u])
	{
		if(vis[v] == 0)
		{
			dfs(v, i);
		}
	}
}

signed main()
{
	cin >> n >> m;
	for(int i=1; i<=m; i++)
	{
		int u, v;
		cin >> u >> v;
		g[v].push_back(u);
	}
	for(int i=n; i>=1; i--)
	{
		dfs(i, i);	//从i点出发, 能到哪个点, 就表示哪个点能到i
	}
	for(int i=1; i<=n; i++)
	{
		cout << a[i] << " ";
	}
	return 0;
}
```